# Binary Specification: iprtprio.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\iprtprio.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `658bcdc04a6bd9ca2f450f17e2694c976bf64f69ac613adefecc7ab337ccc0c6`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CleanUpIpPriority` | `0x1710` | 100 | UnwindData |  |
| 2 | `ComputeRouteMetric` | `0x1780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ComputeRouteMetricEx` | `0x1790` | 145 | UnwindData |  |
| 4 | `GetPriorityInfo` | `0x18C0` | 246 | UnwindData |  |
| 5 | `SetPriorityInfo` | `0x19C0` | 485 | UnwindData |  |
