
import filterpy.kalman as kf

x, P = kf.predict(x=10., P=3., u=1., Q=2.**2)
print(f'{x:.3f}')

# `x` is the state of the system.
# `P` is the variance of the system.
# `u` is the movement due to the process.
# `Q` is the noise in the process.
# You will need to used named arguments when you call `predict()` because most of the arguments are optional. The third argument to `predict()` is **not** `u`.

x, P = kf.update(x=x, P=P, z=12., R=3.5**2)
print(f'{x:.3f} {P:.3f}')

# `x` is the state of the system.
# `P` is the variance of the system.
# `z` is the measurement.
# `R` is the measurement variance.
