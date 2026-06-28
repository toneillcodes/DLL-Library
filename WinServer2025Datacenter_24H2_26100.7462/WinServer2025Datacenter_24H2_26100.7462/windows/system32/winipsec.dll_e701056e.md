# Binary Specification: winipsec.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\winipsec.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e701056ec2745d18280a0bd04a54b023d4a754710a619f0372831ca37bd916be`
* **Total Exported Functions:** 73

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 20 | `DllMain` | `0x1A10` | 288 | UnwindData |  |
| 47 | `AddMMAuthMethods` | `0x1D00` | 519 | UnwindData |  |
| 38 | `AddMMFilter` | `0x1F10` | 607 | UnwindData |  |
| 85 | `AddMMFilterEx` | `0x2180` | 609 | UnwindData |  |
| 33 | `AddMMPolicy` | `0x23F0` | 551 | UnwindData |  |
| 28 | `AddQMPolicy` | `0x2620` | 551 | UnwindData |  |
| 76 | `AddSAs` | `0x2850` | 34 | UnwindData |  |
| 54 | `CloseIKENegotiationHandle` | `0x2850` | 34 | UnwindData |  |
| 60 | `CloseIKENotifyHandle` | `0x2850` | 34 | UnwindData |  |
| 59 | `QueryIKENotifyData` | `0x2850` | 34 | UnwindData |  |
| 58 | `RegisterIKENotifyClient` | `0x2850` | 34 | UnwindData |  |
| 23 | `AddTransportFilter` | `0x2880` | 605 | UnwindData |  |
| 91 | `AddTransportFilterEx` | `0x2AF0` | 609 | UnwindData |  |
| 63 | `AddTunnelFilter` | `0x2D60` | 609 | UnwindData |  |
| 70 | `CloseMMFilterHandle` | `0x2FD0` | 226 | UnwindData |  |
| 72 | `CloseTransportFilterHandle` | `0x30C0` | 226 | UnwindData |  |
| 74 | `CloseTunnelFilterHandle` | `0x31B0` | 226 | UnwindData |  |
| 48 | `DeleteMMAuthMethods` | `0x32A0` | 444 | UnwindData |  |
| 39 | `DeleteMMFilter` | `0x3470` | 226 | UnwindData |  |
| 34 | `DeleteMMPolicy` | `0x3560` | 477 | UnwindData |  |
| 57 | `DeleteMMSAs` | `0x3750` | 647 | UnwindData |  |
| 29 | `DeleteQMPolicy` | `0x39E0` | 477 | UnwindData |  |
| 77 | `DeleteQMSAs` | `0x3BD0` | 583 | UnwindData |  |
| 24 | `DeleteTransportFilter` | `0x3E20` | 226 | UnwindData |  |
| 64 | `DeleteTunnelFilter` | `0x3F10` | 226 | UnwindData |  |
| 75 | `EnumIPSecInterfaces` | `0x4000` | 664 | UnwindData |  |
| 49 | `EnumMMAuthMethods` | `0x42A0` | 622 | UnwindData |  |
| 40 | `EnumMMFilters` | `0x4520` | 718 | UnwindData |  |
| 86 | `EnumMMFiltersEx` | `0x4800` | 720 | UnwindData |  |
| 35 | `EnumMMPolicies` | `0x4AE0` | 622 | UnwindData |  |
| 55 | `EnumMMSAs` | `0x4D60` | 855 | UnwindData |  |
| 30 | `EnumQMPolicies` | `0x50C0` | 622 | UnwindData |  |
| 62 | `EnumQMSAs` | `0x5340` | 630 | UnwindData |  |
| 25 | `EnumTransportFilters` | `0x55C0` | 718 | UnwindData |  |
| 92 | `EnumTransportFiltersEx` | `0x58A0` | 720 | UnwindData |  |
| 65 | `EnumTunnelFilters` | `0x5B80` | 720 | UnwindData |  |
| 78 | `GetConfigurationVariables` | `0x5E60` | 454 | UnwindData |  |
| 51 | `GetMMAuthMethods` | `0x6030` | 533 | UnwindData |  |
| 42 | `GetMMFilter` | `0x6250` | 343 | UnwindData |  |
| 88 | `GetMMFilterEx` | `0x63B0` | 343 | UnwindData |  |
| 37 | `GetMMPolicy` | `0x6510` | 570 | UnwindData |  |
| 46 | `GetMMPolicyByID` | `0x6750` | 533 | UnwindData |  |
| 32 | `GetQMPolicy` | `0x6970` | 583 | UnwindData |  |
| 45 | `GetQMPolicyByID` | `0x6BC0` | 546 | UnwindData |  |
| 27 | `GetTransportFilter` | `0x6DF0` | 343 | UnwindData |  |
| 94 | `GetTransportFilterEx` | `0x6F50` | 343 | UnwindData |  |
| 67 | `GetTunnelFilter` | `0x70B0` | 343 | UnwindData |  |
| 52 | `InitiateIKENegotiation` | `0x7210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `QueryIKENegotiationStatus` | `0x7210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MatchMMFilter` | `0x7220` | 1,122 | UnwindData |  |
| 89 | `MatchMMFilterEx` | `0x7690` | 1,076 | UnwindData |  |
| 44 | `MatchTransportFilter` | `0x7AD0` | 803 | UnwindData |  |
| 95 | `MatchTransportFilterEx` | `0x7E00` | 1,112 | UnwindData |  |
| 68 | `MatchTunnelFilter` | `0x8260` | 805 | UnwindData |  |
| 69 | `OpenMMFilterHandle` | `0x8590` | 553 | UnwindData |  |
| 84 | `OpenMMFilterHandleEx` | `0x87C0` | 553 | UnwindData |  |
| 71 | `OpenTransportFilterHandle` | `0x89F0` | 553 | UnwindData |  |
| 90 | `OpenTransportFilterHandleEx` | `0x8C20` | 553 | UnwindData |  |
| 73 | `OpenTunnelFilterHandle` | `0x8E50` | 553 | UnwindData |  |
| 56 | `QueryIKEStatistics` | `0x9080` | 487 | UnwindData |  |
| 61 | `QueryIPSecStatistics` | `0x9270` | 481 | UnwindData |  |
| 80 | `QuerySpdPolicyState` | `0x9460` | 493 | UnwindData |  |
| 21 | `SPDApiBufferAllocate` | `0x9660` | 102 | UnwindData |  |
| 22 | `SPDApiBufferFree` | `0x9770` | 61 | UnwindData |  |
| 79 | `SetConfigurationVariables` | `0x97C0` | 504 | UnwindData |  |
| 50 | `SetMMAuthMethods` | `0x99C0` | 534 | UnwindData |  |
| 41 | `SetMMFilter` | `0x9BE0` | 423 | UnwindData |  |
| 87 | `SetMMFilterEx` | `0x9D90` | 423 | UnwindData |  |
| 36 | `SetMMPolicy` | `0x9F40` | 626 | UnwindData |  |
| 31 | `SetQMPolicy` | `0xA1C0` | 626 | UnwindData |  |
| 26 | `SetTransportFilter` | `0xA440` | 423 | UnwindData |  |
| 93 | `SetTransportFilterEx` | `0xA5F0` | 423 | UnwindData |  |
| 66 | `SetTunnelFilter` | `0xA7A0` | 423 | UnwindData |  |
