# Binary Specification: WppRecorderUM.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WppRecorderUM.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9fe62dc2504da1b9e6fe7cdf1cd86cc90fc7fe67faad6ade7470b8bba7004a86`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WppAutoLogGetDefaultHandle` | `0x7890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WppAutoLogStart` | `0x78B0` | 876 | UnwindData |  |
| 3 | `WppAutoLogStop` | `0x7C30` | 81 | UnwindData |  |
| 4 | `WppAutoLogTrace` | `0x7C90` | 469 | UnwindData |  |
| 5 | `imp_WppRecorderLogDumpLiveData` | `0x7E70` | 0 | Indeterminate |  |
