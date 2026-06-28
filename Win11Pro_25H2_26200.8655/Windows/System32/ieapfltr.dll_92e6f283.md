# Binary Specification: ieapfltr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ieapfltr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `92e6f283cda4838d555622d2b02b91a1e2453ae68ac94b44e2d6efbf8bebddef`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `CreateIUrlReputationSolution2` | `0x30B0` | 30 | UnwindData |  |
| 1 | `CreateIAppRep2` | `0x1C8A0` | 115 | UnwindData |  |
| 2 | `CreateIAppRepParm2` | `0x1C920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateUrlBlockBroker` | `0x1C930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CreateUrlBlockClient` | `0x1C940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DestroyUrlBlockBroker` | `0x1C950` | 87 | UnwindData |  |
| 7 | `DestroyUrlBlockClient` | `0x1C9B0` | 87 | UnwindData |  |
| 8 | `DllCanUnloadNow` | `0x1CA10` | 142 | UnwindData |  |
| 9 | `DllGetClassObject` | `0x1CAB0` | 157 | UnwindData |  |
| 10 | `DllRegisterServer` | `0x1CB60` | 190 | UnwindData |  |
| 11 | `DllUnregisterServer` | `0x1CC30` | 119 | UnwindData |  |
| 12 | `GetUrlBlockBroker` | `0x1CCB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `GetUrlBlockClient` | `0x1CCC0` | 629,131 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
