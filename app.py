import flask
import arithmetic
import business

#config
file_name = "db.json"

app = flask.Flask(__name__)


u1 = business.User("Nate")
print(u1.user_name)
u1.save_user_to_db(file_name, u1)


@app.route('/v1', methods = ['POST'])
def create_user():
	s1 = "this_is_answer"
	return s1

#if __name__ == '__main__':
#    app.run()
