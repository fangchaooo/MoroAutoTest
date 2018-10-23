*** settings ***
Documentation       Example test case for ewayos CWheelGotoPosition using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             /home/moro/EwayTest/WheelTest.py


*** variables ***
${Job_start}=         CWheelGoToPositionCmd icmd;\n
...                   icmd.m_fRelativeX = 3;\n
...                   icmd.m_fRelativeY = 2;\n
...                   icmd.m_fRelativeTheta = 0.3;\n
...                   SendWheelGoToPosition(&icmd);

${robpos_cmd}=        if(piRobPos->m_dRY <=1.05 && piRobPos->m_dRY >=0.95 )\n
...                   {
...                     CWheelBrakeCmd iBrake;\n
...                     iBrake.m_unCmdCode = SysCom_ID_LCmd_WheelBrake;\n
...                     iBrake.m_nBrakeFlag = CWheelBrakeCmd::Wheel_Brake_ON;\n
...                     SendWheelBrake (&iBrake);\n
...                   }



*** Test Cases ***
CWheelGotoPositon
    Sleep                    20s
    Add Limb
    Add job start code       ${Job_start}
    Add Robot Pos Msg
    Add Robot Pos Cmd        ${robpos_cmd}
    Run                      True
    Sleep                    2 minutes 10 seconds
    Result should be         x=1 y=2 theta=0.3
