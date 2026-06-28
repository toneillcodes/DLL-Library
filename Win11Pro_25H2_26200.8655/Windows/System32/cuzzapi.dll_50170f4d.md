# Binary Specification: cuzzapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cuzzapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `50170f4d7f8d51375b2a59459dcbe3ff16a2e78d09435757ccff12dd50718449`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CuzzDisable` | `0x12A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CuzzEnable` | `0x12C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CuzzGetRandomSeed` | `0x12E0` | 24 | UnwindData |  |
| 4 | `CuzzIsEnabled` | `0x1300` | 24 | UnwindData |  |
| 5 | `CuzzSchedule` | `0x1320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CuzzSetDebugLoweringPoint` | `0x1340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CuzzSetDebugPriority` | `0x1360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CuzzSetPriority` | `0x1380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CuzzSetRandomSeed` | `0x13A0` | 0 | Indeterminate |  |
