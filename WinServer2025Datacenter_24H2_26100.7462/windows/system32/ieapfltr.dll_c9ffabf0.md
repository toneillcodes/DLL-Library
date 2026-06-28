# Binary Specification: ieapfltr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ieapfltr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c9ffabf048d63c5a29107f90122a5c7f72fe0ebc7058d9df409b5a0e76bf41f2`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CreateIUrlReputationSolution2` | `0x31B0` | 30 | UnwindData |  |
| 1 | `CreateIAppRep2` | `0x1CAE0` | 115 | UnwindData |  |
| 2 | `CreateIAppRepParm2` | `0x1CB60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateUrlBlockBroker` | `0x1CB70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CreateUrlBlockClient` | `0x1CB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DestroyUrlBlockBroker` | `0x1CB90` | 87 | UnwindData |  |
| 7 | `DestroyUrlBlockClient` | `0x1CBF0` | 87 | UnwindData |  |
| 8 | `DllCanUnloadNow` | `0x1CC50` | 142 | UnwindData |  |
| 9 | `DllGetClassObject` | `0x1CCF0` | 157 | UnwindData |  |
| 10 | `DllRegisterServer` | `0x1CDA0` | 190 | UnwindData |  |
| 11 | `DllUnregisterServer` | `0x1CE70` | 119 | UnwindData |  |
| 12 | `GetUrlBlockBroker` | `0x1CEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `GetUrlBlockClient` | `0x1CF00` | 648,324 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
