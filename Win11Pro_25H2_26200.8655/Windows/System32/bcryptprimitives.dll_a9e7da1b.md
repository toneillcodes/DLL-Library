# Binary Specification: bcryptprimitives.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\bcryptprimitives.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a9e7da1b143e96f9bdce987965b55cf1ae7164ce3a8319a4236a2d1e0ed32d19`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `GetHashInterface` | `0xACB0` | 142 | UnwindData |  |
| 2 | `GetCipherInterface` | `0xAD50` | 130 | UnwindData |  |
| 11 | `ProcessPrngGuid` | `0x1EB50` | 84 | UnwindData |  |
| 10 | `ProcessPrng` | `0x1FDF0` | 54 | UnwindData |  |
| 9 | `MSCryptConvertRsaPrivateBlobToFullRsaBlob` | `0x44DF0` | 412 | UnwindData |  |
| 7 | `GetSecretAgreementInterface` | `0x46960` | 208 | UnwindData |  |
| 1 | `GetAsymmetricEncryptionInterface` | `0x49370` | 134 | UnwindData |  |
| 6 | `GetRngInterface` | `0x49700` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetKeyDerivationInterface` | `0x49980` | 229 | UnwindData |  |
| 8 | `GetSignatureInterface` | `0x4D420` | 261 | UnwindData |  |
| 5 | `GetKeyEncapsulationInterface` | `0x5F980` | 95 | UnwindData |  |
