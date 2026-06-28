# Binary Specification: comdlg32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\comdlg32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `da82862256aa1ebe96d0f98e5375d79a5bc61a6471ebe74d9ccf34ba0c8051aa`
* **Total Exported Functions:** 30

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 100 | *Ordinal Only* | `0x28750` | 1,258 | UnwindData |  |
| 112 | `GetFileTitleW` | `0x2CFD0` | 252 | UnwindData |  |
| 108 | `DllGetClassObject` | `0x2E570` | 26 | UnwindData |  |
| 107 | `DllCanUnloadNow` | `0x2EF80` | 106,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `ChooseColorA` | `0x48F40` | 485 | UnwindData |  |
| 103 | `ChooseColorW` | `0x49130` | 97 | UnwindData |  |
| 127 | `WantArrows` | `0x4B650` | 414 | UnwindData |  |
| 106 | `CommDlgExtendedError` | `0x4DA60` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `LoadAlterBitmap` | `0x4DBF0` | 424 | UnwindData |  |
| 126 | `Ssync_ANSI_UNICODE_Struct_For_WOW` | `0x4DDA0` | 263 | UnwindData |  |
| 111 | `GetFileTitleA` | `0x52380` | 477 | UnwindData |  |
| 113 | `GetOpenFileNameA` | `0x527E0` | 43 | UnwindData |  |
| 114 | `GetOpenFileNameW` | `0x52820` | 138 | UnwindData |  |
| 115 | `GetSaveFileNameA` | `0x52900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `GetSaveFileNameW` | `0x52920` | 121 | UnwindData |  |
| 128 | `dwLBSubclass` | `0x57270` | 209 | UnwindData |  |
| 129 | `dwOKSubclass` | `0x57350` | 200 | UnwindData |  |
| 109 | `FindTextA` | `0x57A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `FindTextW` | `0x57A70` | 1,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `ReplaceTextA` | `0x58160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `ReplaceTextW` | `0x58180` | 2,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `ChooseFontA` | `0x58B40` | 717 | UnwindData |  |
| 105 | `ChooseFontW` | `0x58E20` | 135 | UnwindData |  |
| 118 | `PageSetupDlgA` | `0x5CF90` | 350 | UnwindData |  |
| 119 | `PageSetupDlgW` | `0x5D100` | 123 | UnwindData |  |
| 120 | `PrintDlgA` | `0x5DC00` | 164 | UnwindData |  |
| 123 | `PrintDlgW` | `0x5DCB0` | 97 | UnwindData |  |
| 101 | *Ordinal Only* | `0x8A550` | 259 | UnwindData |  |
| 121 | `PrintDlgExA` | `0x94AE0` | 227 | UnwindData |  |
| 122 | `PrintDlgExW` | `0x94BD0` | 95 | UnwindData |  |
