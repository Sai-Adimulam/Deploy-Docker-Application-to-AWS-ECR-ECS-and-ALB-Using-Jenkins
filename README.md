# Deploy-Docker-Application-to-AWS-ECR-ECS-and-ALB-Using-Jenkins

Project Implementation Steps

Step 1: Create Application Files

Created the following files:

app.py
requirements.txt
Dockerfile
Jenkinsfile
Step 2: Create Amazon ECR and ECS Resources

Created:

Amazon ECR Repository
Amazon ECS Cluster
ECS Task Definition
Step 3: Configure Networking

Created:

Target Group
Application Load Balancer (ALB)
Security Groups
Step 4: Create ECS Service

Created an ECS Service using the task definition and attached it to the Application Load Balancer.

Step 5: Update Jenkins Pipeline

Configured Jenkins pipeline to:

Build Docker Image
Authenticate with Amazon ECR
Push Docker Image to ECR
Trigger ECS Deployment
Step 6: Push Source Code to GitHub

Uploaded the project source code to GitHub for version control and CI/CD integration.

Step 7: Execute Jenkins Pipeline

Triggered the Jenkins pipeline to:

Pull code from GitHub
Build Docker image
Push image to Amazon ECR
Deploy the latest image to Amazon ECS
Step 8: Access Application

Copied the Application Load Balancer DNS endpoint and accessed the application through a web browser.

End-to-End Workflow
Developer
    │
    ▼
GitHub Repository
    │
    ▼
Jenkins Pipeline
    │
    ▼
Build Docker Image
    │
    ▼
Amazon ECR
    │
    ▼
Amazon ECS Cluster
    │
    ▼
ECS Service
    │
    ▼
Application Load Balancer (ALB)
    │
    ▼
Web Browser / End User

## Jenkinspipeline

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
                sh 'aws ecr get-login-password --region ap-south-2 | docker login --username AWS --password-stdin 908708651361.dkr.ecr.ap-south-2.amazonaws.com'
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
