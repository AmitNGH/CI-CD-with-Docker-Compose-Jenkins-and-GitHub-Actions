pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "amitnd/worldofgames-score"
        CONTAINER_NAME = "worldofgames-score-1"
        PORT = 8777
        DUMMY_FILE = "Scores.txt"
        DOCKER_HUB_CREDENTIALS = 'dockerhub-credentials-id'  // Jenkins credentials ID for DockerHub
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from the repository
                git branch: 'level-4', url: 'https://github.com/AmitNGH/WorldOfGames.git'
            }
        }

        stage('Build') {
            steps {
                // Build the Docker image
                script {
                    sh 'docker compose build'
                }
            }
        }

        stage('Run') {
            steps {
                script {

                    // sh 'docker compose up -d score'
                    sh 'docker compose up -d score'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'docker exec ${CONTAINER_NAME} mkdir Score'
                    sh 'docker exec ${CONTAINER_NAME} /bin/sh -c \"echo \'5\' > Score/Scores.txt\"'
                    sh 'docker network connect jenkins worldofgames-score-1'
                    sh '''
                        python3 -m venv ./venv
                        . ./venv/bin/activate
                        ./venv/bin/pip install -r ./WorldOfGames/requirements.txt
                        ./venv/bin/pip install webdriver-manager
                        '''


                    // Capture the IP address from Docker
                    ip = sh(script: 'docker inspect -f "{{.NetworkSettings.Networks.jenkins.IPAddress}}" worldofgames-score-1', returnStdout: true).trim()
                    echo "IP Address: ${ip}"

                    sh """
                        . ./venv/bin/activate
                        ./venv/bin/python ./WorldOfGames/e2e.py "${ip}" 5000
                    """
                }
            }
        }
    }
    post {
        always {
            script {
                sh 'docker logs ${CONTAINER_NAME}'
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
            }
        }
    }
}