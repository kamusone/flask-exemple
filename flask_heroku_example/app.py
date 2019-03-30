import os
import psycopg2
from flask import Flask, render_template, g
# Flask Packages
from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap 
from flask_uploads import UploadSet,configure_uploads,IMAGES,DATA,ALL
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo 

from werkzeug import secure_filename
import os
import datetime
import time


# EDA Packages
import pandas as pd 
import numpy as np 

# ML Packages
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# ML Packages For Vectorization of Text For Feature Extraction
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')


# def connect_db():
#     return psycopg2.connect(os.environ.get('DATABASE_URL'))


# @app.before_request
# def before_request():
#     g.db_conn = connect_db()


@app.route('/')
def index():
    # cur = g.db_conn.cursor()
    # cur.execute("SELECT * FROM country;")
    # return render_template('index.html', countries=cur.fetchall())
	return ("OK for view")