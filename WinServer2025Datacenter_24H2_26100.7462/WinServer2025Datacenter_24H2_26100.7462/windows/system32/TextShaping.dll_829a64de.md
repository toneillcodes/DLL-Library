# Binary Specification: TextShaping.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\TextShaping.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `829a64dee2b34fd2a25332c3b2e12c76acb55500161a12a520f4c60895b8cc92`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `GetOtlFeatureDefs` | `0xD7C0` | 936 | UnwindData |  |
| 2 | `FreeOtlResources` | `0x10E40` | 42 | UnwindData |  |
| 14 | `ShapingGetBreakingProperties` | `0x21D70` | 342 | UnwindData |  |
| 13 | `ShapingDrawGlyphs` | `0x21ED0` | 592 | UnwindData |  |
| 17 | `ShapingGetGlyphs` | `0x22130` | 180 | UnwindData |  |
| 16 | `ShapingGetGlyphPositions` | `0x22C70` | 186 | UnwindData |  |
| 1 | `BuildOtlCache` | `0x25D00` | 220 | UnwindData |  |
| 12 | `ShapingCreateFontCacheData` | `0x25DF0` | 2,012 | UnwindData |  |
| 15 | `ShapingGetCombiningOptions` | `0x26B60` | 147 | UnwindData |  |
| 10 | `ValidateLogClust` | `0x27420` | 7,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ShapingLoadScriptEngine` | `0x292C0` | 80 | UnwindData |  |
| 7 | `GetOtlVersion` | `0x2B680` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetOtlScriptList` | `0x2B9A0` | 441 | UnwindData |  |
| 11 | `OtlAssertFailed` | `0x31A30` | 114,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ShapingSetAssertFunction` | `0x31A30` | 114,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `ShapingSetInvariantAssertFunction` | `0x31A30` | 114,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetOtlGlyphAlternates` | `0x4D8D0` | 283 | UnwindData |  |
| 5 | `GetOtlLangSysList` | `0x4DA00` | 472 | UnwindData |  |
| 8 | `RepositionOtlSingleGlyph` | `0x4DBE0` | 320 | UnwindData |  |
| 9 | `SubstituteOtlSingleGlyph` | `0x4DD30` | 301 | UnwindData |  |
