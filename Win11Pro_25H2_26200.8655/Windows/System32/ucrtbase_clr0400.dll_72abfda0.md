# Binary Specification: ucrtbase_clr0400.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ucrtbase_clr0400.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `72abfda0c31fa5682ee901bf96ace23141c99e5ae37aa7325ad2b648c44b9ab8`
* **Total Exported Functions:** 1351

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `_Cbuild` | `0x1010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `_LCbuild` | `0x1010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | `cproj` | `0x1020` | 190 | UnwindData |  |
| 2 | `_Cmulcc` | `0x10E0` | 209 | UnwindData |  |
| 12 | `_LCmulcc` | `0x10E0` | 209 | UnwindData |  |
| 3 | `_Cmulcr` | `0x11C0` | 107 | UnwindData |  |
| 13 | `_LCmulcr` | `0x11C0` | 107 | UnwindData |  |
| 1010 | `cpow` | `0x1230` | 304 | UnwindData |  |
| 4 | `_Exit` | `0x1610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `_exit` | `0x1610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `_c_exit` | `0x1630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `_cexit` | `0x1640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `_register_thread_local_exe_atexit_callback` | `0x1660` | 60 | UnwindData |  |
| 1041 | `exit` | `0x16A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1218 | `quick_exit` | `0x16B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `_FCbuild` | `0x16C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `cprojf` | `0x16D0` | 162 | UnwindData |  |
| 6 | `_FCmulcc` | `0x1780` | 155 | UnwindData |  |
| 7 | `_FCmulcr` | `0x1820` | 90 | UnwindData |  |
| 1011 | `cpowf` | `0x1880` | 177 | UnwindData |  |
| 8 | `_Getdays` | `0x1C60` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `_Getmonths` | `0x1DB0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `_Gettnames` | `0x1F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `_Strftime` | `0x1F20` | 30 | UnwindData |  |
| 696 | `_strftime_l` | `0x20B0` | 30 | UnwindData |  |
| 1265 | `strftime` | `0x20D0` | 26 | UnwindData |  |
| 1015 | `cprojl` | `0x20F0` | 190 | UnwindData |  |
| 1012 | `cpowl` | `0x21B0` | 301 | UnwindData |  |
| 15 | `_W_Getdays` | `0x3980` | 395 | UnwindData |  |
| 16 | `_W_Getmonths` | `0x3B10` | 395 | UnwindData |  |
| 17 | `_W_Gettnames` | `0x3CA0` | 1,728 | UnwindData |  |
| 18 | `_Wcsftime` | `0x4360` | 30 | UnwindData |  |
| 786 | `_wcsftime_l` | `0x4530` | 30 | UnwindData |  |
| 1319 | `wcsftime` | `0x4550` | 26 | UnwindData |  |
| 19 | `___lc_codepage_func` | `0x4570` | 47 | UnwindData |  |
| 20 | `___lc_collate_cp_func` | `0x45A0` | 47 | UnwindData |  |
| 21 | `___lc_locale_name_func` | `0x45D0` | 50 | UnwindData |  |
| 22 | `___mb_cur_max_func` | `0x4610` | 47 | UnwindData |  |
| 23 | `___mb_cur_max_l_func` | `0x4640` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `__acrt_iob_func` | `0x4DE0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `_get_stream_buffer_pointers` | `0x4E60` | 71 | UnwindData |  |
| 450 | `_lock_file` | `0x4EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `_unlock_file` | `0x4EC0` | 37,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `__conio_common_vcprintf` | `0xE1F0` | 311 | UnwindData |  |
| 26 | `__conio_common_vcprintf_p` | `0xE330` | 340 | UnwindData |  |
| 27 | `__conio_common_vcprintf_s` | `0xE490` | 311 | UnwindData |  |
| 29 | `__conio_common_vcwprintf` | `0xE5D0` | 315 | UnwindData |  |
| 30 | `__conio_common_vcwprintf_p` | `0xE710` | 344 | UnwindData |  |
| 31 | `__conio_common_vcwprintf_s` | `0xE870` | 315 | UnwindData |  |
| 28 | `__conio_common_vcscanf` | `0x17570` | 208 | UnwindData |  |
| 32 | `__conio_common_vcwscanf` | `0x17640` | 191 | UnwindData |  |
| 33 | `__daylight` | `0x17850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `__dstbias` | `0x17860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `__timezone` | `0x17870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `__tzname` | `0x17880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `_get_daylight` | `0x17890` | 47 | UnwindData |  |
| 267 | `_get_dstbias` | `0x178C0` | 47 | UnwindData |  |
| 281 | `_get_timezone` | `0x178F0` | 47 | UnwindData |  |
| 282 | `_get_tzname` | `0x17920` | 157 | UnwindData |  |
| 34 | `__doserrno` | `0x17A80` | 32 | UnwindData |  |
| 180 | `_errno` | `0x17AA0` | 32 | UnwindData |  |
| 266 | `_get_doserrno` | `0x17AC0` | 59 | UnwindData |  |
| 268 | `_get_errno` | `0x17B00` | 59 | UnwindData |  |
| 657 | `_set_doserrno` | `0x17B40` | 58 | UnwindData |  |
| 658 | `_set_errno` | `0x17B80` | 58 | UnwindData |  |
| 36 | `__fpe_flt_rounds` | `0x17BC0` | 69 | UnwindData |  |
| 1058 | `fegetround` | `0x17C10` | 20 | UnwindData |  |
| 37 | `__fpecode` | `0x17DA0` | 18 | UnwindData |  |
| 59 | `__pxcptinfoptrs` | `0x17DC0` | 18 | UnwindData |  |
| 1219 | `raise` | `0x17DE0` | 638 | UnwindData |  |
| 1248 | `signal` | `0x18060` | 473 | UnwindData |  |
| 38 | `__initialize_lconv_for_unsigned_char` | `0x18240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `__isascii` | `0x18250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__iscsym` | `0x18260` | 127 | UnwindData |  |
| 41 | `__iscsymf` | `0x182E0` | 171 | UnwindData |  |
| 85 | `__toascii` | `0x18390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `_isalnum_l` | `0x183A0` | 249 | UnwindData |  |
| 330 | `_isalpha_l` | `0x184A0` | 249 | UnwindData |  |
| 332 | `_isblank_l` | `0x185A0` | 242 | UnwindData |  |
| 333 | `_iscntrl_l` | `0x186A0` | 242 | UnwindData |  |
| 336 | `_isdigit_l` | `0x187A0` | 242 | UnwindData |  |
| 337 | `_isgraph_l` | `0x188A0` | 249 | UnwindData |  |
| 339 | `_islower_l` | `0x189A0` | 242 | UnwindData |  |
| 404 | `_isprint_l` | `0x18AA0` | 249 | UnwindData |  |
| 405 | `_ispunct_l` | `0x18BA0` | 242 | UnwindData |  |
| 406 | `_isspace_l` | `0x18CA0` | 242 | UnwindData |  |
| 407 | `_isupper_l` | `0x18DA0` | 242 | UnwindData |  |
| 423 | `_isxdigit_l` | `0x18EA0` | 249 | UnwindData |  |
| 1116 | `isalnum` | `0x18FA0` | 171 | UnwindData |  |
| 1117 | `isalpha` | `0x19050` | 171 | UnwindData |  |
| 1118 | `isblank` | `0x19100` | 30 | UnwindData |  |
| 1119 | `iscntrl` | `0x191C0` | 166 | UnwindData |  |
| 1120 | `isdigit` | `0x19270` | 166 | UnwindData |  |
| 1121 | `isgraph` | `0x19320` | 171 | UnwindData |  |
| 1123 | `islower` | `0x193D0` | 166 | UnwindData |  |
| 1124 | `isprint` | `0x19480` | 171 | UnwindData |  |
| 1125 | `ispunct` | `0x19530` | 166 | UnwindData |  |
| 1126 | `isspace` | `0x195E0` | 166 | UnwindData |  |
| 1127 | `isupper` | `0x19690` | 166 | UnwindData |  |
| 1142 | `isxdigit` | `0x19740` | 171 | UnwindData |  |
| 42 | `__iswcsym` | `0x197F0` | 44 | UnwindData |  |
| 412 | `_iswcsym_l` | `0x197F0` | 44 | UnwindData |  |
| 43 | `__iswcsymf` | `0x19820` | 44 | UnwindData |  |
| 413 | `_iswcsymf_l` | `0x19820` | 44 | UnwindData |  |
| 338 | `_isleadbyte_l` | `0x19850` | 75 | UnwindData |  |
| 408 | `_iswalnum_l` | `0x198A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `iswalnum` | `0x198A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `_iswalpha_l` | `0x198B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1129 | `iswalpha` | `0x198B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `_iswblank_l` | `0x198C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1131 | `iswblank` | `0x198C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `_iswcntrl_l` | `0x198E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1132 | `iswcntrl` | `0x198E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `_iswdigit_l` | `0x198F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1134 | `iswdigit` | `0x198F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `_iswgraph_l` | `0x19900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `iswgraph` | `0x19900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `_iswlower_l` | `0x19910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `iswlower` | `0x19910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `_iswprint_l` | `0x19920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `iswprint` | `0x19920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `_iswpunct_l` | `0x19930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `iswpunct` | `0x19930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `_iswspace_l` | `0x19940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1139 | `iswspace` | `0x19940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `_iswupper_l` | `0x19950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1140 | `iswupper` | `0x19950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `_iswxdigit_l` | `0x19960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1141 | `iswxdigit` | `0x19960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `isleadbyte` | `0x19970` | 77 | UnwindData |  |
| 1130 | `iswascii` | `0x199C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `__p___argc` | `0x19A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `__p___argv` | `0x19A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `__p___wargv` | `0x19A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `__p__acmdln` | `0x19A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `__p__pgmptr` | `0x19A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `__p__wcmdln` | `0x19A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `__p__wpgmptr` | `0x19A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `_get_pgmptr` | `0x19A80` | 54 | UnwindData |  |
| 284 | `_get_wpgmptr` | `0x19AC0` | 54 | UnwindData |  |
| 48 | `__p__commode` | `0x19B00` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `__p__environ` | `0x1A0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `__p__wenviron` | `0x1A100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `_get_initial_narrow_environment` | `0x1A110` | 78 | UnwindData |  |
| 272 | `_get_initial_wide_environment` | `0x1A160` | 78 | UnwindData |  |
| 321 | `_initialize_narrow_environment` | `0x1A1B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `_initialize_wide_environment` | `0x1A1C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__p__fmode` | `0x1A1F0` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `__p__mbcasemap` | `0x1AA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `__p__mbctype` | `0x1AA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `_getmbcp` | `0x1AA90` | 58 | UnwindData |  |
| 668 | `_setmbcp` | `0x1AAD0` | 37 | UnwindData |  |
| 57 | `__pctype_func` | `0x1ADC0` | 47 | UnwindData |  |
| 58 | `__pwctype_func` | `0x1ADF0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `__setusermatherr` | `0x1AE60` | 27,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `__stdio_common_vfprintf` | `0x21B60` | 292 | UnwindData |  |
| 62 | `__stdio_common_vfprintf_p` | `0x21C90` | 292 | UnwindData |  |
| 63 | `__stdio_common_vfprintf_s` | `0x21DC0` | 292 | UnwindData |  |
| 65 | `__stdio_common_vfwprintf` | `0x21EF0` | 292 | UnwindData |  |
| 66 | `__stdio_common_vfwprintf_p` | `0x22020` | 292 | UnwindData |  |
| 67 | `__stdio_common_vfwprintf_s` | `0x22150` | 292 | UnwindData |  |
| 69 | `__stdio_common_vsnprintf_s` | `0x22280` | 485 | UnwindData |  |
| 70 | `__stdio_common_vsnwprintf_s` | `0x22470` | 487 | UnwindData |  |
| 71 | `__stdio_common_vsprintf` | `0x22660` | 593 | UnwindData |  |
| 72 | `__stdio_common_vsprintf_p` | `0x228C0` | 182 | UnwindData |  |
| 73 | `__stdio_common_vsprintf_s` | `0x22980` | 273 | UnwindData |  |
| 75 | `__stdio_common_vswprintf` | `0x22AA0` | 601 | UnwindData |  |
| 76 | `__stdio_common_vswprintf_p` | `0x22D00` | 182 | UnwindData |  |
| 77 | `__stdio_common_vswprintf_s` | `0x22DC0` | 273 | UnwindData |  |
| 64 | `__stdio_common_vfscanf` | `0x2CF00` | 139 | UnwindData |  |
| 68 | `__stdio_common_vfwscanf` | `0x2CF90` | 139 | UnwindData |  |
| 74 | `__stdio_common_vsscanf` | `0x2D020` | 292 | UnwindData |  |
| 78 | `__stdio_common_vswscanf` | `0x2D150` | 277 | UnwindData |  |
| 79 | `__strncnt` | `0x2D270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `__sys_errlist` | `0x2D290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `__sys_nerr` | `0x2D2A0` | 1,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `__threadhandle` | `0x2D9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `__threadid` | `0x2D9F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `__wcserror` | `0x2DA00` | 370 | UnwindData |  |
| 88 | `__wcserror_s` | `0x2DB80` | 277 | UnwindData |  |
| 694 | `_strerror` | `0x2DD10` | 290 | UnwindData |  |
| 695 | `_strerror_s` | `0x2DE40` | 240 | UnwindData |  |
| 89 | `__wcsncnt` | `0x2DF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `_abs64` | `0x2DF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1113 | `imaxabs` | `0x2DF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `llabs` | `0x2DF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `abs` | `0x2DF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `labs` | `0x2DF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `_access` | `0x2DF70` | 18 | UnwindData |  |
| 92 | `_access_s` | `0x2DF90` | 235 | UnwindData |  |
| 93 | `_aligned_free` | `0x2E080` | 27 | UnwindData |  |
| 94 | `_aligned_malloc` | `0x2E0A0` | 127 | UnwindData |  |
| 95 | `_aligned_msize` | `0x2E120` | 101 | UnwindData |  |
| 96 | `_aligned_offset_malloc` | `0x2E190` | 197 | UnwindData |  |
| 97 | `_aligned_offset_realloc` | `0x2E260` | 599 | UnwindData |  |
| 98 | `_aligned_offset_recalloc` | `0x2E4C0` | 758 | UnwindData |  |
| 99 | `_aligned_realloc` | `0x2E7C0` | 460 | UnwindData |  |
| 100 | `_aligned_recalloc` | `0x2E990` | 619 | UnwindData |  |
| 101 | `_assert` | `0x2F9D0` | 115 | UnwindData |  |
| 777 | `_wassert` | `0x2FA50` | 115 | UnwindData |  |
| 102 | `_atodbl` | `0x31B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `_atodbl_l` | `0x31B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `_atof_l` | `0x31B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `_atoflt` | `0x31B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `_atoflt_l` | `0x31B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `_wtof` | `0x31B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `_wtof_l` | `0x31BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 940 | `atof` | `0x31BB0` | 5,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `_atoi64` | `0x330A0` | 178 | UnwindData |  |
| 943 | `atoll` | `0x330A0` | 178 | UnwindData |  |
| 108 | `_atoi64_l` | `0x33160` | 188 | UnwindData |  |
| 113 | `_atoll_l` | `0x33160` | 188 | UnwindData |  |
| 109 | `_atoi_l` | `0x33220` | 186 | UnwindData |  |
| 110 | `_atol_l` | `0x33220` | 186 | UnwindData |  |
| 905 | `_wtoi` | `0x332E0` | 176 | UnwindData |  |
| 909 | `_wtol` | `0x332E0` | 176 | UnwindData |  |
| 906 | `_wtoi64` | `0x33390` | 178 | UnwindData |  |
| 911 | `_wtoll` | `0x33390` | 178 | UnwindData |  |
| 907 | `_wtoi64_l` | `0x33450` | 188 | UnwindData |  |
| 912 | `_wtoll_l` | `0x33450` | 188 | UnwindData |  |
| 908 | `_wtoi_l` | `0x33510` | 186 | UnwindData |  |
| 910 | `_wtol_l` | `0x33510` | 186 | UnwindData |  |
| 941 | `atoi` | `0x335D0` | 176 | UnwindData |  |
| 942 | `atol` | `0x335D0` | 176 | UnwindData |  |
| 111 | `_atoldbl` | `0x34300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `_atoldbl_l` | `0x34310` | 326 | UnwindData |  |
| 114 | `_beep` | `0x34460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `_sleep` | `0x34470` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `_beginthread` | `0x34640` | 206 | UnwindData |  |
| 116 | `_beginthreadex` | `0x34710` | 212 | UnwindData |  |
| 177 | `_endthread` | `0x347F0` | 12 | UnwindData |  |
| 178 | `_endthreadex` | `0x34800` | 10 | UnwindData |  |
| 117 | `_byteswap_uint64` | `0x34810` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `_byteswap_ulong` | `0x34890` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `_byteswap_ushort` | `0x348C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `_cabs` | `0x348E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `_callnewh` | `0x34900` | 57 | UnwindData |  |
| 633 | `_query_new_handler` | `0x34940` | 52 | UnwindData |  |
| 662 | `_set_new_handler` | `0x34980` | 89 | UnwindData |  |
| 123 | `_calloc_base` | `0x349E0` | 117 | UnwindData |  |
| 125 | `_cgets` | `0x34A60` | 115 | UnwindData |  |
| 126 | `_cgets_s` | `0x34AE0` | 268 | UnwindData |  |
| 127 | `_cgetws` | `0x34BF0` | 116 | UnwindData |  |
| 128 | `_cgetws_s` | `0x34C70` | 399 | UnwindData |  |
| 129 | `_chdir` | `0x35170` | 308 | UnwindData |  |
| 778 | `_wchdir` | `0x352B0` | 340 | UnwindData |  |
| 130 | `_chdrive` | `0x35410` | 129 | UnwindData |  |
| 294 | `_getdrive` | `0x354A0` | 246 | UnwindData |  |
| 131 | `_chgsign` | `0x355A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `_chgsignf` | `0x355D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `_chmod` | `0x355F0` | 235 | UnwindData |  |
| 134 | `_chsize` | `0x35760` | 21 | UnwindData |  |
| 135 | `_chsize_s` | `0x359B0` | 334 | UnwindData |  |
| 136 | `_clearfp` | `0x35B00` | 110 | UnwindData |  |
| 142 | `_control87` | `0x35B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `_controlfp` | `0x35B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `_fpreset` | `0x35B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 656 | `_set_controlfp` | `0x35BA0` | 52 | UnwindData |  |
| 689 | `_statusfp` | `0x35BE0` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `_close` | `0x35F80` | 152 | UnwindData |  |
| 138 | `_commit` | `0x362D0` | 145 | UnwindData |  |
| 139 | `_configthreadlocale` | `0x369B0` | 105 | UnwindData |  |
| 150 | `_create_locale` | `0x36AE0` | 118 | UnwindData |  |
| 241 | `_free_locale` | `0x36FE0` | 162 | UnwindData |  |
| 264 | `_get_current_locale` | `0x37090` | 187 | UnwindData |  |
| 781 | `_wcreate_locale` | `0x37150` | 328 | UnwindData |  |
| 877 | `_wsetlocale` | `0x37300` | 161 | UnwindData |  |
| 140 | `_configure_narrow_argv` | `0x38420` | 390 | UnwindData |  |
| 141 | `_configure_wide_argv` | `0x385B0` | 386 | UnwindData |  |
| 144 | `_controlfp_s` | `0x38740` | 99 | UnwindData |  |
| 145 | `_copysign` | `0x387B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `_copysignf` | `0x387F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `_cputs` | `0x38820` | 114 | UnwindData |  |
| 148 | `_cputws` | `0x388A0` | 176 | UnwindData |  |
| 149 | `_creat` | `0x38950` | 55 | UnwindData |  |
| 780 | `_wcreat` | `0x38990` | 55 | UnwindData |  |
| 151 | `_crt_at_quick_exit` | `0x38D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `_crt_atexit` | `0x38D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `_execute_onexit_table` | `0x38D30` | 67 | UnwindData |  |
| 322 | `_initialize_onexit_table` | `0x38D80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | `_register_onexit_function` | `0x38DB0` | 72 | UnwindData |  |
| 153 | `_ctime32` | `0x38E00` | 115 | UnwindData |  |
| 154 | `_ctime32_s` | `0x38E80` | 152 | UnwindData |  |
| 155 | `_ctime64` | `0x38F20` | 116 | UnwindData |  |
| 156 | `_ctime64_s` | `0x38FA0` | 152 | UnwindData |  |
| 826 | `_wctime32` | `0x39040` | 115 | UnwindData |  |
| 827 | `_wctime32_s` | `0x390C0` | 163 | UnwindData |  |
| 828 | `_wctime64` | `0x39170` | 116 | UnwindData |  |
| 829 | `_wctime64_s` | `0x391F0` | 163 | UnwindData |  |
| 157 | `_cwait` | `0x392A0` | 182 | UnwindData |  |
| 158 | `_d_int` | `0x39360` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `_dtest` | `0x39480` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `_fd_int` | `0x394F0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `_fdtest` | `0x395D0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `_ld_int` | `0x396D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `_ldtest` | `0x396E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `_dclass` | `0x396F0` | 25 | UnwindData |  |
| 165 | `_dpcomp` | `0x39710` | 99 | UnwindData |  |
| 168 | `_dsign` | `0x39780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `_ldsign` | `0x39780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `nan` | `0x397A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `_dexp` | `0x397B0` | 610 | UnwindData |  |
| 1043 | `exp2` | `0x39A20` | 242 | UnwindData |  |
| 161 | `_difftime32` | `0x39B20` | 43 | UnwindData |  |
| 162 | `_difftime64` | `0x39B50` | 46 | UnwindData |  |
| 163 | `_dlog` | `0x39B80` | 448 | UnwindData |  |
| 164 | `_dnorm` | `0x39DA0` | 389 | UnwindData |  |
| 201 | `_fdnorm` | `0x39F30` | 215 | UnwindData |  |
| 166 | `_dpoly` | `0x3A010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `_ldpoly` | `0x3A010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `erfc` | `0x3A030` | 635 | UnwindData |  |
| 167 | `_dscale` | `0x3A2B0` | 635 | UnwindData |  |
| 205 | `_fdscale` | `0x3A530` | 456 | UnwindData |  |
| 438 | `_ldscale` | `0x3A700` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `_dsin` | `0x3AB20` | 373 | UnwindData |  |
| 1146 | `lgamma` | `0x3ACE0` | 567 | UnwindData |  |
| 171 | `_dunscale` | `0x3B010` | 154 | UnwindData |  |
| 209 | `_fdunscale` | `0x3B0B0` | 138 | UnwindData |  |
| 442 | `_ldunscale` | `0x3B140` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `_dup` | `0x3B2D0` | 213 | UnwindData |  |
| 173 | `_dup2` | `0x3B510` | 260 | UnwindData |  |
| 174 | `_dupenv_s` | `0x3BBE0` | 31 | UnwindData |  |
| 833 | `_wdupenv_s` | `0x3BC00` | 31 | UnwindData |  |
| 859 | `_wgetenv` | `0x3BC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 860 | `_wgetenv_s` | `0x3BC30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1103 | `getenv` | `0x3BC40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `getenv_s` | `0x3BC50` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `_ecvt` | `0x3BFA0` | 313 | UnwindData |  |
| 176 | `_ecvt_s` | `0x3C0E0` | 183 | UnwindData |  |
| 195 | `_fcvt` | `0x3C1A0` | 391 | UnwindData |  |
| 196 | `_fcvt_s` | `0x3C330` | 183 | UnwindData |  |
| 179 | `_eof` | `0x3C4C0` | 161 | UnwindData |  |
| 181 | `_except1` | `0x3C5B0` | 241 | UnwindData |  |
| 182 | `_execl` | `0x3D110` | 50 | UnwindData |  |
| 183 | `_execle` | `0x3D150` | 50 | UnwindData |  |
| 675 | `_spawnl` | `0x3D190` | 43 | UnwindData |  |
| 676 | `_spawnle` | `0x3D1C0` | 43 | UnwindData |  |
| 834 | `_wexecl` | `0x3D1F0` | 50 | UnwindData |  |
| 835 | `_wexecle` | `0x3D230` | 50 | UnwindData |  |
| 881 | `_wspawnl` | `0x3D270` | 43 | UnwindData |  |
| 882 | `_wspawnle` | `0x3D2A0` | 43 | UnwindData |  |
| 184 | `_execlp` | `0x3D4C0` | 50 | UnwindData |  |
| 185 | `_execlpe` | `0x3D500` | 50 | UnwindData |  |
| 677 | `_spawnlp` | `0x3D540` | 43 | UnwindData |  |
| 678 | `_spawnlpe` | `0x3D570` | 43 | UnwindData |  |
| 836 | `_wexeclp` | `0x3D5A0` | 50 | UnwindData |  |
| 837 | `_wexeclpe` | `0x3D5E0` | 50 | UnwindData |  |
| 883 | `_wspawnlp` | `0x3D620` | 43 | UnwindData |  |
| 884 | `_wspawnlpe` | `0x3D650` | 43 | UnwindData |  |
| 187 | `_execv` | `0x3E270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `_execve` | `0x3E290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `_spawnv` | `0x3E2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `_spawnve` | `0x3E2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `_wexecv` | `0x3E2D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 839 | `_wexecve` | `0x3E2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `_wspawnv` | `0x3E310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | `_wspawnve` | `0x3E320` | 1,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `_execvp` | `0x3E9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `_execvpe` | `0x3EA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `_spawnvp` | `0x3EA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 682 | `_spawnvpe` | `0x3EA40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | `_wexecvp` | `0x3EA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 841 | `_wexecvpe` | `0x3EA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | `_wspawnvp` | `0x3EA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 888 | `_wspawnvpe` | `0x3EAA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `_expand` | `0x3EAB0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `_fclose_nolock` | `0x3ECE0` | 152 | UnwindData |  |
| 1051 | `fclose` | `0x3ED80` | 152 | UnwindData |  |
| 194 | `_fcloseall` | `0x3EE20` | 177 | UnwindData |  |
| 198 | `_fdclass` | `0x3EEE0` | 25 | UnwindData |  |
| 203 | `_fdpcomp` | `0x3EF00` | 97 | UnwindData |  |
| 206 | `_fdsign` | `0x3EF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `nanf` | `0x3EF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `_fdexp` | `0x3EFA0` | 574 | UnwindData |  |
| 1044 | `exp2f` | `0x3F1E0` | 238 | UnwindData |  |
| 200 | `_fdlog` | `0x3F2D0` | 399 | UnwindData |  |
| 1165 | `log2f` | `0x3F490` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `_fdopen` | `0x3FC40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `_wfdopen` | `0x3FC50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `_fdpoly` | `0x3FC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `erfcf` | `0x3FC80` | 620 | UnwindData |  |
| 207 | `_fdsin` | `0x402E0` | 297 | UnwindData |  |
| 1147 | `lgammaf` | `0x40510` | 553 | UnwindData |  |
| 210 | `_fflush_nolock` | `0x409F0` | 209 | UnwindData |  |
| 229 | `_flushall` | `0x40AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `fflush` | `0x40AE0` | 102 | UnwindData |  |
| 211 | `_fgetc_nolock` | `0x40B50` | 67 | UnwindData |  |
| 212 | `_fgetchar` | `0x40BA0` | 23 | UnwindData |  |
| 1102 | `getchar` | `0x40BA0` | 23 | UnwindData |  |
| 285 | `_getc_nolock` | `0x40BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `fgetc` | `0x40BD0` | 264 | UnwindData |  |
| 1101 | `getc` | `0x40CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `_fgetwc_nolock` | `0x40CF0` | 431 | UnwindData |  |
| 214 | `_fgetwchar` | `0x40EA0` | 23 | UnwindData |  |
| 1108 | `getwchar` | `0x40EA0` | 23 | UnwindData |  |
| 301 | `_getwc_nolock` | `0x40EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1070 | `fgetwc` | `0x40ED0` | 85 | UnwindData |  |
| 1107 | `getwc` | `0x40F30` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `_filelength` | `0x41160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `_filelengthi64` | `0x41170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `_fileno` | `0x41180` | 38 | UnwindData |  |
| 218 | `_findclose` | `0x41FC0` | 37 | UnwindData |  |
| 219 | `_findfirst32` | `0x41FF0` | 393 | UnwindData |  |
| 220 | `_findfirst32i64` | `0x42180` | 393 | UnwindData |  |
| 221 | `_findfirst64` | `0x42310` | 393 | UnwindData |  |
| 222 | `_findfirst64i32` | `0x424A0` | 393 | UnwindData |  |
| 223 | `_findnext32` | `0x42630` | 224 | UnwindData |  |
| 224 | `_findnext32i64` | `0x42710` | 224 | UnwindData |  |
| 225 | `_findnext64` | `0x427F0` | 224 | UnwindData |  |
| 226 | `_findnext64i32` | `0x428D0` | 224 | UnwindData |  |
| 843 | `_wfindfirst32` | `0x429B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `_wfindfirst32i64` | `0x429C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `_wfindfirst64` | `0x429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `_wfindfirst64i32` | `0x429E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `_wfindnext32` | `0x429F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 848 | `_wfindnext32i64` | `0x42A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `_wfindnext64` | `0x42A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | `_wfindnext64i32` | `0x42A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `_finite` | `0x42A30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `_finitef` | `0x42A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `_fpclass` | `0x42A80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `_fpclassf` | `0x42B10` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `_isnan` | `0x42B80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `_isnanf` | `0x42BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 615 | `_nextafter` | `0x42BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 616 | `_nextafterf` | `0x42BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 647 | `_scalb` | `0x42BF0` | 428 | UnwindData |  |
| 648 | `_scalbf` | `0x42DA0` | 415 | UnwindData |  |
| 232 | `_fpieee_flt` | `0x42F40` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `_fputc_nolock` | `0x430C0` | 171 | UnwindData |  |
| 235 | `_fputchar` | `0x43190` | 33 | UnwindData |  |
| 622 | `_putc_nolock` | `0x431C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1087 | `fputc` | `0x431D0` | 152 | UnwindData |  |
| 1211 | `putc` | `0x43270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `putchar` | `0x43280` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `_fputwc_nolock` | `0x43310` | 154 | UnwindData |  |
| 237 | `_fputwchar` | `0x43540` | 35 | UnwindData |  |
| 628 | `_putwc_nolock` | `0x43570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `fputwc` | `0x43580` | 154 | UnwindData |  |
| 1214 | `putwc` | `0x43620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `putwchar` | `0x43630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `_fread_nolock` | `0x43640` | 29 | UnwindData |  |
| 239 | `_fread_nolock_s` | `0x43660` | 606 | UnwindData |  |
| 1091 | `fread` | `0x438C0` | 29 | UnwindData |  |
| 1092 | `fread_s` | `0x438E0` | 165 | UnwindData |  |
| 240 | `_free_base` | `0x43990` | 60 | UnwindData |  |
| 242 | `_fseek_nolock` | `0x43C20` | 155 | UnwindData |  |
| 243 | `_fseeki64` | `0x43CC0` | 152 | UnwindData |  |
| 244 | `_fseeki64_nolock` | `0x43D60` | 152 | UnwindData |  |
| 1097 | `fseek` | `0x43E00` | 155 | UnwindData |  |
| 245 | `_fsopen` | `0x44030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `_wfopen` | `0x44040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `_wfopen_s` | `0x44050` | 88 | UnwindData |  |
| 855 | `_wfsopen` | `0x440B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `fopen` | `0x440C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1086 | `fopen_s` | `0x440D0` | 88 | UnwindData |  |
| 246 | `_fstat32` | `0x45490` | 214 | UnwindData |  |
| 247 | `_fstat32i64` | `0x45570` | 213 | UnwindData |  |
| 248 | `_fstat64` | `0x45650` | 229 | UnwindData |  |
| 249 | `_fstat64i32` | `0x45740` | 213 | UnwindData |  |
| 685 | `_stat32` | `0x45820` | 254 | UnwindData |  |
| 686 | `_stat32i64` | `0x45920` | 254 | UnwindData |  |
| 687 | `_stat64` | `0x45A20` | 254 | UnwindData |  |
| 688 | `_stat64i32` | `0x45B20` | 254 | UnwindData |  |
| 891 | `_wstat32` | `0x45C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `_wstat32i64` | `0x45C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 893 | `_wstat64` | `0x45C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `_wstat64i32` | `0x45C50` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `_ftell_nolock` | `0x461E0` | 175 | UnwindData |  |
| 251 | `_ftelli64` | `0x46290` | 154 | UnwindData |  |
| 252 | `_ftelli64_nolock` | `0x46330` | 154 | UnwindData |  |
| 1099 | `ftell` | `0x463E0` | 152 | UnwindData |  |
| 253 | `_ftime32` | `0x46480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `_ftime32_s` | `0x46490` | 410 | UnwindData |  |
| 255 | `_ftime64` | `0x46630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `_ftime64_s` | `0x46640` | 411 | UnwindData |  |
| 257 | `_fullpath` | `0x47060` | 176 | UnwindData |  |
| 856 | `_wfullpath` | `0x47110` | 177 | UnwindData |  |
| 258 | `_futime32` | `0x475C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `_futime64` | `0x475D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `_utime32` | `0x475E0` | 147 | UnwindData |  |
| 772 | `_utime64` | `0x47680` | 147 | UnwindData |  |
| 914 | `_wutime32` | `0x47720` | 147 | UnwindData |  |
| 915 | `_wutime64` | `0x477C0` | 147 | UnwindData |  |
| 260 | `_fwrite_nolock` | `0x479B0` | 161 | UnwindData |  |
| 1100 | `fwrite` | `0x47C60` | 161 | UnwindData |  |
| 261 | `_gcvt` | `0x47D10` | 44 | UnwindData |  |
| 262 | `_gcvt_s` | `0x47D40` | 556 | UnwindData |  |
| 263 | `_get_FMA3_enable` | `0x47FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `_set_FMA3_enable` | `0x47FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `_get_fmode` | `0x48010` | 47 | UnwindData |  |
| 660 | `_set_fmode` | `0x48040` | 61 | UnwindData |  |
| 669 | `_setmode` | `0x48080` | 257 | UnwindData |  |
| 270 | `_get_heap_handle` | `0x482A0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `_get_invalid_parameter_handler` | `0x48460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `_get_thread_local_invalid_parameter_handler` | `0x48480` | 26 | UnwindData |  |
| 326 | `_invalid_parameter_noinfo` | `0x48600` | 30 | UnwindData |  |
| 327 | `_invalid_parameter_noinfo_noreturn` | `0x48620` | 47 | UnwindData |  |
| 328 | `_invoke_watson` | `0x48650` | 71 | UnwindData |  |
| 661 | `_set_invalid_parameter_handler` | `0x486A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `_set_thread_local_invalid_parameter_handler` | `0x486E0` | 37 | UnwindData |  |
| 274 | `_get_narrow_winmain_command_line` | `0x48710` | 112 | UnwindData |  |
| 283 | `_get_wide_winmain_command_line` | `0x48780` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `_get_osfhandle` | `0x48C80` | 117 | UnwindData |  |
| 618 | `_open_osfhandle` | `0x48D00` | 257 | UnwindData |  |
| 277 | `_get_printf_count_output` | `0x48E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `_set_printf_count_output` | `0x48E30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `_get_terminate` | `0x48E60` | 34 | UnwindData |  |
| 1244 | `set_terminate` | `0x48E90` | 44 | UnwindData |  |
| 1292 | `terminate` | `0x48EC0` | 42 | UnwindData |  |
| 286 | `_getch` | `0x48F30` | 42 | UnwindData |  |
| 287 | `_getch_nolock` | `0x48F60` | 388 | UnwindData |  |
| 288 | `_getche` | `0x490F0` | 42 | UnwindData |  |
| 289 | `_getche_nolock` | `0x49120` | 102 | UnwindData |  |
| 431 | `_kbhit` | `0x49250` | 42 | UnwindData |  |
| 762 | `_ungetch` | `0x49410` | 46 | UnwindData |  |
| 763 | `_ungetch_nolock` | `0x49440` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `_getcwd` | `0x497B0` | 39 | UnwindData |  |
| 291 | `_getdcwd` | `0x497E0` | 31 | UnwindData |  |
| 857 | `_wgetcwd` | `0x49800` | 39 | UnwindData |  |
| 858 | `_wgetdcwd` | `0x49830` | 31 | UnwindData |  |
| 292 | `_getdiskfree` | `0x49850` | 196 | UnwindData |  |
| 293 | `_getdllprocaddr` | `0x49920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `_getdrives` | `0x49950` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `_getmaxstdio` | `0x49A80` | 46 | UnwindData |  |
| 667 | `_setmaxstdio` | `0x49AB0` | 92 | UnwindData |  |
| 298 | `_getpid` | `0x49B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `_getsystime` | `0x49B20` | 158 | UnwindData |  |
| 670 | `_setsystime` | `0x49BC0` | 163 | UnwindData |  |
| 300 | `_getw` | `0x49C70` | 163 | UnwindData |  |
| 302 | `_getwch` | `0x49D20` | 44 | UnwindData |  |
| 303 | `_getwch_nolock` | `0x49D50` | 220 | UnwindData |  |
| 304 | `_getwche` | `0x49E30` | 44 | UnwindData |  |
| 305 | `_getwche_nolock` | `0x49E60` | 79 | UnwindData |  |
| 765 | `_ungetwch` | `0x49EB0` | 50 | UnwindData |  |
| 766 | `_ungetwch_nolock` | `0x49EF0` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `_getws` | `0x4A210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `_getws_s` | `0x4A220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `gets` | `0x4A230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `gets_s` | `0x4A240` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `_gmtime32` | `0x4A6C0` | 72 | UnwindData |  |
| 309 | `_gmtime32_s` | `0x4A710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `_gmtime64` | `0x4A720` | 72 | UnwindData |  |
| 311 | `_gmtime64_s` | `0x4A770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `_heapchk` | `0x4A780` | 37 | UnwindData |  |
| 313 | `_heapmin` | `0x4A7B0` | 33 | UnwindData |  |
| 314 | `_heapwalk` | `0x4A820` | 206 | UnwindData |  |
| 315 | `_hypot` | `0x4A8F0` | 597 | UnwindData |  |
| 1109 | `hypot` | `0x4AB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `_hypotf` | `0x4AB60` | 291 | UnwindData |  |
| 317 | `_i64toa` | `0x4B170` | 49 | UnwindData |  |
| 318 | `_i64toa_s` | `0x4B1B0` | 33 | UnwindData |  |
| 319 | `_i64tow` | `0x4B1E0` | 49 | UnwindData |  |
| 320 | `_i64tow_s` | `0x4B220` | 33 | UnwindData |  |
| 424 | `_itoa` | `0x4B250` | 48 | UnwindData |  |
| 461 | `_ltoa` | `0x4B250` | 48 | UnwindData |  |
| 425 | `_itoa_s` | `0x4B280` | 32 | UnwindData |  |
| 462 | `_ltoa_s` | `0x4B280` | 32 | UnwindData |  |
| 426 | `_itow` | `0x4B2A0` | 48 | UnwindData |  |
| 463 | `_ltow` | `0x4B2A0` | 48 | UnwindData |  |
| 427 | `_itow_s` | `0x4B2D0` | 32 | UnwindData |  |
| 464 | `_ltow_s` | `0x4B2D0` | 32 | UnwindData |  |
| 751 | `_ui64toa` | `0x4B2F0` | 35 | UnwindData |  |
| 752 | `_ui64toa_s` | `0x4B320` | 19 | UnwindData |  |
| 753 | `_ui64tow` | `0x4B340` | 35 | UnwindData |  |
| 754 | `_ui64tow_s` | `0x4B370` | 19 | UnwindData |  |
| 755 | `_ultoa` | `0x4B390` | 35 | UnwindData |  |
| 756 | `_ultoa_s` | `0x4B3C0` | 19 | UnwindData |  |
| 757 | `_ultow` | `0x4B3E0` | 35 | UnwindData |  |
| 758 | `_ultow_s` | `0x4B410` | 19 | UnwindData |  |
| 324 | `_initterm` | `0x4B430` | 65 | UnwindData |  |
| 325 | `_initterm_e` | `0x4B480` | 71 | UnwindData |  |
| 331 | `_isatty` | `0x4B4D0` | 95 | UnwindData |  |
| 334 | `_isctype` | `0x4B530` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `_isctype_l` | `0x4B560` | 264 | UnwindData |  |
| 340 | `_ismbbalnum` | `0x4B6E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `_ismbbalnum_l` | `0x4B700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `_ismbbalpha` | `0x4B720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `_ismbbalpha_l` | `0x4B740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `_ismbbblank` | `0x4B760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `_ismbbblank_l` | `0x4B780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `_ismbbgraph` | `0x4B7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `_ismbbgraph_l` | `0x4B7C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `_ismbbkalnum` | `0x4B7E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `_ismbbkalnum_l` | `0x4B800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `_ismbbkana` | `0x4B820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `_ismbbkana_l` | `0x4B830` | 101 | UnwindData |  |
| 352 | `_ismbbkprint` | `0x4B8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `_ismbbkprint_l` | `0x4B8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `_ismbbkpunct` | `0x4B8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `_ismbbkpunct_l` | `0x4B900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `_ismbblead` | `0x4B920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `_ismbblead_l` | `0x4B940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `_ismbbprint` | `0x4B960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `_ismbbprint_l` | `0x4B980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `_ismbbpunct` | `0x4B9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `_ismbbpunct_l` | `0x4B9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `_ismbbtrail` | `0x4B9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `_ismbbtrail_l` | `0x4BA00` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `_ismbcalnum` | `0x4BAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `_ismbcalnum_l` | `0x4BAC0` | 118 | UnwindData |  |
| 366 | `_ismbcalpha` | `0x4BB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `_ismbcalpha_l` | `0x4BB50` | 118 | UnwindData |  |
| 368 | `_ismbcblank` | `0x4BBD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `_ismbcblank_l` | `0x4BBE0` | 124 | UnwindData |  |
| 390 | `_ismbcpunct` | `0x4BC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `_ismbcpunct_l` | `0x4BC70` | 110 | UnwindData |  |
| 370 | `_ismbcdigit` | `0x4BCE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `_ismbcdigit_l` | `0x4BCF0` | 92 | UnwindData |  |
| 372 | `_ismbcgraph` | `0x4BD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `_ismbcgraph_l` | `0x4BD60` | 113 | UnwindData |  |
| 374 | `_ismbchira` | `0x4BDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `_ismbchira_l` | `0x4BDF0` | 77 | UnwindData |  |
| 376 | `_ismbckata` | `0x4BE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `_ismbckata_l` | `0x4BE50` | 85 | UnwindData |  |
| 394 | `_ismbcsymbol` | `0x4BEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `_ismbcsymbol_l` | `0x4BEC0` | 85 | UnwindData |  |
| 378 | `_ismbcl0` | `0x4BF20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `_ismbcl0_l` | `0x4BF30` | 97 | UnwindData |  |
| 380 | `_ismbcl1` | `0x4BFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `_ismbcl1_l` | `0x4BFB0` | 102 | UnwindData |  |
| 382 | `_ismbcl2` | `0x4C020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `_ismbcl2_l` | `0x4C030` | 102 | UnwindData |  |
| 384 | `_ismbclegal` | `0x4C0A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `_ismbclegal_l` | `0x4C0B0` | 80 | UnwindData |  |
| 386 | `_ismbclower` | `0x4C100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `_ismbclower_l` | `0x4C110` | 93 | UnwindData |  |
| 388 | `_ismbcprint` | `0x4C170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `_ismbcprint_l` | `0x4C180` | 114 | UnwindData |  |
| 392 | `_ismbcspace` | `0x4C200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `_ismbcspace_l` | `0x4C210` | 93 | UnwindData |  |
| 396 | `_ismbcupper` | `0x4C270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `_ismbcupper_l` | `0x4C280` | 93 | UnwindData |  |
| 398 | `_ismbslead` | `0x4C2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `_ismbslead_l` | `0x4C2F0` | 148 | UnwindData |  |
| 400 | `_ismbstrail` | `0x4C390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `_ismbstrail_l` | `0x4C3A0` | 145 | UnwindData |  |
| 414 | `_iswctype_l` | `0x4C440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1115 | `is_wctype` | `0x4C440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1133 | `iswctype` | `0x4C450` | 108 | UnwindData |  |
| 428 | `_j0` | `0x4C4C0` | 353 | UnwindData |  |
| 429 | `_j1` | `0x4C630` | 402 | UnwindData |  |
| 430 | `_jn` | `0x4C7D0` | 378 | UnwindData |  |
| 916 | `_y0` | `0x4C950` | 415 | UnwindData |  |
| 917 | `_y1` | `0x4CAF0` | 443 | UnwindData |  |
| 918 | `_yn` | `0x4CCB0` | 231 | UnwindData |  |
| 433 | `_ldclass` | `0x4CE70` | 25 | UnwindData |  |
| 436 | `_ldpcomp` | `0x4CE90` | 99 | UnwindData |  |
| 1195 | `nanl` | `0x4CF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `_ldexp` | `0x4CF10` | 610 | UnwindData |  |
| 1045 | `exp2l` | `0x4D180` | 242 | UnwindData |  |
| 435 | `_ldlog` | `0x4D280` | 448 | UnwindData |  |
| 1166 | `log2l` | `0x4D440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `erfcl` | `0x4D450` | 621 | UnwindData |  |
| 440 | `_ldsin` | `0x4DAD0` | 373 | UnwindData |  |
| 1148 | `lgammal` | `0x4DD80` | 567 | UnwindData |  |
| 443 | `_lfind` | `0x4DFC0` | 163 | UnwindData |  |
| 444 | `_lfind_s` | `0x4E070` | 169 | UnwindData |  |
| 445 | `_loaddll` | `0x4E120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 768 | `_unloaddll` | `0x4E130` | 32 | UnwindData |  |
| 446 | `_localtime32` | `0x4E710` | 72 | UnwindData |  |
| 447 | `_localtime32_s` | `0x4E760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `_localtime64` | `0x4E770` | 72 | UnwindData |  |
| 449 | `_localtime64_s` | `0x4E7C0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `_lock_locales` | `0x4E8A0` | 27 | UnwindData |  |
| 770 | `_unlock_locales` | `0x4E8C0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `_locking` | `0x4E9F0` | 277 | UnwindData |  |
| 453 | `_logb` | `0x4EB10` | 221 | UnwindData |  |
| 454 | `_logbf` | `0x4EBF0` | 212 | UnwindData |  |
| 455 | `_lrotl` | `0x4ECD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 643 | `_rotl` | `0x4ECD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `_rotl64` | `0x4ECE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `_lrotr` | `0x4ECF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `_rotr` | `0x4ECF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 646 | `_rotr64` | `0x4ED00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `_lsearch` | `0x4ED10` | 188 | UnwindData |  |
| 458 | `_lsearch_s` | `0x4EDD0` | 194 | UnwindData |  |
| 459 | `_lseek` | `0x4F290` | 152 | UnwindData |  |
| 460 | `_lseeki64` | `0x4F3D0` | 154 | UnwindData |  |
| 465 | `_makepath` | `0x4F520` | 39 | UnwindData |  |
| 466 | `_makepath_s` | `0x4F550` | 384 | UnwindData |  |
| 861 | `_wmakepath` | `0x4F6D0` | 39 | UnwindData |  |
| 862 | `_wmakepath_s` | `0x4F700` | 408 | UnwindData |  |
| 467 | `_malloc_base` | `0x4F8A0` | 94 | UnwindData |  |
| 468 | `_mbbtombc` | `0x4F900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `_mbbtombc_l` | `0x4F910` | 161 | UnwindData |  |
| 489 | `_mbctombb` | `0x4F9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `_mbctombb_l` | `0x4F9D0` | 192 | UnwindData |  |
| 470 | `_mbbtype` | `0x4FA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `_mbbtype_l` | `0x4FAA0` | 135 | UnwindData |  |
| 473 | `_mbccpy` | `0x4FB30` | 30 | UnwindData |  |
| 474 | `_mbccpy_l` | `0x4FB50` | 29 | UnwindData |  |
| 475 | `_mbccpy_s` | `0x4FB70` | 20 | UnwindData |  |
| 476 | `_mbccpy_s_l` | `0x4FB90` | 255 | UnwindData |  |
| 477 | `_mbcjistojms` | `0x4FC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 478 | `_mbcjistojms_l` | `0x4FCA0` | 165 | UnwindData |  |
| 479 | `_mbcjmstojis` | `0x4FD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 480 | `_mbcjmstojis_l` | `0x4FD60` | 187 | UnwindData |  |
| 481 | `_mbclen` | `0x4FE20` | 43 | UnwindData |  |
| 482 | `_mbclen_l` | `0x4FE50` | 43 | UnwindData |  |
| 483 | `_mbctohira` | `0x4FE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `_mbctohira_l` | `0x4FE90` | 55 | UnwindData |  |
| 485 | `_mbctokata` | `0x4FED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `_mbctokata_l` | `0x4FEE0` | 41 | UnwindData |  |
| 487 | `_mbctolower` | `0x4FF10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `_mbctolower_l` | `0x4FF20` | 192 | UnwindData |  |
| 491 | `_mbctoupper` | `0x4FFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 492 | `_mbctoupper_l` | `0x4FFF0` | 192 | UnwindData |  |
| 493 | `_mblen_l` | `0x501D0` | 163 | UnwindData |  |
| 1178 | `mblen` | `0x50280` | 152 | UnwindData |  |
| 494 | `_mbsbtype` | `0x50320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `_mbsbtype_l` | `0x50330` | 179 | UnwindData |  |
| 496 | `_mbscat_s` | `0x503F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 497 | `_mbscat_s_l` | `0x50400` | 408 | UnwindData |  |
| 498 | `_mbschr` | `0x505A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `_mbschr_l` | `0x505B0` | 194 | UnwindData |  |
| 500 | `_mbscmp` | `0x50680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `_mbscmp_l` | `0x50690` | 237 | UnwindData |  |
| 502 | `_mbscoll` | `0x50780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `_mbscoll_l` | `0x50790` | 201 | UnwindData |  |
| 504 | `_mbscpy_s` | `0x50860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `_mbscpy_s_l` | `0x50870` | 314 | UnwindData |  |
| 506 | `_mbscspn` | `0x509B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `_mbscspn_l` | `0x509C0` | 236 | UnwindData |  |
| 508 | `_mbsdec` | `0x50AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `_mbsdec_l` | `0x50AC0` | 148 | UnwindData |  |
| 511 | `_mbsicmp` | `0x50B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `_mbsicmp_l` | `0x50B70` | 494 | UnwindData |  |
| 513 | `_mbsicoll` | `0x50D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `_mbsicoll_l` | `0x50D70` | 201 | UnwindData |  |
| 515 | `_mbsinc` | `0x50E40` | 66 | UnwindData |  |
| 516 | `_mbsinc_l` | `0x50E90` | 39 | UnwindData |  |
| 517 | `_mbslen` | `0x50EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `_mbslen_l` | `0x50ED0` | 110 | UnwindData |  |
| 519 | `_mbslwr` | `0x50F40` | 43 | UnwindData |  |
| 520 | `_mbslwr_l` | `0x50F70` | 43 | UnwindData |  |
| 521 | `_mbslwr_s` | `0x50FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | `_mbslwr_s_l` | `0x50FB0` | 339 | UnwindData |  |
| 523 | `_mbsnbcat` | `0x51110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `_mbsnbcat_l` | `0x51120` | 326 | UnwindData |  |
| 525 | `_mbsnbcat_s` | `0x51270` | 20 | UnwindData |  |
| 526 | `_mbsnbcat_s_l` | `0x51290` | 644 | UnwindData |  |
| 527 | `_mbsnbcmp` | `0x51520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `_mbsnbcmp_l` | `0x51530` | 297 | UnwindData |  |
| 529 | `_mbsnbcnt` | `0x51660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `_mbsnbcnt_l` | `0x51670` | 151 | UnwindData |  |
| 531 | `_mbsnbcoll` | `0x51710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | `_mbsnbcoll_l` | `0x51720` | 275 | UnwindData |  |
| 533 | `_mbsnbcpy` | `0x51840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `_mbsnbcpy_l` | `0x51850` | 242 | UnwindData |  |
| 535 | `_mbsnbcpy_s` | `0x51950` | 20 | UnwindData |  |
| 536 | `_mbsnbcpy_s_l` | `0x51970` | 488 | UnwindData |  |
| 537 | `_mbsnbicmp` | `0x51B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `_mbsnbicmp_l` | `0x51B70` | 423 | UnwindData |  |
| 539 | `_mbsnbicoll` | `0x51D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `_mbsnbicoll_l` | `0x51D30` | 255 | UnwindData |  |
| 541 | `_mbsnbset` | `0x51E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `_mbsnbset_l` | `0x51E40` | 242 | UnwindData |  |
| 543 | `_mbsnbset_s` | `0x51F40` | 20 | UnwindData |  |
| 544 | `_mbsnbset_s_l` | `0x51F60` | 584 | UnwindData |  |
| 545 | `_mbsncat` | `0x521B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | `_mbsncat_l` | `0x521C0` | 299 | UnwindData |  |
| 547 | `_mbsncat_s` | `0x522F0` | 20 | UnwindData |  |
| 548 | `_mbsncat_s_l` | `0x52310` | 580 | UnwindData |  |
| 549 | `_mbsnccnt` | `0x52560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `_mbsnccnt_l` | `0x52570` | 152 | UnwindData |  |
| 551 | `_mbsncmp` | `0x52610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `_mbsncmp_l` | `0x52620` | 256 | UnwindData |  |
| 553 | `_mbsncoll` | `0x52720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `_mbsncoll_l` | `0x52730` | 313 | UnwindData |  |
| 555 | `_mbsncpy` | `0x52870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 556 | `_mbsncpy_l` | `0x52880` | 226 | UnwindData |  |
| 557 | `_mbsncpy_s` | `0x52970` | 20 | UnwindData |  |
| 558 | `_mbsncpy_s_l` | `0x52990` | 505 | UnwindData |  |
| 559 | `_mbsnextc` | `0x52B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `_mbsnextc_l` | `0x52BA0` | 116 | UnwindData |  |
| 561 | `_mbsnicmp` | `0x52C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 562 | `_mbsnicmp_l` | `0x52C30` | 387 | UnwindData |  |
| 563 | `_mbsnicoll` | `0x52DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `_mbsnicoll_l` | `0x52DD0` | 313 | UnwindData |  |
| 565 | `_mbsninc` | `0x52F10` | 35 | UnwindData |  |
| 566 | `_mbsninc_l` | `0x52F40` | 34 | UnwindData |  |
| 567 | `_mbsnlen` | `0x52F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 568 | `_mbsnlen_l` | `0x52F80` | 152 | UnwindData |  |
| 569 | `_mbsnset` | `0x53020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `_mbsnset_l` | `0x53030` | 347 | UnwindData |  |
| 571 | `_mbsnset_s` | `0x53190` | 20 | UnwindData |  |
| 572 | `_mbsnset_s_l` | `0x531B0` | 550 | UnwindData |  |
| 573 | `_mbspbrk` | `0x533E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `_mbspbrk_l` | `0x533F0` | 222 | UnwindData |  |
| 575 | `_mbsrchr` | `0x534D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `_mbsrchr_l` | `0x534E0` | 187 | UnwindData |  |
| 577 | `_mbsrev` | `0x535A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `_mbsrev_l` | `0x535B0` | 212 | UnwindData |  |
| 579 | `_mbsset` | `0x53690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `_mbsset_l` | `0x536A0` | 212 | UnwindData |  |
| 581 | `_mbsset_s` | `0x53780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 582 | `_mbsset_s_l` | `0x53790` | 324 | UnwindData |  |
| 583 | `_mbsspn` | `0x538E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `_mbsspn_l` | `0x538F0` | 237 | UnwindData |  |
| 585 | `_mbsspnp` | `0x539E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `_mbsspnp_l` | `0x539F0` | 237 | UnwindData |  |
| 587 | `_mbsstr` | `0x53AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `_mbsstr_l` | `0x53AF0` | 249 | UnwindData |  |
| 589 | `_mbstok` | `0x53BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `_mbstok_l` | `0x53C00` | 62 | UnwindData |  |
| 591 | `_mbstok_s` | `0x53C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `_mbstok_s_l` | `0x53C50` | 434 | UnwindData |  |
| 593 | `_mbstowcs_l` | `0x54150` | 165 | UnwindData |  |
| 594 | `_mbstowcs_s_l` | `0x54200` | 182 | UnwindData |  |
| 1185 | `mbstowcs` | `0x542C0` | 154 | UnwindData |  |
| 1186 | `mbstowcs_s` | `0x54360` | 168 | UnwindData |  |
| 595 | `_mbstrlen` | `0x544F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 596 | `_mbstrlen_l` | `0x54520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `_mbstrnlen` | `0x54530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `_mbstrnlen_l` | `0x54540` | 52 | UnwindData |  |
| 599 | `_mbsupr` | `0x54580` | 43 | UnwindData |  |
| 600 | `_mbsupr_l` | `0x545B0` | 43 | UnwindData |  |
| 601 | `_mbsupr_s` | `0x545E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `_mbsupr_s_l` | `0x545F0` | 339 | UnwindData |  |
| 603 | `_mbtowc_l` | `0x548C0` | 163 | UnwindData |  |
| 1187 | `mbtowc` | `0x54970` | 152 | UnwindData |  |
| 604 | `_memccpy` | `0x54A10` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `_memicmp` | `0x54A80` | 80 | UnwindData |  |
| 606 | `_memicmp_l` | `0x54AD0` | 170 | UnwindData |  |
| 607 | `_mkdir` | `0x54B80` | 222 | UnwindData |  |
| 608 | `_mkgmtime32` | `0x55310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `_mkgmtime64` | `0x55320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 612 | `_mktime32` | `0x55330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 613 | `_mktime64` | `0x55340` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 610 | `_mktemp` | `0x555D0` | 78 | UnwindData |  |
| 611 | `_mktemp_s` | `0x55620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `_wmktemp` | `0x55630` | 79 | UnwindData |  |
| 865 | `_wmktemp_s` | `0x55680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | `_msize` | `0x55690` | 2,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 617 | `_open` | `0x55F20` | 35 | UnwindData |  |
| 672 | `_sopen` | `0x55F50` | 65 | UnwindData |  |
| 673 | `_sopen_dispatch` | `0x55FA0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `_sopen_s` | `0x560C0` | 50 | UnwindData |  |
| 866 | `_wopen` | `0x56100` | 35 | UnwindData |  |
| 878 | `_wsopen` | `0x56130` | 65 | UnwindData |  |
| 879 | `_wsopen_dispatch` | `0x56180` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `_wsopen_s` | `0x56580` | 50 | UnwindData |  |
| 619 | `_pclose` | `0x57380` | 213 | UnwindData |  |
| 621 | `_popen` | `0x57460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `_wpopen` | `0x57470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 620 | `_pipe` | `0x57480` | 676 | UnwindData |  |
| 623 | `_putch` | `0x57770` | 58 | UnwindData |  |
| 624 | `_putch_nolock` | `0x577B0` | 152 | UnwindData |  |
| 625 | `_putenv` | `0x57FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 626 | `_putenv_s` | `0x57FC0` | 56 | UnwindData |  |
| 869 | `_wputenv` | `0x58000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | `_wputenv_s` | `0x58010` | 56 | UnwindData |  |
| 627 | `_putw` | `0x58050` | 151 | UnwindData |  |
| 629 | `_putwch` | `0x58130` | 59 | UnwindData |  |
| 630 | `_putwch_nolock` | `0x58170` | 59 | UnwindData |  |
| 631 | `_putws` | `0x582A0` | 257 | UnwindData |  |
| 632 | `_query_app_type` | `0x583B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 655 | `_set_app_type` | `0x583C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 634 | `_query_new_mode` | `0x583D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 663 | `_set_new_mode` | `0x583E0` | 43 | UnwindData |  |
| 635 | `_read` | `0x589D0` | 281 | UnwindData |  |
| 636 | `_realloc_base` | `0x58F50` | 122 | UnwindData |  |
| 637 | `_recalloc` | `0x58FD0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 640 | `_resetstkoflw` | `0x59070` | 300 | UnwindData |  |
| 641 | `_rmdir` | `0x591A0` | 222 | UnwindData |  |
| 642 | `_rmtmp` | `0x592A0` | 146 | UnwindData |  |
| 649 | `_searchenv` | `0x59A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `_searchenv_s` | `0x59A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `_wsearchenv` | `0x59A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 876 | `_wsearchenv_s` | `0x59A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | `_seh_filter_dll` | `0x59A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `_seh_filter_exe` | `0x59A90` | 406 | UnwindData |  |
| 654 | `_set_abort_behavior` | `0x59C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `abort` | `0x59C50` | 86 | UnwindData |  |
| 659 | `_set_error_mode` | `0x59CB0` | 64 | UnwindData |  |
| 666 | `_seterrormode` | `0x59CF0` | 2,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `_splitpath` | `0x5A780` | 108 | UnwindData |  |
| 684 | `_splitpath_s` | `0x5A7F0` | 99 | UnwindData |  |
| 889 | `_wsplitpath` | `0x5A860` | 108 | UnwindData |  |
| 890 | `_wsplitpath_s` | `0x5A8D0` | 99 | UnwindData |  |
| 690 | `_strcoll_l` | `0x5A940` | 199 | UnwindData |  |
| 1259 | `strcoll` | `0x5AA10` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `_strdate` | `0x5AC80` | 36 | UnwindData |  |
| 692 | `_strdate_s` | `0x5ACB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `_wstrdate` | `0x5ACC0` | 36 | UnwindData |  |
| 896 | `_wstrdate_s` | `0x5ACF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `_mbsdup` | `0x5AD00` | 117 | UnwindData |  |
| 693 | `_strdup` | `0x5AD00` | 117 | UnwindData |  |
| 697 | `_stricmp` | `0x5ADC0` | 70 | UnwindData |  |
| 698 | `_stricmp_l` | `0x5AE10` | 136 | UnwindData |  |
| 699 | `_stricoll` | `0x5AEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 700 | `_stricoll_l` | `0x5AEC0` | 184 | UnwindData |  |
| 701 | `_strlwr` | `0x5B1A0` | 94 | UnwindData |  |
| 702 | `_strlwr_l` | `0x5B200` | 30 | UnwindData |  |
| 703 | `_strlwr_s` | `0x5B220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `_strlwr_s_l` | `0x5B230` | 75 | UnwindData |  |
| 705 | `_strncoll` | `0x5B280` | 79 | UnwindData |  |
| 706 | `_strncoll_l` | `0x5B2D0` | 255 | UnwindData |  |
| 707 | `_strnicmp` | `0x5B420` | 79 | UnwindData |  |
| 708 | `_strnicmp_l` | `0x5B470` | 173 | UnwindData |  |
| 709 | `_strnicoll` | `0x5B520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `_strnicoll_l` | `0x5B540` | 256 | UnwindData |  |
| 711 | `_strnset` | `0x5B640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `_strnset_s` | `0x5B660` | 116 | UnwindData |  |
| 713 | `_strrev` | `0x5B6E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `_strset` | `0x5B720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 715 | `_strset_s` | `0x5B730` | 73 | UnwindData |  |
| 716 | `_strtime` | `0x5B9B0` | 36 | UnwindData |  |
| 717 | `_strtime_s` | `0x5B9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `_wstrtime` | `0x5B9F0` | 36 | UnwindData |  |
| 898 | `_wstrtime_s` | `0x5BA20` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 718 | `_strtod_l` | `0x5BD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 724 | `_strtold_l` | `0x5BD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `_strtof_l` | `0x5BD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 806 | `_wcstod_l` | `0x5BD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 812 | `_wcstold_l` | `0x5BD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 807 | `_wcstof_l` | `0x5BDA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1275 | `strtod` | `0x5BDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1281 | `strtold` | `0x5BDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1276 | `strtof` | `0x5BDC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `wcstod` | `0x5BDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `wcstold` | `0x5BDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `wcstof` | `0x5BDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 720 | `_strtoi64` | `0x5BDF0` | 179 | UnwindData |  |
| 1277 | `strtoimax` | `0x5BDF0` | 179 | UnwindData |  |
| 1282 | `strtoll` | `0x5BDF0` | 179 | UnwindData |  |
| 721 | `_strtoi64_l` | `0x5BEB0` | 190 | UnwindData |  |
| 722 | `_strtoimax_l` | `0x5BEB0` | 190 | UnwindData |  |
| 725 | `_strtoll_l` | `0x5BEB0` | 190 | UnwindData |  |
| 723 | `_strtol_l` | `0x5BF70` | 188 | UnwindData |  |
| 726 | `_strtoui64` | `0x5C030` | 179 | UnwindData |  |
| 1284 | `strtoull` | `0x5C030` | 179 | UnwindData |  |
| 1285 | `strtoumax` | `0x5C030` | 179 | UnwindData |  |
| 727 | `_strtoui64_l` | `0x5C0F0` | 190 | UnwindData |  |
| 729 | `_strtoull_l` | `0x5C0F0` | 190 | UnwindData |  |
| 730 | `_strtoumax_l` | `0x5C0F0` | 190 | UnwindData |  |
| 728 | `_strtoul_l` | `0x5C1B0` | 188 | UnwindData |  |
| 808 | `_wcstoi64` | `0x5C270` | 179 | UnwindData |  |
| 1333 | `wcstoimax` | `0x5C270` | 179 | UnwindData |  |
| 1338 | `wcstoll` | `0x5C270` | 179 | UnwindData |  |
| 809 | `_wcstoi64_l` | `0x5C330` | 190 | UnwindData |  |
| 810 | `_wcstoimax_l` | `0x5C330` | 190 | UnwindData |  |
| 813 | `_wcstoll_l` | `0x5C330` | 190 | UnwindData |  |
| 811 | `_wcstol_l` | `0x5C3F0` | 188 | UnwindData |  |
| 816 | `_wcstoui64` | `0x5C4B0` | 179 | UnwindData |  |
| 1342 | `wcstoull` | `0x5C4B0` | 179 | UnwindData |  |
| 1343 | `wcstoumax` | `0x5C4B0` | 179 | UnwindData |  |
| 817 | `_wcstoui64_l` | `0x5C570` | 190 | UnwindData |  |
| 819 | `_wcstoull_l` | `0x5C570` | 190 | UnwindData |  |
| 820 | `_wcstoumax_l` | `0x5C570` | 190 | UnwindData |  |
| 818 | `_wcstoul_l` | `0x5C630` | 188 | UnwindData |  |
| 1280 | `strtol` | `0x5C6F0` | 177 | UnwindData |  |
| 1283 | `strtoul` | `0x5C7B0` | 177 | UnwindData |  |
| 1336 | `wcstol` | `0x5C870` | 177 | UnwindData |  |
| 1341 | `wcstoul` | `0x5C930` | 177 | UnwindData |  |
| 731 | `_strupr` | `0x5CC00` | 94 | UnwindData |  |
| 732 | `_strupr_l` | `0x5CC60` | 30 | UnwindData |  |
| 733 | `_strupr_s` | `0x5CC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `_strupr_s_l` | `0x5CC90` | 75 | UnwindData |  |
| 735 | `_strxfrm_l` | `0x5CCE0` | 377 | UnwindData |  |
| 1286 | `strxfrm` | `0x5CE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 736 | `_swab` | `0x5CE70` | 89 | UnwindData |  |
| 737 | `_tell` | `0x5CED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 738 | `_telli64` | `0x5CEE0` | 1,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 739 | `_tempnam` | `0x5D660` | 26 | UnwindData |  |
| 900 | `_wtempnam` | `0x5D680` | 26 | UnwindData |  |
| 740 | `_time32` | `0x5D6A0` | 106 | UnwindData |  |
| 741 | `_time64` | `0x5D710` | 109 | UnwindData |  |
| 742 | `_timespec32_get` | `0x5D780` | 152 | UnwindData |  |
| 743 | `_timespec64_get` | `0x5D820` | 153 | UnwindData |  |
| 744 | `_tolower` | `0x5D8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `_tolower_l` | `0x5D8D0` | 314 | UnwindData |  |
| 746 | `_toupper` | `0x5DA10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `_toupper_l` | `0x5DA20` | 314 | UnwindData |  |
| 1300 | `tolower` | `0x5DB60` | 42 | UnwindData |  |
| 1301 | `toupper` | `0x5DB90` | 42 | UnwindData |  |
| 748 | `_towlower_l` | `0x5DBC0` | 245 | UnwindData |  |
| 1303 | `towlower` | `0x5DCC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `_towupper_l` | `0x5DCD0` | 243 | UnwindData |  |
| 1304 | `towupper` | `0x5DDD0` | 3,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `_tzset` | `0x5E9B0` | 40 | UnwindData |  |
| 759 | `_umask` | `0x5E9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 760 | `_umask_s` | `0x5EA00` | 61 | UnwindData |  |
| 761 | `_ungetc_nolock` | `0x5EA40` | 288 | UnwindData |  |
| 1308 | `ungetc` | `0x5EB60` | 88 | UnwindData |  |
| 764 | `_ungetwc_nolock` | `0x5ECF0` | 313 | UnwindData |  |
| 1309 | `ungetwc` | `0x5EE30` | 94 | UnwindData |  |
| 767 | `_unlink` | `0x5EE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `remove` | `0x5EEA0` | 222 | UnwindData |  |
| 773 | `_waccess` | `0x5EF80` | 18 | UnwindData |  |
| 774 | `_waccess_s` | `0x5EFA0` | 170 | UnwindData |  |
| 775 | `_wasctime` | `0x5F510` | 134 | UnwindData |  |
| 776 | `_wasctime_s` | `0x5F5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `asctime` | `0x5F5B0` | 134 | UnwindData |  |
| 927 | `asctime_s` | `0x5F640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `_wchmod` | `0x5F650` | 155 | UnwindData |  |
| 782 | `_wcscoll_l` | `0x5F6F0` | 188 | UnwindData |  |
| 1315 | `wcscoll` | `0x5F7B0` | 101 | UnwindData |  |
| 783 | `_wcsdup` | `0x5F820` | 130 | UnwindData |  |
| 784 | `_wcserror` | `0x5F8B0` | 176 | UnwindData |  |
| 785 | `_wcserror_s` | `0x5F960` | 143 | UnwindData |  |
| 1263 | `strerror` | `0x5F9F0` | 157 | UnwindData |  |
| 1264 | `strerror_s` | `0x5FA90` | 139 | UnwindData |  |
| 787 | `_wcsicmp` | `0x5FB60` | 70 | UnwindData |  |
| 788 | `_wcsicmp_l` | `0x5FBB0` | 295 | UnwindData |  |
| 789 | `_wcsicoll` | `0x5FCE0` | 70 | UnwindData |  |
| 790 | `_wcsicoll_l` | `0x5FD30` | 169 | UnwindData |  |
| 791 | `_wcslwr` | `0x5FFE0` | 102 | UnwindData |  |
| 792 | `_wcslwr_l` | `0x60050` | 30 | UnwindData |  |
| 793 | `_wcslwr_s` | `0x60070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `_wcslwr_s_l` | `0x60080` | 75 | UnwindData |  |
| 795 | `_wcsncoll` | `0x600D0` | 79 | UnwindData |  |
| 796 | `_wcsncoll_l` | `0x60120` | 214 | UnwindData |  |
| 797 | `_wcsnicmp` | `0x60250` | 70 | UnwindData |  |
| 798 | `_wcsnicmp_l` | `0x602A0` | 335 | UnwindData |  |
| 799 | `_wcsnicoll` | `0x603F0` | 79 | UnwindData |  |
| 800 | `_wcsnicoll_l` | `0x60440` | 240 | UnwindData |  |
| 801 | `_wcsnset` | `0x60530` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `_wcsnset_s` | `0x60560` | 122 | UnwindData |  |
| 803 | `_wcsrev` | `0x605E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 804 | `_wcsset` | `0x60620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `_wcsset_s` | `0x60640` | 78 | UnwindData |  |
| 814 | `_wcstombs_l` | `0x60AF0` | 165 | UnwindData |  |
| 815 | `_wcstombs_s_l` | `0x60BA0` | 182 | UnwindData |  |
| 1339 | `wcstombs` | `0x60C60` | 154 | UnwindData |  |
| 1340 | `wcstombs_s` | `0x60D00` | 168 | UnwindData |  |
| 821 | `_wcsupr` | `0x60FA0` | 102 | UnwindData |  |
| 822 | `_wcsupr_l` | `0x61010` | 30 | UnwindData |  |
| 823 | `_wcsupr_s` | `0x61030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | `_wcsupr_s_l` | `0x61040` | 75 | UnwindData |  |
| 825 | `_wcsxfrm_l` | `0x61090` | 363 | UnwindData |  |
| 1344 | `wcsxfrm` | `0x61200` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `_wctomb_l` | `0x613C0` | 235 | UnwindData |  |
| 831 | `_wctomb_s_l` | `0x614B0` | 173 | UnwindData |  |
| 1346 | `wctomb` | `0x61560` | 197 | UnwindData |  |
| 1347 | `wctomb_s` | `0x61630` | 159 | UnwindData |  |
| 853 | `_wfreopen` | `0x618D0` | 47 | UnwindData |  |
| 854 | `_wfreopen_s` | `0x61900` | 22 | UnwindData |  |
| 1094 | `freopen` | `0x61920` | 47 | UnwindData |  |
| 1095 | `freopen_s` | `0x61950` | 22 | UnwindData |  |
| 863 | `_wmkdir` | `0x61970` | 41 | UnwindData |  |
| 867 | `_wperror` | `0x619A0` | 202 | UnwindData |  |
| 871 | `_wremove` | `0x61A70` | 39 | UnwindData |  |
| 913 | `_wunlink` | `0x61AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `_wrename` | `0x61AB0` | 45 | UnwindData |  |
| 873 | `_write` | `0x62340` | 152 | UnwindData |  |
| 874 | `_wrmdir` | `0x62810` | 39 | UnwindData |  |
| 899 | `_wsystem` | `0x62840` | 327 | UnwindData |  |
| 1287 | `system` | `0x62990` | 327 | UnwindData |  |
| 901 | `_wtmpnam` | `0x63450` | 38 | UnwindData |  |
| 902 | `_wtmpnam_s` | `0x63480` | 53 | UnwindData |  |
| 1296 | `tmpfile` | `0x634C0` | 35 | UnwindData |  |
| 1297 | `tmpfile_s` | `0x634F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1298 | `tmpnam` | `0x63500` | 38 | UnwindData |  |
| 1299 | `tmpnam_s` | `0x63530` | 53 | UnwindData |  |
| 921 | `acos` | `0x63570` | 670 | UnwindData |  |
| 922 | `acosf` | `0x63810` | 556 | UnwindData |  |
| 923 | `acosh` | `0x63A40` | 194 | UnwindData |  |
| 924 | `acoshf` | `0x63B10` | 189 | UnwindData |  |
| 925 | `acoshl` | `0x63BD0` | 194 | UnwindData |  |
| 928 | `asin` | `0x63CA0` | 644 | UnwindData |  |
| 929 | `asinf` | `0x63F30` | 490 | UnwindData |  |
| 930 | `asinh` | `0x64120` | 200 | UnwindData |  |
| 931 | `asinhf` | `0x641F0` | 194 | UnwindData |  |
| 932 | `asinhl` | `0x642C0` | 200 | UnwindData |  |
| 933 | `atan` | `0x64390` | 533 | UnwindData |  |
| 934 | `atan2` | `0x645B0` | 1,774 | UnwindData |  |
| 935 | `atan2f` | `0x64CA0` | 1,015 | UnwindData |  |
| 936 | `atanf` | `0x650A0` | 492 | UnwindData |  |
| 937 | `atanh` | `0x65290` | 193 | UnwindData |  |
| 938 | `atanhf` | `0x65360` | 185 | UnwindData |  |
| 939 | `atanhl` | `0x65420` | 193 | UnwindData |  |
| 944 | `bsearch` | `0x654F0` | 277 | UnwindData |  |
| 945 | `bsearch_s` | `0x65610` | 287 | UnwindData |  |
| 946 | `btowc` | `0x65CD0` | 216 | UnwindData |  |
| 1179 | `mbrlen` | `0x65DB0` | 197 | UnwindData |  |
| 1182 | `mbrtowc` | `0x65E80` | 231 | UnwindData |  |
| 1183 | `mbsrtowcs` | `0x65F70` | 161 | UnwindData |  |
| 1184 | `mbsrtowcs_s` | `0x66020` | 353 | UnwindData |  |
| 947 | `c16rtomb` | `0x66230` | 154 | UnwindData |  |
| 948 | `c32rtomb` | `0x66370` | 154 | UnwindData |  |
| 949 | `cabs` | `0x66410` | 63 | UnwindData |  |
| 950 | `cabsf` | `0x66450` | 64 | UnwindData |  |
| 951 | `cabsl` | `0x66490` | 63 | UnwindData |  |
| 952 | `cacos` | `0x664D0` | 811 | UnwindData |  |
| 953 | `cacosf` | `0x66800` | 696 | UnwindData |  |
| 954 | `cacosh` | `0x66AC0` | 876 | UnwindData |  |
| 955 | `cacoshf` | `0x66E30` | 760 | UnwindData |  |
| 956 | `cacoshl` | `0x67130` | 876 | UnwindData |  |
| 957 | `cacosl` | `0x674A0` | 811 | UnwindData |  |
| 958 | `calloc` | `0x677D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 959 | `carg` | `0x677E0` | 66 | UnwindData |  |
| 960 | `cargf` | `0x67830` | 67 | UnwindData |  |
| 961 | `cargl` | `0x67880` | 63 | UnwindData |  |
| 962 | `casin` | `0x678C0` | 192 | UnwindData |  |
| 963 | `casinf` | `0x67980` | 122 | UnwindData |  |
| 964 | `casinh` | `0x67A00` | 816 | UnwindData |  |
| 965 | `casinhf` | `0x67D30` | 687 | UnwindData |  |
| 966 | `casinhl` | `0x67FE0` | 816 | UnwindData |  |
| 967 | `casinl` | `0x68310` | 192 | UnwindData |  |
| 968 | `catan` | `0x683D0` | 192 | UnwindData |  |
| 969 | `catanf` | `0x68490` | 122 | UnwindData |  |
| 970 | `catanh` | `0x68510` | 877 | UnwindData |  |
| 971 | `catanhf` | `0x68880` | 822 | UnwindData |  |
| 972 | `catanhl` | `0x68BC0` | 877 | UnwindData |  |
| 973 | `catanl` | `0x68F30` | 192 | UnwindData |  |
| 974 | `cbrt` | `0x68FF0` | 379 | UnwindData |  |
| 975 | `cbrtf` | `0x69170` | 336 | UnwindData |  |
| 976 | `cbrtl` | `0x692C0` | 379 | UnwindData |  |
| 977 | `ccos` | `0x69440` | 118 | UnwindData |  |
| 978 | `ccosf` | `0x694C0` | 79 | UnwindData |  |
| 979 | `ccosh` | `0x69610` | 445 | UnwindData |  |
| 980 | `ccoshf` | `0x698D0` | 373 | UnwindData |  |
| 981 | `ccoshl` | `0x69B40` | 445 | UnwindData |  |
| 982 | `ccosl` | `0x69D00` | 118 | UnwindData |  |
| 983 | `ceil` | `0x69D80` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 984 | `ceilf` | `0x69E50` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `cexp` | `0x69EE0` | 516 | UnwindData |  |
| 986 | `cexpf` | `0x6A0F0` | 475 | UnwindData |  |
| 987 | `cexpl` | `0x6A2D0` | 516 | UnwindData |  |
| 988 | `cimag` | `0x6A4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `cimagl` | `0x6A4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `cimagf` | `0x6A4F0` | 47 | UnwindData |  |
| 991 | `clearerr` | `0x6A520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `clearerr_s` | `0x6A530` | 168 | UnwindData |  |
| 993 | `clock` | `0x6A640` | 97 | UnwindData |  |
| 994 | `clog` | `0x6A6B0` | 558 | UnwindData |  |
| 995 | `clog10` | `0x6A8E0` | 81 | UnwindData |  |
| 996 | `clog10f` | `0x6A940` | 29 | UnwindData |  |
| 997 | `clog10l` | `0x6A960` | 81 | UnwindData |  |
| 998 | `clogf` | `0x6A9C0` | 509 | UnwindData |  |
| 999 | `clogl` | `0x6ABC0` | 558 | UnwindData |  |
| 1000 | `conj` | `0x6ADF0` | 98 | UnwindData |  |
| 1002 | `conjl` | `0x6ADF0` | 98 | UnwindData |  |
| 1001 | `conjf` | `0x6AE60` | 75 | UnwindData |  |
| 1003 | `copysign` | `0x6AEB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `copysignl` | `0x6AEB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `copysignf` | `0x6AEF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `cos` | `0x6AF30` | 1,402 | UnwindData |  |
| 1007 | `cosf` | `0x6B4B0` | 1,279 | UnwindData |  |
| 1008 | `cosh` | `0x6B9B0` | 880 | UnwindData |  |
| 1009 | `coshf` | `0x6BE50` | 656 | UnwindData |  |
| 1016 | `creal` | `0x6C210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `creall` | `0x6C210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `crealf` | `0x6C220` | 46 | UnwindData |  |
| 1019 | `csin` | `0x6C250` | 192 | UnwindData |  |
| 1020 | `csinf` | `0x6C310` | 122 | UnwindData |  |
| 1021 | `csinh` | `0x6C530` | 352 | UnwindData |  |
| 1022 | `csinhf` | `0x6C810` | 287 | UnwindData |  |
| 1023 | `csinhl` | `0x6CAD0` | 352 | UnwindData |  |
| 1024 | `csinl` | `0x6CC30` | 192 | UnwindData |  |
| 1025 | `csqrt` | `0x6CEF0` | 487 | UnwindData |  |
| 1026 | `csqrtf` | `0x6D2D0` | 440 | UnwindData |  |
| 1027 | `csqrtl` | `0x6D680` | 487 | UnwindData |  |
| 1028 | `ctan` | `0x6D870` | 192 | UnwindData |  |
| 1029 | `ctanf` | `0x6D930` | 122 | UnwindData |  |
| 1030 | `ctanh` | `0x6D9B0` | 415 | UnwindData |  |
| 1031 | `ctanhf` | `0x6DB50` | 360 | UnwindData |  |
| 1032 | `ctanhl` | `0x6DCC0` | 415 | UnwindData |  |
| 1033 | `ctanl` | `0x6DE60` | 192 | UnwindData |  |
| 1034 | `div` | `0x6DF20` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `ldiv` | `0x6DF20` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `erf` | `0x6DFB0` | 365 | UnwindData |  |
| 1039 | `erff` | `0x6E1B0` | 286 | UnwindData |  |
| 1040 | `erfl` | `0x6E350` | 365 | UnwindData |  |
| 1042 | `exp` | `0x6E4C0` | 1,013 | UnwindData |  |
| 1046 | `expf` | `0x6E8C0` | 679 | UnwindData |  |
| 1047 | `expm1` | `0x6EB70` | 288 | UnwindData |  |
| 1048 | `expm1f` | `0x6EC90` | 209 | UnwindData |  |
| 1049 | `expm1l` | `0x6ED70` | 288 | UnwindData |  |
| 1050 | `fabs` | `0x6EE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `fdim` | `0x6EEA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `fdiml` | `0x6EEA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1053 | `fdimf` | `0x6EED0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1055 | `feclearexcept` | `0x6EF00` | 82 | UnwindData |  |
| 1056 | `fegetenv` | `0x6EF60` | 32 | UnwindData |  |
| 1057 | `fegetexceptflag` | `0x6EF80` | 65 | UnwindData |  |
| 1059 | `feholdexcept` | `0x6EFD0` | 80 | UnwindData |  |
| 1060 | `feof` | `0x6F020` | 43 | UnwindData |  |
| 1061 | `ferror` | `0x6F050` | 43 | UnwindData |  |
| 1062 | `fesetenv` | `0x6F080` | 76 | UnwindData |  |
| 1063 | `fesetexceptflag` | `0x6F0D0` | 121 | UnwindData |  |
| 1064 | `fesetround` | `0x6F150` | 110 | UnwindData |  |
| 1065 | `fetestexcept` | `0x6F1C0` | 33 | UnwindData |  |
| 1068 | `fgetpos` | `0x6F1F0` | 75 | UnwindData |  |
| 1069 | `fgets` | `0x6F3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `fgetws` | `0x6F3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `floor` | `0x6F3F0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `floorf` | `0x6F4A0` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `fma` | `0x6FC40` | 687 | UnwindData |  |
| 1075 | `fmaf` | `0x705A0` | 669 | UnwindData |  |
| 1076 | `fmal` | `0x70F10` | 687 | UnwindData |  |
| 1077 | `fmax` | `0x711C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1079 | `fmaxl` | `0x711C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `fmaxf` | `0x71200` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1080 | `fmin` | `0x71240` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1082 | `fminl` | `0x71240` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1081 | `fminf` | `0x71280` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1083 | `fmod` | `0x712C0` | 724 | UnwindData |  |
| 1084 | `fmodf` | `0x715A0` | 577 | UnwindData |  |
| 1088 | `fputs` | `0x718B0` | 420 | UnwindData |  |
| 1090 | `fputws` | `0x71B30` | 253 | UnwindData |  |
| 1093 | `free` | `0x71C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `frexp` | `0x71C50` | 248 | UnwindData |  |
| 1098 | `fsetpos` | `0x71D50` | 53 | UnwindData |  |
| 1110 | `ilogb` | `0x71D90` | 70 | UnwindData |  |
| 1111 | `ilogbf` | `0x71DE0` | 70 | UnwindData |  |
| 1112 | `ilogbl` | `0x71E30` | 70 | UnwindData |  |
| 1114 | `imaxdiv` | `0x71E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `ldexp` | `0x71EA0` | 366 | UnwindData |  |
| 1150 | `lldiv` | `0x72010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `llrint` | `0x72030` | 121 | UnwindData |  |
| 1152 | `llrintf` | `0x720B0` | 118 | UnwindData |  |
| 1153 | `llrintl` | `0x72130` | 121 | UnwindData |  |
| 1154 | `llround` | `0x721B0` | 90 | UnwindData |  |
| 1155 | `llroundf` | `0x72210` | 88 | UnwindData |  |
| 1156 | `llroundl` | `0x72270` | 90 | UnwindData |  |
| 1157 | `localeconv` | `0x722D0` | 51 | UnwindData |  |
| 1158 | `log` | `0x72310` | 1,323 | UnwindData |  |
| 1159 | `log10` | `0x72840` | 1,451 | UnwindData |  |
| 1160 | `log10f` | `0x72DF0` | 1,237 | UnwindData |  |
| 1161 | `log1p` | `0x732D0` | 201 | UnwindData |  |
| 1162 | `log1pf` | `0x733A0` | 197 | UnwindData |  |
| 1163 | `log1pl` | `0x73470` | 201 | UnwindData |  |
| 1164 | `log2` | `0x73540` | 807 | UnwindData |  |
| 1167 | `logb` | `0x73870` | 109 | UnwindData |  |
| 1168 | `logbf` | `0x738E0` | 108 | UnwindData |  |
| 1169 | `logbl` | `0x73950` | 109 | UnwindData |  |
| 1170 | `logf` | `0x739C0` | 1,014 | UnwindData |  |
| 1171 | `lrint` | `0x73DC0` | 120 | UnwindData |  |
| 1172 | `lrintf` | `0x73E40` | 117 | UnwindData |  |
| 1173 | `lrintl` | `0x73EC0` | 120 | UnwindData |  |
| 1174 | `lround` | `0x73F40` | 89 | UnwindData |  |
| 1175 | `lroundf` | `0x73FA0` | 87 | UnwindData |  |
| 1176 | `lroundl` | `0x74000` | 89 | UnwindData |  |
| 1177 | `malloc` | `0x74060` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `mbrtoc16` | `0x74160` | 161 | UnwindData |  |
| 1181 | `mbrtoc32` | `0x743E0` | 161 | UnwindData |  |
| 1188 | `memcpy_s` | `0x74490` | 135 | UnwindData |  |
| 1189 | `memmove_s` | `0x74520` | 81 | UnwindData |  |
| 1191 | `modf` | `0x74580` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1192 | `modff` | `0x74660` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `nearbyint` | `0x74710` | 41 | UnwindData |  |
| 1197 | `nearbyintf` | `0x74740` | 41 | UnwindData |  |
| 1198 | `nearbyintl` | `0x74770` | 41 | UnwindData |  |
| 1199 | `nextafter` | `0x747A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1200 | `nextafterf` | `0x747B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1201 | `nextafterl` | `0x747C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `nexttoward` | `0x747D0` | 358 | UnwindData |  |
| 1203 | `nexttowardf` | `0x74940` | 329 | UnwindData |  |
| 1204 | `nexttowardl` | `0x74A90` | 358 | UnwindData |  |
| 1205 | `norm` | `0x74C00` | 78 | UnwindData |  |
| 1207 | `norml` | `0x74C00` | 78 | UnwindData |  |
| 1206 | `normf` | `0x74C50` | 69 | UnwindData |  |
| 1208 | `perror` | `0x74D70` | 138 | UnwindData |  |
| 1209 | `pow` | `0x74E00` | 5,777 | UnwindData |  |
| 1210 | `powf` | `0x764A0` | 3,782 | UnwindData |  |
| 1213 | `puts` | `0x77450` | 420 | UnwindData |  |
| 1216 | `qsort` | `0x77600` | 91 | UnwindData |  |
| 1217 | `qsort_s` | `0x77A20` | 106 | UnwindData |  |
| 1220 | `rand` | `0x77EA0` | 41 | UnwindData |  |
| 1255 | `srand` | `0x77ED0` | 22 | UnwindData |  |
| 1221 | `rand_s` | `0x77EF0` | 76 | UnwindData |  |
| 1222 | `realloc` | `0x77F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `remainder` | `0x77F50` | 936 | UnwindData |  |
| 1224 | `remainderf` | `0x78300` | 643 | UnwindData |  |
| 1225 | `remainderl` | `0x78590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `remquo` | `0x785A0` | 491 | UnwindData |  |
| 1228 | `remquof` | `0x78790` | 482 | UnwindData |  |
| 1229 | `remquol` | `0x78980` | 491 | UnwindData |  |
| 1230 | `rename` | `0x78B70` | 319 | UnwindData |  |
| 1231 | `rewind` | `0x78DA0` | 138 | UnwindData |  |
| 1232 | `rint` | `0x78F60` | 75 | UnwindData |  |
| 1233 | `rintf` | `0x790E0` | 74 | UnwindData |  |
| 1234 | `rintl` | `0x79260` | 75 | UnwindData |  |
| 1235 | `round` | `0x792B0` | 101 | UnwindData |  |
| 1236 | `roundf` | `0x79320` | 101 | UnwindData |  |
| 1237 | `roundl` | `0x79390` | 101 | UnwindData |  |
| 1238 | `scalbln` | `0x79400` | 90 | UnwindData |  |
| 1241 | `scalbn` | `0x79400` | 90 | UnwindData |  |
| 1239 | `scalblnf` | `0x79460` | 90 | UnwindData |  |
| 1242 | `scalbnf` | `0x79460` | 90 | UnwindData |  |
| 1240 | `scalblnl` | `0x794C0` | 90 | UnwindData |  |
| 1243 | `scalbnl` | `0x794C0` | 90 | UnwindData |  |
| 1245 | `setbuf` | `0x79520` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1246 | `setlocale` | `0x79830` | 76 | UnwindData |  |
| 1247 | `setvbuf` | `0x799B0` | 308 | UnwindData |  |
| 1249 | `sin` | `0x79AF0` | 1,386 | UnwindData |  |
| 1250 | `sinf` | `0x7A060` | 1,782 | UnwindData |  |
| 1251 | `sinh` | `0x7A760` | 940 | UnwindData |  |
| 1252 | `sinhf` | `0x7AC30` | 676 | UnwindData |  |
| 1253 | `sqrt` | `0x7B000` | 201 | UnwindData |  |
| 1254 | `sqrtf` | `0x7B0D0` | 159 | UnwindData |  |
| 1256 | `strcat` | `0x7B180` | 144 | UnwindData |  |
| 1260 | `strcpy` | `0x7B220` | 183 | UnwindData |  |
| 1257 | `strcat_s` | `0x7B2E0` | 118 | UnwindData |  |
| 1258 | `strcmp` | `0x7B370` | 103 | UnwindData |  |
| 1261 | `strcpy_s` | `0x7B3E0` | 95 | UnwindData |  |
| 1262 | `strcspn` | `0x7B4E0` | 202 | UnwindData |  |
| 1266 | `strlen` | `0x7B8C0` | 168 | UnwindData |  |
| 1267 | `strncat` | `0x7B980` | 405 | UnwindData |  |
| 1268 | `strncat_s` | `0x7BB20` | 237 | UnwindData |  |
| 1269 | `strncmp` | `0x7BC20` | 125 | UnwindData |  |
| 1270 | `strncpy` | `0x7BCB0` | 354 | UnwindData |  |
| 1271 | `strncpy_s` | `0x7BE20` | 211 | UnwindData |  |
| 1272 | `strnlen` | `0x7BF00` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `wcslen` | `0x7C050` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `wcsnlen` | `0x7C180` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1273 | `strpbrk` | `0x7C400` | 968 | UnwindData |  |
| 1274 | `strspn` | `0x7C890` | 202 | UnwindData |  |
| 1278 | `strtok` | `0x7CC60` | 46 | UnwindData |  |
| 1279 | `strtok_s` | `0x7CDB0` | 56 | UnwindData |  |
| 1288 | `tan` | `0x7CDF0` | 1,459 | UnwindData |  |
| 1289 | `tanf` | `0x7D590` | 1,651 | UnwindData |  |
| 1290 | `tanh` | `0x7DD30` | 606 | UnwindData |  |
| 1291 | `tanhf` | `0x7DF90` | 652 | UnwindData |  |
| 1293 | `tgamma` | `0x7EB60` | 584 | UnwindData |  |
| 1294 | `tgammaf` | `0x7F610` | 578 | UnwindData |  |
| 1295 | `tgammal` | `0x801A0` | 584 | UnwindData |  |
| 1302 | `towctrans` | `0x803F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1348 | `wctrans` | `0x80400` | 115 | UnwindData |  |
| 1305 | `trunc` | `0x80480` | 33 | UnwindData |  |
| 1306 | `truncf` | `0x804B0` | 33 | UnwindData |  |
| 1307 | `truncl` | `0x804E0` | 33 | UnwindData |  |
| 1310 | `wcrtomb` | `0x80970` | 58 | UnwindData |  |
| 1311 | `wcrtomb_s` | `0x809B0` | 270 | UnwindData |  |
| 1328 | `wcsrtombs` | `0x80AC0` | 161 | UnwindData |  |
| 1329 | `wcsrtombs_s` | `0x80B70` | 379 | UnwindData |  |
| 1345 | `wctob` | `0x80CF0` | 251 | UnwindData |  |
| 1312 | `wcscat` | `0x80DF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `wcscat_s` | `0x80E20` | 127 | UnwindData |  |
| 1314 | `wcscmp` | `0x80EA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1316 | `wcscpy` | `0x80EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `wcscpy_s` | `0x80F00` | 101 | UnwindData |  |
| 1318 | `wcscspn` | `0x80F70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `wcsncat` | `0x80FB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1322 | `wcsncat_s` | `0x81000` | 253 | UnwindData |  |
| 1323 | `wcsncmp` | `0x81100` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1324 | `wcsncpy` | `0x81130` | 72 | UnwindData |  |
| 1325 | `wcsncpy_s` | `0x81180` | 228 | UnwindData |  |
| 1327 | `wcspbrk` | `0x81270` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `wcsspn` | `0x812B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `wcstok` | `0x81300` | 57 | UnwindData |  |
| 1335 | `wcstok_s` | `0x813F0` | 56 | UnwindData |  |
| 1349 | `wctype` | `0x81430` | 115 | UnwindData |  |
| 1350 | `wmemcpy_s` | `0x814B0` | 122 | UnwindData |  |
| 1351 | `wmemmove_s` | `0x81530` | 82 | UnwindData |  |
| 1190 | `memset` | `0x954B0` | 400 | UnwindData |  |
| 832 | `_wctype` | `0x9D820` | 148,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `_mbcasemap` | `0xC1DE8` | 0 | Indeterminate |  |
