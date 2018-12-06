*** settings ***
Documentation       Example test case for ewayos CHeadMove using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             ../Test.py


*** variables ***
${Job_start}=        CHeadMoveCmd icmd; 	\n
...                  icmd.m_fRY = 0.5;		\n
...                  icmd.m_fRYSpeed = 0.5;	\n
...                  icmd.m_fRZ = 0.5;		\n
...                  icmd.m_fRZSpeed = 0.5;	\n
...                  SendHeadMove(&icmd);	


*** Test Cases ***
HeadMove
    Sleep                    20s
    Add Limb
    Add job start code       ${Job_start}
    Run                      True
    Sleep                    30 seconds
    Result should be         head RY=0.5 RZ=0.5
