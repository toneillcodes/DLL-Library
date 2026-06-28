# Binary Specification: dmvdsitf.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dmvdsitf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2b11e44a7979e68947a2ee606f29657086a7139ec78e1c1a784f7aabd674cf5f`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `?AddLDMObjMapEntry@CDataCache@@QEAAXPEAU_LDM_OBJ_MAP_ENTRY@@@Z` | `0x2B00` | 31 | UnwindData |  |
| 4 | `?GetDiskCount@CDataCache@@QEAAKXZ` | `0x2B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `?GetLdmObjectId@CDMNodeObj@@QEAA_JXZ` | `0x2B80` | 38 | UnwindData |  |
| 6 | `?GetNumMembers@CDMNodeObj@@QEAAKXZ` | `0x2BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `?GetOcxFrameCWndPtr@CTaskData@@QEAAPEAVCWnd@@XZ` | `0x2BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `?GetRegionColorStructPtr@CTaskData@@QEAAXPEAPEAU_REGION_COLORS@@AEAH@Z` | `0x2BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?GetServerName@CDataCache@@QEAA?AVCString@@XZ` | `0x2BF0` | 59 | UnwindData |  |
| 10 | `?GetVolumeCount@CDataCache@@QEAAKXZ` | `0x2C40` | 5,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CreateDataCacheZ` | `0x4130` | 48 | UnwindData |  |
| 11 | `LoadPropertyPageData` | `0xEF90` | 1,379 | UnwindData |  |
| 3 | `CreateServerRequestsZ` | `0x11C00` | 161 | UnwindData |  |
