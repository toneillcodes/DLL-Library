# Binary Specification: pcacli.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\pcacli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2f4278ec60db9b20a8093dd12ca85aaed806cf98f7af88c33a38b603c2861dbb`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `PcaNotifyMsiCustomAction` | `0x12F0` | 359 | UnwindData |  |
| 11 | `PcaSendToService` | `0x1460` | 1,180 | UnwindData |  |
| 7 | `PcaMonitorProcess` | `0x1C90` | 1,040 | UnwindData |  |
| 5 | `PcaIsPcaDisabled` | `0x2800` | 208 | UnwindData |  |
| 12 | `PcaMonitorProcess2` | `0x7120` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `PcaNotifyMsiInstall` | `0x71C0` | 312 | UnwindData |  |
| 1 | `PcaApiSamplingSetValue` | `0x82D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PcaApiSamplingStop` | `0x82D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `PcaApiSamplingStart` | `0x82E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PcaGetFileInfoFromPath` | `0x82F0` | 446 | UnwindData |  |
| 6 | `PcaLinkChildProcessToParent` | `0x84C0` | 344 | UnwindData |  |
| 10 | `PcaNotifyStatusIcon` | `0x8620` | 69 | UnwindData |  |
