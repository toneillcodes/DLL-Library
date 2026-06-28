# Binary Specification: winlogonext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\winlogonext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `075e953942b696f5d5e844a3e8281c7e03417912222dcedebfbec7b311315542`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ConfigureUserArso` | `0x1910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EnableDisableElevationForSessionWorker` | `0x1920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `NotifyInteractiveSessionLogoff` | `0x1940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `UpdateUserTokenSessionId` | `0x1950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WinLogonExt` | `0x1960` | 8 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
