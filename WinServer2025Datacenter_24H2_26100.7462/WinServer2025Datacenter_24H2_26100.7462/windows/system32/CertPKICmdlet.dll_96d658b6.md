# Binary Specification: CertPKICmdlet.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\CertPKICmdlet.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `96d658b601afd38b9a6c8989d7ad628b2f50706960d08b9d3308547982f1d868`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `FreeCertResults` | `0x7530` | 77 | UnwindData |  |
| 12 | `ImportPFXCertificate` | `0x7590` | 1,245 | UnwindData |  |
| 7 | `ExportPFXCertificate` | `0x8830` | 1,334 | UnwindData |  |
| 11 | `ImportCertificate` | `0x9180` | 546 | UnwindData |  |
| 6 | `ExportCertificate` | `0x9510` | 523 | UnwindData |  |
| 5 | `DllMain` | `0x9840` | 123 | UnwindData |  |
| 1 | `FindCertificate` | `0x9D60` | 267 | UnwindData |  |
| 2 | `IsSmartCard` | `0xA310` | 550 | UnwindData |  |
| 3 | `SuppressFreeCert` | `0xA710` | 47 | UnwindData |  |
| 4 | `SuppressFreeStore` | `0xA750` | 65 | UnwindData |  |
| 9 | `FreeResourceString` | `0xA7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `GetCertificateFromEnrollmentInternal` | `0xA7C0` | 268 | UnwindData |  |
| 13 | `IsSecureKernelRunning` | `0xA8E0` | 123 | UnwindData |  |
| 14 | `LoadResourceString` | `0xA970` | 68 | UnwindData |  |
