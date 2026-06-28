# Binary Specification: wudriver.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wudriver.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2d3da0ce8e6166736f60ddd8d39e9fd7d1447929359dc647fb95fe5af01baafd`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DetFilesDownloaded` | `0x66A0` | 45,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `LogDriverNotFound` | `0x66A0` | 45,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `QueryDetectionFiles` | `0x11800` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CancelCDMOperation` | `0x12680` | 36 | UnwindData |  |
| 2 | `CloseCDMContext` | `0x126B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DownloadIsInternetAvailable` | `0x126F0` | 73 | UnwindData |  |
| 5 | `DownloadUpdatedFiles` | `0x12740` | 250 | UnwindData |  |
| 6 | `FindMatchingDriver` | `0x12840` | 213 | UnwindData |  |
| 8 | `OpenCDMContext` | `0x12920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `OpenCDMContextEx` | `0x12930` | 361 | UnwindData |  |
