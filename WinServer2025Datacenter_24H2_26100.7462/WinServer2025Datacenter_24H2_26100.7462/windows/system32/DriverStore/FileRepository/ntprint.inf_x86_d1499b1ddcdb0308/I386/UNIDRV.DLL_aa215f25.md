# Binary Specification: UNIDRV.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\DriverStore\FileRepository\ntprint.inf_x86_d1499b1ddcdb0308\I386\UNIDRV.DLL`
* **Architecture:** x86
* **SHA256 Fingerprint:** `aa215f25d370225ed3c29bffd933c68c321ff625ada5b188927c06ae2f30e77a`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DrvEnableDriver` | `0x25BE0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DrvDisableDriver` | `0x25CD0` | 5,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllMain` | `0x273D0` | 59,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DrvQueryDriverInfo` | `0x35D80` | 247,031 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
