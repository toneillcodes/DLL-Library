# Binary Specification: winrscmd.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\winrscmd.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fedd77289654bda7039f3af0a979330916e891fddfc44cf6d0af2b333396ff8d`
* **Total Exported Functions:** 31

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@XZ` | `0x2740` | 56 | UnwindData |  |
| 2 | `??0?$SafeMap_Iterator@VKey@Locale@@K@@QEAA@AEAV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@_N@Z` | `0x2780` | 268 | UnwindData |  |
| 3 | `??0?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@AEBV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@_N@Z` | `0x28A0` | 50 | UnwindData |  |
| 4 | `??1?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@XZ` | `0x28E0` | 78 | UnwindData |  |
| 5 | `??1?$SafeMap_Iterator@VKey@Locale@@K@@QEAA@XZ` | `0x2940` | 134 | UnwindData |  |
| 6 | `??1?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA@XZ` | `0x29D0` | 32 | UnwindData |  |
| 7 | `??1CWSManCriticalSectionWithConditionVar@@QEAA@XZ` | `0x2A90` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?Acquire@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEBAXXZ` | `0x2B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `?Release@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEBAXXZ` | `0x2B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `WSManPluginReleaseCommandContext` | `0x2B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `WSManPluginReleaseShellContext` | `0x2B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `?Acquire@?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAAXXZ` | `0x2B10` | 84 | UnwindData |  |
| 11 | `?Acquired@?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAA_NXZ` | `0x2B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?AsReference@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEAAAEAV1@XZ` | `0x2B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `?Data@?$SafeMap_Iterator@VKey@Locale@@K@@IEBAAEAV?$STLMap@VKey@Locale@@K@@XZ` | `0x2B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `?DeInitialize@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEAA_NAEAVIRequestContext@@@Z` | `0x2BA0` | 112 | UnwindData |  |
| 15 | `?GetInitError@CWSManCriticalSection@@QEBAKXZ` | `0x2C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `?GetMap@?$SafeMap_Iterator@VKey@Locale@@K@@QEBAAEAV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@XZ` | `0x2C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `?GetMap@?$SafeMap_Lock@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@QEBAAEBV?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@XZ` | `0x2C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `?Initialize@?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@UEAA_NAEAVIRequestContext@@@Z` | `0x2C40` | 201 | UnwindData |  |
| 19 | `?IsValid@?$SafeMap_Iterator@VKey@Locale@@K@@QEBA_NXZ` | `0x2D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `?Reset@?$SafeMap_Iterator@VKey@Locale@@K@@QEAAXXZ` | `0x2D20` | 92 | UnwindData |  |
| 22 | `?SkipOrphans@?$SafeMap_Iterator@VKey@Locale@@K@@IEAAXXZ` | `0x2D90` | 167 | UnwindData |  |
| 23 | `WSManPluginCommand` | `0x3060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `WSManPluginReceive` | `0x3070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `WSManPluginSend` | `0x3080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `WSManPluginShell` | `0x3090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `WSManPluginShutdown` | `0x30A0` | 322 | UnwindData |  |
| 30 | `WSManPluginSignal` | `0x31F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `WSManPluginStartup` | `0x3200` | 437 | UnwindData |  |
| 8 | `??_7?$SafeMap@VKey@Locale@@KV?$SafeMap_Iterator@VKey@Locale@@K@@@@6B@` | `0x17A98` | 0 | Indeterminate |  |
