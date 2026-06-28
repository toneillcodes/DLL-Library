# Binary Specification: clbcatq.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\clbcatq.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fecb023619a83d7a46c0afd2e4f6b70243a9c64c5aefd479535d7a8d62d9f1fe`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 25 | `OpenComponentLibraryEx` | `0x5F50` | 35 | UnwindData |  |
| 20 | `GetCatalogObject` | `0x15C00` | 159 | UnwindData |  |
| 21 | `GetCatalogObject2` | `0x15F50` | 154 | UnwindData |  |
| 17 | `DllGetClassObject` | `0x16C80` | 26,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetGlobalBabyJITEnabled` | `0x1D290` | 199 | UnwindData |  |
| 23 | `GetSimpleTableDispenser` | `0x1E4F0` | 118 | UnwindData |  |
| 9 | `CheckMemoryGates` | `0x1F330` | 401 | UnwindData |  |
| 16 | `DllCanUnloadNow` | `0x20ED0` | 10,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ComPlusEnablePartitions` | `0x23990` | 230 | UnwindData |  |
| 11 | `ComPlusEnableRemoteAccess` | `0x23A80` | 178 | UnwindData |  |
| 13 | `ComPlusPartitionsEnabled` | `0x23B40` | 302 | UnwindData |  |
| 14 | `ComPlusRemoteAccessEnabled` | `0x23C80` | 240 | UnwindData |  |
| 18 | `DllRegisterServer` | `0x23D80` | 189 | UnwindData |  |
| 19 | `DllUnregisterServer` | `0x23E50` | 69 | UnwindData |  |
| 22 | `GetComputerObject` | `0x23EA0` | 64,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CLSIDFromStringByBitness` | `0x338B0` | 428 | UnwindData |  |
| 24 | `InprocServer32FromString` | `0x33A70` | 174 | UnwindData |  |
| 28 | `ServerGetApplicationType` | `0x33B30` | 348 | UnwindData |  |
| 29 | `SetSetupOpen` | `0x33CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `SetSetupSave` | `0x33CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `SetupOpen` | `0x33CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `SetupSave` | `0x33CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `ActivatorUpdateForIsRouterChanges` | `0x33CE0` | 1,057 | UnwindData |  |
| 3 | `DeleteAllActivatorsForClsid` | `0x34170` | 319 | UnwindData |  |
| 6 | `UpdateFromAppChange` | `0x34AE0` | 1,529 | UnwindData |  |
| 7 | `UpdateFromComponentChange` | `0x350E0` | 1,072 | UnwindData |  |
| 4 | `DowngradeAPL` | `0x35660` | 509 | UnwindData |  |
| 12 | `ComPlusMigrate` | `0x37540` | 164 | UnwindData |  |
| 2 | `CoRegCleanup` | `0x3A410` | 66 | UnwindData |  |
| 15 | `CreateComponentLibraryEx` | `0x3A4D0` | 141 | UnwindData |  |
| 26 | `OpenComponentLibraryOnMemEx` | `0x3A570` | 137 | UnwindData |  |
| 27 | `OpenComponentLibraryOnStreamEx` | `0x3A600` | 153 | UnwindData |  |
