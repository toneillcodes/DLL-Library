# Binary Specification: dmdskmgr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dmdskmgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6eea0050f6d5435235c5e064664ee1e6c8b13db61afd2484740522f99f865242`
* **Total Exported Functions:** 233

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 129 | `?GetResultStringArray@CDMNodeObj@@QEAAHAEAVCStringArray@@@Z` | `0x1CD0` | 483 | UnwindData |  |
| 84 | `?GetDriveLetter@CDMNodeObj@@QEAAXAEAG@Z` | `0x1EC0` | 233 | UnwindData |  |
| 117 | `?GetParentDiskPtr@CDMNodeObj@@QEAAPEAV1@XZ` | `0x20A0` | 120 | UnwindData |  |
| 83 | `?GetDiskTypeName@CDMNodeObj@@QEAAXAEAVCString@@@Z` | `0x2120` | 449 | UnwindData |  |
| 53 | `?FindDriveLetter@CDataCache@@QEAAH_JAEAG@Z` | `0x22F0` | 202 | UnwindData |  |
| 138 | `?GetSizeString@CDMNodeObj@@QEAAXAEAVCString@@@Z` | `0x4F90` | 569 | UnwindData |  |
| 90 | `?GetFileSystemName@CDMNodeObj@@QEAAXAEAVCString@@@Z` | `0x5260` | 665 | UnwindData |  |
| 150 | `?GetVolumeStatus@CDMNodeObj@@QEAAHAEAVCString@@@Z` | `0x5590` | 1,296 | UnwindData |  |
| 88 | `?GetExtraRegionStatus@CDMNodeObj@@QEAAHAEAVCString@@H@Z` | `0x5AB0` | 2,614 | UnwindData |  |
| 110 | `?GetName@CDMNodeObj@@QEAAXAEAVCString@@@Z` | `0x6580` | 876 | UnwindData |  |
| 128 | `?GetResultPane@CDMSnapin@@QEAAH_JPEAPEAVCDMResultPane@@@Z` | `0x6900` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `?GetColorRef@CDMNodeObj@@QEAAKXZ` | `0x6960` | 337 | UnwindData |  |
| 118 | `?GetParentVolumePtr@CDMNodeObj@@QEAAPEAV1@XZ` | `0x6AC0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `?IsActive@CDMNodeObj@@QEAAHXZ` | `0x6B40` | 264 | UnwindData |  |
| 40 | `?EnumDiskRegions@CDMNodeObj@@QEAAXPEAPEA_JAEAJ@Z` | `0x6C50` | 156 | UnwindData |  |
| 89 | `?GetFileSystemLabel@CDMNodeObj@@QEAAXAEAVCString@@@Z` | `0x6D00` | 528 | UnwindData |  |
| 141 | `?GetStorageType@CDMNodeObj@@QEAA?AW4_STORAGE_TYPES@@XZ` | `0x6F20` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `?GetRegionInfo@CDMNodeObj@@QEAAHAEAUregioninfoex@@@Z` | `0x7010` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `?ContainsSubDiskNeedResync@CDMNodeObj@@QEAAHXZ` | `0x70A0` | 539 | UnwindData |  |
| 55 | `?FindFileSystem@CDataCache@@QEAAH_JAEAUfilesysteminfo@@@Z` | `0x74E0` | 225 | UnwindData |  |
| 57 | `?FindRegionPtrFromRegionId@CDataCache@@QEAAH_JPEAPEAVCDMNodeObj@@@Z` | `0x75D0` | 170 | UnwindData |  |
| 113 | `?GetObjectId@CDMNodeObj@@QEAAXAEA_J@Z` | `0x7E50` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `?IsFakeVolume@CDMNodeObj@@QEAAHXZ` | `0x7F90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `?EnumFirstVolumeMember@CDMNodeObj@@QEAAXAEA_JAEAJ@Z` | `0x7FC0` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `?GetFlags@CDMNodeObj@@QEAAJXZ` | `0x8300` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `?GetSizeMB@CDMNodeObj@@QEAAXAEA_J@Z` | `0x84A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `?GetSize@CDMNodeObj@@QEAAXAEA_JH@Z` | `0x84F0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `?GetUIState@CTaskData@@QEAAKXZ` | `0x8720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `?GetPatternRef@CDMNodeObj@@QEAAHXZ` | `0x8730` | 187 | UnwindData |  |
| 126 | `?GetRegionColorStructPtr@CTaskData@@QEAAXPEAPEAU_REGION_COLORS@@AEAH@Z` | `0x8800` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `?GetDiskStatus@CDMNodeObj@@QEAAHAEAVCString@@@Z` | `0x8870` | 58 | UnwindData |  |
| 99 | `?GetImageNum@CDMNodeObj@@QEAAHXZ` | `0x8AF0` | 442 | UnwindData |  |
| 66 | `?GetDeviceAttributes@CDMNodeObj@@QEAAKXZ` | `0x8CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `?GetLayoutType@CDMNodeObj@@QEAA?AW4_LAYOUT_TYPES@@XZ` | `0x8CD0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `?GetPartitionStyleString@CDMNodeObj@@QEAAXAEAVCString@@H@Z` | `0x8DC0` | 706 | UnwindData |  |
| 28 | `?CreateRegionNodeObj@CDataCache@@QEAAPEAVCDMNodeObj@@PEAV2@PEAUregioninfoex@@@Z` | `0x9090` | 516 | UnwindData |  |
| 208 | `?RecalculateSpace@CDMNodeObj@@QEAAXXZ` | `0x92A0` | 218 | UnwindData |  |
| 68 | `?GetDeviceType@CDMNodeObj@@QEAAKXZ` | `0x9380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `?IsDiskOffline@CDMNodeObj@@QEAAHXZ` | `0x93A0` | 51 | UnwindData |  |
| 188 | `?IsPreLonghornVdsVersion@CDataCache@@QEAAHXZ` | `0x93E0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `?IsFTVolume@CDMNodeObj@@QEAAHXZ` | `0x94C0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `?GetDeviceState@CDMNodeObj@@QEAAKXZ` | `0x95E0` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `?EnumVolumeMembers@CDMNodeObj@@QEAAXPEAPEA_JAEAJ@Z` | `0x9900` | 198 | UnwindData |  |
| 130 | `?GetScopeNode@CDMScopeNodeCollection@@QEAAH_JPEAPEAVCDMScopeNode@@@Z` | `0x9C00` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `?AddLDMObjMapEntry@CDataCache@@QEAAXPEAU_LDM_OBJ_MAP_ENTRY@@@Z` | `0x9DD0` | 151 | UnwindData |  |
| 119 | `?GetPartitionStyle@CDMNodeObj@@QEAA?AW4_PARTITIONSTYLE@@XZ` | `0xA510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `?GetIVolumeClientVersion@CDMNodeObj@@QEAAFXZ` | `0xA530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `?GetNumMembers@CDMNodeObj@@QEAAKXZ` | `0xA550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `?GetNumRegions@CDMNodeObj@@QEAAKXZ` | `0xA560` | 6,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `?GetDiskCount@CDataCache@@QEAAKXZ` | `0xBF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `?GetLdmObjectId@CDMNodeObj@@QEAA_JXZ` | `0xBF50` | 31 | UnwindData |  |
| 114 | `?GetOcxFrameCWndPtr@CTaskData@@QEAAPEAVCWnd@@XZ` | `0xBF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `?GetServerName@CDataCache@@QEAA?AVCString@@XZ` | `0xBF90` | 41 | UnwindData |  |
| 147 | `?GetVolumeCount@CDataCache@@QEAAKXZ` | `0xBFC0` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `?PopulateDiskGroupData@CDataCache@@QEAAXPEAUDISK_GROUP_DATA@@@Z` | `0xC260` | 2,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `?Command@CContextMenu@@QEAAJJPEAUIDataObject@@_J@Z` | `0xCD50` | 1,482 | UnwindData |  |
| 36 | `?DoDelete@CContextMenu@@QEAAX_J@Z` | `0xF1F0` | 1,792 | UnwindData |  |
| 37 | `?DoRevertToNT4@CContextMenu@@QEAAX_JH@Z` | `0x10ED0` | 337 | UnwindData |  |
| 205 | `?PopUpInit@CContextMenu@@QEAAXPEAVCDMNodeObj@@AEAH1H@Z` | `0x11830` | 4,994 | UnwindData |  |
| 210 | `?RefreshFileSys@CContextMenu@@QEAAX_J@Z` | `0x13280` | 65 | UnwindData |  |
| 220 | `?ShowContextMenu@CContextMenu@@QEAAJPEAVCWnd@@JJ_J@Z` | `0x133D0` | 318 | UnwindData |  |
| 1 | `??0CDataCache@@QEAA@XZ` | `0x140A0` | 867 | UnwindData |  |
| 3 | `??1CDataCache@@UEAA@XZ` | `0x145C0` | 346 | UnwindData |  |
| 4 | `?AddFileSystemInfoToCache@CDataCache@@QEAAXKPEAUfilesysteminfo@@@Z` | `0x14A20` | 157 | UnwindData |  |
| 5 | `?AddFileSystemInfoToListAndMap@CDataCache@@QEAAXKPEAUfilesysteminfo@@@Z` | `0x14AD0` | 185 | UnwindData |  |
| 7 | `?AddRegionToVolumeMemberList@CDataCache@@QEAAXPEAVCDMNodeObj@@@Z` | `0x14B90` | 162 | UnwindData |  |
| 9 | `?AdjustRegionCountInLegendList@CDataCache@@QEAAXW4_REGIONTYPE@@HPEAVCTaskData@@@Z` | `0x14D10` | 78 | UnwindData |  |
| 10 | `?AdjustVolumeCountInLegendList@CDataCache@@QEAAXW4_VOLUMELAYOUT@@HPEAVCTaskData@@@Z` | `0x14D70` | 81 | UnwindData |  |
| 26 | `?CreateDiskList@CDataCache@@QEAAXXZ` | `0x14DD0` | 167 | UnwindData |  |
| 27 | `?CreateNodeObjAndAddToMap@CDataCache@@QEAAPEAVCDMNodeObj@@HW4_NODEOBJ_TYPES@@PEAV1@PEAX_J@Z` | `0x14E80` | 431 | UnwindData |  |
| 29 | `?CreateShortDiskName@CDataCache@@QEAAXAEAUdiskinfoex@@@Z` | `0x15040` | 460 | UnwindData |  |
| 30 | `?CreateVolumeList@CDataCache@@QEAAXXZ` | `0x15220` | 359 | UnwindData |  |
| 31 | `?DeleteDiskGroupData@CDataCache@@QEAAXPEAUDISK_GROUP_DATA@@@Z` | `0x15390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `?DeleteEncapsulateData@CDataCache@@QEAAXPEAUENCAPSULATE_DATA@@@Z` | `0x153B0` | 141 | UnwindData |  |
| 33 | `?DeleteLists@CDataCache@@QEAAXXZ` | `0x15450` | 583 | UnwindData |  |
| 34 | `?DeleteRegionFromVolumeMemberList@CDataCache@@QEAAXPEAVCDMNodeObj@@@Z` | `0x156A0` | 220 | UnwindData |  |
| 43 | `?EnumNTFSwithDriveLetter@CDataCache@@QEAAXPEAHPEAPEAG@Z` | `0x15790` | 265 | UnwindData |  |
| 47 | `?FillDeviceInstanceId@CDataCache@@QEAAXPEAG0@Z` | `0x158A0` | 274 | UnwindData |  |
| 50 | `?FindCookieAndRemoveFromList@CDataCache@@QEAAH_JPEAV?$CList@PEAVCDMNodeObj@@PEAV1@@@@Z` | `0x159C0` | 111 | UnwindData |  |
| 51 | `?FindDeviceInstanceId@CDataCache@@QEAAPEAG_J@Z` | `0x15A40` | 122 | UnwindData |  |
| 52 | `?FindDiskPtrFromDiskId@CDataCache@@QEAAH_JPEAPEAVCDMNodeObj@@@Z` | `0x15AC0` | 138 | UnwindData |  |
| 59 | `?FindRegionPtrOnDiskFromRegionId@CDataCache@@QEAAHPEAVCDMNodeObj@@_JPEAPEAV2@AEAPEAU__POSITION@@@Z` | `0x15B50` | 157 | UnwindData |  |
| 61 | `?GetBootPort@CDataCache@@QEAAHXZ` | `0x15C90` | 115 | UnwindData |  |
| 64 | `?GetComponentData@CDataCache@@QEAAPEAVCDMComponentData@@XZ` | `0x15D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `?GetDiskCookies@CDataCache@@IEAAXAEAKPEAPEA_J@Z` | `0x15D30` | 190 | UnwindData |  |
| 85 | `?GetDriveLetters@CDataCache@@IEAAXAEAFPEAPEAGG@Z` | `0x15E00` | 269 | UnwindData |  |
| 93 | `?GetFileSystemTypes@CDataCache@@QEAAXAEAKPEAPEAUifilesysteminfo@@@Z` | `0x15F20` | 112 | UnwindData |  |
| 100 | `?GetLastKnownState@CDataCache@@QEAA_J_J@Z` | `0x15FA0` | 161 | UnwindData |  |
| 108 | `?GetMinMaxPartitionSizes@CDataCache@@IEAAX_JAEA_J1@Z` | `0x16050` | 210 | UnwindData |  |
| 124 | `GetPropertyPageData` | `0x16130` | 2,316 | UnwindData |  |
| 146 | `?GetVolumeCookies@CDataCache@@IEAAXAEAKPEAPEA_J@Z` | `0x16B10` | 190 | UnwindData |  |
| 153 | `?HasNTFSwithDriveLetter@CDataCache@@QEAAHXZ` | `0x16BE0` | 94 | UnwindData |  |
| 155 | `?HasVMDisk@CDataCache@@QEAAHXZ` | `0x16C50` | 94 | UnwindData |  |
| 157 | `?IsAlpha@CDataCache@@QEAAHXZ` | `0x16CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `?IsDynamic1394@CDataCache@@QEAAHXZ` | `0x16CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `?IsEfi@CDataCache@@QEAAHXZ` | `0x16CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `?IsNEC_98Server@CDataCache@@QEAAHXZ` | `0x16D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `?IsPersonalOrLapTopServer@CDataCache@@QEAAHXZ` | `0x16D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `?IsPostLonghornVdsVersion@CDataCache@@QEAAHXZ` | `0x16D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `IsRequestPending` | `0x16D60` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `?IsWolfpack@CDataCache@@QEAAHXZ` | `0x16E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `LoadPropertyPageData` | `0x16EB0` | 264 | UnwindData |  |
| 207 | `?PopulateEncapsulateData@CDataCache@@QEAAXPEAUENCAPSULATE_DATA@@@Z` | `0x17380` | 429 | UnwindData |  |
| 213 | `?SetDiskList@CDataCache@@QEAAXPEAUdiskinfoex@@K@Z` | `0x179C0` | 206 | UnwindData |  |
| 214 | `?SetDriveLetterInUse@CDataCache@@QEAAXGH@Z` | `0x17AA0` | 238 | UnwindData |  |
| 219 | `?SetVolumeList@CDataCache@@QEAAXPEAUvolumeinfo@@KPEAVCTaskData@@@Z` | `0x17BA0` | 177 | UnwindData |  |
| 221 | `?SupportGpt@CDataCache@@QEAAHXZ` | `0x17C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `?SupportMirror@CDataCache@@QEAAHXZ` | `0x17C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `?SupportRaid5@CDataCache@@QEAAHXZ` | `0x17C80` | 7,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `?AddRow@CDMComponentData@@QEAAXPEAVCDMScopeNode@@_J@Z` | `0x19A00` | 77 | UnwindData |  |
| 12 | `?ChangeRow@CDMComponentData@@QEAAXPEAVCDMScopeNode@@_J@Z` | `0x19A60` | 77 | UnwindData |  |
| 35 | `?DeleteRow@CDMComponentData@@QEAAXPEAVCDMScopeNode@@_J@Z` | `0x19F20` | 77 | UnwindData |  |
| 38 | `?EmptyOcxViewData@CDMComponentData@@QEAAXPEAVCDMScopeNode@@@Z` | `0x1A0E0` | 80 | UnwindData |  |
| 105 | `?GetMMCWindow@CDMComponentData@@QEAAPEAUHWND__@@XZ` | `0x1A2D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `?GetScopeNodeForResultPane@CDMComponentData@@QEAAH_JPEAPEAVCDMScopeNode@@@Z` | `0x1A300` | 81 | UnwindData |  |
| 200 | `?LoadData@CDMComponentData@@QEAAXPEAVCDMScopeNode@@J@Z` | `0x1A920` | 105 | UnwindData |  |
| 209 | `?RefreshDiskView@CDMComponentData@@QEAAXPEAVCDMScopeNode@@@Z` | `0x1B0F0` | 64 | UnwindData |  |
| 211 | `?ReloadData@CDMComponentData@@QEAAXPEAVCDMScopeNode@@@Z` | `0x1B2D0` | 92 | UnwindData |  |
| 216 | `?SetOcxViewType@CDMComponentData@@QEAAXPEAVCDMScopeNode@@@Z` | `0x1B510` | 151 | UnwindData |  |
| 217 | `?SetOcxViewTypeForce@CDMComponentData@@QEAAXPEAVCDMScopeNode@@@Z` | `0x1B5B0` | 55 | UnwindData |  |
| 225 | `?UIStateChange@CDMComponentData@@QEAAXPEAVCDMScopeNode@@K@Z` | `0x1B5F0` | 80 | UnwindData |  |
| 230 | `DllCanUnloadNow` | `0x1BF30` | 121 | UnwindData |  |
| 231 | `DllGetClassObject` | `0x1BFB0` | 161 | UnwindData |  |
| 232 | `DllRegisterServer` | `0x1C060` | 77 | UnwindData |  |
| 212 | `?SetDescriptionBarText@CDMSnapin@@QEAAX_J@Z` | `0x1ECA0` | 446 | UnwindData |  |
| 226 | `?UpDateConsoleView@CDMSnapin@@QEAAX_J@Z` | `0x1F030` | 413 | UnwindData |  |
| 2 | `??1CDMNodeObj@@QEAA@XZ` | `0x1FFD0` | 67 | UnwindData |  |
| 11 | `?CanHaveGPT@CDMNodeObj@@QEAAHXZ` | `0x20020` | 102 | UnwindData |  |
| 14 | `?ContainsActivePartition@CDMNodeObj@@QEAAHXZ` | `0x20090` | 47 | UnwindData |  |
| 15 | `?ContainsBootIniPartition@CDMNodeObj@@QEAAHXZ` | `0x200D0` | 73 | UnwindData |  |
| 16 | `?ContainsBootIniPartitionForWolfpack@CDMNodeObj@@QEAAHXZ` | `0x20120` | 127 | UnwindData |  |
| 17 | `?ContainsBootVolumesNumberChange@CDMNodeObj@@QEAAH_JPEAH@Z` | `0x201B0` | 148 | UnwindData |  |
| 18 | `?ContainsESPPartition@CDMNodeObj@@QEAAHXZ` | `0x20250` | 178 | UnwindData |  |
| 19 | `?ContainsFVEPartition@CDMNodeObj@@QEAAHXZ` | `0x20310` | 44 | UnwindData |  |
| 20 | `?ContainsLogicalDrvBootPartition@CDMNodeObj@@QEAAHXZ` | `0x20350` | 72 | UnwindData |  |
| 21 | `?ContainsPageFile@CDMNodeObj@@QEAAHXZ` | `0x203A0` | 47 | UnwindData |  |
| 22 | `?ContainsRealSystemPartition@CDMNodeObj@@QEAAHXZ` | `0x203E0` | 109 | UnwindData |  |
| 24 | `?ContainsSystemInformation@CDMNodeObj@@QEAAHXZ` | `0x20460` | 109 | UnwindData |  |
| 25 | `?ContainsSystemPartition@CDMNodeObj@@QEAAHXZ` | `0x204E0` | 47 | UnwindData |  |
| 39 | `?EnhancedIsUpgradeable@CDMNodeObj@@QEAAHPEAVCTaskData@@@Z` | `0x20520` | 352 | UnwindData |  |
| 79 | `?GetDiskInfo@CDMNodeObj@@QEAAHAEAUdiskinfoex@@@Z` | `0x20780` | 160 | UnwindData |  |
| 81 | `?GetDiskSpec@CDMNodeObj@@QEAAHAEAUdiskspec@@@Z` | `0x20830` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `?GetExtendedRegionColor@CDMNodeObj@@QEAAKXZ` | `0x20870` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `?GetFileSystemSize@CDMNodeObj@@QEAAXAEAJ@Z` | `0x208C0` | 228 | UnwindData |  |
| 92 | `?GetFileSystemType@CDMNodeObj@@QEAAHXZ` | `0x209B0` | 122 | UnwindData |  |
| 98 | `?GetIconId@CDMNodeObj@@QEAAIH@Z` | `0x20A30` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `?GetLogicalDriveCount@CDMNodeObj@@QEAAKXZ` | `0x20AF0` | 70 | UnwindData |  |
| 104 | `?GetLongName@CDMNodeObj@@QEAAXAEAVCString@@H@Z` | `0x20B40` | 389 | UnwindData |  |
| 106 | `?GetMaxAdjustedFreeSize@CDMNodeObj@@QEAAXAEA_J@Z` | `0x20CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `?GetMaxPartitionCount@CDMNodeObj@@QEAAKXZ` | `0x20CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `?GetOfflineReasonText@CDMNodeObj@@QEAAHAEAVCString@@@Z` | `0x20D10` | 200 | UnwindData |  |
| 122 | `?GetPort@CDMNodeObj@@QEAAHXZ` | `0x20E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `?GetPrimaryPartitionCount@CDMNodeObj@@QEAAKXZ` | `0x20E60` | 70 | UnwindData |  |
| 125 | `?GetRegionByOffset@CDMNodeObj@@QEAAPEAV1@_J@Z` | `0x20EB0` | 84 | UnwindData |  |
| 134 | `?GetShortName@CDMNodeObj@@QEAAXAEAVCString@@@Z` | `0x20F10` | 409 | UnwindData |  |
| 135 | `?GetShrinkableSizeInMB@CDMNodeObj@@QEAA_JXZ` | `0x210B0` | 67 | UnwindData |  |
| 139 | `?GetStartOffset@CDMNodeObj@@QEAA_JXZ` | `0x21100` | 46 | UnwindData |  |
| 140 | `?GetStatus@CDMNodeObj@@QEAAHXZ` | `0x21140` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `?GetStorageType@CDMNodeObj@@QEAAXAEAVCString@@H@Z` | `0x21180` | 1,238 | UnwindData |  |
| 144 | `?GetUnallocSpace@CDMNodeObj@@QEAA_JH@Z` | `0x21660` | 314 | UnwindData |  |
| 145 | `?GetUsableContiguousSpaceInMB@CDMNodeObj@@QEAA_JXZ` | `0x217A0` | 51 | UnwindData |  |
| 148 | `?GetVolumeFileSystemTypes@CDMNodeObj@@QEAAJAEAKPEAPEAUilhfilesysteminfo@@@Z` | `0x217E0` | 99 | UnwindData |  |
| 149 | `?GetVolumeInfo@CDMNodeObj@@QEAAHAEAUvolumeinfo@@@Z` | `0x21850` | 97 | UnwindData |  |
| 151 | `?GetVolumeTotalSizeMB@CDMNodeObj@@QEAA_JXZ` | `0x218C0` | 77 | UnwindData |  |
| 152 | `?HasExtendedPartition@CDMNodeObj@@QEAAHXZ` | `0x21920` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `?IsConvertSuccess@CDMNodeObj@@QEAAJH@Z` | `0x219C0` | 106 | UnwindData |  |
| 160 | `?IsCurrBootVolume@CDMNodeObj@@QEAAHXZ` | `0x21A30` | 104 | UnwindData |  |
| 161 | `?IsCurrSystemVolume@CDMNodeObj@@QEAAHXZ` | `0x21AA0` | 121 | UnwindData |  |
| 162 | `?IsDiskEmpty@CDMNodeObj@@QEAAHXZ` | `0x21B20` | 480 | UnwindData |  |
| 164 | `?IsDiskReadOnly@CDMNodeObj@@QEAAHXZ` | `0x21D10` | 43 | UnwindData |  |
| 166 | `?IsEECoveredGPTDisk@CDMNodeObj@@QEAAHXZ` | `0x21D50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `?IsESPPartition@CDMNodeObj@@QEAAHXZ` | `0x21D80` | 141 | UnwindData |  |
| 170 | `?IsExtendedPartitionCreated@CDMNodeObj@@QEAAJXZ` | `0x21E20` | 94 | UnwindData |  |
| 173 | `?IsFirstFreeRegion@CDMNodeObj@@QEAAHXZ` | `0x21E90` | 427 | UnwindData |  |
| 174 | `?IsFreeSpaceFollowed@CDMNodeObj@@QEAAH_J@Z` | `0x22050` | 169 | UnwindData |  |
| 175 | `?IsHiddenRegion@CDMNodeObj@@QEAAHXZ` | `0x22100` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `?IsInFlux@CDMNodeObj@@QEAAHXZ` | `0x22180` | 18 | UnwindData |  |
| 178 | `?IsMbrEEPartition@CDMNodeObj@@QEAAHXZ` | `0x221A0` | 88 | UnwindData |  |
| 179 | `?IsMember@CDMNodeObj@@QEAAHPEAV1@@Z` | `0x22200` | 140 | UnwindData |  |
| 180 | `?IsNEC_98Disk@CDMNodeObj@@QEAAHXZ` | `0x222A0` | 136 | UnwindData |  |
| 184 | `?IsOemPartition@CDMNodeObj@@QEAAHXZ` | `0x22330` | 292 | UnwindData |  |
| 191 | `?IsRevertable@CDMNodeObj@@QEAAHXZ` | `0x22460` | 261 | UnwindData |  |
| 193 | `?IsSpacesProtectivePartition@CDMNodeObj@@QEAAHXZ` | `0x22570` | 141 | UnwindData |  |
| 194 | `?IsUnknownPartition@CDMNodeObj@@QEAAHXZ` | `0x22610` | 346 | UnwindData |  |
| 195 | `?IsUpgradeable@CDMNodeObj@@QEAAHXZ` | `0x22770` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `?IsVolumeArrived@CDMNodeObj@@QEAAJ_JW4_LAYOUT_TYPES@@@Z` | `0x227D0` | 138 | UnwindData |  |
| 197 | `?IsVolumeSimple@CDMNodeObj@@QEAAHXZ` | `0x22860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `?MarkDiskForLastVolume@CDMNodeObj@@QEAAXPEAV1@@Z` | `0x22880` | 145 | UnwindData |  |
| 203 | `?MarkDisksForLastVolume@CDMNodeObj@@QEAAXXZ` | `0x22920` | 239 | UnwindData |  |
| 204 | `?OnlyContiguousExtendAllowed@CDMNodeObj@@QEAAHXZ` | `0x22A20` | 190 | UnwindData |  |
| 215 | `?SetFSId@CDMNodeObj@@QEAAX_J@Z` | `0x22AF0` | 143 | UnwindData |  |
| 227 | `?VolumeContainsActiveRegion@CDMNodeObj@@QEAAHXZ` | `0x22BD0` | 130 | UnwindData |  |
| 41 | `?EnumDisks@CTaskData@@QEAAXAEAKPEAPEA_J@Z` | `0x25D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `?EnumNTFSwithDriveLetter@CTaskData@@QEAAXPEAHPEAPEAG@Z` | `0x25DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `?EnumVolumes@CTaskData@@QEAAXAEAKPEAPEA_J@Z` | `0x25DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `?FilterCookiesBigEnoughForFTRepair@CTaskData@@QEAAXAEAKPEA_JPEAPEA_J_JPEAVCDMNodeObj@@@Z` | `0x25DF0` | 637 | UnwindData |  |
| 49 | `?FilterCookiesBigEnoughForRAID5Repair@CTaskData@@QEAAXAEAKPEA_JPEAPEA_J_JPEAVCDMNodeObj@@@Z` | `0x26080` | 227 | UnwindData |  |
| 54 | `?FindDriveLetter@CTaskData@@QEAAX_JAEAG@Z` | `0x26170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `?FindFileSystem@CTaskData@@QEAAH_JAEAUfilesysteminfo@@@Z` | `0x26190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `?FindRegionPtrFromRegionId@CTaskData@@QEAAH_JPEAPEAVCDMNodeObj@@@Z` | `0x261B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?GetAssignedDriveLetter@CTaskData@@QEAAH_JAEAG@Z` | `0x261D0` | 34 | UnwindData |  |
| 62 | `?GetBootPort@CTaskData@@QEAAHXZ` | `0x26200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `?GetDMDataObjPtrFromId@CTaskData@@QEAAPEAVCDMNodeObj@@_J@Z` | `0x26220` | 66 | UnwindData |  |
| 70 | `?GetDiskCookies@CTaskData@@QEAAXAEAKPEAPEA_JHKH@Z` | `0x26270` | 254 | UnwindData |  |
| 71 | `?GetDiskCookiesForAddMirror@CTaskData@@QEAAX_JAEAKPEAPEA_J@Z` | `0x26380` | 553 | UnwindData |  |
| 72 | `?GetDiskCookiesForCreateVolume@CTaskData@@QEAAXAEAKPEAPEA_J@Z` | `0x265B0` | 279 | UnwindData |  |
| 73 | `?GetDiskCookiesForExtendVolume@CTaskData@@QEAAX_JAEAKPEAPEA_J@Z` | `0x266D0` | 155 | UnwindData |  |
| 74 | `?GetDiskCookiesForSig@CTaskData@@QEAAXAEAKPEAPEA_J@Z` | `0x26780` | 265 | UnwindData |  |
| 75 | `?GetDiskCookiesForUpgrade@CTaskData@@QEAAXAEAKPEAPEA_J@Z` | `0x26890` | 342 | UnwindData |  |
| 76 | `?GetDiskCookiesToEncap@CTaskData@@QEAAXAEAKPEAPEA_J@Z` | `0x269F0` | 257 | UnwindData |  |
| 77 | `?GetDiskCookiesWithFreeSpace@CTaskData@@QEAAXAEAKPEAPEA_J@Z` | `0x26B00` | 212 | UnwindData |  |
| 80 | `?GetDiskInfoFromVolCookie@CTaskData@@QEAAX_JAEAHAEAKPEAPEA_JKH@Z` | `0x26BE0` | 434 | UnwindData |  |
| 86 | `?GetDriveLetters@CTaskData@@QEAAXAEAFPEAPEAGG@Z` | `0x26DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `?GetFileSystemTypes@CTaskData@@QEAAXAEAKPEAPEAUifilesysteminfo@@@Z` | `0x26DC0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `?GetIVolumeClientVersion@CTaskData@@QEAAFXZ` | `0x26E10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `?GetMinMaxPartitionSizes@CTaskData@@QEAAX_JAEA_J1@Z` | `0x26E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `?GetOtherDisksFromVolCookie@CTaskData@@QEAAX_JAEAKPEAPEA_J@Z` | `0x26E60` | 415 | UnwindData |  |
| 133 | `?GetServerName@CTaskData@@QEAA?AVCString@@XZ` | `0x27010` | 31 | UnwindData |  |
| 154 | `?HasNTFSwithDriveLetter@CTaskData@@QEAAHXZ` | `0x27040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `?IsAlpha@CTaskData@@QEAAHXZ` | `0x27060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `?IsEfi@CTaskData@@QEAAHXZ` | `0x27080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `?IsLocalMachine@CTaskData@@QEAAHXZ` | `0x270A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `?IsNEC_98Server@CTaskData@@QEAAHXZ` | `0x270C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `?IsNTServer@CTaskData@@QEAAHXZ` | `0x270E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `?IsPostLonghornVdsVersion@CTaskData@@QEAAHXZ` | `0x27100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `?IsPreLonghornVdsVersion@CTaskData@@QEAAHXZ` | `0x27120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `?IsSecureSystemPartition@CTaskData@@QEAAHXZ` | `0x27140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `?IsWolfpack@CTaskData@@QEAAHXZ` | `0x27160` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `?SetUIState@CTaskData@@QEAAXK@Z` | `0x27200` | 300 | UnwindData |  |
| 222 | `?SupportGpt@CTaskData@@QEAAHXZ` | `0x27340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `CompareDiskNames` | `0x27360` | 141 | UnwindData |  |
| 229 | `CookieSort` | `0x27400` | 264 | UnwindData |  |
| 233 | `namecmp` | `0x27510` | 276 | UnwindData |  |
