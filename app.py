import flask

app = flask.Flask(__name__)


@app.route('/v1', methods = ['POST'])
def new_desk():
	s1 = "this_is_answer"
	return s1

if __name__ == '__main__':
    app.run()
