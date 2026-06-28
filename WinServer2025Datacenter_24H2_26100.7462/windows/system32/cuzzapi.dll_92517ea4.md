# Binary Specification: cuzzapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cuzzapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `92517ea44c4e8338571cc10584d6e505495c136ec4c24a76980b4cb56b05b208`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CuzzDisable` | `0x1290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CuzzEnable` | `0x12B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CuzzGetRandomSeed` | `0x12D0` | 24 | UnwindData |  |
| 4 | `CuzzIsEnabled` | `0x12F0` | 24 | UnwindData |  |
| 5 | `CuzzSchedule` | `0x1310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CuzzSetDebugLoweringPoint` | `0x1330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CuzzSetDebugPriority` | `0x1350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CuzzSetPriority` | `0x1370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CuzzSetRandomSeed` | `0x1390` | 0 | Indeterminate |  |
