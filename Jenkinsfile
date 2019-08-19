pipeline {
    agent any
    stages {
        stage('build Docker image') {
            steps {
                sh echo "docker build -t vapi:proof ."
            }
        }
    }
}
