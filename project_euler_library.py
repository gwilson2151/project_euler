def sum_1_to_n_divisible_by(target, n):
    p = target // n
    return n * sum_1_to_n(p)

def sum_1_to_n(p):
    return p * (p + 1) // 2