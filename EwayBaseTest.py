import re
import os
import time
import subprocess
from EwayFunFileChange import SdkFileChange as sfc

class EwayBotBaseTest():

    def __init__(self, moro='moro1'):
        self._moro = moro
        self.app_name = 'TestFun'
        self.path = ''
        self.solution_path = ''
        self.file_change = sfc()

    def create_app(self):
        cmd = 'emake -t fapp -n ' + self.app_name + ' -i 127.0.0.1'
        sp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        time.sleep(10)
        self.solution_path = os.getcwd() + '/' +self.app_name
        self.path = self.solution_path + '/' +self.app_name

    def code_write(self, step, text=None):
        if step == 'INITIALIZE':
            self.file_change.insert_line_to_file(self.path+'.cpp', 24, text)
        elif step == 'JOBSTART':
            self.file_change.insert_line_to_file(self.path + '.cpp', 38, text)
        elif step == 'CHECKMSGCODE':
            self.file_change.insert_line_to_file(self.path + '.cpp', 32, text)
        elif step == 'ProcRobPos':
            proc_robot_pos_init_text = "vFeatureList.push_back(SysCom_ID_LMsg_RobPos);"
            proc_robot_pos_htext = "virtual eint ProcRobPos(edouble dTimeStamp, CBotPosMessage *piRobPos);"
            proc_robot_pos_cpptext = "eint " + self.app_name + "::ProcRobPos(edouble dTimeStamp, CBotPosMessage *piRobPos)\n" \
                                     "{" \
                                     "\n" \
                                     "\n" \
                                     "}"
            self.file_change.insert_line_to_file(self.path + '.h', 19, proc_robot_pos_htext)
            self.file_change.insert_line_to_file(self.path + '.cpp', 24, proc_robot_pos_init_text)
            self.file_change.append_to_file(self.path+'.cpp', proc_robot_pos_cpptext)
        elif step == "PROCROBPOS":
            mark = "::ProcRobPos(edouble dTimeStamp, CBotPosMessage *piRobPos)"
            self.file_change.search_insert_line_to_file(self.path+'.cpp', mark, text)
        elif step == "ProcHeadPos":
            proc_head_pos_init_text = "vFeatureList.push_back(SysCom_ID_LMsg_HeadPos);"
            proc_head_pos_htext = "virtual eint ProcHeadPos(edouble dTimeStamp, CHeadPosMessage *piHeadPos);"
            proc_head_pos_cpptext = "eint " + self.app_name + "::ProcHeadPos(edouble dTimeStamp, CHeadPosMessage *piHeadPos)\n" \
                                     "{" \
                                     "\n" \
                                     "\n" \
                                     "}"
            self.file_change.insert_line_to_file(self.path + '.h', 19, proc_head_pos_htext)
            self.file_change.insert_line_to_file(self.path + '.cpp', 24, proc_head_pos_init_text)
            self.file_change.append_to_file(self.path + '.cpp', proc_head_pos_cpptext)
        elif step == "PROCHEADPOS":
            mark = "ProcHeadPos(edouble dTimeStamp, CHeadPosMessage *piHeadPos)"
            self.file_change.search_insert_line_to_file(self.path + '.cpp', mark, text)


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
        cmd_delete_folder = 'rm -rf ' + self.solution_path
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
