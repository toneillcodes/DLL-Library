# Binary Specification: ucrtbase_enclave.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ucrtbase_enclave.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `36612bd99939a340d85d0d23789e11e1089ac84d2c722f66b59b2b45fdfc4c31`
* **Total Exported Functions:** 786

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 487 | `cos` | `0x1110` | 1,402 | UnwindData |  |
| 488 | `cosf` | `0x1950` | 543 | UnwindData |  |
| 523 | `exp` | `0x1B80` | 1,045 | UnwindData |  |
| 527 | `expf` | `0x2120` | 346 | UnwindData |  |
| 553 | `fmod` | `0x2370` | 692 | UnwindData |  |
| 605 | `log` | `0x2640` | 1,323 | UnwindData |  |
| 606 | `log10` | `0x2B80` | 1,451 | UnwindData |  |
| 607 | `log10f` | `0x3350` | 504 | UnwindData |  |
| 617 | `logf` | `0x3720` | 460 | UnwindData |  |
| 661 | `powf` | `0x3900` | 3,766 | UnwindData |  |
| 668 | `remainder` | `0x47D0` | 1,000 | UnwindData |  |
| 678 | `roundf` | `0x5380` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 677 | `round` | `0x53D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 688 | `sin` | `0x5450` | 1,386 | UnwindData |  |
| 689 | `sinf` | `0x5D40` | 845 | UnwindData |  |
| 727 | `tan` | `0x6650` | 1,459 | UnwindData |  |
| 728 | `tanf` | `0x7120` | 730 | UnwindData |  |
| 4 | `_CreateFrameInfo` | `0x7EF0` | 58 | UnwindData |  |
| 10 | `_FindAndUnlinkFrame` | `0x7F30` | 83 | UnwindData |  |
| 11 | `_GetImageBase` | `0x7F90` | 18 | UnwindData |  |
| 12 | `_GetThrowImageBase` | `0x7FB0` | 18 | UnwindData |  |
| 17 | `_SetImageBase` | `0x7FD0` | 24 | UnwindData |  |
| 18 | `_SetThrowImageBase` | `0x7FF0` | 24 | UnwindData |  |
| 27 | `__CxxFrameHandler` | `0x8010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `__CxxFrameHandler2` | `0x8010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `__CxxFrameHandler3` | `0x8020` | 134 | UnwindData |  |
| 30 | `__CxxFrameHandler4` | `0x80B0` | 191 | UnwindData |  |
| 5 | `_CxxThrowException` | `0x8180` | 166 | UnwindData |  |
| 34 | `__DestructExceptionObject` | `0x8230` | 108 | UnwindData |  |
| 13 | `_IsExceptionObjectToBeDestroyed` | `0x82B0` | 47 | UnwindData |  |
| 19 | `_SetWinRTOutOfMemoryExceptionCallback` | `0x82F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `__AdjustPointer` | `0x8300` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `__FrameUnwindFilter` | `0x8330` | 102 | UnwindData |  |
| 36 | `__GetPlatformExceptionInfo` | `0x83A0` | 91 | UnwindData |  |
| 48 | `__current_exception` | `0x8410` | 18 | UnwindData |  |
| 49 | `__current_exception_context` | `0x8430` | 18 | UnwindData |  |
| 61 | `__processing_throw` | `0x8450` | 18 | UnwindData |  |
| 68 | `__std_terminate` | `0x8470` | 10 | UnwindData |  |
| 202 | `_is_exception_typeof` | `0x8480` | 165 | UnwindData |  |
| 21 | `__BuildCatchObject` | `0xB620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `__BuildCatchObjectHelper` | `0xB630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__TypeMatch` | `0xB640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `__C_specific_handler` | `0xB650` | 535 | UnwindData |  |
| 24 | `__C_specific_handler_noexcept` | `0xB870` | 75 | UnwindData |  |
| 25 | `__CxxDetectRethrow` | `0xB8D0` | 68 | UnwindData |  |
| 26 | `__CxxExceptionFilter` | `0xB920` | 503 | UnwindData |  |
| 31 | `__CxxQueryExceptionSize` | `0xBB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `__CxxRegisterExceptionObject` | `0xBB30` | 172 | UnwindData |  |
| 33 | `__CxxUnregisterExceptionObject` | `0xBBF0` | 294 | UnwindData |  |
| 37 | `__NLG_Dispatch2` | `0xBD50` | 1 | UnwindData |  |
| 38 | `__NLG_Return2` | `0xBD60` | 1 | UnwindData |  |
| 39 | `__RTCastToVoid` | `0xC380` | 93 | UnwindData |  |
| 40 | `__RTDynamicCast` | `0xC3F0` | 366 | UnwindData |  |
| 41 | `__RTtypeid` | `0xC570` | 180 | UnwindData |  |
| 66 | `__std_exception_copy` | `0xC640` | 141 | UnwindData |  |
| 67 | `__std_exception_destroy` | `0xC6E0` | 37 | UnwindData |  |
| 69 | `__std_type_info_compare` | `0xC730` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `__std_type_info_destroy_list` | `0xC760` | 42 | UnwindData |  |
| 71 | `__std_type_info_hash` | `0xC790` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `__std_type_info_name` | `0xC7D0` | 277 | UnwindData |  |
| 91 | `__uncaught_exception` | `0xC8F0` | 30 | UnwindData |  |
| 92 | `__uncaught_exceptions` | `0xC920` | 27 | UnwindData |  |
| 185 | `_get_purecall_handler` | `0xC950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `_purecall` | `0xC960` | 25 | UnwindData |  |
| 298 | `_set_purecall_handler` | `0xC980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `_get_unexpected` | `0xC9A0` | 34 | UnwindData |  |
| 686 | `set_unexpected` | `0xC9D0` | 44 | UnwindData |  |
| 743 | `unexpected` | `0xCA10` | 29 | UnwindData |  |
| 255 | `_local_unwind` | `0xCA40` | 41 | UnwindData |  |
| 299 | `_set_se_translator` | `0xCA70` | 45 | UnwindData |  |
| 618 | `longjmp` | `0xCAB0` | 40 | UnwindData |  |
| 64 | `__report_gsfailure` | `0xD1D0` | 19,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `_atodbl` | `0x11E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `_atodbl_l` | `0x11E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `_atof_l` | `0x11E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `_atoflt` | `0x11E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `_atoflt_l` | `0x11E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `_wtof` | `0x11E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `_wtof_l` | `0x11E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `atof` | `0x11E80` | 3,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `_atoldbl` | `0x12B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `_atoldbl_l` | `0x12BA0` | 234 | UnwindData |  |
| 111 | `_atoi64` | `0x144A0` | 75 | UnwindData |  |
| 427 | `atoll` | `0x144A0` | 75 | UnwindData |  |
| 112 | `_atoi64_l` | `0x14500` | 76 | UnwindData |  |
| 117 | `_atoll_l` | `0x14500` | 76 | UnwindData |  |
| 113 | `_atoi_l` | `0x14560` | 74 | UnwindData |  |
| 114 | `_atol_l` | `0x14560` | 74 | UnwindData |  |
| 394 | `_wtoi` | `0x145B0` | 73 | UnwindData |  |
| 398 | `_wtol` | `0x145B0` | 73 | UnwindData |  |
| 395 | `_wtoi64` | `0x14600` | 75 | UnwindData |  |
| 400 | `_wtoll` | `0x14600` | 75 | UnwindData |  |
| 396 | `_wtoi64_l` | `0x14660` | 76 | UnwindData |  |
| 401 | `_wtoll_l` | `0x14660` | 76 | UnwindData |  |
| 397 | `_wtoi_l` | `0x146C0` | 74 | UnwindData |  |
| 399 | `_wtol_l` | `0x146C0` | 74 | UnwindData |  |
| 425 | `atoi` | `0x14710` | 73 | UnwindData |  |
| 426 | `atol` | `0x14710` | 73 | UnwindData |  |
| 431 | `c16rtomb` | `0x14810` | 64 | UnwindData |  |
| 432 | `c32rtomb` | `0x14910` | 62 | UnwindData |  |
| 149 | `_ecvt` | `0x17420` | 67 | UnwindData |  |
| 150 | `_ecvt_s` | `0x17470` | 97 | UnwindData |  |
| 156 | `_fcvt` | `0x174E0` | 67 | UnwindData |  |
| 157 | `_fcvt_s` | `0x17530` | 97 | UnwindData |  |
| 177 | `_gcvt` | `0x177F0` | 44 | UnwindData |  |
| 178 | `_gcvt_s` | `0x17830` | 65 | UnwindData |  |
| 207 | `_isctype` | `0x17880` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `_isctype_l` | `0x178C0` | 105 | UnwindData |  |
| 225 | `_iswctype_l` | `0x17930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `iswctype` | `0x17940` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 626 | `mblen` | `0x17AF0` | 60 | UnwindData |  |
| 628 | `mbrtoc16` | `0x17C40` | 67 | UnwindData |  |
| 629 | `mbrtoc32` | `0x17EB0` | 67 | UnwindData |  |
| 430 | `btowc` | `0x18630` | 124 | UnwindData |  |
| 627 | `mbrlen` | `0x186C0` | 96 | UnwindData |  |
| 630 | `mbrtowc` | `0x18730` | 134 | UnwindData |  |
| 631 | `mbsrtowcs` | `0x187C0` | 67 | UnwindData |  |
| 632 | `mbsrtowcs_s` | `0x18810` | 97 | UnwindData |  |
| 633 | `mbstowcs` | `0x18BE0` | 62 | UnwindData |  |
| 634 | `mbstowcs_s` | `0x18C30` | 78 | UnwindData |  |
| 635 | `mbtowc` | `0x18E50` | 60 | UnwindData |  |
| 318 | `_strtod_l` | `0x191E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `_strtold_l` | `0x191E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `_strtof_l` | `0x191F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `_wcstod_l` | `0x19200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `_wcstold_l` | `0x19200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `_wcstof_l` | `0x19210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 715 | `strtod` | `0x19220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 721 | `strtold` | `0x19220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `strtof` | `0x19230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `wcstod` | `0x19240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 772 | `wcstold` | `0x19240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `wcstof` | `0x19250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `_strtoi64` | `0x19260` | 82 | UnwindData |  |
| 717 | `strtoimax` | `0x19260` | 82 | UnwindData |  |
| 722 | `strtoll` | `0x19260` | 82 | UnwindData |  |
| 321 | `_strtoi64_l` | `0x192C0` | 83 | UnwindData |  |
| 322 | `_strtoimax_l` | `0x192C0` | 83 | UnwindData |  |
| 325 | `_strtoll_l` | `0x192C0` | 83 | UnwindData |  |
| 323 | `_strtol_l` | `0x19320` | 81 | UnwindData |  |
| 326 | `_strtoui64` | `0x19380` | 82 | UnwindData |  |
| 724 | `strtoull` | `0x19380` | 82 | UnwindData |  |
| 725 | `strtoumax` | `0x19380` | 82 | UnwindData |  |
| 327 | `_strtoui64_l` | `0x193E0` | 83 | UnwindData |  |
| 329 | `_strtoull_l` | `0x193E0` | 83 | UnwindData |  |
| 330 | `_strtoumax_l` | `0x193E0` | 83 | UnwindData |  |
| 328 | `_strtoul_l` | `0x19440` | 81 | UnwindData |  |
| 371 | `_wcstoi64` | `0x194A0` | 82 | UnwindData |  |
| 768 | `wcstoimax` | `0x194A0` | 82 | UnwindData |  |
| 773 | `wcstoll` | `0x194A0` | 82 | UnwindData |  |
| 372 | `_wcstoi64_l` | `0x19500` | 83 | UnwindData |  |
| 373 | `_wcstoimax_l` | `0x19500` | 83 | UnwindData |  |
| 376 | `_wcstoll_l` | `0x19500` | 83 | UnwindData |  |
| 374 | `_wcstol_l` | `0x19560` | 81 | UnwindData |  |
| 379 | `_wcstoui64` | `0x195C0` | 82 | UnwindData |  |
| 777 | `wcstoull` | `0x195C0` | 82 | UnwindData |  |
| 778 | `wcstoumax` | `0x195C0` | 82 | UnwindData |  |
| 380 | `_wcstoui64_l` | `0x19620` | 83 | UnwindData |  |
| 382 | `_wcstoull_l` | `0x19620` | 83 | UnwindData |  |
| 383 | `_wcstoumax_l` | `0x19620` | 83 | UnwindData |  |
| 381 | `_wcstoul_l` | `0x19680` | 81 | UnwindData |  |
| 720 | `strtol` | `0x196E0` | 80 | UnwindData |  |
| 723 | `strtoul` | `0x19740` | 80 | UnwindData |  |
| 771 | `wcstol` | `0x197A0` | 80 | UnwindData |  |
| 776 | `wcstoul` | `0x19800` | 80 | UnwindData |  |
| 336 | `_swab` | `0x19860` | 89 | UnwindData |  |
| 337 | `_tolower` | `0x198C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `_tolower_l` | `0x198D0` | 142 | UnwindData |  |
| 339 | `_toupper` | `0x19970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `_toupper_l` | `0x19980` | 142 | UnwindData |  |
| 735 | `tolower` | `0x19A20` | 183 | UnwindData |  |
| 736 | `toupper` | `0x19AE0` | 183 | UnwindData |  |
| 341 | `_towlower_l` | `0x19BA0` | 142 | UnwindData |  |
| 738 | `towlower` | `0x19C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `_towupper_l` | `0x19C50` | 142 | UnwindData |  |
| 739 | `towupper` | `0x19CF0` | 1,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 744 | `wcrtomb` | `0x1A300` | 58 | UnwindData |  |
| 745 | `wcrtomb_s` | `0x1A340` | 78 | UnwindData |  |
| 762 | `wcsrtombs` | `0x1A3A0` | 67 | UnwindData |  |
| 763 | `wcsrtombs_s` | `0x1A3F0` | 265 | UnwindData |  |
| 780 | `wctob` | `0x1A500` | 168 | UnwindData |  |
| 377 | `_wcstombs_l` | `0x1A8C0` | 63 | UnwindData |  |
| 378 | `_wcstombs_s_l` | `0x1A910` | 84 | UnwindData |  |
| 774 | `wcstombs` | `0x1A970` | 62 | UnwindData |  |
| 775 | `wcstombs_s` | `0x1A9C0` | 78 | UnwindData |  |
| 389 | `_wctomb_l` | `0x1AC30` | 313 | UnwindData |  |
| 390 | `_wctomb_s_l` | `0x1AD70` | 71 | UnwindData |  |
| 781 | `wctomb` | `0x1ADC0` | 115 | UnwindData |  |
| 782 | `wctomb_s` | `0x1AE40` | 65 | UnwindData |  |
| 737 | `towctrans` | `0x1AE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 783 | `wctrans` | `0x1AEB0` | 96 | UnwindData |  |
| 784 | `wctype` | `0x1AF20` | 96 | UnwindData |  |
| 192 | `_i64toa` | `0x1B4A0` | 49 | UnwindData |  |
| 193 | `_i64toa_s` | `0x1B4E0` | 33 | UnwindData |  |
| 194 | `_i64tow` | `0x1B510` | 49 | UnwindData |  |
| 195 | `_i64tow_s` | `0x1B550` | 33 | UnwindData |  |
| 235 | `_itoa` | `0x1B580` | 48 | UnwindData |  |
| 263 | `_ltoa` | `0x1B580` | 48 | UnwindData |  |
| 236 | `_itoa_s` | `0x1B5C0` | 32 | UnwindData |  |
| 264 | `_ltoa_s` | `0x1B5C0` | 32 | UnwindData |  |
| 237 | `_itow` | `0x1B5F0` | 48 | UnwindData |  |
| 265 | `_ltow` | `0x1B5F0` | 48 | UnwindData |  |
| 238 | `_itow_s` | `0x1B630` | 32 | UnwindData |  |
| 266 | `_ltow_s` | `0x1B630` | 32 | UnwindData |  |
| 343 | `_ui64toa` | `0x1B660` | 35 | UnwindData |  |
| 344 | `_ui64toa_s` | `0x1B690` | 19 | UnwindData |  |
| 345 | `_ui64tow` | `0x1B6B0` | 35 | UnwindData |  |
| 346 | `_ui64tow_s` | `0x1B6E0` | 19 | UnwindData |  |
| 347 | `_ultoa` | `0x1B700` | 35 | UnwindData |  |
| 348 | `_ultoa_s` | `0x1B730` | 19 | UnwindData |  |
| 349 | `_ultow` | `0x1B750` | 35 | UnwindData |  |
| 350 | `_ultow_s` | `0x1B780` | 19 | UnwindData |  |
| 55 | `__isascii` | `0x1B7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `__iscsym` | `0x1B7C0` | 130 | UnwindData |  |
| 57 | `__iscsymf` | `0x1B850` | 162 | UnwindData |  |
| 88 | `__toascii` | `0x1B900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `_isalnum_l` | `0x1B910` | 195 | UnwindData |  |
| 204 | `_isalpha_l` | `0x1B9E0` | 195 | UnwindData |  |
| 205 | `_isblank_l` | `0x1BAB0` | 189 | UnwindData |  |
| 206 | `_iscntrl_l` | `0x1BB80` | 189 | UnwindData |  |
| 209 | `_isdigit_l` | `0x1BC50` | 189 | UnwindData |  |
| 210 | `_isgraph_l` | `0x1BD20` | 195 | UnwindData |  |
| 212 | `_islower_l` | `0x1BDF0` | 189 | UnwindData |  |
| 215 | `_isprint_l` | `0x1BEC0` | 195 | UnwindData |  |
| 216 | `_ispunct_l` | `0x1BF90` | 189 | UnwindData |  |
| 217 | `_isspace_l` | `0x1C060` | 189 | UnwindData |  |
| 218 | `_isupper_l` | `0x1C130` | 189 | UnwindData |  |
| 234 | `_isxdigit_l` | `0x1C200` | 195 | UnwindData |  |
| 563 | `isalnum` | `0x1C2D0` | 145 | UnwindData |  |
| 564 | `isalpha` | `0x1C370` | 145 | UnwindData |  |
| 565 | `isblank` | `0x1C410` | 150 | UnwindData |  |
| 566 | `iscntrl` | `0x1C4B0` | 140 | UnwindData |  |
| 567 | `isdigit` | `0x1C550` | 140 | UnwindData |  |
| 568 | `isgraph` | `0x1C5F0` | 145 | UnwindData |  |
| 570 | `islower` | `0x1C690` | 140 | UnwindData |  |
| 571 | `isprint` | `0x1C730` | 145 | UnwindData |  |
| 572 | `ispunct` | `0x1C7D0` | 140 | UnwindData |  |
| 573 | `isspace` | `0x1C870` | 140 | UnwindData |  |
| 574 | `isupper` | `0x1C910` | 140 | UnwindData |  |
| 589 | `isxdigit` | `0x1C9B0` | 145 | UnwindData |  |
| 58 | `__iswcsym` | `0x1CC70` | 44 | UnwindData |  |
| 223 | `_iswcsym_l` | `0x1CC70` | 44 | UnwindData |  |
| 59 | `__iswcsymf` | `0x1CCB0` | 44 | UnwindData |  |
| 224 | `_iswcsymf_l` | `0x1CCB0` | 44 | UnwindData |  |
| 211 | `_isleadbyte_l` | `0x1CCF0` | 75 | UnwindData |  |
| 219 | `_iswalnum_l` | `0x1CD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 575 | `iswalnum` | `0x1CD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `_iswalpha_l` | `0x1CD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `iswalpha` | `0x1CD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `_iswblank_l` | `0x1CD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `iswblank` | `0x1CD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `_iswcntrl_l` | `0x1CD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `iswcntrl` | `0x1CD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `_iswdigit_l` | `0x1CDA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 581 | `iswdigit` | `0x1CDA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `_iswgraph_l` | `0x1CDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 582 | `iswgraph` | `0x1CDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `_iswlower_l` | `0x1CDC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `iswlower` | `0x1CDC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `_iswprint_l` | `0x1CDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `iswprint` | `0x1CDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `_iswpunct_l` | `0x1CDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 585 | `iswpunct` | `0x1CDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `_iswspace_l` | `0x1CDF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `iswspace` | `0x1CDF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `_iswupper_l` | `0x1CE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 587 | `iswupper` | `0x1CE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `_iswxdigit_l` | `0x1CE10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `iswxdigit` | `0x1CE10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `isleadbyte` | `0x1CE20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 577 | `iswascii` | `0x1CE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `_aligned_recalloc` | `0x1CE50` | 622 | UnwindData |  |
| 103 | `_aligned_realloc` | `0x1D0D0` | 462 | UnwindData |  |
| 102 | `_aligned_offset_recalloc` | `0x1D2B0` | 784 | UnwindData |  |
| 101 | `_aligned_offset_realloc` | `0x1D5D0` | 602 | UnwindData |  |
| 100 | `_aligned_offset_malloc` | `0x1D830` | 200 | UnwindData |  |
| 99 | `_aligned_msize` | `0x1D900` | 101 | UnwindData |  |
| 98 | `_aligned_malloc` | `0x1D970` | 127 | UnwindData |  |
| 97 | `_aligned_free` | `0x1DA00` | 27 | UnwindData |  |
| 442 | `calloc` | `0x1E610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `_calloc_base` | `0x1E620` | 115 | UnwindData |  |
| 155 | `_expand` | `0x1E770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 555 | `free` | `0x1E780` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `_free_base` | `0x1E7B0` | 60 | UnwindData |  |
| 183 | `_get_heap_handle` | `0x1E800` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `malloc` | `0x1E860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `_malloc_base` | `0x1E870` | 89 | UnwindData |  |
| 271 | `_msize` | `0x1E8D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `_query_new_handler` | `0x1E920` | 67 | UnwindData |  |
| 296 | `_set_new_handler` | `0x1E970` | 101 | UnwindData |  |
| 123 | `_callnewh` | `0x1E9F0` | 51 | UnwindData |  |
| 297 | `_set_new_mode` | `0x1EA30` | 43 | UnwindData |  |
| 276 | `_query_new_mode` | `0x1EA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 667 | `realloc` | `0x1EA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `_realloc_base` | `0x1EA90` | 122 | UnwindData |  |
| 278 | `_recalloc` | `0x1EB10` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `_lock_locales` | `0x1EE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `_unlock_locales` | `0x1EE50` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `__threadhandle` | `0x1F500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `__threadid` | `0x1F510` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `__pctype_func` | `0x1F5D0` | 47 | UnwindData |  |
| 62 | `__pwctype_func` | `0x1F610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `___lc_codepage_func` | `0x1F620` | 47 | UnwindData |  |
| 44 | `___lc_collate_cp_func` | `0x1F660` | 47 | UnwindData |  |
| 45 | `___lc_locale_name_func` | `0x1F6A0` | 50 | UnwindData |  |
| 46 | `___mb_cur_max_func` | `0x1F6E0` | 47 | UnwindData |  |
| 47 | `___mb_cur_max_l_func` | `0x1F720` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 604 | `localeconv` | `0x1F990` | 51 | UnwindData |  |
| 129 | `_configthreadlocale` | `0x1FFA0` | 105 | UnwindData |  |
| 180 | `_get_current_locale` | `0x20010` | 192 | UnwindData |  |
| 189 | `_getmbcp` | `0x20640` | 76 | UnwindData |  |
| 50 | `__doserrno` | `0x20820` | 82 | UnwindData |  |
| 151 | `_errno` | `0x20880` | 82 | UnwindData |  |
| 181 | `_get_doserrno` | `0x208E0` | 41 | UnwindData |  |
| 182 | `_get_errno` | `0x20910` | 41 | UnwindData |  |
| 292 | `_set_doserrno` | `0x20940` | 81 | UnwindData |  |
| 293 | `_set_errno` | `0x209A0` | 81 | UnwindData |  |
| 287 | `_seh_filter_dll` | `0x20A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `_seh_filter_exe` | `0x20A20` | 409 | UnwindData |  |
| 184 | `_get_invalid_parameter_handler` | `0x20BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `_get_thread_local_invalid_parameter_handler` | `0x20BE0` | 71 | UnwindData |  |
| 199 | `_invalid_parameter_noinfo` | `0x20D60` | 14 | UnwindData |  |
| 200 | `_invalid_parameter_noinfo_noreturn` | `0x20D80` | 16 | UnwindData |  |
| 201 | `_invoke_watson` | `0x20DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `_set_invalid_parameter_handler` | `0x20DB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `_set_thread_local_invalid_parameter_handler` | `0x20DF0` | 37 | UnwindData |  |
| 294 | `_set_error_mode` | `0x20E20` | 71 | UnwindData |  |
| 52 | `__fpecode` | `0x20F50` | 18 | UnwindData |  |
| 63 | `__pxcptinfoptrs` | `0x20F70` | 18 | UnwindData |  |
| 665 | `raise` | `0x20F90` | 556 | UnwindData |  |
| 354 | `_wcserror` | `0x21450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `_wcserror_s` | `0x21460` | 112 | UnwindData |  |
| 702 | `strerror` | `0x214E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `strerror_s` | `0x214F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `__sys_errlist` | `0x21500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `__sys_nerr` | `0x21510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `_get_terminate` | `0x21520` | 34 | UnwindData |  |
| 731 | `terminate` | `0x21550` | 31 | UnwindData |  |
| 93 | `__wcserror` | `0x21CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `__wcserror_s` | `0x21CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `_strerror` | `0x21CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `_strerror_s` | `0x21CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `_set_abort_behavior` | `0x21CE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `abort` | `0x21D10` | 76 | UnwindData |  |
| 105 | `_assert` | `0x21D80` | 73 | UnwindData |  |
| 352 | `_wassert` | `0x21E60` | 74 | UnwindData |  |
| 6 | `_Exit` | `0x22030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `_exit` | `0x22030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `_c_exit` | `0x22050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `_cexit` | `0x22070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `_register_thread_local_exe_atexit_callback` | `0x22090` | 60 | UnwindData |  |
| 522 | `exit` | `0x220E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `quick_exit` | `0x220F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `_initterm` | `0x22110` | 54 | UnwindData |  |
| 198 | `_initterm_e` | `0x22150` | 57 | UnwindData |  |
| 135 | `_crt_at_quick_exit` | `0x22520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `_crt_atexit` | `0x22540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `_execute_onexit_table` | `0x22560` | 63 | UnwindData |  |
| 196 | `_initialize_onexit_table` | `0x225B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `_register_onexit_function` | `0x225E0` | 66 | UnwindData |  |
| 78 | `__stdio_common_vsscanf` | `0x27730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `__stdio_common_vswscanf` | `0x27740` | 42,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `__stdio_common_vsnprintf_s` | `0x31D30` | 103 | UnwindData |  |
| 74 | `__stdio_common_vsnwprintf_s` | `0x31DA0` | 103 | UnwindData |  |
| 75 | `__stdio_common_vsprintf` | `0x31E10` | 84 | UnwindData |  |
| 76 | `__stdio_common_vsprintf_p` | `0x31E70` | 84 | UnwindData |  |
| 77 | `__stdio_common_vsprintf_s` | `0x31ED0` | 177 | UnwindData |  |
| 79 | `__stdio_common_vswprintf` | `0x31F90` | 84 | UnwindData |  |
| 80 | `__stdio_common_vswprintf_p` | `0x31FF0` | 84 | UnwindData |  |
| 81 | `__stdio_common_vswprintf_s` | `0x32050` | 84 | UnwindData |  |
| 96 | `_abs64` | `0x320B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `imaxabs` | `0x320B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 596 | `llabs` | `0x320B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `abs` | `0x320D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `labs` | `0x320D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `bsearch` | `0x320E0` | 253 | UnwindData |  |
| 429 | `bsearch_s` | `0x321F0` | 263 | UnwindData |  |
| 118 | `_byteswap_uint64` | `0x32300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `_byteswap_ulong` | `0x32310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `_byteswap_ushort` | `0x32320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 515 | `div` | `0x32330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `ldiv` | `0x32330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 562 | `imaxdiv` | `0x32350` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `_lfind` | `0x32380` | 157 | UnwindData |  |
| 254 | `_lfind_s` | `0x32430` | 161 | UnwindData |  |
| 597 | `lldiv` | `0x324E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `_lsearch` | `0x32500` | 188 | UnwindData |  |
| 262 | `_lsearch_s` | `0x325D0` | 186 | UnwindData |  |
| 662 | `qsort` | `0x32690` | 1,271 | UnwindData |  |
| 663 | `qsort_s` | `0x32B90` | 1,329 | UnwindData |  |
| 666 | `rand` | `0x330D0` | 41 | UnwindData |  |
| 694 | `srand` | `0x33100` | 22 | UnwindData |  |
| 259 | `_lrotl` | `0x33120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `_rotl` | `0x33120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `_rotl64` | `0x33130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `_lrotr` | `0x33150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `_rotr` | `0x33150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `_rotr64` | `0x33160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `memcpy_s` | `0x33180` | 135 | UnwindData |  |
| 641 | `memmove_s` | `0x33210` | 81 | UnwindData |  |
| 269 | `_memicmp` | `0x33270` | 139 | UnwindData |  |
| 270 | `_memicmp_l` | `0x33310` | 170 | UnwindData |  |
| 696 | `strcat_s` | `0x333C0` | 108 | UnwindData |  |
| 700 | `strcpy_s` | `0x33440` | 95 | UnwindData |  |
| 701 | `strcspn` | `0x33540` | 960 | UnwindData |  |
| 302 | `_strdup` | `0x33910` | 140 | UnwindData |  |
| 305 | `_stricmp` | `0x33B50` | 113 | UnwindData |  |
| 306 | `_stricmp_l` | `0x33BD0` | 136 | UnwindData |  |
| 307 | `_strlwr` | `0x33E40` | 94 | UnwindData |  |
| 308 | `_strlwr_l` | `0x33EB0` | 30 | UnwindData |  |
| 309 | `_strlwr_s` | `0x33EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `_strlwr_s_l` | `0x33EF0` | 75 | UnwindData |  |
| 706 | `strncat_s` | `0x34030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `__strncnt` | `0x34040` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `strncpy_s` | `0x34140` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `_strnicmp` | `0x34390` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `_strnicmp_l` | `0x343D0` | 177 | UnwindData |  |
| 710 | `strnlen` | `0x34490` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `wcslen` | `0x345F0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `wcsnlen` | `0x34720` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `_strnset_s` | `0x348F0` | 116 | UnwindData |  |
| 711 | `strpbrk` | `0x349F0` | 959 | UnwindData |  |
| 317 | `_strset_s` | `0x34DC0` | 73 | UnwindData |  |
| 713 | `strspn` | `0x34EA0` | 960 | UnwindData |  |
| 718 | `strtok` | `0x35270` | 46 | UnwindData |  |
| 719 | `strtok_s` | `0x35370` | 56 | UnwindData |  |
| 331 | `_strupr` | `0x35590` | 94 | UnwindData |  |
| 332 | `_strupr_l` | `0x35600` | 30 | UnwindData |  |
| 333 | `_strupr_s` | `0x35630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `_strupr_s_l` | `0x35640` | 75 | UnwindData |  |
| 335 | `_strxfrm_l` | `0x356A0` | 237 | UnwindData |  |
| 726 | `strxfrm` | `0x357A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 746 | `wcscat` | `0x357B0` | 324 | UnwindData |  |
| 747 | `wcscat_s` | `0x35900` | 117 | UnwindData |  |
| 749 | `wcscmp` | `0x35980` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `wcscpy` | `0x359C0` | 336 | UnwindData |  |
| 751 | `wcscpy_s` | `0x35B20` | 101 | UnwindData |  |
| 752 | `wcscspn` | `0x35B90` | 94 | UnwindData |  |
| 353 | `_wcsdup` | `0x35C00` | 158 | UnwindData |  |
| 356 | `_wcsicmp` | `0x35D30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `_wcsicmp_l` | `0x35D60` | 207 | UnwindData |  |
| 358 | `_wcslwr` | `0x36080` | 102 | UnwindData |  |
| 359 | `_wcslwr_l` | `0x360F0` | 30 | UnwindData |  |
| 360 | `_wcslwr_s` | `0x36120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `_wcslwr_s_l` | `0x36130` | 75 | UnwindData |  |
| 754 | `wcsncat` | `0x36190` | 762 | UnwindData |  |
| 755 | `wcsncat_s` | `0x36590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `wcsncmp` | `0x365A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `__wcsncnt` | `0x365E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `wcsncpy` | `0x36610` | 517 | UnwindData |  |
| 758 | `wcsncpy_s` | `0x36920` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `_wcsnicmp` | `0x36990` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `_wcsnicmp_l` | `0x369C0` | 243 | UnwindData |  |
| 364 | `_wcsnset` | `0x36AC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `_wcsnset_s` | `0x36AF0` | 122 | UnwindData |  |
| 760 | `wcspbrk` | `0x36B70` | 77 | UnwindData |  |
| 366 | `_wcsrev` | `0x36BD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `_wcsset` | `0x36C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `_wcsset_s` | `0x36C40` | 78 | UnwindData |  |
| 764 | `wcsspn` | `0x36CA0` | 94 | UnwindData |  |
| 769 | `wcstok` | `0x36D10` | 57 | UnwindData |  |
| 770 | `wcstok_s` | `0x36E10` | 56 | UnwindData |  |
| 384 | `_wcsupr` | `0x370A0` | 102 | UnwindData |  |
| 385 | `_wcsupr_l` | `0x37110` | 30 | UnwindData |  |
| 386 | `_wcsupr_s` | `0x37140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `_wcsupr_s_l` | `0x37150` | 75 | UnwindData |  |
| 388 | `_wcsxfrm_l` | `0x371B0` | 215 | UnwindData |  |
| 779 | `wcsxfrm` | `0x37290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `wmemcpy_s` | `0x372A0` | 122 | UnwindData |  |
| 786 | `wmemmove_s` | `0x37320` | 82 | UnwindData |  |
| 409 | `acosh` | `0x37380` | 209 | UnwindData |  |
| 411 | `acoshl` | `0x37380` | 209 | UnwindData |  |
| 410 | `acoshf` | `0x37460` | 182 | UnwindData |  |
| 414 | `asinh` | `0x37530` | 228 | UnwindData |  |
| 416 | `asinhl` | `0x37530` | 228 | UnwindData |  |
| 415 | `asinhf` | `0x37620` | 202 | UnwindData |  |
| 421 | `atanh` | `0x376F0` | 214 | UnwindData |  |
| 423 | `atanhl` | `0x376F0` | 214 | UnwindData |  |
| 422 | `atanhf` | `0x377D0` | 183 | UnwindData |  |
| 239 | `_j0` | `0x37890` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `_j1` | `0x37BB0` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `_jn` | `0x37EF0` | 372 | UnwindData |  |
| 402 | `_y0` | `0x38070` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `_y1` | `0x38410` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `_yn` | `0x387C0` | 231 | UnwindData |  |
| 434 | `cabsf` | `0x38900` | 30 | UnwindData |  |
| 433 | `cabs` | `0x38930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `cabsl` | `0x38930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `cacos` | `0x38950` | 828 | UnwindData |  |
| 437 | `cacosf` | `0x38CA0` | 713 | UnwindData |  |
| 438 | `cacosh` | `0x38F70` | 894 | UnwindData |  |
| 439 | `cacoshf` | `0x39300` | 805 | UnwindData |  |
| 440 | `cacoshl` | `0x39630` | 894 | UnwindData |  |
| 441 | `cacosl` | `0x399C0` | 828 | UnwindData |  |
| 443 | `carg` | `0x39D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `cargl` | `0x39D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `cargf` | `0x39D30` | 30 | UnwindData |  |
| 446 | `casin` | `0x39D60` | 84 | UnwindData |  |
| 447 | `casinf` | `0x39DC0` | 78 | UnwindData |  |
| 448 | `casinh` | `0x39E20` | 838 | UnwindData |  |
| 449 | `casinhf` | `0x3A170` | 758 | UnwindData |  |
| 450 | `casinhl` | `0x3A470` | 838 | UnwindData |  |
| 451 | `casinl` | `0x3A7C0` | 84 | UnwindData |  |
| 452 | `catan` | `0x3A820` | 84 | UnwindData |  |
| 457 | `catanl` | `0x3A820` | 84 | UnwindData |  |
| 453 | `catanf` | `0x3A880` | 78 | UnwindData |  |
| 454 | `catanh` | `0x3A8E0` | 951 | UnwindData |  |
| 456 | `catanhl` | `0x3A8E0` | 951 | UnwindData |  |
| 455 | `catanhf` | `0x3ACA0` | 880 | UnwindData |  |
| 458 | `cbrt` | `0x3B020` | 945 | UnwindData |  |
| 460 | `cbrtl` | `0x3B020` | 945 | UnwindData |  |
| 459 | `cbrtf` | `0x3B3E0` | 793 | UnwindData |  |
| 461 | `ccos` | `0x3B700` | 66 | UnwindData |  |
| 466 | `ccosl` | `0x3B700` | 66 | UnwindData |  |
| 462 | `ccosf` | `0x3B750` | 45 | UnwindData |  |
| 463 | `ccosh` | `0x3B930` | 574 | UnwindData |  |
| 465 | `ccoshl` | `0x3B930` | 574 | UnwindData |  |
| 464 | `ccoshf` | `0x3BCF0` | 502 | UnwindData |  |
| 469 | `cexp` | `0x3BF00` | 599 | UnwindData |  |
| 471 | `cexpl` | `0x3BF00` | 599 | UnwindData |  |
| 470 | `cexpf` | `0x3C160` | 538 | UnwindData |  |
| 472 | `cimag` | `0x3C380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `cimagl` | `0x3C380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `cimagf` | `0x3C390` | 19 | UnwindData |  |
| 475 | `clog` | `0x3C3B0` | 827 | UnwindData |  |
| 480 | `clogl` | `0x3C3B0` | 827 | UnwindData |  |
| 476 | `clog10` | `0x3C700` | 56 | UnwindData |  |
| 478 | `clog10l` | `0x3C700` | 56 | UnwindData |  |
| 477 | `clog10f` | `0x3C740` | 55 | UnwindData |  |
| 479 | `clogf` | `0x3C780` | 710 | UnwindData |  |
| 481 | `conj` | `0x3CA50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `conjl` | `0x3CA50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `conjf` | `0x3CA80` | 39 | UnwindData |  |
| 132 | `_controlfp_s` | `0x3CAB0` | 99 | UnwindData |  |
| 484 | `copysign` | `0x3CB20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `copysignl` | `0x3CB20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `copysignf` | `0x3CB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `_Cmulcc` | `0x3CB90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `_LCmulcc` | `0x3CB90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `_Cmulcr` | `0x3CBE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `_LCmulcr` | `0x3CBE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `cpow` | `0x3CC10` | 196 | UnwindData |  |
| 8 | `_FCmulcc` | `0x3CCE0` | 74 | UnwindData |  |
| 9 | `_FCmulcr` | `0x3CD30` | 40 | UnwindData |  |
| 492 | `cpowf` | `0x3CD60` | 169 | UnwindData |  |
| 493 | `cpowl` | `0x3CE10` | 196 | UnwindData |  |
| 1 | `_Cbuild` | `0x3CEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `_LCbuild` | `0x3CEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `cproj` | `0x3CF00` | 300 | UnwindData |  |
| 496 | `cprojl` | `0x3CF00` | 300 | UnwindData |  |
| 7 | `_FCbuild` | `0x3D040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `cprojf` | `0x3D050` | 230 | UnwindData |  |
| 497 | `creal` | `0x3D140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `creall` | `0x3D140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `crealf` | `0x3D150` | 18 | UnwindData |  |
| 500 | `csin` | `0x3D170` | 84 | UnwindData |  |
| 505 | `csinl` | `0x3D170` | 84 | UnwindData |  |
| 501 | `csinf` | `0x3D1D0` | 78 | UnwindData |  |
| 502 | `csinh` | `0x3D460` | 479 | UnwindData |  |
| 504 | `csinhl` | `0x3D460` | 479 | UnwindData |  |
| 503 | `csinhf` | `0x3D830` | 395 | UnwindData |  |
| 506 | `csqrt` | `0x3DF60` | 551 | UnwindData |  |
| 507 | `csqrtf` | `0x3E650` | 485 | UnwindData |  |
| 508 | `csqrtl` | `0x3EDD0` | 551 | UnwindData |  |
| 509 | `ctan` | `0x3F000` | 84 | UnwindData |  |
| 514 | `ctanl` | `0x3F000` | 84 | UnwindData |  |
| 510 | `ctanf` | `0x3F060` | 78 | UnwindData |  |
| 511 | `ctanh` | `0x3F0C0` | 570 | UnwindData |  |
| 513 | `ctanhl` | `0x3F0C0` | 570 | UnwindData |  |
| 512 | `ctanhf` | `0x3F300` | 463 | UnwindData |  |
| 143 | `_dpoly` | `0x3F4E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `_ldpoly` | `0x3F4E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `erf` | `0x3F510` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `erfc` | `0x3F7B0` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `_fdpoly` | `0x3FCF0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `erfcf` | `0x40130` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `erfcl` | `0x40670` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `erff` | `0x40840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `erfl` | `0x40860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `_ldexp` | `0x40880` | 1,122 | UnwindData |  |
| 526 | `exp2l` | `0x40CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `expm1` | `0x40D00` | 311 | UnwindData |  |
| 530 | `expm1l` | `0x40D00` | 311 | UnwindData |  |
| 529 | `expm1f` | `0x40E40` | 199 | UnwindData |  |
| 531 | `fabs` | `0x40F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | `fdim` | `0x40F20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `fdiml` | `0x40F20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 533 | `fdimf` | `0x40FA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `feclearexcept` | `0x40FF0` | 98 | UnwindData |  |
| 536 | `fegetexceptflag` | `0x410B0` | 47 | UnwindData |  |
| 51 | `__fpe_flt_rounds` | `0x410F0` | 81 | UnwindData |  |
| 537 | `fegetround` | `0x41150` | 36 | UnwindData |  |
| 538 | `feholdexcept` | `0x41180` | 80 | UnwindData |  |
| 539 | `fesetexceptflag` | `0x41250` | 107 | UnwindData |  |
| 540 | `fesetround` | `0x412D0` | 208 | UnwindData |  |
| 541 | `fetestexcept` | `0x413B0` | 33 | UnwindData |  |
| 544 | `fma` | `0x42560` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `_get_FMA3_enable` | `0x428B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `_set_FMA3_enable` | `0x428D0` | 4,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `fmaf` | `0x43870` | 3,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | `fmal` | `0x44580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `fmax` | `0x445A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `fmaxl` | `0x445A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `fmaxf` | `0x44620` | 3,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `fmin` | `0x45210` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `fminl` | `0x45210` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 551 | `fminf` | `0x45290` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `_except1` | `0x454C0` | 260 | UnwindData |  |
| 556 | `frexp` | `0x45F30` | 407 | UnwindData |  |
| 558 | `ilogb` | `0x460D0` | 159 | UnwindData |  |
| 560 | `ilogbl` | `0x460D0` | 159 | UnwindData |  |
| 559 | `ilogbf` | `0x46180` | 133 | UnwindData |  |
| 591 | `ldexp` | `0x46210` | 768 | UnwindData |  |
| 146 | `_dsin` | `0x46B80` | 401 | UnwindData |  |
| 593 | `lgamma` | `0x46DB0` | 3,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `_fdsin` | `0x47A70` | 298 | UnwindData |  |
| 594 | `lgammaf` | `0x48280` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `_ldsin` | `0x48910` | 401 | UnwindData |  |
| 595 | `lgammal` | `0x48F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `llrint` | `0x48F60` | 106 | UnwindData |  |
| 599 | `llrintf` | `0x48FD0` | 84 | UnwindData |  |
| 600 | `llrintl` | `0x49030` | 106 | UnwindData |  |
| 601 | `llround` | `0x490A0` | 106 | UnwindData |  |
| 603 | `llroundl` | `0x490A0` | 106 | UnwindData |  |
| 602 | `llroundf` | `0x49110` | 84 | UnwindData |  |
| 608 | `log1p` | `0x49170` | 236 | UnwindData |  |
| 610 | `log1pl` | `0x49170` | 236 | UnwindData |  |
| 609 | `log1pf` | `0x49270` | 201 | UnwindData |  |
| 140 | `_dlog` | `0x49340` | 598 | UnwindData |  |
| 245 | `_ldlog` | `0x49340` | 598 | UnwindData |  |
| 613 | `log2l` | `0x495A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 615 | `logbf` | `0x495B0` | 166 | UnwindData |  |
| 614 | `logb` | `0x49660` | 195 | UnwindData |  |
| 616 | `logbl` | `0x49660` | 195 | UnwindData |  |
| 619 | `lrint` | `0x49730` | 105 | UnwindData |  |
| 620 | `lrintf` | `0x497A0` | 83 | UnwindData |  |
| 621 | `lrintl` | `0x49800` | 105 | UnwindData |  |
| 622 | `lround` | `0x49870` | 105 | UnwindData |  |
| 624 | `lroundl` | `0x49870` | 105 | UnwindData |  |
| 623 | `lroundf` | `0x498E0` | 83 | UnwindData |  |
| 65 | `__setusermatherr` | `0x49980` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `_dclass` | `0x499B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `_ldclass` | `0x499B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `_dpcomp` | `0x49A20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `_ldpcomp` | `0x49A20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `_dsign` | `0x49AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `_ldsign` | `0x49AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `nan` | `0x49AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 647 | `nanl` | `0x49AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `_fdclass` | `0x49AC0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `_fdpcomp` | `0x49B10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `_fdsign` | `0x49B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 646 | `nanf` | `0x49B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 648 | `nearbyint` | `0x49B80` | 81 | UnwindData |  |
| 649 | `nearbyintf` | `0x49BE0` | 61 | UnwindData |  |
| 650 | `nearbyintl` | `0x49C30` | 81 | UnwindData |  |
| 272 | `_nextafter` | `0x49C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | `nextafter` | `0x49C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 656 | `nexttowardl` | `0x49C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `_nextafterf` | `0x49CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `nextafterf` | `0x49CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `nextafterl` | `0x49CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `nexttoward` | `0x49CC0` | 293 | UnwindData |  |
| 655 | `nexttowardf` | `0x49DF0` | 275 | UnwindData |  |
| 657 | `norm` | `0x49F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 659 | `norml` | `0x49F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 658 | `normf` | `0x49F30` | 36 | UnwindData |  |
| 670 | `remainderl` | `0x49F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `remquo` | `0x49F70` | 1,095 | UnwindData |  |
| 673 | `remquol` | `0x49F70` | 1,095 | UnwindData |  |
| 672 | `remquof` | `0x4A3C0` | 964 | UnwindData |  |
| 674 | `rint` | `0x4AB80` | 123 | UnwindData |  |
| 675 | `rintf` | `0x4AF80` | 102 | UnwindData |  |
| 676 | `rintl` | `0x4B3E0` | 123 | UnwindData |  |
| 679 | `roundl` | `0x4B470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `scalbln` | `0x4B480` | 424 | UnwindData |  |
| 682 | `scalblnl` | `0x4B480` | 424 | UnwindData |  |
| 683 | `scalbn` | `0x4B480` | 424 | UnwindData |  |
| 685 | `scalbnl` | `0x4B480` | 424 | UnwindData |  |
| 681 | `scalblnf` | `0x4B630` | 349 | UnwindData |  |
| 684 | `scalbnf` | `0x4B630` | 349 | UnwindData |  |
| 732 | `tgamma` | `0x4C420` | 6,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 733 | `tgammaf` | `0x4DBB0` | 5,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `tgammal` | `0x4EF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `trunc` | `0x4EF70` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `truncf` | `0x4EFE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `truncl` | `0x4F040` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `_dnorm` | `0x4F340` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `_fdnorm` | `0x4F3B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `_dscale` | `0x4F400` | 341 | UnwindData |  |
| 165 | `_fdscale` | `0x4F560` | 297 | UnwindData |  |
| 248 | `_ldscale` | `0x4F690` | 334 | UnwindData |  |
| 137 | `_d_int` | `0x4F7F0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `_dtest` | `0x4F8A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `_ldtest` | `0x4F8A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `_fd_int` | `0x4F900` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `_fdtest` | `0x4F990` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `_ld_int` | `0x4F9E0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `_dunscale` | `0x4FA90` | 212 | UnwindData |  |
| 169 | `_fdunscale` | `0x4FB70` | 172 | UnwindData |  |
| 252 | `_ldunscale` | `0x4FC30` | 210 | UnwindData |  |
| 407 | `acos` | `0x4FD10` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `acosf` | `0x50060` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `asin` | `0x50350` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `asinf` | `0x506B0` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `atan` | `0x509D0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `atan2` | `0x50C50` | 2,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `atan2f` | `0x515D0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `atanf` | `0x51BF0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `_cabs` | `0x51E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `ceil` | `0x51E40` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `ceilf` | `0x51F20` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 489 | `cosh` | `0x51FC0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `coshf` | `0x523C0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `floor` | `0x52750` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 543 | `floorf` | `0x52820` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `_hypot` | `0x528C0` | 504 | UnwindData |  |
| 557 | `hypot` | `0x52AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `_hypotf` | `0x52AD0` | 258 | UnwindData |  |
| 257 | `_logb` | `0x52FB0` | 237 | UnwindData |  |
| 258 | `_logbf` | `0x530B0` | 194 | UnwindData |  |
| 643 | `modf` | `0x53180` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `modff` | `0x53250` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 690 | `sinh` | `0x532E0` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `sinhf` | `0x53730` | 960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 692 | `sqrt` | `0x53AF0` | 187 | UnwindData |  |
| 693 | `sqrtf` | `0x53BC0` | 140 | UnwindData |  |
| 729 | `tanh` | `0x53C60` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `tanhf` | `0x53FE0` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `_chgsign` | `0x542F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `_chgsignf` | `0x54320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `_copysign` | `0x54340` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `_copysignf` | `0x54380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `_finite` | `0x543A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `_finitef` | `0x543E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `_memccpy` | `0x54400` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `_strnset` | `0x54440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `_strrev` | `0x54460` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `_strset` | `0x544A0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `_fpieee_flt` | `0x54600` | 11,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `fmodf` | `0x57430` | 540 | UnwindData |  |
| 128 | `_clearfp` | `0x57700` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `_control87` | `0x57760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `_controlfp` | `0x57770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `_fpreset` | `0x57780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `_set_controlfp` | `0x577A0` | 52 | UnwindData |  |
| 301 | `_statusfp` | `0x577E0` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `_fpclass` | `0x57AC0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `_fpclassf` | `0x57B50` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `_isnan` | `0x57BC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `_isnanf` | `0x57C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `_scalb` | `0x57C20` | 434 | UnwindData |  |
| 286 | `_scalbf` | `0x57DE0` | 386 | UnwindData |  |
| 611 | `log2` | `0x57F70` | 813 | UnwindData |  |
| 669 | `remainderf` | `0x585C0` | 627 | UnwindData |  |
| 612 | `log2f` | `0x5BDE0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `exp2f` | `0x5BF00` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `exp2` | `0x5C000` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | `pow` | `0x5C250` | 51,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `_dexp` | `0x68A20` | 1,122 | UnwindData |  |
| 160 | `_fdexp` | `0x68E90` | 982 | UnwindData |  |
| 161 | `_fdlog` | `0x69270` | 482 | UnwindData |  |
| 89 | `__unDName` | `0x70C70` | 39 | UnwindData |  |
| 90 | `__unDNameEx` | `0x70CA0` | 182 | UnwindData |  |
| 697 | `strchr` | `0x70E00` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `strrchr` | `0x70E90` | 317 | UnwindData |  |
| 714 | `strstr` | `0x70FE0` | 492 | UnwindData |  |
| 748 | `wcschr` | `0x711E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `wcsrchr` | `0x71260` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `wcsstr` | `0x71320` | 527 | UnwindData |  |
| 53 | `__intrinsic_setjmp` | `0x71630` | 144 | UnwindData |  |
| 687 | `setjmp` | `0x716D0` | 5 | UnwindData |  |
| 54 | `__intrinsic_setjmpex` | `0x716F0` | 144 | UnwindData |  |
| 695 | `strcat` | `0x71900` | 144 | UnwindData |  |
| 699 | `strcpy` | `0x719A0` | 183 | UnwindData |  |
| 698 | `strcmp` | `0x71A70` | 103 | UnwindData |  |
| 704 | `strlen` | `0x71AF0` | 168 | UnwindData |  |
| 705 | `strncat` | `0x71BB0` | 405 | UnwindData |  |
| 707 | `strncmp` | `0x71D60` | 125 | UnwindData |  |
| 708 | `strncpy` | `0x71DF0` | 354 | UnwindData |  |
| 636 | `memchr` | `0x71F70` | 144 | UnwindData |  |
| 637 | `memcmp` | `0x72010` | 199 | UnwindData |  |
| 638 | `memcpy` | `0x72110` | 1,645 | UnwindData |  |
| 640 | `memmove` | `0x72110` | 1,645 | UnwindData |  |
| 642 | `memset` | `0x727B0` | 904 | UnwindData |  |
| 391 | `_wctype` | `0x7ED10` | 0 | Indeterminate |  |
