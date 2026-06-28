# Binary Specification: usp10.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\usp10.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `23d73fc8824016734847593c0f7767e26d59f99984d8131d45913390d5b7d62b`
* **Total Exported Functions:** 44

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `LpkPresent` | `0x0` | - | Forwarded | Forwarded to: `GDI32.LpkPresent` |
| 2 | `ScriptApplyDigitSubstitution` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptApplyDigitSubstitution` |
| 3 | `ScriptApplyLogicalWidth` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptApplyLogicalWidth` |
| 4 | `ScriptBreak` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptBreak` |
| 5 | `ScriptCPtoX` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptCPtoX` |
| 6 | `ScriptCacheGetHeight` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptCacheGetHeight` |
| 7 | `ScriptFreeCache` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptFreeCache` |
| 8 | `ScriptGetCMap` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptGetCMap` |
| 9 | `ScriptGetFontAlternateGlyphs` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptGetFontAlternateGlyphs` |
| 10 | `ScriptGetFontFeatureTags` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptGetFontFeatureTags` |
| 11 | `ScriptGetFontLanguageTags` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptGetFontLanguageTags` |
| 12 | `ScriptGetFontProperties` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptGetFontProperties` |
| 13 | `ScriptGetFontScriptTags` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptGetFontScriptTags` |
| 14 | `ScriptGetGlyphABCWidth` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptGetGlyphABCWidth` |
| 15 | `ScriptGetLogicalWidths` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptGetLogicalWidths` |
| 16 | `ScriptGetProperties` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptGetProperties` |
| 17 | `ScriptIsComplex` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptIsComplex` |
| 18 | `ScriptItemize` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptItemize` |
| 19 | `ScriptItemizeOpenType` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptItemizeOpenType` |
| 20 | `ScriptJustify` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptJustify` |
| 21 | `ScriptLayout` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptLayout` |
| 22 | `ScriptPlace` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptPlace` |
| 23 | `ScriptPlaceOpenType` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptPlaceOpenType` |
| 24 | `ScriptPositionSingleGlyph` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptPositionSingleGlyph` |
| 25 | `ScriptRecordDigitSubstitution` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptRecordDigitSubstitution` |
| 26 | `ScriptShape` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptShape` |
| 27 | `ScriptShapeOpenType` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptShapeOpenType` |
| 28 | `ScriptStringAnalyse` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptStringAnalyse` |
| 29 | `ScriptStringCPtoX` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptStringCPtoX` |
| 30 | `ScriptStringFree` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptStringFree` |
| 31 | `ScriptStringGetLogicalWidths` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptStringGetLogicalWidths` |
| 32 | `ScriptStringGetOrder` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptStringGetOrder` |
| 33 | `ScriptStringOut` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptStringOut` |
| 34 | `ScriptStringValidate` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptStringValidate` |
| 35 | `ScriptStringXtoCP` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptStringXtoCP` |
| 36 | `ScriptString_pLogAttr` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptString_pLogAttr` |
| 37 | `ScriptString_pSize` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptString_pSize` |
| 38 | `ScriptString_pcOutChars` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptString_pcOutChars` |
| 39 | `ScriptSubstituteSingleGlyph` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptSubstituteSingleGlyph` |
| 40 | `ScriptTextOut` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptTextOut` |
| 41 | `ScriptXtoCP` | `0x0` | - | Forwarded | Forwarded to: `GDI32.ScriptXtoCP` |
| 42 | `UspAllocCache` | `0x0` | - | Forwarded | Forwarded to: `GDI32.UspAllocCache` |
| 43 | `UspAllocTemp` | `0x0` | - | Forwarded | Forwarded to: `GDI32.UspAllocTemp` |
| 44 | `UspFreeMem` | `0x0` | - | Forwarded | Forwarded to: `GDI32.UspFreeMem` |
