# Binary Specification: UNIDRV.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_x86_b818a930ca84de62\I386\UNIDRV.DLL`
* **Architecture:** x86
* **SHA256 Fingerprint:** `ae49f4b5fb22cdde97c25b17b1cc3af7e63d6b19c12696dd2f42e2cac6910df1`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DrvEnableDriver` | `0x25DE0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DrvDisableDriver` | `0x25ED0` | 6,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllMain` | `0x276B0` | 65,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DrvQueryDriverInfo` | `0x374F0` | 246,247 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
