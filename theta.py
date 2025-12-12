import mpmath as mp

def theta(t):
    t = mp.mpf(t)
    return mp.im(mp.log(mp.gamma(mp.mpf("0.25") + 0.5j*t))) - 0.5*t*mp.log(mp.pi)
