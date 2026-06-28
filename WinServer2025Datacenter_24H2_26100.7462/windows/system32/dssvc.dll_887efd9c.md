# Binary Specification: dssvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dssvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `887efd9c1856bef2f639a7d587936259ccb32c7088b5aa01e652e00a867b6b60`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `InitializeService` | `0xB8D0` | 153 | UnwindData |  |
| 2 | `ServiceMain` | `0xBA80` | 459 | UnwindData |  |
| 3 | `SvchostPushServiceGlobals` | `0xBE70` | 15,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DSSCreateSharedFileTokenEx` | `0xFC00` | 1,045 | UnwindData |  |
| 5 | `DSSFreeToken` | `0x10020` | 24 | UnwindData |  |
