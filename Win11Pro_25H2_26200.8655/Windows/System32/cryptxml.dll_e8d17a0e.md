# Binary Specification: cryptxml.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cryptxml.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e8d17a0e5f8e19bca61ec67a2273740f3997087ebe48730eee217a5782157a4c`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 18 | `CryptXmlSign` | `0x2790` | 23 | UnwindData |  |
| 19 | `CryptXmlVerifySignature` | `0x6550` | 192 | UnwindData |  |
| 12 | `CryptXmlGetStatus` | `0x6FA0` | 596 | UnwindData |  |
| 14 | `CryptXmlImportPublicKey` | `0x75A0` | 9 | UnwindData |  |
| 15 | `CryptXmlOpenToDecode` | `0x8200` | 118 | UnwindData |  |
| 3 | `CryptXmlCreateReference` | `0x97A0` | 2,317 | UnwindData |  |
| 16 | `CryptXmlOpenToEncode` | `0xA0C0` | 96 | UnwindData |  |
| 4 | `CryptXmlDigestReference` | `0xB990` | 37 | UnwindData |  |
| 8 | `CryptXmlGetAlgorithmInfo` | `0xE580` | 29 | UnwindData |  |
| 2 | `CryptXmlClose` | `0x12E70` | 88 | UnwindData |  |
| 5 | `CryptXmlEncode` | `0x12ED0` | 210 | UnwindData |  |
| 7 | `CryptXmlFindAlgorithmInfo` | `0x13310` | 245 | UnwindData |  |
| 9 | `CryptXmlGetDocContext` | `0x13480` | 122 | UnwindData |  |
| 11 | `CryptXmlGetSignature` | `0x13500` | 151 | UnwindData |  |
| 1 | `CryptXmlAddObject` | `0x16320` | 584 | UnwindData |  |
| 10 | `CryptXmlGetReference` | `0x16750` | 122 | UnwindData |  |
| 6 | `CryptXmlEnumAlgorithmInfo` | `0x17720` | 315 | UnwindData |  |
| 13 | `CryptXmlGetTransforms` | `0x17870` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `CryptXmlSetHMACSecret` | `0x179B0` | 190 | UnwindData |  |
