# Binary Specification: vfcuzz.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vfcuzz.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dc57aa53550d2e4113c89034aa4586e4b177bda439887d3671ff5973a93b2c2e`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `CuzzDumpDebuggingState` | `0x1300` | 3,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CuzzDisable` | `0x1FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CuzzEnable` | `0x1FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CuzzGetCustomSchedulerInterface` | `0x1FF0` | 139 | UnwindData |  |
| 5 | `CuzzGetPriority` | `0x2090` | 77 | UnwindData |  |
| 6 | `CuzzGetPriorityOfTask` | `0x20F0` | 51 | UnwindData |  |
| 7 | `CuzzGetRandomSeed` | `0x2130` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CuzzIsEnabled` | `0x2310` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CuzzSchedule` | `0x2420` | 223 | UnwindData |  |
| 10 | `CuzzSetDebugLoweringPoint` | `0x2620` | 64 | UnwindData |  |
| 11 | `CuzzSetDebugPriority` | `0x2670` | 55 | UnwindData |  |
| 12 | `CuzzSetFuzzingLevel` | `0x26B0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CuzzSetNumBlockedThreads` | `0x2730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `CuzzSetPriority` | `0x2740` | 99 | UnwindData |  |
| 15 | `CuzzSetRandomSeed` | `0x27B0` | 7,686 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
