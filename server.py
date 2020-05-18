from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

print(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")


@ app.route('/thanks')
def thank_you():
    return render_template("thanks.html")


def write_to_csv(data):
    with open("database.csv", mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",",
                                quotechar="'", quoting=csv.QUOTE_MINIMAL)
        # csv_writer.writerow([])
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # email = request.form['email']
            # subject = request.form['subject']
            # message = request.form['message']
            # write_to_file(data)
            write_to_csv(data)
            # print(data)
            return redirect("thanks")
        except:
            return "did not save to database"
    else:
        return "something went wrong!!!"
