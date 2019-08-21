node {
   stage("clone repo"){
     deleteDir()
     checkout scm
   }
   stage("Build docker image") {
     docker.build("pwall:${BRANCH_NAME}")
   }
   stage("Deploy"){
     sh "ansible-playbook playbook.yaml -v --extra-vars '${BRANCH_NAME}=true hosts=${BRANCH_NAME}'"
   }
}
