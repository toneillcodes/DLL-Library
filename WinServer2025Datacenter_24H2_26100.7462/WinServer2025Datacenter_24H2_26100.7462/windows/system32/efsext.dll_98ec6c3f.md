# Binary Specification: efsext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\efsext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `98ec6c3f2ae30e82d29da0a8ef3784265898a1d6a7f4ef40a7d7a8c02a56767f`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `EdpPlatform_UnregisterUserSessionNotification` | `0x7390` | 8,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `EdpPlatform_QueryUserSessionState` | `0x96B0` | 791 | UnwindData |  |
| 2 | `EdpPlatform_RegisterUserSessionNotification` | `0x99D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `EdpPlatform_ShowDialog` | `0x9A10` | 938 | UnwindData |  |
| 4 | `EdpPlatform_ShowUI` | `0x9DC0` | 43 | UnwindData |  |
| 6 | `EfsPlatform_GetCallerID` | `0x9E00` | 882 | UnwindData |  |
| 7 | `EfsPlatform_IsCallerAutomaticallyDelegated` | `0xA180` | 304 | UnwindData |  |
| 8 | `EfsPlatform_LaunchPromptUI` | `0xA2C0` | 650 | UnwindData |  |
| 9 | `EfsPlatform_SuspendNotificationsAndEncryptFile` | `0xA550` | 178 | UnwindData |  |
| 10 | `EfsPlatform_UnpackSecurePin` | `0xA610` | 777 | UnwindData |  |
| 11 | `FVE_LaunchConsentPromptUI` | `0xA920` | 569 | UnwindData |  |
| 12 | `FVE_LaunchSDCardUI` | `0xAB60` | 18,639 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
