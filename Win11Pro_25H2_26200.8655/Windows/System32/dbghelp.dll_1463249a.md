# Binary Specification: dbghelp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dbghelp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1463249a85bb239fcb536780f3b964c5f2fd68398ffbd35ebec0d65660c8d83e`
* **Total Exported Functions:** 268

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1159 | `MiniDumpReadDumpStream` | `0x0` | - | Forwarded | Forwarded to: `dbgcore.MiniDumpReadDumpStream` |
| 1160 | `MiniDumpWriteDump` | `0x0` | - | Forwarded | Forwarded to: `dbgcore.MiniDumpWriteDump` |
| 1292 | `SymInitialize` | `0xDDA0` | 75 | UnwindData |  |
| 1294 | `SymLoadModule` | `0xDE00` | 44 | UnwindData |  |
| 1295 | `SymLoadModule64` | `0xDE00` | 44 | UnwindData |  |
| 1296 | `SymLoadModuleEx` | `0xDE40` | 216 | UnwindData |  |
| 1293 | `SymInitializeW` | `0xDFF0` | 740 | UnwindData |  |
| 1139 | `EnumerateLoadedModulesW64` | `0xE2E0` | 87 | UnwindData |  |
| 1326 | `SymSetSearchPathW` | `0xE630` | 794 | UnwindData |  |
| 1183 | `SymCleanup` | `0xE960` | 67 | UnwindData |  |
| 1297 | `SymLoadModuleExW` | `0xF3A0` | 87 | UnwindData |  |
| 1231 | `SymFunctionTableAccess64AccessRoutines` | `0x12540` | 798 | UnwindData |  |
| 1345 | `SymUnloadModule` | `0x12870` | 259 | UnwindData |  |
| 1346 | `SymUnloadModule64` | `0x12870` | 259 | UnwindData |  |
| 1250 | `SymGetModuleBase` | `0x13060` | 110 | UnwindData |  |
| 1251 | `SymGetModuleBase64` | `0x13060` | 110 | UnwindData |  |
| 1219 | `SymFromAddr` | `0x13150` | 92 | UnwindData |  |
| 1121 | `SymGetLineFromAddrEx` | `0x131C0` | 219 | UnwindData |  |
| 1107 | *Ordinal Only* | `0x131C0` | 219 | UnwindData |  |
| 1223 | `SymFromInlineContext` | `0x132B0` | 75 | UnwindData |  |
| 1252 | `SymGetModuleInfo` | `0x133E0` | 178 | UnwindData |  |
| 1253 | `SymGetModuleInfo64` | `0x133E0` | 178 | UnwindData |  |
| 1254 | `SymGetModuleInfoW` | `0x134A0` | 1,416 | UnwindData |  |
| 1255 | `SymGetModuleInfoW64` | `0x134A0` | 1,416 | UnwindData |  |
| 1236 | `SymGetLineFromAddr` | `0x13A30` | 207 | UnwindData |  |
| 1237 | `SymGetLineFromAddr64` | `0x13A30` | 207 | UnwindData |  |
| 1115 | *Ordinal Only* | `0x13B10` | 227 | UnwindData |  |
| 1116 | *Ordinal Only* | `0x13D10` | 1,062 | UnwindData |  |
| 1158 | `MakeSureDirectoryPathExists` | `0x17570` | 534 | UnwindData |  |
| 1347 | `UnDecorateSymbolName` | `0x1A0F0` | 625 | UnwindData |  |
| 1161 | `RangeMapAddPeImageSections` | `0x23C30` | 187 | UnwindData |  |
| 1151 | `ImageDirectoryEntryToData` | `0x23D70` | 21 | UnwindData |  |
| 1152 | `ImageDirectoryEntryToDataEx` | `0x24F80` | 314 | UnwindData |  |
| 1153 | `ImageNtHeader` | `0x250C0` | 48 | UnwindData |  |
| 1348 | `UnDecorateSymbolNameW` | `0x297F0` | 166 | UnwindData |  |
| 1164 | `RangeMapRead` | `0x299D0` | 81 | UnwindData |  |
| 1173 | `StackWalk` | `0x29EF0` | 439 | UnwindData |  |
| 1175 | `StackWalk64` | `0x29EF0` | 439 | UnwindData |  |
| 1174 | `StackWalk2` | `0x2A0B0` | 766 | UnwindData |  |
| 1220 | `SymFromAddrW` | `0x2BA30` | 27 | UnwindData |  |
| 1224 | `SymFromInlineContextW` | `0x2BA60` | 75 | UnwindData |  |
| 1168 | `ReportSymbolLoadSummary` | `0x2BB30` | 371 | UnwindData |  |
| 1299 | `SymMatchFileNameW` | `0x2BCB0` | 235 | UnwindData |  |
| 1320 | `SymSetOptions` | `0x2BDB0` | 430 | UnwindData |  |
| 1232 | `SymGetExtendedOption` | `0x2BFA0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `FindDebugInfoFileExW` | `0x2C3A0` | 66 | UnwindData |  |
| 1330 | `SymSrvGetFileIndexInfoW` | `0x2DCC0` | 401 | UnwindData |  |
| 1162 | `RangeMapCreate` | `0x2EDC0` | 77 | UnwindData |  |
| 1277 | `SymGetSymFromAddr` | `0x2EFE0` | 51 | UnwindData |  |
| 1278 | `SymGetSymFromAddr64` | `0x2EFE0` | 51 | UnwindData |  |
| 1302 | `SymMatchStringW` | `0x2F640` | 58 | UnwindData |  |
| 1163 | `RangeMapFree` | `0x2F680` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `SymGetOptions` | `0x2F7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `SymGetSearchPath` | `0x2F7D0` | 129 | UnwindData |  |
| 1229 | `SymFunctionTableAccess` | `0x2F990` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `SymFunctionTableAccess64` | `0x2F990` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1218 | `SymFindFileInPathW` | `0x2FCF0` | 108 | UnwindData |  |
| 1167 | `RemoveInvalidModuleList` | `0x301D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `SetCheckUserInterruptShared` | `0x301D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1157 | `ImagehlpApiVersionEx` | `0x301E0` | 48 | UnwindData |  |
| 1311 | `SymRegisterCallbackW64` | `0x30240` | 130 | UnwindData |  |
| 1317 | `SymSetExtendedOption` | `0x302D0` | 8,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `GetSymLoadError` | `0x323D0` | 1,166,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1130 | `_EFN_DumpImage` | `0x14F140` | 18,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1140 | `ExtensionApiVersion` | `0x1538E0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1349 | `WinDbgExtensionDllInit` | `0x1539F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1350 | `block` | `0x153A40` | 440 | UnwindData |  |
| 1351 | `chksym` | `0x153C00` | 469 | UnwindData |  |
| 1353 | `dh` | `0x153DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1354 | `fptr` | `0x153DF0` | 128 | UnwindData |  |
| 1355 | `homedir` | `0x153E80` | 291 | UnwindData |  |
| 1356 | `inlinedbg` | `0x153FB0` | 92 | UnwindData |  |
| 1357 | `itoldyouso` | `0x154020` | 469 | UnwindData |  |
| 1358 | `lmi` | `0x154200` | 792 | UnwindData |  |
| 1359 | `lminfo` | `0x154520` | 532 | UnwindData |  |
| 1360 | `lmsourcesinfo` | `0x154740` | 802 | UnwindData |  |
| 1361 | `omap` | `0x154A70` | 497 | UnwindData |  |
| 1362 | `optdbgdump` | `0x154C70` | 301 | UnwindData |  |
| 1363 | `optdbgdumpaddr` | `0x154DB0` | 315 | UnwindData |  |
| 1364 | `srcfiles` | `0x154F00` | 269 | UnwindData |  |
| 1365 | `stack_force_ebp` | `0x155020` | 460 | UnwindData |  |
| 1366 | `stackdbg` | `0x155200` | 445 | UnwindData |  |
| 1367 | `sym` | `0x1553D0` | 318 | UnwindData |  |
| 1368 | `vc7fpo` | `0x155520` | 1,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `ImageRvaToSection` | `0x155CE0` | 87 | UnwindData |  |
| 1155 | `ImageRvaToVa` | `0x155D40` | 124 | UnwindData |  |
| 1150 | `GetTimestampForLoadedLibrary` | `0x155DD0` | 351 | UnwindData |  |
| 1233 | `SymGetFileLineOffsets64` | `0x157D90` | 301 | UnwindData |  |
| 1111 | `SymAllocDiaString` | `0x15CCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1117 | *Ordinal Only* | `0x15CD00` | 170 | UnwindData |  |
| 1118 | *Ordinal Only* | `0x15CDB0` | 101 | UnwindData |  |
| 1101 | *Ordinal Only* | `0x15CE20` | 231 | UnwindData |  |
| 1102 | *Ordinal Only* | `0x15CF10` | 132 | UnwindData |  |
| 1120 | *Ordinal Only* | `0x15CFA0` | 309 | UnwindData |  |
| 1119 | *Ordinal Only* | `0x15D0E0` | 106 | UnwindData |  |
| 1112 | `SymFreeDiaString` | `0x15D150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1113 | `SymGetDiaSession` | `0x15D160` | 154 | UnwindData |  |
| 1114 | `SymGetDiaSource` | `0x15D200` | 153 | UnwindData |  |
| 1103 | *Ordinal Only* | `0x15D2A0` | 43 | UnwindData |  |
| 1122 | `SymGetLineFromNameEx` | `0x15D2E0` | 199 | UnwindData |  |
| 1108 | *Ordinal Only* | `0x15D2E0` | 199 | UnwindData |  |
| 1104 | *Ordinal Only* | `0x15D3B0` | 1,621 | UnwindData |  |
| 1123 | `SymGetLineNextEx` | `0x15DA10` | 127 | UnwindData |  |
| 1109 | *Ordinal Only* | `0x15DA10` | 127 | UnwindData |  |
| 1105 | *Ordinal Only* | `0x15DAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `SymGetLinePrevEx` | `0x15DAC0` | 125 | UnwindData |  |
| 1110 | *Ordinal Only* | `0x15DAC0` | 125 | UnwindData |  |
| 1106 | *Ordinal Only* | `0x15DB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1125 | `SymGetOmapBlockBase` | `0x15DB70` | 109 | UnwindData |  |
| 1126 | `SymRegisterGetSourcePathPartCallback` | `0x15DBF0` | 107 | UnwindData |  |
| 1127 | `SymRegisterSourceFileUrlListCallback` | `0x15DC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `SymSetDiaSession` | `0x15DC90` | 41 | UnwindData |  |
| 1129 | `SymSetServiceManager` | `0x15DCC0` | 89 | UnwindData |  |
| 1135 | `EnumerateLoadedModules` | `0x15E090` | 85 | UnwindData |  |
| 1136 | `EnumerateLoadedModules64` | `0x15E090` | 85 | UnwindData |  |
| 1137 | `EnumerateLoadedModulesEx` | `0x15E0F0` | 82 | UnwindData |  |
| 1138 | `EnumerateLoadedModulesExW` | `0x15E150` | 82 | UnwindData |  |
| 1172 | `SetSymLoadError` | `0x15E1B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `SymAddSourceStream` | `0x15E1C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `SymAddSourceStreamA` | `0x15E1D0` | 101 | UnwindData |  |
| 1179 | `SymAddSourceStreamW` | `0x15E240` | 403 | UnwindData |  |
| 1180 | `SymAddSymbol` | `0x15E3E0` | 111 | UnwindData |  |
| 1181 | `SymAddSymbolW` | `0x15E460` | 261 | UnwindData |  |
| 1182 | `SymAddrIncludeInlineTrace` | `0x15E570` | 382 | UnwindData |  |
| 1184 | `SymCompareInlineTrace` | `0x15E700` | 1,386 | UnwindData |  |
| 1185 | `SymDeleteSymbol` | `0x15EC70` | 101 | UnwindData |  |
| 1186 | `SymDeleteSymbolW` | `0x15ECE0` | 337 | UnwindData |  |
| 1187 | `SymEnumLines` | `0x15EE40` | 193 | UnwindData |  |
| 1188 | `SymEnumLinesW` | `0x15EF10` | 93 | UnwindData |  |
| 1189 | `SymEnumProcesses` | `0x15EF80` | 136 | UnwindData |  |
| 1190 | `SymEnumSourceFileTokens` | `0x15F010` | 158 | UnwindData |  |
| 1191 | `SymEnumSourceFiles` | `0x15F0C0` | 33 | UnwindData |  |
| 1192 | `SymEnumSourceFilesW` | `0x15F0F0` | 33 | UnwindData |  |
| 1193 | `SymEnumSourceLines` | `0x15F120` | 69 | UnwindData |  |
| 1194 | `SymEnumSourceLinesW` | `0x15F170` | 69 | UnwindData |  |
| 1195 | `SymEnumSym` | `0x15F1C0` | 34 | UnwindData |  |
| 1196 | `SymEnumSymbols` | `0x15F1F0` | 33 | UnwindData |  |
| 1197 | `SymEnumSymbolsEx` | `0x15F220` | 144 | UnwindData |  |
| 1198 | `SymEnumSymbolsExW` | `0x15F2C0` | 91 | UnwindData |  |
| 1199 | `SymEnumSymbolsForAddr` | `0x15F330` | 321 | UnwindData |  |
| 1200 | `SymEnumSymbolsForAddrW` | `0x15F480` | 324 | UnwindData |  |
| 1201 | `SymEnumSymbolsW` | `0x15F5D0` | 33 | UnwindData |  |
| 1202 | `SymEnumTypes` | `0x15F600` | 70 | UnwindData |  |
| 1203 | `SymEnumTypesByName` | `0x15F650` | 197 | UnwindData |  |
| 1204 | `SymEnumTypesByNameW` | `0x15F720` | 80 | UnwindData |  |
| 1205 | `SymEnumTypesW` | `0x15F780` | 74 | UnwindData |  |
| 1206 | `SymEnumerateModules` | `0x15F7D0` | 52 | UnwindData |  |
| 1207 | `SymEnumerateModules64` | `0x15F7D0` | 52 | UnwindData |  |
| 1208 | `SymEnumerateModulesW64` | `0x15F810` | 56 | UnwindData |  |
| 1209 | `SymEnumerateSymbols` | `0x15F850` | 72 | UnwindData |  |
| 1210 | `SymEnumerateSymbols64` | `0x15F850` | 72 | UnwindData |  |
| 1211 | `SymEnumerateSymbolsW` | `0x15F8A0` | 72 | UnwindData |  |
| 1212 | `SymEnumerateSymbolsW64` | `0x15F8A0` | 72 | UnwindData |  |
| 1221 | `SymFromIndex` | `0x15F8F0` | 143 | UnwindData |  |
| 1222 | `SymFromIndexW` | `0x15F990` | 239 | UnwindData |  |
| 1225 | `SymFromName` | `0x15FA90` | 126 | UnwindData |  |
| 1226 | `SymFromNameW` | `0x15FB20` | 42 | UnwindData |  |
| 1227 | `SymFromToken` | `0x15FB50` | 180 | UnwindData |  |
| 1228 | `SymFromTokenW` | `0x15FC10` | 253 | UnwindData |  |
| 1234 | `SymGetHomeDirectory` | `0x15FD20` | 109 | UnwindData |  |
| 1235 | `SymGetHomeDirectoryW` | `0x15FDA0` | 178 | UnwindData |  |
| 1238 | `SymGetLineFromAddrW64` | `0x15FE60` | 38 | UnwindData |  |
| 1239 | `SymGetLineFromInlineContext` | `0x15FE90` | 43 | UnwindData |  |
| 1240 | `SymGetLineFromInlineContextW` | `0x15FED0` | 43 | UnwindData |  |
| 1241 | `SymGetLineFromName` | `0x15FF10` | 41 | UnwindData |  |
| 1242 | `SymGetLineFromName64` | `0x15FF10` | 41 | UnwindData |  |
| 1243 | `SymGetLineFromNameW64` | `0x15FF40` | 41 | UnwindData |  |
| 1244 | `SymGetLineNext` | `0x15FF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1245 | `SymGetLineNext64` | `0x15FF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1246 | `SymGetLineNextW64` | `0x15FF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1247 | `SymGetLinePrev` | `0x15FFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `SymGetLinePrev64` | `0x15FFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `SymGetLinePrevW64` | `0x15FFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1256 | `SymGetOmaps` | `0x15FFD0` | 221 | UnwindData |  |
| 1258 | `SymGetParentWindow` | `0x1600C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1259 | `SymGetScope` | `0x1600E0` | 152 | UnwindData |  |
| 1260 | `SymGetScopeW` | `0x160180` | 287 | UnwindData |  |
| 1262 | `SymGetSearchPathW` | `0x1602B0` | 101 | UnwindData |  |
| 1263 | `SymGetSourceFile` | `0x160320` | 158 | UnwindData |  |
| 1264 | `SymGetSourceFileChecksum` | `0x1603D0` | 124 | UnwindData |  |
| 1265 | `SymGetSourceFileChecksumW` | `0x160460` | 292 | UnwindData |  |
| 1266 | `SymGetSourceFileFromToken` | `0x160590` | 38 | UnwindData |  |
| 1267 | `SymGetSourceFileFromTokenByTokenName` | `0x1605C0` | 196 | UnwindData |  |
| 1268 | `SymGetSourceFileFromTokenByTokenNameW` | `0x160690` | 126 | UnwindData |  |
| 1269 | `SymGetSourceFileFromTokenW` | `0x160720` | 38 | UnwindData |  |
| 1270 | `SymGetSourceFileToken` | `0x160750` | 43 | UnwindData |  |
| 1271 | `SymGetSourceFileTokenByTokenName` | `0x160790` | 173 | UnwindData |  |
| 1272 | `SymGetSourceFileTokenByTokenNameW` | `0x160850` | 215 | UnwindData |  |
| 1273 | `SymGetSourceFileTokenW` | `0x160930` | 43 | UnwindData |  |
| 1274 | `SymGetSourceFileW` | `0x160970` | 158 | UnwindData |  |
| 1275 | `SymGetSourceVarFromToken` | `0x160A20` | 202 | UnwindData |  |
| 1276 | `SymGetSourceVarFromTokenW` | `0x160AF0` | 165 | UnwindData |  |
| 1279 | `SymGetSymFromName` | `0x160BA0` | 106 | UnwindData |  |
| 1280 | `SymGetSymFromName64` | `0x160BA0` | 106 | UnwindData |  |
| 1281 | `SymGetSymNext` | `0x160C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1282 | `SymGetSymNext64` | `0x160C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1283 | `SymGetSymPrev` | `0x160C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `SymGetSymPrev64` | `0x160C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `SymGetTypeFromName` | `0x160C40` | 189 | UnwindData |  |
| 1288 | `SymGetTypeFromNameW` | `0x160D10` | 312 | UnwindData |  |
| 1289 | `SymGetTypeInfo` | `0x160E50` | 51 | UnwindData |  |
| 1290 | `SymGetTypeInfoEx` | `0x160E90` | 41 | UnwindData |  |
| 1291 | `SymGetUnwindInfo` | `0x160EC0` | 445 | UnwindData |  |
| 1298 | `SymMatchFileName` | `0x161090` | 264 | UnwindData |  |
| 1300 | `SymMatchString` | `0x1611A0` | 58 | UnwindData |  |
| 1301 | `SymMatchStringA` | `0x1611E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `SymNext` | `0x1611F0` | 164 | UnwindData |  |
| 1304 | `SymNextW` | `0x1612A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1305 | `SymPrev` | `0x1612C0` | 162 | UnwindData |  |
| 1306 | `SymPrevW` | `0x161370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `SymQueryInlineTrace` | `0x161380` | 819 | UnwindData |  |
| 1308 | `SymRefreshModuleList` | `0x1616C0` | 199 | UnwindData |  |
| 1309 | `SymRegisterCallback` | `0x161790` | 122 | UnwindData |  |
| 1310 | `SymRegisterCallback64` | `0x161790` | 122 | UnwindData |  |
| 1312 | `SymRegisterFunctionEntryCallback` | `0x161810` | 117 | UnwindData |  |
| 1313 | `SymRegisterFunctionEntryCallback64` | `0x161810` | 117 | UnwindData |  |
| 1314 | `SymSearch` | `0x161890` | 179 | UnwindData |  |
| 1315 | `SymSearchW` | `0x161950` | 112 | UnwindData |  |
| 1316 | `SymSetContext` | `0x1619D0` | 176 | UnwindData |  |
| 1318 | `SymSetHomeDirectory` | `0x161A90` | 150 | UnwindData |  |
| 1319 | `SymSetHomeDirectoryW` | `0x161B30` | 106 | UnwindData |  |
| 1321 | `SymSetParentWindow` | `0x161BA0` | 41 | UnwindData |  |
| 1322 | `SymSetScopeFromAddr` | `0x161BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `SymSetScopeFromIndex` | `0x161BE0` | 176 | UnwindData |  |
| 1324 | `SymSetScopeFromInlineContext` | `0x161CA0` | 196 | UnwindData |  |
| 1325 | `SymSetSearchPath` | `0x161D70` | 59 | UnwindData |  |
| 1343 | `SymUnDName` | `0x161DC0` | 75 | UnwindData |  |
| 1344 | `SymUnDName64` | `0x161DC0` | 75 | UnwindData |  |
| 1352 | `dbghelp` | `0x161E20` | 141 | UnwindData |  |
| 1133 | `EnumDirTree` | `0x162C60` | 293 | UnwindData |  |
| 1134 | `EnumDirTreeW` | `0x162D90` | 80 | UnwindData |  |
| 1141 | `FindDebugInfoFile` | `0x162DF0` | 24 | UnwindData |  |
| 1142 | `FindDebugInfoFileEx` | `0x162E10` | 202 | UnwindData |  |
| 1144 | `FindExecutableImage` | `0x162EE0` | 24 | UnwindData |  |
| 1145 | `FindExecutableImageEx` | `0x162F00` | 250 | UnwindData |  |
| 1146 | `FindExecutableImageExW` | `0x163000` | 66 | UnwindData |  |
| 1147 | `FindFileInPath` | `0x163050` | 73 | UnwindData |  |
| 1148 | `FindFileInSearchPath` | `0x1630A0` | 73 | UnwindData |  |
| 1156 | `ImagehlpApiVersion` | `0x1630F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1169 | `SearchTreeForFile` | `0x163100` | 40 | UnwindData |  |
| 1170 | `SearchTreeForFileW` | `0x163130` | 40 | UnwindData |  |
| 1213 | `SymFindDebugInfoFile` | `0x163160` | 232 | UnwindData |  |
| 1214 | `SymFindDebugInfoFileW` | `0x163250` | 129 | UnwindData |  |
| 1215 | `SymFindExecutableImage` | `0x1632E0` | 246 | UnwindData |  |
| 1216 | `SymFindExecutableImageW` | `0x1633E0` | 129 | UnwindData |  |
| 1217 | `SymFindFileInPath` | `0x163470` | 312 | UnwindData |  |
| 1285 | `SymGetSymbolFile` | `0x167580` | 294 | UnwindData |  |
| 1286 | `SymGetSymbolFileW` | `0x1676B0` | 1,226 | UnwindData |  |
| 1327 | `SymSrvDeltaName` | `0x167B80` | 202 | UnwindData |  |
| 1328 | `SymSrvDeltaNameW` | `0x167C50` | 422 | UnwindData |  |
| 1329 | `SymSrvGetFileIndexInfo` | `0x167E00` | 236 | UnwindData |  |
| 1331 | `SymSrvGetFileIndexString` | `0x167F00` | 185 | UnwindData |  |
| 1332 | `SymSrvGetFileIndexStringW` | `0x167FC0` | 296 | UnwindData |  |
| 1333 | `SymSrvGetFileIndexes` | `0x1680F0` | 96 | UnwindData |  |
| 1334 | `SymSrvGetFileIndexesW` | `0x168160` | 192 | UnwindData |  |
| 1335 | `SymSrvGetSupplement` | `0x168230` | 179 | UnwindData |  |
| 1336 | `SymSrvGetSupplementW` | `0x1682F0` | 259 | UnwindData |  |
| 1337 | `SymSrvIsStore` | `0x168400` | 59 | UnwindData |  |
| 1338 | `SymSrvIsStoreW` | `0x168450` | 247 | UnwindData |  |
| 1339 | `SymSrvStoreFile` | `0x168550` | 149 | UnwindData |  |
| 1340 | `SymSrvStoreFileW` | `0x1685F0` | 196 | UnwindData |  |
| 1341 | `SymSrvStoreSupplement` | `0x1686C0` | 187 | UnwindData |  |
| 1342 | `SymSrvStoreSupplementW` | `0x168790` | 231 | UnwindData |  |
| 1131 | `DbgHelpCreateUserDump` | `0x168880` | 18,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1132 | `DbgHelpCreateUserDumpW` | `0x168880` | 18,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `StackWalkEx` | `0x16CFE0` | 94 | UnwindData |  |
| 1165 | `RangeMapRemove` | `0x178190` | 119 | UnwindData |  |
| 1166 | `RangeMapWrite` | `0x178210` | 82 | UnwindData |  |
