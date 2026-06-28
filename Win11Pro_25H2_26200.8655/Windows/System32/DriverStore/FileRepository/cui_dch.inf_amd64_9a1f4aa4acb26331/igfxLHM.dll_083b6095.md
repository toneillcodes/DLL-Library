# Binary Specification: igfxLHM.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\cui_dch.inf_amd64_9a1f4aa4acb26331\igfxLHM.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `083b609502a4bf1c427e06f2b771760d9cf9f83fd29e43268ecf95ab41252df3`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x48E0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x4910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllInstall` | `0x4930` | 125 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x49B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x49D0` | 138,540 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
