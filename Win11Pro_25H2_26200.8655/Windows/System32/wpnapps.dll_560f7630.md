# Binary Specification: wpnapps.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wpnapps.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `560f7630ef4cd37901b9ed011b3c10fbac21a9f24b8c0304e6ba5aee822d9564`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x29E80` | 556 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x2E8D0` | 665 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x4A070` | 513,308 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
