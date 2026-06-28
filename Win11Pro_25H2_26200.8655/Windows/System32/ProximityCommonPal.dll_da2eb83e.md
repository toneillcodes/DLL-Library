# Binary Specification: ProximityCommonPal.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ProximityCommonPal.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `da2eb83e2d34626dfeb888ac513f37e52c2e2646ba24c0736477fc4cab74f2d7`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `PAL_AppHasPackage` | `0x1E70` | 40 | UnwindData |  |
| 2 | `PAL_FreeTransientObjectSecurityAttribute` | `0x1EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PAL_GetAppPlatformQualifier` | `0x1EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PAL_GetSupportedBrowseTypes` | `0x1EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PAL_HoldReferenceUntilAppExit` | `0x1ED0` | 465 | UnwindData |  |
| 6 | `PAL_QueryTransientObjectSecurityAttribute` | `0x20B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `PAL_RegisterAppSuspendResumeCallback` | `0x20C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `PAL_UnregisterAppSuspendResumeCallback` | `0x20D0` | 184 | UnwindData |  |
