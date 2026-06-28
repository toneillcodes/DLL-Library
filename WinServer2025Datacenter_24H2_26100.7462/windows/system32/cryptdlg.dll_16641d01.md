# Binary Specification: cryptdlg.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cryptdlg.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `16641d01a9fe6fa5fe73b79d4b577428e368e3e6bf30fd2acf9c2f507eedd130`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 14 | `CertSelectCertificateA` | `0x1C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `CertSelectCertificateW` | `0x1C90` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CertConfigureTrustA` | `0x1CF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CertConfigureTrustW` | `0x1CF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CertTrustCertPolicy` | `0x1CF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DecodeAttrSequence` | `0x1D50` | 881 | UnwindData |  |
| 8 | `DecodeRecipientID` | `0x20D0` | 421 | UnwindData |  |
| 9 | `EncodeAttrSequence` | `0x2280` | 457 | UnwindData |  |
| 10 | `EncodeRecipientID` | `0x2450` | 336 | UnwindData |  |
| 11 | `FormatPKIXEmailProtection` | `0x25B0` | 173 | UnwindData |  |
| 12 | `FormatVerisignExtension` | `0x2670` | 69 | UnwindData |  |
| 18 | `DllRegisterServer` | `0x29D0` | 558 | UnwindData |  |
| 19 | `DllUnregisterServer` | `0x2C10` | 363 | UnwindData |  |
| 20 | `GetFriendlyNameOfCertA` | `0x2D90` | 224 | UnwindData |  |
| 21 | `GetFriendlyNameOfCertW` | `0x2E80` | 244 | UnwindData |  |
| 16 | `CertViewPropertiesA` | `0x3930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `CertViewPropertiesW` | `0x3940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CertTrustCleanup` | `0x3960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CertTrustFinalPolicy` | `0x3970` | 1,921 | UnwindData |  |
| 6 | `CertTrustInit` | `0x4100` | 4,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CertModifyCertificatesToTrust` | `0x52D0` | 490 | UnwindData |  |
