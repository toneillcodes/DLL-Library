# Binary Specification: efsext.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\efsext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5d05096756937bac7b14073cb10d32f7291f8b3d0d0882f4877c92b0c43f8e57`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `EdpPlatform_UnregisterUserSessionNotification` | `0x73A0` | 8,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `EdpPlatform_QueryUserSessionState` | `0x96C0` | 791 | UnwindData |  |
| 2 | `EdpPlatform_RegisterUserSessionNotification` | `0x99E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `EdpPlatform_ShowDialog` | `0x9A20` | 938 | UnwindData |  |
| 4 | `EdpPlatform_ShowUI` | `0x9DD0` | 43 | UnwindData |  |
| 6 | `EfsPlatform_GetCallerID` | `0x9E10` | 882 | UnwindData |  |
| 7 | `EfsPlatform_IsCallerAutomaticallyDelegated` | `0xA190` | 304 | UnwindData |  |
| 8 | `EfsPlatform_LaunchPromptUI` | `0xA2D0` | 650 | UnwindData |  |
| 9 | `EfsPlatform_SuspendNotificationsAndEncryptFile` | `0xA560` | 178 | UnwindData |  |
| 10 | `EfsPlatform_UnpackSecurePin` | `0xA620` | 777 | UnwindData |  |
| 11 | `FVE_LaunchConsentPromptUI` | `0xA930` | 569 | UnwindData |  |
| 12 | `FVE_LaunchSDCardUI` | `0xAB70` | 18,639 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
