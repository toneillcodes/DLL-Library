# Binary Specification: ucrtbase_clr0400.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ucrtbase_clr0400.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f5189277b5ac83b754462f259188b0e876706cec5a56bf6f5c35539f1d6510cd`
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
| 4 | `_Exit` | `0x1600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `_exit` | `0x1600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `_c_exit` | `0x1620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `_cexit` | `0x1630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `_register_thread_local_exe_atexit_callback` | `0x1650` | 62 | UnwindData |  |
| 1041 | `exit` | `0x1690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1218 | `quick_exit` | `0x16A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `_FCbuild` | `0x16B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `cprojf` | `0x16C0` | 162 | UnwindData |  |
| 6 | `_FCmulcc` | `0x1770` | 155 | UnwindData |  |
| 7 | `_FCmulcr` | `0x1810` | 90 | UnwindData |  |
| 1011 | `cpowf` | `0x1870` | 177 | UnwindData |  |
| 8 | `_Getdays` | `0x1C60` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `_Getmonths` | `0x1DB0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `_Gettnames` | `0x1F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `_Strftime` | `0x1F20` | 30 | UnwindData |  |
| 696 | `_strftime_l` | `0x20B0` | 30 | UnwindData |  |
| 1265 | `strftime` | `0x20D0` | 26 | UnwindData |  |
| 1015 | `cprojl` | `0x20F0` | 190 | UnwindData |  |
| 1012 | `cpowl` | `0x21B0` | 301 | UnwindData |  |
| 15 | `_W_Getdays` | `0x3990` | 395 | UnwindData |  |
| 16 | `_W_Getmonths` | `0x3B20` | 395 | UnwindData |  |
| 17 | `_W_Gettnames` | `0x3CB0` | 1,728 | UnwindData |  |
| 18 | `_Wcsftime` | `0x4370` | 30 | UnwindData |  |
| 786 | `_wcsftime_l` | `0x4520` | 30 | UnwindData |  |
| 1319 | `wcsftime` | `0x4540` | 26 | UnwindData |  |
| 19 | `___lc_codepage_func` | `0x4560` | 47 | UnwindData |  |
| 20 | `___lc_collate_cp_func` | `0x4590` | 47 | UnwindData |  |
| 21 | `___lc_locale_name_func` | `0x45C0` | 50 | UnwindData |  |
| 22 | `___mb_cur_max_func` | `0x4600` | 47 | UnwindData |  |
| 23 | `___mb_cur_max_l_func` | `0x4630` | 1,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `__acrt_iob_func` | `0x4DD0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `_get_stream_buffer_pointers` | `0x4E50` | 71 | UnwindData |  |
| 450 | `_lock_file` | `0x4EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `_unlock_file` | `0x4EB0` | 36,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `__conio_common_vcprintf` | `0xDEE0` | 311 | UnwindData |  |
| 26 | `__conio_common_vcprintf_p` | `0xE020` | 340 | UnwindData |  |
| 27 | `__conio_common_vcprintf_s` | `0xE180` | 311 | UnwindData |  |
| 29 | `__conio_common_vcwprintf` | `0xE2C0` | 315 | UnwindData |  |
| 30 | `__conio_common_vcwprintf_p` | `0xE400` | 344 | UnwindData |  |
| 31 | `__conio_common_vcwprintf_s` | `0xE560` | 315 | UnwindData |  |
| 28 | `__conio_common_vcscanf` | `0x17030` | 208 | UnwindData |  |
| 32 | `__conio_common_vcwscanf` | `0x17100` | 191 | UnwindData |  |
| 33 | `__daylight` | `0x17310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `__dstbias` | `0x17320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `__timezone` | `0x17330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `__tzname` | `0x17340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `_get_daylight` | `0x17350` | 47 | UnwindData |  |
| 267 | `_get_dstbias` | `0x17380` | 47 | UnwindData |  |
| 281 | `_get_timezone` | `0x173B0` | 47 | UnwindData |  |
| 282 | `_get_tzname` | `0x173E0` | 159 | UnwindData |  |
| 34 | `__doserrno` | `0x17540` | 32 | UnwindData |  |
| 180 | `_errno` | `0x17560` | 32 | UnwindData |  |
| 266 | `_get_doserrno` | `0x17580` | 59 | UnwindData |  |
| 268 | `_get_errno` | `0x175C0` | 59 | UnwindData |  |
| 657 | `_set_doserrno` | `0x17600` | 58 | UnwindData |  |
| 658 | `_set_errno` | `0x17640` | 58 | UnwindData |  |
| 36 | `__fpe_flt_rounds` | `0x17680` | 69 | UnwindData |  |
| 1058 | `fegetround` | `0x176D0` | 20 | UnwindData |  |
| 37 | `__fpecode` | `0x17860` | 18 | UnwindData |  |
| 59 | `__pxcptinfoptrs` | `0x17880` | 18 | UnwindData |  |
| 1219 | `raise` | `0x178A0` | 638 | UnwindData |  |
| 1248 | `signal` | `0x17B20` | 473 | UnwindData |  |
| 38 | `__initialize_lconv_for_unsigned_char` | `0x17D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `__isascii` | `0x17D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__iscsym` | `0x17D20` | 127 | UnwindData |  |
| 41 | `__iscsymf` | `0x17DA0` | 171 | UnwindData |  |
| 85 | `__toascii` | `0x17E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `_isalnum_l` | `0x17E60` | 249 | UnwindData |  |
| 330 | `_isalpha_l` | `0x17F60` | 249 | UnwindData |  |
| 332 | `_isblank_l` | `0x18060` | 242 | UnwindData |  |
| 333 | `_iscntrl_l` | `0x18160` | 242 | UnwindData |  |
| 336 | `_isdigit_l` | `0x18260` | 242 | UnwindData |  |
| 337 | `_isgraph_l` | `0x18360` | 249 | UnwindData |  |
| 339 | `_islower_l` | `0x18460` | 242 | UnwindData |  |
| 404 | `_isprint_l` | `0x18560` | 249 | UnwindData |  |
| 405 | `_ispunct_l` | `0x18660` | 242 | UnwindData |  |
| 406 | `_isspace_l` | `0x18760` | 242 | UnwindData |  |
| 407 | `_isupper_l` | `0x18860` | 242 | UnwindData |  |
| 423 | `_isxdigit_l` | `0x18960` | 249 | UnwindData |  |
| 1116 | `isalnum` | `0x18A60` | 171 | UnwindData |  |
| 1117 | `isalpha` | `0x18B10` | 171 | UnwindData |  |
| 1118 | `isblank` | `0x18BC0` | 30 | UnwindData |  |
| 1119 | `iscntrl` | `0x18C80` | 166 | UnwindData |  |
| 1120 | `isdigit` | `0x18D30` | 166 | UnwindData |  |
| 1121 | `isgraph` | `0x18DE0` | 171 | UnwindData |  |
| 1123 | `islower` | `0x18E90` | 166 | UnwindData |  |
| 1124 | `isprint` | `0x18F40` | 171 | UnwindData |  |
| 1125 | `ispunct` | `0x18FF0` | 166 | UnwindData |  |
| 1126 | `isspace` | `0x190A0` | 166 | UnwindData |  |
| 1127 | `isupper` | `0x19150` | 166 | UnwindData |  |
| 1142 | `isxdigit` | `0x19200` | 171 | UnwindData |  |
| 42 | `__iswcsym` | `0x192B0` | 44 | UnwindData |  |
| 412 | `_iswcsym_l` | `0x192B0` | 44 | UnwindData |  |
| 43 | `__iswcsymf` | `0x192E0` | 44 | UnwindData |  |
| 413 | `_iswcsymf_l` | `0x192E0` | 44 | UnwindData |  |
| 338 | `_isleadbyte_l` | `0x19310` | 75 | UnwindData |  |
| 408 | `_iswalnum_l` | `0x19360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `iswalnum` | `0x19360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `_iswalpha_l` | `0x19370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1129 | `iswalpha` | `0x19370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `_iswblank_l` | `0x19380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1131 | `iswblank` | `0x19380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `_iswcntrl_l` | `0x193A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1132 | `iswcntrl` | `0x193A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `_iswdigit_l` | `0x193B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1134 | `iswdigit` | `0x193B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `_iswgraph_l` | `0x193C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `iswgraph` | `0x193C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `_iswlower_l` | `0x193D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `iswlower` | `0x193D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `_iswprint_l` | `0x193E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `iswprint` | `0x193E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `_iswpunct_l` | `0x193F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `iswpunct` | `0x193F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `_iswspace_l` | `0x19400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1139 | `iswspace` | `0x19400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `_iswupper_l` | `0x19410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1140 | `iswupper` | `0x19410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `_iswxdigit_l` | `0x19420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1141 | `iswxdigit` | `0x19420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `isleadbyte` | `0x19430` | 77 | UnwindData |  |
| 1130 | `iswascii` | `0x19480` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `__p___argc` | `0x194D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `__p___argv` | `0x194E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `__p___wargv` | `0x194F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `__p__acmdln` | `0x19500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `__p__pgmptr` | `0x19510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `__p__wcmdln` | `0x19520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `__p__wpgmptr` | `0x19530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `_get_pgmptr` | `0x19540` | 54 | UnwindData |  |
| 284 | `_get_wpgmptr` | `0x19580` | 54 | UnwindData |  |
| 48 | `__p__commode` | `0x195C0` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `__p__environ` | `0x19BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `__p__wenviron` | `0x19BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `_get_initial_narrow_environment` | `0x19BD0` | 78 | UnwindData |  |
| 272 | `_get_initial_wide_environment` | `0x19C20` | 78 | UnwindData |  |
| 321 | `_initialize_narrow_environment` | `0x19C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `_initialize_wide_environment` | `0x19C80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__p__fmode` | `0x19CB0` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `__p__mbcasemap` | `0x1A530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `__p__mbctype` | `0x1A540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `_getmbcp` | `0x1A550` | 58 | UnwindData |  |
| 668 | `_setmbcp` | `0x1A590` | 37 | UnwindData |  |
| 57 | `__pctype_func` | `0x1A880` | 47 | UnwindData |  |
| 58 | `__pwctype_func` | `0x1A8B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `__setusermatherr` | `0x1A920` | 27,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `__stdio_common_vfprintf` | `0x21460` | 292 | UnwindData |  |
| 62 | `__stdio_common_vfprintf_p` | `0x21590` | 292 | UnwindData |  |
| 63 | `__stdio_common_vfprintf_s` | `0x216C0` | 292 | UnwindData |  |
| 65 | `__stdio_common_vfwprintf` | `0x217F0` | 292 | UnwindData |  |
| 66 | `__stdio_common_vfwprintf_p` | `0x21920` | 292 | UnwindData |  |
| 67 | `__stdio_common_vfwprintf_s` | `0x21A50` | 292 | UnwindData |  |
| 69 | `__stdio_common_vsnprintf_s` | `0x21B80` | 471 | UnwindData |  |
| 70 | `__stdio_common_vsnwprintf_s` | `0x21D60` | 473 | UnwindData |  |
| 71 | `__stdio_common_vsprintf` | `0x21F40` | 593 | UnwindData |  |
| 72 | `__stdio_common_vsprintf_p` | `0x221A0` | 182 | UnwindData |  |
| 73 | `__stdio_common_vsprintf_s` | `0x22260` | 273 | UnwindData |  |
| 75 | `__stdio_common_vswprintf` | `0x22380` | 601 | UnwindData |  |
| 76 | `__stdio_common_vswprintf_p` | `0x225E0` | 182 | UnwindData |  |
| 77 | `__stdio_common_vswprintf_s` | `0x226A0` | 273 | UnwindData |  |
| 64 | `__stdio_common_vfscanf` | `0x2C3E0` | 139 | UnwindData |  |
| 68 | `__stdio_common_vfwscanf` | `0x2C470` | 139 | UnwindData |  |
| 74 | `__stdio_common_vsscanf` | `0x2C500` | 292 | UnwindData |  |
| 78 | `__stdio_common_vswscanf` | `0x2C630` | 277 | UnwindData |  |
| 79 | `__strncnt` | `0x2C750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `__sys_errlist` | `0x2C770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `__sys_nerr` | `0x2C780` | 1,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `__threadhandle` | `0x2CEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `__threadid` | `0x2CED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `__wcserror` | `0x2CEE0` | 370 | UnwindData |  |
| 88 | `__wcserror_s` | `0x2D060` | 277 | UnwindData |  |
| 694 | `_strerror` | `0x2D1F0` | 290 | UnwindData |  |
| 695 | `_strerror_s` | `0x2D320` | 240 | UnwindData |  |
| 89 | `__wcsncnt` | `0x2D410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `_abs64` | `0x2D430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1113 | `imaxabs` | `0x2D430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `llabs` | `0x2D430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `abs` | `0x2D440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `labs` | `0x2D440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `_access` | `0x2D450` | 18 | UnwindData |  |
| 92 | `_access_s` | `0x2D470` | 239 | UnwindData |  |
| 93 | `_aligned_free` | `0x2D560` | 27 | UnwindData |  |
| 94 | `_aligned_malloc` | `0x2D580` | 127 | UnwindData |  |
| 95 | `_aligned_msize` | `0x2D600` | 101 | UnwindData |  |
| 96 | `_aligned_offset_malloc` | `0x2D670` | 197 | UnwindData |  |
| 97 | `_aligned_offset_realloc` | `0x2D740` | 599 | UnwindData |  |
| 98 | `_aligned_offset_recalloc` | `0x2D9A0` | 791 | UnwindData |  |
| 99 | `_aligned_realloc` | `0x2DCC0` | 460 | UnwindData |  |
| 100 | `_aligned_recalloc` | `0x2DE90` | 622 | UnwindData |  |
| 101 | `_assert` | `0x2EEE0` | 115 | UnwindData |  |
| 777 | `_wassert` | `0x2EF60` | 115 | UnwindData |  |
| 102 | `_atodbl` | `0x310A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `_atodbl_l` | `0x310B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `_atof_l` | `0x310C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `_atoflt` | `0x310D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `_atoflt_l` | `0x310E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `_wtof` | `0x310F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `_wtof_l` | `0x31100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 940 | `atof` | `0x31110` | 5,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `_atoi64` | `0x325E0` | 178 | UnwindData |  |
| 943 | `atoll` | `0x325E0` | 178 | UnwindData |  |
| 108 | `_atoi64_l` | `0x326A0` | 188 | UnwindData |  |
| 113 | `_atoll_l` | `0x326A0` | 188 | UnwindData |  |
| 109 | `_atoi_l` | `0x32760` | 186 | UnwindData |  |
| 110 | `_atol_l` | `0x32760` | 186 | UnwindData |  |
| 905 | `_wtoi` | `0x32820` | 176 | UnwindData |  |
| 909 | `_wtol` | `0x32820` | 176 | UnwindData |  |
| 906 | `_wtoi64` | `0x328D0` | 178 | UnwindData |  |
| 911 | `_wtoll` | `0x328D0` | 178 | UnwindData |  |
| 907 | `_wtoi64_l` | `0x32990` | 188 | UnwindData |  |
| 912 | `_wtoll_l` | `0x32990` | 188 | UnwindData |  |
| 908 | `_wtoi_l` | `0x32A50` | 186 | UnwindData |  |
| 910 | `_wtol_l` | `0x32A50` | 186 | UnwindData |  |
| 941 | `atoi` | `0x32B10` | 176 | UnwindData |  |
| 942 | `atol` | `0x32B10` | 176 | UnwindData |  |
| 111 | `_atoldbl` | `0x337F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `_atoldbl_l` | `0x33800` | 326 | UnwindData |  |
| 114 | `_beep` | `0x33950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `_sleep` | `0x33960` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `_beginthread` | `0x33B30` | 202 | UnwindData |  |
| 116 | `_beginthreadex` | `0x33C00` | 212 | UnwindData |  |
| 177 | `_endthread` | `0x33CE0` | 12 | UnwindData |  |
| 178 | `_endthreadex` | `0x33CF0` | 10 | UnwindData |  |
| 117 | `_byteswap_uint64` | `0x33D00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `_byteswap_ulong` | `0x33D80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `_byteswap_ushort` | `0x33DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `_cabs` | `0x33DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `_callnewh` | `0x33DF0` | 57 | UnwindData |  |
| 633 | `_query_new_handler` | `0x33E30` | 52 | UnwindData |  |
| 662 | `_set_new_handler` | `0x33E70` | 89 | UnwindData |  |
| 123 | `_calloc_base` | `0x33ED0` | 117 | UnwindData |  |
| 125 | `_cgets` | `0x33F50` | 115 | UnwindData |  |
| 126 | `_cgets_s` | `0x33FD0` | 268 | UnwindData |  |
| 127 | `_cgetws` | `0x340E0` | 116 | UnwindData |  |
| 128 | `_cgetws_s` | `0x34160` | 399 | UnwindData |  |
| 129 | `_chdir` | `0x34670` | 308 | UnwindData |  |
| 778 | `_wchdir` | `0x347B0` | 345 | UnwindData |  |
| 130 | `_chdrive` | `0x34910` | 129 | UnwindData |  |
| 294 | `_getdrive` | `0x349A0` | 246 | UnwindData |  |
| 131 | `_chgsign` | `0x34AA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `_chgsignf` | `0x34AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `_chmod` | `0x34AF0` | 239 | UnwindData |  |
| 134 | `_chsize` | `0x34C60` | 21 | UnwindData |  |
| 135 | `_chsize_s` | `0x34EB0` | 334 | UnwindData |  |
| 136 | `_clearfp` | `0x35000` | 110 | UnwindData |  |
| 142 | `_control87` | `0x35070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `_controlfp` | `0x35080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `_fpreset` | `0x35090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 656 | `_set_controlfp` | `0x350A0` | 52 | UnwindData |  |
| 689 | `_statusfp` | `0x350E0` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `_close` | `0x35480` | 152 | UnwindData |  |
| 138 | `_commit` | `0x357D0` | 145 | UnwindData |  |
| 139 | `_configthreadlocale` | `0x35EA0` | 105 | UnwindData |  |
| 150 | `_create_locale` | `0x35FD0` | 118 | UnwindData |  |
| 241 | `_free_locale` | `0x364D0` | 162 | UnwindData |  |
| 264 | `_get_current_locale` | `0x36580` | 187 | UnwindData |  |
| 781 | `_wcreate_locale` | `0x36640` | 328 | UnwindData |  |
| 877 | `_wsetlocale` | `0x367F0` | 161 | UnwindData |  |
| 140 | `_configure_narrow_argv` | `0x378F0` | 390 | UnwindData |  |
| 141 | `_configure_wide_argv` | `0x37A80` | 386 | UnwindData |  |
| 144 | `_controlfp_s` | `0x37C10` | 99 | UnwindData |  |
| 145 | `_copysign` | `0x37C80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `_copysignf` | `0x37CC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `_cputs` | `0x37CF0` | 114 | UnwindData |  |
| 148 | `_cputws` | `0x37D70` | 176 | UnwindData |  |
| 149 | `_creat` | `0x37E20` | 55 | UnwindData |  |
| 780 | `_wcreat` | `0x37E60` | 55 | UnwindData |  |
| 151 | `_crt_at_quick_exit` | `0x381E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `_crt_atexit` | `0x381F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `_execute_onexit_table` | `0x38200` | 67 | UnwindData |  |
| 322 | `_initialize_onexit_table` | `0x38250` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | `_register_onexit_function` | `0x38280` | 72 | UnwindData |  |
| 153 | `_ctime32` | `0x382D0` | 115 | UnwindData |  |
| 154 | `_ctime32_s` | `0x38350` | 152 | UnwindData |  |
| 155 | `_ctime64` | `0x383F0` | 116 | UnwindData |  |
| 156 | `_ctime64_s` | `0x38470` | 152 | UnwindData |  |
| 826 | `_wctime32` | `0x38510` | 115 | UnwindData |  |
| 827 | `_wctime32_s` | `0x38590` | 163 | UnwindData |  |
| 828 | `_wctime64` | `0x38640` | 116 | UnwindData |  |
| 829 | `_wctime64_s` | `0x386C0` | 163 | UnwindData |  |
| 157 | `_cwait` | `0x38770` | 182 | UnwindData |  |
| 158 | `_d_int` | `0x38830` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `_dtest` | `0x38950` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `_fd_int` | `0x389C0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `_fdtest` | `0x38AA0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `_ld_int` | `0x38BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `_ldtest` | `0x38BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `_dclass` | `0x38BC0` | 25 | UnwindData |  |
| 165 | `_dpcomp` | `0x38BE0` | 99 | UnwindData |  |
| 168 | `_dsign` | `0x38C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `_ldsign` | `0x38C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `nan` | `0x38C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `_dexp` | `0x38C80` | 602 | UnwindData |  |
| 1043 | `exp2` | `0x38EE0` | 242 | UnwindData |  |
| 161 | `_difftime32` | `0x38FE0` | 43 | UnwindData |  |
| 162 | `_difftime64` | `0x39010` | 46 | UnwindData |  |
| 163 | `_dlog` | `0x39040` | 448 | UnwindData |  |
| 164 | `_dnorm` | `0x39260` | 389 | UnwindData |  |
| 201 | `_fdnorm` | `0x393F0` | 215 | UnwindData |  |
| 166 | `_dpoly` | `0x394D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `_ldpoly` | `0x394D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `erfc` | `0x394F0` | 638 | UnwindData |  |
| 167 | `_dscale` | `0x39770` | 635 | UnwindData |  |
| 205 | `_fdscale` | `0x399F0` | 456 | UnwindData |  |
| 438 | `_ldscale` | `0x39BC0` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `_dsin` | `0x39FF0` | 373 | UnwindData |  |
| 1146 | `lgamma` | `0x3A1B0` | 567 | UnwindData |  |
| 171 | `_dunscale` | `0x3A4E0` | 154 | UnwindData |  |
| 209 | `_fdunscale` | `0x3A580` | 138 | UnwindData |  |
| 442 | `_ldunscale` | `0x3A610` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `_dup` | `0x3A840` | 314 | UnwindData |  |
| 173 | `_dup2` | `0x3AC20` | 152 | UnwindData |  |
| 174 | `_dupenv_s` | `0x3B280` | 31 | UnwindData |  |
| 833 | `_wdupenv_s` | `0x3B2A0` | 31 | UnwindData |  |
| 859 | `_wgetenv` | `0x3B2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 860 | `_wgetenv_s` | `0x3B2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1103 | `getenv` | `0x3B2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `getenv_s` | `0x3B2F0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `_ecvt` | `0x3B660` | 313 | UnwindData |  |
| 176 | `_ecvt_s` | `0x3B7A0` | 183 | UnwindData |  |
| 195 | `_fcvt` | `0x3B860` | 399 | UnwindData |  |
| 196 | `_fcvt_s` | `0x3B9F0` | 183 | UnwindData |  |
| 179 | `_eof` | `0x3BB80` | 161 | UnwindData |  |
| 181 | `_except1` | `0x3BC70` | 241 | UnwindData |  |
| 182 | `_execl` | `0x3C7C0` | 50 | UnwindData |  |
| 183 | `_execle` | `0x3C800` | 50 | UnwindData |  |
| 675 | `_spawnl` | `0x3C840` | 43 | UnwindData |  |
| 676 | `_spawnle` | `0x3C870` | 43 | UnwindData |  |
| 834 | `_wexecl` | `0x3C8A0` | 50 | UnwindData |  |
| 835 | `_wexecle` | `0x3C8E0` | 50 | UnwindData |  |
| 881 | `_wspawnl` | `0x3C920` | 43 | UnwindData |  |
| 882 | `_wspawnle` | `0x3C950` | 43 | UnwindData |  |
| 184 | `_execlp` | `0x3CB70` | 50 | UnwindData |  |
| 185 | `_execlpe` | `0x3CBB0` | 50 | UnwindData |  |
| 677 | `_spawnlp` | `0x3CBF0` | 43 | UnwindData |  |
| 678 | `_spawnlpe` | `0x3CC20` | 43 | UnwindData |  |
| 836 | `_wexeclp` | `0x3CC50` | 50 | UnwindData |  |
| 837 | `_wexeclpe` | `0x3CC90` | 50 | UnwindData |  |
| 883 | `_wspawnlp` | `0x3CCD0` | 43 | UnwindData |  |
| 884 | `_wspawnlpe` | `0x3CD00` | 43 | UnwindData |  |
| 187 | `_execv` | `0x3D920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `_execve` | `0x3D940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `_spawnv` | `0x3D960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `_spawnve` | `0x3D970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `_wexecv` | `0x3D980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 839 | `_wexecve` | `0x3D9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `_wspawnv` | `0x3D9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | `_wspawnve` | `0x3D9D0` | 1,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `_execvp` | `0x3E0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `_execvpe` | `0x3E0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `_spawnvp` | `0x3E0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 682 | `_spawnvpe` | `0x3E0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | `_wexecvp` | `0x3E100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 841 | `_wexecvpe` | `0x3E120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | `_wspawnvp` | `0x3E140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 888 | `_wspawnvpe` | `0x3E150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `_expand` | `0x3E160` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `_fclose_nolock` | `0x3E380` | 152 | UnwindData |  |
| 1051 | `fclose` | `0x3E420` | 152 | UnwindData |  |
| 194 | `_fcloseall` | `0x3E4C0` | 177 | UnwindData |  |
| 198 | `_fdclass` | `0x3E580` | 25 | UnwindData |  |
| 203 | `_fdpcomp` | `0x3E5A0` | 97 | UnwindData |  |
| 206 | `_fdsign` | `0x3E610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `nanf` | `0x3E630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `_fdexp` | `0x3E640` | 569 | UnwindData |  |
| 1044 | `exp2f` | `0x3E880` | 238 | UnwindData |  |
| 200 | `_fdlog` | `0x3E970` | 399 | UnwindData |  |
| 1165 | `log2f` | `0x3EB30` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `_fdopen` | `0x3F2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `_wfdopen` | `0x3F2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `_fdpoly` | `0x3F300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `erfcf` | `0x3F320` | 623 | UnwindData |  |
| 207 | `_fdsin` | `0x3F990` | 297 | UnwindData |  |
| 1147 | `lgammaf` | `0x3FBC0` | 553 | UnwindData |  |
| 210 | `_fflush_nolock` | `0x400A0` | 209 | UnwindData |  |
| 229 | `_flushall` | `0x40180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `fflush` | `0x40190` | 102 | UnwindData |  |
| 211 | `_fgetc_nolock` | `0x40200` | 67 | UnwindData |  |
| 212 | `_fgetchar` | `0x40250` | 23 | UnwindData |  |
| 1102 | `getchar` | `0x40250` | 23 | UnwindData |  |
| 285 | `_getc_nolock` | `0x40270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `fgetc` | `0x40280` | 269 | UnwindData |  |
| 1101 | `getc` | `0x40390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `_fgetwc_nolock` | `0x403A0` | 431 | UnwindData |  |
| 214 | `_fgetwchar` | `0x40550` | 23 | UnwindData |  |
| 1108 | `getwchar` | `0x40550` | 23 | UnwindData |  |
| 301 | `_getwc_nolock` | `0x40570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1070 | `fgetwc` | `0x40580` | 85 | UnwindData |  |
| 1107 | `getwc` | `0x405E0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `_filelength` | `0x40810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `_filelengthi64` | `0x40820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `_fileno` | `0x40830` | 38 | UnwindData |  |
| 218 | `_findclose` | `0x416B0` | 37 | UnwindData |  |
| 219 | `_findfirst32` | `0x416E0` | 396 | UnwindData |  |
| 220 | `_findfirst32i64` | `0x41870` | 396 | UnwindData |  |
| 221 | `_findfirst64` | `0x41A00` | 396 | UnwindData |  |
| 222 | `_findfirst64i32` | `0x41B90` | 396 | UnwindData |  |
| 223 | `_findnext32` | `0x41D20` | 224 | UnwindData |  |
| 224 | `_findnext32i64` | `0x41E00` | 224 | UnwindData |  |
| 225 | `_findnext64` | `0x41EE0` | 224 | UnwindData |  |
| 226 | `_findnext64i32` | `0x41FC0` | 224 | UnwindData |  |
| 843 | `_wfindfirst32` | `0x420A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `_wfindfirst32i64` | `0x420B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `_wfindfirst64` | `0x420C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `_wfindfirst64i32` | `0x420D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `_wfindnext32` | `0x420E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 848 | `_wfindnext32i64` | `0x420F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `_wfindnext64` | `0x42100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | `_wfindnext64i32` | `0x42110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `_finite` | `0x42120` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `_finitef` | `0x42150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `_fpclass` | `0x42170` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `_fpclassf` | `0x42200` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `_isnan` | `0x42270` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `_isnanf` | `0x422A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 615 | `_nextafter` | `0x422C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 616 | `_nextafterf` | `0x422D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 647 | `_scalb` | `0x422E0` | 428 | UnwindData |  |
| 648 | `_scalbf` | `0x42490` | 415 | UnwindData |  |
| 232 | `_fpieee_flt` | `0x42630` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `_fputc_nolock` | `0x427B0` | 171 | UnwindData |  |
| 235 | `_fputchar` | `0x42880` | 33 | UnwindData |  |
| 622 | `_putc_nolock` | `0x428B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1087 | `fputc` | `0x428C0` | 152 | UnwindData |  |
| 1211 | `putc` | `0x42960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `putchar` | `0x42970` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `_fputwc_nolock` | `0x42A00` | 154 | UnwindData |  |
| 237 | `_fputwchar` | `0x42C30` | 35 | UnwindData |  |
| 628 | `_putwc_nolock` | `0x42C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `fputwc` | `0x42C70` | 154 | UnwindData |  |
| 1214 | `putwc` | `0x42D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `putwchar` | `0x42D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `_fread_nolock` | `0x42D30` | 29 | UnwindData |  |
| 239 | `_fread_nolock_s` | `0x42D50` | 606 | UnwindData |  |
| 1091 | `fread` | `0x42FB0` | 29 | UnwindData |  |
| 1092 | `fread_s` | `0x42FD0` | 165 | UnwindData |  |
| 240 | `_free_base` | `0x43080` | 60 | UnwindData |  |
| 242 | `_fseek_nolock` | `0x43310` | 155 | UnwindData |  |
| 243 | `_fseeki64` | `0x433B0` | 152 | UnwindData |  |
| 244 | `_fseeki64_nolock` | `0x43450` | 152 | UnwindData |  |
| 1097 | `fseek` | `0x434F0` | 155 | UnwindData |  |
| 245 | `_fsopen` | `0x43720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `_wfopen` | `0x43730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `_wfopen_s` | `0x43740` | 88 | UnwindData |  |
| 855 | `_wfsopen` | `0x437A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `fopen` | `0x437B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1086 | `fopen_s` | `0x437C0` | 88 | UnwindData |  |
| 246 | `_fstat32` | `0x44B90` | 214 | UnwindData |  |
| 247 | `_fstat32i64` | `0x44C70` | 213 | UnwindData |  |
| 248 | `_fstat64` | `0x44D50` | 229 | UnwindData |  |
| 249 | `_fstat64i32` | `0x44E40` | 213 | UnwindData |  |
| 685 | `_stat32` | `0x44F20` | 258 | UnwindData |  |
| 686 | `_stat32i64` | `0x45030` | 258 | UnwindData |  |
| 687 | `_stat64` | `0x45140` | 258 | UnwindData |  |
| 688 | `_stat64i32` | `0x45250` | 258 | UnwindData |  |
| 891 | `_wstat32` | `0x45360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `_wstat32i64` | `0x45370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 893 | `_wstat64` | `0x45380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `_wstat64i32` | `0x45390` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `_ftell_nolock` | `0x45920` | 175 | UnwindData |  |
| 251 | `_ftelli64` | `0x459D0` | 154 | UnwindData |  |
| 252 | `_ftelli64_nolock` | `0x45A70` | 154 | UnwindData |  |
| 1099 | `ftell` | `0x45B20` | 152 | UnwindData |  |
| 253 | `_ftime32` | `0x45BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `_ftime32_s` | `0x45BD0` | 410 | UnwindData |  |
| 255 | `_ftime64` | `0x45D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `_ftime64_s` | `0x45D80` | 411 | UnwindData |  |
| 257 | `_fullpath` | `0x467A0` | 176 | UnwindData |  |
| 856 | `_wfullpath` | `0x46850` | 179 | UnwindData |  |
| 258 | `_futime32` | `0x46D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `_futime64` | `0x46D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `_utime32` | `0x46D20` | 147 | UnwindData |  |
| 772 | `_utime64` | `0x46DC0` | 147 | UnwindData |  |
| 914 | `_wutime32` | `0x46E60` | 147 | UnwindData |  |
| 915 | `_wutime64` | `0x46F00` | 147 | UnwindData |  |
| 260 | `_fwrite_nolock` | `0x470F0` | 161 | UnwindData |  |
| 1100 | `fwrite` | `0x473A0` | 161 | UnwindData |  |
| 261 | `_gcvt` | `0x47450` | 44 | UnwindData |  |
| 262 | `_gcvt_s` | `0x47480` | 554 | UnwindData |  |
| 263 | `_get_FMA3_enable` | `0x47720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `_set_FMA3_enable` | `0x47730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `_get_fmode` | `0x47750` | 47 | UnwindData |  |
| 660 | `_set_fmode` | `0x47780` | 61 | UnwindData |  |
| 669 | `_setmode` | `0x477C0` | 257 | UnwindData |  |
| 270 | `_get_heap_handle` | `0x479E0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `_get_invalid_parameter_handler` | `0x47BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `_get_thread_local_invalid_parameter_handler` | `0x47BC0` | 26 | UnwindData |  |
| 326 | `_invalid_parameter_noinfo` | `0x47D50` | 30 | UnwindData |  |
| 327 | `_invalid_parameter_noinfo_noreturn` | `0x47D70` | 47 | UnwindData |  |
| 328 | `_invoke_watson` | `0x47DA0` | 71 | UnwindData |  |
| 661 | `_set_invalid_parameter_handler` | `0x47DF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `_set_thread_local_invalid_parameter_handler` | `0x47E30` | 37 | UnwindData |  |
| 274 | `_get_narrow_winmain_command_line` | `0x47E60` | 112 | UnwindData |  |
| 283 | `_get_wide_winmain_command_line` | `0x47ED0` | 1,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `_get_osfhandle` | `0x483D0` | 117 | UnwindData |  |
| 618 | `_open_osfhandle` | `0x48450` | 257 | UnwindData |  |
| 277 | `_get_printf_count_output` | `0x48560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `_set_printf_count_output` | `0x48580` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `_get_terminate` | `0x485B0` | 34 | UnwindData |  |
| 1244 | `set_terminate` | `0x485E0` | 44 | UnwindData |  |
| 1292 | `terminate` | `0x48610` | 42 | UnwindData |  |
| 286 | `_getch` | `0x48690` | 42 | UnwindData |  |
| 287 | `_getch_nolock` | `0x486C0` | 388 | UnwindData |  |
| 288 | `_getche` | `0x48850` | 42 | UnwindData |  |
| 289 | `_getche_nolock` | `0x48880` | 102 | UnwindData |  |
| 431 | `_kbhit` | `0x489B0` | 42 | UnwindData |  |
| 762 | `_ungetch` | `0x48B70` | 46 | UnwindData |  |
| 763 | `_ungetch_nolock` | `0x48BA0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `_getcwd` | `0x48F20` | 39 | UnwindData |  |
| 291 | `_getdcwd` | `0x48F50` | 31 | UnwindData |  |
| 857 | `_wgetcwd` | `0x48F70` | 39 | UnwindData |  |
| 858 | `_wgetdcwd` | `0x48FA0` | 31 | UnwindData |  |
| 292 | `_getdiskfree` | `0x48FC0` | 196 | UnwindData |  |
| 293 | `_getdllprocaddr` | `0x49090` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `_getdrives` | `0x490C0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `_getmaxstdio` | `0x491F0` | 46 | UnwindData |  |
| 667 | `_setmaxstdio` | `0x49220` | 92 | UnwindData |  |
| 298 | `_getpid` | `0x49280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `_getsystime` | `0x49290` | 158 | UnwindData |  |
| 670 | `_setsystime` | `0x49330` | 163 | UnwindData |  |
| 300 | `_getw` | `0x493E0` | 163 | UnwindData |  |
| 302 | `_getwch` | `0x49490` | 44 | UnwindData |  |
| 303 | `_getwch_nolock` | `0x494C0` | 220 | UnwindData |  |
| 304 | `_getwche` | `0x495A0` | 44 | UnwindData |  |
| 305 | `_getwche_nolock` | `0x495D0` | 79 | UnwindData |  |
| 765 | `_ungetwch` | `0x49620` | 50 | UnwindData |  |
| 766 | `_ungetwch_nolock` | `0x49660` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `_getws` | `0x49980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `_getws_s` | `0x49990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `gets` | `0x499A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `gets_s` | `0x499B0` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `_gmtime32` | `0x49E30` | 72 | UnwindData |  |
| 309 | `_gmtime32_s` | `0x49E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `_gmtime64` | `0x49E90` | 72 | UnwindData |  |
| 311 | `_gmtime64_s` | `0x49EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `_heapchk` | `0x49EF0` | 37 | UnwindData |  |
| 313 | `_heapmin` | `0x49F20` | 33 | UnwindData |  |
| 314 | `_heapwalk` | `0x49F90` | 206 | UnwindData |  |
| 315 | `_hypot` | `0x4A060` | 597 | UnwindData |  |
| 1109 | `hypot` | `0x4A2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `_hypotf` | `0x4A2D0` | 291 | UnwindData |  |
| 317 | `_i64toa` | `0x4A8E0` | 49 | UnwindData |  |
| 318 | `_i64toa_s` | `0x4A920` | 33 | UnwindData |  |
| 319 | `_i64tow` | `0x4A950` | 49 | UnwindData |  |
| 320 | `_i64tow_s` | `0x4A990` | 33 | UnwindData |  |
| 424 | `_itoa` | `0x4A9C0` | 48 | UnwindData |  |
| 461 | `_ltoa` | `0x4A9C0` | 48 | UnwindData |  |
| 425 | `_itoa_s` | `0x4A9F0` | 32 | UnwindData |  |
| 462 | `_ltoa_s` | `0x4A9F0` | 32 | UnwindData |  |
| 426 | `_itow` | `0x4AA10` | 48 | UnwindData |  |
| 463 | `_ltow` | `0x4AA10` | 48 | UnwindData |  |
| 427 | `_itow_s` | `0x4AA40` | 32 | UnwindData |  |
| 464 | `_ltow_s` | `0x4AA40` | 32 | UnwindData |  |
| 751 | `_ui64toa` | `0x4AA60` | 35 | UnwindData |  |
| 752 | `_ui64toa_s` | `0x4AA90` | 19 | UnwindData |  |
| 753 | `_ui64tow` | `0x4AAB0` | 35 | UnwindData |  |
| 754 | `_ui64tow_s` | `0x4AAE0` | 19 | UnwindData |  |
| 755 | `_ultoa` | `0x4AB00` | 35 | UnwindData |  |
| 756 | `_ultoa_s` | `0x4AB30` | 19 | UnwindData |  |
| 757 | `_ultow` | `0x4AB50` | 35 | UnwindData |  |
| 758 | `_ultow_s` | `0x4AB80` | 19 | UnwindData |  |
| 324 | `_initterm` | `0x4ABA0` | 65 | UnwindData |  |
| 325 | `_initterm_e` | `0x4ABF0` | 71 | UnwindData |  |
| 331 | `_isatty` | `0x4AC40` | 95 | UnwindData |  |
| 334 | `_isctype` | `0x4ACA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `_isctype_l` | `0x4ACD0` | 264 | UnwindData |  |
| 340 | `_ismbbalnum` | `0x4AE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `_ismbbalnum_l` | `0x4AE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `_ismbbalpha` | `0x4AE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `_ismbbalpha_l` | `0x4AEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `_ismbbblank` | `0x4AED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `_ismbbblank_l` | `0x4AEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `_ismbbgraph` | `0x4AF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `_ismbbgraph_l` | `0x4AF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `_ismbbkalnum` | `0x4AF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `_ismbbkalnum_l` | `0x4AF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `_ismbbkana` | `0x4AF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `_ismbbkana_l` | `0x4AFA0` | 101 | UnwindData |  |
| 352 | `_ismbbkprint` | `0x4B010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `_ismbbkprint_l` | `0x4B030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `_ismbbkpunct` | `0x4B050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `_ismbbkpunct_l` | `0x4B070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `_ismbblead` | `0x4B090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `_ismbblead_l` | `0x4B0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `_ismbbprint` | `0x4B0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `_ismbbprint_l` | `0x4B0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `_ismbbpunct` | `0x4B110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `_ismbbpunct_l` | `0x4B130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `_ismbbtrail` | `0x4B150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `_ismbbtrail_l` | `0x4B170` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `_ismbcalnum` | `0x4B220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `_ismbcalnum_l` | `0x4B230` | 118 | UnwindData |  |
| 366 | `_ismbcalpha` | `0x4B2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `_ismbcalpha_l` | `0x4B2C0` | 118 | UnwindData |  |
| 368 | `_ismbcblank` | `0x4B340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `_ismbcblank_l` | `0x4B350` | 124 | UnwindData |  |
| 390 | `_ismbcpunct` | `0x4B3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `_ismbcpunct_l` | `0x4B3E0` | 110 | UnwindData |  |
| 370 | `_ismbcdigit` | `0x4B450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `_ismbcdigit_l` | `0x4B460` | 92 | UnwindData |  |
| 372 | `_ismbcgraph` | `0x4B4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `_ismbcgraph_l` | `0x4B4D0` | 113 | UnwindData |  |
| 374 | `_ismbchira` | `0x4B550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `_ismbchira_l` | `0x4B560` | 77 | UnwindData |  |
| 376 | `_ismbckata` | `0x4B5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `_ismbckata_l` | `0x4B5C0` | 85 | UnwindData |  |
| 394 | `_ismbcsymbol` | `0x4B620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `_ismbcsymbol_l` | `0x4B630` | 85 | UnwindData |  |
| 378 | `_ismbcl0` | `0x4B690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `_ismbcl0_l` | `0x4B6A0` | 97 | UnwindData |  |
| 380 | `_ismbcl1` | `0x4B710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `_ismbcl1_l` | `0x4B720` | 102 | UnwindData |  |
| 382 | `_ismbcl2` | `0x4B790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `_ismbcl2_l` | `0x4B7A0` | 102 | UnwindData |  |
| 384 | `_ismbclegal` | `0x4B810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `_ismbclegal_l` | `0x4B820` | 80 | UnwindData |  |
| 386 | `_ismbclower` | `0x4B870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `_ismbclower_l` | `0x4B880` | 93 | UnwindData |  |
| 388 | `_ismbcprint` | `0x4B8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `_ismbcprint_l` | `0x4B8F0` | 114 | UnwindData |  |
| 392 | `_ismbcspace` | `0x4B970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `_ismbcspace_l` | `0x4B980` | 93 | UnwindData |  |
| 396 | `_ismbcupper` | `0x4B9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `_ismbcupper_l` | `0x4B9F0` | 93 | UnwindData |  |
| 398 | `_ismbslead` | `0x4BA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `_ismbslead_l` | `0x4BA60` | 148 | UnwindData |  |
| 400 | `_ismbstrail` | `0x4BB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `_ismbstrail_l` | `0x4BB10` | 145 | UnwindData |  |
| 414 | `_iswctype_l` | `0x4BBB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1115 | `is_wctype` | `0x4BBB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1133 | `iswctype` | `0x4BBC0` | 108 | UnwindData |  |
| 428 | `_j0` | `0x4BC30` | 349 | UnwindData |  |
| 429 | `_j1` | `0x4BD90` | 398 | UnwindData |  |
| 430 | `_jn` | `0x4BF20` | 372 | UnwindData |  |
| 916 | `_y0` | `0x4C0A0` | 415 | UnwindData |  |
| 917 | `_y1` | `0x4C240` | 440 | UnwindData |  |
| 918 | `_yn` | `0x4C400` | 231 | UnwindData |  |
| 433 | `_ldclass` | `0x4C5B0` | 25 | UnwindData |  |
| 436 | `_ldpcomp` | `0x4C5D0` | 99 | UnwindData |  |
| 1195 | `nanl` | `0x4C640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `_ldexp` | `0x4C650` | 602 | UnwindData |  |
| 1045 | `exp2l` | `0x4C8B0` | 242 | UnwindData |  |
| 435 | `_ldlog` | `0x4C9B0` | 448 | UnwindData |  |
| 1166 | `log2l` | `0x4CB70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `erfcl` | `0x4CB80` | 624 | UnwindData |  |
| 440 | `_ldsin` | `0x4D210` | 373 | UnwindData |  |
| 1148 | `lgammal` | `0x4D4C0` | 567 | UnwindData |  |
| 443 | `_lfind` | `0x4D700` | 163 | UnwindData |  |
| 444 | `_lfind_s` | `0x4D7B0` | 169 | UnwindData |  |
| 445 | `_loaddll` | `0x4D860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 768 | `_unloaddll` | `0x4D870` | 32 | UnwindData |  |
| 446 | `_localtime32` | `0x4DE50` | 72 | UnwindData |  |
| 447 | `_localtime32_s` | `0x4DEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `_localtime64` | `0x4DEB0` | 72 | UnwindData |  |
| 449 | `_localtime64_s` | `0x4DF00` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `_lock_locales` | `0x4DFE0` | 27 | UnwindData |  |
| 770 | `_unlock_locales` | `0x4E000` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `_locking` | `0x4E130` | 277 | UnwindData |  |
| 453 | `_logb` | `0x4E250` | 221 | UnwindData |  |
| 454 | `_logbf` | `0x4E330` | 212 | UnwindData |  |
| 455 | `_lrotl` | `0x4E410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 643 | `_rotl` | `0x4E410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `_rotl64` | `0x4E420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `_lrotr` | `0x4E430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `_rotr` | `0x4E430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 646 | `_rotr64` | `0x4E440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `_lsearch` | `0x4E450` | 188 | UnwindData |  |
| 458 | `_lsearch_s` | `0x4E510` | 194 | UnwindData |  |
| 459 | `_lseek` | `0x4E9D0` | 152 | UnwindData |  |
| 460 | `_lseeki64` | `0x4EB10` | 154 | UnwindData |  |
| 465 | `_makepath` | `0x4EC60` | 39 | UnwindData |  |
| 466 | `_makepath_s` | `0x4EC90` | 382 | UnwindData |  |
| 861 | `_wmakepath` | `0x4EE10` | 39 | UnwindData |  |
| 862 | `_wmakepath_s` | `0x4EE40` | 401 | UnwindData |  |
| 467 | `_malloc_base` | `0x4EFE0` | 94 | UnwindData |  |
| 468 | `_mbbtombc` | `0x4F040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `_mbbtombc_l` | `0x4F050` | 161 | UnwindData |  |
| 489 | `_mbctombb` | `0x4F100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `_mbctombb_l` | `0x4F110` | 193 | UnwindData |  |
| 470 | `_mbbtype` | `0x4F1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `_mbbtype_l` | `0x4F1F0` | 135 | UnwindData |  |
| 473 | `_mbccpy` | `0x4F280` | 30 | UnwindData |  |
| 474 | `_mbccpy_l` | `0x4F2A0` | 29 | UnwindData |  |
| 475 | `_mbccpy_s` | `0x4F2C0` | 20 | UnwindData |  |
| 476 | `_mbccpy_s_l` | `0x4F2E0` | 255 | UnwindData |  |
| 477 | `_mbcjistojms` | `0x4F3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 478 | `_mbcjistojms_l` | `0x4F3F0` | 165 | UnwindData |  |
| 479 | `_mbcjmstojis` | `0x4F4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 480 | `_mbcjmstojis_l` | `0x4F4B0` | 193 | UnwindData |  |
| 481 | `_mbclen` | `0x4F580` | 43 | UnwindData |  |
| 482 | `_mbclen_l` | `0x4F5B0` | 43 | UnwindData |  |
| 483 | `_mbctohira` | `0x4F5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `_mbctohira_l` | `0x4F5F0` | 55 | UnwindData |  |
| 485 | `_mbctokata` | `0x4F630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `_mbctokata_l` | `0x4F640` | 41 | UnwindData |  |
| 487 | `_mbctolower` | `0x4F670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `_mbctolower_l` | `0x4F680` | 192 | UnwindData |  |
| 491 | `_mbctoupper` | `0x4F740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 492 | `_mbctoupper_l` | `0x4F750` | 192 | UnwindData |  |
| 493 | `_mblen_l` | `0x4F930` | 163 | UnwindData |  |
| 1178 | `mblen` | `0x4F9E0` | 152 | UnwindData |  |
| 494 | `_mbsbtype` | `0x4FA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `_mbsbtype_l` | `0x4FA90` | 179 | UnwindData |  |
| 496 | `_mbscat_s` | `0x4FB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 497 | `_mbscat_s_l` | `0x4FB60` | 410 | UnwindData |  |
| 498 | `_mbschr` | `0x4FD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `_mbschr_l` | `0x4FD10` | 194 | UnwindData |  |
| 500 | `_mbscmp` | `0x4FDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `_mbscmp_l` | `0x4FDF0` | 237 | UnwindData |  |
| 502 | `_mbscoll` | `0x4FEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `_mbscoll_l` | `0x4FEF0` | 201 | UnwindData |  |
| 504 | `_mbscpy_s` | `0x4FFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `_mbscpy_s_l` | `0x4FFD0` | 314 | UnwindData |  |
| 506 | `_mbscspn` | `0x50110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `_mbscspn_l` | `0x50120` | 236 | UnwindData |  |
| 508 | `_mbsdec` | `0x50210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `_mbsdec_l` | `0x50220` | 148 | UnwindData |  |
| 511 | `_mbsicmp` | `0x502C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `_mbsicmp_l` | `0x502D0` | 494 | UnwindData |  |
| 513 | `_mbsicoll` | `0x504C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `_mbsicoll_l` | `0x504D0` | 201 | UnwindData |  |
| 515 | `_mbsinc` | `0x505A0` | 66 | UnwindData |  |
| 516 | `_mbsinc_l` | `0x505F0` | 39 | UnwindData |  |
| 517 | `_mbslen` | `0x50620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `_mbslen_l` | `0x50630` | 110 | UnwindData |  |
| 519 | `_mbslwr` | `0x506A0` | 43 | UnwindData |  |
| 520 | `_mbslwr_l` | `0x506D0` | 43 | UnwindData |  |
| 521 | `_mbslwr_s` | `0x50700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | `_mbslwr_s_l` | `0x50710` | 340 | UnwindData |  |
| 523 | `_mbsnbcat` | `0x50870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `_mbsnbcat_l` | `0x50880` | 326 | UnwindData |  |
| 525 | `_mbsnbcat_s` | `0x509D0` | 20 | UnwindData |  |
| 526 | `_mbsnbcat_s_l` | `0x509F0` | 646 | UnwindData |  |
| 527 | `_mbsnbcmp` | `0x50C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `_mbsnbcmp_l` | `0x50C90` | 297 | UnwindData |  |
| 529 | `_mbsnbcnt` | `0x50DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `_mbsnbcnt_l` | `0x50DD0` | 151 | UnwindData |  |
| 531 | `_mbsnbcoll` | `0x50E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | `_mbsnbcoll_l` | `0x50E80` | 275 | UnwindData |  |
| 533 | `_mbsnbcpy` | `0x50FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `_mbsnbcpy_l` | `0x50FB0` | 242 | UnwindData |  |
| 535 | `_mbsnbcpy_s` | `0x510B0` | 20 | UnwindData |  |
| 536 | `_mbsnbcpy_s_l` | `0x510D0` | 510 | UnwindData |  |
| 537 | `_mbsnbicmp` | `0x512D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `_mbsnbicmp_l` | `0x512E0` | 423 | UnwindData |  |
| 539 | `_mbsnbicoll` | `0x51490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `_mbsnbicoll_l` | `0x514A0` | 255 | UnwindData |  |
| 541 | `_mbsnbset` | `0x515A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `_mbsnbset_l` | `0x515B0` | 242 | UnwindData |  |
| 543 | `_mbsnbset_s` | `0x516B0` | 20 | UnwindData |  |
| 544 | `_mbsnbset_s_l` | `0x516D0` | 584 | UnwindData |  |
| 545 | `_mbsncat` | `0x51920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | `_mbsncat_l` | `0x51930` | 299 | UnwindData |  |
| 547 | `_mbsncat_s` | `0x51A60` | 20 | UnwindData |  |
| 548 | `_mbsncat_s_l` | `0x51A80` | 587 | UnwindData |  |
| 549 | `_mbsnccnt` | `0x51CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `_mbsnccnt_l` | `0x51CE0` | 152 | UnwindData |  |
| 551 | `_mbsncmp` | `0x51D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `_mbsncmp_l` | `0x51D90` | 256 | UnwindData |  |
| 553 | `_mbsncoll` | `0x51E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `_mbsncoll_l` | `0x51EA0` | 313 | UnwindData |  |
| 555 | `_mbsncpy` | `0x51FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 556 | `_mbsncpy_l` | `0x51FF0` | 226 | UnwindData |  |
| 557 | `_mbsncpy_s` | `0x520E0` | 20 | UnwindData |  |
| 558 | `_mbsncpy_s_l` | `0x52100` | 509 | UnwindData |  |
| 559 | `_mbsnextc` | `0x52300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `_mbsnextc_l` | `0x52310` | 116 | UnwindData |  |
| 561 | `_mbsnicmp` | `0x52390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 562 | `_mbsnicmp_l` | `0x523A0` | 387 | UnwindData |  |
| 563 | `_mbsnicoll` | `0x52530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `_mbsnicoll_l` | `0x52540` | 313 | UnwindData |  |
| 565 | `_mbsninc` | `0x52680` | 35 | UnwindData |  |
| 566 | `_mbsninc_l` | `0x526B0` | 34 | UnwindData |  |
| 567 | `_mbsnlen` | `0x526E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 568 | `_mbsnlen_l` | `0x526F0` | 152 | UnwindData |  |
| 569 | `_mbsnset` | `0x52790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `_mbsnset_l` | `0x527A0` | 347 | UnwindData |  |
| 571 | `_mbsnset_s` | `0x52900` | 20 | UnwindData |  |
| 572 | `_mbsnset_s_l` | `0x52920` | 557 | UnwindData |  |
| 573 | `_mbspbrk` | `0x52B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `_mbspbrk_l` | `0x52B60` | 222 | UnwindData |  |
| 575 | `_mbsrchr` | `0x52C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `_mbsrchr_l` | `0x52C50` | 187 | UnwindData |  |
| 577 | `_mbsrev` | `0x52D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `_mbsrev_l` | `0x52D20` | 212 | UnwindData |  |
| 579 | `_mbsset` | `0x52E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `_mbsset_l` | `0x52E10` | 212 | UnwindData |  |
| 581 | `_mbsset_s` | `0x52EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 582 | `_mbsset_s_l` | `0x52F00` | 319 | UnwindData |  |
| 583 | `_mbsspn` | `0x53040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `_mbsspn_l` | `0x53050` | 237 | UnwindData |  |
| 585 | `_mbsspnp` | `0x53140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `_mbsspnp_l` | `0x53150` | 237 | UnwindData |  |
| 587 | `_mbsstr` | `0x53240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `_mbsstr_l` | `0x53250` | 249 | UnwindData |  |
| 589 | `_mbstok` | `0x53350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `_mbstok_l` | `0x53360` | 62 | UnwindData |  |
| 591 | `_mbstok_s` | `0x533A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `_mbstok_s_l` | `0x533B0` | 440 | UnwindData |  |
| 593 | `_mbstowcs_l` | `0x53890` | 165 | UnwindData |  |
| 594 | `_mbstowcs_s_l` | `0x53940` | 182 | UnwindData |  |
| 1185 | `mbstowcs` | `0x53A00` | 154 | UnwindData |  |
| 1186 | `mbstowcs_s` | `0x53AA0` | 168 | UnwindData |  |
| 595 | `_mbstrlen` | `0x53C30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 596 | `_mbstrlen_l` | `0x53C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `_mbstrnlen` | `0x53C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `_mbstrnlen_l` | `0x53C80` | 52 | UnwindData |  |
| 599 | `_mbsupr` | `0x53CC0` | 43 | UnwindData |  |
| 600 | `_mbsupr_l` | `0x53CF0` | 43 | UnwindData |  |
| 601 | `_mbsupr_s` | `0x53D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `_mbsupr_s_l` | `0x53D30` | 340 | UnwindData |  |
| 603 | `_mbtowc_l` | `0x54000` | 163 | UnwindData |  |
| 1187 | `mbtowc` | `0x540B0` | 152 | UnwindData |  |
| 604 | `_memccpy` | `0x54150` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `_memicmp` | `0x541C0` | 80 | UnwindData |  |
| 606 | `_memicmp_l` | `0x54210` | 170 | UnwindData |  |
| 607 | `_mkdir` | `0x542C0` | 226 | UnwindData |  |
| 608 | `_mkgmtime32` | `0x54A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `_mkgmtime64` | `0x54A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 612 | `_mktime32` | `0x54A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 613 | `_mktime64` | `0x54A40` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 610 | `_mktemp` | `0x54CD0` | 78 | UnwindData |  |
| 611 | `_mktemp_s` | `0x54D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `_wmktemp` | `0x54D30` | 79 | UnwindData |  |
| 865 | `_wmktemp_s` | `0x54D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | `_msize` | `0x54D90` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 617 | `_open` | `0x55610` | 35 | UnwindData |  |
| 672 | `_sopen` | `0x55640` | 65 | UnwindData |  |
| 673 | `_sopen_dispatch` | `0x55690` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `_sopen_s` | `0x557C0` | 50 | UnwindData |  |
| 866 | `_wopen` | `0x55800` | 35 | UnwindData |  |
| 878 | `_wsopen` | `0x55830` | 65 | UnwindData |  |
| 879 | `_wsopen_dispatch` | `0x55880` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `_wsopen_s` | `0x55C80` | 50 | UnwindData |  |
| 619 | `_pclose` | `0x56A80` | 213 | UnwindData |  |
| 621 | `_popen` | `0x56B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `_wpopen` | `0x56B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 620 | `_pipe` | `0x56B80` | 676 | UnwindData |  |
| 623 | `_putch` | `0x56E70` | 58 | UnwindData |  |
| 624 | `_putch_nolock` | `0x56EB0` | 152 | UnwindData |  |
| 625 | `_putenv` | `0x576B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 626 | `_putenv_s` | `0x576C0` | 56 | UnwindData |  |
| 869 | `_wputenv` | `0x57700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | `_wputenv_s` | `0x57710` | 56 | UnwindData |  |
| 627 | `_putw` | `0x57750` | 151 | UnwindData |  |
| 629 | `_putwch` | `0x57830` | 59 | UnwindData |  |
| 630 | `_putwch_nolock` | `0x57870` | 59 | UnwindData |  |
| 631 | `_putws` | `0x579A0` | 257 | UnwindData |  |
| 632 | `_query_app_type` | `0x57AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 655 | `_set_app_type` | `0x57AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 634 | `_query_new_mode` | `0x57AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 663 | `_set_new_mode` | `0x57AE0` | 43 | UnwindData |  |
| 635 | `_read` | `0x57FC0` | 281 | UnwindData |  |
| 636 | `_realloc_base` | `0x58530` | 122 | UnwindData |  |
| 637 | `_recalloc` | `0x585B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 640 | `_resetstkoflw` | `0x58650` | 300 | UnwindData |  |
| 641 | `_rmdir` | `0x58780` | 226 | UnwindData |  |
| 642 | `_rmtmp` | `0x58890` | 146 | UnwindData |  |
| 649 | `_searchenv` | `0x59020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `_searchenv_s` | `0x59030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `_wsearchenv` | `0x59040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 876 | `_wsearchenv_s` | `0x59050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | `_seh_filter_dll` | `0x59060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `_seh_filter_exe` | `0x59080` | 385 | UnwindData |  |
| 654 | `_set_abort_behavior` | `0x59210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `abort` | `0x59230` | 86 | UnwindData |  |
| 659 | `_set_error_mode` | `0x59290` | 64 | UnwindData |  |
| 666 | `_seterrormode` | `0x592D0` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `_splitpath` | `0x59D80` | 108 | UnwindData |  |
| 684 | `_splitpath_s` | `0x59DF0` | 99 | UnwindData |  |
| 889 | `_wsplitpath` | `0x59E60` | 108 | UnwindData |  |
| 890 | `_wsplitpath_s` | `0x59ED0` | 99 | UnwindData |  |
| 690 | `_strcoll_l` | `0x59F40` | 199 | UnwindData |  |
| 1259 | `strcoll` | `0x5A010` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `_strdate` | `0x5A280` | 36 | UnwindData |  |
| 692 | `_strdate_s` | `0x5A2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `_wstrdate` | `0x5A2C0` | 36 | UnwindData |  |
| 896 | `_wstrdate_s` | `0x5A2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `_mbsdup` | `0x5A300` | 117 | UnwindData |  |
| 693 | `_strdup` | `0x5A300` | 117 | UnwindData |  |
| 697 | `_stricmp` | `0x5A3C0` | 70 | UnwindData |  |
| 698 | `_stricmp_l` | `0x5A410` | 136 | UnwindData |  |
| 699 | `_stricoll` | `0x5A4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 700 | `_stricoll_l` | `0x5A4C0` | 184 | UnwindData |  |
| 701 | `_strlwr` | `0x5A7A0` | 94 | UnwindData |  |
| 702 | `_strlwr_l` | `0x5A800` | 30 | UnwindData |  |
| 703 | `_strlwr_s` | `0x5A820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `_strlwr_s_l` | `0x5A830` | 75 | UnwindData |  |
| 705 | `_strncoll` | `0x5A880` | 79 | UnwindData |  |
| 706 | `_strncoll_l` | `0x5A8D0` | 255 | UnwindData |  |
| 707 | `_strnicmp` | `0x5AA20` | 79 | UnwindData |  |
| 708 | `_strnicmp_l` | `0x5AA70` | 173 | UnwindData |  |
| 709 | `_strnicoll` | `0x5AB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `_strnicoll_l` | `0x5AB40` | 256 | UnwindData |  |
| 711 | `_strnset` | `0x5AC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `_strnset_s` | `0x5AC60` | 116 | UnwindData |  |
| 713 | `_strrev` | `0x5ACE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `_strset` | `0x5AD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 715 | `_strset_s` | `0x5AD30` | 73 | UnwindData |  |
| 716 | `_strtime` | `0x5AFB0` | 36 | UnwindData |  |
| 717 | `_strtime_s` | `0x5AFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `_wstrtime` | `0x5AFF0` | 36 | UnwindData |  |
| 898 | `_wstrtime_s` | `0x5B020` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 718 | `_strtod_l` | `0x5B370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 724 | `_strtold_l` | `0x5B370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `_strtof_l` | `0x5B380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 806 | `_wcstod_l` | `0x5B390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 812 | `_wcstold_l` | `0x5B390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 807 | `_wcstof_l` | `0x5B3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1275 | `strtod` | `0x5B3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1281 | `strtold` | `0x5B3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1276 | `strtof` | `0x5B3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `wcstod` | `0x5B3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `wcstold` | `0x5B3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `wcstof` | `0x5B3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 720 | `_strtoi64` | `0x5B3F0` | 179 | UnwindData |  |
| 1277 | `strtoimax` | `0x5B3F0` | 179 | UnwindData |  |
| 1282 | `strtoll` | `0x5B3F0` | 179 | UnwindData |  |
| 721 | `_strtoi64_l` | `0x5B4B0` | 190 | UnwindData |  |
| 722 | `_strtoimax_l` | `0x5B4B0` | 190 | UnwindData |  |
| 725 | `_strtoll_l` | `0x5B4B0` | 190 | UnwindData |  |
| 723 | `_strtol_l` | `0x5B570` | 188 | UnwindData |  |
| 726 | `_strtoui64` | `0x5B630` | 179 | UnwindData |  |
| 1284 | `strtoull` | `0x5B630` | 179 | UnwindData |  |
| 1285 | `strtoumax` | `0x5B630` | 179 | UnwindData |  |
| 727 | `_strtoui64_l` | `0x5B6F0` | 190 | UnwindData |  |
| 729 | `_strtoull_l` | `0x5B6F0` | 190 | UnwindData |  |
| 730 | `_strtoumax_l` | `0x5B6F0` | 190 | UnwindData |  |
| 728 | `_strtoul_l` | `0x5B7B0` | 188 | UnwindData |  |
| 808 | `_wcstoi64` | `0x5B870` | 179 | UnwindData |  |
| 1333 | `wcstoimax` | `0x5B870` | 179 | UnwindData |  |
| 1338 | `wcstoll` | `0x5B870` | 179 | UnwindData |  |
| 809 | `_wcstoi64_l` | `0x5B930` | 190 | UnwindData |  |
| 810 | `_wcstoimax_l` | `0x5B930` | 190 | UnwindData |  |
| 813 | `_wcstoll_l` | `0x5B930` | 190 | UnwindData |  |
| 811 | `_wcstol_l` | `0x5B9F0` | 188 | UnwindData |  |
| 816 | `_wcstoui64` | `0x5BAB0` | 179 | UnwindData |  |
| 1342 | `wcstoull` | `0x5BAB0` | 179 | UnwindData |  |
| 1343 | `wcstoumax` | `0x5BAB0` | 179 | UnwindData |  |
| 817 | `_wcstoui64_l` | `0x5BB70` | 190 | UnwindData |  |
| 819 | `_wcstoull_l` | `0x5BB70` | 190 | UnwindData |  |
| 820 | `_wcstoumax_l` | `0x5BB70` | 190 | UnwindData |  |
| 818 | `_wcstoul_l` | `0x5BC30` | 188 | UnwindData |  |
| 1280 | `strtol` | `0x5BCF0` | 177 | UnwindData |  |
| 1283 | `strtoul` | `0x5BDB0` | 177 | UnwindData |  |
| 1336 | `wcstol` | `0x5BE70` | 177 | UnwindData |  |
| 1341 | `wcstoul` | `0x5BF30` | 177 | UnwindData |  |
| 731 | `_strupr` | `0x5C210` | 94 | UnwindData |  |
| 732 | `_strupr_l` | `0x5C270` | 30 | UnwindData |  |
| 733 | `_strupr_s` | `0x5C290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `_strupr_s_l` | `0x5C2A0` | 75 | UnwindData |  |
| 735 | `_strxfrm_l` | `0x5C2F0` | 377 | UnwindData |  |
| 1286 | `strxfrm` | `0x5C470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 736 | `_swab` | `0x5C480` | 89 | UnwindData |  |
| 737 | `_tell` | `0x5C4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 738 | `_telli64` | `0x5C4F0` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 739 | `_tempnam` | `0x5CCA0` | 26 | UnwindData |  |
| 900 | `_wtempnam` | `0x5CCC0` | 26 | UnwindData |  |
| 740 | `_time32` | `0x5CCE0` | 106 | UnwindData |  |
| 741 | `_time64` | `0x5CD50` | 109 | UnwindData |  |
| 742 | `_timespec32_get` | `0x5CDC0` | 152 | UnwindData |  |
| 743 | `_timespec64_get` | `0x5CE60` | 153 | UnwindData |  |
| 744 | `_tolower` | `0x5CF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `_tolower_l` | `0x5CF10` | 307 | UnwindData |  |
| 746 | `_toupper` | `0x5D050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `_toupper_l` | `0x5D060` | 307 | UnwindData |  |
| 1300 | `tolower` | `0x5D1A0` | 42 | UnwindData |  |
| 1301 | `toupper` | `0x5D1D0` | 42 | UnwindData |  |
| 748 | `_towlower_l` | `0x5D200` | 245 | UnwindData |  |
| 1303 | `towlower` | `0x5D300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `_towupper_l` | `0x5D310` | 243 | UnwindData |  |
| 1304 | `towupper` | `0x5D410` | 3,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `_tzset` | `0x5DFF0` | 40 | UnwindData |  |
| 759 | `_umask` | `0x5E020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 760 | `_umask_s` | `0x5E040` | 61 | UnwindData |  |
| 761 | `_ungetc_nolock` | `0x5E080` | 288 | UnwindData |  |
| 1308 | `ungetc` | `0x5E1A0` | 88 | UnwindData |  |
| 764 | `_ungetwc_nolock` | `0x5E340` | 313 | UnwindData |  |
| 1309 | `ungetwc` | `0x5E480` | 94 | UnwindData |  |
| 767 | `_unlink` | `0x5E4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `remove` | `0x5E4F0` | 226 | UnwindData |  |
| 773 | `_waccess` | `0x5E5E0` | 18 | UnwindData |  |
| 774 | `_waccess_s` | `0x5E600` | 170 | UnwindData |  |
| 775 | `_wasctime` | `0x5EB70` | 134 | UnwindData |  |
| 776 | `_wasctime_s` | `0x5EC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `asctime` | `0x5EC10` | 134 | UnwindData |  |
| 927 | `asctime_s` | `0x5ECA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `_wchmod` | `0x5ECB0` | 155 | UnwindData |  |
| 782 | `_wcscoll_l` | `0x5ED50` | 188 | UnwindData |  |
| 1315 | `wcscoll` | `0x5EE10` | 101 | UnwindData |  |
| 783 | `_wcsdup` | `0x5EE80` | 130 | UnwindData |  |
| 784 | `_wcserror` | `0x5EF10` | 176 | UnwindData |  |
| 785 | `_wcserror_s` | `0x5EFC0` | 143 | UnwindData |  |
| 1263 | `strerror` | `0x5F050` | 157 | UnwindData |  |
| 1264 | `strerror_s` | `0x5F0F0` | 139 | UnwindData |  |
| 787 | `_wcsicmp` | `0x5F1C0` | 70 | UnwindData |  |
| 788 | `_wcsicmp_l` | `0x5F210` | 295 | UnwindData |  |
| 789 | `_wcsicoll` | `0x5F340` | 70 | UnwindData |  |
| 790 | `_wcsicoll_l` | `0x5F390` | 169 | UnwindData |  |
| 791 | `_wcslwr` | `0x5F640` | 102 | UnwindData |  |
| 792 | `_wcslwr_l` | `0x5F6B0` | 30 | UnwindData |  |
| 793 | `_wcslwr_s` | `0x5F6D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `_wcslwr_s_l` | `0x5F6E0` | 75 | UnwindData |  |
| 795 | `_wcsncoll` | `0x5F730` | 79 | UnwindData |  |
| 796 | `_wcsncoll_l` | `0x5F780` | 214 | UnwindData |  |
| 797 | `_wcsnicmp` | `0x5F8B0` | 70 | UnwindData |  |
| 798 | `_wcsnicmp_l` | `0x5F900` | 335 | UnwindData |  |
| 799 | `_wcsnicoll` | `0x5FA50` | 79 | UnwindData |  |
| 800 | `_wcsnicoll_l` | `0x5FAA0` | 240 | UnwindData |  |
| 801 | `_wcsnset` | `0x5FB90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `_wcsnset_s` | `0x5FBC0` | 122 | UnwindData |  |
| 803 | `_wcsrev` | `0x5FC40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 804 | `_wcsset` | `0x5FC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `_wcsset_s` | `0x5FCA0` | 78 | UnwindData |  |
| 814 | `_wcstombs_l` | `0x60150` | 165 | UnwindData |  |
| 815 | `_wcstombs_s_l` | `0x60200` | 182 | UnwindData |  |
| 1339 | `wcstombs` | `0x602C0` | 154 | UnwindData |  |
| 1340 | `wcstombs_s` | `0x60360` | 168 | UnwindData |  |
| 821 | `_wcsupr` | `0x60600` | 102 | UnwindData |  |
| 822 | `_wcsupr_l` | `0x60670` | 30 | UnwindData |  |
| 823 | `_wcsupr_s` | `0x60690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | `_wcsupr_s_l` | `0x606A0` | 75 | UnwindData |  |
| 825 | `_wcsxfrm_l` | `0x606F0` | 358 | UnwindData |  |
| 1344 | `wcsxfrm` | `0x60860` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `_wctomb_l` | `0x60A20` | 235 | UnwindData |  |
| 831 | `_wctomb_s_l` | `0x60B10` | 173 | UnwindData |  |
| 1346 | `wctomb` | `0x60BC0` | 197 | UnwindData |  |
| 1347 | `wctomb_s` | `0x60C90` | 159 | UnwindData |  |
| 853 | `_wfreopen` | `0x60F30` | 47 | UnwindData |  |
| 854 | `_wfreopen_s` | `0x60F60` | 22 | UnwindData |  |
| 1094 | `freopen` | `0x60F80` | 47 | UnwindData |  |
| 1095 | `freopen_s` | `0x60FB0` | 22 | UnwindData |  |
| 863 | `_wmkdir` | `0x60FD0` | 41 | UnwindData |  |
| 867 | `_wperror` | `0x61000` | 202 | UnwindData |  |
| 871 | `_wremove` | `0x610D0` | 39 | UnwindData |  |
| 913 | `_wunlink` | `0x61100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `_wrename` | `0x61110` | 45 | UnwindData |  |
| 873 | `_write` | `0x61960` | 152 | UnwindData |  |
| 874 | `_wrmdir` | `0x61E30` | 39 | UnwindData |  |
| 899 | `_wsystem` | `0x61E60` | 327 | UnwindData |  |
| 1287 | `system` | `0x61FB0` | 327 | UnwindData |  |
| 901 | `_wtmpnam` | `0x62A50` | 38 | UnwindData |  |
| 902 | `_wtmpnam_s` | `0x62A80` | 53 | UnwindData |  |
| 1296 | `tmpfile` | `0x62AC0` | 35 | UnwindData |  |
| 1297 | `tmpfile_s` | `0x62AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1298 | `tmpnam` | `0x62B00` | 38 | UnwindData |  |
| 1299 | `tmpnam_s` | `0x62B30` | 53 | UnwindData |  |
| 921 | `acos` | `0x62B70` | 670 | UnwindData |  |
| 922 | `acosf` | `0x62E10` | 556 | UnwindData |  |
| 923 | `acosh` | `0x63040` | 194 | UnwindData |  |
| 924 | `acoshf` | `0x63110` | 189 | UnwindData |  |
| 925 | `acoshl` | `0x631D0` | 194 | UnwindData |  |
| 928 | `asin` | `0x632A0` | 644 | UnwindData |  |
| 929 | `asinf` | `0x63530` | 490 | UnwindData |  |
| 930 | `asinh` | `0x63720` | 200 | UnwindData |  |
| 931 | `asinhf` | `0x637F0` | 194 | UnwindData |  |
| 932 | `asinhl` | `0x638C0` | 200 | UnwindData |  |
| 933 | `atan` | `0x63990` | 533 | UnwindData |  |
| 934 | `atan2` | `0x63BB0` | 1,770 | UnwindData |  |
| 935 | `atan2f` | `0x642A0` | 1,015 | UnwindData |  |
| 936 | `atanf` | `0x646A0` | 492 | UnwindData |  |
| 937 | `atanh` | `0x64890` | 193 | UnwindData |  |
| 938 | `atanhf` | `0x64960` | 185 | UnwindData |  |
| 939 | `atanhl` | `0x64A20` | 193 | UnwindData |  |
| 944 | `bsearch` | `0x64AF0` | 268 | UnwindData |  |
| 945 | `bsearch_s` | `0x64C00` | 278 | UnwindData |  |
| 946 | `btowc` | `0x652A0` | 216 | UnwindData |  |
| 1179 | `mbrlen` | `0x65380` | 197 | UnwindData |  |
| 1182 | `mbrtowc` | `0x65450` | 231 | UnwindData |  |
| 1183 | `mbsrtowcs` | `0x65540` | 161 | UnwindData |  |
| 1184 | `mbsrtowcs_s` | `0x655F0` | 355 | UnwindData |  |
| 947 | `c16rtomb` | `0x65800` | 154 | UnwindData |  |
| 948 | `c32rtomb` | `0x65940` | 154 | UnwindData |  |
| 949 | `cabs` | `0x659E0` | 63 | UnwindData |  |
| 950 | `cabsf` | `0x65A20` | 64 | UnwindData |  |
| 951 | `cabsl` | `0x65A60` | 63 | UnwindData |  |
| 952 | `cacos` | `0x65AA0` | 802 | UnwindData |  |
| 953 | `cacosf` | `0x65DD0` | 696 | UnwindData |  |
| 954 | `cacosh` | `0x66090` | 876 | UnwindData |  |
| 955 | `cacoshf` | `0x66400` | 760 | UnwindData |  |
| 956 | `cacoshl` | `0x66700` | 876 | UnwindData |  |
| 957 | `cacosl` | `0x66A70` | 802 | UnwindData |  |
| 958 | `calloc` | `0x66DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 959 | `carg` | `0x66DB0` | 66 | UnwindData |  |
| 960 | `cargf` | `0x66E00` | 67 | UnwindData |  |
| 961 | `cargl` | `0x66E50` | 63 | UnwindData |  |
| 962 | `casin` | `0x66E90` | 192 | UnwindData |  |
| 963 | `casinf` | `0x66F50` | 122 | UnwindData |  |
| 964 | `casinh` | `0x66FD0` | 816 | UnwindData |  |
| 965 | `casinhf` | `0x67300` | 687 | UnwindData |  |
| 966 | `casinhl` | `0x675B0` | 816 | UnwindData |  |
| 967 | `casinl` | `0x678E0` | 192 | UnwindData |  |
| 968 | `catan` | `0x679A0` | 192 | UnwindData |  |
| 969 | `catanf` | `0x67A60` | 122 | UnwindData |  |
| 970 | `catanh` | `0x67AE0` | 877 | UnwindData |  |
| 971 | `catanhf` | `0x67E50` | 822 | UnwindData |  |
| 972 | `catanhl` | `0x68190` | 877 | UnwindData |  |
| 973 | `catanl` | `0x68500` | 192 | UnwindData |  |
| 974 | `cbrt` | `0x685C0` | 379 | UnwindData |  |
| 975 | `cbrtf` | `0x68740` | 336 | UnwindData |  |
| 976 | `cbrtl` | `0x68890` | 379 | UnwindData |  |
| 977 | `ccos` | `0x68A10` | 118 | UnwindData |  |
| 978 | `ccosf` | `0x68A90` | 79 | UnwindData |  |
| 979 | `ccosh` | `0x68BE0` | 445 | UnwindData |  |
| 980 | `ccoshf` | `0x68EA0` | 373 | UnwindData |  |
| 981 | `ccoshl` | `0x69110` | 445 | UnwindData |  |
| 982 | `ccosl` | `0x692D0` | 118 | UnwindData |  |
| 983 | `ceil` | `0x69350` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 984 | `ceilf` | `0x69420` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `cexp` | `0x694B0` | 516 | UnwindData |  |
| 986 | `cexpf` | `0x696C0` | 475 | UnwindData |  |
| 987 | `cexpl` | `0x698A0` | 516 | UnwindData |  |
| 988 | `cimag` | `0x69AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `cimagl` | `0x69AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `cimagf` | `0x69AC0` | 19 | UnwindData |  |
| 991 | `clearerr` | `0x69AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `clearerr_s` | `0x69AF0` | 168 | UnwindData |  |
| 993 | `clock` | `0x69C00` | 97 | UnwindData |  |
| 994 | `clog` | `0x69C70` | 558 | UnwindData |  |
| 995 | `clog10` | `0x69EA0` | 81 | UnwindData |  |
| 996 | `clog10f` | `0x69F00` | 29 | UnwindData |  |
| 997 | `clog10l` | `0x69F20` | 81 | UnwindData |  |
| 998 | `clogf` | `0x69F80` | 509 | UnwindData |  |
| 999 | `clogl` | `0x6A180` | 558 | UnwindData |  |
| 1000 | `conj` | `0x6A3B0` | 98 | UnwindData |  |
| 1002 | `conjl` | `0x6A3B0` | 98 | UnwindData |  |
| 1001 | `conjf` | `0x6A420` | 75 | UnwindData |  |
| 1003 | `copysign` | `0x6A470` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `copysignl` | `0x6A470` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `copysignf` | `0x6A4B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `cos` | `0x6A4F0` | 1,402 | UnwindData |  |
| 1007 | `cosf` | `0x6AA70` | 1,279 | UnwindData |  |
| 1008 | `cosh` | `0x6AF70` | 880 | UnwindData |  |
| 1009 | `coshf` | `0x6B410` | 656 | UnwindData |  |
| 1016 | `creal` | `0x6B7D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `creall` | `0x6B7D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `crealf` | `0x6B7E0` | 18 | UnwindData |  |
| 1019 | `csin` | `0x6B800` | 192 | UnwindData |  |
| 1020 | `csinf` | `0x6B8C0` | 122 | UnwindData |  |
| 1021 | `csinh` | `0x6BAE0` | 352 | UnwindData |  |
| 1022 | `csinhf` | `0x6BDC0` | 287 | UnwindData |  |
| 1023 | `csinhl` | `0x6C080` | 352 | UnwindData |  |
| 1024 | `csinl` | `0x6C1E0` | 192 | UnwindData |  |
| 1025 | `csqrt` | `0x6C4A0` | 487 | UnwindData |  |
| 1026 | `csqrtf` | `0x6C880` | 440 | UnwindData |  |
| 1027 | `csqrtl` | `0x6CC30` | 487 | UnwindData |  |
| 1028 | `ctan` | `0x6CE20` | 192 | UnwindData |  |
| 1029 | `ctanf` | `0x6CEE0` | 122 | UnwindData |  |
| 1030 | `ctanh` | `0x6CF60` | 407 | UnwindData |  |
| 1031 | `ctanhf` | `0x6D100` | 360 | UnwindData |  |
| 1032 | `ctanhl` | `0x6D270` | 407 | UnwindData |  |
| 1033 | `ctanl` | `0x6D410` | 192 | UnwindData |  |
| 1034 | `div` | `0x6D4D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `ldiv` | `0x6D4D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `erf` | `0x6D560` | 365 | UnwindData |  |
| 1039 | `erff` | `0x6D760` | 286 | UnwindData |  |
| 1040 | `erfl` | `0x6D900` | 365 | UnwindData |  |
| 1042 | `exp` | `0x6DA70` | 1,013 | UnwindData |  |
| 1046 | `expf` | `0x6DE70` | 679 | UnwindData |  |
| 1047 | `expm1` | `0x6E120` | 288 | UnwindData |  |
| 1048 | `expm1f` | `0x6E240` | 209 | UnwindData |  |
| 1049 | `expm1l` | `0x6E320` | 288 | UnwindData |  |
| 1050 | `fabs` | `0x6E440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `fdim` | `0x6E450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `fdiml` | `0x6E450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1053 | `fdimf` | `0x6E480` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1055 | `feclearexcept` | `0x6E4B0` | 82 | UnwindData |  |
| 1056 | `fegetenv` | `0x6E510` | 32 | UnwindData |  |
| 1057 | `fegetexceptflag` | `0x6E530` | 65 | UnwindData |  |
| 1059 | `feholdexcept` | `0x6E580` | 80 | UnwindData |  |
| 1060 | `feof` | `0x6E5D0` | 43 | UnwindData |  |
| 1061 | `ferror` | `0x6E600` | 43 | UnwindData |  |
| 1062 | `fesetenv` | `0x6E630` | 76 | UnwindData |  |
| 1063 | `fesetexceptflag` | `0x6E680` | 121 | UnwindData |  |
| 1064 | `fesetround` | `0x6E700` | 110 | UnwindData |  |
| 1065 | `fetestexcept` | `0x6E770` | 33 | UnwindData |  |
| 1068 | `fgetpos` | `0x6E7A0` | 75 | UnwindData |  |
| 1069 | `fgets` | `0x6E980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `fgetws` | `0x6E990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `floor` | `0x6E9A0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `floorf` | `0x6EA50` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `fma` | `0x6F200` | 687 | UnwindData |  |
| 1075 | `fmaf` | `0x6FB70` | 669 | UnwindData |  |
| 1076 | `fmal` | `0x704F0` | 687 | UnwindData |  |
| 1077 | `fmax` | `0x707A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1079 | `fmaxl` | `0x707A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `fmaxf` | `0x707E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1080 | `fmin` | `0x70820` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1082 | `fminl` | `0x70820` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1081 | `fminf` | `0x70860` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1083 | `fmod` | `0x708A0` | 724 | UnwindData |  |
| 1084 | `fmodf` | `0x70B80` | 575 | UnwindData |  |
| 1088 | `fputs` | `0x70E90` | 420 | UnwindData |  |
| 1090 | `fputws` | `0x71110` | 253 | UnwindData |  |
| 1093 | `free` | `0x71210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `frexp` | `0x71230` | 248 | UnwindData |  |
| 1098 | `fsetpos` | `0x71330` | 53 | UnwindData |  |
| 1110 | `ilogb` | `0x71370` | 70 | UnwindData |  |
| 1111 | `ilogbf` | `0x713C0` | 70 | UnwindData |  |
| 1112 | `ilogbl` | `0x71410` | 70 | UnwindData |  |
| 1114 | `imaxdiv` | `0x71460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `ldexp` | `0x71480` | 366 | UnwindData |  |
| 1150 | `lldiv` | `0x715F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `llrint` | `0x71610` | 121 | UnwindData |  |
| 1152 | `llrintf` | `0x71690` | 118 | UnwindData |  |
| 1153 | `llrintl` | `0x71710` | 121 | UnwindData |  |
| 1154 | `llround` | `0x71790` | 90 | UnwindData |  |
| 1155 | `llroundf` | `0x717F0` | 88 | UnwindData |  |
| 1156 | `llroundl` | `0x71850` | 90 | UnwindData |  |
| 1157 | `localeconv` | `0x718B0` | 51 | UnwindData |  |
| 1158 | `log` | `0x718F0` | 1,323 | UnwindData |  |
| 1159 | `log10` | `0x71E20` | 1,451 | UnwindData |  |
| 1160 | `log10f` | `0x723D0` | 1,237 | UnwindData |  |
| 1161 | `log1p` | `0x728B0` | 201 | UnwindData |  |
| 1162 | `log1pf` | `0x72980` | 197 | UnwindData |  |
| 1163 | `log1pl` | `0x72A50` | 201 | UnwindData |  |
| 1164 | `log2` | `0x72B20` | 807 | UnwindData |  |
| 1167 | `logb` | `0x72E50` | 109 | UnwindData |  |
| 1168 | `logbf` | `0x72EC0` | 108 | UnwindData |  |
| 1169 | `logbl` | `0x72F30` | 109 | UnwindData |  |
| 1170 | `logf` | `0x72FA0` | 1,014 | UnwindData |  |
| 1171 | `lrint` | `0x733A0` | 120 | UnwindData |  |
| 1172 | `lrintf` | `0x73420` | 117 | UnwindData |  |
| 1173 | `lrintl` | `0x734A0` | 120 | UnwindData |  |
| 1174 | `lround` | `0x73520` | 89 | UnwindData |  |
| 1175 | `lroundf` | `0x73580` | 87 | UnwindData |  |
| 1176 | `lroundl` | `0x735E0` | 89 | UnwindData |  |
| 1177 | `malloc` | `0x73640` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `mbrtoc16` | `0x73740` | 161 | UnwindData |  |
| 1181 | `mbrtoc32` | `0x739C0` | 161 | UnwindData |  |
| 1188 | `memcpy_s` | `0x73A70` | 135 | UnwindData |  |
| 1189 | `memmove_s` | `0x73B00` | 81 | UnwindData |  |
| 1191 | `modf` | `0x73B60` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1192 | `modff` | `0x73C40` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `nearbyint` | `0x73CF0` | 41 | UnwindData |  |
| 1197 | `nearbyintf` | `0x73D20` | 41 | UnwindData |  |
| 1198 | `nearbyintl` | `0x73D50` | 41 | UnwindData |  |
| 1199 | `nextafter` | `0x73D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1200 | `nextafterf` | `0x73D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1201 | `nextafterl` | `0x73DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `nexttoward` | `0x73DB0` | 365 | UnwindData |  |
| 1203 | `nexttowardf` | `0x73F20` | 315 | UnwindData |  |
| 1204 | `nexttowardl` | `0x74060` | 365 | UnwindData |  |
| 1205 | `norm` | `0x741D0` | 78 | UnwindData |  |
| 1207 | `norml` | `0x741D0` | 78 | UnwindData |  |
| 1206 | `normf` | `0x74220` | 69 | UnwindData |  |
| 1208 | `perror` | `0x74340` | 138 | UnwindData |  |
| 1209 | `pow` | `0x743D0` | 5,777 | UnwindData |  |
| 1210 | `powf` | `0x75A70` | 3,782 | UnwindData |  |
| 1213 | `puts` | `0x76A20` | 420 | UnwindData |  |
| 1216 | `qsort` | `0x76BD0` | 91 | UnwindData |  |
| 1217 | `qsort_s` | `0x76FE0` | 106 | UnwindData |  |
| 1220 | `rand` | `0x77420` | 41 | UnwindData |  |
| 1255 | `srand` | `0x77450` | 22 | UnwindData |  |
| 1221 | `rand_s` | `0x77470` | 76 | UnwindData |  |
| 1222 | `realloc` | `0x774C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `remainder` | `0x774D0` | 936 | UnwindData |  |
| 1224 | `remainderf` | `0x77880` | 640 | UnwindData |  |
| 1225 | `remainderl` | `0x77B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `remquo` | `0x77B10` | 482 | UnwindData |  |
| 1228 | `remquof` | `0x77D00` | 473 | UnwindData |  |
| 1229 | `remquol` | `0x77EE0` | 482 | UnwindData |  |
| 1230 | `rename` | `0x780D0` | 316 | UnwindData |  |
| 1231 | `rewind` | `0x78300` | 138 | UnwindData |  |
| 1232 | `rint` | `0x784C0` | 75 | UnwindData |  |
| 1233 | `rintf` | `0x78640` | 74 | UnwindData |  |
| 1234 | `rintl` | `0x787C0` | 75 | UnwindData |  |
| 1235 | `round` | `0x78810` | 101 | UnwindData |  |
| 1236 | `roundf` | `0x78880` | 101 | UnwindData |  |
| 1237 | `roundl` | `0x788F0` | 101 | UnwindData |  |
| 1238 | `scalbln` | `0x78960` | 90 | UnwindData |  |
| 1241 | `scalbn` | `0x78960` | 90 | UnwindData |  |
| 1239 | `scalblnf` | `0x789C0` | 90 | UnwindData |  |
| 1242 | `scalbnf` | `0x789C0` | 90 | UnwindData |  |
| 1240 | `scalblnl` | `0x78A20` | 90 | UnwindData |  |
| 1243 | `scalbnl` | `0x78A20` | 90 | UnwindData |  |
| 1245 | `setbuf` | `0x78A80` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1246 | `setlocale` | `0x78D90` | 76 | UnwindData |  |
| 1247 | `setvbuf` | `0x78F10` | 312 | UnwindData |  |
| 1249 | `sin` | `0x79050` | 1,386 | UnwindData |  |
| 1250 | `sinf` | `0x795C0` | 1,782 | UnwindData |  |
| 1251 | `sinh` | `0x79CC0` | 940 | UnwindData |  |
| 1252 | `sinhf` | `0x7A190` | 676 | UnwindData |  |
| 1253 | `sqrt` | `0x7A560` | 201 | UnwindData |  |
| 1254 | `sqrtf` | `0x7A630` | 159 | UnwindData |  |
| 1256 | `strcat` | `0x7A6E0` | 144 | UnwindData |  |
| 1260 | `strcpy` | `0x7A780` | 183 | UnwindData |  |
| 1257 | `strcat_s` | `0x7A840` | 121 | UnwindData |  |
| 1258 | `strcmp` | `0x7A8D0` | 103 | UnwindData |  |
| 1261 | `strcpy_s` | `0x7A940` | 95 | UnwindData |  |
| 1262 | `strcspn` | `0x7AA40` | 202 | UnwindData |  |
| 1266 | `strlen` | `0x7AE20` | 168 | UnwindData |  |
| 1267 | `strncat` | `0x7AEE0` | 405 | UnwindData |  |
| 1268 | `strncat_s` | `0x7B080` | 240 | UnwindData |  |
| 1269 | `strncmp` | `0x7B180` | 125 | UnwindData |  |
| 1270 | `strncpy` | `0x7B210` | 354 | UnwindData |  |
| 1271 | `strncpy_s` | `0x7B380` | 239 | UnwindData |  |
| 1272 | `strnlen` | `0x7B470` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `wcslen` | `0x7B5C0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `wcsnlen` | `0x7B6F0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1273 | `strpbrk` | `0x7B970` | 968 | UnwindData |  |
| 1274 | `strspn` | `0x7BE00` | 202 | UnwindData |  |
| 1278 | `strtok` | `0x7C1D0` | 46 | UnwindData |  |
| 1279 | `strtok_s` | `0x7C330` | 56 | UnwindData |  |
| 1288 | `tan` | `0x7C370` | 1,459 | UnwindData |  |
| 1289 | `tanf` | `0x7CB10` | 1,651 | UnwindData |  |
| 1290 | `tanh` | `0x7D2B0` | 622 | UnwindData |  |
| 1291 | `tanhf` | `0x7D520` | 649 | UnwindData |  |
| 1293 | `tgamma` | `0x7E100` | 589 | UnwindData |  |
| 1294 | `tgammaf` | `0x7EBC0` | 583 | UnwindData |  |
| 1295 | `tgammal` | `0x7F760` | 589 | UnwindData |  |
| 1302 | `towctrans` | `0x7F9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1348 | `wctrans` | `0x7F9C0` | 115 | UnwindData |  |
| 1305 | `trunc` | `0x7FA40` | 33 | UnwindData |  |
| 1306 | `truncf` | `0x7FA70` | 33 | UnwindData |  |
| 1307 | `truncl` | `0x7FAA0` | 33 | UnwindData |  |
| 1310 | `wcrtomb` | `0x7FF20` | 58 | UnwindData |  |
| 1311 | `wcrtomb_s` | `0x7FF60` | 270 | UnwindData |  |
| 1328 | `wcsrtombs` | `0x80070` | 161 | UnwindData |  |
| 1329 | `wcsrtombs_s` | `0x80120` | 379 | UnwindData |  |
| 1345 | `wctob` | `0x802A0` | 251 | UnwindData |  |
| 1312 | `wcscat` | `0x803A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `wcscat_s` | `0x803D0` | 130 | UnwindData |  |
| 1314 | `wcscmp` | `0x80460` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1316 | `wcscpy` | `0x804A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `wcscpy_s` | `0x804C0` | 101 | UnwindData |  |
| 1318 | `wcscspn` | `0x80530` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `wcsncat` | `0x80570` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1322 | `wcsncat_s` | `0x805C0` | 260 | UnwindData |  |
| 1323 | `wcsncmp` | `0x806D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1324 | `wcsncpy` | `0x80700` | 71 | UnwindData |  |
| 1325 | `wcsncpy_s` | `0x80750` | 252 | UnwindData |  |
| 1327 | `wcspbrk` | `0x80850` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `wcsspn` | `0x80890` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `wcstok` | `0x808E0` | 57 | UnwindData |  |
| 1335 | `wcstok_s` | `0x809C0` | 56 | UnwindData |  |
| 1349 | `wctype` | `0x80A00` | 115 | UnwindData |  |
| 1350 | `wmemcpy_s` | `0x80A80` | 122 | UnwindData |  |
| 1351 | `wmemmove_s` | `0x80B00` | 82 | UnwindData |  |
| 1190 | `memset` | `0x94880` | 904 | UnwindData |  |
| 832 | `_wctype` | `0x9C850` | 148,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `_mbcasemap` | `0xC0DE8` | 0 | Indeterminate |  |
