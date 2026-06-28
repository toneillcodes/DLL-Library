# Binary Specification: thumbcache.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\thumbcache.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dd9045c3e924c57ff9ba660deec5735292f1928d66c4597356ec4dc95f2dee4c`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllGetClassObject` | `0x182C0` | 403 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x26DB0` | 45 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x26E10` | 72 | UnwindData |  |
| 4 | `GetProxyDllInfo` | `0x3A300` | 67,420 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
