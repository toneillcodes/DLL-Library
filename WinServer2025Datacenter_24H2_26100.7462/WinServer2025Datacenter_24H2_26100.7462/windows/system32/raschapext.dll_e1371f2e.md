# Binary Specification: raschapext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\raschapext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e1371f2e9a61e0e0bd5dd44aa6d8eec8c2d172f70539539f29d319a6ea81aa9a`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `RasChapExt_FreeMemory` | `0x2990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `RasChapExt_GetConfigForceNotDomainJoined` | `0x29B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `RasChapExt_GetConfigIgnoreIASLogon` | `0x29B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `RasChapExt_GetConfigKeepCredentialsOnFailure` | `0x29B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `RasChapExt_ShowHelp` | `0x29B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `RasChapExt_GetUserCredentials` | `0x29C0` | 1,241 | UnwindData |  |
| 10 | `RasChapExt_InvokeConfigUI` | `0x2EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `RasChapExt_InvokeInteractiveUI` | `0x2EB0` | 37,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0xC050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xC070` | 285 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xC440` | 224 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xC530` | 197 | UnwindData |  |
