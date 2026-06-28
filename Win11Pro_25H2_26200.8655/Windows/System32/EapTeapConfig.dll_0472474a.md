# Binary Specification: EapTeapConfig.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\EapTeapConfig.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0472474a10d753ba5828d0fbde897a43fd0623482e5a367db4e0f894fa44719a`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EapPeerFreeMemory` | `0x4910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EapPeerGetNextPageGuid` | `0x4920` | 97 | UnwindData |  |
| 3 | `EapPeerConfigBlob2Xml` | `0x7480` | 58 | UnwindData |  |
| 4 | `EapPeerConfigXml2Blob` | `0x74C0` | 49 | UnwindData |  |
| 5 | `EapPeerCredentialsXml2Blob` | `0x7500` | 78 | UnwindData |  |
| 6 | `EapPeerFreeErrorMemory` | `0x7560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `EapPeerGetMethodProperties` | `0x7570` | 127 | UnwindData |  |
| 8 | `EapPeerInvokeConfigUI` | `0x7600` | 152 | UnwindData |  |
| 9 | `EapPeerInvokeInteractiveUI` | `0x76A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `EapPeerQueryInteractiveUIInputFields` | `0x76B0` | 20 | UnwindData |  |
