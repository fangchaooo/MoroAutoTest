*** settings ***
Documentation       Example test case for ewayos CWheelGotoPosition using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             /home/moro/EwayTest/Test.py


*** variables ***
${Job_start}=           CArmMoveGripperCmd iCmd;                           \n
...                     iCmd.m_unCmdCode = SysCom_ID_LCmd_GripperMove;     \n
...                     iCmd.m_nLStatus = 50;                              \n
...                     iCmd.m_nRStatus = 50;                              \n
...                     SendArmMoveGripper (&iCmd);                        \n


*** Test Cases ***
CWheelGotoPositon
    Sleep                    20s
    Add Limb
    Add job start code       ${Job_start}
    Run                      True
    Sleep                    2 minutes
    Result should be         x=1 y=2 theta=0.3
