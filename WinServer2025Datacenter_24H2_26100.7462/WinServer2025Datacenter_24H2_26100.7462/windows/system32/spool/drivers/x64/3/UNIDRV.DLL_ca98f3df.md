# Binary Specification: UNIDRV.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\spool\drivers\x64\3\UNIDRV.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ca98f3df8a22fec662135c01e993f26d27ae9801a2e6dd993fa960a608769b3d`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x49520` | 123 | UnwindData |  |
| 2 | `DrvDisableDriver` | `0x495B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DrvEnableDriver` | `0x495D0` | 72 | UnwindData |  |
| 4 | `DrvQueryDriverInfo` | `0x49F20` | 68 | UnwindData |  |
