# Binary Specification: winbio.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\winbio.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `39358c7f161348583c0771c4e1e3cacc2a3090e56da1b8a7042127b995df4ef4`
* **Total Exported Functions:** 91

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `_BioLogonIdentifiedUser` | `0x12350` | 313 | UnwindData |  |
| 3 | `WinBioAcquireFocus` | `0x13010` | 264 | UnwindData |  |
| 4 | `WinBioAreEnhancedSignInSecurityRequirementsMet` | `0x13120` | 149 | UnwindData |  |
| 5 | `WinBioAreNonEssSensorsEnabled` | `0x131C0` | 445 | UnwindData |  |
| 6 | `WinBioAsyncEnumBiometricUnits` | `0x13390` | 440 | UnwindData |  |
| 7 | `WinBioAsyncEnumDatabases` | `0x13550` | 489 | UnwindData |  |
| 8 | `WinBioAsyncEnumServiceProviders` | `0x13740` | 489 | UnwindData |  |
| 9 | `WinBioAsyncMonitorFrameworkChanges` | `0x13930` | 490 | UnwindData |  |
| 10 | `WinBioAsyncOpenFramework` | `0x13B20` | 773 | UnwindData |  |
| 11 | `WinBioAsyncOpenSession` | `0x13E30` | 1,022 | UnwindData |  |
| 12 | `WinBioCancel` | `0x14240` | 346 | UnwindData |  |
| 13 | `WinBioCaptureSample` | `0x143A0` | 843 | UnwindData |  |
| 14 | `WinBioCaptureSampleWithCallback` | `0x14700` | 532 | UnwindData |  |
| 15 | `WinBioCloseFramework` | `0x14920` | 439 | UnwindData |  |
| 16 | `WinBioCloseSession` | `0x14AE0` | 441 | UnwindData |  |
| 17 | `WinBioConsumeFactorDeletedByService` | `0x14CA0` | 272 | UnwindData |  |
| 18 | `WinBioControlUnit` | `0x14DC0` | 1,009 | UnwindData |  |
| 19 | `WinBioControlUnitPrivileged` | `0x151C0` | 1,009 | UnwindData |  |
| 20 | `WinBioDeleteTemplate` | `0x155C0` | 798 | UnwindData |  |
| 21 | `WinBioDeleteVtl0Containers` | `0x158F0` | 115 | UnwindData |  |
| 22 | `WinBioDiscardTicket` | `0x15970` | 147 | UnwindData |  |
| 23 | `WinBioEnrollAuthorize` | `0x15A10` | 498 | UnwindData |  |
| 24 | `WinBioEnrollBegin` | `0x15C10` | 703 | UnwindData |  |
| 25 | `WinBioEnrollCapture` | `0x15EE0` | 647 | UnwindData |  |
| 26 | `WinBioEnrollCaptureWithCallback` | `0x16170` | 533 | UnwindData |  |
| 27 | `WinBioEnrollCommit` | `0x16390` | 693 | UnwindData |  |
| 28 | `WinBioEnrollDiscard` | `0x16650` | 599 | UnwindData |  |
| 29 | `WinBioEnrollRevoke` | `0x168B0` | 456 | UnwindData |  |
| 30 | `WinBioEnrollSelect` | `0x16A80` | 652 | UnwindData |  |
| 31 | `WinBioEnumBiometricUnits` | `0x16D20` | 321 | UnwindData |  |
| 32 | `WinBioEnumDatabases` | `0x16E70` | 1,841 | UnwindData |  |
| 33 | `WinBioEnumEnrollments` | `0x175B0` | 867 | UnwindData |  |
| 34 | `WinBioEnumServiceProviders` | `0x17920` | 342 | UnwindData |  |
| 35 | `WinBioFree` | `0x17A80` | 17 | UnwindData |  |
| 36 | `WinBioGetConnectedSensors` | `0x17AA0` | 185 | UnwindData |  |
| 39 | `WinBioGetDomainLogonSetting` | `0x17B60` | 208 | UnwindData |  |
| 40 | `WinBioGetEnabledSetting` | `0x17C40` | 205 | UnwindData |  |
| 41 | `WinBioGetEnhancedSignInSecurityEnrolledFactors` | `0x17D20` | 185 | UnwindData |  |
| 42 | `WinBioGetEnhancedSignInSecurityStateSource` | `0x17DE0` | 149 | UnwindData |  |
| 43 | `WinBioGetEnrolledFactors` | `0x17E80` | 250 | UnwindData |  |
| 44 | `WinBioGetEssState` | `0x17F80` | 149 | UnwindData |  |
| 45 | `WinBioGetFactorsDeletedByService` | `0x18020` | 318 | UnwindData |  |
| 46 | `WinBioGetGestureMetadata` | `0x18170` | 179 | UnwindData |  |
| 47 | `WinBioGetLastBioUseTime` | `0x18230` | 321 | UnwindData |  |
| 48 | `WinBioGetLogonSetting` | `0x18380` | 208 | UnwindData |  |
| 49 | `WinBioGetPolicyProtectionSupport` | `0x18460` | 55 | UnwindData |  |
| 50 | `WinBioGetProperty` | `0x184A0` | 994 | UnwindData |  |
| 51 | `WinBioGetProtectionPolicy` | `0x18890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `WinBioProtectDataWithPolicy` | `0x18890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `WinBioGetSetting` | `0x188A0` | 354 | UnwindData |  |
| 53 | `WinBioIdentify` | `0x18A10` | 803 | UnwindData |  |
| 54 | `WinBioIdentifyAndReleaseTicket` | `0x18D40` | 838 | UnwindData |  |
| 55 | `WinBioIdentifyWithCallback` | `0x19090` | 533 | UnwindData |  |
| 56 | `WinBioImproveBegin` | `0x192B0` | 540 | UnwindData |  |
| 57 | `WinBioImproveEnd` | `0x194E0` | 512 | UnwindData |  |
| 58 | `WinBioIsDeviceEnhancedSignInSecurityCapable` | `0x196F0` | 222 | UnwindData |  |
| 59 | `WinBioIsDeviceEnhancedSignInSecurityEnabled` | `0x197E0` | 149 | UnwindData |  |
| 60 | `WinBioIsESSCapable` | `0x19880` | 282 | UnwindData |  |
| 61 | `WinBioLocateSensor` | `0x199A0` | 674 | UnwindData |  |
| 62 | `WinBioLocateSensorWithCallback` | `0x19C50` | 533 | UnwindData |  |
| 63 | `WinBioLockUnit` | `0x19E70` | 665 | UnwindData |  |
| 64 | `WinBioLogonIdentifiedUser` | `0x1A110` | 350 | UnwindData |  |
| 65 | `WinBioMonitorPresence` | `0x1A280` | 584 | UnwindData |  |
| 66 | `WinBioNgcAuthorizeEnrollment` | `0x1A4D0` | 186 | UnwindData |  |
| 67 | `WinBioNgcCloseAuthorizationSession` | `0x1A590` | 147 | UnwindData |  |
| 68 | `WinBioNgcGetAuthorizationWithTicket` | `0x1A630` | 179 | UnwindData |  |
| 69 | `WinBioNgcOpenAuthorizationSession` | `0x1A6F0` | 216 | UnwindData |  |
| 70 | `WinBioOpenSession` | `0x1A7D0` | 820 | UnwindData |  |
| 71 | `WinBioProtectData` | `0x1AB10` | 416 | UnwindData |  |
| 73 | `WinBioRegisterEventMonitor` | `0x1ACC0` | 458 | UnwindData |  |
| 75 | `WinBioReleaseFocus` | `0x1AE90` | 264 | UnwindData |  |
| 79 | `WinBioSendTelemetry` | `0x1AFA0` | 150 | UnwindData |  |
| 82 | `WinBioSetProperty` | `0x1B040` | 1,099 | UnwindData |  |
| 83 | `WinBioSetSetting` | `0x1B4A0` | 471 | UnwindData |  |
| 84 | `WinBioUnlockUnit` | `0x1B680` | 640 | UnwindData |  |
| 85 | `WinBioUnprotectData` | `0x1B910` | 386 | UnwindData |  |
| 86 | `WinBioUnregisterEventMonitor` | `0x1BAA0` | 325 | UnwindData |  |
| 88 | `WinBioVerify` | `0x1BBF0` | 813 | UnwindData |  |
| 89 | `WinBioVerifyAndReleaseTicket` | `0x1BF30` | 863 | UnwindData |  |
| 90 | `WinBioVerifyWithCallback` | `0x1C2A0` | 545 | UnwindData |  |
| 91 | `WinBioWait` | `0x1C4D0` | 333 | UnwindData |  |
| 37 | `WinBioGetCredentialState` | `0x1CF70` | 295 | UnwindData |  |
| 38 | `WinBioGetCredentialWithTicket` | `0x1D0A0` | 381 | UnwindData |  |
| 74 | `WinBioRegisterServiceMonitor` | `0x1D230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `WinBioSetMSACredential` | `0x1D230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `WinBioUnregisterServiceMonitor` | `0x1D230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `WinBioRemoveAllCredentials` | `0x1D240` | 188 | UnwindData |  |
| 77 | `WinBioRemoveAllDomainCredentials` | `0x1D310` | 188 | UnwindData |  |
| 78 | `WinBioRemoveCredential` | `0x1D3E0` | 334 | UnwindData |  |
| 80 | `WinBioSetCredential` | `0x1D540` | 420 | UnwindData |  |
| 1 | `WinBioNotifyPasswordChange` | `0x21EC0` | 268 | UnwindData |  |
