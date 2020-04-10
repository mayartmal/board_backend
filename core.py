import arithmetic

def main():

	es1 = arithmetic.Estimation("1m", "3w", "1d", "2h")
	es2 = arithmetic.Estimation("2m", "2w", "4d", "7h")
	es_r = es1 + es2

	print(es1.get_estimation_value())
	print(es2.get_estimation_value())
	print(es_r.get_estimation_value())

main()			