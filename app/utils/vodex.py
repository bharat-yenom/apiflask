import requests
import os

vodex_token = os.environ.get("vodex_token")
vodex_api_url = "https://api.vodex.ai/api/v1/trigger-call"

def make_vodex_api_call(data, name, phoneNumber):
    print("here")
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": vodex_token,
    }
    # Extract data from the request
    name = name
    phone_number = phoneNumber
    job_title = data.get('JobTitle', 'Not specified')
    job_location = data.get('City', 'Not specified')
    hourly_rate = data.get('HourlyRate', 'Not specified')
    job_type = data.get('JobType', 'Not specified')
    remote = data.get('RemoteHybrid', 'Not specified')
    required_skills = data.get('RequiredSkills', 'Not specified')
    recruiter_name = data.get('RecruiterName', 'Not specified')
    recruiter_phone = data.get('RecruiterPhoneNumber', 'Not specified')
    recruiter_email = data.get('RecruiterEmail', 'Not specified')
    duration= data.get('Duration','Not specified')
    salary = data.get('Salary', 'Not specified')
    print(name)
    print(recruiter_name)
 
    # project_id = data.get('projectId')
    result_string = lambda x: ', '.join(x)
    payload = {
        "callList": [
            {
                "firstName": "{}".format(name),
                "lastName": "",
                "phone": "{}".format(phone_number),
                "job_title": "{}".format(job_title),
                "job_location": "{}".format(job_location),
                "hourly_rate": "{}".format(hourly_rate),
                "job_type": "{}".format(job_type),
                "remote": "{}".format(remote),
                "required_skills": "{}".format(result_string(required_skills)),
                "recruiter_name": "{}".format(recruiter_name),
                "recruiter_phone": "{}".format(recruiter_phone),
                "recruiter_email": "{}".format(recruiter_email),
                "duration": "{}".format(duration),
                "lead_name":"{}".format(name),
                "rules":  "{}".format(data['rules'] if 'rules' in data else 'rules not added'),
                "company_information":  "{}".format(data['company_information'] if 'company_information' in data else 'company information not disclosed'),
                "salary": "{}".format(salary)
                }
            ]
    ,
        "projectId": "{}".format("65c63e93f31b37f4b76aa9f7"),
    }
 
    response = requests.post(vodex_api_url, json=payload, headers=headers)
    response.raise_for_status()
    response_data = response.json()  # Get JSON response data
    print(response_data)
    return response.json()