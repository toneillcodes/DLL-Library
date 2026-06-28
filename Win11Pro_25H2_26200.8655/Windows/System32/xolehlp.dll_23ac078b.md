# Binary Specification: xolehlp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\xolehlp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `23ac078b48d15eaf33c95c8451b2fb9e8663eb031e41694b3d6248741598c7a1`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `FreezeLocalTransactionManagers` | `0x2170` | 506 | UnwindData |  |
| 4 | `GetDtcLocaleResourceHandle` | `0x26C0` | 58 | UnwindData |  |
| 9 | `ThawLocalTransactionManagers` | `0x2700` | 78 | UnwindData |  |
| 5 | `DtcGetTransactionManager` | `0x27E0` | 108 | UnwindData |  |
| 7 | `DtcGetTransactionManagerC` | `0x2860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DtcGetTransactionManagerEx` | `0x2880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `DtcGetTransactionManagerExA` | `0x2890` | 327 | UnwindData |  |
| 11 | `DtcGetTransactionManagerExW` | `0x29E0` | 1,082 | UnwindData |  |
