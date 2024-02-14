from scipy.optimize import least_squares
from scipy.special import gamma

def f_kelvin(x, a, b):
    pass

def f_pow(x, a, b):
    pass

def f_pow2(x, a, b, c):
    pass

def err_pow_weight(params, *args):
    pass

def err_pow(params, *args):
    pass

def err_kelvin(params, *args):
    pass

def fit_pow_weight(x, y, weight, parabolic=True):
    pass

def fit_pow(x, y):
    pass

def fit_kelvin(x, y, N=1):
    pass

def Kelvin_power_cross(a0, b0, a1, b1, t0):
    pass

def MSD_power_fit(ms, t0, fill=0.9, scaler=10, Kelvin=False, ReEval=False, mode='scaler', verbose=False):
    pass

def dynamic_interpolation(x, a, b, IsKelvin=True, eps=1e-4, insert=10.0, verbose=True):
    pass

def MSD_interpolate(ms, fitsin, smoothing=True, Nsmoothing=30, insert=2, factor=3.0, eps=1e-4, verbose=True):
    pass

def J_to_G_Mason(J, N=30, r0=5, w=1.0, logstep=True, omax=0.0, logWeight=True, advanced=True, verbose=False, flip=True):
    pass