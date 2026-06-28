# Binary Specification: msvcrt.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msvcrt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5938322de1c4ec43a8131a23fe60c47015696f77dfb610479c364f7ad20ff59d`
* **Total Exported Functions:** 1330

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 117 | `__STRINGTOLD` | `0x1120` | 110 | UnwindData |  |
| 189 | `_atof_l` | `0x11A0` | 243 | UnwindData |  |
| 1070 | `atof` | `0x12A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `__isascii` | `0x12B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `__iscsym` | `0x12D0` | 40 | UnwindData |  |
| 144 | `__iscsymf` | `0x1300` | 37 | UnwindData |  |
| 160 | `__toascii` | `0x1330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `_isalnum_l` | `0x1340` | 98 | UnwindData |  |
| 400 | `_isalpha_l` | `0x13B0` | 98 | UnwindData |  |
| 402 | `_iscntrl_l` | `0x1420` | 95 | UnwindData |  |
| 405 | `_isdigit_l` | `0x1490` | 95 | UnwindData |  |
| 406 | `_isgraph_l` | `0x1500` | 98 | UnwindData |  |
| 408 | `_islower_l` | `0x1570` | 95 | UnwindData |  |
| 469 | `_isprint_l` | `0x15E0` | 98 | UnwindData |  |
| 470 | `_isspace_l` | `0x1650` | 95 | UnwindData |  |
| 471 | `_isupper_l` | `0x16C0` | 95 | UnwindData |  |
| 484 | `_isxdigit_l` | `0x1730` | 98 | UnwindData |  |
| 1138 | `isalnum` | `0x17A0` | 141 | UnwindData |  |
| 1139 | `isalpha` | `0x1840` | 141 | UnwindData |  |
| 1140 | `iscntrl` | `0x18E0` | 136 | UnwindData |  |
| 1141 | `isdigit` | `0x1970` | 136 | UnwindData |  |
| 1142 | `isgraph` | `0x1A00` | 141 | UnwindData |  |
| 1144 | `islower` | `0x1AA0` | 136 | UnwindData |  |
| 1145 | `isprint` | `0x1B30` | 141 | UnwindData |  |
| 1146 | `ispunct` | `0x1BD0` | 136 | UnwindData |  |
| 1147 | `isspace` | `0x1C60` | 136 | UnwindData |  |
| 1148 | `isupper` | `0x1CF0` | 136 | UnwindData |  |
| 1162 | `isxdigit` | `0x1D80` | 141 | UnwindData |  |
| 187 | `_atodbl` | `0x1E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `_atodbl_l` | `0x1E30` | 215 | UnwindData |  |
| 190 | `_atoflt_l` | `0x1F10` | 215 | UnwindData |  |
| 195 | `_atoldbl` | `0x1FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `_atoldbl_l` | `0x2000` | 218 | UnwindData |  |
| 191 | `_atoi64` | `0x20E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `_atoi64_l` | `0x2100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `_atoi_l` | `0x2120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `_atol_l` | `0x2120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `atoi` | `0x2140` | 31 | UnwindData |  |
| 1072 | `atol` | `0x2170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `_chvalidator` | `0x2190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `_chvalidator_l` | `0x21B0` | 96 | UnwindData |  |
| 403 | `_isctype` | `0x2220` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `_isctype_l` | `0x2250` | 245 | UnwindData |  |
| 266 | `_ecvt` | `0x23F0` | 174 | UnwindData |  |
| 267 | `_ecvt_s` | `0x24B0` | 235 | UnwindData |  |
| 285 | `_fcvt` | `0x25B0` | 236 | UnwindData |  |
| 286 | `_fcvt_s` | `0x26B0` | 234 | UnwindData |  |
| 344 | `_gcvt` | `0x27A0` | 44 | UnwindData |  |
| 345 | `_gcvt_s` | `0x27E0` | 373 | UnwindData |  |
| 391 | `_i64toa` | `0x2960` | 41 | UnwindData |  |
| 485 | `_itoa` | `0x2990` | 40 | UnwindData |  |
| 510 | `_ltoa` | `0x2990` | 40 | UnwindData |  |
| 834 | `_ui64toa` | `0x29C0` | 26 | UnwindData |  |
| 838 | `_ultoa` | `0x29E0` | 26 | UnwindData |  |
| 392 | `_i64toa_s` | `0x2AF0` | 35 | UnwindData |  |
| 486 | `_itoa_s` | `0x2B20` | 34 | UnwindData |  |
| 511 | `_ltoa_s` | `0x2B20` | 34 | UnwindData |  |
| 835 | `_ui64toa_s` | `0x2B50` | 19 | UnwindData |  |
| 839 | `_ultoa_s` | `0x2B70` | 19 | UnwindData |  |
| 393 | `_i64tow` | `0x2DF0` | 41 | UnwindData |  |
| 487 | `_itow` | `0x2E20` | 40 | UnwindData |  |
| 512 | `_ltow` | `0x2E20` | 40 | UnwindData |  |
| 836 | `_ui64tow` | `0x2E50` | 26 | UnwindData |  |
| 840 | `_ultow` | `0x2E70` | 26 | UnwindData |  |
| 394 | `_i64tow_s` | `0x2FC0` | 35 | UnwindData |  |
| 488 | `_itow_s` | `0x2FF0` | 34 | UnwindData |  |
| 513 | `_ltow_s` | `0x2FF0` | 34 | UnwindData |  |
| 837 | `_ui64tow_s` | `0x3020` | 19 | UnwindData |  |
| 841 | `_ultow_s` | `0x3040` | 19 | UnwindData |  |
| 407 | `_isleadbyte_l` | `0x32F0` | 67 | UnwindData |  |
| 472 | `_iswalnum_l` | `0x3340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `_iswalpha_l` | `0x3360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `_iswcntrl_l` | `0x3380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 476 | `_iswdigit_l` | `0x33A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 477 | `_iswgraph_l` | `0x33C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 478 | `_iswlower_l` | `0x33E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 479 | `_iswprint_l` | `0x3400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 480 | `_iswpunct_l` | `0x3420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 481 | `_iswspace_l` | `0x3440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `_iswupper_l` | `0x3460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `_iswxdigit_l` | `0x3480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `isleadbyte` | `0x34A0` | 69 | UnwindData |  |
| 1149 | `iswalnum` | `0x34F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1150 | `iswalpha` | `0x3500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `iswascii` | `0x3510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1152 | `iswcntrl` | `0x3530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `iswdigit` | `0x3540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1155 | `iswgraph` | `0x3550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1156 | `iswlower` | `0x3560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1157 | `iswprint` | `0x3570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1158 | `iswpunct` | `0x3580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1159 | `iswspace` | `0x3590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1160 | `iswupper` | `0x35A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1161 | `iswxdigit` | `0x35B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `_iswctype_l` | `0x35C0` | 194 | UnwindData |  |
| 1137 | `is_wctype` | `0x3690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1153 | `iswctype` | `0x36A0` | 147 | UnwindData |  |
| 542 | `_mblen_l` | `0x3740` | 227 | UnwindData |  |
| 1174 | `mblen` | `0x3830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `_mbstowcs_l` | `0x3850` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `_mbstowcs_s_l` | `0x3A60` | 337 | UnwindData |  |
| 1180 | `mbstowcs` | `0x3BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `mbstowcs_s` | `0x3BE0` | 30 | UnwindData |  |
| 646 | `_mbstrlen` | `0x3C10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 647 | `_mbstrlen_l` | `0x3C40` | 174 | UnwindData |  |
| 648 | `_mbstrnlen` | `0x3D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 649 | `_mbstrnlen_l` | `0x3D10` | 287 | UnwindData |  |
| 654 | `_mbtowc_l` | `0x3E40` | 329 | UnwindData |  |
| 1182 | `mbtowc` | `0x3F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `_strtod_l` | `0x3FA0` | 409 | UnwindData |  |
| 1252 | `strtod` | `0x4140` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `_strtoi64` | `0x43C0` | 48 | UnwindData |  |
| 799 | `_strtoi64_l` | `0x4400` | 34 | UnwindData |  |
| 801 | `_strtoui64` | `0x4430` | 51 | UnwindData |  |
| 802 | `_strtoui64_l` | `0x4470` | 37 | UnwindData |  |
| 800 | `_strtol_l` | `0x4720` | 39 | UnwindData |  |
| 803 | `_strtoul_l` | `0x4750` | 42 | UnwindData |  |
| 1255 | `strtol` | `0x4780` | 52 | UnwindData |  |
| 1256 | `strtoul` | `0x4800` | 56 | UnwindData |  |
| 809 | `_swab` | `0x4840` | 103 | UnwindData |  |
| 826 | `_tolower` | `0x48B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `_tolower_l` | `0x48C0` | 331 | UnwindData |  |
| 1272 | `tolower` | `0x4A20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 828 | `_toupper` | `0x4A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 829 | `_toupper_l` | `0x4A60` | 329 | UnwindData |  |
| 1273 | `toupper` | `0x4BB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `_towlower_l` | `0x4BE0` | 225 | UnwindData |  |
| 1274 | `towlower` | `0x4CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `_towupper_l` | `0x4CE0` | 228 | UnwindData |  |
| 1275 | `towupper` | `0x4DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 940 | `_wcstod_l` | `0x4DE0` | 390 | UnwindData |  |
| 1316 | `wcstod` | `0x4F70` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 941 | `_wcstoi64` | `0x5210` | 53 | UnwindData |  |
| 942 | `_wcstoi64_l` | `0x5250` | 40 | UnwindData |  |
| 946 | `_wcstoui64` | `0x5280` | 57 | UnwindData |  |
| 947 | `_wcstoui64_l` | `0x52C0` | 43 | UnwindData |  |
| 943 | `_wcstol_l` | `0x5550` | 39 | UnwindData |  |
| 948 | `_wcstoul_l` | `0x5580` | 42 | UnwindData |  |
| 1319 | `wcstol` | `0x55B0` | 52 | UnwindData |  |
| 1322 | `wcstoul` | `0x5630` | 56 | UnwindData |  |
| 944 | `_wcstombs_l` | `0x5670` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 945 | `_wcstombs_s_l` | `0x5990` | 251 | UnwindData |  |
| 1320 | `wcstombs` | `0x5AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `wcstombs_s` | `0x5AB0` | 30 | UnwindData |  |
| 959 | `_wctomb_l` | `0x5AE0` | 123 | UnwindData |  |
| 960 | `_wctomb_s_l` | `0x5B70` | 416 | UnwindData |  |
| 1325 | `wctomb` | `0x5D20` | 58 | UnwindData |  |
| 1326 | `wctomb_s` | `0x5D60` | 20 | UnwindData |  |
| 1042 | `_wtof` | `0x5D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1043 | `_wtof_l` | `0x5D90` | 217 | UnwindData |  |
| 1044 | `_wtoi` | `0x5E70` | 31 | UnwindData |  |
| 1045 | `_wtoi64` | `0x5EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1046 | `_wtoi64_l` | `0x5EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1047 | `_wtoi_l` | `0x5EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1049 | `_wtol_l` | `0x5EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1048 | `_wtol` | `0x5F00` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1075 | `btowc` | `0x62B0` | 101 | UnwindData |  |
| 1175 | `mbrlen` | `0x6320` | 62 | UnwindData |  |
| 1176 | `mbrtowc` | `0x6370` | 96 | UnwindData |  |
| 1178 | `mbsrtowcs` | `0x63E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1179 | `mbsrtowcs_s` | `0x63F0` | 207 | UnwindData |  |
| 1292 | `wcrtomb` | `0x6770` | 58 | UnwindData |  |
| 1293 | `wcrtomb_s` | `0x67B0` | 152 | UnwindData |  |
| 1312 | `wcsrtombs` | `0x6850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `wcsrtombs_s` | `0x6860` | 209 | UnwindData |  |
| 1324 | `wctob` | `0x6940` | 109 | UnwindData |  |
| 197 | `_beep` | `0x6C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `_sleep` | `0x6C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `_findclose` | `0x6C70` | 37 | UnwindData |  |
| 296 | `_findfirst` | `0x6CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `_findnext` | `0x6CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `_findfirst64` | `0x6CC0` | 358 | UnwindData |  |
| 300 | `_findnext64` | `0x6E30` | 361 | UnwindData |  |
| 298 | `_findfirsti64` | `0x6FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `_findnexti64` | `0x6FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `_getdiskfree` | `0x6FC0` | 205 | UnwindData |  |
| 372 | `_getdrives` | `0x70A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 721 | `_seterrormode` | `0x70B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `_wfindfirst` | `0x70C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `_wfindnext` | `0x70D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `_wfindfirst64` | `0x70E0` | 358 | UnwindData |  |
| 976 | `_wfindnext64` | `0x7250` | 361 | UnwindData |  |
| 974 | `_wfindfirsti64` | `0x73C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `_wfindnexti64` | `0x73D0` | 1,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `__getmainargs` | `0x7B90` | 120 | UnwindData |  |
| 168 | `__wgetmainargs` | `0x7C10` | 167 | UnwindData |  |
| 70 | `_CrtDbgReport` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `_CrtDbgReportV` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `_CrtDbgReportW` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `_CrtDbgReportWV` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `_CrtDumpMemoryLeaks` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `_CrtIsMemoryBlock` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `_CrtMemDifference` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `_CrtReportBlockType` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `_CrtSetAllocHook` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `_CrtSetBreakAlloc` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `_CrtSetDbgFlag` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `_CrtSetDumpClient` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `_CrtSetReportFile` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `_CrtSetReportHook` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `_CrtSetReportHook2` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `_CrtSetReportMode` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `_crtAssertBusy` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `_crtBreakAlloc` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `_crtDbgFlag` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `_get_sbh_threshold` | `0x7DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `_get_environ` | `0x7DD0` | 101 | UnwindData |  |
| 361 | `_get_wenviron` | `0x7E40` | 101 | UnwindData |  |
| 136 | `__doserrno` | `0x7EB0` | 35 | UnwindData |  |
| 272 | `_errno` | `0x7F10` | 35 | UnwindData |  |
| 347 | `_get_doserrno` | `0x7F40` | 54 | UnwindData |  |
| 349 | `_get_errno` | `0x7F80` | 54 | UnwindData |  |
| 714 | `_set_doserrno` | `0x8010` | 36 | UnwindData |  |
| 715 | `_set_errno` | `0x8040` | 36 | UnwindData |  |
| 171 | `_access` | `0x8070` | 18 | UnwindData |  |
| 172 | `_access_s` | `0x8090` | 147 | UnwindData |  |
| 209 | `_chdir` | `0x8130` | 315 | UnwindData |  |
| 210 | `_chdrive` | `0x8280` | 141 | UnwindData |  |
| 371 | `_getdrive` | `0x8320` | 204 | UnwindData |  |
| 213 | `_chmod` | `0x8400` | 130 | UnwindData |  |
| 333 | `_fullpath` | `0x8490` | 299 | UnwindData |  |
| 334 | `_fullpath_dbg` | `0x85D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `_getcwd` | `0x85E0` | 66 | UnwindData |  |
| 369 | `_getdcwd` | `0x8630` | 79 | UnwindData |  |
| 375 | `_getpid` | `0x87F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 658 | `_mkdir` | `0x8800` | 45 | UnwindData |  |
| 695 | `_rmdir` | `0x8840` | 43 | UnwindData |  |
| 764 | `_stat` | `0x8960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `_stat64` | `0x8970` | 1,216 | UnwindData |  |
| 766 | `_stati64` | `0x8E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `_unlink` | `0x8E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `remove` | `0x8E60` | 43 | UnwindData |  |
| 906 | `_waccess` | `0x8EA0` | 18 | UnwindData |  |
| 907 | `_waccess_s` | `0x8EC0` | 147 | UnwindData |  |
| 911 | `_wchdir` | `0x8F60` | 330 | UnwindData |  |
| 912 | `_wchmod` | `0x90B0` | 130 | UnwindData |  |
| 983 | `_wfullpath` | `0x9140` | 327 | UnwindData |  |
| 984 | `_wfullpath_dbg` | `0x9290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `_wgetcwd` | `0x92A0` | 66 | UnwindData |  |
| 986 | `_wgetdcwd` | `0x92F0` | 79 | UnwindData |  |
| 995 | `_wmkdir` | `0x9480` | 45 | UnwindData |  |
| 1009 | `_wremove` | `0x94C0` | 43 | UnwindData |  |
| 1050 | `_wunlink` | `0x9500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `_wrename` | `0x9510` | 359 | UnwindData |  |
| 1012 | `_wrmdir` | `0x9680` | 43 | UnwindData |  |
| 1030 | `_wstat` | `0x97B0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1031 | `_wstat64` | `0x9B40` | 1,070 | UnwindData |  |
| 1032 | `_wstati64` | `0x9F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `rename` | `0x9F90` | 386 | UnwindData |  |
| 1 | `??0__non_rtti_object@@QEAA@AEBV0@@Z` | `0xABE0` | 33 | UnwindData |  |
| 2 | `??0__non_rtti_object@@QEAA@PEBD@Z` | `0xAC10` | 33 | UnwindData |  |
| 3 | `??0bad_cast@@AAE@PBQBD@Z` | `0xAC40` | 33 | UnwindData |  |
| 4 | `??0bad_cast@@AEAA@PEBQEBD@Z` | `0xAC40` | 33 | UnwindData |  |
| 5 | `??0bad_cast@@QAE@ABQBD@Z` | `0xAC40` | 33 | UnwindData |  |
| 6 | `??0bad_cast@@QEAA@AEBQEBD@Z` | `0xAC40` | 33 | UnwindData |  |
| 7 | `??0bad_cast@@QEAA@AEBV0@@Z` | `0xAC70` | 33 | UnwindData |  |
| 8 | `??0bad_cast@@QEAA@PEBD@Z` | `0xACA0` | 42 | UnwindData |  |
| 9 | `??0bad_typeid@@QEAA@AEBV0@@Z` | `0xACD0` | 33 | UnwindData |  |
| 10 | `??0bad_typeid@@QEAA@PEBD@Z` | `0xAD00` | 42 | UnwindData |  |
| 11 | `??0exception@@QEAA@AEBQEBD@Z` | `0xAD30` | 122 | UnwindData |  |
| 12 | `??0exception@@QEAA@AEBQEBDH@Z` | `0xADB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0exception@@QEAA@AEBV0@@Z` | `0xADD0` | 136 | UnwindData |  |
| 14 | `??0exception@@QEAA@XZ` | `0xAE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??1__non_rtti_object@@UEAA@XZ` | `0xAE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??1bad_typeid@@UEAA@XZ` | `0xAE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??1bad_cast@@UEAA@XZ` | `0xAEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??1exception@@UEAA@XZ` | `0xAEC0` | 34 | UnwindData |  |
| 23 | `??4__non_rtti_object@@QEAAAEAV0@AEBV0@@Z` | `0xAEF0` | 23 | UnwindData |  |
| 24 | `??4bad_cast@@QEAAAEAV0@AEBV0@@Z` | `0xAEF0` | 23 | UnwindData |  |
| 25 | `??4bad_typeid@@QEAAAEAV0@AEBV0@@Z` | `0xAEF0` | 23 | UnwindData |  |
| 26 | `??4exception@@QEAAAEAV0@AEBV0@@Z` | `0xAF10` | 131 | UnwindData |  |
| 33 | `??_Fbad_cast@@QEAAXXZ` | `0xB140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??_Fbad_typeid@@QEAAXXZ` | `0xB160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `?what@exception@@UEBAPEBDXZ` | `0xB180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `__DestructExceptionObject` | `0xB1A0` | 112 | UnwindData |  |
| 50 | `__uncaught_exception` | `0xB230` | 24 | UnwindData |  |
| 52 | `?_is_exception_typeof@@YAHAEBVtype_info@@PEAU_EXCEPTION_POINTERS@@@Z` | `0xB250` | 208 | UnwindData |  |
| 104 | `__AdjustPointer` | `0xB360` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `?_inconsistency@@YAXXZ` | `0xB3F0` | 34 | UnwindData |  |
| 65 | `?terminate@@YAXXZ` | `0xB420` | 34 | UnwindData |  |
| 66 | `?unexpected@@YAXXZ` | `0xB450` | 32 | UnwindData |  |
| 57 | `?_set_se_translator@@YAP6AXIPEAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z` | `0xB4A0` | 56 | UnwindData |  |
| 63 | `?set_terminate@@YAP6AXXZP6AXXZ@Z` | `0xB4E0` | 56 | UnwindData |  |
| 64 | `?set_unexpected@@YAP6AXXZP6AXXZ@Z` | `0xB520` | 56 | UnwindData |  |
| 359 | `_get_terminate` | `0xB560` | 21 | UnwindData |  |
| 360 | `_get_unexpected` | `0xB580` | 21 | UnwindData |  |
| 60 | `?name@type_info@@QEBAPEBDXZ` | `0xB5A0` | 207 | UnwindData |  |
| 93 | `_CxxThrowException` | `0xB680` | 190 | UnwindData |  |
| 105 | `__BuildCatchObject` | `0xC210` | 192 | UnwindData |  |
| 106 | `__BuildCatchObjectHelper` | `0xC2E0` | 523 | UnwindData |  |
| 118 | `__TypeMatch` | `0xCBB0` | 302 | UnwindData |  |
| 109 | `__CxxFrameHandler` | `0xDB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `__CxxFrameHandler2` | `0xDB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `__CxxFrameHandler3` | `0xDB10` | 163 | UnwindData |  |
| 112 | `__CxxFrameHandler4` | `0xDBC0` | 210 | UnwindData |  |
| 114 | `__RTCastToVoid` | `0xE130` | 103 | UnwindData |  |
| 115 | `__RTDynamicCast` | `0xE1A0` | 387 | UnwindData |  |
| 116 | `__RTtypeid` | `0xE330` | 180 | UnwindData |  |
| 68 | `_CrtCheckMemory` | `0x15280` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `_CrtIsValidHeapPointer` | `0x15280` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `__unDName` | `0x152D0` | 263 | UnwindData |  |
| 162 | `__unDNameEx` | `0x153E0` | 269 | UnwindData |  |
| 78 | `_CrtIsValidPointer` | `0x155D0` | 8,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??1type_info@@UEAA@XZ` | `0x176E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??8type_info@@QEBAHAEBV0@@Z` | `0x17700` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??9type_info@@QEBAHAEBV0@@Z` | `0x17730` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `?_Doraise@bad_cast@@MEBAXXZ` | `0x177E0` | 35 | UnwindData |  |
| 39 | `?_Doraise@bad_typeid@@MEBAXXZ` | `0x17810` | 35 | UnwindData |  |
| 58 | `?before@type_info@@QEBAHAEBV1@@Z` | `0x17840` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `?name@type_info@@QEBAPEBDPEAU__type_info_node@@@Z` | `0x17870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?raw_name@type_info@@QEBAPEBDXZ` | `0x17880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `__ExceptionPtrCreate` | `0x17890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `__ExceptionPtrDestroy` | `0x178A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `__ExceptionPtrCopy` | `0x178B0` | 50 | UnwindData |  |
| 40 | `__ExceptionPtrAssign` | `0x178F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `__ExceptionPtrCompare` | `0x17900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `__ExceptionPtrToBool` | `0x17910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `__ExceptionPtrSwap` | `0x17920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `__ExceptionPtrCurrentException` | `0x17950` | 115 | UnwindData |  |
| 47 | `__ExceptionPtrRethrow` | `0x179D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__ExceptionPtrCopyException` | `0x179E0` | 115 | UnwindData |  |
| 69 | `_CrtDbgBreak` | `0x17E70` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `_CrtDoForAllClientObjects` | `0x17E70` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `_CrtMemCheckpoint` | `0x17E70` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `_CrtMemDumpAllObjectsSince` | `0x17E70` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `_CrtMemDumpStatistics` | `0x17E70` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `_CrtSetDbgBlockType` | `0x17E70` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `_cwait` | `0x18AA0` | 187 | UnwindData |  |
| 273 | `_execl` | `0x18B70` | 245 | UnwindData |  |
| 274 | `_execle` | `0x18C70` | 260 | UnwindData |  |
| 275 | `_execlp` | `0x18D80` | 244 | UnwindData |  |
| 276 | `_execlpe` | `0x18E80` | 260 | UnwindData |  |
| 277 | `_execv` | `0x18F90` | 85 | UnwindData |  |
| 278 | `_execve` | `0x18FF0` | 633 | UnwindData |  |
| 279 | `_execvp` | `0x19320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `_execvpe` | `0x19330` | 718 | UnwindData |  |
| 350 | `_get_fileinfo` | `0x19610` | 63 | UnwindData |  |
| 717 | `_set_fileinfo` | `0x19660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `_spawnl` | `0x19670` | 246 | UnwindData |  |
| 750 | `_spawnle` | `0x19770` | 261 | UnwindData |  |
| 751 | `_spawnlp` | `0x19880` | 243 | UnwindData |  |
| 752 | `_spawnlpe` | `0x19980` | 261 | UnwindData |  |
| 753 | `_spawnv` | `0x19A90` | 85 | UnwindData |  |
| 754 | `_spawnve` | `0x19AF0` | 653 | UnwindData |  |
| 755 | `_spawnvp` | `0x19E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `_spawnvpe` | `0x19E50` | 763 | UnwindData |  |
| 963 | `_wexecl` | `0x1A160` | 246 | UnwindData |  |
| 964 | `_wexecle` | `0x1A260` | 261 | UnwindData |  |
| 965 | `_wexeclp` | `0x1A370` | 245 | UnwindData |  |
| 966 | `_wexeclpe` | `0x1A470` | 261 | UnwindData |  |
| 967 | `_wexecv` | `0x1A580` | 90 | UnwindData |  |
| 968 | `_wexecve` | `0x1A5E0` | 642 | UnwindData |  |
| 969 | `_wexecvp` | `0x1A910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 970 | `_wexecvpe` | `0x1A920` | 626 | UnwindData |  |
| 1020 | `_wspawnl` | `0x1ABA0` | 247 | UnwindData |  |
| 1021 | `_wspawnle` | `0x1ACA0` | 262 | UnwindData |  |
| 1022 | `_wspawnlp` | `0x1ADB0` | 244 | UnwindData |  |
| 1023 | `_wspawnlpe` | `0x1AEB0` | 262 | UnwindData |  |
| 1024 | `_wspawnv` | `0x1AFC0` | 90 | UnwindData |  |
| 1025 | `_wspawnve` | `0x1B020` | 662 | UnwindData |  |
| 1026 | `_wspawnvp` | `0x1B370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `_wspawnvpe` | `0x1B380` | 658 | UnwindData |  |
| 1037 | `_wsystem` | `0x1B620` | 297 | UnwindData |  |
| 1262 | `system` | `0x1B750` | 297 | UnwindData |  |
| 20 | `??2@YAPEAX_K@Z` | `0x1CAD0` | 57 | UnwindData |  |
| 22 | `??3@YAXPEAX@Z` | `0x1CB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `_free_dbg` | `0x1CB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??2@YAPEAX_KHPEBDH@Z` | `0x1CB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??_U@YAPEAX_K@Z` | `0x1CB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??_U@YAPEAX_KHPEBDH@Z` | `0x1CB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??_V@YAXPEAX@Z` | `0x1CB30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `?_query_new_handler@@YAP6AH_K@ZXZ` | `0x1CB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `?_set_new_handler@@YAP6AH_K@ZP6AH0@Z@Z` | `0x1CB60` | 77 | UnwindData |  |
| 202 | `_callnewh` | `0x1CBC0` | 58 | UnwindData |  |
| 54 | `?_query_new_mode@@YAHXZ` | `0x1CC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `?_set_new_mode@@YAHH@Z` | `0x1CC20` | 63 | UnwindData |  |
| 62 | `?set_new_handler@@YAP6AXXZP6AXXZ@Z` | `0x1CC70` | 18 | UnwindData |  |
| 175 | `_aligned_free` | `0x1CC90` | 27 | UnwindData |  |
| 177 | `_aligned_malloc` | `0x1CCC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `_aligned_malloc_dbg` | `0x1CCC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `_aligned_offset_malloc` | `0x1CCD0` | 195 | UnwindData |  |
| 181 | `_aligned_offset_realloc` | `0x1CDA0` | 480 | UnwindData |  |
| 183 | `_aligned_realloc` | `0x1CF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `_aligned_realloc_dbg` | `0x1CF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `_expand` | `0x1CFA0` | 261 | UnwindData |  |
| 352 | `_get_heap_handle` | `0x1D0B0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 720 | `_set_sbh_threshold` | `0x1D160` | 32 | UnwindData |  |
| 385 | `_heapchk` | `0x1D190` | 81 | UnwindData |  |
| 387 | `_heapset` | `0x1D1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `_heapmin` | `0x1D200` | 69 | UnwindData |  |
| 388 | `_heapwalk` | `0x1D250` | 390 | UnwindData |  |
| 666 | `_msize` | `0x1D3E0` | 73 | UnwindData |  |
| 694 | `_resetstkoflw` | `0x1D430` | 352 | UnwindData |  |
| 1076 | `calloc` | `0x1D5A0` | 65 | UnwindData |  |
| 1115 | `free` | `0x1D5F0` | 61 | UnwindData |  |
| 1173 | `malloc` | `0x1D640` | 206 | UnwindData |  |
| 1208 | `realloc` | `0x1D720` | 211 | UnwindData |  |
| 205 | `_cgets` | `0x1DE80` | 125 | UnwindData |  |
| 206 | `_cgets_s` | `0x1DF10` | 295 | UnwindData |  |
| 207 | `_cgetws` | `0x1E040` | 111 | UnwindData |  |
| 208 | `_cgetws_s` | `0x1E0C0` | 493 | UnwindData |  |
| 214 | `_chsize` | `0x1E2C0` | 21 | UnwindData |  |
| 215 | `_chsize_s` | `0x1E480` | 260 | UnwindData |  |
| 219 | `_close` | `0x1E590` | 257 | UnwindData |  |
| 220 | `_commit` | `0x1E760` | 252 | UnwindData |  |
| 233 | `_cputs` | `0x1E870` | 143 | UnwindData |  |
| 234 | `_cputws` | `0x1E910` | 170 | UnwindData |  |
| 689 | `_putwch` | `0x1E9C0` | 50 | UnwindData |  |
| 235 | `_creat` | `0x1EA60` | 61 | UnwindData |  |
| 264 | `_dup` | `0x1EAB0` | 239 | UnwindData |  |
| 265 | `_dup2` | `0x1ED60` | 369 | UnwindData |  |
| 271 | `_eof` | `0x1F050` | 299 | UnwindData |  |
| 292 | `_filelength` | `0x1F190` | 291 | UnwindData |  |
| 293 | `_filelengthi64` | `0x1F2C0` | 302 | UnwindData |  |
| 318 | `_freea` | `0x1F400` | 31 | UnwindData |  |
| 319 | `_freea_s` | `0x1F400` | 31 | UnwindData |  |
| 366 | `_getch` | `0x1F430` | 42 | UnwindData |  |
| 367 | `_getche` | `0x1F580` | 42 | UnwindData |  |
| 492 | `_kbhit` | `0x1F6C0` | 42 | UnwindData |  |
| 845 | `_ungetch` | `0x1F8B0` | 46 | UnwindData |  |
| 325 | `_fstat` | `0x1F910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `_fstati64` | `0x1F920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `_fstat64` | `0x1F930` | 1,009 | UnwindData |  |
| 351 | `_get_fmode` | `0x1FD30` | 63 | UnwindData |  |
| 718 | `_set_fmode` | `0x1FD80` | 77 | UnwindData |  |
| 726 | `_setmode` | `0x1FDE0` | 289 | UnwindData |  |
| 353 | `_get_osfhandle` | `0x20360` | 213 | UnwindData |  |
| 672 | `_open_osfhandle` | `0x20440` | 269 | UnwindData |  |
| 378 | `_getwch` | `0x20640` | 44 | UnwindData |  |
| 379 | `_getwche` | `0x207C0` | 44 | UnwindData |  |
| 846 | `_ungetwch` | `0x20850` | 50 | UnwindData |  |
| 401 | `_isatty` | `0x208C0` | 111 | UnwindData |  |
| 501 | `_locking` | `0x20940` | 261 | UnwindData |  |
| 508 | `_lseek` | `0x20B30` | 261 | UnwindData |  |
| 509 | `_lseeki64` | `0x20CE0` | 265 | UnwindData |  |
| 662 | `_mktemp` | `0x20E90` | 99 | UnwindData |  |
| 663 | `_mktemp_s` | `0x20F00` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `_open` | `0x21080` | 216 | UnwindData |  |
| 747 | `_sopen` | `0x21160` | 68 | UnwindData |  |
| 748 | `_sopen_s` | `0x21290` | 50 | UnwindData |  |
| 678 | `_pipe` | `0x21AF0` | 787 | UnwindData |  |
| 685 | `_putch` | `0x21E10` | 46 | UnwindData |  |
| 692 | `_read` | `0x21F00` | 289 | UnwindData |  |
| 819 | `_tell` | `0x22A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 820 | `_telli64` | `0x22A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | `_wcreat` | `0x22A90` | 61 | UnwindData |  |
| 996 | `_wmktemp` | `0x22AE0` | 99 | UnwindData |  |
| 997 | `_wmktemp_s` | `0x22B50` | 2,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `_wopen` | `0x234F0` | 186 | UnwindData |  |
| 1018 | `_wsopen` | `0x235B0` | 50 | UnwindData |  |
| 1019 | `_wsopen_s` | `0x236D0` | 50 | UnwindData |  |
| 1011 | `_write` | `0x23710` | 261 | UnwindData |  |
| 374 | `_getmbcp` | `0x24840` | 58 | UnwindData |  |
| 725 | `_setmbcp` | `0x24880` | 576 | UnwindData |  |
| 409 | `_ismbbalnum` | `0x24DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `_ismbbalnum_l` | `0x24E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `_ismbbalpha` | `0x24E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `_ismbbalpha_l` | `0x24E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `_ismbbgraph` | `0x24E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `_ismbbgraph_l` | `0x24E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `_ismbbkalnum` | `0x24EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `_ismbbkalnum_l` | `0x24ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `_ismbbkana` | `0x24EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `_ismbbkana_l` | `0x24F00` | 101 | UnwindData |  |
| 419 | `_ismbbkprint` | `0x24F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `_ismbbkprint_l` | `0x24F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `_ismbbkpunct` | `0x24FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `_ismbbkpunct_l` | `0x24FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `_ismbblead` | `0x24FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `_ismbblead_l` | `0x25010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `_ismbbprint` | `0x25030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `_ismbbprint_l` | `0x25050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `_ismbbpunct` | `0x25070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `_ismbbpunct_l` | `0x25090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `_ismbbtrail` | `0x250B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `_ismbbtrail_l` | `0x250D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `_ismbcalnum` | `0x250F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `_ismbcalnum_l` | `0x25100` | 209 | UnwindData |  |
| 433 | `_ismbcalpha` | `0x251E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `_ismbcalpha_l` | `0x251F0` | 211 | UnwindData |  |
| 435 | `_ismbcdigit` | `0x252D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `_ismbcdigit_l` | `0x252E0` | 213 | UnwindData |  |
| 437 | `_ismbcgraph` | `0x253C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `_ismbcgraph_l` | `0x253D0` | 216 | UnwindData |  |
| 439 | `_ismbchira` | `0x254B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `_ismbchira_l` | `0x254C0` | 77 | UnwindData |  |
| 441 | `_ismbckata` | `0x25520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `_ismbckata_l` | `0x25530` | 85 | UnwindData |  |
| 459 | `_ismbcsymbol` | `0x25590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 460 | `_ismbcsymbol_l` | `0x255A0` | 85 | UnwindData |  |
| 443 | `_ismbcl0` | `0x25600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `_ismbcl0_l` | `0x25610` | 99 | UnwindData |  |
| 445 | `_ismbcl1` | `0x25680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `_ismbcl1_l` | `0x25690` | 104 | UnwindData |  |
| 447 | `_ismbcl2` | `0x25700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `_ismbcl2_l` | `0x25710` | 104 | UnwindData |  |
| 449 | `_ismbclegal` | `0x25780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `_ismbclegal_l` | `0x25790` | 82 | UnwindData |  |
| 451 | `_ismbclower` | `0x257F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `_ismbclower_l` | `0x25800` | 190 | UnwindData |  |
| 453 | `_ismbcprint` | `0x258D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `_ismbcprint_l` | `0x258E0` | 211 | UnwindData |  |
| 455 | `_ismbcpunct` | `0x259C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `_ismbcpunct_l` | `0x259D0` | 206 | UnwindData |  |
| 457 | `_ismbcspace` | `0x25AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `_ismbcspace_l` | `0x25AC0` | 211 | UnwindData |  |
| 461 | `_ismbcupper` | `0x25BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `_ismbcupper_l` | `0x25BB0` | 189 | UnwindData |  |
| 463 | `_ismbslead` | `0x25C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `_ismbslead_l` | `0x25C90` | 164 | UnwindData |  |
| 465 | `_ismbstrail` | `0x25D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `_ismbstrail_l` | `0x25D50` | 161 | UnwindData |  |
| 517 | `_mbbtombc` | `0x25E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `_mbbtombc_l` | `0x25E10` | 161 | UnwindData |  |
| 537 | `_mbctombb` | `0x25EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `_mbctombb_l` | `0x25ED0` | 193 | UnwindData |  |
| 519 | `_mbbtype` | `0x25FA0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `_mbccpy` | `0x26050` | 30 | UnwindData |  |
| 522 | `_mbccpy_l` | `0x26080` | 29 | UnwindData |  |
| 523 | `_mbccpy_s` | `0x260B0` | 230 | UnwindData |  |
| 524 | `_mbccpy_s_l` | `0x261A0` | 296 | UnwindData |  |
| 525 | `_mbcjistojms` | `0x262D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | `_mbcjistojms_l` | `0x262E0` | 165 | UnwindData |  |
| 527 | `_mbcjmstojis` | `0x26390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `_mbcjmstojis_l` | `0x263A0` | 187 | UnwindData |  |
| 529 | `_mbclen` | `0x26470` | 43 | UnwindData |  |
| 530 | `_mbclen_l` | `0x264B0` | 43 | UnwindData |  |
| 531 | `_mbctohira` | `0x264F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | `_mbctohira_l` | `0x26500` | 55 | UnwindData |  |
| 533 | `_mbctokata` | `0x26540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `_mbctokata_l` | `0x26550` | 41 | UnwindData |  |
| 535 | `_mbctolower` | `0x26580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `_mbctolower_l` | `0x26590` | 188 | UnwindData |  |
| 539 | `_mbctoupper` | `0x26660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `_mbctoupper_l` | `0x26670` | 188 | UnwindData |  |
| 543 | `_mbsbtype` | `0x26740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `_mbsbtype_l` | `0x26750` | 214 | UnwindData |  |
| 546 | `_mbscat_s` | `0x26830` | 376 | UnwindData |  |
| 547 | `_mbscat_s_l` | `0x269B0` | 485 | UnwindData |  |
| 548 | `_mbschr` | `0x26BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `_mbschr_l` | `0x26BB0` | 207 | UnwindData |  |
| 550 | `_mbscmp` | `0x26C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 551 | `_mbscmp_l` | `0x26CA0` | 254 | UnwindData |  |
| 552 | `_mbscoll` | `0x26DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `_mbscoll_l` | `0x26DC0` | 213 | UnwindData |  |
| 555 | `_mbscpy_s` | `0x26EA0` | 270 | UnwindData |  |
| 556 | `_mbscpy_s_l` | `0x26FC0` | 377 | UnwindData |  |
| 557 | `_mbscspn` | `0x27140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `_mbscspn_l` | `0x27150` | 254 | UnwindData |  |
| 559 | `_mbsdec` | `0x27260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `_mbsdec_l` | `0x27270` | 164 | UnwindData |  |
| 562 | `_mbsicmp` | `0x27320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `_mbsicmp_l` | `0x27330` | 497 | UnwindData |  |
| 564 | `_mbsicoll` | `0x27530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 565 | `_mbsicoll_l` | `0x27540` | 213 | UnwindData |  |
| 566 | `_mbsinc` | `0x27620` | 81 | UnwindData |  |
| 567 | `_mbsinc_l` | `0x27680` | 39 | UnwindData |  |
| 568 | `_mbslen` | `0x276B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `_mbslen_l` | `0x276C0` | 110 | UnwindData |  |
| 570 | `_mbslwr` | `0x27740` | 43 | UnwindData |  |
| 571 | `_mbslwr_l` | `0x27780` | 43 | UnwindData |  |
| 572 | `_mbslwr_s` | `0x277C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 573 | `_mbslwr_s_l` | `0x277D0` | 348 | UnwindData |  |
| 574 | `_mbsnbcat` | `0x27940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 575 | `_mbsnbcat_l` | `0x27950` | 342 | UnwindData |  |
| 576 | `_mbsnbcat_s` | `0x27AB0` | 604 | UnwindData |  |
| 577 | `_mbsnbcat_s_l` | `0x27D20` | 726 | UnwindData |  |
| 578 | `_mbsnbcmp` | `0x28000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `_mbsnbcmp_l` | `0x28010` | 316 | UnwindData |  |
| 580 | `_mbsnbcnt` | `0x28160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 581 | `_mbsnbcnt_l` | `0x28170` | 166 | UnwindData |  |
| 582 | `_mbsnbcoll` | `0x28220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `_mbsnbcoll_l` | `0x28230` | 300 | UnwindData |  |
| 584 | `_mbsnbcpy` | `0x28370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 585 | `_mbsnbcpy_l` | `0x28380` | 264 | UnwindData |  |
| 586 | `_mbsnbcpy_s` | `0x28490` | 485 | UnwindData |  |
| 587 | `_mbsnbcpy_s_l` | `0x28680` | 603 | UnwindData |  |
| 588 | `_mbsnbicmp` | `0x288F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 589 | `_mbsnbicmp_l` | `0x28900` | 435 | UnwindData |  |
| 590 | `_mbsnbicoll` | `0x28AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 591 | `_mbsnbicoll_l` | `0x28AD0` | 283 | UnwindData |  |
| 592 | `_mbsnbset` | `0x28C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `_mbsnbset_l` | `0x28C10` | 260 | UnwindData |  |
| 594 | `_mbsnbset_s` | `0x28D20` | 570 | UnwindData |  |
| 595 | `_mbsnbset_s_l` | `0x28F60` | 702 | UnwindData |  |
| 596 | `_mbsncat` | `0x29230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `_mbsncat_l` | `0x29240` | 320 | UnwindData |  |
| 598 | `_mbsncat_s` | `0x29390` | 567 | UnwindData |  |
| 599 | `_mbsncat_s_l` | `0x295D0` | 693 | UnwindData |  |
| 600 | `_mbsnccnt` | `0x29890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `_mbsnccnt_l` | `0x298A0` | 167 | UnwindData |  |
| 602 | `_mbsncmp` | `0x29950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `_mbsncmp_l` | `0x29960` | 273 | UnwindData |  |
| 604 | `_mbsncoll` | `0x29A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `_mbsncoll_l` | `0x29A90` | 341 | UnwindData |  |
| 606 | `_mbsncpy` | `0x29BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `_mbsncpy_l` | `0x29C00` | 244 | UnwindData |  |
| 608 | `_mbsncpy_s` | `0x29D00` | 461 | UnwindData |  |
| 609 | `_mbsncpy_s_l` | `0x29EE0` | 547 | UnwindData |  |
| 610 | `_mbsnextc` | `0x2A110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `_mbsnextc_l` | `0x2A120` | 131 | UnwindData |  |
| 612 | `_mbsnicmp` | `0x2A1B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 613 | `_mbsnicmp_l` | `0x2A1C0` | 398 | UnwindData |  |
| 614 | `_mbsnicoll` | `0x2A360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 615 | `_mbsnicoll_l` | `0x2A370` | 341 | UnwindData |  |
| 616 | `_mbsninc` | `0x2A4D0` | 35 | UnwindData |  |
| 617 | `_mbsninc_l` | `0x2A500` | 34 | UnwindData |  |
| 618 | `_mbsnlen` | `0x2A530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `_mbsnlen_l` | `0x2A540` | 152 | UnwindData |  |
| 620 | `_mbsnset` | `0x2A5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 621 | `_mbsnset_l` | `0x2A5F0` | 361 | UnwindData |  |
| 622 | `_mbsnset_s` | `0x2A760` | 507 | UnwindData |  |
| 623 | `_mbsnset_s_l` | `0x2A970` | 660 | UnwindData |  |
| 624 | `_mbspbrk` | `0x2AC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `_mbspbrk_l` | `0x2AC20` | 245 | UnwindData |  |
| 626 | `_mbsrchr` | `0x2AD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 627 | `_mbsrchr_l` | `0x2AD30` | 200 | UnwindData |  |
| 628 | `_mbsrev` | `0x2AE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 629 | `_mbsrev_l` | `0x2AE10` | 224 | UnwindData |  |
| 630 | `_mbsset` | `0x2AF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | `_mbsset_l` | `0x2AF10` | 227 | UnwindData |  |
| 632 | `_mbsset_s` | `0x2B000` | 295 | UnwindData |  |
| 633 | `_mbsset_s_l` | `0x2B130` | 408 | UnwindData |  |
| 634 | `_mbsspn` | `0x2B2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 635 | `_mbsspn_l` | `0x2B2E0` | 254 | UnwindData |  |
| 636 | `_mbsspnp` | `0x2B3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 637 | `_mbsspnp_l` | `0x2B400` | 260 | UnwindData |  |
| 638 | `_mbsstr` | `0x2B510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `_mbsstr_l` | `0x2B520` | 271 | UnwindData |  |
| 640 | `_mbstok` | `0x2B640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 641 | `_mbstok_l` | `0x2B650` | 62 | UnwindData |  |
| 642 | `_mbstok_s` | `0x2B6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 643 | `_mbstok_s_l` | `0x2B6B0` | 493 | UnwindData |  |
| 650 | `_mbsupr` | `0x2B8B0` | 43 | UnwindData |  |
| 651 | `_mbsupr_l` | `0x2B8F0` | 43 | UnwindData |  |
| 652 | `_mbsupr_s` | `0x2B930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `_mbsupr_s_l` | `0x2B940` | 348 | UnwindData |  |
| 176 | `_aligned_free_dbg` | `0x2BAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `_aligned_offset_malloc_dbg` | `0x2BAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `_aligned_offset_realloc_dbg` | `0x2BAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `_calloc_dbg` | `0x2BAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `_expand_dbg` | `0x2BAF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `_malloc_dbg` | `0x2BB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 667 | `_msize_dbg` | `0x2BB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 693 | `_realloc_dbg` | `0x2BB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `_XcptFilter` | `0x2BB30` | 439 | UnwindData |  |
| 108 | `__CppXcptFilter` | `0x2BCF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `__C_specific_handler` | `0x2BD10` | 500 | UnwindData |  |
| 119 | `___lc_codepage_func` | `0x2BF10` | 59 | UnwindData |  |
| 120 | `___lc_collate_cp_func` | `0x2BF60` | 59 | UnwindData |  |
| 121 | `___lc_handle_func` | `0x2BFB0` | 60 | UnwindData |  |
| 122 | `___mb_cur_max_func` | `0x2C000` | 62 | UnwindData |  |
| 123 | `___setlc_active_func` | `0x2C5F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `___unguarded_readlc_active_add_func` | `0x2C600` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `_create_locale` | `0x2CC20` | 270 | UnwindData |  |
| 317 | `_free_locale` | `0x2CFA0` | 173 | UnwindData |  |
| 346 | `_get_current_locale` | `0x2D060` | 156 | UnwindData |  |
| 1216 | `setlocale` | `0x2D960` | 501 | UnwindData |  |
| 128 | `__crtCompareStringA` | `0x2DEF0` | 135 | UnwindData |  |
| 129 | `__crtCompareStringW` | `0x2DF80` | 214 | UnwindData |  |
| 130 | `__crtGetLocaleInfoW` | `0x2E060` | 89 | UnwindData |  |
| 131 | `__crtGetStringTypeW` | `0x2E0C0` | 99 | UnwindData |  |
| 132 | `__crtLCMapStringA` | `0x2E540` | 148 | UnwindData |  |
| 133 | `__crtLCMapStringW` | `0x2E5E0` | 134 | UnwindData |  |
| 135 | `__dllonexit` | `0x2E6C0` | 209 | UnwindData |  |
| 670 | `_onexit` | `0x2E7A0` | 280 | UnwindData |  |
| 1069 | `atexit` | `0x2E8C0` | 23 | UnwindData |  |
| 138 | `__fpecode` | `0x2E8E0` | 20 | UnwindData |  |
| 153 | `__pxcptinfoptrs` | `0x2E910` | 20 | UnwindData |  |
| 1205 | `raise` | `0x2E9F0` | 589 | UnwindData |  |
| 1218 | `signal` | `0x2EC50` | 615 | UnwindData |  |
| 148 | `__lconv_init` | `0x2EEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `__pctype_func` | `0x2EEE0` | 63 | UnwindData |  |
| 152 | `__pwctype_func` | `0x2EF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `__set_app_type` | `0x2EF40` | 20 | UnwindData |  |
| 716 | `_set_error_mode` | `0x2EF60` | 87 | UnwindData |  |
| 165 | `__wcserror` | `0x2EFC0` | 393 | UnwindData |  |
| 166 | `__wcserror_s` | `0x2F150` | 256 | UnwindData |  |
| 170 | `_abs64` | `0x2F260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `abs` | `0x2F280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1163 | `labs` | `0x2F280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `_assert` | `0x2F290` | 1,891 | UnwindData |  |
| 397 | `_invalid_parameter` | `0x2FA00` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `_lfind` | `0x2FAF0` | 175 | UnwindData |  |
| 494 | `_lfind_s` | `0x2FBB0` | 180 | UnwindData |  |
| 495 | `_local_unwind` | `0x2FC70` | 41 | UnwindData |  |
| 504 | `_lrotl` | `0x2FCA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 697 | `_rotl` | `0x2FCA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 698 | `_rotl64` | `0x2FCB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `_lrotr` | `0x2FCD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 699 | `_rotr` | `0x2FCD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 700 | `_rotr64` | `0x2FCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 506 | `_lsearch` | `0x2FD00` | 204 | UnwindData |  |
| 507 | `_lsearch_s` | `0x2FDE0` | 202 | UnwindData |  |
| 514 | `_makepath` | `0x2FEB0` | 39 | UnwindData |  |
| 515 | `_makepath_s` | `0x2FEE0` | 354 | UnwindData |  |
| 684 | `_purecall` | `0x30050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 686 | `_putenv` | `0x30070` | 50 | UnwindData |  |
| 687 | `_putenv_s` | `0x30340` | 123 | UnwindData |  |
| 711 | `_searchenv` | `0x303D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `_searchenv_s` | `0x303F0` | 833 | UnwindData |  |
| 757 | `_splitpath` | `0x30750` | 136 | UnwindData |  |
| 758 | `_splitpath_s` | `0x30A90` | 698 | UnwindData |  |
| 774 | `_strerror` | `0x30D50` | 351 | UnwindData |  |
| 775 | `_strerror_s` | `0x30EC0` | 247 | UnwindData |  |
| 842 | `_umask` | `0x30FC0` | 34 | UnwindData |  |
| 843 | `_umask_s` | `0x30FF0` | 83 | UnwindData |  |
| 910 | `_wassert` | `0x31050` | 2,102 | UnwindData |  |
| 918 | `_wcserror` | `0x31890` | 172 | UnwindData |  |
| 919 | `_wcserror_s` | `0x31950` | 163 | UnwindData |  |
| 987 | `_wgetenv` | `0x31B10` | 90 | UnwindData |  |
| 988 | `_wgetenv_s` | `0x31C40` | 255 | UnwindData |  |
| 993 | `_wmakepath` | `0x31D50` | 39 | UnwindData |  |
| 994 | `_wmakepath_s` | `0x31D80` | 366 | UnwindData |  |
| 1000 | `_wperror` | `0x31F00` | 387 | UnwindData |  |
| 1007 | `_wputenv` | `0x32090` | 50 | UnwindData |  |
| 1008 | `_wputenv_s` | `0x32380` | 123 | UnwindData |  |
| 1015 | `_wsearchenv` | `0x32410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `_wsearchenv_s` | `0x32430` | 857 | UnwindData |  |
| 1017 | `_wsetlocale` | `0x32790` | 636 | UnwindData |  |
| 1028 | `_wsplitpath` | `0x32A20` | 136 | UnwindData |  |
| 1029 | `_wsplitpath_s` | `0x32D70` | 710 | UnwindData |  |
| 1057 | `abort` | `0x33040` | 142 | UnwindData |  |
| 1073 | `bsearch` | `0x330E0` | 262 | UnwindData |  |
| 1074 | `bsearch_s` | `0x331F0` | 278 | UnwindData |  |
| 1088 | `div` | `0x33310` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1165 | `ldiv` | `0x33310` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1131 | `getenv` | `0x334E0` | 90 | UnwindData |  |
| 1132 | `getenv_s` | `0x33540` | 244 | UnwindData |  |
| 1166 | `localeconv` | `0x33640` | 60 | UnwindData |  |
| 1172 | `longjmp` | `0x33690` | 40 | UnwindData |  |
| 1193 | `perror` | `0x336C0` | 200 | UnwindData |  |
| 1203 | `qsort` | `0x33790` | 152 | UnwindData |  |
| 1204 | `qsort_s` | `0x33B40` | 167 | UnwindData |  |
| 1206 | `rand` | `0x33F30` | 41 | UnwindData |  |
| 1227 | `srand` | `0x33F60` | 22 | UnwindData |  |
| 1207 | `rand_s` | `0x33F90` | 302 | UnwindData |  |
| 1238 | `strerror` | `0x340D0` | 160 | UnwindData |  |
| 1239 | `strerror_s` | `0x34180` | 127 | UnwindData |  |
| 733 | `_snprintf_s` | `0x383F0` | 29 | UnwindData |  |
| 886 | `_vsnprintf_s` | `0x38420` | 175 | UnwindData |  |
| 737 | `_snscanf_s` | `0x384E0` | 71 | UnwindData |  |
| 741 | `_snwprintf_s` | `0x38530` | 29 | UnwindData |  |
| 890 | `_vsnwprintf_s` | `0x38560` | 186 | UnwindData |  |
| 745 | `_snwscanf_s` | `0x38620` | 71 | UnwindData |  |
| 991 | `_winput_s` | `0x38C60` | 3,955 | UnwindData |  |
| 999 | `_woutput_s` | `0x39D20` | 2,816 | UnwindData |  |
| 1213 | `scanf_s` | `0x3A970` | 80 | UnwindData |  |
| 1224 | `sprintf_s` | `0x3A9D0` | 29 | UnwindData |  |
| 1287 | `vsprintf_s` | `0x3AA00` | 95 | UnwindData |  |
| 1229 | `sscanf_s` | `0x3AA70` | 93 | UnwindData |  |
| 1259 | `swprintf_s` | `0x3AAE0` | 29 | UnwindData |  |
| 1289 | `vswprintf_s` | `0x3AB10` | 105 | UnwindData |  |
| 1261 | `swscanf_s` | `0x3AB80` | 96 | UnwindData |  |
| 1330 | `wscanf_s` | `0x3ABF0` | 80 | UnwindData |  |
| 281 | `_exit` | `0x3E240` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `_amsg_exit` | `0x3E310` | 80 | UnwindData |  |
| 200 | `_c_exit` | `0x3E370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `_cexit` | `0x3E390` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `_get_osplatform` | `0x3E410` | 67 | UnwindData |  |
| 355 | `_get_osver` | `0x3E460` | 72 | UnwindData |  |
| 357 | `_get_pgmptr` | `0x3E4B0` | 70 | UnwindData |  |
| 362 | `_get_winmajor` | `0x3E500` | 72 | UnwindData |  |
| 363 | `_get_winminor` | `0x3E550` | 72 | UnwindData |  |
| 364 | `_get_winver` | `0x3E5A0` | 72 | UnwindData |  |
| 365 | `_get_wpgmptr` | `0x3E5F0` | 70 | UnwindData |  |
| 395 | `_initterm` | `0x3E690` | 54 | UnwindData |  |
| 396 | `_initterm_e` | `0x3E6D0` | 61 | UnwindData |  |
| 1089 | `exit` | `0x3E920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `__threadhandle` | `0x3E940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `__threadid` | `0x3E950` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `_freefls` | `0x3E990` | 342 | UnwindData |  |
| 198 | `_beginthread` | `0x3ED70` | 256 | UnwindData |  |
| 268 | `_endthread` | `0x3EEB0` | 57 | UnwindData |  |
| 199 | `_beginthreadex` | `0x3EF80` | 264 | UnwindData |  |
| 269 | `_endthreadex` | `0x3F0D0` | 40 | UnwindData |  |
| 500 | `_lock` | `0x3F190` | 68 | UnwindData |  |
| 848 | `_unlock` | `0x3F3E0` | 7,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `__iob_func` | `0x410E0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `_cprintf` | `0x412E0` | 39 | UnwindData |  |
| 228 | `_cprintf_l` | `0x41310` | 33 | UnwindData |  |
| 852 | `_vcprintf` | `0x41340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `_vcprintf_l` | `0x41350` | 2,775 | UnwindData |  |
| 229 | `_cprintf_p` | `0x41E50` | 39 | UnwindData |  |
| 230 | `_cprintf_p_l` | `0x41E80` | 33 | UnwindData |  |
| 854 | `_vcprintf_p` | `0x41EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 855 | `_vcprintf_p_l` | `0x41EC0` | 4,930 | UnwindData |  |
| 231 | `_cprintf_s` | `0x43210` | 39 | UnwindData |  |
| 232 | `_cprintf_s_l` | `0x43240` | 33 | UnwindData |  |
| 856 | `_vcprintf_s` | `0x43270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 857 | `_vcprintf_s_l` | `0x43280` | 2,784 | UnwindData |  |
| 240 | `_cscanf` | `0x44D90` | 39 | UnwindData |  |
| 241 | `_cscanf_l` | `0x44DC0` | 33 | UnwindData |  |
| 242 | `_cscanf_s` | `0x45EE0` | 39 | UnwindData |  |
| 243 | `_cscanf_s_l` | `0x45F10` | 33 | UnwindData |  |
| 250 | `_cwprintf` | `0x46030` | 39 | UnwindData |  |
| 251 | `_cwprintf_l` | `0x46060` | 33 | UnwindData |  |
| 858 | `_vcwprintf` | `0x46090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 859 | `_vcwprintf_l` | `0x460A0` | 2,983 | UnwindData |  |
| 252 | `_cwprintf_p` | `0x46C50` | 39 | UnwindData |  |
| 253 | `_cwprintf_p_l` | `0x46C80` | 33 | UnwindData |  |
| 860 | `_vcwprintf_p` | `0x46CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 861 | `_vcwprintf_p_l` | `0x46CC0` | 5,110 | UnwindData |  |
| 254 | `_cwprintf_s` | `0x480C0` | 39 | UnwindData |  |
| 255 | `_cwprintf_s_l` | `0x480F0` | 33 | UnwindData |  |
| 862 | `_vcwprintf_s` | `0x48120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `_vcwprintf_s_l` | `0x48130` | 2,953 | UnwindData |  |
| 256 | `_cwscanf` | `0x49F20` | 39 | UnwindData |  |
| 257 | `_cwscanf_l` | `0x49F50` | 33 | UnwindData |  |
| 258 | `_cwscanf_s` | `0x4B210` | 39 | UnwindData |  |
| 259 | `_cwscanf_s_l` | `0x4B240` | 33 | UnwindData |  |
| 284 | `_fcloseall` | `0x4B270` | 168 | UnwindData |  |
| 287 | `_fdopen` | `0x4B320` | 497 | UnwindData |  |
| 288 | `_fgetchar` | `0x4B520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1130 | `getchar` | `0x4B520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `_fgetwchar` | `0x4B540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `getwchar` | `0x4B540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `_filbuf` | `0x4B560` | 339 | UnwindData |  |
| 294 | `_fileno` | `0x4B6C0` | 54 | UnwindData |  |
| 304 | `_flsbuf` | `0x4B700` | 399 | UnwindData |  |
| 305 | `_flushall` | `0x4B970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `fflush` | `0x4B980` | 67 | UnwindData |  |
| 310 | `_fprintf_l` | `0x4BAC0` | 29 | UnwindData |  |
| 311 | `_fprintf_p` | `0x4BAF0` | 36 | UnwindData |  |
| 312 | `_fprintf_p_l` | `0x4BB20` | 29 | UnwindData |  |
| 313 | `_fprintf_s_l` | `0x4BB50` | 29 | UnwindData |  |
| 1108 | `fprintf` | `0x4BB80` | 332 | UnwindData |  |
| 1109 | `fprintf_s` | `0x4BCE0` | 36 | UnwindData |  |
| 314 | `_fputchar` | `0x4BD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `putchar` | `0x4BD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `_fputwchar` | `0x4BD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `putwchar` | `0x4BD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `_fscanf_l` | `0x4BD50` | 49 | UnwindData |  |
| 322 | `_fscanf_s_l` | `0x4BD90` | 49 | UnwindData |  |
| 1119 | `fscanf` | `0x4BDD0` | 53 | UnwindData |  |
| 1120 | `fscanf_s` | `0x4BE10` | 53 | UnwindData |  |
| 323 | `_fseeki64` | `0x4BFA0` | 77 | UnwindData |  |
| 324 | `_fsopen` | `0x4C0B0` | 227 | UnwindData |  |
| 1106 | `fopen` | `0x4C1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `fopen_s` | `0x4C1C0` | 99 | UnwindData |  |
| 338 | `_fwprintf_l` | `0x4C230` | 29 | UnwindData |  |
| 339 | `_fwprintf_p` | `0x4C260` | 36 | UnwindData |  |
| 340 | `_fwprintf_p_l` | `0x4C290` | 29 | UnwindData |  |
| 341 | `_fwprintf_s_l` | `0x4C2C0` | 29 | UnwindData |  |
| 1124 | `fwprintf` | `0x4C2F0` | 148 | UnwindData |  |
| 1125 | `fwprintf_s` | `0x4C390` | 36 | UnwindData |  |
| 342 | `_fwscanf_l` | `0x4C3C0` | 49 | UnwindData |  |
| 343 | `_fwscanf_s_l` | `0x4C400` | 49 | UnwindData |  |
| 1127 | `fwscanf` | `0x4C440` | 53 | UnwindData |  |
| 1128 | `fwscanf_s` | `0x4C480` | 53 | UnwindData |  |
| 356 | `_get_output_format` | `0x4C560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `_set_output_format` | `0x4C570` | 68 | UnwindData |  |
| 373 | `_getmaxstdio` | `0x4C5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 724 | `_setmaxstdio` | `0x4C5D0` | 289 | UnwindData |  |
| 377 | `_getw` | `0x4C700` | 205 | UnwindData |  |
| 380 | `_getws` | `0x4C7E0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 675 | `_pclose` | `0x4C960` | 227 | UnwindData |  |
| 679 | `_popen` | `0x4CA50` | 1,748 | UnwindData |  |
| 680 | `_printf_l` | `0x4D1C0` | 33 | UnwindData |  |
| 681 | `_printf_p` | `0x4D1F0` | 39 | UnwindData |  |
| 682 | `_printf_p_l` | `0x4D220` | 33 | UnwindData |  |
| 683 | `_printf_s_l` | `0x4D250` | 33 | UnwindData |  |
| 1196 | `printf` | `0x4D280` | 159 | UnwindData |  |
| 1197 | `printf_s` | `0x4D330` | 39 | UnwindData |  |
| 688 | `_putw` | `0x4D360` | 186 | UnwindData |  |
| 690 | `_putws` | `0x4D420` | 193 | UnwindData |  |
| 696 | `_rmtmp` | `0x4D500` | 158 | UnwindData |  |
| 703 | `_scanf_l` | `0x4D5B0` | 46 | UnwindData |  |
| 704 | `_scanf_s_l` | `0x4D5F0` | 46 | UnwindData |  |
| 1212 | `scanf` | `0x4D630` | 50 | UnwindData |  |
| 705 | `_scprintf` | `0x4D710` | 37 | UnwindData |  |
| 706 | `_scprintf_l` | `0x4D740` | 33 | UnwindData |  |
| 707 | `_scprintf_p_l` | `0x4D770` | 33 | UnwindData |  |
| 734 | `_snprintf_s_l` | `0x4D7A0` | 33 | UnwindData |  |
| 759 | `_sprintf_l` | `0x4D7D0` | 29 | UnwindData |  |
| 760 | `_sprintf_p_l` | `0x4D800` | 29 | UnwindData |  |
| 761 | `_sprintf_s_l` | `0x4D830` | 29 | UnwindData |  |
| 1223 | `sprintf` | `0x4D860` | 162 | UnwindData |  |
| 708 | `_scwprintf` | `0x4D910` | 37 | UnwindData |  |
| 709 | `_scwprintf_l` | `0x4D940` | 33 | UnwindData |  |
| 710 | `_scwprintf_p_l` | `0x4D970` | 33 | UnwindData |  |
| 742 | `_snwprintf_s_l` | `0x4D9A0` | 33 | UnwindData |  |
| 810 | `_swprintf` | `0x4D9D0` | 199 | UnwindData |  |
| 1258 | `swprintf` | `0x4D9D0` | 199 | UnwindData |  |
| 813 | `_swprintf_p_l` | `0x4DAA0` | 29 | UnwindData |  |
| 814 | `_swprintf_s_l` | `0x4DAD0` | 29 | UnwindData |  |
| 729 | `_snprintf` | `0x4DB00` | 185 | UnwindData |  |
| 732 | `_snprintf_l` | `0x4DBC0` | 29 | UnwindData |  |
| 730 | `_snprintf_c` | `0x4DBF0` | 197 | UnwindData |  |
| 731 | `_snprintf_c_l` | `0x4DCC0` | 29 | UnwindData |  |
| 735 | `_snscanf` | `0x4DD10` | 60 | UnwindData |  |
| 736 | `_snscanf_l` | `0x4DD60` | 54 | UnwindData |  |
| 738 | `_snscanf_s_l` | `0x4DDA0` | 54 | UnwindData |  |
| 739 | `_snwprintf` | `0x4DE80` | 235 | UnwindData |  |
| 740 | `_snwprintf_l` | `0x4DF80` | 29 | UnwindData |  |
| 743 | `_snwscanf` | `0x4DFD0` | 60 | UnwindData |  |
| 744 | `_snwscanf_l` | `0x4E020` | 54 | UnwindData |  |
| 746 | `_snwscanf_s_l` | `0x4E060` | 54 | UnwindData |  |
| 762 | `_sscanf_l` | `0x4E140` | 54 | UnwindData |  |
| 763 | `_sscanf_s_l` | `0x4E180` | 54 | UnwindData |  |
| 1228 | `sscanf` | `0x4E1C0` | 55 | UnwindData |  |
| 811 | `_swprintf_c` | `0x4E2B0` | 256 | UnwindData |  |
| 812 | `_swprintf_c_l` | `0x4E3C0` | 29 | UnwindData |  |
| 815 | `_swscanf_l` | `0x4E3F0` | 54 | UnwindData |  |
| 816 | `_swscanf_s_l` | `0x4E430` | 54 | UnwindData |  |
| 1260 | `swscanf` | `0x4E470` | 55 | UnwindData |  |
| 821 | `_tempnam` | `0x4E570` | 684 | UnwindData |  |
| 822 | `_tempnam_dbg` | `0x4E830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `_ungetc_nolock` | `0x4E840` | 270 | UnwindData |  |
| 1276 | `ungetc` | `0x4E960` | 103 | UnwindData |  |
| 864 | `_vfprintf_l` | `0x4E9D0` | 35 | UnwindData |  |
| 865 | `_vfprintf_p` | `0x4EA00` | 35 | UnwindData |  |
| 866 | `_vfprintf_p_l` | `0x4EA30` | 35 | UnwindData |  |
| 867 | `_vfprintf_s_l` | `0x4EA60` | 35 | UnwindData |  |
| 1279 | `vfprintf` | `0x4EA90` | 35 | UnwindData |  |
| 1280 | `vfprintf_s` | `0x4EC30` | 35 | UnwindData |  |
| 868 | `_vfwprintf_l` | `0x4EC60` | 35 | UnwindData |  |
| 869 | `_vfwprintf_p` | `0x4EC90` | 35 | UnwindData |  |
| 870 | `_vfwprintf_p_l` | `0x4ECC0` | 35 | UnwindData |  |
| 871 | `_vfwprintf_s_l` | `0x4ECF0` | 35 | UnwindData |  |
| 1281 | `vfwprintf` | `0x4ED20` | 35 | UnwindData |  |
| 1282 | `vfwprintf_s` | `0x4EE00` | 35 | UnwindData |  |
| 872 | `_vprintf_l` | `0x4EE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `_vprintf_p` | `0x4EE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `_vprintf_p_l` | `0x4EE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `_vprintf_s_l` | `0x4EE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1283 | `vprintf` | `0x4EEB0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `vprintf_s` | `0x4EF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 876 | `_vscprintf` | `0x4EFA0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `_vscprintf_l` | `0x4F040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 878 | `_vscprintf_p_l` | `0x4F060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `_vsprintf_l` | `0x4F080` | 148 | UnwindData |  |
| 1286 | `vsprintf` | `0x4F120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `_vscwprintf` | `0x4F140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `_vscwprintf_l` | `0x4F160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 881 | `_vscwprintf_p_l` | `0x4F180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 896 | `_vswprintf` | `0x4F1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1288 | `vswprintf` | `0x4F1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 899 | `_vswprintf_l` | `0x4F1C0` | 185 | UnwindData |  |
| 882 | `_vsnprintf` | `0x4F280` | 22 | UnwindData |  |
| 1285 | `vsnprintf` | `0x4F280` | 22 | UnwindData |  |
| 885 | `_vsnprintf_l` | `0x4F2A0` | 196 | UnwindData |  |
| 883 | `_vsnprintf_c` | `0x4F370` | 49 | UnwindData |  |
| 884 | `_vsnprintf_c_l` | `0x4F3B0` | 53 | UnwindData |  |
| 887 | `_vsnprintf_s_l` | `0x4F4F0` | 326 | UnwindData |  |
| 893 | `_vsprintf_p` | `0x4F640` | 49 | UnwindData |  |
| 894 | `_vsprintf_p_l` | `0x4F680` | 53 | UnwindData |  |
| 895 | `_vsprintf_s_l` | `0x4F6C0` | 126 | UnwindData |  |
| 888 | `_vsnwprintf` | `0x4F750` | 22 | UnwindData |  |
| 889 | `_vsnwprintf_l` | `0x4F770` | 244 | UnwindData |  |
| 891 | `_vsnwprintf_s_l` | `0x4F870` | 327 | UnwindData |  |
| 897 | `_vswprintf_c` | `0x4F9C0` | 49 | UnwindData |  |
| 898 | `_vswprintf_c_l` | `0x4FA00` | 53 | UnwindData |  |
| 900 | `_vswprintf_p_l` | `0x4FB70` | 53 | UnwindData |  |
| 901 | `_vswprintf_s_l` | `0x4FBB0` | 136 | UnwindData |  |
| 902 | `_vwprintf_l` | `0x4FC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `_vwprintf_p` | `0x4FC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `_vwprintf_p_l` | `0x4FC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 905 | `_vwprintf_s_l` | `0x4FCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `vwprintf` | `0x4FCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1291 | `vwprintf_s` | `0x4FCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 971 | `_wfdopen` | `0x4FD00` | 587 | UnwindData |  |
| 978 | `_wfopen` | `0x4FF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 979 | `_wfopen_s` | `0x4FF80` | 99 | UnwindData |  |
| 982 | `_wfsopen` | `0x4FFF0` | 227 | UnwindData |  |
| 980 | `_wfreopen` | `0x500E0` | 47 | UnwindData |  |
| 981 | `_wfreopen_s` | `0x50210` | 22 | UnwindData |  |
| 1002 | `_wpopen` | `0x50230` | 1,951 | UnwindData |  |
| 1003 | `_wprintf_l` | `0x509E0` | 33 | UnwindData |  |
| 1004 | `_wprintf_p` | `0x50A10` | 39 | UnwindData |  |
| 1005 | `_wprintf_p_l` | `0x50A40` | 33 | UnwindData |  |
| 1006 | `_wprintf_s_l` | `0x50A70` | 33 | UnwindData |  |
| 1327 | `wprintf` | `0x50AA0` | 159 | UnwindData |  |
| 1328 | `wprintf_s` | `0x50B50` | 39 | UnwindData |  |
| 1013 | `_wscanf_l` | `0x50B80` | 46 | UnwindData |  |
| 1014 | `_wscanf_s_l` | `0x50BC0` | 46 | UnwindData |  |
| 1329 | `wscanf` | `0x50C00` | 50 | UnwindData |  |
| 1038 | `_wtempnam` | `0x50C40` | 672 | UnwindData |  |
| 1039 | `_wtempnam_dbg` | `0x50EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1040 | `_wtmpnam` | `0x50F00` | 48 | UnwindData |  |
| 1041 | `_wtmpnam_s` | `0x51100` | 80 | UnwindData |  |
| 1079 | `clearerr` | `0x513A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1080 | `clearerr_s` | `0x513B0` | 193 | UnwindData |  |
| 1093 | `fclose` | `0x51510` | 108 | UnwindData |  |
| 1094 | `feof` | `0x51590` | 56 | UnwindData |  |
| 1095 | `ferror` | `0x515D0` | 56 | UnwindData |  |
| 1097 | `fgetc` | `0x51610` | 299 | UnwindData |  |
| 1129 | `getc` | `0x51610` | 299 | UnwindData |  |
| 1098 | `fgetpos` | `0x51750` | 90 | UnwindData |  |
| 1099 | `fgets` | `0x517B0` | 402 | UnwindData |  |
| 1100 | `fgetwc` | `0x51B50` | 100 | UnwindData |  |
| 1134 | `getwc` | `0x51BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `fgetws` | `0x51BD0` | 204 | UnwindData |  |
| 1110 | `fputc` | `0x51CB0` | 308 | UnwindData |  |
| 1198 | `putc` | `0x51CB0` | 308 | UnwindData |  |
| 1111 | `fputs` | `0x51DF0` | 315 | UnwindData |  |
| 1112 | `fputwc` | `0x52110` | 109 | UnwindData |  |
| 1201 | `putwc` | `0x52190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1113 | `fputws` | `0x521A0` | 188 | UnwindData |  |
| 1114 | `fread` | `0x524C0` | 29 | UnwindData |  |
| 1116 | `freopen` | `0x52690` | 47 | UnwindData |  |
| 1117 | `freopen_s` | `0x526D0` | 22 | UnwindData |  |
| 1121 | `fseek` | `0x527A0` | 129 | UnwindData |  |
| 1122 | `fsetpos` | `0x52830` | 69 | UnwindData |  |
| 1123 | `ftell` | `0x52A60` | 96 | UnwindData |  |
| 1126 | `fwrite` | `0x52C80` | 149 | UnwindData |  |
| 1133 | `gets` | `0x52F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1200 | `puts` | `0x52FB0` | 380 | UnwindData |  |
| 1211 | `rewind` | `0x53140` | 199 | UnwindData |  |
| 1214 | `setbuf` | `0x53210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `setvbuf` | `0x53240` | 280 | UnwindData |  |
| 1268 | `tmpfile` | `0x539E0` | 35 | UnwindData |  |
| 1269 | `tmpfile_s` | `0x53A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1270 | `tmpnam` | `0x53A20` | 48 | UnwindData |  |
| 1271 | `tmpnam_s` | `0x53A60` | 80 | UnwindData |  |
| 1277 | `ungetwc` | `0x53CC0` | 109 | UnwindData |  |
| 157 | `__strncnt` | `0x5F360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `__wcsncnt` | `0x5F390` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `_mbsdup` | `0x5F3D0` | 116 | UnwindData |  |
| 772 | `_strdup` | `0x5F3D0` | 116 | UnwindData |  |
| 773 | `_strdup_dbg` | `0x5F450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `mbsdup_dbg` | `0x5F450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 655 | `_memccpy` | `0x5F460` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 656 | `_memicmp` | `0x5F500` | 96 | UnwindData |  |
| 657 | `_memicmp_l` | `0x5F570` | 235 | UnwindData |  |
| 768 | `_strcmpi` | `0x5F6B0` | 86 | UnwindData |  |
| 776 | `_stricmp` | `0x5F6B0` | 86 | UnwindData |  |
| 777 | `_stricmp_l` | `0x5F710` | 191 | UnwindData |  |
| 769 | `_strcoll_l` | `0x5F7E0` | 210 | UnwindData |  |
| 1234 | `strcoll` | `0x5F8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 778 | `_stricoll` | `0x5F8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `_stricoll_l` | `0x5F8F0` | 195 | UnwindData |  |
| 780 | `_strlwr` | `0x5FBE0` | 109 | UnwindData |  |
| 781 | `_strlwr_l` | `0x5FC60` | 30 | UnwindData |  |
| 782 | `_strlwr_s` | `0x5FC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 783 | `_strlwr_s_l` | `0x5FCA0` | 75 | UnwindData |  |
| 784 | `_strncoll` | `0x5FD00` | 95 | UnwindData |  |
| 785 | `_strncoll_l` | `0x5FD70` | 282 | UnwindData |  |
| 786 | `_strnicmp` | `0x5FF00` | 95 | UnwindData |  |
| 787 | `_strnicmp_l` | `0x5FF70` | 230 | UnwindData |  |
| 788 | `_strnicoll` | `0x60060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `_strnicoll_l` | `0x60080` | 286 | UnwindData |  |
| 790 | `_strnset` | `0x601B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | `_strnset_s` | `0x601D0` | 138 | UnwindData |  |
| 792 | `_strrev` | `0x60260` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `_strset` | `0x602A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `_strset_s` | `0x602C0` | 92 | UnwindData |  |
| 804 | `_strupr` | `0x60540` | 109 | UnwindData |  |
| 805 | `_strupr_l` | `0x605C0` | 30 | UnwindData |  |
| 806 | `_strupr_s` | `0x605F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 807 | `_strupr_s_l` | `0x60600` | 75 | UnwindData |  |
| 808 | `_strxfrm_l` | `0x60660` | 384 | UnwindData |  |
| 1257 | `strxfrm` | `0x607F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 915 | `_wcscoll_l` | `0x60800` | 214 | UnwindData |  |
| 1298 | `wcscoll` | `0x608E0` | 117 | UnwindData |  |
| 916 | `_wcsdup` | `0x60960` | 132 | UnwindData |  |
| 917 | `_wcsdup_dbg` | `0x609F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 921 | `_wcsicmp` | `0x60A00` | 173 | UnwindData |  |
| 922 | `_wcsicmp_l` | `0x60AC0` | 265 | UnwindData |  |
| 923 | `_wcsicoll` | `0x60BD0` | 173 | UnwindData |  |
| 924 | `_wcsicoll_l` | `0x60C90` | 272 | UnwindData |  |
| 925 | `_wcslwr` | `0x60FD0` | 127 | UnwindData |  |
| 926 | `_wcslwr_l` | `0x61060` | 30 | UnwindData |  |
| 927 | `_wcslwr_s` | `0x61090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | `_wcslwr_s_l` | `0x610A0` | 75 | UnwindData |  |
| 929 | `_wcsncoll` | `0x61100` | 95 | UnwindData |  |
| 930 | `_wcsncoll_l` | `0x61170` | 240 | UnwindData |  |
| 931 | `_wcsnicmp` | `0x61270` | 193 | UnwindData |  |
| 932 | `_wcsnicmp_l` | `0x61340` | 306 | UnwindData |  |
| 933 | `_wcsnicoll` | `0x61480` | 191 | UnwindData |  |
| 934 | `_wcsnicoll_l` | `0x61550` | 363 | UnwindData |  |
| 935 | `_wcsnset` | `0x616D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `_wcsnset_s` | `0x61700` | 146 | UnwindData |  |
| 937 | `_wcsrev` | `0x617A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 938 | `_wcsset` | `0x617F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 939 | `_wcsset_s` | `0x61810` | 99 | UnwindData |  |
| 949 | `_wcsupr` | `0x61AE0` | 127 | UnwindData |  |
| 950 | `_wcsupr_l` | `0x61B70` | 30 | UnwindData |  |
| 951 | `_wcsupr_s` | `0x61BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 952 | `_wcsupr_s_l` | `0x61BB0` | 75 | UnwindData |  |
| 953 | `_wcsxfrm_l` | `0x61C10` | 412 | UnwindData |  |
| 1323 | `wcsxfrm` | `0x61DC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `memchr` | `0x61DF0` | 144 | UnwindData |  |
| 1186 | `memcpy_s` | `0x61E90` | 151 | UnwindData |  |
| 1188 | `memmove_s` | `0x61F30` | 97 | UnwindData |  |
| 1231 | `strcat_s` | `0x61FB0` | 129 | UnwindData |  |
| 1232 | `strchr` | `0x62040` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1236 | `strcpy_s` | `0x620D0` | 114 | UnwindData |  |
| 1237 | `strcspn` | `0x62150` | 134 | UnwindData |  |
| 1243 | `strncat_s` | `0x621F0` | 238 | UnwindData |  |
| 1246 | `strncpy_s` | `0x622F0` | 224 | UnwindData |  |
| 1247 | `strnlen` | `0x623E0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `strpbrk` | `0x62530` | 112 | UnwindData |  |
| 1249 | `strrchr` | `0x625B0` | 317 | UnwindData |  |
| 1250 | `strspn` | `0x62700` | 138 | UnwindData |  |
| 1251 | `strstr` | `0x62790` | 492 | UnwindData |  |
| 1253 | `strtok` | `0x62990` | 236 | UnwindData |  |
| 1254 | `strtok_s` | `0x62A90` | 345 | UnwindData |  |
| 1294 | `wcscat` | `0x62BF0` | 47 | UnwindData |  |
| 1299 | `wcscpy` | `0x62C30` | 57 | UnwindData |  |
| 1295 | `wcscat_s` | `0x62C70` | 145 | UnwindData |  |
| 1296 | `wcschr` | `0x62D10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1297 | `wcscmp` | `0x62D90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1300 | `wcscpy_s` | `0x62DD0` | 129 | UnwindData |  |
| 1301 | `wcscspn` | `0x62E60` | 94 | UnwindData |  |
| 1303 | `wcslen` | `0x62ED0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `wcsncat` | `0x62FF0` | 99 | UnwindData |  |
| 1305 | `wcsncat_s` | `0x63060` | 259 | UnwindData |  |
| 1306 | `wcsncmp` | `0x63170` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `wcsncpy` | `0x631B0` | 119 | UnwindData |  |
| 1308 | `wcsncpy_s` | `0x63230` | 244 | UnwindData |  |
| 1309 | `wcsnlen` | `0x63330` | 453 | UnwindData |  |
| 1310 | `wcspbrk` | `0x63500` | 77 | UnwindData |  |
| 1311 | `wcsrchr` | `0x63560` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1314 | `wcsspn` | `0x63620` | 94 | UnwindData |  |
| 1315 | `wcsstr` | `0x63690` | 534 | UnwindData |  |
| 1317 | `wcstok` | `0x638B0` | 167 | UnwindData |  |
| 1318 | `wcstok_s` | `0x63960` | 213 | UnwindData |  |
| 94 | `_Getdays` | `0x64650` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `_Getmonths` | `0x647C0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `_Gettnames` | `0x64940` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `_Strftime` | `0x64DF0` | 30 | UnwindData |  |
| 1240 | `strftime` | `0x64FD0` | 26 | UnwindData |  |
| 99 | `_W_Getdays` | `0x65C30` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `_W_Getmonths` | `0x65DE0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `_W_Gettnames` | `0x65F90` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `_Wcsftime` | `0x664C0` | 30 | UnwindData |  |
| 920 | `_wcsftime_l` | `0x66670` | 30 | UnwindData |  |
| 1302 | `wcsftime` | `0x666A0` | 26 | UnwindData |  |
| 134 | `__daylight` | `0x666C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `__dstbias` | `0x666D0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `_ctime32` | `0x667C0` | 141 | UnwindData |  |
| 245 | `_ctime32_s` | `0x66860` | 183 | UnwindData |  |
| 1086 | `ctime` | `0x66920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `_ctime64` | `0x66930` | 142 | UnwindData |  |
| 247 | `_ctime64_s` | `0x669D0` | 198 | UnwindData |  |
| 261 | `_difftime32` | `0x66AA0` | 43 | UnwindData |  |
| 1087 | `difftime` | `0x66AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `_difftime64` | `0x66AF0` | 46 | UnwindData |  |
| 328 | `_ftime` | `0x66B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `_ftime64` | `0x66B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `_ftime32` | `0x66B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `_ftime32_s` | `0x66B50` | 432 | UnwindData |  |
| 332 | `_ftime64_s` | `0x66D10` | 435 | UnwindData |  |
| 335 | `_futime` | `0x66ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `_futime32` | `0x66EE0` | 553 | UnwindData |  |
| 849 | `_utime` | `0x67110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `utime` | `0x67110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | `_utime32` | `0x67120` | 153 | UnwindData |  |
| 337 | `_futime64` | `0x671C0` | 555 | UnwindData |  |
| 851 | `_utime64` | `0x67400` | 153 | UnwindData |  |
| 376 | `_getsystime` | `0x674A0` | 181 | UnwindData |  |
| 727 | `_setsystime` | `0x67560` | 177 | UnwindData |  |
| 381 | `_gmtime32` | `0x67660` | 69 | UnwindData |  |
| 382 | `_gmtime32_s` | `0x676B0` | 427 | UnwindData |  |
| 1136 | `gmtime` | `0x67870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `_gmtime64` | `0x67880` | 69 | UnwindData |  |
| 384 | `_gmtime64_s` | `0x678D0` | 717 | UnwindData |  |
| 496 | `_localtime32` | `0x67BB0` | 69 | UnwindData |  |
| 497 | `_localtime32_s` | `0x67C00` | 737 | UnwindData |  |
| 1167 | `localtime` | `0x67EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `_localtime64` | `0x67F00` | 69 | UnwindData |  |
| 499 | `_localtime64_s` | `0x67F50` | 805 | UnwindData |  |
| 659 | `_mkgmtime` | `0x68540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | `_mkgmtime32` | `0x68550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `_mktime32` | `0x68560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `mktime` | `0x68570` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 661 | `_mkgmtime64` | `0x68870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `_mktime64` | `0x68880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `_strdate` | `0x68890` | 36 | UnwindData |  |
| 771 | `_strdate_s` | `0x688C0` | 309 | UnwindData |  |
| 795 | `_strtime` | `0x68A00` | 36 | UnwindData |  |
| 796 | `_strtime_s` | `0x68A30` | 282 | UnwindData |  |
| 823 | `_time32` | `0x68B50` | 91 | UnwindData |  |
| 1267 | `time` | `0x68BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | `_time64` | `0x68BD0` | 99 | UnwindData |  |
| 833 | `_tzset` | `0x68F30` | 40 | UnwindData |  |
| 908 | `_wasctime` | `0x696C0` | 123 | UnwindData |  |
| 909 | `_wasctime_s` | `0x69750` | 812 | UnwindData |  |
| 954 | `_wctime` | `0x69A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `_wctime32` | `0x69AA0` | 141 | UnwindData |  |
| 956 | `_wctime32_s` | `0x69B40` | 175 | UnwindData |  |
| 957 | `_wctime64` | `0x69C00` | 142 | UnwindData |  |
| 958 | `_wctime64_s` | `0x69CA0` | 192 | UnwindData |  |
| 1033 | `_wstrdate` | `0x69D70` | 36 | UnwindData |  |
| 1034 | `_wstrdate_s` | `0x69DA0` | 347 | UnwindData |  |
| 1035 | `_wstrtime` | `0x69F10` | 36 | UnwindData |  |
| 1036 | `_wstrtime_s` | `0x69F40` | 321 | UnwindData |  |
| 1051 | `_wutime` | `0x6A090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `_wutime32` | `0x6A0A0` | 153 | UnwindData |  |
| 1053 | `_wutime64` | `0x6A140` | 153 | UnwindData |  |
| 1061 | `asctime` | `0x6A1E0` | 123 | UnwindData |  |
| 1062 | `asctime_s` | `0x6A270` | 763 | UnwindData |  |
| 1081 | `clock` | `0x6A5C0` | 67 | UnwindData |  |
| 156 | `__setusermatherr` | `0x6DCE0` | 31 | UnwindData |  |
| 201 | `_cabs` | `0x6DD50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `_chgsign` | `0x6DD70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `_chgsignf` | `0x6DDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `_clearfp` | `0x6DDC0` | 103 | UnwindData |  |
| 222 | `_control87` | `0x6DE30` | 657 | UnwindData |  |
| 223 | `_controlfp` | `0x6E0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `_fpreset` | `0x6E0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | `_set_controlfp` | `0x6E0F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `_statusfp` | `0x6E130` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `_controlfp_s` | `0x6E190` | 130 | UnwindData |  |
| 225 | `_copysign` | `0x6E220` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `_copysignf` | `0x6E260` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `_finite` | `0x6E290` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `_finitef` | `0x6E2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `_fpclass` | `0x6E2E0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `_fpclassf` | `0x6E380` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `_isnan` | `0x6E410` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `_isnanf` | `0x6E450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 668 | `_nextafter` | `0x6E470` | 493 | UnwindData |  |
| 669 | `_nextafterf` | `0x6E670` | 433 | UnwindData |  |
| 701 | `_scalb` | `0x6E830` | 43 | UnwindData |  |
| 702 | `_scalbf` | `0x6EA60` | 498 | UnwindData |  |
| 389 | `_hypot` | `0x6EC60` | 156 | UnwindData |  |
| 390 | `_hypotf` | `0x6EEF0` | 318 | UnwindData |  |
| 489 | `_j0` | `0x6F040` | 254 | UnwindData |  |
| 490 | `_j1` | `0x6F330` | 283 | UnwindData |  |
| 491 | `_jn` | `0x6F640` | 99 | UnwindData |  |
| 1054 | `_y0` | `0x6F7F0` | 100 | UnwindData |  |
| 1055 | `_y1` | `0x6FB60` | 100 | UnwindData |  |
| 1056 | `_yn` | `0x6FED0` | 187 | UnwindData |  |
| 502 | `_logb` | `0x700F0` | 296 | UnwindData |  |
| 503 | `_logbf` | `0x70220` | 234 | UnwindData |  |
| 1059 | `acos` | `0x70310` | 709 | UnwindData |  |
| 1060 | `acosf` | `0x705E0` | 269 | UnwindData |  |
| 1063 | `asin` | `0x70860` | 750 | UnwindData |  |
| 1064 | `asinf` | `0x70B60` | 598 | UnwindData |  |
| 1065 | `atan` | `0x70DC0` | 608 | UnwindData |  |
| 1066 | `atan2` | `0x71030` | 307 | UnwindData |  |
| 1067 | `atan2f` | `0x717F0` | 1,207 | UnwindData |  |
| 1068 | `atanf` | `0x71CB0` | 597 | UnwindData |  |
| 1077 | `ceil` | `0x71F10` | 273 | UnwindData |  |
| 1078 | `ceilf` | `0x72030` | 215 | UnwindData |  |
| 1082 | `cos` | `0x72110` | 729 | UnwindData |  |
| 1219 | `sin` | `0x724A0` | 359 | UnwindData |  |
| 1083 | `cosf` | `0x72B60` | 1,025 | UnwindData |  |
| 1220 | `sinf` | `0x72F70` | 1,187 | UnwindData |  |
| 1084 | `cosh` | `0x73420` | 91 | UnwindData |  |
| 1085 | `coshf` | `0x73870` | 360 | UnwindData |  |
| 1090 | `exp` | `0x73C00` | 519 | UnwindData |  |
| 1091 | `expf` | `0x73F80` | 436 | UnwindData |  |
| 1092 | `fabs` | `0x74270` | 248 | UnwindData |  |
| 1102 | `floor` | `0x74370` | 255 | UnwindData |  |
| 1103 | `floorf` | `0x74480` | 209 | UnwindData |  |
| 1104 | `fmod` | `0x74560` | 578 | UnwindData |  |
| 1105 | `fmodf` | `0x74B10` | 1,001 | UnwindData |  |
| 1118 | `frexp` | `0x74F00` | 77 | UnwindData |  |
| 1164 | `ldexp` | `0x75020` | 393 | UnwindData |  |
| 1168 | `log` | `0x751B0` | 764 | UnwindData |  |
| 1169 | `log10` | `0x754C0` | 853 | UnwindData |  |
| 1170 | `log10f` | `0x75820` | 544 | UnwindData |  |
| 1171 | `logf` | `0x75A50` | 564 | UnwindData |  |
| 1191 | `modf` | `0x75C90` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1192 | `modff` | `0x75D60` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `pow` | `0x75E00` | 2,993 | UnwindData |  |
| 1195 | `powf` | `0x769C0` | 2,093 | UnwindData |  |
| 1221 | `sinh` | `0x77200` | 365 | UnwindData |  |
| 1222 | `sinhf` | `0x77680` | 923 | UnwindData |  |
| 1225 | `sqrt` | `0x77A30` | 273 | UnwindData |  |
| 1226 | `sqrtf` | `0x77B50` | 237 | UnwindData |  |
| 1263 | `tan` | `0x77C50` | 796 | UnwindData |  |
| 1264 | `tanf` | `0x78420` | 801 | UnwindData |  |
| 1265 | `tanh` | `0x787C0` | 207 | UnwindData |  |
| 1266 | `tanhf` | `0x78B50` | 187 | UnwindData |  |
| 722 | `_setjmp` | `0x7AB10` | 144 | UnwindData |  |
| 1215 | `setjmp` | `0x7ABB0` | 5 | UnwindData |  |
| 723 | `_setjmpex` | `0x7ABD0` | 144 | UnwindData |  |
| 545 | `_mbscat` | `0x7AEB0` | 179 | UnwindData |  |
| 1230 | `strcat` | `0x7AEB0` | 179 | UnwindData |  |
| 554 | `_mbscpy` | `0x7AF70` | 183 | UnwindData |  |
| 1235 | `strcpy` | `0x7AF70` | 183 | UnwindData |  |
| 1184 | `memcmp` | `0x7B050` | 199 | UnwindData |  |
| 1185 | `memcpy` | `0x7B180` | 682 | UnwindData |  |
| 1187 | `memmove` | `0x7B180` | 682 | UnwindData |  |
| 1233 | `strcmp` | `0x7B6E0` | 176 | UnwindData |  |
| 1241 | `strlen` | `0x7B7B0` | 168 | UnwindData |  |
| 1242 | `strncat` | `0x7B880` | 413 | UnwindData |  |
| 1244 | `strncmp` | `0x7BA40` | 181 | UnwindData |  |
| 1245 | `strncpy` | `0x7BB20` | 362 | UnwindData |  |
| 1189 | `memset` | `0x7E030` | 4,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??_7exception@@6B@` | `0x7F008` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??_7bad_cast@@6B@` | `0x7F020` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??_7bad_typeid@@6B@` | `0x7F038` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??_7__non_rtti_object@@6B@` | `0x7F050` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `_sys_errlist` | `0x7F530` | 19,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 961 | `_wctype` | `0x84150` | 2,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `_sys_nerr` | `0x84BA8` | 4,918 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `_ctype` | `0x85EDE` | 95,010 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 676 | `_pctype` | `0x9D200` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `_pwctype` | `0x9D208` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `_aexit_rtn` | `0x9D2E8` | 1,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `_iob` | `0x9DA00` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 832 | `_tzname` | `0x9E090` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `_fileinfo` | `0x9E290` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `__badioinfo` | `0x9E298` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `_mbctype` | `0x9E2F0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `_mbcasemap` | `0x9E400` | 820 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `__mb_cur_max` | `0x9E734` | 940 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `_daylight` | `0x9EAE0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `_dstbias` | `0x9EAE4` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `_timezone` | `0x9EAE8` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `_HUGE` | `0x9EBA0` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `_acmdln` | `0x9F170` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | `_wcmdln` | `0x9F178` | 212 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `_fmode` | `0x9F24C` | 84 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `__lc_handle` | `0x9F2A0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `__lc_codepage` | `0x9F2B8` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `__lc_collate_cp` | `0x9F2BC` | 1,508 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `__winitenv` | `0x9F8A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `__initenv` | `0x9F8A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `__argc` | `0x9F8B0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `__argv` | `0x9F8B8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `__wargv` | `0x9F8C0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `_environ` | `0x9F8C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 962 | `_wenviron` | `0x9F8D0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 677 | `_pgmptr` | `0x9F8D8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `_wpgmptr` | `0x9F8E0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 673 | `_osplatform` | `0x9F8E8` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `_osver` | `0x9F8EC` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `_winver` | `0x9F8F0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `_winmajor` | `0x9F8F4` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `_winminor` | `0x9F8F8` | 2,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `_commode` | `0xA02A8` | 600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `__pioinfo` | `0xA0500` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `__unguarded_readlc_active` | `0xA0700` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `__setlc_active` | `0xA0704` | 0 | Indeterminate |  |
