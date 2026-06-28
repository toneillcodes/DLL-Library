# Binary Specification: ServicingCommon.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ServicingCommon.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a54ace98ea9410deb2d76ab2e996a31bd08b635979d7e10f8cbbadbd0eaabdfa`
* **Total Exported Functions:** 192

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `CbsFindServicingStackDirectory` | `0x256C0` | 904 | UnwindData |  |
| 101 | `RtlFinalizeSmartLBlobUcsWritingContext` | `0x26000` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `RtlFinalizeSmartLBlobWritingContext` | `0x26000` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CbsCreateOfflineSession` | `0x260E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `CbsOfflineFinalize` | `0x26100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `CbsOfflineFinalizeNoShutdownImageStack` | `0x26120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CbsOfflineSetLogFile` | `0x26140` | 72 | UnwindData |  |
| 7 | `CbsCreateOfflineSessionFromStackInImage` | `0x27490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CbsGetSsBinaryPathFromTargetImage` | `0x274B0` | 35 | UnwindData |  |
| 10 | `CbsLoadSssFromTargetImage` | `0x27540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `CbsShutdownImageStack` | `0x27560` | 84,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `CreateSafeOSForRecovery` | `0x3BDC0` | 1,180 | UnwindData |  |
| 21 | `EstimateReconstructWindowsDiskNeeds` | `0x3C270` | 798 | UnwindData |  |
| 22 | `EstimateReconstructWindowsRAMNeeds` | `0x3C5A0` | 47 | UnwindData |  |
| 33 | `ReconstructWindowsEx` | `0x3C5E0` | 88 | UnwindData |  |
| 34 | `ReconstructWindowsEx2` | `0x3C640` | 95 | UnwindData |  |
| 49 | `RtlCommitSmartLBlobUcsWritingContext` | `0x46350` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `RtlCommitSmartLBlobWritingContext` | `0x46350` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CBSWdsLog` | `0x465E0` | 570 | UnwindData |  |
| 4 | `SetCustomLogging` | `0x473C0` | 4,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `RecursiveCopy` | `0x48730` | 528 | UnwindData |  |
| 23 | `FileVersionFromString` | `0x4C1A0` | 323 | UnwindData |  |
| 179 | `SczAlloc` | `0x4C800` | 222 | UnwindData |  |
| 180 | `SczAllocConcat2Sz` | `0x4C9D0` | 417 | UnwindData |  |
| 181 | `SczAllocConcatSz` | `0x4CB80` | 344 | UnwindData |  |
| 182 | `SczAllocFormatted` | `0x4CCE0` | 150 | UnwindData |  |
| 183 | `SczAllocFromAnsiSz` | `0x4CF80` | 333 | UnwindData |  |
| 184 | `SczAllocFromSz` | `0x4D0E0` | 190 | UnwindData |  |
| 185 | `SczAllocPrefixSz` | `0x4D3A0` | 366 | UnwindData |  |
| 186 | `SczEnsureBackslashTerminated` | `0x4D5F0` | 116 | UnwindData |  |
| 187 | `SczFree` | `0x4D670` | 21 | UnwindData |  |
| 190 | `StringsAreEqualCaseInsensitive` | `0x4D6F0` | 47 | UnwindData |  |
| 191 | `SzEnsureBackslashTerminated` | `0x4D730` | 119 | UnwindData |  |
| 65 | `RtlCreateDefaultMicrodomXmlWriter` | `0x51980` | 535 | UnwindData |  |
| 170 | `RtlWriteMicrodomXml` | `0x51BA0` | 476 | UnwindData |  |
| 66 | `RtlCreateDefaultXmlWriter` | `0x53070` | 439 | UnwindData |  |
| 67 | `RtlCreateFilteringMicrodomWriter` | `0x53E70` | 406 | UnwindData |  |
| 68 | `RtlCreateMicrodom` | `0x5B030` | 2,998 | UnwindData |  |
| 69 | `RtlCreateMicrodomUpdateContext` | `0x5ED00` | 303 | UnwindData |  |
| 70 | `RtlCreateUpdatedMicrodomAsMicrodom` | `0x5EE40` | 308 | UnwindData |  |
| 71 | `RtlCreateUpdatedMicrodomAsUtf8` | `0x5EF80` | 313 | UnwindData |  |
| 80 | `RtlDestroyMicrodomUpdateContext` | `0x5F0C0` | 160 | UnwindData |  |
| 135 | `RtlMicrodomUpdateCreateAttributeNs` | `0x5F170` | 424 | UnwindData |  |
| 136 | `RtlMicrodomUpdateCreateElementNs` | `0x5F320` | 623 | UnwindData |  |
| 137 | `RtlMicrodomUpdateCreateTextual` | `0x5F5A0` | 299 | UnwindData |  |
| 138 | `RtlMicrodomUpdateGetCookieForExistingAttribute` | `0x5F6E0` | 135 | UnwindData |  |
| 139 | `RtlMicrodomUpdateGetCookieForExistingNode` | `0x5F770` | 152 | UnwindData |  |
| 140 | `RtlMicrodomUpdateInsertChild` | `0x5F810` | 358 | UnwindData |  |
| 141 | `RtlMicrodomUpdateInsertMicrodomNodeEx` | `0x5F980` | 730 | UnwindData |  |
| 142 | `RtlMicrodomUpdateRemoveChild` | `0x5FC60` | 259 | UnwindData |  |
| 143 | `RtlMicrodomUpdateRemoveElement` | `0x5FD70` | 159 | UnwindData |  |
| 144 | `RtlMicrodomUpdateSetNodeName` | `0x5FE20` | 286 | UnwindData |  |
| 145 | `RtlMicrodomUpdateSetNodeTextContent` | `0x5FF50` | 291 | UnwindData |  |
| 79 | `RtlDestroyGrowingList` | `0x60210` | 137 | UnwindData |  |
| 113 | `RtlIndexIntoGrowingList` | `0x602A0` | 236 | UnwindData |  |
| 117 | `RtlInitializeGrowingList` | `0x603A0` | 148 | UnwindData |  |
| 99 | `RtlExecuteXPathOverMicrodom` | `0x62510` | 1,194 | UnwindData |  |
| 147 | `RtlNsDestroy` | `0x62B50` | 78 | UnwindData |  |
| 148 | `RtlNsInitialize` | `0x62CB0` | 171 | UnwindData |  |
| 171 | `RtlXmlDefaultCompareStrings` | `0x659C0` | 139 | UnwindData |  |
| 173 | `RtlXmlDetermineStreamEncoding` | `0x65C20` | 711 | UnwindData |  |
| 176 | `RtlXmlInitializeTokenization` | `0x65EF0` | 218 | UnwindData |  |
| 178 | `RtlXmlNextToken` | `0x65FD0` | 5,432 | UnwindData |  |
| 172 | `RtlXmlDestroyNextLogicalThing` | `0x67FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `RtlXmlExtentToString` | `0x68000` | 490 | UnwindData |  |
| 175 | `RtlXmlInitializeNextLogicalThing` | `0x68540` | 319 | UnwindData |  |
| 177 | `RtlXmlNextLogicalThing` | `0x68690` | 20 | UnwindData |  |
| 37 | `RtlAllocateLBlob` | `0x704F0` | 142 | UnwindData |  |
| 46 | `RtlBase64EncodeLBlobToLUnicodeString` | `0x70710` | 530 | UnwindData |  |
| 47 | `RtlBase64EncodeLBlobToLUtf8String` | `0x70930` | 530 | UnwindData |  |
| 51 | `RtlCompareEncodedLBlobs` | `0x70B50` | 848 | UnwindData |  |
| 75 | `RtlDecodeBase64LUnicodeStringToLBlob` | `0x71000` | 498 | UnwindData |  |
| 76 | `RtlDecodeBase64LUtf8StringToLBlob` | `0x71200` | 562 | UnwindData |  |
| 82 | `RtlDetermineTranscodedLBlobSize` | `0x71440` | 984 | UnwindData |  |
| 85 | `RtlDuplicateLBlob` | `0x71820` | 364 | UnwindData |  |
| 103 | `RtlFreeLBlob` | `0x719A0` | 29 | UnwindData |  |
| 104 | `RtlFreeLUnicodeString` | `0x719A0` | 29 | UnwindData |  |
| 105 | `RtlFreeLUtf8String` | `0x719A0` | 29 | UnwindData |  |
| 109 | `RtlGetHashAlgorithmHashLength` | `0x719D0` | 282 | UnwindData |  |
| 110 | `RtlHashLBlob` | `0x722B0` | 745 | UnwindData |  |
| 118 | `RtlInitializeSmartLBlobWritingContext` | `0x725A0` | 468 | UnwindData |  |
| 121 | `RtlIsLBlobValid` | `0x72780` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `RtlMatchEncodedLBlobAgainstList` | `0x727B0` | 165 | UnwindData |  |
| 126 | `RtlMatchEncodedLBlobAgainstPointerList` | `0x72860` | 162 | UnwindData |  |
| 150 | `RtlPreInitializeSmartLBlobWritingContext` | `0x72910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `RtlReallocateLBlob` | `0x72930` | 388 | UnwindData |  |
| 162 | `RtlSplitEncodedLBlob` | `0x72AC0` | 1,407 | UnwindData |  |
| 166 | `RtlTranscodeLBlobs` | `0x73050` | 1,734 | UnwindData |  |
| 168 | `RtlWriteDataIntoSmartLBlobWritingContext` | `0x73720` | 805 | UnwindData |  |
| 38 | `RtlAllocateLUnicodeString` | `0x73D50` | 225 | UnwindData |  |
| 40 | `RtlAllocateUnicodeString` | `0x73E40` | 216 | UnwindData |  |
| 41 | `RtlAppendLUnicodeStringToLUnicodeString` | `0x73F20` | 394 | UnwindData |  |
| 43 | `RtlAppendUcsCharacterToLUnicodeString` | `0x74260` | 60 | UnwindData |  |
| 45 | `RtlAppendUcsCharactersToLUnicodeString` | `0x742B0` | 441 | UnwindData |  |
| 53 | `RtlCompareLUnicodeStrings` | `0x74470` | 42 | UnwindData |  |
| 56 | `RtlConcatenateLUnicodeStrings` | `0x744A0` | 587 | UnwindData |  |
| 62 | `RtlCopyLUnicodeString` | `0x74700` | 296 | UnwindData |  |
| 74 | `RtlDeallocateUnicodeString` | `0x74830` | 29 | UnwindData |  |
| 81 | `RtlDetermineFilteredLUnicodeStringLength` | `0x74860` | 386 | UnwindData |  |
| 83 | `RtlDoesLUnicodeStringMatchExpression` | `0x749F0` | 1,387 | UnwindData |  |
| 86 | `RtlDuplicateLUnicodeString` | `0x75040` | 216 | UnwindData |  |
| 88 | `RtlDuplicateLUnicodeStringToUnicodeString` | `0x75120` | 397 | UnwindData |  |
| 91 | `RtlDuplicateNullTerminatedStringToLUnicodeString` | `0x752C0` | 137 | UnwindData |  |
| 92 | `RtlDuplicateUnicodeStringToLUnicodeString` | `0x75350` | 215 | UnwindData |  |
| 95 | `RtlEqualLUnicodeStringPrefix` | `0x75430` | 56 | UnwindData |  |
| 96 | `RtlEqualLUnicodeStrings` | `0x75470` | 121 | UnwindData |  |
| 100 | `RtlFilterLUnicodeString` | `0x754F0` | 387 | UnwindData |  |
| 111 | `RtlHashLUnicodeString` | `0x75680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `RtlInitLUnicodeStringFromNullTerminatedString` | `0x756A0` | 153 | UnwindData |  |
| 115 | `RtlInitLUnicodeStringFromUnicodeString` | `0x75740` | 135 | UnwindData |  |
| 116 | `RtlInitUnicodeStringFromLUnicodeString` | `0x757D0` | 363 | UnwindData |  |
| 122 | `RtlIsLUnicodeStringValid` | `0x75950` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `RtlMatchLUnicodeStringAgainstLUtf8StringList` | `0x759C0` | 502 | UnwindData |  |
| 128 | `RtlMatchLUnicodeStringAgainstLUtf8StringPointerList` | `0x75BC0` | 488 | UnwindData |  |
| 129 | `RtlMatchLUnicodeStringAgainstList` | `0x75DB0` | 495 | UnwindData |  |
| 130 | `RtlMatchLUnicodeStringAgainstPointerList` | `0x75FB0` | 481 | UnwindData |  |
| 152 | `RtlReallocateLUnicodeString` | `0x761A0` | 277 | UnwindData |  |
| 154 | `RtlReallocateUnicodeString` | `0x762C0` | 498 | UnwindData |  |
| 163 | `RtlSplitLUnicodeString` | `0x764C0` | 811 | UnwindData |  |
| 39 | `RtlAllocateLUtf8String` | `0x76800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `RtlAppendLUtf8StringToLUtf8String` | `0x76810` | 387 | UnwindData |  |
| 44 | `RtlAppendUcsCharacterToLUtf8String` | `0x769A0` | 314 | UnwindData |  |
| 48 | `RtlCalculateUtf16StringLengthFromLUtf8String` | `0x76AE0` | 441 | UnwindData |  |
| 52 | `RtlCompareLUnicodeStringToLUtf8String` | `0x76CA0` | 42 | UnwindData |  |
| 54 | `RtlCompareLUtf8StringToLUnicodeString` | `0x76CD0` | 42 | UnwindData |  |
| 55 | `RtlCompareLUtf8Strings` | `0x76D00` | 42 | UnwindData |  |
| 57 | `RtlConcatenateLUtf8Strings` | `0x76D30` | 589 | UnwindData |  |
| 63 | `RtlCopyLUtf8String` | `0x76F90` | 296 | UnwindData |  |
| 64 | `RtlCopyLUtf8StringToLUnicodeString` | `0x770C0` | 257 | UnwindData |  |
| 87 | `RtlDuplicateLUnicodeStringToLUtf8String` | `0x771D0` | 213 | UnwindData |  |
| 89 | `RtlDuplicateLUtf8String` | `0x772B0` | 216 | UnwindData |  |
| 90 | `RtlDuplicateLUtf8StringToLUnicodeString` | `0x77390` | 211 | UnwindData |  |
| 97 | `RtlEqualLUtf8StringPrefix` | `0x77470` | 322 | UnwindData |  |
| 98 | `RtlEqualLUtf8Strings` | `0x775C0` | 158 | UnwindData |  |
| 112 | `RtlHashLUtf8String` | `0x77670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `RtlIsLUtf8StringValid` | `0x77690` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `RtlMatchLUtf8StringAgainstLUnicodeStringList` | `0x776C0` | 502 | UnwindData |  |
| 132 | `RtlMatchLUtf8StringAgainstLUnicodeStringPointerList` | `0x778C0` | 488 | UnwindData |  |
| 133 | `RtlMatchLUtf8StringAgainstList` | `0x77AB0` | 495 | UnwindData |  |
| 134 | `RtlMatchLUtf8StringAgainstPointerList` | `0x77CB0` | 481 | UnwindData |  |
| 153 | `RtlReallocateLUtf8String` | `0x77EA0` | 226 | UnwindData |  |
| 164 | `RtlSplitLUtf8String` | `0x77F90` | 624 | UnwindData |  |
| 119 | `RtlInitializeSmartLUnicodeStringWritingContext` | `0x78580` | 300 | UnwindData |  |
| 120 | `RtlInitializeSmartLUtf8StringWritingContext` | `0x786C0` | 73 | UnwindData |  |
| 108 | `RtlGetEncodingSizeUtf8` | `0x78710` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `RtlLengthOfUcsCharacterEncodedAsUtf8` | `0x78710` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `RtlPreInitializeSmartLBlobUcsWritingContext` | `0x78770` | 37 | UnwindData |  |
| 158 | `RtlSmartMultiUcsEncoder_Utf16LE` | `0x787A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `RtlSmartMultiUcsEncoder_Utf8` | `0x787B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `RtlSmartUcsEncoder_Utf16LE` | `0x787C0` | 60 | UnwindData |  |
| 161 | `RtlSmartUcsEncoder_Utf8` | `0x78810` | 60 | UnwindData |  |
| 169 | `RtlWriteDecodedUcsDataIntoSmartLBlobUcsWritingContext` | `0x78860` | 660 | UnwindData |  |
| 58 | `RtlConvertNtFilePathToWin32FilePath` | `0x79240` | 1,047 | UnwindData |  |
| 59 | `RtlConvertNtRegistryPathToWin32RegistryPath` | `0x79660` | 171 | UnwindData |  |
| 60 | `RtlConvertWin32FilePathToNtFilePath` | `0x79720` | 752 | UnwindData |  |
| 61 | `RtlConvertWin32RegistryPathToNtRegistryPath` | `0x79A20` | 331 | UnwindData |  |
| 165 | `RtlSplitWin32RegistryPathIntoRootAndLeaves` | `0x79B80` | 558 | UnwindData |  |
| 72 | `RtlCreateUtf16LEUCSStringBuilder` | `0x7A630` | 392 | UnwindData |  |
| 73 | `RtlCreateUtf8UCSStringBuilder` | `0x7A7C0` | 382 | UnwindData |  |
| 77 | `RtlDecodeUtf16LE` | `0x7AB40` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `RtlDecodeUtf8` | `0x7ABD0` | 708 | UnwindData |  |
| 84 | `RtlDowncaseUCSCharacter` | `0x7B000` | 58 | UnwindData |  |
| 167 | `RtlUpcaseUCSCharacter` | `0x7B040` | 58 | UnwindData |  |
| 93 | `RtlEncodeUtf16LE` | `0x7B260` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `RtlEncodeUtf8` | `0x7B3E0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `RtlGetEncodingSizeUcs2` | `0x7B710` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `RtlGetEncodingSizeUtf16` | `0x7B740` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `RtlMurmurHashLBlob` | `0x7BA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `RtlRegisterErrorOriginationCallback` | `0x7BA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `RtlReportErrorOrigination` | `0x7BA30` | 153 | UnwindData |  |
| 157 | `RtlReportErrorPropagation` | `0x7BAD0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `ConvertHResultToNtStatus` | `0x7BC80` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ConvertNtStatusToHResult` | `0x7BF10` | 1,093 | UnwindData |  |
| 26 | `GetLoadedHiveKeyName` | `0x7CB30` | 30 | UnwindData |  |
| 28 | `GetTemporaryPath` | `0x7CCA0` | 553 | UnwindData |  |
| 24 | `GetCWcpDll` | `0x7F5E0` | 204 | UnwindData |  |
| 2 | `CreateKeyformFromAttributesIntoBuffer` | `0x7FF60` | 1,744 | UnwindData |  |
| 20 | `DecompressManifest` | `0x81020` | 457 | UnwindData |  |
| 188 | `SfpCreateOfflineRepairObject` | `0x86E50` | 671 | UnwindData |  |
| 189 | `SfpUnload` | `0x87100` | 250 | UnwindData |  |
| 29 | `GetUpdateReserveManagerLoader` | `0x87AC0` | 263 | UnwindData |  |
| 32 | `LoadUpdateReserveManager` | `0x87BD0` | 125 | UnwindData |  |
| 5 | `BeginFileMapEnumerationInternal` | `0x88810` | 868 | UnwindData |  |
| 15 | `CloseFileMapEnumerationInternal` | `0x88B80` | 49 | UnwindData |  |
| 27 | `GetNextFileMapContentInternal` | `0x88BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `IsLuaCdfFile` | `0x88BD0` | 641 | UnwindData |  |
| 16 | `CompareObjectSDToSddl` | `0x89030` | 1,825 | UnwindData |  |
| 30 | `IsKeyProtected` | `0x89B60` | 413 | UnwindData |  |
| 35 | `RemoveFileProtection` | `0x8AAB0` | 277 | UnwindData |  |
| 36 | `RemoveRegKeyProtection` | `0x8AE10` | 385 | UnwindData |  |
| 25 | `GetIdentityAuthority` | `0x8E4B0` | 303 | UnwindData |  |
| 192 | `UninstallWindows` | `0x90730` | 1,307 | UnwindData |  |
