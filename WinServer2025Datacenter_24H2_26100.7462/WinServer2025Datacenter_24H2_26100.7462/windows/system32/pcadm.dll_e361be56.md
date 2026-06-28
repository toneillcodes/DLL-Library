# Binary Specification: pcadm.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\pcadm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e361be562fcf00238787f84af4e43db65260a89409c7ac48fcbe1edaaf7f9686`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `WdiHandleInstance` | `0x2F20` | 65 | UnwindData |  |
| 7 | `WdiDiagnosticModuleMain` | `0xE330` | 100 | UnwindData |  |
| 8 | `WdiGetDiagnosticModuleInterfaceVersion` | `0xE760` | 8,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `PcaPldAddGenDbRecord` | `0x106D0` | 1,344 | UnwindData |  |
| 5 | `PcaPldRecordAppLaunch` | `0x10C20` | 227 | UnwindData |  |
| 2 | `PcaPldGetAppsLaunchedWithinPeriod` | `0x183B0` | 853 | UnwindData |  |
| 3 | `PcaPldGetValueInDictionary` | `0x18710` | 1,128 | UnwindData |  |
| 4 | `PcaPldParseGenDbRecord` | `0x18B80` | 756 | UnwindData |  |
| 6 | `PcaPldSetValueInDictionary` | `0x18E80` | 1,411 | UnwindData |  |
