# Wine Quality prediction using MLFLOW

**Stage 1**

In the first stage I am creating template.py python file in which I will be writing my script to create all the required folder structure along with all the constructor files and other required files.

**Stage 2**

In the second stage I will be using my requirements.txt file where I will be passing all the required packages for this project and at one click I can install all the package.

**Stage 3**

In this stage I will be using setup.py file for creating a local package. 

**Stage 4**

I have created a common.py in util folders where I have stored all the function that are mostly used.

**Workflows**
1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline 
8. update main.py
9. update app.py



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/mukesh1996-ds/Wine_Quality_prediction_using_MLFLOW.mlflow \
MLFLOW_TRACKING_USERNAME=mukesh1996-ds \
MLFLOW_TRACKING_PASSWORD=aa062802eb1f513fcfe5d6c64bf38c73f61143d6 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/mukesh1996-ds/Wine_Quality_prediction_using_MLFLOW.mlflow

export MLFLOW_TRACKING_USERNAME=mukesh1996-ds

export MLFLOW_TRACKING_PASSWORD=aa062802eb1f513fcfe5d6c64bf38c73f61143d6

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model

