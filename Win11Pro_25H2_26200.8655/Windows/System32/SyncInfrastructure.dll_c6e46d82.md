# Binary Specification: SyncInfrastructure.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SyncInfrastructure.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c6e46d820b8d25e567e0b94f21600054a95fd1af77af5aa8f9c2ea79d177cc73`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x7BD0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x7C00` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x7DB0` | 76 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x7E10` | 284,035 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
