# Binary Specification: cfgmgr32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cfgmgr32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `45a0ae7ffd703ebdd71ea811b9e7fdd9455c492d1b1015944e7da45977aae32d`
* **Total Exported Functions:** 283

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 250 | `CM_Uninstall_DevNode_Ex` | `0x1810` | 40 | UnwindData |  |
| 249 | `CM_Uninstall_DevNode` | `0x1840` | 199 | UnwindData |  |
| 245 | `CM_Set_HW_Prof_Flags_ExW` | `0x1910` | 44 | UnwindData |  |
| 104 | `CM_Get_Device_ID_ListA` | `0x1950` | 21 | UnwindData |  |
| 106 | `CM_Get_Device_ID_List_ExA` | `0x1970` | 311 | UnwindData |  |
| 50 | `CM_Enable_DevNode_Ex` | `0x1AB0` | 40 | UnwindData |  |
| 49 | `CM_Enable_DevNode` | `0x1AE0` | 256 | UnwindData |  |
| 137 | `CM_Get_HW_Prof_Flags_ExW` | `0x1D80` | 44 | UnwindData |  |
| 135 | `CM_Get_HW_Prof_FlagsW` | `0x1DC0` | 278 | UnwindData |  |
| 243 | `CM_Set_HW_Prof_FlagsW` | `0x1FF0` | 333 | UnwindData |  |
| 247 | `CM_Setup_DevNode_Ex` | `0x2150` | 40 | UnwindData |  |
| 246 | `CM_Setup_DevNode` | `0x2180` | 277 | UnwindData |  |
| 204 | `CM_Reenumerate_DevNode` | `0x22D0` | 282 | UnwindData |  |
| 93 | `CM_Get_DevNode_Property_Keys_Ex` | `0x23F0` | 44 | UnwindData |  |
| 92 | `CM_Get_DevNode_Property_Keys` | `0x2430` | 269 | UnwindData |  |
| 196 | `CM_Query_And_Remove_SubTree_ExW` | `0x2550` | 52 | UnwindData |  |
| 110 | `CM_Get_Device_ID_List_Size_ExA` | `0x2B90` | 144 | UnwindData |  |
| 173 | `CM_Locate_DevNode_ExA` | `0x2FD0` | 145 | UnwindData |  |
| 111 | `CM_Get_Device_ID_List_Size_ExW` | `0x3330` | 43 | UnwindData |  |
| 194 | `CM_Query_And_Remove_SubTreeW` | `0x36F0` | 352 | UnwindData |  |
| 122 | `CM_Get_Device_Interface_List_SizeA` | `0x3F90` | 21 | UnwindData |  |
| 124 | `CM_Get_Device_Interface_List_Size_ExA` | `0x3FB0` | 384 | UnwindData |  |
| 125 | `CM_Get_Device_Interface_List_Size_ExW` | `0x4140` | 44 | UnwindData |  |
| 123 | `CM_Get_Device_Interface_List_SizeW` | `0x4180` | 76 | UnwindData |  |
| 239 | `CM_Set_Device_Interface_Property_ExW` | `0x4380` | 60 | UnwindData |  |
| 238 | `CM_Set_Device_Interface_PropertyW` | `0x43D0` | 108 | UnwindData |  |
| 233 | `CM_Set_DevNode_Property_ExW` | `0x4450` | 60 | UnwindData |  |
| 232 | `CM_Set_DevNode_PropertyW` | `0x44A0` | 293 | UnwindData |  |
| 192 | `CM_Open_Device_Interface_Key_ExW` | `0x49E0` | 52 | UnwindData |  |
| 105 | `CM_Get_Device_ID_ListW` | `0x4A20` | 20 | UnwindData |  |
| 107 | `CM_Get_Device_ID_List_ExW` | `0x4A40` | 45 | UnwindData |  |
| 190 | `CM_Open_Device_Interface_KeyW` | `0x4AE0` | 97 | UnwindData |  |
| 117 | `CM_Get_Device_Interface_Alias_ExW` | `0x4CA0` | 52 | UnwindData |  |
| 115 | `CM_Get_Device_Interface_AliasW` | `0x4CE0` | 97 | UnwindData |  |
| 127 | `CM_Get_Device_Interface_Property_ExW` | `0x5250` | 62 | UnwindData |  |
| 126 | `CM_Get_Device_Interface_PropertyW` | `0x52A0` | 225 | UnwindData |  |
| 52 | `CM_Enumerate_Classes_Ex` | `0x5B40` | 40 | UnwindData |  |
| 51 | `CM_Enumerate_Classes` | `0x5B70` | 81 | UnwindData |  |
| 121 | `CM_Get_Device_Interface_List_ExW` | `0x5F00` | 52 | UnwindData |  |
| 119 | `CM_Get_Device_Interface_ListW` | `0x5F40` | 93 | UnwindData |  |
| 188 | `CM_Open_DevNode_Key_Ex` | `0x61D0` | 62 | UnwindData |  |
| 131 | `CM_Get_First_Log_Conf_Ex` | `0x6700` | 40 | UnwindData |  |
| 187 | `CM_Open_DevNode_Key` | `0x6730` | 923 | UnwindData |  |
| 148 | `CM_Get_Parent` | `0x6AE0` | 940 | UnwindData |  |
| 130 | `CM_Get_First_Log_Conf` | `0x7060` | 286 | UnwindData |  |
| 97 | `CM_Get_DevNode_Registry_Property_ExW` | `0x7190` | 62 | UnwindData |  |
| 100 | `CM_Get_Device_IDA` | `0x71E0` | 52 | UnwindData |  |
| 102 | `CM_Get_Device_ID_ExA` | `0x72B0` | 65 | UnwindData |  |
| 103 | `CM_Get_Device_ID_ExW` | `0x7380` | 437 | UnwindData |  |
| 157 | `CM_Get_Sibling` | `0x7630` | 989 | UnwindData |  |
| 91 | `CM_Get_DevNode_Property_ExW` | `0x7A20` | 62 | UnwindData |  |
| 90 | `CM_Get_DevNode_PropertyW` | `0x7A70` | 354 | UnwindData |  |
| 68 | `CM_Get_Child` | `0x7BE0` | 972 | UnwindData |  |
| 174 | `CM_Locate_DevNode_ExW` | `0x7FC0` | 40 | UnwindData |  |
| 172 | `CM_Locate_DevNodeW` | `0x7FF0` | 1,870 | UnwindData |  |
| 95 | `CM_Get_DevNode_Registry_PropertyW` | `0x8810` | 344 | UnwindData |  |
| 98 | `CM_Get_DevNode_Status` | `0x9BC0` | 237 | UnwindData |  |
| 99 | `CM_Get_DevNode_Status_Ex` | `0x9DF0` | 44 | UnwindData |  |
| 113 | `CM_Get_Device_ID_Size_Ex` | `0x9E30` | 291 | UnwindData |  |
| 87 | `CM_Get_DevNode_Custom_PropertyW` | `0xA180` | 331 | UnwindData |  |
| 147 | `CM_Get_Next_Res_Des_Ex` | `0xA440` | 52 | UnwindData |  |
| 146 | `CM_Get_Next_Res_Des` | `0xA480` | 436 | UnwindData |  |
| 153 | `CM_Get_Res_Des_Data_Size_Ex` | `0xBF20` | 40 | UnwindData |  |
| 152 | `CM_Get_Res_Des_Data_Size` | `0xBF50` | 440 | UnwindData |  |
| 151 | `CM_Get_Res_Des_Data_Ex` | `0xC110` | 44 | UnwindData |  |
| 150 | `CM_Get_Res_Des_Data` | `0xC150` | 456 | UnwindData |  |
| 169 | `CM_Is_Version_Available` | `0xC990` | 44,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `CM_Set_DevNode_Registry_Property_ExW` | `0x17880` | 52 | UnwindData |  |
| 235 | `CM_Set_DevNode_Registry_PropertyW` | `0x178C0` | 1,120 | UnwindData |  |
| 94 | `CM_Get_DevNode_Registry_PropertyA` | `0x17D30` | 39 | UnwindData |  |
| 96 | `CM_Get_DevNode_Registry_Property_ExA` | `0x17D60` | 504 | UnwindData |  |
| 272 | `DevSetObjectProperties` | `0x190C0` | 221 | UnwindData |  |
| 261 | `DevCreateObjectQueryFromId` | `0x19630` | 99 | UnwindData |  |
| 262 | `DevCreateObjectQueryFromIdEx` | `0x196A0` | 226 | UnwindData |  |
| 270 | `DevGetObjects` | `0x19790` | 75 | UnwindData |  |
| 271 | `DevGetObjectsEx` | `0x197F0` | 474 | UnwindData |  |
| 259 | `DevCreateObjectQuery` | `0x1A560` | 87 | UnwindData |  |
| 260 | `DevCreateObjectQueryEx` | `0x1A7B0` | 207 | UnwindData |  |
| 268 | `DevGetObjectProperties` | `0x1AB20` | 64 | UnwindData |  |
| 269 | `DevGetObjectPropertiesEx` | `0x1AB70` | 752 | UnwindData |  |
| 283 | `SwMemFree` | `0x1C0F0` | 46 | UnwindData |  |
| 277 | `SwDeviceInterfacePropertySet` | `0x1D760` | 386 | UnwindData |  |
| 278 | `SwDeviceInterfaceRegister` | `0x1DD00` | 667 | UnwindData |  |
| 280 | `SwDevicePropertySet` | `0x1DFB0` | 360 | UnwindData |  |
| 279 | `SwDeviceInterfaceSetState` | `0x1E120` | 362 | UnwindData |  |
| 282 | `SwDeviceSetLifetime` | `0x1E290` | 65 | UnwindData |  |
| 276 | `SwDeviceGetLifetime` | `0x1E510` | 83 | UnwindData |  |
| 186 | `CM_Open_Class_Key_ExW` | `0x1E830` | 62 | UnwindData |  |
| 184 | `CM_Open_Class_KeyW` | `0x1E880` | 127 | UnwindData |  |
| 77 | `CM_Get_Class_Name_ExW` | `0x1EB70` | 44 | UnwindData |  |
| 75 | `CM_Get_Class_NameW` | `0x1EBB0` | 274 | UnwindData |  |
| 79 | `CM_Get_Class_Property_ExW` | `0x1ECD0` | 62 | UnwindData |  |
| 78 | `CM_Get_Class_PropertyW` | `0x1ED20` | 228 | UnwindData |  |
| 266 | `DevFreeObjectProperties` | `0x1F760` | 80 | UnwindData |  |
| 212 | `CM_Register_Notification` | `0x1F830` | 23 | UnwindData |  |
| 7 | `CMP_Register_Notification` | `0x1F850` | 1,427 | UnwindData |  |
| 267 | `DevFreeObjects` | `0x1FDF0` | 142 | UnwindData |  |
| 265 | `DevFindProperty` | `0x1FE90` | 210 | UnwindData |  |
| 176 | `CM_MapCrToWin32Err` | `0x1FF70` | 150 | UnwindData |  |
| 175 | `CM_MapCrToSpErr` | `0x20010` | 2,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `CM_Free_Log_Conf_Handle` | `0x20820` | 110 | UnwindData |  |
| 256 | `CM_Unregister_Notification` | `0x20910` | 438 | UnwindData |  |
| 9 | `CMP_WaitNoPendingInstallEvents` | `0x20B30` | 521 | UnwindData |  |
| 66 | `CM_Free_Res_Des_Handle` | `0x21370` | 110 | UnwindData |  |
| 258 | `DevCloseObjectQuery` | `0x216B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `CM_Get_Device_IDW` | `0x216D0` | 21 | UnwindData |  |
| 274 | `SwDeviceCreate` | `0x216F0` | 1,478 | UnwindData |  |
| 149 | `CM_Get_Parent_Ex` | `0x21F20` | 40 | UnwindData |  |
| 84 | `CM_Get_Depth` | `0x21FD0` | 232 | UnwindData |  |
| 170 | `CM_Is_Version_Available_Ex` | `0x22200` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `SwDeviceClose` | `0x223A0` | 280 | UnwindData |  |
| 195 | `CM_Query_And_Remove_SubTree_ExA` | `0x224D0` | 289 | UnwindData |  |
| 109 | `CM_Get_Device_ID_List_SizeW` | `0x22600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `CM_Get_Device_ID_Size` | `0x22610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `CM_Create_DevNode_ExW` | `0x22620` | 44 | UnwindData |  |
| 26 | `CM_Create_DevNodeW` | `0x22660` | 527 | UnwindData |  |
| 69 | `CM_Get_Child_Ex` | `0x22880` | 40 | UnwindData |  |
| 11 | `CM_Add_Driver_PackageW` | `0x22A70` | 281 | UnwindData |  |
| 158 | `CM_Get_Sibling_Ex` | `0x230C0` | 40 | UnwindData |  |
| 171 | `CM_Locate_DevNodeA` | `0x230F0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `CM_Get_DevNode_Custom_Property_ExW` | `0x232A0` | 62 | UnwindData |  |
| 120 | `CM_Get_Device_Interface_List_ExA` | `0x232F0` | 328 | UnwindData |  |
| 44 | `CM_Disable_DevNode` | `0x23440` | 277 | UnwindData |  |
| 23 | `CM_Connect_MachineA` | `0x23820` | 115 | UnwindData |  |
| 24 | `CM_Connect_MachineW` | `0x238A0` | 105 | UnwindData |  |
| 164 | `CM_Install_DriverW` | `0x23AA0` | 234 | UnwindData |  |
| 129 | `CM_Get_Device_Interface_Property_Keys_ExW` | `0x23DB0` | 44 | UnwindData |  |
| 128 | `CM_Get_Device_Interface_Property_KeysW` | `0x23DF0` | 104 | UnwindData |  |
| 162 | `CM_Install_DevNodeW` | `0x23E60` | 359 | UnwindData |  |
| 108 | `CM_Get_Device_ID_List_SizeA` | `0x24040` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CMP_Get_Device_ID_List` | `0x24100` | 23 | UnwindData |  |
| 4 | `CMP_Get_Device_ID_List_Size` | `0x24420` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `CM_Delete_DevNode_Key_Ex` | `0x245C0` | 40 | UnwindData |  |
| 234 | `CM_Set_DevNode_Registry_PropertyA` | `0x25460` | 29 | UnwindData |  |
| 236 | `CM_Set_DevNode_Registry_Property_ExA` | `0x25490` | 360 | UnwindData |  |
| 32 | `CM_Delete_DevNode_Key` | `0x25F20` | 230 | UnwindData |  |
| 1 | `CMP_GetBlockedDriverInfo` | `0x26AB0` | 74 | UnwindData |  |
| 2 | `CMP_GetServerSideDeviceInstallFlags` | `0x26B00` | 84 | UnwindData |  |
| 5 | `CMP_Init_Detection` | `0x26B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CMP_Report_LogOn` | `0x26B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `CMP_WaitServicesAvailable` | `0x26BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `CM_Disconnect_Machine` | `0x26BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `CM_Get_Global_State` | `0x26BE0` | 104 | UnwindData |  |
| 133 | `CM_Get_Global_State_Ex` | `0x26C50` | 40 | UnwindData |  |
| 159 | `CM_Get_Version` | `0x26C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `CM_Get_Version_Ex` | `0x26C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `CM_Query_Arbitrator_Free_Data` | `0x26CB0` | 253 | UnwindData |  |
| 198 | `CM_Query_Arbitrator_Free_Data_Ex` | `0x26DC0` | 52 | UnwindData |  |
| 199 | `CM_Query_Arbitrator_Free_Size` | `0x26E00` | 259 | UnwindData |  |
| 200 | `CM_Query_Arbitrator_Free_Size_Ex` | `0x26F10` | 44 | UnwindData |  |
| 223 | `CM_Run_Detection` | `0x26F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `CM_Run_Detection_Ex` | `0x26F70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `CM_Enumerate_EnumeratorsA` | `0x26FA0` | 21 | UnwindData |  |
| 54 | `CM_Enumerate_EnumeratorsW` | `0x26FC0` | 85 | UnwindData |  |
| 55 | `CM_Enumerate_Enumerators_ExA` | `0x27020` | 150 | UnwindData |  |
| 56 | `CM_Enumerate_Enumerators_ExW` | `0x270C0` | 44 | UnwindData |  |
| 85 | `CM_Get_Depth_Ex` | `0x27100` | 40 | UnwindData |  |
| 6 | `CMP_RegisterServiceNotification` | `0x27130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `CM_Apply_PowerScheme` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `CM_Delete_PowerScheme` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `CM_Duplicate_PowerScheme` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `CM_Import_PowerScheme` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `CM_Move_DevNode` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `CM_Move_DevNode_Ex` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `CM_Query_Remove_SubTree` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `CM_Query_Remove_SubTree_Ex` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `CM_Remove_SubTree` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `CM_Remove_SubTree_Ex` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `CM_RestoreAll_DefaultPowerSchemes` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `CM_Restore_DefaultPowerScheme` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `CM_Set_ActiveScheme` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `CM_Write_UserPowerKey` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `CM_Add_Driver_Package_ExW` | `0x27150` | 277 | UnwindData |  |
| 38 | `CM_Delete_Driver_PackageW` | `0x27270` | 224 | UnwindData |  |
| 39 | `CM_Delete_Driver_Package_ExW` | `0x27360` | 217 | UnwindData |  |
| 251 | `CM_Uninstall_DriverW` | `0x27440` | 234 | UnwindData |  |
| 13 | `CM_Add_Empty_Log_Conf` | `0x27560` | 308 | UnwindData |  |
| 14 | `CM_Add_Empty_Log_Conf_Ex` | `0x276A0` | 44 | UnwindData |  |
| 60 | `CM_Free_Log_Conf` | `0x276E0` | 308 | UnwindData |  |
| 61 | `CM_Free_Log_Conf_Ex` | `0x27820` | 40 | UnwindData |  |
| 142 | `CM_Get_Log_Conf_Priority` | `0x27850` | 298 | UnwindData |  |
| 143 | `CM_Get_Log_Conf_Priority_Ex` | `0x27980` | 40 | UnwindData |  |
| 144 | `CM_Get_Next_Log_Conf` | `0x279B0` | 317 | UnwindData |  |
| 145 | `CM_Get_Next_Log_Conf_Ex` | `0x27B00` | 40 | UnwindData |  |
| 15 | `CM_Add_IDA` | `0x27BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `CM_Add_IDW` | `0x27BD0` | 229 | UnwindData |  |
| 17 | `CM_Add_ID_ExA` | `0x27CC0` | 128 | UnwindData |  |
| 18 | `CM_Add_ID_ExW` | `0x27D50` | 40 | UnwindData |  |
| 25 | `CM_Create_DevNodeA` | `0x27D80` | 21 | UnwindData |  |
| 27 | `CM_Create_DevNode_ExA` | `0x27DA0` | 140 | UnwindData |  |
| 45 | `CM_Disable_DevNode_Ex` | `0x27E40` | 40 | UnwindData |  |
| 193 | `CM_Query_And_Remove_SubTreeA` | `0x27E70` | 29 | UnwindData |  |
| 205 | `CM_Reenumerate_DevNode_Ex` | `0x27EA0` | 40 | UnwindData |  |
| 206 | `CM_Register_Device_Driver` | `0x27ED0` | 218 | UnwindData |  |
| 207 | `CM_Register_Device_Driver_Ex` | `0x27FB0` | 40 | UnwindData |  |
| 215 | `CM_Request_Device_EjectA` | `0x27FE0` | 29 | UnwindData |  |
| 216 | `CM_Request_Device_EjectW` | `0x28010` | 324 | UnwindData |  |
| 217 | `CM_Request_Device_Eject_ExA` | `0x28160` | 292 | UnwindData |  |
| 218 | `CM_Request_Device_Eject_ExW` | `0x28290` | 52 | UnwindData |  |
| 230 | `CM_Set_DevNode_Problem` | `0x282D0` | 283 | UnwindData |  |
| 231 | `CM_Set_DevNode_Problem_Ex` | `0x28400` | 40 | UnwindData |  |
| 19 | `CM_Add_Range` | `0x28520` | 197 | UnwindData |  |
| 29 | `CM_Create_Range_List` | `0x285F0` | 274 | UnwindData |  |
| 41 | `CM_Delete_Range` | `0x28710` | 427 | UnwindData |  |
| 47 | `CM_Dup_Range_List` | `0x288D0` | 284 | UnwindData |  |
| 58 | `CM_Find_Range` | `0x28A00` | 476 | UnwindData |  |
| 59 | `CM_First_Range` | `0x28BF0` | 247 | UnwindData |  |
| 63 | `CM_Free_Range_List` | `0x28CF0` | 200 | UnwindData |  |
| 165 | `CM_Intersect_Range_List` | `0x28DC0` | 569 | UnwindData |  |
| 166 | `CM_Invert_Range_List` | `0x29000` | 398 | UnwindData |  |
| 177 | `CM_Merge_Range_List` | `0x291A0` | 777 | UnwindData |  |
| 182 | `CM_Next_Range` | `0x294B0` | 211 | UnwindData |  |
| 248 | `CM_Test_Range_Available` | `0x29590` | 225 | UnwindData |  |
| 20 | `CM_Add_Res_Des` | `0x29870` | 650 | UnwindData |  |
| 21 | `CM_Add_Res_Des_Ex` | `0x29B00` | 60 | UnwindData |  |
| 42 | `CM_Detect_Resource_Conflict` | `0x29B50` | 39 | UnwindData |  |
| 43 | `CM_Detect_Resource_Conflict_Ex` | `0x29B80` | 456 | UnwindData |  |
| 64 | `CM_Free_Res_Des` | `0x29D50` | 408 | UnwindData |  |
| 65 | `CM_Free_Res_Des_Ex` | `0x29EF0` | 40 | UnwindData |  |
| 178 | `CM_Modify_Res_Des` | `0x29F20` | 659 | UnwindData |  |
| 179 | `CM_Modify_Res_Des_Ex` | `0x2A1C0` | 60 | UnwindData |  |
| 30 | `CM_Delete_Class_Key` | `0x2A3D0` | 72 | UnwindData |  |
| 31 | `CM_Delete_Class_Key_Ex` | `0x2A420` | 40 | UnwindData |  |
| 34 | `CM_Delete_Device_Interface_KeyA` | `0x2A450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `CM_Delete_Device_Interface_KeyW` | `0x2A460` | 68 | UnwindData |  |
| 36 | `CM_Delete_Device_Interface_Key_ExA` | `0x2A4B0` | 117 | UnwindData |  |
| 37 | `CM_Delete_Device_Interface_Key_ExW` | `0x2A530` | 40 | UnwindData |  |
| 70 | `CM_Get_Class_Key_NameA` | `0x2A560` | 21 | UnwindData |  |
| 71 | `CM_Get_Class_Key_NameW` | `0x2A580` | 144 | UnwindData |  |
| 72 | `CM_Get_Class_Key_Name_ExA` | `0x2A620` | 143 | UnwindData |  |
| 73 | `CM_Get_Class_Key_Name_ExW` | `0x2A6C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `CM_Get_Class_NameA` | `0x2A6D0` | 21 | UnwindData |  |
| 76 | `CM_Get_Class_Name_ExA` | `0x2A6F0` | 156 | UnwindData |  |
| 82 | `CM_Get_Class_Registry_PropertyA` | `0x2A7A0` | 399 | UnwindData |  |
| 83 | `CM_Get_Class_Registry_PropertyW` | `0x2A940` | 823 | UnwindData |  |
| 86 | `CM_Get_DevNode_Custom_PropertyA` | `0x2AC80` | 39 | UnwindData |  |
| 88 | `CM_Get_DevNode_Custom_Property_ExA` | `0x2ACB0` | 706 | UnwindData |  |
| 114 | `CM_Get_Device_Interface_AliasA` | `0x2AF80` | 29 | UnwindData |  |
| 116 | `CM_Get_Device_Interface_Alias_ExA` | `0x2AFB0` | 388 | UnwindData |  |
| 118 | `CM_Get_Device_Interface_ListA` | `0x2B140` | 29 | UnwindData |  |
| 183 | `CM_Open_Class_KeyA` | `0x2B170` | 39 | UnwindData |  |
| 185 | `CM_Open_Class_Key_ExA` | `0x2B1A0` | 180 | UnwindData |  |
| 189 | `CM_Open_Device_Interface_KeyA` | `0x2B260` | 29 | UnwindData |  |
| 191 | `CM_Open_Device_Interface_Key_ExA` | `0x2B290` | 151 | UnwindData |  |
| 208 | `CM_Register_Device_InterfaceA` | `0x2B330` | 39 | UnwindData |  |
| 209 | `CM_Register_Device_InterfaceW` | `0x2B360` | 284 | UnwindData |  |
| 210 | `CM_Register_Device_Interface_ExA` | `0x2B490` | 418 | UnwindData |  |
| 211 | `CM_Register_Device_Interface_ExW` | `0x2B640` | 62 | UnwindData |  |
| 228 | `CM_Set_Class_Registry_PropertyA` | `0x2B690` | 360 | UnwindData |  |
| 229 | `CM_Set_Class_Registry_PropertyW` | `0x2B800` | 919 | UnwindData |  |
| 252 | `CM_Unregister_Device_InterfaceA` | `0x2BBA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `CM_Unregister_Device_InterfaceW` | `0x2BBB0` | 68 | UnwindData |  |
| 254 | `CM_Unregister_Device_Interface_ExA` | `0x2BC00` | 182 | UnwindData |  |
| 255 | `CM_Unregister_Device_Interface_ExW` | `0x2BCC0` | 40 | UnwindData |  |
| 57 | `CM_Export_Pnp_StateW` | `0x2BCF0` | 234 | UnwindData |  |
| 67 | `CM_Free_Resource_Conflict_Handle` | `0x2BDE0` | 165 | UnwindData |  |
| 154 | `CM_Get_Resource_Conflict_Count` | `0x2BE90` | 85 | UnwindData |  |
| 155 | `CM_Get_Resource_Conflict_DetailsA` | `0x2BEF0` | 312 | UnwindData |  |
| 156 | `CM_Get_Resource_Conflict_DetailsW` | `0x2C030` | 750 | UnwindData |  |
| 203 | `CM_Query_Resource_Conflict_List` | `0x2C330` | 1,040 | UnwindData |  |
| 80 | `CM_Get_Class_Property_Keys` | `0x2C770` | 193 | UnwindData |  |
| 81 | `CM_Get_Class_Property_Keys_Ex` | `0x2C840` | 44 | UnwindData |  |
| 226 | `CM_Set_Class_PropertyW` | `0x2C880` | 220 | UnwindData |  |
| 227 | `CM_Set_Class_Property_ExW` | `0x2C970` | 60 | UnwindData |  |
| 134 | `CM_Get_HW_Prof_FlagsA` | `0x2C9C0` | 21 | UnwindData |  |
| 136 | `CM_Get_HW_Prof_Flags_ExA` | `0x2C9E0` | 132 | UnwindData |  |
| 138 | `CM_Get_Hardware_Profile_InfoA` | `0x2CA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `CM_Get_Hardware_Profile_InfoW` | `0x2CA80` | 72 | UnwindData |  |
| 140 | `CM_Get_Hardware_Profile_Info_ExA` | `0x2CAD0` | 221 | UnwindData |  |
| 141 | `CM_Get_Hardware_Profile_Info_ExW` | `0x2CBC0` | 40 | UnwindData |  |
| 167 | `CM_Is_Dock_Station_Present` | `0x2CBF0` | 186 | UnwindData |  |
| 168 | `CM_Is_Dock_Station_Present_Ex` | `0x2CCB0` | 40 | UnwindData |  |
| 219 | `CM_Request_Eject_PC` | `0x2CCE0` | 173 | UnwindData |  |
| 220 | `CM_Request_Eject_PC_Ex` | `0x2CDA0` | 40 | UnwindData |  |
| 240 | `CM_Set_HW_Prof` | `0x2CDD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `CM_Set_HW_Prof_Ex` | `0x2CDF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `CM_Set_HW_Prof_FlagsA` | `0x2CE20` | 21 | UnwindData |  |
| 244 | `CM_Set_HW_Prof_Flags_ExA` | `0x2CE40` | 132 | UnwindData |  |
| 163 | `CM_Install_DevNode_ExW` | `0x2CED0` | 241 | UnwindData |  |
| 263 | `DevCreateObjectQueryFromIds` | `0x32740` | 99 | UnwindData |  |
| 264 | `DevCreateObjectQueryFromIdsEx` | `0x327B0` | 293 | UnwindData |  |
| 275 | `SwDeviceGetAttributes` | `0x385D0` | 83 | UnwindData |  |
| 281 | `SwDeviceSetAttributes` | `0x38630` | 65 | UnwindData |  |
