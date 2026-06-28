# Binary Specification: wkscli.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wkscli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9207aa4d33ed79d9a5199185514ecae5c4e85b4bcef633268875898dba5a3367`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 15 | `NetWkstaGetInfo` | `0x20D0` | 400 | UnwindData |  |
| 3 | `NetGetJoinInformation` | `0x2410` | 338 | UnwindData |  |
| 13 | `NetUseGetInfo` | `0x26D0` | 184 | UnwindData |  |
| 12 | `NetUseEnum` | `0x27C0` | 315 | UnwindData |  |
| 22 | `NetWkstaUserGetInfo` | `0x2960` | 226 | UnwindData |  |
| 10 | `NetUseAdd` | `0x2AA0` | 493 | UnwindData |  |
| 17 | `NetWkstaStatisticsGet` | `0x2CA0` | 308 | UnwindData |  |
| 20 | `NetWkstaTransportEnum` | `0x2DE0` | 394 | UnwindData |  |
| 11 | `NetUseDel` | `0x3080` | 144 | UnwindData |  |
| 1 | `NetAddAlternateComputerName` | `0x46A0` | 654 | UnwindData |  |
| 2 | `NetEnumerateComputerNames` | `0x4940` | 521 | UnwindData |  |
| 4 | `NetGetJoinableOUs` | `0x4B50` | 794 | UnwindData |  |
| 5 | `NetJoinDomain` | `0x4E70` | 921 | UnwindData |  |
| 6 | `NetRemoveAlternateComputerName` | `0x5210` | 654 | UnwindData |  |
| 7 | `NetRenameMachineInDomain` | `0x54B0` | 385 | UnwindData |  |
| 8 | `NetSetPrimaryComputerName` | `0x5640` | 607 | UnwindData |  |
| 9 | `NetUnjoinDomain` | `0x58B0` | 617 | UnwindData |  |
| 14 | `NetValidateName` | `0x5B20` | 894 | UnwindData |  |
| 16 | `NetWkstaSetInfo` | `0x5EB0` | 228 | UnwindData |  |
| 18 | `NetWkstaTransportAdd` | `0x5FA0` | 233 | UnwindData |  |
| 19 | `NetWkstaTransportDel` | `0x6090` | 204 | UnwindData |  |
| 21 | `NetWkstaUserEnum` | `0x6170` | 394 | UnwindData |  |
| 23 | `NetWkstaUserSetInfo` | `0x6300` | 226 | UnwindData |  |
| 24 | `NetpWkstaClientCertificateMappingAdd` | `0x6B30` | 205 | UnwindData |  |
| 25 | `NetpWkstaClientCertificateMappingEnum` | `0x6C10` | 239 | UnwindData |  |
| 26 | `NetpWkstaClientCertificateMappingGet` | `0x6D10` | 283 | UnwindData |  |
| 27 | `NetpWkstaClientCertificateMappingModify` | `0x6E40` | 201 | UnwindData |  |
| 28 | `NetpWkstaClientCertificateMappingRemove` | `0x6F10` | 201 | UnwindData |  |
| 29 | `NetpWkstaClientSmbDirectModuleControl` | `0x6FE0` | 187 | UnwindData |  |
