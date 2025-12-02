"""
    Python script with two modes of operation:
    - call /hello endpoint
"""

import socket
import os
import argparse
import requests
import paramiko


def get_host_ip():
    """
    Detect host IP from inside Docker (works on WSL2/Linux/Docker Desktop)
    """

    host_env = os.getenv("FASTAPI_HOST")
    if host_env:
        return host_env

    if os.getenv("HOST_DOCKER_INTERNAL") or os.name == "nt":
        return "host.docker.internal"

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # connect to a public IP (no packets sent), get container's outgoing interface
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

def fetch_hello(api_url: str, output_file: str):
    """Fetch /hello and save locally."""
    response = requests.get(f"{api_url}/hello")
    response.raise_for_status()

    with open(output_file, "w") as f:
        f.write(response.text)

    print(f"[+] Saved /hello response to {output_file}")


def fetch_random_and_ssh(api_url: str, hostname: str, username: str, password: str, remote_filename: str):
    """Fetch /random and store on remote machine via SSH."""
    response = requests.get(f"{api_url}/random")
    response.raise_for_status()
    phrase = response.text

    print("[+] Connecting via SSH...")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)

    sftp = ssh.open_sftp()
    remote_path = f"/{remote_filename}.txt"

    with sftp.open(remote_path, "w") as remote_file:
        remote_file.write(phrase)

    sftp.close()
    ssh.close()

    print(f"[+] Saved /random phrase to remote machine: {remote_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Two-mode task script")

    parser.add_argument(
        "mode",
        choices=["hello", "random"],
        help="Which mode to run"
    )
    parser.add_argument("--api-url", default=None, help="Base URL for FastAPI server, e.g. http://localhost:8000")

    # Options for 'hello' mode
    parser.add_argument("--output-file", default="hello.txt", help="Local file to save /hello response")

    # Options for 'random' mode
    parser.add_argument("--hostname", help="SSH host")
    parser.add_argument("--port", default="8000", help="Port")
    parser.add_argument("--username", help="SSH username")
    parser.add_argument("--password", help="SSH password")
    parser.add_argument("--remote-filename", help="Remote filename without extension")

    args = parser.parse_args()
    
    if args.api_url is None:
        host_ip = get_host_ip()
        args.api_url = f"http://{host_ip}"

    if args.mode == "hello":
        fetch_hello(f"{args.api_url}:{args.port}", args.output_file)

    elif args.mode == "random":
        if not all([args.hostname, args.username, args.password, args.remote_filename]):
            raise ValueError("Missing SSH parameters for random mode")

        fetch_random_and_ssh(
            args.api_url,
            args.hostname,
            args.username,
            args.password,
            args.remote_filename
        )
