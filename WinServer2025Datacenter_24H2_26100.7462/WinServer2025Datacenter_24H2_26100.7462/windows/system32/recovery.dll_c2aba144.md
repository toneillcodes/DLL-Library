# Binary Specification: recovery.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\recovery.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c2aba14461191ef1e878713185b0b086d6495761e63499f120a01648e6961371`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2A90` | 58 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2AD0` | 374 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x2DB0` | 40,684 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2DB0` | 40,684 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
