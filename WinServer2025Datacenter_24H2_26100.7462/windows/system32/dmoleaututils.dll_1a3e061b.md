# Binary Specification: dmoleaututils.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dmoleaututils.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1a3e061b2bd11112ea60234b5757232b10f4154392aec67f89363c60cd337355`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `Base64StrToSafeArray` | `0x2210` | 302 | UnwindData |  |
| 2 | `ByteArrayToSafeArray` | `0x2350` | 252 | UnwindData |  |
| 3 | `MultiStringToSafeArray` | `0x2460` | 496 | UnwindData |  |
| 9 | `SafeArrayToBase64Str` | `0x2660` | 190 | UnwindData |  |
| 10 | `SafeArrayToByteArray` | `0x2730` | 267 | UnwindData |  |
| 11 | `SafeArrayToMultiString` | `0x2850` | 628 | UnwindData |  |
| 4 | `ReadBSTRFromStream` | `0x2C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ReadBSTRFromStreamEx` | `0x2C20` | 281 | UnwindData |  |
| 6 | `ReadStringFromStream` | `0x2FA0` | 315 | UnwindData |  |
| 7 | `ReadVariantFromStream` | `0x30F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `ReadVariantFromStreamEx` | `0x3100` | 553 | UnwindData |  |
| 12 | `WriteBSTRToStream` | `0x3330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `WriteBSTRToStreamEx` | `0x3340` | 202 | UnwindData |  |
| 14 | `WriteStringToStream` | `0x3650` | 291 | UnwindData |  |
| 15 | `WriteVariantToStream` | `0x3780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `WriteVariantToStreamEx` | `0x3790` | 483 | UnwindData |  |
