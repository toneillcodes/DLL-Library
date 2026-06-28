# Binary Specification: WinFax.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WinFax.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `624ddeed66ee701e770f81987fd1bf77fb2402916618205fc0bad52fe83dbff9`
* **Total Exported Functions:** 56

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 37 | `FaxRegisterServiceProviderW` | `0x2370` | 1,474 | UnwindData |  |
| 56 | `FaxUnregisterServiceProviderW` | `0x2940` | 428 | UnwindData |  |
| 1 | `FaxAbort` | `0x2C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `FaxAccessCheck` | `0x2C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `FaxClose` | `0x2C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FaxCompleteJobParamsA` | `0x2CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `FaxCompleteJobParamsW` | `0x2CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `FaxConnectFaxServerA` | `0x2CE0` | 371 | UnwindData |  |
| 7 | `FaxConnectFaxServerW` | `0x2E60` | 134 | UnwindData |  |
| 8 | `FaxEnableRoutingMethodA` | `0x2EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `FaxEnableRoutingMethodW` | `0x2F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `FaxEnumGlobalRoutingInfoA` | `0x2F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `FaxEnumGlobalRoutingInfoW` | `0x2F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `FaxEnumJobsA` | `0x2F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `FaxEnumJobsW` | `0x2F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `FaxEnumPortsA` | `0x2FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `FaxEnumPortsW` | `0x2FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `FaxEnumRoutingMethodsA` | `0x2FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `FaxEnumRoutingMethodsW` | `0x3010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `FaxFreeBuffer` | `0x3030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `FaxGetConfigurationA` | `0x3050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `FaxGetConfigurationW` | `0x3070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `FaxGetDeviceStatusA` | `0x3090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `FaxGetDeviceStatusW` | `0x30B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `FaxGetJobA` | `0x30D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `FaxGetJobW` | `0x30F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `FaxGetLoggingCategoriesA` | `0x3110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `FaxGetLoggingCategoriesW` | `0x3130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `FaxGetPageData` | `0x3150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `FaxGetPortA` | `0x3170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `FaxGetPortW` | `0x3190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `FaxGetRoutingInfoA` | `0x31B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `FaxGetRoutingInfoW` | `0x31D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `FaxInitializeEventQueue` | `0x31F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `FaxOpenPort` | `0x3210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `FaxPrintCoverPageA` | `0x3230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `FaxPrintCoverPageW` | `0x3250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `FaxRegisterRoutingExtensionW` | `0x3270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `FaxSendDocumentA` | `0x3290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `FaxSendDocumentForBroadcastA` | `0x32B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `FaxSendDocumentForBroadcastW` | `0x32D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `FaxSendDocumentW` | `0x32F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `FaxSetConfigurationA` | `0x3310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `FaxSetConfigurationW` | `0x3330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `FaxSetGlobalRoutingInfoA` | `0x3350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `FaxSetGlobalRoutingInfoW` | `0x3370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `FaxSetJobA` | `0x3390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `FaxSetJobW` | `0x33B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `FaxSetLoggingCategoriesA` | `0x33D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `FaxSetLoggingCategoriesW` | `0x33F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `FaxSetPortA` | `0x3410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `FaxSetPortW` | `0x3430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `FaxSetRoutingInfoA` | `0x3450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `FaxSetRoutingInfoW` | `0x3470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `FaxStartPrintJobA` | `0x3490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `FaxStartPrintJobW` | `0x34B0` | 31,164 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
