# Binary Specification: igfxDI.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\cui_dch.inf_amd64_b18a4e283f67c0b5\igfxDI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ab170f7fda214e91a7804c9077a5ab98047f52df597a29b1a0c983e1d116238f`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x47A0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x47D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllInstall` | `0x47F0` | 125 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x4890` | 263,038 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
