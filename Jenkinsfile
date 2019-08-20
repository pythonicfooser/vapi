node {
   stage("clone repo"){
     deleteDir()
     checkout scm
   }
   stage("first") {
     docker.build("pwall:master")
   }
   stage("second"){
     sh "echo 'hi fool'"
   }
}
