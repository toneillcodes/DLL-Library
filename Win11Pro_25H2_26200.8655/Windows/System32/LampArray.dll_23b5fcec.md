# Binary Specification: LampArray.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\LampArray.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `23b5fcec2e27e187e1cb44a5d28fc8de072ef791b01249025b8b3f38d8431a28`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `RegisterLampArrayCallback` | `0x9E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `RegisterLampArrayStatusCallback` | `0x9E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `TrySetLampArrayWorkerThreadAffinityMask` | `0x9E30` | 164 | UnwindData |  |
| 4 | `UnregisterLampArrayCallback` | `0x9EE0` | 114 | UnwindData |  |
