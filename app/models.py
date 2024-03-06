from app import db

# Define your database models here
# Define the Rules model
class Rule(db.Model):
    __tablename__ = 'rules'
   
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rule_text = db.Column(db.Text, nullable=False)
 
    def __repr__(self):
        return f"<Rule id={self.id}, rule_text={self.rule_text}>"

# Define the Company model   
class Company(db.Model):
    __tablename__ = 'companies'
   
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.Text, nullable=False)
    company_details = db.Column(db.Text, nullable=False)
 
    def __repr__(self):
        return f"<Company id={self.id}, company_name={self.company_name}>"
    
# Define the Client model
class Client(db.Model):
    __tablename__ = 'clients'
   
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_name = db.Column(db.Text, nullable=False)
    client_data = db.Column(db.Text, nullable=False)
 
    def __repr__(self):
        return f"<Client id={self.id}, client_name={self.client_name}, client_data={self.client_data}>"

class Recruiter(db.Model):
    __tablename__ = 'recruiters'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    calendly_link = db.Column(db.String(200), nullable=False)
    years_at_aptask = db.Column(db.Integer)
    years_of_experience = db.Column(db.Integer)
    hometown_city = db.Column(db.String(100))
    hometown_state = db.Column(db.String(100))
    hometown_country = db.Column(db.String(100))
    current_city = db.Column(db.String(100))
    current_state = db.Column(db.String(100))
    current_country = db.Column(db.String(100))
    languages_spoken = db.Column(db.String(200))
    countries_traveled = db.Column(db.String(200))
    linkedin_url = db.Column(db.String(200))
    facebook_id = db.Column(db.String(100))
    instagram_id = db.Column(db.String(100))
    twitter_id = db.Column(db.String(100))
    hobbies = db.Column(db.Text)
    education = db.Column(db.Text)
    gender = db.Column(db.String(10))  # Adding the gender field

    def __repr__(self):
        return f"<Recruiter id={self.id}, firstName={self.first_name}, lastName={self.last_name}, email={self.email}>"