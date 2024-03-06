from flask import Blueprint, render_template, jsonify, request
from app.models import Rule, Company, Client, Recruiter
from app.utils.job_diva import quick_job_search
from app.utils.synthflow import make_synthflow_call
from app.utils.vodex import make_vodex_api_call
from flask_cors import cross_origin
import os
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

#Job Diva

@main_bp.route('/search', methods=['GET'])
def search_job():
    search_value = request.args.get('search_value')
    if not search_value:
        return jsonify({'error': 'Search value not provided'}), 400
 
    # You might need to define these variables based on your environment
    api_url = "https://api.jobdiva.com"
    client_id = int(os.environ.get("client_id"))
    username = os.environ.get("jobdiva_username")
    password = os.environ.get("password")
    max_returned = 1  # Example max returned results
 
    search_results = quick_job_search(api_url, client_id, username, password, search_value, max_returned)
    return jsonify(search_results)


# Here we call the api refernce to run the campaign using the csv file, based on the llm we make the call with the certain api.
new_fun= lambda s: s.replace(':', '-') 
@main_bp.route('/campaignRun', methods=['POST','OPTIONS'])
@cross_origin()
def write_json_data():
    result_string = lambda x: ', '.join(x)
    try:
        data = request.get_json()
        if data["LLM"] =="Synthflow" :
 
            custom_variables = [
                "job_title: {}".format(data['JobTitle'] if 'JobTitle' in data else 'not specified'),
                "job_location: {}, {}".format(data['City'] if 'City' in data else '_', data['State'] if 'State' in data else 'not specified'),
            "hourly_rate: {}".format(data['HourlyRate'] if 'HourlyRate' in data else 'not specified'),
            "job_type:  {}".format(data['JobType'] if 'JobType' in data else 'not specified'),
            "remote_or_hybrid:  {}".format(data['RemoteHybrid'] if 'RemoteHybrid' in data else 'not specified'),
            "required_skills: {}".format(result_string(data['RequiredSkills']) if 'RequiredSkills' in data else 'not specified'),
            "duration: {}".format(data['Duration'] if 'Duration' in data else 'not specified'),
            "job_industry: {}".format(result_string(data['Industry']) if 'Industry' in data else 'not specified'),
            "job_description: {}".format(new_fun(data['JobDescription']) if 'JobDescription' in data else 'not specified'),
            "recruiter_name: {}".format(data['RecruiterName'] if 'RecruiterName' in data else 'not specified'),
            "recruiter_phone:  {}".format(data['RecruiterPhoneNumber'] if 'RecruiterPhoneNumber' in data else 'not specified'),
            "recruiter_email:  {}".format(data['RecruiterEmail'] if 'RecruiterEmail' in data else 'not specified'),
            "rules:  {}".format(data['rules'] if 'rules' in data else 'rules not added'),
             "company_information:  {}".format(new_fun(data['company_information']) if 'company_information' in data else 'company information not disclosed'),
            "salary: {}".format(data['Salary'] if 'Salary' in data else 'Not specified'),
            "client_details:  {}".format(new_fun(data['clientData']) if 'clientData' in data else 'client not disclosed'),
            "client_name:  {}".format(data['clientName'] if 'clientName' in data else 'client not disclosed'), ]  
            for entry in data['csvFile']:
                name = entry['Name']
                phone = entry['Phone'].replace('-', '')
                phone = phone.replace('+', '')
                if len(phone) == 10:
                    phone = '1' + phone
                # Here you can use name and phone as needed, for example:
                print(f"Name: {name}, Phone: {phone}")
                # time.sleep(2)
                make_synthflow_call(name,phone,custom_variables)
            # make_test_call(name,phone,custom_variables)
            # Write the JSON data to a file named 'campaign_data.json'
            # with open('campaign_data.json', 'w') as file:
            #     json.dump(data, file)
           
 
            return jsonify({'status': 'success', 'response': 'Making Calls using Synthflow'})
        if data["LLM"] =="Vodex" :
            response_data =""
            for entry in data['csvFile']:
                name = entry['Name']
                phone = entry['Phone'].replace('-', '')
                phone = phone.replace('+', '')
                if len(phone) == 10:
                    phone = '1' + phone
                # Here you can use name and phone as needed, for example:
                print(f"Name: {name}, Phone: {phone}")
                # time.sleep(2)
                response_data = make_vodex_api_call(data,name,phone)
            # make_test_call(name,phone,custom_variables)
            # Write the JSON data to a file named 'campaign_data.json'
            # with open('campaign_data.json', 'w') as file:
            #     json.dump(data, file)
           
            return jsonify({'status': 'success', 'response': 'Making Calls using Vodex'})
    except Exception as e:
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response)
   
  
# Here we call the api refernce to run the campaign for testing only phone and name is required from the recruiter to test, based on the llm we make the call with the certain api.
@main_bp.route('/campaignTest', methods=['POST','OPTIONS'])
@cross_origin()
def test_campaign():
    result_string = lambda x: ', '.join(x)
    try:
        data = request.get_json()
        if data["LLM"] =="Synthflow" :
            name = data['TestName']
            phone = data['TestPhoneNumber'].replace('-', '')
            phone = phone.replace('+', '')
            if len(phone) == 10:
                phone = '1' + phone
            custom_variables = [
                "job_title: {}".format(data['JobTitle'] if 'JobTitle' in data else 'not specified'),
                "job_location: {}, {}".format(data['City'] if 'City' in data else '_', data['State'] if 'State' in data else 'not specified'),
            "hourly_rate: {}".format(data['HourlyRate'] if 'HourlyRate' in data else 'not specified'),
            "job_type:  {}".format(data['JobType'] if 'JobType' in data else 'not specified'),
            "remote_or_hybrid:  {}".format(data['RemoteHybrid'] if 'RemoteHybrid' in data else 'not specified'),
            "required_skills: {}".format(result_string(data['RequiredSkills']) if 'RequiredSkills' in data else 'not specified'),
            "duration: {}".format(data['Duration'] if 'Duration' in data else 'not specified'),
            "job_industry: {}".format(result_string(data['Industry']) if 'Industry' in data else 'not specified'),
            "job_description: {}".format(new_fun(data['JobDescription']) if 'JobDescription' in data else 'not specified'),
            "recruiter_name: {}".format(data['RecruiterName'] if 'RecruiterName' in data else 'not specified'),
            "recruiter_phone:  {}".format(data['RecruiterPhoneNumber'] if 'RecruiterPhoneNumber' in data else 'not specified'),
            "recruiter_email:  {}".format(data['RecruiterEmail'] if 'RecruiterEmail' in data else 'not specified'),
            "rules:  {}".format(data['rules'] if 'rules' in data else 'rules not added'),
             "company_information:  {}".format(new_fun(data['company_information']) if 'company_information' in data else 'company information not disclosed'),
            "salary: {}".format(data['Salary'] if 'Salary' in data else 'Not specified'),
            "client_details:  {}".format(new_fun(data['clientData']) if 'clientData' in data else 'client not disclosed'),
            "client_name:  {}".format(data['clientName'] if 'clientName' in data else 'client not disclosed'), ]  
            print("custom_variables",custom_variables)
            make_synthflow_call(name,phone,custom_variables)
            print("I am here2")
            return jsonify({'status': 'success', 'response': 'Making calls using Synthflow'})
        if data["LLM"] =="Vodex" :
            name=data["TestName"]
            phone = data['TestPhoneNumber'].replace('-', '')
            phone = phone.replace('+', '')
            if len(phone) == 10:
                phone = '1' + phone
 
            response_data = make_vodex_api_call(data,name,phone)
            return jsonify({'status': 'success', 'response': 'Making calls using Vodex'})
    except Exception as e:
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response)

# Add your other routes for managing rules, companies, clients, and recruiters here
@main_bp.route('/getRules', methods=['GET'])
def get_rules():
    try:
        # Query the Rule table to fetch all rules
        rules = Rule.query.all()
 
        # Serialize the rules data into JSON format
        rules_data = [{'id': rule.id, 'rule_text': rule.rule_text} for rule in rules]
 
        # Return the rules data as the response
        return jsonify({'status': 'success', 'rules': rules_data})
    except Exception as e:
        # Handle any exceptions
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response), 500
    

@main_bp.route('/editRules', methods=['POST', 'DELETE'])
def manage_rules():
    if request.method == 'POST':
        # Add new rules
        try:
            data = request.get_json()
            rule_texts = data.get('rule_texts')

            if not rule_texts:
                return jsonify({'status': 'error', 'message': 'Rule texts not provided'}), 400

            # Create Rule objects for each rule text and add them to the database
            for rule_text in rule_texts:
                new_rule = Rule(rule_text=rule_text)
                db.session.add(new_rule)
            
            db.session.commit()

            return jsonify({'status': 'success', 'message': 'Rules added successfully'})
        except Exception as e:
            # Handle any exceptions
            db.session.rollback()
            error_response = {'status': 'error', 'message': str(e)}
            return jsonify(error_response), 500
    elif request.method == 'DELETE':
        # Delete rules
        try:
            data = request.get_json()
            rule_ids = data.get('rule_ids')

            if not rule_ids:
                return jsonify({'status': 'error', 'message': 'Rule IDs not provided'}), 400

            # Delete rules based on the provided rule IDs
            for rule_id in rule_ids:
                rule = Rule.query.get(rule_id)
                if rule:
                    db.session.delete(rule)
                else:
                    return jsonify({'status': 'error', 'message': f'Rule with ID {rule_id} not found'}), 404
            
            db.session.commit()

            return jsonify({'status': 'success', 'message': 'Rules deleted successfully'})
        except Exception as e:
            # Handle any exceptions
            db.session.rollback()
            error_response = {'status': 'error', 'message': str(e)}
            return jsonify(error_response), 500
        
# Company Get

@main_bp.route('/getCompanies', methods=['GET'])
def get_companies():
    try:
        # Query the Company table to fetch all companies
        companies = Company.query.all()
 
        # Serialize the company data into JSON format
        companies_data = [{'id': company.id, 'company_name': company.company_name, 'company_details': company.company_details} for company in companies]
 
        # Return the company data as the response
        return jsonify({'status': 'success', 'companies': companies_data})
    except Exception as e:
        # Handle any exceptions
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response), 500


@main_bp.route('/editCompany', methods=['POST', 'DELETE'])
def manage_company():
    if request.method == 'POST':
        # Edit or Add new company
        try:
            data = request.get_json()
            company_name = data.get('company_name')
            company_details = data.get('company_details')

            if not company_name or not company_details:
                return jsonify({'status': 'error', 'message': 'Company name or details not provided'}), 400

            # Query the Company table to find if the company already exists
            existing_company = Company.query.filter_by(company_name=company_name).first()

            if existing_company:
                # Update existing company details
                existing_company.company_details = company_details
                db.session.commit()
                return jsonify({'status': 'success', 'message': 'Company details updated successfully'})
            else:
                # Create a new Company object and add it to the database
                new_company = Company(company_name=company_name, company_details=company_details)
                db.session.add(new_company)
                db.session.commit()
                return jsonify({'status': 'success', 'message': 'New company added successfully'})
        except Exception as e:
            # Handle any exceptions
            db.session.rollback()
            error_response = {'status': 'error', 'message': str(e)}
            return jsonify(error_response), 500
    
    elif request.method == 'DELETE':
        # Delete company
        try:
            data = request.get_json()
            company_name = data.get('company_name')

            if not company_name:
                return jsonify({'status': 'error', 'message': 'Company name not provided'}), 400

            # Query the Company table to find the company to delete
            company = Company.query.filter_by(company_name=company_name).first()
            if company:
                db.session.delete(company)
                db.session.commit()
                return jsonify({'status': 'success', 'message': 'Company deleted successfully'})
            else:
                return jsonify({'status': 'error', 'message': f'Company with name {company_name} not found'}), 404
        except Exception as e:
            # Handle any exceptions
            db.session.rollback()
            error_response = {'status': 'error', 'message': str(e)}
            return jsonify(error_response), 500

        
# Client Get

@main_bp.route('/getClients', methods=['GET'])
def get_clients():
    try:
        # Query the Client table to fetch all clients
        clients = Client.query.all()

        # Serialize the clients data into JSON format
        clients_data = [{'id': client.id, 'client_name': client.client_name, 'client_data': client.client_data} for client in clients]

        # Return the clients data as the response
        return jsonify({'status': 'success', 'clients': clients_data})
    except Exception as e:
        # Handle any exceptions
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response), 500

@main_bp.route('/editClients', methods=['POST', 'DELETE'])
def manage_clients():
    if request.method == 'POST':
        # Add a new client
        try:
            data = request.get_json()
            client_name = data.get('client_name')
            client_data = data.get('client_data')
 
            if not client_name or not client_data:
                return jsonify({'status': 'error', 'message': 'Client name or data not provided'}), 400
 
            # Create a new Client object and add it to the database
            new_client = Client(client_name=client_name, client_data=client_data)
            db.session.add(new_client)
            db.session.commit()
 
            return jsonify({'status': 'success', 'message': 'Client added successfully'})
        except Exception as e:
            # Handle any exceptions
            db.session.rollback()
            error_response = {'status': 'error', 'message': str(e)}
            return jsonify(error_response), 500
    elif request.method == 'DELETE':
        # Delete a client
        try:
            data = request.get_json()
            client_id = data.get('client_id')
 
            if not client_id:
                return jsonify({'status': 'error', 'message': 'Client ID not provided'}), 400
 
            # Query the database to find the client by ID and delete it
            client = Client.query.get(client_id)
            if client:
                db.session.delete(client)
                db.session.commit()
                return jsonify({'status': 'success', 'message': 'Client deleted successfully'})
            else:
                return jsonify({'status': 'error', 'message': 'Client not found'}), 404
        except Exception as e:
            # Handle any exceptions
            db.session.rollback()
            error_response = {'status': 'error', 'message': str(e)}
            return jsonify(error_response), 500
        
@main_bp.route('/getRecruiters', methods=['GET'])
def get_recruiters():
    try:
        # Query the Recruiter table to fetch all recruiters
        recruiters = Recruiter.query.all()
 
        # Serialize the recruiter data into JSON format
        recruiters_data = [{
            'id': recruiter.id,
            'first_name': recruiter.first_name,
            'last_name': recruiter.last_name,
            'email': recruiter.email,
            'phone': recruiter.phone,
            'calendly_link': recruiter.calendly_link,
            'years_at_aptask': recruiter.years_at_aptask,
            'years_of_experience': recruiter.years_of_experience,
            'hometown_city': recruiter.hometown_city,
            'hometown_state': recruiter.hometown_state,
            'hometown_country': recruiter.hometown_country,
            'current_city': recruiter.current_city,
            'current_state': recruiter.current_state,
            'current_country': recruiter.current_country,
            'languages_spoken': recruiter.languages_spoken,
            'countries_traveled': recruiter.countries_traveled,
            'linkedin_url': recruiter.linkedin_url,
            'facebook_id': recruiter.facebook_id,
            'instagram_id': recruiter.instagram_id,
            'twitter_id': recruiter.twitter_id,
            'hobbies': recruiter.hobbies,
            'education': recruiter.education,
            'gender': recruiter.gender  # Add gender to the response
        } for recruiter in recruiters]
 
        # Return the recruiter data as the response
        return jsonify({'status': 'success', 'recruiters': recruiters_data})
    except Exception as e:
        # Handle any exceptions
        error_response = {'status': 'error', 'response': str(e)}
        return jsonify(error_response), 500
    

@main_bp.route('/editRecruiter', methods=['POST', 'DELETE'])
def manage_recruiter():
    if request.method == 'POST':
        # Add a new recruiter
        try:
            data = request.get_json()
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            phone = data.get('phone')
            calendly_link = data.get('calendly_link')
            years_at_aptask = data.get('years_at_aptask')
            years_of_experience = data.get('years_of_experience')
            hometown_city = data.get('hometown_city')
            hometown_state = data.get('hometown_state')
            hometown_country = data.get('hometown_country')
            current_city = data.get('current_city')
            current_state = data.get('current_state')
            current_country = data.get('current_country')
            languages_spoken = data.get('languages_spoken')
            countries_traveled = data.get('countries_traveled')
            linkedin_url = data.get('linkedin_url')
            facebook_id = data.get('facebook_id')
            instagram_id = data.get('instagram_id')
            twitter_id = data.get('twitter_id')
            hobbies = data.get('hobbies')
            education = data.get('education')
            gender = data.get('gender')  # Added gender field

            # Create a new Recruiter object and add it to the database
            new_recruiter = Recruiter(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                calendly_link=calendly_link,
                years_at_aptask=years_at_aptask,
                years_of_experience=years_of_experience,
                hometown_city=hometown_city,
                hometown_state=hometown_state,
                hometown_country=hometown_country,
                current_city=current_city,
                current_state=current_state,
                current_country=current_country,
                languages_spoken=languages_spoken,
                countries_traveled=countries_traveled,
                linkedin_url=linkedin_url,
                facebook_id=facebook_id,
                instagram_id=instagram_id,
                twitter_id=twitter_id,
                hobbies=hobbies,
                education=education,
                gender=gender  # Added gender field
            )
            db.session.add(new_recruiter)
            db.session.commit()

            return jsonify({'status': 'success', 'message': 'Recruiter added successfully'})
        except Exception as e:
            # Handle any exceptions
            db.session.rollback()
            error_response = {'status': 'error', 'message': str(e)}
            return jsonify(error_response), 500
    
    elif request.method == 'DELETE':
        # Delete a recruiter
        try:
            data = request.get_json()
            recruiter_id = data.get('recruiter_id')

            if not recruiter_id:
                return jsonify({'status': 'error', 'message': 'Recruiter ID not provided'}), 400

            # Query the database to find the recruiter by ID and delete it
            recruiter = Recruiter.query.get(recruiter_id)
            if recruiter:
                db.session.delete(recruiter)
                db.session.commit()
                return jsonify({'status': 'success', 'message': 'Recruiter deleted successfully'})
            else:
                return jsonify({'status': 'error', 'message': 'Recruiter not found'}), 404
        except Exception as e:
            # Handle any exceptions
            db.session.rollback()
            error_response = {'status': 'error', 'message': str(e)}
            return jsonify(error_response), 500