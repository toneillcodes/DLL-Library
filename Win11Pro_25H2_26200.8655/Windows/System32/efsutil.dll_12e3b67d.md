# Binary Specification: efsutil.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\efsutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `12e3b67d85a297cdded37e40e869cf0082e971e4c3b0d7c31bcf4a783d481712`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `EfsUtilCheckCurrentKeyCapabilities` | `0x97A0` | 47 | UnwindData |  |
| 3 | `EfsUtilCreateSelfSignedCertificate` | `0x97E0` | 2,043 | UnwindData |  |
| 4 | `EfsUtilFreeParsedRecoveryPolicy` | `0x9FF0` | 406 | UnwindData |  |
| 5 | `EfsUtilGetCertContextFromCertHash` | `0xA190` | 220 | UnwindData |  |
| 6 | `EfsUtilGetCertDisplayInformation` | `0xA280` | 441 | UnwindData |  |
| 7 | `EfsUtilGetCertNameFromCertContext` | `0xA440` | 424 | UnwindData |  |
| 8 | `EfsUtilGetCurrentKey` | `0xA5F0` | 432 | UnwindData |  |
| 9 | `EfsUtilGetCurrentKey_Deprecated` | `0xA7B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `EfsUtilGetCurrentUserInformation` | `0xA7C0` | 742 | UnwindData |  |
| 11 | `EfsUtilGetProvider` | `0xAAB0` | 404 | UnwindData |  |
| 12 | `EfsUtilGetPublicKeyType` | `0xAC50` | 744 | UnwindData |  |
| 13 | `EfsUtilGetSmartcardProviderName` | `0xAF40` | 758 | UnwindData |  |
| 14 | `EfsUtilGetUserKey` | `0xB240` | 199 | UnwindData |  |
| 15 | `EfsUtilIsSmartcardKey` | `0xB310` | 217 | UnwindData |  |
| 16 | `EfsUtilIsSmartcardProvider` | `0xB3F0` | 181 | UnwindData |  |
| 17 | `EfsUtilParseDataRecoveryPolicy_1_1` | `0xB4B0` | 1,007 | UnwindData |  |
| 23 | `EfsUtilReleaseProvider` | `0xB8B0` | 75 | UnwindData |  |
| 24 | `EfsUtilReleaseUserKey` | `0xB910` | 115 | UnwindData |  |
| 25 | `EfsUtilSetCurrentKey` | `0xB990` | 315 | UnwindData |  |
| 26 | `EfsUtilSetSmartcardPin` | `0xBAE0` | 291 | UnwindData |  |
| 27 | `EfsUtilSmartcardCredsNeededError` | `0xBC10` | 5,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `EfsUtilApplyGroupPolicy` | `0xD180` | 401 | UnwindData |  |
| 18 | `EfsUtilPdeConvertPathsInPolicy` | `0x180E0` | 5,660 | UnwindData |  |
| 19 | `EfsUtilPdeCreateMaintenanceTaskIfNeeded` | `0x19710` | 54 | UnwindData |  |
| 20 | `EfsUtilPdeGetConversionModeFromModeStr` | `0x19750` | 167 | UnwindData |  |
| 21 | `EfsUtilPdeGetConversionModeStrFromMode` | `0x19800` | 167 | UnwindData |  |
| 22 | `EfsUtilPdeTriggerPathsConversionIfNeeded` | `0x198B0` | 1,374 | UnwindData |  |
