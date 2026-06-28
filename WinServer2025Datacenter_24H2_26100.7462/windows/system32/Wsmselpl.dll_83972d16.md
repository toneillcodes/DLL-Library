# Binary Specification: Wsmselpl.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Wsmselpl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `83972d1675f3f942f89bbe20c21764919f97158669e58fda8143c60abf2f44b7`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@XZ` | `0x2660` | 56 | UnwindData |  |
| 2 | `??0?$SafeMap_Iterator@VKey@Locale@@K@@QEAA@AEAV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@_N@Z` | `0x26A0` | 268 | UnwindData |  |
| 3 | `??0?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@AEBV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@_N@Z` | `0x27C0` | 50 | UnwindData |  |
| 4 | `??1?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@XZ` | `0x2810` | 78 | UnwindData |  |
| 5 | `??1?$SafeMap_Iterator@VKey@Locale@@K@@QEAA@XZ` | `0x2870` | 134 | UnwindData |  |
| 6 | `??1?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@XZ` | `0x2900` | 32 | UnwindData |  |
| 7 | `??1CWSManCriticalSectionWithConditionVar@@QEAA@XZ` | `0x2A00` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?Acquire@?$SafeMap@VKey@CWmiPtrCache@@VMapping@2@V?$SafeMap_Iterator@VKey@CWmiPtrCache@@VMapping@2@@@@@UEBAXXZ` | `0x2AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `?Acquire@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEBAXXZ` | `0x2AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `?Release@?$SafeMap@VKey@CWmiPtrCache@@VMapping@2@V?$SafeMap_Iterator@VKey@CWmiPtrCache@@VMapping@2@@@@@UEBAXXZ` | `0x2AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?Release@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEBAXXZ` | `0x2AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `?Acquire@?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAAXXZ` | `0x2AB0` | 84 | UnwindData |  |
| 12 | `?Acquired@?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA_NXZ` | `0x2B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `?AsReference@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAAAEAV1@XZ` | `0x2B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `?Data@?$SafeMap_Iterator@VKey@Locale@@K@@IEBAAEAV?$STLMap@VKey@Locale@@K@@XZ` | `0x2B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?DeInitialize@?$SafeMap@VKey@CWmiPtrCache@@VMapping@2@V?$SafeMap_Iterator@VKey@CWmiPtrCache@@VMapping@2@@@@@UEAA_NAEAVIRequestContext@@@Z` | `0x2B40` | 161 | UnwindData |  |
| 16 | `?DeInitialize@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEAA_NAEAVIRequestContext@@@Z` | `0x2BF0` | 112 | UnwindData |  |
| 17 | `?GetInitError@CWSManCriticalSection@@QEBAKXZ` | `0x2C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `?GetMap@?$SafeMap_Iterator@VKey@Locale@@K@@QEBAAEAV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@XZ` | `0x2C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?GetMap@?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEBAAEBV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@XZ` | `0x2C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `?Initialize@?$SafeMap@VKey@CWmiPtrCache@@VMapping@2@V?$SafeMap_Iterator@VKey@CWmiPtrCache@@VMapping@2@@@@@UEAA_NAEAVIRequestContext@@@Z` | `0x2C90` | 201 | UnwindData |  |
| 21 | `?Initialize@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEAA_NAEAVIRequestContext@@@Z` | `0x2D60` | 201 | UnwindData |  |
| 22 | `?IsValid@?$SafeMap_Iterator@VKey@CWmiPtrCache@@VMapping@2@@@QEBA_NXZ` | `0x2E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `?IsValid@?$SafeMap_Iterator@VKey@Locale@@K@@QEBA_NXZ` | `0x2E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?Reset@?$SafeMap_Iterator@VKey@Locale@@K@@QEAAXXZ` | `0x2E40` | 92 | UnwindData |  |
| 27 | `?SkipOrphans@?$SafeMap_Iterator@VKey@Locale@@K@@IEAAXXZ` | `0x2EB0` | 167 | UnwindData |  |
| 28 | `WSManPluginShutdown` | `0x3270` | 474 | UnwindData |  |
| 29 | `WSManPluginStartup` | `0x3450` | 648 | UnwindData |  |
| 30 | `WSManProvPullEvents` | `0x36E0` | 158 | UnwindData |  |
| 31 | `WSManProvSubscribe` | `0x3790` | 358 | UnwindData |  |
| 32 | `WSManProvUnsubscribe` | `0x3900` | 131 | UnwindData |  |
| 8 | `??_7?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@6B@` | `0x18A98` | 0 | Indeterminate |  |
