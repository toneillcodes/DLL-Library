# Binary Specification: shimgvw.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\shimgvw.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2f172a9d7af0aca77a1649029cc4482df63e2bb956fb6bcd91c689b42a8d9b50`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ImageView_Fullscreen` | `0x4B40` | 217 | UnwindData |  |
| 2 | `ImageView_FullscreenA` | `0x4C20` | 131 | UnwindData |  |
| 3 | `ImageView_FullscreenW` | `0x4CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `imageview_fullscreenW` | `0x4CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ImageView_PrintTo` | `0x4CC0` | 628 | UnwindData |  |
| 5 | `ImageView_PrintToA` | `0x4F40` | 131 | UnwindData |  |
| 6 | `ImageView_PrintToW` | `0x4FD0` | 4,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllCanUnloadNow` | `0x6030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllGetClassObject` | `0x6050` | 151 | UnwindData |  |
