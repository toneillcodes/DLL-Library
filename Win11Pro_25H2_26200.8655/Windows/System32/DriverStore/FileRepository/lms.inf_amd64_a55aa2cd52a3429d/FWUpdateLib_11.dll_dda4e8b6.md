# Binary Specification: FWUpdateLib_11.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\lms.inf_amd64_a55aa2cd52a3429d\FWUpdateLib_11.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `dda4e8b67b8ac232d22fdd30e91e52e76b9e2afc954c25260984f0f7b32d4624`
* **Total Exported Functions:** 25

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `GetFwType` | `0x1DB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `GetOemID` | `0x1E10` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `GetPchSKU` | `0x2020` | 4,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `IsRestorePointImage` | `0x3290` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `VerifyOemId` | `0x3310` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `GetLastStatus` | `0x3450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetLastUpdateResetType` | `0x3480` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `GetInterfaces` | `0x34B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `SaveRestorePoint` | `0x34E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `GetFwVersion` | `0x3530` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CheckPolicy` | `0x3670` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CheckPolicyBuffer` | `0x36D0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FwUpdateCheckPowerSource` | `0x37A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `FWUpdate_QueryStatus_Get_Response` | `0x3800` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `GetExtendedIpuPartitionAttributes` | `0x3900` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `GetIpuPartitionAttributes` | `0x3A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `GetFwUpdateInfoStatus` | `0x3A60` | 2,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `FwUpdatePartial` | `0x4500` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `FwUpdateFull` | `0x4580` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `FwUpdateRestore` | `0x4600` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `FwUpdatePartialWithInstanceId` | `0x4680` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `FwUpdateRestoreBuffer` | `0x46F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `FwUpdatePartialBuffer` | `0x4760` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `FwUpdateFullBuffer` | `0x47A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `FwUpdatePartialWithInstanceIdBuffer` | `0x47D0` | 86,621 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
