# Binary Specification: umpo.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\umpo.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f6e39895facb2e1556f1ff418a46bf8bfd4f2f83975e43551407437aeaba02d4`
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
| 8 | `UmpoFree` | `0xC9D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `UmpoAllocate` | `0xCA20` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `UmpoNotificationHandler` | `0xCF30` | 725 | UnwindData |  |
| 16 | `UmpoMain` | `0x15960` | 1,672 | UnwindData |  |
| 3 | `PtrUmpoOnAcPower` | `0x253E4` | 1,820 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `PtrUmpoDisplayState` | `0x25B00` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PtrUmpoProviderHandle` | `0x26150` | 425 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `PtrUmpoFullPowerPlanSupportDisabled` | `0x262F9` | 391 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PtrUmpoSchemeLock` | `0x26480` | 0 | Indeterminate |  |
