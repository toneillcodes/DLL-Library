# Binary Specification: remotepg.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\remotepg.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e728c2640f72769ddfa744d5054e2042e00137109d0ce3065d147a6069b900cd`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `LaunchRemoteUsersDialog` | `0x1B40` | 110 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x1CB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x1CE0` | 249 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x1E10` | 59,616 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
