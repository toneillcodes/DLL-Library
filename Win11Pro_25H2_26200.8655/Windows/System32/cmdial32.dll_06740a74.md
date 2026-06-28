# Binary Specification: cmdial32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cmdial32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `06740a74c1db771b287f34bd8ac7f2abee097273dadadabc3a7709be2755bcac`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AutoDialFunc` | `0x22C10` | 47 | UnwindData |  |
| 2 | `CmCustomDialDlg` | `0x22C50` | 1,064 | UnwindData |  |
| 3 | `CmCustomHangUp` | `0x23080` | 582 | UnwindData |  |
| 4 | `CmReConnect` | `0x232D0` | 312 | UnwindData |  |
| 5 | `GetCustomProperty` | `0x23580` | 563 | UnwindData |  |
| 6 | `InetDialHandler` | `0x237C0` | 47 | UnwindData |  |
| 7 | `RasCustomDeleteEntryNotify` | `0x23800` | 1,694 | UnwindData |  |
| 8 | `RasCustomDial` | `0x23EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `RasCustomDialDlg` | `0x23EC0` | 696 | UnwindData |  |
| 10 | `RasCustomEntryDlg` | `0x24180` | 405 | UnwindData |  |
| 11 | `RasCustomHangUp` | `0x24320` | 610 | UnwindData |  |
