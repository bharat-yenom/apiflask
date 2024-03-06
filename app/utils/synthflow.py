import requests
import os
from flask import jsonify

auth_token = os.environ.get("AUTH_TOKEN")
SYNTHFLOW_API_URL = "https://fine-tuner.ai/api/1.1/wf/v2_voice_agent_call"

def make_synthflow_call(name, phone, custom_variables):
    try:
 
        model_ide = "1707743556947x474737352736243700"
 
 
        # custom_variables = data.get('custom_variables')
 
        # Make the API call to Synthflow.ai
        payload = {
            "model": model_ide,
            "phone": phone,
            "name": name,
            "custom_variables": custom_variables
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": auth_token
        }
 
        response = requests.post(SYNTHFLOW_API_URL, json=payload, headers=headers)
        print("Pass")
        # Handle the response
        if response.status_code == 200:
            response_data = {'status': 'success', 'response': response.json()}
        else:
            response_data = {'status': 'error', 'response': response.text}
        print(jsonify(response_data))
        print(response_data)
        return jsonify(response_data)
 
    except Exception as e:
        print("I am here3")
        # Handle exceptions
        error_response = {'status': 'error', 'response': str(e)}
        print(error_response)
        return jsonify(error_response)