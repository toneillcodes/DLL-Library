# Binary Specification: directmanipulation.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\directmanipulation.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9dd9fa794fbf24774b968fa2ae82614e6dd80f234cd2d6049666096d33a65935`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllGetClassObject` | `0x4ADE0` | 647 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x4B530` | 413 | UnwindData |  |
| 1 | `InitializeDManipHook` | `0x574F0` | 50,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetActivationFactory` | `0x638F0` | 127 | UnwindData |  |
