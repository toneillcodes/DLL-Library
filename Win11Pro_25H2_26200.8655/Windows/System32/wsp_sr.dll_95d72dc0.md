# Binary Specification: wsp_sr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wsp_sr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `95d72dc00cd208bc91eec381d32bc738f0141cf6c63263e6183ac08620459d95`
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
