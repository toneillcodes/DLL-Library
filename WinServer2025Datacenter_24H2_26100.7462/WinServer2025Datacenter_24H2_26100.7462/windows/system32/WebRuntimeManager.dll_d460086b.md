# Binary Specification: WebRuntimeManager.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WebRuntimeManager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d460086bca7e620f68433da3ff99322e3a4930b9b006bfab1d6f41313d044fce`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateMessagePortEventDispatcher` | `0x3FE20` | 183 | UnwindData |  |
| 2 | `CreateServiceWorkerClientMessageDispatcher` | `0x45B90` | 155 | UnwindData |  |
| 6 | `EnsureServiceWorkerManagerComponent` | `0x49E10` | 35 | UnwindData |  |
| 3 | `CreateWebRuntimeFactory` | `0x55E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateWebRuntimeNotificationFromEventArg` | `0x55E50` | 517 | UnwindData |  |
| 5 | `DllGetActivationFactory` | `0x56210` | 45 | UnwindData |  |
