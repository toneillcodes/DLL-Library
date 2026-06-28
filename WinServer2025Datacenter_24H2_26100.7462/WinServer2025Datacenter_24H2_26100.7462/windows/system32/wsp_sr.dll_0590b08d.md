# Binary Specification: wsp_sr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wsp_sr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0590b08d5b1c18f243264cf55728433bd535d67e3ba6ee8276c995a43d3dfc9f`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0x3110` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `PreShutdown` | `0x3170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SetShutdownCallback` | `0x3170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SmpUnload` | `0x3170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x3190` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x31D0` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x3250` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x32B0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3300` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x3490` | 165,692 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
