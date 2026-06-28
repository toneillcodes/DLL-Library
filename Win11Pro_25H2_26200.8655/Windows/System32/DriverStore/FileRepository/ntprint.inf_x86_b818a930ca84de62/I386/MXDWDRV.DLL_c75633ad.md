# Binary Specification: MXDWDRV.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_x86_b818a930ca84de62\I386\MXDWDRV.DLL`
* **Architecture:** x86
* **SHA256 Fingerprint:** `c75633ad54d3083534bbd8d8a68d544a760990df1a91242b7bffe634c84c4506`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x13B30` | 1,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DrvQueryDriverInfo` | `0x13FA0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DrvDisableDriver` | `0x141A0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DrvEnableDriver` | `0x142F0` | 927,320 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
