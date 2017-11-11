from flask import Flask, request, render_template, redirect
from data import DuelData
import os
import json
import codecs
from analitics import Analitics
from get_kif import get_kif


app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():

    data = DuelData()
    data.create_graph()
    f = codecs.open("senkei.json", 'r', "utf-8")
    senkei = json.load(f)
    f.close()
    return render_template('index.html', senkei=senkei, data=data.get_data())


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
    data.create_graph()

    analitics = Analitics(data.get_data()).get_analitics()
    t = sorted(analitics.items(), key=lambda x: x[0])
    return render_template('analitics.html', analitics=analitics)

@app.route('/kif', methods=['GET'])

def kif():
    get_kif()
    return redirect("/")

@app.route('/config_user', methods=['GET'])
def config_user():
    return render_template('config_user.html')

@app.route('/config_user', methods=['POST'])
def config_user_edit():
    #print(request.form)
    text = request.form.getlist("user")[0]
    print(text)
    text += "\n" + request.form.getlist("password")[0]
    f = open("user_pass.txt", 'w')
    f.write(text)
    f.close()
    kif()
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
