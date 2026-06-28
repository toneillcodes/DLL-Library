# Binary Specification: spsrx_onecore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Speech_OneCore\Engines\SR\spsrx_onecore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8199fddb19a41deaed9ebc5c042222c9e356446c4f56948c8dded48792e1dd64`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x1230` | 271 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x1EC0` | 28,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x8FE0` | 91 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x9050` | 23,885 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
