# Binary Specification: certmgr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\certmgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `094912385df09f332dc15ee2c3e6aba44f8a220663f7a670fad9a66c0dae8e56`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0x14590` | 14,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x14590` | 14,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x17E10` | 143 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x17EB0` | 52 | UnwindData |  |
| 3 | `DllInstall` | `0x17EF0` | 681,788 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
