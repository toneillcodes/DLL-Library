# Binary Specification: setupapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\setupapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cd72d3d97ab2fdaf9e9e1939a89bafb9a6ed41264ae0162080a9e7ed9d5b33b7`
* **Total Exported Functions:** 682

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CMP_GetBlockedDriverInfo` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CMP_GetBlockedDriverInfo` |
| 2 | `CMP_GetServerSideDeviceInstallFlags` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CMP_GetServerSideDeviceInstallFlags` |
| 3 | `CMP_Init_Detection` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CMP_Init_Detection` |
| 4 | `CMP_Report_LogOn` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CMP_Report_LogOn` |
| 5 | `CMP_WaitNoPendingInstallEvents` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CMP_WaitNoPendingInstallEvents` |
| 6 | `CMP_WaitServicesAvailable` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CMP_WaitServicesAvailable` |
| 7 | `CM_Add_Driver_PackageW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Add_Driver_PackageW` |
| 8 | `CM_Add_Empty_Log_Conf` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Add_Empty_Log_Conf` |
| 9 | `CM_Add_Empty_Log_Conf_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Add_Empty_Log_Conf_Ex` |
| 10 | `CM_Add_IDA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Add_IDA` |
| 11 | `CM_Add_IDW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Add_IDW` |
| 12 | `CM_Add_ID_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Add_ID_ExA` |
| 13 | `CM_Add_ID_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Add_ID_ExW` |
| 14 | `CM_Add_Range` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Add_Range` |
| 15 | `CM_Add_Res_Des` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Add_Res_Des` |
| 16 | `CM_Add_Res_Des_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Add_Res_Des_Ex` |
| 18 | `CM_Connect_MachineA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Connect_MachineA` |
| 19 | `CM_Connect_MachineW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Connect_MachineW` |
| 20 | `CM_Create_DevNodeA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Create_DevNodeA` |
| 21 | `CM_Create_DevNodeW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Create_DevNodeW` |
| 22 | `CM_Create_DevNode_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Create_DevNode_ExA` |
| 23 | `CM_Create_DevNode_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Create_DevNode_ExW` |
| 24 | `CM_Create_Range_List` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Create_Range_List` |
| 25 | `CM_Delete_Class_Key` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Delete_Class_Key` |
| 26 | `CM_Delete_Class_Key_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Delete_Class_Key_Ex` |
| 27 | `CM_Delete_DevNode_Key` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Delete_DevNode_Key` |
| 28 | `CM_Delete_DevNode_Key_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Delete_DevNode_Key_Ex` |
| 29 | `CM_Delete_Device_Interface_KeyA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Delete_Device_Interface_KeyA` |
| 30 | `CM_Delete_Device_Interface_KeyW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Delete_Device_Interface_KeyW` |
| 31 | `CM_Delete_Device_Interface_Key_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Delete_Device_Interface_Key_ExA` |
| 32 | `CM_Delete_Device_Interface_Key_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Delete_Device_Interface_Key_ExW` |
| 33 | `CM_Delete_Driver_PackageW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Delete_Driver_PackageW` |
| 35 | `CM_Delete_Range` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Delete_Range` |
| 36 | `CM_Detect_Resource_Conflict` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Detect_Resource_Conflict` |
| 37 | `CM_Detect_Resource_Conflict_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Detect_Resource_Conflict_Ex` |
| 38 | `CM_Disable_DevNode` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Disable_DevNode` |
| 39 | `CM_Disable_DevNode_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Disable_DevNode_Ex` |
| 40 | `CM_Disconnect_Machine` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Disconnect_Machine` |
| 41 | `CM_Dup_Range_List` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Dup_Range_List` |
| 43 | `CM_Enable_DevNode` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Enable_DevNode` |
| 44 | `CM_Enable_DevNode_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Enable_DevNode_Ex` |
| 45 | `CM_Enumerate_Classes` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Enumerate_Classes` |
| 46 | `CM_Enumerate_Classes_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Enumerate_Classes_Ex` |
| 47 | `CM_Enumerate_EnumeratorsA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Enumerate_EnumeratorsA` |
| 48 | `CM_Enumerate_EnumeratorsW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Enumerate_EnumeratorsW` |
| 49 | `CM_Enumerate_Enumerators_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Enumerate_Enumerators_ExA` |
| 50 | `CM_Enumerate_Enumerators_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Enumerate_Enumerators_ExW` |
| 51 | `CM_Find_Range` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Find_Range` |
| 52 | `CM_First_Range` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_First_Range` |
| 53 | `CM_Free_Log_Conf` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Free_Log_Conf` |
| 54 | `CM_Free_Log_Conf_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Free_Log_Conf_Ex` |
| 55 | `CM_Free_Log_Conf_Handle` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Free_Log_Conf_Handle` |
| 56 | `CM_Free_Range_List` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Free_Range_List` |
| 57 | `CM_Free_Res_Des` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Free_Res_Des` |
| 58 | `CM_Free_Res_Des_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Free_Res_Des_Ex` |
| 59 | `CM_Free_Res_Des_Handle` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Free_Res_Des_Handle` |
| 60 | `CM_Free_Resource_Conflict_Handle` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Free_Resource_Conflict_Handle` |
| 61 | `CM_Get_Child` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Child` |
| 62 | `CM_Get_Child_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Child_Ex` |
| 63 | `CM_Get_Class_Key_NameA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Class_Key_NameA` |
| 64 | `CM_Get_Class_Key_NameW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Class_Key_NameW` |
| 65 | `CM_Get_Class_Key_Name_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Class_Key_Name_ExA` |
| 66 | `CM_Get_Class_Key_Name_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Class_Key_Name_ExW` |
| 67 | `CM_Get_Class_NameA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Class_NameA` |
| 68 | `CM_Get_Class_NameW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Class_NameW` |
| 69 | `CM_Get_Class_Name_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Class_Name_ExA` |
| 70 | `CM_Get_Class_Name_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Class_Name_ExW` |
| 71 | `CM_Get_Class_Registry_PropertyA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Class_Registry_PropertyA` |
| 72 | `CM_Get_Class_Registry_PropertyW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Class_Registry_PropertyW` |
| 73 | `CM_Get_Depth` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Depth` |
| 74 | `CM_Get_Depth_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Depth_Ex` |
| 75 | `CM_Get_DevNode_Custom_PropertyA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_DevNode_Custom_PropertyA` |
| 76 | `CM_Get_DevNode_Custom_PropertyW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_DevNode_Custom_PropertyW` |
| 77 | `CM_Get_DevNode_Custom_Property_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_DevNode_Custom_Property_ExA` |
| 78 | `CM_Get_DevNode_Custom_Property_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_DevNode_Custom_Property_ExW` |
| 79 | `CM_Get_DevNode_Registry_PropertyA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_DevNode_Registry_PropertyA` |
| 80 | `CM_Get_DevNode_Registry_PropertyW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_DevNode_Registry_PropertyW` |
| 81 | `CM_Get_DevNode_Registry_Property_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_DevNode_Registry_Property_ExA` |
| 82 | `CM_Get_DevNode_Registry_Property_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_DevNode_Registry_Property_ExW` |
| 83 | `CM_Get_DevNode_Status` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_DevNode_Status` |
| 84 | `CM_Get_DevNode_Status_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_DevNode_Status_Ex` |
| 85 | `CM_Get_Device_IDA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_IDA` |
| 86 | `CM_Get_Device_IDW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_IDW` |
| 87 | `CM_Get_Device_ID_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_ID_ExA` |
| 88 | `CM_Get_Device_ID_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_ID_ExW` |
| 89 | `CM_Get_Device_ID_ListA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_ID_ListA` |
| 90 | `CM_Get_Device_ID_ListW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_ID_ListW` |
| 91 | `CM_Get_Device_ID_List_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_ID_List_ExA` |
| 92 | `CM_Get_Device_ID_List_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_ID_List_ExW` |
| 93 | `CM_Get_Device_ID_List_SizeA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_ID_List_SizeA` |
| 94 | `CM_Get_Device_ID_List_SizeW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_ID_List_SizeW` |
| 95 | `CM_Get_Device_ID_List_Size_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_ID_List_Size_ExA` |
| 96 | `CM_Get_Device_ID_List_Size_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_ID_List_Size_ExW` |
| 97 | `CM_Get_Device_ID_Size` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_ID_Size` |
| 98 | `CM_Get_Device_ID_Size_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_ID_Size_Ex` |
| 99 | `CM_Get_Device_Interface_AliasA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_Interface_AliasA` |
| 100 | `CM_Get_Device_Interface_AliasW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_Interface_AliasW` |
| 101 | `CM_Get_Device_Interface_Alias_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_Interface_Alias_ExA` |
| 102 | `CM_Get_Device_Interface_Alias_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_Interface_Alias_ExW` |
| 103 | `CM_Get_Device_Interface_ListA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_Interface_ListA` |
| 104 | `CM_Get_Device_Interface_ListW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_Interface_ListW` |
| 105 | `CM_Get_Device_Interface_List_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_Interface_List_ExA` |
| 106 | `CM_Get_Device_Interface_List_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_Interface_List_ExW` |
| 107 | `CM_Get_Device_Interface_List_SizeA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_Interface_List_SizeA` |
| 108 | `CM_Get_Device_Interface_List_SizeW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_Interface_List_SizeW` |
| 109 | `CM_Get_Device_Interface_List_Size_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_Interface_List_Size_ExA` |
| 110 | `CM_Get_Device_Interface_List_Size_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Device_Interface_List_Size_ExW` |
| 111 | `CM_Get_First_Log_Conf` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_First_Log_Conf` |
| 112 | `CM_Get_First_Log_Conf_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_First_Log_Conf_Ex` |
| 113 | `CM_Get_Global_State` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Global_State` |
| 114 | `CM_Get_Global_State_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Global_State_Ex` |
| 115 | `CM_Get_HW_Prof_FlagsA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_HW_Prof_FlagsA` |
| 116 | `CM_Get_HW_Prof_FlagsW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_HW_Prof_FlagsW` |
| 117 | `CM_Get_HW_Prof_Flags_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_HW_Prof_Flags_ExA` |
| 118 | `CM_Get_HW_Prof_Flags_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_HW_Prof_Flags_ExW` |
| 119 | `CM_Get_Hardware_Profile_InfoA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Hardware_Profile_InfoA` |
| 120 | `CM_Get_Hardware_Profile_InfoW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Hardware_Profile_InfoW` |
| 121 | `CM_Get_Hardware_Profile_Info_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Hardware_Profile_Info_ExA` |
| 122 | `CM_Get_Hardware_Profile_Info_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Hardware_Profile_Info_ExW` |
| 123 | `CM_Get_Log_Conf_Priority` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Log_Conf_Priority` |
| 124 | `CM_Get_Log_Conf_Priority_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Log_Conf_Priority_Ex` |
| 125 | `CM_Get_Next_Log_Conf` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Next_Log_Conf` |
| 126 | `CM_Get_Next_Log_Conf_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Next_Log_Conf_Ex` |
| 127 | `CM_Get_Next_Res_Des` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Next_Res_Des` |
| 128 | `CM_Get_Next_Res_Des_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Next_Res_Des_Ex` |
| 129 | `CM_Get_Parent` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Parent` |
| 130 | `CM_Get_Parent_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Parent_Ex` |
| 131 | `CM_Get_Res_Des_Data` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Res_Des_Data` |
| 132 | `CM_Get_Res_Des_Data_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Res_Des_Data_Ex` |
| 133 | `CM_Get_Res_Des_Data_Size` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Res_Des_Data_Size` |
| 134 | `CM_Get_Res_Des_Data_Size_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Res_Des_Data_Size_Ex` |
| 135 | `CM_Get_Resource_Conflict_Count` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Resource_Conflict_Count` |
| 136 | `CM_Get_Resource_Conflict_DetailsA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Resource_Conflict_DetailsA` |
| 137 | `CM_Get_Resource_Conflict_DetailsW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Resource_Conflict_DetailsW` |
| 138 | `CM_Get_Sibling` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Sibling` |
| 139 | `CM_Get_Sibling_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Sibling_Ex` |
| 140 | `CM_Get_Version` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Version` |
| 141 | `CM_Get_Version_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Get_Version_Ex` |
| 143 | `CM_Install_DevNodeW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Install_DevNodeW` |
| 144 | `CM_Install_DevNode_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Install_DevNode_ExW` |
| 145 | `CM_Intersect_Range_List` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Intersect_Range_List` |
| 146 | `CM_Invert_Range_List` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Invert_Range_List` |
| 147 | `CM_Is_Dock_Station_Present` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Is_Dock_Station_Present` |
| 148 | `CM_Is_Dock_Station_Present_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Is_Dock_Station_Present_Ex` |
| 149 | `CM_Is_Version_Available` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Is_Version_Available` |
| 150 | `CM_Is_Version_Available_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Is_Version_Available_Ex` |
| 151 | `CM_Locate_DevNodeA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Locate_DevNodeA` |
| 152 | `CM_Locate_DevNodeW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Locate_DevNodeW` |
| 153 | `CM_Locate_DevNode_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Locate_DevNode_ExA` |
| 154 | `CM_Locate_DevNode_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Locate_DevNode_ExW` |
| 155 | `CM_Merge_Range_List` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Merge_Range_List` |
| 156 | `CM_Modify_Res_Des` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Modify_Res_Des` |
| 157 | `CM_Modify_Res_Des_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Modify_Res_Des_Ex` |
| 158 | `CM_Move_DevNode` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Move_DevNode` |
| 159 | `CM_Move_DevNode_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Move_DevNode_Ex` |
| 160 | `CM_Next_Range` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Next_Range` |
| 161 | `CM_Open_Class_KeyA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Open_Class_KeyA` |
| 162 | `CM_Open_Class_KeyW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Open_Class_KeyW` |
| 163 | `CM_Open_Class_Key_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Open_Class_Key_ExA` |
| 164 | `CM_Open_Class_Key_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Open_Class_Key_ExW` |
| 165 | `CM_Open_DevNode_Key` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Open_DevNode_Key` |
| 166 | `CM_Open_DevNode_Key_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Open_DevNode_Key_Ex` |
| 167 | `CM_Open_Device_Interface_KeyA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Open_Device_Interface_KeyA` |
| 168 | `CM_Open_Device_Interface_KeyW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Open_Device_Interface_KeyW` |
| 169 | `CM_Open_Device_Interface_Key_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Open_Device_Interface_Key_ExA` |
| 170 | `CM_Open_Device_Interface_Key_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Open_Device_Interface_Key_ExW` |
| 171 | `CM_Query_And_Remove_SubTreeA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Query_And_Remove_SubTreeA` |
| 172 | `CM_Query_And_Remove_SubTreeW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Query_And_Remove_SubTreeW` |
| 173 | `CM_Query_And_Remove_SubTree_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Query_And_Remove_SubTree_ExA` |
| 174 | `CM_Query_And_Remove_SubTree_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Query_And_Remove_SubTree_ExW` |
| 175 | `CM_Query_Arbitrator_Free_Data` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Query_Arbitrator_Free_Data` |
| 176 | `CM_Query_Arbitrator_Free_Data_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Query_Arbitrator_Free_Data_Ex` |
| 177 | `CM_Query_Arbitrator_Free_Size` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Query_Arbitrator_Free_Size` |
| 178 | `CM_Query_Arbitrator_Free_Size_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Query_Arbitrator_Free_Size_Ex` |
| 179 | `CM_Query_Remove_SubTree` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Query_Remove_SubTree` |
| 180 | `CM_Query_Remove_SubTree_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Query_Remove_SubTree_Ex` |
| 181 | `CM_Query_Resource_Conflict_List` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Query_Resource_Conflict_List` |
| 182 | `CM_Reenumerate_DevNode` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Reenumerate_DevNode` |
| 183 | `CM_Reenumerate_DevNode_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Reenumerate_DevNode_Ex` |
| 184 | `CM_Register_Device_Driver` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Register_Device_Driver` |
| 185 | `CM_Register_Device_Driver_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Register_Device_Driver_Ex` |
| 186 | `CM_Register_Device_InterfaceA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Register_Device_InterfaceA` |
| 187 | `CM_Register_Device_InterfaceW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Register_Device_InterfaceW` |
| 188 | `CM_Register_Device_Interface_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Register_Device_Interface_ExA` |
| 189 | `CM_Register_Device_Interface_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Register_Device_Interface_ExW` |
| 190 | `CM_Remove_SubTree` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Remove_SubTree` |
| 191 | `CM_Remove_SubTree_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Remove_SubTree_Ex` |
| 192 | `CM_Request_Device_EjectA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Request_Device_EjectA` |
| 193 | `CM_Request_Device_EjectW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Request_Device_EjectW` |
| 194 | `CM_Request_Device_Eject_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Request_Device_Eject_ExA` |
| 195 | `CM_Request_Device_Eject_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Request_Device_Eject_ExW` |
| 196 | `CM_Request_Eject_PC` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Request_Eject_PC` |
| 197 | `CM_Request_Eject_PC_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Request_Eject_PC_Ex` |
| 200 | `CM_Run_Detection` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Run_Detection` |
| 201 | `CM_Run_Detection_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Run_Detection_Ex` |
| 203 | `CM_Set_Class_Registry_PropertyA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_Class_Registry_PropertyA` |
| 204 | `CM_Set_Class_Registry_PropertyW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_Class_Registry_PropertyW` |
| 205 | `CM_Set_DevNode_Problem` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_DevNode_Problem` |
| 206 | `CM_Set_DevNode_Problem_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_DevNode_Problem_Ex` |
| 207 | `CM_Set_DevNode_Registry_PropertyA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_DevNode_Registry_PropertyA` |
| 208 | `CM_Set_DevNode_Registry_PropertyW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_DevNode_Registry_PropertyW` |
| 209 | `CM_Set_DevNode_Registry_Property_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_DevNode_Registry_Property_ExA` |
| 210 | `CM_Set_DevNode_Registry_Property_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_DevNode_Registry_Property_ExW` |
| 211 | `CM_Set_HW_Prof` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_HW_Prof` |
| 212 | `CM_Set_HW_Prof_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_HW_Prof_Ex` |
| 213 | `CM_Set_HW_Prof_FlagsA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_HW_Prof_FlagsA` |
| 214 | `CM_Set_HW_Prof_FlagsW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_HW_Prof_FlagsW` |
| 215 | `CM_Set_HW_Prof_Flags_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_HW_Prof_Flags_ExA` |
| 216 | `CM_Set_HW_Prof_Flags_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Set_HW_Prof_Flags_ExW` |
| 217 | `CM_Setup_DevNode` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Setup_DevNode` |
| 218 | `CM_Setup_DevNode_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Setup_DevNode_Ex` |
| 219 | `CM_Test_Range_Available` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Test_Range_Available` |
| 220 | `CM_Uninstall_DevNode` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Uninstall_DevNode` |
| 221 | `CM_Uninstall_DevNode_Ex` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Uninstall_DevNode_Ex` |
| 222 | `CM_Unregister_Device_InterfaceA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Unregister_Device_InterfaceA` |
| 223 | `CM_Unregister_Device_InterfaceW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Unregister_Device_InterfaceW` |
| 224 | `CM_Unregister_Device_Interface_ExA` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Unregister_Device_Interface_ExA` |
| 225 | `CM_Unregister_Device_Interface_ExW` | `0x0` | - | Forwarded | Forwarded to: `cfgmgr32.CM_Unregister_Device_Interface_ExW` |
| 493 | `SetupGetThreadLogToken` | `0x0` | - | Forwarded | Forwarded to: `devrtl.DevRtlGetThreadLogToken` |
| 587 | `SetupSetThreadLogToken` | `0x0` | - | Forwarded | Forwarded to: `devrtl.DevRtlSetThreadLogToken` |
| 595 | `SetupWriteTextLog` | `0x0` | - | Forwarded | Forwarded to: `devrtl.DevRtlWriteTextLog` |
| 596 | `SetupWriteTextLogError` | `0x0` | - | Forwarded | Forwarded to: `devrtl.DevRtlWriteTextLogError` |
| 607 | `pSetupCloseTextLogSection` | `0x0` | - | Forwarded | Forwarded to: `devrtl.DevRtlCloseTextLogSection` |
| 609 | `pSetupCreateTextLogSectionA` | `0x0` | - | Forwarded | Forwarded to: `devrtl.DevRtlCreateTextLogSectionA` |
| 610 | `pSetupCreateTextLogSectionW` | `0x0` | - | Forwarded | Forwarded to: `devrtl.DevRtlCreateTextLogSectionW` |
| 343 | `SetupDiGetClassImageList` | `0x18A0` | 230 | UnwindData |  |
| 289 | `SetupDiBuildClassInfoListExW` | `0x1B40` | 1,028 | UnwindData |  |
| 641 | `pSetupIsBiDiLocalizedSystemEx` | `0x1F50` | 756 | UnwindData |  |
| 345 | `SetupDiGetClassImageListExW` | `0x2250` | 1,967 | UnwindData |  |
| 351 | `SetupDiGetClassPropertyW` | `0x2D00` | 589 | UnwindData |  |
| 672 | `pSetupStringTableLookUpStringEx` | `0x4D80` | 708 | UnwindData |  |
| 620 | `pSetupDuplicateString` | `0x5C70` | 18 | UnwindData |  |
| 453 | `SetupFreeSourceListW` | `0x6DA0` | 243 | UnwindData |  |
| 513 | `SetupIterateCabinetW` | `0x7470` | 204 | UnwindData |  |
| 528 | `SetupPromptForDiskW` | `0x7C30` | 779 | UnwindData |  |
| 439 | `SetupDiSetSelectedDriverW` | `0x8600` | 1,649 | UnwindData |  |
| 662 | `pSetupStringFromGuid` | `0x8C80` | 612 | UnwindData |  |
| 397 | `SetupDiLoadDeviceIcon` | `0x9060` | 333 | UnwindData |  |
| 407 | `SetupDiOpenDeviceInterfaceW` | `0x9610` | 263 | UnwindData |  |
| 363 | `SetupDiGetDeviceInterfaceAlias` | `0x9720` | 343 | UnwindData |  |
| 371 | `SetupDiGetDeviceRegistryPropertyW` | `0x9A00` | 292 | UnwindData |  |
| 364 | `SetupDiGetDeviceInterfaceDetailA` | `0x9B30` | 898 | UnwindData |  |
| 365 | `SetupDiGetDeviceInterfaceDetailW` | `0x9EC0` | 669 | UnwindData |  |
| 369 | `SetupDiGetDevicePropertyW` | `0xA170` | 618 | UnwindData |  |
| 318 | `SetupDiDestroyDeviceInfoList` | `0xA3E0` | 263 | UnwindData |  |
| 322 | `SetupDiEnumDeviceInterfaces` | `0xA4F0` | 391 | UnwindData |  |
| 402 | `SetupDiOpenDevRegKey` | `0xA680` | 428 | UnwindData |  |
| 321 | `SetupDiEnumDeviceInfo` | `0xA840` | 591 | UnwindData |  |
| 617 | `pSetupDiInvalidateHelperModules` | `0xAAA0` | 1,959 | UnwindData |  |
| 370 | `SetupDiGetDeviceRegistryPropertyA` | `0xC130` | 300 | UnwindData |  |
| 338 | `SetupDiGetClassDevsA` | `0xC270` | 386 | UnwindData |  |
| 341 | `SetupDiGetClassDevsW` | `0xC400` | 204 | UnwindData |  |
| 340 | `SetupDiGetClassDevsExW` | `0xC4E0` | 953 | UnwindData |  |
| 305 | `SetupDiCreateDeviceInfoList` | `0xD370` | 156 | UnwindData |  |
| 307 | `SetupDiCreateDeviceInfoListExW` | `0xD420` | 589 | UnwindData |  |
| 628 | `pSetupGetGlobalFlags` | `0xDF30` | 17 | UnwindData |  |
| 594 | `SetupVerifyInfFileW` | `0xEA40` | 2,753 | UnwindData |  |
| 465 | `SetupGetInfDriverStoreLocationW` | `0x106C0` | 903 | UnwindData |  |
| 471 | `SetupGetInfPublishedNameW` | `0x11450` | 793 | UnwindData |  |
| 490 | `SetupGetStringFieldW` | `0x120C0` | 886 | UnwindData |  |
| 625 | `pSetupGetDriverVersion` | `0x12FA0` | 383 | UnwindData |  |
| 608 | `pSetupConcatenatePaths` | `0x17440` | 399 | UnwindData |  |
| 519 | `SetupOpenAppendInfFileW` | `0x1B1C0` | 1,378 | UnwindData |  |
| 520 | `SetupOpenFileQueue` | `0x1B730` | 569 | UnwindData |  |
| 522 | `SetupOpenInfFileW` | `0x1B970` | 823 | UnwindData |  |
| 627 | `pSetupGetFileTitle` | `0x1BCB0` | 19,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 663 | `pSetupStringTableAddString` | `0x20AC0` | 170 | UnwindData |  |
| 479 | `SetupGetLineTextW` | `0x22500` | 884 | UnwindData |  |
| 489 | `SetupGetStringFieldA` | `0x22880` | 514 | UnwindData |  |
| 598 | `UnicodeToMultiByte` | `0x22A90` | 229 | UnwindData |  |
| 676 | `pSetupUnicodeToMultiByte` | `0x22A90` | 229 | UnwindData |  |
| 548 | `SetupQueueCopySectionW` | `0x22B80` | 2,259 | UnwindData |  |
| 626 | `pSetupGetField` | `0x23460` | 313 | UnwindData |  |
| 473 | `SetupGetIntField` | `0x24500` | 199 | UnwindData |  |
| 332 | `SetupDiGetClassDescriptionA` | `0x245D0` | 272 | UnwindData |  |
| 333 | `SetupDiGetClassDescriptionExA` | `0x246F0` | 545 | UnwindData |  |
| 339 | `SetupDiGetClassDevsExA` | `0x24920` | 386 | UnwindData |  |
| 447 | `SetupFindFirstLineA` | `0x24AB0` | 457 | UnwindData |  |
| 403 | `SetupDiOpenDeviceInfoA` | `0x24C80` | 266 | UnwindData |  |
| 294 | `SetupDiClassGuidsFromNameA` | `0x24D90` | 332 | UnwindData |  |
| 605 | `pSetupCaptureAndConvertAnsiArg` | `0x24EF0` | 274 | UnwindData |  |
| 650 | `pSetupMultiByteToUnicode` | `0x25010` | 235 | UnwindData |  |
| 404 | `SetupDiOpenDeviceInfoW` | `0x25110` | 920 | UnwindData |  |
| 443 | `SetupEnumInfSectionsA` | `0x255B0` | 1,169 | UnwindData |  |
| 248 | `PnpIsFilePnpDriver` | `0x25FC0` | 55 | UnwindData |  |
| 290 | `SetupDiBuildDriverInfoList` | `0x29650` | 6,803 | UnwindData |  |
| 263 | `SetupCloseFileQueue` | `0x2B920` | 727 | UnwindData |  |
| 342 | `SetupDiGetClassImageIndex` | `0x2C760` | 404 | UnwindData |  |
| 673 | `pSetupStringTableSetExtraData` | `0x2C900` | 207 | UnwindData |  |
| 384 | `SetupDiGetINFClassW` | `0x2E420` | 1,142 | UnwindData |  |
| 406 | `SetupDiOpenDeviceInterfaceRegKey` | `0x2F160` | 396 | UnwindData |  |
| 668 | `pSetupStringTableGetExtraData` | `0x2F4D0` | 182 | UnwindData |  |
| 648 | `pSetupMalloc` | `0x2FCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 622 | `pSetupFree` | `0x2FCC0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `SetupDiGetDeviceInstanceIdA` | `0x2FD50` | 698 | UnwindData |  |
| 362 | `SetupDiGetDeviceInstanceIdW` | `0x30010` | 380 | UnwindData |  |
| 664 | `pSetupStringTableAddStringEx` | `0x308E0` | 199 | UnwindData |  |
| 457 | `SetupGetFieldCount` | `0x31110` | 396 | UnwindData |  |
| 597 | `SetupWriteTextLogInfLine` | `0x312B0` | 548 | UnwindData |  |
| 315 | `SetupDiDeleteDeviceInterfaceData` | `0x315D0` | 323 | UnwindData |  |
| 367 | `SetupDiGetDeviceInterfacePropertyW` | `0x31970` | 479 | UnwindData |  |
| 358 | `SetupDiGetDeviceInfoListDetailW` | `0x337A0` | 392 | UnwindData |  |
| 515 | `SetupLogErrorW` | `0x341A0` | 127 | UnwindData |  |
| 366 | `SetupDiGetDeviceInterfacePropertyKeys` | `0x34F60` | 427 | UnwindData |  |
| 647 | `pSetupMakeSurePathExists` | `0x35120` | 544 | UnwindData |  |
| 324 | `SetupDiEnumDriverInfoW` | `0x35350` | 531 | UnwindData |  |
| 671 | `pSetupStringTableLookUpString` | `0x35990` | 206 | UnwindData |  |
| 279 | `SetupDefaultQueueCallback` | `0x35FC0` | 928 | UnwindData |  |
| 281 | `SetupDefaultQueueCallbackW` | `0x35FC0` | 928 | UnwindData |  |
| 654 | `pSetupRealloc` | `0x36BC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `SetupFindNextLine` | `0x36BF0` | 157 | UnwindData |  |
| 329 | `SetupDiGetActualSectionToInstallExW` | `0x37090` | 289 | UnwindData |  |
| 335 | `SetupDiGetClassDescriptionW` | `0x371C0` | 272 | UnwindData |  |
| 334 | `SetupDiGetClassDescriptionExW` | `0x372E0` | 295 | UnwindData |  |
| 264 | `SetupCloseInfFile` | `0x37850` | 145 | UnwindData |  |
| 270 | `SetupConfigureWmiFromInfSectionW` | `0x37AA0` | 1,368 | UnwindData |  |
| 301 | `SetupDiClassNameFromGuidW` | `0x38000` | 272 | UnwindData |  |
| 300 | `SetupDiClassNameFromGuidExW` | `0x38120` | 471 | UnwindData |  |
| 296 | `SetupDiClassGuidsFromNameExW` | `0x38420` | 295 | UnwindData |  |
| 393 | `SetupDiInstallDevice` | `0x386C0` | 2,815 | UnwindData |  |
| 624 | `pSetupGetDriverDate` | `0x3AEC0` | 369 | UnwindData |  |
| 434 | `SetupDiSetDeviceRegistryPropertyW` | `0x3B040` | 250 | UnwindData |  |
| 572 | `SetupScanFileQueue` | `0x3B450` | 258 | UnwindData |  |
| 574 | `SetupScanFileQueueW` | `0x3B450` | 258 | UnwindData |  |
| 657 | `pSetupScanFileQueue` | `0x3B560` | 6,061 | UnwindData |  |
| 245 | `PnpEnumDrpFile` | `0x3CE50` | 860 | UnwindData |  |
| 635 | `pSetupGuidFromString` | `0x3DA00` | 97 | UnwindData |  |
| 373 | `SetupDiGetDriverInfoDetailW` | `0x3DA70` | 441 | UnwindData |  |
| 419 | `SetupDiSelectBestCompatDrv` | `0x3DCB0` | 2,320 | UnwindData |  |
| 604 | `pSetupAppendPath` | `0x3E760` | 368 | UnwindData |  |
| 265 | `SetupCloseLog` | `0x3E980` | 183 | UnwindData |  |
| 523 | `SetupOpenLog` | `0x3F930` | 453 | UnwindData |  |
| 330 | `SetupDiGetActualSectionToInstallW` | `0x3FC70` | 289 | UnwindData |  |
| 432 | `SetupDiSetDevicePropertyW` | `0x401D0` | 438 | UnwindData |  |
| 429 | `SetupDiSetDeviceInstallParamsW` | `0x406E0` | 229 | UnwindData |  |
| 481 | `SetupGetMultiSzFieldW` | `0x40DA0` | 816 | UnwindData |  |
| 492 | `SetupGetTargetPathW` | `0x410E0` | 585 | UnwindData |  |
| 399 | `SetupDiOpenClassRegKey` | `0x418F0` | 269 | UnwindData |  |
| 314 | `SetupDiDeleteDeviceInfo` | `0x42290` | 325 | UnwindData |  |
| 428 | `SetupDiSetDeviceInstallParamsA` | `0x423E0` | 296 | UnwindData |  |
| 347 | `SetupDiGetClassInstallParamsW` | `0x425B0` | 347 | UnwindData |  |
| 348 | `SetupDiGetClassPropertyExW` | `0x428D0` | 440 | UnwindData |  |
| 444 | `SetupEnumInfSectionsW` | `0x42B30` | 192 | UnwindData |  |
| 293 | `SetupDiChangeState` | `0x42D90` | 2,946 | UnwindData |  |
| 638 | `pSetupInfIsInbox` | `0x43940` | 199 | UnwindData |  |
| 494 | `SetupInitDefaultQueueCallback` | `0x43A70` | 144 | UnwindData |  |
| 653 | `pSetupQueryMultiSzValueToArray` | `0x43B10` | 752 | UnwindData |  |
| 360 | `SetupDiGetDeviceInstallParamsW` | `0x43FB0` | 328 | UnwindData |  |
| 521 | `SetupOpenInfFileA` | `0x44520` | 391 | UnwindData |  |
| 375 | `SetupDiGetDriverInstallParamsW` | `0x446B0` | 458 | UnwindData |  |
| 469 | `SetupGetInfInformationW` | `0x44B10` | 990 | UnwindData |  |
| 612 | `pSetupDiBuildInfoDataFromStrongName` | `0x45180` | 2,153 | UnwindData |  |
| 368 | `SetupDiGetDevicePropertyKeys` | `0x45CE0` | 427 | UnwindData |  |
| 303 | `SetupDiCreateDevRegKeyW` | `0x45EA0` | 985 | UnwindData |  |
| 387 | `SetupDiGetSelectedDriverW` | `0x47500` | 351 | UnwindData |  |
| 495 | `SetupInitDefaultQueueCallbackEx` | `0x4C390` | 440 | UnwindData |  |
| 448 | `SetupFindFirstLineW` | `0x4C5D0` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `pSetupStringTableStringFromId` | `0x4CCD0` | 141 | UnwindData |  |
| 669 | `pSetupStringTableInitialize` | `0x4CE60` | 82 | UnwindData |  |
| 665 | `pSetupStringTableDestroy` | `0x4CEE0` | 57 | UnwindData |  |
| 670 | `pSetupStringTableInitializeEx` | `0x4D160` | 87 | UnwindData |  |
| 477 | `SetupGetLineCountW` | `0x4D240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `SetupFindNextMatchLineW` | `0x4D260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `SetupDiOpenClassRegKeyExW` | `0x4D280` | 17,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `SetupGetBackupInformationA` | `0x515F0` | 123 | UnwindData |  |
| 455 | `SetupGetBackupInformationW` | `0x51680` | 123 | UnwindData |  |
| 525 | `SetupPrepareQueueForRestoreA` | `0x51710` | 123 | UnwindData |  |
| 526 | `SetupPrepareQueueForRestoreW` | `0x517A0` | 123 | UnwindData |  |
| 498 | `SetupInstallFileA` | `0x519F0` | 241 | UnwindData |  |
| 499 | `SetupInstallFileExA` | `0x51AF0` | 487 | UnwindData |  |
| 500 | `SetupInstallFileExW` | `0x51CE0` | 733 | UnwindData |  |
| 501 | `SetupInstallFileW` | `0x51FD0` | 241 | UnwindData |  |
| 277 | `SetupDecompressOrCopyFileA` | `0x537A0` | 275 | UnwindData |  |
| 278 | `SetupDecompressOrCopyFileW` | `0x538C0` | 275 | UnwindData |  |
| 458 | `SetupGetFileCompressionInfoA` | `0x53B50` | 608 | UnwindData |  |
| 459 | `SetupGetFileCompressionInfoExA` | `0x53DC0` | 622 | UnwindData |  |
| 460 | `SetupGetFileCompressionInfoExW` | `0x54040` | 558 | UnwindData |  |
| 461 | `SetupGetFileCompressionInfoW` | `0x54280` | 544 | UnwindData |  |
| 287 | `SetupDiBuildClassInfoList` | `0x55180` | 272 | UnwindData |  |
| 288 | `SetupDiBuildClassInfoListExA` | `0x552A0` | 362 | UnwindData |  |
| 295 | `SetupDiClassGuidsFromNameExA` | `0x55410` | 414 | UnwindData |  |
| 297 | `SetupDiClassGuidsFromNameW` | `0x555C0` | 272 | UnwindData |  |
| 298 | `SetupDiClassNameFromGuidA` | `0x556E0` | 272 | UnwindData |  |
| 299 | `SetupDiClassNameFromGuidExA` | `0x55800` | 533 | UnwindData |  |
| 383 | `SetupDiGetINFClassA` | `0x55A20` | 531 | UnwindData |  |
| 292 | `SetupDiCancelDriverInfoSearch` | `0x56270` | 308 | UnwindData |  |
| 319 | `SetupDiDestroyDriverInfoList` | `0x563B0` | 658 | UnwindData |  |
| 323 | `SetupDiEnumDriverInfoA` | `0x56650` | 297 | UnwindData |  |
| 372 | `SetupDiGetDriverInfoDetailA` | `0x56780` | 1,592 | UnwindData |  |
| 374 | `SetupDiGetDriverInstallParamsA` | `0x56DC0` | 284 | UnwindData |  |
| 386 | `SetupDiGetSelectedDriverA` | `0x56EF0` | 267 | UnwindData |  |
| 435 | `SetupDiSetDriverInstallParamsA` | `0x57010` | 284 | UnwindData |  |
| 436 | `SetupDiSetDriverInstallParamsW` | `0x57140` | 417 | UnwindData |  |
| 438 | `SetupDiSetSelectedDriverA` | `0x572F0` | 308 | UnwindData |  |
| 614 | `pSetupDiEnumSelectedDrivers` | `0x578D0` | 396 | UnwindData |  |
| 615 | `pSetupDiGetDriverInfoExtensionId` | `0x57A70` | 365 | UnwindData |  |
| 661 | `pSetupShouldDeviceBeExcluded` | `0x57F80` | 321 | UnwindData |  |
| 317 | `SetupDiDestroyClassImageList` | `0x586E0` | 376 | UnwindData |  |
| 320 | `SetupDiDrawMiniIcon` | `0x58860` | 1,107 | UnwindData |  |
| 331 | `SetupDiGetClassBitmapIndex` | `0x58CC0` | 425 | UnwindData |  |
| 344 | `SetupDiGetClassImageListExA` | `0x58E70` | 310 | UnwindData |  |
| 396 | `SetupDiLoadClassIcon` | `0x58FB0` | 430 | UnwindData |  |
| 602 | `pSetupAddMiniIconToList` | `0x59170` | 1,232 | UnwindData |  |
| 304 | `SetupDiCreateDeviceInfoA` | `0x59650` | 375 | UnwindData |  |
| 306 | `SetupDiCreateDeviceInfoListExA` | `0x597D0` | 267 | UnwindData |  |
| 308 | `SetupDiCreateDeviceInfoW` | `0x598F0` | 1,131 | UnwindData |  |
| 309 | `SetupDiCreateDeviceInterfaceA` | `0x59D70` | 287 | UnwindData |  |
| 312 | `SetupDiCreateDeviceInterfaceW` | `0x59EA0` | 437 | UnwindData |  |
| 356 | `SetupDiGetDeviceInfoListClass` | `0x5A060` | 280 | UnwindData |  |
| 357 | `SetupDiGetDeviceInfoListDetailA` | `0x5A180` | 261 | UnwindData |  |
| 405 | `SetupDiOpenDeviceInterfaceA` | `0x5A290` | 244 | UnwindData |  |
| 409 | `SetupDiRegisterDeviceInfo` | `0x5A390` | 676 | UnwindData |  |
| 411 | `SetupDiRemoveDeviceInterface` | `0x5A640` | 302 | UnwindData |  |
| 430 | `SetupDiSetDeviceInterfaceDefault` | `0x5A780` | 437 | UnwindData |  |
| 291 | `SetupDiCallClassInstaller` | `0x5A940` | 229 | UnwindData |  |
| 346 | `SetupDiGetClassInstallParamsA` | `0x5AA30` | 623 | UnwindData |  |
| 359 | `SetupDiGetDeviceInstallParamsA` | `0x5ACB0` | 322 | UnwindData |  |
| 376 | `SetupDiGetHwProfileFriendlyNameA` | `0x5AE00` | 272 | UnwindData |  |
| 377 | `SetupDiGetHwProfileFriendlyNameExA` | `0x5AF20` | 551 | UnwindData |  |
| 378 | `SetupDiGetHwProfileFriendlyNameExW` | `0x5B150` | 584 | UnwindData |  |
| 379 | `SetupDiGetHwProfileFriendlyNameW` | `0x5B3A0` | 272 | UnwindData |  |
| 380 | `SetupDiGetHwProfileList` | `0x5B4C0` | 272 | UnwindData |  |
| 381 | `SetupDiGetHwProfileListExA` | `0x5B5E0` | 366 | UnwindData |  |
| 382 | `SetupDiGetHwProfileListExW` | `0x5B760` | 552 | UnwindData |  |
| 389 | `SetupDiInstallClassA` | `0x5B990` | 338 | UnwindData |  |
| 390 | `SetupDiInstallClassExA` | `0x5BAF0` | 371 | UnwindData |  |
| 391 | `SetupDiInstallClassExW` | `0x5BC70` | 3,523 | UnwindData |  |
| 392 | `SetupDiInstallClassW` | `0x5CA40` | 278 | UnwindData |  |
| 422 | `SetupDiSetClassInstallParamsA` | `0x5CB60` | 422 | UnwindData |  |
| 423 | `SetupDiSetClassInstallParamsW` | `0x5CD10` | 345 | UnwindData |  |
| 325 | `SetupDiGetActualModelsSectionA` | `0x62060` | 474 | UnwindData |  |
| 326 | `SetupDiGetActualModelsSectionW` | `0x62240` | 691 | UnwindData |  |
| 327 | `SetupDiGetActualSectionToInstallA` | `0x62500` | 207 | UnwindData |  |
| 328 | `SetupDiGetActualSectionToInstallExA` | `0x625E0` | 679 | UnwindData |  |
| 394 | `SetupDiInstallDeviceInterfaces` | `0x62890` | 157 | UnwindData |  |
| 395 | `SetupDiInstallDriverFiles` | `0x62940` | 566 | UnwindData |  |
| 398 | `SetupDiMoveDuplicateDevice` | `0x62B80` | 123 | UnwindData |  |
| 408 | `SetupDiRegisterCoDeviceInstallers` | `0x638E0` | 157 | UnwindData |  |
| 410 | `SetupDiRemoveDevice` | `0x63990` | 619 | UnwindData |  |
| 418 | `SetupDiRestartDevices` | `0x63C10` | 431 | UnwindData |  |
| 440 | `SetupDiUnremoveDevice` | `0x63DD0` | 1,054 | UnwindData |  |
| 286 | `SetupDiAskForOEMDisk` | `0x672F0` | 572 | UnwindData |  |
| 421 | `SetupDiSelectOEMDrv` | `0x67540` | 242 | UnwindData |  |
| 236 | `ExtensionPropSheetPageProc` | `0x67640` | 287 | UnwindData |  |
| 336 | `SetupDiGetClassDevPropertySheetsA` | `0x67770` | 369 | UnwindData |  |
| 337 | `SetupDiGetClassDevPropertySheetsW` | `0x678F0` | 3,779 | UnwindData |  |
| 302 | `SetupDiCreateDevRegKeyA` | `0x688D0` | 390 | UnwindData |  |
| 310 | `SetupDiCreateDeviceInterfaceRegKeyA` | `0x68A60` | 379 | UnwindData |  |
| 311 | `SetupDiCreateDeviceInterfaceRegKeyW` | `0x68BF0` | 1,176 | UnwindData |  |
| 313 | `SetupDiDeleteDevRegKey` | `0x69090` | 349 | UnwindData |  |
| 316 | `SetupDiDeleteDeviceInterfaceRegKey` | `0x69200` | 335 | UnwindData |  |
| 349 | `SetupDiGetClassPropertyKeys` | `0x69360` | 284 | UnwindData |  |
| 350 | `SetupDiGetClassPropertyKeysExW` | `0x69490` | 297 | UnwindData |  |
| 352 | `SetupDiGetClassRegistryPropertyA` | `0x695C0` | 744 | UnwindData |  |
| 353 | `SetupDiGetClassRegistryPropertyW` | `0x698B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `SetupDiGetCustomDevicePropertyA` | `0x698D0` | 294 | UnwindData |  |
| 355 | `SetupDiGetCustomDevicePropertyW` | `0x69A00` | 290 | UnwindData |  |
| 400 | `SetupDiOpenClassRegKeyExA` | `0x69B30` | 365 | UnwindData |  |
| 424 | `SetupDiSetClassPropertyExW` | `0x69CB0` | 308 | UnwindData |  |
| 425 | `SetupDiSetClassPropertyW` | `0x69DF0` | 295 | UnwindData |  |
| 426 | `SetupDiSetClassRegistryPropertyA` | `0x69F20` | 590 | UnwindData |  |
| 427 | `SetupDiSetClassRegistryPropertyW` | `0x6A180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `SetupDiSetDeviceInterfacePropertyW` | `0x6A1A0` | 441 | UnwindData |  |
| 433 | `SetupDiSetDeviceRegistryPropertyA` | `0x6A360` | 254 | UnwindData |  |
| 632 | `pSetupGetRealSystemTime` | `0x77300` | 18,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 682 | `pSetupWriteLogError` | `0x77300` | 18,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `pSetupAddTagToGroupOrderListEntry` | `0x7BAF0` | 812 | UnwindData |  |
| 633 | `pSetupGetSourceInfFilename` | `0x7C250` | 44 | UnwindData |  |
| 634 | `pSetupGetUniqueServiceName` | `0x7C290` | 289 | UnwindData |  |
| 656 | `pSetupRetrieveServiceConfig` | `0x7C570` | 359 | UnwindData |  |
| 385 | `SetupDiGetSelectedDevice` | `0x81150` | 300 | UnwindData |  |
| 388 | `SetupDiGetWizardPage` | `0x81290` | 798 | UnwindData |  |
| 420 | `SetupDiSelectDevice` | `0x815C0` | 704 | UnwindData |  |
| 437 | `SetupDiSetSelectedDevice` | `0x81890` | 293 | UnwindData |  |
| 269 | `SetupConfigureWmiFromInfSectionA` | `0x83720` | 305 | UnwindData |  |
| 512 | `SetupIterateCabinetA` | `0x83930` | 257 | UnwindData |  |
| 250 | `SetupAddInstallSectionToDiskSpaceListA` | `0x846F0` | 303 | UnwindData |  |
| 251 | `SetupAddInstallSectionToDiskSpaceListW` | `0x84830` | 263 | UnwindData |  |
| 252 | `SetupAddSectionToDiskSpaceListA` | `0x84940` | 289 | UnwindData |  |
| 253 | `SetupAddSectionToDiskSpaceListW` | `0x84A70` | 206 | UnwindData |  |
| 254 | `SetupAddToDiskSpaceListA` | `0x84B50` | 347 | UnwindData |  |
| 255 | `SetupAddToDiskSpaceListW` | `0x84CC0` | 451 | UnwindData |  |
| 258 | `SetupAdjustDiskSpaceListA` | `0x84E90` | 323 | UnwindData |  |
| 259 | `SetupAdjustDiskSpaceListW` | `0x84FE0` | 431 | UnwindData |  |
| 275 | `SetupCreateDiskSpaceListA` | `0x851A0` | 162 | UnwindData |  |
| 276 | `SetupCreateDiskSpaceListW` | `0x85250` | 367 | UnwindData |  |
| 284 | `SetupDestroyDiskSpaceList` | `0x853D0` | 401 | UnwindData |  |
| 441 | `SetupDuplicateDiskSpaceListA` | `0x85570` | 179 | UnwindData |  |
| 442 | `SetupDuplicateDiskSpaceListW` | `0x85630` | 616 | UnwindData |  |
| 530 | `SetupQueryDrivesInDiskSpaceListA` | `0x858A0` | 182 | UnwindData |  |
| 531 | `SetupQueryDrivesInDiskSpaceListW` | `0x85960` | 185 | UnwindData |  |
| 542 | `SetupQuerySpaceRequiredOnDriveA` | `0x85A20` | 264 | UnwindData |  |
| 543 | `SetupQuerySpaceRequiredOnDriveW` | `0x85B30` | 664 | UnwindData |  |
| 562 | `SetupRemoveFromDiskSpaceListA` | `0x85DD0` | 323 | UnwindData |  |
| 563 | `SetupRemoveFromDiskSpaceListW` | `0x85F20` | 423 | UnwindData |  |
| 566 | `SetupRemoveInstallSectionFromDiskSpaceListA` | `0x860D0` | 303 | UnwindData |  |
| 567 | `SetupRemoveInstallSectionFromDiskSpaceListW` | `0x86210` | 259 | UnwindData |  |
| 568 | `SetupRemoveSectionFromDiskSpaceListA` | `0x86320` | 289 | UnwindData |  |
| 569 | `SetupRemoveSectionFromDiskSpaceListW` | `0x86450` | 206 | UnwindData |  |
| 616 | `pSetupDiGetStrongNameForDriverNode` | `0x8A020` | 498 | UnwindData |  |
| 246 | `PnpIsFileAclIntact` | `0x8A490` | 277 | UnwindData |  |
| 247 | `PnpIsFileContentIntact` | `0x8A5B0` | 291 | UnwindData |  |
| 249 | `PnpRepairWindowsProtectedDriver` | `0x8A6E0` | 2,069 | UnwindData |  |
| 645 | `pSetupIsUserTrustedInstaller` | `0x8BDF0` | 128 | UnwindData |  |
| 496 | `SetupInitializeFileLogA` | `0x8EA40` | 145 | UnwindData |  |
| 497 | `SetupInitializeFileLogW` | `0x8EAE0` | 586 | UnwindData |  |
| 516 | `SetupLogFileA` | `0x8ED30` | 528 | UnwindData |  |
| 517 | `SetupLogFileW` | `0x8EF50` | 442 | UnwindData |  |
| 532 | `SetupQueryFileLogA` | `0x8F110` | 624 | UnwindData |  |
| 533 | `SetupQueryFileLogW` | `0x8F390` | 507 | UnwindData |  |
| 560 | `SetupRemoveFileLogEntryA` | `0x8F5A0` | 277 | UnwindData |  |
| 561 | `SetupRemoveFileLogEntryW` | `0x8F6C0` | 236 | UnwindData |  |
| 589 | `SetupTerminateFileLog` | `0x8F7C0` | 117 | UnwindData |  |
| 462 | `SetupGetFileQueueCount` | `0x8F920` | 409 | UnwindData |  |
| 463 | `SetupGetFileQueueFlags` | `0x8FAC0` | 519 | UnwindData |  |
| 579 | `SetupSetFileQueueAlternatePlatformA` | `0x8FCD0` | 332 | UnwindData |  |
| 580 | `SetupSetFileQueueAlternatePlatformW` | `0x8FE30` | 749 | UnwindData |  |
| 581 | `SetupSetFileQueueFlags` | `0x90130` | 724 | UnwindData |  |
| 631 | `pSetupGetQueueFlags` | `0x90410` | 150 | UnwindData |  |
| 660 | `pSetupSetQueueFlags` | `0x904B0` | 191 | UnwindData |  |
| 544 | `SetupQueueCopyA` | `0x90790` | 787 | UnwindData |  |
| 545 | `SetupQueueCopyIndirectA` | `0x90AB0` | 748 | UnwindData |  |
| 546 | `SetupQueueCopyIndirectW` | `0x90DB0` | 288 | UnwindData |  |
| 547 | `SetupQueueCopySectionA` | `0x90EE0` | 356 | UnwindData |  |
| 549 | `SetupQueueCopyW` | `0x91050` | 261 | UnwindData |  |
| 550 | `SetupQueueDefaultCopyA` | `0x91160` | 429 | UnwindData |  |
| 551 | `SetupQueueDefaultCopyW` | `0x91320` | 644 | UnwindData |  |
| 583 | `SetupSetPlatformPathOverrideA` | `0x915B0` | 244 | UnwindData |  |
| 584 | `SetupSetPlatformPathOverrideW` | `0x916B0` | 421 | UnwindData |  |
| 552 | `SetupQueueDeleteA` | `0x919B0` | 315 | UnwindData |  |
| 553 | `SetupQueueDeleteSectionA` | `0x91B00` | 253 | UnwindData |  |
| 554 | `SetupQueueDeleteSectionW` | `0x91C10` | 695 | UnwindData |  |
| 555 | `SetupQueueDeleteW` | `0x91ED0` | 315 | UnwindData |  |
| 556 | `SetupQueueRenameA` | `0x92020` | 466 | UnwindData |  |
| 557 | `SetupQueueRenameSectionA` | `0x92200` | 253 | UnwindData |  |
| 558 | `SetupQueueRenameSectionW` | `0x92310` | 736 | UnwindData |  |
| 559 | `SetupQueueRenameW` | `0x92600` | 440 | UnwindData |  |
| 266 | `SetupCommitFileQueue` | `0x92990` | 204 | UnwindData |  |
| 267 | `SetupCommitFileQueueA` | `0x92A70` | 197 | UnwindData |  |
| 268 | `SetupCommitFileQueueW` | `0x92B40` | 204 | UnwindData |  |
| 590 | `SetupUninstallNewlyCopiedInfs` | `0x92C20` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 623 | `pSetupGetCurrentDriverSigningPolicy` | `0x92C20` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 636 | `pSetupHandleFailedVerification` | `0x93200` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `pSetupVerifyQueuedCatalogs` | `0x93200` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `pSetupWriteLogEntry` | `0x93200` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `SetupDefaultQueueCallbackA` | `0x93320` | 175 | UnwindData |  |
| 588 | `SetupTermDefaultQueueCallback` | `0x933E0` | 250 | UnwindData |  |
| 529 | `SetupPromptReboot` | `0x95580` | 482 | UnwindData |  |
| 573 | `SetupScanFileQueueA` | `0x95770` | 254 | UnwindData |  |
| 482 | `SetupGetNonInteractiveMode` | `0x976B0` | 21 | UnwindData |  |
| 582 | `SetupSetNonInteractiveMode` | `0x976D0` | 56 | UnwindData |  |
| 649 | `pSetupModifyGlobalFlags` | `0x97710` | 111 | UnwindData |  |
| 659 | `pSetupSetGlobalFlags` | `0x97790` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `SetupGetSourceFileLocationA` | `0x97CB0` | 621 | UnwindData |  |
| 484 | `SetupGetSourceFileLocationW` | `0x97F30` | 524 | UnwindData |  |
| 485 | `SetupGetSourceFileSizeA` | `0x98150` | 519 | UnwindData |  |
| 486 | `SetupGetSourceFileSizeW` | `0x98360` | 519 | UnwindData |  |
| 491 | `SetupGetTargetPathA` | `0x98570` | 520 | UnwindData |  |
| 575 | `SetupSetDirectoryIdA` | `0x98780` | 174 | UnwindData |  |
| 576 | `SetupSetDirectoryIdExA` | `0x98840` | 289 | UnwindData |  |
| 577 | `SetupSetDirectoryIdExW` | `0x98970` | 182 | UnwindData |  |
| 578 | `SetupSetDirectoryIdW` | `0x98A30` | 174 | UnwindData |  |
| 238 | `InstallHinfSection` | `0x99B50` | 104 | UnwindData |  |
| 239 | `InstallHinfSectionA` | `0x99B50` | 104 | UnwindData |  |
| 240 | `InstallHinfSectionW` | `0x99BC0` | 4,051 | UnwindData |  |
| 502 | `SetupInstallFilesFromInfSectionA` | `0x9AC50` | 353 | UnwindData |  |
| 503 | `SetupInstallFilesFromInfSectionW` | `0x9ADC0` | 781 | UnwindData |  |
| 504 | `SetupInstallFromInfSectionA` | `0x9B0E0` | 482 | UnwindData |  |
| 505 | `SetupInstallFromInfSectionW` | `0x9B2D0` | 300 | UnwindData |  |
| 508 | `SetupInstallServicesFromInfSectionA` | `0x9B410` | 257 | UnwindData |  |
| 509 | `SetupInstallServicesFromInfSectionExA` | `0x9B520` | 295 | UnwindData |  |
| 510 | `SetupInstallServicesFromInfSectionExW` | `0x9B650` | 1,766 | UnwindData |  |
| 511 | `SetupInstallServicesFromInfSectionW` | `0x9BD40` | 183 | UnwindData |  |
| 450 | `SetupFindNextMatchLineA` | `0xA5A50` | 269 | UnwindData |  |
| 474 | `SetupGetLineByIndexA` | `0xA5B70` | 260 | UnwindData |  |
| 475 | `SetupGetLineByIndexW` | `0xA5C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 476 | `SetupGetLineCountA` | `0xA5CA0` | 248 | UnwindData |  |
| 273 | `SetupCopyOEMInfA` | `0xA8D30` | 847 | UnwindData |  |
| 274 | `SetupCopyOEMInfW` | `0xA9090` | 2,523 | UnwindData |  |
| 591 | `SetupUninstallOEMInfA` | `0xA9A80` | 298 | UnwindData |  |
| 592 | `SetupUninstallOEMInfW` | `0xA9BB0` | 570 | UnwindData |  |
| 464 | `SetupGetInfDriverStoreLocationA` | `0xAA190` | 590 | UnwindData |  |
| 466 | `SetupGetInfFileListA` | `0xAA3F0` | 343 | UnwindData |  |
| 467 | `SetupGetInfFileListW` | `0xAA550` | 340 | UnwindData |  |
| 468 | `SetupGetInfInformationA` | `0xAA6B0` | 345 | UnwindData |  |
| 470 | `SetupGetInfPublishedNameA` | `0xAA810` | 453 | UnwindData |  |
| 518 | `SetupOpenAppendInfFileA` | `0xAA9E0` | 302 | UnwindData |  |
| 524 | `SetupOpenMasterInf` | `0xAAB20` | 227 | UnwindData |  |
| 534 | `SetupQueryInfFileInformationA` | `0xAAC10` | 477 | UnwindData |  |
| 535 | `SetupQueryInfFileInformationW` | `0xAAE00` | 192 | UnwindData |  |
| 536 | `SetupQueryInfOriginalFileInformationA` | `0xAAED0` | 564 | UnwindData |  |
| 537 | `SetupQueryInfOriginalFileInformationW` | `0xAB110` | 549 | UnwindData |  |
| 538 | `SetupQueryInfVersionInformationA` | `0xAB340` | 697 | UnwindData |  |
| 539 | `SetupQueryInfVersionInformationW` | `0xAB600` | 461 | UnwindData |  |
| 593 | `SetupVerifyInfFileA` | `0xAB7E0` | 611 | UnwindData |  |
| 487 | `SetupGetSourceInfoA` | `0xAC0A0` | 480 | UnwindData |  |
| 488 | `SetupGetSourceInfoW` | `0xAC290` | 202 | UnwindData |  |
| 472 | `SetupGetInfSections` | `0xAC360` | 184 | UnwindData |  |
| 630 | `pSetupGetInfSections` | `0xAC420` | 184 | UnwindData |  |
| 456 | `SetupGetBinaryField` | `0xAC4E0` | 882 | UnwindData |  |
| 478 | `SetupGetLineTextA` | `0xAC930` | 1,203 | UnwindData |  |
| 480 | `SetupGetMultiSzFieldA` | `0xACDF0` | 979 | UnwindData |  |
| 618 | `pSetupDoLastKnownGoodBackup` | `0xAD1D0` | 1,664 | UnwindData |  |
| 514 | `SetupLogErrorA` | `0xADD80` | 179 | UnwindData |  |
| 652 | `pSetupOutOfMemory` | `0xAE500` | 102 | UnwindData |  |
| 606 | `pSetupCenterWindowRelativeToParent` | `0xAEE40` | 406 | UnwindData |  |
| 256 | `SetupAddToSourceListA` | `0xAF160` | 233 | UnwindData |  |
| 257 | `SetupAddToSourceListW` | `0xAF250` | 233 | UnwindData |  |
| 262 | `SetupCancelTemporarySourceList` | `0xAF340` | 233 | UnwindData |  |
| 452 | `SetupFreeSourceListA` | `0xAF430` | 142 | UnwindData |  |
| 540 | `SetupQuerySourceListA` | `0xAF4D0` | 420 | UnwindData |  |
| 541 | `SetupQuerySourceListW` | `0xAF680` | 1,563 | UnwindData |  |
| 564 | `SetupRemoveFromSourceListA` | `0xAFCB0` | 233 | UnwindData |  |
| 565 | `SetupRemoveFromSourceListW` | `0xAFDA0` | 233 | UnwindData |  |
| 585 | `SetupSetSourceListA` | `0xAFE90` | 533 | UnwindData |  |
| 586 | `SetupSetSourceListW` | `0xB00B0` | 533 | UnwindData |  |
| 629 | `pSetupGetIndirectStringsFromDriverInfo` | `0xB1330` | 554 | UnwindData |  |
| 646 | `pSetupLoadIndirectString` | `0xB1560` | 354 | UnwindData |  |
| 237 | `InstallCatalog` | `0xB16D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `MyFree` | `0xB16E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `MyMalloc` | `0xB1700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `MyRealloc` | `0xB1720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `CM_Apply_PowerScheme` | `0xB1740` | 17,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `CM_Delete_PowerScheme` | `0xB1740` | 17,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `CM_Duplicate_PowerScheme` | `0xB1740` | 17,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `CM_Import_PowerScheme` | `0xB1740` | 17,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `CM_RestoreAll_DefaultPowerSchemes` | `0xB1740` | 17,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `CM_Restore_DefaultPowerScheme` | `0xB1740` | 17,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `CM_Set_ActiveScheme` | `0xB1740` | 17,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `CM_Write_UserPowerKey` | `0xB1740` | 17,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `SetupDiApplyPowerScheme` | `0xB1740` | 17,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `SetupBackupErrorA` | `0xB5B00` | 442 | UnwindData |  |
| 261 | `SetupBackupErrorW` | `0xB5CC0` | 720 | UnwindData |  |
| 271 | `SetupCopyErrorA` | `0xB5FA0` | 843 | UnwindData |  |
| 272 | `SetupCopyErrorW` | `0xB6300` | 1,948 | UnwindData |  |
| 282 | `SetupDeleteErrorA` | `0xB6AB0` | 357 | UnwindData |  |
| 283 | `SetupDeleteErrorW` | `0xB6C20` | 720 | UnwindData |  |
| 527 | `SetupPromptForDiskA` | `0xB6F00` | 843 | UnwindData |  |
| 570 | `SetupRenameErrorA` | `0xB7260` | 442 | UnwindData |  |
| 571 | `SetupRenameErrorW` | `0xB7420` | 764 | UnwindData |  |
| 658 | `pSetupSetArrayToMultiSzValue` | `0xB8BF0` | 442 | UnwindData |  |
| 601 | `pSetupAccessRunOnceNodeList` | `0xB96E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `pSetupDestroyRunOnceNodeList` | `0xB96F0` | 235 | UnwindData |  |
| 600 | `pGetDriverPackageHash` | `0xB9E70` | 807 | UnwindData |  |
| 637 | `pSetupInfGetDigitalSignatureInfo` | `0xBA1A0` | 531 | UnwindData |  |
| 639 | `pSetupInfSetDigitalSignatureInfo` | `0xBA3C0` | 422 | UnwindData |  |
| 599 | `VerifyCatalogFile` | `0xBA570` | 51 | UnwindData |  |
| 679 | `pSetupVerifyCatalogFile` | `0xBA570` | 51 | UnwindData |  |
| 412 | `SetupDiReportAdditionalSoftwareRequested` | `0xBA5B0` | 29 | UnwindData |  |
| 413 | `SetupDiReportDeviceInstallError` | `0xBA5B0` | 29 | UnwindData |  |
| 415 | `SetupDiReportDriverPackageImportationError` | `0xBA5B0` | 29 | UnwindData |  |
| 416 | `SetupDiReportGenericDriverInstalled` | `0xBA5B0` | 29 | UnwindData |  |
| 417 | `SetupDiReportPnPDeviceProblem` | `0xBA5B0` | 29 | UnwindData |  |
| 613 | `pSetupDiCrimsonLogDeviceInstall` | `0xBAA40` | 511 | UnwindData |  |
| 414 | `SetupDiReportDriverNotFoundError` | `0xBAD90` | 497 | UnwindData |  |
| 445 | `SetupEnumPublishedInfA` | `0xC2060` | 139 | UnwindData |  |
| 446 | `SetupEnumPublishedInfW` | `0xC2100` | 135 | UnwindData |  |
| 228 | `DriverStoreAddDriverPackageA` | `0xC35F0` | 447 | UnwindData |  |
| 229 | `DriverStoreAddDriverPackageW` | `0xC37C0` | 438 | UnwindData |  |
| 230 | `DriverStoreDeleteDriverPackageA` | `0xC3980` | 104 | UnwindData |  |
| 231 | `DriverStoreDeleteDriverPackageW` | `0xC39F0` | 106 | UnwindData |  |
| 232 | `DriverStoreEnumDriverPackageA` | `0xC3A60` | 171 | UnwindData |  |
| 233 | `DriverStoreEnumDriverPackageW` | `0xC3B20` | 175 | UnwindData |  |
| 234 | `DriverStoreFindDriverPackageA` | `0xC3BE0` | 473 | UnwindData |  |
| 235 | `DriverStoreFindDriverPackageW` | `0xC3DC0` | 223 | UnwindData |  |
| 227 | `DoesUserHavePrivilege` | `0xC4C40` | 403 | UnwindData |  |
| 619 | `pSetupDoesUserHavePrivilege` | `0xC4C40` | 403 | UnwindData |  |
| 621 | `pSetupEnablePrivilege` | `0xC4DE0` | 230 | UnwindData |  |
| 643 | `pSetupIsLocalSystem` | `0xC4ED0` | 282 | UnwindData |  |
| 241 | `IsUserAdmin` | `0xC4FF0` | 285 | UnwindData |  |
| 644 | `pSetupIsUserAdmin` | `0xC4FF0` | 285 | UnwindData |  |
| 506 | `SetupInstallLogCloseEventGroup` | `0xC5260` | 423 | UnwindData |  |
| 507 | `SetupInstallLogCreateEventGroup` | `0xC5410` | 612 | UnwindData |  |
| 651 | `pSetupOpenAndMapFileForRead` | `0xC6460` | 139 | UnwindData |  |
| 678 | `pSetupUnmapAndCloseFile` | `0xC67A0` | 128 | UnwindData |  |
| 642 | `pSetupIsGuidNull` | `0xC68C0` | 1,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 655 | `pSetupRegistryDelnode` | `0xC6E30` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 666 | `pSetupStringTableDuplicate` | `0xC6FE0` | 157 | UnwindData |  |
| 667 | `pSetupStringTableEnum` | `0xC7090` | 170 | UnwindData |  |
| 675 | `pSetupStringTableStringFromIdEx` | `0xC7170` | 321 | UnwindData |  |
| 640 | `pSetupInstallCatalog` | `0xE5AD0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 677 | `pSetupUninstallCatalog` | `0xE5F80` | 14,014 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
