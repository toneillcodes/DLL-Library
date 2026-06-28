# Binary Specification: vpnclientpsprovider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\vpnclientpsprovider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ba0a6485ca4f24896ccd51c65f98645207f3ad68a61e06d030e7489e01aaa1d8`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0xAFC0` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0xB420` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xB460` | 119 | UnwindData |  |
| 3 | `DllMain` | `0xB4E0` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xB540` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xB590` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0xB720` | 289,473 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
