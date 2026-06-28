# Binary Specification: icu.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\icu.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `551bf398863593a4d28e54a68fd1883ee11e75d59c27bc506f39f87b675b71ac`
* **Total Exported Functions:** 1059

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 247 | `ucal_getNow` | `0x1A170` | 83 | UnwindData |  |
| 13 | `UCNV_TO_U_CALLBACK_STOP` | `0x9E000` | 69,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `u_cleanup` | `0x9E000` | 69,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `u_getIntPropertyMinValue` | `0xAEEB0` | 21,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `u_isIDPart` | `0xB4250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `u_isIDStart` | `0xB4260` | 25,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 492 | `udat_setLenient` | `0xBA5F0` | 22,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `u_charDigitValue` | `0xBFD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `u_charsToUChars` | `0xBFD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `u_foldCase` | `0xBFD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `u_getIntPropertyValue` | `0xBFD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `u_hasBinaryProperty` | `0xBFDA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `u_isUAlphabetic` | `0xBFDB0` | 25 | UnwindData |  |
| 66 | `u_isULowercase` | `0xBFDD0` | 21 | UnwindData |  |
| 76 | `u_isdigit` | `0xBFDF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `u_strCaseCompare` | `0xBFE00` | 96 | UnwindData |  |
| 111 | `u_strFromWCS` | `0xBFE70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `u_strToLower` | `0xBFE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `u_strToTitle` | `0xBFE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `u_strToUTF8` | `0xBFEA0` | 44 | UnwindData |  |
| 120 | `u_strToUpper` | `0xBFEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `u_strToWCS` | `0xBFEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `u_strlen` | `0xBFF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `u_tolower` | `0xBFF20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `u_toupper` | `0xBFF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `u_vformatMessage` | `0xBFF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `ublock_getCode` | `0xBFF50` | 25 | UnwindData |  |
| 204 | `ubrk_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `ucal_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `ucol_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `udat_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `udatpg_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `udtitvfmt_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `ufieldpositer_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `ufmt_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `uidna_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 575 | `uldn_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 589 | `ulistfmt_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `umsg_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 673 | `unorm2_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 696 | `unum_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 748 | `unumsys_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `uplrules_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 837 | `ureldatefmt_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1045 | `utrans_close` | `0xBFF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `ubrk_first` | `0xBFF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 675 | `unorm2_getCombiningClass` | `0xBFF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `ubrk_next` | `0xBFFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `ubrk_open` | `0xBFFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `ubrk_openRules` | `0xBFFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `ubrk_preceding` | `0xBFFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 686 | `unorm2_isInert` | `0xBFFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `ubrk_setText` | `0xC0000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `ucal_add` | `0xC0010` | 28 | UnwindData |  |
| 228 | `ucal_clearField` | `0xC0040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `ucal_get` | `0xC0050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `ucal_getCanonicalTimeZoneID` | `0xC0070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `ucal_getDefaultTimeZone` | `0xC0080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `ucal_getKeywordValuesForLocale` | `0xC0090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `ucal_getTimeZoneIDForWindowsID` | `0xC00A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `ucal_getWindowsTimeZoneID` | `0xC00B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `ucal_open` | `0xC00C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `ucal_openTimeZoneIDEnumeration` | `0xC00D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `ucal_openTimeZones` | `0xC00E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `ucal_setGregorianChange` | `0xC0100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `ucal_setMillis` | `0xC0110` | 21 | UnwindData |  |
| 273 | `ucasemap_close` | `0xC0130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `ucasemap_open` | `0xC0140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `ucasemap_utf8FoldCase` | `0xC0150` | 73 | UnwindData |  |
| 372 | `ucol_closeElements` | `0xC01A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `ucol_getAttribute` | `0xC01B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `ucol_getKeywordValuesForLocale` | `0xC01C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `ucol_getRules` | `0xC01D0` | 89 | UnwindData |  |
| 392 | `ucol_getSortKey` | `0xC0230` | 35 | UnwindData |  |
| 393 | `ucol_getStrength` | `0xC0260` | 30 | UnwindData |  |
| 402 | `ucol_next` | `0xC0290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `ucol_open` | `0xC02A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `ucol_openElements` | `0xC02B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `ucol_openRules` | `0xC02C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `ucol_previous` | `0xC02D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `ucol_setAttribute` | `0xC02F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `ucol_setStrength` | `0xC0300` | 33 | UnwindData |  |
| 420 | `ucol_strcoll` | `0xC0330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `ucurr_getDefaultFractionDigits` | `0xC0340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `ucurr_getName` | `0xC0350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `udat_applyPattern` | `0xC0360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `ubrk_countAvailable` | `0xC0370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `ucal_countAvailable` | `0xC0370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `udat_countAvailable` | `0xC0370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `uloc_countAvailable` | `0xC0370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 697 | `unum_countAvailable` | `0xC0370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `udat_countSymbols` | `0xC0380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `udat_format` | `0xC0390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `ubrk_getAvailable` | `0xC03A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `ucal_getAvailable` | `0xC03A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 476 | `udat_getAvailable` | `0xC03A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `uloc_getAvailable` | `0xC03A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 706 | `unum_getAvailable` | `0xC03A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `ubrk_following` | `0xC03B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 478 | `udat_getCalendar` | `0xC03B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `unorm2_hasBoundaryAfter` | `0xC03B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `udat_getSymbols` | `0xC03D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `udat_open` | `0xC03E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 487 | `udat_parseCalendar` | `0xC03F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 489 | `udat_setBooleanAttribute` | `0xC0400` | 31 | UnwindData |  |
| 214 | `ubrk_isBoundary` | `0xC0430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `udat_setCalendar` | `0xC0430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `udat_toPattern` | `0xC0450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `udatpg_getBestPattern` | `0xC0460` | 41 | UnwindData |  |
| 504 | `udatpg_getBestPatternWithOptions` | `0xC0490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `udatpg_open` | `0xC04A0` | 134 | UnwindData |  |
| 530 | `uenum_close` | `0xC0530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 531 | `uenum_count` | `0xC0540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | `uenum_next` | `0xC0550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `uenum_unext` | `0xC0560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 562 | `uidna_nameToASCII` | `0xC0570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 566 | `uidna_openUTS46` | `0xC0580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `uldn_open` | `0xC0590` | 138 | UnwindData |  |
| 599 | `uloc_addLikelySubtags` | `0xC0620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 600 | `uloc_canonicalize` | `0xC0630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `uloc_forLanguageTag` | `0xC0640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 604 | `uloc_getBaseName` | `0xC0650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `uloc_getCountry` | `0xC0660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `uloc_getDefault` | `0xC0670` | 19 | UnwindData |  |
| 621 | `uloc_getLanguage` | `0xC0690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 624 | `uloc_getName` | `0xC06A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `uloc_getParent` | `0xC06B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `uloc_setKeywordValue` | `0xC06C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 634 | `uloc_toLanguageTag` | `0xC06D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | `uloc_toUnicodeLocaleType` | `0xC06E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 640 | `ulocdata_getCLDRVersion` | `0xC06F0` | 97 | UnwindData |  |
| 677 | `unorm2_getInstance` | `0xC0760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 678 | `unorm2_getNFCInstance` | `0xC0770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `unorm2_getNFDInstance` | `0xC0780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 687 | `unorm2_isNormalized` | `0xC0790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 688 | `unorm2_normalize` | `0xC07A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `unum_getSymbol` | `0xC07B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `unum_open` | `0xC07C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `unum_setAttribute` | `0xC07D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 724 | `unum_toPattern` | `0xC07E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `unumsys_getName` | `0xC07F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `unumsys_open` | `0xC0800` | 108 | UnwindData |  |
| 767 | `uregex_close` | `0xC0880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 768 | `uregex_end` | `0xC0890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `uregex_end64` | `0xC0890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 772 | `uregex_findNext` | `0xC08A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 790 | `uregex_matches` | `0xC08B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `uregex_openUText` | `0xC08C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 803 | `uregex_replaceAllUText` | `0xC08D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `uregex_setText` | `0xC08E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 820 | `uregex_start` | `0xC08F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 821 | `uregex_start64` | `0xC08F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `u_catclose` | `0xC0900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `ures_close` | `0xC0900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 859 | `ures_getStringByIndex` | `0xC0910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 884 | `usearch_close` | `0xC0920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `usearch_first` | `0xC0930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `usearch_getMatchedLength` | `0xC0940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 896 | `usearch_last` | `0xC0950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 899 | `usearch_openFromCollator` | `0xC0960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 907 | `usearch_setPattern` | `0xC0970` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 908 | `usearch_setText` | `0xC09C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `utext_char32At` | `0xC09D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1008 | `utext_close` | `0xC09E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `utext_extract` | `0xC09F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `utext_nativeLength` | `0xC0A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `utext_openUChars` | `0xC0A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `utext_openUTF8` | `0xC0A20` | 40,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `ubrk_setUText` | `0xCA680` | 4,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 912 | `uset_addRange` | `0xCB730` | 2,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `ucptrie_close` | `0xCC020` | 30,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `UCNV_FROM_U_CALLBACK_ESCAPE` | `0xD37A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `UCNV_FROM_U_CALLBACK_SKIP` | `0xD37B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `UCNV_FROM_U_CALLBACK_STOP` | `0xD37C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `UCNV_FROM_U_CALLBACK_SUBSTITUTE` | `0xD37D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `UCNV_TO_U_CALLBACK_ESCAPE` | `0xD37E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `UCNV_TO_U_CALLBACK_SKIP` | `0xD37F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `UCNV_TO_U_CALLBACK_SUBSTITUTE` | `0xD3820` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `u_UCharsToChars` | `0xD38E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `u_austrcpy` | `0xD38F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `u_austrncpy` | `0xD3900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `u_catgets` | `0xD3910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `u_catopen` | `0xD3920` | 31 | UnwindData |  |
| 868 | `ures_open` | `0xD3920` | 31 | UnwindData |  |
| 21 | `u_charAge` | `0xD3950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `u_charDirection` | `0xD3960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `u_charFromName` | `0xD3970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `u_charMirror` | `0xD3980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `u_charName` | `0xD3990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `u_charType` | `0xD39A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `u_countChar32` | `0xD39B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `u_digit` | `0xD39C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `u_enumCharNames` | `0xD39D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `u_enumCharTypes` | `0xD39E0` | 72 | UnwindData |  |
| 34 | `u_errorName` | `0xD3A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `u_forDigit` | `0xD3A40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `u_formatMessage` | `0xD3A70` | 45 | UnwindData |  |
| 38 | `u_formatMessageWithError` | `0xD3AB0` | 57 | UnwindData |  |
| 39 | `u_getBidiPairedBracket` | `0xD3AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `u_getBinaryPropertySet` | `0xD3B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `u_getCombiningClass` | `0xD3B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `u_getDataVersion` | `0xD3B20` | 114 | UnwindData |  |
| 43 | `u_getFC_NFKC_Closure` | `0xD3BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `u_getIntPropertyMap` | `0xD3BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `u_getIntPropertyMaxValue` | `0xD3BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `u_getNumericValue` | `0xD3BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `u_getPropertyEnum` | `0xD3BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `u_getPropertyName` | `0xD3BF0` | 58 | UnwindData |  |
| 51 | `u_getPropertyValueEnum` | `0xD3C30` | 59 | UnwindData |  |
| 52 | `u_getPropertyValueName` | `0xD3C80` | 90 | UnwindData |  |
| 53 | `u_getUnicodeVersion` | `0xD3CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `u_getVersion` | `0xD3D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `u_init` | `0xD3D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `u_isIDIgnorable` | `0xD3D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `u_isISOControl` | `0xD3D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `u_isJavaIDPart` | `0xD3D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `u_isJavaIDStart` | `0xD3D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `u_isJavaSpaceChar` | `0xD3D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `u_isMirrored` | `0xD3D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `u_isUUppercase` | `0xD3DA0` | 21 | UnwindData |  |
| 68 | `u_isUWhiteSpace` | `0xD3DC0` | 22 | UnwindData |  |
| 69 | `u_isWhitespace` | `0xD3DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `u_isalnum` | `0xD3DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `u_isalpha` | `0xD3E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `u_isbase` | `0xD3E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `u_isblank` | `0xD3E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `u_iscntrl` | `0xD3E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `u_isdefined` | `0xD3E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `u_isgraph` | `0xD3E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `u_islower` | `0xD3E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `u_isprint` | `0xD3E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `u_ispunct` | `0xD3E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `u_isspace` | `0xD3E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `u_istitle` | `0xD3EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `u_isupper` | `0xD3EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `u_isxdigit` | `0xD3EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `u_memcasecmp` | `0xD3ED0` | 61 | UnwindData |  |
| 86 | `u_memchr` | `0xD3F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `u_memchr32` | `0xD3F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `u_memcmp` | `0xD3F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `u_memcmpCodePointOrder` | `0xD3F50` | 36 | UnwindData |  |
| 90 | `u_memcpy` | `0xD3F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `u_memmove` | `0xD3F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `u_memrchr` | `0xD3FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `u_memrchr32` | `0xD3FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `u_memset` | `0xD3FC0` | 53 | UnwindData |  |
| 95 | `u_parseMessage` | `0xD4000` | 45 | UnwindData |  |
| 96 | `u_parseMessageWithError` | `0xD4040` | 57 | UnwindData |  |
| 97 | `u_setMemoryFunctions` | `0xD4080` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `u_shapeArabic` | `0xD40D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `u_strCompare` | `0xD40E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `u_strCompareIter` | `0xD40F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `u_strFindFirst` | `0xD4100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `u_strFindLast` | `0xD4110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `u_strFoldCase` | `0xD4120` | 70 | UnwindData |  |
| 105 | `u_strFromJavaModifiedUTF8WithSub` | `0xD4170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `u_strFromUTF32` | `0xD4180` | 44 | UnwindData |  |
| 107 | `u_strFromUTF32WithSub` | `0xD41C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `u_strFromUTF8` | `0xD41D0` | 44 | UnwindData |  |
| 109 | `u_strFromUTF8Lenient` | `0xD4210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `u_strFromUTF8WithSub` | `0xD4220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `u_strHasMoreChar32Than` | `0xD4230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `u_strToJavaModifiedUTF8` | `0xD4240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `u_strToUTF32` | `0xD4250` | 44 | UnwindData |  |
| 117 | `u_strToUTF32WithSub` | `0xD4290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `u_strToUTF8WithSub` | `0xD42A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `u_strcasecmp` | `0xD42B0` | 61 | UnwindData |  |
| 123 | `u_strcat` | `0xD4300` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `u_strchr` | `0xD4340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `u_strchr32` | `0xD4350` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `u_strcmp` | `0xD43C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `u_strcmpCodePointOrder` | `0xD43D0` | 36 | UnwindData |  |
| 128 | `u_strcpy` | `0xD4400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `u_strcspn` | `0xD4410` | 24 | UnwindData |  |
| 130 | `u_stringHasBinaryProperty` | `0xD4430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `u_strncasecmp` | `0xD4440` | 63 | UnwindData |  |
| 133 | `u_strncat` | `0xD4490` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `u_strncmp` | `0xD44E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `u_strncmpCodePointOrder` | `0xD44F0` | 36 | UnwindData |  |
| 136 | `u_strncpy` | `0xD4520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `u_strpbrk` | `0xD4530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `u_strrchr` | `0xD4540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `u_strrchr32` | `0xD4550` | 116 | UnwindData |  |
| 140 | `u_strrstr` | `0xD45D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `u_strspn` | `0xD45F0` | 24 | UnwindData |  |
| 142 | `u_strstr` | `0xD4610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `u_strtok_r` | `0xD4630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `u_totitle` | `0xD4640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `u_uastrcpy` | `0xD4650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `u_uastrncpy` | `0xD4660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `u_unescape` | `0xD4670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `u_unescapeAt` | `0xD4680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `u_versionFromString` | `0xD4690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `u_versionFromUString` | `0xD46A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `u_versionToString` | `0xD46B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `u_vformatMessageWithError` | `0xD46C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `u_vparseMessage` | `0xD46D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `u_vparseMessageWithError` | `0xD46E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `ubidi_close` | `0xD46F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `ubidi_countParagraphs` | `0xD4700` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `ubidi_countRuns` | `0xD4730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `ubidi_getBaseDirection` | `0xD4740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `ubidi_getClassCallback` | `0xD4750` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `ubidi_getCustomizedClass` | `0xD4780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `ubidi_getDirection` | `0xD4790` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `ubidi_getLength` | `0xD47C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `ubidi_getLevelAt` | `0xD47F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `ubidi_getLevels` | `0xD4800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `ubidi_getLogicalIndex` | `0xD4810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `ubidi_getLogicalMap` | `0xD4820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `ubidi_getLogicalRun` | `0xD4830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `ubidi_getParaLevel` | `0xD4840` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `ubidi_getParagraph` | `0xD4870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `ubidi_getParagraphByIndex` | `0xD4880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `ubidi_getProcessedLength` | `0xD4890` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `ubidi_getReorderingMode` | `0xD48C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `ubidi_getReorderingOptions` | `0xD48E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `ubidi_getResultLength` | `0xD4900` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `ubidi_getText` | `0xD4930` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `ubidi_getVisualIndex` | `0xD4960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `ubidi_getVisualMap` | `0xD4970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `ubidi_getVisualRun` | `0xD4980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `ubidi_invertMap` | `0xD4990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `ubidi_isInverse` | `0xD49A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `ubidi_isOrderParagraphsLTR` | `0xD49C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `ubidi_open` | `0xD49E0` | 29 | UnwindData |  |
| 186 | `ubidi_openSized` | `0xD4A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `ubidi_orderParagraphsLTR` | `0xD4A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `ubidi_reorderLogical` | `0xD4A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `ubidi_reorderVisual` | `0xD4A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `ubidi_setClassCallback` | `0xD4A60` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `ubidi_setContext` | `0xD4AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `ubidi_setInverse` | `0xD4AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `ubidi_setLine` | `0xD4AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `ubidi_setPara` | `0xD4AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `ubidi_setReorderingMode` | `0xD4B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `ubidi_setReorderingOptions` | `0xD4B10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `ubidi_writeReordered` | `0xD4B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `ubidi_writeReverse` | `0xD4B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `ubiditransform_close` | `0xD4B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `ubiditransform_open` | `0xD4B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `ubiditransform_transform` | `0xD4B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `ubrk_clone` | `0xD4BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `ubrk_current` | `0xD4BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 685 | `unorm2_hasBoundaryBefore` | `0xD4BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `ubrk_getBinaryRules` | `0xD4BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `ubrk_getLocaleByType` | `0xD4BF0` | 62 | UnwindData |  |
| 212 | `ubrk_getRuleStatus` | `0xD4C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 481 | `udat_getNumberFormat` | `0xD4C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `ubrk_getRuleStatusVec` | `0xD4C60` | 25 | UnwindData |  |
| 215 | `ubrk_last` | `0xD4C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `ubrk_openBinaryRules` | `0xD4CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `ubrk_previous` | `0xD4CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `udat_isLenient` | `0xD4CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `ubrk_refreshUText` | `0xD4CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `ucol_getVersion` | `0xD4CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `ubrk_safeClone` | `0xD4CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `ucal_clear` | `0xD4D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `ucal_clone` | `0xD4D10` | 62 | UnwindData |  |
| 232 | `ucal_equivalentTo` | `0xD4D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `ucal_getAttribute` | `0xD4D80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `ucal_getDSTSavings` | `0xD4DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `ucal_getDayOfWeekType` | `0xD4DE0` | 32 | UnwindData |  |
| 240 | `ucal_getFieldDifference` | `0xD4E10` | 29 | UnwindData |  |
| 241 | `ucal_getGregorianChange` | `0xD4E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `ucal_getHostTimeZone` | `0xD4E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `ucal_getLimit` | `0xD4E60` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `ucal_getLocaleByType` | `0xD4EF0` | 65 | UnwindData |  |
| 246 | `ucal_getMillis` | `0xD4F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `ucal_getTZDataVersion` | `0xD4F60` | 39 | UnwindData |  |
| 249 | `ucal_getTimeZoneDisplayName` | `0xD4F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `ucal_getTimeZoneID` | `0xD4FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `ucal_getTimeZoneOffsetFromLocal` | `0xD4FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `ucal_getTimeZoneTransitionDate` | `0xD4FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `ucal_getType` | `0xD4FD0` | 31 | UnwindData |  |
| 255 | `ucal_getWeekendTransition` | `0xD5000` | 32 | UnwindData |  |
| 257 | `ucal_inDaylightTime` | `0xD5030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `ucal_isSet` | `0xD5050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `ucal_isWeekend` | `0xD5060` | 32 | UnwindData |  |
| 261 | `ucal_openCountryTimeZones` | `0xD5090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `ucal_roll` | `0xD50B0` | 28 | UnwindData |  |
| 265 | `ucal_set` | `0xD50E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `ucal_setAttribute` | `0xD50F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `ucal_setDate` | `0xD5140` | 25 | UnwindData |  |
| 268 | `ucal_setDateTime` | `0xD5160` | 55 | UnwindData |  |
| 269 | `ucal_setDefaultTimeZone` | `0xD51A0` | 34 | UnwindData |  |
| 272 | `ucal_setTimeZone` | `0xD51D0` | 70 | UnwindData |  |
| 274 | `ucasemap_getBreakIterator` | `0xD5220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `ucasemap_getLocale` | `0xD5230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | `uregion_getRegionCode` | `0xD5230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `ucasemap_getOptions` | `0xD5240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `ucasemap_setBreakIterator` | `0xD5250` | 61 | UnwindData |  |
| 279 | `ucasemap_setLocale` | `0xD52A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `ucasemap_setOptions` | `0xD52B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `ucasemap_toTitle` | `0xD52D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `ucasemap_utf8ToLower` | `0xD52E0` | 72 | UnwindData |  |
| 284 | `ucasemap_utf8ToTitle` | `0xD5330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `ucasemap_utf8ToUpper` | `0xD5340` | 72 | UnwindData |  |
| 286 | `ucfpos_close` | `0xD5390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `ucfpos_constrainCategory` | `0xD53A0` | 35 | UnwindData |  |
| 288 | `ucfpos_constrainField` | `0xD53D0` | 39 | UnwindData |  |
| 289 | `ucfpos_getCategory` | `0xD5400` | 27 | UnwindData |  |
| 290 | `ucfpos_getField` | `0xD5430` | 27 | UnwindData |  |
| 291 | `ucfpos_getIndexes` | `0xD5460` | 39 | UnwindData |  |
| 292 | `ucfpos_getInt64IterationContext` | `0xD5490` | 28 | UnwindData |  |
| 293 | `ucfpos_matchesField` | `0xD54C0` | 43 | UnwindData |  |
| 294 | `ucfpos_open` | `0xD5500` | 70 | UnwindData |  |
| 295 | `ucfpos_reset` | `0xD5550` | 36 | UnwindData |  |
| 296 | `ucfpos_setInt64IterationContext` | `0xD5580` | 31 | UnwindData |  |
| 297 | `ucfpos_setState` | `0xD55B0` | 47 | UnwindData |  |
| 298 | `ucnv_cbFromUWriteBytes` | `0xD55F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `ucnv_cbFromUWriteSub` | `0xD5600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `ucnv_cbFromUWriteUChars` | `0xD5610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `ucnv_cbToUWriteSub` | `0xD5620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `ucnv_cbToUWriteUChars` | `0xD5630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `ucnv_clone` | `0xD5640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `ucnv_close` | `0xD5660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `ucnv_compareNames` | `0xD5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `ucnv_convert` | `0xD5680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `ucnv_convertEx` | `0xD5690` | 124 | UnwindData |  |
| 308 | `ucnv_countAliases` | `0xD5720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `ucnv_countAvailable` | `0xD5730` | 43 | UnwindData |  |
| 310 | `ucnv_countStandards` | `0xD5770` | 46 | UnwindData |  |
| 311 | `ucnv_detectUnicodeSignature` | `0xD57B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `ucnv_fixFileSeparator` | `0xD57C0` | 96 | UnwindData |  |
| 313 | `ucnv_flushCache` | `0xD5830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `ucnv_fromAlgorithmic` | `0xD5840` | 59 | UnwindData |  |
| 315 | `ucnv_fromUChars` | `0xD5890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `ucnv_fromUCountPending` | `0xD58A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `ucnv_fromUnicode` | `0xD5900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `ucnv_getAlias` | `0xD5910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `ucnv_getAliases` | `0xD5920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `ucnv_getAvailableName` | `0xD5940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `ucnv_getCCSID` | `0xD5950` | 131 | UnwindData |  |
| 322 | `ucnv_getCanonicalName` | `0xD59E0` | 131 | UnwindData |  |
| 323 | `ucnv_getDefaultName` | `0xD5A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `ucnv_getDisplayName` | `0xD5A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `ucnv_getFromUCallBack` | `0xD5A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `ucnv_getInvalidChars` | `0xD5AB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `ucnv_getInvalidUChars` | `0xD5B10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `ucnv_getMaxCharSize` | `0xD5B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `ucnv_getMinCharSize` | `0xD5B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `ucnv_getName` | `0xD5BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `ucnv_getNextUChar` | `0xD5BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `ucnv_getPlatform` | `0xD5BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `ucnv_getStandard` | `0xD5BE0` | 91 | UnwindData |  |
| 334 | `ucnv_getStandardName` | `0xD5C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `ucnv_getStarters` | `0xD5C60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `ucnv_getSubstChars` | `0xD5C90` | 86 | UnwindData |  |
| 337 | `ucnv_getToUCallBack` | `0xD5CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `ucnv_getType` | `0xD5D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `ucnv_getUnicodeSet` | `0xD5D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `ucnv_isAmbiguous` | `0xD5D30` | 21 | UnwindData |  |
| 341 | `ucnv_isFixedWidth` | `0xD5D50` | 79 | UnwindData |  |
| 342 | `ucnv_open` | `0xD5DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `ucnv_openAllNames` | `0xD5DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `ucnv_openCCSID` | `0xD5DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `ucnv_openPackage` | `0xD5DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `ucnv_openStandardNames` | `0xD5DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `ucnv_openU` | `0xD5E00` | 110 | UnwindData |  |
| 348 | `ucnv_reset` | `0xD5E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `ucnv_resetFromUnicode` | `0xD5E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `ucnv_resetToUnicode` | `0xD5EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `ucnv_safeClone` | `0xD5ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `ucnv_setDefaultName` | `0xD5EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `ucnv_setFallback` | `0xD5EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `ucnv_setFromUCallBack` | `0xD5F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `ucnv_setSubstChars` | `0xD5F10` | 81 | UnwindData |  |
| 356 | `ucnv_setSubstString` | `0xD5F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `ucnv_setToUCallBack` | `0xD5F80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `ucnv_toAlgorithmic` | `0xD5FC0` | 61 | UnwindData |  |
| 359 | `ucnv_toUChars` | `0xD6010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `ucnv_toUCountPending` | `0xD6020` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `ucnv_toUnicode` | `0xD6070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `ucnv_usesFallback` | `0xD6080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `ucnvsel_close` | `0xD6090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `ucnvsel_open` | `0xD60A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `ucnvsel_openFromSerialized` | `0xD60B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `ucnvsel_selectForString` | `0xD60C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `ucnvsel_selectForUTF8` | `0xD60D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `ucnvsel_serialize` | `0xD60E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `ucol_clone` | `0xD60F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `ucol_cloneBinary` | `0xD6110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `ucol_countAvailable` | `0xD6120` | 29 | UnwindData |  |
| 374 | `ucol_equal` | `0xD6150` | 28 | UnwindData |  |
| 376 | `ucol_getAvailable` | `0xD6180` | 67 | UnwindData |  |
| 377 | `ucol_getBound` | `0xD61D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `ucol_getContractionsAndExpansions` | `0xD61E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `ucol_getDisplayName` | `0xD61F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `ucol_getEquivalentReorderCodes` | `0xD6200` | 134 | UnwindData |  |
| 381 | `ucol_getFunctionalEquivalent` | `0xD6290` | 69 | UnwindData |  |
| 382 | `ucol_getKeywordValues` | `0xD62E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `ucol_getKeywords` | `0xD62F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `ucol_getLocaleByType` | `0xD6300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `ucol_getMaxExpansion` | `0xD6310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `ucol_getMaxVariable` | `0xD6320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `ucol_getOffset` | `0xD6340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `ucol_getReorderCodes` | `0xD6350` | 32 | UnwindData |  |
| 391 | `ucol_getRulesEx` | `0xD6380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `ucol_getTailoredSet` | `0xD6390` | 74 | UnwindData |  |
| 395 | `ucol_getUCAVersion` | `0xD63E0` | 71 | UnwindData |  |
| 396 | `ucol_getVariableTop` | `0xD6430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `ucol_greater` | `0xD6440` | 29 | UnwindData |  |
| 399 | `ucol_greaterOrEqual` | `0xD6470` | 29 | UnwindData |  |
| 400 | `ucol_keyHashCode` | `0xD64A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `ucol_mergeSortkeys` | `0xD64B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `ucol_nextSortKeyPart` | `0xD64C0` | 58 | UnwindData |  |
| 405 | `ucol_openAvailableLocales` | `0xD6500` | 66 | UnwindData |  |
| 406 | `ucol_openBinary` | `0xD6550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `ucol_primaryOrder` | `0xD6560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `ucol_reset` | `0xD6570` | 42 | UnwindData |  |
| 412 | `ucol_safeClone` | `0xD65A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `ucol_secondaryOrder` | `0xD65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `ucol_setMaxVariable` | `0xD65C0` | 31 | UnwindData |  |
| 491 | `udat_setContext` | `0xD65C0` | 31 | UnwindData |  |
| 416 | `ucol_setOffset` | `0xD65F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `ucol_setReorderCodes` | `0xD6600` | 31 | UnwindData |  |
| 419 | `ucol_setText` | `0xD6630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `ucol_strcollIter` | `0xD6640` | 58 | UnwindData |  |
| 422 | `ucol_strcollUTF8` | `0xD6680` | 53 | UnwindData |  |
| 423 | `ucol_tertiaryOrder` | `0xD66C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `ucpmap_get` | `0xD66D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `ucptrie_get` | `0xD66D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `ucpmap_getRange` | `0xD66E0` | 68 | UnwindData |  |
| 428 | `ucptrie_getRange` | `0xD66E0` | 68 | UnwindData |  |
| 429 | `ucptrie_getType` | `0xD6730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `ucptrie_getValueWidth` | `0xD6740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `ucptrie_internalSmallIndex` | `0xD6750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `ucptrie_internalSmallU8Index` | `0xD6760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `ucptrie_internalU8PrevIndex` | `0xD6770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `ucptrie_openFromBinary` | `0xD6780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `ucptrie_toBinary` | `0xD6790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `ucsdet_close` | `0xD67A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `ucsdet_detect` | `0xD67B0` | 64 | UnwindData |  |
| 438 | `ucsdet_detectAll` | `0xD6800` | 22 | UnwindData |  |
| 439 | `ucsdet_enableInputFilter` | `0xD6820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `ucsdet_getAllDetectableCharsets` | `0xD6840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `ucsdet_getConfidence` | `0xD6850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `ucsdet_getLanguage` | `0xD6870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `ucsdet_getName` | `0xD6890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `ucsdet_getUChars` | `0xD68B0` | 22 | UnwindData |  |
| 445 | `ucsdet_isInputFilterEnabled` | `0xD68D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `ucsdet_open` | `0xD68F0` | 86 | UnwindData |  |
| 447 | `ucsdet_setDeclaredEncoding` | `0xD6950` | 120 | UnwindData |  |
| 448 | `ucsdet_setText` | `0xD69D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `ucurr_countCurrencies` | `0xD6A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `ucurr_forLocale` | `0xD6A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `ucurr_forLocaleAndDate` | `0xD6A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `ucurr_getDefaultFractionDigitsForUsage` | `0xD6A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `ucurr_getKeywordValuesForLocale` | `0xD6A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `ucurr_getNumericCode` | `0xD6A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `ucurr_getPluralName` | `0xD6A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `ucurr_getRoundingIncrement` | `0xD6A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `ucurr_getRoundingIncrementForUsage` | `0xD6A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 460 | `ucurr_isAvailable` | `0xD6AA0` | 147 | UnwindData |  |
| 461 | `ucurr_openISOCurrencies` | `0xD6B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `ucurr_register` | `0xD6B50` | 128 | UnwindData |  |
| 463 | `ucurr_unregister` | `0xD6BE0` | 26 | UnwindData |  |
| 464 | `udat_adoptNumberFormat` | `0xD6C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `udat_adoptNumberFormatForFields` | `0xD6C20` | 119 | UnwindData |  |
| 467 | `udat_clone` | `0xD6CA0` | 62 | UnwindData |  |
| 472 | `udat_formatCalendar` | `0xD6CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `udat_formatCalendarForFields` | `0xD6D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `udat_formatForFields` | `0xD6D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `udat_get2DigitYearStart` | `0xD6D20` | 51 | UnwindData |  |
| 477 | `udat_getBooleanAttribute` | `0xD6D60` | 32 | UnwindData |  |
| 479 | `udat_getContext` | `0xD6D90` | 32 | UnwindData |  |
| 480 | `udat_getLocaleByType` | `0xD6DC0` | 40 | UnwindData |  |
| 709 | `unum_getLocaleByType` | `0xD6DC0` | 40 | UnwindData |  |
| 482 | `udat_getNumberFormatForField` | `0xD6DF0` | 108 | UnwindData |  |
| 486 | `udat_parse` | `0xD6E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `udat_set2DigitYearStart` | `0xD6E80` | 78 | UnwindData |  |
| 493 | `udat_setNumberFormat` | `0xD6EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `udat_setSymbols` | `0xD6F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `udat_toCalendarDateField` | `0xD6F10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 497 | `udatpg_addPattern` | `0xD6F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `udatpg_clone` | `0xD6F50` | 63 | UnwindData |  |
| 500 | `udatpg_getAppendItemFormat` | `0xD6FA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `udatpg_getAppendItemName` | `0xD6FE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `udatpg_getBaseSkeleton` | `0xD7020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `udatpg_getDateTimeFormat` | `0xD7030` | 75 | UnwindData |  |
| 506 | `udatpg_getDecimal` | `0xD7090` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `udatpg_getDefaultHourCycle` | `0xD70C0` | 90 | UnwindData |  |
| 508 | `udatpg_getFieldDisplayName` | `0xD7120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `udatpg_getPatternForSkeleton` | `0xD7130` | 133 | UnwindData |  |
| 510 | `udatpg_getSkeleton` | `0xD71C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `udatpg_openBaseSkeletons` | `0xD71D0` | 30 | UnwindData |  |
| 513 | `udatpg_openEmpty` | `0xD7200` | 112 | UnwindData |  |
| 514 | `udatpg_openSkeletons` | `0xD7280` | 30 | UnwindData |  |
| 515 | `udatpg_replaceFieldTypes` | `0xD72B0` | 68 | UnwindData |  |
| 516 | `udatpg_replaceFieldTypesWithOptions` | `0xD7300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `udatpg_setAppendItemFormat` | `0xD7310` | 86 | UnwindData |  |
| 518 | `udatpg_setAppendItemName` | `0xD7370` | 89 | UnwindData |  |
| 519 | `udatpg_setDateTimeFormat` | `0xD73D0` | 127 | UnwindData |  |
| 520 | `udatpg_setDecimal` | `0xD7460` | 108 | UnwindData |  |
| 522 | `udtitvfmt_closeResult` | `0xD74E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 523 | `udtitvfmt_format` | `0xD74F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `udtitvfmt_formatToResult` | `0xD7500` | 112 | UnwindData |  |
| 525 | `udtitvfmt_getContext` | `0xD7580` | 29 | UnwindData |  |
| 526 | `udtitvfmt_open` | `0xD75B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `udtitvfmt_openResult` | `0xD75C0` | 119 | UnwindData |  |
| 528 | `udtitvfmt_resultAsValue` | `0xD7640` | 23 | UnwindData |  |
| 529 | `udtitvfmt_setContext` | `0xD7660` | 28 | UnwindData |  |
| 533 | `uenum_openCharStringsEnumeration` | `0xD7690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `uenum_openUCharStringsEnumeration` | `0xD76A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `uenum_reset` | `0xD76B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `ufieldpositer_next` | `0xD76C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `ufieldpositer_open` | `0xD76D0` | 76 | UnwindData |  |
| 541 | `ufmt_getArrayItemByIndex` | `0xD7730` | 68 | UnwindData |  |
| 542 | `ufmt_getArrayLength` | `0xD7780` | 32 | UnwindData |  |
| 543 | `ufmt_getDate` | `0xD77B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `ufmt_getDecNumChars` | `0xD77E0` | 85 | UnwindData |  |
| 545 | `ufmt_getDouble` | `0xD7840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | `ufmt_getInt64` | `0xD7850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `ufmt_getLong` | `0xD7860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `ufmt_getObject` | `0xD7870` | 36 | UnwindData |  |
| 549 | `ufmt_getType` | `0xD78A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `ufmt_getUChars` | `0xD78C0` | 99 | UnwindData |  |
| 551 | `ufmt_isNumeric` | `0xD7930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `ufmt_open` | `0xD7950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `ufmtval_getString` | `0xD7960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `ufmtval_nextPosition` | `0xD7970` | 62 | UnwindData |  |
| 555 | `ugender_getInstance` | `0xD79C0` | 110 | UnwindData |  |
| 556 | `ugender_getListGender` | `0xD7A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `uidna_labelToASCII` | `0xD7A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 559 | `uidna_labelToASCII_UTF8` | `0xD7A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `uidna_labelToUnicode` | `0xD7A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `uidna_labelToUnicodeUTF8` | `0xD7A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `uidna_nameToASCII_UTF8` | `0xD7A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `uidna_nameToUnicode` | `0xD7AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 565 | `uidna_nameToUnicodeUTF8` | `0xD7AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 567 | `uiter_current32` | `0xD7AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 568 | `uiter_getState` | `0xD7AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `uiter_next32` | `0xD7AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `uiter_previous32` | `0xD7B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `uiter_setState` | `0xD7B10` | 66 | UnwindData |  |
| 572 | `uiter_setString` | `0xD7B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 573 | `uiter_setUTF16BE` | `0xD7B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `uiter_setUTF8` | `0xD7B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `uldn_getContext` | `0xD7B90` | 29 | UnwindData |  |
| 577 | `uldn_getDialectHandling` | `0xD7BC0` | 29 | UnwindData |  |
| 578 | `uldn_getLocale` | `0xD7BF0` | 33 | UnwindData |  |
| 579 | `uldn_keyDisplayName` | `0xD7C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `uldn_keyValueDisplayName` | `0xD7C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 581 | `uldn_languageDisplayName` | `0xD7C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 582 | `uldn_localeDisplayName` | `0xD7C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `uldn_openForContext` | `0xD7C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 585 | `uldn_regionDisplayName` | `0xD7C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `uldn_scriptCodeDisplayName` | `0xD7C80` | 134 | UnwindData |  |
| 587 | `uldn_scriptDisplayName` | `0xD7D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `uldn_variantDisplayName` | `0xD7D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `ulistfmt_closeResult` | `0xD7D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 591 | `ulistfmt_format` | `0xD7D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `ulistfmt_formatStringsToResult` | `0xD7D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `ulistfmt_open` | `0xD7D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `ulistfmt_openForType` | `0xD7D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 595 | `ulistfmt_openResult` | `0xD7D80` | 119 | UnwindData |  |
| 596 | `ulistfmt_resultAsValue` | `0xD7E00` | 23 | UnwindData |  |
| 597 | `uloc_acceptLanguage` | `0xD7E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `uloc_acceptLanguageFromHTTP` | `0xD7E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `uloc_getCharacterOrientation` | `0xD7E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `uloc_getDisplayCountry` | `0xD7E60` | 49 | UnwindData |  |
| 609 | `uloc_getDisplayKeyword` | `0xD7EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 610 | `uloc_getDisplayKeywordValue` | `0xD7EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `uloc_getDisplayLanguage` | `0xD7EC0` | 49 | UnwindData |  |
| 612 | `uloc_getDisplayName` | `0xD7F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 613 | `uloc_getDisplayScript` | `0xD7F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | `uloc_getDisplayVariant` | `0xD7F20` | 49 | UnwindData |  |
| 615 | `uloc_getISO3Country` | `0xD7F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 616 | `uloc_getISO3Language` | `0xD7F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 617 | `uloc_getISOCountries` | `0xD7F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 618 | `uloc_getISOLanguages` | `0xD7F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `uloc_getKeywordValue` | `0xD7FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 620 | `uloc_getLCID` | `0xD7FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 622 | `uloc_getLineOrientation` | `0xD7FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 623 | `uloc_getLocaleForLCID` | `0xD7FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 626 | `uloc_getScript` | `0xD7FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 627 | `uloc_getVariant` | `0xD8000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 628 | `uloc_isRightToLeft` | `0xD8010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 629 | `uloc_minimizeSubtags` | `0xD8020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `uloc_openAvailableByType` | `0xD8030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | `uloc_openKeywords` | `0xD8040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 632 | `uloc_setDefault` | `0xD8050` | 30 | UnwindData |  |
| 635 | `uloc_toLegacyKey` | `0xD8080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 636 | `uloc_toLegacyType` | `0xD8090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 637 | `uloc_toUnicodeLocaleKey` | `0xD80A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `ulocdata_close` | `0xD80B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 641 | `ulocdata_getDelimiter` | `0xD80C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 642 | `ulocdata_getExemplarSet` | `0xD80D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 643 | `ulocdata_getLocaleDisplayPattern` | `0xD80E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `ulocdata_getLocaleSeparator` | `0xD80F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `ulocdata_getMeasurementSystem` | `0xD8100` | 87 | UnwindData |  |
| 646 | `ulocdata_getNoSubstitute` | `0xD8160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 647 | `ulocdata_getPaperSize` | `0xD8170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 648 | `ulocdata_open` | `0xD8180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 649 | `ulocdata_setNoSubstitute` | `0xD8190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `umsg_applyPattern` | `0xD81A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | `umsg_autoQuoteApostrophe` | `0xD81B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `umsg_clone` | `0xD81C0` | 80 | UnwindData |  |
| 654 | `umsg_format` | `0xD8220` | 33 | UnwindData |  |
| 655 | `umsg_getLocale` | `0xD8250` | 40 | UnwindData |  |
| 656 | `umsg_open` | `0xD8280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 657 | `umsg_parse` | `0xD8290` | 34 | UnwindData |  |
| 658 | `umsg_setLocale` | `0xD82C0` | 126 | UnwindData |  |
| 659 | `umsg_toPattern` | `0xD8350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | `umsg_vformat` | `0xD8360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 661 | `umsg_vparse` | `0xD8370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 662 | `umutablecptrie_buildImmutable` | `0xD8380` | 22 | UnwindData |  |
| 663 | `umutablecptrie_clone` | `0xD83A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `umutablecptrie_close` | `0xD83B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `umutablecptrie_fromUCPMap` | `0xD83C0` | 38 | UnwindData |  |
| 666 | `umutablecptrie_fromUCPTrie` | `0xD83F0` | 38 | UnwindData |  |
| 667 | `umutablecptrie_get` | `0xD8420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 668 | `umutablecptrie_getRange` | `0xD8430` | 68 | UnwindData |  |
| 669 | `umutablecptrie_open` | `0xD8480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 670 | `umutablecptrie_set` | `0xD8490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `umutablecptrie_setRange` | `0xD84A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 672 | `unorm2_append` | `0xD84B0` | 51 | UnwindData |  |
| 674 | `unorm2_composePair` | `0xD84F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 676 | `unorm2_getDecomposition` | `0xD8510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `unorm2_getNFKCCasefoldInstance` | `0xD8520` | 28 | UnwindData |  |
| 681 | `unorm2_getNFKCInstance` | `0xD8550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 682 | `unorm2_getNFKDInstance` | `0xD8560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `unorm2_getRawDecomposition` | `0xD8570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 689 | `unorm2_normalizeSecondAndAppend` | `0xD8580` | 51 | UnwindData |  |
| 690 | `unorm2_openFiltered` | `0xD85C0` | 119 | UnwindData |  |
| 691 | `unorm2_quickCheck` | `0xD8640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 692 | `unorm2_spanQuickCheckYes` | `0xD8650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 693 | `unorm_compare` | `0xD8660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 694 | `unum_applyPattern` | `0xD8670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 695 | `unum_clone` | `0xD8680` | 139 | UnwindData |  |
| 698 | `unum_format` | `0xD8720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 699 | `unum_formatDecimal` | `0xD8730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 700 | `unum_formatDouble` | `0xD8740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 701 | `unum_formatDoubleCurrency` | `0xD8750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | `unum_formatDoubleForFields` | `0xD8760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `unum_formatInt64` | `0xD8770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `unum_formatUFormattable` | `0xD8780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `unum_getAttribute` | `0xD8790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `unum_getContext` | `0xD87A0` | 32 | UnwindData |  |
| 708 | `unum_getDoubleAttribute` | `0xD87D0` | 85 | UnwindData |  |
| 711 | `unum_getTextAttribute` | `0xD8830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | `unum_parse` | `0xD8840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `unum_parseDecimal` | `0xD8850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 715 | `unum_parseDouble` | `0xD8860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `unum_parseDoubleCurrency` | `0xD8870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 717 | `unum_parseInt64` | `0xD8880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 718 | `unum_parseToUFormattable` | `0xD8890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 720 | `unum_setContext` | `0xD88A0` | 31 | UnwindData |  |
| 721 | `unum_setDoubleAttribute` | `0xD88D0` | 88 | UnwindData |  |
| 722 | `unum_setSymbol` | `0xD8930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | `unum_setTextAttribute` | `0xD8940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 725 | `unumf_close` | `0xD8950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 726 | `unumf_closeResult` | `0xD8960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 727 | `unumf_formatDecimal` | `0xD8970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `unumf_formatDouble` | `0xD8980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 729 | `unumf_formatInt` | `0xD8990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `unumf_openForSkeletonAndLocale` | `0xD89A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 731 | `unumf_openForSkeletonAndLocaleWithError` | `0xD89B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `unumf_openResult` | `0xD89C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 733 | `unumf_resultAsValue` | `0xD89D0` | 23 | UnwindData |  |
| 744 | `unumrf_resultAsValue` | `0xD89D0` | 23 | UnwindData |  |
| 734 | `unumf_resultGetAllFieldPositions` | `0xD89F0` | 84 | UnwindData |  |
| 735 | `unumf_resultNextFieldPosition` | `0xD8A50` | 124 | UnwindData |  |
| 736 | `unumf_resultToDecimalNumber` | `0xD8AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `unumrf_resultGetFirstDecimalNumber` | `0xD8AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `unumf_resultToString` | `0xD8AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 738 | `unumrf_close` | `0xD8B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 739 | `unumrf_closeResult` | `0xD8B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `unumrf_formatDecimalRange` | `0xD8B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `unumrf_formatDoubleRange` | `0xD8B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `unumrf_openForSkeletonWithCollapseAndIdentityFallback` | `0xD8B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 743 | `unumrf_openResult` | `0xD8B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 746 | `unumrf_resultGetIdentityResult` | `0xD8B60` | 33 | UnwindData |  |
| 747 | `unumrf_resultGetSecondDecimalNumber` | `0xD8B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `unumsys_getDescription` | `0xD8BA0` | 132 | UnwindData |  |
| 751 | `unumsys_getRadix` | `0xD8C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | `unumsys_isAlgorithmic` | `0xD8C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 754 | `unumsys_openAvailableNames` | `0xD8C50` | 30 | UnwindData |  |
| 755 | `unumsys_openByName` | `0xD8C80` | 21 | UnwindData |  |
| 757 | `uplrules_getKeywords` | `0xD8CA0` | 83 | UnwindData |  |
| 758 | `uplrules_open` | `0xD8D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `uplrules_openForType` | `0xD8D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 760 | `uplrules_select` | `0xD8D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `uplrules_selectFormatted` | `0xD8D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 762 | `uregex_appendReplacement` | `0xD8D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `uregex_appendReplacementUText` | `0xD8D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | `uregex_appendTail` | `0xD8D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `uregex_appendTailUText` | `0xD8D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `uregex_clone` | `0xD8D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `uregex_find` | `0xD8DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `uregex_find64` | `0xD8DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `uregex_flags` | `0xD8DC0` | 33 | UnwindData |  |
| 774 | `uregex_getFindProgressCallback` | `0xD8DF0` | 45 | UnwindData |  |
| 775 | `uregex_getMatchCallback` | `0xD8E30` | 45 | UnwindData |  |
| 776 | `uregex_getStackLimit` | `0xD8E70` | 41 | UnwindData |  |
| 777 | `uregex_getText` | `0xD8EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 778 | `uregex_getTimeLimit` | `0xD8EB0` | 41 | UnwindData |  |
| 779 | `uregex_getUText` | `0xD8EE0` | 42 | UnwindData |  |
| 780 | `uregex_group` | `0xD8F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `uregex_groupCount` | `0xD8F20` | 44 | UnwindData |  |
| 782 | `uregex_groupNumberFromCName` | `0xD8F60` | 57 | UnwindData |  |
| 783 | `uregex_groupNumberFromName` | `0xD8FA0` | 116 | UnwindData |  |
| 784 | `uregex_groupUText` | `0xD9020` | 87 | UnwindData |  |
| 785 | `uregex_hasAnchoringBounds` | `0xD9080` | 36 | UnwindData |  |
| 786 | `uregex_hasTransparentBounds` | `0xD90B0` | 36 | UnwindData |  |
| 787 | `uregex_hitEnd` | `0xD90E0` | 38 | UnwindData |  |
| 788 | `uregex_lookingAt` | `0xD9110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `uregex_lookingAt64` | `0xD9120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | `uregex_matches64` | `0xD9130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 792 | `uregex_open` | `0xD9140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `uregex_openC` | `0xD9150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 795 | `uregex_pattern` | `0xD9160` | 45 | UnwindData |  |
| 796 | `uregex_patternUText` | `0xD91A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `uregex_refreshUText` | `0xD91B0` | 36 | UnwindData |  |
| 798 | `uregex_regionEnd` | `0xD91E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `uregex_regionEnd64` | `0xD91E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 800 | `uregex_regionStart` | `0xD91F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | `uregex_regionStart64` | `0xD91F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `uregex_replaceAll` | `0xD9200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 804 | `uregex_replaceFirst` | `0xD9210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `uregex_replaceFirstUText` | `0xD9220` | 71 | UnwindData |  |
| 806 | `uregex_requireEnd` | `0xD9270` | 38 | UnwindData |  |
| 807 | `uregex_reset` | `0xD92A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 808 | `uregex_reset64` | `0xD92B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 809 | `uregex_setFindProgressCallback` | `0xD92C0` | 45 | UnwindData |  |
| 810 | `uregex_setMatchCallback` | `0xD9300` | 45 | UnwindData |  |
| 811 | `uregex_setRegion` | `0xD9340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 812 | `uregex_setRegion64` | `0xD9360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `uregex_setRegionAndStart` | `0xD9370` | 52 | UnwindData |  |
| 814 | `uregex_setStackLimit` | `0xD93B0` | 36 | UnwindData |  |
| 816 | `uregex_setTimeLimit` | `0xD93E0` | 36 | UnwindData |  |
| 817 | `uregex_setUText` | `0xD9410` | 97 | UnwindData |  |
| 818 | `uregex_split` | `0xD9480` | 130 | UnwindData |  |
| 819 | `uregex_splitUText` | `0xD9510` | 34 | UnwindData |  |
| 822 | `uregex_useAnchoringBounds` | `0xD9540` | 36 | UnwindData |  |
| 823 | `uregex_useTransparentBounds` | `0xD9570` | 36 | UnwindData |  |
| 824 | `uregion_areEqual` | `0xD95A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `uregion_contains` | `0xD95B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 826 | `uregion_getAvailable` | `0xD95C0` | 115 | UnwindData |  |
| 827 | `uregion_getContainedRegions` | `0xD9640` | 30 | UnwindData |  |
| 828 | `uregion_getContainedRegionsOfType` | `0xD9670` | 30 | UnwindData |  |
| 829 | `uregion_getContainingRegion` | `0xD96A0` | 49 | UnwindData |  |
| 830 | `uregion_getContainingRegionOfType` | `0xD96E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `uregion_getNumericCode` | `0xD96F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 832 | `uregion_getPreferredValues` | `0xD9700` | 30 | UnwindData |  |
| 834 | `uregion_getRegionFromCode` | `0xD9730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 835 | `uregion_getRegionFromNumericCode` | `0xD9740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 836 | `uregion_getType` | `0xD9750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `ureldatefmt_closeResult` | `0xD9760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 839 | `ureldatefmt_combineDateAndTime` | `0xD9770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | `ureldatefmt_format` | `0xD9780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 841 | `ureldatefmt_formatNumeric` | `0xD9790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `ureldatefmt_formatNumericToResult` | `0xD97A0` | 124 | UnwindData |  |
| 843 | `ureldatefmt_formatToResult` | `0xD9830` | 124 | UnwindData |  |
| 844 | `ureldatefmt_open` | `0xD98C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `ureldatefmt_openResult` | `0xD98D0` | 119 | UnwindData |  |
| 846 | `ureldatefmt_resultAsValue` | `0xD9950` | 23 | UnwindData |  |
| 848 | `ures_getBinary` | `0xD9970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `ures_getByIndex` | `0xD9980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | `ures_getByKey` | `0xD9990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `ures_getInt` | `0xD99A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `ures_getIntVector` | `0xD99B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `ures_getKey` | `0xD99C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 854 | `ures_getLocaleByType` | `0xD99D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 855 | `ures_getNextResource` | `0xD99E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 856 | `ures_getNextString` | `0xD99F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 857 | `ures_getSize` | `0xD9A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 858 | `ures_getString` | `0xD9A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 860 | `ures_getStringByKey` | `0xD9A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 861 | `ures_getType` | `0xD9A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 862 | `ures_getUInt` | `0xD9A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `ures_getUTF8String` | `0xD9A50` | 90 | UnwindData |  |
| 864 | `ures_getUTF8StringByIndex` | `0xD9AB0` | 76 | UnwindData |  |
| 865 | `ures_getUTF8StringByKey` | `0xD9B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `ures_getVersion` | `0xD9B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `ures_hasNext` | `0xD9B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `ures_openAvailableLocales` | `0xD9B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | `ures_openDirect` | `0xD9B50` | 34 | UnwindData |  |
| 871 | `ures_openU` | `0xD9B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `ures_resetIterator` | `0xD9B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `uscript_breaksBetweenLetters` | `0xD9BB0` | 20 | UnwindData |  |
| 874 | `uscript_getCode` | `0xD9BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `uscript_getName` | `0xD9BE0` | 84 | UnwindData |  |
| 876 | `uscript_getSampleString` | `0xD9C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `uscript_getScript` | `0xD9C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 878 | `uscript_getScriptExtensions` | `0xD9C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `uscript_getShortName` | `0xD9C70` | 83 | UnwindData |  |
| 880 | `uscript_getUsage` | `0xD9CD0` | 21 | UnwindData |  |
| 881 | `uscript_hasScript` | `0xD9CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 882 | `uscript_isCased` | `0xD9D00` | 20 | UnwindData |  |
| 883 | `uscript_isRightToLeft` | `0xD9D20` | 20 | UnwindData |  |
| 886 | `usearch_following` | `0xD9D40` | 72 | UnwindData |  |
| 887 | `usearch_getAttribute` | `0xD9D90` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 888 | `usearch_getBreakIterator` | `0xD9DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `usearch_getCollator` | `0xD9E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 891 | `usearch_getMatchedStart` | `0xD9E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `usearch_getMatchedText` | `0xD9E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 893 | `usearch_getOffset` | `0xD9E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `usearch_getPattern` | `0xD9E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `usearch_getText` | `0xD9E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `usearch_next` | `0xD9EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 898 | `usearch_open` | `0xD9EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 900 | `usearch_preceding` | `0xD9ED0` | 72 | UnwindData |  |
| 901 | `usearch_previous` | `0xD9F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 902 | `usearch_reset` | `0xD9F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `usearch_setAttribute` | `0xD9F40` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `usearch_setBreakIterator` | `0xD9FB0` | 57 | UnwindData |  |
| 905 | `usearch_setCollator` | `0xD9FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 906 | `usearch_setOffset` | `0xDA000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `uset_add` | `0xDA010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | `uset_addAll` | `0xDA020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | `uset_addAllCodePoints` | `0xDA030` | 77 | UnwindData |  |
| 913 | `uset_addString` | `0xDA090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | `uset_applyIntPropertyValue` | `0xDA0A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 915 | `uset_applyPattern` | `0xDA0B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 916 | `uset_applyPropertyAlias` | `0xDA0C0` | 143 | UnwindData |  |
| 917 | `uset_charAt` | `0xDA160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 918 | `uset_clear` | `0xDA170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `uset_clone` | `0xDA180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `uset_cloneAsThawed` | `0xDA190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 921 | `uset_close` | `0xDA1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 922 | `uset_closeOver` | `0xDA1B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 923 | `uset_compact` | `0xDA1C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 924 | `uset_complement` | `0xDA1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 925 | `uset_complementAll` | `0xDA1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `uset_complementAllCodePoints` | `0xDA1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `uset_complementRange` | `0xDA200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | `uset_complementString` | `0xDA210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `uset_contains` | `0xDA220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | `uset_containsAll` | `0xDA230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 931 | `uset_containsAllCodePoints` | `0xDA240` | 94 | UnwindData |  |
| 932 | `uset_containsNone` | `0xDA2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 933 | `uset_containsRange` | `0xDA2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 934 | `uset_containsSome` | `0xDA2D0` | 20 | UnwindData |  |
| 935 | `uset_containsString` | `0xDA2F0` | 94 | UnwindData |  |
| 936 | `uset_equals` | `0xDA360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 937 | `uset_freeze` | `0xDA380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 938 | `uset_getItem` | `0xDA390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 939 | `uset_getItemCount` | `0xDA3A0` | 29 | UnwindData |  |
| 940 | `uset_getRangeCount` | `0xDA3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 941 | `uset_getSerializedRange` | `0xDA3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `uset_getSerializedRangeCount` | `0xDA3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 943 | `uset_getSerializedSet` | `0xDA400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 944 | `uset_hasStrings` | `0xDA410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 945 | `uset_indexOf` | `0xDA420` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 946 | `uset_isEmpty` | `0xDA470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 947 | `uset_isFrozen` | `0xDA480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 948 | `uset_open` | `0xDA490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 949 | `uset_openEmpty` | `0xDA4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 950 | `uset_openPattern` | `0xDA4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 951 | `uset_openPatternOptions` | `0xDA4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 952 | `uset_remove` | `0xDA4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 953 | `uset_removeAll` | `0xDA4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 954 | `uset_removeAllCodePoints` | `0xDA4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `uset_removeAllStrings` | `0xDA500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 956 | `uset_removeRange` | `0xDA510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `uset_removeString` | `0xDA520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 958 | `uset_resemblesPattern` | `0xDA530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 959 | `uset_retain` | `0xDA540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 960 | `uset_retainAll` | `0xDA550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 961 | `uset_retainAllCodePoints` | `0xDA560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 962 | `uset_retainString` | `0xDA570` | 87 | UnwindData |  |
| 963 | `uset_serialize` | `0xDA5D0` | 27 | UnwindData |  |
| 964 | `uset_serializedContains` | `0xDA600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 965 | `uset_set` | `0xDA610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 966 | `uset_setSerializedToOne` | `0xDA620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 967 | `uset_size` | `0xDA630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 968 | `uset_span` | `0xDA640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 969 | `uset_spanBack` | `0xDA650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 970 | `uset_spanBackUTF8` | `0xDA660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 971 | `uset_spanUTF8` | `0xDA670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `uset_toPattern` | `0xDA680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `uspoof_areConfusable` | `0xDA690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 974 | `uspoof_areConfusableUTF8` | `0xDA6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `uspoof_check` | `0xDA6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `uspoof_check2` | `0xDA6D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `uspoof_check2UTF8` | `0xDA6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `uspoof_checkUTF8` | `0xDA6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 979 | `uspoof_clone` | `0xDA710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `uspoof_close` | `0xDA720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `uspoof_closeCheckResult` | `0xDA730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 982 | `uspoof_getAllowedChars` | `0xDA740` | 29 | UnwindData |  |
| 983 | `uspoof_getAllowedLocales` | `0xDA770` | 29 | UnwindData |  |
| 984 | `uspoof_getCheckResultChecks` | `0xDA7A0` | 27 | UnwindData |  |
| 985 | `uspoof_getCheckResultNumerics` | `0xDA7D0` | 30 | UnwindData |  |
| 986 | `uspoof_getCheckResultRestrictionLevel` | `0xDA800` | 33 | UnwindData |  |
| 987 | `uspoof_getChecks` | `0xDA830` | 28 | UnwindData |  |
| 988 | `uspoof_getInclusionSet` | `0xDA860` | 39 | UnwindData |  |
| 989 | `uspoof_getRecommendedSet` | `0xDA890` | 39 | UnwindData |  |
| 990 | `uspoof_getRestrictionLevel` | `0xDA8C0` | 40 | UnwindData |  |
| 991 | `uspoof_getSkeleton` | `0xDA8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `uspoof_getSkeletonUTF8` | `0xDA900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `uspoof_open` | `0xDA910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 994 | `uspoof_openCheckResult` | `0xDA920` | 79 | UnwindData |  |
| 995 | `uspoof_openFromSerialized` | `0xDA980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `uspoof_openFromSource` | `0xDA990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 997 | `uspoof_serialize` | `0xDA9A0` | 83 | UnwindData |  |
| 998 | `uspoof_setAllowedChars` | `0xDAA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `uspoof_setAllowedLocales` | `0xDAA10` | 43 | UnwindData |  |
| 1000 | `uspoof_setChecks` | `0xDAA50` | 50 | UnwindData |  |
| 1001 | `uspoof_setRestrictionLevel` | `0xDAA90` | 41 | UnwindData |  |
| 1002 | `usprep_close` | `0xDAAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `usprep_open` | `0xDAAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `usprep_openByType` | `0xDAAE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `usprep_prepare` | `0xDAB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `utext_clone` | `0xDAB30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `utext_copy` | `0xDAB40` | 68 | UnwindData |  |
| 1010 | `utext_current32` | `0xDAB90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `utext_equals` | `0xDABA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | `utext_freeze` | `0xDABB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `utext_getNativeIndex` | `0xDABC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `utext_getPreviousNativeIndex` | `0xDABD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `utext_hasMetaData` | `0xDABE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `utext_isLengthExpensive` | `0xDABF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `utext_isWritable` | `0xDAC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `utext_moveIndex32` | `0xDAC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `utext_next32` | `0xDAC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `utext_next32From` | `0xDAC30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `utext_previous32` | `0xDAC40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `utext_previous32From` | `0xDAC50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `utext_replace` | `0xDAC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1028 | `utext_setNativeIndex` | `0xDAC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1029 | `utext_setup` | `0xDAC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1030 | `utf8_appendCharSafeBody` | `0xDAC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1031 | `utf8_back1SafeBody` | `0xDACA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `utf8_nextCharSafeBody` | `0xDACB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1033 | `utf8_prevCharSafeBody` | `0xDACC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1034 | `utmscale_fromInt64` | `0xDACD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `utmscale_getTimeScaleValue` | `0xDACE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `utmscale_toInt64` | `0xDAD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `utrace_format` | `0xDAD30` | 30 | UnwindData |  |
| 1038 | `utrace_functionName` | `0xDAD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `utrace_getFunctions` | `0xDAD70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1040 | `utrace_getLevel` | `0xDADA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | `utrace_setFunctions` | `0xDADB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1042 | `utrace_setLevel` | `0xDADE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1043 | `utrace_vformat` | `0xDAE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1044 | `utrans_clone` | `0xDAE10` | 78 | UnwindData |  |
| 1046 | `utrans_countAvailableIDs` | `0xDAE70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1047 | `utrans_getSourceSet` | `0xDAE80` | 98 | UnwindData |  |
| 1048 | `utrans_getUnicodeID` | `0xDAEF0` | 61 | UnwindData |  |
| 1049 | `utrans_openIDs` | `0xDAF40` | 132 | UnwindData |  |
| 1050 | `utrans_openInverse` | `0xDAFD0` | 75 | UnwindData |  |
| 1051 | `utrans_openU` | `0xDB030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `utrans_register` | `0xDB040` | 25 | UnwindData |  |
| 1053 | `utrans_setFilter` | `0xDB060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `utrans_toRules` | `0xDB070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1055 | `utrans_trans` | `0xDB080` | 115 | UnwindData |  |
| 1056 | `utrans_transIncremental` | `0xDB100` | 102 | UnwindData |  |
| 1057 | `utrans_transIncrementalUChars` | `0xDB170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `utrans_transUChars` | `0xDB180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `utrans_unregisterID` | `0xDB190` | 77 | UnwindData |  |
| 4 | `SortCloseHandle` | `0xDDDE0` | 20 | UnwindData |  |
| 5 | `SortGetHandle` | `0xDDE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SortGetSearchKey` | `0xDDE20` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CloseDefaultICUGroupingLetters` | `0xDE080` | 82 | UnwindData |  |
| 2 | `GetDefaultICUGroupingLetters` | `0xDE0E0` | 970 | UnwindData |  |
| 3 | `GetICUGroupingLetter` | `0xDE4B0` | 907 | UnwindData |  |
