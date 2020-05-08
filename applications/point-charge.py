import numpy as np
from typing import Union

T = Union[int, float]


def surfaceIntSphere(r: float) -> float:
    """ Surface integral of 1 over a sphere with radius r """
    return 4.0 * np.pi * r * r


def pointChargeElecFluxDensity(q: T, r: T) -> float:
    """ Electric flux density due to point charge. 
    The direction depends on charge 's sign, and along radial """
    return q / surfaceIntSphere(r)
