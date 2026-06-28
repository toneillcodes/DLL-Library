# Binary Specification: dhcpcsvc6.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dhcpcsvc6.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e81f2a6d7a73bc666e6d46162db30ba2dc0c695733a5651f7e79de746124f434`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `Dhcpv6FreeLeaseInfo` | `0x1010` | 168 | UnwindData |  |
| 10 | `Dhcpv6FreeLeaseInfoArray` | `0x11B0` | 69 | UnwindData |  |
| 7 | `Dhcpv6FreeCachedParamsData` | `0x1770` | 19 | UnwindData |  |
| 13 | `Dhcpv6IsEnabled` | `0x1CC0` | 31 | UnwindData |  |
| 14 | `Dhcpv6QueryLeaseInfo` | `0x2200` | 2,704 | UnwindData |  |
| 15 | `Dhcpv6QueryLeaseInfoArray` | `0x2CA0` | 2,360 | UnwindData |  |
| 1 | `Dhcpv6AcquireParameters` | `0x5750` | 371 | UnwindData |  |
| 2 | `Dhcpv6CApiCleanup` | `0x58D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `Dhcpv6CApiInitialize` | `0x58E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `Dhcpv6CancelOperation` | `0x5900` | 186 | UnwindData |  |
| 5 | `Dhcpv6EnableDhcp` | `0x59C0` | 371 | UnwindData |  |
| 8 | `Dhcpv6FreeCachedParamsDataEx` | `0x5B40` | 132 | UnwindData |  |
| 11 | `Dhcpv6GetTraceArray` | `0x5BD0` | 343 | UnwindData |  |
| 12 | `Dhcpv6GetUserClasses` | `0x5D30` | 565 | UnwindData |  |
| 16 | `Dhcpv6ReleaseParameters` | `0x5F70` | 371 | UnwindData |  |
| 17 | `Dhcpv6ReleasePrefix` | `0x60F0` | 172 | UnwindData |  |
| 18 | `Dhcpv6ReleasePrefixEx` | `0x61B0` | 721 | UnwindData |  |
| 19 | `Dhcpv6RenewPrefix` | `0x6490` | 197 | UnwindData |  |
| 20 | `Dhcpv6RenewPrefixEx` | `0x6560` | 1,143 | UnwindData |  |
| 21 | `Dhcpv6RequestCachedParams` | `0x69E0` | 934 | UnwindData |  |
| 22 | `Dhcpv6RequestCachedParamsEx` | `0x6D90` | 1,026 | UnwindData |  |
| 23 | `Dhcpv6RequestParams` | `0x71A0` | 1,127 | UnwindData |  |
| 24 | `Dhcpv6RequestPrefix` | `0x7610` | 189 | UnwindData |  |
| 25 | `Dhcpv6RequestPrefixEx` | `0x76E0` | 1,113 | UnwindData |  |
| 26 | `Dhcpv6SetUserClass` | `0x7B40` | 414 | UnwindData |  |
| 6 | `Dhcpv6EnableTracing` | `0x7CF0` | 0 | Indeterminate |  |
