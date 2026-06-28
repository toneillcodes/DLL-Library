# Binary Specification: lltdapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\lltdapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ee7d7dd34b573181d06fcc245d0da20dae3dedf7a8908a88c49c09e0dafab0b9`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1C70` | 70 | UnwindData |  |
| 5 | `LLTDCreateMapper` | `0x2B30` | 169 | UnwindData |  |
| 3 | `LLTDCreateEnumerator` | `0x2F70` | 169 | UnwindData |  |
| 4 | `LLTDCreateMapFromXML` | `0x40A0` | 163 | UnwindData |  |
| 6 | `LLTDCreateNode` | `0x5600` | 225 | UnwindData |  |
