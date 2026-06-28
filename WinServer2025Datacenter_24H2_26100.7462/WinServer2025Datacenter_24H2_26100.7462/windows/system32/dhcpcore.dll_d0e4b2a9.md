# Binary Specification: dhcpcore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dhcpcore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d0e4b2a99703246a2d792f4cc1a59c7cf4cc6982e3e56ab927414564a9ef3ca9`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `ServiceMain` | `0x27550` | 788 | UnwindData |  |
| 2 | `DhcpGlobalServiceSyncEvent` | `0x64958` | 248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DhcpGlobalIsShuttingDown` | `0x64A50` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DhcpGlobalTerminateEvent` | `0x64B50` | 0 | Indeterminate |  |
