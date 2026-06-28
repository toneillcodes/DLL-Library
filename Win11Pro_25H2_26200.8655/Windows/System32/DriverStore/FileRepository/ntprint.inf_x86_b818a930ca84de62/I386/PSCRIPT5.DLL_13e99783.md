# Binary Specification: PSCRIPT5.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_x86_b818a930ca84de62\I386\PSCRIPT5.DLL`
* **Architecture:** x86
* **SHA256 Fingerprint:** `13e99783e9ea098ac2e0ce0f3f5d892c5542507a7515bc425e0bef8091892580`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0xDBE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DrvQueryDriverInfo` | `0xDC10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DrvEnableDriver` | `0xDC50` | 2,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DrvDisableDriver` | `0xE7E0` | 311,881 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
