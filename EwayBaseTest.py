import re
import os
import time
import subprocess


class EwayBotBaseTest():

    def __init__(self, moro='moro1'):
        self._moro = moro
        self.app_name = 'TestFun'
        self.path = ''

    def create_app(self):
        cmd = 'emake -t fapp -n ' + self.app_name + ' -i 127.0.0.1'
        sp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        time.sleep(10)
        self.path = os.getcwd()

    def code_write(self, step, text=None):
        if step == 'INITIALIZE':
            self.insert_to_file(24, text, '.cpp')
        elif step == 'JOBSTART':
            self.insert_to_file(38, text, '.cpp')
        elif step == 'CHECKMSGCODE':
            self.insert_to_file(32, text, '.cpp')
        elif step == 'ProcRobPos':
            proc_robot_pos_init_text = "vFeatureList.push_back(SysCom_ID_LMsg_RobPos);"
            proc_robot_pos_htext = "virtual eint ProcRobPos(edouble dTimeStamp, CBotPosMessage *piRobPos);"
            proc_robot_pos_cpptext = "eint " + self.app_name + "::ProcRobPos(edouble dTimeStamp, CBotPosMessage *piRobPos)\n" \
                                     "{" \
                                     "\n" \
                                     "\n" \
                                     "}"
            self.insert_to_file(19, proc_robot_pos_htext, '.h')
            self.insert_to_file(24,proc_robot_pos_init_text, '.cpp')
            self.append_to_file(proc_robot_pos_cpptext, '.cpp')
        elif step == "PROCROBPOS":
            self.insert_to_file(55, text, '.cpp')
        elif step == "SETIMER":
            self.insert_to_file()

    def insert_to_file(self, new_line, code, file_type):
        path = self.app_name + '/' + self.app_name + file_type
        fp = open(path)
        s = fp.read()
        fp.close()
        a = s.split('\n')
        a.insert(new_line, code)
        s = '\n'.join(a)
        fp =open(path, 'w')
        fp.write(s)
        fp.close()

    def append_to_file(self, code, file_type):
        path = self.app_name + '/' + self.app_name + file_type
        with open(path, 'a+') as f:
            f.write(code)

    def start_simulation(self):
        cmd = 'emake -s ' + self._moro
        sp = subprocess.Popen(cmd, shell=True)
        time.sleep(10)

    def start_cmd(self):
        cmd = 'cd '+self.app_name+' && qmake && make &&'+self.app_name
        print(cmd)
        sp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        time.sleep(10)

    def close_simulation(self):
        os.system('emake -q')
        cmd_pkill_fun = 'pkill '+ self.app_name
        cmd_delete_folder = 'rm -rf ' + self.path + '/' + self.app_name
        os.system(cmd_pkill_fun)
        os.system(cmd_delete_folder)

    def _result(self):
        try:
            """
            ToDo: get robot pos
            """
            return 'x=1 y=2 theta=0.3'
        except SyntaxError:
            raise EwayBotBaseTest('Invalid expression.')
        except ZeroDivisionError:
            raise EwayBotBaseTest('Division by zero.')
