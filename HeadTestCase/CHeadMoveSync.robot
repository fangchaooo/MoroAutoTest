*** settings ***
Documentation       Example test case for ewayos CWheelGotoPosition using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             /home/moro/EwayTest/Test.py


*** variables ***
${Job_start}=        CHeadMoveSyncCmd icmd;   \n
...                  icmd.m_fRY = 0.5;        \n
...                  icmd.m_fRZ = -0.5;       \n
...                  icmd.m_dDuration = 5;    \n
...                  SendHeadMoveSync(&icmd);


*** Test Cases ***
CWheelGotoPositon
    Sleep                    20s
    Add Limb
    Add job start code       ${Job_start}
    Run                      True
    Sleep                    2 minutes
    Result should be         x=1 y=2 theta=0.3
