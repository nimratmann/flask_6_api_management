# flask_6_api_management
To develop and document APIs using Flask, and manage them with Azure API Management

## Schema
My Github repository contains a Flask folder and a BMI Checker folder. Within the Flask folder, there is a basic Flask app that I deployed locally to utilize a GET request and a Flasgger Flask app which is a Flask extension, utilizing the Flassger interface, to extract OpenAPI-Specification from all Flask views registered in your API. Within the BMI checker folder, I created Python files to define the body mass index calculations to launch an Azure Serverless Function Application. This application was successfully deployed locally and is accessible via Azure. 
Azure API Deployment Link: [https://mannapp.azurewebsites.net](https://mannapp.azurewebsites.net/api/bmi)
