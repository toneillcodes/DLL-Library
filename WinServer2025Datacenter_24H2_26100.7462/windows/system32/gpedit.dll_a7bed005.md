# Binary Specification: gpedit.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\gpedit.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a7bed005fb41b8c380714605d85169458f9cff666143b8a23427f96ab34b3812`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 108 | `DllCanUnloadNow` | `0x1A940` | 51 | UnwindData |  |
| 109 | `DllGetClassObject` | `0x1A980` | 616 | UnwindData |  |
| 105 | `CreateGPOLink` | `0x21310` | 751 | UnwindData |  |
| 106 | `DeleteAllGPOLinks` | `0x21610` | 294 | UnwindData |  |
| 107 | `DeleteGPOLink` | `0x21740` | 757 | UnwindData |  |
| 104 | `BrowseForGPO` | `0x2DA50` | 1,229 | UnwindData |  |
| 110 | `ExportRSoPData` | `0x31FA0` | 701 | UnwindData |  |
| 111 | `ImportRSoPData` | `0x32270` | 366 | UnwindData |  |
| 100 | *Ordinal Only* | `0x33830` | 461 | UnwindData |  |
| 101 | *Ordinal Only* | `0x33A10` | 50 | UnwindData |  |
| 102 | *Ordinal Only* | `0x33A50` | 127 | UnwindData |  |
| 103 | *Ordinal Only* | `0x33AE0` | 191,698 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
