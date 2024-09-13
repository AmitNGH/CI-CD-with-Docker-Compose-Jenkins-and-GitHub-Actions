pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "amitnd/worldofgames-score:latest"
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
                    docker compose build
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

//         stage('Test') {
//             steps {
//                 script {
//                     // Run e2e.py using Selenium to test the application
//                     sh 'python3 e2e.py'
//
//                     // Verify if tests passed or fail the pipeline
//                     script {
//                         def result = sh(script: 'python3 e2e.py', returnStatus: true)
//                         if (result != 0) {
//                             error "e2e tests failed!"
//                         }
//                     }
//                 }
//             }
//         }
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
//     post {
//         success {
//             echo 'Pipeline completed successfully!'
//         }
//
//         failure {
//             echo 'Pipeline failed!'
//         }
//
//         always {
//             // Ensure container is terminated if still running
//             script {
//                 sh "docker stop ${CONTAINER_NAME} || true"
//                 sh "docker rm ${CONTAINER_NAME} || true"
//             }
//         }
//     }
}