# Binary Specification: dhcpcore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dhcpcore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d600b0f01f3c9a5877c2171af011f0f63216606acf4ae367827f7f2c3c6655e4`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `ServiceMain` | `0x27280` | 785 | UnwindData |  |
| 2 | `DhcpGlobalServiceSyncEvent` | `0x64968` | 264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DhcpGlobalIsShuttingDown` | `0x64A70` | 264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DhcpGlobalTerminateEvent` | `0x64B78` | 0 | Indeterminate |  |
