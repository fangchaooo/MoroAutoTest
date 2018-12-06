from EwayOut import Result


class Judge:
    def __init__(self):
        self.r = Result()
        self.r.find_data()

    @property
    def head_motion(self):
        return [float(self.r.head_data["RY"][-1]), float(self.r.head_data["RZ"][-1])]

    @property
    def arm_motion(self):
        return [float(self.r.arm_data["0"][-1]) - float(self.r.arm_data["0"][0]),
                float(self.r.arm_data["1"][-1]) - float(self.r.arm_data["1"][0]),
                float(self.r.arm_data["2"][-1]) - float(self.r.arm_data["2"][0]),
                float(self.r.arm_data["3"][-1]) - float(self.r.arm_data["3"][0]),
                float(self.r.arm_data["4"][-1]) - float(self.r.arm_data["4"][0]),
                float(self.r.arm_data["5"][-1]) - float(self.r.arm_data["5"][0]),
                float(self.r.arm_data["6"][-1]) - float(self.r.arm_data["6"][0]),
                float(self.r.arm_data["7"][-1]) - float(self.r.arm_data["7"][0]),
                float(self.r.arm_data["8"][-1]) - float(self.r.arm_data["8"][0]),
                float(self.r.arm_data["9"][-1]) - float(self.r.arm_data["9"][0]),
                float(self.r.arm_data["10"][-1]) - float(self.r.arm_data["10"][0]),
                float(self.r.arm_data["11"][-1]) - float(self.r.arm_data["11"][0]),
                float(self.r.arm_data["12"][-1]) - float(self.r.arm_data["12"][0]),
                float(self.r.arm_data["13"][-1]) - float(self.r.arm_data["13"][0]),
                float(self.r.arm_data["14"][-1]) - float(self.r.arm_data["14"][0])]

    @property
    def wheel_motion(self):
        return [float(self.r.wheel_data["X"][-1]) - float(self.r.wheel_data["X"][0]),
                float(self.r.wheel_data["Y"][-1]) - float(self.r.wheel_data["Y"][0]),
                float(self.r.wheel_data["RZ"][-1]) - float(self.r.wheel_data["RZ"][0])]



if __name__ == "__main__":
    a = Judge()
    print(a.arm_motion)
    print(' '.join(float(a.arm_motion)))