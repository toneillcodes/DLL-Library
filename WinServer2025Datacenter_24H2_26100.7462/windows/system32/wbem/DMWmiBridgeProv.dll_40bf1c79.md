# Binary Specification: DMWmiBridgeProv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\DMWmiBridgeProv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `40bf1c79e4229b386ac28fa5cc903a8f8b5f7b72566940733c48ca7800fab4cd`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllMain` | `0x1E70` | 82 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x2A80` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2AC0` | 119 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2B40` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x2B90` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x2D20` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0x2E30` | 2,366,444 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
