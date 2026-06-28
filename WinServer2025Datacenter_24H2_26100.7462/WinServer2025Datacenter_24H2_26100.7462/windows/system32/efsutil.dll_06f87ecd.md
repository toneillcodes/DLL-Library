# Binary Specification: efsutil.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\efsutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `06f87ecd3cf82c377e1250e0c1fb28bac4280dca7ae226cb7be3fddc0372a364`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `EfsUtilCheckCurrentKeyCapabilities` | `0x9790` | 47 | UnwindData |  |
| 3 | `EfsUtilCreateSelfSignedCertificate` | `0x97D0` | 2,043 | UnwindData |  |
| 4 | `EfsUtilFreeParsedRecoveryPolicy` | `0x9FE0` | 406 | UnwindData |  |
| 5 | `EfsUtilGetCertContextFromCertHash` | `0xA180` | 220 | UnwindData |  |
| 6 | `EfsUtilGetCertDisplayInformation` | `0xA270` | 441 | UnwindData |  |
| 7 | `EfsUtilGetCertNameFromCertContext` | `0xA430` | 424 | UnwindData |  |
| 8 | `EfsUtilGetCurrentKey` | `0xA5E0` | 432 | UnwindData |  |
| 9 | `EfsUtilGetCurrentKey_Deprecated` | `0xA7A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `EfsUtilGetCurrentUserInformation` | `0xA7B0` | 742 | UnwindData |  |
| 11 | `EfsUtilGetProvider` | `0xAAA0` | 404 | UnwindData |  |
| 12 | `EfsUtilGetPublicKeyType` | `0xAC40` | 744 | UnwindData |  |
| 13 | `EfsUtilGetSmartcardProviderName` | `0xAF30` | 758 | UnwindData |  |
| 14 | `EfsUtilGetUserKey` | `0xB230` | 199 | UnwindData |  |
| 15 | `EfsUtilIsSmartcardKey` | `0xB300` | 217 | UnwindData |  |
| 16 | `EfsUtilIsSmartcardProvider` | `0xB3E0` | 181 | UnwindData |  |
| 17 | `EfsUtilParseDataRecoveryPolicy_1_1` | `0xB4A0` | 1,007 | UnwindData |  |
| 23 | `EfsUtilReleaseProvider` | `0xB8A0` | 75 | UnwindData |  |
| 24 | `EfsUtilReleaseUserKey` | `0xB900` | 115 | UnwindData |  |
| 25 | `EfsUtilSetCurrentKey` | `0xB980` | 315 | UnwindData |  |
| 26 | `EfsUtilSetSmartcardPin` | `0xBAD0` | 291 | UnwindData |  |
| 27 | `EfsUtilSmartcardCredsNeededError` | `0xBC00` | 5,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `EfsUtilApplyGroupPolicy` | `0xD170` | 401 | UnwindData |  |
| 18 | `EfsUtilPdeConvertPathsInPolicy` | `0x180D0` | 5,652 | UnwindData |  |
| 19 | `EfsUtilPdeCreateMaintenanceTaskIfNeeded` | `0x196F0` | 54 | UnwindData |  |
| 20 | `EfsUtilPdeGetConversionModeFromModeStr` | `0x19730` | 167 | UnwindData |  |
| 21 | `EfsUtilPdeGetConversionModeStrFromMode` | `0x197E0` | 167 | UnwindData |  |
| 22 | `EfsUtilPdeTriggerPathsConversionIfNeeded` | `0x19890` | 1,374 | UnwindData |  |
