# Binary Specification: AuthBroker.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AuthBroker.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `775a0c9fa21664a09c1e15f7debaceb5d53c1dfcd1443fca5a653fd8d6b37b93`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllCanUnloadNow` | `0x3D60` | 102 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x3DD0` | 165 | UnwindData |  |
| 7 | `DllGetActivationFactory` | `0x4510` | 146 | UnwindData |  |
| 4 | `AuthBrokerFreeClientContext` | `0x5A90` | 198 | UnwindData |  |
| 10 | `DllRegisterServer` | `0xA930` | 13,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `FindCallingThreadImmersiveWindow` | `0xDE20` | 720 | UnwindData |  |
| 2 | `AuthBrokerClearThreadClientContext` | `0x114D0` | 236 | UnwindData |  |
| 3 | `AuthBrokerCreateClientContext` | `0x115D0` | 322 | UnwindData |  |
| 5 | `AuthBrokerSetThreadClientContext` | `0x11720` | 316 | UnwindData |  |
| 9 | `DllInstall` | `0x11870` | 93 | UnwindData |  |
| 11 | `PurgeAuthHostSsoCache` | `0x118E0` | 340 | UnwindData |  |
