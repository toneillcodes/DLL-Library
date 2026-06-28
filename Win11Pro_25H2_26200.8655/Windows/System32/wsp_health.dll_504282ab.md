# Binary Specification: wsp_health.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wsp_health.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `504282ab0a40e1cc1c3222c239d781a24930144d6f6e827c16d8951254e4dfd8`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `PreShutdown` | `0x9BE0` | 4,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SetShutdownCallback` | `0x9BE0` | 4,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MI_Main` | `0xACB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SmpUnload` | `0xAD10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0xAD60` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xADA0` | 119 | UnwindData |  |
| 3 | `DllMain` | `0xAE20` | 134 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xAEB0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xAF00` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0xB090` | 532,272 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
