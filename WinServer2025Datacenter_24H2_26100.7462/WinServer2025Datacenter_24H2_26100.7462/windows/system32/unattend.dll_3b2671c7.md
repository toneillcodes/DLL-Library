# Binary Specification: unattend.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\unattend.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3b2671c7ccc15e23a374e1296a4ac39336e6e6bb9cd98213e54ea87a3a48b138`
* **Total Exported Functions:** 78

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x2090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllMain` | `0x20A0` | 32 | UnwindData |  |
| 1 | `Sysprep_Specialize_Offline_Unattend` | `0x79A0` | 611 | UnwindData |  |
| 2 | `Sysprep_Specialize_Unattend` | `0x7C10` | 39 | UnwindData |  |
| 5 | `UnattendAddResults` | `0x9650` | 166 | UnwindData |  |
| 7 | `UnattendCtxAddOrModifyNodeText` | `0x9700` | 67 | UnwindData |  |
| 8 | `UnattendCtxBeginModify` | `0x9750` | 92 | UnwindData |  |
| 9 | `UnattendCtxCancelModify` | `0x97C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `UnattendCtxCleanup` | `0x97E0` | 67 | UnwindData |  |
| 11 | `UnattendCtxCommitModify` | `0x9830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `UnattendCtxCompareNodes` | `0x9850` | 276 | UnwindData |  |
| 13 | `UnattendCtxDeserialize` | `0x9970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `UnattendCtxDeserializeBuffer` | `0x9980` | 148 | UnwindData |  |
| 15 | `UnattendCtxDeserializeFile` | `0x9A20` | 258 | UnwindData |  |
| 16 | `UnattendCtxDeserializeString` | `0x9B30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `UnattendCtxDeserializeWithResults` | `0x9B70` | 351 | UnwindData |  |
| 20 | `UnattendCtxGetCount` | `0x9CE0` | 58 | UnwindData |  |
| 21 | `UnattendCtxGetCountByNode` | `0x9D20` | 149 | UnwindData |  |
| 22 | `UnattendCtxGetEnumValue` | `0x9DC0` | 96 | UnwindData |  |
| 23 | `UnattendCtxGetEnumValueByNode` | `0x9E30` | 96 | UnwindData |  |
| 24 | `UnattendCtxGetExpandedString` | `0x9EA0` | 135 | UnwindData |  |
| 25 | `UnattendCtxGetExpandedStringByNode` | `0x9F30` | 133 | UnwindData |  |
| 26 | `UnattendCtxGetFlag` | `0x9FC0` | 74 | UnwindData |  |
| 27 | `UnattendCtxGetFlagByNode` | `0xA010` | 73 | UnwindData |  |
| 28 | `UnattendCtxGetLong` | `0xA060` | 128 | UnwindData |  |
| 29 | `UnattendCtxGetLongByNode` | `0xA0F0` | 182 | UnwindData |  |
| 30 | `UnattendCtxGetNodeAttr` | `0xA1B0` | 167 | UnwindData |  |
| 31 | `UnattendCtxGetNodeChild` | `0xA260` | 185 | UnwindData |  |
| 32 | `UnattendCtxGetNodePath` | `0xA320` | 648 | UnwindData |  |
| 33 | `UnattendCtxGetNodeValue` | `0xA5B0` | 67 | UnwindData |  |
| 34 | `UnattendCtxGetRootNode` | `0xA6C0` | 110 | UnwindData |  |
| 37 | `UnattendCtxGetString` | `0xA740` | 63 | UnwindData |  |
| 38 | `UnattendCtxGetStringByNode` | `0xA790` | 62 | UnwindData |  |
| 39 | `UnattendCtxGetUlong` | `0xA7E0` | 128 | UnwindData |  |
| 40 | `UnattendCtxGetUlongByNode` | `0xA870` | 182 | UnwindData |  |
| 41 | `UnattendCtxOpenNode` | `0xA930` | 58 | UnwindData |  |
| 42 | `UnattendCtxOpenNodeByNode` | `0xA970` | 58 | UnwindData |  |
| 43 | `UnattendCtxPrettyPrint` | `0xA9B0` | 80 | UnwindData |  |
| 44 | `UnattendCtxRemoveAttr` | `0xAAD0` | 62 | UnwindData |  |
| 45 | `UnattendCtxRemoveNode` | `0xAB20` | 62 | UnwindData |  |
| 46 | `UnattendCtxReplaceMatchedNodesWithText` | `0xAB70` | 344 | UnwindData |  |
| 47 | `UnattendCtxReplaceNode` | `0xACD0` | 491 | UnwindData |  |
| 48 | `UnattendCtxSerialize` | `0xAED0` | 146 | UnwindData |  |
| 50 | `UnattendCtxSerializeToBuffer` | `0xAF70` | 120 | UnwindData |  |
| 51 | `UnattendCtxSerializeToBufferFromNode` | `0xAFF0` | 77 | UnwindData |  |
| 54 | `UnattendCtxSetNodeName` | `0xB050` | 67 | UnwindData |  |
| 55 | `UnattendCtxSetString` | `0xB0A0` | 95 | UnwindData |  |
| 56 | `UnattendCtxSetStringByNode` | `0xB110` | 124 | UnwindData |  |
| 57 | `UnattendCtxSpliceTrees` | `0xB1A0` | 103 | UnwindData |  |
| 66 | `UnattendFreeNode` | `0xB210` | 119 | UnwindData |  |
| 67 | `UnattendFreeResults` | `0xB290` | 36 | UnwindData |  |
| 68 | `UnattendFreeSetting` | `0xB2C0` | 228 | UnwindData |  |
| 70 | `UnattendGetFirstFailingSetting` | `0xB450` | 417 | UnwindData |  |
| 74 | `UnattendIsNodeValid` | `0xB7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `UnattendCleanup` | `0xB7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `UnattendDeserializeWithResults` | `0xB810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `UnattendGetCount` | `0xB830` | 134 | UnwindData |  |
| 71 | `UnattendGetFlag` | `0xB8C0` | 81 | UnwindData |  |
| 72 | `UnattendGetImplicitContext` | `0xB920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `UnattendGetString` | `0xB940` | 124 | UnwindData |  |
| 18 | `UnattendCtxEnumGet` | `0xBE30` | 161 | UnwindData |  |
| 19 | `UnattendCtxEnumOrderedSubNodes` | `0xBEE0` | 329 | UnwindData |  |
| 59 | `UnattendEnumFree` | `0xC030` | 48 | UnwindData |  |
| 65 | `UnattendFormatPath` | `0xC070` | 62 | UnwindData |  |
| 78 | `UnattendVFormatPath` | `0xC0C0` | 378 | UnwindData |  |
| 35 | `UnattendCtxGetShowUI` | `0xC240` | 62 | UnwindData |  |
| 36 | `UnattendCtxGetShowUIFromNode` | `0xC290` | 359 | UnwindData |  |
| 49 | `UnattendCtxSerializeSettingsStream` | `0xC6A0` | 250 | UnwindData |  |
| 52 | `UnattendCtxSerializeToStream` | `0xC7A0` | 77 | UnwindData |  |
| 53 | `UnattendCtxSerializeToStreamFromNode` | `0xC800` | 77 | UnwindData |  |
| 60 | `UnattendFindAnswerFile` | `0xDA80` | 277 | UnwindData |  |
| 61 | `UnattendFindAnswerFileSkipPantherFolder` | `0xDBA0` | 255 | UnwindData |  |
| 62 | `UnattendFindAnswerFileWithResults` | `0xDCB0` | 217 | UnwindData |  |
| 64 | `UnattendFindFileFromCmdLine` | `0xDD90` | 286 | UnwindData |  |
| 63 | `UnattendFindAnswerPackageWithResults` | `0xEEA0` | 1,989 | UnwindData |  |
| 75 | `UnattendIsPassUnusedInCtx` | `0xF670` | 205 | UnwindData |  |
| 76 | `UnattendMarkPassUsedInCtx` | `0xF750` | 140 | UnwindData |  |
| 77 | `UnattendUsedPassesExistInCtx` | `0xF7F0` | 122 | UnwindData |  |
