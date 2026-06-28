# Binary Specification: dsclient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dsclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `983c72a5e6d40f93e6964f9fd4e5727395273abc56647ac231c2dfaaf8a89c95`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DSGetSharedFileName` | `0x12E0` | 60 | UnwindData |  |
| 2 | `DSCreateSharedFileToken` | `0x1500` | 667 | UnwindData |  |
| 6 | `DSGetSharingTokenInformation` | `0x1A00` | 182 | UnwindData |  |
| 4 | `DSFreeString` | `0x1C20` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DSRemoveExpiredTokens` | `0x1EB0` | 343 | UnwindData |  |
| 1 | `DSCopyFromSharedFile` | `0x2E20` | 233 | UnwindData |  |
| 3 | `DSDelegateSharingToken` | `0x2F10` | 236 | UnwindData |  |
| 7 | `DSOpenSharedFile` | `0x3010` | 232 | UnwindData |  |
| 9 | `DSRemoveSharingToken` | `0x3100` | 201 | UnwindData |  |
