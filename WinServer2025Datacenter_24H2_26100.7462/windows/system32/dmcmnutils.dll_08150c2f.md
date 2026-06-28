# Binary Specification: dmcmnutils.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dmcmnutils.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `08150c2fd2f87737e27a6dda3fbe3260866c7d969e52d5d8ee29cbf79f136a75`
* **Total Exported Functions:** 135

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `DecodeBase64W` | `0x5B460` | 360 | UnwindData |  |
| 87 | `EncodeBase64` | `0x5B5D0` | 361 | UnwindData |  |
| 88 | `EncodeBase64W` | `0x5B740` | 429 | UnwindData |  |
| 23 | `DmExecuteProcessAndCollect` | `0x5C2E0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `DmInitializeContainer` | `0x5C2E0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `DmReleaseContainer` | `0x5C2E0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `DmStartContainerActivity` | `0x5C2E0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `DmStopContainerActivity` | `0x5C2E0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `DmMdmSign` | `0x5C790` | 529 | UnwindData |  |
| 14 | `DmCopyDirectoryRecursive` | `0x5E720` | 638 | UnwindData |  |
| 15 | `DmCreateFileSafe` | `0x5E9B0` | 445 | UnwindData |  |
| 40 | `DmGetFileSize` | `0x5EB80` | 146 | UnwindData |  |
| 2 | `ComputeHmac` | `0x5F240` | 127 | UnwindData |  |
| 5 | `CreateRebootCSPTasksFromRegistry` | `0x5F7A0` | 104 | UnwindData |  |
| 10 | `DeleteRebootCSPTaskInRegistry` | `0x60740` | 198 | UnwindData |  |
| 133 | `WriteRebootCSPTaskToRegistry` | `0x60900` | 514 | UnwindData |  |
| 6 | `DMGetClientHardwareUID` | `0x60C10` | 390 | UnwindData |  |
| 7 | `DMGetDeviceClientID` | `0x60DA0` | 149 | UnwindData |  |
| 8 | `DMSetDeviceClientID` | `0x60E40` | 123 | UnwindData |  |
| 97 | `GetPhoneUID` | `0x61280` | 141 | UnwindData |  |
| 38 | `DmGetEnrollmentTypeName` | `0x614F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `DmGetEnrollmentTypeValue` | `0x61520` | 92 | UnwindData |  |
| 90 | `GetHeader` | `0x61740` | 503 | UnwindData |  |
| 110 | `IsDesktopSku` | `0x61970` | 92 | UnwindData |  |
| 111 | `IsServerVersionOrAbove` | `0x619E0` | 237 | UnwindData |  |
| 112 | `IsWvdFeatureAllowed` | `0x61AE0` | 77 | UnwindData |  |
| 113 | `IsWvdSku` | `0x61B40` | 175 | UnwindData |  |
| 115 | `OmDmRegistryAllocAndGetString` | `0x61C00` | 266 | UnwindData |  |
| 116 | `OmaDmRegistryDeleteValue` | `0x61D10` | 177 | UnwindData |  |
| 117 | `OmaDmRegistryGetAllSubKeys` | `0x61DD0` | 570 | UnwindData |  |
| 118 | `OmaDmRegistryGetAllValues` | `0x62010` | 570 | UnwindData |  |
| 119 | `OmaDmRegistryGetBinary` | `0x62250` | 223 | UnwindData |  |
| 120 | `OmaDmRegistryGetDWORD` | `0x62340` | 244 | UnwindData |  |
| 121 | `OmaDmRegistryGetString` | `0x62440` | 235 | UnwindData |  |
| 122 | `OmaDmRegistryRetrieveCurrentUsersHKCU` | `0x62540` | 229 | UnwindData |  |
| 123 | `OmaDmRegistrySetBinary` | `0x62630` | 231 | UnwindData |  |
| 124 | `OmaDmRegistrySetDWORD` | `0x62720` | 217 | UnwindData |  |
| 125 | `OmaDmRegistrySetString` | `0x62800` | 246 | UnwindData |  |
| 130 | `SetConnectionPriority` | `0x629D0` | 201 | UnwindData |  |
| 98 | `Hash_Create` | `0x62DE0` | 204 | UnwindData |  |
| 99 | `Hash_Delete` | `0x62EC0` | 287 | UnwindData |  |
| 100 | `Hash_Destroy` | `0x62FF0` | 177 | UnwindData |  |
| 101 | `Hash_DestroyCallback` | `0x630B0` | 62 | UnwindData |  |
| 102 | `Hash_EnumCallback` | `0x63100` | 297 | UnwindData |  |
| 103 | `Hash_Get` | `0x63230` | 261 | UnwindData |  |
| 104 | `Hash_Insert` | `0x63340` | 400 | UnwindData |  |
| 105 | `Hash_SetBucketThreshold` | `0x634E0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `DmGetSmbiosSerialNumber` | `0x63640` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `DmGetTpmInfo` | `0x636B0` | 514 | UnwindData |  |
| 48 | `DmGetTpmIsAlgorithmSupported` | `0x638C0` | 655 | UnwindData |  |
| 49 | `DmGetTpmState` | `0x63B60` | 717 | UnwindData |  |
| 41 | `DmGetIMEI` | `0x63E80` | 673 | UnwindData |  |
| 61 | `DmIsDeviceConnected` | `0x64130` | 163 | UnwindData |  |
| 62 | `DmIsDeviceRoaming` | `0x641E0` | 485 | UnwindData |  |
| 72 | `DmRegisterRoamingNotification` | `0x643D0` | 194 | UnwindData |  |
| 83 | `DmUnregisterRoamingNotification` | `0x644A0` | 88 | UnwindData |  |
| 95 | `GetPGListRegKeyName` | `0x64540` | 64 | UnwindData |  |
| 91 | `GetICCID` | `0x64B30` | 479 | UnwindData |  |
| 92 | `GetIMEI` | `0x64D20` | 235 | UnwindData |  |
| 93 | `GetIMSI` | `0x64E20` | 476 | UnwindData |  |
| 94 | `GetIMSIByIccID` | `0x65010` | 1,895 | UnwindData |  |
| 96 | `GetPhoneNumber` | `0x657E0` | 235 | UnwindData |  |
| 126 | `QueryPolicy` | `0x65C80` | 254 | UnwindData |  |
| 131 | `SetPolicy` | `0x65E70` | 599 | UnwindData |  |
| 16 | `DmCreateTask` | `0x66150` | 6,434 | UnwindData |  |
| 17 | `DmDeleteTask` | `0x67A80` | 1,492 | UnwindData |  |
| 18 | `DmDeleteTaskFolder` | `0x68060` | 2,293 | UnwindData |  |
| 20 | `DmDisableTask` | `0x68960` | 1,790 | UnwindData |  |
| 21 | `DmEnableTask` | `0x69070` | 1,790 | UnwindData |  |
| 66 | `DmIsTaskScheduled` | `0x69780` | 1,432 | UnwindData |  |
| 67 | `DmIsTaskScheduledAndEnabled` | `0x69D20` | 1,536 | UnwindData |  |
| 78 | `DmRunTask` | `0x6A330` | 1,419 | UnwindData |  |
| 22 | `DmEnumUsers` | `0x6AC20` | 958 | UnwindData |  |
| 33 | `DmGetActiveUserSid` | `0x6AFF0` | 586 | UnwindData |  |
| 34 | `DmGetAllActiveUserSids` | `0x6B240` | 1,241 | UnwindData |  |
| 36 | `DmGetCurrentUserSid` | `0x6B720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `DmGetCurrentUserToken` | `0x6B730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `DmGetUserSidFromToken` | `0x6B740` | 157 | UnwindData |  |
| 54 | `DmGetUserTokenFromSid` | `0x6B7F0` | 288 | UnwindData |  |
| 55 | `DmImpersonate` | `0x6B920` | 289 | UnwindData |  |
| 63 | `DmIsRunningInSystemContext` | `0x6BA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `DmIsSystemOrAdmin` | `0x6BA60` | 38 | UnwindData |  |
| 65 | `DmIsSystemOrUserIsAdmin` | `0x6BA90` | 38 | UnwindData |  |
| 77 | `DmRevertToSelf` | `0x6BAC0` | 90 | UnwindData |  |
| 1 | `BigStrcat` | `0x6DF20` | 236 | UnwindData |  |
| 3 | `CopyString` | `0x6E020` | 272 | UnwindData |  |
| 4 | `CreateBstrArray` | `0x6E140` | 347 | UnwindData |  |
| 82 | `DmStringCchPrintfAllStrings` | `0x6E2B0` | 343 | UnwindData |  |
| 89 | `EscapeStringW` | `0x6E410` | 376 | UnwindData |  |
| 106 | `InvStrCmpIW` | `0x6E590` | 145 | UnwindData |  |
| 107 | `InvStrCmpNIW` | `0x6E630` | 152 | UnwindData |  |
| 108 | `InvStrCmpNW` | `0x6E6D0` | 149 | UnwindData |  |
| 109 | `InvStrCmpW` | `0x6E770` | 144 | UnwindData |  |
| 114 | `MBToUnicode` | `0x6E810` | 351 | UnwindData |  |
| 127 | `SafeMultiByteToWideChar` | `0x6EA10` | 196 | UnwindData |  |
| 128 | `SafeStringToDword` | `0x6EAE0` | 317 | UnwindData |  |
| 129 | `SafeWideCharToMultiByte` | `0x6EC30` | 236 | UnwindData |  |
| 132 | `UnicodeToMB` | `0x6ED80` | 362 | UnwindData |  |
| 134 | `BinaryToHexString` | `0x6F090` | 23 | UnwindData |  |
| 135 | `HexStringToBinary` | `0x6F0B0` | 221 | UnwindData |  |
| 70 | `DmRaiseToastNotification` | `0x70580` | 593 | UnwindData |  |
| 71 | `DmRaiseToastNotificationAndWait` | `0x707E0` | 4,340 | UnwindData |  |
| 74 | `DmRemoveToastNotification` | `0x718E0` | 283 | UnwindData |  |
| 75 | `DmRemoveToastNotificationByExecutablePath` | `0x71A10` | 412 | UnwindData |  |
| 69 | `DmPlayNotificationSound` | `0x72A50` | 10,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DmCheckIfAadAccountLoggedOn` | `0x751A0` | 136 | UnwindData |  |
| 27 | `DmGetAadDeviceMdmEnrollmentResourceUrlForRecovery` | `0x755A0` | 1,570 | UnwindData |  |
| 28 | `DmGetAadDeviceMdmEnrollmentResourceUrlWithDiscovery` | `0x75BD0` | 385 | UnwindData |  |
| 29 | `DmGetAadDeviceToken` | `0x75D60` | 51 | UnwindData |  |
| 30 | `DmGetAadDeviceTokenWithDiscovery` | `0x75DA0` | 388 | UnwindData |  |
| 31 | `DmGetAadEnrollmentResource` | `0x75F30` | 276 | UnwindData |  |
| 32 | `DmGetAadUserToken` | `0x76050` | 58 | UnwindData |  |
| 59 | `DmInvalidateAadDeviceToken` | `0x775F0` | 52 | UnwindData |  |
| 60 | `DmInvalidateAadUserToken` | `0x77630` | 51 | UnwindData |  |
| 76 | `DmRequestAadUserToken` | `0x77670` | 50 | UnwindData |  |
| 11 | `DmCancelGetUserPermissionAsync` | `0x7AB20` | 83 | UnwindData |  |
| 50 | `DmGetUserEditFieldInput` | `0x7AB80` | 96 | UnwindData |  |
| 51 | `DmGetUserPermission` | `0x7ABF0` | 84 | UnwindData |  |
| 52 | `DmGetUserPermissionAsync` | `0x7AC50` | 273 | UnwindData |  |
| 56 | `DmInformUser` | `0x7AD70` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `DmWnfGetNotification` | `0x7AE40` | 393 | UnwindData |  |
| 85 | `DmWnfPublish` | `0x7AFD0` | 87 | UnwindData |  |
| 86 | `DmWnfQuery` | `0x7B030` | 146 | UnwindData |  |
| 12 | `DmCheckAikOld` | `0x879A0` | 209 | UnwindData |  |
| 19 | `DmDiagnoseEkAikMissingOld` | `0x87A80` | 320 | UnwindData |  |
| 24 | `DmGenerateAttestationClaimsOld` | `0x87BD0` | 2,218 | UnwindData |  |
| 25 | `DmGenerateMaaAttestationClaims` | `0x88480` | 2,791 | UnwindData |  |
| 26 | `DmGenerateMaaAttestationClaimsOld` | `0x88F70` | 2,287 | UnwindData |  |
| 42 | `DmGetKeyFromContext` | `0x89870` | 509 | UnwindData |  |
| 43 | `DmGetKeyNameFromContext` | `0x89A80` | 636 | UnwindData |  |
| 45 | `DmGetTargetAikOld` | `0x89D10` | 534 | UnwindData |  |
| 46 | `DmGetTargetAikWithRetryOld` | `0x89F30` | 551 | UnwindData |  |
| 79 | `DmSetWindowsAIKStorageLocationOld` | `0x8A160` | 785 | UnwindData |  |
| 35 | `DmGetCorrelationVectorForDmSession` | `0x94410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `DmInitializeCVForLocalConfigSession` | `0x94420` | 170,460 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
