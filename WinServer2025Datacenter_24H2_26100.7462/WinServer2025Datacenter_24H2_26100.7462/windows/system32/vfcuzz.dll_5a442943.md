# Binary Specification: vfcuzz.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vfcuzz.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5a44294352828f9fb32a68933bbbe0aaa29f736a9b3b5a84fe4548db868fb18f`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `CuzzDumpDebuggingState` | `0x1300` | 3,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CuzzDisable` | `0x1F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CuzzEnable` | `0x1FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CuzzGetCustomSchedulerInterface` | `0x1FC0` | 139 | UnwindData |  |
| 5 | `CuzzGetPriority` | `0x2060` | 77 | UnwindData |  |
| 6 | `CuzzGetPriorityOfTask` | `0x20C0` | 51 | UnwindData |  |
| 7 | `CuzzGetRandomSeed` | `0x2100` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CuzzIsEnabled` | `0x22E0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CuzzSchedule` | `0x23F0` | 223 | UnwindData |  |
| 10 | `CuzzSetDebugLoweringPoint` | `0x25F0` | 64 | UnwindData |  |
| 11 | `CuzzSetDebugPriority` | `0x2640` | 55 | UnwindData |  |
| 12 | `CuzzSetFuzzingLevel` | `0x2680` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CuzzSetNumBlockedThreads` | `0x2700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `CuzzSetPriority` | `0x2710` | 99 | UnwindData |  |
| 15 | `CuzzSetRandomSeed` | `0x2780` | 7,526 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
