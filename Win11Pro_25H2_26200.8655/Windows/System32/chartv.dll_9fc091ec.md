# Binary Specification: chartv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\chartv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9fc091ec69c4d2c219923d11663c5a0f48ac68c54690a9562b2482943bf8e68f`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CvCloseDataSource` | `0x151E0` | 55 | UnwindData |  |
| 2 | `CvCreateDataSource` | `0x15220` | 434 | UnwindData |  |
| 3 | `CvGetData` | `0x153E0` | 383 | UnwindData |  |
| 4 | `CvGetDataSourceName` | `0x15570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CvInitialize` | `0x15580` | 253 | UnwindData |  |
| 6 | `CvSetData` | `0x15690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CvSetDataSourceName` | `0x156A0` | 419 | UnwindData |  |
| 8 | `CvUninitialize` | `0x15850` | 31 | UnwindData |  |
