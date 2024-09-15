pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "amitnd/worldofgames-score"
        CONTAINER_NAME = "worldofgames-score"
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
                    sh 'echo "5" > ${DUMMY_FILE}'

                    sh """
                    docker run -d --name ${CONTAINER_NAME} \
                    -p ${PORT}:8777 \
                    -v ${WORKSPACE}/${DUMMY_FILE}:/worldofgames/Score/${DUMMY_FILE} \
                    ${DOCKER_IMAGE}:latest
                    """
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run e2e.py using Selenium to test the application
                    sh 'pip install -r ./WorldOfGames/requirements.txt'
                    sh 'python3 ./WorldOfGames/e2e.py'

                    // Verify if tests passed or fail the pipeline
                    script {
                        def result = sh(script: 'python3 e2e.py', returnStatus: true)
                        if (result != 0) {
                            error "e2e tests failed!"
                        }
                    }
                }
            }
        }
//
//         stage('Finalize') {
//             steps {
//                 script {
//                     // Stop and remove the running container
//                     sh "docker stop ${CONTAINER_NAME}"
//                     sh "docker rm ${CONTAINER_NAME}"
//
//                     // Log in to DockerHub
//                     withCredentials([usernamePassword(credentialsId: "${DOCKER_HUB_CREDENTIALS}", passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
//                         sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
//
//                         // Push the built image to DockerHub
//                         sh "docker push ${DOCKER_IMAGE}:latest"
//                     }
//
//                     // Clean up workspace
//                     cleanWs()
//                 }
//             }
//         }
    }
//
    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }

        always {
            // Ensure container is terminated if still running
            script {
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
            }
        }
    }
}


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
                    sh 'echo "5" > ${DUMMY_FILE}'

                    // sh 'docker compose up -d score'
                    sh 'docker compose up -d score'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'docker exec ${CONTAINER_NAME} /bin/sh -c \"echo \'5\' > Score.txt\"'
                    sh 'docker container list'
                    sh 'docker network connect jenkins worldofgames-score-1'
                    sh 'curl http://$(docker inspect -f \'{{.NetworkSettings.Networks.jenkins.IPAddress}}\' worldofgames-score-1):<port>'
                    // Run e2e.py using Selenium to test the application
                    // sh 'python3 -m venv ./venv'
                    // sh './venv/bin/pip install -r ./WorldOfGames/requirements.txt'
                    // sh './venv/bin/pip install webdriver-manager'
                    // sh './venv/bin/python3 ./WorldOfGames/e2e.py'

                    // Verify if tests passed or fail the pipeline
                    // script {
                    //     def result = sh(script: 'python3 e2e.py', returnStatus: true)
                    //     if (result != 0) {
                    //         error "e2e tests failed!"
                    //     }
                    // }
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }

        always {
            // Ensure container is terminated if still running
            script {
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
            }
        }
    }
}

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
                    sh 'echo "5" > ${DUMMY_FILE}'

                    // sh 'docker compose up -d score'
                    sh 'docker compose up -d score'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'docker exec ${CONTAINER_NAME} /bin/sh -c \"echo \'5\' > Score/Score.txt\"'
                    sh 'docker container list'
                    sh 'docker network connect jenkins worldofgames-score-1'
                    // sh "curl http://\$(docker inspect -f '{{.NetworkSettings.Networks.jenkins.IPAddress}}' worldofgames-score-1):5000"

                    // Run e2e.py using Selenium to test the application
                    sh 'python3 -m venv ./venv'
                    sh './venv/bin/pip install -r ./WorldOfGames/requirements.txt'
                    sh './venv/bin/pip install webdriver-manager'
                    // sh  """
                    //     ip=\$(docker inspect -f "{{.NetworkSettings.Networks.jenkins.IPAddress}}" worldofgames-score-1)'
                    //     sh './venv/bin/python -c "import e2e; e2e.main_function('$ip', 5000)"'

                    //     """
                    // Capture the IP address from Docker


                    // Capture the IP address from Docker
                    def ip = sh(script: 'docker inspect -f "{{.NetworkSettings.Networks.jenkins.IPAddress}}" worldofgames-score-1', returnStdout: true).trim()
                    echo "IP Address: ${ip}"

                    // Run the Python script and capture output and exit code
                    def pythonScript = """
                        ./venv/bin/python -c "from WorldOfGames import e2e; e2e.main_function('${ip}', 5000)"
                        echo \$?
                    """
                    echo "Running Python script..."
                    def pythonOutput = sh(script: pythonScript, returnStdout: true).trim()

                    // Extract exit code from the output
                    def outputLines = pythonOutput.split('\n')
                    def exitCode = outputLines.size() > 1 ? outputLines[-1].toInteger() : 0
                    echo "Python Script Output: ${pythonOutput}"
                    echo "Python Script Exit Code: ${exitCode}"

                    // Store exit code in environment variable as a string
                    env.PYTHON_EXIT_CODE = exitCode.toString()

                    // Check if the Python script failed
                    if (exitCode != 0) {
                        error "Python script failed with exit code ${exitCode}"
                    }

                    echo "Python script succeeded"
                        // sh  '''
                        //     ip=$(docker inspect -f "{{.NetworkSettings.Networks.jenkins.IPAddress}}" worldofgames-score-1)
                        //     ls -l
                        //     ./venv/bin/python -c "from WorldOfGames import e2e; e2e.main_function(\\\"$ip\\\", 5000)"
                        //     exit_code=$?
                        //     if [ $exit_code -ne 0 ]; then
                        //         echo "e2e Tests failed!"
                        //       exit $exit_code
                        //     '''

                        // sh 'python -c "import e2e; e2e.main_function(\\"$ip\\", 5000)"'


                    // Verify if tests passed or fail the pipeline
                    // script {
                    //     def result = sh(script: 'python3 e2e.py', returnStatus: true)
                    //     if (result != 0) {
                    //         error "e2e tests failed!"
                    //     }
                    // }
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }

        always {
            // Ensure container is terminated if still running
            script {
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
            }
        }
    }
}