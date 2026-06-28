# Binary Specification: zipcontainer.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\zipcontainer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `96745e6ef41977923986ced213601a4d299d2220d5525b7a8b0100f98636cc17`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateFileStream` | `0xC180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ZipContainerCreateArchiveOnFile` | `0xC190` | 454 | UnwindData |  |
| 3 | `ZipContainerInitialize` | `0xC360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ZipContainerUninitialize` | `0xC370` | 13,735 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
