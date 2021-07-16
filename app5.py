from flask import Flask
from flask import redirect, render_template
from flask import request, url_for
import random

app = Flask(__name__)


@app.route('/')
def log():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    iname = request.form['itemname']
    iprice = request.form['itemprice']
    item = iname.split()
    iquantity = request.form['itemquantity']
    if (len(iname) > 0) and (len(iprice) > 0) and (len(iquantity) > 0):
        item_id = item[-2] + str(random.randint(1, 10000))
        list = [iname, iprice, item_id, iquantity]
        return render_template('shoppinglist.html', list=list)
    else:
        return "Error in adding books to your cart" + request.method


if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True)
