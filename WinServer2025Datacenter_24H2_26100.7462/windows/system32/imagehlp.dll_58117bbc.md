# Binary Specification: imagehlp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\imagehlp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `58117bbc51c4a56b6c4789e190f33a540b7734e394ada9652e2832e3d2e16588`
* **Total Exported Functions:** 165

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 31 | `ImageEnumerateCertificates` | `0x1010` | 679 | UnwindData |  |
| 34 | `ImageGetCertificateHeader` | `0x12C0` | 294 | UnwindData |  |
| 32 | `ImageGetCertificateData` | `0x13F0` | 24 | UnwindData |  |
| 33 | `ImageGetCertificateDataEx` | `0x1410` | 655 | UnwindData |  |
| 44 | `IsBufferCleanOfInvalidMarkers` | `0x2040` | 105 | UnwindData |  |
| 29 | `ImageDirectoryEntryToData` | `0x2B40` | 24 | UnwindData |  |
| 30 | `ImageDirectoryEntryToDataEx` | `0x2B60` | 29 | UnwindData |  |
| 37 | `ImageNtHeader` | `0x2CC0` | 48 | UnwindData |  |
| 40 | `ImageRvaToVa` | `0x3310` | 107 | UnwindData |  |
| 39 | `ImageRvaToSection` | `0x3390` | 92 | UnwindData |  |
| 48 | `MapFileAndCheckSumW` | `0x3400` | 156 | UnwindData |  |
| 47 | `MapFileAndCheckSumA` | `0x34B0` | 102 | UnwindData |  |
| 12 | `CheckSumMappedFile` | `0x3600` | 39 | UnwindData |  |
| 36 | `ImageLoad` | `0x3A00` | 68 | UnwindData |  |
| 2 | `SymAllocDiaString` | `0x3DB0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SymFreeDiaString` | `0x3E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SymGetDiaSession` | `0x3E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SymGetDiaSource` | `0x3E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SymRegisterGetSourcePathPartCallback` | `0x3EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SymRegisterSourceFileUrlListCallback` | `0x3ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SymSetDiaSession` | `0x3EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SymSetServiceManager` | `0x3F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `EnumerateLoadedModules` | `0x3F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `EnumerateLoadedModules64` | `0x3F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `EnumerateLoadedModulesEx` | `0x3F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `EnumerateLoadedModulesExW` | `0x3F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `EnumerateLoadedModulesW64` | `0x3F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `FindDebugInfoFile` | `0x3FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `FindDebugInfoFileEx` | `0x3FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `FindExecutableImage` | `0x3FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `FindExecutableImageEx` | `0x4010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `FindFileInPath` | `0x4030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `FindFileInSearchPath` | `0x4050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `GetSymLoadError` | `0x4070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `ImagehlpApiVersion` | `0x4090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `ImagehlpApiVersionEx` | `0x40B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `MakeSureDirectoryPathExists` | `0x40D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `RemoveInvalidModuleList` | `0x40F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `ReportSymbolLoadSummary` | `0x4110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `SearchTreeForFile` | `0x4130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `SetCheckUserInterruptShared` | `0x4150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `SetSymLoadError` | `0x4170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `StackWalk` | `0x4190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `StackWalk64` | `0x4190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `StackWalk2` | `0x41B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `StackWalkEx` | `0x41D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `SymAddrIncludeInlineTrace` | `0x41F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `SymCleanup` | `0x4210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `SymCompareInlineTrace` | `0x4230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `SymEnumSym` | `0x4250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `SymEnumSymbols` | `0x4270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `SymEnumSymbolsEx` | `0x4290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `SymEnumSymbolsExW` | `0x42B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `SymEnumSymbolsForAddr` | `0x42D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `SymEnumTypes` | `0x42F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `SymEnumTypesByName` | `0x4310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `SymEnumTypesByNameW` | `0x4330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `SymEnumTypesW` | `0x4350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `SymEnumerateModules` | `0x4370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `SymEnumerateModules64` | `0x4370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `SymEnumerateSymbols` | `0x4390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `SymEnumerateSymbols64` | `0x4390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `SymEnumerateSymbolsW` | `0x43B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `SymEnumerateSymbolsW64` | `0x43B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `SymFindFileInPath` | `0x43D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `SymFindFileInPathW` | `0x43F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `SymFromAddr` | `0x4410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `SymFromInlineContext` | `0x4430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `SymFromInlineContextW` | `0x4450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `SymFromName` | `0x4470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `SymFunctionTableAccess` | `0x4490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `SymFunctionTableAccess64` | `0x4490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `SymFunctionTableAccess64AccessRoutines` | `0x44B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `SymGetExtendedOption` | `0x44D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `SymGetLineFromAddr` | `0x44F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `SymGetLineFromAddr64` | `0x44F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `SymGetLineFromInlineContext` | `0x4510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `SymGetLineFromInlineContextW` | `0x4530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `SymGetLineFromName` | `0x4550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `SymGetLineFromName64` | `0x4550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `SymGetLineNext` | `0x4570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `SymGetLineNext64` | `0x4570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `SymGetLinePrev` | `0x4590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `SymGetLinePrev64` | `0x4590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `SymGetModuleBase` | `0x45B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `SymGetModuleBase64` | `0x45B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `SymGetModuleInfo` | `0x45D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `SymGetModuleInfo64` | `0x45D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `SymGetModuleInfoW` | `0x45F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `SymGetModuleInfoW64` | `0x45F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `SymGetOptions` | `0x4610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `SymGetParentWindow` | `0x4630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `SymGetSearchPath` | `0x4650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `SymGetSourceFileChecksumW` | `0x4670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `SymGetSourceFileFromTokenByTokenName` | `0x4690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `SymGetSourceFileFromTokenByTokenNameW` | `0x46B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `SymGetSourceFileFromTokenW` | `0x46D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `SymGetSourceFileTokenByTokenName` | `0x46F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `SymGetSourceFileTokenByTokenNameW` | `0x4710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `SymGetSourceFileTokenW` | `0x4730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `SymGetSourceVarFromTokenW` | `0x4750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `SymGetSymFromAddr` | `0x4770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `SymGetSymFromAddr64` | `0x4770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `SymGetSymFromName` | `0x4790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `SymGetSymFromName64` | `0x4790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `SymGetSymNext` | `0x47B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `SymGetSymNext64` | `0x47B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `SymGetSymPrev` | `0x47D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `SymGetSymPrev64` | `0x47D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `SymGetSymbolFile` | `0x47F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `SymGetSymbolFileW` | `0x4810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `SymGetTypeFromName` | `0x4830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `SymGetTypeFromNameW` | `0x4850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `SymGetTypeInfo` | `0x4870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `SymGetTypeInfoEx` | `0x4890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `SymInitialize` | `0x48B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `SymLoadModule` | `0x48D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `SymLoadModule64` | `0x48D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `SymMatchFileName` | `0x48F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `SymMatchFileNameW` | `0x4910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `SymMatchString` | `0x4930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `SymMatchStringA` | `0x4950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `SymMatchStringW` | `0x4970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `SymQueryInlineTrace` | `0x4990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `SymRegisterCallback` | `0x49B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `SymRegisterCallback64` | `0x49B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `SymRegisterFunctionEntryCallback` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `SymRegisterFunctionEntryCallback64` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `SymSetContext` | `0x49F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `SymSetExtendedOption` | `0x4A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `SymSetOptions` | `0x4A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `SymSetScopeFromAddr` | `0x4A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `SymSetScopeFromIndex` | `0x4A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `SymSetScopeFromInlineContext` | `0x4A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `SymSetSearchPath` | `0x4AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `SymSrvGetFileIndexString` | `0x4AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `SymSrvGetFileIndexStringW` | `0x4AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `SymSrvGetFileIndexes` | `0x4B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `SymSrvGetFileIndexesW` | `0x4B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `SymUnDName` | `0x4B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `SymUnDName64` | `0x4B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `SymUnloadModule` | `0x4B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `SymUnloadModule64` | `0x4B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `UnDecorateSymbolName` | `0x4B90` | 13,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `BindImage` | `0x7F20` | 32 | UnwindData |  |
| 11 | `BindImageEx` | `0x7F50` | 1,332 | UnwindData |  |
| 25 | `GetImageUnusedHeaderBytes` | `0x8690` | 273 | UnwindData |  |
| 27 | `GetTimestampForLoadedLibrary` | `0x87B0` | 351 | UnwindData |  |
| 161 | `TouchFileTimes` | `0x8A20` | 149 | UnwindData |  |
| 24 | `GetImageConfigInformation` | `0x8DE0` | 178 | UnwindData |  |
| 41 | `ImageUnload` | `0x8EA0` | 106 | UnwindData |  |
| 46 | `MapAndLoad` | `0x8F10` | 685 | UnwindData |  |
| 57 | `SetImageConfigInformation` | `0x92C0` | 399 | UnwindData |  |
| 163 | `UnMapAndLoad` | `0x9460` | 115 | UnwindData |  |
| 1 | `RemoveRelocations` | `0x9B60` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `ReBaseImage` | `0x9CB0` | 1,146 | UnwindData |  |
| 50 | `ReBaseImage64` | `0x9CB0` | 1,146 | UnwindData |  |
| 59 | `SplitSymbols` | `0xA130` | 959 | UnwindData |  |
| 52 | `RemovePrivateCvSymbolic` | `0xA500` | 72 | UnwindData |  |
| 53 | `RemovePrivateCvSymbolicEx` | `0xA550` | 835 | UnwindData |  |
| 164 | `UpdateDebugInfoFile` | `0xA8A0` | 23 | UnwindData |  |
| 165 | `UpdateDebugInfoFileEx` | `0xA8C0` | 519 | UnwindData |  |
| 28 | `ImageAddCertificate` | `0xAE10` | 936 | UnwindData |  |
| 35 | `ImageGetDigestStream` | `0xB1C0` | 1,939 | UnwindData |  |
| 38 | `ImageRemoveCertificate` | `0xB960` | 576 | UnwindData |  |
