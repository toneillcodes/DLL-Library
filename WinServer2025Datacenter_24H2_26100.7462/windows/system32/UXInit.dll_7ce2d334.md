# Binary Specification: UXInit.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\UXInit.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7ce2d334dd28c351c5bc9c1d2be7c265bf9ca643272cb43c27a966a7be88470e`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#412` |
| 7 | `ThemesOnCreateSession` | `0x20F0` | 42 | UnwindData |  |
| 1 | `ThemeWatchForStart` | `0x2120` | 61 | UnwindData |  |
| 4 | `ThemeUserLogon` | `0x8980` | 95 | UnwindData |  |
| 3 | `ThemeUserLogoff` | `0x89F0` | 75 | UnwindData |  |
| 8 | `ThemesOnTerminateSession` | `0x8A50` | 51 | UnwindData |  |
| 9 | `ThemesOnLogon` | `0x98A0` | 154 | UnwindData |  |
| 13 | `ThemesOnEarlyCreateSession` | `0xD8E0` | 49 | UnwindData |  |
| 10 | `ThemesOnLogoff` | `0x11D80` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `ThemesOnDisconnect` | `0x11EC0` | 12,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ThemeUserStartShell` | `0x14EA0` | 25 | UnwindData |  |
| 6 | `ThemeUserTSReconnect` | `0x14EC0` | 22 | UnwindData |  |
| 11 | `ThemesOnReconnect` | `0x14EE0` | 12,620 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
