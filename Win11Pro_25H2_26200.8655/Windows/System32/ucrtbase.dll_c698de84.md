# Binary Specification: ucrtbase.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ucrtbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c698de8463ea580d5d00fa314487097b75bce41c432d941951e4c3fe6a95566f`
* **Total Exported Functions:** 2484

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 649 | `_mbstowcs_s_l` | `0x1170` | 124 | UnwindData |  |
| 1725 | `_o_wcstombs_s` | `0x1200` | 38 | UnwindData |  |
| 2440 | `wcrtomb` | `0x1370` | 58 | UnwindData |  |
| 2441 | `wcrtomb_s` | `0x13B0` | 103 | UnwindData |  |
| 2461 | `wcsrtombs_s` | `0x1420` | 303 | UnwindData |  |
| 1609 | `_o_mbstowcs_s` | `0x1B80` | 38 | UnwindData |  |
| 2472 | `wcstombs` | `0x1D20` | 87 | UnwindData |  |
| 2305 | `mbstowcs` | `0x1EC0` | 87 | UnwindData |  |
| 2306 | `mbstowcs_s` | `0x2070` | 332 | UnwindData |  |
| 2473 | `wcstombs_s` | `0x25D0` | 326 | UnwindData |  |
| 1934 | `_wcstombs_s_l` | `0x2720` | 345 | UnwindData |  |
| 2372 | `setlocale` | `0x2C60` | 76 | UnwindData |  |
| 174 | `_calloc_base` | `0x4FF0` | 43 | UnwindData |  |
| 522 | `_malloc_base` | `0x50A0` | 10 | UnwindData |  |
| 1750 | `_query_new_handler` | `0x5130` | 76 | UnwindData |  |
| 1779 | `_set_new_handler` | `0x51B0` | 123 | UnwindData |  |
| 173 | `_callnewh` | `0x5240` | 51 | UnwindData |  |
| 26 | `_W_Gettnames` | `0x63E0` | 3,375 | UnwindData |  |
| 338 | `_getc_nolock` | `0x7200` | 66 | UnwindData |  |
| 669 | `_msize` | `0x72E0` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `_fgetc_nolock` | `0x78B0` | 70 | UnwindData |  |
| 231 | `_errno` | `0x7A60` | 229 | UnwindData |  |
| 379 | `_invalid_parameter_noinfo` | `0x7B50` | 14 | UnwindData |  |
| 1752 | `_read` | `0x7B70` | 335 | UnwindData |  |
| 268 | `_fileno` | `0x7D40` | 41 | UnwindData |  |
| 2186 | `fgetc` | `0x8010` | 441 | UnwindData |  |
| 333 | `_get_timezone` | `0x8360` | 21 | UnwindData |  |
| 2388 | `strcpy_s` | `0x8420` | 120 | UnwindData |  |
| 2443 | `wcscat_s` | `0x84A0` | 139 | UnwindData |  |
| 2245 | `isspace` | `0x9400` | 52 | UnwindData |  |
| 2239 | `isdigit` | `0x9620` | 18 | UnwindData |  |
| 1755 | `_register_onexit_function` | `0x9790` | 89 | UnwindData |  |
| 731 | `_o___stdio_common_vswprintf_s` | `0x9FD0` | 55 | UnwindData |  |
| 1474 | `_o_bsearch` | `0xA010` | 38 | UnwindData |  |
| 2063 | `bsearch` | `0xA0C0` | 40 | UnwindData |  |
| 516 | `_ltoa` | `0xA2C0` | 205 | UnwindData |  |
| 2433 | `towupper` | `0xA590` | 865 | UnwindData |  |
| 729 | `_o___stdio_common_vswprintf` | `0xA900` | 55 | UnwindData |  |
| 2212 | `free` | `0xAD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2297 | `malloc` | `0xADA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2252 | `iswctype` | `0xADB0` | 109 | UnwindData |  |
| 1868 | `_towupper_l` | `0xB260` | 936 | UnwindData |  |
| 1867 | `_towlower_l` | `0xB610` | 1,726 | UnwindData |  |
| 2432 | `towlower` | `0xC5C0` | 1,574 | UnwindData |  |
| 2429 | `tolower` | `0xCBF0` | 1,007 | UnwindData |  |
| 1864 | `_tolower_l` | `0xCFF0` | 1,025 | UnwindData |  |
| 118 | `__stdio_common_vsprintf` | `0xD400` | 117 | UnwindData |  |
| 120 | `__stdio_common_vsprintf_s` | `0xD790` | 118 | UnwindData |  |
| 2474 | `wcstoul` | `0xDAC0` | 112 | UnwindData |  |
| 2344 | `rand` | `0xDB40` | 41 | UnwindData |  |
| 2235 | `isalnum` | `0xDBE0` | 54 | UnwindData |  |
| 643 | `_mbsstr_l` | `0xDCB0` | 43 | UnwindData |  |
| 53 | `___lc_locale_name_func` | `0xDEE0` | 97 | UnwindData |  |
| 381 | `_invoke_watson` | `0x11840` | 66 | UnwindData |  |
| 122 | `__stdio_common_vswprintf` | `0x11890` | 121 | UnwindData |  |
| 291 | `_free_base` | `0x12D60` | 70 | UnwindData |  |
| 110 | `__stdio_common_vfprintf_s` | `0x18630` | 109 | UnwindData |  |
| 112 | `__stdio_common_vfwprintf` | `0x19CE0` | 109 | UnwindData |  |
| 108 | `__stdio_common_vfprintf` | `0x19DF0` | 109 | UnwindData |  |
| 2207 | `fputs` | `0x19F00` | 85 | UnwindData |  |
| 515 | `_lseeki64` | `0x1AEC0` | 87 | UnwindData |  |
| 114 | `__stdio_common_vfwprintf_s` | `0x1AF20` | 245 | UnwindData |  |
| 2337 | `puts` | `0x1B480` | 376 | UnwindData |  |
| 2219 | `fwrite` | `0x1B760` | 219 | UnwindData |  |
| 302 | `_ftelli64` | `0x1BFB0` | 87 | UnwindData |  |
| 2185 | `fflush` | `0x1C0A0` | 88 | UnwindData |  |
| 261 | `_fflush_nolock` | `0x1C220` | 231 | UnwindData |  |
| 326 | `_get_osfhandle` | `0x1CCA0` | 138 | UnwindData |  |
| 2187 | `fgetpos` | `0x1D570` | 75 | UnwindData |  |
| 294 | `_fseeki64` | `0x1D870` | 85 | UnwindData |  |
| 2206 | `fputc` | `0x1D930` | 86 | UnwindData |  |
| 2216 | `fseek` | `0x1DB20` | 88 | UnwindData |  |
| 2210 | `fread` | `0x1DE00` | 32 | UnwindData |  |
| 2211 | `fread_s` | `0x1DE30` | 172 | UnwindData |  |
| 290 | `_fread_nolock_s` | `0x1DEF0` | 53 | UnwindData |  |
| 70 | `__doserrno` | `0x1E650` | 35 | UnwindData |  |
| 2218 | `ftell` | `0x1E920` | 85 | UnwindData |  |
| 1999 | `_wsopen_s` | `0x1FDA0` | 50 | UnwindData |  |
| 27 | `_Wcsftime` | `0x1FF20` | 30 | UnwindData |  |
| 1712 | `_o_wcsftime` | `0x1FF50` | 28 | UnwindData |  |
| 2392 | `strftime` | `0x1FFE0` | 26 | UnwindData |  |
| 23 | `_Strftime` | `0x20000` | 30 | UnwindData |  |
| 2450 | `wcsftime` | `0x20030` | 26 | UnwindData |  |
| 2302 | `mbrtowc` | `0x20220` | 163 | UnwindData |  |
| 1902 | `_wcsdup` | `0x22DF0` | 180 | UnwindData |  |
| 1910 | `_wcslwr` | `0x22EB0` | 115 | UnwindData |  |
| 1913 | `_wcslwr_s_l` | `0x22F30` | 75 | UnwindData |  |
| 1900 | `_wcreate_locale` | `0x242C0` | 329 | UnwindData |  |
| 292 | `_free_locale` | `0x24520` | 174 | UnwindData |  |
| 2454 | `wcsncmp` | `0x267C0` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1423 | `_o__wsplitpath_s` | `0x26F90` | 90 | UnwindData |  |
| 2009 | `_wsplitpath_s` | `0x270A0` | 96 | UnwindData |  |
| 2008 | `_wsplitpath` | `0x278A0` | 105 | UnwindData |  |
| 724 | `_o___stdio_common_vsnwprintf_s` | `0x28810` | 61 | UnwindData |  |
| 117 | `__stdio_common_vsnwprintf_s` | `0x288F0` | 136 | UnwindData |  |
| 124 | `__stdio_common_vswprintf_s` | `0x28D50` | 120 | UnwindData |  |
| 2332 | `perror` | `0x2A410` | 78 | UnwindData |  |
| 2459 | `wcsrchr` | `0x2CBE0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `_endthreadex` | `0x2CE10` | 10 | UnwindData |  |
| 503 | `_localtime64` | `0x2CE70` | 72 | UnwindData |  |
| 1775 | `_set_errno` | `0x2CF30` | 44 | UnwindData |  |
| 347 | `_getdrive` | `0x2E090` | 204 | UnwindData |  |
| 1906 | `_wcsicmp` | `0x2EA30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1916 | `_wcsnicmp` | `0x2EA60` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2445 | `wcscmp` | `0x2EE10` | 3,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2462 | `wcsspn` | `0x2FA00` | 88 | UnwindData |  |
| 2444 | `wcschr` | `0x2FC20` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1869 | `_tzset` | `0x2FD90` | 42 | UnwindData |  |
| 51 | `___lc_codepage_func` | `0x302F0` | 90 | UnwindData |  |
| 1918 | `_wcsnicoll` | `0x30470` | 79 | UnwindData |  |
| 2077 | `calloc` | `0x304D0` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `_mbschr_l` | `0x31110` | 232 | UnwindData |  |
| 2384 | `strchr` | `0x31200` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1828 | `_strnicoll` | `0x31690` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1754 | `_recalloc` | `0x31870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1753 | `_realloc_base` | `0x31880` | 130 | UnwindData |  |
| 1751 | `_query_new_mode` | `0x31910` | 25 | UnwindData |  |
| 1780 | `_set_new_mode` | `0x31930` | 57 | UnwindData |  |
| 1977 | `_wgetdcwd` | `0x31970` | 14 | UnwindData |  |
| 1975 | `_wfullpath` | `0x31E00` | 14 | UnwindData |  |
| 225 | `_dupenv_s` | `0x32190` | 14 | UnwindData |  |
| 1976 | `_wgetcwd` | `0x32520` | 22 | UnwindData |  |
| 343 | `_getcwd` | `0x32610` | 22 | UnwindData |  |
| 308 | `_fullpath` | `0x327D0` | 14 | UnwindData |  |
| 1732 | `_o_wmemmove_s` | `0x32C70` | 35 | UnwindData |  |
| 1242 | `_o__splitpath_s` | `0x33060` | 90 | UnwindData |  |
| 1802 | `_splitpath` | `0x33170` | 105 | UnwindData |  |
| 1713 | `_o_wcsncat_s` | `0x331E0` | 35 | UnwindData |  |
| 1803 | `_splitpath_s` | `0x334C0` | 96 | UnwindData |  |
| 590 | `_mbsnbcpy_s` | `0x33840` | 20 | UnwindData |  |
| 591 | `_mbsnbcpy_s_l` | `0x33860` | 458 | UnwindData |  |
| 1714 | `_o_wcsncpy_s` | `0x33A30` | 35 | UnwindData |  |
| 1731 | `_o_wmemcpy_s` | `0x33A60` | 35 | UnwindData |  |
| 2456 | `wcsncpy_s` | `0x33B40` | 313 | UnwindData |  |
| 2483 | `wmemcpy_s` | `0x33C80` | 133 | UnwindData |  |
| 629 | `_mbspbrk_l` | `0x33E20` | 170 | UnwindData |  |
| 2400 | `strpbrk` | `0x33ED0` | 73 | UnwindData |  |
| 1006 | `_o__itoa_s` | `0x35660` | 27 | UnwindData |  |
| 1040 | `_o__ltoa_s` | `0x356F0` | 27 | UnwindData |  |
| 517 | `_ltoa_s` | `0x35780` | 34 | UnwindData |  |
| 479 | `_itoa_s` | `0x357B0` | 32 | UnwindData |  |
| 1305 | `_o__ultoa_s` | `0x357E0` | 27 | UnwindData |  |
| 1875 | `_ultoa_s` | `0x35870` | 19 | UnwindData |  |
| 580 | `_mbsnbcat_s` | `0x35980` | 20 | UnwindData |  |
| 581 | `_mbsnbcat_s_l` | `0x359A0` | 881 | UnwindData |  |
| 459 | `_ispunct_l` | `0x35F80` | 24 | UnwindData |  |
| 461 | `_isupper_l` | `0x36070` | 24 | UnwindData |  |
| 2240 | `isgraph` | `0x37590` | 161 | UnwindData |  |
| 2237 | `isblank` | `0x37640` | 21 | UnwindData |  |
| 2243 | `isprint` | `0x37780` | 161 | UnwindData |  |
| 2242 | `islower` | `0x378B0` | 156 | UnwindData |  |
| 2238 | `iscntrl` | `0x37960` | 156 | UnwindData |  |
| 52 | `___lc_collate_cp_func` | `0x37A10` | 47 | UnwindData |  |
| 2412 | `strtoul` | `0x37B10` | 114 | UnwindData |  |
| 2060 | `atoi` | `0x37BD0` | 112 | UnwindData |  |
| 2061 | `atol` | `0x37BD0` | 112 | UnwindData |  |
| 2409 | `strtol` | `0x38C20` | 112 | UnwindData |  |
| 95 | `__pctype_func` | `0x397E0` | 90 | UnwindData |  |
| 1845 | `_strtoui64` | `0x39990` | 116 | UnwindData |  |
| 2413 | `strtoull` | `0x39990` | 116 | UnwindData |  |
| 2414 | `strtoumax` | `0x39990` | 116 | UnwindData |  |
| 506 | `_lock_locales` | `0x3E640` | 591 | UnwindData |  |
| 119 | `__stdio_common_vsprintf_p` | `0x46830` | 124 | UnwindData |  |
| 1915 | `_wcsncoll_l` | `0x489A0` | 238 | UnwindData |  |
| 1909 | `_wcsicoll_l` | `0x48AA0` | 200 | UnwindData |  |
| 1919 | `_wcsnicoll_l` | `0x48BD0` | 234 | UnwindData |  |
| 1917 | `_wcsnicmp_l` | `0x48CC0` | 68 | UnwindData |  |
| 1829 | `_strnicoll_l` | `0x48FB0` | 309 | UnwindData |  |
| 1827 | `_strnicmp_l` | `0x490F0` | 177 | UnwindData |  |
| 1901 | `_wcscoll_l` | `0x491B0` | 219 | UnwindData |  |
| 1635 | `_o_qsort_s` | `0x496B0` | 38 | UnwindData |  |
| 319 | `_get_errno` | `0x497E0` | 47 | UnwindData |  |
| 237 | `_execute_onexit_table` | `0x49820` | 67 | UnwindData |  |
| 1475 | `_o_bsearch_s` | `0x49970` | 48 | UnwindData |  |
| 2064 | `bsearch_s` | `0x49A30` | 40 | UnwindData |  |
| 2341 | `qsort_s` | `0x4A370` | 189 | UnwindData |  |
| 1634 | `_o_qsort` | `0x4A8F0` | 28 | UnwindData |  |
| 2340 | `qsort` | `0x4A990` | 164 | UnwindData |  |
| 2081 | `casin` | `0x4AF70` | 84 | UnwindData |  |
| 2129 | `cpow` | `0x4AFD0` | 196 | UnwindData |  |
| 2104 | `cexp` | `0x4B0A0` | 599 | UnwindData |  |
| 2075 | `cacoshl` | `0x4B300` | 894 | UnwindData |  |
| 2073 | `cacosh` | `0x4B690` | 894 | UnwindData |  |
| 2144 | `csqrt` | `0x4BA20` | 328 | UnwindData |  |
| 2083 | `casinh` | `0x4C190` | 833 | UnwindData |  |
| 2113 | `clog` | `0x4C4E0` | 608 | UnwindData |  |
| 2118 | `clogl` | `0x4C750` | 902 | UnwindData |  |
| 2048 | `asinf` | `0x4CF80` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2047 | `asin` | `0x4D1C0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2053 | `atan2` | `0x4D400` | 2,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2420 | `tanhf` | `0x4DF50` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `_hypotf` | `0x4E670` | 269 | UnwindData |  |
| 368 | `_hypot` | `0x4E790` | 135 | UnwindData |  |
| 2040 | `acos` | `0x4E9E0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `_logb` | `0x4ED60` | 248 | UnwindData |  |
| 2049 | `asinh` | `0x4EE90` | 227 | UnwindData |  |
| 2379 | `sqrt` | `0x4EF80` | 195 | UnwindData |  |
| 2056 | `atanh` | `0x4F050` | 212 | UnwindData |  |
| 2280 | `log1p` | `0x4F130` | 237 | UnwindData |  |
| 2283 | `log2` | `0x4F390` | 823 | UnwindData |  |
| 2380 | `sqrtf` | `0x4F970` | 151 | UnwindData |  |
| 232 | `_except1` | `0x4FA10` | 241 | UnwindData |  |
| 2203 | `fmodf` | `0x4FCB0` | 816 | UnwindData |  |
| 2145 | `csqrtf` | `0x50A90` | 408 | UnwindData |  |
| 2263 | `ldexp` | `0x51160` | 69 | UnwindData |  |
| 2084 | `casinhf` | `0x512F0` | 786 | UnwindData |  |
| 2054 | `atan2f` | `0x51610` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2050 | `asinhf` | `0x51E10` | 205 | UnwindData |  |
| 2057 | `atanhf` | `0x51EF0` | 181 | UnwindData |  |
| 2281 | `log1pf` | `0x51FB0` | 199 | UnwindData |  |
| 2090 | `catanhf` | `0x52080` | 807 | UnwindData |  |
| 2146 | `csqrtl` | `0x523B0` | 484 | UnwindData |  |
| 2058 | `atanhl` | `0x52BB0` | 226 | UnwindData |  |
| 492 | `_ldscale` | `0x52CA0` | 337 | UnwindData |  |
| 2051 | `asinhl` | `0x52E00` | 229 | UnwindData |  |
| 2351 | `remquo` | `0x52EF0` | 1,229 | UnwindData |  |
| 222 | `_dunscale` | `0x533D0` | 218 | UnwindData |  |
| 2095 | `cbrtl` | `0x534B0` | 1,014 | UnwindData |  |
| 2093 | `cbrt` | `0x538B0` | 1,014 | UnwindData |  |
| 218 | `_dscale` | `0x53CB0` | 321 | UnwindData |  |
| 215 | `_dnorm` | `0x53E00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2364 | `scalblnl` | `0x53E80` | 444 | UnwindData |  |
| 2365 | `scalbn` | `0x53E80` | 444 | UnwindData |  |
| 2367 | `scalbnl` | `0x53E80` | 444 | UnwindData |  |
| 2353 | `remquol` | `0x54050` | 1,259 | UnwindData |  |
| 2282 | `log1pl` | `0x54550` | 248 | UnwindData |  |
| 2294 | `lround` | `0x54650` | 107 | UnwindData |  |
| 2296 | `lroundl` | `0x54650` | 107 | UnwindData |  |
| 2273 | `llround` | `0x546D0` | 108 | UnwindData |  |
| 2275 | `llroundl` | `0x546D0` | 108 | UnwindData |  |
| 214 | `_dlog` | `0x54750` | 619 | UnwindData |  |
| 2271 | `llrintf` | `0x549D0` | 86 | UnwindData |  |
| 2327 | `nexttowardf` | `0x54A30` | 300 | UnwindData |  |
| 2181 | `fesetenv` | `0x54B70` | 112 | UnwindData |  |
| 2175 | `fegetenv` | `0x54BF0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2174 | `feclearexcept` | `0x54D40` | 83 | UnwindData |  |
| 256 | `_fdscale` | `0x54DA0` | 296 | UnwindData |  |
| 2094 | `cbrtf` | `0x54ED0` | 143 | UnwindData |  |
| 251 | `_fdlog` | `0x55240` | 532 | UnwindData |  |
| 252 | `_fdnorm` | `0x55460` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2270 | `llrint` | `0x554B0` | 108 | UnwindData |  |
| 2291 | `lrint` | `0x55530` | 107 | UnwindData |  |
| 2292 | `lrintf` | `0x55620` | 85 | UnwindData |  |
| 2295 | `lroundf` | `0x55680` | 85 | UnwindData |  |
| 2184 | `fetestexcept` | `0x556E0` | 30 | UnwindData |  |
| 2176 | `fegetexceptflag` | `0x55710` | 55 | UnwindData |  |
| 2182 | `fesetexceptflag` | `0x55800` | 158 | UnwindData |  |
| 2183 | `fesetround` | `0x55E00` | 140 | UnwindData |  |
| 72 | `__fpe_flt_rounds` | `0x567E0` | 62 | UnwindData |  |
| 2177 | `fegetround` | `0x56830` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2230 | `ilogbf` | `0x56990` | 133 | UnwindData |  |
| 260 | `_fdunscale` | `0x56A20` | 170 | UnwindData |  |
| 2366 | `scalbnf` | `0x56AD0` | 359 | UnwindData |  |
| 2352 | `remquof` | `0x56C40` | 1,139 | UnwindData |  |
| 2044 | `acoshl` | `0x570C0` | 215 | UnwindData |  |
| 489 | `_ldlog` | `0x571A0` | 615 | UnwindData |  |
| 2439 | `ungetwc` | `0x584B0` | 110 | UnwindData |  |
| 1883 | `_ungetwc_nolock` | `0x58530` | 254 | UnwindData |  |
| 2189 | `fgetwc` | `0x58FE0` | 94 | UnwindData |  |
| 264 | `_fgetwc_nolock` | `0x59150` | 619 | UnwindData |  |
| 2438 | `ungetc` | `0x593D0` | 104 | UnwindData |  |
| 1880 | `_ungetc_nolock` | `0x59440` | 300 | UnwindData |  |
| 1927 | `_wcstoi64` | `0x5B580` | 116 | UnwindData |  |
| 2466 | `wcstoimax` | `0x5B580` | 116 | UnwindData |  |
| 2471 | `wcstoll` | `0x5B580` | 116 | UnwindData |  |
| 1935 | `_wcstoui64` | `0x5B600` | 114 | UnwindData |  |
| 2475 | `wcstoull` | `0x5B600` | 114 | UnwindData |  |
| 2476 | `wcstoumax` | `0x5B600` | 114 | UnwindData |  |
| 2025 | `_wtoi64` | `0x5C0C0` | 114 | UnwindData |  |
| 2030 | `_wtoll` | `0x5C0C0` | 114 | UnwindData |  |
| 2258 | `iswspace` | `0x5DC30` | 107 | UnwindData |  |
| 278 | `_finite` | `0x5E890` | 2,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2399 | `strnlen` | `0x5F0A0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2457 | `wcsnlen` | `0x5F200` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `_fdclass` | `0x5F410` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2244 | `ispunct` | `0x5F460` | 52 | UnwindData |  |
| 2246 | `isupper` | `0x5F530` | 52 | UnwindData |  |
| 2261 | `isxdigit` | `0x5F600` | 54 | UnwindData |  |
| 2236 | `isalpha` | `0x5F6D0` | 54 | UnwindData |  |
| 389 | `_isctype_l` | `0x5F7A0` | 269 | UnwindData |  |
| 1773 | `_set_controlfp` | `0x5FB60` | 54 | UnwindData |  |
| 195 | `_controlfp_s` | `0x5FBA0` | 105 | UnwindData |  |
| 1759 | `_rmtmp` | `0x60090` | 167 | UnwindData |  |
| 244 | `_fclose_nolock` | `0x60140` | 85 | UnwindData |  |
| 1736 | `_pipe` | `0x60350` | 752 | UnwindData |  |
| 617 | `_mbsnicmp_l` | `0x60650` | 444 | UnwindData |  |
| 1735 | `_pclose` | `0x60880` | 220 | UnwindData |  |
| 208 | `_cwait` | `0x60970` | 178 | UnwindData |  |
| 2373 | `setvbuf` | `0x60E50` | 90 | UnwindData |  |
| 188 | `_close` | `0x61110` | 85 | UnwindData |  |
| 2170 | `fclose` | `0x61170` | 85 | UnwindData |  |
| 245 | `_fcloseall` | `0x61530` | 201 | UnwindData |  |
| 2205 | `fopen_s` | `0x61AD0` | 90 | UnwindData |  |
| 1971 | `_wfopen_s` | `0x61B30` | 90 | UnwindData |  |
| 1793 | `_sopen_s` | `0x61EE0` | 50 | UnwindData |  |
| 593 | `_mbsnbicmp_l` | `0x62370` | 170 | UnwindData |  |
| 1826 | `_strnicmp` | `0x62420` | 139 | UnwindData |  |
| 2428 | `tmpnam_s` | `0x626E0` | 59 | UnwindData |  |
| 142 | `_access` | `0x62CF0` | 18 | UnwindData |  |
| 143 | `_access_s` | `0x62D10` | 149 | UnwindData |  |
| 1892 | `_waccess` | `0x62DB0` | 18 | UnwindData |  |
| 1893 | `_waccess_s` | `0x62DD0` | 189 | UnwindData |  |
| 1952 | `_wdupenv_s` | `0x630B0` | 14 | UnwindData |  |
| 631 | `_mbsrchr_l` | `0x633F0` | 273 | UnwindData |  |
| 2401 | `strrchr` | `0x63510` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `__dcrt_get_wide_environment_from_os` | `0x639F0` | 131 | UnwindData |  |
| 24 | `_W_Getdays` | `0x64430` | 521 | UnwindData |  |
| 25 | `_W_Getmonths` | `0x64820` | 872 | UnwindData |  |
| 2430 | `toupper` | `0x64D80` | 114 | UnwindData |  |
| 1008 | `_o__itow_s` | `0x64F10` | 27 | UnwindData |  |
| 481 | `_itow_s` | `0x64FB0` | 64 | UnwindData |  |
| 1874 | `_ultoa` | `0x65460` | 35 | UnwindData |  |
| 478 | `_itoa` | `0x65490` | 50 | UnwindData |  |
| 1525 | `_o_free` | `0x65970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | `_o___stdio_common_vsnprintf_s` | `0x65990` | 60 | UnwindData |  |
| 116 | `__stdio_common_vsnprintf_s` | `0x65A70` | 136 | UnwindData |  |
| 1907 | `_wcsicmp_l` | `0x65EC0` | 55 | UnwindData |  |
| 1876 | `_ultow` | `0x66770` | 35 | UnwindData |  |
| 480 | `_itow` | `0x66800` | 48 | UnwindData |  |
| 518 | `_ltow` | `0x66800` | 48 | UnwindData |  |
| 1042 | `_o__ltow_s` | `0x66950` | 27 | UnwindData |  |
| 519 | `_ltow_s` | `0x669E0` | 34 | UnwindData |  |
| 1344 | `_o__wcsnicmp` | `0x66B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1600 | `_o_malloc` | `0x66B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2448 | `wcscpy_s` | `0x66BB0` | 129 | UnwindData |  |
| 2260 | `iswxdigit` | `0x67000` | 109 | UnwindData |  |
| 1307 | `_o__ultow_s` | `0x68630` | 27 | UnwindData |  |
| 1877 | `_ultow_s` | `0x686D0` | 63 | UnwindData |  |
| 2248 | `iswalpha` | `0x68820` | 109 | UnwindData |  |
| 210 | `_dclass` | `0x688F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 487 | `_ldclass` | `0x688F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `_dtest` | `0x68960` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `_ldtest` | `0x68960` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `_o__msize` | `0x689C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `__stdio_common_vswprintf_p` | `0x689D0` | 124 | UnwindData |  |
| 144 | `_aligned_free` | `0x6A800` | 27 | UnwindData |  |
| 145 | `_aligned_malloc` | `0x6A830` | 23 | UnwindData |  |
| 146 | `_aligned_msize` | `0x6A8D0` | 101 | UnwindData |  |
| 150 | `_aligned_realloc` | `0x6A940` | 144 | UnwindData |  |
| 151 | `_aligned_recalloc` | `0x6AB50` | 622 | UnwindData |  |
| 147 | `_aligned_offset_malloc` | `0x6ADD0` | 204 | UnwindData |  |
| 243 | `_expand` | `0x6AFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1940 | `_wcsupr` | `0x6AFF0` | 100 | UnwindData |  |
| 1943 | `_wcsupr_s_l` | `0x6B060` | 75 | UnwindData |  |
| 1889 | `_unlock_locales` | `0x6BB70` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1566 | `_o_iswspace` | `0x6BD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2458 | `wcspbrk` | `0x6BDA0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `_isnan` | `0x6BE30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1702 | `_o_towlower` | `0x6BE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1703 | `_o_towupper` | `0x6BE90` | 2,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `_o__ui64tow_s` | `0x6C6A0` | 28 | UnwindData |  |
| 1873 | `_ui64tow_s` | `0x6C740` | 52 | UnwindData |  |
| 1334 | `_o__wcsicmp` | `0x6C880` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1611 | `_o_memcpy_s` | `0x6CA30` | 28 | UnwindData |  |
| 2463 | `wcsstr` | `0x6CB70` | 561 | UnwindData |  |
| 463 | `_iswalpha_l` | `0x6CDB0` | 109 | UnwindData |  |
| 476 | `_iswxdigit_l` | `0x6E060` | 109 | UnwindData |  |
| 2284 | `log2f` | `0x6E480` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1678 | `_o_strncat_s` | `0x6E560` | 35 | UnwindData |  |
| 1679 | `_o_strncpy_s` | `0x6E590` | 35 | UnwindData |  |
| 2479 | `wctomb` | `0x6E640` | 148 | UnwindData |  |
| 54 | `___mb_cur_max_func` | `0x6E740` | 90 | UnwindData |  |
| 2276 | `localeconv` | `0x6F6E0` | 98 | UnwindData |  |
| 2259 | `iswupper` | `0x6F7C0` | 107 | UnwindData |  |
| 372 | `_i64tow` | `0x6F840` | 51 | UnwindData |  |
| 1872 | `_ui64tow` | `0x6F880` | 35 | UnwindData |  |
| 1264 | `_o__strnicmp` | `0x6F9E0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `_ld_int` | `0x6FDB0` | 1,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `_get_daylight` | `0x70450` | 66 | UnwindData |  |
| 77 | `__isascii` | `0x704A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2039 | `abs` | `0x704C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2262 | `labs` | `0x704C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `_get_dstbias` | `0x704D0` | 66 | UnwindData |  |
| 932 | `_o__i64tow_s` | `0x70520` | 28 | UnwindData |  |
| 373 | `_i64tow_s` | `0x705B0` | 35 | UnwindData |  |
| 1511 | `_o_floorf` | `0x70740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `_lock_file` | `0x70760` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `_initterm` | `0x707A0` | 56 | UnwindData |  |
| 259 | `_fdtest` | `0x707E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2451 | `wcslen` | `0x70830` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `_ecvt` | `0x70940` | 92 | UnwindData |  |
| 247 | `_fcvt_s` | `0x70A40` | 122 | UnwindData |  |
| 246 | `_fcvt` | `0x70AC0` | 92 | UnwindData |  |
| 562 | `_mbscspn_l` | `0x71260` | 275 | UnwindData |  |
| 2389 | `strcspn` | `0x71380` | 70 | UnwindData |  |
| 556 | `_mbscmp_l` | `0x71730` | 376 | UnwindData |  |
| 1639 | `_o_realloc` | `0x718B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `_ecvt_s` | `0x718D0` | 686 | UnwindData |  |
| 224 | `_dup2` | `0x71B90` | 85 | UnwindData |  |
| 2153 | `div` | `0x72300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2264 | `ldiv` | `0x72300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2112 | `clock` | `0x72320` | 131 | UnwindData |  |
| 1700 | `_o_tolower` | `0x723B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1335 | `_o__wcsicmp_l` | `0x723D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1730 | `_o_wctomb_s` | `0x723F0` | 29 | UnwindData |  |
| 2480 | `wctomb_s` | `0x72480` | 91 | UnwindData |  |
| 565 | `_mbsdup` | `0x724F0` | 158 | UnwindData |  |
| 1812 | `_strdup` | `0x724F0` | 158 | UnwindData |  |
| 1701 | `_o_toupper` | `0x72610` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `_difftime64` | `0x72680` | 46 | UnwindData |  |
| 2315 | `modf` | `0x72710` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1996 | `_wsetlocale` | `0x72830` | 60 | UnwindData |  |
| 388 | `_isctype` | `0x72880` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1888 | `_unlock_file` | `0x728C0` | 2,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2449 | `wcscspn` | `0x731B0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `_o__ltoa` | `0x733B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2316 | `modff` | `0x73420` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `_mbsinc` | `0x735D0` | 14 | UnwindData |  |
| 2247 | `iswalnum` | `0x73780` | 103 | UnwindData |  |
| 216 | `_dpcomp` | `0x737F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `__strncnt` | `0x73870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2041 | `acosf` | `0x73890` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `_iswupper_l` | `0x73AD0` | 107 | UnwindData |  |
| 170 | `_byteswap_ushort` | `0x73B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1720 | `_o_wcstok_s` | `0x73B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `_ismbblead` | `0x73B80` | 64 | UnwindData |  |
| 1980 | `_wmakepath` | `0x73BD0` | 39 | UnwindData |  |
| 56 | `__acrt_iob_func` | `0x73DE0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2024 | `_wtoi` | `0x73F40` | 112 | UnwindData |  |
| 2028 | `_wtol` | `0x73F40` | 112 | UnwindData |  |
| 1568 | `_o_iswxdigit` | `0x73FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1532 | `_o_fwrite` | `0x73FE0` | 35 | UnwindData |  |
| 1866 | `_toupper_l` | `0x74090` | 363 | UnwindData |  |
| 462 | `_iswalnum_l` | `0x74210` | 103 | UnwindData |  |
| 725 | `_o___stdio_common_vsprintf` | `0x74280` | 55 | UnwindData |  |
| 727 | `_o___stdio_common_vsprintf_s` | `0x742C0` | 55 | UnwindData |  |
| 1553 | `_o_isspace` | `0x74300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `_lrotl` | `0x74320` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1760 | `_rotl` | `0x74320` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2469 | `wcstol` | `0x743A0` | 114 | UnwindData |  |
| 1556 | `_o_iswalpha` | `0x74420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `_o__stricmp` | `0x74440` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1477 | `_o_calloc` | `0x744A0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 567 | `_mbsicmp_l` | `0x74580` | 737 | UnwindData |  |
| 1817 | `_stricmp_l` | `0x74870` | 161 | UnwindData |  |
| 2197 | `fmaxf` | `0x74970` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `_byteswap_ulong` | `0x74A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `_o_floor` | `0x74A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2403 | `strstr` | `0x74A40` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `_initterm_e` | `0x74C60` | 148 | UnwindData |  |
| 2200 | `fminf` | `0x74EA0` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1523 | `_o_fread` | `0x75300` | 35 | UnwindData |  |
| 574 | `_mbslwr` | `0x75330` | 43 | UnwindData |  |
| 577 | `_mbslwr_s_l` | `0x75370` | 792 | UnwindData |  |
| 2345 | `rand_s` | `0x756E0` | 71 | UnwindData |  |
| 2052 | `atan` | `0x75790` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2215 | `frexp` | `0x75A40` | 280 | UnwindData |  |
| 1726 | `_o_wcstoul` | `0x75B60` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | `_o__hypotf` | `0x76260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2253 | `iswdigit` | `0x76280` | 100 | UnwindData |  |
| 1670 | `_o_sqrtf` | `0x762F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1544 | `_o_isalpha` | `0x76310` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2333 | `pow` | `0x766E0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2169 | `fabs` | `0x76970` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2419 | `tanh` | `0x769F0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1547 | `_o_isdigit` | `0x76DC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `_ldpcomp` | `0x76E20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1870 | `_ui64toa` | `0x76EA0` | 35 | UnwindData |  |
| 370 | `_i64toa` | `0x76ED0` | 51 | UnwindData |  |
| 1569 | `_o_isxdigit` | `0x76FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `_fpclass` | `0x77010` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1653 | `_o_roundf` | `0x770B0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `_o__register_onexit_function` | `0x77170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `_byteswap_uint64` | `0x77190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1499 | `_o_expf` | `0x771A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2209 | `fputws` | `0x771C0` | 195 | UnwindData |  |
| 367 | `_heapwalk` | `0x77D60` | 204 | UnwindData |  |
| 1481 | `_o_ceilf` | `0x77E90` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2455 | `wcsncpy` | `0x78130` | 532 | UnwindData |  |
| 1543 | `_o_isalnum` | `0x78850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `_o_logf` | `0x78870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1711 | `_o_wcscpy_s` | `0x78890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 939 | `_o__isctype` | `0x788B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `_o_fgetc` | `0x78950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `_lrotr` | `0x78970` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1762 | `_rotr` | `0x78970` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 809 | `_o__errno` | `0x78D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2055 | `atanf` | `0x78D20` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2404 | `strtod` | `0x790A0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2410 | `strtold` | `0x790A0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `_crt_atexit` | `0x792E0` | 76 | UnwindData |  |
| 1223 | `_o__set_errno` | `0x79340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2468 | `wcstok_s` | `0x79360` | 56 | UnwindData |  |
| 2442 | `wcscat` | `0x793A0` | 301 | UnwindData |  |
| 2447 | `wcscpy` | `0x794E0` | 317 | UnwindData |  |
| 1666 | `_o_sinf` | `0x79630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `_o___stdio_common_vswscanf` | `0x79650` | 48 | UnwindData |  |
| 125 | `__stdio_common_vswscanf` | `0x79710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1552 | `_o_ispunct` | `0x79720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `_initialize_onexit_table` | `0x79740` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `_o_lrintf` | `0x79770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1839 | `_strtoi64` | `0x79790` | 116 | UnwindData |  |
| 2406 | `strtoimax` | `0x79790` | 116 | UnwindData |  |
| 2411 | `strtoll` | `0x79790` | 116 | UnwindData |  |
| 660 | `_memicmp` | `0x79870` | 124 | UnwindData |  |
| 1485 | `_o_cosf` | `0x79900` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1554 | `_o_isupper` | `0x79A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `_o_log` | `0x79A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2163 | `exp2f` | `0x79A70` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2346 | `realloc` | `0x79BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1627 | `_o_pow` | `0x79BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1361 | `_o__wcstoui64` | `0x79C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1727 | `_o_wcstoull` | `0x79C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `_gmtime64` | `0x79C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | `_o__i64toa_s` | `0x79C40` | 28 | UnwindData |  |
| 1301 | `_o__ui64toa_s` | `0x79CD0` | 28 | UnwindData |  |
| 371 | `_i64toa_s` | `0x79D60` | 35 | UnwindData |  |
| 1871 | `_ui64toa_s` | `0x79D90` | 19 | UnwindData |  |
| 1354 | `_o__wcstoi64` | `0x79E40` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1723 | `_o_wcstoll` | `0x79E40` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `_o__ecvt_s` | `0x79EB0` | 55 | UnwindData |  |
| 739 | `_o__aligned_malloc` | `0x7A070` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `_beginthread` | `0x7A0F0` | 177 | UnwindData |  |
| 760 | `_o__beginthreadex` | `0x7A1B0` | 46 | UnwindData |  |
| 167 | `_beginthreadex` | `0x7A260` | 189 | UnwindData |  |
| 1708 | `_o_wcscat_s` | `0x7A390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `_makepath` | `0x7A3B0` | 39 | UnwindData |  |
| 564 | `_mbsdec_l` | `0x7A570` | 167 | UnwindData |  |
| 1555 | `_o_iswalnum` | `0x7A620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1401 | `_o__wmakepath_s` | `0x7A640` | 48 | UnwindData |  |
| 1981 | `_wmakepath_s` | `0x7A700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1860 | `_time64` | `0x7A710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1859 | `_time32` | `0x7A720` | 120 | UnwindData |  |
| 1669 | `_o_sqrt` | `0x7A7E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2307 | `mbtowc` | `0x7A860` | 85 | UnwindData |  |
| 193 | `_control87` | `0x7A8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1665 | `_o_sin` | `0x7A8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `_o___stdio_common_vfwprintf` | `0x7A8F0` | 45 | UnwindData |  |
| 721 | `_o___stdio_common_vfwprintf_s` | `0x7A930` | 45 | UnwindData |  |
| 884 | `_o__get_errno` | `0x7A9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2123 | `copysignf` | `0x7AA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 893 | `_o__get_stream_buffer_pointers` | `0x7AA20` | 28 | UnwindData |  |
| 330 | `_get_stream_buffer_pointers` | `0x7AAB0` | 71 | UnwindData |  |
| 682 | `_o____lc_locale_name_func` | `0x7AB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2313 | `memmove_s` | `0x7AB20` | 81 | UnwindData |  |
| 738 | `_o__aligned_free` | `0x7AB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1436 | `_o__wtoi` | `0x7ABA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1583 | `_o_log10f` | `0x7ABC0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 647 | `_mbstok_s_l` | `0x7AD20` | 483 | UnwindData |  |
| 2408 | `strtok_s` | `0x7AF70` | 57 | UnwindData |  |
| 1788 | `_setmode` | `0x7B180` | 338 | UnwindData |  |
| 1820 | `_strlwr` | `0x7B3C0` | 94 | UnwindData |  |
| 1823 | `_strlwr_s_l` | `0x7B430` | 75 | UnwindData |  |
| 306 | `_ftime64` | `0x7B850` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `_ftime64_s` | `0x7B850` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1279 | `_o__strtoui64` | `0x7BB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1688 | `_o_strtoull` | `0x7BB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1567 | `_o_iswupper` | `0x7BB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2208 | `fputwc` | `0x7BB40` | 87 | UnwindData |  |
| 680 | `_o____lc_codepage_func` | `0x7BC40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 718 | `_o___stdio_common_vfscanf` | `0x7BCA0` | 45 | UnwindData |  |
| 715 | `_o___stdio_common_vfprintf` | `0x7BCE0` | 45 | UnwindData |  |
| 2022 | `_wtof` | `0x7BE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `_o__wcslwr` | `0x7BE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1784 | `_set_thread_local_invalid_parameter_handler` | `0x7BE30` | 37 | UnwindData |  |
| 639 | `_mbsspn_l` | `0x7BE60` | 117 | UnwindData |  |
| 2402 | `strspn` | `0x7BEE0` | 1,263 | UnwindData |  |
| 1684 | `_o_strtol` | `0x7C470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `_o____mb_cur_max_func` | `0x7C490` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1663 | `_o_setlocale` | `0x7C5E0` | 1,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `_gmtime64_s` | `0x7CB60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2196 | `fmax` | `0x7CB70` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 934 | `_o__initialize_onexit_table` | `0x7CBF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1561 | `_o_iswdigit` | `0x7CC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2298 | `mblen` | `0x7CC70` | 85 | UnwindData |  |
| 134 | `__unDName` | `0x7D4E0` | 39 | UnwindData |  |
| 135 | `__unDNameEx` | `0x7D510` | 183 | UnwindData |  |
| 1674 | `_o_strcpy_s` | `0x7EFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2199 | `fmin` | `0x7EFE0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `_clearfp` | `0x7F1B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `_o__recalloc` | `0x7F220` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `_o___stdio_common_vsscanf` | `0x7F380` | 48 | UnwindData |  |
| 121 | `__stdio_common_vsscanf` | `0x7F440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `_fdsign` | `0x7F450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1559 | `_o_iswcntrl` | `0x7F460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2198 | `fmaxl` | `0x7F480` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2162 | `exp2` | `0x7F500` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `_o__calloc_base` | `0x7F660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1480 | `_o_ceil` | `0x7F680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `_o__gcvt_s` | `0x7F6A0` | 28 | UnwindData |  |
| 312 | `_gcvt` | `0x7F790` | 44 | UnwindData |  |
| 313 | `_gcvt_s` | `0x7F7D0` | 90 | UnwindData |  |
| 1628 | `_o_powf` | `0x7FA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1582 | `_o_log10` | `0x7FA20` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `_create_locale` | `0x7FA90` | 119 | UnwindData |  |
| 1721 | `_o_wcstol` | `0x7FB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1637 | `_o_rand` | `0x7FB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2201 | `fminl` | `0x7FB50` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1808 | `_statusfp` | `0x7FBD0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 858 | `_o__free_base` | `0x7FC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `_isleadbyte_l` | `0x7FC60` | 75 | UnwindData |  |
| 850 | `_o__fpclass` | `0x7FCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1778 | `_set_invalid_parameter_handler` | `0x7FCE0` | 107 | UnwindData |  |
| 469 | `_iswdigit_l` | `0x7FD60` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1528 | `_o_frexp` | `0x7FE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1850 | `_strupr` | `0x7FE80` | 58 | UnwindData |  |
| 1853 | `_strupr_s_l` | `0x7FEC0` | 75 | UnwindData |  |
| 1546 | `_o_iscntrl` | `0x802F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1045 | `_o__malloc_base` | `0x80310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `_localtime64_s` | `0x80330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1340 | `_o__wcslwr_s` | `0x80340` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1031 | `_o__lock_file` | `0x803B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1318 | `_o__unlock_file` | `0x803D0` | 1,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `_o__aligned_offset_malloc` | `0x80840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1985 | `_wopen` | `0x80860` | 35 | UnwindData |  |
| 1560 | `_o_iswctype` | `0x80950` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1734 | `_open_osfhandle` | `0x809C0` | 275 | UnwindData |  |
| 1652 | `_o_round` | `0x80E30` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2220 | `getc` | `0x810A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2233 | `imaxdiv` | `0x810B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 657 | `_mbsupr_s_l` | `0x810E0` | 758 | UnwindData |  |
| 2179 | `feof` | `0x813E0` | 44 | UnwindData |  |
| 1041 | `_o__ltow` | `0x81420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1680 | `_o_strtod` | `0x81440` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1685 | `_o_strtold` | `0x81440` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 668 | `_mktime64` | `0x81770` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `_atoi64` | `0x81A40` | 114 | UnwindData |  |
| 2062 | `atoll` | `0x81A40` | 114 | UnwindData |  |
| 1484 | `_o_cos` | `0x81AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 811 | `_o__execute_onexit_table` | `0x81AE0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1472 | `_o_atol` | `0x81E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `_get_fmode` | `0x81E40` | 61 | UnwindData |  |
| 2381 | `srand` | `0x82960` | 22 | UnwindData |  |
| 1495 | `_o_exp` | `0x82980` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1536 | `_o_getenv_s` | `0x82BB0` | 28 | UnwindData |  |
| 2223 | `getenv_s` | `0x82C40` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1163 | `_o__mbsstr` | `0x82CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `_lseek` | `0x82CF0` | 85 | UnwindData |  |
| 709 | `_o___pctype_func` | `0x82D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `_iswcntrl_l` | `0x82D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2251 | `iswcntrl` | `0x82D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1437 | `_o__wtoi64` | `0x82D80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1442 | `_o__wtoll` | `0x82D80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2127 | `cosh` | `0x82E10` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1992 | `_write` | `0x830A0` | 85 | UnwindData |  |
| 823 | `_o__fdclass` | `0x83100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `_ismbcspace_l` | `0x83110` | 84 | UnwindData |  |
| 2335 | `putc` | `0x83170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `_nextafterf` | `0x83180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2324 | `nextafterf` | `0x83180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `_dsign` | `0x83190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `_ldsign` | `0x83190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `_fwrite_nolock` | `0x831A0` | 92 | UnwindData |  |
| 2180 | `ferror` | `0x83220` | 44 | UnwindData |  |
| 681 | `_o____lc_collate_cp_func` | `0x83F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `_o__realloc_base` | `0x83F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1855 | `_swab` | `0x83F80` | 90 | UnwindData |  |
| 1458 | `_o_asin` | `0x83FE0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2465 | `wcstof` | `0x84180` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `_o__dclass` | `0x842A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `_o__ldclass` | `0x842A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `_o__wcsdup` | `0x842B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1306 | `_o__ultow` | `0x842D0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1693 | `_o_tanhf` | `0x843A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | `_o___std_type_info_destroy_list` | `0x843C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2027 | `_wtoi_l` | `0x843D0` | 122 | UnwindData |  |
| 2029 | `_wtol_l` | `0x843D0` | 122 | UnwindData |  |
| 133 | `__tzname` | `0x84450` | 25 | UnwindData |  |
| 2304 | `mbsrtowcs_s` | `0x844F0` | 122 | UnwindData |  |
| 2398 | `strncpy_s` | `0x847F0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2374 | `signal` | `0x849E0` | 540 | UnwindData |  |
| 217 | `_dpoly` | `0x84CA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1360 | `_o__wcstombs_s_l` | `0x84CD0` | 48 | UnwindData |  |
| 1367 | `_o__wcsupr_s` | `0x84D10` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `_get_heap_handle` | `0x84EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1297 | `_o__towlower_l` | `0x84EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2059 | `atof` | `0x84EE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `_mbstrlen` | `0x84F40` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1580 | `_o_localeconv` | `0x851D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1974 | `_wfsopen` | `0x85240` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1516 | `_o_fmodf` | `0x85890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 555 | `_mbscmp` | `0x858B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `_o___std_exception_destroy` | `0x858C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1908 | `_wcsicoll` | `0x858D0` | 70 | UnwindData |  |
| 672 | `_o__Getdays` | `0x85920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `_configthreadlocale` | `0x85940` | 107 | UnwindData |  |
| 2383 | `strcat_s` | `0x859C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 678 | `_o__W_Gettnames` | `0x859D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1672 | `_o_strcat_s` | `0x859F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 673 | `_o__Getmonths` | `0x85A50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1395 | `_o__wfullpath` | `0x85A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2269 | `lldiv` | `0x85AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 661 | `_memicmp_l` | `0x85AD0` | 154 | UnwindData |  |
| 354 | `_getwc_nolock` | `0x85B70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `_o___std_type_info_name` | `0x85BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `_o___acrt_iob_func` | `0x85BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `_mkgmtime64` | `0x85BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1465 | `_o_atan2f` | `0x85C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 711 | `_o___std_exception_copy` | `0x85C20` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `_commit` | `0x85CB0` | 140 | UnwindData |  |
| 1087 | `_o__mbsicmp` | `0x85E40` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2446 | `wcscoll` | `0x85ED0` | 101 | UnwindData |  |
| 1440 | `_o__wtol` | `0x85F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1671 | `_o_srand` | `0x85F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2378 | `sinhf` | `0x85F70` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1339 | `_o__wcslwr_l` | `0x86180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `_iswlower_l` | `0x861A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2255 | `iswlower` | `0x861A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1077 | `_o__mbscmp` | `0x861B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2111 | `clearerr_s` | `0x861D0` | 206 | UnwindData |  |
| 2326 | `nexttoward` | `0x862B0` | 315 | UnwindData |  |
| 1772 | `_set_app_type` | `0x86430` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `_ismbclower_l` | `0x86580` | 93 | UnwindData |  |
| 642 | `_mbsstr` | `0x865F0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1687 | `_o_strtoul` | `0x86700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 677 | `_o__W_Getmonths` | `0x86720` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `_iswblank_l` | `0x867C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2250 | `iswblank` | `0x867C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2299 | `mbrlen` | `0x867E0` | 125 | UnwindData |  |
| 784 | `_o__crt_atexit` | `0x868F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1638 | `_o_rand_s` | `0x86900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 676 | `_o__W_Getdays` | `0x86910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1434 | `_o__wtof` | `0x86930` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1925 | `_wcstod_l` | `0x869B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1931 | `_wcstold_l` | `0x869B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `_o__Gettnames` | `0x869C0` | 3,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1747 | `_putwch_nolock` | `0x87590` | 82 | UnwindData |  |
| 199 | `_cputws` | `0x87690` | 205 | UnwindData |  |
| 1184 | `_o__mkgmtime64` | `0x877C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `_o__mbslwr_s` | `0x877E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1777 | `_set_fmode` | `0x87800` | 73 | UnwindData |  |
| 1328 | `_o__wcreate_locale` | `0x87850` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2405 | `strtof` | `0x87B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1464 | `_o_atan2` | `0x87B50` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2464 | `wcstod` | `0x87BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2470 | `wcstold` | `0x87BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1466 | `_o_atanf` | `0x87BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1471 | `_o_atoi` | `0x87C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `_iswprint_l` | `0x87C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2256 | `iswprint` | `0x87C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `_dup` | `0x87C30` | 85 | UnwindData |  |
| 2228 | `hypot` | `0x87FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `_fdpcomp` | `0x88000` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 891 | `_o__get_osfhandle` | `0x88050` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 924 | `_o__gmtime64_s` | `0x88090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `_ldpoly` | `0x880B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2317 | `nan` | `0x880E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2319 | `nanl` | `0x880E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2467 | `wcstok` | `0x880F0` | 57 | UnwindData |  |
| 2407 | `strtok` | `0x88190` | 46 | UnwindData |  |
| 1091 | `_o__mbsinc` | `0x881D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1463 | `_o_atan` | `0x881E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `_mbccpy_s` | `0x88200` | 20 | UnwindData |  |
| 531 | `_mbccpy_s_l` | `0x88220` | 204 | UnwindData |  |
| 71 | `__dstbias` | `0x88300` | 25 | UnwindData |  |
| 859 | `_o__free_locale` | `0x883C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 573 | `_mbslen_l` | `0x883D0` | 112 | UnwindData |  |
| 2122 | `copysign` | `0x88450` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2124 | `copysignl` | `0x88450` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1912 | `_wcslwr_s` | `0x884A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `_ldunscale` | `0x884B0` | 216 | UnwindData |  |
| 67 | `__daylight` | `0x885E0` | 25 | UnwindData |  |
| 1564 | `_o_iswprint` | `0x88600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 783 | `_o__create_locale` | `0x88620` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `_Getdays` | `0x886A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1989 | `_wputenv_s` | `0x886B0` | 56 | UnwindData |  |
| 131 | `__timezone` | `0x889F0` | 25 | UnwindData |  |
| 2355 | `rewind` | `0x88A10` | 78 | UnwindData |  |
| 566 | `_mbsicmp` | `0x88B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `_mbsnbcmp_l` | `0x88B80` | 333 | UnwindData |  |
| 2354 | `rename` | `0x88CE0` | 263 | UnwindData |  |
| 1991 | `_wrename` | `0x88DF0` | 45 | UnwindData |  |
| 351 | `_getpid` | `0x88EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1470 | `_o_atof` | `0x88EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2142 | `csinhl` | `0x88ED0` | 558 | UnwindData |  |
| 14 | `_Getmonths` | `0x89550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1879 | `_umask_s` | `0x89560` | 61 | UnwindData |  |
| 1809 | `_strcoll_l` | `0x895B0` | 228 | UnwindData |  |
| 1030 | `_o__localtime64_s` | `0x896A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2249 | `iswascii` | `0x896C0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `_o__memicmp` | `0x89770` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2188 | `fgets` | `0x897F0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2452 | `wcsncat` | `0x89990` | 782 | UnwindData |  |
| 1733 | `_open` | `0x89D00` | 35 | UnwindData |  |
| 322 | `_get_initial_narrow_environment` | `0x89DF0` | 35 | UnwindData |  |
| 86 | `__p__commode` | `0x89E20` | 6,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1598 | `_o_lroundf` | `0x8B710` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2241 | `isleadbyte` | `0x8B7A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1922 | `_wcsrev` | `0x8B7B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1587 | `_o_log2` | `0x8B800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `_abs64` | `0x8B820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2232 | `imaxabs` | `0x8B820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2268 | `llabs` | `0x8B820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1365 | `_o__wcsupr` | `0x8B840` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2368 | `set_terminate` | `0x8C210` | 44 | UnwindData |  |
| 1504 | `_o_fflush` | `0x8C250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `_kbhit` | `0x8C270` | 48 | UnwindData |  |
| 2478 | `wctob` | `0x8C550` | 469 | UnwindData |  |
| 1399 | `_o__wgetenv_s` | `0x8C780` | 28 | UnwindData |  |
| 1979 | `_wgetenv_s` | `0x8C810` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1597 | `_o_lround` | `0x8CE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1599 | `_o_lroundl` | `0x8CE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1718 | `_o_wcstof` | `0x8CE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2350 | `remove` | `0x8CE40` | 143 | UnwindData |  |
| 1394 | `_o__wfsopen` | `0x8CEE0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `_difftime32` | `0x8CF50` | 43 | UnwindData |  |
| 2106 | `cexpl` | `0x8CF90` | 643 | UnwindData |  |
| 15 | `_Gettnames` | `0x8D220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1486 | `_o_cosh` | `0x8D230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `_o__set_app_type` | `0x8D250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2377 | `sinh` | `0x8D260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `_mbslwr_s` | `0x8D280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 667 | `_mktime32` | `0x8D290` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `_ismbcdigit_l` | `0x8D2F0` | 92 | UnwindData |  |
| 700 | `_o___p__commode` | `0x8D360` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1274 | `_o__strtoi64` | `0x8D3E0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `_o_strtoll` | `0x8D3E0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `_gmtime32_s` | `0x8D4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1846 | `_strtoui64_l` | `0x8D4B0` | 127 | UnwindData |  |
| 1848 | `_strtoull_l` | `0x8D4B0` | 127 | UnwindData |  |
| 1849 | `_strtoumax_l` | `0x8D4B0` | 127 | UnwindData |  |
| 1790 | `_sleep` | `0x8D540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `_gmtime32` | `0x8D560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `_chmod` | `0x8D570` | 149 | UnwindData |  |
| 1898 | `_wchmod` | `0x8D610` | 175 | UnwindData |  |
| 1501 | `_o_fclose` | `0x8D6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1551 | `_o_isprint` | `0x8D710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2217 | `fsetpos` | `0x8D730` | 53 | UnwindData |  |
| 839 | `_o__fileno` | `0x8D770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2222 | `getenv` | `0x8D790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `_fpreset` | `0x8D7A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2190 | `fgetws` | `0x8D820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1224 | `_o__set_fmode` | `0x8D830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `_localtime32_s` | `0x8D850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `_iswgraph_l` | `0x8D860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2254 | `iswgraph` | `0x8D860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1998 | `_wsopen_dispatch` | `0x8D870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1515 | `_o_fmod` | `0x8D880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `_mbsrchr` | `0x8D8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `_o_log2f` | `0x8D8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1692 | `_o_tanh` | `0x8D8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `_o__set_new_mode` | `0x8D8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `_ismbcspace` | `0x8D910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1942 | `_wcsupr_s` | `0x8D920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `_o__Wcsftime` | `0x8D930` | 38 | UnwindData |  |
| 323 | `_get_initial_wide_environment` | `0x8DB20` | 35 | UnwindData |  |
| 615 | `_mbsnextc_l` | `0x8DB50` | 141 | UnwindData |  |
| 1535 | `_o_getenv` | `0x8DC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 778 | `_o__configure_wide_argv` | `0x8DC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 659 | `_memccpy` | `0x8DC60` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1577 | `_o_llround` | `0x8DE10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1579 | `_o_llroundl` | `0x8DE10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2065 | `btowc` | `0x8DE70` | 155 | UnwindData |  |
| 1970 | `_wfopen` | `0x8DFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `_locking` | `0x8DFC0` | 321 | UnwindData |  |
| 209 | `_d_int` | `0x8E3D0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `_ismbcalpha_l` | `0x8E480` | 129 | UnwindData |  |
| 1188 | `_o__mktime64` | `0x8E510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1608 | `_o_mbstowcs` | `0x8E530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `__initialize_lconv_for_unsigned_char` | `0x8E550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `_mbschr` | `0x8E570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1677 | `_o_strftime` | `0x8E580` | 28 | UnwindData |  |
| 1654 | `_o_roundl` | `0x8E610` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 589 | `_mbsnbcpy_l` | `0x8E660` | 269 | UnwindData |  |
| 296 | `_fsopen` | `0x8E780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `_o__configthreadlocale` | `0x8E790` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1613 | `_o_modf` | `0x8EBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2173 | `fdiml` | `0x8EBE0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `_get_wide_winmain_command_line` | `0x8EC60` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1691 | `_o_tanf` | `0x8ED00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1878 | `_umask` | `0x8ED50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 935 | `_o__initialize_wide_environment` | `0x8ED70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `_controlfp` | `0x8ED90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1459 | `_o_asinf` | `0x8EDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2141 | `csinhf` | `0x8EDC0` | 427 | UnwindData |  |
| 1352 | `_o__wcstod_l` | `0x8F0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1357 | `_o__wcstold_l` | `0x8F0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `__sys_nerr` | `0x8F110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 898 | `_o__get_wide_winmain_command_line` | `0x8F120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2023 | `_wtof_l` | `0x8F140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 658 | `_mbtowc_l` | `0x8F150` | 96 | UnwindData |  |
| 1256 | `_o__stricoll` | `0x8F240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1769 | `_seh_filter_exe` | `0x8F260` | 178 | UnwindData |  |
| 2140 | `csinh` | `0x8F320` | 479 | UnwindData |  |
| 1792 | `_sopen_dispatch` | `0x91540` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `_iswpunct_l` | `0x91570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2257 | `iswpunct` | `0x91570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1494 | `_o_exit` | `0x91580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `_o__itow` | `0x915A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1982 | `_wmkdir` | `0x91610` | 41 | UnwindData |  |
| 248 | `_fd_int` | `0x91640` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2160 | `exit` | `0x91700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `__stdio_common_vfscanf` | `0x91710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1717 | `_o_wcstod` | `0x91720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1722 | `_o_wcstold` | `0x91720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `_o__gcvt` | `0x91740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1683 | `_o_strtok_s` | `0x91760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2286 | `logb` | `0x91780` | 195 | UnwindData |  |
| 2395 | `strncat_s` | `0x91850` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2074 | `cacoshf` | `0x918B0` | 805 | UnwindData |  |
| 127 | `__sys_errlist` | `0x91BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `_mbclen` | `0x91BF0` | 95 | UnwindData |  |
| 1990 | `_wremove` | `0x91C60` | 39 | UnwindData |  |
| 670 | `_nextafter` | `0x91C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2323 | `nextafter` | `0x91C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2325 | `nextafterl` | `0x91C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2328 | `nexttowardl` | `0x91C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `_o_ldexp` | `0x91CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `_initialize_narrow_environment` | `0x91CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `__p___argc` | `0x91CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `_o__mbstrlen` | `0x91CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `_mbsdec` | `0x91CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1776 | `_set_error_mode` | `0x91D00` | 71 | UnwindData |  |
| 277 | `_findnext64i32` | `0x91D50` | 45 | UnwindData |  |
| 836 | `_o__fgetwchar` | `0x91D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1540 | `_o_getwchar` | `0x91D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1250 | `_o__strdup` | `0x91DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `_flushall` | `0x91DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `_findclose` | `0x91DE0` | 37 | UnwindData |  |
| 265 | `_fgetwchar` | `0x91E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2227 | `getwchar` | `0x91E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 662 | `_mkdir` | `0x91E30` | 147 | UnwindData |  |
| 888 | `_o__get_initial_wide_environment` | `0x91ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2166 | `expm1` | `0x91EF0` | 315 | UnwindData |  |
| 2042 | `acosh` | `0x92040` | 224 | UnwindData |  |
| 777 | `_o__configure_narrow_argv` | `0x92130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1724 | `_o_wcstombs` | `0x92150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1756 | `_register_thread_local_exe_atexit_callback` | `0x92170` | 60 | UnwindData |  |
| 440 | `_ismbclower` | `0x921C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1758 | `_rmdir` | `0x921D0` | 143 | UnwindData |  |
| 1719 | `_o_wcstok` | `0x92270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `__p___wargv` | `0x92290` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 774 | `_o__close` | `0x927F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 698 | `_o___p___wargv` | `0x92810` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2012 | `_wstat64` | `0x92B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2171 | `fdim` | `0x92B10` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2013 | `_wstat64i32` | `0x92BE0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1774 | `_set_doserrno` | `0x92C30` | 40 | UnwindData |  |
| 543 | `_mbctolower_l` | `0x92C60` | 133 | UnwindData |  |
| 2085 | `casinhl` | `0x92CF0` | 843 | UnwindData |  |
| 192 | `_configure_wide_argv` | `0x93310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | `_o__difftime64` | `0x93320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `_o__tell` | `0x93340` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `__p__environ` | `0x93370` | 25 | UnwindData |  |
| 2391 | `strerror_s` | `0x93390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2231 | `ilogbl` | `0x933A0` | 159 | UnwindData |  |
| 2363 | `scalblnf` | `0x93450` | 364 | UnwindData |  |
| 1854 | `_strxfrm_l` | `0x935D0` | 478 | UnwindData |  |
| 790 | `_o__difftime32` | `0x93840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1856 | `_tell` | `0x93850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2172 | `fdimf` | `0x93870` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2453 | `wcsncat_s` | `0x938C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 923 | `_o__gmtime64` | `0x938D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 933 | `_o__initialize_narrow_environment` | `0x938F0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2484 | `wmemmove_s` | `0x939E0` | 82 | UnwindData |  |
| 2043 | `acoshf` | `0x93A40` | 195 | UnwindData |  |
| 196 | `_copysign` | `0x93B70` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2193 | `fma` | `0x93EF0` | 3,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2226 | `getwc` | `0x94B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1192 | `_o__open_osfhandle` | `0x94B80` | 3,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2348 | `remainderf` | `0x95820` | 627 | UnwindData |  |
| 656 | `_mbsupr_s` | `0x95AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `_initialize_wide_environment` | `0x95AB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `_o__dup2` | `0x95B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1565 | `_o_iswpunct` | `0x95B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2311 | `memcpy_s` | `0x95B70` | 130 | UnwindData |  |
| 2204 | `fopen` | `0x95C00` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2362 | `scalbln` | `0x95D30` | 424 | UnwindData |  |
| 2072 | `cacosf` | `0x96100` | 714 | UnwindData |  |
| 1681 | `_o_strtof` | `0x963D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1838 | `_strtof_l` | `0x963F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2288 | `logbl` | `0x96400` | 195 | UnwindData |  |
| 1509 | `_o_fgetws` | `0x964D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1743 | `_putenv_s` | `0x964F0` | 56 | UnwindData |  |
| 1452 | `_o_acosf` | `0x96530` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1807 | `_stat64i32` | `0x967A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2168 | `expm1l` | `0x967B0` | 311 | UnwindData |  |
| 528 | `_mbccpy` | `0x968F0` | 134 | UnwindData |  |
| 273 | `_findfirst64i32` | `0x96980` | 45 | UnwindData |  |
| 887 | `_o__get_initial_narrow_environment` | `0x969C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `_o__mktime32` | `0x969E0` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `__p___argv` | `0x97540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 697 | `_o___p___argv` | `0x97550` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2045 | `asctime` | `0x976A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2301 | `mbrtoc32` | `0x976B0` | 92 | UnwindData |  |
| 696 | `_o___p___argc` | `0x97720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2361 | `roundl` | `0x97740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1029 | `_o__localtime64` | `0x97750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `_fread_nolock` | `0x97770` | 29 | UnwindData |  |
| 801 | `_o__dup` | `0x977B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1862 | `_timespec64_get` | `0x977D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1863 | `_tolower` | `0x977E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `_o__get_narrow_winmain_command_line` | `0x977F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `_get_narrow_winmain_command_line` | `0x97810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1557 | `_o_iswascii` | `0x97820` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1346 | `_o__wcsnicoll` | `0x979C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `_makepath_s` | `0x979E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2229 | `ilogb` | `0x979F0` | 159 | UnwindData |  |
| 2370 | `setbuf` | `0x97AA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2482 | `wctype` | `0x97AD0` | 96 | UnwindData |  |
| 2037 | `_yn` | `0x97BC0` | 231 | UnwindData |  |
| 191 | `_configure_narrow_argv` | `0x97CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2046 | `asctime_s` | `0x97CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `_o_fputc` | `0x97CD0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1993 | `_wrmdir` | `0x980F0` | 39 | UnwindData |  |
| 582 | `_mbsnbcmp` | `0x98120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1293 | `_o__tolower` | `0x98130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1978 | `_wgetenv` | `0x98150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `_fstat64i32` | `0x98160` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1521 | `_o_fputwc` | `0x981E0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1837 | `_strtod_l` | `0x983B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1843 | `_strtold_l` | `0x983B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2285 | `log2l` | `0x983C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `__p__wenviron` | `0x983D0` | 25 | UnwindData |  |
| 1451 | `_o_acos` | `0x98460` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1857 | `_telli64` | `0x984E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `_o__strlwr` | `0x98500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2318 | `nanf` | `0x98520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `_ctime64_s` | `0x98530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1742 | `_putenv` | `0x98540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `_fdopen` | `0x98550` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `_ismbcdigit` | `0x98620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1924 | `_wcsset_s` | `0x98630` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 572 | `_mbslen` | `0x98AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2082 | `casinf` | `0x98AC0` | 78 | UnwindData |  |
| 807 | `_o__endthreadex` | `0x98D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1840 | `_strtoi64_l` | `0x98D60` | 127 | UnwindData |  |
| 1841 | `_strtoimax_l` | `0x98D60` | 127 | UnwindData |  |
| 1844 | `_strtoll_l` | `0x98D60` | 127 | UnwindData |  |
| 1225 | `_o__set_invalid_parameter_handler` | `0x98DF0` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2390 | `strerror` | `0x99510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `_localtime32` | `0x99520` | 72 | UnwindData |  |
| 88 | `__p__fmode` | `0x99570` | 25 | UnwindData |  |
| 1563 | `_o_iswlower` | `0x99590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | `_mbsnextc` | `0x995B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1822 | `_strlwr_s` | `0x995C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1852 | `_strupr_s` | `0x995D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `_ismbcalpha` | `0x995E0` | 2,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `_Cmulcc` | `0x9A020` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `_LCmulcc` | `0x9A020` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `_findfirst64` | `0x9A200` | 45 | UnwindData |  |
| 1506 | `_o_fgetpos` | `0x9A240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `_o__pipe` | `0x9A260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2110 | `clearerr` | `0x9A280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1610 | `_o_mbtowc` | `0x9A290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1415 | `_o__wsetlocale` | `0x9A2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `_o_fseek` | `0x9A2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `_o__setmode` | `0x9A2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1476 | `_o_btowc` | `0x9A300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `_mbscspn` | `0x9A310` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1690 | `_o_tan` | `0x9A7C0` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 733 | `_o___timezone` | `0x9B190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2386 | `strcoll` | `0x9B1B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `_o__dsign` | `0x9B1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1503 | `_o_ferror` | `0x9B1E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1787 | `_setmbcp` | `0x9B260` | 58 | UnwindData |  |
| 861 | `_o__fseeki64` | `0x9B3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1661 | `_o_set_terminate` | `0x9B3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `_mbsnbicmp` | `0x9B3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 628 | `_mbspbrk` | `0x9B3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1260 | `_o__strlwr_s` | `0x9B400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `_o__beginthread` | `0x9B420` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `_ctime64` | `0x9B5D0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1815 | `_strftime_l` | `0x9B7A0` | 30 | UnwindData |  |
| 1965 | `_wfindfirst64i32` | `0x9B7D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `_o___stdio_common_vswprintf_p` | `0x9B7E0` | 55 | UnwindData |  |
| 1507 | `_o_fgets` | `0x9B820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `_o__waccess` | `0x9B840` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1771 | `_set_abort_behavior` | `0x9B8B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1969 | `_wfindnext64i32` | `0x9B8E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2194 | `fmaf` | `0x9B960` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `_mbctolower` | `0x9BA90` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `_get_terminate` | `0x9BBD0` | 34 | UnwindData |  |
| 1398 | `_o__wgetenv` | `0x9BC00` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 775 | `_o__commit` | `0x9BCF0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `_FCbuild` | `0x9C130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `_get_tzname` | `0x9C140` | 236 | UnwindData |  |
| 1222 | `_o__set_doserrno` | `0x9C250` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `_fstat64` | `0x9C650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2108 | `cimagf` | `0x9C660` | 19 | UnwindData |  |
| 328 | `_get_printf_count_output` | `0x9C680` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `_o_feof` | `0x9C7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1520 | `_o_fputs` | `0x9C7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1246 | `_o__stat64i32` | `0x9C7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `_o__wmkdir` | `0x9C810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | `_mbsspn` | `0x9C830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `_ftime32` | `0x9C840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `_ftime32_s` | `0x9C840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `_get_current_locale` | `0x9C850` | 192 | UnwindData |  |
| 1988 | `_wputenv` | `0x9C920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 640 | `_mbsspnp` | `0x9C930` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `_fstat32i64` | `0x9CA50` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2164 | `exp2l` | `0x9CBC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1816 | `_stricmp` | `0x9CBD0` | 6,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `_cexit` | `0x9E510` | 181 | UnwindData |  |
| 2036 | `_y1` | `0x9E910` | 3,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `_getwche_nolock` | `0x9F6C0` | 83 | UnwindData |  |
| 1930 | `_wcstol_l` | `0x9FA80` | 125 | UnwindData |  |
| 342 | `_getche_nolock` | `0x9FD80` | 62 | UnwindData |  |
| 163 | `_atoldbl_l` | `0x9FEA0` | 234 | UnwindData |  |
| 1894 | `_wasctime` | `0xA04D0` | 122 | UnwindData |  |
| 2287 | `logbf` | `0xA0550` | 166 | UnwindData |  |
| 1891 | `_utime64` | `0xA09E0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `___mb_cur_max_l_func` | `0xA0A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 692 | `_o___conio_common_vcwscanf` | `0xA0A90` | 35 | UnwindData |  |
| 1886 | `_unlink` | `0xA0B30` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `_mbsrev_l` | `0xA0C20` | 269 | UnwindData |  |
| 1920 | `_wcsnset` | `0xA0DA0` | 3,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1806 | `_stat64` | `0xA1C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `_o__wputenv_s` | `0xA1C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1406 | `_o__wpopen` | `0xA1C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1348 | `_o__wcsnset` | `0xA1C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `_o__strupr_s` | `0xA1CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `_o__controlfp_s` | `0xA1CC0` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2005 | `_wspawnve` | `0xA1FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1614 | `_o_modff` | `0xA1FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1648 | `_o_rewind` | `0xA2010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1682 | `_o_strtok` | `0xA2030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1432 | `_o__wsystem` | `0xA2050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `_o__mbsbtype` | `0xA2070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1446 | `_o__wutime64` | `0xA2090` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 641 | `_mbsspnp_l` | `0xA22C0` | 263 | UnwindData |  |
| 2034 | `_wutime64` | `0xA2740` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `_mbsbtype` | `0xA27A0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2415 | `strxfrm` | `0xA28B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 646 | `_mbstok_s` | `0xA28C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 632 | `_mbsrev` | `0xA28D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 937 | `_o__invalid_parameter_noinfo_noreturn` | `0xA28E0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1968 | `_wfindnext64` | `0xA2A30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2032 | `_wunlink` | `0xA2AA0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `_fdsin` | `0xA2B60` | 298 | UnwindData |  |
| 1961 | `_wfdopen` | `0xA3110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1895 | `_wasctime_s` | `0xA3120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1948 | `_wctime64_s` | `0xA3130` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2119 | `conj` | `0xA3360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2121 | `conjl` | `0xA3360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2303 | `mbsrtowcs` | `0xA3390` | 92 | UnwindData |  |
| 148 | `_aligned_offset_realloc` | `0xA36B0` | 602 | UnwindData |  |
| 149 | `_aligned_offset_recalloc` | `0xA3910` | 784 | UnwindData |  |
| 552 | `_mbscat_s_l` | `0xA3D80` | 572 | UnwindData |  |
| 2167 | `expm1f` | `0xA4080` | 199 | UnwindData |  |
| 2017 | `_wstrtime_s` | `0xA41F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `_mbsncat_s_l` | `0xA4200` | 677 | UnwindData |  |
| 2120 | `conjf` | `0xA45D0` | 39 | UnwindData |  |
| 345 | `_getdiskfree` | `0xA49C0` | 196 | UnwindData |  |
| 2213 | `freopen` | `0xA4AF0` | 47 | UnwindData |  |
| 1526 | `_o_freopen` | `0xA4B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `_fdpoly` | `0xA4B50` | 1,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2038 | `abort` | `0xA5230` | 106 | UnwindData |  |
| 6 | `_Exit` | `0xA52A0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `_exit` | `0xA52A0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `__stdio_common_vfwscanf` | `0xA5340` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `_futime64` | `0xA5600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `_Cbuild` | `0xA5610` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `_LCbuild` | `0xA5610` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `_atof_l` | `0xA5820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `_mktemp` | `0xA5830` | 81 | UnwindData |  |
| 383 | `_isalnum_l` | `0xA5B10` | 24 | UnwindData |  |
| 384 | `_isalpha_l` | `0xA5BF0` | 24 | UnwindData |  |
| 390 | `_isdigit_l` | `0xA5CD0` | 20 | UnwindData |  |
| 1897 | `_wchdir` | `0xA5E50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2015 | `_wstrdate_s` | `0xA5EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1262 | `_o__strncoll` | `0xA5EC0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2078 | `carg` | `0xA6130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2080 | `cargl` | `0xA6130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1997 | `_wsopen` | `0xA6150` | 68 | UnwindData |  |
| 1904 | `_wcserror_s` | `0xA61A0` | 127 | UnwindData |  |
| 607 | `_mbsncmp_l` | `0xA6A50` | 320 | UnwindData |  |
| 181 | `_chdrive` | `0xA7110` | 129 | UnwindData |  |
| 153 | `_atodbl` | `0xA71F0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `_FCmulcc` | `0xA7460` | 74 | UnwindData |  |
| 2178 | `feholdexcept` | `0xA74E0` | 80 | UnwindData |  |
| 2136 | `crealf` | `0xA75F0` | 18 | UnwindData |  |
| 1125 | `_o__mbsnccnt` | `0xA7610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `_o__mbsrev_l` | `0xA7630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1259 | `_o__strlwr_l` | `0xA7650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2107 | `cimag` | `0xA7670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2109 | `cimagl` | `0xA7670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2135 | `creal` | `0xA7680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2137 | `creall` | `0xA7680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1309 | `_o__umask_s` | `0xA7690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1749 | `_query_app_type` | `0xA76A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `_mbsnbcpy` | `0xA76B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1994 | `_wsearchenv` | `0xA76C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1903 | `_wcserror` | `0xA76E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2125 | `cos` | `0xA7730` | 1,402 | UnwindData |  |
| 2126 | `cosf` | `0xA7F70` | 543 | UnwindData |  |
| 2161 | `exp` | `0xA81A0` | 1,045 | UnwindData |  |
| 2165 | `expf` | `0xA8740` | 346 | UnwindData |  |
| 2202 | `fmod` | `0xA8990` | 692 | UnwindData |  |
| 2277 | `log` | `0xA8C60` | 1,323 | UnwindData |  |
| 2278 | `log10` | `0xA91A0` | 1,451 | UnwindData |  |
| 2279 | `log10f` | `0xA9970` | 504 | UnwindData |  |
| 2289 | `logf` | `0xA9D40` | 460 | UnwindData |  |
| 2334 | `powf` | `0xA9F20` | 3,766 | UnwindData |  |
| 2347 | `remainder` | `0xAADF0` | 1,000 | UnwindData |  |
| 2360 | `roundf` | `0xAB9A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2359 | `round` | `0xAB9F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2375 | `sin` | `0xABA70` | 1,386 | UnwindData |  |
| 2376 | `sinf` | `0xAC360` | 845 | UnwindData |  |
| 2417 | `tan` | `0xACC70` | 1,459 | UnwindData |  |
| 2418 | `tanf` | `0xAD740` | 730 | UnwindData |  |
| 4 | `_CreateFrameInfo` | `0xAE510` | 58 | UnwindData |  |
| 10 | `_FindAndUnlinkFrame` | `0xAE550` | 83 | UnwindData |  |
| 11 | `_GetImageBase` | `0xAE5B0` | 18 | UnwindData |  |
| 12 | `_GetThrowImageBase` | `0xAE5D0` | 18 | UnwindData |  |
| 20 | `_SetImageBase` | `0xAE5F0` | 24 | UnwindData |  |
| 21 | `_SetThrowImageBase` | `0xAE610` | 24 | UnwindData |  |
| 35 | `__CxxFrameHandler` | `0xAE630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `__CxxFrameHandler2` | `0xAE630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `__CxxFrameHandler3` | `0xAE640` | 134 | UnwindData |  |
| 38 | `__CxxFrameHandler4` | `0xAE6D0` | 191 | UnwindData |  |
| 5 | `_CxxThrowException` | `0xAE7A0` | 166 | UnwindData |  |
| 42 | `__DestructExceptionObject` | `0xAE850` | 108 | UnwindData |  |
| 16 | `_IsExceptionObjectToBeDestroyed` | `0xAE8D0` | 47 | UnwindData |  |
| 22 | `_SetWinRTOutOfMemoryExceptionCallback` | `0xAE910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `__AdjustPointer` | `0xAE920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__FrameUnwindFilter` | `0xAE950` | 102 | UnwindData |  |
| 44 | `__GetPlatformExceptionInfo` | `0xAE9C0` | 91 | UnwindData |  |
| 65 | `__current_exception` | `0xAEA30` | 18 | UnwindData |  |
| 66 | `__current_exception_context` | `0xAEA50` | 18 | UnwindData |  |
| 96 | `__processing_throw` | `0xAEA70` | 18 | UnwindData |  |
| 103 | `__std_terminate` | `0xAEA90` | 10 | UnwindData |  |
| 382 | `_is_exception_typeof` | `0xAEAA0` | 165 | UnwindData |  |
| 29 | `__BuildCatchObject` | `0xB1C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `__BuildCatchObjectHelper` | `0xB1C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__TypeMatch` | `0xB1C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `__C_specific_handler` | `0xB1C80` | 535 | UnwindData |  |
| 32 | `__C_specific_handler_noexcept` | `0xB1EA0` | 75 | UnwindData |  |
| 33 | `__CxxDetectRethrow` | `0xB1F00` | 68 | UnwindData |  |
| 34 | `__CxxExceptionFilter` | `0xB1F50` | 503 | UnwindData |  |
| 39 | `__CxxQueryExceptionSize` | `0xB2150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__CxxRegisterExceptionObject` | `0xB2160` | 172 | UnwindData |  |
| 41 | `__CxxUnregisterExceptionObject` | `0xB2220` | 294 | UnwindData |  |
| 45 | `__NLG_Dispatch2` | `0xB2380` | 1 | UnwindData |  |
| 46 | `__NLG_Return2` | `0xB2390` | 1 | UnwindData |  |
| 47 | `__RTCastToVoid` | `0xB29B0` | 93 | UnwindData |  |
| 48 | `__RTDynamicCast` | `0xB2A20` | 366 | UnwindData |  |
| 49 | `__RTtypeid` | `0xB2BA0` | 180 | UnwindData |  |
| 101 | `__std_exception_copy` | `0xB2C70` | 141 | UnwindData |  |
| 102 | `__std_exception_destroy` | `0xB2D10` | 37 | UnwindData |  |
| 104 | `__std_type_info_compare` | `0xB2D60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `__std_type_info_destroy_list` | `0xB2D90` | 42 | UnwindData |  |
| 106 | `__std_type_info_hash` | `0xB2DC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `__std_type_info_name` | `0xB2E00` | 277 | UnwindData |  |
| 136 | `__uncaught_exception` | `0xB2F20` | 30 | UnwindData |  |
| 137 | `__uncaught_exceptions` | `0xB2F50` | 27 | UnwindData |  |
| 329 | `_get_purecall_handler` | `0xB2F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1738 | `_purecall` | `0xB2F90` | 25 | UnwindData |  |
| 1782 | `_set_purecall_handler` | `0xB2FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `_get_unexpected` | `0xB2FD0` | 34 | UnwindData |  |
| 2369 | `set_unexpected` | `0xB3000` | 44 | UnwindData |  |
| 2437 | `unexpected` | `0xB3040` | 29 | UnwindData |  |
| 500 | `_local_unwind` | `0xB3070` | 41 | UnwindData |  |
| 1783 | `_set_se_translator` | `0xB30B0` | 45 | UnwindData |  |
| 2290 | `longjmp` | `0xB30F0` | 40 | UnwindData |  |
| 99 | `__report_gsfailure` | `0xB3B50` | 210 | UnwindData |  |
| 675 | `_o__Strftime` | `0xB9B80` | 38 | UnwindData |  |
| 685 | `_o___conio_common_vcprintf` | `0xB9BB0` | 35 | UnwindData |  |
| 686 | `_o___conio_common_vcprintf_p` | `0xB9BE0` | 35 | UnwindData |  |
| 687 | `_o___conio_common_vcprintf_s` | `0xB9C10` | 35 | UnwindData |  |
| 688 | `_o___conio_common_vcscanf` | `0xB9C40` | 35 | UnwindData |  |
| 689 | `_o___conio_common_vcwprintf` | `0xB9C70` | 35 | UnwindData |  |
| 690 | `_o___conio_common_vcwprintf_p` | `0xB9CA0` | 35 | UnwindData |  |
| 691 | `_o___conio_common_vcwprintf_s` | `0xB9CD0` | 35 | UnwindData |  |
| 693 | `_o___daylight` | `0xB9D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 694 | `_o___dstbias` | `0xB9D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 695 | `_o___fpe_flt_rounds` | `0xB9D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 699 | `_o___p__acmdln` | `0xB9D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 701 | `_o___p__environ` | `0xB9D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | `_o___p__fmode` | `0xB9DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `_o___p__mbcasemap` | `0xB9DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `_o___p__mbctype` | `0xB9DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `_o___p__pgmptr` | `0xB9E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 706 | `_o___p__wcmdln` | `0xB9E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `_o___p__wenviron` | `0xB9E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 708 | `_o___p__wpgmptr` | `0xB9E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `_o___pwctype_func` | `0xB9E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `_o___stdio_common_vfprintf_p` | `0xB9EA0` | 45 | UnwindData |  |
| 717 | `_o___stdio_common_vfprintf_s` | `0xB9EE0` | 45 | UnwindData |  |
| 720 | `_o___stdio_common_vfwprintf_p` | `0xB9F20` | 45 | UnwindData |  |
| 722 | `_o___stdio_common_vfwscanf` | `0xB9F60` | 45 | UnwindData |  |
| 726 | `_o___stdio_common_vsprintf_p` | `0xB9FA0` | 55 | UnwindData |  |
| 734 | `_o___tzname` | `0xB9FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `_o___wcserror` | `0xBA000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 736 | `_o__access` | `0xBA020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `_o__access_s` | `0xBA040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `_o__aligned_msize` | `0xBA060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `_o__aligned_offset_realloc` | `0xBA080` | 35 | UnwindData |  |
| 743 | `_o__aligned_offset_recalloc` | `0xBA0B0` | 38 | UnwindData |  |
| 744 | `_o__aligned_realloc` | `0xBA0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `_o__aligned_recalloc` | `0xBA100` | 35 | UnwindData |  |
| 746 | `_o__atodbl` | `0xBA130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `_o__atodbl_l` | `0xBA150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 748 | `_o__atof_l` | `0xBA170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `_o__atoflt` | `0xBA190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `_o__atoflt_l` | `0xBA1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `_o__atoi64` | `0xBA1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1473 | `_o_atoll` | `0xBA1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | `_o__atoi64_l` | `0xBA1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `_o__atoll_l` | `0xBA1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `_o__atoi_l` | `0xBA210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 754 | `_o__atol_l` | `0xBA210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 755 | `_o__atoldbl` | `0xBA230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `_o__atoldbl_l` | `0xBA250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `_o__beep` | `0xBA270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `_o__cabs` | `0xBA280` | 28 | UnwindData |  |
| 762 | `_o__callnewh` | `0xBA2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | `_o__cexit` | `0xBA2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `_o__cgets` | `0xBA2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `_o__cgets_s` | `0xBA300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `_o__cgetws` | `0xBA320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 768 | `_o__cgetws_s` | `0xBA340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `_o__chdir` | `0xBA360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `_o__chdrive` | `0xBA380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `_o__chmod` | `0xBA3A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 772 | `_o__chsize` | `0xBA3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `_o__chsize_s` | `0xBA3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 780 | `_o__cputs` | `0xBA3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `_o__cputws` | `0xBA400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 782 | `_o__creat` | `0xBA420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `_o__ctime32_s` | `0xBA440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 786 | `_o__ctime64_s` | `0xBA460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | `_o__cwait` | `0xBA480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 788 | `_o__d_int` | `0xBA4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 792 | `_o__dlog` | `0xBA4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `_o__dnorm` | `0xBA4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `_o__dpcomp` | `0xBA4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 795 | `_o__dpoly` | `0xBA510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `_o__dscale` | `0xBA530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `_o__dsin` | `0xBA550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `_o__dtest` | `0xBA570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `_o__ldtest` | `0xBA570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 800 | `_o__dunscale` | `0xBA580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 803 | `_o__dupenv_s` | `0xBA5A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 804 | `_o__ecvt` | `0xBA5C0` | 35 | UnwindData |  |
| 806 | `_o__endthread` | `0xBA5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 808 | `_o__eof` | `0xBA610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `_o__except1` | `0xBA630` | 38 | UnwindData |  |
| 812 | `_o__execv` | `0xBA660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `_o__execve` | `0xBA680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `_o__execvp` | `0xBA6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `_o__execvpe` | `0xBA6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 816 | `_o__exit` | `0xBA6E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `_o__expand` | `0xBA700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `_o__fclose_nolock` | `0xBA720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `_o__fcloseall` | `0xBA740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 820 | `_o__fcvt` | `0xBA760` | 35 | UnwindData |  |
| 821 | `_o__fcvt_s` | `0xBA790` | 55 | UnwindData |  |
| 822 | `_o__fd_int` | `0xBA7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | `_o__fdexp` | `0xBA7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `_o__fdlog` | `0xBA810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 826 | `_o__fdopen` | `0xBA830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `_o__fdpcomp` | `0xBA840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 828 | `_o__fdpoly` | `0xBA860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 829 | `_o__fdscale` | `0xBA880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `_o__fdsign` | `0xBA8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `_o__fdsin` | `0xBA8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 832 | `_o__fflush_nolock` | `0xBA8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | `_o__fgetc_nolock` | `0xBA900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 834 | `_o__fgetchar` | `0xBA920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1534 | `_o_getchar` | `0xBA920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 835 | `_o__fgetwc_nolock` | `0xBA940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 837 | `_o__filelength` | `0xBA960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `_o__filelengthi64` | `0xBA980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | `_o__findclose` | `0xBA9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 841 | `_o__findfirst32` | `0xBA9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `_o__findfirst32i64` | `0xBA9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `_o__findfirst64` | `0xBAA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `_o__findfirst64i32` | `0xBAA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `_o__findnext32` | `0xBAA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `_o__findnext32i64` | `0xBAA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `_o__findnext64` | `0xBAA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 848 | `_o__findnext64i32` | `0xBAAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `_o__flushall` | `0xBAAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `_o__fpclassf` | `0xBAAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `_o__fputc_nolock` | `0xBAB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `_o__fputchar` | `0xBAB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 854 | `_o__fputwc_nolock` | `0xBAB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 855 | `_o__fputwchar` | `0xBAB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 856 | `_o__fread_nolock` | `0xBAB80` | 35 | UnwindData |  |
| 857 | `_o__fread_nolock_s` | `0xBABB0` | 45 | UnwindData |  |
| 860 | `_o__fseek_nolock` | `0xBABF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 862 | `_o__fseeki64_nolock` | `0xBAC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `_o__fsopen` | `0xBAC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `_o__fstat32` | `0xBAC50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | `_o__fstat32i64` | `0xBAC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `_o__fstat64` | `0xBAC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `_o__fstat64i32` | `0xBAC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `_o__ftell_nolock` | `0xBAC90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `_o__ftelli64` | `0xBACB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | `_o__ftelli64_nolock` | `0xBACD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 871 | `_o__ftime32` | `0xBACF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `_o__ftime32_s` | `0xBAD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `_o__ftime64` | `0xBAD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `_o__ftime64_s` | `0xBAD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `_o__fullpath` | `0xBAD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 876 | `_o__futime32` | `0xBAD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `_o__futime64` | `0xBAD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 878 | `_o__fwrite_nolock` | `0xBAD70` | 35 | UnwindData |  |
| 881 | `_o__get_daylight` | `0xBADA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 882 | `_o__get_doserrno` | `0xBADC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 883 | `_o__get_dstbias` | `0xBADD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `_o__get_fmode` | `0xBADF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | `_o__get_heap_handle` | `0xBAE10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `_o__get_invalid_parameter_handler` | `0xBAE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `_o__get_pgmptr` | `0xBAE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `_o__get_terminate` | `0xBAE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `_o__get_thread_local_invalid_parameter_handler` | `0xBAE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 896 | `_o__get_timezone` | `0xBAE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `_o__get_tzname` | `0xBAEA0` | 28 | UnwindData |  |
| 899 | `_o__get_wpgmptr` | `0xBAED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 900 | `_o__getc_nolock` | `0xBAEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 901 | `_o__getch` | `0xBAF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 902 | `_o__getch_nolock` | `0xBAF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `_o__getche` | `0xBAF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `_o__getche_nolock` | `0xBAF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 905 | `_o__getcwd` | `0xBAF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 906 | `_o__getdcwd` | `0xBAFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 907 | `_o__getdiskfree` | `0xBAFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 908 | `_o__getdllprocaddr` | `0xBAFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `_o__getdrive` | `0xBAFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | `_o__getdrives` | `0xBB010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | `_o__getmbcp` | `0xBB020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 912 | `_o__getsystime` | `0xBB040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | `_o__getw` | `0xBB050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | `_o__getwc_nolock` | `0xBB070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 915 | `_o__getwch` | `0xBB090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 916 | `_o__getwch_nolock` | `0xBB0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 917 | `_o__getwche` | `0xBB0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 918 | `_o__getwche_nolock` | `0xBB0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `_o__getws` | `0xBB110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `_o__getws_s` | `0xBB130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 921 | `_o__gmtime32` | `0xBB150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 922 | `_o__gmtime32_s` | `0xBB170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 925 | `_o__heapchk` | `0xBB190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `_o__heapmin` | `0xBB1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `_o__hypot` | `0xBB1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `_o__i64toa` | `0xBB1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 931 | `_o__i64tow` | `0xBB210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `_o__invalid_parameter_noinfo` | `0xBB230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 938 | `_o__isatty` | `0xBB250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 940 | `_o__isctype_l` | `0xBB270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 941 | `_o__isleadbyte_l` | `0xBB290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `_o__ismbbalnum` | `0xBB2B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 943 | `_o__ismbbalnum_l` | `0xBB2D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 944 | `_o__ismbbalpha` | `0xBB2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 945 | `_o__ismbbalpha_l` | `0xBB310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 946 | `_o__ismbbblank` | `0xBB330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 947 | `_o__ismbbblank_l` | `0xBB350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 948 | `_o__ismbbgraph` | `0xBB370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 949 | `_o__ismbbgraph_l` | `0xBB390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 950 | `_o__ismbbkalnum` | `0xBB3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 951 | `_o__ismbbkalnum_l` | `0xBB3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 952 | `_o__ismbbkana` | `0xBB3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 953 | `_o__ismbbkana_l` | `0xBB410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 954 | `_o__ismbbkprint` | `0xBB430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `_o__ismbbkprint_l` | `0xBB450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 956 | `_o__ismbbkpunct` | `0xBB470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `_o__ismbbkpunct_l` | `0xBB490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 958 | `_o__ismbblead` | `0xBB4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 959 | `_o__ismbblead_l` | `0xBB4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 960 | `_o__ismbbprint` | `0xBB4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 961 | `_o__ismbbprint_l` | `0xBB510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 962 | `_o__ismbbpunct` | `0xBB530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 963 | `_o__ismbbpunct_l` | `0xBB550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 964 | `_o__ismbbtrail` | `0xBB570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 965 | `_o__ismbbtrail_l` | `0xBB590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 966 | `_o__ismbcalnum` | `0xBB5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 967 | `_o__ismbcalnum_l` | `0xBB5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 968 | `_o__ismbcalpha` | `0xBB5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 969 | `_o__ismbcalpha_l` | `0xBB610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 970 | `_o__ismbcblank` | `0xBB630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 971 | `_o__ismbcblank_l` | `0xBB650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `_o__ismbcdigit` | `0xBB670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `_o__ismbcdigit_l` | `0xBB690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 974 | `_o__ismbcgraph` | `0xBB6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `_o__ismbcgraph_l` | `0xBB6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `_o__ismbchira` | `0xBB6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `_o__ismbchira_l` | `0xBB710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `_o__ismbckata` | `0xBB730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 979 | `_o__ismbckata_l` | `0xBB750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `_o__ismbcl0` | `0xBB770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `_o__ismbcl0_l` | `0xBB790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 982 | `_o__ismbcl1` | `0xBB7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 983 | `_o__ismbcl1_l` | `0xBB7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 984 | `_o__ismbcl2` | `0xBB7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `_o__ismbcl2_l` | `0xBB810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `_o__ismbclegal` | `0xBB830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 987 | `_o__ismbclegal_l` | `0xBB850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `_o__ismbclower` | `0xBB870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `_o__ismbclower_l` | `0xBB890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `_o__ismbcprint` | `0xBB8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `_o__ismbcprint_l` | `0xBB8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `_o__ismbcpunct` | `0xBB8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `_o__ismbcpunct_l` | `0xBB910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 994 | `_o__ismbcspace` | `0xBB930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 995 | `_o__ismbcspace_l` | `0xBB950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `_o__ismbcsymbol` | `0xBB970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 997 | `_o__ismbcsymbol_l` | `0xBB990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `_o__ismbcupper` | `0xBB9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `_o__ismbcupper_l` | `0xBB9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `_o__ismbslead` | `0xBB9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `_o__ismbslead_l` | `0xBBA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `_o__ismbstrail` | `0xBBA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `_o__ismbstrail_l` | `0xBBA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `_o__iswctype_l` | `0xBBA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `_o__itoa` | `0xBBA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `_o__j0` | `0xBBAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `_o__j1` | `0xBBAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `_o__jn` | `0xBBAF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `_o__kbhit` | `0xBBB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | `_o__ld_int` | `0xBBB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `_o__ldexp` | `0xBBB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `_o__ldlog` | `0xBBB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `_o__ldpcomp` | `0xBBB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `_o__ldpoly` | `0xBBBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `_o__ldscale` | `0xBBBD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `_o__ldsign` | `0xBBBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `_o__ldsin` | `0xBBC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `_o__ldunscale` | `0xBBC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `_o__lfind` | `0xBBC40` | 38 | UnwindData |  |
| 1025 | `_o__lfind_s` | `0xBBC70` | 48 | UnwindData |  |
| 1026 | `_o__loaddll` | `0xBBCB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `_o__localtime32` | `0xBBCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1028 | `_o__localtime32_s` | `0xBBCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `_o__locking` | `0xBBD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1033 | `_o__logb` | `0xBBD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1034 | `_o__logbf` | `0xBBD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `_o__lsearch` | `0xBBD60` | 38 | UnwindData |  |
| 1036 | `_o__lsearch_s` | `0xBBD90` | 48 | UnwindData |  |
| 1037 | `_o__lseek` | `0xBBDD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `_o__lseeki64` | `0xBBDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1043 | `_o__makepath` | `0xBBE10` | 38 | UnwindData |  |
| 1044 | `_o__makepath_s` | `0xBBE40` | 48 | UnwindData |  |
| 1046 | `_o__mbbtombc` | `0xBBE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1047 | `_o__mbbtombc_l` | `0xBBEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1048 | `_o__mbbtype` | `0xBBEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1049 | `_o__mbbtype_l` | `0xBBED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1050 | `_o__mbccpy` | `0xBBEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1051 | `_o__mbccpy_l` | `0xBBF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `_o__mbccpy_s` | `0xBBF30` | 28 | UnwindData |  |
| 1053 | `_o__mbccpy_s_l` | `0xBBF60` | 38 | UnwindData |  |
| 1054 | `_o__mbcjistojms` | `0xBBF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1055 | `_o__mbcjistojms_l` | `0xBBFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `_o__mbcjmstojis` | `0xBBFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `_o__mbcjmstojis_l` | `0xBBFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `_o__mbclen` | `0xBC010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `_o__mbclen_l` | `0xBC030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1060 | `_o__mbctohira` | `0xBC050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `_o__mbctohira_l` | `0xBC070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1062 | `_o__mbctokata` | `0xBC090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1063 | `_o__mbctokata_l` | `0xBC0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1064 | `_o__mbctolower` | `0xBC0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1065 | `_o__mbctolower_l` | `0xBC0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `_o__mbctombb` | `0xBC110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `_o__mbctombb_l` | `0xBC130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1068 | `_o__mbctoupper` | `0xBC150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1069 | `_o__mbctoupper_l` | `0xBC170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1070 | `_o__mblen_l` | `0xBC190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `_o__mbsbtype_l` | `0xBC1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `_o__mbscat_s` | `0xBC1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `_o__mbscat_s_l` | `0xBC1F0` | 35 | UnwindData |  |
| 1075 | `_o__mbschr` | `0xBC220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `_o__mbschr_l` | `0xBC240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `_o__mbscmp_l` | `0xBC260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1079 | `_o__mbscoll` | `0xBC280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1080 | `_o__mbscoll_l` | `0xBC2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1081 | `_o__mbscpy_s` | `0xBC2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1082 | `_o__mbscpy_s_l` | `0xBC2E0` | 35 | UnwindData |  |
| 1083 | `_o__mbscspn` | `0xBC310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1084 | `_o__mbscspn_l` | `0xBC330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `_o__mbsdec` | `0xBC350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1086 | `_o__mbsdec_l` | `0xBC370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1088 | `_o__mbsicmp_l` | `0xBC390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `_o__mbsicoll` | `0xBC3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `_o__mbsicoll_l` | `0xBC3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `_o__mbsinc_l` | `0xBC3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `_o__mbslen` | `0xBC410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `_o__mbslen_l` | `0xBC430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `_o__mbslwr` | `0xBC450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `_o__mbslwr_l` | `0xBC470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1098 | `_o__mbslwr_s_l` | `0xBC490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1099 | `_o__mbsnbcat` | `0xBC4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1100 | `_o__mbsnbcat_l` | `0xBC4D0` | 35 | UnwindData |  |
| 1101 | `_o__mbsnbcat_s` | `0xBC500` | 35 | UnwindData |  |
| 1102 | `_o__mbsnbcat_s_l` | `0xBC530` | 45 | UnwindData |  |
| 1103 | `_o__mbsnbcmp` | `0xBC570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `_o__mbsnbcmp_l` | `0xBC590` | 35 | UnwindData |  |
| 1105 | `_o__mbsnbcnt` | `0xBC5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `_o__mbsnbcnt_l` | `0xBC5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `_o__mbsnbcoll` | `0xBC600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1108 | `_o__mbsnbcoll_l` | `0xBC620` | 35 | UnwindData |  |
| 1109 | `_o__mbsnbcpy` | `0xBC650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1110 | `_o__mbsnbcpy_l` | `0xBC670` | 35 | UnwindData |  |
| 1111 | `_o__mbsnbcpy_s` | `0xBC6A0` | 35 | UnwindData |  |
| 1112 | `_o__mbsnbcpy_s_l` | `0xBC6D0` | 45 | UnwindData |  |
| 1113 | `_o__mbsnbicmp` | `0xBC710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1114 | `_o__mbsnbicmp_l` | `0xBC730` | 35 | UnwindData |  |
| 1115 | `_o__mbsnbicoll` | `0xBC760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1116 | `_o__mbsnbicoll_l` | `0xBC780` | 35 | UnwindData |  |
| 1117 | `_o__mbsnbset` | `0xBC7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1118 | `_o__mbsnbset_l` | `0xBC7D0` | 35 | UnwindData |  |
| 1119 | `_o__mbsnbset_s` | `0xBC800` | 35 | UnwindData |  |
| 1120 | `_o__mbsnbset_s_l` | `0xBC830` | 45 | UnwindData |  |
| 1121 | `_o__mbsncat` | `0xBC870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `_o__mbsncat_l` | `0xBC890` | 35 | UnwindData |  |
| 1123 | `_o__mbsncat_s` | `0xBC8C0` | 35 | UnwindData |  |
| 1124 | `_o__mbsncat_s_l` | `0xBC8F0` | 45 | UnwindData |  |
| 1126 | `_o__mbsnccnt_l` | `0xBC930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1127 | `_o__mbsncmp` | `0xBC950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `_o__mbsncmp_l` | `0xBC970` | 35 | UnwindData |  |
| 1129 | `_o__mbsncoll` | `0xBC9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1130 | `_o__mbsncoll_l` | `0xBC9C0` | 35 | UnwindData |  |
| 1131 | `_o__mbsncpy` | `0xBC9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1132 | `_o__mbsncpy_l` | `0xBCA10` | 35 | UnwindData |  |
| 1133 | `_o__mbsncpy_s` | `0xBCA40` | 35 | UnwindData |  |
| 1134 | `_o__mbsncpy_s_l` | `0xBCA70` | 45 | UnwindData |  |
| 1135 | `_o__mbsnextc` | `0xBCAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `_o__mbsnextc_l` | `0xBCAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `_o__mbsnicmp` | `0xBCAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `_o__mbsnicmp_l` | `0xBCB00` | 35 | UnwindData |  |
| 1139 | `_o__mbsnicoll` | `0xBCB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1140 | `_o__mbsnicoll_l` | `0xBCB50` | 35 | UnwindData |  |
| 1141 | `_o__mbsninc` | `0xBCB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `_o__mbsninc_l` | `0xBCBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `_o__mbsnlen` | `0xBCBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `_o__mbsnlen_l` | `0xBCBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `_o__mbsnset` | `0xBCC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `_o__mbsnset_l` | `0xBCC20` | 35 | UnwindData |  |
| 1147 | `_o__mbsnset_s` | `0xBCC50` | 35 | UnwindData |  |
| 1148 | `_o__mbsnset_s_l` | `0xBCC80` | 45 | UnwindData |  |
| 1149 | `_o__mbspbrk` | `0xBCCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1150 | `_o__mbspbrk_l` | `0xBCCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `_o__mbsrchr` | `0xBCD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1152 | `_o__mbsrchr_l` | `0xBCD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1153 | `_o__mbsrev` | `0xBCD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1155 | `_o__mbsset` | `0xBCD60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1156 | `_o__mbsset_l` | `0xBCD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1157 | `_o__mbsset_s` | `0xBCDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1158 | `_o__mbsset_s_l` | `0xBCDC0` | 28 | UnwindData |  |
| 1159 | `_o__mbsspn` | `0xBCDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1160 | `_o__mbsspn_l` | `0xBCE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1161 | `_o__mbsspnp` | `0xBCE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1162 | `_o__mbsspnp_l` | `0xBCE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1164 | `_o__mbsstr_l` | `0xBCE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1165 | `_o__mbstok` | `0xBCE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1166 | `_o__mbstok_l` | `0xBCEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `_o__mbstok_s` | `0xBCED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1168 | `_o__mbstok_s_l` | `0xBCEF0` | 28 | UnwindData |  |
| 1169 | `_o__mbstowcs_l` | `0xBCF20` | 28 | UnwindData |  |
| 1170 | `_o__mbstowcs_s_l` | `0xBCF50` | 48 | UnwindData |  |
| 1172 | `_o__mbstrlen_l` | `0xBCF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `_o__mbstrnlen` | `0xBCFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `_o__mbstrnlen_l` | `0xBCFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `_o__mbsupr` | `0xBCFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `_o__mbsupr_l` | `0xBD010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `_o__mbsupr_s` | `0xBD030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `_o__mbsupr_s_l` | `0xBD050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1179 | `_o__mbtowc_l` | `0xBD070` | 28 | UnwindData |  |
| 1181 | `_o__memicmp_l` | `0xBD0A0` | 28 | UnwindData |  |
| 1182 | `_o__mkdir` | `0xBD0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `_o__mkgmtime32` | `0xBD0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `_o__mktemp` | `0xBD110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1186 | `_o__mktemp_s` | `0xBD130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `_o__nextafter` | `0xBD150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `_o_nextafter` | `0xBD150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `_o__nextafterf` | `0xBD170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1622 | `_o_nextafterf` | `0xBD170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `_o__pclose` | `0xBD190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `_o__popen` | `0xBD1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `_o__purecall` | `0xBD1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1197 | `_o__putc_nolock` | `0xBD1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `_o__putch` | `0xBD210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `_o__putch_nolock` | `0xBD230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1200 | `_o__putenv` | `0xBD250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1201 | `_o__putenv_s` | `0xBD270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `_o__putw` | `0xBD290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `_o__putwc_nolock` | `0xBD2B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1204 | `_o__putwch` | `0xBD2D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `_o__putwch_nolock` | `0xBD2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1206 | `_o__putws` | `0xBD310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `_o__read` | `0xBD330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `_o__resetstkoflw` | `0xBD350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `_o__rmdir` | `0xBD370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `_o__rmtmp` | `0xBD390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1214 | `_o__scalb` | `0xBD3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `_o__scalbf` | `0xBD3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1216 | `_o__searchenv` | `0xBD3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `_o__searchenv_s` | `0xBD410` | 28 | UnwindData |  |
| 1218 | `_o__seh_filter_dll` | `0xBD440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1219 | `_o__seh_filter_exe` | `0xBD460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `_o__set_abort_behavior` | `0xBD480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `_o__set_new_handler` | `0xBD490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1228 | `_o__set_thread_local_invalid_parameter_handler` | `0xBD4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `_o__seterrormode` | `0xBD4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `_o__setmbcp` | `0xBD4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `_o__setsystime` | `0xBD500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1233 | `_o__sleep` | `0xBD520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `_o__sopen` | `0xBD530` | 28 | UnwindData |  |
| 1235 | `_o__sopen_dispatch` | `0xBD560` | 46 | UnwindData |  |
| 1236 | `_o__sopen_s` | `0xBD5A0` | 36 | UnwindData |  |
| 1237 | `_o__spawnv` | `0xBD5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1238 | `_o__spawnve` | `0xBD5F0` | 34 | UnwindData |  |
| 1239 | `_o__spawnvp` | `0xBD620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1240 | `_o__spawnvpe` | `0xBD640` | 34 | UnwindData |  |
| 1241 | `_o__splitpath` | `0xBD670` | 38 | UnwindData |  |
| 1243 | `_o__stat32` | `0xBD6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1244 | `_o__stat32i64` | `0xBD6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1245 | `_o__stat64` | `0xBD6E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1247 | `_o__strcoll_l` | `0xBD700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `_o__strdate` | `0xBD720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `_o__strdate_s` | `0xBD740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1251 | `_o__strerror` | `0xBD760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1252 | `_o__strerror_s` | `0xBD780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `_o__strftime_l` | `0xBD7A0` | 38 | UnwindData |  |
| 1255 | `_o__stricmp_l` | `0xBD7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `_o__stricoll_l` | `0xBD7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `_o__strlwr_s_l` | `0xBD810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1263 | `_o__strncoll_l` | `0xBD830` | 35 | UnwindData |  |
| 1265 | `_o__strnicmp_l` | `0xBD860` | 35 | UnwindData |  |
| 1266 | `_o__strnicoll` | `0xBD890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1267 | `_o__strnicoll_l` | `0xBD8B0` | 35 | UnwindData |  |
| 1268 | `_o__strnset_s` | `0xBD8E0` | 28 | UnwindData |  |
| 1269 | `_o__strset_s` | `0xBD910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1270 | `_o__strtime` | `0xBD930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1271 | `_o__strtime_s` | `0xBD950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1272 | `_o__strtod_l` | `0xBD970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1277 | `_o__strtold_l` | `0xBD970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1273 | `_o__strtof_l` | `0xBD990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1275 | `_o__strtoi64_l` | `0xBD9B0` | 35 | UnwindData |  |
| 1278 | `_o__strtoll_l` | `0xBD9B0` | 35 | UnwindData |  |
| 1276 | `_o__strtol_l` | `0xBD9E0` | 28 | UnwindData |  |
| 1280 | `_o__strtoui64_l` | `0xBDA10` | 35 | UnwindData |  |
| 1282 | `_o__strtoull_l` | `0xBDA10` | 35 | UnwindData |  |
| 1281 | `_o__strtoul_l` | `0xBDA40` | 28 | UnwindData |  |
| 1283 | `_o__strupr` | `0xBDA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `_o__strupr_l` | `0xBDA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1286 | `_o__strupr_s_l` | `0xBDAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `_o__strxfrm_l` | `0xBDAD0` | 28 | UnwindData |  |
| 1288 | `_o__swab` | `0xBDB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `_o__telli64` | `0xBDB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1291 | `_o__timespec32_get` | `0xBDB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1292 | `_o__timespec64_get` | `0xBDB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1294 | `_o__tolower_l` | `0xBDB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1295 | `_o__toupper` | `0xBDBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1296 | `_o__toupper_l` | `0xBDBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1298 | `_o__towupper_l` | `0xBDBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `_o__tzset` | `0xBDC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1300 | `_o__ui64toa` | `0xBDC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `_o__ui64tow` | `0xBDC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `_o__ultoa` | `0xBDC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1308 | `_o__umask` | `0xBDC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1310 | `_o__ungetc_nolock` | `0xBDCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `_o__ungetch` | `0xBDCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1312 | `_o__ungetch_nolock` | `0xBDCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `_o__ungetwc_nolock` | `0xBDD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1314 | `_o__ungetwch` | `0xBDD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1315 | `_o__ungetwch_nolock` | `0xBDD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1316 | `_o__unlink` | `0xBDD60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `_o__unloaddll` | `0xBDD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `_o__utime32` | `0xBDDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `_o__utime64` | `0xBDDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1322 | `_o__waccess_s` | `0xBDDE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `_o__wasctime` | `0xBDE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1324 | `_o__wasctime_s` | `0xBDE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1325 | `_o__wchdir` | `0xBDE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `_o__wchmod` | `0xBDE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1327 | `_o__wcreat` | `0xBDE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1329 | `_o__wcscoll_l` | `0xBDE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `_o__wcserror` | `0xBDEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `_o__wcserror_s` | `0xBDEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1333 | `_o__wcsftime_l` | `0xBDEE0` | 38 | UnwindData |  |
| 1336 | `_o__wcsicoll` | `0xBDF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `_o__wcsicoll_l` | `0xBDF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1341 | `_o__wcslwr_s_l` | `0xBDF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1342 | `_o__wcsncoll` | `0xBDF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1343 | `_o__wcsncoll_l` | `0xBDF90` | 35 | UnwindData |  |
| 1345 | `_o__wcsnicmp_l` | `0xBDFC0` | 35 | UnwindData |  |
| 1347 | `_o__wcsnicoll_l` | `0xBDFF0` | 35 | UnwindData |  |
| 1349 | `_o__wcsnset_s` | `0xBE020` | 29 | UnwindData |  |
| 1350 | `_o__wcsset` | `0xBE050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1351 | `_o__wcsset_s` | `0xBE070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1353 | `_o__wcstof_l` | `0xBE090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `_o__wcstoi64_l` | `0xBE0B0` | 35 | UnwindData |  |
| 1358 | `_o__wcstoll_l` | `0xBE0B0` | 35 | UnwindData |  |
| 1356 | `_o__wcstol_l` | `0xBE0E0` | 28 | UnwindData |  |
| 1359 | `_o__wcstombs_l` | `0xBE110` | 28 | UnwindData |  |
| 1362 | `_o__wcstoui64_l` | `0xBE140` | 35 | UnwindData |  |
| 1364 | `_o__wcstoull_l` | `0xBE140` | 35 | UnwindData |  |
| 1363 | `_o__wcstoul_l` | `0xBE170` | 28 | UnwindData |  |
| 1366 | `_o__wcsupr_l` | `0xBE1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1368 | `_o__wcsupr_s_l` | `0xBE1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1369 | `_o__wcsxfrm_l` | `0xBE1E0` | 28 | UnwindData |  |
| 1370 | `_o__wctime32` | `0xBE210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1371 | `_o__wctime32_s` | `0xBE220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1372 | `_o__wctime64` | `0xBE240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1373 | `_o__wctime64_s` | `0xBE250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1374 | `_o__wctomb_l` | `0xBE270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1375 | `_o__wctomb_s_l` | `0xBE290` | 39 | UnwindData |  |
| 1376 | `_o__wdupenv_s` | `0xBE2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1377 | `_o__wexecv` | `0xBE2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1378 | `_o__wexecve` | `0xBE300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1379 | `_o__wexecvp` | `0xBE320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1380 | `_o__wexecvpe` | `0xBE340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1381 | `_o__wfdopen` | `0xBE360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1382 | `_o__wfindfirst32` | `0xBE370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1383 | `_o__wfindfirst32i64` | `0xBE390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `_o__wfindfirst64` | `0xBE3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1385 | `_o__wfindfirst64i32` | `0xBE3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1386 | `_o__wfindnext32` | `0xBE3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `_o__wfindnext32i64` | `0xBE410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1388 | `_o__wfindnext64` | `0xBE430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1389 | `_o__wfindnext64i32` | `0xBE450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1390 | `_o__wfopen` | `0xBE470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1391 | `_o__wfopen_s` | `0xBE490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1392 | `_o__wfreopen` | `0xBE4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1393 | `_o__wfreopen_s` | `0xBE4D0` | 28 | UnwindData |  |
| 1396 | `_o__wgetcwd` | `0xBE500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1397 | `_o__wgetdcwd` | `0xBE520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1400 | `_o__wmakepath` | `0xBE540` | 38 | UnwindData |  |
| 1403 | `_o__wmktemp` | `0xBE570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1404 | `_o__wmktemp_s` | `0xBE590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1405 | `_o__wperror` | `0xBE5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `_o__wputenv` | `0xBE5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1409 | `_o__wremove` | `0xBE5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1410 | `_o__wrename` | `0xBE600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1411 | `_o__write` | `0xBE620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1412 | `_o__wrmdir` | `0xBE640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1413 | `_o__wsearchenv` | `0xBE660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1414 | `_o__wsearchenv_s` | `0xBE680` | 28 | UnwindData |  |
| 1416 | `_o__wsopen_dispatch` | `0xBE6B0` | 46 | UnwindData |  |
| 1417 | `_o__wsopen_s` | `0xBE6F0` | 36 | UnwindData |  |
| 1418 | `_o__wspawnv` | `0xBE720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1419 | `_o__wspawnve` | `0xBE740` | 34 | UnwindData |  |
| 1420 | `_o__wspawnvp` | `0xBE770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1421 | `_o__wspawnvpe` | `0xBE790` | 34 | UnwindData |  |
| 1422 | `_o__wsplitpath` | `0xBE7C0` | 38 | UnwindData |  |
| 1424 | `_o__wstat32` | `0xBE7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `_o__wstat32i64` | `0xBE810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1426 | `_o__wstat64` | `0xBE830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1427 | `_o__wstat64i32` | `0xBE850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1428 | `_o__wstrdate` | `0xBE870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1429 | `_o__wstrdate_s` | `0xBE890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `_o__wstrtime` | `0xBE8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `_o__wstrtime_s` | `0xBE8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1433 | `_o__wtmpnam_s` | `0xBE8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1435 | `_o__wtof_l` | `0xBE910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1438 | `_o__wtoi64_l` | `0xBE930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1443 | `_o__wtoll_l` | `0xBE930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1439 | `_o__wtoi_l` | `0xBE950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1441 | `_o__wtol_l` | `0xBE950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `_o__wunlink` | `0xBE970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1445 | `_o__wutime32` | `0xBE990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1447 | `_o__y0` | `0xBE9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `_o__y1` | `0xBE9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1449 | `_o__yn` | `0xBE9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1450 | `_o_abort` | `0xBEA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1453 | `_o_acosh` | `0xBEA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1454 | `_o_acoshf` | `0xBEA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1455 | `_o_acoshl` | `0xBEA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1456 | `_o_asctime` | `0xBEA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1457 | `_o_asctime_s` | `0xBEAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1460 | `_o_asinh` | `0xBEAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1461 | `_o_asinhf` | `0xBEAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1462 | `_o_asinhl` | `0xBEB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1467 | `_o_atanh` | `0xBEB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1468 | `_o_atanhf` | `0xBEB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1469 | `_o_atanhl` | `0xBEB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1478 | `_o_cbrt` | `0xBEB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `_o_cbrtf` | `0xBEBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1482 | `_o_clearerr` | `0xBEBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1483 | `_o_clearerr_s` | `0xBEBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1487 | `_o_coshf` | `0xBEC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1488 | `_o_erf` | `0xBEC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1489 | `_o_erfc` | `0xBEC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1490 | `_o_erfcf` | `0xBEC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1491 | `_o_erfcl` | `0xBEC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1492 | `_o_erff` | `0xBECA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1493 | `_o_erfl` | `0xBECC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1496 | `_o_exp2` | `0xBECE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1497 | `_o_exp2f` | `0xBED00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1498 | `_o_exp2l` | `0xBED20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1500 | `_o_fabs` | `0xBED40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1508 | `_o_fgetwc` | `0xBED60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `_o_fma` | `0xBED80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1513 | `_o_fmaf` | `0xBEDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1514 | `_o_fmal` | `0xBEDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1517 | `_o_fopen` | `0xBEDE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1518 | `_o_fopen_s` | `0xBEE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `_o_fputws` | `0xBEE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1524 | `_o_fread_s` | `0xBEE40` | 45 | UnwindData |  |
| 1527 | `_o_freopen_s` | `0xBEE80` | 28 | UnwindData |  |
| 1530 | `_o_fsetpos` | `0xBEEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `_o_ftell` | `0xBEED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1533 | `_o_getc` | `0xBEEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1537 | `_o_gets` | `0xBEF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `_o_gets_s` | `0xBEF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `_o_getwc` | `0xBEF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1541 | `_o_hypot` | `0xBEF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1542 | `_o_is_wctype` | `0xBEF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1545 | `_o_isblank` | `0xBEFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1548 | `_o_isgraph` | `0xBEFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1549 | `_o_isleadbyte` | `0xBEFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1550 | `_o_islower` | `0xBF010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1558 | `_o_iswblank` | `0xBF030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1562 | `_o_iswgraph` | `0xBF050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1571 | `_o_lgamma` | `0xBF070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1572 | `_o_lgammaf` | `0xBF090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1573 | `_o_lgammal` | `0xBF0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1574 | `_o_llrint` | `0xBF0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1575 | `_o_llrintf` | `0xBF0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1576 | `_o_llrintl` | `0xBF110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `_o_llroundf` | `0xBF130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1584 | `_o_log1p` | `0xBF150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1585 | `_o_log1pf` | `0xBF170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1586 | `_o_log1pl` | `0xBF190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1589 | `_o_log2l` | `0xBF1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1590 | `_o_logb` | `0xBF1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1591 | `_o_logbf` | `0xBF1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1592 | `_o_logbl` | `0xBF210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1594 | `_o_lrint` | `0xBF230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1596 | `_o_lrintl` | `0xBF250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1601 | `_o_mblen` | `0xBF270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1602 | `_o_mbrlen` | `0xBF290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1603 | `_o_mbrtoc16` | `0xBF2B0` | 28 | UnwindData |  |
| 1604 | `_o_mbrtoc32` | `0xBF2E0` | 28 | UnwindData |  |
| 1605 | `_o_mbrtowc` | `0xBF310` | 28 | UnwindData |  |
| 1606 | `_o_mbsrtowcs` | `0xBF340` | 28 | UnwindData |  |
| 1607 | `_o_mbsrtowcs_s` | `0xBF370` | 48 | UnwindData |  |
| 1615 | `_o_nan` | `0xBF3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1616 | `_o_nanf` | `0xBF3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `_o_nanl` | `0xBF3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1618 | `_o_nearbyint` | `0xBF3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1619 | `_o_nearbyintf` | `0xBF410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1620 | `_o_nearbyintl` | `0xBF430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1623 | `_o_nextafterl` | `0xBF450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1626 | `_o_nexttowardl` | `0xBF450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1624 | `_o_nexttoward` | `0xBF470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1625 | `_o_nexttowardf` | `0xBF490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1629 | `_o_putc` | `0xBF4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `_o_putchar` | `0xBF4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1631 | `_o_puts` | `0xBF4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1632 | `_o_putwc` | `0xBF510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1633 | `_o_putwchar` | `0xBF530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1636 | `_o_raise` | `0xBF550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1640 | `_o_remainder` | `0xBF570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1641 | `_o_remainderf` | `0xBF590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `_o_remainderl` | `0xBF5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1643 | `_o_remove` | `0xBF5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `_o_remquo` | `0xBF5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1645 | `_o_remquof` | `0xBF610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1646 | `_o_remquol` | `0xBF630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1647 | `_o_rename` | `0xBF650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1649 | `_o_rint` | `0xBF670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1650 | `_o_rintf` | `0xBF690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1651 | `_o_rintl` | `0xBF6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1655 | `_o_scalbln` | `0xBF6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1656 | `_o_scalblnf` | `0xBF6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1657 | `_o_scalblnl` | `0xBF710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1658 | `_o_scalbn` | `0xBF730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1660 | `_o_scalbnl` | `0xBF730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1659 | `_o_scalbnf` | `0xBF750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1662 | `_o_setbuf` | `0xBF770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1664 | `_o_setvbuf` | `0xBF790` | 28 | UnwindData |  |
| 1667 | `_o_sinh` | `0xBF7C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `_o_sinhf` | `0xBF7E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1673 | `_o_strcoll` | `0xBF800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1675 | `_o_strerror` | `0xBF820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1676 | `_o_strerror_s` | `0xBF830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1689 | `_o_system` | `0xBF850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1694 | `_o_terminate` | `0xBF870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1695 | `_o_tgamma` | `0xBF880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1696 | `_o_tgammaf` | `0xBF8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1697 | `_o_tgammal` | `0xBF8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1698 | `_o_tmpfile_s` | `0xBF8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1699 | `_o_tmpnam_s` | `0xBF8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1704 | `_o_ungetc` | `0xBF910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1705 | `_o_ungetwc` | `0xBF930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1706 | `_o_wcrtomb` | `0xBF950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1707 | `_o_wcrtomb_s` | `0xBF970` | 39 | UnwindData |  |
| 1709 | `_o_wcscoll` | `0xBF9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1710 | `_o_wcscpy` | `0xBF9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1715 | `_o_wcsrtombs` | `0xBF9E0` | 28 | UnwindData |  |
| 1716 | `_o_wcsrtombs_s` | `0xBFA10` | 48 | UnwindData |  |
| 1728 | `_o_wctob` | `0xBFA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1729 | `_o_wctomb` | `0xBFA70` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `_atodbl_l` | `0xBFC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `_atoflt` | `0xBFC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `_atoflt_l` | `0xBFC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `_atoldbl` | `0xBFC30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `_atoi64_l` | `0xBFC40` | 76 | UnwindData |  |
| 164 | `_atoll_l` | `0xBFC40` | 76 | UnwindData |  |
| 160 | `_atoi_l` | `0xBFCA0` | 74 | UnwindData |  |
| 161 | `_atol_l` | `0xBFCA0` | 74 | UnwindData |  |
| 2026 | `_wtoi64_l` | `0xBFCF0` | 76 | UnwindData |  |
| 2031 | `_wtoll_l` | `0xBFCF0` | 76 | UnwindData |  |
| 2066 | `c16rtomb` | `0xBFD50` | 64 | UnwindData |  |
| 2067 | `c32rtomb` | `0xBFDA0` | 62 | UnwindData |  |
| 454 | `_ismbstrail` | `0xBFEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `_ismbstrail_l` | `0xBFF00` | 162 | UnwindData |  |
| 468 | `_iswctype_l` | `0xBFFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2234 | `is_wctype` | `0xBFFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `_mblen_l` | `0xBFFC0` | 61 | UnwindData |  |
| 2300 | `mbrtoc16` | `0xC0110` | 67 | UnwindData |  |
| 648 | `_mbstowcs_l` | `0xC0160` | 63 | UnwindData |  |
| 1926 | `_wcstof_l` | `0xC01B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1842 | `_strtol_l` | `0xC01C0` | 81 | UnwindData |  |
| 1847 | `_strtoul_l` | `0xC0220` | 81 | UnwindData |  |
| 1928 | `_wcstoi64_l` | `0xC0280` | 83 | UnwindData |  |
| 1929 | `_wcstoimax_l` | `0xC0280` | 83 | UnwindData |  |
| 1932 | `_wcstoll_l` | `0xC0280` | 83 | UnwindData |  |
| 1936 | `_wcstoui64_l` | `0xC02E0` | 83 | UnwindData |  |
| 1938 | `_wcstoull_l` | `0xC02E0` | 83 | UnwindData |  |
| 1939 | `_wcstoumax_l` | `0xC02E0` | 83 | UnwindData |  |
| 1937 | `_wcstoul_l` | `0xC0340` | 81 | UnwindData |  |
| 1865 | `_toupper` | `0xC03A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2460 | `wcsrtombs` | `0xC03B0` | 67 | UnwindData |  |
| 1933 | `_wcstombs_l` | `0xC0400` | 63 | UnwindData |  |
| 1949 | `_wctomb_l` | `0xC0450` | 135 | UnwindData |  |
| 1950 | `_wctomb_s_l` | `0xC04E0` | 71 | UnwindData |  |
| 2431 | `towctrans` | `0xC0530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2481 | `wctrans` | `0xC0550` | 96 | UnwindData |  |
| 78 | `__iscsym` | `0xC05C0` | 123 | UnwindData |  |
| 79 | `__iscsymf` | `0xC0650` | 162 | UnwindData |  |
| 132 | `__toascii` | `0xC0700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `_isblank_l` | `0xC0710` | 189 | UnwindData |  |
| 387 | `_iscntrl_l` | `0xC07E0` | 189 | UnwindData |  |
| 391 | `_isgraph_l` | `0xC08B0` | 196 | UnwindData |  |
| 393 | `_islower_l` | `0xC0980` | 189 | UnwindData |  |
| 458 | `_isprint_l` | `0xC0A50` | 196 | UnwindData |  |
| 460 | `_isspace_l` | `0xC0B20` | 189 | UnwindData |  |
| 477 | `_isxdigit_l` | `0xC0BF0` | 196 | UnwindData |  |
| 651 | `_mbstrlen_l` | `0xC0CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `_mbstrnlen` | `0xC0CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `_mbstrnlen_l` | `0xC0CF0` | 52 | UnwindData |  |
| 80 | `__iswcsym` | `0xC0D30` | 44 | UnwindData |  |
| 466 | `_iswcsym_l` | `0xC0D30` | 44 | UnwindData |  |
| 81 | `__iswcsymf` | `0xC0D70` | 44 | UnwindData |  |
| 467 | `_iswcsymf_l` | `0xC0D70` | 44 | UnwindData |  |
| 474 | `_iswspace_l` | `0xC0DB0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `__threadhandle` | `0xC0EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `__threadid` | `0xC0EB0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `__pwctype_func` | `0xC11B0` | 2,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `__p__mbcasemap` | `0xC1D00` | 25 | UnwindData |  |
| 90 | `__p__mbctype` | `0xC1D20` | 25 | UnwindData |  |
| 350 | `_getmbcp` | `0xC1D40` | 76 | UnwindData |  |
| 317 | `_get_doserrno` | `0xC1E40` | 41 | UnwindData |  |
| 1768 | `_seh_filter_dll` | `0xC1E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `_get_invalid_parameter_handler` | `0xC1E90` | 43 | UnwindData |  |
| 332 | `_get_thread_local_invalid_parameter_handler` | `0xC1ED0` | 26 | UnwindData |  |
| 380 | `_invalid_parameter_noinfo_noreturn` | `0xC1EF0` | 31 | UnwindData |  |
| 73 | `__fpecode` | `0xC1F20` | 18 | UnwindData |  |
| 98 | `__pxcptinfoptrs` | `0xC1F40` | 18 | UnwindData |  |
| 2343 | `raise` | `0xC1F60` | 518 | UnwindData |  |
| 2421 | `terminate` | `0xC2170` | 31 | UnwindData |  |
| 1986 | `_wperror` | `0xC21A0` | 210 | UnwindData |  |
| 138 | `__wcserror` | `0xC2640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `__wcserror_s` | `0xC2650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1813 | `_strerror` | `0xC2660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1814 | `_strerror_s` | `0xC2670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `__p__acmdln` | `0xC2680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `__p__pgmptr` | `0xC2690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `__p__wcmdln` | `0xC26A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `__p__wpgmptr` | `0xC26B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `_get_pgmptr` | `0xC26C0` | 54 | UnwindData |  |
| 337 | `_get_wpgmptr` | `0xC2700` | 54 | UnwindData |  |
| 152 | `_assert` | `0xC3220` | 114 | UnwindData |  |
| 1896 | `_wassert` | `0xC32A0` | 114 | UnwindData |  |
| 171 | `_c_exit` | `0xC3430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2342 | `quick_exit` | `0xC3450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `_crt_at_quick_exit` | `0xC3470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `_endthread` | `0xC3490` | 12 | UnwindData |  |
| 263 | `_fgetchar` | `0xC34B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2221 | `getchar` | `0xC34B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `_fputc_nolock` | `0xC34D0` | 60 | UnwindData |  |
| 286 | `_fputchar` | `0xC3520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `_putc_nolock` | `0xC3540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2336 | `putchar` | `0xC3550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `_fputwc_nolock` | `0xC3560` | 64 | UnwindData |  |
| 288 | `_fputwchar` | `0xC35B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1745 | `_putwc_nolock` | `0xC35D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2338 | `putwc` | `0xC35E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2339 | `putwchar` | `0xC35F0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1972 | `_wfreopen` | `0xC3710` | 47 | UnwindData |  |
| 1973 | `_wfreopen_s` | `0xC3750` | 22 | UnwindData |  |
| 2214 | `freopen_s` | `0xC3770` | 22 | UnwindData |  |
| 293 | `_fseek_nolock` | `0xC3790` | 60 | UnwindData |  |
| 295 | `_fseeki64_nolock` | `0xC37E0` | 60 | UnwindData |  |
| 301 | `_ftell_nolock` | `0xC39C0` | 54 | UnwindData |  |
| 303 | `_ftelli64_nolock` | `0xC3A00` | 56 | UnwindData |  |
| 359 | `_getws` | `0xC3BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `_getws_s` | `0xC3BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2224 | `gets` | `0xC3BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2225 | `gets_s` | `0xC3C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `_getw` | `0xC3C20` | 170 | UnwindData |  |
| 109 | `__stdio_common_vfprintf_p` | `0xC5FC0` | 74 | UnwindData |  |
| 113 | `__stdio_common_vfwprintf_p` | `0xC6010` | 74 | UnwindData |  |
| 1781 | `_set_printf_count_output` | `0xC6060` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1744 | `_putw` | `0xC6090` | 152 | UnwindData |  |
| 1748 | `_putws` | `0xC6290` | 163 | UnwindData |  |
| 349 | `_getmaxstdio` | `0xC64C0` | 37 | UnwindData |  |
| 1786 | `_setmaxstdio` | `0xC64F0` | 87 | UnwindData |  |
| 1858 | `_tempnam` | `0xC6A40` | 14 | UnwindData |  |
| 2019 | `_wtempnam` | `0xC6A60` | 14 | UnwindData |  |
| 2020 | `_wtmpnam` | `0xC7200` | 38 | UnwindData |  |
| 2021 | `_wtmpnam_s` | `0xC7230` | 59 | UnwindData |  |
| 2425 | `tmpfile` | `0xC7280` | 35 | UnwindData |  |
| 2426 | `tmpfile_s` | `0xC72B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2427 | `tmpnam` | `0xC72C0` | 38 | UnwindData |  |
| 497 | `_lfind` | `0xC72F0` | 155 | UnwindData |  |
| 498 | `_lfind_s` | `0xC73A0` | 159 | UnwindData |  |
| 512 | `_lsearch` | `0xC7450` | 216 | UnwindData |  |
| 513 | `_lsearch_s` | `0xC7530` | 222 | UnwindData |  |
| 1761 | `_rotl64` | `0xC7620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1763 | `_rotr64` | `0xC7640` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1818 | `_stricoll` | `0xC7690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1819 | `_stricoll_l` | `0xC76B0` | 209 | UnwindData |  |
| 1821 | `_strlwr_l` | `0xC7790` | 30 | UnwindData |  |
| 1824 | `_strncoll` | `0xC77C0` | 79 | UnwindData |  |
| 1825 | `_strncoll_l` | `0xC7820` | 247 | UnwindData |  |
| 1831 | `_strnset_s` | `0xC7960` | 116 | UnwindData |  |
| 1834 | `_strset_s` | `0xC79E0` | 73 | UnwindData |  |
| 1851 | `_strupr_l` | `0xC7A30` | 30 | UnwindData |  |
| 1911 | `_wcslwr_l` | `0xC7A60` | 30 | UnwindData |  |
| 140 | `__wcsncnt` | `0xC7A90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1914 | `_wcsncoll` | `0xC7AC0` | 79 | UnwindData |  |
| 1921 | `_wcsnset_s` | `0xC7B20` | 122 | UnwindData |  |
| 1923 | `_wcsset` | `0xC7BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1941 | `_wcsupr_l` | `0xC7BC0` | 30 | UnwindData |  |
| 1944 | `_wcsxfrm_l` | `0xC7BF0` | 370 | UnwindData |  |
| 2477 | `wcsxfrm` | `0xC7D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `_j0` | `0xC7D80` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `_j1` | `0xC7F80` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `_jn` | `0xC81B0` | 372 | UnwindData |  |
| 2035 | `_y0` | `0xC8330` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2069 | `cabsf` | `0xC8820` | 30 | UnwindData |  |
| 2068 | `cabs` | `0xC8850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2070 | `cabsl` | `0xC8850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2071 | `cacos` | `0xC8870` | 828 | UnwindData |  |
| 2076 | `cacosl` | `0xC8BC0` | 818 | UnwindData |  |
| 2079 | `cargf` | `0xC8F00` | 30 | UnwindData |  |
| 2086 | `casinl` | `0xC8F30` | 84 | UnwindData |  |
| 2087 | `catan` | `0xC8F90` | 84 | UnwindData |  |
| 2088 | `catanf` | `0xC8FF0` | 78 | UnwindData |  |
| 2089 | `catanh` | `0xC9050` | 951 | UnwindData |  |
| 2091 | `catanhl` | `0xC9410` | 951 | UnwindData |  |
| 2092 | `catanl` | `0xC97D0` | 84 | UnwindData |  |
| 2096 | `ccos` | `0xC9830` | 66 | UnwindData |  |
| 2097 | `ccosf` | `0xC9880` | 45 | UnwindData |  |
| 2098 | `ccosh` | `0xC98C0` | 574 | UnwindData |  |
| 2099 | `ccoshf` | `0xC9B10` | 502 | UnwindData |  |
| 2100 | `ccoshl` | `0xC9D10` | 574 | UnwindData |  |
| 2101 | `ccosl` | `0xC9F60` | 66 | UnwindData |  |
| 2105 | `cexpf` | `0xC9FB0` | 538 | UnwindData |  |
| 2114 | `clog10` | `0xCA1D0` | 56 | UnwindData |  |
| 2115 | `clog10f` | `0xCA210` | 55 | UnwindData |  |
| 2116 | `clog10l` | `0xCA250` | 56 | UnwindData |  |
| 2117 | `clogf` | `0xCA290` | 710 | UnwindData |  |
| 3 | `_Cmulcr` | `0xCA560` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `_LCmulcr` | `0xCA560` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `_FCmulcr` | `0xCA590` | 40 | UnwindData |  |
| 2130 | `cpowf` | `0xCA5C0` | 169 | UnwindData |  |
| 2131 | `cpowl` | `0xCA670` | 196 | UnwindData |  |
| 2132 | `cproj` | `0xCA740` | 300 | UnwindData |  |
| 2134 | `cprojl` | `0xCA740` | 300 | UnwindData |  |
| 2133 | `cprojf` | `0xCA880` | 230 | UnwindData |  |
| 2138 | `csin` | `0xCA970` | 84 | UnwindData |  |
| 2139 | `csinf` | `0xCA9D0` | 78 | UnwindData |  |
| 2143 | `csinl` | `0xCAA30` | 84 | UnwindData |  |
| 2147 | `ctan` | `0xCAA90` | 84 | UnwindData |  |
| 2152 | `ctanl` | `0xCAA90` | 84 | UnwindData |  |
| 2148 | `ctanf` | `0xCAAF0` | 78 | UnwindData |  |
| 2149 | `ctanh` | `0xCAB50` | 570 | UnwindData |  |
| 2151 | `ctanhl` | `0xCAB50` | 570 | UnwindData |  |
| 2150 | `ctanhf` | `0xCAD90` | 463 | UnwindData |  |
| 2154 | `erf` | `0xCAF70` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2155 | `erfc` | `0xCB120` | 1,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2156 | `erfcf` | `0xCB690` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2157 | `erfcl` | `0xCB970` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2158 | `erff` | `0xCBB40` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2159 | `erfl` | `0xCBCF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `_ldexp` | `0xCBD10` | 1,122 | UnwindData |  |
| 314 | `_get_FMA3_enable` | `0xCC390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1770 | `_set_FMA3_enable` | `0xCC3B0` | 6,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2195 | `fmal` | `0xCDEE0` | 2,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `_dsin` | `0xCEA70` | 401 | UnwindData |  |
| 2265 | `lgamma` | `0xCEC10` | 2,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2266 | `lgammaf` | `0xCF720` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `_ldsin` | `0xCFDB0` | 401 | UnwindData |  |
| 2267 | `lgammal` | `0xD0230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2272 | `llrintl` | `0xD0250` | 106 | UnwindData |  |
| 2274 | `llroundf` | `0xD02C0` | 84 | UnwindData |  |
| 2293 | `lrintl` | `0xD0320` | 105 | UnwindData |  |
| 100 | `__setusermatherr` | `0xD0390` | 56 | UnwindData |  |
| 2329 | `norm` | `0xD0480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2331 | `norml` | `0xD0480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2330 | `normf` | `0xD04A0` | 36 | UnwindData |  |
| 2349 | `remainderl` | `0xD04D0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2422 | `tgamma` | `0xD0570` | 2,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2423 | `tgammaf` | `0xD0E50` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2424 | `tgammal` | `0xD1300` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `_cgets` | `0xD13F0` | 115 | UnwindData |  |
| 177 | `_cgets_s` | `0xD1470` | 272 | UnwindData |  |
| 178 | `_cgetws` | `0xD1590` | 116 | UnwindData |  |
| 179 | `_cgetws_s` | `0xD1610` | 420 | UnwindData |  |
| 57 | `__conio_common_vcprintf` | `0xD4370` | 61 | UnwindData |  |
| 58 | `__conio_common_vcprintf_p` | `0xD43C0` | 61 | UnwindData |  |
| 59 | `__conio_common_vcprintf_s` | `0xD4410` | 61 | UnwindData |  |
| 61 | `__conio_common_vcwprintf` | `0xD4460` | 61 | UnwindData |  |
| 62 | `__conio_common_vcwprintf_p` | `0xD44B0` | 61 | UnwindData |  |
| 63 | `__conio_common_vcwprintf_s` | `0xD4500` | 61 | UnwindData |  |
| 198 | `_cputs` | `0xD4550` | 120 | UnwindData |  |
| 60 | `__conio_common_vcscanf` | `0xD70B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `__conio_common_vcwscanf` | `0xD70C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `_getch` | `0xD70D0` | 48 | UnwindData |  |
| 340 | `_getch_nolock` | `0xD7110` | 365 | UnwindData |  |
| 341 | `_getche` | `0xD7290` | 48 | UnwindData |  |
| 1881 | `_ungetch` | `0xD73A0` | 52 | UnwindData |  |
| 1882 | `_ungetch_nolock` | `0xD73E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `_getwch` | `0xD7420` | 50 | UnwindData |  |
| 356 | `_getwch_nolock` | `0xD7460` | 229 | UnwindData |  |
| 357 | `_getwche` | `0xD7550` | 50 | UnwindData |  |
| 1884 | `_ungetwch` | `0xD7590` | 56 | UnwindData |  |
| 1885 | `_ungetwch_nolock` | `0xD75D0` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `_popen` | `0xD7AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1987 | `_wpopen` | `0xD7AD0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1740 | `_putch` | `0xD7B50` | 54 | UnwindData |  |
| 1741 | `_putch_nolock` | `0xD7B90` | 54 | UnwindData |  |
| 1746 | `_putwch` | `0xD7C40` | 55 | UnwindData |  |
| 270 | `_findfirst32` | `0xD8580` | 45 | UnwindData |  |
| 271 | `_findfirst32i64` | `0xD85C0` | 45 | UnwindData |  |
| 274 | `_findnext32` | `0xD8600` | 45 | UnwindData |  |
| 275 | `_findnext32i64` | `0xD8640` | 45 | UnwindData |  |
| 276 | `_findnext64` | `0xD8680` | 45 | UnwindData |  |
| 1962 | `_wfindfirst32` | `0xD86C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1963 | `_wfindfirst32i64` | `0xD86D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1964 | `_wfindfirst64` | `0xD86E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1966 | `_wfindnext32` | `0xD86F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1967 | `_wfindnext32i64` | `0xD8700` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `_fstat32` | `0xD8DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1804 | `_stat32` | `0xD8DC0` | 143 | UnwindData |  |
| 1805 | `_stat32i64` | `0xD8E60` | 143 | UnwindData |  |
| 2010 | `_wstat32` | `0xD8F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2011 | `_wstat32i64` | `0xD8F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `_chsize` | `0xD8F20` | 21 | UnwindData |  |
| 186 | `_chsize_s` | `0xD8F40` | 60 | UnwindData |  |
| 200 | `_creat` | `0xD8F90` | 63 | UnwindData |  |
| 1899 | `_wcreat` | `0xD8FE0` | 63 | UnwindData |  |
| 230 | `_eof` | `0xD9160` | 156 | UnwindData |  |
| 266 | `_filelength` | `0xD9330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `_filelengthi64` | `0xD9340` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 666 | `_mktemp_s` | `0xD9390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1983 | `_wmktemp` | `0xD93A0` | 82 | UnwindData |  |
| 1984 | `_wmktemp_s` | `0xD9400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1791 | `_sopen` | `0xD9410` | 68 | UnwindData |  |
| 204 | `_ctime32` | `0xD9740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `_ctime32_s` | `0xD9750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1945 | `_wctime32` | `0xD9760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1946 | `_wctime32_s` | `0xD9770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1947 | `_wctime64` | `0xD9780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 663 | `_mkgmtime32` | `0xD9790` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1810 | `_strdate` | `0xD98D0` | 36 | UnwindData |  |
| 1811 | `_strdate_s` | `0xD9900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2014 | `_wstrdate` | `0xD9910` | 36 | UnwindData |  |
| 1835 | `_strtime` | `0xD9A50` | 36 | UnwindData |  |
| 1836 | `_strtime_s` | `0xD9A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2016 | `_wstrtime` | `0xD9A90` | 36 | UnwindData |  |
| 1861 | `_timespec32_get` | `0xD9B60` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `_futime32` | `0xD9DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1890 | `_utime32` | `0xD9DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2033 | `_wutime32` | `0xD9DD0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1905 | `_wcsftime_l` | `0xD9E50` | 30 | UnwindData |  |
| 1766 | `_searchenv` | `0xDA030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1767 | `_searchenv_s` | `0xDA050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1995 | `_wsearchenv_s` | `0xDA060` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `_getdllprocaddr` | `0xDA570` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `_loaddll` | `0xDA5A0` | 109 | UnwindData |  |
| 1887 | `_unloaddll` | `0xDA620` | 32 | UnwindData |  |
| 233 | `_execl` | `0xDA860` | 50 | UnwindData |  |
| 234 | `_execle` | `0xDA8A0` | 50 | UnwindData |  |
| 1794 | `_spawnl` | `0xDA8E0` | 43 | UnwindData |  |
| 1795 | `_spawnle` | `0xDA920` | 43 | UnwindData |  |
| 1953 | `_wexecl` | `0xDA960` | 50 | UnwindData |  |
| 1954 | `_wexecle` | `0xDA9A0` | 50 | UnwindData |  |
| 2000 | `_wspawnl` | `0xDA9E0` | 43 | UnwindData |  |
| 2001 | `_wspawnle` | `0xDAA20` | 43 | UnwindData |  |
| 235 | `_execlp` | `0xDAB60` | 50 | UnwindData |  |
| 236 | `_execlpe` | `0xDABA0` | 50 | UnwindData |  |
| 1796 | `_spawnlp` | `0xDABE0` | 43 | UnwindData |  |
| 1797 | `_spawnlpe` | `0xDAC20` | 43 | UnwindData |  |
| 1955 | `_wexeclp` | `0xDAC60` | 50 | UnwindData |  |
| 1956 | `_wexeclpe` | `0xDACA0` | 50 | UnwindData |  |
| 2002 | `_wspawnlp` | `0xDACE0` | 43 | UnwindData |  |
| 2003 | `_wspawnlpe` | `0xDAD20` | 43 | UnwindData |  |
| 238 | `_execv` | `0xDB060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `_execve` | `0xDB080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1798 | `_spawnv` | `0xDB0A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1799 | `_spawnve` | `0xDB0B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1957 | `_wexecv` | `0xDB0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1958 | `_wexecve` | `0xDB0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2004 | `_wspawnv` | `0xDB100` | 1,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `_execvp` | `0xDB8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `_execvpe` | `0xDB8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1800 | `_spawnvp` | `0xDB900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1801 | `_spawnvpe` | `0xDB910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1959 | `_wexecvp` | `0xDB920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1960 | `_wexecvpe` | `0xDB940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2006 | `_wspawnvp` | `0xDB960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2007 | `_wspawnvpe` | `0xDB970` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2018 | `_wsystem` | `0xDBAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2416 | `system` | `0xDBAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `_heapchk` | `0xDBAF0` | 37 | UnwindData |  |
| 366 | `_heapmin` | `0xDBB20` | 33 | UnwindData |  |
| 418 | `_ismbcalnum` | `0xDBB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `_ismbcalnum_l` | `0xDBB60` | 129 | UnwindData |  |
| 394 | `_ismbbalnum` | `0xDBBF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `_ismbbalnum_l` | `0xDBC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `_ismbbalpha` | `0xDBC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `_ismbbalpha_l` | `0xDBC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `_ismbbblank` | `0xDBC70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `_ismbbblank_l` | `0xDBCA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `_ismbbgraph` | `0xDBCD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `_ismbbgraph_l` | `0xDBCF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `_ismbbkalnum` | `0xDBD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `_ismbbkalnum_l` | `0xDBD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `_ismbbkana` | `0xDBD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `_ismbbkana_l` | `0xDBD60` | 116 | UnwindData |  |
| 406 | `_ismbbkprint` | `0xDBDE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `_ismbbkprint_l` | `0xDBE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `_ismbbkpunct` | `0xDBE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `_ismbbkpunct_l` | `0xDBE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `_ismbblead_l` | `0xDBE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `_ismbbprint` | `0xDBE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `_ismbbprint_l` | `0xDBEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `_ismbbpunct` | `0xDBEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `_ismbbpunct_l` | `0xDBEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `_ismbbtrail` | `0xDBF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `_ismbbtrail_l` | `0xDBF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `_ismbcgraph` | `0xDBF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `_ismbcgraph_l` | `0xDBF50` | 137 | UnwindData |  |
| 428 | `_ismbchira` | `0xDBFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `_ismbchira_l` | `0xDBFF0` | 77 | UnwindData |  |
| 430 | `_ismbckata` | `0xDC050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `_ismbckata_l` | `0xDC060` | 85 | UnwindData |  |
| 448 | `_ismbcsymbol` | `0xDC0C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `_ismbcsymbol_l` | `0xDC0D0` | 85 | UnwindData |  |
| 438 | `_ismbclegal` | `0xDC130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `_ismbclegal_l` | `0xDC140` | 80 | UnwindData |  |
| 442 | `_ismbcprint` | `0xDC1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `_ismbcprint_l` | `0xDC1B0` | 114 | UnwindData |  |
| 422 | `_ismbcblank` | `0xDC230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `_ismbcblank_l` | `0xDC240` | 145 | UnwindData |  |
| 444 | `_ismbcpunct` | `0xDC2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `_ismbcpunct_l` | `0xDC2F0` | 134 | UnwindData |  |
| 452 | `_ismbslead` | `0xDC380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `_ismbslead_l` | `0xDC390` | 165 | UnwindData |  |
| 450 | `_ismbcupper` | `0xDC440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `_ismbcupper_l` | `0xDC450` | 93 | UnwindData |  |
| 525 | `_mbbtype` | `0xDC4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | `_mbbtype_l` | `0xDC4D0` | 231 | UnwindData |  |
| 529 | `_mbccpy_l` | `0xDC5C0` | 29 | UnwindData |  |
| 537 | `_mbclen_l` | `0xDC5F0` | 58 | UnwindData |  |
| 432 | `_ismbcl0` | `0xDC630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `_ismbcl0_l` | `0xDC640` | 97 | UnwindData |  |
| 434 | `_ismbcl1` | `0xDC6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `_ismbcl1_l` | `0xDC6C0` | 102 | UnwindData |  |
| 436 | `_ismbcl2` | `0xDC730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `_ismbcl2_l` | `0xDC740` | 102 | UnwindData |  |
| 550 | `_mbsbtype_l` | `0xDC7B0` | 234 | UnwindData |  |
| 551 | `_mbscat_s` | `0xDC8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `_mbscoll` | `0xDC8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `_mbscoll_l` | `0xDC8C0` | 227 | UnwindData |  |
| 559 | `_mbscpy_s` | `0xDC9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `_mbscpy_s_l` | `0xDC9C0` | 461 | UnwindData |  |
| 568 | `_mbsicoll` | `0xDCBA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `_mbsicoll_l` | `0xDCBB0` | 227 | UnwindData |  |
| 571 | `_mbsinc_l` | `0xDCCA0` | 54 | UnwindData |  |
| 622 | `_mbsnlen` | `0xDCCE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 623 | `_mbsnlen_l` | `0xDCCF0` | 477 | UnwindData |  |
| 575 | `_mbslwr_l` | `0xDCEE0` | 43 | UnwindData |  |
| 578 | `_mbsnbcat` | `0xDCF20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `_mbsnbcat_l` | `0xDCF30` | 362 | UnwindData |  |
| 584 | `_mbsnbcnt` | `0xDD0A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 585 | `_mbsnbcnt_l` | `0xDD0B0` | 165 | UnwindData |  |
| 586 | `_mbsnbcoll` | `0xDD160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 587 | `_mbsnbcoll_l` | `0xDD170` | 265 | UnwindData |  |
| 594 | `_mbsnbicoll` | `0xDD280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 595 | `_mbsnbicoll_l` | `0xDD290` | 280 | UnwindData |  |
| 596 | `_mbsnbset` | `0xDD3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `_mbsnbset_l` | `0xDD3C0` | 283 | UnwindData |  |
| 598 | `_mbsnbset_s` | `0xDD4F0` | 20 | UnwindData |  |
| 599 | `_mbsnbset_s_l` | `0xDD510` | 768 | UnwindData |  |
| 600 | `_mbsncat` | `0xDD820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `_mbsncat_l` | `0xDD830` | 340 | UnwindData |  |
| 602 | `_mbsncat_s` | `0xDD990` | 20 | UnwindData |  |
| 604 | `_mbsnccnt` | `0xDD9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `_mbsnccnt_l` | `0xDD9C0` | 171 | UnwindData |  |
| 606 | `_mbsncmp` | `0xDDA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `_mbsncoll` | `0xDDA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `_mbsncoll_l` | `0xDDAA0` | 332 | UnwindData |  |
| 610 | `_mbsncpy` | `0xDDC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `_mbsncpy_l` | `0xDDC10` | 266 | UnwindData |  |
| 612 | `_mbsncpy_s` | `0xDDD20` | 20 | UnwindData |  |
| 613 | `_mbsncpy_s_l` | `0xDDD40` | 613 | UnwindData |  |
| 616 | `_mbsnicmp` | `0xDDFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 618 | `_mbsnicoll` | `0xDDFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `_mbsnicoll_l` | `0xDDFD0` | 332 | UnwindData |  |
| 620 | `_mbsninc` | `0xDE130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 621 | `_mbsninc_l` | `0xDE140` | 34 | UnwindData |  |
| 624 | `_mbsnset` | `0xDE170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `_mbsnset_l` | `0xDE180` | 386 | UnwindData |  |
| 626 | `_mbsnset_s` | `0xDE310` | 20 | UnwindData |  |
| 627 | `_mbsnset_s_l` | `0xDE330` | 748 | UnwindData |  |
| 634 | `_mbsset` | `0xDE630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 635 | `_mbsset_l` | `0xDE640` | 259 | UnwindData |  |
| 636 | `_mbsset_s` | `0xDE750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 637 | `_mbsset_s_l` | `0xDE760` | 470 | UnwindData |  |
| 644 | `_mbstok` | `0xDE940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `_mbstok_l` | `0xDE950` | 62 | UnwindData |  |
| 654 | `_mbsupr` | `0xDE9A0` | 43 | UnwindData |  |
| 655 | `_mbsupr_l` | `0xDE9E0` | 43 | UnwindData |  |
| 538 | `_mbctohira` | `0xDEA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `_mbctohira_l` | `0xDEA30` | 55 | UnwindData |  |
| 540 | `_mbctokata` | `0xDEA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `_mbctokata_l` | `0xDEA80` | 41 | UnwindData |  |
| 546 | `_mbctoupper` | `0xDEAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `_mbctoupper_l` | `0xDEAC0` | 232 | UnwindData |  |
| 532 | `_mbcjistojms` | `0xDEBB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 533 | `_mbcjistojms_l` | `0xDEBC0` | 213 | UnwindData |  |
| 534 | `_mbcjmstojis` | `0xDECA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `_mbcjmstojis_l` | `0xDECB0` | 237 | UnwindData |  |
| 523 | `_mbbtombc` | `0xDEDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `_mbbtombc_l` | `0xDEDC0` | 185 | UnwindData |  |
| 544 | `_mbctombb` | `0xDEE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `_mbctombb_l` | `0xDEE90` | 221 | UnwindData |  |
| 180 | `_chdir` | `0xDF210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `_getdrives` | `0xDF220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `_getdcwd` | `0xDF230` | 14 | UnwindData |  |
| 1757 | `_resetstkoflw` | `0xDF250` | 397 | UnwindData |  |
| 1785 | `_seterrormode` | `0xDF3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `_beep` | `0xDF400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `_getsystime` | `0xDF410` | 168 | UnwindData |  |
| 1789 | `_setsystime` | `0xDF4C0` | 179 | UnwindData |  |
| 172 | `_cabs` | `0xDF580` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2128 | `coshf` | `0xDF6D0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `_logbf` | `0xDFAA0` | 194 | UnwindData |  |
| 182 | `_chgsign` | `0xDFB70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `_chgsignf` | `0xDFBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `_copysignf` | `0xDFBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `_finitef` | `0xDFBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1830 | `_strnset` | `0xDFC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1832 | `_strrev` | `0xDFC20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1833 | `_strset` | `0xDFC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `_fpieee_flt` | `0xDFC80` | 11,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `_fpclassf` | `0xE2A20` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `_isnanf` | `0xE2A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1764 | `_scalb` | `0xE2AB0` | 434 | UnwindData |  |
| 1765 | `_scalbf` | `0xE2C70` | 386 | UnwindData |  |
| 211 | `_dexp` | `0xE7CC0` | 1,122 | UnwindData |  |
| 250 | `_fdexp` | `0xE8130` | 982 | UnwindData |  |
| 385 | `_isatty` | `0xED400` | 18 | UnwindData |  |
| 75 | `__intrinsic_setjmp` | `0xED430` | 144 | UnwindData |  |
| 2371 | `setjmp` | `0xED4D0` | 5 | UnwindData |  |
| 76 | `__intrinsic_setjmpex` | `0xED4F0` | 144 | UnwindData |  |
| 2382 | `strcat` | `0xED700` | 144 | UnwindData |  |
| 2387 | `strcpy` | `0xED7A0` | 183 | UnwindData |  |
| 2385 | `strcmp` | `0xED870` | 103 | UnwindData |  |
| 2393 | `strlen` | `0xED8F0` | 168 | UnwindData |  |
| 2394 | `strncat` | `0xED9B0` | 405 | UnwindData |  |
| 2396 | `strncmp` | `0xEDB60` | 125 | UnwindData |  |
| 2397 | `strncpy` | `0xEDBF0` | 354 | UnwindData |  |
| 1612 | `_o_memset` | `0xEDD90` | 904 | UnwindData |  |
| 2314 | `memset` | `0xEDD90` | 904 | UnwindData |  |
| 2308 | `memchr` | `0xEE130` | 144 | UnwindData |  |
| 2309 | `memcmp` | `0xEE1D0` | 199 | UnwindData |  |
| 2310 | `memcpy` | `0xEE2D0` | 1,645 | UnwindData |  |
| 2312 | `memmove` | `0xEE2D0` | 1,645 | UnwindData |  |
| 2102 | `ceil` | `0xF8020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2103 | `ceilf` | `0xF8030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2191 | `floor` | `0xF8040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2192 | `floorf` | `0xF8050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2320 | `nearbyint` | `0xF8060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2321 | `nearbyintf` | `0xF8070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2322 | `nearbyintl` | `0xF8080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2356 | `rint` | `0xF8090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2357 | `rintf` | `0xF80A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2358 | `rintl` | `0xF80B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2434 | `trunc` | `0xF80C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2435 | `truncf` | `0xF80D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2436 | `truncl` | `0xF80E0` | 36,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1951 | `_wctype` | `0x100F30` | 231,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `_mbcasemap` | `0x1397E0` | 2,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `__dcrt_initial_narrow_environment` | `0x13A2A0` | 0 | Indeterminate |  |
