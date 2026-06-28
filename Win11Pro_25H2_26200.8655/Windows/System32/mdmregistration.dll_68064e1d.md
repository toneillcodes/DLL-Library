# Binary Specification: mdmregistration.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mdmregistration.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `68064e1d474087deb801d5ad7db6887ae63c8f3730749f08e66cf5fd90321e72`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DiscoverManagementService` | `0xD8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DiscoverManagementServiceEx` | `0xD8F0` | 1,399 | UnwindData |  |
| 5 | `GetDeviceManagementConfigInfo` | `0xDF10` | 283 | UnwindData |  |
| 6 | `GetDeviceRegistrationInfo` | `0xE040` | 1,053 | UnwindData |  |
| 7 | `GetManagementAppHyperlink` | `0xE470` | 902 | UnwindData |  |
| 8 | `IsDeviceRegisteredWithManagement` | `0xE800` | 422 | UnwindData |  |
| 9 | `IsManagementRegistrationAllowed` | `0xE9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `IsMdmUxWithoutAadAllowed` | `0xE9C0` | 21,712 | UnwindData |  |
| 11 | `RegisterDeviceWithManagement` | `0x14130` | 1,281 | UnwindData |  |
| 12 | `RegisterDeviceWithManagementUsingAADCredentials` | `0x14640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `RegisterDeviceWithManagementUsingAADDeviceCredentials` | `0x14660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `RegisterDeviceWithManagementUsingAADDeviceCredentials2` | `0x14680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `SetDeviceManagementConfigInfo` | `0x146A0` | 432 | UnwindData |  |
| 16 | `SetManagedExternally` | `0x14860` | 145 | UnwindData |  |
| 17 | `UnregisterDeviceWithManagement` | `0x14900` | 1,017 | UnwindData |  |
| 2 | `FindDiscoveryService` | `0x15B30` | 260,873 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
