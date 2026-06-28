# Binary Specification: UNIDRV.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\DriverStore\FileRepository\ntprint.inf_amd64_d1499b1ddcdb0308\Amd64\UNIDRV.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5663c5d9b07180ec0637471ca8e68c78da39b83ea760da6be8846486a770b1a2`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x49520` | 123 | UnwindData |  |
| 2 | `DrvDisableDriver` | `0x495B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DrvEnableDriver` | `0x495D0` | 72 | UnwindData |  |
| 4 | `DrvQueryDriverInfo` | `0x49F20` | 68 | UnwindData |  |
