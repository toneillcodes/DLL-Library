# Binary Specification: AudioEng.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\AudioEng.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `de4540cbe3a6a0f2139cec4226898a5e5d0a4cd08996dfdd6fdccac213faccde`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `AERT_Free` | `0x10550` | 138 | UnwindData |  |
| 1 | `AERT_Allocate` | `0x105E0` | 278 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x42F40` | 147,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllCanUnloadNow` | `0x66FF0` | 75 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x672A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x672B0` | 584,580 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
