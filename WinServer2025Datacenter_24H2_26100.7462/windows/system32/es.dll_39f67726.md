# Binary Specification: es.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\es.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `39f677260737efcc4ca9d17b72ba067e54bf282dd250ac578e26c0d6bdc3ed87`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `NotifyLogoffUser` | `0x12C10` | 32 | UnwindData |  |
| 6 | `NotifyLogonUser` | `0x13030` | 35 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x135F0` | 525 | UnwindData |  |
| 7 | `ServiceMain` | `0x22280` | 215 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x269C0` | 31,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `SvchostPushServiceGlobals` | `0x2E610` | 36,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `LCEControlServer` | `0x37300` | 134 | UnwindData |  |
