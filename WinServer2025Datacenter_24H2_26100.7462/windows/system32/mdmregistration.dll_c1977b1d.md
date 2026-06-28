# Binary Specification: mdmregistration.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mdmregistration.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c1977b1d810fee56ad53b398147dd5cf46725a2c3ca56f539732659c962d46a3`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DiscoverManagementService` | `0xD7E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DiscoverManagementServiceEx` | `0xD7F0` | 1,399 | UnwindData |  |
| 5 | `GetDeviceManagementConfigInfo` | `0xDE10` | 283 | UnwindData |  |
| 6 | `GetDeviceRegistrationInfo` | `0xDF40` | 1,053 | UnwindData |  |
| 7 | `GetManagementAppHyperlink` | `0xE370` | 902 | UnwindData |  |
| 8 | `IsDeviceRegisteredWithManagement` | `0xE700` | 422 | UnwindData |  |
| 9 | `IsManagementRegistrationAllowed` | `0xE8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `IsMdmUxWithoutAadAllowed` | `0xE8C0` | 21,712 | UnwindData |  |
| 11 | `RegisterDeviceWithManagement` | `0x14030` | 1,281 | UnwindData |  |
| 12 | `RegisterDeviceWithManagementUsingAADCredentials` | `0x14540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `RegisterDeviceWithManagementUsingAADDeviceCredentials` | `0x14560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `RegisterDeviceWithManagementUsingAADDeviceCredentials2` | `0x14580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `SetDeviceManagementConfigInfo` | `0x145A0` | 432 | UnwindData |  |
| 16 | `SetManagedExternally` | `0x14760` | 145 | UnwindData |  |
| 17 | `UnregisterDeviceWithManagement` | `0x14800` | 1,017 | UnwindData |  |
| 2 | `FindDiscoveryService` | `0x15A00` | 259,529 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
