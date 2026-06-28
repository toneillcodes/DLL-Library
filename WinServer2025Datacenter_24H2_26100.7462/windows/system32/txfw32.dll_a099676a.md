# Binary Specification: txfw32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\txfw32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a099676af62a85bed119072ddc0427178d181af0e6f427edb89371589c06c8dd`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `TxfGetThreadMiniVersionForCreate` | `0x1910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `TxfLogCreateFileReadContext` | `0x1930` | 344 | UnwindData |  |
| 3 | `TxfLogCreateRangeReadContext` | `0x1A90` | 29 | UnwindData |  |
| 4 | `TxfLogDestroyReadContext` | `0x1AC0` | 129 | UnwindData |  |
| 5 | `TxfLogReadRecords` | `0x1B50` | 404 | UnwindData |  |
| 6 | `TxfLogRecordGetFileName` | `0x1CF0` | 633 | UnwindData |  |
| 7 | `TxfLogRecordGetGenericType` | `0x1F70` | 130 | UnwindData |  |
| 8 | `TxfReadMetadataInfo` | `0x2000` | 29 | UnwindData |  |
| 9 | `TxfSetThreadMiniVersionForCreate` | `0x2030` | 0 | Indeterminate |  |
