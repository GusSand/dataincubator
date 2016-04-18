from flask import Flask

app = Flask(__name__)

@app.route("/api/images/bernietwitter", methods=['GET'])
def bernietwitter():
	app.logger.debug('Entered images_leaderboard. Payload: ' )
	app.logger.debug(request.get_json())


@app.route('/api/images/berniebills')
def berniebills():

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080)
    app.run()
