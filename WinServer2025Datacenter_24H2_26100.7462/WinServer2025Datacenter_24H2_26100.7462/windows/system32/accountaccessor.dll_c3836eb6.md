# Binary Specification: accountaccessor.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\accountaccessor.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c3836eb6952497da4734914c30cc3325eed85705717e92d8800e43be5874513d`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `CreateDefaultWindowsLiveAccount` | `0x7D60` | 3,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllCanUnloadNow` | `0x8BF0` | 42 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x8C20` | 302 | UnwindData |  |
| 1 | `GetConversationSyncEnabled` | `0xAB70` | 394 | UnwindData |  |
| 2 | `GetUnifiedInboxEnabled` | `0xADD0` | 245 | UnwindData |  |
| 3 | `GetUnifiedInboxServerValue` | `0xAED0` | 245 | UnwindData |  |
| 4 | `SetConversationSyncEnabled` | `0xB4C0` | 243 | UnwindData |  |
| 5 | `SetUnifiedInboxEnabled` | `0xB5C0` | 243 | UnwindData |  |
| 10 | `GetConversationSyncDateFilter` | `0x12650` | 423 | UnwindData |  |
| 11 | `IsExtendedConversationSyncDateFiltersSupported` | `0x12800` | 293 | UnwindData |  |
| 13 | `SetConversationSyncDateFilter` | `0x12930` | 447 | UnwindData |  |
| 9 | `FindMatchingPartnership` | `0x13E30` | 1,590 | UnwindData |  |
| 12 | `LoadGoldenPartnershipAccessor` | `0x14580` | 435 | UnwindData |  |
| 14 | `UnenrollAndMarkAccountForDeletion` | `0x14740` | 114 | UnwindData |  |
| 15 | `UpdateGoogleAccountConversationFlags` | `0x150D0` | 106 | UnwindData |  |
| 16 | `UpdateGoogleAccountServerSendsMeetingProp` | `0x15570` | 115 | UnwindData |  |
| 17 | `UpdateWebDavAccountProperties` | `0x155F0` | 2,624 | UnwindData |  |
