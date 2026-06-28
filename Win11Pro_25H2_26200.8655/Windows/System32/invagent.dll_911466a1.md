# Binary Specification: invagent.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\invagent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `911466a1ec649cd16b2bef2d25be0dc59142e77c8550c663cba2bd7b9b74deb4`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetDetailedAppInventoryReport` | `0x112F0` | 1,632 | UnwindData |  |
| 2 | `GetFileSigningInfoTC` | `0x11960` | 1,124 | UnwindData |  |
| 3 | `RunUpdate` | `0x17710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `RunUpdateTC` | `0x17720` | 732 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x1D0B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllGetClassObject` | `0x1D0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllRegisterServer` | `0x1D0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllUnregisterServer` | `0x1D100` | 809,786 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
