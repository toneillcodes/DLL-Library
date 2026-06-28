# Binary Specification: ucrtbase.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ucrtbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c2ed69b4a1bb9432c75134e813c70539e27c8c1fe96a784d9be78c874e93d9d5`
* **Total Exported Functions:** 2484

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2332 | `perror` | `0x1010` | 78 | UnwindData |  |
| 2459 | `wcsrchr` | `0x3660` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `_endthreadex` | `0x3890` | 10 | UnwindData |  |
| 503 | `_localtime64` | `0x38F0` | 72 | UnwindData |  |
| 1775 | `_set_errno` | `0x39B0` | 44 | UnwindData |  |
| 347 | `_getdrive` | `0x4B10` | 204 | UnwindData |  |
| 1906 | `_wcsicmp` | `0x54B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1916 | `_wcsnicmp` | `0x54E0` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2445 | `wcscmp` | `0x5890` | 3,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2462 | `wcsspn` | `0x6480` | 88 | UnwindData |  |
| 2444 | `wcschr` | `0x66A0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1869 | `_tzset` | `0x6810` | 42 | UnwindData |  |
| 51 | `___lc_codepage_func` | `0x6D70` | 90 | UnwindData |  |
| 1918 | `_wcsnicoll` | `0x6EF0` | 79 | UnwindData |  |
| 2077 | `calloc` | `0x6F50` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1977 | `_wgetdcwd` | `0x71C0` | 14 | UnwindData |  |
| 1975 | `_wfullpath` | `0x7650` | 14 | UnwindData |  |
| 225 | `_dupenv_s` | `0x7AA0` | 14 | UnwindData |  |
| 1976 | `_wgetcwd` | `0x7DC0` | 22 | UnwindData |  |
| 1677 | `_o_strftime` | `0x7DE0` | 28 | UnwindData |  |
| 1850 | `_strupr` | `0x7E70` | 58 | UnwindData |  |
| 1853 | `_strupr_s_l` | `0x7EB0` | 75 | UnwindData |  |
| 1820 | `_strlwr` | `0x82E0` | 94 | UnwindData |  |
| 1823 | `_strlwr_s_l` | `0x8350` | 75 | UnwindData |  |
| 68 | `__dcrt_get_wide_environment_from_os` | `0x87F0` | 131 | UnwindData |  |
| 1712 | `_o_wcsftime` | `0x9630` | 28 | UnwindData |  |
| 2392 | `strftime` | `0x98E0` | 26 | UnwindData |  |
| 1902 | `_wcsdup` | `0x9980` | 180 | UnwindData |  |
| 1910 | `_wcslwr` | `0x9A40` | 115 | UnwindData |  |
| 1913 | `_wcslwr_s_l` | `0x9AC0` | 75 | UnwindData |  |
| 23 | `_Strftime` | `0xB210` | 30 | UnwindData |  |
| 2450 | `wcsftime` | `0xB240` | 26 | UnwindData |  |
| 2472 | `wcstombs` | `0xCD80` | 87 | UnwindData |  |
| 2305 | `mbstowcs` | `0xCF20` | 87 | UnwindData |  |
| 2306 | `mbstowcs_s` | `0xD0D0` | 332 | UnwindData |  |
| 2473 | `wcstombs_s` | `0xD630` | 326 | UnwindData |  |
| 1934 | `_wcstombs_s_l` | `0xD780` | 345 | UnwindData |  |
| 2372 | `setlocale` | `0xDCC0` | 76 | UnwindData |  |
| 174 | `_calloc_base` | `0x10050` | 43 | UnwindData |  |
| 522 | `_malloc_base` | `0x10100` | 10 | UnwindData |  |
| 1750 | `_query_new_handler` | `0x10190` | 76 | UnwindData |  |
| 1779 | `_set_new_handler` | `0x10210` | 123 | UnwindData |  |
| 173 | `_callnewh` | `0x102A0` | 51 | UnwindData |  |
| 26 | `_W_Gettnames` | `0x11440` | 3,375 | UnwindData |  |
| 338 | `_getc_nolock` | `0x12260` | 66 | UnwindData |  |
| 669 | `_msize` | `0x12340` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `_fgetc_nolock` | `0x12910` | 70 | UnwindData |  |
| 231 | `_errno` | `0x12AC0` | 229 | UnwindData |  |
| 379 | `_invalid_parameter_noinfo` | `0x12BB0` | 14 | UnwindData |  |
| 1752 | `_read` | `0x12BD0` | 335 | UnwindData |  |
| 268 | `_fileno` | `0x12DA0` | 41 | UnwindData |  |
| 2186 | `fgetc` | `0x13070` | 441 | UnwindData |  |
| 333 | `_get_timezone` | `0x133C0` | 21 | UnwindData |  |
| 2388 | `strcpy_s` | `0x13480` | 120 | UnwindData |  |
| 2443 | `wcscat_s` | `0x13500` | 139 | UnwindData |  |
| 2245 | `isspace` | `0x14460` | 52 | UnwindData |  |
| 2239 | `isdigit` | `0x14680` | 18 | UnwindData |  |
| 1755 | `_register_onexit_function` | `0x147F0` | 89 | UnwindData |  |
| 731 | `_o___stdio_common_vswprintf_s` | `0x15030` | 55 | UnwindData |  |
| 1474 | `_o_bsearch` | `0x15070` | 38 | UnwindData |  |
| 2063 | `bsearch` | `0x15120` | 40 | UnwindData |  |
| 516 | `_ltoa` | `0x15320` | 205 | UnwindData |  |
| 2433 | `towupper` | `0x155F0` | 865 | UnwindData |  |
| 729 | `_o___stdio_common_vswprintf` | `0x15960` | 55 | UnwindData |  |
| 2212 | `free` | `0x15DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2297 | `malloc` | `0x15E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2252 | `iswctype` | `0x15E10` | 109 | UnwindData |  |
| 1868 | `_towupper_l` | `0x162C0` | 936 | UnwindData |  |
| 1867 | `_towlower_l` | `0x16670` | 1,726 | UnwindData |  |
| 2432 | `towlower` | `0x17620` | 1,574 | UnwindData |  |
| 2429 | `tolower` | `0x17C50` | 1,007 | UnwindData |  |
| 1864 | `_tolower_l` | `0x18050` | 1,025 | UnwindData |  |
| 118 | `__stdio_common_vsprintf` | `0x18460` | 117 | UnwindData |  |
| 120 | `__stdio_common_vsprintf_s` | `0x187F0` | 118 | UnwindData |  |
| 2474 | `wcstoul` | `0x18B20` | 112 | UnwindData |  |
| 2344 | `rand` | `0x18BA0` | 41 | UnwindData |  |
| 2235 | `isalnum` | `0x18C40` | 54 | UnwindData |  |
| 643 | `_mbsstr_l` | `0x18D10` | 43 | UnwindData |  |
| 53 | `___lc_locale_name_func` | `0x18F40` | 97 | UnwindData |  |
| 381 | `_invoke_watson` | `0x1CB90` | 66 | UnwindData |  |
| 122 | `__stdio_common_vswprintf` | `0x1CBE0` | 121 | UnwindData |  |
| 291 | `_free_base` | `0x1E0E0` | 70 | UnwindData |  |
| 124 | `__stdio_common_vswprintf_s` | `0x1FFD0` | 120 | UnwindData |  |
| 117 | `__stdio_common_vsnwprintf_s` | `0x20400` | 136 | UnwindData |  |
| 724 | `_o___stdio_common_vsnwprintf_s` | `0x208F0` | 61 | UnwindData |  |
| 2081 | `casin` | `0x209C0` | 84 | UnwindData |  |
| 2129 | `cpow` | `0x20A20` | 196 | UnwindData |  |
| 2104 | `cexp` | `0x20AF0` | 599 | UnwindData |  |
| 2075 | `cacoshl` | `0x20D50` | 894 | UnwindData |  |
| 2073 | `cacosh` | `0x210E0` | 894 | UnwindData |  |
| 2144 | `csqrt` | `0x21470` | 328 | UnwindData |  |
| 2083 | `casinh` | `0x21BE0` | 833 | UnwindData |  |
| 2113 | `clog` | `0x21F30` | 608 | UnwindData |  |
| 2118 | `clogl` | `0x221A0` | 902 | UnwindData |  |
| 2048 | `asinf` | `0x229D0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2047 | `asin` | `0x22C10` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2053 | `atan2` | `0x22E50` | 2,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2420 | `tanhf` | `0x239A0` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `_hypotf` | `0x240C0` | 269 | UnwindData |  |
| 368 | `_hypot` | `0x241E0` | 135 | UnwindData |  |
| 2040 | `acos` | `0x24430` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `_logb` | `0x247B0` | 248 | UnwindData |  |
| 2049 | `asinh` | `0x248E0` | 227 | UnwindData |  |
| 2379 | `sqrt` | `0x249D0` | 195 | UnwindData |  |
| 2056 | `atanh` | `0x24AA0` | 212 | UnwindData |  |
| 2280 | `log1p` | `0x24B80` | 237 | UnwindData |  |
| 2283 | `log2` | `0x24DE0` | 823 | UnwindData |  |
| 2380 | `sqrtf` | `0x253C0` | 151 | UnwindData |  |
| 232 | `_except1` | `0x25460` | 241 | UnwindData |  |
| 2203 | `fmodf` | `0x25700` | 816 | UnwindData |  |
| 2145 | `csqrtf` | `0x264E0` | 408 | UnwindData |  |
| 2263 | `ldexp` | `0x26BB0` | 69 | UnwindData |  |
| 2084 | `casinhf` | `0x26D40` | 786 | UnwindData |  |
| 2054 | `atan2f` | `0x27060` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2050 | `asinhf` | `0x27860` | 205 | UnwindData |  |
| 2057 | `atanhf` | `0x27940` | 181 | UnwindData |  |
| 2281 | `log1pf` | `0x27A00` | 199 | UnwindData |  |
| 2090 | `catanhf` | `0x27AD0` | 807 | UnwindData |  |
| 2146 | `csqrtl` | `0x27E00` | 484 | UnwindData |  |
| 2058 | `atanhl` | `0x28600` | 226 | UnwindData |  |
| 2364 | `scalblnl` | `0x286F0` | 444 | UnwindData |  |
| 2365 | `scalbn` | `0x286F0` | 444 | UnwindData |  |
| 2367 | `scalbnl` | `0x286F0` | 444 | UnwindData |  |
| 492 | `_ldscale` | `0x288C0` | 337 | UnwindData |  |
| 2051 | `asinhl` | `0x28A20` | 229 | UnwindData |  |
| 2351 | `remquo` | `0x28B10` | 1,229 | UnwindData |  |
| 222 | `_dunscale` | `0x28FF0` | 218 | UnwindData |  |
| 2095 | `cbrtl` | `0x290D0` | 1,014 | UnwindData |  |
| 2093 | `cbrt` | `0x294D0` | 1,014 | UnwindData |  |
| 218 | `_dscale` | `0x298D0` | 321 | UnwindData |  |
| 215 | `_dnorm` | `0x29A20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2353 | `remquol` | `0x29AA0` | 1,259 | UnwindData |  |
| 2282 | `log1pl` | `0x29FA0` | 248 | UnwindData |  |
| 2294 | `lround` | `0x2A0A0` | 107 | UnwindData |  |
| 2296 | `lroundl` | `0x2A0A0` | 107 | UnwindData |  |
| 2273 | `llround` | `0x2A120` | 108 | UnwindData |  |
| 2275 | `llroundl` | `0x2A120` | 108 | UnwindData |  |
| 214 | `_dlog` | `0x2A1A0` | 619 | UnwindData |  |
| 2271 | `llrintf` | `0x2A420` | 86 | UnwindData |  |
| 2327 | `nexttowardf` | `0x2A480` | 300 | UnwindData |  |
| 2181 | `fesetenv` | `0x2A5C0` | 112 | UnwindData |  |
| 2175 | `fegetenv` | `0x2A640` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2174 | `feclearexcept` | `0x2A790` | 83 | UnwindData |  |
| 256 | `_fdscale` | `0x2A7F0` | 296 | UnwindData |  |
| 2094 | `cbrtf` | `0x2A920` | 143 | UnwindData |  |
| 251 | `_fdlog` | `0x2AC90` | 532 | UnwindData |  |
| 252 | `_fdnorm` | `0x2AEB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2270 | `llrint` | `0x2AF00` | 108 | UnwindData |  |
| 2291 | `lrint` | `0x2AF80` | 107 | UnwindData |  |
| 2292 | `lrintf` | `0x2B070` | 85 | UnwindData |  |
| 2295 | `lroundf` | `0x2B0D0` | 85 | UnwindData |  |
| 2184 | `fetestexcept` | `0x2B130` | 30 | UnwindData |  |
| 2176 | `fegetexceptflag` | `0x2B160` | 55 | UnwindData |  |
| 2182 | `fesetexceptflag` | `0x2B250` | 158 | UnwindData |  |
| 72 | `__fpe_flt_rounds` | `0x2C030` | 62 | UnwindData |  |
| 2177 | `fegetround` | `0x2C080` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2183 | `fesetround` | `0x2C0C0` | 140 | UnwindData |  |
| 195 | `_controlfp_s` | `0x2C250` | 105 | UnwindData |  |
| 110 | `__stdio_common_vfprintf_s` | `0x33210` | 109 | UnwindData |  |
| 112 | `__stdio_common_vfwprintf` | `0x34510` | 109 | UnwindData |  |
| 108 | `__stdio_common_vfprintf` | `0x34620` | 109 | UnwindData |  |
| 2207 | `fputs` | `0x34730` | 85 | UnwindData |  |
| 515 | `_lseeki64` | `0x356F0` | 87 | UnwindData |  |
| 114 | `__stdio_common_vfwprintf_s` | `0x35750` | 245 | UnwindData |  |
| 2337 | `puts` | `0x35CB0` | 376 | UnwindData |  |
| 2219 | `fwrite` | `0x35F90` | 219 | UnwindData |  |
| 302 | `_ftelli64` | `0x367E0` | 87 | UnwindData |  |
| 2185 | `fflush` | `0x368D0` | 88 | UnwindData |  |
| 261 | `_fflush_nolock` | `0x36A50` | 231 | UnwindData |  |
| 326 | `_get_osfhandle` | `0x374D0` | 138 | UnwindData |  |
| 2187 | `fgetpos` | `0x37E90` | 75 | UnwindData |  |
| 294 | `_fseeki64` | `0x38190` | 85 | UnwindData |  |
| 2206 | `fputc` | `0x38250` | 86 | UnwindData |  |
| 2216 | `fseek` | `0x38440` | 88 | UnwindData |  |
| 2210 | `fread` | `0x38720` | 32 | UnwindData |  |
| 2211 | `fread_s` | `0x38750` | 172 | UnwindData |  |
| 290 | `_fread_nolock_s` | `0x38810` | 53 | UnwindData |  |
| 70 | `__doserrno` | `0x38F70` | 35 | UnwindData |  |
| 2218 | `ftell` | `0x39240` | 85 | UnwindData |  |
| 1999 | `_wsopen_s` | `0x3A6C0` | 50 | UnwindData |  |
| 514 | `_lseek` | `0x3AF30` | 85 | UnwindData |  |
| 1985 | `_wopen` | `0x3AF90` | 35 | UnwindData |  |
| 1734 | `_open_osfhandle` | `0x3B180` | 275 | UnwindData |  |
| 1793 | `_sopen_s` | `0x3B2A0` | 50 | UnwindData |  |
| 1971 | `_wfopen_s` | `0x3B3C0` | 90 | UnwindData |  |
| 2205 | `fopen_s` | `0x3B420` | 90 | UnwindData |  |
| 554 | `_mbschr_l` | `0x3CBA0` | 232 | UnwindData |  |
| 2384 | `strchr` | `0x3CC90` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1828 | `_strnicoll` | `0x3D120` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1754 | `_recalloc` | `0x3D1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1753 | `_realloc_base` | `0x3D200` | 130 | UnwindData |  |
| 1751 | `_query_new_mode` | `0x3D290` | 25 | UnwindData |  |
| 1780 | `_set_new_mode` | `0x3D2B0` | 57 | UnwindData |  |
| 1743 | `_putenv_s` | `0x3D610` | 56 | UnwindData |  |
| 1732 | `_o_wmemmove_s` | `0x3D650` | 35 | UnwindData |  |
| 1242 | `_o__splitpath_s` | `0x3DA40` | 90 | UnwindData |  |
| 1802 | `_splitpath` | `0x3DB50` | 105 | UnwindData |  |
| 1713 | `_o_wcsncat_s` | `0x3DBC0` | 35 | UnwindData |  |
| 1803 | `_splitpath_s` | `0x3DEA0` | 96 | UnwindData |  |
| 590 | `_mbsnbcpy_s` | `0x3E1E0` | 20 | UnwindData |  |
| 591 | `_mbsnbcpy_s_l` | `0x3E200` | 458 | UnwindData |  |
| 1714 | `_o_wcsncpy_s` | `0x3E3D0` | 35 | UnwindData |  |
| 1731 | `_o_wmemcpy_s` | `0x3E400` | 35 | UnwindData |  |
| 2456 | `wcsncpy_s` | `0x3E4E0` | 313 | UnwindData |  |
| 2483 | `wmemcpy_s` | `0x3E620` | 133 | UnwindData |  |
| 629 | `_mbspbrk_l` | `0x3E7C0` | 170 | UnwindData |  |
| 2400 | `strpbrk` | `0x3E870` | 73 | UnwindData |  |
| 506 | `_lock_locales` | `0x3F7D0` | 591 | UnwindData |  |
| 123 | `__stdio_common_vswprintf_p` | `0x42630` | 124 | UnwindData |  |
| 119 | `__stdio_common_vsprintf_p` | `0x48820` | 124 | UnwindData |  |
| 1915 | `_wcsncoll_l` | `0x4A990` | 238 | UnwindData |  |
| 1909 | `_wcsicoll_l` | `0x4AA90` | 200 | UnwindData |  |
| 1919 | `_wcsnicoll_l` | `0x4ABC0` | 234 | UnwindData |  |
| 1917 | `_wcsnicmp_l` | `0x4ACB0` | 68 | UnwindData |  |
| 1829 | `_strnicoll_l` | `0x4AFA0` | 309 | UnwindData |  |
| 1827 | `_strnicmp_l` | `0x4B0E0` | 177 | UnwindData |  |
| 1901 | `_wcscoll_l` | `0x4B1A0` | 219 | UnwindData |  |
| 1635 | `_o_qsort_s` | `0x4B6A0` | 38 | UnwindData |  |
| 319 | `_get_errno` | `0x4B7D0` | 47 | UnwindData |  |
| 237 | `_execute_onexit_table` | `0x4B810` | 67 | UnwindData |  |
| 1475 | `_o_bsearch_s` | `0x4B960` | 48 | UnwindData |  |
| 2064 | `bsearch_s` | `0x4BA20` | 40 | UnwindData |  |
| 2341 | `qsort_s` | `0x4C360` | 189 | UnwindData |  |
| 1634 | `_o_qsort` | `0x4C8E0` | 28 | UnwindData |  |
| 2340 | `qsort` | `0x4C980` | 164 | UnwindData |  |
| 2439 | `ungetwc` | `0x4DF90` | 110 | UnwindData |  |
| 1883 | `_ungetwc_nolock` | `0x4E010` | 254 | UnwindData |  |
| 2189 | `fgetwc` | `0x4EAC0` | 94 | UnwindData |  |
| 264 | `_fgetwc_nolock` | `0x4EC30` | 619 | UnwindData |  |
| 2438 | `ungetc` | `0x4EEB0` | 104 | UnwindData |  |
| 1880 | `_ungetc_nolock` | `0x4EF20` | 300 | UnwindData |  |
| 1927 | `_wcstoi64` | `0x51080` | 116 | UnwindData |  |
| 2466 | `wcstoimax` | `0x51080` | 116 | UnwindData |  |
| 2471 | `wcstoll` | `0x51080` | 116 | UnwindData |  |
| 1935 | `_wcstoui64` | `0x51100` | 114 | UnwindData |  |
| 2475 | `wcstoull` | `0x51100` | 114 | UnwindData |  |
| 2476 | `wcstoumax` | `0x51100` | 114 | UnwindData |  |
| 2025 | `_wtoi64` | `0x51BC0` | 114 | UnwindData |  |
| 2030 | `_wtoll` | `0x51BC0` | 114 | UnwindData |  |
| 2412 | `strtoul` | `0x54750` | 114 | UnwindData |  |
| 2060 | `atoi` | `0x54810` | 112 | UnwindData |  |
| 2061 | `atol` | `0x54810` | 112 | UnwindData |  |
| 2409 | `strtol` | `0x55860` | 112 | UnwindData |  |
| 95 | `__pctype_func` | `0x56420` | 90 | UnwindData |  |
| 1845 | `_strtoui64` | `0x565D0` | 116 | UnwindData |  |
| 2413 | `strtoull` | `0x565D0` | 116 | UnwindData |  |
| 2414 | `strtoumax` | `0x565D0` | 116 | UnwindData |  |
| 1423 | `_o__wsplitpath_s` | `0x5B9C0` | 90 | UnwindData |  |
| 2009 | `_wsplitpath_s` | `0x5BAD0` | 96 | UnwindData |  |
| 201 | `_create_locale` | `0x5BEC0` | 119 | UnwindData |  |
| 1900 | `_wcreate_locale` | `0x5BFA0` | 329 | UnwindData |  |
| 292 | `_free_locale` | `0x5C200` | 174 | UnwindData |  |
| 2454 | `wcsncmp` | `0x5E4A0` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2008 | `_wsplitpath` | `0x5F0E0` | 105 | UnwindData |  |
| 2449 | `wcscspn` | `0x5F400` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2258 | `iswspace` | `0x5F730` | 107 | UnwindData |  |
| 2333 | `pow` | `0x5F7B0` | 3,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `_finite` | `0x604A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2399 | `strnlen` | `0x60520` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2457 | `wcsnlen` | `0x60680` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `_fdclass` | `0x60890` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2244 | `ispunct` | `0x608E0` | 52 | UnwindData |  |
| 2246 | `isupper` | `0x609B0` | 52 | UnwindData |  |
| 2261 | `isxdigit` | `0x60A80` | 54 | UnwindData |  |
| 2236 | `isalpha` | `0x60B50` | 54 | UnwindData |  |
| 389 | `_isctype_l` | `0x60C20` | 269 | UnwindData |  |
| 1759 | `_rmtmp` | `0x61050` | 167 | UnwindData |  |
| 244 | `_fclose_nolock` | `0x61100` | 85 | UnwindData |  |
| 1736 | `_pipe` | `0x61310` | 752 | UnwindData |  |
| 1735 | `_pclose` | `0x61610` | 220 | UnwindData |  |
| 208 | `_cwait` | `0x61700` | 178 | UnwindData |  |
| 2373 | `setvbuf` | `0x61BE0` | 90 | UnwindData |  |
| 188 | `_close` | `0x61EA0` | 85 | UnwindData |  |
| 2170 | `fclose` | `0x61F00` | 85 | UnwindData |  |
| 245 | `_fcloseall` | `0x622C0` | 201 | UnwindData |  |
| 2428 | `tmpnam_s` | `0x62980` | 59 | UnwindData |  |
| 142 | `_access` | `0x62F90` | 18 | UnwindData |  |
| 143 | `_access_s` | `0x62FB0` | 149 | UnwindData |  |
| 1892 | `_waccess` | `0x63050` | 18 | UnwindData |  |
| 1893 | `_waccess_s` | `0x63070` | 189 | UnwindData |  |
| 1952 | `_wdupenv_s` | `0x63350` | 14 | UnwindData |  |
| 631 | `_mbsrchr_l` | `0x63690` | 273 | UnwindData |  |
| 2401 | `strrchr` | `0x637B0` | 3,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `_W_Getdays` | `0x643C0` | 521 | UnwindData |  |
| 25 | `_W_Getmonths` | `0x647B0` | 872 | UnwindData |  |
| 2430 | `toupper` | `0x64D10` | 114 | UnwindData |  |
| 1008 | `_o__itow_s` | `0x64EA0` | 27 | UnwindData |  |
| 481 | `_itow_s` | `0x64F40` | 64 | UnwindData |  |
| 1874 | `_ultoa` | `0x653F0` | 35 | UnwindData |  |
| 478 | `_itoa` | `0x65420` | 50 | UnwindData |  |
| 1525 | `_o_free` | `0x65900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | `_o___stdio_common_vsnprintf_s` | `0x65920` | 60 | UnwindData |  |
| 116 | `__stdio_common_vsnprintf_s` | `0x65A00` | 136 | UnwindData |  |
| 1907 | `_wcsicmp_l` | `0x65E50` | 55 | UnwindData |  |
| 1876 | `_ultow` | `0x663A0` | 35 | UnwindData |  |
| 480 | `_itow` | `0x66430` | 48 | UnwindData |  |
| 518 | `_ltow` | `0x66430` | 48 | UnwindData |  |
| 1042 | `_o__ltow_s` | `0x66580` | 27 | UnwindData |  |
| 519 | `_ltow_s` | `0x66610` | 34 | UnwindData |  |
| 1344 | `_o__wcsnicmp` | `0x667A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1600 | `_o_malloc` | `0x667C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2448 | `wcscpy_s` | `0x667E0` | 129 | UnwindData |  |
| 2260 | `iswxdigit` | `0x66C30` | 109 | UnwindData |  |
| 1307 | `_o__ultow_s` | `0x68260` | 27 | UnwindData |  |
| 1877 | `_ultow_s` | `0x68300` | 63 | UnwindData |  |
| 2248 | `iswalpha` | `0x68450` | 109 | UnwindData |  |
| 210 | `_dclass` | `0x68520` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 487 | `_ldclass` | `0x68520` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `_dtest` | `0x68590` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `_ldtest` | `0x68590` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `_o__msize` | `0x685F0` | 3,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `_aligned_free` | `0x69250` | 27 | UnwindData |  |
| 145 | `_aligned_malloc` | `0x69280` | 23 | UnwindData |  |
| 146 | `_aligned_msize` | `0x69320` | 101 | UnwindData |  |
| 150 | `_aligned_realloc` | `0x69390` | 144 | UnwindData |  |
| 151 | `_aligned_recalloc` | `0x695A0` | 622 | UnwindData |  |
| 147 | `_aligned_offset_malloc` | `0x69820` | 204 | UnwindData |  |
| 243 | `_expand` | `0x69A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1940 | `_wcsupr` | `0x69A40` | 100 | UnwindData |  |
| 1943 | `_wcsupr_s_l` | `0x69AB0` | 75 | UnwindData |  |
| 1889 | `_unlock_locales` | `0x6A5C0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1566 | `_o_iswspace` | `0x6A7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2458 | `wcspbrk` | `0x6A7F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `_isnan` | `0x6A880` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1702 | `_o_towlower` | `0x6A8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1703 | `_o_towupper` | `0x6A8E0` | 2,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `_o__ui64tow_s` | `0x6B0F0` | 28 | UnwindData |  |
| 1873 | `_ui64tow_s` | `0x6B190` | 52 | UnwindData |  |
| 1334 | `_o__wcsicmp` | `0x6B2D0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1611 | `_o_memcpy_s` | `0x6B480` | 28 | UnwindData |  |
| 2463 | `wcsstr` | `0x6B5C0` | 561 | UnwindData |  |
| 463 | `_iswalpha_l` | `0x6B800` | 109 | UnwindData |  |
| 476 | `_iswxdigit_l` | `0x6CAB0` | 109 | UnwindData |  |
| 2284 | `log2f` | `0x6CC50` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1678 | `_o_strncat_s` | `0x6CD30` | 35 | UnwindData |  |
| 1679 | `_o_strncpy_s` | `0x6CD60` | 35 | UnwindData |  |
| 2479 | `wctomb` | `0x6CE10` | 148 | UnwindData |  |
| 54 | `___mb_cur_max_func` | `0x6CF10` | 90 | UnwindData |  |
| 2276 | `localeconv` | `0x6DEB0` | 98 | UnwindData |  |
| 2259 | `iswupper` | `0x6DF90` | 107 | UnwindData |  |
| 372 | `_i64tow` | `0x6E010` | 51 | UnwindData |  |
| 1872 | `_ui64tow` | `0x6E050` | 35 | UnwindData |  |
| 1264 | `_o__strnicmp` | `0x6E1B0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `_ld_int` | `0x6E2E0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `_get_daylight` | `0x6E390` | 66 | UnwindData |  |
| 77 | `__isascii` | `0x6E3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2039 | `abs` | `0x6E400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2262 | `labs` | `0x6E400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `_get_dstbias` | `0x6E410` | 66 | UnwindData |  |
| 932 | `_o__i64tow_s` | `0x6E460` | 28 | UnwindData |  |
| 373 | `_i64tow_s` | `0x6E4F0` | 35 | UnwindData |  |
| 1511 | `_o_floorf` | `0x6E680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `_lock_file` | `0x6E6A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `_initterm` | `0x6E6E0` | 56 | UnwindData |  |
| 259 | `_fdtest` | `0x6E720` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2451 | `wcslen` | `0x6E770` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `_ecvt` | `0x6E880` | 92 | UnwindData |  |
| 247 | `_fcvt_s` | `0x6E980` | 122 | UnwindData |  |
| 246 | `_fcvt` | `0x6EA00` | 92 | UnwindData |  |
| 562 | `_mbscspn_l` | `0x6F1A0` | 275 | UnwindData |  |
| 2389 | `strcspn` | `0x6F2C0` | 70 | UnwindData |  |
| 556 | `_mbscmp_l` | `0x6F670` | 376 | UnwindData |  |
| 1639 | `_o_realloc` | `0x6F7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2238 | `iscntrl` | `0x6F810` | 156 | UnwindData |  |
| 227 | `_ecvt_s` | `0x6F8C0` | 686 | UnwindData |  |
| 2065 | `btowc` | `0x6FC40` | 155 | UnwindData |  |
| 2304 | `mbsrtowcs_s` | `0x6FCF0` | 122 | UnwindData |  |
| 2299 | `mbrlen` | `0x6FE80` | 125 | UnwindData |  |
| 2302 | `mbrtowc` | `0x70080` | 163 | UnwindData |  |
| 224 | `_dup2` | `0x70930` | 85 | UnwindData |  |
| 2153 | `div` | `0x710A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2264 | `ldiv` | `0x710A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2112 | `clock` | `0x710C0` | 131 | UnwindData |  |
| 1700 | `_o_tolower` | `0x71150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1335 | `_o__wcsicmp_l` | `0x71170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1730 | `_o_wctomb_s` | `0x71190` | 29 | UnwindData |  |
| 2480 | `wctomb_s` | `0x71220` | 91 | UnwindData |  |
| 565 | `_mbsdup` | `0x71290` | 158 | UnwindData |  |
| 1812 | `_strdup` | `0x71290` | 158 | UnwindData |  |
| 1701 | `_o_toupper` | `0x713B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `_difftime64` | `0x71420` | 46 | UnwindData |  |
| 2315 | `modf` | `0x714B0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1996 | `_wsetlocale` | `0x715D0` | 60 | UnwindData |  |
| 388 | `_isctype` | `0x71620` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1888 | `_unlock_file` | `0x71660` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `_o__ltoa` | `0x717D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2316 | `modff` | `0x71840` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2242 | `islower` | `0x719A0` | 156 | UnwindData |  |
| 570 | `_mbsinc` | `0x71A90` | 14 | UnwindData |  |
| 2247 | `iswalnum` | `0x71C40` | 103 | UnwindData |  |
| 216 | `_dpcomp` | `0x71CB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `__strncnt` | `0x71D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2041 | `acosf` | `0x71D50` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `_iswupper_l` | `0x71F90` | 107 | UnwindData |  |
| 170 | `_byteswap_ushort` | `0x72010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1720 | `_o_wcstok_s` | `0x72020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `_ismbblead` | `0x72040` | 64 | UnwindData |  |
| 1980 | `_wmakepath` | `0x72090` | 39 | UnwindData |  |
| 56 | `__acrt_iob_func` | `0x722A0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2024 | `_wtoi` | `0x72400` | 112 | UnwindData |  |
| 2028 | `_wtol` | `0x72400` | 112 | UnwindData |  |
| 1568 | `_o_iswxdigit` | `0x72480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1532 | `_o_fwrite` | `0x724A0` | 35 | UnwindData |  |
| 1866 | `_toupper_l` | `0x72650` | 363 | UnwindData |  |
| 462 | `_iswalnum_l` | `0x727D0` | 103 | UnwindData |  |
| 725 | `_o___stdio_common_vsprintf` | `0x72840` | 55 | UnwindData |  |
| 727 | `_o___stdio_common_vsprintf_s` | `0x72880` | 55 | UnwindData |  |
| 1553 | `_o_isspace` | `0x728C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `_lrotl` | `0x728E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1760 | `_rotl` | `0x728E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2469 | `wcstol` | `0x72960` | 114 | UnwindData |  |
| 1556 | `_o_iswalpha` | `0x729E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `_o__stricmp` | `0x72A00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1477 | `_o_calloc` | `0x72A60` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 567 | `_mbsicmp_l` | `0x72B40` | 737 | UnwindData |  |
| 1817 | `_stricmp_l` | `0x72E30` | 161 | UnwindData |  |
| 2197 | `fmaxf` | `0x72F30` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `_byteswap_ulong` | `0x72FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `_o_floor` | `0x72FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2403 | `strstr` | `0x73000` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `_initterm_e` | `0x73220` | 148 | UnwindData |  |
| 2200 | `fminf` | `0x73460` | 1,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `_o__itoa_s` | `0x73BB0` | 27 | UnwindData |  |
| 1040 | `_o__ltoa_s` | `0x73C40` | 27 | UnwindData |  |
| 517 | `_ltoa_s` | `0x73CD0` | 34 | UnwindData |  |
| 479 | `_itoa_s` | `0x73D00` | 32 | UnwindData |  |
| 1305 | `_o__ultoa_s` | `0x73D30` | 27 | UnwindData |  |
| 1875 | `_ultoa_s` | `0x73DC0` | 19 | UnwindData |  |
| 580 | `_mbsnbcat_s` | `0x73ED0` | 20 | UnwindData |  |
| 581 | `_mbsnbcat_s_l` | `0x73EF0` | 881 | UnwindData |  |
| 1523 | `_o_fread` | `0x74760` | 35 | UnwindData |  |
| 574 | `_mbslwr` | `0x74790` | 43 | UnwindData |  |
| 577 | `_mbslwr_s_l` | `0x747D0` | 792 | UnwindData |  |
| 2345 | `rand_s` | `0x74B40` | 71 | UnwindData |  |
| 2052 | `atan` | `0x74BF0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2215 | `frexp` | `0x74EA0` | 280 | UnwindData |  |
| 1726 | `_o_wcstoul` | `0x74FC0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | `_o__hypotf` | `0x75060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2253 | `iswdigit` | `0x75080` | 100 | UnwindData |  |
| 1670 | `_o_sqrtf` | `0x750F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1544 | `_o_isalpha` | `0x75110` | 1,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2169 | `fabs` | `0x75750` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2419 | `tanh` | `0x757D0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1547 | `_o_isdigit` | `0x75BA0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `_ldpcomp` | `0x75C00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1870 | `_ui64toa` | `0x75C80` | 35 | UnwindData |  |
| 370 | `_i64toa` | `0x75CB0` | 51 | UnwindData |  |
| 1569 | `_o_isxdigit` | `0x75DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `_fpclass` | `0x75DF0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1653 | `_o_roundf` | `0x75E90` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `_o__register_onexit_function` | `0x75F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `_byteswap_uint64` | `0x75F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1499 | `_o_expf` | `0x75F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2209 | `fputws` | `0x75FA0` | 195 | UnwindData |  |
| 367 | `_heapwalk` | `0x76B40` | 204 | UnwindData |  |
| 1481 | `_o_ceilf` | `0x76C70` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2455 | `wcsncpy` | `0x76F10` | 532 | UnwindData |  |
| 2243 | `isprint` | `0x77380` | 161 | UnwindData |  |
| 1543 | `_o_isalnum` | `0x776F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `_o_logf` | `0x77710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1711 | `_o_wcscpy_s` | `0x77730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 939 | `_o__isctype` | `0x77750` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `_o_fgetc` | `0x777F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `_lrotr` | `0x77810` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1762 | `_rotr` | `0x77810` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 809 | `_o__errno` | `0x77BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2055 | `atanf` | `0x77BC0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2404 | `strtod` | `0x77F40` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2410 | `strtold` | `0x77F40` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2461 | `wcsrtombs_s` | `0x78070` | 303 | UnwindData |  |
| 203 | `_crt_atexit` | `0x786D0` | 76 | UnwindData |  |
| 1223 | `_o__set_errno` | `0x78730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2468 | `wcstok_s` | `0x78750` | 56 | UnwindData |  |
| 2442 | `wcscat` | `0x78790` | 301 | UnwindData |  |
| 2447 | `wcscpy` | `0x788D0` | 317 | UnwindData |  |
| 1666 | `_o_sinf` | `0x78A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `_o___stdio_common_vswscanf` | `0x78A40` | 48 | UnwindData |  |
| 125 | `__stdio_common_vswscanf` | `0x78B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1552 | `_o_ispunct` | `0x78B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `_initialize_onexit_table` | `0x78B30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `_o_lrintf` | `0x78B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1839 | `_strtoi64` | `0x78B80` | 116 | UnwindData |  |
| 2406 | `strtoimax` | `0x78B80` | 116 | UnwindData |  |
| 2411 | `strtoll` | `0x78B80` | 116 | UnwindData |  |
| 660 | `_memicmp` | `0x78C60` | 124 | UnwindData |  |
| 1485 | `_o_cosf` | `0x78CF0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2440 | `wcrtomb` | `0x78D70` | 58 | UnwindData |  |
| 2441 | `wcrtomb_s` | `0x78DB0` | 103 | UnwindData |  |
| 52 | `___lc_collate_cp_func` | `0x790E0` | 47 | UnwindData |  |
| 1554 | `_o_isupper` | `0x79120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `_o_log` | `0x79140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2163 | `exp2f` | `0x79160` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2346 | `realloc` | `0x792D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1627 | `_o_pow` | `0x792E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1361 | `_o__wcstoui64` | `0x79300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1727 | `_o_wcstoull` | `0x79300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `_gmtime64` | `0x79320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | `_o__i64toa_s` | `0x79330` | 28 | UnwindData |  |
| 1301 | `_o__ui64toa_s` | `0x793C0` | 28 | UnwindData |  |
| 371 | `_i64toa_s` | `0x79450` | 35 | UnwindData |  |
| 1871 | `_ui64toa_s` | `0x79480` | 19 | UnwindData |  |
| 1354 | `_o__wcstoi64` | `0x79530` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1723 | `_o_wcstoll` | `0x79530` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `_o__ecvt_s` | `0x795A0` | 55 | UnwindData |  |
| 739 | `_o__aligned_malloc` | `0x79720` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `_beginthread` | `0x797A0` | 177 | UnwindData |  |
| 760 | `_o__beginthreadex` | `0x79860` | 46 | UnwindData |  |
| 167 | `_beginthreadex` | `0x79910` | 189 | UnwindData |  |
| 2237 | `isblank` | `0x79A40` | 21 | UnwindData |  |
| 1708 | `_o_wcscat_s` | `0x79B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `_makepath` | `0x79B20` | 39 | UnwindData |  |
| 564 | `_mbsdec_l` | `0x79CE0` | 167 | UnwindData |  |
| 1555 | `_o_iswalnum` | `0x79D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1401 | `_o__wmakepath_s` | `0x79DB0` | 48 | UnwindData |  |
| 1981 | `_wmakepath_s` | `0x79E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1860 | `_time64` | `0x79E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1859 | `_time32` | `0x79E90` | 120 | UnwindData |  |
| 1669 | `_o_sqrt` | `0x79F50` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2307 | `mbtowc` | `0x79FD0` | 85 | UnwindData |  |
| 193 | `_control87` | `0x7A030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1665 | `_o_sin` | `0x7A040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `_o___stdio_common_vfwprintf` | `0x7A060` | 45 | UnwindData |  |
| 721 | `_o___stdio_common_vfwprintf_s` | `0x7A0A0` | 45 | UnwindData |  |
| 884 | `_o__get_errno` | `0x7A150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2123 | `copysignf` | `0x7A170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 893 | `_o__get_stream_buffer_pointers` | `0x7A190` | 28 | UnwindData |  |
| 330 | `_get_stream_buffer_pointers` | `0x7A220` | 71 | UnwindData |  |
| 682 | `_o____lc_locale_name_func` | `0x7A270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2313 | `memmove_s` | `0x7A290` | 81 | UnwindData |  |
| 738 | `_o__aligned_free` | `0x7A2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1436 | `_o__wtoi` | `0x7A310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1583 | `_o_log10f` | `0x7A330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2240 | `isgraph` | `0x7A350` | 161 | UnwindData |  |
| 647 | `_mbstok_s_l` | `0x7A540` | 483 | UnwindData |  |
| 2408 | `strtok_s` | `0x7A790` | 57 | UnwindData |  |
| 1788 | `_setmode` | `0x7A9A0` | 338 | UnwindData |  |
| 306 | `_ftime64` | `0x7ABE0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `_ftime64_s` | `0x7ABE0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1279 | `_o__strtoui64` | `0x7AE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1688 | `_o_strtoull` | `0x7AE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1567 | `_o_iswupper` | `0x7AEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2208 | `fputwc` | `0x7AED0` | 87 | UnwindData |  |
| 680 | `_o____lc_codepage_func` | `0x7AFD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 718 | `_o___stdio_common_vfscanf` | `0x7B030` | 45 | UnwindData |  |
| 715 | `_o___stdio_common_vfprintf` | `0x7B070` | 45 | UnwindData |  |
| 2022 | `_wtof` | `0x7B190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `_o__wcslwr` | `0x7B1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1784 | `_set_thread_local_invalid_parameter_handler` | `0x7B1C0` | 37 | UnwindData |  |
| 639 | `_mbsspn_l` | `0x7B1F0` | 117 | UnwindData |  |
| 2402 | `strspn` | `0x7B270` | 1,263 | UnwindData |  |
| 1684 | `_o_strtol` | `0x7B800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `_o____mb_cur_max_func` | `0x7B820` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1663 | `_o_setlocale` | `0x7B970` | 1,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `_gmtime64_s` | `0x7BEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2196 | `fmax` | `0x7BF00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 934 | `_o__initialize_onexit_table` | `0x7BF80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1561 | `_o_iswdigit` | `0x7BFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2298 | `mblen` | `0x7C000` | 85 | UnwindData |  |
| 134 | `__unDName` | `0x7C870` | 39 | UnwindData |  |
| 135 | `__unDNameEx` | `0x7C8A0` | 183 | UnwindData |  |
| 1674 | `_o_strcpy_s` | `0x7E350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2199 | `fmin` | `0x7E370` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `_clearfp` | `0x7E540` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `_o__recalloc` | `0x7E5B0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `_o___stdio_common_vsscanf` | `0x7E710` | 48 | UnwindData |  |
| 121 | `__stdio_common_vsscanf` | `0x7E7D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `_fdsign` | `0x7E7E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1559 | `_o_iswcntrl` | `0x7E7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2198 | `fmaxl` | `0x7E810` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2162 | `exp2` | `0x7E890` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `_o__calloc_base` | `0x7E9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1480 | `_o_ceil` | `0x7EA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `_o__gcvt_s` | `0x7EA30` | 28 | UnwindData |  |
| 312 | `_gcvt` | `0x7EB20` | 44 | UnwindData |  |
| 313 | `_gcvt_s` | `0x7EB60` | 90 | UnwindData |  |
| 1628 | `_o_powf` | `0x7ED90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1582 | `_o_log10` | `0x7EDB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1721 | `_o_wcstol` | `0x7EDD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1637 | `_o_rand` | `0x7EDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2201 | `fminl` | `0x7EE10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1808 | `_statusfp` | `0x7EE90` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 858 | `_o__free_base` | `0x7EF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `_isleadbyte_l` | `0x7EF20` | 75 | UnwindData |  |
| 850 | `_o__fpclass` | `0x7EF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1778 | `_set_invalid_parameter_handler` | `0x7EFA0` | 107 | UnwindData |  |
| 617 | `_mbsnicmp_l` | `0x7F020` | 444 | UnwindData |  |
| 593 | `_mbsnbicmp_l` | `0x7F1F0` | 170 | UnwindData |  |
| 1826 | `_strnicmp` | `0x7F2A0` | 139 | UnwindData |  |
| 469 | `_iswdigit_l` | `0x7F340` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1528 | `_o_frexp` | `0x7F440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1546 | `_o_iscntrl` | `0x7F460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1045 | `_o__malloc_base` | `0x7F480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `_localtime64_s` | `0x7F4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1340 | `_o__wcslwr_s` | `0x7F4B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1031 | `_o__lock_file` | `0x7F520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1318 | `_o__unlock_file` | `0x7F540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `_o__aligned_offset_malloc` | `0x7F560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1560 | `_o_iswctype` | `0x7F580` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1652 | `_o_round` | `0x7F890` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2220 | `getc` | `0x7FB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2233 | `imaxdiv` | `0x7FB10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 657 | `_mbsupr_s_l` | `0x7FB40` | 758 | UnwindData |  |
| 2179 | `feof` | `0x7FE40` | 44 | UnwindData |  |
| 1041 | `_o__ltow` | `0x7FE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1680 | `_o_strtod` | `0x7FEA0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1685 | `_o_strtold` | `0x7FEA0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 668 | `_mktime64` | `0x801D0` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `_atoi64` | `0x804A0` | 114 | UnwindData |  |
| 2062 | `atoll` | `0x804A0` | 114 | UnwindData |  |
| 1484 | `_o_cos` | `0x80520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 811 | `_o__execute_onexit_table` | `0x80540` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1472 | `_o_atol` | `0x80840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `_get_fmode` | `0x80850` | 61 | UnwindData |  |
| 2381 | `srand` | `0x81370` | 22 | UnwindData |  |
| 1495 | `_o_exp` | `0x81390` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1536 | `_o_getenv_s` | `0x814E0` | 28 | UnwindData |  |
| 2223 | `getenv_s` | `0x81570` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1163 | `_o__mbsstr` | `0x81600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `_o___pctype_func` | `0x81620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `_iswcntrl_l` | `0x81640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2251 | `iswcntrl` | `0x81640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1437 | `_o__wtoi64` | `0x81650` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1442 | `_o__wtoll` | `0x81650` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2127 | `cosh` | `0x816E0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1992 | `_write` | `0x81920` | 85 | UnwindData |  |
| 823 | `_o__fdclass` | `0x81980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `_ismbcspace_l` | `0x81990` | 84 | UnwindData |  |
| 2335 | `putc` | `0x819F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `_nextafterf` | `0x81A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2324 | `nextafterf` | `0x81A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `_dsign` | `0x81A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `_ldsign` | `0x81A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `_fwrite_nolock` | `0x81A20` | 92 | UnwindData |  |
| 2180 | `ferror` | `0x81AA0` | 44 | UnwindData |  |
| 681 | `_o____lc_collate_cp_func` | `0x827C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `_o__realloc_base` | `0x827E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1855 | `_swab` | `0x82800` | 90 | UnwindData |  |
| 1458 | `_o_asin` | `0x82980` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2465 | `wcstof` | `0x82B20` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `_o__dclass` | `0x82C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `_o__ldclass` | `0x82C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `_o__wcsdup` | `0x82C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1306 | `_o__ultow` | `0x82C70` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1693 | `_o_tanhf` | `0x82D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | `_o___std_type_info_destroy_list` | `0x82D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2027 | `_wtoi_l` | `0x82D70` | 122 | UnwindData |  |
| 2029 | `_wtol_l` | `0x82D70` | 122 | UnwindData |  |
| 133 | `__tzname` | `0x82DF0` | 25 | UnwindData |  |
| 2398 | `strncpy_s` | `0x82E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `_o__Wcsftime` | `0x82E20` | 38 | UnwindData |  |
| 27 | `_Wcsftime` | `0x82EC0` | 30 | UnwindData |  |
| 2374 | `signal` | `0x830C0` | 540 | UnwindData |  |
| 217 | `_dpoly` | `0x83380` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1360 | `_o__wcstombs_s_l` | `0x833B0` | 48 | UnwindData |  |
| 1367 | `_o__wcsupr_s` | `0x833F0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `_get_heap_handle` | `0x83590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1297 | `_o__towlower_l` | `0x835A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2059 | `atof` | `0x835C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `_mbstrlen` | `0x83620` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1580 | `_o_localeconv` | `0x838B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1974 | `_wfsopen` | `0x83920` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1516 | `_o_fmodf` | `0x83F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 555 | `_mbscmp` | `0x83F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `_o___std_exception_destroy` | `0x83FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1908 | `_wcsicoll` | `0x83FB0` | 70 | UnwindData |  |
| 672 | `_o__Getdays` | `0x84000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `_configthreadlocale` | `0x84020` | 107 | UnwindData |  |
| 2383 | `strcat_s` | `0x840A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 678 | `_o__W_Gettnames` | `0x840B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1672 | `_o_strcat_s` | `0x840D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 673 | `_o__Getmonths` | `0x84130` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1395 | `_o__wfullpath` | `0x84170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2269 | `lldiv` | `0x84190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 661 | `_memicmp_l` | `0x841B0` | 154 | UnwindData |  |
| 1609 | `_o_mbstowcs_s` | `0x84250` | 38 | UnwindData |  |
| 354 | `_getwc_nolock` | `0x842F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `_o___std_type_info_name` | `0x84300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `_o___acrt_iob_func` | `0x84320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `_mkgmtime64` | `0x84330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1465 | `_o_atan2f` | `0x84340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 711 | `_o___std_exception_copy` | `0x84360` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `_commit` | `0x843F0` | 140 | UnwindData |  |
| 1087 | `_o__mbsicmp` | `0x84580` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2446 | `wcscoll` | `0x84610` | 101 | UnwindData |  |
| 1440 | `_o__wtol` | `0x84680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1671 | `_o_srand` | `0x84690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2378 | `sinhf` | `0x846B0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1339 | `_o__wcslwr_l` | `0x848C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `_iswlower_l` | `0x848E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2255 | `iswlower` | `0x848E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1077 | `_o__mbscmp` | `0x848F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2111 | `clearerr_s` | `0x84910` | 206 | UnwindData |  |
| 2326 | `nexttoward` | `0x849F0` | 315 | UnwindData |  |
| 1772 | `_set_app_type` | `0x84B70` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `_ismbclower_l` | `0x84CC0` | 93 | UnwindData |  |
| 642 | `_mbsstr` | `0x84D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `_getcwd` | `0x84D40` | 22 | UnwindData |  |
| 308 | `_fullpath` | `0x84EB0` | 14 | UnwindData |  |
| 1687 | `_o_strtoul` | `0x854B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 677 | `_o__W_Getmonths` | `0x854D0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `_iswblank_l` | `0x85570` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2250 | `iswblank` | `0x85570` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 784 | `_o__crt_atexit` | `0x85610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1638 | `_o_rand_s` | `0x85620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 676 | `_o__W_Getdays` | `0x85630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1434 | `_o__wtof` | `0x85650` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1925 | `_wcstod_l` | `0x856D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1931 | `_wcstold_l` | `0x856D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `_o__Gettnames` | `0x856E0` | 3,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1747 | `_putwch_nolock` | `0x862B0` | 82 | UnwindData |  |
| 199 | `_cputws` | `0x863B0` | 205 | UnwindData |  |
| 1184 | `_o__mkgmtime64` | `0x864E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `_o__mbslwr_s` | `0x86500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1777 | `_set_fmode` | `0x86520` | 73 | UnwindData |  |
| 1328 | `_o__wcreate_locale` | `0x86570` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2405 | `strtof` | `0x86860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1464 | `_o_atan2` | `0x86870` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2464 | `wcstod` | `0x868F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2470 | `wcstold` | `0x868F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1466 | `_o_atanf` | `0x86900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1471 | `_o_atoi` | `0x86920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `_iswprint_l` | `0x86940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2256 | `iswprint` | `0x86940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `_dup` | `0x86950` | 85 | UnwindData |  |
| 2228 | `hypot` | `0x86D10` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `_fdpcomp` | `0x86D80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 891 | `_o__get_osfhandle` | `0x86DD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 924 | `_o__gmtime64_s` | `0x86E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `_ldpoly` | `0x86E30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2230 | `ilogbf` | `0x86E60` | 133 | UnwindData |  |
| 2317 | `nan` | `0x86EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2319 | `nanl` | `0x86EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2467 | `wcstok` | `0x86F00` | 57 | UnwindData |  |
| 2407 | `strtok` | `0x86FA0` | 46 | UnwindData |  |
| 1091 | `_o__mbsinc` | `0x86FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1463 | `_o_atan` | `0x86FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `_mbccpy_s` | `0x87010` | 20 | UnwindData |  |
| 531 | `_mbccpy_s_l` | `0x87030` | 204 | UnwindData |  |
| 71 | `__dstbias` | `0x87110` | 25 | UnwindData |  |
| 859 | `_o__free_locale` | `0x871D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 573 | `_mbslen_l` | `0x871E0` | 112 | UnwindData |  |
| 2122 | `copysign` | `0x87260` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2124 | `copysignl` | `0x87260` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1912 | `_wcslwr_s` | `0x872B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `_ldunscale` | `0x872C0` | 216 | UnwindData |  |
| 67 | `__daylight` | `0x873F0` | 25 | UnwindData |  |
| 1564 | `_o_iswprint` | `0x87410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 783 | `_o__create_locale` | `0x87430` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `_Getdays` | `0x874B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `__timezone` | `0x87520` | 25 | UnwindData |  |
| 2355 | `rewind` | `0x87540` | 78 | UnwindData |  |
| 566 | `_mbsicmp` | `0x876A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `_mbsnbcmp_l` | `0x876B0` | 333 | UnwindData |  |
| 2354 | `rename` | `0x87810` | 263 | UnwindData |  |
| 1991 | `_wrename` | `0x87920` | 45 | UnwindData |  |
| 489 | `_ldlog` | `0x879D0` | 615 | UnwindData |  |
| 351 | `_getpid` | `0x87C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `_fdunscale` | `0x87C50` | 170 | UnwindData |  |
| 1470 | `_o_atof` | `0x87D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2142 | `csinhl` | `0x87D20` | 558 | UnwindData |  |
| 14 | `_Getmonths` | `0x883A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1879 | `_umask_s` | `0x883B0` | 61 | UnwindData |  |
| 1809 | `_strcoll_l` | `0x88400` | 228 | UnwindData |  |
| 1030 | `_o__localtime64_s` | `0x884F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2249 | `iswascii` | `0x88510` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `_o__memicmp` | `0x885C0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2188 | `fgets` | `0x88640` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2452 | `wcsncat` | `0x88850` | 782 | UnwindData |  |
| 1733 | `_open` | `0x88BC0` | 35 | UnwindData |  |
| 322 | `_get_initial_narrow_environment` | `0x88CB0` | 35 | UnwindData |  |
| 2352 | `remquof` | `0x88CE0` | 1,139 | UnwindData |  |
| 86 | `__p__commode` | `0x89160` | 6,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1598 | `_o_lroundf` | `0x8AA50` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2241 | `isleadbyte` | `0x8AAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1922 | `_wcsrev` | `0x8AAF0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1587 | `_o_log2` | `0x8AB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `_abs64` | `0x8AB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2232 | `imaxabs` | `0x8AB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2268 | `llabs` | `0x8AB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1365 | `_o__wcsupr` | `0x8AB80` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2368 | `set_terminate` | `0x8B550` | 44 | UnwindData |  |
| 1504 | `_o_fflush` | `0x8B590` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `_kbhit` | `0x8B610` | 48 | UnwindData |  |
| 1725 | `_o_wcstombs_s` | `0x8B8F0` | 38 | UnwindData |  |
| 2478 | `wctob` | `0x8B990` | 469 | UnwindData |  |
| 1399 | `_o__wgetenv_s` | `0x8BBC0` | 28 | UnwindData |  |
| 1979 | `_wgetenv_s` | `0x8BC50` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1597 | `_o_lround` | `0x8C240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1599 | `_o_lroundl` | `0x8C240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1718 | `_o_wcstof` | `0x8C260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2350 | `remove` | `0x8C280` | 143 | UnwindData |  |
| 1394 | `_o__wfsopen` | `0x8C320` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `_difftime32` | `0x8C390` | 43 | UnwindData |  |
| 2106 | `cexpl` | `0x8C3D0` | 643 | UnwindData |  |
| 15 | `_Gettnames` | `0x8C660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1486 | `_o_cosh` | `0x8C670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `_o__set_app_type` | `0x8C690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2377 | `sinh` | `0x8C6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `_mbslwr_s` | `0x8C6C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 667 | `_mktime32` | `0x8C6D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `_ismbcdigit_l` | `0x8C6E0` | 92 | UnwindData |  |
| 700 | `_o___p__commode` | `0x8C750` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1274 | `_o__strtoi64` | `0x8C7D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `_o_strtoll` | `0x8C7D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `_gmtime32_s` | `0x8C820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1846 | `_strtoui64_l` | `0x8C830` | 127 | UnwindData |  |
| 1848 | `_strtoull_l` | `0x8C830` | 127 | UnwindData |  |
| 1849 | `_strtoumax_l` | `0x8C830` | 127 | UnwindData |  |
| 1790 | `_sleep` | `0x8C8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `_gmtime32` | `0x8C8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `_chmod` | `0x8C8F0` | 149 | UnwindData |  |
| 1898 | `_wchmod` | `0x8C990` | 175 | UnwindData |  |
| 1501 | `_o_fclose` | `0x8CA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1551 | `_o_isprint` | `0x8CA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2217 | `fsetpos` | `0x8CAB0` | 53 | UnwindData |  |
| 839 | `_o__fileno` | `0x8CAF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2222 | `getenv` | `0x8CB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `_fpreset` | `0x8CB20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2190 | `fgetws` | `0x8CBA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1224 | `_o__set_fmode` | `0x8CBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `_localtime32_s` | `0x8CBD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `_iswgraph_l` | `0x8CBE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2254 | `iswgraph` | `0x8CBE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1998 | `_wsopen_dispatch` | `0x8CBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1515 | `_o_fmod` | `0x8CC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `_mbsrchr` | `0x8CC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `_o_log2f` | `0x8CC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1692 | `_o_tanh` | `0x8CC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `_o__set_new_mode` | `0x8CC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `_ismbcspace` | `0x8CC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1942 | `_wcsupr_s` | `0x8CCA0` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `_get_initial_wide_environment` | `0x8CF80` | 35 | UnwindData |  |
| 615 | `_mbsnextc_l` | `0x8CFB0` | 141 | UnwindData |  |
| 1535 | `_o_getenv` | `0x8D080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 778 | `_o__configure_wide_argv` | `0x8D0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 659 | `_memccpy` | `0x8D0C0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1577 | `_o_llround` | `0x8D270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1579 | `_o_llroundl` | `0x8D270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2366 | `scalbnf` | `0x8D290` | 359 | UnwindData |  |
| 1970 | `_wfopen` | `0x8D480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `_locking` | `0x8D4A0` | 321 | UnwindData |  |
| 209 | `_d_int` | `0x8D8B0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `_ismbcalpha_l` | `0x8D960` | 129 | UnwindData |  |
| 1188 | `_o__mktime64` | `0x8D9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1608 | `_o_mbstowcs` | `0x8DA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `__initialize_lconv_for_unsigned_char` | `0x8DA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2044 | `acoshl` | `0x8DA50` | 215 | UnwindData |  |
| 553 | `_mbschr` | `0x8DB30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1654 | `_o_roundl` | `0x8DB40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 589 | `_mbsnbcpy_l` | `0x8DB90` | 269 | UnwindData |  |
| 296 | `_fsopen` | `0x8DCB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `_o__configthreadlocale` | `0x8DCC0` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1613 | `_o_modf` | `0x8E0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2173 | `fdiml` | `0x8E110` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `_get_wide_winmain_command_line` | `0x8E190` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1691 | `_o_tanf` | `0x8E230` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1878 | `_umask` | `0x8E280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 935 | `_o__initialize_wide_environment` | `0x8E2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 649 | `_mbstowcs_s_l` | `0x8E2C0` | 124 | UnwindData |  |
| 194 | `_controlfp` | `0x8E350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1459 | `_o_asinf` | `0x8E360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2141 | `csinhf` | `0x8E380` | 427 | UnwindData |  |
| 1352 | `_o__wcstod_l` | `0x8E6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1357 | `_o__wcstold_l` | `0x8E6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `__sys_nerr` | `0x8E6D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 898 | `_o__get_wide_winmain_command_line` | `0x8E6E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2023 | `_wtof_l` | `0x8E700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 658 | `_mbtowc_l` | `0x8E710` | 96 | UnwindData |  |
| 1256 | `_o__stricoll` | `0x8E800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1769 | `_seh_filter_exe` | `0x8E820` | 178 | UnwindData |  |
| 2140 | `csinh` | `0x8E8E0` | 479 | UnwindData |  |
| 1792 | `_sopen_dispatch` | `0x90B00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `_iswpunct_l` | `0x90B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2257 | `iswpunct` | `0x90B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1494 | `_o_exit` | `0x90B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `_o__itow` | `0x90B60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1982 | `_wmkdir` | `0x90BD0` | 41 | UnwindData |  |
| 248 | `_fd_int` | `0x90C00` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2160 | `exit` | `0x90CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `__stdio_common_vfscanf` | `0x90CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1717 | `_o_wcstod` | `0x90CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1722 | `_o_wcstold` | `0x90CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `_o__gcvt` | `0x90CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1683 | `_o_strtok_s` | `0x90D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2286 | `logb` | `0x90D20` | 195 | UnwindData |  |
| 2395 | `strncat_s` | `0x90DF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2074 | `cacoshf` | `0x90E50` | 805 | UnwindData |  |
| 127 | `__sys_errlist` | `0x91180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `_mbclen` | `0x91190` | 95 | UnwindData |  |
| 1990 | `_wremove` | `0x91200` | 39 | UnwindData |  |
| 670 | `_nextafter` | `0x91230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2323 | `nextafter` | `0x91230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2325 | `nextafterl` | `0x91230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2328 | `nexttowardl` | `0x91230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `_o_ldexp` | `0x91240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `_initialize_narrow_environment` | `0x91260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `__p___argc` | `0x91270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `_o__mbstrlen` | `0x91280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `_mbsdec` | `0x91290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1776 | `_set_error_mode` | `0x912A0` | 71 | UnwindData |  |
| 277 | `_findnext64i32` | `0x912F0` | 45 | UnwindData |  |
| 836 | `_o__fgetwchar` | `0x91330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1540 | `_o_getwchar` | `0x91330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1250 | `_o__strdup` | `0x91350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `_flushall` | `0x91370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `_findclose` | `0x91380` | 37 | UnwindData |  |
| 265 | `_fgetwchar` | `0x913B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2227 | `getwchar` | `0x913B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 662 | `_mkdir` | `0x913D0` | 147 | UnwindData |  |
| 888 | `_o__get_initial_wide_environment` | `0x91470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2166 | `expm1` | `0x91490` | 315 | UnwindData |  |
| 2042 | `acosh` | `0x915E0` | 224 | UnwindData |  |
| 777 | `_o__configure_narrow_argv` | `0x916D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1724 | `_o_wcstombs` | `0x916F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1756 | `_register_thread_local_exe_atexit_callback` | `0x91710` | 60 | UnwindData |  |
| 440 | `_ismbclower` | `0x91760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1758 | `_rmdir` | `0x91770` | 143 | UnwindData |  |
| 1719 | `_o_wcstok` | `0x91810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `__p___wargv` | `0x91830` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 774 | `_o__close` | `0x91D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 698 | `_o___p___wargv` | `0x91DB0` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2012 | `_wstat64` | `0x920A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2171 | `fdim` | `0x920B0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2013 | `_wstat64i32` | `0x92180` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1774 | `_set_doserrno` | `0x921D0` | 40 | UnwindData |  |
| 543 | `_mbctolower_l` | `0x92200` | 133 | UnwindData |  |
| 2085 | `casinhl` | `0x92290` | 843 | UnwindData |  |
| 192 | `_configure_wide_argv` | `0x928B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | `_o__difftime64` | `0x928C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `_o__tell` | `0x928E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `__p__environ` | `0x92910` | 25 | UnwindData |  |
| 2391 | `strerror_s` | `0x92930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2231 | `ilogbl` | `0x92940` | 159 | UnwindData |  |
| 2363 | `scalblnf` | `0x929F0` | 364 | UnwindData |  |
| 1854 | `_strxfrm_l` | `0x92B70` | 478 | UnwindData |  |
| 790 | `_o__difftime32` | `0x92DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1856 | `_tell` | `0x92DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2172 | `fdimf` | `0x92E10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2453 | `wcsncat_s` | `0x92E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 923 | `_o__gmtime64` | `0x92E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 933 | `_o__initialize_narrow_environment` | `0x92E90` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2484 | `wmemmove_s` | `0x92F80` | 82 | UnwindData |  |
| 2043 | `acoshf` | `0x92FE0` | 195 | UnwindData |  |
| 196 | `_copysign` | `0x93110` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2193 | `fma` | `0x93490` | 3,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2226 | `getwc` | `0x94110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1192 | `_o__open_osfhandle` | `0x94120` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2348 | `remainderf` | `0x94920` | 627 | UnwindData |  |
| 656 | `_mbsupr_s` | `0x94BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `_initialize_wide_environment` | `0x94BB0` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `_o__dup2` | `0x950C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1565 | `_o_iswpunct` | `0x950E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2311 | `memcpy_s` | `0x95100` | 130 | UnwindData |  |
| 2204 | `fopen` | `0x95190` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2362 | `scalbln` | `0x952C0` | 424 | UnwindData |  |
| 2072 | `cacosf` | `0x95690` | 714 | UnwindData |  |
| 1681 | `_o_strtof` | `0x95960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1838 | `_strtof_l` | `0x95980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2288 | `logbl` | `0x95990` | 195 | UnwindData |  |
| 1509 | `_o_fgetws` | `0x95A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1452 | `_o_acosf` | `0x95A80` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1807 | `_stat64i32` | `0x95CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2168 | `expm1l` | `0x95D00` | 311 | UnwindData |  |
| 528 | `_mbccpy` | `0x95E40` | 134 | UnwindData |  |
| 273 | `_findfirst64i32` | `0x95ED0` | 45 | UnwindData |  |
| 887 | `_o__get_initial_narrow_environment` | `0x95F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `_o__mktime32` | `0x95F90` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `__p___argv` | `0x96AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 697 | `_o___p___argv` | `0x96B00` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2045 | `asctime` | `0x96C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2301 | `mbrtoc32` | `0x96C60` | 92 | UnwindData |  |
| 696 | `_o___p___argc` | `0x96CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2361 | `roundl` | `0x96CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1029 | `_o__localtime64` | `0x96D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `_fread_nolock` | `0x96D20` | 29 | UnwindData |  |
| 801 | `_o__dup` | `0x96D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1862 | `_timespec64_get` | `0x96D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1863 | `_tolower` | `0x96D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `_o__get_narrow_winmain_command_line` | `0x96DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `_get_narrow_winmain_command_line` | `0x96DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1557 | `_o_iswascii` | `0x96DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1346 | `_o__wcsnicoll` | `0x96DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `_makepath_s` | `0x96E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2229 | `ilogb` | `0x96E20` | 159 | UnwindData |  |
| 1989 | `_wputenv_s` | `0x96ED0` | 56 | UnwindData |  |
| 2370 | `setbuf` | `0x96F10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2482 | `wctype` | `0x96F40` | 96 | UnwindData |  |
| 2037 | `_yn` | `0x97030` | 231 | UnwindData |  |
| 191 | `_configure_narrow_argv` | `0x97120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2046 | `asctime_s` | `0x97130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `_o_fputc` | `0x97140` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1993 | `_wrmdir` | `0x97560` | 39 | UnwindData |  |
| 582 | `_mbsnbcmp` | `0x97590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1293 | `_o__tolower` | `0x975A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1978 | `_wgetenv` | `0x975C0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `_fstat64i32` | `0x97730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1773 | `_set_controlfp` | `0x97740` | 54 | UnwindData |  |
| 1521 | `_o_fputwc` | `0x977B0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1837 | `_strtod_l` | `0x97980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1843 | `_strtold_l` | `0x97980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2285 | `log2l` | `0x97990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `__p__wenviron` | `0x979A0` | 25 | UnwindData |  |
| 1451 | `_o_acos` | `0x97A30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1857 | `_telli64` | `0x97AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `_o__strlwr` | `0x97AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2318 | `nanf` | `0x97AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `_ctime64_s` | `0x97B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1742 | `_putenv` | `0x97B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `_fdopen` | `0x97B20` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `_ismbcdigit` | `0x97BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1924 | `_wcsset_s` | `0x97C00` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 572 | `_mbslen` | `0x98080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2082 | `casinf` | `0x98090` | 78 | UnwindData |  |
| 807 | `_o__endthreadex` | `0x98310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1840 | `_strtoi64_l` | `0x98330` | 127 | UnwindData |  |
| 1841 | `_strtoimax_l` | `0x98330` | 127 | UnwindData |  |
| 1844 | `_strtoll_l` | `0x98330` | 127 | UnwindData |  |
| 461 | `_isupper_l` | `0x983C0` | 24 | UnwindData |  |
| 1225 | `_o__set_invalid_parameter_handler` | `0x984B0` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2390 | `strerror` | `0x98BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `_localtime32` | `0x98BC0` | 72 | UnwindData |  |
| 88 | `__p__fmode` | `0x98C10` | 25 | UnwindData |  |
| 1563 | `_o_iswlower` | `0x98C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | `_mbsnextc` | `0x98C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1822 | `_strlwr_s` | `0x98C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1852 | `_strupr_s` | `0x98C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `_ismbcalpha` | `0x98C80` | 2,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `_Cmulcc` | `0x996C0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `_LCmulcc` | `0x996C0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `_findfirst64` | `0x998A0` | 45 | UnwindData |  |
| 1506 | `_o_fgetpos` | `0x998E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `_o__pipe` | `0x99900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2110 | `clearerr` | `0x99920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1610 | `_o_mbtowc` | `0x99930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1415 | `_o__wsetlocale` | `0x99950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `_o_fseek` | `0x99960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `_o__setmode` | `0x99980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1476 | `_o_btowc` | `0x999A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `_mbscspn` | `0x999B0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1690 | `_o_tan` | `0x99E60` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 733 | `_o___timezone` | `0x9A830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2386 | `strcoll` | `0x9A850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `_o__dsign` | `0x9A860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1503 | `_o_ferror` | `0x9A880` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1787 | `_setmbcp` | `0x9A900` | 58 | UnwindData |  |
| 459 | `_ispunct_l` | `0x9AA50` | 24 | UnwindData |  |
| 861 | `_o__fseeki64` | `0x9AC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1661 | `_o_set_terminate` | `0x9AC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `_mbsnbicmp` | `0x9AC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 628 | `_mbspbrk` | `0x9ACA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1260 | `_o__strlwr_s` | `0x9ACB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `_o__beginthread` | `0x9ACD0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `_ctime64` | `0x9AE80` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1815 | `_strftime_l` | `0x9B050` | 30 | UnwindData |  |
| 1965 | `_wfindfirst64i32` | `0x9B080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `_o___stdio_common_vswprintf_p` | `0x9B090` | 55 | UnwindData |  |
| 1507 | `_o_fgets` | `0x9B0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `_o__waccess` | `0x9B0F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1771 | `_set_abort_behavior` | `0x9B160` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1969 | `_wfindnext64i32` | `0x9B190` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2194 | `fmaf` | `0x9B210` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `_mbctolower` | `0x9B340` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `_get_terminate` | `0x9B480` | 34 | UnwindData |  |
| 1398 | `_o__wgetenv` | `0x9B4B0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 775 | `_o__commit` | `0x9B5A0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `_FCbuild` | `0x9B9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `_get_tzname` | `0x9B9F0` | 236 | UnwindData |  |
| 1222 | `_o__set_doserrno` | `0x9BB00` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `_fstat64` | `0x9BF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2108 | `cimagf` | `0x9BF10` | 19 | UnwindData |  |
| 328 | `_get_printf_count_output` | `0x9BF30` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `_o_feof` | `0x9C060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1520 | `_o_fputs` | `0x9C080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1246 | `_o__stat64i32` | `0x9C0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `_o__wmkdir` | `0x9C0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | `_mbsspn` | `0x9C0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `_ftime32` | `0x9C0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `_ftime32_s` | `0x9C0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `_get_current_locale` | `0x9C100` | 192 | UnwindData |  |
| 1988 | `_wputenv` | `0x9C1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 640 | `_mbsspnp` | `0x9C1E0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `_fstat32i64` | `0x9C300` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2164 | `exp2l` | `0x9C470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1816 | `_stricmp` | `0x9C480` | 6,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `_cexit` | `0x9DD90` | 181 | UnwindData |  |
| 2036 | `_y1` | `0x9E190` | 3,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `_getwche_nolock` | `0x9EF40` | 83 | UnwindData |  |
| 1930 | `_wcstol_l` | `0x9F300` | 125 | UnwindData |  |
| 342 | `_getche_nolock` | `0x9F600` | 62 | UnwindData |  |
| 163 | `_atoldbl_l` | `0x9F720` | 234 | UnwindData |  |
| 1894 | `_wasctime` | `0x9FD50` | 122 | UnwindData |  |
| 2287 | `logbf` | `0x9FDD0` | 166 | UnwindData |  |
| 1891 | `_utime64` | `0xA0260` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `___mb_cur_max_l_func` | `0xA02F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 692 | `_o___conio_common_vcwscanf` | `0xA0310` | 35 | UnwindData |  |
| 1886 | `_unlink` | `0xA03B0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `_mbsrev_l` | `0xA04A0` | 269 | UnwindData |  |
| 1920 | `_wcsnset` | `0xA0620` | 3,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1806 | `_stat64` | `0xA14B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `_o__wputenv_s` | `0xA14C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1406 | `_o__wpopen` | `0xA14E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1348 | `_o__wcsnset` | `0xA1500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `_o__strupr_s` | `0xA1520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `_o__controlfp_s` | `0xA1540` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2005 | `_wspawnve` | `0xA1860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1614 | `_o_modff` | `0xA1870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1648 | `_o_rewind` | `0xA1890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1682 | `_o_strtok` | `0xA18B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1432 | `_o__wsystem` | `0xA18D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `_o__mbsbtype` | `0xA18F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1446 | `_o__wutime64` | `0xA1910` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 641 | `_mbsspnp_l` | `0xA1B40` | 263 | UnwindData |  |
| 2034 | `_wutime64` | `0xA1FC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `_mbsbtype` | `0xA2020` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2415 | `strxfrm` | `0xA2130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 646 | `_mbstok_s` | `0xA2140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 632 | `_mbsrev` | `0xA2150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 937 | `_o__invalid_parameter_noinfo_noreturn` | `0xA2160` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1968 | `_wfindnext64` | `0xA22B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2032 | `_wunlink` | `0xA2320` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `_fdsin` | `0xA23E0` | 298 | UnwindData |  |
| 1961 | `_wfdopen` | `0xA2990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1895 | `_wasctime_s` | `0xA29A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1948 | `_wctime64_s` | `0xA29B0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2119 | `conj` | `0xA2BE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2121 | `conjl` | `0xA2BE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2303 | `mbsrtowcs` | `0xA2C10` | 92 | UnwindData |  |
| 148 | `_aligned_offset_realloc` | `0xA2F30` | 602 | UnwindData |  |
| 149 | `_aligned_offset_recalloc` | `0xA3190` | 784 | UnwindData |  |
| 552 | `_mbscat_s_l` | `0xA3600` | 572 | UnwindData |  |
| 2167 | `expm1f` | `0xA3900` | 199 | UnwindData |  |
| 2017 | `_wstrtime_s` | `0xA3A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `_mbsncat_s_l` | `0xA3A80` | 677 | UnwindData |  |
| 2120 | `conjf` | `0xA3E50` | 39 | UnwindData |  |
| 345 | `_getdiskfree` | `0xA4240` | 196 | UnwindData |  |
| 2213 | `freopen` | `0xA4370` | 47 | UnwindData |  |
| 1526 | `_o_freopen` | `0xA43B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `_fdpoly` | `0xA43D0` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2038 | `abort` | `0xA4A80` | 106 | UnwindData |  |
| 6 | `_Exit` | `0xA4AF0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `_exit` | `0xA4AF0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `__stdio_common_vfwscanf` | `0xA4B90` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `_futime64` | `0xA4E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `_Cbuild` | `0xA4E60` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `_LCbuild` | `0xA4E60` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `_atof_l` | `0xA5070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `_mktemp` | `0xA5080` | 81 | UnwindData |  |
| 383 | `_isalnum_l` | `0xA5360` | 24 | UnwindData |  |
| 384 | `_isalpha_l` | `0xA5440` | 24 | UnwindData |  |
| 390 | `_isdigit_l` | `0xA5520` | 20 | UnwindData |  |
| 1897 | `_wchdir` | `0xA56A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2015 | `_wstrdate_s` | `0xA5700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1262 | `_o__strncoll` | `0xA5710` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2078 | `carg` | `0xA5980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2080 | `cargl` | `0xA5980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1997 | `_wsopen` | `0xA59A0` | 68 | UnwindData |  |
| 1904 | `_wcserror_s` | `0xA59F0` | 127 | UnwindData |  |
| 607 | `_mbsncmp_l` | `0xA62A0` | 320 | UnwindData |  |
| 181 | `_chdrive` | `0xA6960` | 129 | UnwindData |  |
| 153 | `_atodbl` | `0xA6A40` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `_FCmulcc` | `0xA6CB0` | 74 | UnwindData |  |
| 2178 | `feholdexcept` | `0xA6D30` | 80 | UnwindData |  |
| 2136 | `crealf` | `0xA6E40` | 18 | UnwindData |  |
| 1125 | `_o__mbsnccnt` | `0xA6E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `_o__mbsrev_l` | `0xA6E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1259 | `_o__strlwr_l` | `0xA6EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2107 | `cimag` | `0xA6EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2109 | `cimagl` | `0xA6EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2135 | `creal` | `0xA6ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2137 | `creall` | `0xA6ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1309 | `_o__umask_s` | `0xA6EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1749 | `_query_app_type` | `0xA6EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `_mbsnbcpy` | `0xA6F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1994 | `_wsearchenv` | `0xA6F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1903 | `_wcserror` | `0xA6F30` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2125 | `cos` | `0xA6F80` | 1,402 | UnwindData |  |
| 2126 | `cosf` | `0xA77C0` | 543 | UnwindData |  |
| 2161 | `exp` | `0xA79F0` | 1,045 | UnwindData |  |
| 2165 | `expf` | `0xA7F90` | 346 | UnwindData |  |
| 2202 | `fmod` | `0xA81E0` | 692 | UnwindData |  |
| 2277 | `log` | `0xA84B0` | 1,323 | UnwindData |  |
| 2278 | `log10` | `0xA89F0` | 1,451 | UnwindData |  |
| 2279 | `log10f` | `0xA91C0` | 504 | UnwindData |  |
| 2289 | `logf` | `0xA9590` | 460 | UnwindData |  |
| 2334 | `powf` | `0xA9770` | 3,766 | UnwindData |  |
| 2347 | `remainder` | `0xAA640` | 1,000 | UnwindData |  |
| 2360 | `roundf` | `0xAB1F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2359 | `round` | `0xAB240` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2375 | `sin` | `0xAB2C0` | 1,386 | UnwindData |  |
| 2376 | `sinf` | `0xABBB0` | 845 | UnwindData |  |
| 2417 | `tan` | `0xAC4C0` | 1,459 | UnwindData |  |
| 2418 | `tanf` | `0xACF90` | 730 | UnwindData |  |
| 4 | `_CreateFrameInfo` | `0xADD60` | 58 | UnwindData |  |
| 10 | `_FindAndUnlinkFrame` | `0xADDA0` | 83 | UnwindData |  |
| 11 | `_GetImageBase` | `0xADE00` | 18 | UnwindData |  |
| 12 | `_GetThrowImageBase` | `0xADE20` | 18 | UnwindData |  |
| 20 | `_SetImageBase` | `0xADE40` | 24 | UnwindData |  |
| 21 | `_SetThrowImageBase` | `0xADE60` | 24 | UnwindData |  |
| 35 | `__CxxFrameHandler` | `0xADE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `__CxxFrameHandler2` | `0xADE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `__CxxFrameHandler3` | `0xADE90` | 134 | UnwindData |  |
| 38 | `__CxxFrameHandler4` | `0xADF20` | 191 | UnwindData |  |
| 5 | `_CxxThrowException` | `0xADFF0` | 166 | UnwindData |  |
| 42 | `__DestructExceptionObject` | `0xAE0A0` | 108 | UnwindData |  |
| 16 | `_IsExceptionObjectToBeDestroyed` | `0xAE120` | 47 | UnwindData |  |
| 22 | `_SetWinRTOutOfMemoryExceptionCallback` | `0xAE160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `__AdjustPointer` | `0xAE170` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__FrameUnwindFilter` | `0xAE1A0` | 102 | UnwindData |  |
| 44 | `__GetPlatformExceptionInfo` | `0xAE210` | 91 | UnwindData |  |
| 65 | `__current_exception` | `0xAE280` | 18 | UnwindData |  |
| 66 | `__current_exception_context` | `0xAE2A0` | 18 | UnwindData |  |
| 96 | `__processing_throw` | `0xAE2C0` | 18 | UnwindData |  |
| 103 | `__std_terminate` | `0xAE2E0` | 10 | UnwindData |  |
| 382 | `_is_exception_typeof` | `0xAE2F0` | 165 | UnwindData |  |
| 29 | `__BuildCatchObject` | `0xB14A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `__BuildCatchObjectHelper` | `0xB14B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__TypeMatch` | `0xB14C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `__C_specific_handler` | `0xB14D0` | 535 | UnwindData |  |
| 32 | `__C_specific_handler_noexcept` | `0xB16F0` | 75 | UnwindData |  |
| 33 | `__CxxDetectRethrow` | `0xB1750` | 68 | UnwindData |  |
| 34 | `__CxxExceptionFilter` | `0xB17A0` | 503 | UnwindData |  |
| 39 | `__CxxQueryExceptionSize` | `0xB19A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__CxxRegisterExceptionObject` | `0xB19B0` | 172 | UnwindData |  |
| 41 | `__CxxUnregisterExceptionObject` | `0xB1A70` | 294 | UnwindData |  |
| 45 | `__NLG_Dispatch2` | `0xB1BD0` | 1 | UnwindData |  |
| 46 | `__NLG_Return2` | `0xB1BE0` | 1 | UnwindData |  |
| 47 | `__RTCastToVoid` | `0xB2200` | 93 | UnwindData |  |
| 48 | `__RTDynamicCast` | `0xB2270` | 366 | UnwindData |  |
| 49 | `__RTtypeid` | `0xB23F0` | 180 | UnwindData |  |
| 101 | `__std_exception_copy` | `0xB24C0` | 141 | UnwindData |  |
| 102 | `__std_exception_destroy` | `0xB2560` | 37 | UnwindData |  |
| 104 | `__std_type_info_compare` | `0xB25B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `__std_type_info_destroy_list` | `0xB25E0` | 42 | UnwindData |  |
| 106 | `__std_type_info_hash` | `0xB2610` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `__std_type_info_name` | `0xB2650` | 277 | UnwindData |  |
| 136 | `__uncaught_exception` | `0xB2770` | 30 | UnwindData |  |
| 137 | `__uncaught_exceptions` | `0xB27A0` | 27 | UnwindData |  |
| 329 | `_get_purecall_handler` | `0xB27D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1738 | `_purecall` | `0xB27E0` | 25 | UnwindData |  |
| 1782 | `_set_purecall_handler` | `0xB2800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `_get_unexpected` | `0xB2820` | 34 | UnwindData |  |
| 2369 | `set_unexpected` | `0xB2850` | 44 | UnwindData |  |
| 2437 | `unexpected` | `0xB2890` | 29 | UnwindData |  |
| 500 | `_local_unwind` | `0xB28C0` | 41 | UnwindData |  |
| 1783 | `_set_se_translator` | `0xB2900` | 45 | UnwindData |  |
| 2290 | `longjmp` | `0xB2940` | 40 | UnwindData |  |
| 99 | `__report_gsfailure` | `0xB33A0` | 210 | UnwindData |  |
| 675 | `_o__Strftime` | `0xB93D0` | 38 | UnwindData |  |
| 685 | `_o___conio_common_vcprintf` | `0xB9400` | 35 | UnwindData |  |
| 686 | `_o___conio_common_vcprintf_p` | `0xB9430` | 35 | UnwindData |  |
| 687 | `_o___conio_common_vcprintf_s` | `0xB9460` | 35 | UnwindData |  |
| 688 | `_o___conio_common_vcscanf` | `0xB9490` | 35 | UnwindData |  |
| 689 | `_o___conio_common_vcwprintf` | `0xB94C0` | 35 | UnwindData |  |
| 690 | `_o___conio_common_vcwprintf_p` | `0xB94F0` | 35 | UnwindData |  |
| 691 | `_o___conio_common_vcwprintf_s` | `0xB9520` | 35 | UnwindData |  |
| 693 | `_o___daylight` | `0xB9550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 694 | `_o___dstbias` | `0xB9570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 695 | `_o___fpe_flt_rounds` | `0xB9590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 699 | `_o___p__acmdln` | `0xB95B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 701 | `_o___p__environ` | `0xB95D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | `_o___p__fmode` | `0xB95F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `_o___p__mbcasemap` | `0xB9610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `_o___p__mbctype` | `0xB9630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `_o___p__pgmptr` | `0xB9650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 706 | `_o___p__wcmdln` | `0xB9670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `_o___p__wenviron` | `0xB9690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 708 | `_o___p__wpgmptr` | `0xB96B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `_o___pwctype_func` | `0xB96D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `_o___stdio_common_vfprintf_p` | `0xB96F0` | 45 | UnwindData |  |
| 717 | `_o___stdio_common_vfprintf_s` | `0xB9730` | 45 | UnwindData |  |
| 720 | `_o___stdio_common_vfwprintf_p` | `0xB9770` | 45 | UnwindData |  |
| 722 | `_o___stdio_common_vfwscanf` | `0xB97B0` | 45 | UnwindData |  |
| 726 | `_o___stdio_common_vsprintf_p` | `0xB97F0` | 55 | UnwindData |  |
| 734 | `_o___tzname` | `0xB9830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `_o___wcserror` | `0xB9850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 736 | `_o__access` | `0xB9870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `_o__access_s` | `0xB9890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `_o__aligned_msize` | `0xB98B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `_o__aligned_offset_realloc` | `0xB98D0` | 35 | UnwindData |  |
| 743 | `_o__aligned_offset_recalloc` | `0xB9900` | 38 | UnwindData |  |
| 744 | `_o__aligned_realloc` | `0xB9930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `_o__aligned_recalloc` | `0xB9950` | 35 | UnwindData |  |
| 746 | `_o__atodbl` | `0xB9980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `_o__atodbl_l` | `0xB99A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 748 | `_o__atof_l` | `0xB99C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `_o__atoflt` | `0xB99E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `_o__atoflt_l` | `0xB9A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `_o__atoi64` | `0xB9A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1473 | `_o_atoll` | `0xB9A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | `_o__atoi64_l` | `0xB9A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `_o__atoll_l` | `0xB9A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `_o__atoi_l` | `0xB9A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 754 | `_o__atol_l` | `0xB9A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 755 | `_o__atoldbl` | `0xB9A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `_o__atoldbl_l` | `0xB9AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `_o__beep` | `0xB9AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `_o__cabs` | `0xB9AD0` | 28 | UnwindData |  |
| 762 | `_o__callnewh` | `0xB9B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | `_o__cexit` | `0xB9B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `_o__cgets` | `0xB9B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `_o__cgets_s` | `0xB9B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `_o__cgetws` | `0xB9B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 768 | `_o__cgetws_s` | `0xB9B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `_o__chdir` | `0xB9BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `_o__chdrive` | `0xB9BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `_o__chmod` | `0xB9BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 772 | `_o__chsize` | `0xB9C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `_o__chsize_s` | `0xB9C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 780 | `_o__cputs` | `0xB9C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `_o__cputws` | `0xB9C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 782 | `_o__creat` | `0xB9C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `_o__ctime32_s` | `0xB9C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 786 | `_o__ctime64_s` | `0xB9CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | `_o__cwait` | `0xB9CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 788 | `_o__d_int` | `0xB9CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 792 | `_o__dlog` | `0xB9D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `_o__dnorm` | `0xB9D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `_o__dpcomp` | `0xB9D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 795 | `_o__dpoly` | `0xB9D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `_o__dscale` | `0xB9D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `_o__dsin` | `0xB9DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `_o__dtest` | `0xB9DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `_o__ldtest` | `0xB9DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 800 | `_o__dunscale` | `0xB9DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 803 | `_o__dupenv_s` | `0xB9DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 804 | `_o__ecvt` | `0xB9E10` | 35 | UnwindData |  |
| 806 | `_o__endthread` | `0xB9E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 808 | `_o__eof` | `0xB9E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `_o__except1` | `0xB9E80` | 38 | UnwindData |  |
| 812 | `_o__execv` | `0xB9EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `_o__execve` | `0xB9ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `_o__execvp` | `0xB9EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `_o__execvpe` | `0xB9F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 816 | `_o__exit` | `0xB9F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `_o__expand` | `0xB9F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `_o__fclose_nolock` | `0xB9F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `_o__fcloseall` | `0xB9F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 820 | `_o__fcvt` | `0xB9FB0` | 35 | UnwindData |  |
| 821 | `_o__fcvt_s` | `0xB9FE0` | 55 | UnwindData |  |
| 822 | `_o__fd_int` | `0xBA020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | `_o__fdexp` | `0xBA040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `_o__fdlog` | `0xBA060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 826 | `_o__fdopen` | `0xBA080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `_o__fdpcomp` | `0xBA090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 828 | `_o__fdpoly` | `0xBA0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 829 | `_o__fdscale` | `0xBA0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `_o__fdsign` | `0xBA0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `_o__fdsin` | `0xBA110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 832 | `_o__fflush_nolock` | `0xBA130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | `_o__fgetc_nolock` | `0xBA150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 834 | `_o__fgetchar` | `0xBA170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1534 | `_o_getchar` | `0xBA170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 835 | `_o__fgetwc_nolock` | `0xBA190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 837 | `_o__filelength` | `0xBA1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `_o__filelengthi64` | `0xBA1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | `_o__findclose` | `0xBA1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 841 | `_o__findfirst32` | `0xBA210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `_o__findfirst32i64` | `0xBA230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `_o__findfirst64` | `0xBA250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `_o__findfirst64i32` | `0xBA270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `_o__findnext32` | `0xBA290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `_o__findnext32i64` | `0xBA2B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `_o__findnext64` | `0xBA2D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 848 | `_o__findnext64i32` | `0xBA2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `_o__flushall` | `0xBA310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `_o__fpclassf` | `0xBA330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `_o__fputc_nolock` | `0xBA350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `_o__fputchar` | `0xBA370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 854 | `_o__fputwc_nolock` | `0xBA390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 855 | `_o__fputwchar` | `0xBA3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 856 | `_o__fread_nolock` | `0xBA3D0` | 35 | UnwindData |  |
| 857 | `_o__fread_nolock_s` | `0xBA400` | 45 | UnwindData |  |
| 860 | `_o__fseek_nolock` | `0xBA440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 862 | `_o__fseeki64_nolock` | `0xBA460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `_o__fsopen` | `0xBA480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `_o__fstat32` | `0xBA4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | `_o__fstat32i64` | `0xBA4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `_o__fstat64` | `0xBA4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `_o__fstat64i32` | `0xBA4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `_o__ftell_nolock` | `0xBA4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `_o__ftelli64` | `0xBA500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | `_o__ftelli64_nolock` | `0xBA520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 871 | `_o__ftime32` | `0xBA540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `_o__ftime32_s` | `0xBA550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `_o__ftime64` | `0xBA560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `_o__ftime64_s` | `0xBA570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `_o__fullpath` | `0xBA580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 876 | `_o__futime32` | `0xBA5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `_o__futime64` | `0xBA5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 878 | `_o__fwrite_nolock` | `0xBA5C0` | 35 | UnwindData |  |
| 881 | `_o__get_daylight` | `0xBA5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 882 | `_o__get_doserrno` | `0xBA610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 883 | `_o__get_dstbias` | `0xBA620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `_o__get_fmode` | `0xBA640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | `_o__get_heap_handle` | `0xBA660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `_o__get_invalid_parameter_handler` | `0xBA670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `_o__get_pgmptr` | `0xBA690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `_o__get_terminate` | `0xBA6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `_o__get_thread_local_invalid_parameter_handler` | `0xBA6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 896 | `_o__get_timezone` | `0xBA6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `_o__get_tzname` | `0xBA6F0` | 28 | UnwindData |  |
| 899 | `_o__get_wpgmptr` | `0xBA720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 900 | `_o__getc_nolock` | `0xBA730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 901 | `_o__getch` | `0xBA750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 902 | `_o__getch_nolock` | `0xBA770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `_o__getche` | `0xBA790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `_o__getche_nolock` | `0xBA7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 905 | `_o__getcwd` | `0xBA7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 906 | `_o__getdcwd` | `0xBA7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 907 | `_o__getdiskfree` | `0xBA810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 908 | `_o__getdllprocaddr` | `0xBA820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `_o__getdrive` | `0xBA840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | `_o__getdrives` | `0xBA860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | `_o__getmbcp` | `0xBA870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 912 | `_o__getsystime` | `0xBA890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | `_o__getw` | `0xBA8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | `_o__getwc_nolock` | `0xBA8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 915 | `_o__getwch` | `0xBA8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 916 | `_o__getwch_nolock` | `0xBA900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 917 | `_o__getwche` | `0xBA920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 918 | `_o__getwche_nolock` | `0xBA940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `_o__getws` | `0xBA960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `_o__getws_s` | `0xBA980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 921 | `_o__gmtime32` | `0xBA9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 922 | `_o__gmtime32_s` | `0xBA9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 925 | `_o__heapchk` | `0xBA9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `_o__heapmin` | `0xBAA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `_o__hypot` | `0xBAA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `_o__i64toa` | `0xBAA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 931 | `_o__i64tow` | `0xBAA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `_o__invalid_parameter_noinfo` | `0xBAA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 938 | `_o__isatty` | `0xBAAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 940 | `_o__isctype_l` | `0xBAAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 941 | `_o__isleadbyte_l` | `0xBAAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `_o__ismbbalnum` | `0xBAB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 943 | `_o__ismbbalnum_l` | `0xBAB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 944 | `_o__ismbbalpha` | `0xBAB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 945 | `_o__ismbbalpha_l` | `0xBAB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 946 | `_o__ismbbblank` | `0xBAB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 947 | `_o__ismbbblank_l` | `0xBABA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 948 | `_o__ismbbgraph` | `0xBABC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 949 | `_o__ismbbgraph_l` | `0xBABE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 950 | `_o__ismbbkalnum` | `0xBAC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 951 | `_o__ismbbkalnum_l` | `0xBAC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 952 | `_o__ismbbkana` | `0xBAC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 953 | `_o__ismbbkana_l` | `0xBAC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 954 | `_o__ismbbkprint` | `0xBAC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `_o__ismbbkprint_l` | `0xBACA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 956 | `_o__ismbbkpunct` | `0xBACC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `_o__ismbbkpunct_l` | `0xBACE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 958 | `_o__ismbblead` | `0xBAD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 959 | `_o__ismbblead_l` | `0xBAD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 960 | `_o__ismbbprint` | `0xBAD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 961 | `_o__ismbbprint_l` | `0xBAD60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 962 | `_o__ismbbpunct` | `0xBAD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 963 | `_o__ismbbpunct_l` | `0xBADA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 964 | `_o__ismbbtrail` | `0xBADC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 965 | `_o__ismbbtrail_l` | `0xBADE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 966 | `_o__ismbcalnum` | `0xBAE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 967 | `_o__ismbcalnum_l` | `0xBAE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 968 | `_o__ismbcalpha` | `0xBAE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 969 | `_o__ismbcalpha_l` | `0xBAE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 970 | `_o__ismbcblank` | `0xBAE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 971 | `_o__ismbcblank_l` | `0xBAEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `_o__ismbcdigit` | `0xBAEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `_o__ismbcdigit_l` | `0xBAEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 974 | `_o__ismbcgraph` | `0xBAF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `_o__ismbcgraph_l` | `0xBAF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `_o__ismbchira` | `0xBAF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `_o__ismbchira_l` | `0xBAF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `_o__ismbckata` | `0xBAF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 979 | `_o__ismbckata_l` | `0xBAFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `_o__ismbcl0` | `0xBAFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `_o__ismbcl0_l` | `0xBAFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 982 | `_o__ismbcl1` | `0xBB000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 983 | `_o__ismbcl1_l` | `0xBB020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 984 | `_o__ismbcl2` | `0xBB040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `_o__ismbcl2_l` | `0xBB060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `_o__ismbclegal` | `0xBB080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 987 | `_o__ismbclegal_l` | `0xBB0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `_o__ismbclower` | `0xBB0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `_o__ismbclower_l` | `0xBB0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `_o__ismbcprint` | `0xBB100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `_o__ismbcprint_l` | `0xBB120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `_o__ismbcpunct` | `0xBB140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `_o__ismbcpunct_l` | `0xBB160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 994 | `_o__ismbcspace` | `0xBB180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 995 | `_o__ismbcspace_l` | `0xBB1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `_o__ismbcsymbol` | `0xBB1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 997 | `_o__ismbcsymbol_l` | `0xBB1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `_o__ismbcupper` | `0xBB200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `_o__ismbcupper_l` | `0xBB220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `_o__ismbslead` | `0xBB240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `_o__ismbslead_l` | `0xBB260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `_o__ismbstrail` | `0xBB280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `_o__ismbstrail_l` | `0xBB2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `_o__iswctype_l` | `0xBB2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `_o__itoa` | `0xBB2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `_o__j0` | `0xBB300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `_o__j1` | `0xBB320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `_o__jn` | `0xBB340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `_o__kbhit` | `0xBB360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | `_o__ld_int` | `0xBB380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `_o__ldexp` | `0xBB3A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `_o__ldlog` | `0xBB3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `_o__ldpcomp` | `0xBB3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `_o__ldpoly` | `0xBB400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `_o__ldscale` | `0xBB420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `_o__ldsign` | `0xBB440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `_o__ldsin` | `0xBB450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `_o__ldunscale` | `0xBB470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `_o__lfind` | `0xBB490` | 38 | UnwindData |  |
| 1025 | `_o__lfind_s` | `0xBB4C0` | 48 | UnwindData |  |
| 1026 | `_o__loaddll` | `0xBB500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `_o__localtime32` | `0xBB510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1028 | `_o__localtime32_s` | `0xBB530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `_o__locking` | `0xBB550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1033 | `_o__logb` | `0xBB570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1034 | `_o__logbf` | `0xBB590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `_o__lsearch` | `0xBB5B0` | 38 | UnwindData |  |
| 1036 | `_o__lsearch_s` | `0xBB5E0` | 48 | UnwindData |  |
| 1037 | `_o__lseek` | `0xBB620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `_o__lseeki64` | `0xBB640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1043 | `_o__makepath` | `0xBB660` | 38 | UnwindData |  |
| 1044 | `_o__makepath_s` | `0xBB690` | 48 | UnwindData |  |
| 1046 | `_o__mbbtombc` | `0xBB6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1047 | `_o__mbbtombc_l` | `0xBB6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1048 | `_o__mbbtype` | `0xBB710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1049 | `_o__mbbtype_l` | `0xBB720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1050 | `_o__mbccpy` | `0xBB740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1051 | `_o__mbccpy_l` | `0xBB760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `_o__mbccpy_s` | `0xBB780` | 28 | UnwindData |  |
| 1053 | `_o__mbccpy_s_l` | `0xBB7B0` | 38 | UnwindData |  |
| 1054 | `_o__mbcjistojms` | `0xBB7E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1055 | `_o__mbcjistojms_l` | `0xBB800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `_o__mbcjmstojis` | `0xBB820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `_o__mbcjmstojis_l` | `0xBB840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `_o__mbclen` | `0xBB860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `_o__mbclen_l` | `0xBB880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1060 | `_o__mbctohira` | `0xBB8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `_o__mbctohira_l` | `0xBB8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1062 | `_o__mbctokata` | `0xBB8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1063 | `_o__mbctokata_l` | `0xBB900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1064 | `_o__mbctolower` | `0xBB920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1065 | `_o__mbctolower_l` | `0xBB940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `_o__mbctombb` | `0xBB960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `_o__mbctombb_l` | `0xBB980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1068 | `_o__mbctoupper` | `0xBB9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1069 | `_o__mbctoupper_l` | `0xBB9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1070 | `_o__mblen_l` | `0xBB9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `_o__mbsbtype_l` | `0xBBA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `_o__mbscat_s` | `0xBBA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `_o__mbscat_s_l` | `0xBBA40` | 35 | UnwindData |  |
| 1075 | `_o__mbschr` | `0xBBA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `_o__mbschr_l` | `0xBBA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `_o__mbscmp_l` | `0xBBAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1079 | `_o__mbscoll` | `0xBBAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1080 | `_o__mbscoll_l` | `0xBBAF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1081 | `_o__mbscpy_s` | `0xBBB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1082 | `_o__mbscpy_s_l` | `0xBBB30` | 35 | UnwindData |  |
| 1083 | `_o__mbscspn` | `0xBBB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1084 | `_o__mbscspn_l` | `0xBBB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `_o__mbsdec` | `0xBBBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1086 | `_o__mbsdec_l` | `0xBBBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1088 | `_o__mbsicmp_l` | `0xBBBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `_o__mbsicoll` | `0xBBC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `_o__mbsicoll_l` | `0xBBC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `_o__mbsinc_l` | `0xBBC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `_o__mbslen` | `0xBBC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `_o__mbslen_l` | `0xBBC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `_o__mbslwr` | `0xBBCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `_o__mbslwr_l` | `0xBBCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1098 | `_o__mbslwr_s_l` | `0xBBCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1099 | `_o__mbsnbcat` | `0xBBD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1100 | `_o__mbsnbcat_l` | `0xBBD20` | 35 | UnwindData |  |
| 1101 | `_o__mbsnbcat_s` | `0xBBD50` | 35 | UnwindData |  |
| 1102 | `_o__mbsnbcat_s_l` | `0xBBD80` | 45 | UnwindData |  |
| 1103 | `_o__mbsnbcmp` | `0xBBDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `_o__mbsnbcmp_l` | `0xBBDE0` | 35 | UnwindData |  |
| 1105 | `_o__mbsnbcnt` | `0xBBE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `_o__mbsnbcnt_l` | `0xBBE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `_o__mbsnbcoll` | `0xBBE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1108 | `_o__mbsnbcoll_l` | `0xBBE70` | 35 | UnwindData |  |
| 1109 | `_o__mbsnbcpy` | `0xBBEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1110 | `_o__mbsnbcpy_l` | `0xBBEC0` | 35 | UnwindData |  |
| 1111 | `_o__mbsnbcpy_s` | `0xBBEF0` | 35 | UnwindData |  |
| 1112 | `_o__mbsnbcpy_s_l` | `0xBBF20` | 45 | UnwindData |  |
| 1113 | `_o__mbsnbicmp` | `0xBBF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1114 | `_o__mbsnbicmp_l` | `0xBBF80` | 35 | UnwindData |  |
| 1115 | `_o__mbsnbicoll` | `0xBBFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1116 | `_o__mbsnbicoll_l` | `0xBBFD0` | 35 | UnwindData |  |
| 1117 | `_o__mbsnbset` | `0xBC000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1118 | `_o__mbsnbset_l` | `0xBC020` | 35 | UnwindData |  |
| 1119 | `_o__mbsnbset_s` | `0xBC050` | 35 | UnwindData |  |
| 1120 | `_o__mbsnbset_s_l` | `0xBC080` | 45 | UnwindData |  |
| 1121 | `_o__mbsncat` | `0xBC0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `_o__mbsncat_l` | `0xBC0E0` | 35 | UnwindData |  |
| 1123 | `_o__mbsncat_s` | `0xBC110` | 35 | UnwindData |  |
| 1124 | `_o__mbsncat_s_l` | `0xBC140` | 45 | UnwindData |  |
| 1126 | `_o__mbsnccnt_l` | `0xBC180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1127 | `_o__mbsncmp` | `0xBC1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `_o__mbsncmp_l` | `0xBC1C0` | 35 | UnwindData |  |
| 1129 | `_o__mbsncoll` | `0xBC1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1130 | `_o__mbsncoll_l` | `0xBC210` | 35 | UnwindData |  |
| 1131 | `_o__mbsncpy` | `0xBC240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1132 | `_o__mbsncpy_l` | `0xBC260` | 35 | UnwindData |  |
| 1133 | `_o__mbsncpy_s` | `0xBC290` | 35 | UnwindData |  |
| 1134 | `_o__mbsncpy_s_l` | `0xBC2C0` | 45 | UnwindData |  |
| 1135 | `_o__mbsnextc` | `0xBC300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `_o__mbsnextc_l` | `0xBC310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `_o__mbsnicmp` | `0xBC330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `_o__mbsnicmp_l` | `0xBC350` | 35 | UnwindData |  |
| 1139 | `_o__mbsnicoll` | `0xBC380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1140 | `_o__mbsnicoll_l` | `0xBC3A0` | 35 | UnwindData |  |
| 1141 | `_o__mbsninc` | `0xBC3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `_o__mbsninc_l` | `0xBC3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `_o__mbsnlen` | `0xBC410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `_o__mbsnlen_l` | `0xBC430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `_o__mbsnset` | `0xBC450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `_o__mbsnset_l` | `0xBC470` | 35 | UnwindData |  |
| 1147 | `_o__mbsnset_s` | `0xBC4A0` | 35 | UnwindData |  |
| 1148 | `_o__mbsnset_s_l` | `0xBC4D0` | 45 | UnwindData |  |
| 1149 | `_o__mbspbrk` | `0xBC510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1150 | `_o__mbspbrk_l` | `0xBC530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `_o__mbsrchr` | `0xBC550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1152 | `_o__mbsrchr_l` | `0xBC570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1153 | `_o__mbsrev` | `0xBC590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1155 | `_o__mbsset` | `0xBC5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1156 | `_o__mbsset_l` | `0xBC5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1157 | `_o__mbsset_s` | `0xBC5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1158 | `_o__mbsset_s_l` | `0xBC610` | 28 | UnwindData |  |
| 1159 | `_o__mbsspn` | `0xBC640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1160 | `_o__mbsspn_l` | `0xBC660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1161 | `_o__mbsspnp` | `0xBC680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1162 | `_o__mbsspnp_l` | `0xBC6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1164 | `_o__mbsstr_l` | `0xBC6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1165 | `_o__mbstok` | `0xBC6E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1166 | `_o__mbstok_l` | `0xBC700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `_o__mbstok_s` | `0xBC720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1168 | `_o__mbstok_s_l` | `0xBC740` | 28 | UnwindData |  |
| 1169 | `_o__mbstowcs_l` | `0xBC770` | 28 | UnwindData |  |
| 1170 | `_o__mbstowcs_s_l` | `0xBC7A0` | 48 | UnwindData |  |
| 1172 | `_o__mbstrlen_l` | `0xBC7E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `_o__mbstrnlen` | `0xBC800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `_o__mbstrnlen_l` | `0xBC820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `_o__mbsupr` | `0xBC840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `_o__mbsupr_l` | `0xBC860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `_o__mbsupr_s` | `0xBC880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `_o__mbsupr_s_l` | `0xBC8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1179 | `_o__mbtowc_l` | `0xBC8C0` | 28 | UnwindData |  |
| 1181 | `_o__memicmp_l` | `0xBC8F0` | 28 | UnwindData |  |
| 1182 | `_o__mkdir` | `0xBC920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `_o__mkgmtime32` | `0xBC940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `_o__mktemp` | `0xBC960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1186 | `_o__mktemp_s` | `0xBC980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `_o__nextafter` | `0xBC9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `_o_nextafter` | `0xBC9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `_o__nextafterf` | `0xBC9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1622 | `_o_nextafterf` | `0xBC9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `_o__pclose` | `0xBC9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `_o__popen` | `0xBCA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `_o__purecall` | `0xBCA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1197 | `_o__putc_nolock` | `0xBCA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `_o__putch` | `0xBCA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `_o__putch_nolock` | `0xBCA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1200 | `_o__putenv` | `0xBCAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1201 | `_o__putenv_s` | `0xBCAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `_o__putw` | `0xBCAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `_o__putwc_nolock` | `0xBCB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1204 | `_o__putwch` | `0xBCB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `_o__putwch_nolock` | `0xBCB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1206 | `_o__putws` | `0xBCB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `_o__read` | `0xBCB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `_o__resetstkoflw` | `0xBCBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `_o__rmdir` | `0xBCBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `_o__rmtmp` | `0xBCBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1214 | `_o__scalb` | `0xBCC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `_o__scalbf` | `0xBCC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1216 | `_o__searchenv` | `0xBCC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `_o__searchenv_s` | `0xBCC60` | 28 | UnwindData |  |
| 1218 | `_o__seh_filter_dll` | `0xBCC90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1219 | `_o__seh_filter_exe` | `0xBCCB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `_o__set_abort_behavior` | `0xBCCD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `_o__set_new_handler` | `0xBCCE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1228 | `_o__set_thread_local_invalid_parameter_handler` | `0xBCCF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `_o__seterrormode` | `0xBCD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `_o__setmbcp` | `0xBCD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `_o__setsystime` | `0xBCD50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1233 | `_o__sleep` | `0xBCD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `_o__sopen` | `0xBCD80` | 28 | UnwindData |  |
| 1235 | `_o__sopen_dispatch` | `0xBCDB0` | 46 | UnwindData |  |
| 1236 | `_o__sopen_s` | `0xBCDF0` | 36 | UnwindData |  |
| 1237 | `_o__spawnv` | `0xBCE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1238 | `_o__spawnve` | `0xBCE40` | 34 | UnwindData |  |
| 1239 | `_o__spawnvp` | `0xBCE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1240 | `_o__spawnvpe` | `0xBCE90` | 34 | UnwindData |  |
| 1241 | `_o__splitpath` | `0xBCEC0` | 38 | UnwindData |  |
| 1243 | `_o__stat32` | `0xBCEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1244 | `_o__stat32i64` | `0xBCF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1245 | `_o__stat64` | `0xBCF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1247 | `_o__strcoll_l` | `0xBCF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `_o__strdate` | `0xBCF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `_o__strdate_s` | `0xBCF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1251 | `_o__strerror` | `0xBCFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1252 | `_o__strerror_s` | `0xBCFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `_o__strftime_l` | `0xBCFF0` | 38 | UnwindData |  |
| 1255 | `_o__stricmp_l` | `0xBD020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `_o__stricoll_l` | `0xBD040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `_o__strlwr_s_l` | `0xBD060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1263 | `_o__strncoll_l` | `0xBD080` | 35 | UnwindData |  |
| 1265 | `_o__strnicmp_l` | `0xBD0B0` | 35 | UnwindData |  |
| 1266 | `_o__strnicoll` | `0xBD0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1267 | `_o__strnicoll_l` | `0xBD100` | 35 | UnwindData |  |
| 1268 | `_o__strnset_s` | `0xBD130` | 28 | UnwindData |  |
| 1269 | `_o__strset_s` | `0xBD160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1270 | `_o__strtime` | `0xBD180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1271 | `_o__strtime_s` | `0xBD1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1272 | `_o__strtod_l` | `0xBD1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1277 | `_o__strtold_l` | `0xBD1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1273 | `_o__strtof_l` | `0xBD1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1275 | `_o__strtoi64_l` | `0xBD200` | 35 | UnwindData |  |
| 1278 | `_o__strtoll_l` | `0xBD200` | 35 | UnwindData |  |
| 1276 | `_o__strtol_l` | `0xBD230` | 28 | UnwindData |  |
| 1280 | `_o__strtoui64_l` | `0xBD260` | 35 | UnwindData |  |
| 1282 | `_o__strtoull_l` | `0xBD260` | 35 | UnwindData |  |
| 1281 | `_o__strtoul_l` | `0xBD290` | 28 | UnwindData |  |
| 1283 | `_o__strupr` | `0xBD2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `_o__strupr_l` | `0xBD2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1286 | `_o__strupr_s_l` | `0xBD300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `_o__strxfrm_l` | `0xBD320` | 28 | UnwindData |  |
| 1288 | `_o__swab` | `0xBD350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `_o__telli64` | `0xBD370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1291 | `_o__timespec32_get` | `0xBD390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1292 | `_o__timespec64_get` | `0xBD3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1294 | `_o__tolower_l` | `0xBD3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1295 | `_o__toupper` | `0xBD3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1296 | `_o__toupper_l` | `0xBD410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1298 | `_o__towupper_l` | `0xBD430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `_o__tzset` | `0xBD450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1300 | `_o__ui64toa` | `0xBD470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `_o__ui64tow` | `0xBD490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `_o__ultoa` | `0xBD4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1308 | `_o__umask` | `0xBD4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1310 | `_o__ungetc_nolock` | `0xBD4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `_o__ungetch` | `0xBD510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1312 | `_o__ungetch_nolock` | `0xBD530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `_o__ungetwc_nolock` | `0xBD550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1314 | `_o__ungetwch` | `0xBD570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1315 | `_o__ungetwch_nolock` | `0xBD590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1316 | `_o__unlink` | `0xBD5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `_o__unloaddll` | `0xBD5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `_o__utime32` | `0xBD5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `_o__utime64` | `0xBD610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1322 | `_o__waccess_s` | `0xBD630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `_o__wasctime` | `0xBD650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1324 | `_o__wasctime_s` | `0xBD660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1325 | `_o__wchdir` | `0xBD680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `_o__wchmod` | `0xBD6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1327 | `_o__wcreat` | `0xBD6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1329 | `_o__wcscoll_l` | `0xBD6E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `_o__wcserror` | `0xBD700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `_o__wcserror_s` | `0xBD710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1333 | `_o__wcsftime_l` | `0xBD730` | 38 | UnwindData |  |
| 1336 | `_o__wcsicoll` | `0xBD760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `_o__wcsicoll_l` | `0xBD780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1341 | `_o__wcslwr_s_l` | `0xBD7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1342 | `_o__wcsncoll` | `0xBD7C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1343 | `_o__wcsncoll_l` | `0xBD7E0` | 35 | UnwindData |  |
| 1345 | `_o__wcsnicmp_l` | `0xBD810` | 35 | UnwindData |  |
| 1347 | `_o__wcsnicoll_l` | `0xBD840` | 35 | UnwindData |  |
| 1349 | `_o__wcsnset_s` | `0xBD870` | 29 | UnwindData |  |
| 1350 | `_o__wcsset` | `0xBD8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1351 | `_o__wcsset_s` | `0xBD8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1353 | `_o__wcstof_l` | `0xBD8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `_o__wcstoi64_l` | `0xBD900` | 35 | UnwindData |  |
| 1358 | `_o__wcstoll_l` | `0xBD900` | 35 | UnwindData |  |
| 1356 | `_o__wcstol_l` | `0xBD930` | 28 | UnwindData |  |
| 1359 | `_o__wcstombs_l` | `0xBD960` | 28 | UnwindData |  |
| 1362 | `_o__wcstoui64_l` | `0xBD990` | 35 | UnwindData |  |
| 1364 | `_o__wcstoull_l` | `0xBD990` | 35 | UnwindData |  |
| 1363 | `_o__wcstoul_l` | `0xBD9C0` | 28 | UnwindData |  |
| 1366 | `_o__wcsupr_l` | `0xBD9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1368 | `_o__wcsupr_s_l` | `0xBDA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1369 | `_o__wcsxfrm_l` | `0xBDA30` | 28 | UnwindData |  |
| 1370 | `_o__wctime32` | `0xBDA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1371 | `_o__wctime32_s` | `0xBDA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1372 | `_o__wctime64` | `0xBDA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1373 | `_o__wctime64_s` | `0xBDAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1374 | `_o__wctomb_l` | `0xBDAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1375 | `_o__wctomb_s_l` | `0xBDAE0` | 39 | UnwindData |  |
| 1376 | `_o__wdupenv_s` | `0xBDB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1377 | `_o__wexecv` | `0xBDB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1378 | `_o__wexecve` | `0xBDB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1379 | `_o__wexecvp` | `0xBDB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1380 | `_o__wexecvpe` | `0xBDB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1381 | `_o__wfdopen` | `0xBDBB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1382 | `_o__wfindfirst32` | `0xBDBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1383 | `_o__wfindfirst32i64` | `0xBDBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `_o__wfindfirst64` | `0xBDC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1385 | `_o__wfindfirst64i32` | `0xBDC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1386 | `_o__wfindnext32` | `0xBDC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `_o__wfindnext32i64` | `0xBDC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1388 | `_o__wfindnext64` | `0xBDC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1389 | `_o__wfindnext64i32` | `0xBDCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1390 | `_o__wfopen` | `0xBDCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1391 | `_o__wfopen_s` | `0xBDCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1392 | `_o__wfreopen` | `0xBDD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1393 | `_o__wfreopen_s` | `0xBDD20` | 28 | UnwindData |  |
| 1396 | `_o__wgetcwd` | `0xBDD50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1397 | `_o__wgetdcwd` | `0xBDD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1400 | `_o__wmakepath` | `0xBDD90` | 38 | UnwindData |  |
| 1403 | `_o__wmktemp` | `0xBDDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1404 | `_o__wmktemp_s` | `0xBDDE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1405 | `_o__wperror` | `0xBDE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `_o__wputenv` | `0xBDE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1409 | `_o__wremove` | `0xBDE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1410 | `_o__wrename` | `0xBDE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1411 | `_o__write` | `0xBDE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1412 | `_o__wrmdir` | `0xBDE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1413 | `_o__wsearchenv` | `0xBDEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1414 | `_o__wsearchenv_s` | `0xBDED0` | 28 | UnwindData |  |
| 1416 | `_o__wsopen_dispatch` | `0xBDF00` | 46 | UnwindData |  |
| 1417 | `_o__wsopen_s` | `0xBDF40` | 36 | UnwindData |  |
| 1418 | `_o__wspawnv` | `0xBDF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1419 | `_o__wspawnve` | `0xBDF90` | 34 | UnwindData |  |
| 1420 | `_o__wspawnvp` | `0xBDFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1421 | `_o__wspawnvpe` | `0xBDFE0` | 34 | UnwindData |  |
| 1422 | `_o__wsplitpath` | `0xBE010` | 38 | UnwindData |  |
| 1424 | `_o__wstat32` | `0xBE040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `_o__wstat32i64` | `0xBE060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1426 | `_o__wstat64` | `0xBE080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1427 | `_o__wstat64i32` | `0xBE0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1428 | `_o__wstrdate` | `0xBE0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1429 | `_o__wstrdate_s` | `0xBE0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `_o__wstrtime` | `0xBE100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `_o__wstrtime_s` | `0xBE120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1433 | `_o__wtmpnam_s` | `0xBE140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1435 | `_o__wtof_l` | `0xBE160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1438 | `_o__wtoi64_l` | `0xBE180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1443 | `_o__wtoll_l` | `0xBE180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1439 | `_o__wtoi_l` | `0xBE1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1441 | `_o__wtol_l` | `0xBE1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `_o__wunlink` | `0xBE1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1445 | `_o__wutime32` | `0xBE1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1447 | `_o__y0` | `0xBE200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `_o__y1` | `0xBE220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1449 | `_o__yn` | `0xBE240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1450 | `_o_abort` | `0xBE260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1453 | `_o_acosh` | `0xBE280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1454 | `_o_acoshf` | `0xBE2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1455 | `_o_acoshl` | `0xBE2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1456 | `_o_asctime` | `0xBE2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1457 | `_o_asctime_s` | `0xBE2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1460 | `_o_asinh` | `0xBE310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1461 | `_o_asinhf` | `0xBE330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1462 | `_o_asinhl` | `0xBE350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1467 | `_o_atanh` | `0xBE370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1468 | `_o_atanhf` | `0xBE390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1469 | `_o_atanhl` | `0xBE3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1478 | `_o_cbrt` | `0xBE3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `_o_cbrtf` | `0xBE3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1482 | `_o_clearerr` | `0xBE410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1483 | `_o_clearerr_s` | `0xBE430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1487 | `_o_coshf` | `0xBE450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1488 | `_o_erf` | `0xBE470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1489 | `_o_erfc` | `0xBE490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1490 | `_o_erfcf` | `0xBE4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1491 | `_o_erfcl` | `0xBE4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1492 | `_o_erff` | `0xBE4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1493 | `_o_erfl` | `0xBE510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1496 | `_o_exp2` | `0xBE530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1497 | `_o_exp2f` | `0xBE550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1498 | `_o_exp2l` | `0xBE570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1500 | `_o_fabs` | `0xBE590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1508 | `_o_fgetwc` | `0xBE5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `_o_fma` | `0xBE5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1513 | `_o_fmaf` | `0xBE5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1514 | `_o_fmal` | `0xBE610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1517 | `_o_fopen` | `0xBE630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1518 | `_o_fopen_s` | `0xBE650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `_o_fputws` | `0xBE670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1524 | `_o_fread_s` | `0xBE690` | 45 | UnwindData |  |
| 1527 | `_o_freopen_s` | `0xBE6D0` | 28 | UnwindData |  |
| 1530 | `_o_fsetpos` | `0xBE700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `_o_ftell` | `0xBE720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1533 | `_o_getc` | `0xBE740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1537 | `_o_gets` | `0xBE760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `_o_gets_s` | `0xBE780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `_o_getwc` | `0xBE7A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1541 | `_o_hypot` | `0xBE7C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1542 | `_o_is_wctype` | `0xBE7E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1545 | `_o_isblank` | `0xBE800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1548 | `_o_isgraph` | `0xBE820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1549 | `_o_isleadbyte` | `0xBE840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1550 | `_o_islower` | `0xBE860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1558 | `_o_iswblank` | `0xBE880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1562 | `_o_iswgraph` | `0xBE8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1571 | `_o_lgamma` | `0xBE8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1572 | `_o_lgammaf` | `0xBE8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1573 | `_o_lgammal` | `0xBE900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1574 | `_o_llrint` | `0xBE920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1575 | `_o_llrintf` | `0xBE940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1576 | `_o_llrintl` | `0xBE960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `_o_llroundf` | `0xBE980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1584 | `_o_log1p` | `0xBE9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1585 | `_o_log1pf` | `0xBE9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1586 | `_o_log1pl` | `0xBE9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1589 | `_o_log2l` | `0xBEA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1590 | `_o_logb` | `0xBEA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1591 | `_o_logbf` | `0xBEA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1592 | `_o_logbl` | `0xBEA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1594 | `_o_lrint` | `0xBEA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1596 | `_o_lrintl` | `0xBEAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1601 | `_o_mblen` | `0xBEAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1602 | `_o_mbrlen` | `0xBEAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1603 | `_o_mbrtoc16` | `0xBEB00` | 28 | UnwindData |  |
| 1604 | `_o_mbrtoc32` | `0xBEB30` | 28 | UnwindData |  |
| 1605 | `_o_mbrtowc` | `0xBEB60` | 28 | UnwindData |  |
| 1606 | `_o_mbsrtowcs` | `0xBEB90` | 28 | UnwindData |  |
| 1607 | `_o_mbsrtowcs_s` | `0xBEBC0` | 48 | UnwindData |  |
| 1615 | `_o_nan` | `0xBEC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1616 | `_o_nanf` | `0xBEC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `_o_nanl` | `0xBEC30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1618 | `_o_nearbyint` | `0xBEC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1619 | `_o_nearbyintf` | `0xBEC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1620 | `_o_nearbyintl` | `0xBEC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1623 | `_o_nextafterl` | `0xBECA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1626 | `_o_nexttowardl` | `0xBECA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1624 | `_o_nexttoward` | `0xBECC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1625 | `_o_nexttowardf` | `0xBECE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1629 | `_o_putc` | `0xBED00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `_o_putchar` | `0xBED20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1631 | `_o_puts` | `0xBED40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1632 | `_o_putwc` | `0xBED60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1633 | `_o_putwchar` | `0xBED80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1636 | `_o_raise` | `0xBEDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1640 | `_o_remainder` | `0xBEDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1641 | `_o_remainderf` | `0xBEDE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `_o_remainderl` | `0xBEE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1643 | `_o_remove` | `0xBEE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `_o_remquo` | `0xBEE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1645 | `_o_remquof` | `0xBEE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1646 | `_o_remquol` | `0xBEE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1647 | `_o_rename` | `0xBEEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1649 | `_o_rint` | `0xBEEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1650 | `_o_rintf` | `0xBEEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1651 | `_o_rintl` | `0xBEF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1655 | `_o_scalbln` | `0xBEF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1656 | `_o_scalblnf` | `0xBEF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1657 | `_o_scalblnl` | `0xBEF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1658 | `_o_scalbn` | `0xBEF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1660 | `_o_scalbnl` | `0xBEF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1659 | `_o_scalbnf` | `0xBEFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1662 | `_o_setbuf` | `0xBEFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1664 | `_o_setvbuf` | `0xBEFE0` | 28 | UnwindData |  |
| 1667 | `_o_sinh` | `0xBF010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `_o_sinhf` | `0xBF030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1673 | `_o_strcoll` | `0xBF050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1675 | `_o_strerror` | `0xBF070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1676 | `_o_strerror_s` | `0xBF080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1689 | `_o_system` | `0xBF0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1694 | `_o_terminate` | `0xBF0C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1695 | `_o_tgamma` | `0xBF0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1696 | `_o_tgammaf` | `0xBF0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1697 | `_o_tgammal` | `0xBF110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1698 | `_o_tmpfile_s` | `0xBF130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1699 | `_o_tmpnam_s` | `0xBF140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1704 | `_o_ungetc` | `0xBF160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1705 | `_o_ungetwc` | `0xBF180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1706 | `_o_wcrtomb` | `0xBF1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1707 | `_o_wcrtomb_s` | `0xBF1C0` | 39 | UnwindData |  |
| 1709 | `_o_wcscoll` | `0xBF1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1710 | `_o_wcscpy` | `0xBF210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1715 | `_o_wcsrtombs` | `0xBF230` | 28 | UnwindData |  |
| 1716 | `_o_wcsrtombs_s` | `0xBF260` | 48 | UnwindData |  |
| 1728 | `_o_wctob` | `0xBF2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1729 | `_o_wctomb` | `0xBF2C0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `_atodbl_l` | `0xBF450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `_atoflt` | `0xBF460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `_atoflt_l` | `0xBF470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `_atoldbl` | `0xBF480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `_atoi64_l` | `0xBF490` | 76 | UnwindData |  |
| 164 | `_atoll_l` | `0xBF490` | 76 | UnwindData |  |
| 160 | `_atoi_l` | `0xBF4F0` | 74 | UnwindData |  |
| 161 | `_atol_l` | `0xBF4F0` | 74 | UnwindData |  |
| 2026 | `_wtoi64_l` | `0xBF540` | 76 | UnwindData |  |
| 2031 | `_wtoll_l` | `0xBF540` | 76 | UnwindData |  |
| 2066 | `c16rtomb` | `0xBF5A0` | 64 | UnwindData |  |
| 2067 | `c32rtomb` | `0xBF5F0` | 62 | UnwindData |  |
| 454 | `_ismbstrail` | `0xBF740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `_ismbstrail_l` | `0xBF750` | 162 | UnwindData |  |
| 468 | `_iswctype_l` | `0xBF800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2234 | `is_wctype` | `0xBF800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `_mblen_l` | `0xBF810` | 61 | UnwindData |  |
| 2300 | `mbrtoc16` | `0xBF960` | 67 | UnwindData |  |
| 648 | `_mbstowcs_l` | `0xBF9B0` | 63 | UnwindData |  |
| 1926 | `_wcstof_l` | `0xBFA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1842 | `_strtol_l` | `0xBFA10` | 81 | UnwindData |  |
| 1847 | `_strtoul_l` | `0xBFA70` | 81 | UnwindData |  |
| 1928 | `_wcstoi64_l` | `0xBFAD0` | 83 | UnwindData |  |
| 1929 | `_wcstoimax_l` | `0xBFAD0` | 83 | UnwindData |  |
| 1932 | `_wcstoll_l` | `0xBFAD0` | 83 | UnwindData |  |
| 1936 | `_wcstoui64_l` | `0xBFB30` | 83 | UnwindData |  |
| 1938 | `_wcstoull_l` | `0xBFB30` | 83 | UnwindData |  |
| 1939 | `_wcstoumax_l` | `0xBFB30` | 83 | UnwindData |  |
| 1937 | `_wcstoul_l` | `0xBFB90` | 81 | UnwindData |  |
| 1865 | `_toupper` | `0xBFBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2460 | `wcsrtombs` | `0xBFC00` | 67 | UnwindData |  |
| 1933 | `_wcstombs_l` | `0xBFC50` | 63 | UnwindData |  |
| 1949 | `_wctomb_l` | `0xBFCA0` | 135 | UnwindData |  |
| 1950 | `_wctomb_s_l` | `0xBFD30` | 71 | UnwindData |  |
| 2431 | `towctrans` | `0xBFD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2481 | `wctrans` | `0xBFDA0` | 96 | UnwindData |  |
| 78 | `__iscsym` | `0xBFE10` | 123 | UnwindData |  |
| 79 | `__iscsymf` | `0xBFEA0` | 162 | UnwindData |  |
| 132 | `__toascii` | `0xBFF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `_isblank_l` | `0xBFF60` | 189 | UnwindData |  |
| 387 | `_iscntrl_l` | `0xC0030` | 189 | UnwindData |  |
| 391 | `_isgraph_l` | `0xC0100` | 196 | UnwindData |  |
| 393 | `_islower_l` | `0xC01D0` | 189 | UnwindData |  |
| 458 | `_isprint_l` | `0xC02A0` | 196 | UnwindData |  |
| 460 | `_isspace_l` | `0xC0370` | 189 | UnwindData |  |
| 477 | `_isxdigit_l` | `0xC0440` | 196 | UnwindData |  |
| 651 | `_mbstrlen_l` | `0xC0510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `_mbstrnlen` | `0xC0530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `_mbstrnlen_l` | `0xC0540` | 52 | UnwindData |  |
| 80 | `__iswcsym` | `0xC0580` | 44 | UnwindData |  |
| 466 | `_iswcsym_l` | `0xC0580` | 44 | UnwindData |  |
| 81 | `__iswcsymf` | `0xC05C0` | 44 | UnwindData |  |
| 467 | `_iswcsymf_l` | `0xC05C0` | 44 | UnwindData |  |
| 474 | `_iswspace_l` | `0xC0600` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `__threadhandle` | `0xC06F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `__threadid` | `0xC0700` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `__pwctype_func` | `0xC0A00` | 2,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `__p__mbcasemap` | `0xC1550` | 25 | UnwindData |  |
| 90 | `__p__mbctype` | `0xC1570` | 25 | UnwindData |  |
| 350 | `_getmbcp` | `0xC1590` | 76 | UnwindData |  |
| 317 | `_get_doserrno` | `0xC1690` | 41 | UnwindData |  |
| 1768 | `_seh_filter_dll` | `0xC16C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `_get_invalid_parameter_handler` | `0xC16E0` | 43 | UnwindData |  |
| 332 | `_get_thread_local_invalid_parameter_handler` | `0xC1720` | 26 | UnwindData |  |
| 380 | `_invalid_parameter_noinfo_noreturn` | `0xC1740` | 31 | UnwindData |  |
| 73 | `__fpecode` | `0xC1770` | 18 | UnwindData |  |
| 98 | `__pxcptinfoptrs` | `0xC1790` | 18 | UnwindData |  |
| 2343 | `raise` | `0xC17B0` | 518 | UnwindData |  |
| 2421 | `terminate` | `0xC19C0` | 31 | UnwindData |  |
| 1986 | `_wperror` | `0xC19F0` | 210 | UnwindData |  |
| 138 | `__wcserror` | `0xC1E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `__wcserror_s` | `0xC1EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1813 | `_strerror` | `0xC1EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1814 | `_strerror_s` | `0xC1EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `__p__acmdln` | `0xC1ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `__p__pgmptr` | `0xC1EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `__p__wcmdln` | `0xC1EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `__p__wpgmptr` | `0xC1F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `_get_pgmptr` | `0xC1F10` | 54 | UnwindData |  |
| 337 | `_get_wpgmptr` | `0xC1F50` | 54 | UnwindData |  |
| 152 | `_assert` | `0xC2A70` | 114 | UnwindData |  |
| 1896 | `_wassert` | `0xC2AF0` | 114 | UnwindData |  |
| 171 | `_c_exit` | `0xC2C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2342 | `quick_exit` | `0xC2CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `_crt_at_quick_exit` | `0xC2CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `_endthread` | `0xC2CE0` | 12 | UnwindData |  |
| 263 | `_fgetchar` | `0xC2D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2221 | `getchar` | `0xC2D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `_fputc_nolock` | `0xC2D20` | 60 | UnwindData |  |
| 286 | `_fputchar` | `0xC2D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `_putc_nolock` | `0xC2D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2336 | `putchar` | `0xC2DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `_fputwc_nolock` | `0xC2DB0` | 64 | UnwindData |  |
| 288 | `_fputwchar` | `0xC2E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1745 | `_putwc_nolock` | `0xC2E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2338 | `putwc` | `0xC2E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2339 | `putwchar` | `0xC2E40` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1972 | `_wfreopen` | `0xC2F60` | 47 | UnwindData |  |
| 1973 | `_wfreopen_s` | `0xC2FA0` | 22 | UnwindData |  |
| 2214 | `freopen_s` | `0xC2FC0` | 22 | UnwindData |  |
| 293 | `_fseek_nolock` | `0xC2FE0` | 60 | UnwindData |  |
| 295 | `_fseeki64_nolock` | `0xC3030` | 60 | UnwindData |  |
| 301 | `_ftell_nolock` | `0xC3210` | 54 | UnwindData |  |
| 303 | `_ftelli64_nolock` | `0xC3250` | 56 | UnwindData |  |
| 359 | `_getws` | `0xC3410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `_getws_s` | `0xC3430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2224 | `gets` | `0xC3440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2225 | `gets_s` | `0xC3460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `_getw` | `0xC3470` | 170 | UnwindData |  |
| 109 | `__stdio_common_vfprintf_p` | `0xC5810` | 74 | UnwindData |  |
| 113 | `__stdio_common_vfwprintf_p` | `0xC5860` | 74 | UnwindData |  |
| 1781 | `_set_printf_count_output` | `0xC58B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1744 | `_putw` | `0xC58E0` | 152 | UnwindData |  |
| 1748 | `_putws` | `0xC5AE0` | 163 | UnwindData |  |
| 349 | `_getmaxstdio` | `0xC5D10` | 37 | UnwindData |  |
| 1786 | `_setmaxstdio` | `0xC5D40` | 87 | UnwindData |  |
| 1858 | `_tempnam` | `0xC6290` | 14 | UnwindData |  |
| 2019 | `_wtempnam` | `0xC62B0` | 14 | UnwindData |  |
| 2020 | `_wtmpnam` | `0xC6A50` | 38 | UnwindData |  |
| 2021 | `_wtmpnam_s` | `0xC6A80` | 59 | UnwindData |  |
| 2425 | `tmpfile` | `0xC6AD0` | 35 | UnwindData |  |
| 2426 | `tmpfile_s` | `0xC6B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2427 | `tmpnam` | `0xC6B10` | 38 | UnwindData |  |
| 497 | `_lfind` | `0xC6B40` | 155 | UnwindData |  |
| 498 | `_lfind_s` | `0xC6BF0` | 159 | UnwindData |  |
| 512 | `_lsearch` | `0xC6CA0` | 216 | UnwindData |  |
| 513 | `_lsearch_s` | `0xC6D80` | 222 | UnwindData |  |
| 1761 | `_rotl64` | `0xC6E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1763 | `_rotr64` | `0xC6E90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1818 | `_stricoll` | `0xC6EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1819 | `_stricoll_l` | `0xC6F00` | 209 | UnwindData |  |
| 1821 | `_strlwr_l` | `0xC6FE0` | 30 | UnwindData |  |
| 1824 | `_strncoll` | `0xC7010` | 79 | UnwindData |  |
| 1825 | `_strncoll_l` | `0xC7070` | 247 | UnwindData |  |
| 1831 | `_strnset_s` | `0xC71B0` | 116 | UnwindData |  |
| 1834 | `_strset_s` | `0xC7230` | 73 | UnwindData |  |
| 1851 | `_strupr_l` | `0xC7280` | 30 | UnwindData |  |
| 1911 | `_wcslwr_l` | `0xC72B0` | 30 | UnwindData |  |
| 140 | `__wcsncnt` | `0xC72E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1914 | `_wcsncoll` | `0xC7310` | 79 | UnwindData |  |
| 1921 | `_wcsnset_s` | `0xC7370` | 122 | UnwindData |  |
| 1923 | `_wcsset` | `0xC73F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1941 | `_wcsupr_l` | `0xC7410` | 30 | UnwindData |  |
| 1944 | `_wcsxfrm_l` | `0xC7440` | 370 | UnwindData |  |
| 2477 | `wcsxfrm` | `0xC75C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `_j0` | `0xC75D0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `_j1` | `0xC77D0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `_jn` | `0xC7A00` | 372 | UnwindData |  |
| 2035 | `_y0` | `0xC7B80` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2069 | `cabsf` | `0xC8070` | 30 | UnwindData |  |
| 2068 | `cabs` | `0xC80A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2070 | `cabsl` | `0xC80A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2071 | `cacos` | `0xC80C0` | 828 | UnwindData |  |
| 2076 | `cacosl` | `0xC8410` | 818 | UnwindData |  |
| 2079 | `cargf` | `0xC8750` | 30 | UnwindData |  |
| 2086 | `casinl` | `0xC8780` | 84 | UnwindData |  |
| 2087 | `catan` | `0xC87E0` | 84 | UnwindData |  |
| 2088 | `catanf` | `0xC8840` | 78 | UnwindData |  |
| 2089 | `catanh` | `0xC88A0` | 951 | UnwindData |  |
| 2091 | `catanhl` | `0xC8C60` | 951 | UnwindData |  |
| 2092 | `catanl` | `0xC9020` | 84 | UnwindData |  |
| 2096 | `ccos` | `0xC9080` | 66 | UnwindData |  |
| 2097 | `ccosf` | `0xC90D0` | 45 | UnwindData |  |
| 2098 | `ccosh` | `0xC9110` | 574 | UnwindData |  |
| 2099 | `ccoshf` | `0xC9360` | 502 | UnwindData |  |
| 2100 | `ccoshl` | `0xC9560` | 574 | UnwindData |  |
| 2101 | `ccosl` | `0xC97B0` | 66 | UnwindData |  |
| 2105 | `cexpf` | `0xC9800` | 538 | UnwindData |  |
| 2114 | `clog10` | `0xC9A20` | 56 | UnwindData |  |
| 2115 | `clog10f` | `0xC9A60` | 55 | UnwindData |  |
| 2116 | `clog10l` | `0xC9AA0` | 56 | UnwindData |  |
| 2117 | `clogf` | `0xC9AE0` | 710 | UnwindData |  |
| 3 | `_Cmulcr` | `0xC9DB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `_LCmulcr` | `0xC9DB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `_FCmulcr` | `0xC9DE0` | 40 | UnwindData |  |
| 2130 | `cpowf` | `0xC9E10` | 169 | UnwindData |  |
| 2131 | `cpowl` | `0xC9EC0` | 196 | UnwindData |  |
| 2132 | `cproj` | `0xC9F90` | 300 | UnwindData |  |
| 2134 | `cprojl` | `0xC9F90` | 300 | UnwindData |  |
| 2133 | `cprojf` | `0xCA0D0` | 230 | UnwindData |  |
| 2138 | `csin` | `0xCA1C0` | 84 | UnwindData |  |
| 2139 | `csinf` | `0xCA220` | 78 | UnwindData |  |
| 2143 | `csinl` | `0xCA280` | 84 | UnwindData |  |
| 2147 | `ctan` | `0xCA2E0` | 84 | UnwindData |  |
| 2152 | `ctanl` | `0xCA2E0` | 84 | UnwindData |  |
| 2148 | `ctanf` | `0xCA340` | 78 | UnwindData |  |
| 2149 | `ctanh` | `0xCA3A0` | 570 | UnwindData |  |
| 2151 | `ctanhl` | `0xCA3A0` | 570 | UnwindData |  |
| 2150 | `ctanhf` | `0xCA5E0` | 463 | UnwindData |  |
| 2154 | `erf` | `0xCA7C0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2155 | `erfc` | `0xCA970` | 1,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2156 | `erfcf` | `0xCAEE0` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2157 | `erfcl` | `0xCB1C0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2158 | `erff` | `0xCB390` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2159 | `erfl` | `0xCB540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `_ldexp` | `0xCB560` | 1,122 | UnwindData |  |
| 314 | `_get_FMA3_enable` | `0xCBBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1770 | `_set_FMA3_enable` | `0xCBC00` | 6,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2195 | `fmal` | `0xCD730` | 2,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `_dsin` | `0xCE2C0` | 401 | UnwindData |  |
| 2265 | `lgamma` | `0xCE460` | 2,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2266 | `lgammaf` | `0xCEF70` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `_ldsin` | `0xCF600` | 401 | UnwindData |  |
| 2267 | `lgammal` | `0xCFA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2272 | `llrintl` | `0xCFAA0` | 106 | UnwindData |  |
| 2274 | `llroundf` | `0xCFB10` | 84 | UnwindData |  |
| 2293 | `lrintl` | `0xCFB70` | 105 | UnwindData |  |
| 100 | `__setusermatherr` | `0xCFBE0` | 56 | UnwindData |  |
| 2329 | `norm` | `0xCFCD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2331 | `norml` | `0xCFCD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2330 | `normf` | `0xCFCF0` | 36 | UnwindData |  |
| 2349 | `remainderl` | `0xCFD20` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2422 | `tgamma` | `0xCFDC0` | 2,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2423 | `tgammaf` | `0xD06A0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2424 | `tgammal` | `0xD0B50` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `_cgets` | `0xD0C40` | 115 | UnwindData |  |
| 177 | `_cgets_s` | `0xD0CC0` | 272 | UnwindData |  |
| 178 | `_cgetws` | `0xD0DE0` | 116 | UnwindData |  |
| 179 | `_cgetws_s` | `0xD0E60` | 420 | UnwindData |  |
| 57 | `__conio_common_vcprintf` | `0xD3BA0` | 61 | UnwindData |  |
| 58 | `__conio_common_vcprintf_p` | `0xD3BF0` | 61 | UnwindData |  |
| 59 | `__conio_common_vcprintf_s` | `0xD3C40` | 61 | UnwindData |  |
| 61 | `__conio_common_vcwprintf` | `0xD3C90` | 61 | UnwindData |  |
| 62 | `__conio_common_vcwprintf_p` | `0xD3CE0` | 61 | UnwindData |  |
| 63 | `__conio_common_vcwprintf_s` | `0xD3D30` | 61 | UnwindData |  |
| 198 | `_cputs` | `0xD3D80` | 120 | UnwindData |  |
| 60 | `__conio_common_vcscanf` | `0xD68E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `__conio_common_vcwscanf` | `0xD68F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `_getch` | `0xD6900` | 48 | UnwindData |  |
| 340 | `_getch_nolock` | `0xD6940` | 365 | UnwindData |  |
| 341 | `_getche` | `0xD6AC0` | 48 | UnwindData |  |
| 1881 | `_ungetch` | `0xD6BD0` | 52 | UnwindData |  |
| 1882 | `_ungetch_nolock` | `0xD6C10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `_getwch` | `0xD6C50` | 50 | UnwindData |  |
| 356 | `_getwch_nolock` | `0xD6C90` | 229 | UnwindData |  |
| 357 | `_getwche` | `0xD6D80` | 50 | UnwindData |  |
| 1884 | `_ungetwch` | `0xD6DC0` | 56 | UnwindData |  |
| 1885 | `_ungetwch_nolock` | `0xD6E00` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `_popen` | `0xD72F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1987 | `_wpopen` | `0xD7300` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1740 | `_putch` | `0xD7380` | 54 | UnwindData |  |
| 1741 | `_putch_nolock` | `0xD73C0` | 54 | UnwindData |  |
| 1746 | `_putwch` | `0xD7470` | 55 | UnwindData |  |
| 270 | `_findfirst32` | `0xD7DB0` | 45 | UnwindData |  |
| 271 | `_findfirst32i64` | `0xD7DF0` | 45 | UnwindData |  |
| 274 | `_findnext32` | `0xD7E30` | 45 | UnwindData |  |
| 275 | `_findnext32i64` | `0xD7E70` | 45 | UnwindData |  |
| 276 | `_findnext64` | `0xD7EB0` | 45 | UnwindData |  |
| 1962 | `_wfindfirst32` | `0xD7EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1963 | `_wfindfirst32i64` | `0xD7F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1964 | `_wfindfirst64` | `0xD7F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1966 | `_wfindnext32` | `0xD7F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1967 | `_wfindnext32i64` | `0xD7F30` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `_fstat32` | `0xD85E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1804 | `_stat32` | `0xD85F0` | 143 | UnwindData |  |
| 1805 | `_stat32i64` | `0xD8690` | 143 | UnwindData |  |
| 2010 | `_wstat32` | `0xD8730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2011 | `_wstat32i64` | `0xD8740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `_chsize` | `0xD8750` | 21 | UnwindData |  |
| 186 | `_chsize_s` | `0xD8770` | 60 | UnwindData |  |
| 200 | `_creat` | `0xD87C0` | 63 | UnwindData |  |
| 1899 | `_wcreat` | `0xD8810` | 63 | UnwindData |  |
| 230 | `_eof` | `0xD8990` | 156 | UnwindData |  |
| 266 | `_filelength` | `0xD8B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `_filelengthi64` | `0xD8B70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 666 | `_mktemp_s` | `0xD8BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1983 | `_wmktemp` | `0xD8BD0` | 82 | UnwindData |  |
| 1984 | `_wmktemp_s` | `0xD8C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1791 | `_sopen` | `0xD8C40` | 68 | UnwindData |  |
| 204 | `_ctime32` | `0xD8F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `_ctime32_s` | `0xD8F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1945 | `_wctime32` | `0xD8F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1946 | `_wctime32_s` | `0xD8FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1947 | `_wctime64` | `0xD8FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 663 | `_mkgmtime32` | `0xD8FC0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1810 | `_strdate` | `0xD9100` | 36 | UnwindData |  |
| 1811 | `_strdate_s` | `0xD9130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2014 | `_wstrdate` | `0xD9140` | 36 | UnwindData |  |
| 1835 | `_strtime` | `0xD9280` | 36 | UnwindData |  |
| 1836 | `_strtime_s` | `0xD92B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2016 | `_wstrtime` | `0xD92C0` | 36 | UnwindData |  |
| 1861 | `_timespec32_get` | `0xD9390` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `_futime32` | `0xD95E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1890 | `_utime32` | `0xD95F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2033 | `_wutime32` | `0xD9600` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1905 | `_wcsftime_l` | `0xD9680` | 30 | UnwindData |  |
| 1766 | `_searchenv` | `0xD9860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1767 | `_searchenv_s` | `0xD9880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1995 | `_wsearchenv_s` | `0xD9890` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `_getdllprocaddr` | `0xD9DA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `_loaddll` | `0xD9DD0` | 109 | UnwindData |  |
| 1887 | `_unloaddll` | `0xD9E50` | 32 | UnwindData |  |
| 233 | `_execl` | `0xDA090` | 50 | UnwindData |  |
| 234 | `_execle` | `0xDA0D0` | 50 | UnwindData |  |
| 1794 | `_spawnl` | `0xDA110` | 43 | UnwindData |  |
| 1795 | `_spawnle` | `0xDA150` | 43 | UnwindData |  |
| 1953 | `_wexecl` | `0xDA190` | 50 | UnwindData |  |
| 1954 | `_wexecle` | `0xDA1D0` | 50 | UnwindData |  |
| 2000 | `_wspawnl` | `0xDA210` | 43 | UnwindData |  |
| 2001 | `_wspawnle` | `0xDA250` | 43 | UnwindData |  |
| 235 | `_execlp` | `0xDA390` | 50 | UnwindData |  |
| 236 | `_execlpe` | `0xDA3D0` | 50 | UnwindData |  |
| 1796 | `_spawnlp` | `0xDA410` | 43 | UnwindData |  |
| 1797 | `_spawnlpe` | `0xDA450` | 43 | UnwindData |  |
| 1955 | `_wexeclp` | `0xDA490` | 50 | UnwindData |  |
| 1956 | `_wexeclpe` | `0xDA4D0` | 50 | UnwindData |  |
| 2002 | `_wspawnlp` | `0xDA510` | 43 | UnwindData |  |
| 2003 | `_wspawnlpe` | `0xDA550` | 43 | UnwindData |  |
| 238 | `_execv` | `0xDA890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `_execve` | `0xDA8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1798 | `_spawnv` | `0xDA8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1799 | `_spawnve` | `0xDA8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1957 | `_wexecv` | `0xDA8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1958 | `_wexecve` | `0xDA910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2004 | `_wspawnv` | `0xDA930` | 1,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `_execvp` | `0xDB0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `_execvpe` | `0xDB110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1800 | `_spawnvp` | `0xDB130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1801 | `_spawnvpe` | `0xDB140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1959 | `_wexecvp` | `0xDB150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1960 | `_wexecvpe` | `0xDB170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2006 | `_wspawnvp` | `0xDB190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2007 | `_wspawnvpe` | `0xDB1A0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2018 | `_wsystem` | `0xDB300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2416 | `system` | `0xDB310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `_heapchk` | `0xDB320` | 37 | UnwindData |  |
| 366 | `_heapmin` | `0xDB350` | 33 | UnwindData |  |
| 418 | `_ismbcalnum` | `0xDB380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `_ismbcalnum_l` | `0xDB390` | 129 | UnwindData |  |
| 394 | `_ismbbalnum` | `0xDB420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `_ismbbalnum_l` | `0xDB440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `_ismbbalpha` | `0xDB460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `_ismbbalpha_l` | `0xDB480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `_ismbbblank` | `0xDB4A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `_ismbbblank_l` | `0xDB4D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `_ismbbgraph` | `0xDB500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `_ismbbgraph_l` | `0xDB520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `_ismbbkalnum` | `0xDB540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `_ismbbkalnum_l` | `0xDB560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `_ismbbkana` | `0xDB580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `_ismbbkana_l` | `0xDB590` | 116 | UnwindData |  |
| 406 | `_ismbbkprint` | `0xDB610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `_ismbbkprint_l` | `0xDB630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `_ismbbkpunct` | `0xDB650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `_ismbbkpunct_l` | `0xDB670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `_ismbblead_l` | `0xDB690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `_ismbbprint` | `0xDB6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `_ismbbprint_l` | `0xDB6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `_ismbbpunct` | `0xDB6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `_ismbbpunct_l` | `0xDB710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `_ismbbtrail` | `0xDB730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `_ismbbtrail_l` | `0xDB750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `_ismbcgraph` | `0xDB770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `_ismbcgraph_l` | `0xDB780` | 137 | UnwindData |  |
| 428 | `_ismbchira` | `0xDB810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `_ismbchira_l` | `0xDB820` | 77 | UnwindData |  |
| 430 | `_ismbckata` | `0xDB880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `_ismbckata_l` | `0xDB890` | 85 | UnwindData |  |
| 448 | `_ismbcsymbol` | `0xDB8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `_ismbcsymbol_l` | `0xDB900` | 85 | UnwindData |  |
| 438 | `_ismbclegal` | `0xDB960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `_ismbclegal_l` | `0xDB970` | 80 | UnwindData |  |
| 442 | `_ismbcprint` | `0xDB9D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `_ismbcprint_l` | `0xDB9E0` | 114 | UnwindData |  |
| 422 | `_ismbcblank` | `0xDBA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `_ismbcblank_l` | `0xDBA70` | 145 | UnwindData |  |
| 444 | `_ismbcpunct` | `0xDBB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `_ismbcpunct_l` | `0xDBB20` | 134 | UnwindData |  |
| 452 | `_ismbslead` | `0xDBBB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `_ismbslead_l` | `0xDBBC0` | 165 | UnwindData |  |
| 450 | `_ismbcupper` | `0xDBC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `_ismbcupper_l` | `0xDBC80` | 93 | UnwindData |  |
| 525 | `_mbbtype` | `0xDBCF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | `_mbbtype_l` | `0xDBD00` | 231 | UnwindData |  |
| 529 | `_mbccpy_l` | `0xDBDF0` | 29 | UnwindData |  |
| 537 | `_mbclen_l` | `0xDBE20` | 58 | UnwindData |  |
| 432 | `_ismbcl0` | `0xDBE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `_ismbcl0_l` | `0xDBE70` | 97 | UnwindData |  |
| 434 | `_ismbcl1` | `0xDBEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `_ismbcl1_l` | `0xDBEF0` | 102 | UnwindData |  |
| 436 | `_ismbcl2` | `0xDBF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `_ismbcl2_l` | `0xDBF70` | 102 | UnwindData |  |
| 550 | `_mbsbtype_l` | `0xDBFE0` | 234 | UnwindData |  |
| 551 | `_mbscat_s` | `0xDC0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `_mbscoll` | `0xDC0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `_mbscoll_l` | `0xDC0F0` | 227 | UnwindData |  |
| 559 | `_mbscpy_s` | `0xDC1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `_mbscpy_s_l` | `0xDC1F0` | 461 | UnwindData |  |
| 568 | `_mbsicoll` | `0xDC3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `_mbsicoll_l` | `0xDC3E0` | 227 | UnwindData |  |
| 571 | `_mbsinc_l` | `0xDC4D0` | 54 | UnwindData |  |
| 622 | `_mbsnlen` | `0xDC510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 623 | `_mbsnlen_l` | `0xDC520` | 477 | UnwindData |  |
| 575 | `_mbslwr_l` | `0xDC710` | 43 | UnwindData |  |
| 578 | `_mbsnbcat` | `0xDC750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `_mbsnbcat_l` | `0xDC760` | 362 | UnwindData |  |
| 584 | `_mbsnbcnt` | `0xDC8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 585 | `_mbsnbcnt_l` | `0xDC8E0` | 165 | UnwindData |  |
| 586 | `_mbsnbcoll` | `0xDC990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 587 | `_mbsnbcoll_l` | `0xDC9A0` | 265 | UnwindData |  |
| 594 | `_mbsnbicoll` | `0xDCAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 595 | `_mbsnbicoll_l` | `0xDCAC0` | 280 | UnwindData |  |
| 596 | `_mbsnbset` | `0xDCBE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `_mbsnbset_l` | `0xDCBF0` | 283 | UnwindData |  |
| 598 | `_mbsnbset_s` | `0xDCD20` | 20 | UnwindData |  |
| 599 | `_mbsnbset_s_l` | `0xDCD40` | 768 | UnwindData |  |
| 600 | `_mbsncat` | `0xDD050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `_mbsncat_l` | `0xDD060` | 340 | UnwindData |  |
| 602 | `_mbsncat_s` | `0xDD1C0` | 20 | UnwindData |  |
| 604 | `_mbsnccnt` | `0xDD1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `_mbsnccnt_l` | `0xDD1F0` | 171 | UnwindData |  |
| 606 | `_mbsncmp` | `0xDD2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `_mbsncoll` | `0xDD2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `_mbsncoll_l` | `0xDD2D0` | 332 | UnwindData |  |
| 610 | `_mbsncpy` | `0xDD430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `_mbsncpy_l` | `0xDD440` | 266 | UnwindData |  |
| 612 | `_mbsncpy_s` | `0xDD550` | 20 | UnwindData |  |
| 613 | `_mbsncpy_s_l` | `0xDD570` | 613 | UnwindData |  |
| 616 | `_mbsnicmp` | `0xDD7E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 618 | `_mbsnicoll` | `0xDD7F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `_mbsnicoll_l` | `0xDD800` | 332 | UnwindData |  |
| 620 | `_mbsninc` | `0xDD960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 621 | `_mbsninc_l` | `0xDD970` | 34 | UnwindData |  |
| 624 | `_mbsnset` | `0xDD9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `_mbsnset_l` | `0xDD9B0` | 386 | UnwindData |  |
| 626 | `_mbsnset_s` | `0xDDB40` | 20 | UnwindData |  |
| 627 | `_mbsnset_s_l` | `0xDDB60` | 748 | UnwindData |  |
| 634 | `_mbsset` | `0xDDE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 635 | `_mbsset_l` | `0xDDE70` | 259 | UnwindData |  |
| 636 | `_mbsset_s` | `0xDDF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 637 | `_mbsset_s_l` | `0xDDF90` | 470 | UnwindData |  |
| 644 | `_mbstok` | `0xDE170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `_mbstok_l` | `0xDE180` | 62 | UnwindData |  |
| 654 | `_mbsupr` | `0xDE1D0` | 43 | UnwindData |  |
| 655 | `_mbsupr_l` | `0xDE210` | 43 | UnwindData |  |
| 538 | `_mbctohira` | `0xDE250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `_mbctohira_l` | `0xDE260` | 55 | UnwindData |  |
| 540 | `_mbctokata` | `0xDE2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `_mbctokata_l` | `0xDE2B0` | 41 | UnwindData |  |
| 546 | `_mbctoupper` | `0xDE2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `_mbctoupper_l` | `0xDE2F0` | 232 | UnwindData |  |
| 532 | `_mbcjistojms` | `0xDE3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 533 | `_mbcjistojms_l` | `0xDE3F0` | 213 | UnwindData |  |
| 534 | `_mbcjmstojis` | `0xDE4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `_mbcjmstojis_l` | `0xDE4E0` | 237 | UnwindData |  |
| 523 | `_mbbtombc` | `0xDE5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `_mbbtombc_l` | `0xDE5F0` | 185 | UnwindData |  |
| 544 | `_mbctombb` | `0xDE6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `_mbctombb_l` | `0xDE6C0` | 221 | UnwindData |  |
| 180 | `_chdir` | `0xDEA40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `_getdrives` | `0xDEA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `_getdcwd` | `0xDEA60` | 14 | UnwindData |  |
| 1757 | `_resetstkoflw` | `0xDEA80` | 397 | UnwindData |  |
| 1785 | `_seterrormode` | `0xDEC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `_beep` | `0xDEC30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `_getsystime` | `0xDEC40` | 168 | UnwindData |  |
| 1789 | `_setsystime` | `0xDECF0` | 179 | UnwindData |  |
| 172 | `_cabs` | `0xDEDB0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2128 | `coshf` | `0xDEF00` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `_logbf` | `0xDF2D0` | 194 | UnwindData |  |
| 182 | `_chgsign` | `0xDF3A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `_chgsignf` | `0xDF3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `_copysignf` | `0xDF3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `_finitef` | `0xDF410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1830 | `_strnset` | `0xDF430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1832 | `_strrev` | `0xDF450` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1833 | `_strset` | `0xDF490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `_fpieee_flt` | `0xDF4B0` | 11,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `_fpclassf` | `0xE2250` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `_isnanf` | `0xE22C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1764 | `_scalb` | `0xE22E0` | 434 | UnwindData |  |
| 1765 | `_scalbf` | `0xE24A0` | 386 | UnwindData |  |
| 211 | `_dexp` | `0xE74F0` | 1,122 | UnwindData |  |
| 250 | `_fdexp` | `0xE7960` | 982 | UnwindData |  |
| 385 | `_isatty` | `0xECC30` | 18 | UnwindData |  |
| 75 | `__intrinsic_setjmp` | `0xECC60` | 144 | UnwindData |  |
| 2371 | `setjmp` | `0xECD00` | 5 | UnwindData |  |
| 76 | `__intrinsic_setjmpex` | `0xECD20` | 144 | UnwindData |  |
| 2382 | `strcat` | `0xECF30` | 144 | UnwindData |  |
| 2387 | `strcpy` | `0xECFD0` | 183 | UnwindData |  |
| 2385 | `strcmp` | `0xED0A0` | 103 | UnwindData |  |
| 2393 | `strlen` | `0xED120` | 168 | UnwindData |  |
| 2394 | `strncat` | `0xED1E0` | 405 | UnwindData |  |
| 2396 | `strncmp` | `0xED390` | 125 | UnwindData |  |
| 2397 | `strncpy` | `0xED420` | 354 | UnwindData |  |
| 1612 | `_o_memset` | `0xED5C0` | 904 | UnwindData |  |
| 2314 | `memset` | `0xED5C0` | 904 | UnwindData |  |
| 2308 | `memchr` | `0xED960` | 144 | UnwindData |  |
| 2309 | `memcmp` | `0xEDA00` | 199 | UnwindData |  |
| 2310 | `memcpy` | `0xEDB00` | 1,645 | UnwindData |  |
| 2312 | `memmove` | `0xEDB00` | 1,645 | UnwindData |  |
| 2102 | `ceil` | `0xF7020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2103 | `ceilf` | `0xF7030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2191 | `floor` | `0xF7040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2192 | `floorf` | `0xF7050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2320 | `nearbyint` | `0xF7060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2321 | `nearbyintf` | `0xF7070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2322 | `nearbyintl` | `0xF7080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2356 | `rint` | `0xF7090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2357 | `rintf` | `0xF70A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2358 | `rintl` | `0xF70B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2434 | `trunc` | `0xF70C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2435 | `truncf` | `0xF70D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2436 | `truncl` | `0xF70E0` | 38,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1951 | `_wctype` | `0x100620` | 229,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `_mbcasemap` | `0x1387E0` | 2,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `__dcrt_initial_narrow_environment` | `0x1392A0` | 0 | Indeterminate |  |
