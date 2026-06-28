# Binary Specification: igfxLHM.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\cui_dch.inf_amd64_5207db0559876a61\igfxLHM.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `393178788e111c0a4d5fed1b294f0e866de2976e2334b0a332ab59ad1324d100`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x48B0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x48E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllInstall` | `0x4900` | 125 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x49A0` | 139,372 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
