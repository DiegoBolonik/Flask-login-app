import os
from flask import Blueprint, Flask, render_template, request, send_file, flash, redirect, url_for 
from . import db
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

main = Blueprint('main', __name__)
#app = Flask(__name__, template_folder='templates')

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

@main.route('/')
def index():
    return render_template('index.html')
    
@main.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return "file has been uploaded"
    return render_template('home.html', form=form)
    

@main.route('/profile')
#@login_required
def profile():
    return render_template('profile.html')
