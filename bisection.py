# bisection method
import numpy as np

def f(x):
    return np.sin(x) - 2*x + 1

def bisection (xl, xu, es, max_itr):
    if f(xl) * f(xu) >= 0:
        print("No sign change, change initial guess value.")
        return None
    
    itr_count = 0
    xm_old = xl
    ea= 100

    print(f"{'iter':>4} {'(xm)':>12} {'f(xm)':>12} {'error %':>12}")

    while ea > es and itr_count < max_itr:
        xm = (xl + xu) / 2
        if itr_count > 0:
            ea = abs((xm - xm_old) / xm) * 100
        xm_old = xm
        f_xm = f(xm)
        f_xl = f(xl)
        print(f"{itr_count:>4} {xm:>12.4f} {f_xm:>12.6f} {ea:>12.6f}")
        if f_xl * f_xm < 0:
            xu = xm
        elif f_xl * f_xm > 0:
            xl = xm
        else:
            ea = 0
        itr_count += 1
    return xm, itr_count

root, count = bisection (xl = 0, xu = 2, es = 0.05, max_itr = 500)

print("root is", root, "after", count, "iterations")
    