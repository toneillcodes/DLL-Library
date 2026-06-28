# Binary Specification: basesrv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\basesrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3871785a7bee4f39ea35802b4a81e600367a6fcdc845d0d2579f1fc76b88db8a`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `ServerDllInitialization` | `0x2F50` | 417 | UnwindData |  |
| 3 | `BaseSrvNlsLogon` | `0x64C0` | 472 | UnwindData |  |
| 4 | `BaseSrvNlsUpdateRegistryCache` | `0x68E0` | 180 | UnwindData |  |
| 1 | `BaseGetProcessCrtlRoutine` | `0x6DA0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `BaseSrvRegisterSxS` | `0x6EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `BaseSetProcessCreateNotify` | `0x6ED0` | 23,195 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
