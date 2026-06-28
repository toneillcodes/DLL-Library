# Binary Specification: WpcApi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WpcApi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c4fd15a56579f4acd1ff290c3b6a6fe573107bc99e996f2119a2ac4ee10b7701`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xACB0` | 433 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xAE70` | 417 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xB020` | 242 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xB250` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0xB280` | 11,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `WpcSetupNotifyHomeSharedAccountChanged` | `0xDE80` | 22 | UnwindData |  |
