# Binary Specification: Chakrathunk.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Chakrathunk.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dbac1441eb6da35f76aed21c0c6ac659bc28019efad03013a2e1863fa802d9bd`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `JsThunk_AllocateData` | `0x2BA0` | 869 | UnwindData |  |
| 2 | `JsThunk_Cleanup` | `0x2F10` | 83 | UnwindData |  |
| 3 | `JsThunk_CleanupDefer` | `0x2F70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `JsThunk_CleanupFinish` | `0x2FB0` | 95 | UnwindData |  |
| 5 | `JsThunk_DataToCode` | `0x3020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `JsThunk_GetSize` | `0x3040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `JsThunk_InitData` | `0x3050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `JsThunk_Is` | `0x3080` | 192 | UnwindData |  |
