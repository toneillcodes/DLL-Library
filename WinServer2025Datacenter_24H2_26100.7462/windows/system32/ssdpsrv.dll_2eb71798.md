# Binary Specification: ssdpsrv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ssdpsrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2eb717987b6ba0193cb046fc6266a81993b66afbb1faf9bf736d6aef70e0b838`
* **Total Exported Functions:** 2

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ServiceMain` | `0x2A8E0` | 376 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x2AAD0` | 63,148 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
