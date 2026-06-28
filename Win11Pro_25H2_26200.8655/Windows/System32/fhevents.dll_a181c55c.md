# Binary Specification: fhevents.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fhevents.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a181c55c0706b5f4090caf75a26744c02614506e42a6bf0467bfba09aa9cbf4a`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DpElGetNextEvent` | `0x3DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DpElReleaseObjects` | `0x3DC0` | 190 | UnwindData |  |
| 3 | `DpElScanEvents` | `0x3E90` | 285 | UnwindData |  |
