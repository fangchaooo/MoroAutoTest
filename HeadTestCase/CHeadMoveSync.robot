*** settings ***
Documentation       Example test case for ewayos CHeadMoveSync using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             ../Test.py


*** variables ***
${Job_start}=        CHeadMoveSyncCmd icmd;   \n
...                  icmd.m_fRY = -0.3;        \n
...                  icmd.m_fRZ = -0.3;       \n
...                  icmd.m_dDuration = 5;    \n
...                  SendHeadMoveSync(&icmd);


*** Test Cases ***
HeadMoveSync
    Sleep                    20s
    Add Limb
    Add job start code       ${Job_start}
    Run                      True
    Sleep                    30 seconds
    Result should be         head RY=-0.3 RZ=-0.3
