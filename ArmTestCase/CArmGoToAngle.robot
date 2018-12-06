*** settings ***
Documentation       Example test case for ewayos CArmGotoAngle using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             ../Test.py


*** variables ***

${Job_start}=           CArmGoToAngleCmd iArmAngle;                           \n
...                     iArmAngle.m_unCmdCode = SysCom_ID_LCmd_ArmAngle;      \n
...                     CAngleMoveInfo iInfo;                                 \n
...                                                                           \n
...                     for(euint m = 0; m < MoRoLArmJointTotalNum; m++)      \n
...                     {                                                     \n
...                        iInfo.Clear ();                                    \n
...                        iInfo.m_nServoID = CJointDef::JointID_LArm1 + m;   \n
...                        iInfo.m_fSpeed = 0.2;                              \n
...                        iInfo.m_fPosition = 0.5;                           \n
...                        iArmAngle.m_viArmAngle.push_back (iInfo);          \n
...                     }                                                     \n
...                     iInfo.Clear ();                                       \n
...                     iInfo.m_nServoID = CJointDef::JointID_Shoulder ;      \n
...                     iInfo.m_fSpeed = 0.03;                                \n
...                     iInfo.m_fPosition = 0.4;                              \n
...                     iArmAngle.m_viArmAngle.push_back (iInfo);             \n
...                     SendArmGoToAngle (&iArmAngle);

${except_pos_arm} =     0.5 0.5 0.5 0.5 0.5 0.5 0 0 0 0 0 0

*** Test Cases ***
ArmGotoAngle
    Sleep                    10s
    Add Limb
    Add job start code       ${Job_start}
    Run                      True
    Sleep                    30 seconds
    Arm Should Be            ${except_pos_arm}
