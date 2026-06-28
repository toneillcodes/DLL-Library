# Binary Specification: wpx.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wpx.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b61b0e0615a605a747749bdda6239501493b6a43285a10b5f16fe5764d8dcb1d`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WpxCreateConfig` | `0x8640` | 142 | UnwindData |  |
| 7 | `WpxSetLogger` | `0x9240` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `WpxSetScratchDirectory` | `0x97A0` | 227 | UnwindData |  |
| 4 | `WpxGetDeplSettings` | `0x37690` | 351 | UnwindData |  |
| 5 | `WpxResetDeplSettings` | `0x37800` | 243 | UnwindData |  |
| 6 | `WpxSetDeplSettings` | `0x37900` | 299 | UnwindData |  |
| 2 | `WpxCreateWriteOpt` | `0x599F0` | 175 | UnwindData |  |
| 3 | `WpxGetAnswerFileType` | `0x59BA0` | 982 | UnwindData |  |
