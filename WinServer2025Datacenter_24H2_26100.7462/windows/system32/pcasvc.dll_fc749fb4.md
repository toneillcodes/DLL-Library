# Binary Specification: pcasvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\pcasvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fc749fb467e00e2801bb20b31c5861497bcd333e35e8a72bb482774a30d3ba44`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `PcaPatchSdbTask` | `0x249C0` | 52 | UnwindData |  |
| 3 | `ServiceMain` | `0x43D70` | 803 | UnwindData |  |
| 2 | `PcaWallpaperAppDetect` | `0x54250` | 22,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SvchostPushServiceGlobals` | `0x59960` | 379,319 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
