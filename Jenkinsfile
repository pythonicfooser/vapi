node {
   stage("clone repo"){
     deleteDir()
     checkout scm
   }
   stage("Build docker image") {
     docker.build("pwall:${GIT_BRANCH}")
   }
   stage("Deploy"){
     sh "ansible-playbook playbook.yaml -v --extra-vars '${GIT_BRANCH}=true hosts=${GIT_BRANCH}'"
   }
}
