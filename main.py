import re
from manager import Encrypter
from flask import render_template, Flask, redirect, url_for, request, flash
import os
from flask_bootstrap import Bootstrap
import subprocess

####################
encrypter = Encrypter()
#input_message = input('Enter your message: ').upper().strip()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.app_context().push()
Bootstrap(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        input_message = request.form["input"].upper().strip()
        if re.search('[^_/. -]', input_message):  # returns true if any characters other than '_, /, ., - are found in the input.
            encrypter.encrypt_message(input_message)
            if encrypter.error:
                return render_template("index.html", error=', '.join(encrypter.invalid_letters), type='encrypt')
            else:
                return render_template("index.html", type='encrypt', message=encrypter.encrypted_message)
        else:
            encrypter.decrypt_message(input_message)
            if encrypter.error:
                return render_template("index.html", error=', '.join(encrypter.invalid_letters), type='decipher')
            else:
                return render_template("index.html", type='decipher', message=encrypter.decrypted_message)


    return render_template("index.html")

subprocess.run('cmd /c start chrome "http://127.0.0.1:5000"')
if __name__ == '__main__':
    app.run()



