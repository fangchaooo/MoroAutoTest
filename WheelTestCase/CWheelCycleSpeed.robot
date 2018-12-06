*** settings ***
Documentation       Example test case for ewayos CWheelGotoPosition using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             ../Test.py


*** variables ***
${Job_start}=               CWheelCycleSpeedCmd iCycleSpeed;\n
...                         iCycleSpeed.m_fRadius = 0.5;\n
...                         iCycleSpeed.m_fSpeed = 2;\n
...                         SendWheelCycleSpeed (&iCycleSpeed);


*** Test Cases ***
CWheelGotoPositon
    Sleep                    20s
    Add Limb
    Add job start code       ${Job_start}
    Run                      True
    Sleep                    2 minutes 10 seconds
    Result should be         x=1 y=2 theta=0.3
