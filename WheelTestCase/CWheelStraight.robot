*** settings ***
Documentation       Example test case for ewayos CWheelGotoPosition using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             /home/moro/EwayTest/Test.py


*** variables ***
${Job_start}=           CWheelStraightCmd iStraight;\n
...                     iStraight.m_fDistance = 1;\n
...                     iStraight.m_fSpeed = 0.5;\n
...                     SendWheelStraight (&iStraight);



*** Test Cases ***
CWheelGotoPositon
    Sleep                    20s
    Add Limb
    Add job start code       ${Job_start}
    Run                      True
    Sleep                    2 minutes
    Result should be         x=1 y=2 theta=0.3
