# Binary Specification: TtlsAuth.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\TtlsAuth.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8503faac078aecb3659dc11d78312aedcf5c833accf2870d38ff3c5c38812cd2`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `EapPeerGetInfo` | `0xBB50` | 169 | UnwindData |  |
| 6 | `EapPeerFreeMemory` | `0xF220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EapPeerFreeErrorMemory` | `0xF230` | 51 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x12710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x12730` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x12920` | 91 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x12990` | 17 | UnwindData |  |
