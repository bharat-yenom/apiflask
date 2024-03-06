import os

class Config:
    # Set your fallback database URI here
    SQLALCHEMY_DATABASE_URI = os.environ.get('database') or 'postgresql://default:XC71SxrNuAvh@ep-frosty-flower-a4kfm17u.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require'
