# Binary Specification: msls31.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msls31.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `50b807166a3b02045f77b80a6afba32d30d1dae98f1cacdd96358767e40961e7`
* **Total Exported Functions:** 79

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 43 | `LsQueryLinePointPcp` | `0x1D10` | 261 | UnwindData |  |
| 42 | `LsQueryLineCpPpoint` | `0x26C0` | 42 | UnwindData |  |
| 44 | `LsQueryLineDup` | `0x2B70` | 158 | UnwindData |  |
| 40 | `LsDisplayLine` | `0x2C20` | 110 | UnwindData |  |
| 3 | `LsCreateLine` | `0x3F70` | 120 | UnwindData |  |
| 73 | `LsGetMinDurBreaks` | `0xC790` | 135 | UnwindData |  |
| 80 | `LsLwMultDivR` | `0x11950` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `LsDestroyLine` | `0x120F0` | 89 | UnwindData |  |
| 20 | `LsdnFinishRegular` | `0x123C0` | 85 | UnwindData |  |
| 7 | `LsFetchAppendToCurrentSubline` | `0x12600` | 74 | UnwindData |  |
| 1 | `LsCreateContext` | `0x12960` | 53 | UnwindData |  |
| 2 | `LsDestroyContext` | `0x131D0` | 175 | UnwindData |  |
| 16 | `LsDestroySubline` | `0x141D0` | 366 | UnwindData |  |
| 48 | `LsSetDoc` | `0x179E0` | 54 | UnwindData |  |
| 49 | `LsSetModWidthPairs` | `0x17BA0` | 63 | UnwindData |  |
| 52 | `LsSetBreaking` | `0x187E0` | 63 | UnwindData |  |
| 6 | `LsCreateSubline` | `0x18D10` | 835 | UnwindData |  |
| 68 | `LsFetchAppendToCurrentSublineResume` | `0x19060` | 608 | UnwindData |  |
| 27 | `LsdnQueryObjDimRange` | `0x195D0` | 135 | UnwindData |  |
| 53 | `LssbGetObjDimSubline` | `0x1AE90` | 49 | UnwindData |  |
| 41 | `LsDisplaySubline` | `0x1B180` | 66 | UnwindData |  |
| 59 | `LsPointXYFromPointUV` | `0x1CB20` | 2,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `LsdnSubmitSublines` | `0x1D520` | 808 | UnwindData |  |
| 54 | `LssbGetDupSubline` | `0x1D880` | 5,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `LsEnumLine` | `0x1EF80` | 177 | UnwindData |  |
| 71 | `LsGetReverseLsimethods` | `0x1F9A0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `LsGetWarichuLsimethods` | `0x1FAC0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `LsGetHihLsimethods` | `0x1FBE0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `LsGetRubyLsimethods` | `0x1FD00` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `LsGetTatenakayokoLsimethods` | `0x1FE20` | 1,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `LsFinishCurrentSubline` | `0x204E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `LssbFDonePresSubline` | `0x20520` | 3,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `LsPointUV2FromPointUV1` | `0x212A0` | 147 | UnwindData |  |
| 22 | `LsdnFinishDelete` | `0x22190` | 148 | UnwindData |  |
| 74 | `LsGetLineDur` | `0x269E0` | 135 | UnwindData |  |
| 4 | `LsModifyLineHeight` | `0x26A70` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `LsAppendRunToCurrentSubline` | `0x26AE0` | 425 | UnwindData |  |
| 65 | `LsCompressSubline` | `0x26C90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `LsExpandSubline` | `0x26CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `LsFindNextBreakSubline` | `0x26CE0` | 122 | UnwindData |  |
| 12 | `LsFindPrevBreakSubline` | `0x26D60` | 122 | UnwindData |  |
| 14 | `LsForceBreakSubline` | `0x26DE0` | 110 | UnwindData |  |
| 19 | `LsGetSpecialEffectsSubline` | `0x26E60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `LsMatchPresSubline` | `0x26E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `LsResetRMInCurrentSubline` | `0x26EB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `LsSetBreakSubline` | `0x26EF0` | 88 | UnwindData |  |
| 64 | `LsSqueezeSubline` | `0x26F50` | 78 | UnwindData |  |
| 11 | `LsTruncateSubline` | `0x26FB0` | 157 | UnwindData |  |
| 26 | `LsdnFinishByOneChar` | `0x27060` | 280 | UnwindData |  |
| 23 | `LsdnFinishByPen` | `0x27180` | 390 | UnwindData |  |
| 24 | `LsdnFinishBySubline` | `0x27310` | 458 | UnwindData |  |
| 25 | `LsdnFinishDeleteAll` | `0x274E0` | 454 | UnwindData |  |
| 21 | `LsdnFinishRegularAddAdvancePen` | `0x276B0` | 267 | UnwindData |  |
| 37 | `LsdnDistribute` | `0x277D0` | 339 | UnwindData |  |
| 35 | `LsdnGetCurTabInfo` | `0x27930` | 388 | UnwindData |  |
| 32 | `LsdnGetDup` | `0x27AC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `LsdnGetFormatDepth` | `0x27B20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `LsdnModifyParaEnding` | `0x27B60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `LsdnQueryPenNode` | `0x27BB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `LsdnResetObjDim` | `0x27C00` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `LsdnResetPenNode` | `0x27CA0` | 255 | UnwindData |  |
| 34 | `LsdnResolvePrevTab` | `0x27DB0` | 134 | UnwindData |  |
| 33 | `LsdnSetAbsBaseLine` | `0x27E40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `LsdnSetRigidDup` | `0x27E90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `LsdnSkipCurTab` | `0x27EE0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `LsEnumSubline` | `0x28080` | 58 | UnwindData |  |
| 45 | `LsQueryFLineEmpty` | `0x283A0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `LsQueryTextCellDetails` | `0x28440` | 139 | UnwindData |  |
| 47 | `LsQueryCpPpointSubline` | `0x284E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `LsQueryPointPcpSubline` | `0x28500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `LsSetCompression` | `0x28520` | 215 | UnwindData |  |
| 51 | `LsSetExpansion` | `0x28600` | 207 | UnwindData |  |
| 70 | `LssbFDoneDisplay` | `0x28730` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `LssbFIsSublineEmpty` | `0x28760` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `LssbGetDurTrailInSubline` | `0x28790` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `LssbGetDurTrailWithPensInSubline` | `0x287C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `LssbGetNumberDnodesInSubline` | `0x287F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `LssbGetPlsrunsFromSubline` | `0x28840` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `LssbGetVisibleDcpInSubline` | `0x288A0` | 60,784 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
