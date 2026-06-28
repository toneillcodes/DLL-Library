# Binary Specification: iassvcs.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\iassvcs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3eb873fd9d35adfb12c8f7fed4387bffcff01694047e97fb00300b1d23933645`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `IASAdler32` | `0x2210` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `IASAllocateUniqueID` | `0x2270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `IASGetDictionary` | `0x2290` | 370 | UnwindData |  |
| 8 | `IASGetHostByName` | `0x2410` | 703 | UnwindData |  |
| 9 | `IASGetLocalDictionary` | `0x26E0` | 276 | UnwindData |  |
| 10 | `IASGetProductLimits` | `0x2800` | 42,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `IASGlobalLock` | `0xCEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `IASGlobalUnlock` | `0xCEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `IASInitialize` | `0xCEE0` | 374 | UnwindData |  |
| 14 | `IASRadiusCrypt` | `0xD180` | 479 | UnwindData |  |
| 15 | `IASRegisterComponent` | `0xD370` | 1,446 | UnwindData |  |
| 16 | `IASReportEvent` | `0xD920` | 85 | UnwindData |  |
| 17 | `IASReportLicenseViolation` | `0xD980` | 34 | UnwindData |  |
| 18 | `IASReportSecurityEvent` | `0xD9B0` | 72 | UnwindData |  |
| 19 | `IASRequestThread` | `0xDA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `IASSetMaxNumberOfThreads` | `0xDA10` | 124 | UnwindData |  |
| 21 | `IASSetMaxThreadIdle` | `0xDAA0` | 124 | UnwindData |  |
| 22 | `IASShutdown` | `0xDB30` | 79 | UnwindData |  |
| 23 | `IASUninitialize` | `0xDB90` | 264 | UnwindData |  |
| 24 | `IASVariantChangeType` | `0xDCA0` | 847 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x100F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x10110` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x102C0` | 618 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x10530` | 70 | UnwindData |  |
