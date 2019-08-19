pipeline {
  agent any
  stages {
    stage('build Docker image'){
        steps{
	        sh echo "docker build -t vapi:${GIT_BRANCH} ."
        }
    }
    stage('first_data'){
        steps{
	        sh echo "Jenkinsfile."
        }
    }
  }
}
