# Binary Specification: AudioEng.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AudioEng.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f540c4a06baff4f70503ea97e4929f63fd007fd7c416daac52253c355540500c`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `AERT_Free` | `0x104D0` | 138 | UnwindData |  |
| 1 | `AERT_Allocate` | `0x10560` | 278 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x42E80` | 147,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllCanUnloadNow` | `0x66F60` | 75 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x67210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x67220` | 575,158 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
