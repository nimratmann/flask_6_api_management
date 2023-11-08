import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def calculate_bmi(weight, height):
    weight_num = float(weight)
    height_num = float(height)
    bmi = weight_num / (height_num * height_num)
    return bmi

@app.route("bmi")
def bmi_calculator(req: func.HttpRequest) -> func.HttpResponse:
    weight = req.params.get("weight")
    height = req.params.get("height")

    if not weight or not height:
        return func.HttpResponse("Please provide both weight and height parameters.", status_code=400)

    try:
        bmi = calculate_bmi(weight, height)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        response_message = f'Your BMI is {bmi:.2f}, which is categorized as {category}.'
        return func.HttpResponse(response_message)
    except ValueError:
        return func.HttpResponse('Invalid weight or height values. Please provide numeric values.', status_code=400)
