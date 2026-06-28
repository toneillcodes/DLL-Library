# Binary Specification: tlscsp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\tlscsp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f36ba5a6315e4aae17f746ddd103f3181f8bb3f07916789ed7103e451cb0d41f`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `TLSFreeTSCertificate` | `0x1D40` | 36 | UnwindData |  |
| 3 | `TLSGetTSCertificate` | `0x1D70` | 204 | UnwindData |  |
| 7 | `LsCsp_DecryptEnvelopedData` | `0x3180` | 349 | UnwindData |  |
| 6 | `LsCsp_EncryptHwid` | `0x32F0` | 175 | UnwindData |  |
| 5 | `LsCsp_GetServerData` | `0x37E0` | 592 | UnwindData |  |
| 1 | `TLSCspInit` | `0x5790` | 111 | UnwindData |  |
| 2 | `TLSCspShutdown` | `0x5810` | 271 | UnwindData |  |
| 10 | `TLSCspStartInstallCertificateThread` | `0x5930` | 169 | UnwindData |  |
| 9 | `LsCsp_RetrieveSecret` | `0x6250` | 37 | UnwindData |  |
| 8 | `LsCsp_StoreSecret` | `0x6280` | 119 | UnwindData |  |
