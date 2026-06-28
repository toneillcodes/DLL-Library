# Binary Specification: cfgbkend.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cfgbkend.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9b27c845f7342a5c4b30f87018bdd8d89f364f544e93a1a5731d3280429cd71a`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x5870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x5890` | 281 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x5AE0` | 223 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x5BD0` | 197 | UnwindData |  |
| 1 | `CLSID_CfgComp` | `0x13468` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `IID_ISettingsComp2` | `0x13478` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `IID_ISettingsComp` | `0x13488` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `IID_ICfgComp` | `0x13498` | 0 | Indeterminate |  |
