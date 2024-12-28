pipeline{
  agent any
  stages{
    stage('Access Minikube Service'){
      steps{
        script{
          def minikubeServiceUrl = "http://192.168.49.2:30414"
          sh "curl -X GET ${minikubeServiceUrl}"
        }
      }
    }
  }
}
