# Binary Specification: WppRecorderUM.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WppRecorderUM.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `787e2f9351dfe39928ffd168e79217396ef8eea918312cb3ed05a5f01cd31614`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WppAutoLogGetDefaultHandle` | `0x7880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WppAutoLogStart` | `0x78A0` | 876 | UnwindData |  |
| 3 | `WppAutoLogStop` | `0x7C20` | 81 | UnwindData |  |
| 4 | `WppAutoLogTrace` | `0x7C80` | 469 | UnwindData |  |
| 5 | `imp_WppRecorderLogDumpLiveData` | `0x7E60` | 0 | Indeterminate |  |
