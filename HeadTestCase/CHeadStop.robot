*** settings ***
Documentation       Example test case for ewayos CHeadMoveStop using Gazebo
Test Setup          Start Simulation and Create App
Test Teardown       Close Simulation
Library             ../Test.py


*** variables ***
${Job_start}=        CHeadMoveSyncCmd icmd;
...                  icmd.m_fRY = 0.6;
...                  icmd.m_fRZ = 0.6;
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
HeadMoveAndStop
    Sleep                    20s
    Add Limb
    Add job start code       ${Job_start}
    Add Head Pos Msg
    Add Head Pos Cmd         ${head_pos_cmd}
    Run                      True
    Sleep                    30 seconds
    Result should be         head RY=0.5 RZ=0.5
