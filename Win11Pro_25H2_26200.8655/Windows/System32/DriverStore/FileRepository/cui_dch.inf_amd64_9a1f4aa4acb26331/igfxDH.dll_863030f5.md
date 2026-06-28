# Binary Specification: igfxDH.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\cui_dch.inf_amd64_9a1f4aa4acb26331\igfxDH.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `863030f56689e96dc85c8c60040610d95ab852eb5df3d7a775f90feb99e64384`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x4920` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x4950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllInstall` | `0x4970` | 125 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x49F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x4A10` | 572,414 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
