import numpy as np
import math
import matplotlib.pyplot as plt
from EwayJudge import Judge


def show(x, y):
    plt.plot(x, y)
    plt.show()


s = Judge()
show(s.r.wheel_data["X"], s.r.wheel_data["Y"])
print(s.wheel_motion)
print(math.sqrt(s.wheel_motion[0] ** 2 + s.wheel_motion[1] ** 2))
