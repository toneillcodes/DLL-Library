# Binary Specification: sxshared.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sxshared.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `358163e18195b114111f621c3dd5679c82d71059e173a75af0fb5f9168adc735`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `SxTracerGetThreadContextRetail` | `0x1010` | 15 | UnwindData |  |
| 10 | `SxTracerShouldTrackFailure` | `0x1670` | 5,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x2D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x2D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2D80` | 127 | UnwindData |  |
| 7 | `SxTracerDebuggerBreak` | `0x2E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SxTracerGetThreadContextDebug` | `0x2E20` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetLastFailureAsHRESULT` | `0x3180` | 150 | UnwindData |  |
| 6 | `HRESULTFromNTSTATUS` | `0x3220` | 124 | UnwindData |  |
| 11 | `Win32FromHRESULT` | `0x33C0` | 311 | UnwindData |  |
| 12 | `Win32FromNTSTATUS` | `0x3500` | 59 | UnwindData |  |
