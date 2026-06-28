# Binary Specification: qdv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\qdv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `abc64a75e4eef49259bd1ec3f15c5aed9358cbdafab3d5a06d57bbdfc1e7a282`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x26C0` | 192 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x2790` | 135 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x2A50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2AB0` | 223 | UnwindData |  |
