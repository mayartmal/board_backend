class Board(object):

	def __init__(self):
		super(Board, self).__init__()
		self.title = None
		self.columns = None
		self.created_at = None
		self.created_by = None
		self.last_updated_at = None
		self.last_updated_by = None


		def create_board(self, title, columns):
			self.title = title
			self.columns = columns

		def delete_board(self):
			print("you try to delete board")
			pass

class Card(object):
	def __init__(self):
		super(Card, self).__init__()
		self.title = None
		self.board = None
		self.status = None
		self.description = None
		self.assignee = None
		self.estimation = None


	def create_card(self, title, board, status, descripton, assignee):
		pass	

	def set_estimation(self, estimation):
		self.estimation = estimation
		pass
	
class User(object):
	def __init__(self, arg):
		super(User, self).__init__()
		self.arg = arg
	def get_all_boards():
			pass	

class Estimation(object):
	def __init__(self):
		super(Estimation, self).__init__()
		self.h = None
		self.d = None
		self.w = None
		self.m = None
	
	def __add__(self, additional_estimation):
		result_estimation = Estimation()
		result_estimation.h = self.h + additional_estimation.h
		return result_estimation


	def set_m(self, m):
		self.m = self.__universal_set(m, "m")
	def get_m(self):
		timed_m = self.__universal_get(self.m, "m")
		return timed_m

	def set_w(self, w):
		self.w = self.__universal_set(w, "w")

	def get_w(self):
		timed_w = self.__universal_get(self.w, "w")
		return timed_w

	def set_d(self, d):
		self.d = self.__universal_set(d, "d")
	def get_d(self):
		timed_d = self.__universal_get(self.d, "d")
		return timed_d

	def set_h(self, h):
		self.h = self.__universal_set(h, "h")
	def get_h(self):
		timed_h = self.__universal_get(self.h, "h")
		return timed_h


	def __universal_set(self, time_value, time_base):
		if (str(type(time_value)) == "<class 'str'>") & ((time_value[-1] == time_base)):
			numeric_value = int(time_value[:-1])
			return numeric_value
		else:
			raise NameError("The input value must be string and have '-" + time_base + "' ending")

	def __universal_get(self, numeric_value, time_base):
		timed_value = str(numeric_value) + time_base
		return timed_value		

	


		