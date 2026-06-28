# Binary Specification: w32time.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\w32time.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7083e141a13265aa6eda71a43bedeb7d49a47e77625827f3db5acb2fd1befbbc`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 23 | `W32TimeQueryStatus` | `0x286D0` | 835 | UnwindData |  |
| 10 | `TimeProvCommand` | `0x2C3A0` | 18,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SvchostPushServiceGlobals` | `0x30BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `W32TimeBufferFree` | `0x30C00` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `TimeProvOpen` | `0x30EC0` | 182 | UnwindData |  |
| 25 | `W32TimeSyncNow` | `0x32550` | 424 | UnwindData |  |
| 28 | `W32TmServiceMain` | `0x36690` | 3,109 | UnwindData |  |
| 9 | `TimeProvClose` | `0x48FA0` | 92 | UnwindData |  |
| 4 | `DllInstall` | `0x4AD80` | 377 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x4AF00` | 78 | UnwindData |  |
| 6 | `DllUnregisterServer` | `0x4AF60` | 24 | UnwindData |  |
| 13 | `W32TimeDcPromo` | `0x4AF80` | 791 | UnwindData |  |
| 26 | `W32TimeVerifyJoinConfig` | `0x4B2A0` | 418 | UnwindData |  |
| 27 | `W32TimeVerifyUnjoinConfig` | `0x4B450` | 335 | UnwindData |  |
| 7 | `SvchostEntry_W32Time` | `0x50430` | 15,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `W32TimeGetNetlogonServiceBits` | `0x53EF0` | 370 | UnwindData |  |
| 16 | `W32TimeLog` | `0x54070` | 363 | UnwindData |  |
| 18 | `W32TimeQueryConfiguration` | `0x541F0` | 453 | UnwindData |  |
| 19 | `W32TimeQueryHardwareProviderStatus` | `0x543C0` | 26 | UnwindData |  |
| 20 | `W32TimeQueryNTPProviderStatus` | `0x543E0` | 23 | UnwindData |  |
| 21 | `W32TimeQueryNtpProviderConfiguration` | `0x54400` | 515 | UnwindData |  |
| 22 | `W32TimeQuerySource` | `0x54610` | 453 | UnwindData |  |
| 14 | `W32TimeDeleteConfig` | `0x54AF0` | 156 | UnwindData |  |
| 17 | `W32TimeQueryConfig` | `0x54BA0` | 234 | UnwindData |  |
| 24 | `W32TimeSetConfig` | `0x54C90` | 209 | UnwindData |  |
| 1 | `fnW32TmI_ScSetServiceBits` | `0xA6B60` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `fnW32TmSetServiceStatus` | `0xA6B68` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `fnW32TmRegisterServiceCtrlHandlerEx` | `0xA6B70` | 0 | Indeterminate |  |
