# Binary Specification: cmstplua.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cmstplua.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8c3f3c0707ed1895092f01248c1a895f433e6376cb5eadcbe6eb4f502e11a075`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllAddRef` | `0x1950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x1960` | 53 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x19A0` | 124 | UnwindData |  |
| 4 | `DllMain` | `0x1A30` | 32 | UnwindData |  |
| 5 | `DllRelease` | `0x1A60` | 512 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
