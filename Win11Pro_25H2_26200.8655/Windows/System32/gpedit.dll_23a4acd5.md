# Binary Specification: gpedit.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\gpedit.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `23a4acd5ca99b5522829773abec5a8b23f7d6dd13f1a7f92394e0ddda78517ce`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 108 | `DllCanUnloadNow` | `0x19270` | 51 | UnwindData |  |
| 109 | `DllGetClassObject` | `0x192B0` | 616 | UnwindData |  |
| 105 | `CreateGPOLink` | `0x1FB90` | 737 | UnwindData |  |
| 106 | `DeleteAllGPOLinks` | `0x1FE80` | 294 | UnwindData |  |
| 107 | `DeleteGPOLink` | `0x1FFB0` | 743 | UnwindData |  |
| 104 | `BrowseForGPO` | `0x2C190` | 1,222 | UnwindData |  |
| 110 | `ExportRSoPData` | `0x302A0` | 701 | UnwindData |  |
| 111 | `ImportRSoPData` | `0x30570` | 366 | UnwindData |  |
| 100 | *Ordinal Only* | `0x31B30` | 461 | UnwindData |  |
| 101 | *Ordinal Only* | `0x31D10` | 50 | UnwindData |  |
| 102 | *Ordinal Only* | `0x31D50` | 127 | UnwindData |  |
| 103 | *Ordinal Only* | `0x31DE0` | 188,674 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
