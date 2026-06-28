# Binary Specification: PSCRIPT5.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\DriverStore\FileRepository\ntprint.inf_x86_d1499b1ddcdb0308\I386\PSCRIPT5.DLL`
* **Architecture:** x86
* **SHA256 Fingerprint:** `4aa5a9e0f110bf0e3efc519cf788867bf01075a9963bfdbfeffa37fcc7b8f8ee`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0xDBE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DrvQueryDriverInfo` | `0xDC10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DrvEnableDriver` | `0xDC50` | 2,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DrvDisableDriver` | `0xE7E0` | 311,849 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
