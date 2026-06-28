# Binary Specification: WofUtil.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WofUtil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9c17ddbeba5b21e2eb2bc6dd71fa01c2a94cdd709db0782c59cedce73a62606e`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WofEnumEntries` | `0x1910` | 667 | UnwindData |  |
| 3 | `WofGetDriverVersion` | `0x1BC0` | 148 | UnwindData |  |
| 4 | `WofIsExternalFile` | `0x1C60` | 218 | UnwindData |  |
| 5 | `WofSetFileDataLocation` | `0x1D40` | 440 | UnwindData |  |
| 7 | `WofWimAddEntry` | `0x1F00` | 602 | UnwindData |  |
| 9 | `WofWimRemoveEntry` | `0x2160` | 206 | UnwindData |  |
| 10 | `WofWimSuspendEntry` | `0x2240` | 206 | UnwindData |  |
| 11 | `WofWimUpdateEntry` | `0x2320` | 439 | UnwindData |  |
| 2 | `WofFileEnumFiles` | `0x24E0` | 42 | UnwindData |  |
| 8 | `WofWimEnumFiles` | `0x2510` | 31 | UnwindData |  |
| 6 | `WofShouldCompressBinaries` | `0x4A50` | 2,541 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
