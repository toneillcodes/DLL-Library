# Binary Specification: GraphicsPerfSvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\GraphicsPerfSvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dda63129452af817e90e6215d29a2b84552a072ddad9150c41949363b464f66d`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0xDA30` | 84 | UnwindData |  |
| 2 | `ServiceMain` | `0x11440` | 1,168 | UnwindData |  |
| 3 | `SvchostPushServiceGlobalsEx` | `0x118E0` | 109,587 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
