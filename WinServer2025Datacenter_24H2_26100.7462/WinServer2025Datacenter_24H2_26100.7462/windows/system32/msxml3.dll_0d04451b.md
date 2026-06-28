# Binary Specification: msxml3.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msxml3.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0d04451ba2081ad9f3bac7c6a9b8be8ef18e0816a6ae63b34c0c92169121038b`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x384A0` | 902 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x40520` | 142 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x45620` | 20,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x45620` | 20,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllMain` | `0x4A6C0` | 802,236 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
