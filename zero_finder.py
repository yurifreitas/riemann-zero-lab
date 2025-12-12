import mpmath as mp
from hardy_z import Z

def find_zero(a, b):
    try:
        with mp.workdps(70):
            return mp.findroot(lambda t: Z(t), (a, b))
    except:
        return None
