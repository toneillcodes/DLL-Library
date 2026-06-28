# Binary Specification: ttdplm.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ttdplm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4a11fed9d973b2ea4857785738ff2a77e5e8c8f3222b006a5bbb39d201569403`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateModernAppToDelete` | `0x5D60` | 58 | UnwindData |  |
| 2 | `CreateModernAppToTrace` | `0x5DA0` | 193 | UnwindData |  |
| 3 | `GetMaxPackageNameLength` | `0x5E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetPackageFromPid` | `0x5E80` | 159 | UnwindData |  |
| 5 | `SetPermisionsForFolder` | `0x5F30` | 114 | UnwindData |  |
