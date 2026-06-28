# Binary Specification: winprint.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\spool\prtprocs\x64\winprint.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a569deb213223dcf2c46c72b1b8516e7efe55aa196a98dadfbda987f392f0f71`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `GetPrintProcessorCapabilities` | `0x1010` | 58 | UnwindData |  |
| 4 | `EnumPrintProcessorDatatypesW` | `0x1340` | 73 | UnwindData |  |
| 3 | `DllMain` | `0x1850` | 6,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `ClosePrintProcessor` | `0x31F0` | 420 | UnwindData |  |
| 2 | `ControlPrintProcessor` | `0x33A0` | 155 | UnwindData |  |
| 6 | `OpenPrintProcessor` | `0x3650` | 1,328 | UnwindData |  |
| 7 | `PrintDocumentOnPrintProcessor` | `0x6970` | 140 | UnwindData |  |
