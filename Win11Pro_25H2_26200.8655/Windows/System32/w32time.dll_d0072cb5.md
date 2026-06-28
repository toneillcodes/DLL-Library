# Binary Specification: w32time.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\w32time.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d0072cb50b50c5ad39382aa3c6e8a5886feb29413d94bd504d3b6d1986d75d21`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 23 | `W32TimeQueryStatus` | `0x28A50` | 835 | UnwindData |  |
| 10 | `TimeProvCommand` | `0x2C720` | 18,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SvchostPushServiceGlobals` | `0x30F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `W32TimeBufferFree` | `0x30F80` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `TimeProvOpen` | `0x31240` | 182 | UnwindData |  |
| 25 | `W32TimeSyncNow` | `0x327D0` | 424 | UnwindData |  |
| 28 | `W32TmServiceMain` | `0x36680` | 3,109 | UnwindData |  |
| 9 | `TimeProvClose` | `0x49030` | 92 | UnwindData |  |
| 4 | `DllInstall` | `0x4AE10` | 377 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x4AF90` | 78 | UnwindData |  |
| 6 | `DllUnregisterServer` | `0x4AFF0` | 24 | UnwindData |  |
| 13 | `W32TimeDcPromo` | `0x4B010` | 791 | UnwindData |  |
| 26 | `W32TimeVerifyJoinConfig` | `0x4B330` | 418 | UnwindData |  |
| 27 | `W32TimeVerifyUnjoinConfig` | `0x4B4E0` | 335 | UnwindData |  |
| 7 | `SvchostEntry_W32Time` | `0x4DAB0` | 15,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `W32TimeGetNetlogonServiceBits` | `0x51570` | 370 | UnwindData |  |
| 16 | `W32TimeLog` | `0x516F0` | 363 | UnwindData |  |
| 18 | `W32TimeQueryConfiguration` | `0x51870` | 453 | UnwindData |  |
| 19 | `W32TimeQueryHardwareProviderStatus` | `0x51A40` | 26 | UnwindData |  |
| 20 | `W32TimeQueryNTPProviderStatus` | `0x51A60` | 23 | UnwindData |  |
| 21 | `W32TimeQueryNtpProviderConfiguration` | `0x51A80` | 515 | UnwindData |  |
| 22 | `W32TimeQuerySource` | `0x51C90` | 453 | UnwindData |  |
| 14 | `W32TimeDeleteConfig` | `0x52170` | 156 | UnwindData |  |
| 17 | `W32TimeQueryConfig` | `0x52220` | 234 | UnwindData |  |
| 24 | `W32TimeSetConfig` | `0x52310` | 209 | UnwindData |  |
| 1 | `fnW32TmI_ScSetServiceBits` | `0xA3B60` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `fnW32TmSetServiceStatus` | `0xA3B68` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `fnW32TmRegisterServiceCtrlHandlerEx` | `0xA3B70` | 0 | Indeterminate |  |
