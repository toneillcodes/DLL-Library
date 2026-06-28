# Binary Specification: vdsutil.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vdsutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e2f3f3f93d1817adeb1608ecaf4b314ad98bbd7b0d129a696df8056d7fe9f7b5`
* **Total Exported Functions:** 238

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 100 | `?m_ExtraLogging@CVdsTraceSettings@@QEAAHXZ` | `0x26F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `?m_NoDebuggerLogging@CVdsTraceSettings@@QEAAHXZ` | `0x2700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0CPrvEnumObject@@QEAA@XZ` | `0x2710` | 105 | UnwindData |  |
| 6 | `??0CRtlSharedLock@@QEAA@XZ` | `0x2780` | 45 | UnwindData |  |
| 9 | `??0CVdsCriticalSection@@QEAA@PEAU_RTL_CRITICAL_SECTION@@@Z` | `0x27C0` | 37 | UnwindData |  |
| 10 | `??0CVdsPnPNotificationBase@@QEAA@XZ` | `0x27F0` | 61 | UnwindData |  |
| 12 | `??0CVdsUnlockIt@@QEAA@AEAJ@Z` | `0x2840` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??1CPrvEnumObject@@QEAA@XZ` | `0x28B0` | 211 | UnwindData |  |
| 19 | `??1CRtlSharedLock@@QEAA@XZ` | `0x2990` | 23 | UnwindData |  |
| 22 | `??1CVdsCriticalSection@@QEAA@XZ` | `0x29B0` | 26 | UnwindData |  |
| 23 | `??1CVdsPnPNotificationBase@@QEAA@XZ` | `0x29D0` | 44 | UnwindData |  |
| 24 | `??1CVdsUnlockIt@@QEAA@XZ` | `0x2A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??_FCRtlList@@QEAAXXZ` | `0x2A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??_FCRtlMap@@QEAAXXZ` | `0x2A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `?AcquireRead@CRtlSharedLock@@AEAAXXZ` | `0x2A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `?AcquireWrite@CRtlSharedLock@@AEAAXXZ` | `0x2A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `?AllowCancel@CVdsAsyncObjectBase@@QEAAXXZ` | `0x2AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `?CurrentThreadIsWriter@CRtlSharedLock@@QEAAHXZ` | `0x2AB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `?DisallowCancel@CVdsAsyncObjectBase@@QEAAXXZ` | `0x2AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `?Downgrade@CRtlSharedLock@@AEAAXXZ` | `0x2AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `?GetOutputType@CVdsAsyncObjectBase@@QEAA?AW4_VDS_ASYNC_OUTPUT_TYPE@@XZ` | `0x2B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `?IsCancelRequested@CVdsAsyncObjectBase@@QEAAHXZ` | `0x2B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?Release@CRtlSharedLock@@AEAAXXZ` | `0x2B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `?SetOutput@CVdsAsyncObjectBase@@QEAAXU_VDS_ASYNC_OUTPUT@@@Z` | `0x2B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `?SetOutputType@CVdsAsyncObjectBase@@QEAAXW4_VDS_ASYNC_OUTPUT_TYPE@@@Z` | `0x2B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `?SetPositionToLast@CPrvEnumObject@@QEAAXXZ` | `0x2B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `?Upgrade@CRtlSharedLock@@AEAAXXZ` | `0x2BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `?ZeroAsyncOut@CVdsAsyncObjectBase@@QEAAXXZ` | `0x2BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `StartReferenceHistory` | `0x2BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??1CGlobalResource@@QEAA@XZ` | `0x2BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `StopReferenceHistory` | `0x2BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `AcquireRundownProtection` | `0x2C00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `InitializeRundownProtection` | `0x2C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `ReInitializeRundownProtection` | `0x2C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `ReleaseRundownProtection` | `0x2C50` | 80 | UnwindData |  |
| 188 | `RundownCompleted` | `0x2CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `WaitForRundownProtectionRelease` | `0x2CC0` | 385 | UnwindData |  |
| 196 | `VdsAssert` | `0x2ED0` | 203 | UnwindData |  |
| 8 | `??0CVdsCallTracer@@QEAA@KPEBD@Z` | `0x2FB0` | 49 | UnwindData |  |
| 11 | `??0CVdsTraceSettings@@QEAA@XZ` | `0x2FF0` | 187 | UnwindData |  |
| 21 | `??1CVdsCallTracer@@QEAA@XZ` | `0x30C0` | 34 | UnwindData |  |
| 210 | `VdsTrace` | `0x30F0` | 44 | UnwindData |  |
| 211 | `VdsTraceEx` | `0x3130` | 30 | UnwindData |  |
| 212 | `VdsTraceExHelper` | `0x3160` | 359 | UnwindData |  |
| 213 | `VdsTraceExW` | `0x32D0` | 30 | UnwindData |  |
| 214 | `VdsTraceExWHelper` | `0x3300` | 438 | UnwindData |  |
| 215 | `VdsTraceW` | `0x34C0` | 49 | UnwindData |  |
| 7 | `??0CVdsAsyncObjectBase@@QEAA@XZ` | `0x3560` | 138 | UnwindData |  |
| 20 | `??1CVdsAsyncObjectBase@@QEAA@XZ` | `0x35F0` | 96 | UnwindData |  |
| 35 | `?Append@CPrvEnumObject@@QEAAJPEAUIUnknown@@@Z` | `0x36A0` | 91 | UnwindData |  |
| 39 | `?Cancel@CVdsAsyncObjectBase@@UEAAJXZ` | `0x3710` | 48 | UnwindData |  |
| 40 | `?Clear@CPrvEnumObject@@QEAAXXZ` | `0x3750` | 157 | UnwindData |  |
| 41 | `?Clone@CPrvEnumObject@@UEAAJPEAPEAUIEnumVdsObject@@@Z` | `0x3800` | 392 | UnwindData |  |
| 56 | `?Initialize@CVdsAsyncObjectBase@@SAKXZ` | `0x3AA0` | 218 | UnwindData |  |
| 68 | `?IsFinished@CVdsAsyncObjectBase@@QEAAHXZ` | `0x3B80` | 162 | UnwindData |  |
| 69 | `?Next@CPrvEnumObject@@UEAAJKPEAPEAUIUnknown@@PEAK@Z` | `0x3C30` | 226 | UnwindData |  |
| 76 | `?QueryStatus@CVdsAsyncObjectBase@@UEAAJPEAJPEAK@Z` | `0x3E40` | 139 | UnwindData |  |
| 84 | `?Reset@CPrvEnumObject@@UEAAJXZ` | `0x3F70` | 73 | UnwindData |  |
| 86 | `?SetCompletionStatus@CVdsAsyncObjectBase@@QEAAXJK@Z` | `0x3FC0` | 147 | UnwindData |  |
| 90 | `?Signal@CVdsAsyncObjectBase@@QEAAXXZ` | `0x4060` | 140 | UnwindData |  |
| 91 | `?Skip@CPrvEnumObject@@UEAAJK@Z` | `0x4100` | 129 | UnwindData |  |
| 92 | `?Uninitialize@CVdsAsyncObjectBase@@SAXXZ` | `0x4200` | 106 | UnwindData |  |
| 97 | `?WaitImpl@CVdsAsyncObjectBase@@QEAAJPEAJ@Z` | `0x4270` | 179 | UnwindData |  |
| 194 | `VdsAllocateEmptyString` | `0x4330` | 116 | UnwindData |  |
| 195 | `VdsAllocateString` | `0x43B0` | 246 | UnwindData |  |
| 199 | `VdsHeapAlloc` | `0x44B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `VdsHeapFree` | `0x44D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `VdsInitializeCriticalSection` | `0x4500` | 74 | UnwindData |  |
| 1 | `??0?$CVdsHandleImpl@$0?0@@QEAA@XZ` | `0x4550` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??1?$CVdsHandleImpl@$0?0@@QEAA@XZ` | `0x4590` | 45 | UnwindData |  |
| 26 | `??4?$CVdsHandleImpl@$0?0@@QEAAPEAXPEAX@Z` | `0x45D0` | 59 | UnwindData |  |
| 28 | `??8?$CVdsHandleImpl@$0?0@@QEBA_NPEAX@Z` | `0x4620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??B?$CVdsHandleImpl@$0?0@@QEAAPEAXXZ` | `0x4630` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `?CreateListenThread@CVdsPnPNotificationBase@@AEAAKXZ` | `0x4D40` | 546 | UnwindData |  |
| 54 | `?GetWindowHandle@CVdsPnPNotificationBase@@QEAAPEAUHWND__@@XZ` | `0x5AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?Initialize@CVdsPnPNotificationBase@@QEAAKXZ` | `0x5AC0` | 268 | UnwindData |  |
| 73 | `?NotificationThread@CVdsPnPNotificationBase@@AEAAKPEAX@Z` | `0x5D00` | 654 | UnwindData |  |
| 74 | `?NotificationThreadEntry@CVdsPnPNotificationBase@@CAKPEAX@Z` | `0x5FA0` | 63 | UnwindData |  |
| 77 | `?Register@CVdsPnPNotificationBase@@QEAAKPEAU_NotificationListeningRequest@@K@Z` | `0x61D0` | 238 | UnwindData |  |
| 78 | `?RegisterHandle@CVdsPnPNotificationBase@@QEAAKPEAXPEAPEAX@Z` | `0x62D0` | 205 | UnwindData |  |
| 93 | `?Uninitialize@CVdsPnPNotificationBase@@QEAAXXZ` | `0x6810` | 246 | UnwindData |  |
| 94 | `?Unregister@CVdsPnPNotificationBase@@QEAAXPEAU_NotificationListeningRequest@@@Z` | `0x6910` | 279 | UnwindData |  |
| 95 | `?UnregisterHandle@CVdsPnPNotificationBase@@QEAAXPEAX@Z` | `0x6A30` | 108 | UnwindData |  |
| 98 | `?WindowProcEntry@CVdsPnPNotificationBase@@CA_JPEAUHWND__@@I_K_J@Z` | `0x6C90` | 167 | UnwindData |  |
| 103 | `AddEventSource` | `0x6F00` | 565 | UnwindData |  |
| 104 | `AllocateAndGetVolumePathName` | `0x7140` | 370 | UnwindData |  |
| 105 | `AssignTempVolumeName` | `0x72C0` | 303 | UnwindData |  |
| 106 | `BacksBootVolume` | `0x7400` | 78 | UnwindData |  |
| 107 | `BootBackedByWim` | `0x7460` | 78 | UnwindData |  |
| 108 | `CoFreeStringArray` | `0x74C0` | 132 | UnwindData |  |
| 109 | `CreateDeviceInfoSet` | `0x7550` | 404 | UnwindData |  |
| 110 | `DeleteBcdObjects` | `0x76F0` | 531 | UnwindData |  |
| 111 | `DeleteNetworkShare` | `0x7910` | 383 | UnwindData |  |
| 112 | `DllMain` | `0x7AA0` | 397 | UnwindData |  |
| 113 | `GarbageCollectDriveLetters` | `0x7C40` | 471 | UnwindData |  |
| 114 | `GetBootDiskNumber` | `0x7E20` | 501 | UnwindData |  |
| 115 | `GetBootFromDiskNumber` | `0x8020` | 761 | UnwindData |  |
| 116 | `GetBootVolumeHandle` | `0x8320` | 680 | UnwindData |  |
| 117 | `GetDefaultAlignment` | `0x85D0` | 524 | UnwindData |  |
| 118 | `GetDeviceAndMediaType` | `0x87F0` | 622 | UnwindData |  |
| 119 | `GetDeviceId` | `0x8A70` | 341 | UnwindData |  |
| 120 | `GetDeviceLocation` | `0x8BD0` | 785 | UnwindData |  |
| 121 | `GetDeviceLocationEx` | `0x8EF0` | 944 | UnwindData |  |
| 122 | `GetDeviceLocationPath` | `0x92B0` | 711 | UnwindData |  |
| 123 | `GetDeviceManufacturerInfo` | `0x9580` | 744 | UnwindData |  |
| 124 | `GetDeviceName` | `0x9870` | 331 | UnwindData |  |
| 125 | `GetDeviceNumber` | `0x99D0` | 172 | UnwindData |  |
| 126 | `GetDeviceRegistryPropertyByInfo` | `0x9A90` | 584 | UnwindData |  |
| 127 | `GetDeviceRegistryPropertyByInst` | `0x9CE0` | 392 | UnwindData |  |
| 128 | `GetDiskFlags` | `0x9E70` | 386 | UnwindData |  |
| 129 | `GetDiskIdentifiers` | `0xA000` | 947 | UnwindData |  |
| 130 | `GetDiskLayout` | `0xA3C0` | 396 | UnwindData |  |
| 131 | `GetDiskOfflineReason` | `0xA560` | 424 | UnwindData |  |
| 132 | `GetDiskRedundancyCount` | `0xA710` | 298 | UnwindData |  |
| 138 | `GetFileSystemRecognitionName` | `0xA840` | 561 | UnwindData |  |
| 139 | `GetInterfaceDetailData` | `0xAA80` | 373 | UnwindData |  |
| 140 | `GetIsRemovable` | `0xAC00` | 191 | UnwindData |  |
| 141 | `GetMediaGeometry` | `0xACD0` | 181 | UnwindData |  |
| 142 | `GetMediaGeometryEx` | `0xAD90` | 181 | UnwindData |  |
| 143 | `GetPartitionInformation` | `0xAE50` | 145 | UnwindData |  |
| 144 | `GetRegistryValue` | `0xAEF0` | 503 | UnwindData |  |
| 145 | `GetStorageAccessAlignmentProperty` | `0xB0F0` | 219 | UnwindData |  |
| 146 | `GetSystemVolumeHandle` | `0xB1E0` | 661 | UnwindData |  |
| 147 | `GetVolumeDiskExtentInfo` | `0xB480` | 347 | UnwindData |  |
| 148 | `GetVolumeGuidPathnames` | `0xB5F0` | 1,141 | UnwindData |  |
| 149 | `GetVolumeName` | `0xBA70` | 763 | UnwindData |  |
| 150 | `GetVolumePath` | `0xBD80` | 410 | UnwindData |  |
| 151 | `GetVolumeSize` | `0xBF20` | 191 | UnwindData |  |
| 152 | `GetVolumeUniqueId` | `0xBFF0` | 497 | UnwindData |  |
| 153 | `GuidToString` | `0xC1F0` | 248 | UnwindData |  |
| 155 | `InitializeSecurityDescriptorHelper` | `0xC2F0` | 870 | UnwindData |  |
| 156 | `InvalidateDiskCache` | `0xC660` | 212 | UnwindData |  |
| 157 | `IoctlMountmgrQueryPointsDevicePath` | `0xC740` | 870 | UnwindData |  |
| 158 | `IsClientSKU` | `0xCAB0` | 131 | UnwindData |  |
| 159 | `IsDeviceFullyInstalled` | `0xCB40` | 268 | UnwindData |  |
| 160 | `IsDiskClustered` | `0xCC60` | 630 | UnwindData |  |
| 161 | `IsDiskCurrentStateReadOnly` | `0xCEE0` | 250 | UnwindData |  |
| 162 | `IsDiskReadOnly` | `0xCFE0` | 288 | UnwindData |  |
| 163 | `IsDriveLetter` | `0xD110` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `IsEfiFirmware` | `0xD160` | 99 | UnwindData |  |
| 165 | `IsLocalComputer` | `0xD1D0` | 691 | UnwindData |  |
| 166 | `IsMediaPresent` | `0xD490` | 111 | UnwindData |  |
| 167 | `IsNoAutoMount` | `0xD510` | 361 | UnwindData |  |
| 168 | `IsRamDrive` | `0xD680` | 380 | UnwindData |  |
| 169 | `IsRunningOnAMD64` | `0xD810` | 55 | UnwindData |  |
| 170 | `IsVdsLoggingEnabled` | `0xD850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `IsWinPE` | `0xD870` | 124 | UnwindData |  |
| 172 | `LockDismountVolume` | `0xD900` | 213 | UnwindData |  |
| 173 | `LockVolume` | `0xD9E0` | 207 | UnwindData |  |
| 174 | `LogError` | `0xDAC0` | 274 | UnwindData |  |
| 175 | `LogEvent` | `0xDBE0` | 246 | UnwindData |  |
| 176 | `LogInfo` | `0xDCE0` | 263 | UnwindData |  |
| 177 | `LogWarning` | `0xDDF0` | 274 | UnwindData |  |
| 178 | `MirrorBcdObjects` | `0xDF10` | 1,615 | UnwindData |  |
| 179 | `MountVolume` | `0xE570` | 191 | UnwindData |  |
| 180 | `OpenDevice` | `0xE640` | 408 | UnwindData |  |
| 181 | `QueryObjects` | `0xE7E0` | 211 | UnwindData |  |
| 182 | `QueryVolPersistentState` | `0xE8C0` | 194 | UnwindData |  |
| 184 | `RegisterProvider` | `0xE990` | 534 | UnwindData |  |
| 186 | `RemoveEventSource` | `0xEBB0` | 188 | UnwindData |  |
| 187 | `RemoveTempVolumeName` | `0xEC80` | 340 | UnwindData |  |
| 189 | `SetDiskLayout` | `0xEDE0` | 177 | UnwindData |  |
| 193 | `UnregisterProvider` | `0xEEA0` | 390 | UnwindData |  |
| 197 | `VdsDisableCOMFatalExceptionHandling` | `0xF030` | 152 | UnwindData |  |
| 198 | `VdsDoesDiskHaveArcPath` | `0xF0D0` | 1,066 | UnwindData |  |
| 238 | `WriteBootCode` | `0xF5A0` | 740 | UnwindData |  |
| 202 | `VdsIscsiCacheSessionDevices` | `0xF890` | 1,269 | UnwindData |  |
| 203 | `VdsIscsiCheckEqualIpAddress` | `0xFD90` | 935 | UnwindData |  |
| 204 | `VdsIscsiGetIpAddressFromInstance` | `0x10140` | 879 | UnwindData |  |
| 205 | `VdsIscsiIpAddressToIpsecId` | `0x104C0` | 504 | UnwindData |  |
| 206 | `VdsIscsiIpAddressToString` | `0x106C0` | 586 | UnwindData |  |
| 207 | `VdsIscsiIpsecIdToIpAddress` | `0x10910` | 291 | UnwindData |  |
| 208 | `VdsIscsiIsIscsiLun` | `0x10A40` | 845 | UnwindData |  |
| 209 | `VdsIscsiSetIpAddressInInstance` | `0x10DA0` | 747 | UnwindData |  |
| 13 | `??0CVdsWmiVariantObjectArrayEnum@@QEAA@XZ` | `0x110A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??1CVdsWmiVariantObjectArrayEnum@@QEAA@XZ` | `0x110C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `?Detach@CVdsWmiVariantObjectArrayEnum@@QEAAJXZ` | `0x110C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?Attach@CVdsWmiVariantObjectArrayEnum@@QEAAJPEAUtagVARIANT@@@Z` | `0x110E0` | 178 | UnwindData |  |
| 72 | `?Next@CVdsWmiVariantObjectArrayEnum@@QEAAJPEAPEAUIWbemClassObject@@@Z` | `0x111A0` | 212 | UnwindData |  |
| 85 | `?Reset@CVdsWmiVariantObjectArrayEnum@@QEAAJXZ` | `0x11280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `VdsWmiCallMethod` | `0x11290` | 313 | UnwindData |  |
| 217 | `VdsWmiConnectToNamespace` | `0x113D0` | 248 | UnwindData |  |
| 218 | `VdsWmiCopyFromVariantByteArray` | `0x114D0` | 430 | UnwindData |  |
| 219 | `VdsWmiCopyToVariantByteArray` | `0x11690` | 295 | UnwindData |  |
| 220 | `VdsWmiCreateClassInstance` | `0x117C0` | 148 | UnwindData |  |
| 221 | `VdsWmiCreateVariantArray` | `0x11860` | 122 | UnwindData |  |
| 222 | `VdsWmiFindInstanceOfClass` | `0x118E0` | 489 | UnwindData |  |
| 223 | `VdsWmiGetBoolFromInstance` | `0x11AD0` | 196 | UnwindData |  |
| 224 | `VdsWmiGetByteFromInstance` | `0x11BA0` | 177 | UnwindData |  |
| 225 | `VdsWmiGetByteInVariantByteArray` | `0x11C60` | 348 | UnwindData |  |
| 226 | `VdsWmiGetMethodArgumentObject` | `0x11DD0` | 240 | UnwindData |  |
| 227 | `VdsWmiGetObjectFromInstance` | `0x11ED0` | 207 | UnwindData |  |
| 228 | `VdsWmiGetObjectInVariantObjectArray` | `0x11FB0` | 419 | UnwindData |  |
| 229 | `VdsWmiGetUlongFromInstance` | `0x12160` | 177 | UnwindData |  |
| 230 | `VdsWmiGetUlonglongFromInstance` | `0x12220` | 196 | UnwindData |  |
| 231 | `VdsWmiSetBoolInInstance` | `0x122F0` | 184 | UnwindData |  |
| 232 | `VdsWmiSetByteInInstance` | `0x123B0` | 159 | UnwindData |  |
| 233 | `VdsWmiSetObjectInInstance` | `0x12460` | 206 | UnwindData |  |
| 234 | `VdsWmiSetStringInInstance` | `0x12540` | 204 | UnwindData |  |
| 235 | `VdsWmiSetUlongInInstance` | `0x12620` | 159 | UnwindData |  |
| 236 | `VdsWmiSetUlonglongInInstance` | `0x126D0` | 258 | UnwindData |  |
| 4 | `??0CRtlList@@QEAA@P6AXPEAVCRtlEntry@@@Z@Z` | `0x127E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0CRtlMap@@QEAA@KP6AXPEAVCRtlEntry@@@Z1@Z` | `0x12800` | 85 | UnwindData |  |
| 17 | `??1CRtlList@@QEAA@XZ` | `0x12860` | 26 | UnwindData |  |
| 18 | `??1CRtlMap@@UEAA@XZ` | `0x12880` | 49 | UnwindData |  |
| 27 | `??4CRtlList@@QEAAAEAV0@AEAV0@@Z` | `0x128C0` | 133 | UnwindData |  |
| 37 | `?Begin@CRtlList@@QEAA?AVCRtlListIter@@XZ` | `0x12A10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `?Begin@CRtlMap@@QEAA?AVCRtlMapIter@@XZ` | `0x12A50` | 52 | UnwindData |  |
| 47 | `?End@CRtlList@@QEAA?AVCRtlListIter@@XZ` | `0x12BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `?Find@CRtlMap@@QEAAHAEAVCRtlEntry@@PEAV2@@Z` | `0x12BF0` | 130 | UnwindData |  |
| 49 | `?FindPtr@CRtlMap@@QEAAHAEAVCRtlEntry@@PEAPEAV2@@Z` | `0x12C80` | 122 | UnwindData |  |
| 50 | `?GetEntry@CRtlListIter@@QEAAPEAVCRtlEntry@@XZ` | `0x12D80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `?GetEntryPointer@CRtlListIter@@QEAAPEAXXZ` | `0x12DB0` | 32 | UnwindData |  |
| 52 | `?GetNode@CRtlListIter@@QEAAPEAVCRtlListEntry@@XZ` | `0x12DE0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `?Insert@CRtlList@@QEAAHAEAVCRtlListIter@@AEAVCRtlEntry@@@Z` | `0x12E60` | 52 | UnwindData |  |
| 59 | `?Insert@CRtlMap@@QEAAHAEAVCRtlEntry@@0@Z` | `0x12EA0` | 168 | UnwindData |  |
| 60 | `?InsertHead@CRtlList@@QEAAHAEAVCRtlEntry@@@Z` | `0x12F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?InsertHeadPointer@CRtlList@@QEAAHPEAX@Z` | `0x12F70` | 46 | UnwindData |  |
| 62 | `?InsertPointer@CRtlList@@QEAAHAEAVCRtlListIter@@PEAX@Z` | `0x12FB0` | 77 | UnwindData |  |
| 63 | `?InsertTail@CRtlList@@QEAAHAEAVCRtlEntry@@@Z` | `0x13010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `?InsertTailPointer@CRtlList@@QEAAHPEAX@Z` | `0x13030` | 46 | UnwindData |  |
| 65 | `?InsertUnique@CRtlMap@@QEAAHAEAVCRtlEntry@@0@Z` | `0x13070` | 130 | UnwindData |  |
| 67 | `?IsDone@CRtlListIter@@QEAAHXZ` | `0x13100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `?Next@CRtlListIter@@QEAAAEAV1@XZ` | `0x13120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `?Next@CRtlMapIter@@QEAAAEAV1@XZ` | `0x13140` | 72 | UnwindData |  |
| 75 | `?Prev@CRtlListIter@@QEAAAEAV1@XZ` | `0x13190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `?Remove@CRtlList@@QEAAXAEAVCRtlListIter@@@Z` | `0x131B0` | 138 | UnwindData |  |
| 81 | `?Remove@CRtlMap@@QEAAHAEAVCRtlEntry@@@Z` | `0x13240` | 105 | UnwindData |  |
| 82 | `?RemoveAll@CRtlList@@QEAAXXZ` | `0x132B0` | 88 | UnwindData |  |
| 83 | `?RemoveAll@CRtlMap@@QEAAXH@Z` | `0x13310` | 105 | UnwindData |  |
| 2 | `??0CGlobalResource@@QEAA@XZ` | `0x134C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `?Initialize@CGlobalResource@@QEAAJXZ` | `0x13500` | 113 | UnwindData |  |
| 133 | `GetFMIFSEnableCompressionRoutine` | `0x13860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `GetFMIFSFormatEx2Routine` | `0x13880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `GetFMIFSGetDefaultFilesystemRoutine` | `0x138A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `GetFMIFSQueryDeviceInfo` | `0x138C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `GetFMIFSQueryDeviceInfoByHandle` | `0x138E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `UnInitializeGlobalResouce` | `0x13900` | 104 | UnwindData |  |
