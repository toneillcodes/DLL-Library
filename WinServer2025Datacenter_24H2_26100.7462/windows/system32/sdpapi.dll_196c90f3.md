# Binary Specification: sdpapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sdpapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `196c90f30fe9325e7f40c379be61fdbff3bf8fe4b1a5969efd7d74a669592752`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SDPCpuQueryAllStats` | `0x12F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SDPCpuQueryStats` | `0x12F50` | 25 | UnwindData |  |
| 3 | `SDPETWQueryAllStats` | `0x12F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SDPETWQueryRequests` | `0x12F90` | 885 | UnwindData |  |
| 5 | `SDPETWQueryStats` | `0x13310` | 31 | UnwindData |  |
| 6 | `SDPETWRemoveRequest` | `0x13340` | 369 | UnwindData |  |
| 7 | `SDPETWRequest` | `0x134C0` | 369 | UnwindData |  |
| 8 | `SDPFreeCpuRecordSet` | `0x13640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SDPFreeETWRecordSet` | `0x13650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SDPFreeETWRequestSet` | `0x13660` | 66 | UnwindData |  |
| 11 | `SDPFreeNetworkRecordSet` | `0x136B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SDPFreePerfCounterRecordSet` | `0x136C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `SDPFreePerfCounterRequestSet` | `0x136D0` | 152 | UnwindData |  |
| 14 | `SDPFreePhysicalDiskRecordSet` | `0x13770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `SDPFreeVolumeRecordSet` | `0x13780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SDPNetworkQueryAllStats` | `0x13790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SDPNetworkQueryStats` | `0x137B0` | 25 | UnwindData |  |
| 18 | `SDPPerfCounterQueryAllStats` | `0x137D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `SDPPerfCounterQueryRequests` | `0x137F0` | 909 | UnwindData |  |
| 20 | `SDPPerfCounterQueryStats` | `0x13B90` | 25 | UnwindData |  |
| 21 | `SDPPerfCounterRemoveRequest` | `0x13BB0` | 535 | UnwindData |  |
| 22 | `SDPPerfCounterRequest` | `0x13DD0` | 561 | UnwindData |  |
| 23 | `SDPPhysicalDiskQueryAllStats` | `0x14010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `SDPPhysicalDiskQueryStats` | `0x14030` | 25 | UnwindData |  |
| 25 | `SDPVolumeQueryAllStats` | `0x140F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `SDPVolumeQueryStats` | `0x14110` | 25 | UnwindData |  |
