# Binary Specification: cabinet.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cabinet.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `074504cad602a2a69fceb0a4e62ba233525ad3114017948d2b7fa22b640046d5`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `FCICreate` | `0x1060` | 704 | UnwindData |  |
| 14 | `FCIDestroy` | `0x1330` | 102 | UnwindData |  |
| 13 | `FCIFlushCabinet` | `0x1B00` | 136 | UnwindData |  |
| 22 | `FDICopy` | `0x3EE0` | 699 | UnwindData |  |
| 3 | `Extract` | `0x7A70` | 417 | UnwindData |  |
| 23 | `FDIDestroy` | `0x7E10` | 180 | UnwindData |  |
| 11 | `FCIAddFile` | `0xB8E0` | 349 | UnwindData |  |
| 33 | `Compress` | `0x11C40` | 43 | UnwindData |  |
| 43 | `Decompress` | `0x11CB0` | 40 | UnwindData |  |
| 21 | `FDIIsCabinet` | `0x12D00` | 232 | UnwindData |  |
| 20 | `FDICreate` | `0x12DF0` | 268 | UnwindData |  |
| 40 | `CreateDecompressor` | `0x139E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `CreateCompressor` | `0x139F0` | 2,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `CloseDecompressor` | `0x14570` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `CloseCompressor` | `0x145B0` | 7,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetVersion` | `0x16180` | 152 | UnwindData |  |
| 1 | `GetDllVersion` | `0x16220` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DeleteExtractedFiles` | `0x163D0` | 187 | UnwindData |  |
| 24 | `FDITruncateCabinet` | `0x16560` | 467 | UnwindData |  |
| 12 | `FCIFlushFolder` | `0x177E0` | 63 | UnwindData |  |
| 32 | `QueryCompressorInformation` | `0x18140` | 23 | UnwindData |  |
| 42 | `QueryDecompressorInformation` | `0x181F0` | 20 | UnwindData |  |
| 34 | `ResetCompressor` | `0x18210` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `ResetDecompressor` | `0x18290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `SetCompressorInformation` | `0x182A0` | 23 | UnwindData |  |
| 41 | `SetDecompressorInformation` | `0x18350` | 20 | UnwindData |  |
