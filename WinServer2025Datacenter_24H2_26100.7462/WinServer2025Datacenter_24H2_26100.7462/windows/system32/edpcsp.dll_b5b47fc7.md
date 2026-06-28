# Binary Specification: edpcsp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\edpcsp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b5b47fc77a3be1e69fd0567a8fd9d657ca2d7e85d36dcef651a492f36e06f559`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x9240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0x9260` | 239 | UnwindData |  |
| 1 | `CreateAllEdpTasks` | `0xE930` | 2,688 | UnwindData |  |
| 2 | `DeleteAllEdpTasks` | `0x10300` | 640 | UnwindData |  |
