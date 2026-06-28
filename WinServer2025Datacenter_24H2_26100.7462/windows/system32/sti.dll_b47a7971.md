# Binary Specification: sti.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sti.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b47a79717367036582baf60a974e29ca13b29b932a0660be0c41ac61871badac`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `DllGetClassObject` | `0x2E50` | 320 | UnwindData |  |
| 15 | `DllRegisterServer` | `0x68A0` | 71 | UnwindData |  |
| 16 | `DllUnregisterServer` | `0x68F0` | 71 | UnwindData |  |
| 13 | `DllCanUnloadNow` | `0x6AD0` | 42 | UnwindData |  |
| 18 | `MigrateRegisteredSTIAppsForWIAEvents` | `0x6B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `SelectDeviceDialog2` | `0x6B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `StiCreateInstance` | `0x6B20` | 15 | UnwindData |  |
| 21 | `StiCreateInstanceW` | `0x6B20` | 15 | UnwindData |  |
| 17 | `GetProxyDllInfo` | `0x74B0` | 32,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0BUFFER@@QEAA@I@Z` | `0xF3D0` | 36 | UnwindData |  |
| 2 | `??0BUFFER_CHAIN@@QEAA@XZ` | `0xF400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0BUFFER_CHAIN_ITEM@@QEAA@I@Z` | `0xF420` | 33 | UnwindData |  |
| 4 | `??1BUFFER@@QEAA@XZ` | `0xF450` | 30 | UnwindData |  |
| 5 | `??1BUFFER_CHAIN@@QEAA@XZ` | `0xF480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??1BUFFER_CHAIN_ITEM@@QEAA@XZ` | `0xF490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??_FBUFFER@@QEAAXXZ` | `0xF4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??_FBUFFER_CHAIN_ITEM@@QEAAXXZ` | `0xF4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?QueryPtr@BUFFER@@QEBAPEAXXZ` | `0xF4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `?QuerySize@BUFFER@@QEBAIXZ` | `0xF4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `?QueryUsed@BUFFER_CHAIN_ITEM@@QEBAKXZ` | `0xF500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?SetUsed@BUFFER_CHAIN_ITEM@@QEAAXK@Z` | `0xF510` | 104,716 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
