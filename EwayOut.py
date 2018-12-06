import re


class Result:
    def __init__(self):
        self.wheel_data = {
            "X": [],
            "Y": [],
            "Z": [],
            "RX": [],
            "RY": [],
            "RZ": [],
        }
        self.arm_data = {
            "0": [],
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [],
            "9": [],
            "10": [],
            "11": [],
            "12": [],
            "13": [],
            "14": [],
        }
        self.head_data = {
            "RY": [],
            "RZ": [],
        }
        self.path = '/home/moro/MoroPosition'

    def write_data(self, data, one_data):
        if one_data == 'wheel_data':
            for i in data:
                self.wheel_data["X"].append(i[0])
                self.wheel_data["Y"].append(i[1])
                self.wheel_data["Z"].append(i[2])
                self.wheel_data["RX"].append(i[3])
                self.wheel_data["RY"].append(i[4])
                self.wheel_data["RZ"].append(i[5])
        elif one_data == 'head_data':
            for head_data in data:
                if head_data[0] == '0':
                    self.head_data['RZ'].append(head_data[1])
                if head_data[0] == '1':
                    self.head_data['RY'].append(head_data[1])

        else:
            for i, j in data:
                self.arm_data[i].append(j)

    def find_data(self):
        try:
            f = open(self.path, 'r+')
        except FileNotFoundError:
            raise FileNotFoundError("No Robot Pos File")
        s = f.read()
        re_moro = re.compile(r'MORO X=(.+) Y=(.+) Z=(.+) RX=(.+) RY=(.+) RZ=(.+)')
        re_head = re.compile(r'Head ID=(.+) Angle=(.+)')
        re_arm = re.compile(r'Arm ID=(.+) Angle=(.+)')
        read_pos_arm = re_arm.findall(s)
        read_pos_wheel = re_moro.findall(s)
        read_pos_head = re_head.findall(s)
        self.write_data(read_pos_wheel, 'wheel_data')
        self.write_data(read_pos_head, 'head_data')
        self.write_data(read_pos_arm, 'arm_data')
