# Binary Specification: uniplat.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\uniplat.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5485ccd4b455645581f8cad49b08f8c97ededc91cbd3766cf1b4cf4870299d3d`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 214 | `CallBeginning` | `0x1B20` | 76 | UnwindData |  |
| 215 | `CallEnding` | `0x1B80` | 79 | UnwindData |  |
| 212 | `MonitorHandle` | `0x1DB0` | 369 | UnwindData |  |
| 216 | `ResetCallCount` | `0x1F60` | 77 | UnwindData |  |
| 210 | `StartMonitorThread` | `0x1FC0` | 233 | UnwindData |  |
| 211 | `StopMonitorThread` | `0x20B0` | 212 | UnwindData |  |
| 213 | `StopMonitoringHandle` | `0x2190` | 129 | UnwindData |  |
| 113 | `AllocateOverStructEx` | `0x25B0` | 74 | UnwindData |  |
| 111 | `CreateOverStructPool` | `0x2620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `DestroyOverStructPool` | `0x2630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `FreeOverStruct` | `0x2640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `ReinitOverStruct` | `0x2660` | 44 | UnwindData |  |
| 116 | `SyncDeviceIoControl` | `0x26A0` | 305 | UnwindData |  |
| 104 | `UnimodemDeviceIoControlEx` | `0x2840` | 121 | UnwindData |  |
| 106 | `UnimodemQueueUserAPC` | `0x28C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `UnimodemReadFileEx` | `0x28F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `UnimodemWaitCommEventEx` | `0x2910` | 48 | UnwindData |  |
| 103 | `UnimodemWriteFileEx` | `0x2950` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `UmPlatformDeinitialize` | `0x2AD0` | 134 | UnwindData |  |
| 100 | `UmPlatformInitialize` | `0x2B60` | 202 | UnwindData |  |
| 117 | `WinntIsWorkstation` | `0x2CB0` | 250 | UnwindData |  |
| 110 | `CancelUnimodemTimer` | `0x2DB0` | 31 | UnwindData |  |
| 107 | `CreateUnimodemTimer` | `0x2DE0` | 126 | UnwindData |  |
| 108 | `FreeUnimodemTimer` | `0x2E70` | 54 | UnwindData |  |
| 109 | `SetUnimodemTimer` | `0x2EB0` | 82 | UnwindData |  |
| 207 | `UnimodemNotifyTSP` | `0x2F30` | 514 | UnwindData |  |
