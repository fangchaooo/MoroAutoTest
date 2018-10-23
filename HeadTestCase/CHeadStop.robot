*** settings ***
Documentation       Example test case for ewayos CWheelGotoPosition using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             /home/moro/EwayTest/Test.py


*** variables ***
${Job_start}=        CHeadMoveSyncCmd icmd;
...                  icmd.m_fRY = 0.5;
...                  icmd.m_fRZ = -0.5;
...                  icmd.m_dDuration = 5;
...                  SendHeadMoveSync(&icmd);

${head_pos_cmd}=            for(auto i :piHeadPos->m_viHeadJointList)               \n
...                         {                                                       \n
...                             if(i.m_dPosition <= 0.5 && i.m_dPosition>=0.3)      \n
...                             {                                                   \n
...                                CBaseCommand iStop;                              \n
...                                 iStop.m_unCmdCode = SysCom_ID_LCmd_HeadStop;    \n
...                                eint nRetCode = SendHeadStop (&iStop);           \n
...                             }                                                   \n
...                         }                                                       \n
*** Test Cases ***
CWheelGotoPositon
    Sleep                    20s
    Add Limb
    Add job start code       ${Job_start}
    Add Head Pos Msg
    Add Head Pos Cmd         ${head_pos_cmd}
    Run                      True
    Sleep                    2 minutes 10 seconds
    Result should be         x=1 y=2 theta=0.3
