# Binary Specification: p9np.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\p9np.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4be8757e1ec9a77633c6198a96ef41b86ef9faf535fe6f8f83224bed9c1bab67`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NPAddConnection` | `0xCE00` | 31 | UnwindData |  |
| 2 | `NPAddConnection3` | `0xCE30` | 949 | UnwindData |  |
| 3 | `NPCancelConnection` | `0xD1F0` | 962 | UnwindData |  |
| 8 | `NPGetConnection` | `0xD5C0` | 359 | UnwindData |  |
| 4 | `NPCloseEnum` | `0xE200` | 41 | UnwindData |  |
| 5 | `NPEnumResource` | `0xE230` | 165 | UnwindData |  |
| 6 | `NPFormatNetworkName` | `0xE2E0` | 340 | UnwindData |  |
| 7 | `NPGetCaps` | `0xE440` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `NPGetResourceInformation` | `0xE4A0` | 639 | UnwindData |  |
| 10 | `NPOpenEnum` | `0xE730` | 393 | UnwindData |  |
