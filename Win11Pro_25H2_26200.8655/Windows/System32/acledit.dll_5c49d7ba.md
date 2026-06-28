# Binary Specification: acledit.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\acledit.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5c49d7bad0a28967a4f39b76a3f554370beff5e5534483fdcecb2568ece76ab0`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EditAuditInfo` | `0x1910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `EditOwnerInfo` | `0x1930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `EditPermissionInfo` | `0x1950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FMExtensionProcW` | `0x1970` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllMain` | `0x1A60` | 45 | UnwindData |  |
| 6 | `SedDiscretionaryAclEditor` | `0x1AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SedSystemAclEditor` | `0x1AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SedTakeOwnership` | `0x1AE0` | 0 | Indeterminate |  |
