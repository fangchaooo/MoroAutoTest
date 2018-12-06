*** settings ***
Documentation       Example test case for ewayos ArmGoToAngleSync using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             ../Test.py


*** variables ***
${Job_start}=           CArmGoToAngleSyncCmd iArmAngleSync;                         \n
...                     iArmAngleSync.m_unCmdCode = SysCom_ID_LCmd_ArmAngleSync;    \n
...                     CAngleMoveInfo iInfo;                                       \n
...                     for(euint m = 0; m < MoRoRArmJointTotalNum; m++)            \n
...                     {                                                           \n
...                        iInfo.Clear ();                                          \n
...                        iInfo.m_nServoID = CJointDef::JointID_RArm1 + m;         \n
...                        iInfo.m_fSpeed = 0.5;                                    \n
...                        iInfo.m_fPosition = 0.9;                                 \n
...                        iArmAngleSync.m_viArmAngle.push_back (iInfo);            \n
...                     }                                                           \n
...                     iArmAngleSync.m_dDuration = 5;                              \n
...                     SendArmGoToAngleSync (&iArmAngleSync);

${except_pos_arm} =     0 0 0 0 0 0 0.9 0.9 0.9 0.9 0.9 0.9

*** Test Cases ***
CWheelGotoPositon
    Sleep                    10s
    Add Limb
    Add job start code       ${Job_start}
    Run                      True
    Sleep                    30 seconds
    Arm Should Be            ${except_pos_arm}
