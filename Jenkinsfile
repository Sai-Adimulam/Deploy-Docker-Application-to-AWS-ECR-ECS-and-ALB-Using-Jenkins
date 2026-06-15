pipeline{
    agent any
   
     stages{
        stage('Github'){
            steps{
              git branch : 'main',
              url :'https://github.com/Sai-Adimulam/Deploy-Docker-Application-to-AWS-ECR-ECS-and-ALB-Using-Jenkins'
            }
        }
        stage('Build Docker Image'){
            steps{
               sh 'docker build -t app-2:v1 .'
            }
        }
        stage('AWS Authentication ECR'){
            steps{
                sh 'aws ecr get-login-password --region app-south-2 | docker login --username AWS --password-stdin 908708651361.dkr.ecr.ap-south-2.amazonaws.com'
            }
        }
        stage('Tag image to ecr'){
            steps{
                sh 'docker tag app-2:v1  908708651361.dkr.ecr.ap-south-2.amazonaws.com/app-2:v1'
            }
        }
        stage('Push image to ecr'){
            steps{
                sh 'docker push 908708651361.dkr.ecr.ap-south-2.amazonaws.com/app-2:v1'
            }
        }
        stage('Deploy to ECS'){
            steps{
                sh '''
                aws ecs update-service \
                --cluster app-2-cluster \
                --service app-2-task-service \
                --force-new-deployment \
                --region ap-south-2 
                '''
            }
        }
     }
}
