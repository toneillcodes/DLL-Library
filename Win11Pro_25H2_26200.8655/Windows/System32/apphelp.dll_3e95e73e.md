# Binary Specification: apphelp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\apphelp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3e95e73e3bf77ba23a50620849344c3886cd0ae56e6cf890e5fe6e56db84026f`
* **Total Exported Functions:** 244

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 121 | `SdbFindFirstTag` | `0x3B50` | 229 | UnwindData |  |
| 152 | `SdbGetFirstChild` | `0x3C40` | 169 | UnwindData |  |
| 162 | `SdbGetNextChild` | `0x3CF0` | 236 | UnwindData |  |
| 173 | `SdbGetTagFromTagID` | `0x3DF0` | 150 | UnwindData |  |
| 18 | *Ordinal Only* | `0x4BF0` | 370 | UnwindData |  |
| 128 | `SdbFindNextTag` | `0x50E0` | 295 | UnwindData |  |
| 215 | `SdbReadQWORDTag` | `0x5210` | 154 | UnwindData |  |
| 172 | `SdbGetTagDataSize` | `0x56C0` | 745 | UnwindData |  |
| 171 | `SdbGetStringTagPtr` | `0x5BB0` | 24 | UnwindData |  |
| 210 | `SdbReadDWORDTag` | `0x62C0` | 476 | UnwindData |  |
| 127 | `SdbFindNextStringIndexedTag` | `0x67E0` | 59 | UnwindData |  |
| 155 | `SdbGetItemFromItemRef` | `0x77F0` | 969 | UnwindData |  |
| 238 | `SdbTagRefToTagID` | `0x7BC0` | 207 | UnwindData |  |
| 237 | `SdbTagIDToTagRef` | `0x7CA0` | 113 | UnwindData |  |
| 218 | `SdbReadStringTagRef` | `0x8450` | 112 | UnwindData |  |
| 122 | `SdbFindFirstTagRef` | `0x84D0` | 366 | UnwindData |  |
| 217 | `SdbReadStringTag` | `0x8B90` | 169 | UnwindData |  |
| 120 | `SdbFindFirstStringIndexedTag` | `0x8C40` | 201 | UnwindData |  |
| 154 | `SdbGetIndex` | `0x8D10` | 215 | UnwindData |  |
| 20 | *Ordinal Only* | `0x8DF0` | 412 | UnwindData |  |
| 219 | `SdbReadWORDTag` | `0xA7F0` | 156 | UnwindData |  |
| 139 | `SdbGetBinaryTagData` | `0xBAA0` | 110 | UnwindData |  |
| 73 | `SE_DynamicShim` | `0xBE10` | 820 | UnwindData |  |
| 163 | `SdbGetNthUserSdb` | `0x11430` | 120 | UnwindData |  |
| 159 | `SdbGetMatchingExe` | `0x14140` | 277 | UnwindData |  |
| 223 | `SdbReleaseDatabase` | `0x14880` | 238 | UnwindData |  |
| 101 | `SdbCloseDatabase` | `0x14A50` | 223 | UnwindData |  |
| 141 | `SdbGetDatabaseID` | `0x15210` | 267 | UnwindData |  |
| 209 | `SdbReadBinaryTag` | `0x15330` | 183 | UnwindData |  |
| 147 | `SdbGetEntryFlags` | `0x153F0` | 200 | UnwindData |  |
| 148 | `SdbGetFileAttributes` | `0x162B0` | 800 | UnwindData |  |
| 166 | `SdbGetPathSystemSdb` | `0x18240` | 40 | UnwindData |  |
| 76 | `SE_GetProcAddressForCaller` | `0x19090` | 1,891 | UnwindData |  |
| 89 | `SE_ProcessDying` | `0x1B840` | 127 | UnwindData |  |
| 82 | `SE_InstallAfterInit` | `0x1C810` | 131 | UnwindData |  |
| 83 | `SE_InstallBeforeInit` | `0x1C8A0` | 287 | UnwindData |  |
| 85 | `SE_LdrEntryRemoved` | `0x1D6A0` | 286 | UnwindData |  |
| 71 | `SE_DllLoaded` | `0x1E950` | 259 | UnwindData |  |
| 23 | *Ordinal Only* | `0x1F710` | 49 | UnwindData |  |
| 54 | `ApphelpIsPortMonAllowed` | `0x1FC90` | 253 | UnwindData |  |
| 44 | `ApphelpCheckShellObject` | `0x1FDA0` | 569 | UnwindData |  |
| 90 | `SE_ShimDPF` | `0x20850` | 60 | UnwindData |  |
| 86 | `SE_LdrResolveDllName` | `0x22830` | 800 | UnwindData |  |
| 240 | `SdbUnpackAppCompatData` | `0x22CB0` | 276 | UnwindData |  |
| 241 | `SdbUnpackQueryResult` | `0x22DD0` | 78 | UnwindData |  |
| 194 | `SdbPackAppCompatData` | `0x22E30` | 1,309 | UnwindData |  |
| 129 | `SdbFindNextTagRef` | `0x23ED0` | 209 | UnwindData |  |
| 70 | `SE_COM_Lookup` | `0x25220` | 105 | UnwindData |  |
| 216 | `SdbReadQWORDTagRef` | `0x297B0` | 97 | UnwindData |  |
| 80 | `SE_GetShimId` | `0x29820` | 307 | UnwindData |  |
| 132 | `SdbFreeFileAttributes` | `0x29D60` | 143 | UnwindData |  |
| 231 | `SdbShowApphelpFromQuery` | `0x2AC20` | 171 | UnwindData |  |
| 176 | `SdbInitDatabase` | `0x2C990` | 65 | UnwindData |  |
| 91 | `SE_ShimDllLoaded` | `0x2EAF0` | 163 | UnwindData |  |
| 116 | `SdbFindFirstGUIDIndexedTag` | `0x2EBA0` | 196 | UnwindData |  |
| 182 | `SdbIsTagrefFromMainDB` | `0x2EEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `SdbOpenDatabase` | `0x2EEC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `SdbReadDWORDTagRef` | `0x2EF20` | 96 | UnwindData |  |
| 103 | `SdbCloseLocalDatabase` | `0x2EFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `SdbFindFirstMsiPackage_Str` | `0x2EFE0` | 139 | UnwindData |  |
| 117 | `SdbFindFirstMsiPackage` | `0x2F080` | 96 | UnwindData |  |
| 181 | `SdbIsTagrefFromLocalDB` | `0x2F4F0` | 3,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `SdbAddLayerTagRefToQuery` | `0x30210` | 495 | UnwindData |  |
| 68 | `SE_COM_HookInterface` | `0x30410` | 131 | UnwindData |  |
| 119 | `SdbFindFirstNamedTag` | `0x304D0` | 30 | UnwindData |  |
| 167 | `SdbGetPermLayerKeys` | `0x30690` | 180 | UnwindData |  |
| 24 | *Ordinal Only* | `0x309F0` | 342 | UnwindData |  |
| 69 | `SE_COM_HookObject` | `0x30B50` | 137 | UnwindData |  |
| 177 | `SdbInitDatabaseEx` | `0x31B30` | 831 | UnwindData |  |
| 130 | `SdbFormatAttribute` | `0x32040` | 993 | UnwindData |  |
| 239 | `SdbTagToString` | `0x32430` | 6,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `ApphelpCheckModule` | `0x33DF0` | 452 | UnwindData |  |
| 46 | `ApphelpCreateAppcompatData` | `0x33FC0` | 655 | UnwindData |  |
| 81 | `SE_InitializeEngine` | `0x34260` | 1,080 | UnwindData |  |
| 153 | `SdbGetImageType` | `0x35BA0` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `ApphelpCheckAPO` | `0x36130` | 584 | UnwindData |  |
| 38 | `ApphelpCheckIME` | `0x36380` | 73 | UnwindData |  |
| 39 | `ApphelpCheckInstallShieldPackage` | `0x363D0` | 545 | UnwindData |  |
| 41 | `ApphelpCheckMsiPackage` | `0x36600` | 694 | UnwindData |  |
| 47 | `ApphelpFixMsiPackage` | `0x368C0` | 712 | UnwindData |  |
| 48 | `ApphelpFixMsiPackageExe` | `0x36B90` | 669 | UnwindData |  |
| 51 | `ApphelpGetMsiProperties` | `0x36E40` | 178 | UnwindData |  |
| 52 | `ApphelpGetNTVDMInfo` | `0x36F00` | 315 | UnwindData |  |
| 35 | `AllowPermLayer` | `0x37AC0` | 170 | UnwindData |  |
| 61 | `ApphelpUpdateCacheEntry` | `0x37B70` | 29 | UnwindData |  |
| 62 | `GetPermLayers` | `0x37BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `SetPermLayerState` | `0x37BB0` | 34 | UnwindData |  |
| 254 | `SetPermLayerStateEx` | `0x37BE0` | 69 | UnwindData |  |
| 255 | `SetPermLayers` | `0x37C30` | 96 | UnwindData |  |
| 49 | `ApphelpFreeFileAttributes` | `0x37CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `ApphelpGetFileAttributes` | `0x37CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `ApphelpShowDialog` | `0x37CC0` | 52 | UnwindData |  |
| 110 | `SdbDumpSearchPathPartCaches` | `0x37D00` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `SdbFreeFileInfo` | `0x37D00` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `ShimDumpCache` | `0x37D00` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `ApphelpGetShimDebugLevel` | `0x38860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `SdbGetFileInfo` | `0x38860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `SdbGetShowDebugInfoOption` | `0x38860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `SdbGetShowDebugInfoOptionValue` | `0x38860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `ApphelpNotifyPcaOfProblem` | `0x38870` | 1,034 | UnwindData |  |
| 135 | `SdbGUIDFromString` | `0x38C80` | 29 | UnwindData |  |
| 136 | `SdbGUIDToString` | `0x38CB0` | 34 | UnwindData |  |
| 27 | *Ordinal Only* | `0x38CE0` | 34 | UnwindData |  |
| 187 | `SdbOpenApphelpDetailsDatabaseSP` | `0x38D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `SdbStringDuplicate` | `0x38D20` | 44 | UnwindData |  |
| 235 | `SdbStringReplace` | `0x38D60` | 53 | UnwindData |  |
| 236 | `SdbStringReplaceArray` | `0x38DA0` | 58 | UnwindData |  |
| 256 | `ShimDbgPrint` | `0x38DE0` | 2,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `SdbIsNullGUID` | `0x39670` | 12,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | *Ordinal Only* | `0x3C840` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `SdbBeginWriteListTag` | `0x3C880` | 110 | UnwindData |  |
| 102 | `SdbCloseDatabaseWrite` | `0x3CB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `SdbCommitIndexes` | `0x3CB60` | 69 | UnwindData |  |
| 105 | `SdbCreateDatabase` | `0x3CC20` | 264 | UnwindData |  |
| 22 | *Ordinal Only* | `0x3CD30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `SdbDeclareIndex` | `0x3CD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | *Ordinal Only* | `0x3CD90` | 911 | UnwindData |  |
| 111 | `SdbEndWriteListTag` | `0x3D130` | 402 | UnwindData |  |
| 232 | `SdbStartIndexing` | `0x3DA00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `SdbStopIndexing` | `0x3DA30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `SdbWriteBYTETag` | `0x3DA60` | 69 | UnwindData |  |
| 244 | `SdbWriteBinaryTag` | `0x3DAB0` | 53 | UnwindData |  |
| 245 | `SdbWriteBinaryTagFromFile` | `0x3DAF0` | 474 | UnwindData |  |
| 246 | `SdbWriteDWORDTag` | `0x3DCD0` | 69 | UnwindData |  |
| 247 | `SdbWriteNULLTag` | `0x3DD20` | 59 | UnwindData |  |
| 248 | `SdbWriteQWORDTag` | `0x3DD70` | 69 | UnwindData |  |
| 249 | `SdbWriteStringRefTag` | `0x3DDC0` | 69 | UnwindData |  |
| 250 | `SdbWriteStringTag` | `0x3DE10` | 102 | UnwindData |  |
| 251 | `SdbWriteStringTagDirect` | `0x3DE80` | 78 | UnwindData |  |
| 252 | `SdbWriteWORDTag` | `0x3DEE0` | 70 | UnwindData |  |
| 134 | `SdbFreeFlagInfo` | `0x3ED20` | 41 | UnwindData |  |
| 140 | `SdbGetDatabaseGUID` | `0x3ED50` | 165 | UnwindData |  |
| 25 | *Ordinal Only* | `0x3EE00` | 145 | UnwindData |  |
| 157 | `SdbGetLayerTagRef` | `0x3EEA0` | 147 | UnwindData |  |
| 158 | `SdbGetLocalPDB` | `0x3EF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `SdbGetNamedLayer` | `0x3EF60` | 153 | UnwindData |  |
| 164 | `SdbGetPDBFromGUID` | `0x3F000` | 155 | UnwindData |  |
| 183 | `SdbIsTagrefFromMergeStubDB` | `0x3F0B0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `SdbQueryBlockUpgrade` | `0x3F490` | 120 | UnwindData |  |
| 197 | `SdbQueryContext` | `0x3F510` | 604 | UnwindData |  |
| 201 | `SdbQueryFlagInfo` | `0x3F780` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `SdbQueryFlagMask` | `0x3F7D0` | 649 | UnwindData |  |
| 204 | `SdbQueryReinstallUpgrade` | `0x3FDE0` | 120 | UnwindData |  |
| 224 | `SdbReleaseMatchingExe` | `0x3FF20` | 3,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `SdbApphelpNotify` | `0x40B30` | 114 | UnwindData |  |
| 96 | `SdbApphelpNotifyEx` | `0x40BB0` | 120 | UnwindData |  |
| 97 | `SdbApphelpNotifyEx2` | `0x40C30` | 168 | UnwindData |  |
| 100 | `SdbCloseApphelpInformation` | `0x40DD0` | 174 | UnwindData |  |
| 106 | `SdbCreateHelpCenterURL` | `0x40E90` | 1,343 | UnwindData |  |
| 113 | `SdbEscapeApphelpURL` | `0x41560` | 490 | UnwindData |  |
| 184 | `SdbLoadString` | `0x41750` | 261 | UnwindData |  |
| 186 | `SdbOpenApphelpDetailsDatabase` | `0x41860` | 140 | UnwindData |  |
| 188 | `SdbOpenApphelpInformation` | `0x41900` | 592 | UnwindData |  |
| 189 | `SdbOpenApphelpInformationByID` | `0x41B60` | 332 | UnwindData |  |
| 190 | `SdbOpenApphelpResourceFile` | `0x41CC0` | 225 | UnwindData |  |
| 192 | `SdbOpenDbFromGuid` | `0x41DB0` | 242 | UnwindData |  |
| 195 | `SdbQueryApphelpInformation` | `0x41EB0` | 796 | UnwindData |  |
| 205 | `SdbReadApphelpData` | `0x421E0` | 361 | UnwindData |  |
| 206 | `SdbReadApphelpDetailsData` | `0x42350` | 1,137 | UnwindData |  |
| 226 | `SdbSetApphelpDebugParameters` | `0x427D0` | 300 | UnwindData |  |
| 230 | `SdbShowApphelpDialog` | `0x42910` | 138 | UnwindData |  |
| 99 | `SdbBuildCompatEnvVariables` | `0x44410` | 516 | UnwindData |  |
| 109 | `SdbDeletePermLayerKeys` | `0x44620` | 354 | UnwindData |  |
| 26 | *Ordinal Only* | `0x44790` | 354 | UnwindData |  |
| 229 | `SdbSetPermLayerKeys` | `0x44900` | 491 | UnwindData |  |
| 32 | *Ordinal Only* | `0x44B00` | 34 | UnwindData |  |
| 33 | *Ordinal Only* | `0x44B30` | 1,285 | UnwindData |  |
| 131 | `SdbFreeDatabaseInformation` | `0x45230` | 44 | UnwindData |  |
| 142 | `SdbGetDatabaseInformation` | `0x45270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `SdbGetDatabaseInformationByName` | `0x45280` | 432 | UnwindData |  |
| 145 | `SdbGetDatabaseVersion` | `0x45580` | 382 | UnwindData |  |
| 28 | *Ordinal Only* | `0x45710` | 248 | UnwindData |  |
| 146 | `SdbGetDllPath` | `0x465E0` | 20 | UnwindData |  |
| 193 | `SdbOpenLocalDatabase` | `0x466F0` | 42 | UnwindData |  |
| 214 | `SdbReadPatchBits` | `0x46720` | 475 | UnwindData |  |
| 228 | `SdbSetImageType` | `0x46910` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `SdbCreateMsiTransformFile` | `0x47110` | 335 | UnwindData |  |
| 112 | `SdbEnumMsiTransforms` | `0x47270` | 414 | UnwindData |  |
| 15 | *Ordinal Only* | `0x47420` | 805 | UnwindData |  |
| 114 | `SdbFindCustomActionForPackage` | `0x47750` | 221 | UnwindData |  |
| 17 | *Ordinal Only* | `0x47840` | 81 | UnwindData |  |
| 123 | `SdbFindMsiPackageByID` | `0x478A0` | 434 | UnwindData |  |
| 126 | `SdbFindNextMsiPackage` | `0x47A60` | 171 | UnwindData |  |
| 16 | *Ordinal Only* | `0x47B20` | 90 | UnwindData |  |
| 160 | `SdbGetMsiPackageInformation` | `0x47B80` | 413 | UnwindData |  |
| 213 | `SdbReadMsiTransformInfo` | `0x47D30` | 920 | UnwindData |  |
| 115 | `SdbFindFirstDWORDIndexedTag` | `0x48790` | 189 | UnwindData |  |
| 124 | `SdbFindNextDWORDIndexedTag` | `0x48860` | 55 | UnwindData |  |
| 125 | `SdbFindNextGUIDIndexedTag` | `0x488A0` | 55 | UnwindData |  |
| 185 | `SdbMakeIndexKeyFromString` | `0x488E0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | *Ordinal Only* | `0x48B90` | 295 | UnwindData |  |
| 221 | `SdbRegisterDatabase` | `0x48CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `SdbRegisterDatabaseEx` | `0x48CD0` | 1,678 | UnwindData |  |
| 29 | *Ordinal Only* | `0x49370` | 349 | UnwindData |  |
| 242 | `SdbUnregisterDatabase` | `0x494E0` | 501 | UnwindData |  |
| 30 | *Ordinal Only* | `0x496E0` | 259 | UnwindData |  |
| 149 | `SdbGetFileImageType` | `0x497F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `SdbGetFileImageTypeEx` | `0x49810` | 184 | UnwindData |  |
| 138 | `SdbGetAppPatchDir` | `0x49B80` | 106 | UnwindData |  |
| 156 | `SdbGetLayerName` | `0x49BF0` | 190 | UnwindData |  |
| 165 | `SdbGetPathCustomSdb` | `0x49CC0` | 221 | UnwindData |  |
| 170 | `SdbGetStandardDatabaseGUID` | `0x49DE0` | 120 | UnwindData |  |
| 180 | `SdbIsStandardDatabase` | `0x49E60` | 151 | UnwindData |  |
| 225 | `SdbResolveDatabase` | `0x49F00` | 31 | UnwindData |  |
| 227 | `SdbSetEntryFlags` | `0x4A2F0` | 282 | UnwindData |  |
| 207 | `SdbReadBYTETag` | `0x4B210` | 153 | UnwindData |  |
| 208 | `SdbReadBYTETagRef` | `0x4B2B0` | 96 | UnwindData |  |
| 220 | `SdbReadWORDTagRef` | `0x4B420` | 99 | UnwindData |  |
| 144 | `SdbGetDatabaseMatch` | `0x4BD00` | 565 | UnwindData |  |
| 178 | `SdbIsDbRuntimePlatformSupportedOnHost` | `0x4BF40` | 150 | UnwindData |  |
| 198 | `SdbQueryData` | `0x4BFE0` | 41 | UnwindData |  |
| 199 | `SdbQueryDataEx` | `0x4C010` | 225 | UnwindData |  |
| 200 | `SdbQueryDataExTagID` | `0x4C100` | 1,520 | UnwindData |  |
| 212 | `SdbReadEntryInformation` | `0x4C700` | 402 | UnwindData |  |
| 174 | `SdbGrabMatchingInfo` | `0x4DFC0` | 36 | UnwindData |  |
| 175 | `SdbGrabMatchingInfoEx` | `0x4DFF0` | 948 | UnwindData |  |
| 203 | `SdbQueryName` | `0x4EEE0` | 482 | UnwindData |  |
| 37 | `ApphelpCheckExe` | `0x4FAB0` | 33 | UnwindData |  |
| 42 | `ApphelpCheckRunApp` | `0x4FAE0` | 132 | UnwindData |  |
| 43 | `ApphelpCheckRunAppEx` | `0x4FB70` | 358 | UnwindData |  |
| 56 | `ApphelpParseModuleData` | `0x4FCE0` | 326 | UnwindData |  |
| 57 | `ApphelpQueryModSettingsAlloc` | `0x4FE30` | 516 | UnwindData |  |
| 58 | `ApphelpQueryModuleData` | `0x50040` | 43 | UnwindData |  |
| 59 | `ApphelpQueryModuleDataEx` | `0x50080` | 540 | UnwindData |  |
| 258 | `ShimFlushCache` | `0x50A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `ApphelpChpeModSettingsFromQueryResult` | `0x50A80` | 512 | UnwindData |  |
| 137 | `SdbGetAppCompatDataSize` | `0x51C00` | 110 | UnwindData |  |
| 34 | *Ordinal Only* | `0x51C80` | 403 | UnwindData |  |
| 63 | `SE_AddHookset` | `0x51FC0` | 395 | UnwindData |  |
| 64 | `SE_CALLBACK_AddHook` | `0x52160` | 158 | UnwindData |  |
| 65 | `SE_CALLBACK_Lookup` | `0x52210` | 122 | UnwindData |  |
| 66 | `SE_COM_AddHook` | `0x52290` | 139 | UnwindData |  |
| 67 | `SE_COM_AddServer` | `0x52330` | 157 | UnwindData |  |
| 72 | `SE_DllUnloaded` | `0x523E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `SE_GetHookAPIs` | `0x52430` | 410 | UnwindData |  |
| 75 | `SE_GetMaxShimCount` | `0x525D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `SE_GetProcAddressIgnoreIncExc` | `0x525E0` | 115 | UnwindData |  |
| 78 | `SE_GetProcAddressLoad` | `0x52660` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `SE_GetShimCount` | `0x526B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `SE_IsShimDll` | `0x526D0` | 134 | UnwindData |  |
| 87 | `SE_LookupAddress` | `0x52760` | 271 | UnwindData |  |
| 88 | `SE_LookupCaller` | `0x52880` | 421 | UnwindData |  |
| 92 | `SE_WINRT_AddHook` | `0x52A30` | 139 | UnwindData |  |
| 93 | `SE_WINRT_HookObject` | `0x52B50` | 132 | UnwindData |  |
