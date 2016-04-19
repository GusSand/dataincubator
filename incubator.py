from flask import Flask
from flask import request, render_template

app = Flask(__name__)


@app.route('/hillary')
def hillarybills():
    return render_template('hillary.html')


@app.route('/')
@app.route('/bernie')
def berniebills():
    return render_template('bernie.html')


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080, debug=True)
    app.run()
