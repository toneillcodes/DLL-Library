# Binary Specification: netcfgx.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\netcfgx.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fc98014acd27a3e5e081c2671d53a6375ffcb4953ce6822af8079cccf0c29c3c`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x2EF0` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2EF0` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x3950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x3970` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `LanaCfgFromCommandArgs` | `0x3B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `NetCfgDiagFromCommandArgs` | `0x3B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `NetCfgDiagRepairRegistryBindings` | `0x3B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `NetClassInstaller` | `0x3B90` | 251 | UnwindData |  |
| 9 | `NetPropPageProvider` | `0x3CA0` | 225 | UnwindData |  |
| 10 | `OnMachineUILanguageInit` | `0x3D90` | 47,964 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `OnMachineUILanguageSwitch` | `0x3D90` | 47,964 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
