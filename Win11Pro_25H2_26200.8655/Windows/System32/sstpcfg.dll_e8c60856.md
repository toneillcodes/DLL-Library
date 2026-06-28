# Binary Specification: sstpcfg.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sstpcfg.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e8c608567dcfa893e08089aa936057b8dcd0bc03dde9285159e92d51786417b2`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CheckIfCertificateAllowed` | `0x1D70` | 1,973 | UnwindData |  |
| 3 | `FreeSstpCertList` | `0x3270` | 81 | UnwindData |  |
| 4 | `FreeSstpCertNode` | `0x32D0` | 264 | UnwindData |  |
| 5 | `GetCertificateFromHash` | `0x39F0` | 694 | UnwindData |  |
| 6 | `GetCertificateFromSha256Hash` | `0x4060` | 535 | UnwindData |  |
| 7 | `GetCertificateFromStoreForSha256Hash` | `0x45B0` | 430 | UnwindData |  |
| 8 | `GetCryptoBindingInfo` | `0x4770` | 1,953 | UnwindData |  |
| 9 | `GetCryptoBindingSupportedAlgoInfo` | `0x4F20` | 731 | UnwindData |  |
| 10 | `GetHashFromCertificate` | `0x5210` | 1,173 | UnwindData |  |
| 11 | `GetSstpCertListRemote` | `0x5BB0` | 1,811 | UnwindData |  |
| 12 | `GetSstpConfiguration` | `0x62D0` | 731 | UnwindData |  |
| 13 | `GetSstpProxyConfig` | `0x67D0` | 513 | UnwindData |  |
| 14 | `GetSstpServerConfig` | `0x69E0` | 527 | UnwindData |  |
| 15 | `GetUrlForConfig` | `0x6E90` | 324 | UnwindData |  |
| 16 | `IsCertificateEKUServerAuth` | `0x7570` | 904 | UnwindData |  |
| 18 | `SetSstpConfiguration` | `0x9440` | 1,198 | UnwindData |  |
| 19 | `SetSstpProxyConfig` | `0x9900` | 539 | UnwindData |  |
| 20 | `SetupSstpServerConfig` | `0x9D00` | 1,117 | UnwindData |  |
| 2 | `ClearSstpCfgParams` | `0xB340` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SetSstpCfgParams` | `0xB3D0` | 63 | UnwindData |  |
