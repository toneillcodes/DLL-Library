# Binary Specification: msdtclog.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msdtclog.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ae2bc84fa00a424704dd82f06e6a8e75f6bc27c64e5428ccca97dade1221c2d5`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateInstance` | `0x6520` | 106 | UnwindData |  |
| 2 | `DeleteInstance` | `0x6590` | 33 | UnwindData |  |
| 3 | `DllGetDTCLOG2` | `0x8D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetDTCLOG` | `0x8D80` | 101 | UnwindData |  |
| 5 | `DllGetClassObject` | `0x8DF0` | 187 | UnwindData |  |
| 6 | `DllRegisterServer` | `0x8F10` | 1,190 | UnwindData |  |
| 7 | `DllUnregisterServer` | `0x93C0` | 191 | UnwindData |  |
