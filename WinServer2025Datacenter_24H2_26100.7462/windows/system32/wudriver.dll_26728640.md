# Binary Specification: wudriver.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wudriver.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `267286408414481d93dc73011969908b602c9c73dbb7f757f2d65642963de6a6`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DetFilesDownloaded` | `0xD830` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `LogDriverNotFound` | `0xD830` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `QueryDetectionFiles` | `0xD870` | 4,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CancelCDMOperation` | `0xEA50` | 36 | UnwindData |  |
| 2 | `CloseCDMContext` | `0xEA80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DownloadIsInternetAvailable` | `0xEAC0` | 73 | UnwindData |  |
| 5 | `DownloadUpdatedFiles` | `0xEB10` | 250 | UnwindData |  |
| 6 | `FindMatchingDriver` | `0xEC10` | 213 | UnwindData |  |
| 8 | `OpenCDMContext` | `0xECF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `OpenCDMContextEx` | `0xED00` | 361 | UnwindData |  |
