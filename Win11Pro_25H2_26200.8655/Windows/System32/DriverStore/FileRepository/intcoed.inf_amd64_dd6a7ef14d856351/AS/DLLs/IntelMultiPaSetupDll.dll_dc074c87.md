# Binary Specification: IntelMultiPaSetupDll.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\intcoed.inf_amd64_dd6a7ef14d856351\AS\DLLs\IntelMultiPaSetupDll.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dc074c87cb039680e4c8ec1222a2a6731e6fb3eb7d6ee3cf5817273e45e3b39a`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `AssistantSubscribe` | `0x2D90` | 48 | UnwindData |  |
| 4 | `AssistantUnsubscribe` | `0x2DC0` | 45 | UnwindData |  |
| 13 | `RegisterPdt` | `0x2DF0` | 45 | UnwindData |  |
| 14 | `RegisterUdt` | `0x2E20` | 66 | UnwindData |  |
| 2 | `AddSv` | `0x2E70` | 66 | UnwindData |  |
| 20 | `UnregisterPdt` | `0x2EC0` | 42 | UnwindData |  |
| 21 | `UnregisterUdt` | `0x2EF0` | 45 | UnwindData |  |
| 17 | `RemoveSv` | `0x2F20` | 48 | UnwindData |  |
| 10 | `QueryCapabilities` | `0x2F50` | 29 | UnwindData |  |
| 11 | `QueryCurrentLanguage` | `0x2F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetApiVersion` | `0x2F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetApiVersionV2` | `0x2FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `SetParameter` | `0x2FD0` | 79 | UnwindData |  |
| 9 | `GetParameter` | `0x3020` | 66 | UnwindData |  |
| 1 | `AddSid` | `0x3070` | 45 | UnwindData |  |
| 16 | `RemoveSid` | `0x30A0` | 48 | UnwindData |  |
| 19 | `StartEnrollment` | `0x30D0` | 48 | UnwindData |  |
| 6 | `FeedEnrollmentData` | `0x3100` | 82 | UnwindData |  |
| 5 | `CompleteEnrollment` | `0x3160` | 48 | UnwindData |  |
| 15 | `RemoveEnrollment` | `0x3190` | 48 | UnwindData |  |
| 12 | `QueryEnrollmentConfiguration` | `0x31C0` | 48 | UnwindData |  |
