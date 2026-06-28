# Binary Specification: nlmgp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\nlmgp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a8ac58bc17f3f4c0094dda9bbd88557c75ceb9880e347f00532b52b474302f8f`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xE250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xE270` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0xE4D0` | 91 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xE540` | 37,148 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
