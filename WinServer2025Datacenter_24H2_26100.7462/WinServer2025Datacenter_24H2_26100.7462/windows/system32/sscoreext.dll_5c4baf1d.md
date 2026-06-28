# Binary Specification: sscoreext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sscoreext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5c4baf1da8e66b1d84d91c3f321316e67d4038aae7f06f14019c6b77a72ffc68`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SsCoreExtMiApplicationClose` | `0x17D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SsCoreExtMiOperationClose` | `0x17D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SsCoreExtMiApplicationInitialize` | `0x1800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SsCoreExtMiApplicationNewOperationOptions` | `0x1820` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SsCoreExtMiApplicationNewParameterSet` | `0x1860` | 62 | UnwindData |  |
| 5 | `SsCoreExtMiApplicationNewSession` | `0x18B0` | 119 | UnwindData |  |
| 6 | `SsCoreExtMiInstanceAddElement` | `0x1930` | 55 | UnwindData |  |
| 7 | `SsCoreExtMiInstanceDelete` | `0x1970` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SsCoreExtMiOperationGetInstance` | `0x19A0` | 90 | UnwindData |  |
| 10 | `SsCoreExtMiOperationOptionsDelete` | `0x1A00` | 34 | UnwindData |  |
| 11 | `SsCoreExtMiOperationOptionsSetResourceUriPrefix` | `0x1A30` | 53 | UnwindData |  |
| 12 | `SsCoreExtMiSessionClose` | `0x1A70` | 66 | UnwindData |  |
| 13 | `SsCoreExtMiSessionInvoke` | `0x1AC0` | 217 | UnwindData |  |
