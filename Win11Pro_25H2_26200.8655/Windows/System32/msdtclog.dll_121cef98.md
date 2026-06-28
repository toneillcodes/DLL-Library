# Binary Specification: msdtclog.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msdtclog.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `121cef98c365896a7afb770674b9b06a030f52ede198d27133f0ba8e308f2917`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateInstance` | `0x6320` | 106 | UnwindData |  |
| 2 | `DeleteInstance` | `0x6390` | 33 | UnwindData |  |
| 3 | `DllGetDTCLOG2` | `0x8B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetDTCLOG` | `0x8B80` | 101 | UnwindData |  |
| 5 | `DllGetClassObject` | `0x8BF0` | 187 | UnwindData |  |
| 6 | `DllRegisterServer` | `0x8D10` | 1,190 | UnwindData |  |
| 7 | `DllUnregisterServer` | `0x91C0` | 191 | UnwindData |  |
