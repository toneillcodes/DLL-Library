# Binary Specification: rastapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rastapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4de26e9e254e4edf969c0cdd8644e2014ab345071242016a48ca36879cd92ff3`
* **Total Exported Functions:** 45

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `InitializeDriverIoControl` | `0xDD80` | 591 | UnwindData |  |
| 1 | `AddPorts` | `0x110B0` | 297 | UnwindData |  |
| 2 | `CheckRasmanDependency` | `0x111E0` | 105 | UnwindData |  |
| 3 | `DeviceConnect` | `0x11250` | 1,660 | UnwindData |  |
| 4 | `DeviceDone` | `0x118E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DeviceEnum` | `0x118F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DeviceGetDevConfig` | `0x11910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DeviceGetDevConfigEx` | `0x11920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DeviceGetInfo` | `0x11940` | 90 | UnwindData |  |
| 9 | `DeviceListen` | `0x119A0` | 584 | UnwindData |  |
| 10 | `DeviceSetDevConfig` | `0x11BF0` | 220 | UnwindData |  |
| 11 | `DeviceSetInfo` | `0x11CE0` | 97 | UnwindData |  |
| 12 | `DeviceWork` | `0x11D50` | 1,138 | UnwindData |  |
| 13 | `EnableDeviceForDialIn` | `0x12840` | 378 | UnwindData |  |
| 14 | `GetConnectInfo` | `0x135C0` | 691 | UnwindData |  |
| 15 | `GetZeroDeviceInfo` | `0x14870` | 227 | UnwindData |  |
| 17 | `PortChangeCallback` | `0x14F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `PortClearStatistics` | `0x14F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `PortCompressionSetInfo` | `0x14F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `PortGetPortState` | `0x14F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `PortGetStatistics` | `0x14F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `PortInit` | `0x14F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `PortSetFraming` | `0x14F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `PortClose` | `0x14F30` | 398 | UnwindData |  |
| 21 | `PortConnect` | `0x150D0` | 1,340 | UnwindData |  |
| 22 | `PortDisconnect` | `0x15620` | 299 | UnwindData |  |
| 23 | `PortEnum` | `0x15760` | 648 | UnwindData |  |
| 24 | `PortGetIOHandle` | `0x159F0` | 137 | UnwindData |  |
| 25 | `PortGetInfo` | `0x15A80` | 161 | UnwindData |  |
| 29 | `PortOpen` | `0x15B30` | 20 | UnwindData |  |
| 30 | `PortOpenExternal` | `0x15B50` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `PortReceive` | `0x16090` | 338 | UnwindData |  |
| 32 | `PortReceiveComplete` | `0x161F0` | 254 | UnwindData |  |
| 33 | `PortSend` | `0x16300` | 462 | UnwindData |  |
| 35 | `PortSetInfo` | `0x164E0` | 102 | UnwindData |  |
| 36 | `PortSetIoCompletionPort` | `0x16550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `PortTestSignalState` | `0x16570` | 294 | UnwindData |  |
| 38 | `RasTapiIsPulseDial` | `0x166A0` | 396 | UnwindData |  |
| 39 | `RastapiGetCalledID` | `0x16840` | 184 | UnwindData |  |
| 40 | `RastapiSetCalledID` | `0x16900` | 266 | UnwindData |  |
| 41 | `RefreshDevices` | `0x16A10` | 218 | UnwindData |  |
| 42 | `RemovePort` | `0x16AF0` | 338 | UnwindData |  |
| 43 | `SetCommSettings` | `0x16C50` | 320 | UnwindData |  |
| 44 | `UnloadRastapiDll` | `0x174A0` | 474 | UnwindData |  |
| 45 | `UpdateTapiService` | `0x17810` | 444 | UnwindData |  |
