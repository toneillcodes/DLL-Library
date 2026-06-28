# Binary Specification: pdm.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\F12\pdm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b853b860dc77d7c239db404540bbafe3e9e8d600779a0b410986ce43bcbad8dd`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2A3B0` | 78 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2A400` | 290 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x2A530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2A540` | 192,988 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
