# Binary Specification: atlthunk.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\atlthunk.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `256a6238584780958eb0372f1594e533cc67f1c0ba29223ce490b671611ed3d5`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AtlThunk_AllocateData` | `0x1430` | 635 | UnwindData |  |
| 3 | `AtlThunk_FreeData` | `0x1A40` | 114 | UnwindData |  |
| 2 | `AtlThunk_DataToCode` | `0x1AC0` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `AtlThunk_InitData` | `0x2110` | 6,470 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
