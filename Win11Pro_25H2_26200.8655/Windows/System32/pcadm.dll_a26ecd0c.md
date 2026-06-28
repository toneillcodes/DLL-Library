# Binary Specification: pcadm.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\pcadm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a26ecd0c415589a1a0a7ade5137b4aea3ed922467ac1f5f50a097962938ebb50`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `WdiHandleInstance` | `0x2EF0` | 65 | UnwindData |  |
| 7 | `WdiDiagnosticModuleMain` | `0xE250` | 100 | UnwindData |  |
| 8 | `WdiGetDiagnosticModuleInterfaceVersion` | `0xE680` | 7,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `PcaPldAddGenDbRecord` | `0x10470` | 1,344 | UnwindData |  |
| 5 | `PcaPldRecordAppLaunch` | `0x109C0` | 227 | UnwindData |  |
| 2 | `PcaPldGetAppsLaunchedWithinPeriod` | `0x18100` | 853 | UnwindData |  |
| 3 | `PcaPldGetValueInDictionary` | `0x18460` | 1,128 | UnwindData |  |
| 4 | `PcaPldParseGenDbRecord` | `0x188D0` | 756 | UnwindData |  |
| 6 | `PcaPldSetValueInDictionary` | `0x18BD0` | 1,411 | UnwindData |  |
