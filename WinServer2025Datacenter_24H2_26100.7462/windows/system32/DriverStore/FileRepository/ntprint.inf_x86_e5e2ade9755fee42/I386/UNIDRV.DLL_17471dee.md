# Binary Specification: UNIDRV.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\DriverStore\FileRepository\ntprint.inf_x86_e5e2ade9755fee42\I386\UNIDRV.DLL`
* **Architecture:** x86
* **SHA256 Fingerprint:** `17471dee23a2ed62f6211b0e7da014331b18a975cf1873276d8f3534a72820eb`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DrvEnableDriver` | `0x25BE0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DrvDisableDriver` | `0x25CD0` | 5,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllMain` | `0x273D0` | 59,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DrvQueryDriverInfo` | `0x35D80` | 247,031 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
