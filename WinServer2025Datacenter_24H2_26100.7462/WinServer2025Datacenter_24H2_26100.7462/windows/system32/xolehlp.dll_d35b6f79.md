# Binary Specification: xolehlp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\xolehlp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d35b6f7948c28f471307ee4c19a9159c43d9a7117f72bd758d4534cd110d0dc1`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `FreezeLocalTransactionManagers` | `0x23B0` | 506 | UnwindData |  |
| 4 | `GetDtcLocaleResourceHandle` | `0x2920` | 58 | UnwindData |  |
| 9 | `ThawLocalTransactionManagers` | `0x2960` | 78 | UnwindData |  |
| 5 | `DtcGetTransactionManager` | `0x2A40` | 108 | UnwindData |  |
| 7 | `DtcGetTransactionManagerC` | `0x2AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DtcGetTransactionManagerEx` | `0x2AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `DtcGetTransactionManagerExA` | `0x2AF0` | 327 | UnwindData |  |
| 11 | `DtcGetTransactionManagerExW` | `0x2C40` | 1,082 | UnwindData |  |
