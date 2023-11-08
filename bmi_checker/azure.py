import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Parse the query parameters from the request
    weight_value = req.params.get('weight', '70')
    height_value = req.params.get('height', '1.75')

    # Convert weight and height to numbers
    weight_num = float(weight_value)
    height_num = float(height_value)

    # Calculate BMI
    bmi = weight_num / (height_num * height_num)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal Weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    # Create a JSON response
    response = {
        'entered_weight': weight_num,
        'entered_height': height_num,
        'bmi': bmi,
        'category': category
    }

    return func.HttpResponse(json.dumps(response), mimetype="application/json")
