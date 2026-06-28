# Binary Specification: capisp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\capisp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6cd8b3ed5ba9b342bd4261423c01c8ca7496a13238da5ef2c1e6f9673e319844`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CAPISysPrep_Generalize` | `0x1910` | 660 | UnwindData |  |
| 2 | `CryptoSysPrep_Clean` | `0x2350` | 308 | UnwindData |  |
| 3 | `CryptoSysPrep_Specialize` | `0x2490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CryptoSysPrep_Specialize_Clone` | `0x24A0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CryptoSysPrep_Specialize_Offline` | `0x2870` | 178 | UnwindData |  |
