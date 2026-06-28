# Binary Specification: apphelp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\apphelp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `19ac8bf20132a4568d82587ae66d3ab58cd5d2cf174aa356a06d02ab4c393697`
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
| 86 | `SE_LdrResolveDllName` | `0x22820` | 800 | UnwindData |  |
| 240 | `SdbUnpackAppCompatData` | `0x22CA0` | 276 | UnwindData |  |
| 241 | `SdbUnpackQueryResult` | `0x22DC0` | 78 | UnwindData |  |
| 194 | `SdbPackAppCompatData` | `0x22E20` | 1,309 | UnwindData |  |
| 129 | `SdbFindNextTagRef` | `0x23EC0` | 209 | UnwindData |  |
| 70 | `SE_COM_Lookup` | `0x25210` | 105 | UnwindData |  |
| 216 | `SdbReadQWORDTagRef` | `0x297A0` | 97 | UnwindData |  |
| 80 | `SE_GetShimId` | `0x29810` | 307 | UnwindData |  |
| 132 | `SdbFreeFileAttributes` | `0x29D50` | 143 | UnwindData |  |
| 231 | `SdbShowApphelpFromQuery` | `0x2AC10` | 171 | UnwindData |  |
| 176 | `SdbInitDatabase` | `0x2C980` | 65 | UnwindData |  |
| 91 | `SE_ShimDllLoaded` | `0x2EAE0` | 163 | UnwindData |  |
| 116 | `SdbFindFirstGUIDIndexedTag` | `0x2EB90` | 196 | UnwindData |  |
| 182 | `SdbIsTagrefFromMainDB` | `0x2EE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `SdbOpenDatabase` | `0x2EEB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `SdbReadDWORDTagRef` | `0x2EF10` | 96 | UnwindData |  |
| 103 | `SdbCloseLocalDatabase` | `0x2EFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `SdbFindFirstMsiPackage_Str` | `0x2EFD0` | 139 | UnwindData |  |
| 117 | `SdbFindFirstMsiPackage` | `0x2F070` | 96 | UnwindData |  |
| 181 | `SdbIsTagrefFromLocalDB` | `0x2F4E0` | 3,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `SdbAddLayerTagRefToQuery` | `0x30200` | 495 | UnwindData |  |
| 68 | `SE_COM_HookInterface` | `0x30400` | 131 | UnwindData |  |
| 119 | `SdbFindFirstNamedTag` | `0x304C0` | 30 | UnwindData |  |
| 167 | `SdbGetPermLayerKeys` | `0x30680` | 180 | UnwindData |  |
| 24 | *Ordinal Only* | `0x309E0` | 342 | UnwindData |  |
| 69 | `SE_COM_HookObject` | `0x30B40` | 137 | UnwindData |  |
| 177 | `SdbInitDatabaseEx` | `0x31B20` | 831 | UnwindData |  |
| 130 | `SdbFormatAttribute` | `0x32030` | 993 | UnwindData |  |
| 239 | `SdbTagToString` | `0x32420` | 6,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `ApphelpCheckModule` | `0x33DE0` | 452 | UnwindData |  |
| 46 | `ApphelpCreateAppcompatData` | `0x33FB0` | 655 | UnwindData |  |
| 81 | `SE_InitializeEngine` | `0x34250` | 1,080 | UnwindData |  |
| 153 | `SdbGetImageType` | `0x35B90` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `ApphelpCheckAPO` | `0x36120` | 584 | UnwindData |  |
| 38 | `ApphelpCheckIME` | `0x36370` | 73 | UnwindData |  |
| 39 | `ApphelpCheckInstallShieldPackage` | `0x363C0` | 545 | UnwindData |  |
| 41 | `ApphelpCheckMsiPackage` | `0x365F0` | 694 | UnwindData |  |
| 47 | `ApphelpFixMsiPackage` | `0x368B0` | 712 | UnwindData |  |
| 48 | `ApphelpFixMsiPackageExe` | `0x36B80` | 669 | UnwindData |  |
| 51 | `ApphelpGetMsiProperties` | `0x36E30` | 178 | UnwindData |  |
| 52 | `ApphelpGetNTVDMInfo` | `0x36EF0` | 315 | UnwindData |  |
| 35 | `AllowPermLayer` | `0x37AB0` | 170 | UnwindData |  |
| 61 | `ApphelpUpdateCacheEntry` | `0x37B60` | 29 | UnwindData |  |
| 62 | `GetPermLayers` | `0x37B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `SetPermLayerState` | `0x37BA0` | 34 | UnwindData |  |
| 254 | `SetPermLayerStateEx` | `0x37BD0` | 69 | UnwindData |  |
| 255 | `SetPermLayers` | `0x37C20` | 96 | UnwindData |  |
| 49 | `ApphelpFreeFileAttributes` | `0x37C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `ApphelpGetFileAttributes` | `0x37CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `ApphelpShowDialog` | `0x37CB0` | 52 | UnwindData |  |
| 110 | `SdbDumpSearchPathPartCaches` | `0x37CF0` | 2,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `SdbFreeFileInfo` | `0x37CF0` | 2,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `ShimDumpCache` | `0x37CF0` | 2,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `ApphelpGetShimDebugLevel` | `0x38800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `SdbGetFileInfo` | `0x38800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `SdbGetShowDebugInfoOption` | `0x38800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `SdbGetShowDebugInfoOptionValue` | `0x38800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `ApphelpNotifyPcaOfProblem` | `0x38810` | 1,034 | UnwindData |  |
| 135 | `SdbGUIDFromString` | `0x38C20` | 29 | UnwindData |  |
| 136 | `SdbGUIDToString` | `0x38C50` | 34 | UnwindData |  |
| 27 | *Ordinal Only* | `0x38C80` | 34 | UnwindData |  |
| 187 | `SdbOpenApphelpDetailsDatabaseSP` | `0x38CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `SdbStringDuplicate` | `0x38CC0` | 44 | UnwindData |  |
| 235 | `SdbStringReplace` | `0x38D00` | 53 | UnwindData |  |
| 236 | `SdbStringReplaceArray` | `0x38D40` | 58 | UnwindData |  |
| 256 | `ShimDbgPrint` | `0x38D80` | 2,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `SdbIsNullGUID` | `0x39610` | 12,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | *Ordinal Only* | `0x3C7E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `SdbBeginWriteListTag` | `0x3C820` | 110 | UnwindData |  |
| 102 | `SdbCloseDatabaseWrite` | `0x3CAF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `SdbCommitIndexes` | `0x3CB00` | 69 | UnwindData |  |
| 105 | `SdbCreateDatabase` | `0x3CBC0` | 264 | UnwindData |  |
| 22 | *Ordinal Only* | `0x3CCD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `SdbDeclareIndex` | `0x3CD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | *Ordinal Only* | `0x3CD30` | 911 | UnwindData |  |
| 111 | `SdbEndWriteListTag` | `0x3D0D0` | 402 | UnwindData |  |
| 232 | `SdbStartIndexing` | `0x3D9A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `SdbStopIndexing` | `0x3D9D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `SdbWriteBYTETag` | `0x3DA00` | 69 | UnwindData |  |
| 244 | `SdbWriteBinaryTag` | `0x3DA50` | 53 | UnwindData |  |
| 245 | `SdbWriteBinaryTagFromFile` | `0x3DA90` | 474 | UnwindData |  |
| 246 | `SdbWriteDWORDTag` | `0x3DC70` | 69 | UnwindData |  |
| 247 | `SdbWriteNULLTag` | `0x3DCC0` | 59 | UnwindData |  |
| 248 | `SdbWriteQWORDTag` | `0x3DD10` | 69 | UnwindData |  |
| 249 | `SdbWriteStringRefTag` | `0x3DD60` | 69 | UnwindData |  |
| 250 | `SdbWriteStringTag` | `0x3DDB0` | 102 | UnwindData |  |
| 251 | `SdbWriteStringTagDirect` | `0x3DE20` | 78 | UnwindData |  |
| 252 | `SdbWriteWORDTag` | `0x3DE80` | 70 | UnwindData |  |
| 134 | `SdbFreeFlagInfo` | `0x3ECC0` | 41 | UnwindData |  |
| 140 | `SdbGetDatabaseGUID` | `0x3ECF0` | 165 | UnwindData |  |
| 25 | *Ordinal Only* | `0x3EDA0` | 145 | UnwindData |  |
| 157 | `SdbGetLayerTagRef` | `0x3EE40` | 147 | UnwindData |  |
| 158 | `SdbGetLocalPDB` | `0x3EEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `SdbGetNamedLayer` | `0x3EF00` | 153 | UnwindData |  |
| 164 | `SdbGetPDBFromGUID` | `0x3EFA0` | 155 | UnwindData |  |
| 183 | `SdbIsTagrefFromMergeStubDB` | `0x3F050` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `SdbQueryBlockUpgrade` | `0x3F430` | 120 | UnwindData |  |
| 197 | `SdbQueryContext` | `0x3F4B0` | 604 | UnwindData |  |
| 201 | `SdbQueryFlagInfo` | `0x3F720` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `SdbQueryFlagMask` | `0x3F770` | 649 | UnwindData |  |
| 204 | `SdbQueryReinstallUpgrade` | `0x3FD80` | 120 | UnwindData |  |
| 224 | `SdbReleaseMatchingExe` | `0x3FEC0` | 3,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `SdbApphelpNotify` | `0x40AD0` | 114 | UnwindData |  |
| 96 | `SdbApphelpNotifyEx` | `0x40B50` | 120 | UnwindData |  |
| 97 | `SdbApphelpNotifyEx2` | `0x40BD0` | 168 | UnwindData |  |
| 100 | `SdbCloseApphelpInformation` | `0x40D70` | 174 | UnwindData |  |
| 106 | `SdbCreateHelpCenterURL` | `0x40E30` | 1,343 | UnwindData |  |
| 113 | `SdbEscapeApphelpURL` | `0x41500` | 490 | UnwindData |  |
| 184 | `SdbLoadString` | `0x416F0` | 261 | UnwindData |  |
| 186 | `SdbOpenApphelpDetailsDatabase` | `0x41800` | 140 | UnwindData |  |
| 188 | `SdbOpenApphelpInformation` | `0x418A0` | 592 | UnwindData |  |
| 189 | `SdbOpenApphelpInformationByID` | `0x41B00` | 332 | UnwindData |  |
| 190 | `SdbOpenApphelpResourceFile` | `0x41C60` | 225 | UnwindData |  |
| 192 | `SdbOpenDbFromGuid` | `0x41D50` | 242 | UnwindData |  |
| 195 | `SdbQueryApphelpInformation` | `0x41E50` | 796 | UnwindData |  |
| 205 | `SdbReadApphelpData` | `0x42180` | 361 | UnwindData |  |
| 206 | `SdbReadApphelpDetailsData` | `0x422F0` | 1,137 | UnwindData |  |
| 226 | `SdbSetApphelpDebugParameters` | `0x42770` | 300 | UnwindData |  |
| 230 | `SdbShowApphelpDialog` | `0x428B0` | 138 | UnwindData |  |
| 99 | `SdbBuildCompatEnvVariables` | `0x443B0` | 516 | UnwindData |  |
| 109 | `SdbDeletePermLayerKeys` | `0x445C0` | 354 | UnwindData |  |
| 26 | *Ordinal Only* | `0x44730` | 354 | UnwindData |  |
| 229 | `SdbSetPermLayerKeys` | `0x448A0` | 491 | UnwindData |  |
| 32 | *Ordinal Only* | `0x44AA0` | 34 | UnwindData |  |
| 33 | *Ordinal Only* | `0x44AD0` | 1,285 | UnwindData |  |
| 131 | `SdbFreeDatabaseInformation` | `0x451D0` | 44 | UnwindData |  |
| 142 | `SdbGetDatabaseInformation` | `0x45210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `SdbGetDatabaseInformationByName` | `0x45220` | 432 | UnwindData |  |
| 145 | `SdbGetDatabaseVersion` | `0x45520` | 382 | UnwindData |  |
| 28 | *Ordinal Only* | `0x456B0` | 248 | UnwindData |  |
| 146 | `SdbGetDllPath` | `0x46580` | 20 | UnwindData |  |
| 193 | `SdbOpenLocalDatabase` | `0x46690` | 42 | UnwindData |  |
| 214 | `SdbReadPatchBits` | `0x466C0` | 475 | UnwindData |  |
| 228 | `SdbSetImageType` | `0x468B0` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `SdbCreateMsiTransformFile` | `0x470B0` | 335 | UnwindData |  |
| 112 | `SdbEnumMsiTransforms` | `0x47210` | 414 | UnwindData |  |
| 15 | *Ordinal Only* | `0x473C0` | 805 | UnwindData |  |
| 114 | `SdbFindCustomActionForPackage` | `0x476F0` | 221 | UnwindData |  |
| 17 | *Ordinal Only* | `0x477E0` | 81 | UnwindData |  |
| 123 | `SdbFindMsiPackageByID` | `0x47840` | 434 | UnwindData |  |
| 126 | `SdbFindNextMsiPackage` | `0x47A00` | 171 | UnwindData |  |
| 16 | *Ordinal Only* | `0x47AC0` | 90 | UnwindData |  |
| 160 | `SdbGetMsiPackageInformation` | `0x47B20` | 413 | UnwindData |  |
| 213 | `SdbReadMsiTransformInfo` | `0x47CD0` | 920 | UnwindData |  |
| 115 | `SdbFindFirstDWORDIndexedTag` | `0x48730` | 189 | UnwindData |  |
| 124 | `SdbFindNextDWORDIndexedTag` | `0x48800` | 55 | UnwindData |  |
| 125 | `SdbFindNextGUIDIndexedTag` | `0x48840` | 55 | UnwindData |  |
| 185 | `SdbMakeIndexKeyFromString` | `0x48880` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | *Ordinal Only* | `0x48B30` | 295 | UnwindData |  |
| 221 | `SdbRegisterDatabase` | `0x48C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `SdbRegisterDatabaseEx` | `0x48C70` | 1,678 | UnwindData |  |
| 29 | *Ordinal Only* | `0x49310` | 349 | UnwindData |  |
| 242 | `SdbUnregisterDatabase` | `0x49480` | 501 | UnwindData |  |
| 30 | *Ordinal Only* | `0x49680` | 259 | UnwindData |  |
| 149 | `SdbGetFileImageType` | `0x49790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `SdbGetFileImageTypeEx` | `0x497B0` | 184 | UnwindData |  |
| 138 | `SdbGetAppPatchDir` | `0x49B20` | 106 | UnwindData |  |
| 156 | `SdbGetLayerName` | `0x49B90` | 190 | UnwindData |  |
| 165 | `SdbGetPathCustomSdb` | `0x49C60` | 221 | UnwindData |  |
| 170 | `SdbGetStandardDatabaseGUID` | `0x49D80` | 120 | UnwindData |  |
| 180 | `SdbIsStandardDatabase` | `0x49E00` | 151 | UnwindData |  |
| 225 | `SdbResolveDatabase` | `0x49EA0` | 31 | UnwindData |  |
| 227 | `SdbSetEntryFlags` | `0x4A290` | 282 | UnwindData |  |
| 207 | `SdbReadBYTETag` | `0x4B1B0` | 153 | UnwindData |  |
| 208 | `SdbReadBYTETagRef` | `0x4B250` | 96 | UnwindData |  |
| 220 | `SdbReadWORDTagRef` | `0x4B3C0` | 99 | UnwindData |  |
| 144 | `SdbGetDatabaseMatch` | `0x4BDF0` | 565 | UnwindData |  |
| 178 | `SdbIsDbRuntimePlatformSupportedOnHost` | `0x4C030` | 150 | UnwindData |  |
| 198 | `SdbQueryData` | `0x4C0D0` | 41 | UnwindData |  |
| 199 | `SdbQueryDataEx` | `0x4C100` | 225 | UnwindData |  |
| 200 | `SdbQueryDataExTagID` | `0x4C1F0` | 1,520 | UnwindData |  |
| 212 | `SdbReadEntryInformation` | `0x4C7F0` | 402 | UnwindData |  |
| 174 | `SdbGrabMatchingInfo` | `0x4E120` | 36 | UnwindData |  |
| 175 | `SdbGrabMatchingInfoEx` | `0x4E150` | 948 | UnwindData |  |
| 203 | `SdbQueryName` | `0x4F040` | 482 | UnwindData |  |
| 37 | `ApphelpCheckExe` | `0x4FC10` | 33 | UnwindData |  |
| 42 | `ApphelpCheckRunApp` | `0x4FC40` | 132 | UnwindData |  |
| 43 | `ApphelpCheckRunAppEx` | `0x4FCD0` | 358 | UnwindData |  |
| 56 | `ApphelpParseModuleData` | `0x4FE40` | 326 | UnwindData |  |
| 57 | `ApphelpQueryModSettingsAlloc` | `0x4FF90` | 516 | UnwindData |  |
| 58 | `ApphelpQueryModuleData` | `0x501A0` | 43 | UnwindData |  |
| 59 | `ApphelpQueryModuleDataEx` | `0x501E0` | 540 | UnwindData |  |
| 258 | `ShimFlushCache` | `0x50BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `ApphelpChpeModSettingsFromQueryResult` | `0x50BE0` | 512 | UnwindData |  |
| 137 | `SdbGetAppCompatDataSize` | `0x51D60` | 110 | UnwindData |  |
| 34 | *Ordinal Only* | `0x51DE0` | 403 | UnwindData |  |
| 63 | `SE_AddHookset` | `0x52120` | 395 | UnwindData |  |
| 64 | `SE_CALLBACK_AddHook` | `0x522C0` | 158 | UnwindData |  |
| 65 | `SE_CALLBACK_Lookup` | `0x52370` | 122 | UnwindData |  |
| 66 | `SE_COM_AddHook` | `0x523F0` | 139 | UnwindData |  |
| 67 | `SE_COM_AddServer` | `0x52490` | 157 | UnwindData |  |
| 72 | `SE_DllUnloaded` | `0x52540` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `SE_GetHookAPIs` | `0x52590` | 410 | UnwindData |  |
| 75 | `SE_GetMaxShimCount` | `0x52730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `SE_GetProcAddressIgnoreIncExc` | `0x52740` | 115 | UnwindData |  |
| 78 | `SE_GetProcAddressLoad` | `0x527C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `SE_GetShimCount` | `0x52810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `SE_IsShimDll` | `0x52830` | 134 | UnwindData |  |
| 87 | `SE_LookupAddress` | `0x528C0` | 271 | UnwindData |  |
| 88 | `SE_LookupCaller` | `0x529E0` | 421 | UnwindData |  |
| 92 | `SE_WINRT_AddHook` | `0x52B90` | 139 | UnwindData |  |
| 93 | `SE_WINRT_HookObject` | `0x52CB0` | 132 | UnwindData |  |
