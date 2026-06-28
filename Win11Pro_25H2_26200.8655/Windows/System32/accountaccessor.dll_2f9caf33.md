# Binary Specification: accountaccessor.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\accountaccessor.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2f9caf33f2388f48e898cafc302f1cd4a1a0fe1671084024789e9c115f591305`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `CreateDefaultWindowsLiveAccount` | `0x7D70` | 3,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllCanUnloadNow` | `0x8C00` | 42 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x8C30` | 302 | UnwindData |  |
| 1 | `GetConversationSyncEnabled` | `0xAB80` | 394 | UnwindData |  |
| 2 | `GetUnifiedInboxEnabled` | `0xADE0` | 245 | UnwindData |  |
| 3 | `GetUnifiedInboxServerValue` | `0xAEE0` | 245 | UnwindData |  |
| 4 | `SetConversationSyncEnabled` | `0xB4D0` | 243 | UnwindData |  |
| 5 | `SetUnifiedInboxEnabled` | `0xB5D0` | 243 | UnwindData |  |
| 10 | `GetConversationSyncDateFilter` | `0x12660` | 423 | UnwindData |  |
| 11 | `IsExtendedConversationSyncDateFiltersSupported` | `0x12810` | 293 | UnwindData |  |
| 13 | `SetConversationSyncDateFilter` | `0x12940` | 447 | UnwindData |  |
| 9 | `FindMatchingPartnership` | `0x13E40` | 1,590 | UnwindData |  |
| 12 | `LoadGoldenPartnershipAccessor` | `0x14590` | 435 | UnwindData |  |
| 14 | `UnenrollAndMarkAccountForDeletion` | `0x14750` | 114 | UnwindData |  |
| 15 | `UpdateGoogleAccountConversationFlags` | `0x150E0` | 106 | UnwindData |  |
| 16 | `UpdateGoogleAccountServerSendsMeetingProp` | `0x15580` | 115 | UnwindData |  |
| 17 | `UpdateWebDavAccountProperties` | `0x15600` | 2,624 | UnwindData |  |
