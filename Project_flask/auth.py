from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
import re

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
	return render_template("login.html")

@auth.route('/logout')
def logout():
	return "<p>logout</p>"

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
	if request.method == 'POST':
		email = request.form.get('email')
		firstName = request.form.get('firstName')
		surname = request.form.get('surname')
		pw1 = request.form.get('pw1')
		pw2 = request.form.get('pw2')
		special_characters = re.compile('~!@#$%^&*":')
		if len(email) < 5:
			flash('**Email must be greater than 5 characters')
		elif '@' not in email:
			flash('**Please enter an email in a valid format i.e. name123@hotmail.com')
		elif len(firstName) < 2:
			flash('**First name must be at least 2 characters or more.')
		elif len(pw1) < 8 or special_characters.search('pw1') == False:
			flash('**Password should be at least 8 characters long, including a number and at least 1 special character from: ~!@#$%^&*":')
		elif pw1 != pw2:
			flash('**Please check that the passwords match')
		else:
			new_user = User(email=email, firstName=firstName, surname=surname, password=generate_password_hash(pw1, method='sha256'))
			db.session.add(new_user)
			db.session.commit()
			flash('Account successfully created!')
			return redirect(url_for('views.home'))

	return render_template("Sign_up.html")

@auth.route('/contact')
def Contact():
	return "<p>Contact</p>"

@auth.route('/booknow')
def BookNow():
	return "<p>Book Now</p>"