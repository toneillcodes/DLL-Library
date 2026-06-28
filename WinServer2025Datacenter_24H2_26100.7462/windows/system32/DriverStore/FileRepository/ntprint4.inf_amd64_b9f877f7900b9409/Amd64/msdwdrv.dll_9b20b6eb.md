# Binary Specification: msdwdrv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\DriverStore\FileRepository\ntprint4.inf_amd64_b9f877f7900b9409\Amd64\msdwdrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9b20b6eb887287edd58b5e1aa222d1dbfb4b71498df05794275f5ab99de3f406`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DrvDisableDriver` | `0x5220` | 10,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllMain` | `0x7CC0` | 32 | UnwindData |  |
| 3 | `DrvEnableDriver` | `0x80C0` | 124 | UnwindData |  |
| 4 | `DrvQueryDriverInfo` | `0x88C0` | 134 | UnwindData |  |
