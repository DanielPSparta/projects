from flask import Flask, make_response, request, render_template
from random import random         #get random numbers
import jwt
import datetime


SECRET_KEY = "C7E2F9D46E9"
flask_app = Flask(__name__)                         #makes flask server to run under name flask_app

def verify_token(token):
    if token:   #i ftoken exists
        decoded_token = jwt.decode(token, SECRET_KEY, "HS256")
        print(decoded_token)
    #check whether infor in coded token is correct or not
        return True #if inforamtion is correct, otherwise return false
    else:  # else no token so here
        return False


@flask_app.route('/')                               #makes a new page on the server
def index_page():
    print(request.cookies)         #find the cookies sent with the request
    isUserLoggedIn = False
    if 'token' in request.cookies: #if there is a token in cookies return true
        isUserLoggedIn = verify_token(request.cookies['token'])
    if isUserLoggedIn:  #if there is a token go here
        return "welcome back to the website"
    else:  # if no token in cookies go here
        user_id = random()                     #user id is a random number
        print(f"User ID: {user_id}")           # print the user id server side
        resp = make_response("This is the index page of a secure REST API")    #make a response to return to the user
        resp.set_cookie('user_id', str(user_id))        #sets a cookie on the user attached to the response
        return resp

@flask_app.route('/help')
def help_page():
    return "This is the help page"

@flask_app.route('/login')
def login_page():
    #need to render the login.html page
    return render_template('login.html')

def create_token(username, password):
    validity = datetime.datetime.utcnow() + datetime.timedelta(days=15)      #get current date + 15 days
    token = jwt.encode({'user_id': 123154,'username':username, 'expiry': str(validity)}, SECRET_KEY, "HS256")      #user id any number since we don't have a database for users
    #HS256" the hashing algorithm SHA 256
    return token

@flask_app.route('/authenticate', methods = ['POST']) #accept POST methods
def authenticate_users():
    data = request.form   #retreive data from the post from the login page
    username = data['username']       # store username and password from html
    password = data['password']

    #check whether the username and password are correct

    #create token
    user_token = create_token(username,password)
    #make response to resend
    resp = make_response("Logged in successfully")
    #cookie creation
    #resp.set_cookie("loggedIn", "True")

    #token set to a cookie for responce
    resp.set_cookie('token', user_token)
    return resp   #retreive data from the post from the login page

if __name__ == "__main__":
    print("This is a secure REST API Server")
    flask_app.run(debug = True, ssl_context=('cert/cert.pem','cert/key.pem'))   #runs the flask app so create a server debug =True means that it will auto update
