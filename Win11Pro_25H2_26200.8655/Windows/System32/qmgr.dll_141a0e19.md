# Binary Specification: qmgr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\qmgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `141a0e195cf2246a20c2dfbcc435569b384cf2dd2d9c14f8ea338b1d05466697`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `?GetCounter32@CPerfMon@@QEAAPEAJPEAU__COUNTER_ID@1@PEAU__INSTANCE_ID@1@@Z` | `0x9A990` | 25,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `?GetCounter64@CPerfMon@@QEAAPEA_JPEAU__COUNTER_ID@1@PEAU__INSTANCE_ID@1@@Z` | `0x9A990` | 25,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??4CPerfMon@@QEAAAEAV0@AEBV0@@Z` | `0xA0E20` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `?CounterIdToPerfItem@CPerfMon@@AEBAPEAU_PERF_ITEM@1@PEAU__COUNTER_ID@1@@Z` | `0xA13F0` | 42 | UnwindData |  |
| 5 | `?IsValidInstId@CPerfMon@@AEBAHPEAU__OBJECT_ORD@1@PEAU__INSTANCE_ID@1@@Z` | `0xA2090` | 126 | UnwindData |  |
| 6 | `?IsValidObjOrd@CPerfMon@@AEBAHPEAU__OBJECT_ORD@1@@Z` | `0xA2120` | 2,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `?ObjectIdToPerfItem@CPerfMon@@AEBAPEAU_PERF_ITEM@1@PEAU__OBJECT_ID@1@@Z` | `0xA2930` | 47 | UnwindData |  |
| 8 | `?ObjectIdToPerfItemIndex@CPerfMon@@AEBAHPEAU__OBJECT_ID@1@@Z` | `0xA2970` | 5,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `ServiceMain` | `0xA3D60` | 5,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `BITSServiceMain` | `0xA5280` | 17 | UnwindData |  |
