# AWS ML Model Deployment with REST API

This repository provides a comprehensive guide and code example for deploying a machine learning model on Amazon Web Services (AWS) using a REST API. The deployment process involves creating an inference script using FastAPI and deploying it on an Amazon EC2 instance.

## 1. Table of Contents

- [Introduction](intro)
- [Deployment Process](deployment-process)
- [Accessing the App](accessing-the-app)
- [Usage](usage)
- [Contributing](contributing)
- [License](license)

## 2. Introduction <a name="intro"></a>

Deploying machine learning models into production requires careful consideration of various factors beyond just technical functionality. This repository offers a step-by-step guide to deploying a trained machine learning model using AWS EC2 and FastAPI to create a REST API for predictions. The guide ensures that the model is accessible from anywhere, bridging the gap between local development and production.

## 3. Deployment Process <a name="deployment-process"></a>

##### 3.1 Model Training:
The process begins by training a machine learning model tailored to your problem. The used model for this repo can be accessed in [this repo](https://github.com/MUmairAB/Stroke-Prediction-using-Machine-Learning).

#### 3.2 Inference Script with FastAPI:
The trained model can be used for inference by developing a FastAPI for the model. This script allows you to receive input data, pass it through the trained model, and receive predictions. The inference script is stored as [Stroke Prediction APP.py](https://github.com/MUmairAB/AWS-ML-Model-Deplyment-with-REST-API/blob/main/Stroke%20Prediction%20APP.py).

#### 3.3 Setting Up AWS EC2 Instance:
Follow the instructions provided in my article published in Towards DataScience on Medium. This instance will serve as a remote web server for hosting the FastAPI application.

#### 3.4 Deploying FastAPI on EC2:
Once the EC2 instance is set up, transfer the requirements.txt, Stroke Prediction APP.py, and trained_model.sav files to the web server using instructions provided in the same article. Then, run the Python script on the EC2 instance to make the model accessible through the internet by running the following commands provided in [CLI Commands.txt](https://github.com/MUmairAB/AWS-ML-Model-Deplyment-with-REST-API/blob/main/CLI%20Commands.txt)

```
sudo yum update --> to upgrade the installed packages to the latest version
sudo yum install python3-pip --> to install the pip3

cd Model_files --> move to the folder containing the Python script and other supporting files

ls -lrt --> list all the files

pip3 install -r requirements.txt --> install the libraries specified in the file
python3 'Stroke Prediction APP.py' --> run the Python file
```

<img src="https://github.com/MUmairAB/AWS-ML-Model-Deplyment-with-REST-API/blob/main/Images%20of%20Running%20App/Running%20the%20app%20from%20PuTTY.png?raw=true" />

## 4. Accessing the App <a name="accessing-the-app"></a>

The app is accessible through the "**Public IPv4 DNS:8080**" address. In my case, it was "**http://ec2-16-171-47-137.eu-north-1.compute.amazonaws.com:8080**" The Public IPv4 DNS address will be different for your web server. Nonetheless, there are multiple ways to use this address to access the app.

#### 4.1 Access the Web App From the Internet
We can simply paste the app address in the search bar of a browser and it will be accessible to us. As shown by the SwaggerUI/OpenAI Docs.

<img src="https://github.com/MUmairAB/AWS-ML-Model-Deplyment-with-REST-API/blob/main/Images%20of%20Running%20App/SwaggerUI%20from%20internet%20croped.png?raw=true" />

#### 4.2 Use the Web App From Shell
We can use the deployed app from the Shell as well. Here, we'll access it using GitBash using the following commands provided in [Accessing Deployed App From Shell.sh](https://github.com/MUmairAB/AWS-ML-Model-Deplyment-with-REST-API/blob/main/Accessing%20Deployed%20App%20From%20Shell.sh) file.

```
curl -X 'POST' \
'http://ec2-16-171-47-137.eu-north-1.compute.amazonaws.com:8080/predict'
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
  "gender": "Male",
  "age": 60,
  "hypertension": true,
  "heart": true,
  "work": "Private Job",
  "glucose": 250,
  "bmi": 60
}'
```
The screenshot of GitBash shows the output.
<img src="https://github.com/MUmairAB/AWS-ML-Model-Deplyment-with-REST-API/blob/main/Images%20of%20Running%20App/Accessing%20the%20AWS%20app%20from%20Git%20Bash.png?raw=true" />

#### 4.3 Use the Web App From the Python Code
We can use the deployed app for inference from Python code as well. Use the script provided in [Using AWS Model in Python Code](https://github.com/MUmairAB/AWS-ML-Model-Deplyment-with-REST-API/blob/main/Using%20AWS%20Model%20in%20Python%20Code) file.

<img src="https://github.com/MUmairAB/AWS-ML-Model-Deplyment-with-REST-API/blob/main/Images%20of%20Running%20App/Using%20ML%20model%20from%20AWS%20EC2%20in%20Python%20code.png?raw=true" />

## 5. Usage <a name="usage"></a>

- Clone this repository to your local machine.
- Review the provided code files, especially the Stroke Prediction APP.py script.
- Follow the guide provided in the article to understand the deployment process.
- Create an EC2 instance on AWS as outlined in the guide and ensure you have the necessary credentials.
- Use WinSCP or similar tools to transfer the files to your EC2 instance as shown in the guide.
- SSH into your EC2 instance using PuTTY or a similar tool and follow the commands in the guide to set up the environment and run the FastAPI script.
- Access the deployed model's REST API by using the EC2 instance's public DNS and port (usually port 8080) in your web browser or through HTTP requests.

## 6. Contributing <a name="contributing"></a>
Contributions to this repository are welcome! If you find any issues or have improvements to suggest, feel free to create pull requests.

## 7. License <a name="license"></a>
This repository is licensed under the MIT License. See the LICENSE file for details.
