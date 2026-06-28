# Binary Specification: p9np.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\p9np.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3d51c728e8623555e8b7aa83d4abdc33545ed6a83b9acc9c36cb1c8e992a062d`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NPAddConnection` | `0xCDE0` | 31 | UnwindData |  |
| 2 | `NPAddConnection3` | `0xCE10` | 949 | UnwindData |  |
| 3 | `NPCancelConnection` | `0xD1D0` | 962 | UnwindData |  |
| 8 | `NPGetConnection` | `0xD5A0` | 359 | UnwindData |  |
| 4 | `NPCloseEnum` | `0xE1E0` | 41 | UnwindData |  |
| 5 | `NPEnumResource` | `0xE210` | 165 | UnwindData |  |
| 6 | `NPFormatNetworkName` | `0xE2C0` | 340 | UnwindData |  |
| 7 | `NPGetCaps` | `0xE420` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `NPGetResourceInformation` | `0xE480` | 639 | UnwindData |  |
| 10 | `NPOpenEnum` | `0xE710` | 393 | UnwindData |  |
