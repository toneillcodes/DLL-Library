# Binary Specification: comdlg32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\comdlg32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `277f03b537f9c808f573d29ae6089c1e13b61531329c25314a4513c93f5be67c`
* **Total Exported Functions:** 30

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 100 | *Ordinal Only* | `0x29A50` | 1,258 | UnwindData |  |
| 112 | `GetFileTitleW` | `0x2DE70` | 252 | UnwindData |  |
| 108 | `DllGetClassObject` | `0x2F030` | 26 | UnwindData |  |
| 107 | `DllCanUnloadNow` | `0x2FBD0` | 100,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `ChooseColorA` | `0x483D0` | 485 | UnwindData |  |
| 103 | `ChooseColorW` | `0x485C0` | 97 | UnwindData |  |
| 127 | `WantArrows` | `0x4AAE0` | 414 | UnwindData |  |
| 106 | `CommDlgExtendedError` | `0x4CEF0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `LoadAlterBitmap` | `0x4D080` | 424 | UnwindData |  |
| 126 | `Ssync_ANSI_UNICODE_Struct_For_WOW` | `0x4D230` | 263 | UnwindData |  |
| 111 | `GetFileTitleA` | `0x51810` | 477 | UnwindData |  |
| 113 | `GetOpenFileNameA` | `0x51C70` | 43 | UnwindData |  |
| 114 | `GetOpenFileNameW` | `0x51CB0` | 138 | UnwindData |  |
| 115 | `GetSaveFileNameA` | `0x51D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `GetSaveFileNameW` | `0x51DB0` | 121 | UnwindData |  |
| 128 | `dwLBSubclass` | `0x56700` | 209 | UnwindData |  |
| 129 | `dwOKSubclass` | `0x567E0` | 200 | UnwindData |  |
| 109 | `FindTextA` | `0x56EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `FindTextW` | `0x56F00` | 1,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `ReplaceTextA` | `0x575F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `ReplaceTextW` | `0x57610` | 2,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `ChooseFontA` | `0x57FD0` | 717 | UnwindData |  |
| 105 | `ChooseFontW` | `0x582B0` | 135 | UnwindData |  |
| 118 | `PageSetupDlgA` | `0x5C420` | 350 | UnwindData |  |
| 119 | `PageSetupDlgW` | `0x5C590` | 123 | UnwindData |  |
| 120 | `PrintDlgA` | `0x5D090` | 164 | UnwindData |  |
| 123 | `PrintDlgW` | `0x5D140` | 97 | UnwindData |  |
| 101 | *Ordinal Only* | `0x876D0` | 259 | UnwindData |  |
| 121 | `PrintDlgExA` | `0x91C40` | 227 | UnwindData |  |
| 122 | `PrintDlgExW` | `0x91D30` | 95 | UnwindData |  |
