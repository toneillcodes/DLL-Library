# Binary Specification: perfcore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\F12\perfcore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `33e1c7c934181c67e1ee60dd38417292a0df419944890dfe5afaf1016f0a483c`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x124B0` | 92,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x124B0` | 92,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x28F50` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x28F80` | 7,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GroupCompatibleEtwTraces` | `0x2AAE0` | 692 | UnwindData |  |
| 6 | `GroupUnifiedEtwTraces` | `0x2ADA0` | 840 | UnwindData |  |
