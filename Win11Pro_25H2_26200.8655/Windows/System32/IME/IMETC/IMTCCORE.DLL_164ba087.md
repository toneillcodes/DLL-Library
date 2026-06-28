# Binary Specification: IMTCCORE.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\IME\IMETC\IMTCCORE.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `164ba08729f08b86660efa054aa319ddb93ef18ef731578f5ce6c0a881947e29`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateUDicProxy` | `0xDE50` | 3,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0xEC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xEC80` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0xEDD0` | 418 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xEF80` | 48 | UnwindData |  |
