# Binary Specification: unattend.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\unattend.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f35097dfbb1603caa817223f24d123552ad3b5bdb38e231c1ae1fb02774b1989`
* **Total Exported Functions:** 78

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x20C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllMain` | `0x20D0` | 32 | UnwindData |  |
| 1 | `Sysprep_Specialize_Offline_Unattend` | `0x7AA0` | 611 | UnwindData |  |
| 2 | `Sysprep_Specialize_Unattend` | `0x7D10` | 39 | UnwindData |  |
| 5 | `UnattendAddResults` | `0x9770` | 166 | UnwindData |  |
| 7 | `UnattendCtxAddOrModifyNodeText` | `0x9820` | 67 | UnwindData |  |
| 8 | `UnattendCtxBeginModify` | `0x9870` | 92 | UnwindData |  |
| 9 | `UnattendCtxCancelModify` | `0x98E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `UnattendCtxCleanup` | `0x9900` | 67 | UnwindData |  |
| 11 | `UnattendCtxCommitModify` | `0x9950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `UnattendCtxCompareNodes` | `0x9970` | 276 | UnwindData |  |
| 13 | `UnattendCtxDeserialize` | `0x9A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `UnattendCtxDeserializeBuffer` | `0x9AA0` | 148 | UnwindData |  |
| 15 | `UnattendCtxDeserializeFile` | `0x9B40` | 258 | UnwindData |  |
| 16 | `UnattendCtxDeserializeString` | `0x9C50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `UnattendCtxDeserializeWithResults` | `0x9C90` | 351 | UnwindData |  |
| 20 | `UnattendCtxGetCount` | `0x9E00` | 58 | UnwindData |  |
| 21 | `UnattendCtxGetCountByNode` | `0x9E40` | 149 | UnwindData |  |
| 22 | `UnattendCtxGetEnumValue` | `0x9EE0` | 96 | UnwindData |  |
| 23 | `UnattendCtxGetEnumValueByNode` | `0x9F50` | 96 | UnwindData |  |
| 24 | `UnattendCtxGetExpandedString` | `0x9FC0` | 135 | UnwindData |  |
| 25 | `UnattendCtxGetExpandedStringByNode` | `0xA050` | 133 | UnwindData |  |
| 26 | `UnattendCtxGetFlag` | `0xA0E0` | 74 | UnwindData |  |
| 27 | `UnattendCtxGetFlagByNode` | `0xA130` | 73 | UnwindData |  |
| 28 | `UnattendCtxGetLong` | `0xA180` | 128 | UnwindData |  |
| 29 | `UnattendCtxGetLongByNode` | `0xA210` | 182 | UnwindData |  |
| 30 | `UnattendCtxGetNodeAttr` | `0xA2D0` | 167 | UnwindData |  |
| 31 | `UnattendCtxGetNodeChild` | `0xA380` | 185 | UnwindData |  |
| 32 | `UnattendCtxGetNodePath` | `0xA440` | 648 | UnwindData |  |
| 33 | `UnattendCtxGetNodeValue` | `0xA6D0` | 67 | UnwindData |  |
| 34 | `UnattendCtxGetRootNode` | `0xA7E0` | 110 | UnwindData |  |
| 37 | `UnattendCtxGetString` | `0xA860` | 63 | UnwindData |  |
| 38 | `UnattendCtxGetStringByNode` | `0xA8B0` | 62 | UnwindData |  |
| 39 | `UnattendCtxGetUlong` | `0xA900` | 128 | UnwindData |  |
| 40 | `UnattendCtxGetUlongByNode` | `0xA990` | 182 | UnwindData |  |
| 41 | `UnattendCtxOpenNode` | `0xAA50` | 58 | UnwindData |  |
| 42 | `UnattendCtxOpenNodeByNode` | `0xAA90` | 58 | UnwindData |  |
| 43 | `UnattendCtxPrettyPrint` | `0xAAD0` | 80 | UnwindData |  |
| 44 | `UnattendCtxRemoveAttr` | `0xABF0` | 62 | UnwindData |  |
| 45 | `UnattendCtxRemoveNode` | `0xAC40` | 62 | UnwindData |  |
| 46 | `UnattendCtxReplaceMatchedNodesWithText` | `0xAC90` | 344 | UnwindData |  |
| 47 | `UnattendCtxReplaceNode` | `0xADF0` | 491 | UnwindData |  |
| 48 | `UnattendCtxSerialize` | `0xAFF0` | 146 | UnwindData |  |
| 50 | `UnattendCtxSerializeToBuffer` | `0xB090` | 120 | UnwindData |  |
| 51 | `UnattendCtxSerializeToBufferFromNode` | `0xB110` | 77 | UnwindData |  |
| 54 | `UnattendCtxSetNodeName` | `0xB170` | 67 | UnwindData |  |
| 55 | `UnattendCtxSetString` | `0xB1C0` | 95 | UnwindData |  |
| 56 | `UnattendCtxSetStringByNode` | `0xB230` | 124 | UnwindData |  |
| 57 | `UnattendCtxSpliceTrees` | `0xB2C0` | 103 | UnwindData |  |
| 66 | `UnattendFreeNode` | `0xB330` | 119 | UnwindData |  |
| 67 | `UnattendFreeResults` | `0xB3B0` | 36 | UnwindData |  |
| 68 | `UnattendFreeSetting` | `0xB3E0` | 228 | UnwindData |  |
| 70 | `UnattendGetFirstFailingSetting` | `0xB570` | 417 | UnwindData |  |
| 74 | `UnattendIsNodeValid` | `0xB8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `UnattendCleanup` | `0xB910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `UnattendDeserializeWithResults` | `0xB930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `UnattendGetCount` | `0xB950` | 134 | UnwindData |  |
| 71 | `UnattendGetFlag` | `0xB9E0` | 81 | UnwindData |  |
| 72 | `UnattendGetImplicitContext` | `0xBA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `UnattendGetString` | `0xBA60` | 124 | UnwindData |  |
| 18 | `UnattendCtxEnumGet` | `0xBF50` | 161 | UnwindData |  |
| 19 | `UnattendCtxEnumOrderedSubNodes` | `0xC000` | 329 | UnwindData |  |
| 59 | `UnattendEnumFree` | `0xC150` | 48 | UnwindData |  |
| 65 | `UnattendFormatPath` | `0xC190` | 62 | UnwindData |  |
| 78 | `UnattendVFormatPath` | `0xC1E0` | 378 | UnwindData |  |
| 35 | `UnattendCtxGetShowUI` | `0xC360` | 62 | UnwindData |  |
| 36 | `UnattendCtxGetShowUIFromNode` | `0xC3B0` | 359 | UnwindData |  |
| 49 | `UnattendCtxSerializeSettingsStream` | `0xC7C0` | 250 | UnwindData |  |
| 52 | `UnattendCtxSerializeToStream` | `0xC8C0` | 77 | UnwindData |  |
| 53 | `UnattendCtxSerializeToStreamFromNode` | `0xC920` | 77 | UnwindData |  |
| 60 | `UnattendFindAnswerFile` | `0xDBA0` | 277 | UnwindData |  |
| 61 | `UnattendFindAnswerFileSkipPantherFolder` | `0xDCC0` | 255 | UnwindData |  |
| 62 | `UnattendFindAnswerFileWithResults` | `0xDDD0` | 217 | UnwindData |  |
| 64 | `UnattendFindFileFromCmdLine` | `0xDEB0` | 286 | UnwindData |  |
| 63 | `UnattendFindAnswerPackageWithResults` | `0xEFC0` | 1,989 | UnwindData |  |
| 75 | `UnattendIsPassUnusedInCtx` | `0xF790` | 205 | UnwindData |  |
| 76 | `UnattendMarkPassUsedInCtx` | `0xF870` | 140 | UnwindData |  |
| 77 | `UnattendUsedPassesExistInCtx` | `0xF910` | 122 | UnwindData |  |
