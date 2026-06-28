# Binary Specification: wlidprov.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wlidprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `58dd30a4603ec26518b46c4577c7f7a84134b1ba2555f78f7d3b6750bb170fc6`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x13FF0` | 360 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x14C30` | 65 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x1EB30` | 241,820 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x1EB30` | 241,820 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
