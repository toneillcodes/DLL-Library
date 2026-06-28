# Binary Specification: EhStorShell.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\EhStorShell.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e6c6a328d6f9ba4ecd65aef2f7ece46b39208efac93216474e5f4746b5590639`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x19B0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x5B60` | 240 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x8650` | 43,084 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x8650` | 43,084 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
