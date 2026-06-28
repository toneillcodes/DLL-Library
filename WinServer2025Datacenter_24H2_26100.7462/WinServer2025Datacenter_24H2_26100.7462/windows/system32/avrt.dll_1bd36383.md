# Binary Specification: avrt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\avrt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1bd363830b00993bdb1f2cdeae0f149f461ed1679acbeca3cfb70354d3a848de`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `AvSetMmThreadPriority` | `0x1010` | 367 | UnwindData |  |
| 19 | `AvTaskIndexYieldCancel` | `0x1190` | 20 | UnwindData |  |
| 17 | `AvSetMultimediaMode` | `0x1240` | 46 | UnwindData |  |
| 20 | `AvThreadOpenTaskIndex` | `0x1300` | 78 | UnwindData |  |
| 2 | `AvQuerySystemResponsiveness` | `0x1360` | 105 | UnwindData |  |
| 18 | `AvTaskIndexYield` | `0x1490` | 52 | UnwindData |  |
| 14 | `AvSetMmThreadCharacteristicsA` | `0x1550` | 38 | UnwindData |  |
| 15 | `AvSetMmThreadCharacteristicsW` | `0x16C0` | 38 | UnwindData |  |
| 4 | `AvRevertMmThreadCharacteristics` | `0x1C60` | 48 | UnwindData |  |
| 1 | `AvCreateTaskIndex` | `0x1F30` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `AvRtCreateThreadOrderingGroup` | `0x2390` | 29 | UnwindData |  |
| 6 | `AvRtCreateThreadOrderingGroupExA` | `0x2390` | 29 | UnwindData |  |
| 7 | `AvRtCreateThreadOrderingGroupExW` | `0x2390` | 29 | UnwindData |  |
| 8 | `AvRtDeleteThreadOrderingGroup` | `0x2390` | 29 | UnwindData |  |
| 9 | `AvRtJoinThreadOrderingGroup` | `0x2390` | 29 | UnwindData |  |
| 10 | `AvRtLeaveThreadOrderingGroup` | `0x2390` | 29 | UnwindData |  |
| 11 | `AvRtWaitOnThreadOrderingGroup` | `0x2390` | 29 | UnwindData |  |
| 3 | `AvQueryTaskIndexValue` | `0x23C0` | 53 | UnwindData |  |
| 12 | `AvSetMmMaxThreadCharacteristicsA` | `0x2400` | 34 | UnwindData |  |
| 13 | `AvSetMmMaxThreadCharacteristicsW` | `0x2430` | 34 | UnwindData |  |
