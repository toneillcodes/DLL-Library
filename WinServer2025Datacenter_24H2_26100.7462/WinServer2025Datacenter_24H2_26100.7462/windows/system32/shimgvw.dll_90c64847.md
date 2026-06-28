# Binary Specification: shimgvw.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\shimgvw.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `90c64847f3620b0065a9ec2eaaee4042a157a417f49bdd05e5dc74cccf9cc793`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ImageView_Fullscreen` | `0x4B30` | 217 | UnwindData |  |
| 2 | `ImageView_FullscreenA` | `0x4C10` | 131 | UnwindData |  |
| 3 | `ImageView_FullscreenW` | `0x4CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `imageview_fullscreenW` | `0x4CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ImageView_PrintTo` | `0x4CB0` | 628 | UnwindData |  |
| 5 | `ImageView_PrintToA` | `0x4F30` | 131 | UnwindData |  |
| 6 | `ImageView_PrintToW` | `0x4FC0` | 4,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllCanUnloadNow` | `0x6020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllGetClassObject` | `0x6040` | 151 | UnwindData |  |
