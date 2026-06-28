# Binary Specification: GraphicsPerfSvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\GraphicsPerfSvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `74065031927c093f9c677e67584889348d963ffdf347703eee62b7b607f3a751`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllMain` | `0xDB60` | 84 | UnwindData |  |
| 2 | `ServiceMain` | `0x11550` | 1,168 | UnwindData |  |
| 3 | `SvchostPushServiceGlobalsEx` | `0x119F0` | 112,611 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
