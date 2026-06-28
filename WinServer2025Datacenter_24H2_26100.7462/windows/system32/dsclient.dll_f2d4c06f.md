# Binary Specification: dsclient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dsclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f2d4c06f41c9f6e4b023335b04c8aca716142ff72bcdec303d1fc9a9b30fa052`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DSGetSharedFileName` | `0x13E0` | 60 | UnwindData |  |
| 2 | `DSCreateSharedFileToken` | `0x1600` | 667 | UnwindData |  |
| 6 | `DSGetSharingTokenInformation` | `0x1BE0` | 182 | UnwindData |  |
| 4 | `DSFreeString` | `0x2110` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DSRemoveExpiredTokens` | `0x22F0` | 343 | UnwindData |  |
| 1 | `DSCopyFromSharedFile` | `0x3250` | 233 | UnwindData |  |
| 3 | `DSDelegateSharingToken` | `0x3340` | 236 | UnwindData |  |
| 7 | `DSOpenSharedFile` | `0x3440` | 232 | UnwindData |  |
| 9 | `DSRemoveSharingToken` | `0x3530` | 201 | UnwindData |  |
