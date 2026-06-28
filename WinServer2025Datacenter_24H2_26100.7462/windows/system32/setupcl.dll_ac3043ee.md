# Binary Specification: setupcl.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\setupcl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ac3043eeeb8b6253541b7184a2d5db65f56d5ffa1be1c903c23e3533905de3b5`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SclAcquireRequiredPrivileges` | `0x1010` | 96 | UnwindData |  |
| 11 | `SclReleasePrivileges` | `0x19B0` | 190 | UnwindData |  |
| 2 | `SclClearPendedRequest` | `0x1E60` | 223 | UnwindData |  |
| 5 | `SclFreeRequest` | `0x2000` | 161 | UnwindData |  |
| 6 | `SclGetPendedRequest` | `0x20B0` | 1,558 | UnwindData |  |
| 8 | `SclPendRequest` | `0x2730` | 1,021 | UnwindData |  |
| 9 | `SclPendedRequestExists` | `0x2B40` | 332 | UnwindData |  |
| 3 | `SclExecutePendedRequests` | `0x56D0` | 818 | UnwindData |  |
| 4 | `SclExecuteRequest` | `0x5A10` | 305 | UnwindData |  |
| 10 | `SclPreCompilePendedRequests` | `0x5E50` | 770 | UnwindData |  |
| 7 | `SclLoadStringResource` | `0x7B60` | 166 | UnwindData |  |
