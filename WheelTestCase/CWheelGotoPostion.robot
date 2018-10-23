*** settings ***
Documentation       Example test case for ewayos CWheelGotoPosition using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             /home/moro/EwayTest/WheelTest.py


*** variables ***
${Job_start}=         CWheelGoToPositionCmd icmd;\n
...                   icmd.m_fRelativeX = 1;\n
...                   icmd.m_fRelativeY = 2;\n
...                   icmd.m_fRelativeTheta = 0.3;\n
...                   SendWheelGoToPosition(&icmd);


*** Test Cases ***
CWheelGotoPositon
    Sleep                    20s
    Add Limb
    Add job start code       ${Job_start}
    Run                      True
    Sleep                    2 minutes 10 seconds
    Result should be         x=1 y=2 theta=0.3
