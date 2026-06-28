# Binary Specification: mycomput.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mycomput.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8863249ea18fc53718f31fe6c203d4a84d1af14d25ae87843e6d0822947c8190`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x3BA0` | 86 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x3C00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x3C30` | 1,001 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x4020` | 33 | UnwindData |  |
