# Binary Specification: MP3DMOD.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\MP3DMOD.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `389f6f8bbd28cac91b25ac36162bfde1396aee156df4bbcb78e98cf8151c47bb`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllGetClassObject` | `0xCA90` | 241 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0xD360` | 12,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x105F0` | 204 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x106D0` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateInstance` | `0x10B70` | 121 | UnwindData |  |
