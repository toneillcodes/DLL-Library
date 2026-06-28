# Binary Specification: sti.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sti.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `63a3a76cbac55294a8dd7442f73018b7e8b6a8d76729e1d65d6fdce95d2d2ea7`
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
| 17 | `GetProxyDllInfo` | `0x74B0` | 32,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0BUFFER@@QEAA@I@Z` | `0xF400` | 36 | UnwindData |  |
| 2 | `??0BUFFER_CHAIN@@QEAA@XZ` | `0xF430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0BUFFER_CHAIN_ITEM@@QEAA@I@Z` | `0xF450` | 33 | UnwindData |  |
| 4 | `??1BUFFER@@QEAA@XZ` | `0xF480` | 30 | UnwindData |  |
| 5 | `??1BUFFER_CHAIN@@QEAA@XZ` | `0xF4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??1BUFFER_CHAIN_ITEM@@QEAA@XZ` | `0xF4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??_FBUFFER@@QEAAXXZ` | `0xF4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??_FBUFFER_CHAIN_ITEM@@QEAAXXZ` | `0xF4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?QueryPtr@BUFFER@@QEBAPEAXXZ` | `0xF510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `?QuerySize@BUFFER@@QEBAIXZ` | `0xF520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `?QueryUsed@BUFFER_CHAIN_ITEM@@QEBAKXZ` | `0xF530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?SetUsed@BUFFER_CHAIN_ITEM@@QEAAXK@Z` | `0xF540` | 104,716 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
