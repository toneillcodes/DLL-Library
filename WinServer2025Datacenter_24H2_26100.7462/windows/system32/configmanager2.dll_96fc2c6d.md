# Binary Specification: configmanager2.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\configmanager2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `96fc2c6d47e90baf90b9a878bbf25ec031bfa634f2160ccce7726d934e6125fe`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CmLockSvcInit` | `0x105C0` | 789 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x35E70` | 287 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x3E5C0` | 5,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CmLockSvcDeinit` | `0x3FA90` | 256,892 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
