from flask import Flask,request,render_template,redirect
from flask_mysqldb import MySQL

import numpy as np 
from sklearn import datasets, linear_model, metrics 

app = Flask(__name__,template_folder='template')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'trial'

mysql = MySQL(app)

@app.route('/home', methods=['POST'])
def home():
    #res=request.form
    m=0
    res="OK"
    home_gender = request.form['gender']
    home_pcm = request.form['pcm']
    #cur = mysql.connection.cursor()
    #res=cur.execute("""SELECT * FROM user""")
    #cur.close()
    #Regression
    if(home_gender=='male'):
        g=1
    if(home_gender=='female'):
        g=0
    if(home_pcm=='80'):
        m=1
    if(home_pcm=='60'):
        m=0
    if(home_pcm=='40'):
        m=-1
    reg = linear_model.LinearRegression()
    from sklearn.model_selection import train_test_split 
    if(g==1):
        if(m>0 or m==0):
            res="You are recommended Engineering"
        if(m==-1):
            res="You are recommended Arts"
    if(g==0):
        if(m==1):
            res="You are recommended Engineering"
        elif(m==0):
            res="You are recommended Economics"
    if(g==0):
        if(m==-1):
            res="You are recommended Arts"
    
    #create linear regression object 
     
    #fmse=2
    #fmss=1
    #mmse=1
    #mmsf=1
    #fe=2
    #if(
    return res

@app.route('/user_input', methods=['post'])
def user_input():
    #res=request.form
    gender = request.form.get('gender')
    interests = request.form['interests']
    pcm = request.form['pcm']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user(gender,interests,pcm) VALUES (%s,%s,%s)", [gender,interests,pcm])
    mysql.connection.commit()
    cur.close()
    return ("OK")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
