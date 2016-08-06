# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, request
from app import app
from forms import LoginForm
from app import babel
from config import LANGUAGES
from flask_babel import gettext

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'BerkutSoft' }# -*- coding: utf-8 -*-
    posts = [  # список выдуманных постов
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(gettext('Login requested for OpenID')+'="' + form.openid.data + '",'+ gettext('remember_me')+'=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title=gettext('Sign In'),
                           form=form)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())