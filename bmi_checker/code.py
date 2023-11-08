import requests
import pandas as pd

df = pd.DataFrame({
    'weight': [70, 80, 90, 75],
    'height': [1.75, 1.80, 1.85, 1.70]
})

weight_value = df[:1]['weight'][0]
height_value = df[:1]['height'][0]

# Fill in your Azure Function URL
azure_function_url = 'https://mannapp.azurewebsites.net/api/bmi'

analysis = requests.get(
    url=azure_function_url,
    params={
        "weight": weight_value,
        "height": height_value
    }
)

analysis.text
