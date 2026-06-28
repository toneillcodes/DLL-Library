# Binary Specification: wlangpui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wlangpui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `236f77643f615d01741a829f8e663861057ea3eaa8d5b682275a83289c933da9`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xDB40` | 94 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xDBB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0xDBE0` | 73 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xDC30` | 97,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetAdPolicyAsXML` | `0x25AD0` | 661 | UnwindData |  |
| 6 | `GetWmiPolicyAsXML` | `0x25D70` | 977 | UnwindData |  |
