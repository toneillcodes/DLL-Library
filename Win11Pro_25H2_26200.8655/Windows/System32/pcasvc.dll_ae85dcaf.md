# Binary Specification: pcasvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\pcasvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ae85dcaf6520adf283f6ba6ec2c0e26c4d0aff1f1b03bd73a300a95f03122f2c`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `PcaPatchSdbTask` | `0x24070` | 52 | UnwindData |  |
| 3 | `ServiceMain` | `0x41890` | 803 | UnwindData |  |
| 2 | `PcaWallpaperAppDetect` | `0x51190` | 22,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SvchostPushServiceGlobals` | `0x56920` | 379,084 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
