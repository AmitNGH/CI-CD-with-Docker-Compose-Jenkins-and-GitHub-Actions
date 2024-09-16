pipeline {
    agent any

    environment {
        CONTAINER_NAME = "worldofgames-score-1"
        PORT = 5000
        DUMMY_FILE = "Scores.txt"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'level-4', url: 'https://github.com/AmitNGH/WorldOfGames.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'docker compose build'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh 'docker compose up -d score'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'docker exec ${CONTAINER_NAME} mkdir Score'
                    sh 'docker exec ${CONTAINER_NAME} /bin/sh -c \"echo \'5\' > Score/${DUMMY_FILE}\"'
                    sh 'docker network connect jenkins ${CONTAINER_NAME}'
                    sh """
                        python3 -m venv ./venv
                        . ./venv/bin/activate
                        ./venv/bin/pip install -r ./WorldOfGames/requirements.txt
                    """

                    ip = sh(script: 'docker inspect -f "{{.NetworkSettings.Networks.jenkins.IPAddress}}" ${CONTAINER_NAME}', returnStdout: true).trim()
                    echo "IP Address: ${ip}"

                    sh """
                        . ./venv/bin/activate
                        ./venv/bin/python ./WorldOfGames/e2e.py "${ip}" "${PORT}"
                    """
                }
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-repository', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    script {
                        sh "echo  $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                        sh "docker compose push"
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
            }
        }
    }
}