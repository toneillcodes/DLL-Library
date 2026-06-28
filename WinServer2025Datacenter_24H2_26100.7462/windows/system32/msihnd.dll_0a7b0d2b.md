# Binary Specification: msihnd.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msihnd.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0a7b0d2bbb0273824c7b86f23cb8b171858e3abd00540dfbadf2cde5ac39743c`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllRegisterServer` | `0x1FE10` | 30 | UnwindData |  |
| 2 | `DllUnregisterServer` | `0x1FE40` | 30 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x21030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x21050` | 156,236 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
