# Binary Specification: UNIDRV.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_b818a930ca84de62\Amd64\UNIDRV.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4a7b222d07ae2ceb9cbb21b8134452222c82fe9059b61605cd7d7d373ff65231`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0x49320` | 123 | UnwindData |  |
| 2 | `DrvDisableDriver` | `0x493B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DrvEnableDriver` | `0x493D0` | 72 | UnwindData |  |
| 4 | `DrvQueryDriverInfo` | `0x49D20` | 68 | UnwindData |  |
