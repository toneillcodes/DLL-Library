# Binary Specification: IMTCCORE.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\IME\IMETC\IMTCCORE.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e92e3ba5d66a91b97278b7681a8448f779cb9cb7ea47403e576820a46967d060`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateUDicProxy` | `0xDD70` | 3,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0xEB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xEBA0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0xECF0` | 418 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xEEA0` | 48 | UnwindData |  |
