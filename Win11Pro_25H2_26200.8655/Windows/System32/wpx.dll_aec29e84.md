# Binary Specification: wpx.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wpx.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `aec29e8441f8f95feda4258edfc42768cb33b682ff3eb8954b45c1fe09c8a384`
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
| 2 | `WpxCreateWriteOpt` | `0x59A00` | 175 | UnwindData |  |
| 3 | `WpxGetAnswerFileType` | `0x59BB0` | 982 | UnwindData |  |
