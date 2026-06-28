# Binary Specification: wsp_health.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wsp_health.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6466496af5c0c84d03401bda0a9b5d39d67a4234961c27ee1f635897c80161b3`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `PreShutdown` | `0x9B40` | 4,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SetShutdownCallback` | `0x9B40` | 4,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0xAC10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SmpUnload` | `0xAC70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0xACC0` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xAD00` | 119 | UnwindData |  |
| 3 | `DllMain` | `0xAD80` | 134 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xAE10` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xAE60` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0xAFF0` | 532,224 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
