class Estimation(object):
	day_2_hour_coef = 8
	week_2_hour_coef = 40
	month_2_hour_coef = 160


	def __init__(self, m, w, d, h):
		super(Estimation, self).__init__()
		self.m = None
		self.w = None
		self.d = None
		self.h = None
		self.set_m(m)
		self.set_w(w)
		self.set_d(d)
		self.set_h(h)
		self._total_h = self.h + (self.d) * self.day_2_hour_coef + (self.w) * self.week_2_hour_coef + (self.m) * self.month_2_hour_coef


	def __add__(self, additional_estimation):
		result_estimation = Estimation("0m", "0w", "0d", "0h")
		result_estimation._total_h = self._total_h + additional_estimation._total_h
		
		result_estimation.m = result_estimation._total_h // self.month_2_hour_coef
		hours_transfert = result_estimation._total_h % self.month_2_hour_coef
		
		result_estimation.w = hours_transfert // self.week_2_hour_coef
		hours_transfert = hours_transfert % self.week_2_hour_coef

		result_estimation.d = hours_transfert // self.day_2_hour_coef
		hours_transfert = hours_transfert % self.day_2_hour_coef

		result_estimation.h = hours_transfert
		
		return result_estimation


	def get_estimation_value(self):
		estimation_value = self.get_m() + self.get_w() + self.get_d() + self.get_h()
		return estimation_value
	
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
			if (time_base == "h") & (numeric_value > 7):
				raise NameError("The hour value can be greater then 7")
			if (time_base == "d") & (numeric_value > 4):
				raise NameError("The day value can be greater then 4")		
			if (time_base == "w") & (numeric_value > 3):
				raise NameError("The week value can be greater then 3")	
			return numeric_value
		else:
			raise NameError("The input value must be string and have '-" + time_base + "' ending")

	def __universal_get(self, numeric_value, time_base):
		timed_value = str(numeric_value) + time_base
		return timed_value		

	


		