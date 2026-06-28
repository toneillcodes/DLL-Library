# Binary Specification: BamSettingsClient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\BamSettingsClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4ce8ce15bc81e74a74b0bcbfe623cde5b2f60f9fb18c98fd21cd2dfe680562e5`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `BamCreateSettingsClientLib` | `0x1F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `BamDestroySettingsClientLib` | `0x1F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `BamFreeQueriedApplications` | `0x1F40` | 78 | UnwindData |  |
| 4 | `BamQueryKnownApplications` | `0x1FA0` | 258 | UnwindData |  |
| 5 | `BamSetUserManagementState` | `0x20B0` | 108 | UnwindData |  |
