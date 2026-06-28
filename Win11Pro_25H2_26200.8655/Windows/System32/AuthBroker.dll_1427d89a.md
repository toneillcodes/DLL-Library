# Binary Specification: AuthBroker.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\AuthBroker.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1427d89a42bfa59d5e2d127b13ee09674ac9f0f47da09deb4f491ae7f1cb9946`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllCanUnloadNow` | `0x3D60` | 102 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x3DD0` | 165 | UnwindData |  |
| 7 | `DllGetActivationFactory` | `0x4510` | 146 | UnwindData |  |
| 4 | `AuthBrokerFreeClientContext` | `0x5A90` | 198 | UnwindData |  |
| 10 | `DllRegisterServer` | `0xA940` | 13,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `FindCallingThreadImmersiveWindow` | `0xDE40` | 720 | UnwindData |  |
| 2 | `AuthBrokerClearThreadClientContext` | `0x114F0` | 236 | UnwindData |  |
| 3 | `AuthBrokerCreateClientContext` | `0x115F0` | 322 | UnwindData |  |
| 5 | `AuthBrokerSetThreadClientContext` | `0x11740` | 316 | UnwindData |  |
| 9 | `DllInstall` | `0x11890` | 93 | UnwindData |  |
| 11 | `PurgeAuthHostSsoCache` | `0x11900` | 340 | UnwindData |  |
