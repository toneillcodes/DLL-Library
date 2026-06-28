# Binary Specification: mprext.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mprext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7c972d7cb5bdb4216497cfd9950b80329cefc90b6aca195c5b63bb755a62bbd4`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DoBroadcastSystemMessageWorker` | `0x1590` | 210 | UnwindData |  |
| 2 | `DoCommandLinePromptWorker` | `0x1670` | 76 | UnwindData |  |
| 3 | `DoPasswordDialogWorker` | `0x16D0` | 303 | UnwindData |  |
| 4 | `DoProfileErrorDialogWorker` | `0x1810` | 663 | UnwindData |  |
| 5 | `ShowReconnectDialogEndWorker` | `0x1DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ShowReconnectDialogUIWorker` | `0x1DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ShowReconnectDialogWorker` | `0x1E10` | 105 | UnwindData |  |
| 8 | `WNetConnectionDialog1WWorker` | `0x1F30` | 151 | UnwindData |  |
| 9 | `WNetConnectionDialogWorker` | `0x1FD0` | 90 | UnwindData |  |
| 10 | `WNetDisconnectDialog1WWorker` | `0x2030` | 110 | UnwindData |  |
| 11 | `WNetDisconnectDialogWorker` | `0x20B0` | 0 | Indeterminate |  |
