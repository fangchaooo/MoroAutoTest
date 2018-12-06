*** settings ***
Documentation       Example test case for ewayos CWheelGotoPosition using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             /home/moro/EwayTest/WheelTest.py


*** variables ***
${Job_start}=           CWheelStraightSpeedCmd iStraightSpeed;\n
...                     iStraightSpeed.m_fSpeed = 0.3;\n
...                     eint nRetCode = SendWheelStraightSpeed (&iStraightSpeed);

*** Test Cases ***
CWheelGotoPositon
    Sleep                    20s
    Add Limb
    Add job start code       ${Job_start}
    Run                      True
    Sleep                    1 minutes 30 seconds
    Result should be         x=1 y=2 theta=0.3
