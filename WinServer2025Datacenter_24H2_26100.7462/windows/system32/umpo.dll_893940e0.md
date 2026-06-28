# Binary Specification: umpo.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\umpo.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `893940e06954c234e300a1770689e92a9ee2e0407f73a5a958c0db6b07e77afc`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 18 | `UmpoNotifyKernelAllPowerPolicyChanged` | `0x5610` | 502 | UnwindData |  |
| 20 | `UmpoWriteToUserPowerKey` | `0x5F00` | 517 | UnwindData |  |
| 12 | `UmpoInternalDataAccessorToString` | `0x6110` | 22 | UnwindData |  |
| 13 | `UmpoInternalGetKeyValueGuid` | `0x6160` | 282 | UnwindData |  |
| 19 | `UmpoSendKernelPowerPolicyNotification` | `0x69A0` | 74 | UnwindData |  |
| 7 | `UmpoAlpcSendPowerMessage` | `0x6CF0` | 58 | UnwindData |  |
| 9 | `UmpoGetActiveScheme` | `0x73A0` | 142 | UnwindData |  |
| 14 | `UmpoInternalOpenGUIDSubKey` | `0x7610` | 81 | UnwindData |  |
| 11 | `UmpoInternalConvertGuidToString` | `0x7970` | 277 | UnwindData |  |
| 15 | `UmpoInternalOpenUserPowerKey` | `0x8250` | 203 | UnwindData |  |
| 10 | `UmpoInternalCloseUserPowerKey` | `0x8A80` | 92 | UnwindData |  |
| 8 | `UmpoFree` | `0xCA10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `UmpoAllocate` | `0xCA60` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `UmpoNotificationHandler` | `0xCF70` | 725 | UnwindData |  |
| 16 | `UmpoMain` | `0x16950` | 1,672 | UnwindData |  |
| 3 | `PtrUmpoOnAcPower` | `0x273E4` | 1,884 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `PtrUmpoDisplayState` | `0x27B40` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PtrUmpoProviderHandle` | `0x28250` | 425 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `PtrUmpoFullPowerPlanSupportDisabled` | `0x283F9` | 391 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PtrUmpoSchemeLock` | `0x28580` | 0 | Indeterminate |  |
