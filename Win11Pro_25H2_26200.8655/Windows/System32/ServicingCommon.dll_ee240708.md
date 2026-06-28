# Binary Specification: ServicingCommon.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ServicingCommon.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ee240708b899680e1a765f73bed865bc00992b3cc5b4b581024c87e3b07d3d3f`
* **Total Exported Functions:** 192

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `CbsFindServicingStackDirectory` | `0x256F0` | 904 | UnwindData |  |
| 101 | `RtlFinalizeSmartLBlobUcsWritingContext` | `0x26030` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `RtlFinalizeSmartLBlobWritingContext` | `0x26030` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CbsCreateOfflineSession` | `0x26110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `CbsOfflineFinalize` | `0x26130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `CbsOfflineFinalizeNoShutdownImageStack` | `0x26150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CbsOfflineSetLogFile` | `0x26170` | 72 | UnwindData |  |
| 7 | `CbsCreateOfflineSessionFromStackInImage` | `0x274C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CbsGetSsBinaryPathFromTargetImage` | `0x274E0` | 35 | UnwindData |  |
| 10 | `CbsLoadSssFromTargetImage` | `0x27570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `CbsShutdownImageStack` | `0x27590` | 82,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `CreateSafeOSForRecovery` | `0x3B9C0` | 1,180 | UnwindData |  |
| 21 | `EstimateReconstructWindowsDiskNeeds` | `0x3BE70` | 798 | UnwindData |  |
| 22 | `EstimateReconstructWindowsRAMNeeds` | `0x3C1A0` | 47 | UnwindData |  |
| 33 | `ReconstructWindowsEx` | `0x3C1E0` | 88 | UnwindData |  |
| 34 | `ReconstructWindowsEx2` | `0x3C240` | 95 | UnwindData |  |
| 49 | `RtlCommitSmartLBlobUcsWritingContext` | `0x45F70` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `RtlCommitSmartLBlobWritingContext` | `0x45F70` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CBSWdsLog` | `0x461B0` | 570 | UnwindData |  |
| 4 | `SetCustomLogging` | `0x46B00` | 4,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `RecursiveCopy` | `0x47E30` | 528 | UnwindData |  |
| 23 | `FileVersionFromString` | `0x4B350` | 323 | UnwindData |  |
| 179 | `SczAlloc` | `0x4B9B0` | 222 | UnwindData |  |
| 180 | `SczAllocConcat2Sz` | `0x4BB80` | 417 | UnwindData |  |
| 181 | `SczAllocConcatSz` | `0x4BD30` | 344 | UnwindData |  |
| 182 | `SczAllocFormatted` | `0x4BE90` | 150 | UnwindData |  |
| 183 | `SczAllocFromAnsiSz` | `0x4C130` | 333 | UnwindData |  |
| 184 | `SczAllocFromSz` | `0x4C290` | 190 | UnwindData |  |
| 185 | `SczAllocPrefixSz` | `0x4C550` | 366 | UnwindData |  |
| 186 | `SczEnsureBackslashTerminated` | `0x4C7A0` | 116 | UnwindData |  |
| 187 | `SczFree` | `0x4C820` | 21 | UnwindData |  |
| 190 | `StringsAreEqualCaseInsensitive` | `0x4C8A0` | 47 | UnwindData |  |
| 191 | `SzEnsureBackslashTerminated` | `0x4C8E0` | 119 | UnwindData |  |
| 65 | `RtlCreateDefaultMicrodomXmlWriter` | `0x51020` | 535 | UnwindData |  |
| 170 | `RtlWriteMicrodomXml` | `0x51240` | 476 | UnwindData |  |
| 66 | `RtlCreateDefaultXmlWriter` | `0x52710` | 439 | UnwindData |  |
| 67 | `RtlCreateFilteringMicrodomWriter` | `0x53510` | 406 | UnwindData |  |
| 68 | `RtlCreateMicrodom` | `0x5A6D0` | 2,998 | UnwindData |  |
| 69 | `RtlCreateMicrodomUpdateContext` | `0x5E3A0` | 303 | UnwindData |  |
| 70 | `RtlCreateUpdatedMicrodomAsMicrodom` | `0x5E4E0` | 308 | UnwindData |  |
| 71 | `RtlCreateUpdatedMicrodomAsUtf8` | `0x5E620` | 313 | UnwindData |  |
| 80 | `RtlDestroyMicrodomUpdateContext` | `0x5E760` | 160 | UnwindData |  |
| 135 | `RtlMicrodomUpdateCreateAttributeNs` | `0x5E810` | 424 | UnwindData |  |
| 136 | `RtlMicrodomUpdateCreateElementNs` | `0x5E9C0` | 623 | UnwindData |  |
| 137 | `RtlMicrodomUpdateCreateTextual` | `0x5EC40` | 299 | UnwindData |  |
| 138 | `RtlMicrodomUpdateGetCookieForExistingAttribute` | `0x5ED80` | 135 | UnwindData |  |
| 139 | `RtlMicrodomUpdateGetCookieForExistingNode` | `0x5EE10` | 152 | UnwindData |  |
| 140 | `RtlMicrodomUpdateInsertChild` | `0x5EEB0` | 358 | UnwindData |  |
| 141 | `RtlMicrodomUpdateInsertMicrodomNodeEx` | `0x5F020` | 730 | UnwindData |  |
| 142 | `RtlMicrodomUpdateRemoveChild` | `0x5F300` | 259 | UnwindData |  |
| 143 | `RtlMicrodomUpdateRemoveElement` | `0x5F410` | 159 | UnwindData |  |
| 144 | `RtlMicrodomUpdateSetNodeName` | `0x5F4C0` | 286 | UnwindData |  |
| 145 | `RtlMicrodomUpdateSetNodeTextContent` | `0x5F5F0` | 291 | UnwindData |  |
| 79 | `RtlDestroyGrowingList` | `0x5F8B0` | 137 | UnwindData |  |
| 113 | `RtlIndexIntoGrowingList` | `0x5F940` | 236 | UnwindData |  |
| 117 | `RtlInitializeGrowingList` | `0x5FA40` | 148 | UnwindData |  |
| 99 | `RtlExecuteXPathOverMicrodom` | `0x61BB0` | 1,194 | UnwindData |  |
| 147 | `RtlNsDestroy` | `0x621F0` | 78 | UnwindData |  |
| 148 | `RtlNsInitialize` | `0x62350` | 171 | UnwindData |  |
| 171 | `RtlXmlDefaultCompareStrings` | `0x65060` | 139 | UnwindData |  |
| 173 | `RtlXmlDetermineStreamEncoding` | `0x652C0` | 711 | UnwindData |  |
| 176 | `RtlXmlInitializeTokenization` | `0x65590` | 218 | UnwindData |  |
| 178 | `RtlXmlNextToken` | `0x65670` | 5,432 | UnwindData |  |
| 172 | `RtlXmlDestroyNextLogicalThing` | `0x67680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `RtlXmlExtentToString` | `0x676A0` | 490 | UnwindData |  |
| 175 | `RtlXmlInitializeNextLogicalThing` | `0x67BE0` | 319 | UnwindData |  |
| 177 | `RtlXmlNextLogicalThing` | `0x67D30` | 20 | UnwindData |  |
| 37 | `RtlAllocateLBlob` | `0x6FB90` | 142 | UnwindData |  |
| 46 | `RtlBase64EncodeLBlobToLUnicodeString` | `0x6FDB0` | 530 | UnwindData |  |
| 47 | `RtlBase64EncodeLBlobToLUtf8String` | `0x6FFD0` | 530 | UnwindData |  |
| 51 | `RtlCompareEncodedLBlobs` | `0x701F0` | 848 | UnwindData |  |
| 75 | `RtlDecodeBase64LUnicodeStringToLBlob` | `0x706A0` | 498 | UnwindData |  |
| 76 | `RtlDecodeBase64LUtf8StringToLBlob` | `0x708A0` | 562 | UnwindData |  |
| 82 | `RtlDetermineTranscodedLBlobSize` | `0x70AE0` | 984 | UnwindData |  |
| 85 | `RtlDuplicateLBlob` | `0x70EC0` | 364 | UnwindData |  |
| 103 | `RtlFreeLBlob` | `0x71040` | 29 | UnwindData |  |
| 104 | `RtlFreeLUnicodeString` | `0x71040` | 29 | UnwindData |  |
| 105 | `RtlFreeLUtf8String` | `0x71040` | 29 | UnwindData |  |
| 109 | `RtlGetHashAlgorithmHashLength` | `0x71070` | 282 | UnwindData |  |
| 110 | `RtlHashLBlob` | `0x71950` | 745 | UnwindData |  |
| 118 | `RtlInitializeSmartLBlobWritingContext` | `0x71C40` | 468 | UnwindData |  |
| 121 | `RtlIsLBlobValid` | `0x71E20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `RtlMatchEncodedLBlobAgainstList` | `0x71E50` | 165 | UnwindData |  |
| 126 | `RtlMatchEncodedLBlobAgainstPointerList` | `0x71F00` | 162 | UnwindData |  |
| 150 | `RtlPreInitializeSmartLBlobWritingContext` | `0x71FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `RtlReallocateLBlob` | `0x71FD0` | 388 | UnwindData |  |
| 162 | `RtlSplitEncodedLBlob` | `0x72160` | 1,407 | UnwindData |  |
| 166 | `RtlTranscodeLBlobs` | `0x726F0` | 1,734 | UnwindData |  |
| 168 | `RtlWriteDataIntoSmartLBlobWritingContext` | `0x72DC0` | 805 | UnwindData |  |
| 38 | `RtlAllocateLUnicodeString` | `0x733F0` | 225 | UnwindData |  |
| 40 | `RtlAllocateUnicodeString` | `0x734E0` | 216 | UnwindData |  |
| 41 | `RtlAppendLUnicodeStringToLUnicodeString` | `0x735C0` | 394 | UnwindData |  |
| 43 | `RtlAppendUcsCharacterToLUnicodeString` | `0x73900` | 60 | UnwindData |  |
| 45 | `RtlAppendUcsCharactersToLUnicodeString` | `0x73950` | 441 | UnwindData |  |
| 53 | `RtlCompareLUnicodeStrings` | `0x73B10` | 42 | UnwindData |  |
| 56 | `RtlConcatenateLUnicodeStrings` | `0x73B40` | 587 | UnwindData |  |
| 62 | `RtlCopyLUnicodeString` | `0x73DA0` | 296 | UnwindData |  |
| 74 | `RtlDeallocateUnicodeString` | `0x73ED0` | 29 | UnwindData |  |
| 81 | `RtlDetermineFilteredLUnicodeStringLength` | `0x73F00` | 386 | UnwindData |  |
| 83 | `RtlDoesLUnicodeStringMatchExpression` | `0x74090` | 1,387 | UnwindData |  |
| 86 | `RtlDuplicateLUnicodeString` | `0x746E0` | 216 | UnwindData |  |
| 88 | `RtlDuplicateLUnicodeStringToUnicodeString` | `0x747C0` | 397 | UnwindData |  |
| 91 | `RtlDuplicateNullTerminatedStringToLUnicodeString` | `0x74960` | 137 | UnwindData |  |
| 92 | `RtlDuplicateUnicodeStringToLUnicodeString` | `0x749F0` | 215 | UnwindData |  |
| 95 | `RtlEqualLUnicodeStringPrefix` | `0x74AD0` | 56 | UnwindData |  |
| 96 | `RtlEqualLUnicodeStrings` | `0x74B10` | 121 | UnwindData |  |
| 100 | `RtlFilterLUnicodeString` | `0x74B90` | 387 | UnwindData |  |
| 111 | `RtlHashLUnicodeString` | `0x74D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `RtlInitLUnicodeStringFromNullTerminatedString` | `0x74D40` | 153 | UnwindData |  |
| 115 | `RtlInitLUnicodeStringFromUnicodeString` | `0x74DE0` | 135 | UnwindData |  |
| 116 | `RtlInitUnicodeStringFromLUnicodeString` | `0x74E70` | 363 | UnwindData |  |
| 122 | `RtlIsLUnicodeStringValid` | `0x74FF0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `RtlMatchLUnicodeStringAgainstLUtf8StringList` | `0x75060` | 502 | UnwindData |  |
| 128 | `RtlMatchLUnicodeStringAgainstLUtf8StringPointerList` | `0x75260` | 488 | UnwindData |  |
| 129 | `RtlMatchLUnicodeStringAgainstList` | `0x75450` | 495 | UnwindData |  |
| 130 | `RtlMatchLUnicodeStringAgainstPointerList` | `0x75650` | 481 | UnwindData |  |
| 152 | `RtlReallocateLUnicodeString` | `0x75840` | 277 | UnwindData |  |
| 154 | `RtlReallocateUnicodeString` | `0x75960` | 498 | UnwindData |  |
| 163 | `RtlSplitLUnicodeString` | `0x75B60` | 811 | UnwindData |  |
| 39 | `RtlAllocateLUtf8String` | `0x75EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `RtlAppendLUtf8StringToLUtf8String` | `0x75EB0` | 387 | UnwindData |  |
| 44 | `RtlAppendUcsCharacterToLUtf8String` | `0x76040` | 314 | UnwindData |  |
| 48 | `RtlCalculateUtf16StringLengthFromLUtf8String` | `0x76180` | 441 | UnwindData |  |
| 52 | `RtlCompareLUnicodeStringToLUtf8String` | `0x76340` | 42 | UnwindData |  |
| 54 | `RtlCompareLUtf8StringToLUnicodeString` | `0x76370` | 42 | UnwindData |  |
| 55 | `RtlCompareLUtf8Strings` | `0x763A0` | 42 | UnwindData |  |
| 57 | `RtlConcatenateLUtf8Strings` | `0x763D0` | 589 | UnwindData |  |
| 63 | `RtlCopyLUtf8String` | `0x76630` | 296 | UnwindData |  |
| 64 | `RtlCopyLUtf8StringToLUnicodeString` | `0x76760` | 257 | UnwindData |  |
| 87 | `RtlDuplicateLUnicodeStringToLUtf8String` | `0x76870` | 213 | UnwindData |  |
| 89 | `RtlDuplicateLUtf8String` | `0x76950` | 216 | UnwindData |  |
| 90 | `RtlDuplicateLUtf8StringToLUnicodeString` | `0x76A30` | 211 | UnwindData |  |
| 97 | `RtlEqualLUtf8StringPrefix` | `0x76B10` | 322 | UnwindData |  |
| 98 | `RtlEqualLUtf8Strings` | `0x76C60` | 158 | UnwindData |  |
| 112 | `RtlHashLUtf8String` | `0x76D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `RtlIsLUtf8StringValid` | `0x76D30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `RtlMatchLUtf8StringAgainstLUnicodeStringList` | `0x76D60` | 502 | UnwindData |  |
| 132 | `RtlMatchLUtf8StringAgainstLUnicodeStringPointerList` | `0x76F60` | 488 | UnwindData |  |
| 133 | `RtlMatchLUtf8StringAgainstList` | `0x77150` | 495 | UnwindData |  |
| 134 | `RtlMatchLUtf8StringAgainstPointerList` | `0x77350` | 481 | UnwindData |  |
| 153 | `RtlReallocateLUtf8String` | `0x77540` | 226 | UnwindData |  |
| 164 | `RtlSplitLUtf8String` | `0x77630` | 624 | UnwindData |  |
| 119 | `RtlInitializeSmartLUnicodeStringWritingContext` | `0x77C20` | 300 | UnwindData |  |
| 120 | `RtlInitializeSmartLUtf8StringWritingContext` | `0x77D60` | 73 | UnwindData |  |
| 108 | `RtlGetEncodingSizeUtf8` | `0x77DB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `RtlLengthOfUcsCharacterEncodedAsUtf8` | `0x77DB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `RtlPreInitializeSmartLBlobUcsWritingContext` | `0x77E10` | 37 | UnwindData |  |
| 158 | `RtlSmartMultiUcsEncoder_Utf16LE` | `0x77E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `RtlSmartMultiUcsEncoder_Utf8` | `0x77E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `RtlSmartUcsEncoder_Utf16LE` | `0x77E60` | 60 | UnwindData |  |
| 161 | `RtlSmartUcsEncoder_Utf8` | `0x77EB0` | 60 | UnwindData |  |
| 169 | `RtlWriteDecodedUcsDataIntoSmartLBlobUcsWritingContext` | `0x77F00` | 660 | UnwindData |  |
| 58 | `RtlConvertNtFilePathToWin32FilePath` | `0x788E0` | 1,047 | UnwindData |  |
| 59 | `RtlConvertNtRegistryPathToWin32RegistryPath` | `0x78D00` | 171 | UnwindData |  |
| 60 | `RtlConvertWin32FilePathToNtFilePath` | `0x78DC0` | 752 | UnwindData |  |
| 61 | `RtlConvertWin32RegistryPathToNtRegistryPath` | `0x790C0` | 331 | UnwindData |  |
| 165 | `RtlSplitWin32RegistryPathIntoRootAndLeaves` | `0x79220` | 558 | UnwindData |  |
| 72 | `RtlCreateUtf16LEUCSStringBuilder` | `0x79CD0` | 392 | UnwindData |  |
| 73 | `RtlCreateUtf8UCSStringBuilder` | `0x79E60` | 382 | UnwindData |  |
| 77 | `RtlDecodeUtf16LE` | `0x7A1E0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `RtlDecodeUtf8` | `0x7A270` | 708 | UnwindData |  |
| 84 | `RtlDowncaseUCSCharacter` | `0x7A6A0` | 58 | UnwindData |  |
| 167 | `RtlUpcaseUCSCharacter` | `0x7A6E0` | 58 | UnwindData |  |
| 93 | `RtlEncodeUtf16LE` | `0x7A900` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `RtlEncodeUtf8` | `0x7AA80` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `RtlGetEncodingSizeUcs2` | `0x7ADB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `RtlGetEncodingSizeUtf16` | `0x7ADE0` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `RtlMurmurHashLBlob` | `0x7B0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `RtlRegisterErrorOriginationCallback` | `0x7B0C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `RtlReportErrorOrigination` | `0x7B0D0` | 153 | UnwindData |  |
| 157 | `RtlReportErrorPropagation` | `0x7B170` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `ConvertHResultToNtStatus` | `0x7B320` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ConvertNtStatusToHResult` | `0x7B5B0` | 1,093 | UnwindData |  |
| 26 | `GetLoadedHiveKeyName` | `0x7C1D0` | 30 | UnwindData |  |
| 28 | `GetTemporaryPath` | `0x7C340` | 553 | UnwindData |  |
| 24 | `GetCWcpDll` | `0x7EC80` | 204 | UnwindData |  |
| 2 | `CreateKeyformFromAttributesIntoBuffer` | `0x7F600` | 1,744 | UnwindData |  |
| 20 | `DecompressManifest` | `0x806C0` | 457 | UnwindData |  |
| 188 | `SfpCreateOfflineRepairObject` | `0x864F0` | 671 | UnwindData |  |
| 189 | `SfpUnload` | `0x867A0` | 250 | UnwindData |  |
| 29 | `GetUpdateReserveManagerLoader` | `0x87160` | 263 | UnwindData |  |
| 32 | `LoadUpdateReserveManager` | `0x87270` | 125 | UnwindData |  |
| 5 | `BeginFileMapEnumerationInternal` | `0x87EB0` | 868 | UnwindData |  |
| 15 | `CloseFileMapEnumerationInternal` | `0x88220` | 49 | UnwindData |  |
| 27 | `GetNextFileMapContentInternal` | `0x88260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `IsLuaCdfFile` | `0x88270` | 641 | UnwindData |  |
| 16 | `CompareObjectSDToSddl` | `0x886D0` | 1,825 | UnwindData |  |
| 30 | `IsKeyProtected` | `0x89200` | 413 | UnwindData |  |
| 35 | `RemoveFileProtection` | `0x8A150` | 277 | UnwindData |  |
| 36 | `RemoveRegKeyProtection` | `0x8A4B0` | 385 | UnwindData |  |
| 25 | `GetIdentityAuthority` | `0x8DB50` | 303 | UnwindData |  |
| 192 | `UninstallWindows` | `0x8FDD0` | 1,307 | UnwindData |  |
