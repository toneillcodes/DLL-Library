# Binary Specification: basesrv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\basesrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c42e7621be474afb6a282e67a4dc55611879c6d1de8d2a9fd00ee2ca29562549`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `ServerDllInitialization` | `0x2F50` | 417 | UnwindData |  |
| 3 | `BaseSrvNlsLogon` | `0x64C0` | 472 | UnwindData |  |
| 4 | `BaseSrvNlsUpdateRegistryCache` | `0x68E0` | 180 | UnwindData |  |
| 1 | `BaseGetProcessCrtlRoutine` | `0x6DA0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `BaseSrvRegisterSxS` | `0x6EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `BaseSetProcessCreateNotify` | `0x6ED0` | 25,787 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
