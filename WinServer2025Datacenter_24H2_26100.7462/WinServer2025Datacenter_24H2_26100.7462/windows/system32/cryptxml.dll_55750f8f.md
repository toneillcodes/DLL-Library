# Binary Specification: cryptxml.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cryptxml.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `55750f8f1c3d1d5fc1b8724417011d103f6f6536edf1531e6c9e03183f6593a4`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 18 | `CryptXmlSign` | `0x3070` | 23 | UnwindData |  |
| 19 | `CryptXmlVerifySignature` | `0x6E30` | 192 | UnwindData |  |
| 12 | `CryptXmlGetStatus` | `0x7880` | 596 | UnwindData |  |
| 14 | `CryptXmlImportPublicKey` | `0x7E80` | 9 | UnwindData |  |
| 15 | `CryptXmlOpenToDecode` | `0x8AE0` | 118 | UnwindData |  |
| 3 | `CryptXmlCreateReference` | `0xA080` | 2,317 | UnwindData |  |
| 16 | `CryptXmlOpenToEncode` | `0xA9A0` | 96 | UnwindData |  |
| 4 | `CryptXmlDigestReference` | `0xC270` | 37 | UnwindData |  |
| 8 | `CryptXmlGetAlgorithmInfo` | `0xEE60` | 29 | UnwindData |  |
| 2 | `CryptXmlClose` | `0x141B0` | 88 | UnwindData |  |
| 5 | `CryptXmlEncode` | `0x14210` | 210 | UnwindData |  |
| 7 | `CryptXmlFindAlgorithmInfo` | `0x14650` | 245 | UnwindData |  |
| 9 | `CryptXmlGetDocContext` | `0x147C0` | 122 | UnwindData |  |
| 11 | `CryptXmlGetSignature` | `0x14840` | 151 | UnwindData |  |
| 1 | `CryptXmlAddObject` | `0x161D0` | 584 | UnwindData |  |
| 10 | `CryptXmlGetReference` | `0x16600` | 122 | UnwindData |  |
| 6 | `CryptXmlEnumAlgorithmInfo` | `0x175D0` | 315 | UnwindData |  |
| 13 | `CryptXmlGetTransforms` | `0x17720` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `CryptXmlSetHMACSecret` | `0x17860` | 190 | UnwindData |  |
