import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "postgresql://ziqqrywnwiazam:1f783a88274eacb6f0c66931d04bdc48dc116992a8cf24a63d2ebb03c89c7fa3@ec2-34-233-114-40.compute-1.amazonaws.com:5432/d451t6v7a3ue7s"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')