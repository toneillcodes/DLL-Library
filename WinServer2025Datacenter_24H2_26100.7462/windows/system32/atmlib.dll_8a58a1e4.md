# Binary Specification: atmlib.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\atmlib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8a58a1e4c0d7c1a01f4711d0363c0697c86394a71635fcd3c6cf222f8aaef78e`
* **Total Exported Functions:** 76

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ATMAddFont` | `0x3310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ATMAddFontA` | `0x3320` | 311 | UnwindData |  |
| 3 | `ATMAddFontEx` | `0x3460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ATMAddFontExA` | `0x3470` | 428 | UnwindData |  |
| 5 | `ATMAddFontExW` | `0x3630` | 3,753 | UnwindData |  |
| 6 | `ATMAddFontW` | `0x44E0` | 335 | UnwindData |  |
| 7 | `ATMBBoxBaseXYShowText` | `0x4640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `ATMBBoxBaseXYShowTextA` | `0x4640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `ATMBBoxBaseXYShowTextW` | `0x4640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `ATMXYShowText` | `0x4640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `ATMXYShowTextA` | `0x4640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `ATMXYShowTextW` | `0x4640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ATMBeginFontChange` | `0x4650` | 52 | UnwindData |  |
| 11 | `ATMClient` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `ATMFontStatus` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ATMFontStatusA` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `ATMFontStatusW` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `ATMGetFontInfo` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `ATMGetFontInfoA` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `ATMGetFontInfoW` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `ATMInstallSubstFontA` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `ATMInstallSubstFontW` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `ATMMakePSS` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `ATMMakePSSA` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `ATMMakePSSW` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `ATMRemoveSubstFontA` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `ATMRemoveSubstFontW` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `ATMSelectEncoding` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `ATMSelectObject` | `0x4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `ATMEndFontChange` | `0x46A0` | 106 | UnwindData |  |
| 13 | `ATMEnumFonts` | `0x4710` | 37 | UnwindData |  |
| 14 | `ATMEnumFontsA` | `0x4710` | 37 | UnwindData |  |
| 15 | `ATMEnumFontsW` | `0x4740` | 37 | UnwindData |  |
| 16 | `ATMEnumMMFonts` | `0x4770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `ATMEnumMMFontsA` | `0x4780` | 149 | UnwindData |  |
| 18 | `ATMEnumMMFontsW` | `0x4820` | 39 | UnwindData |  |
| 19 | `ATMFinish` | `0x4850` | 52 | UnwindData |  |
| 20 | `ATMFontAvailable` | `0x4890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `ATMFontAvailableA` | `0x48A0` | 174 | UnwindData |  |
| 22 | `ATMFontAvailableW` | `0x4960` | 426 | UnwindData |  |
| 23 | `ATMFontSelected` | `0x4B10` | 48 | UnwindData |  |
| 27 | `ATMForceFontChange` | `0x4B50` | 27 | UnwindData |  |
| 28 | `ATMGetBuildStr` | `0x4B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `ATMGetBuildStrA` | `0x4BA0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `ATMGetBuildStrW` | `0x4C60` | 97 | UnwindData |  |
| 31 | `ATMGetFontBBox` | `0x4CD0` | 146 | UnwindData |  |
| 35 | `ATMGetFontPaths` | `0x4D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `ATMGetFontPathsA` | `0x4D80` | 489 | UnwindData |  |
| 37 | `ATMGetFontPathsW` | `0x4F70` | 845 | UnwindData |  |
| 38 | `ATMGetGlyphList` | `0x52D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `ATMGetGlyphListA` | `0x52D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `ATMGetGlyphListW` | `0x52E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `ATMGetMenuName` | `0x52F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `ATMGetMenuNameA` | `0x5300` | 254 | UnwindData |  |
| 43 | `ATMGetMenuNameW` | `0x5410` | 532 | UnwindData |  |
| 44 | `ATMGetNtmFields` | `0x5630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `ATMGetNtmFieldsA` | `0x5640` | 137 | UnwindData |  |
| 46 | `ATMGetNtmFieldsW` | `0x56D0` | 381 | UnwindData |  |
| 47 | `ATMGetOutline` | `0x5860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `ATMGetOutlineA` | `0x5870` | 160 | UnwindData |  |
| 49 | `ATMGetOutlineW` | `0x5920` | 511 | UnwindData |  |
| 50 | `ATMGetPostScriptName` | `0x5B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `ATMGetPostScriptNameA` | `0x5B40` | 255 | UnwindData |  |
| 52 | `ATMGetPostScriptNameW` | `0x5C50` | 516 | UnwindData |  |
| 53 | `ATMGetVersion` | `0x5E60` | 39 | UnwindData |  |
| 54 | `ATMGetVersionEx` | `0x5E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `ATMGetVersionExA` | `0x5EA0` | 233 | UnwindData |  |
| 56 | `ATMGetVersionExW` | `0x5F90` | 273 | UnwindData |  |
| 59 | `ATMMakePFM` | `0x60B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `ATMMakePFMA` | `0x60C0` | 244 | UnwindData |  |
| 61 | `ATMMakePFMW` | `0x61C0` | 1,224 | UnwindData |  |
| 65 | `ATMProperlyLoaded` | `0x6690` | 140 | UnwindData |  |
| 66 | `ATMRemoveFont` | `0x6730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `ATMRemoveFontA` | `0x6740` | 167 | UnwindData |  |
| 68 | `ATMRemoveFontW` | `0x67F0` | 2,125 | UnwindData |  |
| 73 | `ATMSetFlags` | `0x7050` | 102 | UnwindData |  |
