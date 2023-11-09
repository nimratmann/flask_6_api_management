# flask_6_api_management
To develop and document APIs using Flask, and manage them with Azure API Management

## Schema
My Github repository contains a Flask folder and a BMI Checker folder. Within the Flask folder, there is a basic Flask app that I deployed locally to utilize a GET request and a Flasgger Flask app which is a Flask extension, utilizing the Flassger interface, to extract OpenAPI-Specification from all Flask views registered in your API. Within the BMI checker folder, I created Python files to define the body mass index calculations to launch an Azure Serverless Function Application. This application was successfully deployed locally and is accessible via Azure. 
Azure API Deployment Link: [https://mannapp.azurewebsites.net](https://mannapp.azurewebsites.net/api/bmi)


## Flask-Based RESTful API with Flasgger:

1. Create a Basic Flask Application with Flasgger:
Start by creating a basic Flask application with an endpoint and Flasgger integration. 
```
from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api')
def api():
    """
    API Endpoint
    This is an example endpoint that accepts a variable as a query parameter.
    ---
    parameters:
      - in: query
        name: variable
        type: string
        description: A variable to be included in the response.
    responses:
      200:
        description: An API response with the provided variable.
        content:
          application/json:
            example: {"message": "You provided 'variable' with the value 'value'."}
    """
    variable = request.args.get('variable', 'default')
    return jsonify({"message": f"You provided 'variable' with the value '{variable}.'"})

if __name__ == '__main__':
    app.run(debug=True)
```
2. Install Flask and Flasgger:
Ensure you have Flask and Flasgger installed in your virtual environment. If you haven't already installed Flasgger, you can do so using pip:
```
pip install Flask
pip install flasgger
```
3. Run the Flask Application:
```
python app.py
```
4. Access the Flasgger Interface:

You can access the Flasgger interface by navigating to the endpoint /apidocs in your web browser: http://127.0.0.1:5000/apidocs
This interactive interface allows you to observe and interact with the API operations documented in your Flask application, including the /api endpoint with the variable parameter.

5. Test the API Endpoint:

To test the /api endpoint, navigate to: http://127.0.0.1:5000/api?variable=value
Replace value with your desired value. You can add multiple query parameters by separating them with '&'. You should see the documented response with the provided variable in the Flasgger interface.



## Azure API Deployment
1. Install Azure Functions Core Tools using the following command:
```
sudo apt-get install azure-functions-core-tools-4
```
2. Create a Local Function:
Navigate to your project's directory, and run the following command to create a local function project:
```
func init LocalFunctionProj --python -m V2
```
This command will create a folder containing various files, including a .py file to run your app.

3. Edit the function_app.py file within the LocalFunctionProj folder and add your desired functions. The syntax is similar to Flask but not identical. Here's an example:

```
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="HttpExample")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("HttpExample function processed a request!")
```
4. Run Your Function Locally using the following command:
```
func start
```
This will start a local development server, and you can test your API requests using the endpoints and variables specified in your function.

5. Create Azure Resources:

In Azure, create the necessary resources to host your app, including a resource group, a storage account, and an Azure Function App. You can create these resources using Azure CLI commands:

Create a resource group:
```
az group create --name (ResourceGroupName) --location (Region)
```
Create a storage account:
```
az storage account create --name (StorageAccountName) --location (Region) --resource-group (ResourceGroupName) --sku Standard_LRS
```
Create an Azure Function App:

```
az functionapp create --resource-group (ResourceGroupName) --consumption-plan-location (Region) --runtime python --runtime-version 3.9 --functions-version 4 --name (AppName) --os-type linux --storage-account (StorageAccountName)
```
6. Update Local Settings:

In the local.settings.json file within the LocalFunctionProj folder, replace the "AzureWebJobsStorage" value with the connection string value for your storage account.

Here's an example local.settings.json:
```
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
    "AzureWebJobsStorage": "your_connection_string_here"
  }
}
```
7. Deploy Your App:

Deploy your app using the following command, replacing (AppName) with the name of your Azure Function App:

```
func azure functionapp publish (AppName)
```
8. Update App Settings:

To update the app settings, run the following command, replacing (FUNCTION_APP_NAME) and (RESOURCE_GROUP_NAME) with your specific values:
```
az functionapp config appsettings set --name (FUNCTION_APP_NAME) --resource-group (RESOURCE_GROUP_NAME) --settings AzureWebJobsFeatureFlags=EnableWorkerIndexing
```

You've successfully deployed an Azure Function API. Your API should now be available on Azure, and you can access it through the specified endpoint.
Azure API Deployment Link: [https://mannapp.azurewebsites.net](https://mannapp.azurewebsites.net/api/bmi)

## Open API



## Errors

