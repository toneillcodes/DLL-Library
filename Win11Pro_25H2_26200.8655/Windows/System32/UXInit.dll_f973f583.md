# Binary Specification: UXInit.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\UXInit.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f973f583719632a7007fd639ce5e610b6f6f15ed5cefe3ec072d6bd27b988cb9`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#412` |
| 13 | `ThemesOnEarlyCreateSession` | `0x1F30` | 49 | UnwindData |  |
| 8 | `ThemesOnTerminateSession` | `0x39F0` | 51 | UnwindData |  |
| 9 | `ThemesOnLogon` | `0x8760` | 154 | UnwindData |  |
| 3 | `ThemeUserLogoff` | `0x9EE0` | 75 | UnwindData |  |
| 4 | `ThemeUserLogon` | `0x9F40` | 95 | UnwindData |  |
| 7 | `ThemesOnCreateSession` | `0xF310` | 42 | UnwindData |  |
| 1 | `ThemeWatchForStart` | `0xF340` | 61 | UnwindData |  |
| 10 | `ThemesOnLogoff` | `0x11D40` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `ThemesOnDisconnect` | `0x11F00` | 19,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ThemeUserStartShell` | `0x16C60` | 25 | UnwindData |  |
| 6 | `ThemeUserTSReconnect` | `0x16C80` | 38 | UnwindData |  |
| 11 | `ThemesOnReconnect` | `0x16CB0` | 31 | UnwindData |  |
