import json
import codecs


class User(object):
	def __init__(self, user_name):
		super(User, self).__init__()
		self.user_name = user_name
		

	def save_user_to_db(self, file_name, user):
		with codecs.open(file_name, 'r', 'utf8') as f:
			db = json.load(f)
			result = db['users_list']

		result['users_list'] = {
			'u1': 'zorro'
		}	

		with codecs.open(file_name, 'w', 'utf8') as f:
			dumped = json.dumps(result, indent=2, sort_keys=True)
			f.write(dumped)

		print(result)
		print('ok file')
		