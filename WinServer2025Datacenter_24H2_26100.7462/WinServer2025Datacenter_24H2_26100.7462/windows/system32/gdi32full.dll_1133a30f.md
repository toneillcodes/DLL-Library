# Binary Specification: gdi32full.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\gdi32full.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1133a30fbd644948d1fd9821fe32b578ad7fe477fc1fc20cc4ba3fc750b50e7c`
* **Total Exported Functions:** 1017

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1097 | `CreateDCW` | `0x0` | - | Forwarded | Forwarded to: `GDI32.CreateDCW` |
| 1118 | `CreateICW` | `0x0` | - | Forwarded | Forwarded to: `GDI32.CreateICW` |
| 1135 | `DeleteDC` | `0x0` | - | Forwarded | Forwarded to: `GDI32.DeleteDC` |
| 1892 | `ScriptFreeCache` | `0x21C0` | 115 | UnwindData |  |
| 2007 | `UspAllocCache` | `0x5E50` | 100 | UnwindData |  |
| 1911 | `ScriptShape` | `0x6850` | 182 | UnwindData |  |
| 2009 | `UspFreeMem` | `0x8DC0` | 433 | UnwindData |  |
| 1907 | `ScriptPlace` | `0x8F80` | 114 | UnwindData |  |
| 1906 | `ScriptLayout` | `0xA700` | 75 | UnwindData |  |
| 1891 | `ScriptCacheGetHeight` | `0xCBF0` | 42 | UnwindData |  |
| 2008 | `UspAllocTemp` | `0xDE70` | 53 | UnwindData |  |
| 1360 | `GetObjectA` | `0xE0C0` | 825 | UnwindData |  |
| 1362 | `GetObjectW` | `0xE480` | 234 | UnwindData |  |
| 1238 | `GdiFixUpHandle` | `0xE570` | 102 | UnwindData |  |
| 1915 | `ScriptStringFree` | `0xEAE0` | 34 | UnwindData |  |
| 1887 | `ScriptApplyDigitSubstitution` | `0xEE60` | 59 | UnwindData |  |
| 1402 | `GetViewportExtEx` | `0xF660` | 325 | UnwindData |  |
| 1310 | `GetCurrentObject` | `0xF7B0` | 452 | UnwindData |  |
| 1405 | `GetWindowExtEx` | `0xF980` | 288 | UnwindData |  |
| 1264 | `GdiRealizationInfo` | `0xFAB0` | 39 | UnwindData |  |
| 1364 | `GetOutlineTextMetricsW` | `0xFEA0` | 47 | UnwindData |  |
| 1914 | `ScriptStringCPtoX` | `0x10360` | 377 | UnwindData |  |
| 1890 | `ScriptCPtoX` | `0x104E0` | 427 | UnwindData |  |
| 1918 | `ScriptStringOut` | `0x10C50` | 104 | UnwindData |  |
| 1286 | `GetBkMode` | `0x12C70` | 256 | UnwindData |  |
| 1361 | `GetObjectType` | `0x12EB0` | 638 | UnwindData |  |
| 1426 | `LpkTabbedTextOut` | `0x13140` | 1,193 | UnwindData |  |
| 1386 | `GetTextColor` | `0x135F0` | 167 | UnwindData |  |
| 1123 | `CreatePen` | `0x137A0` | 364 | UnwindData |  |
| 1428 | `MaskBlt` | `0x13A90` | 514 | UnwindData |  |
| 1285 | `GetBkColor` | `0x13CA0` | 167 | UnwindData |  |
| 1416 | `LPtoDP` | `0x13D50` | 396 | UnwindData |  |
| 1311 | `GetCurrentPositionEx` | `0x13EF0` | 100 | UnwindData |  |
| 1860 | `PolyPatBlt` | `0x147A0` | 1,012 | UnwindData |  |
| 1943 | `SetBrushOrgEx` | `0x15D20` | 716 | UnwindData |  |
| 1070 | `BitBlt` | `0x161A0` | 901 | UnwindData |  |
| 1848 | `PatBlt` | `0x16530` | 986 | UnwindData |  |
| 1954 | `SetGraphicsMode` | `0x169F0` | 306 | UnwindData |  |
| 1986 | `SetWindowOrgEx` | `0x17AB0` | 302 | UnwindData |  |
| 1982 | `SetViewportOrgEx` | `0x18000` | 689 | UnwindData |  |
| 1973 | `SetStretchBltModeImpl` | `0x182C0` | 619 | UnwindData |  |
| 1979 | `SetTextColorImpl` | `0x185E0` | 749 | UnwindData |  |
| 1435 | `MoveToExImpl` | `0x188E0` | 709 | UnwindData |  |
| 1976 | `SetTextAlignImpl` | `0x18BB0` | 631 | UnwindData |  |
| 1938 | `SetBkColor` | `0x18F10` | 773 | UnwindData |  |
| 1940 | `SetBkModeImpl` | `0x19220` | 615 | UnwindData |  |
| 1967 | `SetPixelV` | `0x196A0` | 500 | UnwindData |  |
| 1377 | `GetStockObject` | `0x198A0` | 327 | UnwindData |  |
| 1079 | `CloseFigureImpl` | `0x19BA0` | 118 | UnwindData |  |
| 1049 | `SelectObjectImpl` | `0x19C20` | 125 | UnwindData |  |
| 1041 | `LineToImpl` | `0x1B370` | 272 | UnwindData |  |
| 1858 | `PolyBezierToImpl` | `0x1B5F0` | 492 | UnwindData |  |
| 1191 | `FillPathImpl` | `0x1DB40` | 192 | UnwindData |  |
| 1962 | `SetMetaRgn` | `0x1E160` | 122 | UnwindData |  |
| 1352 | `GetMapMode` | `0x1E3E0` | 279 | UnwindData |  |
| 1406 | `GetWindowOrgEx` | `0x1E500` | 203 | UnwindData |  |
| 1403 | `GetViewportOrgEx` | `0x1E5E0` | 297 | UnwindData |  |
| 1101 | `CreateDIBitmap` | `0x1E710` | 2,007 | UnwindData |  |
| 1996 | `StrokePathImpl` | `0x1EFD0` | 194 | UnwindData |  |
| 1107 | `CreateEnhMetaFileW` | `0x1F580` | 236 | UnwindData |  |
| 1994 | `StretchDIBitsImpl` | `0x1F780` | 4,075 | UnwindData |  |
| 1317 | `GetDIBits` | `0x20780` | 165 | UnwindData |  |
| 1106 | `CreateEnhMetaFileA` | `0x20CF0` | 327 | UnwindData |  |
| 1853 | `PlayMetaFile` | `0x210F0` | 98 | UnwindData |  |
| 1932 | `SelectPalette` | `0x21160` | 159 | UnwindData |  |
| 1949 | `SetDIBits` | `0x21210` | 777 | UnwindData |  |
| 1950 | `SetDIBitsToDevice` | `0x21520` | 4,020 | UnwindData |  |
| 1094 | `CreateCompatibleDC` | `0x224E0` | 306 | UnwindData |  |
| 1854 | `PlayMetaFileRecord` | `0x232E0` | 8,200 | UnwindData |  |
| 1852 | `PlayEnhMetaFileRecord` | `0x25320` | 1,040 | UnwindData |  |
| 1279 | `GditPushCallerInfo` | `0x25740` | 75 | UnwindData |  |
| 1998 | `TextOutA` | `0x257A0` | 180 | UnwindData |  |
| 1019 | `ExtTextOutAImpl` | `0x25860` | 70 | UnwindData |  |
| 1278 | `GditPopCallerInfo` | `0x26150` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1999 | `TextOutW` | `0x261C0` | 653 | UnwindData |  |
| 1870 | `QueryFontAssocStatus` | `0x26460` | 41 | UnwindData |  |
| 1011 | `DeleteFont` | `0x265B0` | 273 | UnwindData |  |
| 1387 | `GetTextExtentExPointA` | `0x26B20` | 824 | UnwindData |  |
| 1307 | `GetCodePage` | `0x26E60` | 303 | UnwindData |  |
| 1248 | `GdiGetVariationStoreDelta` | `0x27780` | 395 | UnwindData |  |
| 1185 | `ExtCreatePen` | `0x28560` | 453 | UnwindData |  |
| 1090 | `CreateBrushIndirect` | `0x28730` | 195 | UnwindData |  |
| 1108 | `CreateFontA` | `0x28960` | 179 | UnwindData |  |
| 1109 | `CreateFontIndirectA` | `0x28A20` | 174 | UnwindData |  |
| 1114 | `CreateFontW` | `0x28AE0` | 230 | UnwindData |  |
| 1112 | `CreateFontIndirectW` | `0x29030` | 341 | UnwindData |  |
| 1113 | `CreateFontIndirectWImpl` | `0x29030` | 341 | UnwindData |  |
| 1111 | `CreateFontIndirectExW` | `0x29190` | 569 | UnwindData |  |
| 1272 | `GdiTrackHCreate` | `0x293D0` | 252 | UnwindData |  |
| 1077 | `CloseEnhMetaFile` | `0x2A530` | 946 | UnwindData |  |
| 1410 | `InternalDeleteDC` | `0x2A8F0` | 968 | UnwindData |  |
| 1408 | `IcmDeleteLocalDC` | `0x2ACC0` | 314 | UnwindData |  |
| 1273 | `GdiTrackHDelete` | `0x2AE00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1042 | `MF_DeleteObjectHelper` | `0x2AE30` | 196 | UnwindData |  |
| 1330 | `GetEnhMetaFileW` | `0x2B480` | 104 | UnwindData |  |
| 1117 | `CreateICA` | `0x2BD00` | 29 | UnwindData |  |
| 1008 | `CreateDCAImpl` | `0x2BD30` | 26 | UnwindData |  |
| 1055 | `hdcCreateDCW` | `0x2BF60` | 2,174 | UnwindData |  |
| 1409 | `IcmReleaseCachedColorSpace` | `0x2C7F0` | 470 | UnwindData |  |
| 1335 | `GetFontLanguageInfo` | `0x2CEC0` | 105 | UnwindData |  |
| 1985 | `SetWindowExtEx` | `0x2D020` | 615 | UnwindData |  |
| 1981 | `SetViewportExtEx` | `0x2D290` | 532 | UnwindData |  |
| 1845 | `OffsetViewportOrgEx` | `0x2D4B0` | 476 | UnwindData |  |
| 1957 | `SetLayout` | `0x2D6A0` | 338 | UnwindData |  |
| 1046 | `SaveDCImpl` | `0x2D800` | 390 | UnwindData |  |
| 1959 | `SetMapMode` | `0x2D990` | 389 | UnwindData |  |
| 1846 | `OffsetWindowOrgEx` | `0x2DB20` | 459 | UnwindData |  |
| 1045 | `RestoreDCImpl` | `0x2DD00` | 563 | UnwindData |  |
| 1970 | `SetROP2` | `0x2E130` | 498 | UnwindData |  |
| 1131 | `CreateSessionMappedDIBSection` | `0x2E7F0` | 44 | UnwindData |  |
| 1102 | `CreateDPIScaledDIBSection` | `0x2E830` | 52 | UnwindData |  |
| 1100 | `CreateDIBSection` | `0x2E870` | 49 | UnwindData |  |
| 1346 | `GetICMProfileW` | `0x30440` | 446 | UnwindData |  |
| 1179 | `EnumICMProfilesW` | `0x31DE0` | 217 | UnwindData |  |
| 1945 | `SetColorSpace` | `0x323C0` | 128 | UnwindData |  |
| 1050 | `SetICMModeImpl` | `0x32450` | 1,060 | UnwindData |  |
| 1262 | `GdiPrinterThunk` | `0x32940` | 11,109 | UnwindData |  |
| 1043 | `RectangleImpl` | `0x35AA0` | 306 | UnwindData |  |
| 1018 | `ExtEscapeImpl` | `0x37210` | 1,523 | UnwindData |  |
| 1254 | `GdiIsUMPDSandboxingEnabled` | `0x37AD0` | 660 | UnwindData |  |
| 1389 | `GetTextExtentExPointW` | `0x37DF0` | 130 | UnwindData |  |
| 1040 | `GetTextMetricsAImpl` | `0x38700` | 378 | UnwindData |  |
| 1343 | `GetGraphicsMode` | `0x38A60` | 164 | UnwindData |  |
| 1242 | `GdiGetCharDimensions` | `0x39340` | 516 | UnwindData |  |
| 1383 | `GetTextCharacterExtra` | `0x396E0` | 169 | UnwindData |  |
| 1020 | `ExtTextOutWImpl` | `0x39A30` | 2,084 | UnwindData |  |
| 1395 | `GetTextExtentPointW` | `0x3AB10` | 624 | UnwindData |  |
| 1420 | `LpkExtTextOut` | `0x3B310` | 76 | UnwindData |  |
| 1306 | `GetClipRgn` | `0x3BA10` | 273 | UnwindData |  |
| 1349 | `GetLayout` | `0x3BB30` | 282 | UnwindData |  |
| 1392 | `GetTextExtentPoint32W` | `0x3BC50` | 627 | UnwindData |  |
| 1382 | `GetTextAlign` | `0x3CC40` | 237 | UnwindData |  |
| 1336 | `GetFontRealizationInfo` | `0x3CD40` | 110 | UnwindData |  |
| 1400 | `GetTextMetricsW` | `0x3D0D0` | 221 | UnwindData |  |
| 1313 | `GetDCDpiScaleValue` | `0x3DE40` | 301 | UnwindData |  |
| 1925 | `ScriptTextOut` | `0x3E480` | 171 | UnwindData |  |
| 1422 | `LpkGetTextExtentExPoint` | `0x3EC40` | 2,542 | UnwindData |  |
| 1419 | `LpkDrawTextEx` | `0x3FDD0` | 127 | UnwindData |  |
| 1910 | `ScriptRecordDigitSubstitution` | `0x404B0` | 949 | UnwindData |  |
| 1903 | `ScriptItemize` | `0x425D0` | 110 | UnwindData |  |
| 1913 | `ScriptStringAnalyse` | `0x42650` | 73 | UnwindData |  |
| 1902 | `ScriptIsComplex` | `0x48EE0` | 60 | UnwindData |  |
| 2001 | `TranslateCharsetInfo` | `0x4AF10` | 578 | UnwindData |  |
| 1865 | `Polygon` | `0x4B7F0` | 244 | UnwindData |  |
| 1866 | `Polyline` | `0x4B8F0` | 243 | UnwindData |  |
| 1099 | `CreateDIBPatternBrushPt` | `0x4C040` | 164 | UnwindData |  |
| 1415 | `IsValidEnhMetaRecordOffExt` | `0x4C890` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `GdiAlphaBlend` | `0x4CC30` | 484 | UnwindData |  |
| 1344 | `GetHFONT` | `0x4D400` | 234 | UnwindData |  |
| 1187 | `ExtSelectClipRgnImpl` | `0x4D4F0` | 1,372 | UnwindData |  |
| 1393 | `GetTextExtentPointA` | `0x4DC60` | 23 | UnwindData |  |
| 1391 | `GetTextExtentPoint32A` | `0x4DC80` | 20 | UnwindData |  |
| 1427 | `LpkUseGDIWidthCache` | `0x4E0D0` | 568 | UnwindData |  |
| 1222 | `GdiEndPageEMF` | `0x4F9D0` | 461 | UnwindData |  |
| 1433 | `ModifyWorldTransform` | `0x50550` | 465 | UnwindData |  |
| 1988 | `SetWorldTransformImpl` | `0x50730` | 439 | UnwindData |  |
| 1337 | `GetFontResourceInfoW` | `0x510E0` | 441 | UnwindData |  |
| 1877 | `RemoveFontResourceExW` | `0x512A0` | 193 | UnwindData |  |
| 1198 | `GdiAddFontResourceW` | `0x51370` | 419 | UnwindData |  |
| 2013 | `bMakePathNameW` | `0x518D0` | 711 | UnwindData |  |
| 2014 | `cGetTTFFromFOT` | `0x51BA0` | 841 | UnwindData |  |
| 2012 | `bInitSystemAndFontsDirectoriesW` | `0x52180` | 584 | UnwindData |  |
| 1889 | `ScriptBreak` | `0x52B50` | 405 | UnwindData |  |
| 1250 | `GdiInitializeLanguagePack` | `0x52CF0` | 134 | UnwindData |  |
| 1423 | `LpkInitialize` | `0x52D80` | 94 | UnwindData |  |
| 1885 | `ScaleViewportExtEx` | `0x532A0` | 426 | UnwindData |  |
| 1886 | `ScaleWindowExtEx` | `0x53450` | 426 | UnwindData |  |
| 1412 | `IntersectClipRectImpl` | `0x53600` | 220 | UnwindData |  |
| 1916 | `ScriptStringGetLogicalWidths` | `0x53960` | 309 | UnwindData |  |
| 1900 | `ScriptGetLogicalWidths` | `0x53AA0` | 362 | UnwindData |  |
| 1093 | `CreateCompatibleBitmap` | `0x53ED0` | 543 | UnwindData |  |
| 1920 | `ScriptStringXtoCP` | `0x54C90` | 446 | UnwindData |  |
| 1926 | `ScriptXtoCP` | `0x54E60` | 495 | UnwindData |  |
| 1007 | *Ordinal Only* | `0x557B0` | 337 | UnwindData |  |
| 1176 | `EnumFontsA` | `0x559B0` | 35 | UnwindData |  |
| 1172 | `EnumFontFamiliesA` | `0x559E0` | 37 | UnwindData |  |
| 1177 | `EnumFontsW` | `0x55A10` | 39 | UnwindData |  |
| 1175 | `EnumFontFamiliesW` | `0x55A40` | 43 | UnwindData |  |
| 1173 | `EnumFontFamiliesExA` | `0x55A80` | 70 | UnwindData |  |
| 1174 | `EnumFontFamiliesExW` | `0x55BE0` | 80 | UnwindData |  |
| 1908 | `ScriptPlaceOpenType` | `0x56700` | 1,153 | UnwindData |  |
| 1992 | `StretchBlt` | `0x56F70` | 912 | UnwindData |  |
| 1241 | `GdiGetBitmapBitsSize` | `0x57770` | 173 | UnwindData |  |
| 1220 | `GdiDrawStream` | `0x57930` | 1,383 | UnwindData |  |
| 1166 | `EngQueryEMFInfo` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `FixBrushOrgEx` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `GdiEntry1` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1224 | `GdiEntry10` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `GdiEntry11` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `GdiEntry14` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1228 | `GdiEntry15` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `GdiEntry2` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `GdiEntry3` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `GdiEntry4` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1233 | `GdiEntry5` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `GdiEntry6` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1235 | `GdiEntry7` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1236 | `GdiEntry8` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1256 | `GdiPlayDCScript` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `GdiPlayJournal` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `GdiPlayScript` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `ModerncoreCreateICW` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `ModerncoreDeleteDC` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1432 | `ModerncoreGdiInit` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1496 | `NtGdiD3dContextCreate` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1497 | `NtGdiD3dContextDestroy` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1498 | `NtGdiD3dContextDestroyAll` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1499 | `NtGdiD3dDrawPrimitives2` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1500 | `NtGdiD3dValidateTextureStageState` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1507 | `NtGdiDdAddAttachedSurface` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1508 | `NtGdiDdAlphaBlt` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1509 | `NtGdiDdAttachSurface` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `NtGdiDdBeginMoCompFrame` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1511 | `NtGdiDdBlt` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `NtGdiDdCanCreateD3DBuffer` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1513 | `NtGdiDdCanCreateSurface` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1514 | `NtGdiDdColorControl` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1515 | `NtGdiDdCreateD3DBuffer` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1516 | `NtGdiDdCreateDirectDrawObject` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1518 | `NtGdiDdCreateMoComp` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `NtGdiDdCreateSurface` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1520 | `NtGdiDdCreateSurfaceEx` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1521 | `NtGdiDdCreateSurfaceObject` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `NtGdiDdDeleteDirectDrawObject` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1523 | `NtGdiDdDeleteSurfaceObject` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1524 | `NtGdiDdDestroyD3DBuffer` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1526 | `NtGdiDdDestroyMoComp` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1527 | `NtGdiDdDestroySurface` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1528 | `NtGdiDdEndMoCompFrame` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `NtGdiDdFlip` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1530 | `NtGdiDdFlipToGDISurface` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `NtGdiDdGetAvailDriverMemory` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1532 | `NtGdiDdGetBltStatus` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1533 | `NtGdiDdGetDC` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1534 | `NtGdiDdGetDriverInfo` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1535 | `NtGdiDdGetDriverState` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1536 | `NtGdiDdGetDxHandle` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1537 | `NtGdiDdGetFlipStatus` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `NtGdiDdGetInternalMoCompInfo` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `NtGdiDdGetMoCompBuffInfo` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1540 | `NtGdiDdGetMoCompFormats` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1541 | `NtGdiDdGetMoCompGuids` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1542 | `NtGdiDdGetScanLine` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1543 | `NtGdiDdLock` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1544 | `NtGdiDdLockD3D` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1546 | `NtGdiDdQueryDirectDrawObject` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1547 | `NtGdiDdQueryMoCompStatus` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1549 | `NtGdiDdReenableDirectDrawObject` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1550 | `NtGdiDdReleaseDC` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1551 | `NtGdiDdRenderMoComp` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1552 | `NtGdiDdResetVisrgn` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1553 | `NtGdiDdSetColorKey` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1554 | `NtGdiDdSetExclusiveMode` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1555 | `NtGdiDdSetGammaRamp` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1556 | `NtGdiDdSetOverlayPosition` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1558 | `NtGdiDdUnlock` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1559 | `NtGdiDdUnlockD3D` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1560 | `NtGdiDdUpdateOverlay` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1561 | `NtGdiDdWaitForVerticalBlank` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1573 | `NtGdiDvpAcquireNotification` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1574 | `NtGdiDvpCanCreateVideoPort` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1575 | `NtGdiDvpColorControl` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1576 | `NtGdiDvpCreateVideoPort` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1577 | `NtGdiDvpDestroyVideoPort` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `NtGdiDvpFlipVideoPort` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1579 | `NtGdiDvpGetVideoPortBandwidth` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1580 | `NtGdiDvpGetVideoPortConnectInfo` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `NtGdiDvpGetVideoPortField` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1582 | `NtGdiDvpGetVideoPortFlipStatus` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1583 | `NtGdiDvpGetVideoPortInputFormats` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1584 | `NtGdiDvpGetVideoPortLine` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1585 | `NtGdiDvpGetVideoPortOutputFormats` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1586 | `NtGdiDvpGetVideoSignalStatus` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1587 | `NtGdiDvpReleaseNotification` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `NtGdiDvpUpdateVideoPort` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1589 | `NtGdiDvpWaitForVideoPortSync` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1591 | `NtGdiDxgGenericThunk` | `0x57F30` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `GetFontFileInfo` | `0x58E30` | 789 | UnwindData |  |
| 1251 | `GdiIsMetaPrintDC` | `0x59200` | 80 | UnwindData |  |
| 1888 | `ScriptApplyLogicalWidth` | `0x59450` | 859 | UnwindData |  |
| 1005 | *Ordinal Only* | `0x59830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1367 | `GetPixel` | `0x59850` | 305 | UnwindData |  |
| 1398 | `GetTextFaceW` | `0x599F0` | 57 | UnwindData |  |
| 1324 | `GetEnhMetaFileBits` | `0x59A30` | 168 | UnwindData |  |
| 1897 | `ScriptGetFontProperties` | `0x59CA0` | 255 | UnwindData |  |
| 1965 | `SetPixel` | `0x59DB0` | 621 | UnwindData |  |
| 1861 | `PolyPolygon` | `0x5A160` | 265 | UnwindData |  |
| 1859 | `PolyDrawImpl` | `0x5A3E0` | 235 | UnwindData |  |
| 1342 | `GetGlyphOutlineW` | `0x5A730` | 93 | UnwindData |  |
| 1912 | `ScriptShapeOpenType` | `0x5A7A0` | 1,114 | UnwindData |  |
| 1868 | `PtInRegion` | `0x5AC00` | 264 | UnwindData |  |
| 1132 | `CreateSolidBrush` | `0x5AD10` | 58 | UnwindData |  |
| 1239 | `GdiFlush` | `0x5AD50` | 27 | UnwindData |  |
| 1089 | `CreateBitmapIndirect` | `0x5AD80` | 386 | UnwindData |  |
| 1088 | `CreateBitmap` | `0x5AF10` | 123 | UnwindData |  |
| 1252 | `GdiIsPlayMetafileDC` | `0x5AFA0` | 170 | UnwindData |  |
| 1249 | `GdiGradientFill` | `0x5B140` | 675 | UnwindData |  |
| 1031 | `GdiHandleBeingTracked` | `0x5B3F0` | 65 | UnwindData |  |
| 1390 | `GetTextExtentExPointWPri` | `0x5C230` | 60 | UnwindData |  |
| 1893 | `ScriptGetCMap` | `0x5C2F0` | 292 | UnwindData |  |
| 1378 | `GetStretchBltMode` | `0x5F1B0` | 164 | UnwindData |  |
| 1371 | `GetROP2` | `0x5F6C0` | 165 | UnwindData |  |
| 1289 | `GetBrushOrgEx` | `0x5F770` | 213 | UnwindData |  |
| 1309 | `GetColorSpace` | `0x5F850` | 181 | UnwindData |  |
| 1369 | `GetPolyFillMode` | `0x5F910` | 171 | UnwindData |  |
| 1087 | `CopyMetaFileW` | `0x600E0` | 374 | UnwindData |  |
| 1085 | `CopyEnhMetaFileW` | `0x603C0` | 389 | UnwindData |  |
| 1138 | `DeleteMetaFile` | `0x60CB0` | 92 | UnwindData |  |
| 1355 | `GetMetaFileW` | `0x60D20` | 92 | UnwindData |  |
| 1984 | `SetWinMetaFileBits` | `0x61140` | 1,184 | UnwindData |  |
| 1961 | `SetMetaFileBitsEx` | `0x61630` | 133 | UnwindData |  |
| 1952 | `SetEnhMetaFileBits` | `0x617F0` | 137 | UnwindData |  |
| 1080 | `CloseMetaFile` | `0x61A10` | 618 | UnwindData |  |
| 1137 | `DeleteEnhMetaFile` | `0x61C80` | 77 | UnwindData |  |
| 1259 | `GdiPlayPageEMF` | `0x620E0` | 1,160 | UnwindData |  |
| 1246 | `GdiGetPageHandle` | `0x62EB0` | 216 | UnwindData |  |
| 1038 | `GetFontDataImpl` | `0x63440` | 190 | UnwindData |  |
| 1368 | `GetPixelFormat` | `0x636B0` | 131 | UnwindData |  |
| 1904 | `ScriptItemizeOpenType` | `0x638B0` | 192 | UnwindData |  |
| 1303 | `GetCharacterPlacementA` | `0x639A0` | 841 | UnwindData |  |
| 1304 | `GetCharacterPlacementW` | `0x63CF0` | 181 | UnwindData |  |
| 1421 | `LpkGetCharacterPlacement` | `0x63DB0` | 1,883 | UnwindData |  |
| 1917 | `ScriptStringGetOrder` | `0x64520` | 555 | UnwindData |  |
| 1930 | `SelectClipRgnImpl` | `0x64810` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1997 | `SwapBuffers` | `0x64A70` | 123 | UnwindData |  |
| 1969 | `SetPolyFillModeImpl` | `0x64B20` | 432 | UnwindData |  |
| 1184 | `ExcludeClipRect` | `0x65420` | 223 | UnwindData |  |
| 1298 | `GetCharWidthA` | `0x656C0` | 26 | UnwindData |  |
| 1296 | `GetCharWidth32A` | `0x656E0` | 26 | UnwindData |  |
| 1302 | `GetCharWidthW` | `0x65B20` | 26 | UnwindData |  |
| 1297 | `GetCharWidth32W` | `0x65B40` | 26 | UnwindData |  |
| 1946 | `SetDCBrushColor` | `0x66170` | 557 | UnwindData |  |
| 1977 | `SetTextCharacterExtra` | `0x66530` | 347 | UnwindData |  |
| 1901 | `ScriptGetProperties` | `0x68C80` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1294 | `GetCharABCWidthsI` | `0x68E20` | 40 | UnwindData |  |
| 1862 | `PolyPolyline` | `0x68E50` | 250 | UnwindData |  |
| 1895 | `ScriptGetFontFeatureTags` | `0x69310` | 584 | UnwindData |  |
| 1301 | `GetCharWidthI` | `0x69860` | 91 | UnwindData |  |
| 1397 | `GetTextFaceAliasW` | `0x698D0` | 58 | UnwindData |  |
| 1139 | `DescribePixelFormat` | `0x69910` | 159 | UnwindData |  |
| 1204 | `GdiComment` | `0x69D70` | 139 | UnwindData |  |
| 1316 | `GetDIBColorTable` | `0x6A0D0` | 44 | UnwindData |  |
| 1069 | `BeginPathImpl` | `0x6A110` | 118 | UnwindData |  |
| 1147 | `EndPathImpl` | `0x6A6A0` | 118 | UnwindData |  |
| 1314 | `GetDCOrgEx` | `0x6A820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `GetWorldTransform` | `0x6A840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1347 | `GetKerningPairsA` | `0x6A860` | 730 | UnwindData |  |
| 1000 | *Ordinal Only* | `0x6ACD0` | 55 | UnwindData |  |
| 1871 | `RealizePalette` | `0x6B9B0` | 156 | UnwindData |  |
| 1205 | `GdiConvertAndCheckDC` | `0x6BA60` | 139 | UnwindData |  |
| 1003 | *Ordinal Only* | `0x6BB40` | 43 | UnwindData |  |
| 1372 | `GetRandomRgn` | `0x6BEB0` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1896 | `ScriptGetFontLanguageTags` | `0x6C300` | 475 | UnwindData |  |
| 2003 | `UnrealizeObject` | `0x6C900` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1898 | `ScriptGetFontScriptTags` | `0x6C930` | 244 | UnwindData |  |
| 1293 | `GetCharABCWidthsFloatW` | `0x6CDA0` | 23 | UnwindData |  |
| 1295 | `GetCharABCWidthsW` | `0x6CDC0` | 26 | UnwindData |  |
| 1847 | `PaintRgn` | `0x6CE40` | 261 | UnwindData |  |
| 1414 | `IsValidEnhMetaRecord` | `0x6DAA0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1417 | `LineDDA` | `0x6DC20` | 306 | UnwindData |  |
| 1274 | `GdiTransparentBlt` | `0x6DD60` | 517 | UnwindData |  |
| 1947 | `SetDCPenColor` | `0x6E030` | 571 | UnwindData |  |
| 1009 | *Ordinal Only* | `0x6E280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1963 | `SetMiterLimitImpl` | `0x6E2A0` | 166 | UnwindData |  |
| 1384 | `GetTextCharset` | `0x6E710` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1401 | `GetTransform` | `0x6E950` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1358 | `GetNearestColor` | `0x6ED00` | 2,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | *Ordinal Only* | `0x6F520` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1396 | `GetTextFaceA` | `0x6F580` | 479 | UnwindData |  |
| 1333 | `GetFontFileData` | `0x6F860` | 69 | UnwindData |  |
| 1133 | `DPtoLP` | `0x6F8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `GetFontAssocStatus` | `0x6F8C0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `EngComputeGlyphSet` | `0x6FA60` | 124 | UnwindData |  |
| 1935 | `SetBitmapAttributes` | `0x6FB60` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1936 | `SetBitmapBits` | `0x6FC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1292 | `GetCharABCWidthsFloatI` | `0x6FC90` | 40 | UnwindData |  |
| 1980 | `SetTextJustification` | `0x6FF80` | 310 | UnwindData |  |
| 1075 | `ClearBitmapAttributes` | `0x700F0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1327 | `GetEnhMetaFileHeader` | `0x70450` | 233 | UnwindData |  |
| 1143 | `Ellipse` | `0x70590` | 292 | UnwindData |  |
| 1883 | `RoundRect` | `0x70730` | 335 | UnwindData |  |
| 1941 | `SetBoundsRect` | `0x70920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1247 | `GdiGetSpoolFileHandle` | `0x70940` | 531 | UnwindData |  |
| 1275 | `GdiValidateHandle` | `0x71320` | 134 | UnwindData |  |
| 1127 | `CreateRoundRectRgn` | `0x71D00` | 44 | UnwindData |  |
| 1928 | `SelectClipPathImpl` | `0x71DB0` | 125 | UnwindData |  |
| 1348 | `GetKerningPairsW` | `0x71FC0` | 54 | UnwindData |  |
| 1017 | `EscapeImpl` | `0x72000` | 1,779 | UnwindData |  |
| 1083 | `CombineTransform` | `0x727F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1158 | `EngFindResource` | `0x72850` | 167 | UnwindData |  |
| 1380 | `GetSystemPaletteEntries` | `0x72A40` | 313 | UnwindData |  |
| 1872 | `RectVisible` | `0x72B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1365 | `GetPaletteEntries` | `0x72BA0` | 35 | UnwindData |  |
| 1171 | `EnumEnhMetaFile` | `0x72E70` | 59 | UnwindData |  |
| 1867 | `PolylineToImpl` | `0x73190` | 231 | UnwindData |  |
| 1121 | `CreatePalette` | `0x73280` | 62 | UnwindData |  |
| 1217 | `GdiDisableUMPDSandboxing` | `0x732D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1219 | `GdiDllInitializeWrapper` | `0x732D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `GdiEntry12` | `0x732D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `GdiSetServerAttr` | `0x732D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `LpkPresent` | `0x732D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1905 | `ScriptJustify` | `0x732E0` | 2,029 | UnwindData |  |
| 1354 | `GetMetaFileBitsEx` | `0x73DC0` | 139 | UnwindData |  |
| 1844 | `OffsetClipRgn` | `0x73E60` | 177 | UnwindData |  |
| 2016 | `vFreeUFIHashTable` | `0x73F30` | 166 | UnwindData |  |
| 1122 | `CreatePatternBrush` | `0x73FE0` | 33 | UnwindData |  |
| 1849 | `PathToRegion` | `0x74160` | 170 | UnwindData |  |
| 1066 | `Arc` | `0x74430` | 423 | UnwindData |  |
| 1429 | `MirrorRgn` | `0x746E0` | 92 | UnwindData |  |
| 1315 | `GetDCPenColor` | `0x74790` | 190 | UnwindData |  |
| 1192 | `FillRgn` | `0x74960` | 275 | UnwindData |  |
| 1287 | `GetBoundsRect` | `0x74A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1312 | `GetDCBrushColor` | `0x74AA0` | 190 | UnwindData |  |
| 1899 | `ScriptGetGlyphABCWidth` | `0x74CA0` | 124 | UnwindData |  |
| 1922 | `ScriptString_pSize` | `0x74F30` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1966 | `SetPixelFormat` | `0x75050` | 267 | UnwindData |  |
| 1958 | `SetLayoutWidth` | `0x75170` | 251 | UnwindData |  |
| 1119 | `CreateMetaFileA` | `0x75280` | 142 | UnwindData |  |
| 1120 | `CreateMetaFileW` | `0x75320` | 574 | UnwindData |  |
| 1934 | `SetArcDirection` | `0x7BAA0` | 48 | UnwindData |  |
| 1995 | `StrokeAndFillPath` | `0x7BB10` | 199 | UnwindData |  |
| 1388 | `GetTextExtentExPointI` | `0x7BDC0` | 63 | UnwindData |  |
| 1124 | `CreatePenIndirect` | `0x7C7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1366 | `GetPath` | `0x7C7C0` | 60 | UnwindData |  |
| 1283 | `GetBitmapBits` | `0x7C830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1060 | `AddFontResourceExW` | `0x7C850` | 49 | UnwindData |  |
| 1057 | `AddFontMemResourceEx` | `0x7CC10` | 68 | UnwindData |  |
| 1266 | `GdiSetBatchLimit` | `0x7CC60` | 56 | UnwindData |  |
| 1180 | `EnumMetaFile` | `0x7CD10` | 58 | UnwindData |  |
| 1194 | `FlattenPath` | `0x7CD50` | 118 | UnwindData |  |
| 1340 | `GetGlyphIndicesW` | `0x7CE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `GdiConvertToDevmodeW` | `0x7CE30` | 339 | UnwindData |  |
| 1037 | `GetClipBoxImpl` | `0x7D610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1370 | `GetProcessSessionFonts` | `0x7D630` | 37 | UnwindData |  |
| 1413 | `InvertRgn` | `0x7D710` | 249 | UnwindData |  |
| 1851 | `PlayEnhMetaFile` | `0x7DBB0` | 136 | UnwindData |  |
| 1067 | `ArcTo` | `0x7DC40` | 379 | UnwindData |  |
| 1059 | `AddFontResourceExA` | `0x7DDD0` | 345 | UnwindData |  |
| 1341 | `GetGlyphOutlineA` | `0x7DF30` | 51 | UnwindData |  |
| 1170 | `EngWideCharToMultiByte` | `0x7E0D0` | 61 | UnwindData |  |
| 1065 | `AnyLinkedFonts` | `0x7E270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `CancelDC` | `0x7E290` | 285 | UnwindData |  |
| 1116 | `CreateHatchBrush` | `0x7E3C0` | 31 | UnwindData |  |
| 1063 | `AngleArc` | `0x7E3F0` | 297 | UnwindData |  |
| 1319 | `GetDeviceGammaRamp` | `0x7E520` | 53 | UnwindData |  |
| 1155 | `EngDeletePalette` | `0x7E560` | 34 | UnwindData |  |
| 1284 | `GetBitmapDimensionEx` | `0x7E590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1160 | `EngGetCurrentCodePage` | `0x7E5B0` | 58 | UnwindData |  |
| 1153 | `EngCreatePalette` | `0x7E7E0` | 44 | UnwindData |  |
| 1073 | `ChoosePixelFormat` | `0x7E820` | 139 | UnwindData |  |
| 1053 | `StartPageImpl` | `0x7EB50` | 469 | UnwindData |  |
| 1196 | `FontIsLinked` | `0x7ED50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1874 | `RemoveFontMemResourceEx` | `0x7ED70` | 50 | UnwindData |  |
| 1951 | `SetDeviceGammaRamp` | `0x7EDB0` | 116 | UnwindData |  |
| 1280 | `GetArcDirection` | `0x7EF10` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1125 | `CreatePolyPolygonRgn` | `0x7F2F0` | 51 | UnwindData |  |
| 1027 | `GdiDeleteLocalDC` | `0x7F330` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `GdiEntry16` | `0x7F330` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1034 | `GdiReleaseLocalDC` | `0x7F330` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `GdiSetAttrs` | `0x7F330` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1270 | `GdiSupportsFontChangeEvent` | `0x7F330` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `GetEnhMetaFileDescriptionW` | `0x7F360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1948 | `SetDIBColorTable` | `0x7F380` | 47 | UnwindData |  |
| 1255 | `GdiLoadType1Fonts` | `0x7F470` | 290 | UnwindData |  |
| 1240 | `GdiGetBatchLimit` | `0x7F5A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1983 | `SetVirtualResolution` | `0x7F600` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1864 | `PolyTextOutW` | `0x7F660` | 359 | UnwindData |  |
| 1195 | `FloodFill` | `0x7F7D0` | 20 | UnwindData |  |
| 1186 | `ExtFloodFill` | `0x7F7F0` | 539 | UnwindData |  |
| 1357 | `GetMiterLimit` | `0x7FA20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `CreateDCExW` | `0x7FA60` | 53 | UnwindData |  |
| 1359 | `GetNearestPaletteIndex` | `0x7FAA0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2010 | `WidenPath` | `0x7FBF0` | 116 | UnwindData |  |
| 1150 | `EngCreateBitmap` | `0x7FD60` | 38 | UnwindData |  |
| 1381 | `GetSystemPaletteUse` | `0x7FDE0` | 5,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1363 | `GetOutlineTextMetricsA` | `0x814D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1159 | `EngFreeModule` | `0x814E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `GdiConvertEnhMetaFile` | `0x81500` | 120 | UnwindData |  |
| 1394 | `GetTextExtentPointI` | `0x81580` | 30 | UnwindData |  |
| 1876 | `RemoveFontResourceExA` | `0x81660` | 376 | UnwindData |  |
| 1197 | `FrameRgn` | `0x817E0` | 292 | UnwindData |  |
| 1141 | `DwmCreatedBitmapRemotingOutput` | `0x81D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `GdiCurrentProcessSplWow64` | `0x81D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1163 | `EngLoadModule` | `0x81D60` | 3,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1919 | `ScriptStringValidate` | `0x82A00` | 241 | UnwindData |  |
| 1263 | `GdiProcessSetup` | `0x83660` | 1,263 | UnwindData |  |
| 1218 | `GdiDllInitialize` | `0x83D50` | 6,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `CreateEllipticRgn` | `0x85590` | 28 | UnwindData |  |
| 1879 | `RemoveFontResourceWImpl` | `0x85A60` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `GdiCreateLocalEnhMetaFile` | `0x85BC0` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1960 | `SetMapperFlags` | `0x85F00` | 281 | UnwindData |  |
| 1351 | `GetLogColorSpaceW` | `0x86150` | 187 | UnwindData |  |
| 1436 | `NamedEscape` | `0x86220` | 317 | UnwindData |  |
| 1320 | `GetETM` | `0x86370` | 80 | UnwindData |  |
| 1308 | `GetColorAdjustment` | `0x86480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1424 | `LpkPSMTextOut` | `0x864A0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2000 | `TraceLoggingGdiBatchInProcessing` | `0x866E0` | 132 | UnwindData |  |
| 1136 | `DeleteEMFSpoolData` | `0x86B20` | 71 | UnwindData |  |
| 1092 | `CreateColorSpaceW` | `0x86BC0` | 4,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1068 | `BeginPath` | `0x87E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `CloseFigure` | `0x87E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `CreateDCA` | `0x87EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1126 | `CreateRectRgn` | `0x87EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `EndDoc` | `0x87EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `EndPage` | `0x87ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `EndPath` | `0x87EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1188 | `ExtTextOutA` | `0x87EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `ExtTextOutW` | `0x87F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `FillPath` | `0x87F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1305 | `GetClipBox` | `0x87F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1318 | `GetDeviceCaps` | `0x87F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `GetFontData` | `0x87F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1374 | `GetRegionData` | `0x87F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1376 | `GetRgnBox` | `0x87F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1399 | `GetTextMetricsA` | `0x87F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1411 | `IntersectClipRect` | `0x87F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1418 | `LineTo` | `0x87F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1434 | `MoveToEx` | `0x87FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1857 | `PolyBezierTo` | `0x87FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1873 | `Rectangle` | `0x87FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1882 | `RestoreDC` | `0x87FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1884 | `SaveDC` | `0x87FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1927 | `SelectClipPath` | `0x87FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1929 | `SelectClipRgn` | `0x88000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1931 | `SelectObject` | `0x88010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1939 | `SetBkMode` | `0x88020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1968 | `SetPolyFillMode` | `0x88030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1972 | `SetStretchBltMode` | `0x88040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1975 | `SetTextAlign` | `0x88050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1978 | `SetTextColor` | `0x88060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1987 | `SetWorldTransform` | `0x88070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1990 | `StartDocW` | `0x88080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1991 | `StartPage` | `0x88090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1993 | `StretchDIBits` | `0x880A0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1115 | `CreateHalftonePalette` | `0x88430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1483 | `NtGdiCreateHalftonePalette` | `0x88430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1201 | `GdiAddInitialFonts` | `0x88440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1276 | `GdiWaitForTextReady` | `0x88450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `GetFontUnicodeRanges` | `0x88460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1689 | `NtGdiGetFontUnicodeRanges` | `0x88460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1385 | `GetTextCharsetInfo` | `0x88470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1721 | `NtGdiGetTextCharsetInfo` | `0x88470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1437 | `NtGdiAbortDoc` | `0x88480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1438 | `NtGdiAbortPath` | `0x88490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1439 | `NtGdiAddEmbFontToDC` | `0x884A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1440 | `NtGdiAddFontMemResourceEx` | `0x884B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1441 | `NtGdiAddFontResourceW` | `0x884C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1442 | `NtGdiAddRemoteFontToDC` | `0x884D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1443 | `NtGdiAddRemoteMMInstanceToDC` | `0x884E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `NtGdiAlphaBlend` | `0x884F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1445 | `NtGdiAngleArc` | `0x88500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1446 | `NtGdiAnyLinkedFonts` | `0x88510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1447 | `NtGdiArcInternal` | `0x88520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `NtGdiBRUSHOBJ_DeleteRbrush` | `0x88530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1449 | `NtGdiBRUSHOBJ_hGetColorTransform` | `0x88540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1450 | `NtGdiBRUSHOBJ_pvAllocRbrush` | `0x88550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1451 | `NtGdiBRUSHOBJ_pvGetRbrush` | `0x88560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1452 | `NtGdiBRUSHOBJ_ulGetBrushColor` | `0x88570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1453 | `NtGdiBeginGdiRendering` | `0x88580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1454 | `NtGdiBeginPath` | `0x88590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1455 | `NtGdiBitBlt` | `0x885A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1456 | `NtGdiCLIPOBJ_bEnum` | `0x885B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1457 | `NtGdiCLIPOBJ_cEnumStart` | `0x885C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1458 | `NtGdiCLIPOBJ_ppoGetPath` | `0x885D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1459 | `NtGdiCancelDC` | `0x885E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1460 | `NtGdiChangeGhostFont` | `0x885F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1461 | `NtGdiCheckBitmapBits` | `0x88600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1462 | `NtGdiClearBitmapAttributes` | `0x88610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1463 | `NtGdiClearBrushAttributes` | `0x88620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1464 | `NtGdiCloseFigure` | `0x88630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1465 | `NtGdiColorCorrectPalette` | `0x88640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1466 | `NtGdiCombineRgn` | `0x88650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1467 | `NtGdiCombineTransform` | `0x88660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1468 | `NtGdiComputeXformCoefficients` | `0x88670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1469 | `NtGdiConfigureOPMProtectedOutput` | `0x88680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1470 | `NtGdiConvertMetafileRect` | `0x88690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1471 | `NtGdiCreateBitmap` | `0x886A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1472 | `NtGdiCreateBitmapFromDxSurface` | `0x886B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1473 | `NtGdiCreateBitmapFromDxSurface2` | `0x886C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1474 | `NtGdiCreateClientObj` | `0x886D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1475 | `NtGdiCreateColorSpace` | `0x886E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1476 | `NtGdiCreateColorTransform` | `0x886F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1477 | `NtGdiCreateCompatibleBitmap` | `0x88700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1478 | `NtGdiCreateCompatibleDC` | `0x88710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `NtGdiCreateDIBBrush` | `0x88720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1480 | `NtGdiCreateDIBSection` | `0x88730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1481 | `NtGdiCreateDIBitmapInternal` | `0x88740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1482 | `NtGdiCreateEllipticRgn` | `0x88750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1484 | `NtGdiCreateHatchBrushInternal` | `0x88760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1485 | `NtGdiCreateMetafileDC` | `0x88770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1486 | `NtGdiCreateOPMProtectedOutput` | `0x88780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1487 | `NtGdiCreateOPMProtectedOutputs` | `0x88790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1488 | `NtGdiCreatePaletteInternal` | `0x887A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1489 | `NtGdiCreatePatternBrushInternal` | `0x887B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1490 | `NtGdiCreatePen` | `0x887C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1491 | `NtGdiCreateRectRgn` | `0x887D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1492 | `NtGdiCreateRoundRectRgn` | `0x887E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1493 | `NtGdiCreateServerMetaFile` | `0x887F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1494 | `NtGdiCreateSessionMappedDIBSection` | `0x88800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1495 | `NtGdiCreateSolidBrush` | `0x88810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1501 | `NtGdiDDCCIGetCapabilitiesString` | `0x88820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `NtGdiDDCCIGetCapabilitiesStringLength` | `0x88830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1503 | `NtGdiDDCCIGetTimingReport` | `0x88840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1504 | `NtGdiDDCCIGetVCPFeature` | `0x88850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `NtGdiDDCCISaveCurrentSettings` | `0x88860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1506 | `NtGdiDDCCISetVCPFeature` | `0x88870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1517 | `NtGdiDdCreateFullscreenSprite` | `0x88880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1525 | `NtGdiDdDestroyFullscreenSprite` | `0x88890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1545 | `NtGdiDdNotifyFullscreenSpriteUpdate` | `0x888A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1548 | `NtGdiDdQueryVisRgnUniqueness` | `0x888B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1562 | `NtGdiDeleteClientObj` | `0x888C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1563 | `NtGdiDeleteColorSpace` | `0x888D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1564 | `NtGdiDeleteColorTransform` | `0x888E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1565 | `NtGdiDeleteObjectApp` | `0x888F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1566 | `NtGdiDescribePixelFormat` | `0x88900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1567 | `NtGdiDestroyOPMProtectedOutput` | `0x88910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1568 | `NtGdiDestroyPhysicalMonitor` | `0x88920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1569 | `NtGdiDoBanding` | `0x88930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `NtGdiDoPalette` | `0x88940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1571 | `NtGdiDrawEscape` | `0x88950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1572 | `NtGdiDrawStream` | `0x88960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1590 | `NtGdiDwmCreatedBitmapRemotingOutput` | `0x88970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1592 | `NtGdiEllipse` | `0x88980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `NtGdiEnableEudc` | `0x88990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1594 | `NtGdiEndDoc` | `0x889A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `NtGdiEndGdiRendering` | `0x889B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1596 | `NtGdiEndPage` | `0x889C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1597 | `NtGdiEndPath` | `0x889D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1598 | `NtGdiEngAlphaBlend` | `0x889E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1599 | `NtGdiEngAssociateSurface` | `0x889F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1600 | `NtGdiEngBitBlt` | `0x88A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1601 | `NtGdiEngCheckAbort` | `0x88A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1602 | `NtGdiEngComputeGlyphSet` | `0x88A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1603 | `NtGdiEngCopyBits` | `0x88A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1604 | `NtGdiEngCreateClip` | `0x88A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1605 | `NtGdiEngDeleteClip` | `0x88A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1606 | `NtGdiEngDeletePath` | `0x88A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1607 | `NtGdiEngEraseSurface` | `0x88A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1608 | `NtGdiEngFillPath` | `0x88A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1609 | `NtGdiEngGradientFill` | `0x88A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1610 | `NtGdiEngLineTo` | `0x88AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1611 | `NtGdiEngLockSurface` | `0x88AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1612 | `NtGdiEngMarkBandingSurface` | `0x88AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1613 | `NtGdiEngPaint` | `0x88AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1614 | `NtGdiEngPlgBlt` | `0x88AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1615 | `NtGdiEngStretchBlt` | `0x88AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1616 | `NtGdiEngStretchBltROP` | `0x88B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `NtGdiEngStrokeAndFillPath` | `0x88B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1618 | `NtGdiEngStrokePath` | `0x88B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1619 | `NtGdiEngTextOut` | `0x88B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1620 | `NtGdiEngTransparentBlt` | `0x88B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `NtGdiEngUnlockSurface` | `0x88B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1622 | `NtGdiEnsureDpiDepDefaultGuiFontForPlateau` | `0x88B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1623 | `NtGdiEnumFonts` | `0x88B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1624 | `NtGdiEnumObjects` | `0x88B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1625 | `NtGdiEqualRgn` | `0x88B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1626 | `NtGdiEudcLoadUnloadLink` | `0x88BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1627 | `NtGdiExcludeClipRect` | `0x88BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1628 | `NtGdiExtCreatePen` | `0x88BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1629 | `NtGdiExtCreateRegion` | `0x88BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `NtGdiExtEscape` | `0x88BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1631 | `NtGdiExtFloodFill` | `0x88BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1632 | `NtGdiExtGetObjectW` | `0x88C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1633 | `NtGdiExtSelectClipRgn` | `0x88C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1634 | `NtGdiExtTextOutW` | `0x88C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1635 | `NtGdiFONTOBJ_cGetAllGlyphHandles` | `0x88C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1636 | `NtGdiFONTOBJ_cGetGlyphs` | `0x88C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1637 | `NtGdiFONTOBJ_pQueryGlyphAttrs` | `0x88C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1638 | `NtGdiFONTOBJ_pfdg` | `0x88C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1639 | `NtGdiFONTOBJ_pifi` | `0x88C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1640 | `NtGdiFONTOBJ_pvTrueTypeFontFile` | `0x88C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1641 | `NtGdiFONTOBJ_pxoGetXform` | `0x88C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `NtGdiFONTOBJ_vGetInfo` | `0x88CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1643 | `NtGdiFillPath` | `0x88CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `NtGdiFillRgn` | `0x88CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1645 | `NtGdiFlattenPath` | `0x88CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1646 | `NtGdiFlush` | `0x88CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1647 | `NtGdiFontIsLinked` | `0x88CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1648 | `NtGdiForceUFIMapping` | `0x88D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1649 | `NtGdiFrameRgn` | `0x88D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1650 | `NtGdiFullscreenControl` | `0x88D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1651 | `NtGdiGetAndSetDCDword` | `0x88D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1652 | `NtGdiGetAppClipBox` | `0x88D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1653 | `NtGdiGetBitmapBits` | `0x88D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1654 | `NtGdiGetBitmapDimension` | `0x88D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1655 | `NtGdiGetBitmapDpiScaleValue` | `0x88D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1656 | `NtGdiGetBoundsRect` | `0x88D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1657 | `NtGdiGetCOPPCompatibleOPMInformation` | `0x88D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1658 | `NtGdiGetCertificate` | `0x88DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1659 | `NtGdiGetCertificateByHandle` | `0x88DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1660 | `NtGdiGetCertificateSize` | `0x88DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1661 | `NtGdiGetCertificateSizeByHandle` | `0x88DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1662 | `NtGdiGetCharABCWidthsW` | `0x88DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1663 | `NtGdiGetCharSet` | `0x88DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1664 | `NtGdiGetCharWidthInfo` | `0x88E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1665 | `NtGdiGetCharWidthW` | `0x88E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1666 | `NtGdiGetCharacterPlacementW` | `0x88E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1667 | `NtGdiGetColorAdjustment` | `0x88E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `NtGdiGetColorSpaceforBitmap` | `0x88E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1669 | `NtGdiGetCurrentDpiInfo` | `0x88E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1670 | `NtGdiGetDCDpiScaleValue` | `0x88E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1671 | `NtGdiGetDCDword` | `0x88E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1672 | `NtGdiGetDCObject` | `0x88E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1673 | `NtGdiGetDCPoint` | `0x88E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1674 | `NtGdiGetDCforBitmap` | `0x88EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1675 | `NtGdiGetDIBitsInternal` | `0x88EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1676 | `NtGdiGetDeviceCaps` | `0x88EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1677 | `NtGdiGetDeviceCapsAll` | `0x88ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1678 | `NtGdiGetDeviceWidth` | `0x88EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1679 | `NtGdiGetDhpdev` | `0x88EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1680 | `NtGdiGetETM` | `0x88F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1681 | `NtGdiGetEmbUFI` | `0x88F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1682 | `NtGdiGetEmbedFonts` | `0x88F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1683 | `NtGdiGetEntry` | `0x88F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1684 | `NtGdiGetEudcTimeStampEx` | `0x88F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1685 | `NtGdiGetFontData` | `0x88F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `NtGdiGetFontFileData` | `0x88F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1687 | `NtGdiGetFontFileInfo` | `0x88F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1688 | `NtGdiGetFontResourceInfoInternalW` | `0x88F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1690 | `NtGdiGetGlyphIndicesW` | `0x88F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1691 | `NtGdiGetGlyphIndicesWInternal` | `0x88FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1692 | `NtGdiGetGlyphOutline` | `0x88FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1693 | `NtGdiGetKerningPairs` | `0x88FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1694 | `NtGdiGetLinkedUFIs` | `0x88FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1695 | `NtGdiGetMiterLimit` | `0x88FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1696 | `NtGdiGetMonitorID` | `0x88FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1697 | `NtGdiGetNearestColor` | `0x89000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1698 | `NtGdiGetNearestPaletteIndex` | `0x89010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1699 | `NtGdiGetNumberOfPhysicalMonitors` | `0x89020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1700 | `NtGdiGetOPMInformation` | `0x89030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1701 | `NtGdiGetOPMRandomNumber` | `0x89040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1702 | `NtGdiGetObjectBitmapHandle` | `0x89050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1703 | `NtGdiGetOutlineTextMetricsInternalW` | `0x89060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1704 | `NtGdiGetPath` | `0x89070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1705 | `NtGdiGetPerBandInfo` | `0x89080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1706 | `NtGdiGetPhysicalMonitorDescription` | `0x89090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1707 | `NtGdiGetPhysicalMonitorFromTarget` | `0x890A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1708 | `NtGdiGetPhysicalMonitors` | `0x890B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1709 | `NtGdiGetPixel` | `0x890C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1710 | `NtGdiGetRandomRgn` | `0x890D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1711 | `NtGdiGetRasterizerCaps` | `0x890E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1712 | `NtGdiGetRealizationInfo` | `0x890F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1713 | `NtGdiGetRegionData` | `0x89100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1714 | `NtGdiGetRgnBox` | `0x89110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1715 | `NtGdiGetServerMetaFileBits` | `0x89120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1716 | `NtGdiGetSpoolMessage` | `0x89130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1717 | `NtGdiGetStats` | `0x89140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1718 | `NtGdiGetStringBitmapW` | `0x89150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1719 | `NtGdiGetSuggestedOPMProtectedOutputArraySize` | `0x89160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1720 | `NtGdiGetSystemPaletteUse` | `0x89170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1722 | `NtGdiGetTextExtent` | `0x89180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1723 | `NtGdiGetTextExtentExW` | `0x89190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1724 | `NtGdiGetTextFaceW` | `0x891A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1725 | `NtGdiGetTextMetricsW` | `0x891B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1726 | `NtGdiGetTransform` | `0x891C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1727 | `NtGdiGetUFI` | `0x891D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1728 | `NtGdiGetUFIPathname` | `0x891E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1729 | `NtGdiGetWidthTable` | `0x891F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1730 | `NtGdiGradientFill` | `0x89200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1731 | `NtGdiHLSurfGetInformation` | `0x89210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1732 | `NtGdiHLSurfSetInformation` | `0x89220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1733 | `NtGdiHT_Get8BPPFormatPalette` | `0x89230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1734 | `NtGdiHT_Get8BPPMaskPalette` | `0x89240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1735 | `NtGdiHfontCreate` | `0x89250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1736 | `NtGdiIcmBrushInfo` | `0x89260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `NtGdiInit` | `0x89270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1738 | `NtGdiInit2` | `0x89280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `NtGdiInitSpool` | `0x89290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1740 | `NtGdiIntersectClipRect` | `0x892A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1741 | `NtGdiInvertRgn` | `0x892B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1742 | `NtGdiLineTo` | `0x892C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1743 | `NtGdiMakeFontDir` | `0x892D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1744 | `NtGdiMakeInfoDC` | `0x892E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1745 | `NtGdiMakeObjectUnXferable` | `0x892F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1746 | `NtGdiMakeObjectXferable` | `0x89300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1747 | `NtGdiMaskBlt` | `0x89310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1748 | `NtGdiMirrorWindowOrg` | `0x89320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1749 | `NtGdiModifyWorldTransform` | `0x89330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1750 | `NtGdiMonoBitmap` | `0x89340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1751 | `NtGdiMoveTo` | `0x89350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1752 | `NtGdiOffsetClipRgn` | `0x89360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1753 | `NtGdiOffsetRgn` | `0x89370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1754 | `NtGdiOpenDCW` | `0x89380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1755 | `NtGdiPATHOBJ_bEnum` | `0x89390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1756 | `NtGdiPATHOBJ_bEnumClipLines` | `0x893A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1757 | `NtGdiPATHOBJ_vEnumStart` | `0x893B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1758 | `NtGdiPATHOBJ_vEnumStartClipLines` | `0x893C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1759 | `NtGdiPATHOBJ_vGetBounds` | `0x893D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1760 | `NtGdiPatBlt` | `0x893E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1761 | `NtGdiPathToRegion` | `0x893F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1762 | `NtGdiPlgBlt` | `0x89400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1763 | `NtGdiPolyDraw` | `0x89410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1764 | `NtGdiPolyPatBlt` | `0x89420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1765 | `NtGdiPolyPolyDraw` | `0x89430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1766 | `NtGdiPolyTextOutW` | `0x89440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1767 | `NtGdiPtInRegion` | `0x89450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1768 | `NtGdiPtVisible` | `0x89460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1769 | `NtGdiQueryFontAssocInfo` | `0x89470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1770 | `NtGdiQueryFonts` | `0x89480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1771 | `NtGdiRectInRegion` | `0x89490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1772 | `NtGdiRectVisible` | `0x894A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1773 | `NtGdiRectangle` | `0x894B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1774 | `NtGdiRemoveFontMemResourceEx` | `0x894C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1775 | `NtGdiRemoveFontResourceW` | `0x894D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1776 | `NtGdiRemoveMergeFont` | `0x894E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1777 | `NtGdiResetDC` | `0x894F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1778 | `NtGdiResizePalette` | `0x89500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1779 | `NtGdiRestoreDC` | `0x89510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1780 | `NtGdiRoundRect` | `0x89520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1781 | `NtGdiSTROBJ_bEnum` | `0x89530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1782 | `NtGdiSTROBJ_bEnumPositionsOnly` | `0x89540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1783 | `NtGdiSTROBJ_bGetAdvanceWidths` | `0x89550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1784 | `NtGdiSTROBJ_dwGetCodePage` | `0x89560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1785 | `NtGdiSTROBJ_vEnumStart` | `0x89570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1786 | `NtGdiSaveDC` | `0x89580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1787 | `NtGdiScaleRgn` | `0x89590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1788 | `NtGdiScaleValues` | `0x895A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1789 | `NtGdiScaleViewportExtEx` | `0x895B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1790 | `NtGdiScaleWindowExtEx` | `0x895C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1791 | `NtGdiSelectBitmap` | `0x895D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1792 | `NtGdiSelectBrush` | `0x895E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1793 | `NtGdiSelectClipPath` | `0x895F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1794 | `NtGdiSelectFont` | `0x89600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1795 | `NtGdiSelectPen` | `0x89610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1796 | `NtGdiSetBitmapAttributes` | `0x89620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1797 | `NtGdiSetBitmapBits` | `0x89630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1798 | `NtGdiSetBitmapDimension` | `0x89640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1799 | `NtGdiSetBoundsRect` | `0x89650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1800 | `NtGdiSetBrushAttributes` | `0x89660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1801 | `NtGdiSetBrushOrg` | `0x89670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1802 | `NtGdiSetColorAdjustment` | `0x89680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1803 | `NtGdiSetColorSpace` | `0x89690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1804 | `NtGdiSetDIBitsToDeviceInternal` | `0x896A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1805 | `NtGdiSetFontEnumeration` | `0x896B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1806 | `NtGdiSetFontXform` | `0x896C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1807 | `NtGdiSetIcmMode` | `0x896D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1808 | `NtGdiSetLayout` | `0x896E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1809 | `NtGdiSetLinkedUFIs` | `0x896F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1810 | `NtGdiSetMagicColors` | `0x89700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1811 | `NtGdiSetMetaRgn` | `0x89710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1812 | `NtGdiSetMiterLimit` | `0x89720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1813 | `NtGdiSetOPMSigningKeyAndSequenceNumbers` | `0x89730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1814 | `NtGdiSetPUMPDOBJ` | `0x89740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1815 | `NtGdiSetPixel` | `0x89750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1816 | `NtGdiSetPixelFormat` | `0x89760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1817 | `NtGdiSetRectRgn` | `0x89770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1818 | `NtGdiSetSizeDevice` | `0x89780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1819 | `NtGdiSetSystemPaletteUse` | `0x89790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1820 | `NtGdiSetTextJustification` | `0x897A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1821 | `NtGdiSetUMPDSandboxState` | `0x897B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1822 | `NtGdiSetVirtualResolution` | `0x897C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1823 | `NtGdiStartDoc` | `0x897D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1824 | `NtGdiStartPage` | `0x897E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1825 | `NtGdiStretchBlt` | `0x897F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1826 | `NtGdiStretchDIBitsInternal` | `0x89800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1827 | `NtGdiStrokeAndFillPath` | `0x89810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1828 | `NtGdiStrokePath` | `0x89820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1829 | `NtGdiSwapBuffers` | `0x89830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1830 | `NtGdiTransformPoints` | `0x89840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1831 | `NtGdiTransparentBlt` | `0x89850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1832 | `NtGdiUMPDEngFreeUserMem` | `0x89860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1833 | `NtGdiUnloadPrinterDriver` | `0x89870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1834 | `NtGdiUnmapMemFont` | `0x89880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1835 | `NtGdiUnrealizeObject` | `0x89890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1836 | `NtGdiUpdateColors` | `0x898A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1837 | `NtGdiUpdateTransform` | `0x898B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1838 | `NtGdiWidenPath` | `0x898C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1839 | `NtGdiXFORMOBJ_bApplyXform` | `0x898D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1840 | `NtGdiXFORMOBJ_iGetXform` | `0x898E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1841 | `NtGdiXLATEOBJ_cGetPalette` | `0x898F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1842 | `NtGdiXLATEOBJ_hGetColorTransform` | `0x89900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1843 | `NtGdiXLATEOBJ_iXlate` | `0x89910` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | *Ordinal Only* | `0x89C00` | 43 | UnwindData |  |
| 1142 | `DwmGetDirtyRgnImpl` | `0x89C40` | 29 | UnwindData |  |
| 2005 | `UpdateICMRegKeyA` | `0x89C40` | 29 | UnwindData |  |
| 2006 | `UpdateICMRegKeyW` | `0x89C40` | 29 | UnwindData |  |
| 1006 | *Ordinal Only* | `0x89C70` | 43 | UnwindData |  |
| 1001 | *Ordinal Only* | `0x89CB0` | 41 | UnwindData |  |
| 1002 | *Ordinal Only* | `0x89CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1237 | `GdiEntry9` | `0x89D00` | 252 | UnwindData |  |
| 1557 | `NtGdiDdUnattachSurface` | `0x89E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1856 | `PolyBezier` | `0x89E20` | 229 | UnwindData |  |
| 1869 | `PtVisible` | `0x89F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `ClearBrushAttributes` | `0x89F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1282 | `GetBitmapAttributes` | `0x89F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1288 | `GetBrushAttributes` | `0x89F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1942 | `SetBrushAttributes` | `0x89F70` | 3,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1944 | `SetColorAdjustment` | `0x8ADA0` | 139 | UnwindData |  |
| 1974 | `SetSystemPaletteUse` | `0x8AE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `AddFontResourceA` | `0x8AE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `AddFontResourceTracking` | `0x8AE70` | 413 | UnwindData |  |
| 1062 | `AddFontResourceWImpl` | `0x8B020` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `CreateScalableFontResourceA` | `0x8B0B0` | 313 | UnwindData |  |
| 1129 | `CreateScalableFontResourceWImpl` | `0x8B790` | 429 | UnwindData |  |
| 1373 | `GetRasterizerCaps` | `0x8B950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1875 | `RemoveFontResourceA` | `0x8B970` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1878 | `RemoveFontResourceTracking` | `0x8BA70` | 230 | UnwindData |  |
| 1953 | `SetFontEnumeration` | `0x8BB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2002 | `UnloadNetworkFonts` | `0x8BB80` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1375 | `GetRelAbs` | `0x8BDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1971 | `SetRelAbs` | `0x8BDC0` | 39 | UnwindData |  |
| 1353 | `GetMetaFileA` | `0x8BE50` | 161 | UnwindData |  |
| 1086 | `CopyMetaFileA` | `0x8BF70` | 186 | UnwindData |  |
| 1064 | `AnimatePalette` | `0x8CBF0` | 143 | UnwindData |  |
| 1964 | `SetPaletteEntries` | `0x8CC90` | 135 | UnwindData |  |
| 1056 | `AbortPath` | `0x8CD20` | 116 | UnwindData |  |
| 1216 | `GdiDescribePixelFormat` | `0x8CDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1267 | `GdiSetPixelFormat` | `0x8CDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1271 | `GdiSwapBuffers` | `0x8CDE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1182 | `EudcLoadLinkW` | `0x8CE00` | 88 | UnwindData |  |
| 1183 | `EudcUnloadLinkW` | `0x8CE60` | 75 | UnwindData |  |
| 1321 | `GetEUDCTimeStamp` | `0x8CEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1322 | `GetEUDCTimeStampExW` | `0x8CEE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1379 | `GetStringBitmapA` | `0x8CF10` | 122 | UnwindData |  |
| 1165 | `EngMultiByteToWideChar` | `0x8E9D0` | 50 | UnwindData |  |
| 1021 | `GdiCleanCacheDC` | `0x90300` | 50 | UnwindData |  |
| 1023 | `GdiConvertBitmap` | `0x90340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `GdiConvertBrush` | `0x90340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `GdiConvertDC` | `0x90340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `GdiConvertFont` | `0x90340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `GdiConvertPalette` | `0x90340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `GdiConvertRegion` | `0x90340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1028 | `GdiGetLocalBrush` | `0x90340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1029 | `GdiGetLocalDC` | `0x90340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1030 | `GdiGetLocalFont` | `0x90340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `GdiIsMetaFileDC` | `0x90350` | 89 | UnwindData |  |
| 1033 | `GdiQueryTable` | `0x903B0` | 71 | UnwindData |  |
| 1047 | `SelectBrushLocal` | `0x92C70` | 8,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1048 | `SelectFontLocal` | `0x92C70` | 8,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `GetGlyphOutlineWow` | `0x94D10` | 54 | UnwindData |  |
| 1281 | `GetAspectRatioFilterEx` | `0x950B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `GetCharABCWidthsA` | `0x950D0` | 26 | UnwindData |  |
| 1291 | `GetCharABCWidthsFloatA` | `0x950F0` | 23 | UnwindData |  |
| 1299 | `GetCharWidthFloatA` | `0x95110` | 26 | UnwindData |  |
| 1300 | `GetCharWidthFloatW` | `0x95130` | 23 | UnwindData |  |
| 1339 | `GetGlyphIndicesA` | `0x95150` | 588 | UnwindData |  |
| 1044 | `ResetDCWImpl` | `0x953B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `gdiPlaySpoolStream` | `0x953C0` | 32 | UnwindData |  |
| 1098 | `CreateDIBPatternBrush` | `0x953F0` | 89 | UnwindData |  |
| 1103 | `CreateDiscardableBitmap` | `0x95450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `CreateEllipticRgnIndirect` | `0x95460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1110 | `CreateFontIndirectExA` | `0x95480` | 172 | UnwindData |  |
| 1130 | `CreateScaledCompatibleBitmap` | `0x95540` | 97 | UnwindData |  |
| 1181 | `EnumObjects` | `0x955B0` | 290 | UnwindData |  |
| 1253 | `GdiIsScreenDC` | `0x956E0` | 127 | UnwindData |  |
| 1356 | `GetMetaRgn` | `0x95770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1880 | `ResetDCA` | `0x95790` | 119 | UnwindData |  |
| 1881 | `ResizePalette` | `0x95810` | 178 | UnwindData |  |
| 1937 | `SetBitmapDimensionEx` | `0x958D0` | 1,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `CheckColorsInGamut` | `0x96000` | 603 | UnwindData |  |
| 1081 | `ColorCorrectPalette` | `0x96270` | 732 | UnwindData |  |
| 1082 | `ColorMatchToTarget` | `0x96560` | 399 | UnwindData |  |
| 1091 | `CreateColorSpaceA` | `0x968B0` | 346 | UnwindData |  |
| 1134 | `DeleteColorSpace` | `0x96A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `EnumICMProfilesA` | `0x96A30` | 214 | UnwindData |  |
| 1206 | `GdiConvertBitmapV5` | `0x96B10` | 1,818 | UnwindData |  |
| 1345 | `GetICMProfileA` | `0x97230` | 256 | UnwindData |  |
| 1350 | `GetLogColorSpaceA` | `0x97340` | 340 | UnwindData |  |
| 1955 | `SetICMProfileA` | `0x990A0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1956 | `SetICMProfileW` | `0x991F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1084 | `CopyEnhMetaFileA` | `0x99210` | 186 | UnwindData |  |
| 1323 | `GetEnhMetaFileA` | `0x992D0` | 159 | UnwindData |  |
| 1325 | `GetEnhMetaFileDescriptionA` | `0x99380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `GetEnhMetaFilePaletteEntries` | `0x99390` | 329 | UnwindData |  |
| 1329 | `GetEnhMetaFilePixelFormat` | `0x994E0` | 247 | UnwindData |  |
| 1404 | `GetWinMetaFileBits` | `0x995E0` | 531 | UnwindData |  |
| 1199 | `GdiAddGlsBounds` | `0x9A140` | 37 | UnwindData |  |
| 1200 | `GdiAddGlsRecord` | `0x9A170` | 292 | UnwindData |  |
| 1210 | `GdiConvertMetaFilePict` | `0x9C5F0` | 172 | UnwindData |  |
| 1214 | `GdiCreateLocalMetaFilePict` | `0x9C6B0` | 13,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `AbortDocImpl` | `0x9FB00` | 469 | UnwindData |  |
| 1012 | `DeviceCapabilitiesExA` | `0x9FCE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `EndDocImpl` | `0x9FCF0` | 910 | UnwindData |  |
| 1015 | `EndFormPage` | `0xA0090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `EndPageImpl` | `0xA00A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `GdiConsoleTextOut` | `0xA00B0` | 29 | UnwindData |  |
| 1051 | `StartDocWImpl` | `0xA03A0` | 2,419 | UnwindData |  |
| 1052 | `StartFormPage` | `0xA0D20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `Chord` | `0xA0DA0` | 426 | UnwindData |  |
| 1140 | `DrawEscape` | `0xA0F50` | 175 | UnwindData |  |
| 1277 | `GditGetCallerTLStorage` | `0xA1010` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1850 | `Pie` | `0xA1040` | 426 | UnwindData |  |
| 1855 | `PlgBlt` | `0xA11F0` | 467 | UnwindData |  |
| 1863 | `PolyTextOutA` | `0xA13D0` | 836 | UnwindData |  |
| 1933 | `SetAbortProc` | `0xA1720` | 150 | UnwindData |  |
| 1989 | `StartDocA` | `0xA17C0` | 447 | UnwindData |  |
| 2004 | `UpdateColors` | `0xA1990` | 2,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `GdiDeleteSpoolFileHandle` | `0xA2460` | 361 | UnwindData |  |
| 1221 | `GdiEndDocEMF` | `0xA25D0` | 102 | UnwindData |  |
| 1243 | `GdiGetDC` | `0xA2640` | 22 | UnwindData |  |
| 1244 | `GdiGetDevmodeForPage` | `0xA2660` | 129 | UnwindData |  |
| 1245 | `GdiGetPageCount` | `0xA26F0` | 118 | UnwindData |  |
| 1257 | `GdiPlayEMF` | `0xA2770` | 394 | UnwindData |  |
| 1260 | `GdiPlayPrivatePageEMF` | `0xA2900` | 55 | UnwindData |  |
| 1265 | `GdiResetDCEMF` | `0xA2940` | 117 | UnwindData |  |
| 1268 | `GdiStartDocEMF` | `0xA29C0` | 151 | UnwindData |  |
| 1269 | `GdiStartPageEMF` | `0xA2A60` | 23 | UnwindData |  |
| 1151 | `EngCreateDeviceBitmap` | `0xA3D10` | 28 | UnwindData |  |
| 1152 | `EngCreateDeviceSurface` | `0xA3D40` | 28 | UnwindData |  |
| 1157 | `EngDeleteSurface` | `0xA3D70` | 34 | UnwindData |  |
| 1203 | `GdiArtificialDecrementDriver` | `0xA3DA0` | 322 | UnwindData |  |
| 1161 | `EngGetDriverName` | `0xA3FD0` | 97 | UnwindData |  |
| 1162 | `EngGetPrinterDataFileName` | `0xA4040` | 97 | UnwindData |  |
| 1921 | `ScriptString_pLogAttr` | `0xA4130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1923 | `ScriptString_pcOutChars` | `0xA4150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1894 | `ScriptGetFontAlternateGlyphs` | `0xA4170` | 324 | UnwindData |  |
| 1909 | `ScriptPositionSingleGlyph` | `0xA42C0` | 504 | UnwindData |  |
| 1924 | `ScriptSubstituteSingleGlyph` | `0xA44C0` | 445 | UnwindData |  |
| 2015 | `ftsWordBreak` | `0xAF370` | 235 | UnwindData |  |
| 1148 | `EngAcquireSemaphore` | `0xAF890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `EngCreateSemaphore` | `0xAF8B0` | 70 | UnwindData |  |
| 1156 | `EngDeleteSemaphore` | `0xAF900` | 62 | UnwindData |  |
| 1164 | `EngMultiByteToUnicodeN` | `0xAF950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `EngQueryLocalTime` | `0xAF970` | 140 | UnwindData |  |
| 1168 | `EngReleaseSemaphore` | `0xAFA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1169 | `EngUnicodeToMultiByteN` | `0xAFA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2011 | `XLATEOBJ_piVector` | `0xAFA50` | 14,444 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
