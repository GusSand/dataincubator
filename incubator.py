from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route("/api/images/bernietwitter", methods=['GET'])
def bernietwitter():
	app.logger.debug('Entered images_leaderboard. Payload: ' )
	app.logger.debug(request.get_json())


@app.route('/bernie')
def berniebills():
    return render_template('bernie.html')


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080, debug=True)
    app.run()
