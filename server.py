import csv

from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route("/")
#username has a default value
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file=database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open('database.csv','a',newline=" ") as csv_data:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]


        csv_writer = csv.writer(csv_data, delimiter=',', quotechar="'",  quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])






@app.route("/submit_form", methods=["POST"])
def submit_form():

    if request.method=="POST":
        try:
            data= request.form.to_dict()
            write_to_csv(data)
        except:
            return 'info was not saved'

        return redirect('thankyou.html')
    else:
        return "something went wrong try again!"