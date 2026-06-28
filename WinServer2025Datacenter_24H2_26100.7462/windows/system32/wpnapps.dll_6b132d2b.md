# Binary Specification: wpnapps.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wpnapps.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6b132d2ba1fb857b5a6ec879507bca3db0cef6b9c9aa1df493b35d49b7303235`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2A4A0` | 556 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x2EEF0` | 665 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x4A510` | 512,780 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
