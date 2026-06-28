# Binary Specification: rastapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rastapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `649475331b7a32c47f5ffbc4067e13a68c4c7239d1f24cbf649e6130b6d15d60`
* **Total Exported Functions:** 45

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `InitializeDriverIoControl` | `0xDD80` | 591 | UnwindData |  |
| 1 | `AddPorts` | `0x110B0` | 297 | UnwindData |  |
| 2 | `CheckRasmanDependency` | `0x111E0` | 29 | UnwindData |  |
| 3 | `DeviceConnect` | `0x11210` | 1,660 | UnwindData |  |
| 4 | `DeviceDone` | `0x118A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DeviceEnum` | `0x118B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DeviceGetDevConfig` | `0x118D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DeviceGetDevConfigEx` | `0x118E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DeviceGetInfo` | `0x11900` | 90 | UnwindData |  |
| 9 | `DeviceListen` | `0x11960` | 584 | UnwindData |  |
| 10 | `DeviceSetDevConfig` | `0x11BB0` | 220 | UnwindData |  |
| 11 | `DeviceSetInfo` | `0x11CA0` | 97 | UnwindData |  |
| 12 | `DeviceWork` | `0x11D10` | 1,138 | UnwindData |  |
| 13 | `EnableDeviceForDialIn` | `0x12800` | 378 | UnwindData |  |
| 14 | `GetConnectInfo` | `0x13550` | 691 | UnwindData |  |
| 15 | `GetZeroDeviceInfo` | `0x14800` | 227 | UnwindData |  |
| 17 | `PortChangeCallback` | `0x14EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `PortClearStatistics` | `0x14EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `PortCompressionSetInfo` | `0x14EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `PortGetPortState` | `0x14EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `PortGetStatistics` | `0x14EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `PortInit` | `0x14EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `PortSetFraming` | `0x14EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `PortClose` | `0x14EC0` | 398 | UnwindData |  |
| 21 | `PortConnect` | `0x15060` | 1,340 | UnwindData |  |
| 22 | `PortDisconnect` | `0x155B0` | 299 | UnwindData |  |
| 23 | `PortEnum` | `0x156F0` | 648 | UnwindData |  |
| 24 | `PortGetIOHandle` | `0x15980` | 137 | UnwindData |  |
| 25 | `PortGetInfo` | `0x15A10` | 161 | UnwindData |  |
| 29 | `PortOpen` | `0x15AC0` | 20 | UnwindData |  |
| 30 | `PortOpenExternal` | `0x15AE0` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `PortReceive` | `0x16020` | 338 | UnwindData |  |
| 32 | `PortReceiveComplete` | `0x16180` | 254 | UnwindData |  |
| 33 | `PortSend` | `0x16290` | 462 | UnwindData |  |
| 35 | `PortSetInfo` | `0x16470` | 102 | UnwindData |  |
| 36 | `PortSetIoCompletionPort` | `0x164E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `PortTestSignalState` | `0x16500` | 294 | UnwindData |  |
| 38 | `RasTapiIsPulseDial` | `0x16630` | 396 | UnwindData |  |
| 39 | `RastapiGetCalledID` | `0x167D0` | 184 | UnwindData |  |
| 40 | `RastapiSetCalledID` | `0x16890` | 266 | UnwindData |  |
| 41 | `RefreshDevices` | `0x169A0` | 218 | UnwindData |  |
| 42 | `RemovePort` | `0x16A80` | 338 | UnwindData |  |
| 43 | `SetCommSettings` | `0x16BE0` | 320 | UnwindData |  |
| 44 | `UnloadRastapiDll` | `0x17430` | 474 | UnwindData |  |
| 45 | `UpdateTapiService` | `0x17780` | 444 | UnwindData |  |
