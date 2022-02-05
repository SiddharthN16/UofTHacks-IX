from flask import Flask, redirect, url_for, render_template, request
from flask_qrcode import QRcode
import uuid

app = Flask(__name__)
QRcode(app)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        firstName = str(request.form.get("f-name")).lower()
        lastName = str(request.form.get("l-name")).lower()
        studentNum = int(request.form.get("num"))
        return render_template("qrcode.html", data={"firstName": firstName, "lastName": lastName, "num": studentNum, "uuid": hash(firstName+lastName)})

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
