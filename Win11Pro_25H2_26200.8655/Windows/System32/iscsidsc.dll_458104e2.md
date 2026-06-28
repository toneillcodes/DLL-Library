# Binary Specification: iscsidsc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\iscsidsc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `458104e223fb734806041be725c42df2e6f9d5a54a2bbcd0b8a13bb650029355`
* **Total Exported Functions:** 80

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `DllMain` | `0x1A40` | 249 | UnwindData |  |
| 26 | `GetIScsiVersionInformation` | `0x1B40` | 135 | UnwindData |  |
| 5 | `AddIScsiSendTargetPortalA` | `0x1C10` | 217 | UnwindData |  |
| 6 | `AddIScsiSendTargetPortalW` | `0x1CF0` | 86 | UnwindData |  |
| 32 | `RefreshIScsiSendTargetPortalA` | `0x21D0` | 180 | UnwindData |  |
| 33 | `RefreshIScsiSendTargetPortalW` | `0x2290` | 65 | UnwindData |  |
| 39 | `RemoveIScsiSendTargetPortalA` | `0x22E0` | 180 | UnwindData |  |
| 40 | `RemoveIScsiSendTargetPortalW` | `0x23A0` | 63 | UnwindData |  |
| 55 | `ReportIScsiSendTargetPortalsA` | `0x23F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `ReportIScsiSendTargetPortalsExA` | `0x2420` | 149 | UnwindData |  |
| 57 | `ReportIScsiSendTargetPortalsExW` | `0x24C0` | 149 | UnwindData |  |
| 58 | `ReportIScsiSendTargetPortalsW` | `0x2560` | 5,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `GetDevicesForIScsiSessionA` | `0x3A80` | 130 | UnwindData |  |
| 16 | `GetDevicesForIScsiSessionW` | `0x3B10` | 172 | UnwindData |  |
| 21 | `GetIScsiSessionListA` | `0x3BD0` | 113 | UnwindData |  |
| 22 | `GetIScsiSessionListEx` | `0x3C50` | 100 | UnwindData |  |
| 23 | `GetIScsiSessionListW` | `0x3CC0` | 113 | UnwindData |  |
| 9 | `AddPersistentIScsiDeviceA` | `0x3D40` | 102 | UnwindData |  |
| 10 | `AddPersistentIScsiDeviceW` | `0x3DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `ClearPersistentIScsiDevices` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `RemovePersistentIScsiDeviceA` | `0x3DE0` | 102 | UnwindData |  |
| 44 | `RemovePersistentIScsiDeviceW` | `0x3E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `ReportPersistentIScsiDevicesA` | `0x3E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `ReportPersistentIScsiDevicesW` | `0x3E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `SetupPersistentIScsiDevices` | `0x3EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `SetupPersistentIScsiVolumes` | `0x3EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `AddIScsiConnectionA` | `0x3EC0` | 212 | UnwindData |  |
| 4 | `AddIScsiConnectionW` | `0x3FA0` | 90 | UnwindData |  |
| 27 | `LoginIScsiTargetA` | `0x4000` | 481 | UnwindData |  |
| 28 | `LoginIScsiTargetW` | `0x41F0` | 382 | UnwindData |  |
| 29 | `LogoutIScsiTarget` | `0x4380` | 57 | UnwindData |  |
| 36 | `RemoveIScsiConnection` | `0x43C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `RemoveIScsiPersistentTargetA` | `0x43D0` | 261 | UnwindData |  |
| 38 | `RemoveIScsiPersistentTargetW` | `0x44E0` | 260 | UnwindData |  |
| 53 | `ReportIScsiPersistentLoginsA` | `0x45F0` | 44 | UnwindData |  |
| 54 | `ReportIScsiPersistentLoginsW` | `0x4630` | 44 | UnwindData |  |
| 7 | `AddIScsiStaticTargetA` | `0x4670` | 331 | UnwindData |  |
| 8 | `AddIScsiStaticTargetW` | `0x47D0` | 328 | UnwindData |  |
| 24 | `GetIScsiTargetInformationA` | `0x59A0` | 256 | UnwindData |  |
| 25 | `GetIScsiTargetInformationW` | `0x5AB0` | 226 | UnwindData |  |
| 41 | `RemoveIScsiStaticTargetA` | `0x5BA0` | 76 | UnwindData |  |
| 42 | `RemoveIScsiStaticTargetW` | `0x5C00` | 147 | UnwindData |  |
| 47 | `ReportActiveIScsiTargetMappingsA` | `0x5CA0` | 84 | UnwindData |  |
| 48 | `ReportActiveIScsiTargetMappingsW` | `0x5D00` | 84 | UnwindData |  |
| 59 | `ReportIScsiTargetPortalsA` | `0x5D60` | 270 | UnwindData |  |
| 60 | `ReportIScsiTargetPortalsW` | `0x5E80` | 282 | UnwindData |  |
| 61 | `ReportIScsiTargetsA` | `0x5FA0` | 41 | UnwindData |  |
| 62 | `ReportIScsiTargetsW` | `0x5FD0` | 41 | UnwindData |  |
| 67 | `SendScsiInquiry` | `0x6000` | 820 | UnwindData |  |
| 68 | `SendScsiReadCapacity` | `0x6340` | 758 | UnwindData |  |
| 69 | `SendScsiReportLuns` | `0x6640` | 588 | UnwindData |  |
| 1 | `AddISNSServerA` | `0x68A0` | 117 | UnwindData |  |
| 2 | `AddISNSServerW` | `0x6920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `RefreshISNSServerA` | `0x6950` | 84 | UnwindData |  |
| 31 | `RefreshISNSServerW` | `0x69B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `RemoveISNSServerA` | `0x69D0` | 84 | UnwindData |  |
| 35 | `RemoveISNSServerW` | `0x6A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `ReportISNSServerListA` | `0x6A50` | 479 | UnwindData |  |
| 50 | `ReportISNSServerListW` | `0x6C40` | 278 | UnwindData |  |
| 19 | `GetIScsiInitiatorNodeNameA` | `0x6D60` | 147 | UnwindData |  |
| 20 | `GetIScsiInitiatorNodeNameW` | `0x6E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `ReportIScsiInitiatorListA` | `0x6E10` | 72 | UnwindData |  |
| 52 | `ReportIScsiInitiatorListW` | `0x6E60` | 76 | UnwindData |  |
| 74 | `SetIScsiInitiatorNodeNameA` | `0x6EC0` | 76 | UnwindData |  |
| 75 | `SetIScsiInitiatorNodeNameW` | `0x6F20` | 112 | UnwindData |  |
| 11 | `AddRadiusServerA` | `0x6FA0` | 117 | UnwindData |  |
| 12 | `AddRadiusServerW` | `0x7020` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `GetIScsiIKEInfoA` | `0x7050` | 119 | UnwindData |  |
| 18 | `GetIScsiIKEInfoW` | `0x70D0` | 107 | UnwindData |  |
| 45 | `RemoveRadiusServerA` | `0x7150` | 84 | UnwindData |  |
| 46 | `RemoveRadiusServerW` | `0x71B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `ReportRadiusServerListA` | `0x71D0` | 479 | UnwindData |  |
| 66 | `ReportRadiusServerListW` | `0x73C0` | 278 | UnwindData |  |
| 70 | `SetIScsiGroupPresharedKey` | `0x74E0` | 74 | UnwindData |  |
| 71 | `SetIScsiIKEInfoA` | `0x7530` | 138 | UnwindData |  |
| 72 | `SetIScsiIKEInfoW` | `0x75C0` | 99 | UnwindData |  |
| 73 | `SetIScsiInitiatorCHAPSharedSecret` | `0x7630` | 58 | UnwindData |  |
| 76 | `SetIScsiInitiatorRADIUSSharedSecret` | `0x7670` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `SetIScsiTunnelModeOuterAddressA` | `0x76A0` | 259 | UnwindData |  |
| 78 | `SetIScsiTunnelModeOuterAddressW` | `0x77B0` | 23,072 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
