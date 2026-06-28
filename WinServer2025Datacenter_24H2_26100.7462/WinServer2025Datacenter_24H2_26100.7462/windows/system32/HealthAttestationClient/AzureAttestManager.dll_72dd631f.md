# Binary Specification: AzureAttestManager.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\HealthAttestationClient\AzureAttestManager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `72dd631fb1d81c029a482a6d7e12ff13653bec380194a44e7a08797c56d84bf7`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `AttestationCloseSession` | `0x57600` | 147 | UnwindData |  |
| 4 | `AttestationGetReport` | `0x576A0` | 175 | UnwindData |  |
| 1 | `AttestationAttest` | `0x57760` | 220 | UnwindData |  |
| 3 | `AttestationCreateSession` | `0x57850` | 270 | UnwindData |  |
| 5 | `InitializeAttestationLibrary` | `0x57970` | 47 | UnwindData |  |
| 9 | `__GetHostMetadata` | `0x57E00` | 16 | UnwindData |  |
| 12 | `__SignHash` | `0x58960` | 16 | UnwindData |  |
| 13 | `__TraceLog` | `0x58BF0` | 16 | UnwindData |  |
| 10 | `__GetKeyInfo` | `0x58E40` | 16 | UnwindData |  |
| 11 | `__GetTcgLog` | `0x59070` | 16 | UnwindData |  |
| 8 | `__FreeMemory` | `0x593E0` | 16 | UnwindData |  |
| 6 | `__AllocateMemory` | `0x59460` | 16 | UnwindData |  |
| 7 | `__AllocateParams` | `0x594F0` | 99,964 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
