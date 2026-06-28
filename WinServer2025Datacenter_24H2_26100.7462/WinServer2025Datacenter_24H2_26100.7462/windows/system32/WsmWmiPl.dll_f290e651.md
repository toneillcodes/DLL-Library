# Binary Specification: WsmWmiPl.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WsmWmiPl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f290e651ce2d93fff4985ee497cc8bd1a3e65b73d7122245fcae0a58eb92e5e3`
* **Total Exported Functions:** 39

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@XZ` | `0x2C50` | 56 | UnwindData |  |
| 2 | `??0?$SafeMap_Iterator@VKey@Locale@@K@@QEAA@AEAV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@_N@Z` | `0x2C90` | 163 | UnwindData |  |
| 3 | `??0?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@AEBV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@_N@Z` | `0x2D40` | 36 | UnwindData |  |
| 4 | `??1?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@XZ` | `0x2D80` | 47 | UnwindData |  |
| 5 | `??1?$SafeMap_Iterator@VKey@Locale@@K@@QEAA@XZ` | `0x2DC0` | 118 | UnwindData |  |
| 6 | `??1?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@XZ` | `0x2E40` | 32 | UnwindData |  |
| 7 | `??1CWSManCriticalSectionWithConditionVar@@QEAA@XZ` | `0x2F10` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?Acquire@?$SafeMap@VKey@CWmiPtrCache@@VMapping@2@V?$SafeMap_Iterator@VKey@CWmiPtrCache@@VMapping@2@@@@@UEBAXXZ` | `0x3050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `?Acquire@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEBAXXZ` | `0x3050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `?Release@?$SafeMap@VKey@CWmiPtrCache@@VMapping@2@V?$SafeMap_Iterator@VKey@CWmiPtrCache@@VMapping@2@@@@@UEBAXXZ` | `0x3050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?Release@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEBAXXZ` | `0x3050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `?Acquire@?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAAXXZ` | `0x3060` | 84 | UnwindData |  |
| 12 | `?Acquired@?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA_NXZ` | `0x30C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `?AsReference@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAAAEAV1@XZ` | `0x30D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `?Data@?$SafeMap_Iterator@VKey@Locale@@K@@IEBAAEAV?$STLMap@VKey@Locale@@K@@XZ` | `0x30E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?DeInitialize@?$SafeMap@VKey@CWmiPtrCache@@VMapping@2@V?$SafeMap_Iterator@VKey@CWmiPtrCache@@VMapping@2@@@@@UEAA_NAEAVIRequestContext@@@Z` | `0x30F0` | 81 | UnwindData |  |
| 16 | `?DeInitialize@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEAA_NAEAVIRequestContext@@@Z` | `0x3150` | 81 | UnwindData |  |
| 17 | `?GetInitError@CWSManCriticalSection@@QEBAKXZ` | `0x31B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `?GetMap@?$SafeMap_Iterator@VKey@Locale@@K@@QEBAAEAV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@XZ` | `0x31C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?GetMap@?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEBAAEBV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@XZ` | `0x31C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `?Initialize@?$SafeMap@VKey@CWmiPtrCache@@VMapping@2@V?$SafeMap_Iterator@VKey@CWmiPtrCache@@VMapping@2@@@@@UEAA_NAEAVIRequestContext@@@Z` | `0x31D0` | 201 | UnwindData |  |
| 21 | `?Initialize@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEAA_NAEAVIRequestContext@@@Z` | `0x32A0` | 201 | UnwindData |  |
| 22 | `?IsValid@?$SafeMap_Iterator@VKey@CWmiPtrCache@@VMapping@2@@@QEBA_NXZ` | `0x3370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `?IsValid@?$SafeMap_Iterator@VKey@Locale@@K@@QEBA_NXZ` | `0x3370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?Reset@?$SafeMap_Iterator@VKey@Locale@@K@@QEAAXXZ` | `0x3380` | 92 | UnwindData |  |
| 27 | `?SkipOrphans@?$SafeMap_Iterator@VKey@Locale@@K@@IEAAXXZ` | `0x33F0` | 145 | UnwindData |  |
| 28 | `WSManPluginShutdown` | `0x3EB0` | 860 | UnwindData |  |
| 29 | `WSManPluginStartup` | `0x4220` | 1,740 | UnwindData |  |
| 30 | `WSManProvCreate` | `0x4900` | 611 | UnwindData |  |
| 31 | `WSManProvDelete` | `0x4B70` | 460 | UnwindData |  |
| 32 | `WSManProvEnumerate` | `0x4D50` | 733 | UnwindData |  |
| 33 | `WSManProvGet` | `0x5040` | 558 | UnwindData |  |
| 34 | `WSManProvIdentify` | `0x5280` | 611 | UnwindData |  |
| 35 | `WSManProvInvoke` | `0x54F0` | 651 | UnwindData |  |
| 36 | `WSManProvPullEvents` | `0x5790` | 370 | UnwindData |  |
| 37 | `WSManProvPut` | `0x5910` | 689 | UnwindData |  |
| 38 | `WSManProvSubscribe` | `0x5BD0` | 733 | UnwindData |  |
| 39 | `WSManProvUnsubscribe` | `0x5EC0` | 185 | UnwindData |  |
| 8 | `??_7?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@6B@` | `0x39A98` | 0 | Indeterminate |  |
