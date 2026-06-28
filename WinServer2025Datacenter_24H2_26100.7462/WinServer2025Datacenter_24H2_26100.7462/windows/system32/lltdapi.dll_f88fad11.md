# Binary Specification: lltdapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\lltdapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f88fad1173271abbc4c713be80465daf3c9beefe0a76038e9af3fa56add569bd`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x86F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x8710` | 70 | UnwindData |  |
| 5 | `LLTDCreateMapper` | `0x95D0` | 169 | UnwindData |  |
| 3 | `LLTDCreateEnumerator` | `0x9A10` | 169 | UnwindData |  |
| 4 | `LLTDCreateMapFromXML` | `0xAB40` | 163 | UnwindData |  |
| 6 | `LLTDCreateNode` | `0xC0A0` | 225 | UnwindData |  |
