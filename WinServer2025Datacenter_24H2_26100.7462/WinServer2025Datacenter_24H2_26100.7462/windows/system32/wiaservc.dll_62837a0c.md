# Binary Specification: wiaservc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wiaservc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `62837a0c740a39a6b6a3f84b9411fea15c312f82c22572fc94cb9439aaeffedc`
* **Total Exported Functions:** 57

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `wiasDebugTrace` | `0x87E0` | 839 | UnwindData |  |
| 11 | `wiasFormatArgs` | `0xFF50` | 613 | UnwindData |  |
| 8 | `wiasDebugError` | `0x135C0` | 481 | UnwindData |  |
| 36 | `wiasSetItemPropNames` | `0x17E20` | 381 | UnwindData |  |
| 56 | `wiasWritePropLong` | `0x17FB0` | 688 | UnwindData |  |
| 19 | `wiasGetDrvItem` | `0x18470` | 353 | UnwindData |  |
| 35 | `wiasSetItemPropAttribs` | `0x185E0` | 554 | UnwindData |  |
| 32 | `wiasReadPropLong` | `0x18A30` | 512 | UnwindData |  |
| 38 | `wiasSetPropertyAttributes` | `0x18C40` | 1,115 | UnwindData |  |
| 23 | `wiasGetRootItem` | `0x23790` | 226 | UnwindData |  |
| 1 | `ServiceMain` | `0x34C20` | 1,218 | UnwindData |  |
| 2 | `DllRegisterServer` | `0x36D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllUnregisterServer` | `0x36DA0` | 16,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `wiasQueueEvent` | `0x3AE50` | 291 | UnwindData |  |
| 5 | `wiasCreateDrvItem` | `0x3E2B0` | 755 | UnwindData |  |
| 6 | `wiasCreateLogInstance` | `0x3E5B0` | 274 | UnwindData |  |
| 7 | `wiasCreatePropContext` | `0x3E6D0` | 640 | UnwindData |  |
| 10 | `wiasDownSampleBuffer` | `0x3E960` | 797 | UnwindData |  |
| 12 | `wiasFreePropContext` | `0x3EC90` | 209 | UnwindData |  |
| 13 | `wiasGetChangedValueFloat` | `0x3ED70` | 435 | UnwindData |  |
| 14 | `wiasGetChangedValueGuid` | `0x3EF30` | 435 | UnwindData |  |
| 15 | `wiasGetChangedValueLong` | `0x3F0F0` | 435 | UnwindData |  |
| 16 | `wiasGetChangedValueStr` | `0x3F2B0` | 435 | UnwindData |  |
| 17 | `wiasGetChildrenContexts` | `0x3F470` | 1,105 | UnwindData |  |
| 18 | `wiasGetContextFromName` | `0x3F8D0` | 570 | UnwindData |  |
| 20 | `wiasGetImageInformation` | `0x3FB10` | 568 | UnwindData |  |
| 21 | `wiasGetItemType` | `0x3FD50` | 282 | UnwindData |  |
| 22 | `wiasGetPropertyAttributes` | `0x3FE70` | 413 | UnwindData |  |
| 24 | `wiasIsPropChanged` | `0x40020` | 428 | UnwindData |  |
| 25 | `wiasParseEndorserString` | `0x401E0` | 1,779 | UnwindData |  |
| 26 | `wiasPrintDebugHResult` | `0x408E0` | 99 | UnwindData |  |
| 28 | `wiasReadMultiple` | `0x40950` | 500 | UnwindData |  |
| 29 | `wiasReadPropBin` | `0x40B50` | 644 | UnwindData |  |
| 30 | `wiasReadPropFloat` | `0x40DE0` | 520 | UnwindData |  |
| 31 | `wiasReadPropGuid` | `0x40FF0` | 556 | UnwindData |  |
| 33 | `wiasReadPropStr` | `0x41230` | 763 | UnwindData |  |
| 34 | `wiasSendEndOfPage` | `0x41540` | 284 | UnwindData |  |
| 37 | `wiasSetPropChanged` | `0x41670` | 377 | UnwindData |  |
| 39 | `wiasSetValidFlag` | `0x417F0` | 459 | UnwindData |  |
| 40 | `wiasSetValidListFloat` | `0x419D0` | 597 | UnwindData |  |
| 41 | `wiasSetValidListGuid` | `0x41C30` | 608 | UnwindData |  |
| 42 | `wiasSetValidListLong` | `0x41EA0` | 600 | UnwindData |  |
| 43 | `wiasSetValidListStr` | `0x42100` | 839 | UnwindData |  |
| 44 | `wiasSetValidRangeFloat` | `0x42450` | 496 | UnwindData |  |
| 45 | `wiasSetValidRangeLong` | `0x42650` | 655 | UnwindData |  |
| 46 | `wiasUpdateScanRect` | `0x428F0` | 505 | UnwindData |  |
| 47 | `wiasUpdateValidFormat` | `0x42AF0` | 1,491 | UnwindData |  |
| 48 | `wiasValidateItemProperties` | `0x430D0` | 914 | UnwindData |  |
| 49 | `wiasWriteBufToFile` | `0x43470` | 388 | UnwindData |  |
| 50 | `wiasWriteMultiple` | `0x43600` | 854 | UnwindData |  |
| 51 | `wiasWritePageBufToFile` | `0x43960` | 432 | UnwindData |  |
| 52 | `wiasWritePageBufToStream` | `0x43B20` | 411 | UnwindData |  |
| 53 | `wiasWritePropBin` | `0x43CD0` | 809 | UnwindData |  |
| 54 | `wiasWritePropFloat` | `0x44000` | 712 | UnwindData |  |
| 55 | `wiasWritePropGuid` | `0x442D0` | 841 | UnwindData |  |
| 57 | `wiasWritePropStr` | `0x44620` | 660 | UnwindData |  |
| 4 | `wiasCreateChildAppItem` | `0x45060` | 579 | UnwindData |  |
