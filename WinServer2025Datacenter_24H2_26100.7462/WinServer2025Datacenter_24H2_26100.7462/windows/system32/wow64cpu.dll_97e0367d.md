# Binary Specification: wow64cpu.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wow64cpu.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `97e0367de5e78a591982538f517a0dc9f3c3b554c3cff07c69014b71ba18d7c0`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `BTCpuSetContext` | `0x1010` | 230 | UnwindData |  |
| 2 | `BTCpuGetContext` | `0x1100` | 184 | UnwindData |  |
| 1 | `BTCpuGetBopCode` | `0x11C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `BTCpuResetToConsistentState` | `0x11F0` | 27 | UnwindData |  |
| 3 | `BTCpuProcessInit` | `0x1310` | 282 | UnwindData |  |
| 7 | `BTCpuThreadInit` | `0x1430` | 99 | UnwindData |  |
| 6 | `BTCpuSimulate` | `0x1780` | 19 | UnwindData |  |
| 8 | `BTCpuTurboThunkControl` | `0x17A0` | 244 | UnwindData |  |
| 10 | `TurboDispatchJumpAddressStart` | `0x1A65` | 9 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `TurboDispatchJumpAddressEnd` | `0x1A6E` | 0 | Indeterminate |  |
