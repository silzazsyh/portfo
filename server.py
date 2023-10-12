from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('./index.html')

@app.route("/index.html")
def index():
    return render_template('./index.html')
    
@app.route("/about.html")
def about_me():
    return render_template('./about.html')

@app.route("/components.html")
def components():
    return render_template('./components.html')

@app.route("/contact.html")
def contact_me():
    return render_template('./contact.html')

@app.route("/thankyou.html")
def thank_you():
    return render_template('./thankyou.html')

@app.route("/work.html")
def work():
    return render_template('./work.html')

@app.route("/works.html")
def works():
    return render_template('./works.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n Email: {email}, Subject: {subject}, Message: {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. try again.'
