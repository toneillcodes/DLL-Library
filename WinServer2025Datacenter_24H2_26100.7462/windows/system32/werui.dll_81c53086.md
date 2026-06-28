# Binary Specification: werui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\werui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `81c53086adb82d77f247ccbfa3f40241abf2ef8b838dbb7e0d0ff256a8dfddc9`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `WerUIpCheckWindow` | `0x36D0` | 459 | UnwindData |  |
| 14 | `WerUIpDefSubclassProc` | `0x38B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `WerUIpHeadlessOrImersive` | `0x38D0` | 71 | UnwindData |  |
| 16 | `WerUIpRemoveWindowSubclass` | `0x3920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `WerUIpSetWindowSubclass` | `0x3940` | 45 | UnwindData |  |
| 18 | `WerUIpTaskDialogIndirect` | `0x3980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `WerUIpUIHandleWERWindowMsg` | `0x39A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WerUICreate` | `0x39B0` | 272 | UnwindData |  |
| 3 | `WerUIDelete` | `0x3AD0` | 86 | UnwindData |  |
| 4 | `WerUIGetUserSelection` | `0x3B30` | 95 | UnwindData |  |
| 5 | `WerUIPromptForSecondLevel` | `0x3BA0` | 95 | UnwindData |  |
| 6 | `WerUIPromptUser` | `0x3C10` | 473 | UnwindData |  |
| 7 | `WerUIShowUpsell` | `0x3DF0` | 85 | UnwindData |  |
| 8 | `WerUIStart` | `0x3E50` | 95 | UnwindData |  |
| 9 | `WerUITerminate` | `0x3EC0` | 82 | UnwindData |  |
| 10 | `WerUIUpdateStateProgress` | `0x3F20` | 144 | UnwindData |  |
| 11 | `WerUIUpdateUIForState` | `0x3FC0` | 144 | UnwindData |  |
| 12 | `WerUIWaitForUserAction` | `0x4060` | 77 | UnwindData |  |
| 1 | `WerUIReportSilentProcessExit` | `0xFFC0` | 655 | UnwindData |  |
