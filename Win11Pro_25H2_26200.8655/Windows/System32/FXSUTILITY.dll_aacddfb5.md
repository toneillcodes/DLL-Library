# Binary Specification: FXSUTILITY.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\FXSUTILITY.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `aacddfb5344b8af6c0acf18075750ea5ff8378f5d95848ae124ccb684741453b`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `GetProxyDllInfo` | `0x1FF0` | 12,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x4F60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x4F90` | 129 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x50F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x5130` | 94 | UnwindData |  |
| 1 | `CanSendToFaxRecipient` | `0x5690` | 174 | UnwindData |  |
| 7 | `SendToFaxRecipient` | `0x5750` | 645 | UnwindData |  |
