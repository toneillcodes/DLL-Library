# Binary Specification: version.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\version.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cea99f212af557a9613150c5509631403ed0f05f5d9a06ac42039bd59b40e39a`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `VerLanguageNameA` | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.VerLanguageNameA` |
| 15 | `VerLanguageNameW` | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.VerLanguageNameW` |
| 8 | `GetFileVersionInfoSizeW` | `0x1010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `VerQueryValueW` | `0x1030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `GetFileVersionInfoW` | `0x1050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetFileVersionInfoSizeExW` | `0x1070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetFileVersionInfoExW` | `0x1090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetFileVersionInfoSizeA` | `0x10B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `VerQueryValueA` | `0x10D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GetFileVersionInfoA` | `0x10F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `GetFileVersionInfoByHandle` | `0x1110` | 2,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetFileVersionInfoExA` | `0x1AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetFileVersionInfoSizeExA` | `0x1AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `VerFindFileA` | `0x1AF0` | 67 | UnwindData |  |
| 12 | `VerInstallFileA` | `0x1B40` | 1,053 | UnwindData |  |
| 11 | `VerFindFileW` | `0x2160` | 67 | UnwindData |  |
| 13 | `VerInstallFileW` | `0x2EA0` | 1,685 | UnwindData |  |
