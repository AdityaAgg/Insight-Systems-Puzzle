import datetime
import os

from flask import Flask, render_template, redirect, url_for
from forms import ItemForm
from models import Items
from database import db_session

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        print("Name: %s Quantity: %s Description: %s  \n" %(form.name.data, form.quantity.data, form.description.data))
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
    results_str = ""
    final_item = None
    for result in results:
        results_str += output_item(result)
        final_item = result

    results_str += "<br>"
    results_str += "Item Bought: <br>"
    results_str += output_item(final_item)

    return results_str

def output_item(result):
    return repr(result.name).rjust(15) + repr(result.quantity).rjust(6) + repr(result.description).rjust(30) + str(result.date_added).rjust(20) + "<br>"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
