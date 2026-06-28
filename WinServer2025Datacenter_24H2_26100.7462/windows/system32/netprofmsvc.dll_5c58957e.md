# Binary Specification: netprofmsvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\netprofmsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5c58957e27990606058fa4dcdcf1aedadd15115c64d0003501c0ae5823243fb1`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllMain` | `0xA1CF0` | 407 | UnwindData |  |
| 1 | `ServiceMain` | `0xA3780` | 422 | UnwindData |  |
| 2 | `SvchostPushServiceGlobalsEx` | `0xA3F80` | 703,867 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
