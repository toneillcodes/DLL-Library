# Binary Specification: EhStorShell.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\EhStorShell.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `71a3abc06fb16c16a907554d2d7d77b0703a847c463590ee2c2fa335090da8c2`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1790` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1EA0` | 42 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x8280` | 12,220 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x8280` | 12,220 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
