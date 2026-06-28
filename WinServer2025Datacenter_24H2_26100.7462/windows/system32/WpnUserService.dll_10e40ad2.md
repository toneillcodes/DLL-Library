# Binary Specification: WpnUserService.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WpnUserService.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `10e40ad23189bc82d287591bf198eb1af88620e18a3c55d186c6f626ddfbc350`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xD9B0` | 70 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xDA00` | 232 | UnwindData |  |
| 3 | `ServiceMain` | `0xDB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SvchostPushServiceGlobals` | `0xDB90` | 12,801 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
