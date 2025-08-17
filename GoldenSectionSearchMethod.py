import math

def golden_search(f, xl, xu, tol, max_itr):
    phi = (math.sqrt(5) - 1) / 2
    for _ in range(max_itr):
        d = phi * (xu - xl)
        x1 = xl + d
        x2 = xu - d
        if f(x1) > f(x2):
            xl = x2
        else:
            xu = x1
        if abs(xu - xl) < tol:
            break
    x_max = (xl + xu) / 2
    return x_max, f(x_max)

f = lambda x: math.sin(x) * (x - 2)**2 + 4
xl = 0
xu = 2
tol = 0.000011
max_itr = 1000

x_max, f_max = golden_search(f, xl, xu, tol, max_itr)
print(f"maximum at x={x_max:.4f}, f(x)={f_max:.4f}")
