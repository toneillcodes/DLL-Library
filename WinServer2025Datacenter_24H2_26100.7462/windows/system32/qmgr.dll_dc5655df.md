# Binary Specification: qmgr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\qmgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dc5655df1058700f52dc698295059762035847b2c21ba2703a5c6f6805a41dee`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `?GetCounter32@CPerfMon@@QEAAPEAJPEAU__COUNTER_ID@1@PEAU__INSTANCE_ID@1@@Z` | `0x9AD50` | 25,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `?GetCounter64@CPerfMon@@QEAAPEA_JPEAU__COUNTER_ID@1@PEAU__INSTANCE_ID@1@@Z` | `0x9AD50` | 25,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??4CPerfMon@@QEAAAEAV0@AEBV0@@Z` | `0xA11E0` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `?CounterIdToPerfItem@CPerfMon@@AEBAPEAU_PERF_ITEM@1@PEAU__COUNTER_ID@1@@Z` | `0xA17B0` | 42 | UnwindData |  |
| 5 | `?IsValidInstId@CPerfMon@@AEBAHPEAU__OBJECT_ORD@1@PEAU__INSTANCE_ID@1@@Z` | `0xA2430` | 126 | UnwindData |  |
| 6 | `?IsValidObjOrd@CPerfMon@@AEBAHPEAU__OBJECT_ORD@1@@Z` | `0xA24C0` | 2,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `?ObjectIdToPerfItem@CPerfMon@@AEBAPEAU_PERF_ITEM@1@PEAU__OBJECT_ID@1@@Z` | `0xA2CD0` | 47 | UnwindData |  |
| 8 | `?ObjectIdToPerfItemIndex@CPerfMon@@AEBAHPEAU__OBJECT_ID@1@@Z` | `0xA2D10` | 4,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `ServiceMain` | `0xA4090` | 5,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `BITSServiceMain` | `0xA55A0` | 17 | UnwindData |  |
