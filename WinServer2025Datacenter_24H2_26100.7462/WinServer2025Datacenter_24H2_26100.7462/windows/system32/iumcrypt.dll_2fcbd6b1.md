# Binary Specification: iumcrypt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\iumcrypt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2fcbd6b1048b5b4c234e4d4d45e084fb8bfd49c6f6222a52c90c49ef010e98d0`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `iumCryptMsgClose` | `0x6B40` | 934 | UnwindData |  |
| 6 | `iumCryptMsgDuplicate` | `0x6EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `iumCryptMsgGetParam` | `0x6F10` | 1,014 | UnwindData |  |
| 8 | `iumCryptMsgOpenToEncode` | `0x7310` | 141 | UnwindData |  |
| 9 | `iumCryptMsgUpdate` | `0x73B0` | 372 | UnwindData |  |
| 1 | `iumCryptEncodeObject` | `0x84B0` | 39 | UnwindData |  |
| 2 | `iumCryptEncodeObjectEx` | `0x84E0` | 449 | UnwindData |  |
| 4 | `iumCryptFindOIDInfo` | `0x8CD0` | 277 | UnwindData |  |
| 3 | `iumCryptExportPublicKeyInfoFromBCryptKeyHandle` | `0x9920` | 380 | UnwindData |  |
| 10 | `iumCryptSignAndEncodeCertificate` | `0x9AB0` | 397 | UnwindData |  |
