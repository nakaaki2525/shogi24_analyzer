from flask import Flask, request, render_template, redirect
from data import DuelData
import os
import json
import codecs
from analitics import Analitics
from get_kif import get_kif
from user import Users

app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():

    page = int(request.args.get("page", "1"))

    data = DuelData()
    user= Users()
    page_num = list(range(1, 1+int(len(data.get_data())/100)+1))
    f = codecs.open("senkei.json", 'r', "utf-8")
    senkei = json.load(f)
    f.close()
    return render_template('index.html', senkei=senkei, data=data.get_data(page), page_num=page_num, page=page)


@app.route('/', methods=['POST'])
def edit():
    #print(request.form)
    DuelData().save_data(request.form)
    try:
        DuelData().save_data(request.form)
    except:
        pass

    return index()

@app.route('/analitics', methods=['GET'])

def analitics():

    data = DuelData()
    user= Users()

    analitics = Analitics(data.get_data()).get_analitics()
    t = sorted(analitics.items(), key=lambda x: x[0])
    return render_template('analitics.html', analitics=analitics)

@app.route('/rate', methods=['GET'])
def rate():
    data = DuelData()
    user= Users()
    data.create_graph()
    user_names = []
    for user_name, password in user.get_users().items():
        data.create_user_graph(user_name)
        user_names.append(user_name)
    return render_template('rate.html', user_names=user_names)


@app.route('/kif', methods=['GET'])

def kif():
    get_kif()
    return redirect("/")

@app.route('/config_user', methods=['GET'])
def config_user():
    users = Users().get_users()
    return render_template('config_user.html', users=users)

@app.route('/config_user', methods=['POST'])
def config_user_edit():
    #print(request.form)
    user_name = request.form.getlist("user")[0]
    password = request.form.getlist("password")[0]
    user= Users()
    user.add_user(user_name, password)
    kif()
    return render_template('config_user.html', users=user.get_users())

@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_name = request.form.getlist("user")[0]
    user= Users()
    user.delete_user(user_name)
    kif()
    return render_template('config_user.html', users=user.get_users())

if __name__ == "__main__":
    app.run(debug=True)
