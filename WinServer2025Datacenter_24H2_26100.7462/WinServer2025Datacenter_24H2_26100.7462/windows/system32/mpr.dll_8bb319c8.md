# Binary Specification: mpr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mpr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8bb319c8c8255e915c05c03eccc24981cf9653025d2f720fb7fffdd4d524309c`
* **Total Exported Functions:** 85

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 21 | `WNetAddConnectionA` | `0x12D0` | 182 | UnwindData |  |
| 27 | `WNetClearConnections` | `0x18D0` | 323 | UnwindData |  |
| 28 | `WNetCloseEnum` | `0x1A20` | 459 | UnwindData |  |
| 37 | `WNetEnumResourceA` | `0x1C00` | 155 | UnwindData |  |
| 65 | `WNetGetUniversalNameA` | `0x1CB0` | 473 | UnwindData |  |
| 70 | `WNetOpenEnumA` | `0x2020` | 158 | UnwindData |  |
| 45 | `WNetGetConnectionA` | `0x20D0` | 211 | UnwindData |  |
| 38 | `WNetEnumResourceW` | `0x27A0` | 263 | UnwindData |  |
| 46 | `WNetGetConnectionW` | `0x3870` | 137 | UnwindData |  |
| 71 | `WNetOpenEnumW` | `0x50B0` | 695 | UnwindData |  |
| 53 | `WNetGetNetworkInformationW` | `0x5370` | 43 | UnwindData |  |
| 61 | `WNetGetResourceInformationW` | `0x5570` | 145 | UnwindData |  |
| 44 | `WNetGetConnection3W` | `0x5610` | 194 | UnwindData |  |
| 66 | `WNetGetUniversalNameW` | `0x56E0` | 1,886 | UnwindData |  |
| 40 | `WNetFormatNetworkNameW` | `0x5E50` | 340 | UnwindData |  |
| 57 | `WNetGetProviderNameW` | `0x5FB0` | 404 | UnwindData |  |
| 59 | `WNetGetProviderTypeW` | `0x7CD0` | 210 | UnwindData |  |
| 85 | `WNetUseConnectionW` | `0x8180` | 270 | UnwindData |  |
| 16 | `WNetAddConnection2W` | `0x8420` | 256 | UnwindData |  |
| 75 | `WNetRestoreAllConnectionsW` | `0x8530` | 364 | UnwindData |  |
| 5 | `ShowReconnectDialog` | `0x9680` | 62 | UnwindData |  |
| 80 | `WNetSetLastErrorW` | `0xC1E0` | 416 | UnwindData |  |
| 68 | `WNetGetUserW` | `0xCE10` | 1,177 | UnwindData |  |
| 12 | `MultinetGetConnectionPerformanceW` | `0xD7E0` | 164 | UnwindData |  |
| 24 | `WNetCancelConnection2W` | `0xDF90` | 5,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `WNetAddConnection3W` | `0xF630` | 40 | UnwindData |  |
| 20 | `WNetAddConnection4W` | `0xF660` | 66 | UnwindData |  |
| 22 | `WNetAddConnectionW` | `0xF6B0` | 198 | UnwindData |  |
| 26 | `WNetCancelConnectionW` | `0xF780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `WNetGetConnection2W` | `0xF7A0` | 327 | UnwindData |  |
| 76 | `WNetRestoreSingleConnectionW` | `0xF8F0` | 766 | UnwindData |  |
| 78 | `WNetSetConnectionW` | `0xFC00` | 676 | UnwindData |  |
| 83 | `WNetUseConnection4W` | `0xFEB0` | 180 | UnwindData |  |
| 69 | `WNetLogonNotify` | `0xFF70` | 1,198 | UnwindData |  |
| 72 | `WNetPasswordChangeNotify` | `0x10430` | 888 | UnwindData |  |
| 14 | `MultinetGetErrorTextW` | `0x107B0` | 583 | UnwindData |  |
| 51 | `WNetGetLastErrorW` | `0x10A00` | 307 | UnwindData |  |
| 11 | `MultinetGetConnectionPerformanceA` | `0x10C70` | 118 | UnwindData |  |
| 13 | `MultinetGetErrorTextA` | `0x10CF0` | 320 | UnwindData |  |
| 15 | `WNetAddConnection2A` | `0x10E40` | 47 | UnwindData |  |
| 17 | `WNetAddConnection3A` | `0x10E80` | 40 | UnwindData |  |
| 19 | `WNetAddConnection4A` | `0x10EB0` | 66 | UnwindData |  |
| 23 | `WNetCancelConnection2A` | `0x10F00` | 131 | UnwindData |  |
| 25 | `WNetCancelConnectionA` | `0x10F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `WNetConnectionDialog1A` | `0x10FB0` | 185 | UnwindData |  |
| 32 | `WNetDirectoryNotifyA` | `0x11070` | 133 | UnwindData |  |
| 35 | `WNetDisconnectDialog1A` | `0x11100` | 210 | UnwindData |  |
| 39 | `WNetFormatNetworkNameA` | `0x111E0` | 216 | UnwindData |  |
| 41 | `WNetGetConnection2A` | `0x112C0` | 361 | UnwindData |  |
| 43 | `WNetGetConnection3A` | `0x11430` | 155 | UnwindData |  |
| 47 | `WNetGetDirectoryTypeA` | `0x114E0` | 133 | UnwindData |  |
| 50 | `WNetGetLastErrorA` | `0x11570` | 106 | UnwindData |  |
| 52 | `WNetGetNetworkInformationA` | `0x115E0` | 118 | UnwindData |  |
| 54 | `WNetGetPropertyTextA` | `0x11660` | 205 | UnwindData |  |
| 56 | `WNetGetProviderNameA` | `0x11740` | 171 | UnwindData |  |
| 58 | `WNetGetProviderTypeA` | `0x11800` | 118 | UnwindData |  |
| 60 | `WNetGetResourceInformationA` | `0x11880` | 305 | UnwindData |  |
| 62 | `WNetGetResourceParentA` | `0x119C0` | 230 | UnwindData |  |
| 67 | `WNetGetUserA` | `0x11AB0` | 197 | UnwindData |  |
| 73 | `WNetPropertyDialogA` | `0x11B80` | 154 | UnwindData |  |
| 77 | `WNetSetConnectionA` | `0x11C20` | 131 | UnwindData |  |
| 79 | `WNetSetLastErrorA` | `0x11CB0` | 90 | UnwindData |  |
| 82 | `WNetUseConnection4A` | `0x11D10` | 305 | UnwindData |  |
| 84 | `WNetUseConnectionA` | `0x11E50` | 301 | UnwindData |  |
| 55 | `WNetGetPropertyTextW` | `0x11F90` | 576 | UnwindData |  |
| 74 | `WNetPropertyDialogW` | `0x121E0` | 558 | UnwindData |  |
| 10 | `I_MprSaveConn` | `0x12700` | 89 | UnwindData |  |
| 1 | `DoBroadcastSystemMessage` | `0x12760` | 69 | UnwindData |  |
| 2 | `DoCommandLinePrompt` | `0x127B0` | 121 | UnwindData |  |
| 3 | `DoPasswordDialog` | `0x12830` | 123 | UnwindData |  |
| 4 | `DoProfileErrorDialog` | `0x128C0` | 95 | UnwindData |  |
| 6 | `ShowReconnectDialogEnd` | `0x12930` | 40 | UnwindData |  |
| 7 | `ShowReconnectDialogUI` | `0x12960` | 55 | UnwindData |  |
| 8 | `WNetConnectionDialog2` | `0x129A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `WNetDisconnectDialog2` | `0x129B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `WNetConnectionDialog` | `0x129C0` | 60 | UnwindData |  |
| 31 | `WNetConnectionDialog1W` | `0x12A10` | 50 | UnwindData |  |
| 34 | `WNetDisconnectDialog` | `0x12A50` | 60 | UnwindData |  |
| 36 | `WNetDisconnectDialog1W` | `0x12AA0` | 50 | UnwindData |  |
| 64 | `WNetGetSearchDialog` | `0x12AE0` | 145 | UnwindData |  |
| 81 | `WNetSupportGlobalEnum` | `0x12B80` | 168 | UnwindData |  |
| 63 | `WNetGetResourceParentW` | `0x12C50` | 76 | UnwindData |  |
| 33 | `WNetDirectoryNotifyW` | `0x12DB0` | 533 | UnwindData |  |
| 48 | `WNetGetDirectoryTypeW` | `0x12FD0` | 658 | UnwindData |  |
| 49 | `WNetGetHomeDirectoryW` | `0x13270` | 210 | UnwindData |  |
