def sum_divisible_by(target, n):
	p = target // n
	return n * sum_series_from_1(p)

def sum_series_from_1(p):
	return p * (p + 1) // 2