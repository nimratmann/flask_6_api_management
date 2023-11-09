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



## Open API



## Errors

