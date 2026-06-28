# Binary Specification: appidapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\appidapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `74e51955f577c24a3c84e46f163e94c9061f2fc6d568eafd4d11b998aec71efc`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `AppIDDecodeAttributeString` | `0x0` | - | Forwarded | Forwarded to: `srpapi.AppIDDecodeAttributeString` |
| 3 | `AppIDEncodeAttributeString` | `0x0` | - | Forwarded | Forwarded to: `srpapi.AppIDEncodeAttributeString` |
| 4 | `AppIDFreeAttributeString` | `0x0` | - | Forwarded | Forwarded to: `srpapi.AppIDFreeAttributeString` |
| 1 | `AppIDConstructAppxAttributes` | `0x2B20` | 183 | UnwindData |  |
| 5 | `AppIDGetAppxFileAttributes` | `0x2BE0` | 468 | UnwindData |  |
| 6 | `AppIDGetFileAttributes` | `0x2DC0` | 490 | UnwindData |  |
| 7 | `AppIDGetMsiVersionInfo` | `0x2FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `AppIDReleaseAppxFileAttributes` | `0x2FC0` | 82 | UnwindData |  |
| 9 | `AppIDReleaseFileAttributes` | `0x3020` | 27 | UnwindData |  |
| 10 | `CompareToSystemCIPolicy` | `0x3DF0` | 439 | UnwindData |  |
| 11 | `UpdateSystemCIPolicy` | `0x3FB0` | 716 | UnwindData |  |
