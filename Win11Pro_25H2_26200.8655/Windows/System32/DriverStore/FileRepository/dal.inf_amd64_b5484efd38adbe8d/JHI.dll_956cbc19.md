# Binary Specification: JHI.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\dal.inf_amd64_b5484efd38adbe8d\JHI.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `956cbc19c15ae5ce2388c21820f6ebf928d5684bf3ab669ec934509ef5e8d5c6`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `JHI_Initialize` | `0x9120` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `JHI_Deinit` | `0x9470` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `JHI_CreateSession` | `0x9890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `JHI_SendAndRecv2` | `0x98B0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `JHI_Install2` | `0x9A20` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `JHI_Uninstall` | `0x9C50` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `JHI_GetAppletProperty` | `0x9DD0` | 1,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `JHI_GetSessionsCount` | `0xA350` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `JHI_CloseSession` | `0xA750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `JHI_ForceCloseSession` | `0xA770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `JHI_GetSessionInfo` | `0xA790` | 1,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `JHI_RegisterEvents` | `0xADD0` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `JHI_UnRegisterEvents` | `0xB0C0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `JHI_GetVersionInfo` | `0xB230` | 121,674 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
