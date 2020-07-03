def explicit(s, dt, n):
    if n == 0:
        return s
    else:
        return explicit(s, dt, n - 1) * (1 - 10 * dt)


def implicit(s, dt, n):
    if n == 0:
        return float(s)
    else:
        return implicit(s, dt, n - 1) / (1 + 10 * dt)


def print_schemes(s, dt, n):
    print("explicit: %.5f" %explicit(s, dt, n))
    print("implicit: %.5f" %implicit(s, dt, n))


s0 = 1
t0 = 0
delta_ts = [0.05, 0.1, 0.2, 0.25]

for delta_t in delta_ts:
    print("delta is %.2f" %delta_t)
    print_schemes(s0,delta_t,4)

