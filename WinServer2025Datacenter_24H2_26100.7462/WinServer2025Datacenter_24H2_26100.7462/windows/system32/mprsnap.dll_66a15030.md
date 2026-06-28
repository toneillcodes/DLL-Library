# Binary Specification: mprsnap.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mprsnap.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `66a150304e7cc4945f58e04f840527751326ef0da9711e8c511bd44115b56f49`
* **Total Exported Functions:** 52

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `CreateInterfaceInfoAggregation` | `0x8E50` | 170 | UnwindData |  |
| 13 | `CreateRouterInfoAggregation` | `0x8F00` | 181 | UnwindData |  |
| 14 | `CreateRtrMgrInfoAggregation` | `0x8FC0` | 170 | UnwindData |  |
| 16 | `CreateRtrMgrInterfaceInfoAggregation` | `0x9070` | 170 | UnwindData |  |
| 18 | `CreateRtrMgrProtocolInfoAggregation` | `0x9120` | 170 | UnwindData |  |
| 20 | `CreateRtrMgrProtocolInterfaceInfoAggregation` | `0x91D0` | 170 | UnwindData |  |
| 3 | `CheckedGetBlock` | `0x36800` | 89 | UnwindData |  |
| 4 | `CheckedGetData` | `0x36860` | 89 | UnwindData |  |
| 10 | `CreateInterfaceInfo` | `0x368C0` | 131 | UnwindData |  |
| 12 | `CreateRouterInfo` | `0x36950` | 127 | UnwindData |  |
| 15 | `CreateRtrMgrInterfaceInfo` | `0x369E0` | 142 | UnwindData |  |
| 17 | `CreateRtrMgrProtocolInfo` | `0x36A80` | 149 | UnwindData |  |
| 19 | `CreateRtrMgrProtocolInterfaceInfo` | `0x36B20` | 148 | UnwindData |  |
| 34 | `LoadInfoBase` | `0x36BC0` | 482 | UnwindData |  |
| 35 | `LookupRtrMgr` | `0x38C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `LookupRtrMgrInterface` | `0x38C50` | 120 | UnwindData |  |
| 37 | `LookupRtrMgrProtocol` | `0x38CD0` | 113 | UnwindData |  |
| 38 | `LookupRtrMgrProtocolInterface` | `0x38D50` | 121 | UnwindData |  |
| 7 | `ConnectRegistry` | `0x5AB70` | 87 | UnwindData |  |
| 21 | `DisconnectRegistry` | `0x5ABD0` | 31 | UnwindData |  |
| 28 | `GetNTVersion` | `0x5AC00` | 766 | UnwindData |  |
| 32 | `IsNT4Machine` | `0x5AF10` | 61 | UnwindData |  |
| 42 | `QueryRouterType` | `0x5AF60` | 376 | UnwindData |  |
| 43 | `QueryRouterVersionInfo` | `0x5B0E0` | 952 | UnwindData |  |
| 1 | `SetupWithCYS` | `0x6ACB0` | 921 | UnwindData |  |
| 22 | `DllCanUnloadNow` | `0x791A0` | 94 | UnwindData |  |
| 23 | `DllGetClassObject` | `0x79210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `DllRegisterServer` | `0x79240` | 627 | UnwindData |  |
| 25 | `DllUnregisterServer` | `0x794C0` | 321 | UnwindData |  |
| 2 | `AddIpPerInterfaceBlocks` | `0x7D810` | 199 | UnwindData |  |
| 5 | `ConnectInterface` | `0x7DA10` | 226 | UnwindData |  |
| 6 | `ConnectInterfaceEx` | `0x7DB00` | 205 | UnwindData |  |
| 8 | `ConnectRouter` | `0x7DBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `ErasePSK` | `0x7DC00` | 198 | UnwindData |  |
| 27 | `ForceGlobalRefresh` | `0x7DCD0` | 279 | UnwindData |  |
| 29 | `GetRouterServiceStartType` | `0x7DDF0` | 108 | UnwindData |  |
| 30 | `GetRouterServiceStatus` | `0x7DE70` | 135 | UnwindData |  |
| 31 | `GetRouterUpTime` | `0x7DF00` | 134 | UnwindData |  |
| 33 | `IsRouterServiceRunning` | `0x7DF90` | 42 | UnwindData |  |
| 40 | `PauseRouterService` | `0x7E1C0` | 238 | UnwindData |  |
| 41 | `PromptForCredentials` | `0x7E2C0` | 839 | UnwindData |  |
| 44 | `ResumeRouterService` | `0x7E610` | 182 | UnwindData |  |
| 45 | `SetRouterServiceStartType` | `0x7E6D0` | 81 | UnwindData |  |
| 46 | `StartRAMgmtService` | `0x7E730` | 217 | UnwindData |  |
| 47 | `StartRouterService` | `0x7E810` | 595 | UnwindData |  |
| 48 | `StopRAMgmtService` | `0x7EA70` | 172 | UnwindData |  |
| 49 | `StopRouterService` | `0x7EB30` | 192 | UnwindData |  |
| 50 | `UpdateDDM` | `0x7EC00` | 539 | UnwindData |  |
| 51 | `UpdateRoutes` | `0x7EE30` | 239 | UnwindData |  |
| 52 | `UpdateRoutesEx` | `0x7EF30` | 184 | UnwindData |  |
| 39 | `MprConfigServerUnattendedInstall` | `0x81710` | 112 | UnwindData |  |
| 9 | `CreateInfoBase` | `0x82980` | 108 | UnwindData |  |
