# Binary Specification: WwaExt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WwaExt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f82fed3b80fdef09209da730e0addb8af68161baee768b90e2e28192146154a7`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllMain` | `0x10E0` | 43 | UnwindData |  |
| 15 | `WWABehaviorEnabled` | `0x1550` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetExtensionHostModuleCount` | `0x15E0` | 1,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ExtensionModulePreActivate` | `0x19D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetExtensionWebModuleCount` | `0x19E0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `GetExtensionWebMultiThreadedModuleCount` | `0x1A80` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetExtensionWebModuleFactory` | `0x1E00` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `StaticExtensionInitialization` | `0x20D0` | 113 | UnwindData |  |
| 14 | `StaticExtensionUnInitialization` | `0x22B0` | 49 | UnwindData |  |
| 1 | `CheckAllowDiagnosticsMode` | `0x54C0` | 38 | UnwindData |  |
| 2 | `DetermineCurrentDisplayRotationAngle` | `0x54F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ProcessDisplayRotation` | `0x54F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SetPhoneWerParameters` | `0x54F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetExtensionHostModuleFactory` | `0x5500` | 22 | UnwindData |  |
| 10 | `GetExtensionWebMultiThreadedModuleFactory` | `0x5520` | 22 | UnwindData |  |
