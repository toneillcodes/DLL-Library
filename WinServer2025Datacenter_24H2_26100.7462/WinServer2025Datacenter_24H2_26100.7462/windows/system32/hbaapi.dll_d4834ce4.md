# Binary Specification: hbaapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\hbaapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d4834ce4e412d38089f659557352742cf8b38a31e107e5aa6ed9a6dea4d820a5`
* **Total Exported Functions:** 93

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `HBA_CloseAdapter` | `0x19C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `HBA_GetAdapterName` | `0x19D0` | 135 | UnwindData |  |
| 15 | `HBA_GetNumberOfAdapters` | `0x1A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `HBA_OpenAdapter` | `0x1A70` | 175 | UnwindData |  |
| 25 | `HBA_OpenAdapterByWWN` | `0x1B30` | 192 | UnwindData |  |
| 26 | `HBA_RefreshAdapterConfiguration` | `0x1C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `HBA_RefreshInformation` | `0x1C10` | 873 | UnwindData |  |
| 58 | `HbaGetAdapterNameByDeviceInstanceId` | `0x1F80` | 413 | UnwindData |  |
| 28 | `HBA_RegisterForAdapterAddEvents` | `0x3220` | 31 | UnwindData |  |
| 29 | `HBA_RegisterForAdapterEvents` | `0x3250` | 28 | UnwindData |  |
| 30 | `HBA_RegisterForAdapterPortEvents` | `0x3280` | 361 | UnwindData |  |
| 31 | `HBA_RegisterForAdapterPortStatEvents` | `0x33F0` | 435 | UnwindData |  |
| 32 | `HBA_RegisterForLinkEvents` | `0x35B0` | 367 | UnwindData |  |
| 33 | `HBA_RegisterForTargetEvents` | `0x3730` | 405 | UnwindData |  |
| 37 | `HBA_RemoveCallback` | `0x38D0` | 595 | UnwindData |  |
| 77 | `SMHBA_RegisterForAdapterAddEvents` | `0x5B20` | 34 | UnwindData |  |
| 78 | `SMHBA_RegisterForAdapterEvents` | `0x5B50` | 31 | UnwindData |  |
| 79 | `SMHBA_RegisterForAdapterPhyStatEvents` | `0x5B80` | 556 | UnwindData |  |
| 80 | `SMHBA_RegisterForAdapterPortEvents` | `0x5DC0` | 432 | UnwindData |  |
| 81 | `SMHBA_RegisterForAdapterPortStatEvents` | `0x5F80` | 367 | UnwindData |  |
| 82 | `SMHBA_RegisterForTargetEvents` | `0x6100` | 496 | UnwindData |  |
| 8 | `HBA_GetDiscoveredPortAttributes` | `0x6300` | 310 | UnwindData |  |
| 9 | `HBA_GetEventBuffer` | `0x6440` | 374 | UnwindData |  |
| 10 | `HBA_GetFC4Statistics` | `0x65C0` | 301 | UnwindData |  |
| 11 | `HBA_GetFCPStatistics` | `0x6700` | 402 | UnwindData |  |
| 17 | `HBA_GetPortAttributesByWWN` | `0x68A0` | 484 | UnwindData |  |
| 19 | `HBA_GetRNIDMgmtInfo` | `0x6A90` | 341 | UnwindData |  |
| 39 | `HBA_ResetStatistics` | `0x6BF0` | 180 | UnwindData |  |
| 43 | `HBA_SendCTPassThru` | `0x6CB0` | 66 | UnwindData |  |
| 44 | `HBA_SendCTPassThruV2` | `0x6D00` | 646 | UnwindData |  |
| 45 | `HBA_SendLIRR` | `0x6F90` | 614 | UnwindData |  |
| 46 | `HBA_SendRLS` | `0x7200` | 605 | UnwindData |  |
| 47 | `HBA_SendRNID` | `0x7470` | 395 | UnwindData |  |
| 48 | `HBA_SendRNIDV2` | `0x7610` | 606 | UnwindData |  |
| 49 | `HBA_SendRPL` | `0x7880` | 625 | UnwindData |  |
| 50 | `HBA_SendRPS` | `0x7B00` | 620 | UnwindData |  |
| 53 | `HBA_SendSRL` | `0x7D80` | 598 | UnwindData |  |
| 57 | `HBA_SetRNIDMgmtInfo` | `0x7FE0` | 334 | UnwindData |  |
| 2 | `HBA_FreeLibrary` | `0x8F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `HBA_LoadLibrary` | `0x8F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `HBA_GetVendorLibraryAttributes` | `0x8F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `HBA_GetVersion` | `0x8F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `HBA_RegisterLibrary` | `0x8F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `HBA_RegisterLibraryV2` | `0x8F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `SMHBA_RegisterLibrary` | `0x8F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `HBA_GetWrapperLibraryAttributes` | `0x8F70` | 241 | UnwindData |  |
| 3 | `HBA_GetAdapterAttributes` | `0x9070` | 711 | UnwindData |  |
| 5 | `HBA_GetAdapterPortAttributes` | `0x9340` | 436 | UnwindData |  |
| 18 | `HBA_GetPortStatistics` | `0x9500` | 664 | UnwindData |  |
| 6 | `HBA_GetBindingCapability` | `0x98B0` | 246 | UnwindData |  |
| 7 | `HBA_GetBindingSupport` | `0x99B0` | 246 | UnwindData |  |
| 12 | `HBA_GetFcpPersistentBinding` | `0x9AB0` | 449 | UnwindData |  |
| 16 | `HBA_GetPersistentBindingV2` | `0x9C80` | 857 | UnwindData |  |
| 36 | `HBA_RemoveAllPersistentBindings` | `0x9FE0` | 231 | UnwindData |  |
| 38 | `HBA_RemovePersistentBinding` | `0xA0D0` | 795 | UnwindData |  |
| 55 | `HBA_SetBindingSupport` | `0xA400` | 232 | UnwindData |  |
| 56 | `HBA_SetPersistentBindingV2` | `0xA4F0` | 669 | UnwindData |  |
| 59 | `SMHBA_GetAdapterAttributes` | `0xB2B0` | 1,687 | UnwindData |  |
| 60 | `SMHBA_GetAdapterPortAttributes` | `0xB950` | 382 | UnwindData |  |
| 61 | `SMHBA_GetBindingCapability` | `0xBAE0` | 290 | UnwindData |  |
| 62 | `SMHBA_GetBindingSupport` | `0xBC10` | 277 | UnwindData |  |
| 63 | `SMHBA_GetDiscoveredPortAttributes` | `0xBD30` | 368 | UnwindData |  |
| 64 | `SMHBA_GetFCPhyAttributes` | `0xBEB0` | 391 | UnwindData |  |
| 65 | `SMHBA_GetLUNStatistics` | `0xC040` | 474 | UnwindData |  |
| 66 | `SMHBA_GetNumberOfPorts` | `0xC220` | 65 | UnwindData |  |
| 67 | `SMHBA_GetPersistentBinding` | `0xC270` | 1,007 | UnwindData |  |
| 68 | `SMHBA_GetPhyStatistics` | `0xC670` | 343 | UnwindData |  |
| 69 | `SMHBA_GetPortAttributesByWWN` | `0xC7D0` | 369 | UnwindData |  |
| 70 | `SMHBA_GetPortType` | `0xC950` | 322 | UnwindData |  |
| 71 | `SMHBA_GetProtocolStatistics` | `0xCAA0` | 492 | UnwindData |  |
| 72 | `SMHBA_GetSASPhyAttributes` | `0xCCA0` | 288 | UnwindData |  |
| 74 | `SMHBA_GetVendorLibraryAttributes` | `0xCDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `SMHBA_GetVersion` | `0xCDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `SMHBA_GetWrapperLibraryAttributes` | `0xCDF0` | 228 | UnwindData |  |
| 84 | `SMHBA_RemoveAllPersistentBindings` | `0xCEE0` | 315 | UnwindData |  |
| 85 | `SMHBA_RemovePersistentBinding` | `0xD030` | 886 | UnwindData |  |
| 86 | `SMHBA_ScsiInquiry` | `0xD3B0` | 682 | UnwindData |  |
| 87 | `SMHBA_ScsiReadCapacity` | `0xD660` | 619 | UnwindData |  |
| 88 | `SMHBA_ScsiReportLuns` | `0xD8E0` | 640 | UnwindData |  |
| 89 | `SMHBA_SendECHO` | `0xDB70` | 476 | UnwindData |  |
| 90 | `SMHBA_SendSMPPassThru` | `0xDD60` | 503 | UnwindData |  |
| 91 | `SMHBA_SendTEST` | `0xDF60` | 351 | UnwindData |  |
| 92 | `SMHBA_SetBindingSupport` | `0xE0D0` | 246 | UnwindData |  |
| 93 | `SMHBA_SetPersistentBinding` | `0xE1D0` | 934 | UnwindData |  |
| 13 | `HBA_GetFcpTargetMapping` | `0xE580` | 374 | UnwindData |  |
| 14 | `HBA_GetFcpTargetMappingV2` | `0xE700` | 818 | UnwindData |  |
| 40 | `HBA_ScsiInquiryV2` | `0xEA40` | 584 | UnwindData |  |
| 41 | `HBA_ScsiReadCapacityV2` | `0xEC90` | 534 | UnwindData |  |
| 42 | `HBA_ScsiReportLUNsV2` | `0xEEB0` | 544 | UnwindData |  |
| 51 | `HBA_SendReadCapacity` | `0xF0E0` | 246 | UnwindData |  |
| 52 | `HBA_SendReportLUNs` | `0xF1E0` | 98 | UnwindData |  |
| 54 | `HBA_SendScsiInquiry` | `0xF250` | 124 | UnwindData |  |
| 73 | `SMHBA_GetTargetMapping` | `0x10560` | 1,240 | UnwindData |  |
