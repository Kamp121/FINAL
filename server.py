from flask import Flask, render_template, url_for,  request 

import csv

app = Flask(__name__)
print(__name__) 

@app.route("/<username>/<int:post_id>_")
def hello_world(username=None,post_id=None):
    return render_template('index.html',name=username, post_id=post_id)

@app.route('/')
def about():
    return render_template('Home.html')

def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
  
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
   if request.method == 'POST':
       data = request.form.to_dict()
       write_to_csv(data)
       return 'form submitted hooorayyyyy!'

