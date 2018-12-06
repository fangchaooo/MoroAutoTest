*** settings ***
Documentation       Example test case for ewayos CWheelGotoPosition using Gazebo
Test Setup          start simulation and create app
Test Teardown       Close Simulation
Library             ../Test.py


*** variables ***
${Job_start}=         CWheelGoToPositionCmd icmd;\n
...                   icmd.m_fRelativeX = 1;\n
...                   icmd.m_fRelativeY = 2;\n
...                   icmd.m_fRelativeTheta = 0.3;\n
...                   icmd.m_fSpeed = 0.5;\n
...                   SendWheelGoToPosition(&icmd);


*** Test Cases ***
CWheelGotoPositon
    Sleep                    10s
    Add Limb
    Add job start code       ${Job_start}
    Run                      True
    Sleep                    30 seconds
    Result should be         wheel x=1 y=2 theta=0.3
