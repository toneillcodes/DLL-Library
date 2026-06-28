# Binary Specification: tlscsp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\tlscsp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dc2e3337ece1fc72b2c499a9cd69500f05c2c3e8a8eeff9360d17f17f54d98ec`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `TLSFreeTSCertificate` | `0x1F80` | 36 | UnwindData |  |
| 3 | `TLSGetTSCertificate` | `0x1FB0` | 204 | UnwindData |  |
| 7 | `LsCsp_DecryptEnvelopedData` | `0x33C0` | 349 | UnwindData |  |
| 6 | `LsCsp_EncryptHwid` | `0x3530` | 175 | UnwindData |  |
| 5 | `LsCsp_GetServerData` | `0x3A20` | 592 | UnwindData |  |
| 1 | `TLSCspInit` | `0x59D0` | 111 | UnwindData |  |
| 2 | `TLSCspShutdown` | `0x5A50` | 271 | UnwindData |  |
| 10 | `TLSCspStartInstallCertificateThread` | `0x5B70` | 169 | UnwindData |  |
| 9 | `LsCsp_RetrieveSecret` | `0x6490` | 37 | UnwindData |  |
| 8 | `LsCsp_StoreSecret` | `0x64C0` | 119 | UnwindData |  |
