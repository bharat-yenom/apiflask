import requests
import os

# Your Vapi API Authorization token
auth_token = os.environ.get("vapi_token")
# The Phone Number ID, and the Customer details for the call
phone_number_id = 'e64d70b8-884e-426d-be57-b8400eb26803'

result_string = lambda x: ', '.join(x)
def make_vapi_calls(data):
        
        customer_number = data['TestPhoneNumber']
 
        # Create the header with Authorization token
        headers = {
            'Authorization': f'Bearer {auth_token}',
            'Content-Type': 'application/json',
        }
        name = data['TestName']
        job_title= data['JobTitle'] if 'JobTitle' in data else 'not specified'
        job_location = data['City'] if 'City' in data else '_'
        hourly_rate = data['HourlyRate'] if 'HourlyRate' in data else 'not specified'
        job_type = data['JobType'] if 'JobType' in data else 'not specified'
        remote_or_hybrid = data['RemoteHybrid'] if 'RemoteHybrid' in data else 'not specified'
        required_skills = result_string(data['RequiredSkills']) if 'RequiredSkills' in data else 'not specified'
        duration = data['Duration'] if 'Duration' in data else 'it is fulltime job'
        job_industry = result_string(data['Industry']) if 'Industry' in data else 'not specified'
        job_description = data['JobDescription'] if 'JobDescription' in data else 'not specified'
        recruiter_name = data['RecruiterName'] if 'RecruiterName' in data else 'not specified'
        recruiter_phone = data['RecruiterPhoneNumber'] if 'RecruiterPhoneNumber' in data else 'not specified'
        recruiter_email = data['RecruiterEmail'] if 'RecruiterEmail' in data else 'not specified'
        rules = data['rules']
        # company_information = company_information
        salary = data['Salary'] if 'Salary' in data else 'Not specified'
        client_details = data['clientData'] if 'clientData' in data else 'client not disclosed'
        client_name = data['clientName'] if 'clientName' in data else 'client not disclosed'
        seniority_level = data['SeniorityLevel'] if 'seniorityLevel' in data else 'seniority level not disclosed'
        company_information=data['company_information']
        # Create the data payload for the API request
        data = {
            'assistant': {
                "firstMessage": f"Hey, {name}, I am calling from aptask is this a good time to chat?",
                "model": {
                    "provider": "openai",
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {
                            "role": "assistant",
                            "content": f"""        *BACKGROUND INFO:*
        Your name is {recruiter_name}'s AI Assistant, and you are an AI Recruiter at Aptask, a leading Recruitment company specializing in providing Staffing Solutions to clients all over the globe. Your role involves conducting pre-qualification interviews to quickly assess if candidates have the basic skills and experience required for the Job.
       
        Recruitment Agency
        This the recruitment agency you are calling from.
        {company_information}
       
       Client Details
       You are hiring for {client_name}
       {client_details}
 
       
        Job Details:
        The ideal candidate should have strong experience working in a {job_title} and has experience with {required_skills}
        {job_type} position that requires someone who has experience working in {job_title} and has experience with {required_skills}.
        Candidate's job title is {job_title}, job location is {job_location}.
        Job Type - {job_type} [Make sure to include this in the about the job]
        Duration (only for contract job type) - {duration}
        Hourly rate (only for contract job type) - {hourly_rate} (if the recruiter do not gives this ask for the candidate their pereferred rate)
        Salary - (only for full time job type) - {salary} (if the recruiter do not gives this ask for the candidate preffered salary)
        Remote or Hybrid - {remote_or_hybrid} [make sure to mention these in the about the job]
        Job Industry (mention only if the candiate asks) - {job_industry}
        Seniority Level (mention only if the candiate asks) - {seniority_level}
        Job Description - {job_description}
       
        Recruiter Details:
        Recruiter Name - {recruiter_name}
        Recruiter Phone (read the individual numbers slowly) - {recruiter_phone}
        Recruiter Email (read the individual letters slowly) - {recruiter_email}
       
        ---
        **Rules to be followed while calls: **
        {rules}
 
        ---
        *INTERVIEW STRUCTURE AND QUESTIONS:*
        1. Introduction and Consent for Pre-Screening (1 minute):
        - [Wait for the candidate to respond. If they agree, proceed to the next questions. If they decline, thank them for their time and end the call.]
        2. About the job (1 minute):
        - You: 'Great, let’s get started. The job is for {job_title} in {job_location}. Is this something you’d be interested in?'
        - [Mention the job type also, either full time or contract, mention duration for the contract]
        - [Wait for the candidate to respond, do not interrupt. If they agree, proceed to the next questions. If they decline, thank them for their time and end the call.]
        3. Experience Check (1 minute):
        - You: 'Can you please tell me how much experience you have working in {job_title}?'
        - [Wait for the candidate to respond, do not interrupt.]
        4. Preferred hourly rate (1 minute):
        - You: 'It seems that you could be a fit for our client. What is the hourly rate you will be looking for this position?'
        - [Wait for the candidate to respond, do not interrupt.]
        5. Available time Check (1 minute):
        - You: 'What times are good for you for the phone call with the recruiter?'
        - [Wait for the candidate to respond, do not interrupt.]
        6. Doubt Solving for the candiadate (1 minute):
        - You: 'Do you have any questions for me?'
        - [Wait for the candidate to respond, do not interrupt.]
        - [Make use of the job details section]
        7. Closing (1 minute):
        - You: 'Great, as an AI, my job ends here, I will have a real recruiter contact you for more details. Please email your resume to the recruiter at {recruiter_email}. Thank you for your time.Also do  you have any more questions for me.'
        - [Wait for the candidate to respond. Then disconnect the call.]
            """
                        }
                    ]
                },
                "voice": "marissa-11labs"
            },
            'phoneNumberId': phone_number_id,
            'customer': {
                'number': customer_number,
            },
            "maxDurationSeconds": 1800,
        }
        # Make the POST request to Vapi to create the phone call
        response = requests.post(
            'https://api.vapi.ai/call/phone', headers=headers, json=data)
 
        # Check if the request was successful and print the response
        if response.status_code == 201:
            print('Call created successfully')
            print(response.json())
        else:
            print('Failed to create call')
            print(response.text)