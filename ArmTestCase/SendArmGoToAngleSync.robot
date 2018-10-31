*** settings ***
Documentation       Example test case for ewayos CWheelGotoPosition using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             /home/moro/EwayTest/Test.py


*** variables ***
${Job_start}=          CArmGoToAngleCmd iArmAngle;                                  \n
...                    iArmAngle.m_unCmdCode = SysCom_ID_LCmd_ArmAngle;             \n
...                    CAngleMoveInfo iInfo;                                        \n
...                    for(euint m = 0; m < MoRoLArmJointTotalNum; m++)             \n
...                    {                                                            \n
...                       iInfo.Clear ();                                           \n
...                       iInfo.m_nServoID = CJointDef::JointID_LArm1 + m;          \n
...                       iInfo.m_fSpeed = 0.2;                                     \n
...                       iInfo.m_fPosition = 0;                                    \n
...                       iArmAngle.m_viArmAngle.push_back (iInfo);                 \n
...                    }                                                            \n
...                    SendArmGoToAngle (&iArmAngle);



*** Test Cases ***
CWheelGotoPositon
    Sleep                    20s
    Add Limb
    Add job start code       ${Job_start}
    Run                      True
    Sleep                    2 minutes
    Result should be         x=1 y=2 theta=0.3
