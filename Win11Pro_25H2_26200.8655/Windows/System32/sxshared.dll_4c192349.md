# Binary Specification: sxshared.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sxshared.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4c19234930378ee7b19c8042ca12e51656fcfc2602a0298dee9001790f34b794`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `SxTracerGetThreadContextRetail` | `0x11A0` | 15 | UnwindData |  |
| 10 | `SxTracerShouldTrackFailure` | `0x1800` | 5,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x2EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x2F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2F30` | 127 | UnwindData |  |
| 7 | `SxTracerDebuggerBreak` | `0x2FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SxTracerGetThreadContextDebug` | `0x2FD0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetLastFailureAsHRESULT` | `0x33D0` | 150 | UnwindData |  |
| 6 | `HRESULTFromNTSTATUS` | `0x3470` | 124 | UnwindData |  |
| 11 | `Win32FromHRESULT` | `0x3610` | 311 | UnwindData |  |
| 12 | `Win32FromNTSTATUS` | `0x3750` | 59 | UnwindData |  |
