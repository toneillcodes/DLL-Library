# Binary Specification: PSModuleDiscoveryProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\PSModuleDiscoveryProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `08bafbb4dc8cdc8f6f1875841ab5b6bf5868078e4ddf1db6e120d6cc9358dea0`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2630` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2670` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x26F0` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2750` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x27A0` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x29C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x2A20` | 10,991 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
