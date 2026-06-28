# Binary Specification: wiaservc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wiaservc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ec9b7ef924981cadb6dafb60141c28f031ef43e2efcb972bbbb858fd1949706b`
* **Total Exported Functions:** 57

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `wiasDebugTrace` | `0x8E50` | 839 | UnwindData |  |
| 11 | `wiasFormatArgs` | `0x10580` | 613 | UnwindData |  |
| 8 | `wiasDebugError` | `0x13BF0` | 481 | UnwindData |  |
| 36 | `wiasSetItemPropNames` | `0x17940` | 381 | UnwindData |  |
| 56 | `wiasWritePropLong` | `0x17AD0` | 688 | UnwindData |  |
| 19 | `wiasGetDrvItem` | `0x17F90` | 353 | UnwindData |  |
| 35 | `wiasSetItemPropAttribs` | `0x18100` | 554 | UnwindData |  |
| 32 | `wiasReadPropLong` | `0x18550` | 512 | UnwindData |  |
| 38 | `wiasSetPropertyAttributes` | `0x18760` | 1,115 | UnwindData |  |
| 23 | `wiasGetRootItem` | `0x23650` | 226 | UnwindData |  |
| 1 | `ServiceMain` | `0x34DC0` | 1,218 | UnwindData |  |
| 2 | `DllRegisterServer` | `0x36F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllUnregisterServer` | `0x36F50` | 16,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `wiasQueueEvent` | `0x3B000` | 291 | UnwindData |  |
| 5 | `wiasCreateDrvItem` | `0x3DB80` | 755 | UnwindData |  |
| 6 | `wiasCreateLogInstance` | `0x3DE80` | 274 | UnwindData |  |
| 7 | `wiasCreatePropContext` | `0x3DFA0` | 640 | UnwindData |  |
| 10 | `wiasDownSampleBuffer` | `0x3E230` | 797 | UnwindData |  |
| 12 | `wiasFreePropContext` | `0x3E560` | 209 | UnwindData |  |
| 13 | `wiasGetChangedValueFloat` | `0x3E640` | 435 | UnwindData |  |
| 14 | `wiasGetChangedValueGuid` | `0x3E800` | 435 | UnwindData |  |
| 15 | `wiasGetChangedValueLong` | `0x3E9C0` | 435 | UnwindData |  |
| 16 | `wiasGetChangedValueStr` | `0x3EB80` | 435 | UnwindData |  |
| 17 | `wiasGetChildrenContexts` | `0x3ED40` | 1,105 | UnwindData |  |
| 18 | `wiasGetContextFromName` | `0x3F1A0` | 570 | UnwindData |  |
| 20 | `wiasGetImageInformation` | `0x3F3E0` | 568 | UnwindData |  |
| 21 | `wiasGetItemType` | `0x3F620` | 282 | UnwindData |  |
| 22 | `wiasGetPropertyAttributes` | `0x3F740` | 413 | UnwindData |  |
| 24 | `wiasIsPropChanged` | `0x3F8F0` | 428 | UnwindData |  |
| 25 | `wiasParseEndorserString` | `0x3FAB0` | 1,757 | UnwindData |  |
| 26 | `wiasPrintDebugHResult` | `0x401A0` | 99 | UnwindData |  |
| 28 | `wiasReadMultiple` | `0x40210` | 500 | UnwindData |  |
| 29 | `wiasReadPropBin` | `0x40410` | 644 | UnwindData |  |
| 30 | `wiasReadPropFloat` | `0x406A0` | 520 | UnwindData |  |
| 31 | `wiasReadPropGuid` | `0x408B0` | 556 | UnwindData |  |
| 33 | `wiasReadPropStr` | `0x40AF0` | 763 | UnwindData |  |
| 34 | `wiasSendEndOfPage` | `0x40E00` | 284 | UnwindData |  |
| 37 | `wiasSetPropChanged` | `0x40F30` | 377 | UnwindData |  |
| 39 | `wiasSetValidFlag` | `0x410B0` | 459 | UnwindData |  |
| 40 | `wiasSetValidListFloat` | `0x41290` | 597 | UnwindData |  |
| 41 | `wiasSetValidListGuid` | `0x414F0` | 608 | UnwindData |  |
| 42 | `wiasSetValidListLong` | `0x41760` | 600 | UnwindData |  |
| 43 | `wiasSetValidListStr` | `0x419C0` | 839 | UnwindData |  |
| 44 | `wiasSetValidRangeFloat` | `0x41D10` | 496 | UnwindData |  |
| 45 | `wiasSetValidRangeLong` | `0x41F10` | 655 | UnwindData |  |
| 46 | `wiasUpdateScanRect` | `0x421B0` | 505 | UnwindData |  |
| 47 | `wiasUpdateValidFormat` | `0x423B0` | 1,491 | UnwindData |  |
| 48 | `wiasValidateItemProperties` | `0x42990` | 914 | UnwindData |  |
| 49 | `wiasWriteBufToFile` | `0x42D30` | 388 | UnwindData |  |
| 50 | `wiasWriteMultiple` | `0x42EC0` | 854 | UnwindData |  |
| 51 | `wiasWritePageBufToFile` | `0x43220` | 432 | UnwindData |  |
| 52 | `wiasWritePageBufToStream` | `0x433E0` | 411 | UnwindData |  |
| 53 | `wiasWritePropBin` | `0x43590` | 809 | UnwindData |  |
| 54 | `wiasWritePropFloat` | `0x438C0` | 712 | UnwindData |  |
| 55 | `wiasWritePropGuid` | `0x43B90` | 841 | UnwindData |  |
| 57 | `wiasWritePropStr` | `0x43EE0` | 660 | UnwindData |  |
| 4 | `wiasCreateChildAppItem` | `0x44530` | 579 | UnwindData |  |
