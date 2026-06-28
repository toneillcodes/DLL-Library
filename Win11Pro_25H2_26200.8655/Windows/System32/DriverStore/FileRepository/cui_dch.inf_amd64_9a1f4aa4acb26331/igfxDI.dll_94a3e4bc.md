# Binary Specification: igfxDI.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\cui_dch.inf_amd64_9a1f4aa4acb26331\igfxDI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `94a3e4bc858571f694a488b7c725a1919a63df02c593c70d0bd1e29089bca3aa`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x47D0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x4800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllInstall` | `0x4820` | 125 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x48A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x48C0` | 261,582 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
