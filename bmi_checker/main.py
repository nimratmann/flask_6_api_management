from flask import escape
import functions_framework
import json
import pandas as pd 

@functions_framework.http
def hello_http(request):
    request_args = request.args

    if request_args and "weight" in request_args:
        weight_value = request_args["weight"]
    else:
        weight_value = 70  # Default weight in kilograms

    if request_args and "height" in request_args:
        height_value = request_args["height"]
    else:
        height_value = 1.75  # Default height in meters

    # Step 1: Convert everything to numbers
    weight_num = int(weight_value)
    height_num = int(height_value)

    # Step 2: Calculate BMI
    bmi = weight_num / (height_num * height_num)

    # Step 3: Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal Weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    # Step 4: Create a JSON object to return to the user
    output = json.dumps(
        {
            "entered_weight": weight_num,
            "entered_height": height_num,
            "bmi": bmi,
            "category": category
        }
    )

    return output

