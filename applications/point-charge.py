import numpy as np
from typing import Union


def surfaceIntSphere(r: float) -> float:
    """ Surface integral of 1 over a sphere with radius r """
    return 4.0 * np.pi * r * r`