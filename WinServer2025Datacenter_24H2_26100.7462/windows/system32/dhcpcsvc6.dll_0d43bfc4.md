# Binary Specification: dhcpcsvc6.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dhcpcsvc6.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0d43bfc4a046deeb870849ec9027b5dbde6a9e765fd6bdb67f1242b774bdaf95`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `Dhcpv6FreeLeaseInfo` | `0x1010` | 168 | UnwindData |  |
| 9 | `Dhcpv6FreeLeaseInfoArray` | `0x1210` | 69 | UnwindData |  |
| 7 | `Dhcpv6FreeCachedParamsData` | `0x1A60` | 19 | UnwindData |  |
| 12 | `Dhcpv6IsEnabled` | `0x1D60` | 30 | UnwindData |  |
| 13 | `Dhcpv6QueryLeaseInfo` | `0x2290` | 2,687 | UnwindData |  |
| 14 | `Dhcpv6QueryLeaseInfoArray` | `0x2D20` | 2,339 | UnwindData |  |
| 1 | `Dhcpv6AcquireParameters` | `0x4B00` | 361 | UnwindData |  |
| 2 | `Dhcpv6CApiCleanup` | `0x4C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `Dhcpv6CApiInitialize` | `0x4C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `Dhcpv6CancelOperation` | `0x4CA0` | 179 | UnwindData |  |
| 5 | `Dhcpv6EnableDhcp` | `0x4D60` | 361 | UnwindData |  |
| 6 | `Dhcpv6EnableTracing` | `0x4ED0` | 271 | UnwindData |  |
| 10 | `Dhcpv6GetTraceArray` | `0x4FF0` | 336 | UnwindData |  |
| 11 | `Dhcpv6GetUserClasses` | `0x5150` | 560 | UnwindData |  |
| 15 | `Dhcpv6ReleaseParameters` | `0x5390` | 361 | UnwindData |  |
| 16 | `Dhcpv6ReleasePrefix` | `0x5500` | 166 | UnwindData |  |
| 17 | `Dhcpv6ReleasePrefixEx` | `0x55B0` | 711 | UnwindData |  |
| 18 | `Dhcpv6RenewPrefix` | `0x5880` | 191 | UnwindData |  |
| 19 | `Dhcpv6RenewPrefixEx` | `0x5950` | 1,133 | UnwindData |  |
| 20 | `Dhcpv6RequestCachedParams` | `0x5DD0` | 642 | UnwindData |  |
| 21 | `Dhcpv6RequestParams` | `0x6060` | 1,099 | UnwindData |  |
| 22 | `Dhcpv6RequestPrefix` | `0x64C0` | 183 | UnwindData |  |
| 23 | `Dhcpv6RequestPrefixEx` | `0x6580` | 1,103 | UnwindData |  |
| 24 | `Dhcpv6SetUserClass` | `0x69E0` | 723 | UnwindData |  |
