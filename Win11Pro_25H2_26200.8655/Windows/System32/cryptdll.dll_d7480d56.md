# Binary Specification: cryptdll.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cryptdll.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d7480d564e49762db8b6c965f05a226bdda2eac5444862be39f5624310f2134d`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 15 | `MD5Final` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD5Final` |
| 16 | `MD5Init` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD5Init` |
| 17 | `MD5Update` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.MD5Update` |
| 19 | `aesCTSDecryptMsg` | `0x13D0` | 247 | UnwindData |  |
| 13 | `HMACwithSHA` | `0x14D0` | 349 | UnwindData |  |
| 7 | `CDLocateCSystem` | `0x3150` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CDLocateCheckSum` | `0x3190` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `CDRegisterCSystem` | `0x3460` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `CDRegisterCheckSum` | `0x34E0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CDBuildIntegrityVect` | `0x3570` | 106 | UnwindData |  |
| 14 | `KRBFXCF2` | `0x3790` | 113 | UnwindData |  |
| 6 | `CDGetIntegrityVect` | `0x3B50` | 643 | UnwindData |  |
| 12 | `CDRegisterRng` | `0x49B0` | 4,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CDBuildVect` | `0x5AD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CDFindCommonCSystem` | `0x5B10` | 97 | UnwindData |  |
| 4 | `CDFindCommonCSystemWithKey` | `0x5B80` | 139 | UnwindData |  |
| 5 | `CDGenerateRandomBits` | `0x5C20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CDLocateRng` | `0x5C50` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `PBKDF2` | `0x5CE0` | 136 | UnwindData |  |
| 20 | `aesCTSEncryptMsg` | `0x5F70` | 241 | UnwindData |  |
