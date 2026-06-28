# Binary Specification: winbio.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\winbio.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `aa1e133e914f75737eb5b4a0b816c7c57c804d700b10bfc90cc2f6ea96e4f162`
* **Total Exported Functions:** 91

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `_BioLogonIdentifiedUser` | `0x11C90` | 313 | UnwindData |  |
| 3 | `WinBioAcquireFocus` | `0x12A80` | 264 | UnwindData |  |
| 4 | `WinBioAreEnhancedSignInSecurityRequirementsMet` | `0x12B90` | 149 | UnwindData |  |
| 5 | `WinBioAreNonEssSensorsEnabled` | `0x12C30` | 122 | UnwindData |  |
| 6 | `WinBioAsyncEnumBiometricUnits` | `0x12CB0` | 440 | UnwindData |  |
| 7 | `WinBioAsyncEnumDatabases` | `0x12E70` | 489 | UnwindData |  |
| 8 | `WinBioAsyncEnumServiceProviders` | `0x13060` | 489 | UnwindData |  |
| 9 | `WinBioAsyncMonitorFrameworkChanges` | `0x13250` | 490 | UnwindData |  |
| 10 | `WinBioAsyncOpenFramework` | `0x13440` | 773 | UnwindData |  |
| 11 | `WinBioAsyncOpenSession` | `0x13750` | 1,022 | UnwindData |  |
| 12 | `WinBioCancel` | `0x13B60` | 346 | UnwindData |  |
| 13 | `WinBioCaptureSample` | `0x13CC0` | 843 | UnwindData |  |
| 14 | `WinBioCaptureSampleWithCallback` | `0x14020` | 532 | UnwindData |  |
| 15 | `WinBioCloseFramework` | `0x14240` | 439 | UnwindData |  |
| 16 | `WinBioCloseSession` | `0x14400` | 441 | UnwindData |  |
| 17 | `WinBioConsumeFactorDeletedByService` | `0x145C0` | 272 | UnwindData |  |
| 18 | `WinBioControlUnit` | `0x146E0` | 1,009 | UnwindData |  |
| 19 | `WinBioControlUnitPrivileged` | `0x14AE0` | 1,009 | UnwindData |  |
| 20 | `WinBioDeleteTemplate` | `0x14EE0` | 798 | UnwindData |  |
| 21 | `WinBioDeleteVtl0Containers` | `0x15210` | 115 | UnwindData |  |
| 22 | `WinBioDiscardTicket` | `0x15290` | 147 | UnwindData |  |
| 23 | `WinBioEnrollAuthorize` | `0x15330` | 498 | UnwindData |  |
| 24 | `WinBioEnrollBegin` | `0x15530` | 703 | UnwindData |  |
| 25 | `WinBioEnrollCapture` | `0x15800` | 647 | UnwindData |  |
| 26 | `WinBioEnrollCaptureWithCallback` | `0x15A90` | 533 | UnwindData |  |
| 27 | `WinBioEnrollCommit` | `0x15CB0` | 693 | UnwindData |  |
| 28 | `WinBioEnrollDiscard` | `0x15F70` | 599 | UnwindData |  |
| 29 | `WinBioEnrollRevoke` | `0x161D0` | 456 | UnwindData |  |
| 30 | `WinBioEnrollSelect` | `0x163A0` | 652 | UnwindData |  |
| 31 | `WinBioEnumBiometricUnits` | `0x16640` | 321 | UnwindData |  |
| 32 | `WinBioEnumDatabases` | `0x16790` | 1,841 | UnwindData |  |
| 33 | `WinBioEnumEnrollments` | `0x16ED0` | 867 | UnwindData |  |
| 34 | `WinBioEnumServiceProviders` | `0x17240` | 342 | UnwindData |  |
| 35 | `WinBioFree` | `0x173A0` | 17 | UnwindData |  |
| 36 | `WinBioGetConnectedSensors` | `0x173C0` | 185 | UnwindData |  |
| 39 | `WinBioGetDomainLogonSetting` | `0x17480` | 208 | UnwindData |  |
| 40 | `WinBioGetEnabledSetting` | `0x17560` | 205 | UnwindData |  |
| 41 | `WinBioGetEnhancedSignInSecurityEnrolledFactors` | `0x17640` | 185 | UnwindData |  |
| 42 | `WinBioGetEnhancedSignInSecurityStateSource` | `0x17700` | 149 | UnwindData |  |
| 43 | `WinBioGetEnrolledFactors` | `0x177A0` | 250 | UnwindData |  |
| 44 | `WinBioGetEssState` | `0x178A0` | 149 | UnwindData |  |
| 45 | `WinBioGetFactorsDeletedByService` | `0x17940` | 318 | UnwindData |  |
| 46 | `WinBioGetGestureMetadata` | `0x17A90` | 179 | UnwindData |  |
| 47 | `WinBioGetLastBioUseTime` | `0x17B50` | 321 | UnwindData |  |
| 48 | `WinBioGetLogonSetting` | `0x17CA0` | 208 | UnwindData |  |
| 49 | `WinBioGetPolicyProtectionSupport` | `0x17D80` | 55 | UnwindData |  |
| 50 | `WinBioGetProperty` | `0x17DC0` | 994 | UnwindData |  |
| 51 | `WinBioGetProtectionPolicy` | `0x181B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `WinBioProtectDataWithPolicy` | `0x181B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `WinBioGetSetting` | `0x181C0` | 354 | UnwindData |  |
| 53 | `WinBioIdentify` | `0x18330` | 803 | UnwindData |  |
| 54 | `WinBioIdentifyAndReleaseTicket` | `0x18660` | 838 | UnwindData |  |
| 55 | `WinBioIdentifyWithCallback` | `0x189B0` | 533 | UnwindData |  |
| 56 | `WinBioImproveBegin` | `0x18BD0` | 540 | UnwindData |  |
| 57 | `WinBioImproveEnd` | `0x18E00` | 512 | UnwindData |  |
| 58 | `WinBioIsDeviceEnhancedSignInSecurityCapable` | `0x19010` | 121 | UnwindData |  |
| 59 | `WinBioIsDeviceEnhancedSignInSecurityEnabled` | `0x19090` | 149 | UnwindData |  |
| 60 | `WinBioIsESSCapable` | `0x19130` | 287 | UnwindData |  |
| 61 | `WinBioLocateSensor` | `0x19260` | 674 | UnwindData |  |
| 62 | `WinBioLocateSensorWithCallback` | `0x19510` | 533 | UnwindData |  |
| 63 | `WinBioLockUnit` | `0x19730` | 665 | UnwindData |  |
| 64 | `WinBioLogonIdentifiedUser` | `0x199D0` | 350 | UnwindData |  |
| 65 | `WinBioMonitorPresence` | `0x19B40` | 584 | UnwindData |  |
| 66 | `WinBioNgcAuthorizeEnrollment` | `0x19D90` | 186 | UnwindData |  |
| 67 | `WinBioNgcCloseAuthorizationSession` | `0x19E50` | 147 | UnwindData |  |
| 68 | `WinBioNgcGetAuthorizationWithTicket` | `0x19EF0` | 179 | UnwindData |  |
| 69 | `WinBioNgcOpenAuthorizationSession` | `0x19FB0` | 216 | UnwindData |  |
| 70 | `WinBioOpenSession` | `0x1A090` | 820 | UnwindData |  |
| 71 | `WinBioProtectData` | `0x1A3D0` | 416 | UnwindData |  |
| 73 | `WinBioRegisterEventMonitor` | `0x1A580` | 458 | UnwindData |  |
| 75 | `WinBioReleaseFocus` | `0x1A750` | 264 | UnwindData |  |
| 79 | `WinBioSendTelemetry` | `0x1A860` | 150 | UnwindData |  |
| 82 | `WinBioSetProperty` | `0x1A900` | 1,099 | UnwindData |  |
| 83 | `WinBioSetSetting` | `0x1AD60` | 530 | UnwindData |  |
| 84 | `WinBioUnlockUnit` | `0x1AF80` | 640 | UnwindData |  |
| 85 | `WinBioUnprotectData` | `0x1B210` | 386 | UnwindData |  |
| 86 | `WinBioUnregisterEventMonitor` | `0x1B3A0` | 325 | UnwindData |  |
| 88 | `WinBioVerify` | `0x1B4F0` | 813 | UnwindData |  |
| 89 | `WinBioVerifyAndReleaseTicket` | `0x1B830` | 863 | UnwindData |  |
| 90 | `WinBioVerifyWithCallback` | `0x1BBA0` | 545 | UnwindData |  |
| 91 | `WinBioWait` | `0x1BDD0` | 333 | UnwindData |  |
| 37 | `WinBioGetCredentialState` | `0x1C870` | 295 | UnwindData |  |
| 38 | `WinBioGetCredentialWithTicket` | `0x1C9A0` | 381 | UnwindData |  |
| 74 | `WinBioRegisterServiceMonitor` | `0x1CB30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `WinBioSetMSACredential` | `0x1CB30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `WinBioUnregisterServiceMonitor` | `0x1CB30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `WinBioRemoveAllCredentials` | `0x1CB40` | 188 | UnwindData |  |
| 77 | `WinBioRemoveAllDomainCredentials` | `0x1CC10` | 188 | UnwindData |  |
| 78 | `WinBioRemoveCredential` | `0x1CCE0` | 334 | UnwindData |  |
| 80 | `WinBioSetCredential` | `0x1CE40` | 420 | UnwindData |  |
| 1 | `WinBioNotifyPasswordChange` | `0x217F0` | 268 | UnwindData |  |
