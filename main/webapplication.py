from flask import Flask, request, json
from flask import render_template
import xml.etree.ElementTree as ET

app = Flask(__name__)
app.debug = True
info = []


@app.route("/")
def home():
    return render_template('index.html')
username = ''
@app.route("/signin", methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    videoid = request.form['videoid']
    # Create a dictionary to store user data
    user_data = {
        'username': username,
        'password': password,
        'videoid': videoid
    }
    # Convert the dictionary to a JSON string
    userdata = json.dumps(user_data)
        # Write the JSON string to a file
    with open('userdata.json', 'w') as file:
        file.write(userdata)
    
    return ''

if __name__ == "__main__":
    app.run()

