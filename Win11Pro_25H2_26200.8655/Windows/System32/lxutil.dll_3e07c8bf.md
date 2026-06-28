# Binary Specification: lxutil.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\lxutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3e07c8bfe5f753c1f261b4b8eefe4ef3c6d66eae3c8ffa4349ba3313eda63c46`
* **Total Exported Functions:** 77

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `LxUtilBufferRead` | `0x2590` | 30 | UnwindData |  |
| 2 | `LxUtilBufferWrite` | `0x25C0` | 33 | UnwindData |  |
| 3 | `LxUtilCheckTraversePrivilege` | `0x25F0` | 198 | UnwindData |  |
| 49 | `LxUtilLxErrorToNtStatus` | `0x26C0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `LxUtilLxPathToNtPath` | `0x28E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `LxUtilNtFileNameAppendEscaped` | `0x2930` | 202 | UnwindData |  |
| 52 | `LxUtilNtFileNameEscape` | `0x2A00` | 226 | UnwindData |  |
| 53 | `LxUtilNtFileNameEscapeInPlace` | `0x2AF0` | 91 | UnwindData |  |
| 54 | `LxUtilNtFileNameFreeCopy` | `0x2B60` | 63 | UnwindData |  |
| 55 | `LxUtilNtFileNameLegacyEscape` | `0x2BB0` | 438 | UnwindData |  |
| 56 | `LxUtilNtFileNameLegacyUnescape` | `0x2D70` | 510 | UnwindData |  |
| 59 | `LxUtilNtPathAppend` | `0x2F80` | 166 | UnwindData |  |
| 60 | `LxUtilNtPathAppendLength` | `0x3030` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `LxUtilNtPathEscapeInPlace` | `0x3080` | 103 | UnwindData |  |
| 62 | `LxUtilNtPathToLxPath` | `0x30F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `LxUtilNtPathUnescape` | `0x3140` | 418 | UnwindData |  |
| 64 | `LxUtilNtStatusToLxError` | `0x32F0` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `LxUtilNtTimeToTimespec` | `0x3830` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `LxUtilTimespecToNtTime` | `0x3890` | 188 | UnwindData |  |
| 68 | `LxUtilTranslateLxPathToWidePath` | `0x3960` | 298 | UnwindData |  |
| 69 | `LxUtilTranslateWidePathToLxPath` | `0x3A90` | 409 | UnwindData |  |
| 70 | `LxUtilUnicodeStringDuplicate` | `0x3C30` | 133 | UnwindData |  |
| 4 | `LxUtilDirectoryEnumeratorCleanup` | `0x4140` | 68 | UnwindData |  |
| 5 | `LxUtilDirectoryEnumeratorCurrent` | `0x4190` | 341 | UnwindData |  |
| 6 | `LxUtilDirectoryEnumeratorInitialize` | `0x42F0` | 123 | UnwindData |  |
| 7 | `LxUtilDirectoryEnumeratorNext` | `0x4380` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `LxUtilFsAllocationSizeToBlockCount` | `0x45E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `LxUtilFsCheckSecurity` | `0x4620` | 479 | UnwindData |  |
| 10 | `LxUtilFsChmod` | `0x4810` | 149 | UnwindData |  |
| 11 | `LxUtilFsConvertMode` | `0x48B0` | 268 | UnwindData |  |
| 12 | `LxUtilFsCreateLink` | `0x49D0` | 206 | UnwindData |  |
| 13 | `LxUtilFsCreateLinkReparseBuffer` | `0x4AB0` | 178 | UnwindData |  |
| 14 | `LxUtilFsCreateMetadataEaBuffer` | `0x4B70` | 295 | UnwindData |  |
| 15 | `LxUtilFsCreateNtLinkReparseBuffer` | `0x4CA0` | 285 | UnwindData |  |
| 16 | `LxUtilFsCreateRenameInformation` | `0x4DD0` | 47 | UnwindData |  |
| 17 | `LxUtilFsDeleteFile` | `0x4E10` | 90 | UnwindData |  |
| 18 | `LxUtilFsDeleteFileCore` | `0x4E70` | 179 | UnwindData |  |
| 19 | `LxUtilFsDeleteReadOnlyFile` | `0x4F30` | 179 | UnwindData |  |
| 20 | `LxUtilFsDetermineCompatibilityFlags` | `0x4FF0` | 485 | UnwindData |  |
| 21 | `LxUtilFsDetermineCreationInfo` | `0x51E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `LxUtilFsDetermineInodeAttributes` | `0x5210` | 512 | UnwindData |  |
| 23 | `LxUtilFsDisableAccessTime` | `0x5420` | 84 | UnwindData |  |
| 24 | `LxUtilFsFileModeToReparseTag` | `0x5480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `LxUtilFsGetFileSystemAttributes` | `0x54E0` | 184 | UnwindData |  |
| 26 | `LxUtilFsGetFileSystemBlockSize` | `0x55A0` | 113 | UnwindData |  |
| 27 | `LxUtilFsGetLxAttributes` | `0x5620` | 334 | UnwindData |  |
| 28 | `LxUtilFsGetLxFileSystemAttributes` | `0x5780` | 233 | UnwindData |  |
| 29 | `LxUtilFsGetVolumeFlags` | `0x5870` | 79 | UnwindData |  |
| 30 | `LxUtilFsInitialize` | `0x58D0` | 273 | UnwindData |  |
| 31 | `LxUtilFsIsAppExecLink` | `0x59F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `LxUtilFsQueryInformationByName` | `0x5A10` | 116 | UnwindData |  |
| 33 | `LxUtilFsQueryStatInformation` | `0x5A90` | 356 | UnwindData |  |
| 34 | `LxUtilFsQueryStatInformationByName` | `0x5C00` | 29 | UnwindData |  |
| 35 | `LxUtilFsQueryStatLxInformation` | `0x5C30` | 141 | UnwindData |  |
| 36 | `LxUtilFsQueryStatLxInformationByName` | `0x5CD0` | 177 | UnwindData |  |
| 37 | `LxUtilFsReadAppExecLink` | `0x5D90` | 72 | UnwindData |  |
| 38 | `LxUtilFsReadDir` | `0x5DE0` | 526 | UnwindData |  |
| 39 | `LxUtilFsReadLinkLength` | `0x6000` | 351 | UnwindData |  |
| 40 | `LxUtilFsReadReparseLink` | `0x6170` | 436 | UnwindData |  |
| 41 | `LxUtilFsRename` | `0x6330` | 50 | UnwindData |  |
| 42 | `LxUtilFsReparseTagToFileMode` | `0x6370` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `LxUtilFsReparseTagToFileType` | `0x63E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `LxUtilFsSetCaseSensitivity` | `0x6450` | 34 | UnwindData |  |
| 45 | `LxUtilFsSetTimes` | `0x6480` | 264 | UnwindData |  |
| 46 | `LxUtilFsTruncate` | `0x6590` | 35 | UnwindData |  |
| 47 | `LxUtilFsUnlinkAt` | `0x65C0` | 155 | UnwindData |  |
| 48 | `LxUtilFsUpdateLxAttributes` | `0x6670` | 106 | UnwindData |  |
| 57 | `LxUtilNtHandleGetFileInformation` | `0x6750` | 75 | UnwindData |  |
| 58 | `LxUtilNtHandleRename` | `0x67B0` | 207 | UnwindData |  |
| 66 | `LxUtilSymlinkRead` | `0x69F0` | 388 | UnwindData |  |
| 71 | `LxUtilXattrGet` | `0x6DE0` | 304 | UnwindData |  |
| 72 | `LxUtilXattrGetSystem` | `0x6F20` | 126 | UnwindData |  |
| 73 | `LxUtilXattrIsCaseSensitiveAttribute` | `0x6FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `LxUtilXattrList` | `0x6FD0` | 926 | UnwindData |  |
| 75 | `LxUtilXattrRemove` | `0x7380` | 205 | UnwindData |  |
| 76 | `LxUtilXattrSet` | `0x7460` | 141 | UnwindData |  |
| 77 | `LxUtilXattrSetSystem` | `0x7500` | 162 | UnwindData |  |
