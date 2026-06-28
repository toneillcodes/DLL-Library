# Binary Specification: bitsperf.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\bitsperf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ba5edd7c1527a24c0508f0e94239e90be7dad16152e983d72fa0b127157c1540`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `?GetCounter@CPerfMon@@AEAAPEAEPEAU__COUNTER_ID@1@PEAU__INSTANCE_ID@1@@Z` | `0x1010` | 531 | UnwindData |  |
| 30 | `PerfMon_Close` | `0x1250` | 42 | UnwindData |  |
| 31 | `PerfMon_Collect` | `0x1280` | 36 | UnwindData |  |
| 7 | `?CollectAllObjects@CPerfMon@@AEBAKPEAGPEAPEAEPEAK2@Z` | `0x12B0` | 641 | UnwindData |  |
| 2 | `??1CPerfMon@@QEAA@XZ` | `0x1660` | 285 | UnwindData |  |
| 8 | `?CollectAnObject@CPerfMon@@AEBAKPEAU__OBJECT_ORD@1@PEAPEAE@Z` | `0x17D0` | 267 | UnwindData |  |
| 4 | `?CalcBytesForPerfObject@CPerfMon@@AEBAKPEAU__OBJECT_ORD@1@@Z` | `0x1A30` | 155 | UnwindData |  |
| 21 | `?InitializePerfMon@CPerfMon@@AEAAKH@Z` | `0x1B70` | 70 | UnwindData |  |
| 32 | `PerfMon_Open` | `0x2910` | 242 | UnwindData |  |
| 5 | `?CalcPerfMetrics@CPerfMon@@AEBAXPEAU__OBJECT_ORD@1@PEAU__INSTANCE_ID@1@PEAU_PERF_METRICS@1@PEAPEAU_PERF_ITEM@1@@Z` | `0x2AD0` | 463 | UnwindData |  |
| 12 | `?CounterIdToPerfItemIndex@CPerfMon@@AEBAHPEAU__COUNTER_ID@1@PEAH@Z` | `0x2CB0` | 199 | UnwindData |  |
| 20 | `?Initialize@CPerfMon@@QEAAKH@Z` | `0x2D80` | 77 | UnwindData |  |
| 29 | `?VerifyPerfItemTable@CPerfMon@@AEAAKXZ` | `0x2DE0` | 763 | UnwindData |  |
| 14 | `?DetermineObjectsToCollect@CPerfMon@@AEBAXPEAU__OBJECT_ORD@1@@Z` | `0x31C0` | 47 | UnwindData |  |
| 28 | `?ObjectOrdToPerfItemIndex@CPerfMon@@AEBAHPEAU__OBJECT_ORD@1@@Z` | `0x32F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?IdToPerfItemIndex@CPerfMon@@AEBAHH_K@Z` | `0x3320` | 154 | UnwindData |  |
| 10 | `?CounterIdToObjectOrd@CPerfMon@@AEBAPEAU__OBJECT_ORD@1@PEAU__COUNTER_ID@1@PEAH@Z` | `0x33C0` | 266 | UnwindData |  |
| 27 | `?ObjectOrdToPerfItem@CPerfMon@@AEBAPEAU_PERF_ITEM@1@PEAU__OBJECT_ORD@1@@Z` | `0x34D0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `?CounterOrdToPerfItem@CPerfMon@@AEBAPEAU_PERF_ITEM@1@PEAU__OBJECT_ORD@1@PEAU__COUNTER_ORD@1@@Z` | `0x35B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0CPerfMon@@QEAA@PEAGPEAU_PERF_ITEM@0@@Z` | `0x35F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?ObjectIdToPerfItemIndex@CPerfMon@@AEBAHPEAU__OBJECT_ID@1@@Z` | `0x3640` | 114 | UnwindData |  |
| 18 | `?HowManyInstancesAreInUse@CPerfMon@@AEBAHPEAU__OBJECT_ORD@1@@Z` | `0x36C0` | 208 | UnwindData |  |
| 6 | `?Collect@CPerfMon@@QEAAKPEAGPEAPEAEPEAK2@Z` | `0x37A0` | 3,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??4CPerfMon@@QEAAAEAV0@AEBV0@@Z` | `0x4730` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `?CounterIdToPerfItem@CPerfMon@@AEBAPEAU_PERF_ITEM@1@PEAU__COUNTER_ID@1@@Z` | `0x4770` | 35 | UnwindData |  |
| 15 | `?GetCounter32@CPerfMon@@QEAAPEAJPEAU__COUNTER_ID@1@PEAU__INSTANCE_ID@1@@Z` | `0x47A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `?GetCounter64@CPerfMon@@QEAAPEA_JPEAU__COUNTER_ID@1@PEAU__INSTANCE_ID@1@@Z` | `0x47A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `?IsValidInstId@CPerfMon@@AEBAHPEAU__OBJECT_ORD@1@PEAU__INSTANCE_ID@1@@Z` | `0x47B0` | 142 | UnwindData |  |
| 23 | `?IsValidObjOrd@CPerfMon@@AEBAHPEAU__OBJECT_ORD@1@@Z` | `0x4850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?ObjectIdToPerfItem@CPerfMon@@AEBAPEAU_PERF_ITEM@1@PEAU__OBJECT_ID@1@@Z` | `0x4870` | 40 | UnwindData |  |
| 9 | `?ConvertInstIdToInUseInstId@CPerfMon@@AEBAHPEAU__OBJECT_ORD@1@PEAU__INSTANCE_ID@1@@Z` | `0x4A10` | 190 | UnwindData |  |
| 24 | `?ObjectIdToObjectOrd@CPerfMon@@AEBAPEAU__OBJECT_ORD@1@PEAU__OBJECT_ID@1@@Z` | `0x4AE0` | 131 | UnwindData |  |
