# Binary Specification: nlmgp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\nlmgp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7bba7e2ab7066f0cd674fdbc62b838219bd24becf8af994640d1c4bc9482d218`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x15AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x15AE0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x15D40` | 91 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x15DB0` | 37,244 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
