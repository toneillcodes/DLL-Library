# Binary Specification: ucrtbase_enclave.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ucrtbase_enclave.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ea087fed60a9126d7f0770c28adc47c3ff99a6716774f9a8c72136149d032825`
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
| 82 | `__stdio_common_vswscanf` | `0x27740` | 42,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `__stdio_common_vsnprintf_s` | `0x31D20` | 103 | UnwindData |  |
| 74 | `__stdio_common_vsnwprintf_s` | `0x31D90` | 103 | UnwindData |  |
| 75 | `__stdio_common_vsprintf` | `0x31E00` | 84 | UnwindData |  |
| 76 | `__stdio_common_vsprintf_p` | `0x31E60` | 84 | UnwindData |  |
| 77 | `__stdio_common_vsprintf_s` | `0x31EC0` | 177 | UnwindData |  |
| 79 | `__stdio_common_vswprintf` | `0x31F80` | 84 | UnwindData |  |
| 80 | `__stdio_common_vswprintf_p` | `0x31FE0` | 84 | UnwindData |  |
| 81 | `__stdio_common_vswprintf_s` | `0x32040` | 84 | UnwindData |  |
| 96 | `_abs64` | `0x320A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `imaxabs` | `0x320A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 596 | `llabs` | `0x320A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `abs` | `0x320C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `labs` | `0x320C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `bsearch` | `0x320D0` | 253 | UnwindData |  |
| 429 | `bsearch_s` | `0x321E0` | 263 | UnwindData |  |
| 118 | `_byteswap_uint64` | `0x322F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `_byteswap_ulong` | `0x32300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `_byteswap_ushort` | `0x32310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 515 | `div` | `0x32320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `ldiv` | `0x32320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 562 | `imaxdiv` | `0x32340` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `_lfind` | `0x32370` | 157 | UnwindData |  |
| 254 | `_lfind_s` | `0x32420` | 161 | UnwindData |  |
| 597 | `lldiv` | `0x324D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `_lsearch` | `0x324F0` | 188 | UnwindData |  |
| 262 | `_lsearch_s` | `0x325C0` | 186 | UnwindData |  |
| 662 | `qsort` | `0x32680` | 1,271 | UnwindData |  |
| 663 | `qsort_s` | `0x32B80` | 1,329 | UnwindData |  |
| 666 | `rand` | `0x330C0` | 41 | UnwindData |  |
| 694 | `srand` | `0x330F0` | 22 | UnwindData |  |
| 259 | `_lrotl` | `0x33110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `_rotl` | `0x33110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `_rotl64` | `0x33120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `_lrotr` | `0x33140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `_rotr` | `0x33140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `_rotr64` | `0x33150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `memcpy_s` | `0x33170` | 135 | UnwindData |  |
| 641 | `memmove_s` | `0x33200` | 81 | UnwindData |  |
| 269 | `_memicmp` | `0x33260` | 139 | UnwindData |  |
| 270 | `_memicmp_l` | `0x33300` | 170 | UnwindData |  |
| 696 | `strcat_s` | `0x333B0` | 108 | UnwindData |  |
| 700 | `strcpy_s` | `0x33430` | 95 | UnwindData |  |
| 701 | `strcspn` | `0x33530` | 960 | UnwindData |  |
| 302 | `_strdup` | `0x33900` | 140 | UnwindData |  |
| 305 | `_stricmp` | `0x33B40` | 113 | UnwindData |  |
| 306 | `_stricmp_l` | `0x33BC0` | 136 | UnwindData |  |
| 307 | `_strlwr` | `0x33E30` | 94 | UnwindData |  |
| 308 | `_strlwr_l` | `0x33EA0` | 30 | UnwindData |  |
| 309 | `_strlwr_s` | `0x33ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `_strlwr_s_l` | `0x33EE0` | 75 | UnwindData |  |
| 706 | `strncat_s` | `0x34020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `__strncnt` | `0x34030` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `strncpy_s` | `0x34130` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `_strnicmp` | `0x34380` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `_strnicmp_l` | `0x343C0` | 177 | UnwindData |  |
| 710 | `strnlen` | `0x34480` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `wcslen` | `0x345E0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `wcsnlen` | `0x34710` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `_strnset_s` | `0x348E0` | 116 | UnwindData |  |
| 711 | `strpbrk` | `0x349E0` | 959 | UnwindData |  |
| 317 | `_strset_s` | `0x34DB0` | 73 | UnwindData |  |
| 713 | `strspn` | `0x34E90` | 960 | UnwindData |  |
| 718 | `strtok` | `0x35260` | 46 | UnwindData |  |
| 719 | `strtok_s` | `0x35360` | 56 | UnwindData |  |
| 331 | `_strupr` | `0x35580` | 94 | UnwindData |  |
| 332 | `_strupr_l` | `0x355F0` | 30 | UnwindData |  |
| 333 | `_strupr_s` | `0x35620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `_strupr_s_l` | `0x35630` | 75 | UnwindData |  |
| 335 | `_strxfrm_l` | `0x35690` | 237 | UnwindData |  |
| 726 | `strxfrm` | `0x35790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 746 | `wcscat` | `0x357A0` | 324 | UnwindData |  |
| 747 | `wcscat_s` | `0x358F0` | 117 | UnwindData |  |
| 749 | `wcscmp` | `0x35970` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `wcscpy` | `0x359B0` | 336 | UnwindData |  |
| 751 | `wcscpy_s` | `0x35B10` | 101 | UnwindData |  |
| 752 | `wcscspn` | `0x35B80` | 94 | UnwindData |  |
| 353 | `_wcsdup` | `0x35BF0` | 158 | UnwindData |  |
| 356 | `_wcsicmp` | `0x35D20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `_wcsicmp_l` | `0x35D50` | 207 | UnwindData |  |
| 358 | `_wcslwr` | `0x36070` | 102 | UnwindData |  |
| 359 | `_wcslwr_l` | `0x360E0` | 30 | UnwindData |  |
| 360 | `_wcslwr_s` | `0x36110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `_wcslwr_s_l` | `0x36120` | 75 | UnwindData |  |
| 754 | `wcsncat` | `0x36180` | 762 | UnwindData |  |
| 755 | `wcsncat_s` | `0x36580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `wcsncmp` | `0x36590` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `__wcsncnt` | `0x365D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `wcsncpy` | `0x36600` | 517 | UnwindData |  |
| 758 | `wcsncpy_s` | `0x36910` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `_wcsnicmp` | `0x36980` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `_wcsnicmp_l` | `0x369B0` | 243 | UnwindData |  |
| 364 | `_wcsnset` | `0x36AB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `_wcsnset_s` | `0x36AE0` | 122 | UnwindData |  |
| 760 | `wcspbrk` | `0x36B60` | 77 | UnwindData |  |
| 366 | `_wcsrev` | `0x36BC0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `_wcsset` | `0x36C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `_wcsset_s` | `0x36C30` | 78 | UnwindData |  |
| 764 | `wcsspn` | `0x36C90` | 94 | UnwindData |  |
| 769 | `wcstok` | `0x36D00` | 57 | UnwindData |  |
| 770 | `wcstok_s` | `0x36E00` | 56 | UnwindData |  |
| 384 | `_wcsupr` | `0x37090` | 102 | UnwindData |  |
| 385 | `_wcsupr_l` | `0x37100` | 30 | UnwindData |  |
| 386 | `_wcsupr_s` | `0x37130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `_wcsupr_s_l` | `0x37140` | 75 | UnwindData |  |
| 388 | `_wcsxfrm_l` | `0x371A0` | 215 | UnwindData |  |
| 779 | `wcsxfrm` | `0x37280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `wmemcpy_s` | `0x37290` | 122 | UnwindData |  |
| 786 | `wmemmove_s` | `0x37310` | 82 | UnwindData |  |
| 409 | `acosh` | `0x37370` | 209 | UnwindData |  |
| 411 | `acoshl` | `0x37370` | 209 | UnwindData |  |
| 410 | `acoshf` | `0x37450` | 182 | UnwindData |  |
| 414 | `asinh` | `0x37520` | 228 | UnwindData |  |
| 416 | `asinhl` | `0x37520` | 228 | UnwindData |  |
| 415 | `asinhf` | `0x37610` | 202 | UnwindData |  |
| 421 | `atanh` | `0x376E0` | 214 | UnwindData |  |
| 423 | `atanhl` | `0x376E0` | 214 | UnwindData |  |
| 422 | `atanhf` | `0x377C0` | 183 | UnwindData |  |
| 239 | `_j0` | `0x37880` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `_j1` | `0x37BA0` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `_jn` | `0x37EE0` | 372 | UnwindData |  |
| 402 | `_y0` | `0x38060` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `_y1` | `0x38400` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `_yn` | `0x387B0` | 231 | UnwindData |  |
| 434 | `cabsf` | `0x388F0` | 30 | UnwindData |  |
| 433 | `cabs` | `0x38920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `cabsl` | `0x38920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `cacos` | `0x38940` | 828 | UnwindData |  |
| 437 | `cacosf` | `0x38C90` | 713 | UnwindData |  |
| 438 | `cacosh` | `0x38F60` | 894 | UnwindData |  |
| 439 | `cacoshf` | `0x392F0` | 805 | UnwindData |  |
| 440 | `cacoshl` | `0x39620` | 894 | UnwindData |  |
| 441 | `cacosl` | `0x399B0` | 828 | UnwindData |  |
| 443 | `carg` | `0x39D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `cargl` | `0x39D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `cargf` | `0x39D20` | 30 | UnwindData |  |
| 446 | `casin` | `0x39D50` | 84 | UnwindData |  |
| 447 | `casinf` | `0x39DB0` | 78 | UnwindData |  |
| 448 | `casinh` | `0x39E10` | 838 | UnwindData |  |
| 449 | `casinhf` | `0x3A160` | 758 | UnwindData |  |
| 450 | `casinhl` | `0x3A460` | 838 | UnwindData |  |
| 451 | `casinl` | `0x3A7B0` | 84 | UnwindData |  |
| 452 | `catan` | `0x3A810` | 84 | UnwindData |  |
| 457 | `catanl` | `0x3A810` | 84 | UnwindData |  |
| 453 | `catanf` | `0x3A870` | 78 | UnwindData |  |
| 454 | `catanh` | `0x3A8D0` | 951 | UnwindData |  |
| 456 | `catanhl` | `0x3A8D0` | 951 | UnwindData |  |
| 455 | `catanhf` | `0x3AC90` | 880 | UnwindData |  |
| 458 | `cbrt` | `0x3B010` | 945 | UnwindData |  |
| 460 | `cbrtl` | `0x3B010` | 945 | UnwindData |  |
| 459 | `cbrtf` | `0x3B3D0` | 793 | UnwindData |  |
| 461 | `ccos` | `0x3B6F0` | 66 | UnwindData |  |
| 466 | `ccosl` | `0x3B6F0` | 66 | UnwindData |  |
| 462 | `ccosf` | `0x3B740` | 45 | UnwindData |  |
| 463 | `ccosh` | `0x3B920` | 574 | UnwindData |  |
| 465 | `ccoshl` | `0x3B920` | 574 | UnwindData |  |
| 464 | `ccoshf` | `0x3BCE0` | 502 | UnwindData |  |
| 469 | `cexp` | `0x3BEF0` | 599 | UnwindData |  |
| 471 | `cexpl` | `0x3BEF0` | 599 | UnwindData |  |
| 470 | `cexpf` | `0x3C150` | 538 | UnwindData |  |
| 472 | `cimag` | `0x3C370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `cimagl` | `0x3C370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `cimagf` | `0x3C380` | 19 | UnwindData |  |
| 475 | `clog` | `0x3C3A0` | 827 | UnwindData |  |
| 480 | `clogl` | `0x3C3A0` | 827 | UnwindData |  |
| 476 | `clog10` | `0x3C6F0` | 56 | UnwindData |  |
| 478 | `clog10l` | `0x3C6F0` | 56 | UnwindData |  |
| 477 | `clog10f` | `0x3C730` | 55 | UnwindData |  |
| 479 | `clogf` | `0x3C770` | 710 | UnwindData |  |
| 481 | `conj` | `0x3CA40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `conjl` | `0x3CA40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `conjf` | `0x3CA70` | 39 | UnwindData |  |
| 132 | `_controlfp_s` | `0x3CAA0` | 99 | UnwindData |  |
| 484 | `copysign` | `0x3CB10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `copysignl` | `0x3CB10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `copysignf` | `0x3CB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `_Cmulcc` | `0x3CB80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `_LCmulcc` | `0x3CB80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `_Cmulcr` | `0x3CBD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `_LCmulcr` | `0x3CBD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `cpow` | `0x3CC00` | 196 | UnwindData |  |
| 8 | `_FCmulcc` | `0x3CCD0` | 74 | UnwindData |  |
| 9 | `_FCmulcr` | `0x3CD20` | 40 | UnwindData |  |
| 492 | `cpowf` | `0x3CD50` | 169 | UnwindData |  |
| 493 | `cpowl` | `0x3CE00` | 196 | UnwindData |  |
| 1 | `_Cbuild` | `0x3CED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `_LCbuild` | `0x3CED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `cproj` | `0x3CEF0` | 300 | UnwindData |  |
| 496 | `cprojl` | `0x3CEF0` | 300 | UnwindData |  |
| 7 | `_FCbuild` | `0x3D030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `cprojf` | `0x3D040` | 230 | UnwindData |  |
| 497 | `creal` | `0x3D130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `creall` | `0x3D130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `crealf` | `0x3D140` | 18 | UnwindData |  |
| 500 | `csin` | `0x3D160` | 84 | UnwindData |  |
| 505 | `csinl` | `0x3D160` | 84 | UnwindData |  |
| 501 | `csinf` | `0x3D1C0` | 78 | UnwindData |  |
| 502 | `csinh` | `0x3D450` | 479 | UnwindData |  |
| 504 | `csinhl` | `0x3D450` | 479 | UnwindData |  |
| 503 | `csinhf` | `0x3D820` | 395 | UnwindData |  |
| 506 | `csqrt` | `0x3DF50` | 551 | UnwindData |  |
| 507 | `csqrtf` | `0x3E640` | 485 | UnwindData |  |
| 508 | `csqrtl` | `0x3EDC0` | 551 | UnwindData |  |
| 509 | `ctan` | `0x3EFF0` | 84 | UnwindData |  |
| 514 | `ctanl` | `0x3EFF0` | 84 | UnwindData |  |
| 510 | `ctanf` | `0x3F050` | 78 | UnwindData |  |
| 511 | `ctanh` | `0x3F0B0` | 570 | UnwindData |  |
| 513 | `ctanhl` | `0x3F0B0` | 570 | UnwindData |  |
| 512 | `ctanhf` | `0x3F2F0` | 463 | UnwindData |  |
| 143 | `_dpoly` | `0x3F4D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `_ldpoly` | `0x3F4D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `erf` | `0x3F500` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `erfc` | `0x3F7A0` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `_fdpoly` | `0x3FCE0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `erfcf` | `0x40120` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `erfcl` | `0x40660` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `erff` | `0x40830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `erfl` | `0x40850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `_ldexp` | `0x40870` | 1,122 | UnwindData |  |
| 526 | `exp2l` | `0x40CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `expm1` | `0x40CF0` | 311 | UnwindData |  |
| 530 | `expm1l` | `0x40CF0` | 311 | UnwindData |  |
| 529 | `expm1f` | `0x40E30` | 199 | UnwindData |  |
| 531 | `fabs` | `0x40F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | `fdim` | `0x40F10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `fdiml` | `0x40F10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 533 | `fdimf` | `0x40F90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `feclearexcept` | `0x40FE0` | 98 | UnwindData |  |
| 536 | `fegetexceptflag` | `0x410A0` | 47 | UnwindData |  |
| 51 | `__fpe_flt_rounds` | `0x410E0` | 81 | UnwindData |  |
| 537 | `fegetround` | `0x41140` | 36 | UnwindData |  |
| 538 | `feholdexcept` | `0x41170` | 80 | UnwindData |  |
| 539 | `fesetexceptflag` | `0x41240` | 107 | UnwindData |  |
| 540 | `fesetround` | `0x412C0` | 208 | UnwindData |  |
| 541 | `fetestexcept` | `0x413A0` | 33 | UnwindData |  |
| 544 | `fma` | `0x42550` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `_get_FMA3_enable` | `0x428A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `_set_FMA3_enable` | `0x428C0` | 4,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `fmaf` | `0x43860` | 3,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | `fmal` | `0x44570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `fmax` | `0x44590` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `fmaxl` | `0x44590` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `fmaxf` | `0x44610` | 3,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `fmin` | `0x45200` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `fminl` | `0x45200` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 551 | `fminf` | `0x45280` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `_except1` | `0x454B0` | 260 | UnwindData |  |
| 556 | `frexp` | `0x45F20` | 407 | UnwindData |  |
| 558 | `ilogb` | `0x460C0` | 159 | UnwindData |  |
| 560 | `ilogbl` | `0x460C0` | 159 | UnwindData |  |
| 559 | `ilogbf` | `0x46170` | 133 | UnwindData |  |
| 591 | `ldexp` | `0x46200` | 768 | UnwindData |  |
| 146 | `_dsin` | `0x46B70` | 401 | UnwindData |  |
| 593 | `lgamma` | `0x46DA0` | 3,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `_fdsin` | `0x47A60` | 298 | UnwindData |  |
| 594 | `lgammaf` | `0x48270` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `_ldsin` | `0x48900` | 401 | UnwindData |  |
| 595 | `lgammal` | `0x48F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `llrint` | `0x48F50` | 106 | UnwindData |  |
| 599 | `llrintf` | `0x48FC0` | 84 | UnwindData |  |
| 600 | `llrintl` | `0x49020` | 106 | UnwindData |  |
| 601 | `llround` | `0x49090` | 106 | UnwindData |  |
| 603 | `llroundl` | `0x49090` | 106 | UnwindData |  |
| 602 | `llroundf` | `0x49100` | 84 | UnwindData |  |
| 608 | `log1p` | `0x49160` | 236 | UnwindData |  |
| 610 | `log1pl` | `0x49160` | 236 | UnwindData |  |
| 609 | `log1pf` | `0x49260` | 201 | UnwindData |  |
| 140 | `_dlog` | `0x49330` | 598 | UnwindData |  |
| 245 | `_ldlog` | `0x49330` | 598 | UnwindData |  |
| 613 | `log2l` | `0x49590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 615 | `logbf` | `0x495A0` | 166 | UnwindData |  |
| 614 | `logb` | `0x49650` | 195 | UnwindData |  |
| 616 | `logbl` | `0x49650` | 195 | UnwindData |  |
| 619 | `lrint` | `0x49720` | 105 | UnwindData |  |
| 620 | `lrintf` | `0x49790` | 83 | UnwindData |  |
| 621 | `lrintl` | `0x497F0` | 105 | UnwindData |  |
| 622 | `lround` | `0x49860` | 105 | UnwindData |  |
| 624 | `lroundl` | `0x49860` | 105 | UnwindData |  |
| 623 | `lroundf` | `0x498D0` | 83 | UnwindData |  |
| 65 | `__setusermatherr` | `0x49970` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `_dclass` | `0x499A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `_ldclass` | `0x499A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `_dpcomp` | `0x49A10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `_ldpcomp` | `0x49A10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `_dsign` | `0x49A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `_ldsign` | `0x49A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `nan` | `0x49AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 647 | `nanl` | `0x49AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `_fdclass` | `0x49AB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `_fdpcomp` | `0x49B00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `_fdsign` | `0x49B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 646 | `nanf` | `0x49B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 648 | `nearbyint` | `0x49B70` | 81 | UnwindData |  |
| 649 | `nearbyintf` | `0x49BD0` | 61 | UnwindData |  |
| 650 | `nearbyintl` | `0x49C20` | 81 | UnwindData |  |
| 272 | `_nextafter` | `0x49C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | `nextafter` | `0x49C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 656 | `nexttowardl` | `0x49C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `_nextafterf` | `0x49C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `nextafterf` | `0x49C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `nextafterl` | `0x49CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `nexttoward` | `0x49CB0` | 293 | UnwindData |  |
| 655 | `nexttowardf` | `0x49DE0` | 275 | UnwindData |  |
| 657 | `norm` | `0x49F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 659 | `norml` | `0x49F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 658 | `normf` | `0x49F20` | 36 | UnwindData |  |
| 670 | `remainderl` | `0x49F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `remquo` | `0x49F60` | 1,095 | UnwindData |  |
| 673 | `remquol` | `0x49F60` | 1,095 | UnwindData |  |
| 672 | `remquof` | `0x4A3B0` | 964 | UnwindData |  |
| 674 | `rint` | `0x4AB70` | 123 | UnwindData |  |
| 675 | `rintf` | `0x4AF70` | 102 | UnwindData |  |
| 676 | `rintl` | `0x4B3D0` | 123 | UnwindData |  |
| 679 | `roundl` | `0x4B460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `scalbln` | `0x4B470` | 424 | UnwindData |  |
| 682 | `scalblnl` | `0x4B470` | 424 | UnwindData |  |
| 683 | `scalbn` | `0x4B470` | 424 | UnwindData |  |
| 685 | `scalbnl` | `0x4B470` | 424 | UnwindData |  |
| 681 | `scalblnf` | `0x4B620` | 349 | UnwindData |  |
| 684 | `scalbnf` | `0x4B620` | 349 | UnwindData |  |
| 732 | `tgamma` | `0x4C410` | 6,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 733 | `tgammaf` | `0x4DBA0` | 5,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `tgammal` | `0x4EF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `trunc` | `0x4EF60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `truncf` | `0x4EFD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `truncl` | `0x4F030` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `_dnorm` | `0x4F330` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `_fdnorm` | `0x4F3A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `_dscale` | `0x4F3F0` | 341 | UnwindData |  |
| 165 | `_fdscale` | `0x4F550` | 297 | UnwindData |  |
| 248 | `_ldscale` | `0x4F680` | 334 | UnwindData |  |
| 137 | `_d_int` | `0x4F7E0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `_dtest` | `0x4F890` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `_ldtest` | `0x4F890` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `_fd_int` | `0x4F8F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `_fdtest` | `0x4F980` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `_ld_int` | `0x4F9D0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `_dunscale` | `0x4FA80` | 212 | UnwindData |  |
| 169 | `_fdunscale` | `0x4FB60` | 172 | UnwindData |  |
| 252 | `_ldunscale` | `0x4FC20` | 210 | UnwindData |  |
| 407 | `acos` | `0x4FD00` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `acosf` | `0x50050` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `asin` | `0x50340` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `asinf` | `0x506A0` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `atan` | `0x509C0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `atan2` | `0x50C40` | 2,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `atan2f` | `0x515C0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `atanf` | `0x51BE0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `_cabs` | `0x51E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `ceil` | `0x51E30` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `ceilf` | `0x51F10` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 489 | `cosh` | `0x51FB0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `coshf` | `0x523B0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `floor` | `0x52740` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 543 | `floorf` | `0x52810` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `_hypot` | `0x528B0` | 504 | UnwindData |  |
| 557 | `hypot` | `0x52AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `_hypotf` | `0x52AC0` | 258 | UnwindData |  |
| 257 | `_logb` | `0x52FA0` | 237 | UnwindData |  |
| 258 | `_logbf` | `0x530A0` | 194 | UnwindData |  |
| 643 | `modf` | `0x53170` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `modff` | `0x53240` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 690 | `sinh` | `0x532D0` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `sinhf` | `0x53720` | 960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 692 | `sqrt` | `0x53AE0` | 187 | UnwindData |  |
| 693 | `sqrtf` | `0x53BB0` | 140 | UnwindData |  |
| 729 | `tanh` | `0x53C50` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `tanhf` | `0x53FD0` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `_chgsign` | `0x542E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `_chgsignf` | `0x54310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `_copysign` | `0x54330` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `_copysignf` | `0x54370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `_finite` | `0x54390` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `_finitef` | `0x543D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `_memccpy` | `0x543F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `_strnset` | `0x54430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `_strrev` | `0x54450` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `_strset` | `0x54490` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `_fpieee_flt` | `0x545F0` | 11,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `fmodf` | `0x57420` | 540 | UnwindData |  |
| 128 | `_clearfp` | `0x576F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `_control87` | `0x57750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `_controlfp` | `0x57760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `_fpreset` | `0x57770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `_set_controlfp` | `0x57790` | 52 | UnwindData |  |
| 301 | `_statusfp` | `0x577D0` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `_fpclass` | `0x57AB0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `_fpclassf` | `0x57B40` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `_isnan` | `0x57BB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `_isnanf` | `0x57BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `_scalb` | `0x57C10` | 434 | UnwindData |  |
| 286 | `_scalbf` | `0x57DD0` | 386 | UnwindData |  |
| 611 | `log2` | `0x57F60` | 813 | UnwindData |  |
| 669 | `remainderf` | `0x585B0` | 627 | UnwindData |  |
| 612 | `log2f` | `0x5BDD0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `exp2f` | `0x5BEF0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `exp2` | `0x5BFF0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | `pow` | `0x5C240` | 51,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `_dexp` | `0x689A0` | 1,122 | UnwindData |  |
| 160 | `_fdexp` | `0x68E10` | 982 | UnwindData |  |
| 161 | `_fdlog` | `0x691F0` | 482 | UnwindData |  |
| 89 | `__unDName` | `0x70BF0` | 39 | UnwindData |  |
| 90 | `__unDNameEx` | `0x70C20` | 182 | UnwindData |  |
| 697 | `strchr` | `0x70D80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `strrchr` | `0x70E10` | 317 | UnwindData |  |
| 714 | `strstr` | `0x70F60` | 492 | UnwindData |  |
| 748 | `wcschr` | `0x71160` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `wcsrchr` | `0x711E0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `wcsstr` | `0x712A0` | 527 | UnwindData |  |
| 53 | `__intrinsic_setjmp` | `0x715B0` | 144 | UnwindData |  |
| 687 | `setjmp` | `0x71650` | 5 | UnwindData |  |
| 54 | `__intrinsic_setjmpex` | `0x71670` | 144 | UnwindData |  |
| 695 | `strcat` | `0x71880` | 144 | UnwindData |  |
| 699 | `strcpy` | `0x71920` | 183 | UnwindData |  |
| 698 | `strcmp` | `0x719F0` | 103 | UnwindData |  |
| 704 | `strlen` | `0x71A70` | 168 | UnwindData |  |
| 705 | `strncat` | `0x71B30` | 405 | UnwindData |  |
| 707 | `strncmp` | `0x71CE0` | 125 | UnwindData |  |
| 708 | `strncpy` | `0x71D70` | 354 | UnwindData |  |
| 636 | `memchr` | `0x71EF0` | 144 | UnwindData |  |
| 637 | `memcmp` | `0x71F90` | 199 | UnwindData |  |
| 638 | `memcpy` | `0x72090` | 1,645 | UnwindData |  |
| 640 | `memmove` | `0x72090` | 1,645 | UnwindData |  |
| 642 | `memset` | `0x72730` | 904 | UnwindData |  |
| 391 | `_wctype` | `0x7ED10` | 0 | Indeterminate |  |
