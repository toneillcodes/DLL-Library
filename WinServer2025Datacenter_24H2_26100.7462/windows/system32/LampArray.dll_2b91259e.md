# Binary Specification: LampArray.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\LampArray.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2b91259ee4c167c3a27f027f11fd9a26a88a62bf744922262e71c321cc4f4d16`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `RegisterLampArrayCallback` | `0xA770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `RegisterLampArrayStatusCallback` | `0xA780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `TrySetLampArrayWorkerThreadAffinityMask` | `0xA790` | 164 | UnwindData |  |
| 4 | `UnregisterLampArrayCallback` | `0xA840` | 114 | UnwindData |  |
