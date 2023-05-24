import requests
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "9KCEHHF6PQI6ADTeoecRqjtf1LtrtH8u3faUkjfAxFyE"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

payload_scoring = {"input_data": [{"field": [["ph","Hardness","Solids","Chloramin","Sulfate","Conductivity","Organic_carbon","Trichalomethanes","Turbidity"]], "values": [[9,128,19859,8,300,451,14,73,4]]}]}

response_scoring = requests.post('https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/82f5d5bd-e956-4579-acfa-c83a665eb79d/predictions?version=2023-05-24', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json()['predictions'][0]['values'][0][0])