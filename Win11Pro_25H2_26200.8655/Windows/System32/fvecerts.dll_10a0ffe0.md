# Binary Specification: fvecerts.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fvecerts.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `10a0ffe04d1dabf97945554c4bc7dd07dd0b269b65471de2fb46daf1b112069b`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `FveCertCanCertificateBeAdded` | `0x23C0` | 785 | UnwindData |  |
| 2 | `FveCertCreateCertInfo` | `0x26E0` | 297 | UnwindData |  |
| 3 | `FveCertCreateSelfSignedCertificate` | `0x2810` | 594 | UnwindData |  |
| 4 | `FveCertFilterForValidCertificates` | `0x2A70` | 791 | UnwindData |  |
| 5 | `FveCertFindValidCertificates` | `0x2D90` | 350 | UnwindData |  |
| 6 | `FveCertFreeCertInfo` | `0x2F00` | 52 | UnwindData |  |
| 7 | `FveCertGetCertContextFromCert` | `0x2F40` | 1,214 | UnwindData |  |
| 8 | `FveCertGetCertContextFromPfx` | `0x3410` | 1,121 | UnwindData |  |
| 9 | `FveCertGetCertHashFromCertContext` | `0x3880` | 176 | UnwindData |  |
| 10 | `FveCertGetPrivateKeyHandle` | `0x3940` | 1,124 | UnwindData |  |
| 11 | `FveCertGetPublicKeyHandle` | `0x3DB0` | 188 | UnwindData |  |
| 12 | `FveCertIsAlternateCert` | `0x3E80` | 435 | UnwindData |  |
| 13 | `FveCertIsValidCertInfo` | `0x4040` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `FveCertSignData` | `0x40A0` | 565 | UnwindData |  |
| 15 | `FveCertWritePfxFromCertContext` | `0x42E0` | 1,013 | UnwindData |  |
