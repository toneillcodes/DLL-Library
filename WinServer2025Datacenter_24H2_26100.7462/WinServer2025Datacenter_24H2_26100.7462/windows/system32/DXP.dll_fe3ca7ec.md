# Binary Specification: DXP.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\DXP.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fe3ca7ecff9be2741a34503d74ffecadc7f4e388f1f44fb690537526acd3cf16`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1890` | 9,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x3F80` | 350 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xBC40` | 160,652 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0xBC40` | 160,652 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
