import business_objects


def main():
	
	#test_board = business_objects.Board("Karantin", ["Todo", "In Work", "Done"])
	#print(test_board.title)
	#print(test_board.columns)


	estimation_task1 = business_objects.Estimation()
	estimation_task1.set_h("1h")
	estimation_task2 = business_objects.Estimation()
	estimation_task2.set_h("3h")

	a = estimation_task1 + estimation_task2
	print(a.get_h())

	a.set_h("11h")
	print(a.get_h())
	print("Good")

main()			