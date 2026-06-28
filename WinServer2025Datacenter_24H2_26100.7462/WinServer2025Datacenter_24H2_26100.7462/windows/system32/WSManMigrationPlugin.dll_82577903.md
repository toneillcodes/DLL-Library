# Binary Specification: WSManMigrationPlugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WSManMigrationPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `82577903eb29d0fa303242e263508b65f3f966ded79331d4c30e339c27dc7fa5`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 23 | `DllCanUnloadNow` | `0x5800` | 42 | UnwindData |  |
| 24 | `DllGetClassObject` | `0x5830` | 302 | UnwindData |  |
| 25 | `DllMain` | `0x5970` | 59 | UnwindData |  |
| 26 | `DllRegisterServer` | `0x59C0` | 268 | UnwindData |  |
| 27 | `DllUnregisterServer` | `0x5AE0` | 253 | UnwindData |  |
| 1 | `??0?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@XZ` | `0x5CF0` | 56 | UnwindData |  |
| 2 | `??0?$SafeMap_Iterator@VKey@Locale@@K@@QEAA@AEAV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@_N@Z` | `0x5D30` | 268 | UnwindData |  |
| 3 | `??0?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@AEBV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@_N@Z` | `0x5E50` | 50 | UnwindData |  |
| 4 | `??1?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@XZ` | `0x6550` | 78 | UnwindData |  |
| 5 | `??1?$SafeMap_Iterator@VKey@Locale@@K@@QEAA@XZ` | `0x65B0` | 134 | UnwindData |  |
| 6 | `??1?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@XZ` | `0x6640` | 32 | UnwindData |  |
| 7 | `??1CWSManCriticalSectionWithConditionVar@@QEAA@XZ` | `0x6700` | 1,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?Acquire@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEBAXXZ` | `0x6B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `?Release@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEBAXXZ` | `0x6B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `?Acquire@?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAAXXZ` | `0x6B80` | 84 | UnwindData |  |
| 11 | `?Acquired@?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA_NXZ` | `0x6BE0` | 2,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?AsReference@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAAAEAV1@XZ` | `0x74C0` | 1,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `?Data@?$SafeMap_Iterator@VKey@Locale@@K@@IEBAAEAV?$STLMap@VKey@Locale@@K@@XZ` | `0x7B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `?DeInitialize@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEAA_NAEAVIRequestContext@@@Z` | `0x7B70` | 112 | UnwindData |  |
| 15 | `?GetInitError@CWSManCriticalSection@@QEBAKXZ` | `0x7FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `?GetMap@?$SafeMap_Iterator@VKey@Locale@@K@@QEBAAEAV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@XZ` | `0x7FB0` | 2,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `?GetMap@?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEBAAEBV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@XZ` | `0x7FB0` | 2,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `?Initialize@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEAA_NAEAVIRequestContext@@@Z` | `0x8AF0` | 201 | UnwindData |  |
| 19 | `?IsValid@?$SafeMap_Iterator@VKey@Locale@@K@@QEBA_NXZ` | `0x9050` | 2,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `?Reset@?$SafeMap_Iterator@VKey@Locale@@K@@QEAAXXZ` | `0x9980` | 92 | UnwindData |  |
| 22 | `?SkipOrphans@?$SafeMap_Iterator@VKey@Locale@@K@@IEAAXXZ` | `0x9B80` | 167 | UnwindData |  |
| 8 | `??_7?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@6B@` | `0x10000` | 0 | Indeterminate |  |
