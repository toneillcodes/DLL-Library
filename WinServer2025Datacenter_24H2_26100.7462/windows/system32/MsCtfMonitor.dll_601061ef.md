# Binary Specification: MsCtfMonitor.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MsCtfMonitor.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `601061efbb85b10bdb9fdf322a3ce31f3a4359417157f5e7e9f692b31f64ae2d`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x9BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x9BD0` | 248 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x9CD0` | 538 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x9EF0` | 340 | UnwindData |  |
| 5 | `DoMsCtfMonitor` | `0xA9B0` | 2,175 | UnwindData |  |
| 6 | `InitLocalMsCtfMonitor` | `0xB480` | 220 | UnwindData |  |
| 7 | `UninitLocalMsCtfMonitor` | `0xB570` | 143 | UnwindData |  |
