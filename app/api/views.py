from flask import jsonify, request
import requests
import os
from app.api import api_bp
from app.utils.synthflow import make_synthflow_call
from app.utils.vodex import make_vodex_api_call

auth_token = os.environ.get("AUTH_TOKEN")
SYNTHFLOW_API_URL = "https://fine-tuner.ai/api/1.1/wf/v2_voice_agent_call"

@api_bp.route('/call', methods=['POST'])
def make_call():
    try:
        data = request.get_json()
 
        # Extract data from the request
        name = data.get('name')
        phone = data.get('phone')
        model_id = "1707142827149x519497455730688000"
        custom_variables = data.get('custom_variables')
 
        # Make the API call to Synthflow.ai
        payload = {
            "model": model_id,
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
 
        # Handle the response
        if response.status_code == 200:
            response_data = {'status': 'success', 'response': response.json()}
        else:
            response_data = {'status': 'error', 'response': response.text}
 
        return jsonify(response_data)
 
    except Exception as e:
        # Handle exceptions
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response)

@api_bp.route('/vodexcall', methods=['POST'])
def make_vodex_call():
    try:
        data = request.get_json()
 
        # Extract data from the request
        name = data.get('TestName')
        phone_number = data.get('TestPhoneNumber')
        job_title = data.get('JobTitle')
        job_location = data.get('City')
        hourly_rate = data.get('HourlyRate')
        job_type = data.get('JobType')
        remote = data.get('RemoteHybrid')
        required_skills = data.get('RequiredSkills')
        recruiter_name = data.get('RecruiterName')
        recruiter_phone = data.get('RecruiterPhoneNumber')
        recruiter_email = data.get('RecruiterEmail')
        print(name)
        print(recruiter_name)
 
        # project_id = data.get('projectId')
 
        payload = {
            "callList": [
                {
                    "firstName": "{}".format(name),
                    "lastName": "Sai",
                    "phone": "{}".format(phone_number),
                    "job_title": "{}".format(job_title),
                    "job_location": "{}".format(job_location),
                    "hourly_rate": "{}".format(hourly_rate),
                    "job_type": "{}".format(job_type),
                    "remote": "{}".format(remote),
                    "required_skills": "{}".format(required_skills),
                    "recruiter_name": "{}".format(recruiter_name),
                    "recruiter_phone": "{}".format(recruiter_phone),
                    "recruiter_email": "{}".format(recruiter_email),
                    }
                ]
        ,
            "projectId": "{}".format("65c63e93f31b37f4b76aa9f7"),
        }
 
        response_data = make_vodex_api_call(payload)
        return jsonify({'status': 'success', 'response': response_data})
 
    except Exception as e:
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response)