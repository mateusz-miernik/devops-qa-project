pipeline {
    agent any

    parameters {
        choice(
            name: 'MODE',
            choices: ['hello', 'random'],
            description: 'Which mode to run in the Python script'
        )
        string(
            name: 'API_URL',
            defaultValue: 'http://host.docker.internal:8000',
            description: 'URL of the FastAPI server'
        )
        string(
            name: 'SSH_HOST',
            defaultValue: '',
            description: 'Remote SSH host (required for random mode)'
        )
        string(
            name: 'SSH_USER',
            defaultValue: '',
            description: 'SSH username (required for random mode)'
        )
        password(
            name: 'SSH_PASSWORD',
            defaultValue: '',
            description: 'SSH password (required for random mode)'
        )
        string(
            name: 'REMOTE_FILENAME',
            defaultValue: 'output',
            description: 'Output filename on remote machine (random mode only)'
        )
    }

    stages {

        stage('Pull or Build Docker Image') {
            steps {
                echo "Ensuring Docker image exists..."
                sh """
                    if ! docker images | grep -q 'task-runner'; then
                        echo 'Image not found, building...'
                        docker build -t task-runner .
                    else
                        echo 'Docker image task-runner already exists.'
                    fi
                """
            }
        }

        stage('Run Script in Docker') {
            steps {
                script {
                    if (params.MODE == 'hello') {
                        echo "Running Hello mode..."
                        sh """
                            docker run --rm task-runner \
                                hello \
                                --api-url ${params.API_URL}
                        """
                    } else {
                        echo "Running Random mode..."
                        sh """
                            docker run --rm task-runner \
                                random \
                                --api-url ${params.API_URL} \
                                --hostname ${params.SSH_HOST} \
                                --username ${params.SSH_USER} \
                                --password ${params.SSH_PASSWORD} \
                                --remote-filename ${params.REMOTE_FILENAME}
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}