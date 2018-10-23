from EwayBaseTest import EwayBotBaseTest


class Test():
    def __repr__(self):
        return "A moro wheel test framework!"

    def __init__(self):
        self._baseTest = EwayBotBaseTest()
        self._result = ''

    def start_simulation_and_create_app(self):
        self._baseTest.start_simulation()
        self._baseTest.create_app()

    def run(self, pos):
        if pos:
            self._baseTest.start_cmd()

    def Close_Simulation(self):
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


    def result_should_be(self, expected):
        if self._baseTest._result() != expected:
            raise AssertionError('%s != %s' % (self._result, expected))

    def add_set_timer(self):
        self._baseTest.code_write('SetTimer')
