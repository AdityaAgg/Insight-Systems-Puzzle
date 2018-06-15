import datetime
import os

from flask import Flask, render_template, redirect, url_for
from forms import ItemForm
from models import Items
from database import db_session
import json

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())

        db_session.add(item)
        db_session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route("/success")
def success():
    results = []
    qry = db_session.query(Items)
    results = qry.all()
    results_obj = []
    for result in results:
        res = json.loads(output_item_json(result))
        results_obj.append(res)
    return json.dumps(results_obj)

def output_item(result):
    return repr(result.name).rjust(15) + repr(result.quantity).rjust(6) + repr(result.description).rjust(30) + str(result.date_added).rjust(20) + "<br>"

def output_item_json(result):
    return"{\"name\":\""+str(result.name) + "\",\"quantity\":" + str(result.quantity) + ",\"description\":\"" + str(result.description) + "\" ,\"date_added\":\""+ str(result.date_added) + "\"}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
