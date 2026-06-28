# Binary Specification: cfgmgr32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cfgmgr32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3ee15d23144ad80b3b6cb2a274c2a44f4d0f7ad0f0dbb64ce55423e649906acd`
* **Total Exported Functions:** 283

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 250 | `CM_Uninstall_DevNode_Ex` | `0x1680` | 40 | UnwindData |  |
| 249 | `CM_Uninstall_DevNode` | `0x16B0` | 199 | UnwindData |  |
| 245 | `CM_Set_HW_Prof_Flags_ExW` | `0x1780` | 44 | UnwindData |  |
| 104 | `CM_Get_Device_ID_ListA` | `0x17C0` | 21 | UnwindData |  |
| 106 | `CM_Get_Device_ID_List_ExA` | `0x17E0` | 311 | UnwindData |  |
| 50 | `CM_Enable_DevNode_Ex` | `0x1920` | 40 | UnwindData |  |
| 49 | `CM_Enable_DevNode` | `0x1950` | 256 | UnwindData |  |
| 137 | `CM_Get_HW_Prof_Flags_ExW` | `0x1BF0` | 44 | UnwindData |  |
| 135 | `CM_Get_HW_Prof_FlagsW` | `0x1C30` | 278 | UnwindData |  |
| 243 | `CM_Set_HW_Prof_FlagsW` | `0x1E60` | 333 | UnwindData |  |
| 247 | `CM_Setup_DevNode_Ex` | `0x1FC0` | 40 | UnwindData |  |
| 246 | `CM_Setup_DevNode` | `0x1FF0` | 277 | UnwindData |  |
| 204 | `CM_Reenumerate_DevNode` | `0x2140` | 282 | UnwindData |  |
| 93 | `CM_Get_DevNode_Property_Keys_Ex` | `0x2260` | 44 | UnwindData |  |
| 92 | `CM_Get_DevNode_Property_Keys` | `0x22A0` | 269 | UnwindData |  |
| 196 | `CM_Query_And_Remove_SubTree_ExW` | `0x23C0` | 52 | UnwindData |  |
| 110 | `CM_Get_Device_ID_List_Size_ExA` | `0x2A00` | 144 | UnwindData |  |
| 173 | `CM_Locate_DevNode_ExA` | `0x2E40` | 145 | UnwindData |  |
| 111 | `CM_Get_Device_ID_List_Size_ExW` | `0x31A0` | 43 | UnwindData |  |
| 194 | `CM_Query_And_Remove_SubTreeW` | `0x3560` | 352 | UnwindData |  |
| 122 | `CM_Get_Device_Interface_List_SizeA` | `0x3E00` | 21 | UnwindData |  |
| 124 | `CM_Get_Device_Interface_List_Size_ExA` | `0x3E20` | 384 | UnwindData |  |
| 125 | `CM_Get_Device_Interface_List_Size_ExW` | `0x3FB0` | 44 | UnwindData |  |
| 123 | `CM_Get_Device_Interface_List_SizeW` | `0x3FF0` | 76 | UnwindData |  |
| 239 | `CM_Set_Device_Interface_Property_ExW` | `0x41F0` | 60 | UnwindData |  |
| 238 | `CM_Set_Device_Interface_PropertyW` | `0x4240` | 108 | UnwindData |  |
| 233 | `CM_Set_DevNode_Property_ExW` | `0x42C0` | 60 | UnwindData |  |
| 232 | `CM_Set_DevNode_PropertyW` | `0x4310` | 293 | UnwindData |  |
| 192 | `CM_Open_Device_Interface_Key_ExW` | `0x4850` | 52 | UnwindData |  |
| 105 | `CM_Get_Device_ID_ListW` | `0x4890` | 20 | UnwindData |  |
| 107 | `CM_Get_Device_ID_List_ExW` | `0x48B0` | 45 | UnwindData |  |
| 190 | `CM_Open_Device_Interface_KeyW` | `0x4950` | 97 | UnwindData |  |
| 117 | `CM_Get_Device_Interface_Alias_ExW` | `0x4B10` | 52 | UnwindData |  |
| 115 | `CM_Get_Device_Interface_AliasW` | `0x4B50` | 97 | UnwindData |  |
| 127 | `CM_Get_Device_Interface_Property_ExW` | `0x50C0` | 62 | UnwindData |  |
| 126 | `CM_Get_Device_Interface_PropertyW` | `0x5110` | 225 | UnwindData |  |
| 52 | `CM_Enumerate_Classes_Ex` | `0x59B0` | 40 | UnwindData |  |
| 51 | `CM_Enumerate_Classes` | `0x59E0` | 81 | UnwindData |  |
| 121 | `CM_Get_Device_Interface_List_ExW` | `0x5D70` | 52 | UnwindData |  |
| 119 | `CM_Get_Device_Interface_ListW` | `0x5DB0` | 93 | UnwindData |  |
| 188 | `CM_Open_DevNode_Key_Ex` | `0x6040` | 62 | UnwindData |  |
| 131 | `CM_Get_First_Log_Conf_Ex` | `0x6570` | 40 | UnwindData |  |
| 187 | `CM_Open_DevNode_Key` | `0x65A0` | 923 | UnwindData |  |
| 148 | `CM_Get_Parent` | `0x6950` | 940 | UnwindData |  |
| 130 | `CM_Get_First_Log_Conf` | `0x6ED0` | 286 | UnwindData |  |
| 97 | `CM_Get_DevNode_Registry_Property_ExW` | `0x7000` | 62 | UnwindData |  |
| 100 | `CM_Get_Device_IDA` | `0x7050` | 52 | UnwindData |  |
| 102 | `CM_Get_Device_ID_ExA` | `0x7120` | 65 | UnwindData |  |
| 103 | `CM_Get_Device_ID_ExW` | `0x71F0` | 437 | UnwindData |  |
| 157 | `CM_Get_Sibling` | `0x74A0` | 989 | UnwindData |  |
| 91 | `CM_Get_DevNode_Property_ExW` | `0x7890` | 62 | UnwindData |  |
| 90 | `CM_Get_DevNode_PropertyW` | `0x78E0` | 354 | UnwindData |  |
| 68 | `CM_Get_Child` | `0x7A50` | 972 | UnwindData |  |
| 174 | `CM_Locate_DevNode_ExW` | `0x7E30` | 40 | UnwindData |  |
| 172 | `CM_Locate_DevNodeW` | `0x7E60` | 1,870 | UnwindData |  |
| 95 | `CM_Get_DevNode_Registry_PropertyW` | `0x8680` | 344 | UnwindData |  |
| 98 | `CM_Get_DevNode_Status` | `0x9A30` | 237 | UnwindData |  |
| 99 | `CM_Get_DevNode_Status_Ex` | `0x9C60` | 44 | UnwindData |  |
| 113 | `CM_Get_Device_ID_Size_Ex` | `0x9CA0` | 291 | UnwindData |  |
| 87 | `CM_Get_DevNode_Custom_PropertyW` | `0x9FF0` | 331 | UnwindData |  |
| 147 | `CM_Get_Next_Res_Des_Ex` | `0xA2B0` | 52 | UnwindData |  |
| 146 | `CM_Get_Next_Res_Des` | `0xA2F0` | 436 | UnwindData |  |
| 153 | `CM_Get_Res_Des_Data_Size_Ex` | `0xBD90` | 40 | UnwindData |  |
| 152 | `CM_Get_Res_Des_Data_Size` | `0xBDC0` | 440 | UnwindData |  |
| 151 | `CM_Get_Res_Des_Data_Ex` | `0xBF80` | 44 | UnwindData |  |
| 150 | `CM_Get_Res_Des_Data` | `0xBFC0` | 456 | UnwindData |  |
| 169 | `CM_Is_Version_Available` | `0xC800` | 44,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `CM_Set_DevNode_Registry_Property_ExW` | `0x176F0` | 52 | UnwindData |  |
| 235 | `CM_Set_DevNode_Registry_PropertyW` | `0x17730` | 1,120 | UnwindData |  |
| 94 | `CM_Get_DevNode_Registry_PropertyA` | `0x17BA0` | 39 | UnwindData |  |
| 96 | `CM_Get_DevNode_Registry_Property_ExA` | `0x17BD0` | 504 | UnwindData |  |
| 272 | `DevSetObjectProperties` | `0x18F30` | 221 | UnwindData |  |
| 261 | `DevCreateObjectQueryFromId` | `0x194A0` | 99 | UnwindData |  |
| 262 | `DevCreateObjectQueryFromIdEx` | `0x19510` | 226 | UnwindData |  |
| 270 | `DevGetObjects` | `0x19600` | 75 | UnwindData |  |
| 271 | `DevGetObjectsEx` | `0x19660` | 474 | UnwindData |  |
| 259 | `DevCreateObjectQuery` | `0x1A3D0` | 87 | UnwindData |  |
| 260 | `DevCreateObjectQueryEx` | `0x1A620` | 207 | UnwindData |  |
| 268 | `DevGetObjectProperties` | `0x1A990` | 64 | UnwindData |  |
| 269 | `DevGetObjectPropertiesEx` | `0x1A9E0` | 752 | UnwindData |  |
| 283 | `SwMemFree` | `0x1BF60` | 46 | UnwindData |  |
| 277 | `SwDeviceInterfacePropertySet` | `0x1D5D0` | 386 | UnwindData |  |
| 278 | `SwDeviceInterfaceRegister` | `0x1DB70` | 667 | UnwindData |  |
| 280 | `SwDevicePropertySet` | `0x1DE20` | 360 | UnwindData |  |
| 279 | `SwDeviceInterfaceSetState` | `0x1DF90` | 362 | UnwindData |  |
| 282 | `SwDeviceSetLifetime` | `0x1E100` | 65 | UnwindData |  |
| 276 | `SwDeviceGetLifetime` | `0x1E380` | 83 | UnwindData |  |
| 186 | `CM_Open_Class_Key_ExW` | `0x1E620` | 62 | UnwindData |  |
| 184 | `CM_Open_Class_KeyW` | `0x1E670` | 127 | UnwindData |  |
| 77 | `CM_Get_Class_Name_ExW` | `0x1E960` | 44 | UnwindData |  |
| 75 | `CM_Get_Class_NameW` | `0x1E9A0` | 274 | UnwindData |  |
| 79 | `CM_Get_Class_Property_ExW` | `0x1EAC0` | 62 | UnwindData |  |
| 78 | `CM_Get_Class_PropertyW` | `0x1EB10` | 228 | UnwindData |  |
| 266 | `DevFreeObjectProperties` | `0x1F550` | 80 | UnwindData |  |
| 212 | `CM_Register_Notification` | `0x1F620` | 23 | UnwindData |  |
| 7 | `CMP_Register_Notification` | `0x1F640` | 1,427 | UnwindData |  |
| 267 | `DevFreeObjects` | `0x1FBE0` | 142 | UnwindData |  |
| 265 | `DevFindProperty` | `0x1FC80` | 210 | UnwindData |  |
| 176 | `CM_MapCrToWin32Err` | `0x1FD60` | 150 | UnwindData |  |
| 175 | `CM_MapCrToSpErr` | `0x1FE00` | 2,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `CM_Free_Log_Conf_Handle` | `0x20610` | 110 | UnwindData |  |
| 256 | `CM_Unregister_Notification` | `0x20700` | 438 | UnwindData |  |
| 9 | `CMP_WaitNoPendingInstallEvents` | `0x20920` | 521 | UnwindData |  |
| 66 | `CM_Free_Res_Des_Handle` | `0x21160` | 110 | UnwindData |  |
| 258 | `DevCloseObjectQuery` | `0x214A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `CM_Get_Device_IDW` | `0x214C0` | 21 | UnwindData |  |
| 274 | `SwDeviceCreate` | `0x214E0` | 1,478 | UnwindData |  |
| 149 | `CM_Get_Parent_Ex` | `0x21D10` | 40 | UnwindData |  |
| 84 | `CM_Get_Depth` | `0x21DC0` | 232 | UnwindData |  |
| 170 | `CM_Is_Version_Available_Ex` | `0x21FF0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `SwDeviceClose` | `0x22190` | 280 | UnwindData |  |
| 195 | `CM_Query_And_Remove_SubTree_ExA` | `0x222C0` | 289 | UnwindData |  |
| 109 | `CM_Get_Device_ID_List_SizeW` | `0x223F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `CM_Get_Device_ID_Size` | `0x22400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `CM_Create_DevNode_ExW` | `0x22410` | 44 | UnwindData |  |
| 26 | `CM_Create_DevNodeW` | `0x22450` | 527 | UnwindData |  |
| 69 | `CM_Get_Child_Ex` | `0x22670` | 40 | UnwindData |  |
| 11 | `CM_Add_Driver_PackageW` | `0x22860` | 281 | UnwindData |  |
| 158 | `CM_Get_Sibling_Ex` | `0x22EB0` | 40 | UnwindData |  |
| 171 | `CM_Locate_DevNodeA` | `0x22EE0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `CM_Get_DevNode_Custom_Property_ExW` | `0x23090` | 62 | UnwindData |  |
| 120 | `CM_Get_Device_Interface_List_ExA` | `0x230E0` | 328 | UnwindData |  |
| 44 | `CM_Disable_DevNode` | `0x23230` | 277 | UnwindData |  |
| 23 | `CM_Connect_MachineA` | `0x23610` | 115 | UnwindData |  |
| 24 | `CM_Connect_MachineW` | `0x23690` | 105 | UnwindData |  |
| 164 | `CM_Install_DriverW` | `0x23890` | 234 | UnwindData |  |
| 129 | `CM_Get_Device_Interface_Property_Keys_ExW` | `0x23BA0` | 44 | UnwindData |  |
| 128 | `CM_Get_Device_Interface_Property_KeysW` | `0x23BE0` | 104 | UnwindData |  |
| 162 | `CM_Install_DevNodeW` | `0x23C50` | 359 | UnwindData |  |
| 108 | `CM_Get_Device_ID_List_SizeA` | `0x23E30` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CMP_Get_Device_ID_List` | `0x23EF0` | 23 | UnwindData |  |
| 4 | `CMP_Get_Device_ID_List_Size` | `0x24210` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `CM_Delete_DevNode_Key_Ex` | `0x243B0` | 40 | UnwindData |  |
| 234 | `CM_Set_DevNode_Registry_PropertyA` | `0x25250` | 29 | UnwindData |  |
| 236 | `CM_Set_DevNode_Registry_Property_ExA` | `0x25280` | 360 | UnwindData |  |
| 32 | `CM_Delete_DevNode_Key` | `0x25D10` | 230 | UnwindData |  |
| 1 | `CMP_GetBlockedDriverInfo` | `0x26860` | 74 | UnwindData |  |
| 2 | `CMP_GetServerSideDeviceInstallFlags` | `0x268B0` | 84 | UnwindData |  |
| 5 | `CMP_Init_Detection` | `0x26910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CMP_Report_LogOn` | `0x26930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `CMP_WaitServicesAvailable` | `0x26950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `CM_Disconnect_Machine` | `0x26970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `CM_Get_Global_State` | `0x26990` | 104 | UnwindData |  |
| 133 | `CM_Get_Global_State_Ex` | `0x26A00` | 40 | UnwindData |  |
| 159 | `CM_Get_Version` | `0x26A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `CM_Get_Version_Ex` | `0x26A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `CM_Query_Arbitrator_Free_Data` | `0x26A60` | 253 | UnwindData |  |
| 198 | `CM_Query_Arbitrator_Free_Data_Ex` | `0x26B70` | 52 | UnwindData |  |
| 199 | `CM_Query_Arbitrator_Free_Size` | `0x26BB0` | 259 | UnwindData |  |
| 200 | `CM_Query_Arbitrator_Free_Size_Ex` | `0x26CC0` | 44 | UnwindData |  |
| 223 | `CM_Run_Detection` | `0x26D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `CM_Run_Detection_Ex` | `0x26D20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `CM_Enumerate_EnumeratorsA` | `0x26D50` | 21 | UnwindData |  |
| 54 | `CM_Enumerate_EnumeratorsW` | `0x26D70` | 85 | UnwindData |  |
| 55 | `CM_Enumerate_Enumerators_ExA` | `0x26DD0` | 150 | UnwindData |  |
| 56 | `CM_Enumerate_Enumerators_ExW` | `0x26E70` | 44 | UnwindData |  |
| 85 | `CM_Get_Depth_Ex` | `0x26EB0` | 40 | UnwindData |  |
| 6 | `CMP_RegisterServiceNotification` | `0x26EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `CM_Apply_PowerScheme` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `CM_Delete_PowerScheme` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `CM_Duplicate_PowerScheme` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `CM_Import_PowerScheme` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `CM_Move_DevNode` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `CM_Move_DevNode_Ex` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `CM_Query_Remove_SubTree` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `CM_Query_Remove_SubTree_Ex` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `CM_Remove_SubTree` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `CM_Remove_SubTree_Ex` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `CM_RestoreAll_DefaultPowerSchemes` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `CM_Restore_DefaultPowerScheme` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `CM_Set_ActiveScheme` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `CM_Write_UserPowerKey` | `0x26EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `CM_Add_Driver_Package_ExW` | `0x26F00` | 277 | UnwindData |  |
| 38 | `CM_Delete_Driver_PackageW` | `0x27020` | 224 | UnwindData |  |
| 39 | `CM_Delete_Driver_Package_ExW` | `0x27110` | 217 | UnwindData |  |
| 251 | `CM_Uninstall_DriverW` | `0x271F0` | 234 | UnwindData |  |
| 13 | `CM_Add_Empty_Log_Conf` | `0x27310` | 308 | UnwindData |  |
| 14 | `CM_Add_Empty_Log_Conf_Ex` | `0x27450` | 44 | UnwindData |  |
| 60 | `CM_Free_Log_Conf` | `0x27490` | 308 | UnwindData |  |
| 61 | `CM_Free_Log_Conf_Ex` | `0x275D0` | 40 | UnwindData |  |
| 142 | `CM_Get_Log_Conf_Priority` | `0x27600` | 298 | UnwindData |  |
| 143 | `CM_Get_Log_Conf_Priority_Ex` | `0x27730` | 40 | UnwindData |  |
| 144 | `CM_Get_Next_Log_Conf` | `0x27760` | 317 | UnwindData |  |
| 145 | `CM_Get_Next_Log_Conf_Ex` | `0x278B0` | 40 | UnwindData |  |
| 15 | `CM_Add_IDA` | `0x27970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `CM_Add_IDW` | `0x27980` | 229 | UnwindData |  |
| 17 | `CM_Add_ID_ExA` | `0x27A70` | 128 | UnwindData |  |
| 18 | `CM_Add_ID_ExW` | `0x27B00` | 40 | UnwindData |  |
| 25 | `CM_Create_DevNodeA` | `0x27B30` | 21 | UnwindData |  |
| 27 | `CM_Create_DevNode_ExA` | `0x27B50` | 140 | UnwindData |  |
| 45 | `CM_Disable_DevNode_Ex` | `0x27BF0` | 40 | UnwindData |  |
| 193 | `CM_Query_And_Remove_SubTreeA` | `0x27C20` | 29 | UnwindData |  |
| 205 | `CM_Reenumerate_DevNode_Ex` | `0x27C50` | 40 | UnwindData |  |
| 206 | `CM_Register_Device_Driver` | `0x27C80` | 218 | UnwindData |  |
| 207 | `CM_Register_Device_Driver_Ex` | `0x27D60` | 40 | UnwindData |  |
| 215 | `CM_Request_Device_EjectA` | `0x27D90` | 29 | UnwindData |  |
| 216 | `CM_Request_Device_EjectW` | `0x27DC0` | 324 | UnwindData |  |
| 217 | `CM_Request_Device_Eject_ExA` | `0x27F10` | 292 | UnwindData |  |
| 218 | `CM_Request_Device_Eject_ExW` | `0x28040` | 52 | UnwindData |  |
| 230 | `CM_Set_DevNode_Problem` | `0x28080` | 283 | UnwindData |  |
| 231 | `CM_Set_DevNode_Problem_Ex` | `0x281B0` | 40 | UnwindData |  |
| 19 | `CM_Add_Range` | `0x282D0` | 197 | UnwindData |  |
| 29 | `CM_Create_Range_List` | `0x283A0` | 274 | UnwindData |  |
| 41 | `CM_Delete_Range` | `0x284C0` | 427 | UnwindData |  |
| 47 | `CM_Dup_Range_List` | `0x28680` | 284 | UnwindData |  |
| 58 | `CM_Find_Range` | `0x287B0` | 476 | UnwindData |  |
| 59 | `CM_First_Range` | `0x289A0` | 247 | UnwindData |  |
| 63 | `CM_Free_Range_List` | `0x28AA0` | 200 | UnwindData |  |
| 165 | `CM_Intersect_Range_List` | `0x28B70` | 569 | UnwindData |  |
| 166 | `CM_Invert_Range_List` | `0x28DB0` | 398 | UnwindData |  |
| 177 | `CM_Merge_Range_List` | `0x28F50` | 777 | UnwindData |  |
| 182 | `CM_Next_Range` | `0x29260` | 211 | UnwindData |  |
| 248 | `CM_Test_Range_Available` | `0x29340` | 225 | UnwindData |  |
| 20 | `CM_Add_Res_Des` | `0x29620` | 650 | UnwindData |  |
| 21 | `CM_Add_Res_Des_Ex` | `0x298B0` | 60 | UnwindData |  |
| 42 | `CM_Detect_Resource_Conflict` | `0x29900` | 39 | UnwindData |  |
| 43 | `CM_Detect_Resource_Conflict_Ex` | `0x29930` | 456 | UnwindData |  |
| 64 | `CM_Free_Res_Des` | `0x29B00` | 408 | UnwindData |  |
| 65 | `CM_Free_Res_Des_Ex` | `0x29CA0` | 40 | UnwindData |  |
| 178 | `CM_Modify_Res_Des` | `0x29CD0` | 659 | UnwindData |  |
| 179 | `CM_Modify_Res_Des_Ex` | `0x29F70` | 60 | UnwindData |  |
| 30 | `CM_Delete_Class_Key` | `0x2A180` | 72 | UnwindData |  |
| 31 | `CM_Delete_Class_Key_Ex` | `0x2A1D0` | 40 | UnwindData |  |
| 34 | `CM_Delete_Device_Interface_KeyA` | `0x2A200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `CM_Delete_Device_Interface_KeyW` | `0x2A210` | 68 | UnwindData |  |
| 36 | `CM_Delete_Device_Interface_Key_ExA` | `0x2A260` | 117 | UnwindData |  |
| 37 | `CM_Delete_Device_Interface_Key_ExW` | `0x2A2E0` | 40 | UnwindData |  |
| 70 | `CM_Get_Class_Key_NameA` | `0x2A310` | 21 | UnwindData |  |
| 71 | `CM_Get_Class_Key_NameW` | `0x2A330` | 144 | UnwindData |  |
| 72 | `CM_Get_Class_Key_Name_ExA` | `0x2A3D0` | 143 | UnwindData |  |
| 73 | `CM_Get_Class_Key_Name_ExW` | `0x2A470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `CM_Get_Class_NameA` | `0x2A480` | 21 | UnwindData |  |
| 76 | `CM_Get_Class_Name_ExA` | `0x2A4A0` | 156 | UnwindData |  |
| 82 | `CM_Get_Class_Registry_PropertyA` | `0x2A550` | 399 | UnwindData |  |
| 83 | `CM_Get_Class_Registry_PropertyW` | `0x2A6F0` | 823 | UnwindData |  |
| 86 | `CM_Get_DevNode_Custom_PropertyA` | `0x2AA30` | 39 | UnwindData |  |
| 88 | `CM_Get_DevNode_Custom_Property_ExA` | `0x2AA60` | 706 | UnwindData |  |
| 114 | `CM_Get_Device_Interface_AliasA` | `0x2AD30` | 29 | UnwindData |  |
| 116 | `CM_Get_Device_Interface_Alias_ExA` | `0x2AD60` | 388 | UnwindData |  |
| 118 | `CM_Get_Device_Interface_ListA` | `0x2AEF0` | 29 | UnwindData |  |
| 183 | `CM_Open_Class_KeyA` | `0x2AF20` | 39 | UnwindData |  |
| 185 | `CM_Open_Class_Key_ExA` | `0x2AF50` | 180 | UnwindData |  |
| 189 | `CM_Open_Device_Interface_KeyA` | `0x2B010` | 29 | UnwindData |  |
| 191 | `CM_Open_Device_Interface_Key_ExA` | `0x2B040` | 151 | UnwindData |  |
| 208 | `CM_Register_Device_InterfaceA` | `0x2B0E0` | 39 | UnwindData |  |
| 209 | `CM_Register_Device_InterfaceW` | `0x2B110` | 284 | UnwindData |  |
| 210 | `CM_Register_Device_Interface_ExA` | `0x2B240` | 418 | UnwindData |  |
| 211 | `CM_Register_Device_Interface_ExW` | `0x2B3F0` | 62 | UnwindData |  |
| 228 | `CM_Set_Class_Registry_PropertyA` | `0x2B440` | 360 | UnwindData |  |
| 229 | `CM_Set_Class_Registry_PropertyW` | `0x2B5B0` | 919 | UnwindData |  |
| 252 | `CM_Unregister_Device_InterfaceA` | `0x2B950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `CM_Unregister_Device_InterfaceW` | `0x2B960` | 68 | UnwindData |  |
| 254 | `CM_Unregister_Device_Interface_ExA` | `0x2B9B0` | 182 | UnwindData |  |
| 255 | `CM_Unregister_Device_Interface_ExW` | `0x2BA70` | 40 | UnwindData |  |
| 57 | `CM_Export_Pnp_StateW` | `0x2BAA0` | 234 | UnwindData |  |
| 67 | `CM_Free_Resource_Conflict_Handle` | `0x2BB90` | 165 | UnwindData |  |
| 154 | `CM_Get_Resource_Conflict_Count` | `0x2BC40` | 85 | UnwindData |  |
| 155 | `CM_Get_Resource_Conflict_DetailsA` | `0x2BCA0` | 312 | UnwindData |  |
| 156 | `CM_Get_Resource_Conflict_DetailsW` | `0x2BDE0` | 750 | UnwindData |  |
| 203 | `CM_Query_Resource_Conflict_List` | `0x2C0E0` | 1,040 | UnwindData |  |
| 80 | `CM_Get_Class_Property_Keys` | `0x2C520` | 193 | UnwindData |  |
| 81 | `CM_Get_Class_Property_Keys_Ex` | `0x2C5F0` | 44 | UnwindData |  |
| 226 | `CM_Set_Class_PropertyW` | `0x2C630` | 220 | UnwindData |  |
| 227 | `CM_Set_Class_Property_ExW` | `0x2C720` | 60 | UnwindData |  |
| 134 | `CM_Get_HW_Prof_FlagsA` | `0x2C770` | 21 | UnwindData |  |
| 136 | `CM_Get_HW_Prof_Flags_ExA` | `0x2C790` | 132 | UnwindData |  |
| 138 | `CM_Get_Hardware_Profile_InfoA` | `0x2C820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `CM_Get_Hardware_Profile_InfoW` | `0x2C830` | 72 | UnwindData |  |
| 140 | `CM_Get_Hardware_Profile_Info_ExA` | `0x2C880` | 221 | UnwindData |  |
| 141 | `CM_Get_Hardware_Profile_Info_ExW` | `0x2C970` | 40 | UnwindData |  |
| 167 | `CM_Is_Dock_Station_Present` | `0x2C9A0` | 186 | UnwindData |  |
| 168 | `CM_Is_Dock_Station_Present_Ex` | `0x2CA60` | 40 | UnwindData |  |
| 219 | `CM_Request_Eject_PC` | `0x2CA90` | 173 | UnwindData |  |
| 220 | `CM_Request_Eject_PC_Ex` | `0x2CB50` | 40 | UnwindData |  |
| 240 | `CM_Set_HW_Prof` | `0x2CB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `CM_Set_HW_Prof_Ex` | `0x2CBA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `CM_Set_HW_Prof_FlagsA` | `0x2CBD0` | 21 | UnwindData |  |
| 244 | `CM_Set_HW_Prof_Flags_ExA` | `0x2CBF0` | 132 | UnwindData |  |
| 163 | `CM_Install_DevNode_ExW` | `0x2CC80` | 241 | UnwindData |  |
| 263 | `DevCreateObjectQueryFromIds` | `0x324F0` | 99 | UnwindData |  |
| 264 | `DevCreateObjectQueryFromIdsEx` | `0x32560` | 293 | UnwindData |  |
| 275 | `SwDeviceGetAttributes` | `0x32CA0` | 83 | UnwindData |  |
| 281 | `SwDeviceSetAttributes` | `0x32D00` | 65 | UnwindData |  |
