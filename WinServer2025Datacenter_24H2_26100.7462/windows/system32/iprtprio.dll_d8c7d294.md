# Binary Specification: iprtprio.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\iprtprio.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d8c7d29434f3d614005cac4de4bc3735f910b0f3a97eb044b6503fa34799dc17`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CleanUpIpPriority` | `0x1710` | 100 | UnwindData |  |
| 2 | `ComputeRouteMetric` | `0x1780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ComputeRouteMetricEx` | `0x1790` | 145 | UnwindData |  |
| 4 | `GetPriorityInfo` | `0x18C0` | 246 | UnwindData |  |
| 5 | `SetPriorityInfo` | `0x19C0` | 485 | UnwindData |  |
