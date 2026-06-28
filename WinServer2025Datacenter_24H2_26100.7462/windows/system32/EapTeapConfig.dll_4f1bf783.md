# Binary Specification: EapTeapConfig.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\EapTeapConfig.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4f1bf783d2b0938ab3a75a290a148e1f82eae7147d3c02e4ca4f49a62dea36d2`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EapPeerFreeMemory` | `0x4910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EapPeerGetNextPageGuid` | `0x4920` | 97 | UnwindData |  |
| 3 | `EapPeerConfigBlob2Xml` | `0x7460` | 58 | UnwindData |  |
| 4 | `EapPeerConfigXml2Blob` | `0x74A0` | 49 | UnwindData |  |
| 5 | `EapPeerCredentialsXml2Blob` | `0x74E0` | 78 | UnwindData |  |
| 6 | `EapPeerFreeErrorMemory` | `0x7540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `EapPeerGetMethodProperties` | `0x7550` | 127 | UnwindData |  |
| 8 | `EapPeerInvokeConfigUI` | `0x75E0` | 152 | UnwindData |  |
| 9 | `EapPeerInvokeInteractiveUI` | `0x7680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `EapPeerQueryInteractiveUIInputFields` | `0x7690` | 20 | UnwindData |  |
