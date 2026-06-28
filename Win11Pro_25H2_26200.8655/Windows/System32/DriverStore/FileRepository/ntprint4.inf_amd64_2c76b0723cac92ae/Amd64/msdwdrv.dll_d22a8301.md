# Binary Specification: msdwdrv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\ntprint4.inf_amd64_2c76b0723cac92ae\Amd64\msdwdrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d22a8301c49e7c369931f96ad7c3566ef5b9ccb5fa635a98ffbacb92e805fe27`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DrvDisableDriver` | `0x5230` | 10,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllMain` | `0x7CD0` | 32 | UnwindData |  |
| 3 | `DrvEnableDriver` | `0x80D0` | 124 | UnwindData |  |
| 4 | `DrvQueryDriverInfo` | `0x88D0` | 134 | UnwindData |  |
