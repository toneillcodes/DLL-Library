# Binary Specification: dwminit.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dwminit.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `94cbc4b167ed513539c3d665585818d7a2569643eb1886e5ee18f35d613c03ff`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DwmpCreateSessionProcess` | `0xD8A0` | 430 | UnwindData |  |
| 2 | `DwmpIsInitialSessionInteractive` | `0xDA60` | 130 | UnwindData |  |
| 3 | `DwmpNotifyUserLogoff` | `0xDAF0` | 128 | UnwindData |  |
| 4 | `DwmpNotifyUserLogon` | `0xDB80` | 903 | UnwindData |  |
| 5 | `DwmpShutdownWinlogonMouseThread` | `0xDF10` | 251 | UnwindData |  |
| 6 | `DwmpStartWinlogonMouseThread` | `0xE020` | 501 | UnwindData |  |
| 7 | `DwmpTerminateSessionProcess` | `0xE220` | 801 | UnwindData |  |
