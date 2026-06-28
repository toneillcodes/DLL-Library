# Binary Specification: winlogonext.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\winlogonext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7cce20ba07c0f6be69f61193c3125a334f096cd04c235516379b9645d8bfc777`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ConfigureUserArso` | `0x1910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EnableDisableElevationForSessionWorker` | `0x1920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `NotifyInteractiveSessionLogoff` | `0x1940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `UpdateUserTokenSessionId` | `0x1950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WinLogonExt` | `0x1960` | 8 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
