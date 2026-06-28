# Binary Specification: dmcmnutils.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dmcmnutils.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `280e77b93fff371d4ce59046e6785603bffb40cf4e896052fbc16b1275fdf403`
* **Total Exported Functions:** 135

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `DecodeBase64W` | `0x5AD70` | 360 | UnwindData |  |
| 87 | `EncodeBase64` | `0x5AEE0` | 361 | UnwindData |  |
| 88 | `EncodeBase64W` | `0x5B050` | 429 | UnwindData |  |
| 23 | `DmExecuteProcessAndCollect` | `0x5BBF0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `DmInitializeContainer` | `0x5BBF0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `DmReleaseContainer` | `0x5BBF0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `DmStartContainerActivity` | `0x5BBF0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `DmStopContainerActivity` | `0x5BBF0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `DmMdmSign` | `0x5C0A0` | 529 | UnwindData |  |
| 14 | `DmCopyDirectoryRecursive` | `0x5DB00` | 638 | UnwindData |  |
| 15 | `DmCreateFileSafe` | `0x5DD90` | 445 | UnwindData |  |
| 40 | `DmGetFileSize` | `0x5DF60` | 146 | UnwindData |  |
| 2 | `ComputeHmac` | `0x5E620` | 127 | UnwindData |  |
| 5 | `CreateRebootCSPTasksFromRegistry` | `0x5EB80` | 104 | UnwindData |  |
| 10 | `DeleteRebootCSPTaskInRegistry` | `0x5FB20` | 198 | UnwindData |  |
| 133 | `WriteRebootCSPTaskToRegistry` | `0x5FCE0` | 514 | UnwindData |  |
| 6 | `DMGetClientHardwareUID` | `0x5FFF0` | 390 | UnwindData |  |
| 7 | `DMGetDeviceClientID` | `0x60180` | 149 | UnwindData |  |
| 8 | `DMSetDeviceClientID` | `0x60220` | 123 | UnwindData |  |
| 97 | `GetPhoneUID` | `0x60660` | 141 | UnwindData |  |
| 38 | `DmGetEnrollmentTypeName` | `0x608D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `DmGetEnrollmentTypeValue` | `0x60900` | 92 | UnwindData |  |
| 90 | `GetHeader` | `0x60AE0` | 503 | UnwindData |  |
| 110 | `IsDesktopSku` | `0x60D10` | 92 | UnwindData |  |
| 111 | `IsServerVersionOrAbove` | `0x60D80` | 237 | UnwindData |  |
| 112 | `IsWvdFeatureAllowed` | `0x60E80` | 77 | UnwindData |  |
| 113 | `IsWvdSku` | `0x60EE0` | 175 | UnwindData |  |
| 115 | `OmDmRegistryAllocAndGetString` | `0x60FA0` | 266 | UnwindData |  |
| 116 | `OmaDmRegistryDeleteValue` | `0x610B0` | 177 | UnwindData |  |
| 117 | `OmaDmRegistryGetAllSubKeys` | `0x61170` | 570 | UnwindData |  |
| 118 | `OmaDmRegistryGetAllValues` | `0x613B0` | 570 | UnwindData |  |
| 119 | `OmaDmRegistryGetBinary` | `0x615F0` | 223 | UnwindData |  |
| 120 | `OmaDmRegistryGetDWORD` | `0x616E0` | 244 | UnwindData |  |
| 121 | `OmaDmRegistryGetString` | `0x617E0` | 235 | UnwindData |  |
| 122 | `OmaDmRegistryRetrieveCurrentUsersHKCU` | `0x618E0` | 229 | UnwindData |  |
| 123 | `OmaDmRegistrySetBinary` | `0x619D0` | 231 | UnwindData |  |
| 124 | `OmaDmRegistrySetDWORD` | `0x61AC0` | 217 | UnwindData |  |
| 125 | `OmaDmRegistrySetString` | `0x61BA0` | 246 | UnwindData |  |
| 130 | `SetConnectionPriority` | `0x61D70` | 201 | UnwindData |  |
| 98 | `Hash_Create` | `0x62180` | 204 | UnwindData |  |
| 99 | `Hash_Delete` | `0x62260` | 287 | UnwindData |  |
| 100 | `Hash_Destroy` | `0x62390` | 177 | UnwindData |  |
| 101 | `Hash_DestroyCallback` | `0x62450` | 62 | UnwindData |  |
| 102 | `Hash_EnumCallback` | `0x624A0` | 297 | UnwindData |  |
| 103 | `Hash_Get` | `0x625D0` | 261 | UnwindData |  |
| 104 | `Hash_Insert` | `0x626E0` | 400 | UnwindData |  |
| 105 | `Hash_SetBucketThreshold` | `0x62880` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `DmGetSmbiosSerialNumber` | `0x629E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `DmGetTpmInfo` | `0x62A50` | 514 | UnwindData |  |
| 48 | `DmGetTpmIsAlgorithmSupported` | `0x62C60` | 655 | UnwindData |  |
| 49 | `DmGetTpmState` | `0x62F00` | 717 | UnwindData |  |
| 41 | `DmGetIMEI` | `0x63220` | 673 | UnwindData |  |
| 61 | `DmIsDeviceConnected` | `0x634D0` | 163 | UnwindData |  |
| 62 | `DmIsDeviceRoaming` | `0x63580` | 485 | UnwindData |  |
| 72 | `DmRegisterRoamingNotification` | `0x63770` | 194 | UnwindData |  |
| 83 | `DmUnregisterRoamingNotification` | `0x63840` | 88 | UnwindData |  |
| 95 | `GetPGListRegKeyName` | `0x638E0` | 64 | UnwindData |  |
| 91 | `GetICCID` | `0x63ED0` | 479 | UnwindData |  |
| 92 | `GetIMEI` | `0x640C0` | 235 | UnwindData |  |
| 93 | `GetIMSI` | `0x641C0` | 476 | UnwindData |  |
| 94 | `GetIMSIByIccID` | `0x643B0` | 1,895 | UnwindData |  |
| 96 | `GetPhoneNumber` | `0x64B80` | 235 | UnwindData |  |
| 126 | `QueryPolicy` | `0x65020` | 254 | UnwindData |  |
| 131 | `SetPolicy` | `0x65210` | 599 | UnwindData |  |
| 16 | `DmCreateTask` | `0x654F0` | 6,434 | UnwindData |  |
| 17 | `DmDeleteTask` | `0x66E20` | 1,492 | UnwindData |  |
| 18 | `DmDeleteTaskFolder` | `0x67400` | 2,293 | UnwindData |  |
| 20 | `DmDisableTask` | `0x67D00` | 1,790 | UnwindData |  |
| 21 | `DmEnableTask` | `0x68410` | 1,790 | UnwindData |  |
| 66 | `DmIsTaskScheduled` | `0x68B20` | 1,432 | UnwindData |  |
| 67 | `DmIsTaskScheduledAndEnabled` | `0x690C0` | 1,536 | UnwindData |  |
| 78 | `DmRunTask` | `0x696D0` | 1,419 | UnwindData |  |
| 22 | `DmEnumUsers` | `0x69FC0` | 958 | UnwindData |  |
| 33 | `DmGetActiveUserSid` | `0x6A390` | 586 | UnwindData |  |
| 34 | `DmGetAllActiveUserSids` | `0x6A5E0` | 1,241 | UnwindData |  |
| 36 | `DmGetCurrentUserSid` | `0x6AAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `DmGetCurrentUserToken` | `0x6AAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `DmGetUserSidFromToken` | `0x6AAE0` | 157 | UnwindData |  |
| 54 | `DmGetUserTokenFromSid` | `0x6AB90` | 288 | UnwindData |  |
| 55 | `DmImpersonate` | `0x6ACC0` | 289 | UnwindData |  |
| 63 | `DmIsRunningInSystemContext` | `0x6ADF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `DmIsSystemOrAdmin` | `0x6AE00` | 38 | UnwindData |  |
| 65 | `DmIsSystemOrUserIsAdmin` | `0x6AE30` | 38 | UnwindData |  |
| 77 | `DmRevertToSelf` | `0x6AE60` | 90 | UnwindData |  |
| 1 | `BigStrcat` | `0x6C4F0` | 236 | UnwindData |  |
| 3 | `CopyString` | `0x6C5F0` | 272 | UnwindData |  |
| 4 | `CreateBstrArray` | `0x6C710` | 347 | UnwindData |  |
| 82 | `DmStringCchPrintfAllStrings` | `0x6C880` | 343 | UnwindData |  |
| 89 | `EscapeStringW` | `0x6C9E0` | 376 | UnwindData |  |
| 106 | `InvStrCmpIW` | `0x6CB60` | 145 | UnwindData |  |
| 107 | `InvStrCmpNIW` | `0x6CC00` | 152 | UnwindData |  |
| 108 | `InvStrCmpNW` | `0x6CCA0` | 149 | UnwindData |  |
| 109 | `InvStrCmpW` | `0x6CD40` | 144 | UnwindData |  |
| 114 | `MBToUnicode` | `0x6CDE0` | 351 | UnwindData |  |
| 127 | `SafeMultiByteToWideChar` | `0x6CFE0` | 196 | UnwindData |  |
| 128 | `SafeStringToDword` | `0x6D0B0` | 317 | UnwindData |  |
| 129 | `SafeWideCharToMultiByte` | `0x6D200` | 236 | UnwindData |  |
| 132 | `UnicodeToMB` | `0x6D350` | 362 | UnwindData |  |
| 134 | `BinaryToHexString` | `0x6D660` | 23 | UnwindData |  |
| 135 | `HexStringToBinary` | `0x6D680` | 221 | UnwindData |  |
| 70 | `DmRaiseToastNotification` | `0x6EB50` | 593 | UnwindData |  |
| 71 | `DmRaiseToastNotificationAndWait` | `0x6EDB0` | 4,340 | UnwindData |  |
| 74 | `DmRemoveToastNotification` | `0x6FEB0` | 283 | UnwindData |  |
| 75 | `DmRemoveToastNotificationByExecutablePath` | `0x6FFE0` | 412 | UnwindData |  |
| 69 | `DmPlayNotificationSound` | `0x71020` | 10,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DmCheckIfAadAccountLoggedOn` | `0x73790` | 136 | UnwindData |  |
| 27 | `DmGetAadDeviceMdmEnrollmentResourceUrlForRecovery` | `0x73B90` | 1,570 | UnwindData |  |
| 28 | `DmGetAadDeviceMdmEnrollmentResourceUrlWithDiscovery` | `0x741C0` | 385 | UnwindData |  |
| 29 | `DmGetAadDeviceToken` | `0x74350` | 51 | UnwindData |  |
| 30 | `DmGetAadDeviceTokenWithDiscovery` | `0x74390` | 388 | UnwindData |  |
| 31 | `DmGetAadEnrollmentResource` | `0x74520` | 276 | UnwindData |  |
| 32 | `DmGetAadUserToken` | `0x74640` | 58 | UnwindData |  |
| 59 | `DmInvalidateAadDeviceToken` | `0x75BE0` | 52 | UnwindData |  |
| 60 | `DmInvalidateAadUserToken` | `0x75C20` | 51 | UnwindData |  |
| 76 | `DmRequestAadUserToken` | `0x75C60` | 50 | UnwindData |  |
| 11 | `DmCancelGetUserPermissionAsync` | `0x79BC0` | 83 | UnwindData |  |
| 50 | `DmGetUserEditFieldInput` | `0x79C20` | 96 | UnwindData |  |
| 51 | `DmGetUserPermission` | `0x79C90` | 84 | UnwindData |  |
| 52 | `DmGetUserPermissionAsync` | `0x79CF0` | 273 | UnwindData |  |
| 56 | `DmInformUser` | `0x79E10` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `DmWnfGetNotification` | `0x79EE0` | 393 | UnwindData |  |
| 85 | `DmWnfPublish` | `0x7A070` | 87 | UnwindData |  |
| 86 | `DmWnfQuery` | `0x7A0D0` | 146 | UnwindData |  |
| 12 | `DmCheckAikOld` | `0x86A40` | 209 | UnwindData |  |
| 19 | `DmDiagnoseEkAikMissingOld` | `0x86B20` | 320 | UnwindData |  |
| 24 | `DmGenerateAttestationClaimsOld` | `0x86C70` | 2,218 | UnwindData |  |
| 25 | `DmGenerateMaaAttestationClaims` | `0x87520` | 2,791 | UnwindData |  |
| 26 | `DmGenerateMaaAttestationClaimsOld` | `0x88010` | 2,287 | UnwindData |  |
| 42 | `DmGetKeyFromContext` | `0x88910` | 509 | UnwindData |  |
| 43 | `DmGetKeyNameFromContext` | `0x88B20` | 636 | UnwindData |  |
| 45 | `DmGetTargetAikOld` | `0x88DB0` | 534 | UnwindData |  |
| 46 | `DmGetTargetAikWithRetryOld` | `0x88FD0` | 551 | UnwindData |  |
| 79 | `DmSetWindowsAIKStorageLocationOld` | `0x89200` | 785 | UnwindData |  |
| 35 | `DmGetCorrelationVectorForDmSession` | `0x934B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `DmInitializeCVForLocalConfigSession` | `0x934C0` | 169,564 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
