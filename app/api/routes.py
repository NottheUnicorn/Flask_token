from cgi import print_exception
from turtle import color
from flask import Flask
app = Flask(__name__)


from urllib import response
from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Contact, contact_schema, contacts_schema

api = Blueprint('api',__name__, url_prefix='/api')

def create_contact(current_user_token):
    print("comin here")
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    color = request.json['color']
    price = request.json['price']
    user_token = current_user_token.token
    print(make,model,year,color,price)
    print(f'BIG TESTER: {current_user_token.token}')
    
    contact = Contact(make, model, year, color, price, user_token)
    
    db.session.add(contact)
    db.session.commit()
    
    response = contact_schema.dump(contact)
    return jsonify(response)


@api.route('/user_posts', methods = ['POST'])
@token_required
def create_contact(current_user_token):
    print("comin here")
    name = request.json['username']
    email = request.json['email']
    user_token = current_user_token.token
    print(name)
    print(f'BIG TESTER: {current_user_token.token}')
    
    user_posts = Contact(email,name,user_token)
    
    db.session.add(user_posts)
    db.session.commit()
    
    response = contact_schema.dump(user_posts)
    return jsonify(response)