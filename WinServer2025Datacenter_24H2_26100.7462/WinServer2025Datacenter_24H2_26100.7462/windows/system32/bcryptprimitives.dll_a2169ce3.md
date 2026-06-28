# Binary Specification: bcryptprimitives.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\bcryptprimitives.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a2169ce3ad4b7cb060d75519b1b078f52ed79a8aa20d416aaec2762875be55f8`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `GetHashInterface` | `0xACB0` | 142 | UnwindData |  |
| 2 | `GetCipherInterface` | `0xAD50` | 130 | UnwindData |  |
| 11 | `ProcessPrngGuid` | `0x1E9A0` | 84 | UnwindData |  |
| 10 | `ProcessPrng` | `0x1FC40` | 54 | UnwindData |  |
| 9 | `MSCryptConvertRsaPrivateBlobToFullRsaBlob` | `0x44960` | 412 | UnwindData |  |
| 7 | `GetSecretAgreementInterface` | `0x464D0` | 208 | UnwindData |  |
| 1 | `GetAsymmetricEncryptionInterface` | `0x48EE0` | 134 | UnwindData |  |
| 6 | `GetRngInterface` | `0x49270` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetKeyDerivationInterface` | `0x494F0` | 229 | UnwindData |  |
| 8 | `GetSignatureInterface` | `0x4CF90` | 261 | UnwindData |  |
| 5 | `GetKeyEncapsulationInterface` | `0x5F500` | 95 | UnwindData |  |
