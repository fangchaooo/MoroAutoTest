import re
from EwayBaseTest import EwayBotBaseTest


class Test:
    def __init__(self):
        self._baseTest = EwayBotBaseTest()

    def start_simulation_and_create_app(self):
        self._baseTest.start_simulation()
        self._baseTest.create_app()

    def run(self, pos):
        if pos:
            self._baseTest.start_cmd()

    def close_simulation(self):
        self._baseTest.close_simulation()

    def add_limb(self):
        self._baseTest.code_write('INITIALIZE', 'bLimbAuthority = true;')

    def add_feature(self):
        self._baseTest.code_write('INITIALIZE', 'vFeatureList = true;')

    def add_job_start_code(self, job_code):
        self._baseTest.code_write('JOBSTART', job_code)

    def add_robot_pos_msg(self):
        self._baseTest.code_write('ProcRobPos')

    def add_head_pos_msg(self):
        self._baseTest.code_write('ProcHeadPos')

    def add_robot_pos_cmd(self, code):
        self._baseTest.code_write('PROCROBPOS', code)

    def add_head_pos_cmd(self, code):
        self._baseTest.code_write('PROCHEADPOS', code)

    def is_wheel_correct(self, input_wheel_data, get_data_wheel):
        for x, y, theta in input_wheel_data:
            assert get_data_wheel[0]-0.2 <= float(x) <= get_data_wheel[0]+0.2, \
                "x pos error(except {} but in fact {} )".format(float(x), get_data_wheel[0])
            assert get_data_wheel[1]-0.2 <= float(y) <= get_data_wheel[1]+0.2, \
                "y pos error(except {} but in fact {} )".format(float(y), get_data_wheel[1])
            assert get_data_wheel[2]-0.2 <= float(theta) <= get_data_wheel[0]+0.2, \
                "z pos error(except {} but in fact {} )".format(float(theta), get_data_wheel[2])

    def is_head_correct(self, input_data_head, get_data_head):
        for ry, rz in input_data_head:
            assert get_data_head[0]-0.05 <= float(ry) <= get_data_head[0]+0.05, \
                "RY pos error(except {} but in fact {} )".format(float(ry), get_data_head[0])
            assert get_data_head[1]-0.05 <= float(rz) <= get_data_head[1]+0.05, \
                "RY pos error(except {} but in fact {} )".format(float(rz), get_data_head[1])

    def arm_should_be(self, expected):
        get_data_arm = self._baseTest._result("arm")
        input_data_arm = expected.split()
        for i, j in zip(get_data_arm, input_data_arm):
            assert i-0.05 <= float(j) <= i+0.05, \
                "The arm pos error!(except {} but in fact {})".format(j, i)

    def result_should_be(self, expected):
        moro_pos_type = expected.split()
        if moro_pos_type[0] == "head":
            get_data_head = self._baseTest._result("head")
            input_head_data = re.findall(r'RY=(.+) RZ=(.+)', expected)
            print(input_head_data)
        if moro_pos_type[0] == "wheel":
            get_data_wheel = self._baseTest._result("wheel")
            input_wheel_data = re.findall(r'x=(.+) y=(.+) theta=(.+)', expected)
            self.is_wheel_correct(input_wheel_data, get_data_wheel)

    def add_set_timer(self):
        self._baseTest.code_write('SetTimer')


