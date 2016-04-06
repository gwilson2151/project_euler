import project_euler_library as pe_lib

def n1():
    target = 999
    return pe_lib.sum_divisible_by(target, 3) + pe_lib.sum_divisible_by(target, 5) - pe_lib.sum_divisible_by(target, 15)