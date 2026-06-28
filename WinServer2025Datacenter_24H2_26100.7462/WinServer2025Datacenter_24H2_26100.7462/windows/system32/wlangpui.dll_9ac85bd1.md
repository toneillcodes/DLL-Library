# Binary Specification: wlangpui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wlangpui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9ac85bd15da9cbd7036efc512900b6bdb1bcbc4dbd1fd0b94ddcf3cb784b5879`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xDB30` | 94 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xDBA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0xDBD0` | 73 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xDC20` | 97,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetAdPolicyAsXML` | `0x25AC0` | 661 | UnwindData |  |
| 6 | `GetWmiPolicyAsXML` | `0x25D60` | 977 | UnwindData |  |
