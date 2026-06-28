# Binary Specification: MXDWDRV.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\DriverStore\FileRepository\ntprint.inf_x86_d1499b1ddcdb0308\I386\MXDWDRV.DLL`
* **Architecture:** x86
* **SHA256 Fingerprint:** `a4dbdd421e1b2df10be3951a284cd2d2c286c019f60e52a86f457f20b6ff562a`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x13D00` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DrvQueryDriverInfo` | `0x14160` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DrvDisableDriver` | `0x14360` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DrvEnableDriver` | `0x144B0` | 1,026,504 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
