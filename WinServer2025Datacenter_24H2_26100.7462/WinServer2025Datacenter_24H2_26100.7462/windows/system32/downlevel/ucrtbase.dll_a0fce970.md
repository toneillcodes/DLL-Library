# Binary Specification: ucrtbase.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\downlevel\ucrtbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a0fce9704e8a4ecbd663b694bcc36e4224e41d19a9c69cb14f9cc265b3a98fa1`
* **Total Exported Functions:** 2484

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1759 | `_rmtmp` | `0x1080` | 167 | UnwindData |  |
| 244 | `_fclose_nolock` | `0x1130` | 85 | UnwindData |  |
| 1736 | `_pipe` | `0x1340` | 752 | UnwindData |  |
| 1735 | `_pclose` | `0x1640` | 220 | UnwindData |  |
| 208 | `_cwait` | `0x1730` | 178 | UnwindData |  |
| 2373 | `setvbuf` | `0x1C10` | 90 | UnwindData |  |
| 188 | `_close` | `0x1ED0` | 85 | UnwindData |  |
| 2170 | `fclose` | `0x1F30` | 85 | UnwindData |  |
| 245 | `_fcloseall` | `0x22F0` | 201 | UnwindData |  |
| 631 | `_mbsrchr_l` | `0x2AC0` | 273 | UnwindData |  |
| 2401 | `strrchr` | `0x2BE0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1989 | `_wputenv_s` | `0x2C90` | 56 | UnwindData |  |
| 2428 | `tmpnam_s` | `0x2CD0` | 59 | UnwindData |  |
| 142 | `_access` | `0x3400` | 18 | UnwindData |  |
| 143 | `_access_s` | `0x3420` | 149 | UnwindData |  |
| 1892 | `_waccess` | `0x34C0` | 18 | UnwindData |  |
| 1893 | `_waccess_s` | `0x34E0` | 189 | UnwindData |  |
| 1952 | `_wdupenv_s` | `0x4040` | 14 | UnwindData |  |
| 225 | `_dupenv_s` | `0x40B0` | 14 | UnwindData |  |
| 2462 | `wcsspn` | `0x4E80` | 88 | UnwindData |  |
| 2444 | `wcschr` | `0x5010` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1869 | `_tzset` | `0x5180` | 42 | UnwindData |  |
| 51 | `___lc_codepage_func` | `0x56E0` | 90 | UnwindData |  |
| 1918 | `_wcsnicoll` | `0x5860` | 79 | UnwindData |  |
| 2077 | `calloc` | `0x58C0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1829 | `_strnicoll_l` | `0x5C50` | 309 | UnwindData |  |
| 1827 | `_strnicmp_l` | `0x5D90` | 177 | UnwindData |  |
| 68 | `__dcrt_get_wide_environment_from_os` | `0x5F90` | 131 | UnwindData |  |
| 554 | `_mbschr_l` | `0x7120` | 232 | UnwindData |  |
| 2384 | `strchr` | `0x7210` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1828 | `_strnicoll` | `0x7330` | 2,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2299 | `mbrlen` | `0x7EC0` | 125 | UnwindData |  |
| 1793 | `_sopen_s` | `0x86C0` | 50 | UnwindData |  |
| 27 | `_Wcsftime` | `0x91E0` | 30 | UnwindData |  |
| 1712 | `_o_wcsftime` | `0x9210` | 28 | UnwindData |  |
| 2392 | `strftime` | `0x92A0` | 26 | UnwindData |  |
| 23 | `_Strftime` | `0x92C0` | 30 | UnwindData |  |
| 2450 | `wcsftime` | `0x92F0` | 26 | UnwindData |  |
| 2302 | `mbrtowc` | `0x94E0` | 163 | UnwindData |  |
| 2472 | `wcstombs` | `0xC0A0` | 87 | UnwindData |  |
| 2305 | `mbstowcs` | `0xC240` | 87 | UnwindData |  |
| 2306 | `mbstowcs_s` | `0xC3F0` | 332 | UnwindData |  |
| 2473 | `wcstombs_s` | `0xC950` | 326 | UnwindData |  |
| 1934 | `_wcstombs_s_l` | `0xCAA0` | 345 | UnwindData |  |
| 2372 | `setlocale` | `0xCFE0` | 76 | UnwindData |  |
| 174 | `_calloc_base` | `0xF370` | 43 | UnwindData |  |
| 522 | `_malloc_base` | `0xF420` | 10 | UnwindData |  |
| 1750 | `_query_new_handler` | `0xF4B0` | 76 | UnwindData |  |
| 1779 | `_set_new_handler` | `0xF530` | 123 | UnwindData |  |
| 173 | `_callnewh` | `0xF5C0` | 51 | UnwindData |  |
| 26 | `_W_Gettnames` | `0xFDA0` | 3,375 | UnwindData |  |
| 262 | `_fgetc_nolock` | `0x10BC0` | 69 | UnwindData |  |
| 338 | `_getc_nolock` | `0x10BC0` | 69 | UnwindData |  |
| 268 | `_fileno` | `0x10C10` | 41 | UnwindData |  |
| 669 | `_msize` | `0x10CD0` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `_errno` | `0x112A0` | 229 | UnwindData |  |
| 379 | `_invalid_parameter_noinfo` | `0x11390` | 14 | UnwindData |  |
| 2186 | `fgetc` | `0x113B0` | 441 | UnwindData |  |
| 1826 | `_strnicmp` | `0x11570` | 165 | UnwindData |  |
| 1816 | `_stricmp` | `0x11620` | 125 | UnwindData |  |
| 1916 | `_wcsnicmp` | `0x116B0` | 149 | UnwindData |  |
| 333 | `_get_timezone` | `0x11750` | 21 | UnwindData |  |
| 2388 | `strcpy_s` | `0x11810` | 120 | UnwindData |  |
| 2443 | `wcscat_s` | `0x11890` | 139 | UnwindData |  |
| 1906 | `_wcsicmp` | `0x12780` | 138 | UnwindData |  |
| 2245 | `isspace` | `0x12810` | 52 | UnwindData |  |
| 2474 | `wcstoul` | `0x129D0` | 112 | UnwindData |  |
| 124 | `__stdio_common_vswprintf_s` | `0x12A50` | 120 | UnwindData |  |
| 120 | `__stdio_common_vsprintf_s` | `0x12E80` | 118 | UnwindData |  |
| 118 | `__stdio_common_vsprintf` | `0x131B0` | 117 | UnwindData |  |
| 2344 | `rand` | `0x139A0` | 41 | UnwindData |  |
| 2239 | `isdigit` | `0x139D0` | 52 | UnwindData |  |
| 731 | `_o___stdio_common_vswprintf_s` | `0x13BE0` | 55 | UnwindData |  |
| 1474 | `_o_bsearch` | `0x13C20` | 38 | UnwindData |  |
| 2063 | `bsearch` | `0x13CD0` | 40 | UnwindData |  |
| 516 | `_ltoa` | `0x13ED0` | 205 | UnwindData |  |
| 729 | `_o___stdio_common_vswprintf` | `0x14070` | 55 | UnwindData |  |
| 2252 | `iswctype` | `0x142F0` | 109 | UnwindData |  |
| 2212 | `free` | `0x144F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2297 | `malloc` | `0x14510` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1755 | `_register_onexit_function` | `0x149B0` | 89 | UnwindData |  |
| 144 | `_aligned_free` | `0x15880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `_aligned_malloc` | `0x158A0` | 23 | UnwindData |  |
| 146 | `_aligned_msize` | `0x15940` | 101 | UnwindData |  |
| 150 | `_aligned_realloc` | `0x159B0` | 144 | UnwindData |  |
| 151 | `_aligned_recalloc` | `0x15BC0` | 622 | UnwindData |  |
| 147 | `_aligned_offset_malloc` | `0x15E40` | 204 | UnwindData |  |
| 1731 | `_o_wmemcpy_s` | `0x15FA0` | 35 | UnwindData |  |
| 1008 | `_o__itow_s` | `0x16050` | 27 | UnwindData |  |
| 481 | `_itow_s` | `0x160F0` | 64 | UnwindData |  |
| 725 | `_o___stdio_common_vsprintf` | `0x162D0` | 55 | UnwindData |  |
| 727 | `_o___stdio_common_vsprintf_s` | `0x16310` | 55 | UnwindData |  |
| 1714 | `_o_wcsncpy_s` | `0x16350` | 35 | UnwindData |  |
| 1679 | `_o_strncpy_s` | `0x16380` | 35 | UnwindData |  |
| 1754 | `_recalloc` | `0x16460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1753 | `_realloc_base` | `0x16470` | 130 | UnwindData |  |
| 1751 | `_query_new_mode` | `0x16500` | 25 | UnwindData |  |
| 1780 | `_set_new_mode` | `0x16520` | 57 | UnwindData |  |
| 203 | `_crt_atexit` | `0x16560` | 76 | UnwindData |  |
| 237 | `_execute_onexit_table` | `0x165F0` | 67 | UnwindData |  |
| 1475 | `_o_bsearch_s` | `0x16740` | 48 | UnwindData |  |
| 2064 | `bsearch_s` | `0x16800` | 40 | UnwindData |  |
| 2341 | `qsort_s` | `0x17140` | 189 | UnwindData |  |
| 1634 | `_o_qsort` | `0x176D0` | 28 | UnwindData |  |
| 2340 | `qsort` | `0x17770` | 164 | UnwindData |  |
| 1635 | `_o_qsort_s` | `0x17D50` | 38 | UnwindData |  |
| 1901 | `_wcscoll_l` | `0x18250` | 219 | UnwindData |  |
| 1919 | `_wcsnicoll_l` | `0x18440` | 234 | UnwindData |  |
| 224 | `_dup2` | `0x18830` | 85 | UnwindData |  |
| 2205 | `fopen_s` | `0x18FF0` | 90 | UnwindData |  |
| 1971 | `_wfopen_s` | `0x19050` | 90 | UnwindData |  |
| 1734 | `_open_osfhandle` | `0x191A0` | 275 | UnwindData |  |
| 1985 | `_wopen` | `0x193C0` | 35 | UnwindData |  |
| 1999 | `_wsopen_s` | `0x19710` | 50 | UnwindData |  |
| 2218 | `ftell` | `0x1A920` | 85 | UnwindData |  |
| 2210 | `fread` | `0x1A980` | 32 | UnwindData |  |
| 2211 | `fread_s` | `0x1A9B0` | 172 | UnwindData |  |
| 290 | `_fread_nolock_s` | `0x1AA70` | 53 | UnwindData |  |
| 1752 | `_read` | `0x1AF20` | 335 | UnwindData |  |
| 70 | `__doserrno` | `0x1B530` | 35 | UnwindData |  |
| 112 | `__stdio_common_vfwprintf` | `0x1B8C0` | 109 | UnwindData |  |
| 2216 | `fseek` | `0x1BB90` | 88 | UnwindData |  |
| 2207 | `fputs` | `0x1BBF0` | 85 | UnwindData |  |
| 294 | `_fseeki64` | `0x1BCB0` | 85 | UnwindData |  |
| 2187 | `fgetpos` | `0x1C150` | 75 | UnwindData |  |
| 515 | `_lseeki64` | `0x1C5A0` | 87 | UnwindData |  |
| 114 | `__stdio_common_vfwprintf_s` | `0x1C660` | 245 | UnwindData |  |
| 302 | `_ftelli64` | `0x1C7D0` | 87 | UnwindData |  |
| 2185 | `fflush` | `0x1C8C0` | 88 | UnwindData |  |
| 261 | `_fflush_nolock` | `0x1CA40` | 231 | UnwindData |  |
| 326 | `_get_osfhandle` | `0x1D4C0` | 138 | UnwindData |  |
| 2337 | `puts` | `0x1D6B0` | 376 | UnwindData |  |
| 2219 | `fwrite` | `0x1D990` | 219 | UnwindData |  |
| 410 | `_ismbblead` | `0x1EEB0` | 64 | UnwindData |  |
| 381 | `_invoke_watson` | `0x234E0` | 66 | UnwindData |  |
| 122 | `__stdio_common_vswprintf` | `0x23530` | 121 | UnwindData |  |
| 291 | `_free_base` | `0x24A00` | 70 | UnwindData |  |
| 2177 | `fegetround` | `0x2C4E0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `__fpe_flt_rounds` | `0x2C710` | 62 | UnwindData |  |
| 2183 | `fesetround` | `0x2C7B0` | 140 | UnwindData |  |
| 2181 | `fesetenv` | `0x2D7D0` | 112 | UnwindData |  |
| 2175 | `fegetenv` | `0x2D850` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2174 | `feclearexcept` | `0x2D9A0` | 83 | UnwindData |  |
| 256 | `_fdscale` | `0x2DA80` | 296 | UnwindData |  |
| 2094 | `cbrtf` | `0x2DBB0` | 143 | UnwindData |  |
| 251 | `_fdlog` | `0x2DF20` | 532 | UnwindData |  |
| 252 | `_fdnorm` | `0x2E140` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2270 | `llrint` | `0x2E190` | 108 | UnwindData |  |
| 2291 | `lrint` | `0x2E210` | 107 | UnwindData |  |
| 2292 | `lrintf` | `0x2E300` | 85 | UnwindData |  |
| 2295 | `lroundf` | `0x2E360` | 85 | UnwindData |  |
| 2184 | `fetestexcept` | `0x2E3C0` | 30 | UnwindData |  |
| 2176 | `fegetexceptflag` | `0x2E3F0` | 55 | UnwindData |  |
| 2182 | `fesetexceptflag` | `0x2E4E0` | 348 | UnwindData |  |
| 2271 | `llrintf` | `0x2E6A0` | 86 | UnwindData |  |
| 214 | `_dlog` | `0x2E700` | 619 | UnwindData |  |
| 2273 | `llround` | `0x2E980` | 108 | UnwindData |  |
| 2275 | `llroundl` | `0x2E980` | 108 | UnwindData |  |
| 2327 | `nexttowardf` | `0x2EA00` | 300 | UnwindData |  |
| 2294 | `lround` | `0x2EB40` | 107 | UnwindData |  |
| 2296 | `lroundl` | `0x2EB40` | 107 | UnwindData |  |
| 2282 | `log1pl` | `0x2EBC0` | 248 | UnwindData |  |
| 2353 | `remquol` | `0x2ECC0` | 1,259 | UnwindData |  |
| 222 | `_dunscale` | `0x2F1C0` | 218 | UnwindData |  |
| 2095 | `cbrtl` | `0x2F2A0` | 1,014 | UnwindData |  |
| 2093 | `cbrt` | `0x2F6A0` | 1,014 | UnwindData |  |
| 218 | `_dscale` | `0x2FAA0` | 321 | UnwindData |  |
| 215 | `_dnorm` | `0x2FBF0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2230 | `ilogbf` | `0x2FC70` | 133 | UnwindData |  |
| 260 | `_fdunscale` | `0x2FD00` | 170 | UnwindData |  |
| 2364 | `scalblnl` | `0x2FDB0` | 444 | UnwindData |  |
| 2365 | `scalbn` | `0x2FDB0` | 444 | UnwindData |  |
| 2367 | `scalbnl` | `0x2FDB0` | 444 | UnwindData |  |
| 2351 | `remquo` | `0x2FF80` | 1,229 | UnwindData |  |
| 2051 | `asinhl` | `0x30460` | 229 | UnwindData |  |
| 492 | `_ldscale` | `0x30550` | 337 | UnwindData |  |
| 2058 | `atanhl` | `0x306B0` | 226 | UnwindData |  |
| 496 | `_ldunscale` | `0x307A0` | 216 | UnwindData |  |
| 2144 | `csqrt` | `0x30880` | 328 | UnwindData |  |
| 2083 | `casinh` | `0x30FF0` | 833 | UnwindData |  |
| 2113 | `clog` | `0x31340` | 608 | UnwindData |  |
| 2118 | `clogl` | `0x315B0` | 902 | UnwindData |  |
| 2048 | `asinf` | `0x31DE0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2047 | `asin` | `0x32020` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2053 | `atan2` | `0x32260` | 2,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2420 | `tanhf` | `0x32DB0` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `_hypotf` | `0x334D0` | 269 | UnwindData |  |
| 368 | `_hypot` | `0x335F0` | 135 | UnwindData |  |
| 2040 | `acos` | `0x33840` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `_logb` | `0x33BC0` | 248 | UnwindData |  |
| 2049 | `asinh` | `0x33CF0` | 227 | UnwindData |  |
| 2379 | `sqrt` | `0x33DE0` | 195 | UnwindData |  |
| 2056 | `atanh` | `0x33EB0` | 212 | UnwindData |  |
| 2280 | `log1p` | `0x33F90` | 237 | UnwindData |  |
| 2283 | `log2` | `0x341F0` | 823 | UnwindData |  |
| 2380 | `sqrtf` | `0x347D0` | 151 | UnwindData |  |
| 232 | `_except1` | `0x34870` | 241 | UnwindData |  |
| 2203 | `fmodf` | `0x34B10` | 873 | UnwindData |  |
| 2145 | `csqrtf` | `0x35920` | 408 | UnwindData |  |
| 2263 | `ldexp` | `0x35FF0` | 69 | UnwindData |  |
| 2084 | `casinhf` | `0x36180` | 786 | UnwindData |  |
| 2054 | `atan2f` | `0x364A0` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2050 | `asinhf` | `0x36CA0` | 205 | UnwindData |  |
| 2057 | `atanhf` | `0x36D80` | 181 | UnwindData |  |
| 2281 | `log1pf` | `0x36E40` | 199 | UnwindData |  |
| 2090 | `catanhf` | `0x36F10` | 807 | UnwindData |  |
| 2146 | `csqrtl` | `0x37240` | 484 | UnwindData |  |
| 2043 | `acoshf` | `0x37A40` | 195 | UnwindData |  |
| 2082 | `casinf` | `0x37B10` | 78 | UnwindData |  |
| 2074 | `cacoshf` | `0x37B70` | 805 | UnwindData |  |
| 2075 | `cacoshl` | `0x37EA0` | 894 | UnwindData |  |
| 2085 | `casinhl` | `0x38230` | 843 | UnwindData |  |
| 2072 | `cacosf` | `0x38590` | 714 | UnwindData |  |
| 1940 | `_wcsupr` | `0x395E0` | 100 | UnwindData |  |
| 1943 | `_wcsupr_s_l` | `0x39650` | 75 | UnwindData |  |
| 2433 | `towupper` | `0x39AB0` | 828 | UnwindData |  |
| 1868 | `_towupper_l` | `0x39E00` | 905 | UnwindData |  |
| 1917 | `_wcsnicmp_l` | `0x3A8B0` | 68 | UnwindData |  |
| 1867 | `_towlower_l` | `0x3AA50` | 1,726 | UnwindData |  |
| 2432 | `towlower` | `0x3B120` | 1,606 | UnwindData |  |
| 724 | `_o___stdio_common_vsnwprintf_s` | `0x3BBC0` | 61 | UnwindData |  |
| 117 | `__stdio_common_vsnwprintf_s` | `0x3BCA0` | 127 | UnwindData |  |
| 2429 | `tolower` | `0x3D1D0` | 1,007 | UnwindData |  |
| 2008 | `_wsplitpath` | `0x3E150` | 105 | UnwindData |  |
| 1423 | `_o__wsplitpath_s` | `0x3E4E0` | 90 | UnwindData |  |
| 2009 | `_wsplitpath_s` | `0x3E5F0` | 96 | UnwindData |  |
| 201 | `_create_locale` | `0x3E9E0` | 119 | UnwindData |  |
| 1900 | `_wcreate_locale` | `0x3EAC0` | 329 | UnwindData |  |
| 292 | `_free_locale` | `0x3ED20` | 174 | UnwindData |  |
| 2454 | `wcsncmp` | `0x40C40` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2449 | `wcscspn` | `0x411A0` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1909 | `_wcsicoll_l` | `0x41A20` | 200 | UnwindData |  |
| 1907 | `_wcsicmp_l` | `0x42180` | 55 | UnwindData |  |
| 347 | `_getdrive` | `0x42A40` | 204 | UnwindData |  |
| 2459 | `wcsrchr` | `0x431F0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `_endthreadex` | `0x43420` | 10 | UnwindData |  |
| 503 | `_localtime64` | `0x43480` | 72 | UnwindData |  |
| 1775 | `_set_errno` | `0x43540` | 44 | UnwindData |  |
| 2374 | `signal` | `0x456C0` | 540 | UnwindData |  |
| 506 | `_lock_locales` | `0x468C0` | 591 | UnwindData |  |
| 459 | `_ispunct_l` | `0x46C30` | 24 | UnwindData |  |
| 461 | `_isupper_l` | `0x46D20` | 24 | UnwindData |  |
| 2240 | `isgraph` | `0x48260` | 161 | UnwindData |  |
| 2237 | `isblank` | `0x48310` | 21 | UnwindData |  |
| 2243 | `isprint` | `0x48450` | 161 | UnwindData |  |
| 2242 | `islower` | `0x48580` | 156 | UnwindData |  |
| 2238 | `iscntrl` | `0x48630` | 156 | UnwindData |  |
| 52 | `___lc_collate_cp_func` | `0x486E0` | 47 | UnwindData |  |
| 2412 | `strtoul` | `0x487E0` | 114 | UnwindData |  |
| 2060 | `atoi` | `0x488A0` | 112 | UnwindData |  |
| 2061 | `atol` | `0x488A0` | 112 | UnwindData |  |
| 2409 | `strtol` | `0x498F0` | 112 | UnwindData |  |
| 95 | `__pctype_func` | `0x4A4B0` | 90 | UnwindData |  |
| 1845 | `_strtoui64` | `0x4A660` | 116 | UnwindData |  |
| 2413 | `strtoull` | `0x4A660` | 116 | UnwindData |  |
| 2414 | `strtoumax` | `0x4A660` | 116 | UnwindData |  |
| 264 | `_fgetwc_nolock` | `0x4B400` | 619 | UnwindData |  |
| 1839 | `_strtoi64` | `0x4BCC0` | 116 | UnwindData |  |
| 2406 | `strtoimax` | `0x4BCC0` | 116 | UnwindData |  |
| 2411 | `strtoll` | `0x4BCC0` | 116 | UnwindData |  |
| 2189 | `fgetwc` | `0x4C320` | 94 | UnwindData |  |
| 2438 | `ungetc` | `0x4C390` | 104 | UnwindData |  |
| 1880 | `_ungetc_nolock` | `0x4DC30` | 300 | UnwindData |  |
| 123 | `__stdio_common_vswprintf_p` | `0x55A40` | 124 | UnwindData |  |
| 2439 | `ungetwc` | `0x57780` | 110 | UnwindData |  |
| 1883 | `_ungetwc_nolock` | `0x57800` | 254 | UnwindData |  |
| 1927 | `_wcstoi64` | `0x5A2B0` | 116 | UnwindData |  |
| 2466 | `wcstoimax` | `0x5A2B0` | 116 | UnwindData |  |
| 2471 | `wcstoll` | `0x5A2B0` | 116 | UnwindData |  |
| 1935 | `_wcstoui64` | `0x5A330` | 116 | UnwindData |  |
| 2475 | `wcstoull` | `0x5A330` | 116 | UnwindData |  |
| 2476 | `wcstoumax` | `0x5A330` | 116 | UnwindData |  |
| 2025 | `_wtoi64` | `0x5ADF0` | 114 | UnwindData |  |
| 2030 | `_wtoll` | `0x5ADF0` | 114 | UnwindData |  |
| 2244 | `ispunct` | `0x5C980` | 52 | UnwindData |  |
| 2246 | `isupper` | `0x5CA50` | 52 | UnwindData |  |
| 2261 | `isxdigit` | `0x5CB20` | 54 | UnwindData |  |
| 2236 | `isalpha` | `0x5CBF0` | 54 | UnwindData |  |
| 2235 | `isalnum` | `0x5CCC0` | 54 | UnwindData |  |
| 389 | `_isctype_l` | `0x5CD90` | 269 | UnwindData |  |
| 1864 | `_tolower_l` | `0x5CF40` | 1,025 | UnwindData |  |
| 643 | `_mbsstr_l` | `0x5D5F0` | 43 | UnwindData |  |
| 2403 | `strstr` | `0x5D820` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2258 | `iswspace` | `0x5D940` | 107 | UnwindData |  |
| 2333 | `pow` | `0x5E160` | 2,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `_finite` | `0x5EA20` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2399 | `strnlen` | `0x5EE50` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2457 | `wcsnlen` | `0x5EFB0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `_fdclass` | `0x5F1C0` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1773 | `_set_controlfp` | `0x5F4B0` | 54 | UnwindData |  |
| 195 | `_controlfp_s` | `0x5F4F0` | 105 | UnwindData |  |
| 2430 | `toupper` | `0x60180` | 114 | UnwindData |  |
| 1874 | `_ultoa` | `0x60A00` | 35 | UnwindData |  |
| 478 | `_itoa` | `0x60A30` | 50 | UnwindData |  |
| 1525 | `_o_free` | `0x60B40` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | `_o___stdio_common_vsnprintf_s` | `0x60F20` | 60 | UnwindData |  |
| 116 | `__stdio_common_vsnprintf_s` | `0x61000` | 136 | UnwindData |  |
| 25 | `_W_Getmonths` | `0x61450` | 872 | UnwindData |  |
| 1876 | `_ultow` | `0x61830` | 35 | UnwindData |  |
| 480 | `_itow` | `0x618C0` | 48 | UnwindData |  |
| 518 | `_ltow` | `0x618C0` | 48 | UnwindData |  |
| 1042 | `_o__ltow_s` | `0x61A10` | 27 | UnwindData |  |
| 519 | `_ltow_s` | `0x61AA0` | 34 | UnwindData |  |
| 1344 | `_o__wcsnicmp` | `0x61C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1600 | `_o_malloc` | `0x61C50` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2448 | `wcscpy_s` | `0x61EF0` | 129 | UnwindData |  |
| 110 | `__stdio_common_vfprintf_s` | `0x62570` | 109 | UnwindData |  |
| 108 | `__stdio_common_vfprintf` | `0x62AF0` | 109 | UnwindData |  |
| 24 | `_W_Getdays` | `0x64D90` | 521 | UnwindData |  |
| 2445 | `wcscmp` | `0x65180` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2260 | `iswxdigit` | `0x651C0` | 109 | UnwindData |  |
| 1307 | `_o__ultow_s` | `0x658D0` | 27 | UnwindData |  |
| 1877 | `_ultow_s` | `0x65970` | 63 | UnwindData |  |
| 2248 | `iswalpha` | `0x65AC0` | 109 | UnwindData |  |
| 210 | `_dclass` | `0x65B90` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 487 | `_ldclass` | `0x65B90` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `_dtest` | `0x65C00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `_ldtest` | `0x65C00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `_o__msize` | `0x65C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2206 | `fputc` | `0x65C70` | 86 | UnwindData |  |
| 243 | `_expand` | `0x65F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1910 | `_wcslwr` | `0x65FA0` | 115 | UnwindData |  |
| 1913 | `_wcslwr_s_l` | `0x66020` | 75 | UnwindData |  |
| 1242 | `_o__splitpath_s` | `0x66D80` | 90 | UnwindData |  |
| 1802 | `_splitpath` | `0x66E90` | 105 | UnwindData |  |
| 1803 | `_splitpath_s` | `0x671B0` | 96 | UnwindData |  |
| 590 | `_mbsnbcpy_s` | `0x674F0` | 20 | UnwindData |  |
| 591 | `_mbsnbcpy_s_l` | `0x67510` | 458 | UnwindData |  |
| 629 | `_mbspbrk_l` | `0x677F0` | 170 | UnwindData |  |
| 2400 | `strpbrk` | `0x678A0` | 73 | UnwindData |  |
| 1889 | `_unlock_locales` | `0x67F60` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1566 | `_o_iswspace` | `0x68170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2458 | `wcspbrk` | `0x68190` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `_isnan` | `0x68220` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1702 | `_o_towlower` | `0x68260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1703 | `_o_towupper` | `0x68280` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `_o__ui64tow_s` | `0x698F0` | 28 | UnwindData |  |
| 1873 | `_ui64tow_s` | `0x69990` | 52 | UnwindData |  |
| 1334 | `_o__wcsicmp` | `0x69AD0` | 8,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1611 | `_o_memcpy_s` | `0x6BB30` | 28 | UnwindData |  |
| 2463 | `wcsstr` | `0x6BC70` | 561 | UnwindData |  |
| 463 | `_iswalpha_l` | `0x6BEB0` | 109 | UnwindData |  |
| 476 | `_iswxdigit_l` | `0x6C170` | 109 | UnwindData |  |
| 2284 | `log2f` | `0x6CB60` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `___lc_locale_name_func` | `0x6CC40` | 97 | UnwindData |  |
| 2276 | `localeconv` | `0x6CCF0` | 98 | UnwindData |  |
| 2259 | `iswupper` | `0x6CDD0` | 107 | UnwindData |  |
| 372 | `_i64tow` | `0x6CE50` | 51 | UnwindData |  |
| 1872 | `_ui64tow` | `0x6CE90` | 35 | UnwindData |  |
| 1264 | `_o__strnicmp` | `0x6CFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2456 | `wcsncpy_s` | `0x6D010` | 285 | UnwindData |  |
| 486 | `_ld_int` | `0x6D4F0` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `_get_daylight` | `0x6DB70` | 66 | UnwindData |  |
| 77 | `__isascii` | `0x6DBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2039 | `abs` | `0x6DBE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2262 | `labs` | `0x6DBE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `_get_dstbias` | `0x6DBF0` | 66 | UnwindData |  |
| 932 | `_o__i64tow_s` | `0x6DC40` | 28 | UnwindData |  |
| 373 | `_i64tow_s` | `0x6DCD0` | 35 | UnwindData |  |
| 1511 | `_o_floorf` | `0x6DE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `_lock_file` | `0x6DE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2479 | `wctomb` | `0x6DEA0` | 148 | UnwindData |  |
| 54 | `___mb_cur_max_func` | `0x6DF40` | 90 | UnwindData |  |
| 377 | `_initterm` | `0x6DFC0` | 56 | UnwindData |  |
| 259 | `_fdtest` | `0x6E000` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2451 | `wcslen` | `0x6E050` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `_ecvt` | `0x6E160` | 92 | UnwindData |  |
| 247 | `_fcvt_s` | `0x6E260` | 122 | UnwindData |  |
| 246 | `_fcvt` | `0x6E2E0` | 92 | UnwindData |  |
| 562 | `_mbscspn_l` | `0x6EA20` | 275 | UnwindData |  |
| 2389 | `strcspn` | `0x6EB40` | 70 | UnwindData |  |
| 556 | `_mbscmp_l` | `0x6EEF0` | 376 | UnwindData |  |
| 1639 | `_o_realloc` | `0x6F070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `_ecvt_s` | `0x6F090` | 686 | UnwindData |  |
| 2153 | `div` | `0x6F350` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2264 | `ldiv` | `0x6F350` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2112 | `clock` | `0x6F5C0` | 131 | UnwindData |  |
| 1902 | `_wcsdup` | `0x6F650` | 180 | UnwindData |  |
| 1700 | `_o_tolower` | `0x6F710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1335 | `_o__wcsicmp_l` | `0x6F730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1730 | `_o_wctomb_s` | `0x6F750` | 29 | UnwindData |  |
| 2480 | `wctomb_s` | `0x6F7E0` | 91 | UnwindData |  |
| 565 | `_mbsdup` | `0x6F850` | 158 | UnwindData |  |
| 1812 | `_strdup` | `0x6F850` | 158 | UnwindData |  |
| 1701 | `_o_toupper` | `0x6F970` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `_difftime64` | `0x6F9E0` | 46 | UnwindData |  |
| 2315 | `modf` | `0x6FA70` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1996 | `_wsetlocale` | `0x6FB90` | 60 | UnwindData |  |
| 388 | `_isctype` | `0x6FBE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1888 | `_unlock_file` | `0x6FC20` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `_o__ltoa` | `0x6FD10` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2316 | `modff` | `0x6FD80` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `_mbsinc` | `0x6FE60` | 14 | UnwindData |  |
| 2247 | `iswalnum` | `0x6FEE0` | 103 | UnwindData |  |
| 216 | `_dpcomp` | `0x70090` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `__strncnt` | `0x70110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2041 | `acosf` | `0x70130` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `_iswupper_l` | `0x70370` | 107 | UnwindData |  |
| 170 | `_byteswap_ushort` | `0x703F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1720 | `_o_wcstok_s` | `0x70400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1980 | `_wmakepath` | `0x70420` | 39 | UnwindData |  |
| 2162 | `exp2` | `0x705F0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `__acrt_iob_func` | `0x707A0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2024 | `_wtoi` | `0x70900` | 112 | UnwindData |  |
| 2028 | `_wtol` | `0x70900` | 112 | UnwindData |  |
| 1568 | `_o_iswxdigit` | `0x70980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1532 | `_o_fwrite` | `0x709A0` | 35 | UnwindData |  |
| 1866 | `_toupper_l` | `0x70B50` | 363 | UnwindData |  |
| 462 | `_iswalnum_l` | `0x70CD0` | 103 | UnwindData |  |
| 1553 | `_o_isspace` | `0x70D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `_lrotl` | `0x70D60` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1760 | `_rotl` | `0x70D60` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2469 | `wcstol` | `0x70DE0` | 114 | UnwindData |  |
| 1556 | `_o_iswalpha` | `0x70E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `_o__stricmp` | `0x70E80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1477 | `_o_calloc` | `0x70EE0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 567 | `_mbsicmp_l` | `0x70FC0` | 737 | UnwindData |  |
| 1817 | `_stricmp_l` | `0x712B0` | 161 | UnwindData |  |
| 2197 | `fmaxf` | `0x713B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `_byteswap_ulong` | `0x71450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `_o_floor` | `0x71460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2200 | `fminf` | `0x71480` | 1,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `_o__itoa_s` | `0x71BD0` | 27 | UnwindData |  |
| 1040 | `_o__ltoa_s` | `0x71C60` | 27 | UnwindData |  |
| 517 | `_ltoa_s` | `0x71CF0` | 34 | UnwindData |  |
| 479 | `_itoa_s` | `0x71D20` | 32 | UnwindData |  |
| 1305 | `_o__ultoa_s` | `0x71D50` | 27 | UnwindData |  |
| 1875 | `_ultoa_s` | `0x71DE0` | 19 | UnwindData |  |
| 580 | `_mbsnbcat_s` | `0x71EF0` | 20 | UnwindData |  |
| 581 | `_mbsnbcat_s_l` | `0x71F10` | 881 | UnwindData |  |
| 2483 | `wmemcpy_s` | `0x72370` | 78 | UnwindData |  |
| 319 | `_get_errno` | `0x72770` | 47 | UnwindData |  |
| 1523 | `_o_fread` | `0x72840` | 35 | UnwindData |  |
| 574 | `_mbslwr` | `0x72870` | 43 | UnwindData |  |
| 577 | `_mbslwr_s_l` | `0x728B0` | 792 | UnwindData |  |
| 2345 | `rand_s` | `0x72C20` | 71 | UnwindData |  |
| 2052 | `atan` | `0x72CD0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2215 | `frexp` | `0x72F80` | 280 | UnwindData |  |
| 1726 | `_o_wcstoul` | `0x730A0` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | `_o__hypotf` | `0x737A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2253 | `iswdigit` | `0x737C0` | 100 | UnwindData |  |
| 1670 | `_o_sqrtf` | `0x73830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1544 | `_o_isalpha` | `0x73850` | 1,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2169 | `fabs` | `0x73E90` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1547 | `_o_isdigit` | `0x73F10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `_ldpcomp` | `0x73F70` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1870 | `_ui64toa` | `0x73FF0` | 35 | UnwindData |  |
| 370 | `_i64toa` | `0x74020` | 51 | UnwindData |  |
| 1569 | `_o_isxdigit` | `0x74140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `_fpclass` | `0x74160` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1653 | `_o_roundf` | `0x74200` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `_o__register_onexit_function` | `0x742C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `_heapwalk` | `0x742E0` | 226 | UnwindData |  |
| 168 | `_byteswap_uint64` | `0x74420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1499 | `_o_expf` | `0x74430` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `_getcwd` | `0x745D0` | 22 | UnwindData |  |
| 1976 | `_wgetcwd` | `0x74740` | 22 | UnwindData |  |
| 1977 | `_wgetdcwd` | `0x74950` | 14 | UnwindData |  |
| 1975 | `_wfullpath` | `0x74DE0` | 14 | UnwindData |  |
| 308 | `_fullpath` | `0x75140` | 14 | UnwindData |  |
| 469 | `_iswdigit_l` | `0x755E0` | 100 | UnwindData |  |
| 1481 | `_o_ceilf` | `0x75FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `_initterm_e` | `0x75FF0` | 59 | UnwindData |  |
| 2455 | `wcsncpy` | `0x761E0` | 529 | UnwindData |  |
| 1543 | `_o_isalnum` | `0x76A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `__stdio_common_vsprintf_p` | `0x76A80` | 124 | UnwindData |  |
| 1593 | `_o_logf` | `0x777F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1711 | `_o_wcscpy_s` | `0x77810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 939 | `_o__isctype` | `0x77830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `_o_fgetc` | `0x77850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `_lrotr` | `0x77870` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1762 | `_rotr` | `0x77870` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 809 | `_o__errno` | `0x77C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2055 | `atanf` | `0x77C20` | 2,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2163 | `exp2f` | `0x78560` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2404 | `strtod` | `0x786C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2410 | `strtold` | `0x786C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2461 | `wcsrtombs_s` | `0x786D0` | 303 | UnwindData |  |
| 1223 | `_o__set_errno` | `0x78E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2468 | `wcstok_s` | `0x78E30` | 56 | UnwindData |  |
| 2442 | `wcscat` | `0x78E70` | 301 | UnwindData |  |
| 2447 | `wcscpy` | `0x78FB0` | 317 | UnwindData |  |
| 1666 | `_o_sinf` | `0x79100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `_o___stdio_common_vswscanf` | `0x79120` | 48 | UnwindData |  |
| 125 | `__stdio_common_vswscanf` | `0x791E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1552 | `_o_ispunct` | `0x791F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `_initialize_onexit_table` | `0x79210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2419 | `tanh` | `0x79240` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `_o_lrintf` | `0x794D0` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | `_memicmp` | `0x797A0` | 124 | UnwindData |  |
| 1485 | `_o_cosf` | `0x79830` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2440 | `wcrtomb` | `0x798B0` | 58 | UnwindData |  |
| 2441 | `wcrtomb_s` | `0x798F0` | 103 | UnwindData |  |
| 1554 | `_o_isupper` | `0x79B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `_o_log` | `0x79BA0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2346 | `realloc` | `0x79C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1627 | `_o_pow` | `0x79C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1361 | `_o__wcstoui64` | `0x79C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1727 | `_o_wcstoull` | `0x79C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `_gmtime64` | `0x79CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | `_o__i64toa_s` | `0x79CC0` | 28 | UnwindData |  |
| 1301 | `_o__ui64toa_s` | `0x79D50` | 28 | UnwindData |  |
| 371 | `_i64toa_s` | `0x79DE0` | 35 | UnwindData |  |
| 1871 | `_ui64toa_s` | `0x79E10` | 19 | UnwindData |  |
| 2355 | `rewind` | `0x7A1C0` | 78 | UnwindData |  |
| 514 | `_lseek` | `0x7A320` | 85 | UnwindData |  |
| 1354 | `_o__wcstoi64` | `0x7A630` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1723 | `_o_wcstoll` | `0x7A630` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `_o__ecvt_s` | `0x7A6A0` | 55 | UnwindData |  |
| 739 | `_o__aligned_malloc` | `0x7A770` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `_beginthread` | `0x7A7F0` | 177 | UnwindData |  |
| 760 | `_o__beginthreadex` | `0x7A8B0` | 46 | UnwindData |  |
| 167 | `_beginthreadex` | `0x7A960` | 189 | UnwindData |  |
| 1708 | `_o_wcscat_s` | `0x7AA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `_makepath` | `0x7AAB0` | 39 | UnwindData |  |
| 564 | `_mbsdec_l` | `0x7AC70` | 167 | UnwindData |  |
| 1555 | `_o_iswalnum` | `0x7AD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1401 | `_o__wmakepath_s` | `0x7AD40` | 48 | UnwindData |  |
| 1981 | `_wmakepath_s` | `0x7AE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1860 | `_time64` | `0x7AE10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1859 | `_time32` | `0x7AE20` | 120 | UnwindData |  |
| 1669 | `_o_sqrt` | `0x7AEE0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2307 | `mbtowc` | `0x7AF60` | 85 | UnwindData |  |
| 193 | `_control87` | `0x7AFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1665 | `_o_sin` | `0x7AFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `_o___stdio_common_vfwprintf` | `0x7AFF0` | 45 | UnwindData |  |
| 721 | `_o___stdio_common_vfwprintf_s` | `0x7B030` | 45 | UnwindData |  |
| 884 | `_o__get_errno` | `0x7B0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2123 | `copysignf` | `0x7B100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 893 | `_o__get_stream_buffer_pointers` | `0x7B120` | 28 | UnwindData |  |
| 330 | `_get_stream_buffer_pointers` | `0x7B1B0` | 71 | UnwindData |  |
| 682 | `_o____lc_locale_name_func` | `0x7B200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2313 | `memmove_s` | `0x7B220` | 81 | UnwindData |  |
| 738 | `_o__aligned_free` | `0x7B280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1436 | `_o__wtoi` | `0x7B2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1583 | `_o_log10f` | `0x7B2C0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 647 | `_mbstok_s_l` | `0x7B410` | 483 | UnwindData |  |
| 2408 | `strtok_s` | `0x7B660` | 57 | UnwindData |  |
| 1788 | `_setmode` | `0x7B930` | 338 | UnwindData |  |
| 1820 | `_strlwr` | `0x7BB70` | 94 | UnwindData |  |
| 1823 | `_strlwr_s_l` | `0x7BBE0` | 75 | UnwindData |  |
| 306 | `_ftime64` | `0x7C000` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `_ftime64_s` | `0x7C000` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1279 | `_o__strtoui64` | `0x7C2B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1688 | `_o_strtoull` | `0x7C2B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1567 | `_o_iswupper` | `0x7C2D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2208 | `fputwc` | `0x7C2F0` | 87 | UnwindData |  |
| 680 | `_o____lc_codepage_func` | `0x7C3F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 718 | `_o___stdio_common_vfscanf` | `0x7C450` | 45 | UnwindData |  |
| 715 | `_o___stdio_common_vfprintf` | `0x7C490` | 45 | UnwindData |  |
| 2022 | `_wtof` | `0x7C670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `_o__wcslwr` | `0x7C680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1784 | `_set_thread_local_invalid_parameter_handler` | `0x7C6A0` | 37 | UnwindData |  |
| 1684 | `_o_strtol` | `0x7C6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `_o____mb_cur_max_func` | `0x7C6F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1663 | `_o_setlocale` | `0x7C770` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `_gmtime64_s` | `0x7C7E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2196 | `fmax` | `0x7C7F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 934 | `_o__initialize_onexit_table` | `0x7C870` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1561 | `_o_iswdigit` | `0x7C8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2298 | `mblen` | `0x7C8F0` | 85 | UnwindData |  |
| 134 | `__unDName` | `0x7D160` | 39 | UnwindData |  |
| 135 | `__unDNameEx` | `0x7D190` | 183 | UnwindData |  |
| 1674 | `_o_strcpy_s` | `0x7EC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2199 | `fmin` | `0x7EC60` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `_clearfp` | `0x7EE30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `_o__recalloc` | `0x7EEA0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `_o___stdio_common_vsscanf` | `0x7F000` | 48 | UnwindData |  |
| 121 | `__stdio_common_vsscanf` | `0x7F0C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `_fdsign` | `0x7F0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1559 | `_o_iswcntrl` | `0x7F0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2198 | `fmaxl` | `0x7F100` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `_o__calloc_base` | `0x7F180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1480 | `_o_ceil` | `0x7F1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `_o__gcvt_s` | `0x7F1C0` | 28 | UnwindData |  |
| 312 | `_gcvt` | `0x7F2B0` | 44 | UnwindData |  |
| 313 | `_gcvt_s` | `0x7F2F0` | 90 | UnwindData |  |
| 1628 | `_o_powf` | `0x7F520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1582 | `_o_log10` | `0x7F540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1721 | `_o_wcstol` | `0x7F560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1637 | `_o_rand` | `0x7F580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2201 | `fminl` | `0x7F5A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1808 | `_statusfp` | `0x7F620` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 858 | `_o__free_base` | `0x7F690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `_isleadbyte_l` | `0x7F6B0` | 75 | UnwindData |  |
| 850 | `_o__fpclass` | `0x7F710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1778 | `_set_invalid_parameter_handler` | `0x7F730` | 107 | UnwindData |  |
| 1528 | `_o_frexp` | `0x7F930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1850 | `_strupr` | `0x7F950` | 58 | UnwindData |  |
| 1853 | `_strupr_s_l` | `0x7F990` | 75 | UnwindData |  |
| 1546 | `_o_iscntrl` | `0x7FDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1045 | `_o__malloc_base` | `0x7FDE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `_localtime64_s` | `0x7FE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1340 | `_o__wcslwr_s` | `0x7FE10` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1031 | `_o__lock_file` | `0x7FE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1318 | `_o__unlock_file` | `0x7FEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2209 | `fputws` | `0x7FEC0` | 195 | UnwindData |  |
| 741 | `_o__aligned_offset_malloc` | `0x7FFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `_mbsspn_l` | `0x80000` | 117 | UnwindData |  |
| 2402 | `strspn` | `0x80080` | 66 | UnwindData |  |
| 1560 | `_o_iswctype` | `0x80510` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1652 | `_o_round` | `0x807F0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2220 | `getc` | `0x80A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2233 | `imaxdiv` | `0x80A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 657 | `_mbsupr_s_l` | `0x80AA0` | 758 | UnwindData |  |
| 2179 | `feof` | `0x80DA0` | 44 | UnwindData |  |
| 1041 | `_o__ltow` | `0x80DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1680 | `_o_strtod` | `0x80E00` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1685 | `_o_strtold` | `0x80E00` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 668 | `_mktime64` | `0x810A0` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `_atoi64` | `0x81370` | 114 | UnwindData |  |
| 2062 | `atoll` | `0x81370` | 114 | UnwindData |  |
| 1484 | `_o_cos` | `0x813F0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 811 | `_o__execute_onexit_table` | `0x81680` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1472 | `_o_atol` | `0x81710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `_get_fmode` | `0x81720` | 61 | UnwindData |  |
| 2381 | `srand` | `0x82240` | 22 | UnwindData |  |
| 1495 | `_o_exp` | `0x82260` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1536 | `_o_getenv_s` | `0x82420` | 28 | UnwindData |  |
| 2223 | `getenv_s` | `0x824B0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1163 | `_o__mbsstr` | `0x82540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `_o___pctype_func` | `0x82560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `_iswcntrl_l` | `0x82580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2251 | `iswcntrl` | `0x82580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1437 | `_o__wtoi64` | `0x82590` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1442 | `_o__wtoll` | `0x82590` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2127 | `cosh` | `0x82620` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1992 | `_write` | `0x828B0` | 85 | UnwindData |  |
| 823 | `_o__fdclass` | `0x82910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `_ismbcspace_l` | `0x82920` | 84 | UnwindData |  |
| 2335 | `putc` | `0x82980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `_nextafterf` | `0x82990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2324 | `nextafterf` | `0x82990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `_dsign` | `0x829A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `_ldsign` | `0x829A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `_fwrite_nolock` | `0x829B0` | 92 | UnwindData |  |
| 2180 | `ferror` | `0x82A30` | 44 | UnwindData |  |
| 681 | `_o____lc_collate_cp_func` | `0x83750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `_o__realloc_base` | `0x83770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1855 | `_swab` | `0x83790` | 90 | UnwindData |  |
| 1458 | `_o_asin` | `0x837F0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2465 | `wcstof` | `0x83990` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `_o__dclass` | `0x83AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `_o__ldclass` | `0x83AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `_o__wcsdup` | `0x83AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1306 | `_o__ultow` | `0x83AE0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1678 | `_o_strncat_s` | `0x83BB0` | 35 | UnwindData |  |
| 1693 | `_o_tanhf` | `0x83BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | `_o___std_type_info_destroy_list` | `0x83C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2027 | `_wtoi_l` | `0x83C10` | 122 | UnwindData |  |
| 2029 | `_wtol_l` | `0x83C10` | 122 | UnwindData |  |
| 133 | `__tzname` | `0x83C90` | 25 | UnwindData |  |
| 2398 | `strncpy_s` | `0x83CB0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `_dpoly` | `0x83EA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1360 | `_o__wcstombs_s_l` | `0x83ED0` | 48 | UnwindData |  |
| 1367 | `_o__wcsupr_s` | `0x83F10` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `_get_heap_handle` | `0x83F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1297 | `_o__towlower_l` | `0x83F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2059 | `atof` | `0x83FB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `_mbstrlen` | `0x84010` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1580 | `_o_localeconv` | `0x841E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1974 | `_wfsopen` | `0x84250` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1516 | `_o_fmodf` | `0x84340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 555 | `_mbscmp` | `0x84360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `_o___std_exception_destroy` | `0x84370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1908 | `_wcsicoll` | `0x84380` | 70 | UnwindData |  |
| 672 | `_o__Getdays` | `0x843D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `_configthreadlocale` | `0x843F0` | 107 | UnwindData |  |
| 2383 | `strcat_s` | `0x84470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 678 | `_o__W_Gettnames` | `0x84480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1672 | `_o_strcat_s` | `0x844A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 673 | `_o__Getmonths` | `0x84500` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1395 | `_o__wfullpath` | `0x84540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2269 | `lldiv` | `0x84560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 661 | `_memicmp_l` | `0x84580` | 154 | UnwindData |  |
| 1609 | `_o_mbstowcs_s` | `0x84620` | 38 | UnwindData |  |
| 354 | `_getwc_nolock` | `0x846C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `_o___std_type_info_name` | `0x846D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `_o___acrt_iob_func` | `0x846F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `_mkgmtime64` | `0x84700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1465 | `_o_atan2f` | `0x84710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 711 | `_o___std_exception_copy` | `0x84730` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `_commit` | `0x84940` | 140 | UnwindData |  |
| 1087 | `_o__mbsicmp` | `0x84AD0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2446 | `wcscoll` | `0x84B60` | 101 | UnwindData |  |
| 1440 | `_o__wtol` | `0x84BD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1671 | `_o_srand` | `0x84C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2378 | `sinhf` | `0x84C40` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1339 | `_o__wcslwr_l` | `0x84E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `_iswlower_l` | `0x84E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2255 | `iswlower` | `0x84E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1077 | `_o__mbscmp` | `0x84E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2111 | `clearerr_s` | `0x84EA0` | 206 | UnwindData |  |
| 2326 | `nexttoward` | `0x84F80` | 315 | UnwindData |  |
| 1772 | `_set_app_type` | `0x85100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2332 | `perror` | `0x85110` | 78 | UnwindData |  |
| 441 | `_ismbclower_l` | `0x853A0` | 93 | UnwindData |  |
| 642 | `_mbsstr` | `0x85410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1687 | `_o_strtoul` | `0x85420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 677 | `_o__W_Getmonths` | `0x85440` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 784 | `_o__crt_atexit` | `0x85560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1638 | `_o_rand_s` | `0x85570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 676 | `_o__W_Getdays` | `0x85580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1434 | `_o__wtof` | `0x855A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1925 | `_wcstod_l` | `0x85620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1931 | `_wcstold_l` | `0x85620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `_o__Gettnames` | `0x85630` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1747 | `_putwch_nolock` | `0x85CE0` | 82 | UnwindData |  |
| 199 | `_cputws` | `0x85DE0` | 205 | UnwindData |  |
| 1184 | `_o__mkgmtime64` | `0x85F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `_o__mbslwr_s` | `0x85F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1777 | `_set_fmode` | `0x85F50` | 73 | UnwindData |  |
| 1328 | `_o__wcreate_locale` | `0x85FA0` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2405 | `strtof` | `0x86290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1464 | `_o_atan2` | `0x862A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2464 | `wcstod` | `0x86320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2470 | `wcstold` | `0x86320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1466 | `_o_atanf` | `0x86330` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1471 | `_o_atoi` | `0x86460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `_iswprint_l` | `0x86480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2256 | `iswprint` | `0x86480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2228 | `hypot` | `0x86490` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `_fdpcomp` | `0x86500` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 891 | `_o__get_osfhandle` | `0x86760` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 924 | `_o__gmtime64_s` | `0x867A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `_ldpoly` | `0x867C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2317 | `nan` | `0x867F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2319 | `nanl` | `0x867F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2467 | `wcstok` | `0x86800` | 57 | UnwindData |  |
| 2407 | `strtok` | `0x868A0` | 46 | UnwindData |  |
| 1091 | `_o__mbsinc` | `0x868E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1463 | `_o_atan` | `0x868F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `_mbccpy_s` | `0x86910` | 20 | UnwindData |  |
| 531 | `_mbccpy_s_l` | `0x86930` | 204 | UnwindData |  |
| 71 | `__dstbias` | `0x86A10` | 25 | UnwindData |  |
| 859 | `_o__free_locale` | `0x86AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 573 | `_mbslen_l` | `0x86AE0` | 112 | UnwindData |  |
| 2122 | `copysign` | `0x86B60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2124 | `copysignl` | `0x86B60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1912 | `_wcslwr_s` | `0x86BB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `__daylight` | `0x86C10` | 25 | UnwindData |  |
| 1564 | `_o_iswprint` | `0x86C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1713 | `_o_wcsncat_s` | `0x86C50` | 35 | UnwindData |  |
| 783 | `_o__create_locale` | `0x86C80` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `_Getdays` | `0x86D00` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `__timezone` | `0x86D70` | 25 | UnwindData |  |
| 464 | `_iswblank_l` | `0x86D90` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2250 | `iswblank` | `0x86D90` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 566 | `_mbsicmp` | `0x86EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `_mbsnbcmp_l` | `0x86F00` | 333 | UnwindData |  |
| 2304 | `mbsrtowcs_s` | `0x870D0` | 122 | UnwindData |  |
| 2354 | `rename` | `0x87260` | 263 | UnwindData |  |
| 1991 | `_wrename` | `0x87370` | 45 | UnwindData |  |
| 489 | `_ldlog` | `0x87420` | 615 | UnwindData |  |
| 351 | `_getpid` | `0x87690` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1470 | `_o_atof` | `0x876F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2142 | `csinhl` | `0x87710` | 558 | UnwindData |  |
| 14 | `_Getmonths` | `0x87D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1879 | `_umask_s` | `0x87DA0` | 61 | UnwindData |  |
| 1809 | `_strcoll_l` | `0x87DF0` | 228 | UnwindData |  |
| 1030 | `_o__localtime64_s` | `0x87EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2249 | `iswascii` | `0x87F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `_o__memicmp` | `0x87F20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2188 | `fgets` | `0x87FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2452 | `wcsncat` | `0x87FB0` | 782 | UnwindData |  |
| 1733 | `_open` | `0x88320` | 35 | UnwindData |  |
| 322 | `_get_initial_narrow_environment` | `0x88410` | 35 | UnwindData |  |
| 2352 | `remquof` | `0x88440` | 1,139 | UnwindData |  |
| 86 | `__p__commode` | `0x888C0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1598 | `_o_lroundf` | `0x88960` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2241 | `isleadbyte` | `0x889F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1922 | `_wcsrev` | `0x88A00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1587 | `_o_log2` | `0x88A50` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `_abs64` | `0x88AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2232 | `imaxabs` | `0x88AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2268 | `llabs` | `0x88AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1365 | `_o__wcsupr` | `0x88AE0` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2368 | `set_terminate` | `0x894B0` | 44 | UnwindData |  |
| 1504 | `_o_fflush` | `0x894F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `_kbhit` | `0x89570` | 48 | UnwindData |  |
| 1725 | `_o_wcstombs_s` | `0x89850` | 38 | UnwindData |  |
| 2478 | `wctob` | `0x898F0` | 469 | UnwindData |  |
| 1399 | `_o__wgetenv_s` | `0x89AD0` | 28 | UnwindData |  |
| 1979 | `_wgetenv_s` | `0x89B60` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1597 | `_o_lround` | `0x8A150` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1599 | `_o_lroundl` | `0x8A150` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1718 | `_o_wcstof` | `0x8A1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2350 | `remove` | `0x8A1E0` | 143 | UnwindData |  |
| 1394 | `_o__wfsopen` | `0x8A280` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `_difftime32` | `0x8A2F0` | 43 | UnwindData |  |
| 2106 | `cexpl` | `0x8A330` | 643 | UnwindData |  |
| 15 | `_Gettnames` | `0x8A5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1486 | `_o_cosh` | `0x8A5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `_o__set_app_type` | `0x8A5F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2377 | `sinh` | `0x8A600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `_mbslwr_s` | `0x8A620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 667 | `_mktime32` | `0x8A630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `_ismbcdigit_l` | `0x8A640` | 92 | UnwindData |  |
| 700 | `_o___p__commode` | `0x8A6B0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1274 | `_o__strtoi64` | `0x8A730` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `_o_strtoll` | `0x8A730` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `_gmtime32_s` | `0x8A7F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1846 | `_strtoui64_l` | `0x8A800` | 127 | UnwindData |  |
| 1848 | `_strtoull_l` | `0x8A800` | 127 | UnwindData |  |
| 1849 | `_strtoumax_l` | `0x8A800` | 127 | UnwindData |  |
| 1790 | `_sleep` | `0x8A890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `_gmtime32` | `0x8A8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `_dup` | `0x8A8C0` | 85 | UnwindData |  |
| 184 | `_chmod` | `0x8A9E0` | 149 | UnwindData |  |
| 1898 | `_wchmod` | `0x8AA80` | 175 | UnwindData |  |
| 1501 | `_o_fclose` | `0x8ABD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1551 | `_o_isprint` | `0x8ABF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2217 | `fsetpos` | `0x8AC10` | 53 | UnwindData |  |
| 839 | `_o__fileno` | `0x8AC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2222 | `getenv` | `0x8AC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `_fpreset` | `0x8AC80` | 2,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2190 | `fgetws` | `0x8B580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1224 | `_o__set_fmode` | `0x8B590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `_localtime32_s` | `0x8B5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `_iswgraph_l` | `0x8B5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2254 | `iswgraph` | `0x8B5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1998 | `_wsopen_dispatch` | `0x8B5D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1515 | `_o_fmod` | `0x8B5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `_mbsrchr` | `0x8B600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `_o_log2f` | `0x8B610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1692 | `_o_tanh` | `0x8B630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `_o__set_new_mode` | `0x8B650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `_ismbcspace` | `0x8B670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1942 | `_wcsupr_s` | `0x8B680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `_o__Wcsftime` | `0x8B690` | 38 | UnwindData |  |
| 323 | `_get_initial_wide_environment` | `0x8BA00` | 35 | UnwindData |  |
| 615 | `_mbsnextc_l` | `0x8BA30` | 141 | UnwindData |  |
| 1535 | `_o_getenv` | `0x8BB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 778 | `_o__configure_wide_argv` | `0x8BB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 659 | `_memccpy` | `0x8BB40` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1577 | `_o_llround` | `0x8BCF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1579 | `_o_llroundl` | `0x8BCF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2366 | `scalbnf` | `0x8BD10` | 359 | UnwindData |  |
| 2065 | `btowc` | `0x8BED0` | 155 | UnwindData |  |
| 1970 | `_wfopen` | `0x8C000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `_locking` | `0x8C020` | 321 | UnwindData |  |
| 209 | `_d_int` | `0x8C4E0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `_ismbcalpha_l` | `0x8C590` | 129 | UnwindData |  |
| 1188 | `_o__mktime64` | `0x8C620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1608 | `_o_mbstowcs` | `0x8C640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `__initialize_lconv_for_unsigned_char` | `0x8C660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2044 | `acoshl` | `0x8C680` | 215 | UnwindData |  |
| 553 | `_mbschr` | `0x8C760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1677 | `_o_strftime` | `0x8C770` | 28 | UnwindData |  |
| 1654 | `_o_roundl` | `0x8C800` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 589 | `_mbsnbcpy_l` | `0x8C850` | 269 | UnwindData |  |
| 296 | `_fsopen` | `0x8C970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `_o__configthreadlocale` | `0x8C980` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1613 | `_o_modf` | `0x8CDB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2173 | `fdiml` | `0x8CDD0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `_get_wide_winmain_command_line` | `0x8CE50` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1691 | `_o_tanf` | `0x8CEF0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `_mbsnbicmp_l` | `0x8CF40` | 170 | UnwindData |  |
| 1878 | `_umask` | `0x8CFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 935 | `_o__initialize_wide_environment` | `0x8D010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 649 | `_mbstowcs_s_l` | `0x8D030` | 124 | UnwindData |  |
| 1459 | `_o_asinf` | `0x8D5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `_controlfp` | `0x8D600` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2141 | `csinhf` | `0x8D7D0` | 427 | UnwindData |  |
| 1352 | `_o__wcstod_l` | `0x8DB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1357 | `_o__wcstold_l` | `0x8DB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `__sys_nerr` | `0x8DB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 898 | `_o__get_wide_winmain_command_line` | `0x8DB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2023 | `_wtof_l` | `0x8DB70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 658 | `_mbtowc_l` | `0x8DB80` | 96 | UnwindData |  |
| 1256 | `_o__stricoll` | `0x8DC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1769 | `_seh_filter_exe` | `0x8DC90` | 178 | UnwindData |  |
| 2140 | `csinh` | `0x8DD50` | 479 | UnwindData |  |
| 1792 | `_sopen_dispatch` | `0x8E3B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `_iswpunct_l` | `0x8E3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2257 | `iswpunct` | `0x8E3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1494 | `_o_exit` | `0x8E3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2073 | `cacosh` | `0x8E410` | 894 | UnwindData |  |
| 1007 | `_o__itow` | `0x8E7A0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1982 | `_wmkdir` | `0x8E8E0` | 41 | UnwindData |  |
| 248 | `_fd_int` | `0x8E910` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2160 | `exit` | `0x8E9B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `__stdio_common_vfscanf` | `0x8EA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1717 | `_o_wcstod` | `0x8EA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1722 | `_o_wcstold` | `0x8EA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `_o__gcvt` | `0x8EA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1683 | `_o_strtok_s` | `0x8EA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2286 | `logb` | `0x8EA90` | 195 | UnwindData |  |
| 2395 | `strncat_s` | `0x8EB60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `__sys_errlist` | `0x8EB70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `_mbclen` | `0x8EBD0` | 95 | UnwindData |  |
| 1990 | `_wremove` | `0x8EC40` | 39 | UnwindData |  |
| 670 | `_nextafter` | `0x8EC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2323 | `nextafter` | `0x8EC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2325 | `nextafterl` | `0x8EC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2328 | `nexttowardl` | `0x8EC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `_o_ldexp` | `0x8EC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `_initialize_narrow_environment` | `0x8ECA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `__p___argc` | `0x8ECB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `_o__mbstrlen` | `0x8ECC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `_mbsdec` | `0x8ECD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1776 | `_set_error_mode` | `0x8ECE0` | 71 | UnwindData |  |
| 277 | `_findnext64i32` | `0x8ED30` | 45 | UnwindData |  |
| 836 | `_o__fgetwchar` | `0x8ED70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1540 | `_o_getwchar` | `0x8ED70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1250 | `_o__strdup` | `0x8ED90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `_flushall` | `0x8EDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `_findclose` | `0x8EDC0` | 37 | UnwindData |  |
| 265 | `_fgetwchar` | `0x8EDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2227 | `getwchar` | `0x8EDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 662 | `_mkdir` | `0x8EE10` | 147 | UnwindData |  |
| 888 | `_o__get_initial_wide_environment` | `0x8EEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2166 | `expm1` | `0x8EED0` | 315 | UnwindData |  |
| 2042 | `acosh` | `0x8F020` | 224 | UnwindData |  |
| 777 | `_o__configure_narrow_argv` | `0x8F110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1724 | `_o_wcstombs` | `0x8F130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1756 | `_register_thread_local_exe_atexit_callback` | `0x8F150` | 60 | UnwindData |  |
| 440 | `_ismbclower` | `0x8F1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1758 | `_rmdir` | `0x8F1B0` | 143 | UnwindData |  |
| 1719 | `_o_wcstok` | `0x8F250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `__p___wargv` | `0x8F270` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 774 | `_o__close` | `0x8F2D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 698 | `_o___p___wargv` | `0x8F2F0` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2012 | `_wstat64` | `0x8F5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2171 | `fdim` | `0x8F5F0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2013 | `_wstat64i32` | `0x8F6C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1774 | `_set_doserrno` | `0x8F710` | 40 | UnwindData |  |
| 543 | `_mbctolower_l` | `0x8F740` | 133 | UnwindData |  |
| 192 | `_configure_wide_argv` | `0x8FA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | `_o__difftime64` | `0x8FAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2129 | `cpow` | `0x8FAC0` | 196 | UnwindData |  |
| 2104 | `cexp` | `0x8FB90` | 599 | UnwindData |  |
| 1289 | `_o__tell` | `0x8FDF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `__p__environ` | `0x8FE20` | 25 | UnwindData |  |
| 1915 | `_wcsncoll_l` | `0x8FE40` | 238 | UnwindData |  |
| 2391 | `strerror_s` | `0x8FF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2231 | `ilogbl` | `0x8FF50` | 159 | UnwindData |  |
| 2363 | `scalblnf` | `0x90000` | 364 | UnwindData |  |
| 1854 | `_strxfrm_l` | `0x90180` | 478 | UnwindData |  |
| 790 | `_o__difftime32` | `0x903F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1856 | `_tell` | `0x90400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2172 | `fdimf` | `0x90420` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2453 | `wcsncat_s` | `0x90470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 923 | `_o__gmtime64` | `0x90480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 933 | `_o__initialize_narrow_environment` | `0x904A0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2484 | `wmemmove_s` | `0x90640` | 82 | UnwindData |  |
| 196 | `_copysign` | `0x906A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2193 | `fma` | `0x906E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2226 | `getwc` | `0x90700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1192 | `_o__open_osfhandle` | `0x90710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 656 | `_mbsupr_s` | `0x90730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `_initialize_wide_environment` | `0x90740` | 3,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `_o__dup2` | `0x913B0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1565 | `_o_iswpunct` | `0x91440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2311 | `memcpy_s` | `0x91460` | 130 | UnwindData |  |
| 2204 | `fopen` | `0x914F0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1681 | `_o_strtof` | `0x916F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1838 | `_strtof_l` | `0x91710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2362 | `scalbln` | `0x91720` | 424 | UnwindData |  |
| 2288 | `logbl` | `0x918D0` | 195 | UnwindData |  |
| 1509 | `_o_fgetws` | `0x919A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1452 | `_o_acosf` | `0x919C0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1807 | `_stat64i32` | `0x91C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2168 | `expm1l` | `0x91C40` | 311 | UnwindData |  |
| 528 | `_mbccpy` | `0x91D80` | 134 | UnwindData |  |
| 273 | `_findfirst64i32` | `0x91E10` | 45 | UnwindData |  |
| 617 | `_mbsnicmp_l` | `0x91EB0` | 444 | UnwindData |  |
| 887 | `_o__get_initial_narrow_environment` | `0x92080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `_o__mktime32` | `0x920A0` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `__p___argv` | `0x92C00` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2045 | `asctime` | `0x933B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2301 | `mbrtoc32` | `0x933C0` | 92 | UnwindData |  |
| 696 | `_o___p___argc` | `0x93430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 697 | `_o___p___argv` | `0x93450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2361 | `roundl` | `0x93470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1029 | `_o__localtime64` | `0x93480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `_fread_nolock` | `0x934A0` | 29 | UnwindData |  |
| 801 | `_o__dup` | `0x934E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1743 | `_putenv_s` | `0x93500` | 56 | UnwindData |  |
| 1862 | `_timespec64_get` | `0x93540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1863 | `_tolower` | `0x93550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `_o__get_narrow_winmain_command_line` | `0x93560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2348 | `remainderf` | `0x93580` | 627 | UnwindData |  |
| 325 | `_get_narrow_winmain_command_line` | `0x93800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1557 | `_o_iswascii` | `0x93810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1346 | `_o__wcsnicoll` | `0x93830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `_makepath_s` | `0x93850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2229 | `ilogb` | `0x93860` | 159 | UnwindData |  |
| 2482 | `wctype` | `0x93910` | 96 | UnwindData |  |
| 2037 | `_yn` | `0x93980` | 231 | UnwindData |  |
| 191 | `_configure_narrow_argv` | `0x93A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2370 | `setbuf` | `0x93A80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2046 | `asctime_s` | `0x93AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `_o_fputc` | `0x93AC0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1993 | `_wrmdir` | `0x93EE0` | 39 | UnwindData |  |
| 582 | `_mbsnbcmp` | `0x93F10` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1293 | `_o__tolower` | `0x93FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1978 | `_wgetenv` | `0x93FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `_fstat64i32` | `0x93FD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1521 | `_o_fputwc` | `0x94010` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1837 | `_strtod_l` | `0x941E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1843 | `_strtold_l` | `0x941E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2285 | `log2l` | `0x941F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `__p__wenviron` | `0x94200` | 25 | UnwindData |  |
| 1451 | `_o_acos` | `0x94290` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1857 | `_telli64` | `0x94310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `_o__strlwr` | `0x94330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2318 | `nanf` | `0x94350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `_ctime64_s` | `0x94360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1742 | `_putenv` | `0x94370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `_fdopen` | `0x94380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `_ismbcdigit` | `0x94390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1924 | `_wcsset_s` | `0x943A0` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 572 | `_mbslen` | `0x94820` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1732 | `_o_wmemmove_s` | `0x94A60` | 35 | UnwindData |  |
| 807 | `_o__endthreadex` | `0x94A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1840 | `_strtoi64_l` | `0x94AB0` | 127 | UnwindData |  |
| 1841 | `_strtoimax_l` | `0x94AB0` | 127 | UnwindData |  |
| 1844 | `_strtoll_l` | `0x94AB0` | 127 | UnwindData |  |
| 1225 | `_o__set_invalid_parameter_handler` | `0x94B40` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2390 | `strerror` | `0x95250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `_localtime32` | `0x95260` | 72 | UnwindData |  |
| 88 | `__p__fmode` | `0x952B0` | 25 | UnwindData |  |
| 1563 | `_o_iswlower` | `0x952D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | `_mbsnextc` | `0x952F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1822 | `_strlwr_s` | `0x95300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1852 | `_strupr_s` | `0x95310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `_ismbcalpha` | `0x95320` | 2,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `_Cmulcc` | `0x95D60` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `_LCmulcc` | `0x95D60` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `_findfirst64` | `0x95F40` | 45 | UnwindData |  |
| 1506 | `_o_fgetpos` | `0x95F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `_o__pipe` | `0x95FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2110 | `clearerr` | `0x95FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1610 | `_o_mbtowc` | `0x95FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1415 | `_o__wsetlocale` | `0x95FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `_o_fseek` | `0x96000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `_o__setmode` | `0x96020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1476 | `_o_btowc` | `0x96040` | 1,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `_mbscspn` | `0x96500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1690 | `_o_tan` | `0x96510` | 9,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 733 | `_o___timezone` | `0x989B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2386 | `strcoll` | `0x989D0` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `_o__dsign` | `0x991D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1503 | `_o_ferror` | `0x991F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1787 | `_setmbcp` | `0x99270` | 58 | UnwindData |  |
| 861 | `_o__fseeki64` | `0x993D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1661 | `_o_set_terminate` | `0x993F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `_mbsnbicmp` | `0x99400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 628 | `_mbspbrk` | `0x99410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1260 | `_o__strlwr_s` | `0x99420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `_o__beginthread` | `0x99440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `_ctime64` | `0x99460` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1815 | `_strftime_l` | `0x995F0` | 30 | UnwindData |  |
| 1965 | `_wfindfirst64i32` | `0x99620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `_o___stdio_common_vswprintf_p` | `0x99630` | 55 | UnwindData |  |
| 1507 | `_o_fgets` | `0x99670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `_o__waccess` | `0x99690` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1771 | `_set_abort_behavior` | `0x99700` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1969 | `_wfindnext64i32` | `0x99C60` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `_mbctolower` | `0x99D80` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `_get_terminate` | `0x99EC0` | 34 | UnwindData |  |
| 1398 | `_o__wgetenv` | `0x9A4B0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 775 | `_o__commit` | `0x9A5A0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `_FCbuild` | `0x9A9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `_get_tzname` | `0x9A9F0` | 236 | UnwindData |  |
| 1222 | `_o__set_doserrno` | `0x9AB00` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `_fstat64` | `0x9AF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2108 | `cimagf` | `0x9AF10` | 19 | UnwindData |  |
| 328 | `_get_printf_count_output` | `0x9AF30` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `_o_feof` | `0x9B060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1520 | `_o_fputs` | `0x9B080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1246 | `_o__stat64i32` | `0x9B0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `_o__wmkdir` | `0x9B0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | `_mbsspn` | `0x9B0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `_ftime32` | `0x9B0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `_ftime32_s` | `0x9B0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `_get_current_locale` | `0x9B100` | 192 | UnwindData |  |
| 1988 | `_wputenv` | `0x9B360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2194 | `fmaf` | `0x9B370` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `_fstat32i64` | `0x9B490` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2081 | `casin` | `0x9B930` | 84 | UnwindData |  |
| 2164 | `exp2l` | `0x9BAF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `_cexit` | `0x9BB00` | 7,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2038 | `abort` | `0x9D670` | 106 | UnwindData |  |
| 6 | `_Exit` | `0x9D6E0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `_exit` | `0x9D6E0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2036 | `_y1` | `0x9DAC0` | 6,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `_getwche_nolock` | `0x9F5C0` | 83 | UnwindData |  |
| 163 | `_atoldbl_l` | `0x9F920` | 172 | UnwindData |  |
| 1930 | `_wcstol_l` | `0x9FBF0` | 125 | UnwindData |  |
| 342 | `_getche_nolock` | `0x9FEF0` | 62 | UnwindData |  |
| 1894 | `_wasctime` | `0xA0170` | 122 | UnwindData |  |
| 2287 | `logbf` | `0xA01F0` | 166 | UnwindData |  |
| 1891 | `_utime64` | `0xA03F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `___mb_cur_max_l_func` | `0xA0480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 692 | `_o___conio_common_vcwscanf` | `0xA04A0` | 35 | UnwindData |  |
| 1886 | `_unlink` | `0xA0540` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `_mbsrev_l` | `0xA07F0` | 269 | UnwindData |  |
| 1920 | `_wcsnset` | `0xA0970` | 3,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1806 | `_stat64` | `0xA18B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `_o__wputenv_s` | `0xA18C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1406 | `_o__wpopen` | `0xA18E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1348 | `_o__wcsnset` | `0xA1900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `_o__strupr_s` | `0xA1920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `_o__controlfp_s` | `0xA1940` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2005 | `_wspawnve` | `0xA1BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1614 | `_o_modff` | `0xA1BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1648 | `_o_rewind` | `0xA1C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1682 | `_o_strtok` | `0xA1C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1432 | `_o__wsystem` | `0xA1C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `_o__mbsbtype` | `0xA1C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1446 | `_o__wutime64` | `0xA1C90` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 641 | `_mbsspnp_l` | `0xA1E70` | 263 | UnwindData |  |
| 2034 | `_wutime64` | `0xA22F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `_mbsbtype` | `0xA2350` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2415 | `strxfrm` | `0xA2460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 646 | `_mbstok_s` | `0xA2470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 632 | `_mbsrev` | `0xA2480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 640 | `_mbsspnp` | `0xA2490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 937 | `_o__invalid_parameter_noinfo_noreturn` | `0xA24A0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1968 | `_wfindnext64` | `0xA25F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2032 | `_wunlink` | `0xA2660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `_fdsin` | `0xA2670` | 298 | UnwindData |  |
| 1961 | `_wfdopen` | `0xA2BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1895 | `_wasctime_s` | `0xA2BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1948 | `_wctime64_s` | `0xA2BE0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2119 | `conj` | `0xA2E10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2121 | `conjl` | `0xA2E10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2303 | `mbsrtowcs` | `0xA2E40` | 92 | UnwindData |  |
| 148 | `_aligned_offset_realloc` | `0xA3160` | 602 | UnwindData |  |
| 149 | `_aligned_offset_recalloc` | `0xA33C0` | 784 | UnwindData |  |
| 552 | `_mbscat_s_l` | `0xA3820` | 572 | UnwindData |  |
| 2167 | `expm1f` | `0xA3B60` | 199 | UnwindData |  |
| 2017 | `_wstrtime_s` | `0xA3CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `_mbsncat_s_l` | `0xA3CE0` | 677 | UnwindData |  |
| 2120 | `conjf` | `0xA40B0` | 39 | UnwindData |  |
| 345 | `_getdiskfree` | `0xA4390` | 196 | UnwindData |  |
| 2213 | `freopen` | `0xA44C0` | 47 | UnwindData |  |
| 1526 | `_o_freopen` | `0xA4500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `_fdpoly` | `0xA4520` | 1,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `__stdio_common_vfwscanf` | `0xA4C00` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `_futime64` | `0xA4EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `_Cbuild` | `0xA4ED0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `_LCbuild` | `0xA4ED0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `_atof_l` | `0xA50E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `_mktemp` | `0xA50F0` | 81 | UnwindData |  |
| 383 | `_isalnum_l` | `0xA53D0` | 24 | UnwindData |  |
| 384 | `_isalpha_l` | `0xA54B0` | 24 | UnwindData |  |
| 390 | `_isdigit_l` | `0xA5590` | 20 | UnwindData |  |
| 1897 | `_wchdir` | `0xA57D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2015 | `_wstrdate_s` | `0xA5830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1262 | `_o__strncoll` | `0xA5840` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2078 | `carg` | `0xA5A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2080 | `cargl` | `0xA5A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1997 | `_wsopen` | `0xA5A20` | 68 | UnwindData |  |
| 1904 | `_wcserror_s` | `0xA5A70` | 127 | UnwindData |  |
| 607 | `_mbsncmp_l` | `0xA61D0` | 320 | UnwindData |  |
| 181 | `_chdrive` | `0xA67A0` | 129 | UnwindData |  |
| 153 | `_atodbl` | `0xA6880` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `_FCmulcc` | `0xA6AF0` | 74 | UnwindData |  |
| 2178 | `feholdexcept` | `0xA6B70` | 80 | UnwindData |  |
| 2136 | `crealf` | `0xA6C80` | 18 | UnwindData |  |
| 1125 | `_o__mbsnccnt` | `0xA6CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `_o__mbsrev_l` | `0xA6CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1259 | `_o__strlwr_l` | `0xA6CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2107 | `cimag` | `0xA6D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2109 | `cimagl` | `0xA6D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2135 | `creal` | `0xA6D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2137 | `creall` | `0xA6D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1309 | `_o__umask_s` | `0xA6D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1749 | `_query_app_type` | `0xA6D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `_mbsnbcpy` | `0xA6D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1994 | `_wsearchenv` | `0xA6D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1903 | `_wcserror` | `0xA6D70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2125 | `cos` | `0xA6DC0` | 1,402 | UnwindData |  |
| 2126 | `cosf` | `0xA7600` | 543 | UnwindData |  |
| 2161 | `exp` | `0xA7830` | 1,045 | UnwindData |  |
| 2165 | `expf` | `0xA7DD0` | 346 | UnwindData |  |
| 2202 | `fmod` | `0xA8020` | 692 | UnwindData |  |
| 2277 | `log` | `0xA82F0` | 1,323 | UnwindData |  |
| 2278 | `log10` | `0xA8830` | 1,451 | UnwindData |  |
| 2279 | `log10f` | `0xA9000` | 504 | UnwindData |  |
| 2289 | `logf` | `0xA93D0` | 460 | UnwindData |  |
| 2334 | `powf` | `0xA95B0` | 3,766 | UnwindData |  |
| 2347 | `remainder` | `0xAA480` | 1,000 | UnwindData |  |
| 2360 | `roundf` | `0xAB030` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2359 | `round` | `0xAB080` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2375 | `sin` | `0xAB100` | 1,386 | UnwindData |  |
| 2376 | `sinf` | `0xAB9F0` | 845 | UnwindData |  |
| 2417 | `tan` | `0xAC300` | 1,459 | UnwindData |  |
| 2418 | `tanf` | `0xACDD0` | 730 | UnwindData |  |
| 4 | `_CreateFrameInfo` | `0xADBA0` | 58 | UnwindData |  |
| 10 | `_FindAndUnlinkFrame` | `0xADBE0` | 83 | UnwindData |  |
| 11 | `_GetImageBase` | `0xADC40` | 18 | UnwindData |  |
| 12 | `_GetThrowImageBase` | `0xADC60` | 18 | UnwindData |  |
| 20 | `_SetImageBase` | `0xADC80` | 24 | UnwindData |  |
| 21 | `_SetThrowImageBase` | `0xADCA0` | 24 | UnwindData |  |
| 35 | `__CxxFrameHandler` | `0xADCC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `__CxxFrameHandler2` | `0xADCC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `__CxxFrameHandler3` | `0xADCD0` | 134 | UnwindData |  |
| 38 | `__CxxFrameHandler4` | `0xADD60` | 191 | UnwindData |  |
| 5 | `_CxxThrowException` | `0xADE30` | 166 | UnwindData |  |
| 42 | `__DestructExceptionObject` | `0xADEE0` | 108 | UnwindData |  |
| 16 | `_IsExceptionObjectToBeDestroyed` | `0xADF60` | 47 | UnwindData |  |
| 22 | `_SetWinRTOutOfMemoryExceptionCallback` | `0xADFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `__AdjustPointer` | `0xADFB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `__FrameUnwindFilter` | `0xADFE0` | 102 | UnwindData |  |
| 44 | `__GetPlatformExceptionInfo` | `0xAE050` | 91 | UnwindData |  |
| 65 | `__current_exception` | `0xAE0C0` | 18 | UnwindData |  |
| 66 | `__current_exception_context` | `0xAE0E0` | 18 | UnwindData |  |
| 96 | `__processing_throw` | `0xAE100` | 18 | UnwindData |  |
| 103 | `__std_terminate` | `0xAE120` | 10 | UnwindData |  |
| 382 | `_is_exception_typeof` | `0xAE130` | 165 | UnwindData |  |
| 29 | `__BuildCatchObject` | `0xB12E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `__BuildCatchObjectHelper` | `0xB12F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `__TypeMatch` | `0xB1300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `__C_specific_handler` | `0xB1310` | 535 | UnwindData |  |
| 32 | `__C_specific_handler_noexcept` | `0xB1530` | 75 | UnwindData |  |
| 33 | `__CxxDetectRethrow` | `0xB1590` | 68 | UnwindData |  |
| 34 | `__CxxExceptionFilter` | `0xB15E0` | 503 | UnwindData |  |
| 39 | `__CxxQueryExceptionSize` | `0xB17E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `__CxxRegisterExceptionObject` | `0xB17F0` | 172 | UnwindData |  |
| 41 | `__CxxUnregisterExceptionObject` | `0xB18B0` | 294 | UnwindData |  |
| 45 | `__NLG_Dispatch2` | `0xB1A10` | 1 | UnwindData |  |
| 46 | `__NLG_Return2` | `0xB1A20` | 1 | UnwindData |  |
| 47 | `__RTCastToVoid` | `0xB2040` | 93 | UnwindData |  |
| 48 | `__RTDynamicCast` | `0xB20B0` | 366 | UnwindData |  |
| 49 | `__RTtypeid` | `0xB2230` | 180 | UnwindData |  |
| 101 | `__std_exception_copy` | `0xB2300` | 141 | UnwindData |  |
| 102 | `__std_exception_destroy` | `0xB23A0` | 37 | UnwindData |  |
| 104 | `__std_type_info_compare` | `0xB23F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `__std_type_info_destroy_list` | `0xB2420` | 42 | UnwindData |  |
| 106 | `__std_type_info_hash` | `0xB2450` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `__std_type_info_name` | `0xB2490` | 277 | UnwindData |  |
| 136 | `__uncaught_exception` | `0xB25B0` | 30 | UnwindData |  |
| 137 | `__uncaught_exceptions` | `0xB25E0` | 27 | UnwindData |  |
| 329 | `_get_purecall_handler` | `0xB2610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1738 | `_purecall` | `0xB2620` | 25 | UnwindData |  |
| 1782 | `_set_purecall_handler` | `0xB2640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `_get_unexpected` | `0xB2660` | 34 | UnwindData |  |
| 2369 | `set_unexpected` | `0xB2690` | 44 | UnwindData |  |
| 2437 | `unexpected` | `0xB26D0` | 29 | UnwindData |  |
| 500 | `_local_unwind` | `0xB2700` | 41 | UnwindData |  |
| 1783 | `_set_se_translator` | `0xB2740` | 45 | UnwindData |  |
| 2290 | `longjmp` | `0xB2780` | 40 | UnwindData |  |
| 99 | `__report_gsfailure` | `0xB31E0` | 210 | UnwindData |  |
| 675 | `_o__Strftime` | `0xB9280` | 38 | UnwindData |  |
| 685 | `_o___conio_common_vcprintf` | `0xB92B0` | 35 | UnwindData |  |
| 686 | `_o___conio_common_vcprintf_p` | `0xB92E0` | 35 | UnwindData |  |
| 687 | `_o___conio_common_vcprintf_s` | `0xB9310` | 35 | UnwindData |  |
| 688 | `_o___conio_common_vcscanf` | `0xB9340` | 35 | UnwindData |  |
| 689 | `_o___conio_common_vcwprintf` | `0xB9370` | 35 | UnwindData |  |
| 690 | `_o___conio_common_vcwprintf_p` | `0xB93A0` | 35 | UnwindData |  |
| 691 | `_o___conio_common_vcwprintf_s` | `0xB93D0` | 35 | UnwindData |  |
| 693 | `_o___daylight` | `0xB9400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 694 | `_o___dstbias` | `0xB9420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 695 | `_o___fpe_flt_rounds` | `0xB9440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 699 | `_o___p__acmdln` | `0xB9460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 701 | `_o___p__environ` | `0xB9480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | `_o___p__fmode` | `0xB94A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `_o___p__mbcasemap` | `0xB94C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `_o___p__mbctype` | `0xB94E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `_o___p__pgmptr` | `0xB9500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 706 | `_o___p__wcmdln` | `0xB9520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `_o___p__wenviron` | `0xB9540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 708 | `_o___p__wpgmptr` | `0xB9560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `_o___pwctype_func` | `0xB9580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `_o___stdio_common_vfprintf_p` | `0xB95A0` | 45 | UnwindData |  |
| 717 | `_o___stdio_common_vfprintf_s` | `0xB95E0` | 45 | UnwindData |  |
| 720 | `_o___stdio_common_vfwprintf_p` | `0xB9620` | 45 | UnwindData |  |
| 722 | `_o___stdio_common_vfwscanf` | `0xB9660` | 45 | UnwindData |  |
| 726 | `_o___stdio_common_vsprintf_p` | `0xB96A0` | 55 | UnwindData |  |
| 734 | `_o___tzname` | `0xB96E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `_o___wcserror` | `0xB9700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 736 | `_o__access` | `0xB9720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `_o__access_s` | `0xB9740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `_o__aligned_msize` | `0xB9760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `_o__aligned_offset_realloc` | `0xB9780` | 35 | UnwindData |  |
| 743 | `_o__aligned_offset_recalloc` | `0xB97B0` | 38 | UnwindData |  |
| 744 | `_o__aligned_realloc` | `0xB97E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `_o__aligned_recalloc` | `0xB9800` | 35 | UnwindData |  |
| 746 | `_o__atodbl` | `0xB9830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `_o__atodbl_l` | `0xB9850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 748 | `_o__atof_l` | `0xB9870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `_o__atoflt` | `0xB9890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `_o__atoflt_l` | `0xB98B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `_o__atoi64` | `0xB98D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1473 | `_o_atoll` | `0xB98D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | `_o__atoi64_l` | `0xB98F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `_o__atoll_l` | `0xB98F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `_o__atoi_l` | `0xB9910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 754 | `_o__atol_l` | `0xB9910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 755 | `_o__atoldbl` | `0xB9930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `_o__atoldbl_l` | `0xB9950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `_o__beep` | `0xB9970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `_o__cabs` | `0xB9980` | 28 | UnwindData |  |
| 762 | `_o__callnewh` | `0xB99B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | `_o__cexit` | `0xB99C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `_o__cgets` | `0xB99E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `_o__cgets_s` | `0xB9A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `_o__cgetws` | `0xB9A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 768 | `_o__cgetws_s` | `0xB9A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `_o__chdir` | `0xB9A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `_o__chdrive` | `0xB9A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `_o__chmod` | `0xB9AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 772 | `_o__chsize` | `0xB9AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `_o__chsize_s` | `0xB9AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 780 | `_o__cputs` | `0xB9AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `_o__cputws` | `0xB9B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 782 | `_o__creat` | `0xB9B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `_o__ctime32_s` | `0xB9B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 786 | `_o__ctime64_s` | `0xB9B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | `_o__cwait` | `0xB9B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 788 | `_o__d_int` | `0xB9BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 792 | `_o__dlog` | `0xB9BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `_o__dnorm` | `0xB9BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `_o__dpcomp` | `0xB9BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 795 | `_o__dpoly` | `0xB9C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `_o__dscale` | `0xB9C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `_o__dsin` | `0xB9C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `_o__dtest` | `0xB9C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `_o__ldtest` | `0xB9C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 800 | `_o__dunscale` | `0xB9C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 803 | `_o__dupenv_s` | `0xB9CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 804 | `_o__ecvt` | `0xB9CC0` | 35 | UnwindData |  |
| 806 | `_o__endthread` | `0xB9CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 808 | `_o__eof` | `0xB9D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `_o__except1` | `0xB9D30` | 38 | UnwindData |  |
| 812 | `_o__execv` | `0xB9D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `_o__execve` | `0xB9D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `_o__execvp` | `0xB9DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `_o__execvpe` | `0xB9DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 816 | `_o__exit` | `0xB9DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `_o__expand` | `0xB9E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `_o__fclose_nolock` | `0xB9E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `_o__fcloseall` | `0xB9E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 820 | `_o__fcvt` | `0xB9E60` | 35 | UnwindData |  |
| 821 | `_o__fcvt_s` | `0xB9E90` | 55 | UnwindData |  |
| 822 | `_o__fd_int` | `0xB9ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | `_o__fdexp` | `0xB9EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `_o__fdlog` | `0xB9F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 826 | `_o__fdopen` | `0xB9F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `_o__fdpcomp` | `0xB9F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 828 | `_o__fdpoly` | `0xB9F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 829 | `_o__fdscale` | `0xB9F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `_o__fdsign` | `0xB9FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `_o__fdsin` | `0xB9FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 832 | `_o__fflush_nolock` | `0xB9FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | `_o__fgetc_nolock` | `0xBA000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 900 | `_o__getc_nolock` | `0xBA000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 834 | `_o__fgetchar` | `0xBA020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1534 | `_o_getchar` | `0xBA020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 835 | `_o__fgetwc_nolock` | `0xBA040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 837 | `_o__filelength` | `0xBA060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `_o__filelengthi64` | `0xBA080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | `_o__findclose` | `0xBA0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 841 | `_o__findfirst32` | `0xBA0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `_o__findfirst32i64` | `0xBA0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `_o__findfirst64` | `0xBA100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `_o__findfirst64i32` | `0xBA120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `_o__findnext32` | `0xBA140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `_o__findnext32i64` | `0xBA160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `_o__findnext64` | `0xBA180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 848 | `_o__findnext64i32` | `0xBA1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `_o__flushall` | `0xBA1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `_o__fpclassf` | `0xBA1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `_o__fputc_nolock` | `0xBA200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `_o__fputchar` | `0xBA220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 854 | `_o__fputwc_nolock` | `0xBA240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 855 | `_o__fputwchar` | `0xBA260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 856 | `_o__fread_nolock` | `0xBA280` | 35 | UnwindData |  |
| 857 | `_o__fread_nolock_s` | `0xBA2B0` | 45 | UnwindData |  |
| 860 | `_o__fseek_nolock` | `0xBA2F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 862 | `_o__fseeki64_nolock` | `0xBA310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `_o__fsopen` | `0xBA330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `_o__fstat32` | `0xBA350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | `_o__fstat32i64` | `0xBA360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `_o__fstat64` | `0xBA370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `_o__fstat64i32` | `0xBA380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `_o__ftell_nolock` | `0xBA390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `_o__ftelli64` | `0xBA3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | `_o__ftelli64_nolock` | `0xBA3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 871 | `_o__ftime32` | `0xBA3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `_o__ftime32_s` | `0xBA400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `_o__ftime64` | `0xBA410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `_o__ftime64_s` | `0xBA420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `_o__fullpath` | `0xBA430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 876 | `_o__futime32` | `0xBA450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `_o__futime64` | `0xBA460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 878 | `_o__fwrite_nolock` | `0xBA470` | 35 | UnwindData |  |
| 881 | `_o__get_daylight` | `0xBA4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 882 | `_o__get_doserrno` | `0xBA4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 883 | `_o__get_dstbias` | `0xBA4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `_o__get_fmode` | `0xBA4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | `_o__get_heap_handle` | `0xBA510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `_o__get_invalid_parameter_handler` | `0xBA520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `_o__get_pgmptr` | `0xBA540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `_o__get_terminate` | `0xBA550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `_o__get_thread_local_invalid_parameter_handler` | `0xBA560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 896 | `_o__get_timezone` | `0xBA580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `_o__get_tzname` | `0xBA5A0` | 28 | UnwindData |  |
| 899 | `_o__get_wpgmptr` | `0xBA5D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 901 | `_o__getch` | `0xBA5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 902 | `_o__getch_nolock` | `0xBA600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `_o__getche` | `0xBA620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `_o__getche_nolock` | `0xBA640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 905 | `_o__getcwd` | `0xBA660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 906 | `_o__getdcwd` | `0xBA680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 907 | `_o__getdiskfree` | `0xBA6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 908 | `_o__getdllprocaddr` | `0xBA6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `_o__getdrive` | `0xBA6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | `_o__getdrives` | `0xBA6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | `_o__getmbcp` | `0xBA700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 912 | `_o__getsystime` | `0xBA720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | `_o__getw` | `0xBA730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | `_o__getwc_nolock` | `0xBA750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 915 | `_o__getwch` | `0xBA770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 916 | `_o__getwch_nolock` | `0xBA790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 917 | `_o__getwche` | `0xBA7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 918 | `_o__getwche_nolock` | `0xBA7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `_o__getws` | `0xBA7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `_o__getws_s` | `0xBA810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 921 | `_o__gmtime32` | `0xBA830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 922 | `_o__gmtime32_s` | `0xBA850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 925 | `_o__heapchk` | `0xBA870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `_o__heapmin` | `0xBA890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `_o__hypot` | `0xBA8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `_o__i64toa` | `0xBA8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 931 | `_o__i64tow` | `0xBA8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `_o__invalid_parameter_noinfo` | `0xBA910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 938 | `_o__isatty` | `0xBA930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 940 | `_o__isctype_l` | `0xBA950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 941 | `_o__isleadbyte_l` | `0xBA970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `_o__ismbbalnum` | `0xBA990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 943 | `_o__ismbbalnum_l` | `0xBA9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 944 | `_o__ismbbalpha` | `0xBA9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 945 | `_o__ismbbalpha_l` | `0xBA9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 946 | `_o__ismbbblank` | `0xBAA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 947 | `_o__ismbbblank_l` | `0xBAA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 948 | `_o__ismbbgraph` | `0xBAA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 949 | `_o__ismbbgraph_l` | `0xBAA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 950 | `_o__ismbbkalnum` | `0xBAA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 951 | `_o__ismbbkalnum_l` | `0xBAAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 952 | `_o__ismbbkana` | `0xBAAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 953 | `_o__ismbbkana_l` | `0xBAAF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 954 | `_o__ismbbkprint` | `0xBAB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `_o__ismbbkprint_l` | `0xBAB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 956 | `_o__ismbbkpunct` | `0xBAB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `_o__ismbbkpunct_l` | `0xBAB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 958 | `_o__ismbblead` | `0xBAB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 959 | `_o__ismbblead_l` | `0xBABB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 960 | `_o__ismbbprint` | `0xBABD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 961 | `_o__ismbbprint_l` | `0xBABF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 962 | `_o__ismbbpunct` | `0xBAC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 963 | `_o__ismbbpunct_l` | `0xBAC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 964 | `_o__ismbbtrail` | `0xBAC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 965 | `_o__ismbbtrail_l` | `0xBAC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 966 | `_o__ismbcalnum` | `0xBAC90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 967 | `_o__ismbcalnum_l` | `0xBACB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 968 | `_o__ismbcalpha` | `0xBACD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 969 | `_o__ismbcalpha_l` | `0xBACF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 970 | `_o__ismbcblank` | `0xBAD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 971 | `_o__ismbcblank_l` | `0xBAD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `_o__ismbcdigit` | `0xBAD50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `_o__ismbcdigit_l` | `0xBAD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 974 | `_o__ismbcgraph` | `0xBAD90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `_o__ismbcgraph_l` | `0xBADB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `_o__ismbchira` | `0xBADD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `_o__ismbchira_l` | `0xBADF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `_o__ismbckata` | `0xBAE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 979 | `_o__ismbckata_l` | `0xBAE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `_o__ismbcl0` | `0xBAE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `_o__ismbcl0_l` | `0xBAE70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 982 | `_o__ismbcl1` | `0xBAE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 983 | `_o__ismbcl1_l` | `0xBAEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 984 | `_o__ismbcl2` | `0xBAED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `_o__ismbcl2_l` | `0xBAEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `_o__ismbclegal` | `0xBAF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 987 | `_o__ismbclegal_l` | `0xBAF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `_o__ismbclower` | `0xBAF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `_o__ismbclower_l` | `0xBAF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `_o__ismbcprint` | `0xBAF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `_o__ismbcprint_l` | `0xBAFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `_o__ismbcpunct` | `0xBAFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `_o__ismbcpunct_l` | `0xBAFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 994 | `_o__ismbcspace` | `0xBB010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 995 | `_o__ismbcspace_l` | `0xBB030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `_o__ismbcsymbol` | `0xBB050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 997 | `_o__ismbcsymbol_l` | `0xBB070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `_o__ismbcupper` | `0xBB090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `_o__ismbcupper_l` | `0xBB0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `_o__ismbslead` | `0xBB0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `_o__ismbslead_l` | `0xBB0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `_o__ismbstrail` | `0xBB110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `_o__ismbstrail_l` | `0xBB130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `_o__iswctype_l` | `0xBB150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `_o__itoa` | `0xBB170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `_o__j0` | `0xBB190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `_o__j1` | `0xBB1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `_o__jn` | `0xBB1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `_o__kbhit` | `0xBB1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | `_o__ld_int` | `0xBB210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `_o__ldexp` | `0xBB230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `_o__ldlog` | `0xBB250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `_o__ldpcomp` | `0xBB270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `_o__ldpoly` | `0xBB290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `_o__ldscale` | `0xBB2B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `_o__ldsign` | `0xBB2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `_o__ldsin` | `0xBB2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `_o__ldunscale` | `0xBB300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `_o__lfind` | `0xBB320` | 38 | UnwindData |  |
| 1025 | `_o__lfind_s` | `0xBB350` | 48 | UnwindData |  |
| 1026 | `_o__loaddll` | `0xBB390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `_o__localtime32` | `0xBB3A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1028 | `_o__localtime32_s` | `0xBB3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `_o__locking` | `0xBB3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1033 | `_o__logb` | `0xBB400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1034 | `_o__logbf` | `0xBB420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `_o__lsearch` | `0xBB440` | 38 | UnwindData |  |
| 1036 | `_o__lsearch_s` | `0xBB470` | 48 | UnwindData |  |
| 1037 | `_o__lseek` | `0xBB4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `_o__lseeki64` | `0xBB4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1043 | `_o__makepath` | `0xBB4F0` | 38 | UnwindData |  |
| 1044 | `_o__makepath_s` | `0xBB520` | 48 | UnwindData |  |
| 1046 | `_o__mbbtombc` | `0xBB560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1047 | `_o__mbbtombc_l` | `0xBB580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1048 | `_o__mbbtype` | `0xBB5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1049 | `_o__mbbtype_l` | `0xBB5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1050 | `_o__mbccpy` | `0xBB5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1051 | `_o__mbccpy_l` | `0xBB5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `_o__mbccpy_s` | `0xBB610` | 28 | UnwindData |  |
| 1053 | `_o__mbccpy_s_l` | `0xBB640` | 38 | UnwindData |  |
| 1054 | `_o__mbcjistojms` | `0xBB670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1055 | `_o__mbcjistojms_l` | `0xBB690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `_o__mbcjmstojis` | `0xBB6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `_o__mbcjmstojis_l` | `0xBB6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `_o__mbclen` | `0xBB6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `_o__mbclen_l` | `0xBB710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1060 | `_o__mbctohira` | `0xBB730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `_o__mbctohira_l` | `0xBB750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1062 | `_o__mbctokata` | `0xBB770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1063 | `_o__mbctokata_l` | `0xBB790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1064 | `_o__mbctolower` | `0xBB7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1065 | `_o__mbctolower_l` | `0xBB7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `_o__mbctombb` | `0xBB7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `_o__mbctombb_l` | `0xBB810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1068 | `_o__mbctoupper` | `0xBB830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1069 | `_o__mbctoupper_l` | `0xBB850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1070 | `_o__mblen_l` | `0xBB870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `_o__mbsbtype_l` | `0xBB890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `_o__mbscat_s` | `0xBB8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `_o__mbscat_s_l` | `0xBB8D0` | 35 | UnwindData |  |
| 1075 | `_o__mbschr` | `0xBB900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `_o__mbschr_l` | `0xBB920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `_o__mbscmp_l` | `0xBB940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1079 | `_o__mbscoll` | `0xBB960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1080 | `_o__mbscoll_l` | `0xBB980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1081 | `_o__mbscpy_s` | `0xBB9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1082 | `_o__mbscpy_s_l` | `0xBB9C0` | 35 | UnwindData |  |
| 1083 | `_o__mbscspn` | `0xBB9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1084 | `_o__mbscspn_l` | `0xBBA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `_o__mbsdec` | `0xBBA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1086 | `_o__mbsdec_l` | `0xBBA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1088 | `_o__mbsicmp_l` | `0xBBA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `_o__mbsicoll` | `0xBBA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `_o__mbsicoll_l` | `0xBBAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `_o__mbsinc_l` | `0xBBAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `_o__mbslen` | `0xBBAF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `_o__mbslen_l` | `0xBBB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `_o__mbslwr` | `0xBBB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `_o__mbslwr_l` | `0xBBB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1098 | `_o__mbslwr_s_l` | `0xBBB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1099 | `_o__mbsnbcat` | `0xBBB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1100 | `_o__mbsnbcat_l` | `0xBBBB0` | 35 | UnwindData |  |
| 1101 | `_o__mbsnbcat_s` | `0xBBBE0` | 35 | UnwindData |  |
| 1102 | `_o__mbsnbcat_s_l` | `0xBBC10` | 45 | UnwindData |  |
| 1103 | `_o__mbsnbcmp` | `0xBBC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `_o__mbsnbcmp_l` | `0xBBC70` | 35 | UnwindData |  |
| 1105 | `_o__mbsnbcnt` | `0xBBCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `_o__mbsnbcnt_l` | `0xBBCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `_o__mbsnbcoll` | `0xBBCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1108 | `_o__mbsnbcoll_l` | `0xBBD00` | 35 | UnwindData |  |
| 1109 | `_o__mbsnbcpy` | `0xBBD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1110 | `_o__mbsnbcpy_l` | `0xBBD50` | 35 | UnwindData |  |
| 1111 | `_o__mbsnbcpy_s` | `0xBBD80` | 35 | UnwindData |  |
| 1112 | `_o__mbsnbcpy_s_l` | `0xBBDB0` | 45 | UnwindData |  |
| 1113 | `_o__mbsnbicmp` | `0xBBDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1114 | `_o__mbsnbicmp_l` | `0xBBE10` | 35 | UnwindData |  |
| 1115 | `_o__mbsnbicoll` | `0xBBE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1116 | `_o__mbsnbicoll_l` | `0xBBE60` | 35 | UnwindData |  |
| 1117 | `_o__mbsnbset` | `0xBBE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1118 | `_o__mbsnbset_l` | `0xBBEB0` | 35 | UnwindData |  |
| 1119 | `_o__mbsnbset_s` | `0xBBEE0` | 35 | UnwindData |  |
| 1120 | `_o__mbsnbset_s_l` | `0xBBF10` | 45 | UnwindData |  |
| 1121 | `_o__mbsncat` | `0xBBF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `_o__mbsncat_l` | `0xBBF70` | 35 | UnwindData |  |
| 1123 | `_o__mbsncat_s` | `0xBBFA0` | 35 | UnwindData |  |
| 1124 | `_o__mbsncat_s_l` | `0xBBFD0` | 45 | UnwindData |  |
| 1126 | `_o__mbsnccnt_l` | `0xBC010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1127 | `_o__mbsncmp` | `0xBC030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `_o__mbsncmp_l` | `0xBC050` | 35 | UnwindData |  |
| 1129 | `_o__mbsncoll` | `0xBC080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1130 | `_o__mbsncoll_l` | `0xBC0A0` | 35 | UnwindData |  |
| 1131 | `_o__mbsncpy` | `0xBC0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1132 | `_o__mbsncpy_l` | `0xBC0F0` | 35 | UnwindData |  |
| 1133 | `_o__mbsncpy_s` | `0xBC120` | 35 | UnwindData |  |
| 1134 | `_o__mbsncpy_s_l` | `0xBC150` | 45 | UnwindData |  |
| 1135 | `_o__mbsnextc` | `0xBC190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `_o__mbsnextc_l` | `0xBC1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `_o__mbsnicmp` | `0xBC1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `_o__mbsnicmp_l` | `0xBC1E0` | 35 | UnwindData |  |
| 1139 | `_o__mbsnicoll` | `0xBC210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1140 | `_o__mbsnicoll_l` | `0xBC230` | 35 | UnwindData |  |
| 1141 | `_o__mbsninc` | `0xBC260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `_o__mbsninc_l` | `0xBC280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `_o__mbsnlen` | `0xBC2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `_o__mbsnlen_l` | `0xBC2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `_o__mbsnset` | `0xBC2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `_o__mbsnset_l` | `0xBC300` | 35 | UnwindData |  |
| 1147 | `_o__mbsnset_s` | `0xBC330` | 35 | UnwindData |  |
| 1148 | `_o__mbsnset_s_l` | `0xBC360` | 45 | UnwindData |  |
| 1149 | `_o__mbspbrk` | `0xBC3A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1150 | `_o__mbspbrk_l` | `0xBC3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `_o__mbsrchr` | `0xBC3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1152 | `_o__mbsrchr_l` | `0xBC400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1153 | `_o__mbsrev` | `0xBC420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1155 | `_o__mbsset` | `0xBC440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1156 | `_o__mbsset_l` | `0xBC460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1157 | `_o__mbsset_s` | `0xBC480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1158 | `_o__mbsset_s_l` | `0xBC4A0` | 28 | UnwindData |  |
| 1159 | `_o__mbsspn` | `0xBC4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1160 | `_o__mbsspn_l` | `0xBC4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1161 | `_o__mbsspnp` | `0xBC510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1162 | `_o__mbsspnp_l` | `0xBC530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1164 | `_o__mbsstr_l` | `0xBC550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1165 | `_o__mbstok` | `0xBC570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1166 | `_o__mbstok_l` | `0xBC590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `_o__mbstok_s` | `0xBC5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1168 | `_o__mbstok_s_l` | `0xBC5D0` | 28 | UnwindData |  |
| 1169 | `_o__mbstowcs_l` | `0xBC600` | 28 | UnwindData |  |
| 1170 | `_o__mbstowcs_s_l` | `0xBC630` | 48 | UnwindData |  |
| 1172 | `_o__mbstrlen_l` | `0xBC670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `_o__mbstrnlen` | `0xBC690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `_o__mbstrnlen_l` | `0xBC6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `_o__mbsupr` | `0xBC6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `_o__mbsupr_l` | `0xBC6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `_o__mbsupr_s` | `0xBC710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `_o__mbsupr_s_l` | `0xBC730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1179 | `_o__mbtowc_l` | `0xBC750` | 28 | UnwindData |  |
| 1181 | `_o__memicmp_l` | `0xBC780` | 28 | UnwindData |  |
| 1182 | `_o__mkdir` | `0xBC7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `_o__mkgmtime32` | `0xBC7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `_o__mktemp` | `0xBC7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1186 | `_o__mktemp_s` | `0xBC810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `_o__nextafter` | `0xBC830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `_o_nextafter` | `0xBC830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1623 | `_o_nextafterl` | `0xBC830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1626 | `_o_nexttowardl` | `0xBC830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `_o__nextafterf` | `0xBC850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1622 | `_o_nextafterf` | `0xBC850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `_o__pclose` | `0xBC870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `_o__popen` | `0xBC890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1196 | `_o__purecall` | `0xBC8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1197 | `_o__putc_nolock` | `0xBC8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `_o__putch` | `0xBC8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `_o__putch_nolock` | `0xBC910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1200 | `_o__putenv` | `0xBC930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1201 | `_o__putenv_s` | `0xBC950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `_o__putw` | `0xBC970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `_o__putwc_nolock` | `0xBC990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1204 | `_o__putwch` | `0xBC9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `_o__putwch_nolock` | `0xBC9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1206 | `_o__putws` | `0xBC9F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `_o__read` | `0xBCA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `_o__resetstkoflw` | `0xBCA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `_o__rmdir` | `0xBCA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `_o__rmtmp` | `0xBCA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1214 | `_o__scalb` | `0xBCA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `_o__scalbf` | `0xBCAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1216 | `_o__searchenv` | `0xBCAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `_o__searchenv_s` | `0xBCAF0` | 28 | UnwindData |  |
| 1218 | `_o__seh_filter_dll` | `0xBCB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1219 | `_o__seh_filter_exe` | `0xBCB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `_o__set_abort_behavior` | `0xBCB60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `_o__set_new_handler` | `0xBCB70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1228 | `_o__set_thread_local_invalid_parameter_handler` | `0xBCB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `_o__seterrormode` | `0xBCBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `_o__setmbcp` | `0xBCBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `_o__setsystime` | `0xBCBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1233 | `_o__sleep` | `0xBCC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `_o__sopen` | `0xBCC10` | 28 | UnwindData |  |
| 1235 | `_o__sopen_dispatch` | `0xBCC40` | 46 | UnwindData |  |
| 1236 | `_o__sopen_s` | `0xBCC80` | 36 | UnwindData |  |
| 1237 | `_o__spawnv` | `0xBCCB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1238 | `_o__spawnve` | `0xBCCD0` | 34 | UnwindData |  |
| 1239 | `_o__spawnvp` | `0xBCD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1240 | `_o__spawnvpe` | `0xBCD20` | 34 | UnwindData |  |
| 1241 | `_o__splitpath` | `0xBCD50` | 38 | UnwindData |  |
| 1243 | `_o__stat32` | `0xBCD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1244 | `_o__stat32i64` | `0xBCDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1245 | `_o__stat64` | `0xBCDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1247 | `_o__strcoll_l` | `0xBCDE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `_o__strdate` | `0xBCE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `_o__strdate_s` | `0xBCE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1251 | `_o__strerror` | `0xBCE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1252 | `_o__strerror_s` | `0xBCE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `_o__strftime_l` | `0xBCE80` | 38 | UnwindData |  |
| 1255 | `_o__stricmp_l` | `0xBCEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `_o__stricoll_l` | `0xBCED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `_o__strlwr_s_l` | `0xBCEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1263 | `_o__strncoll_l` | `0xBCF10` | 35 | UnwindData |  |
| 1265 | `_o__strnicmp_l` | `0xBCF40` | 35 | UnwindData |  |
| 1266 | `_o__strnicoll` | `0xBCF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1267 | `_o__strnicoll_l` | `0xBCF90` | 35 | UnwindData |  |
| 1268 | `_o__strnset_s` | `0xBCFC0` | 28 | UnwindData |  |
| 1269 | `_o__strset_s` | `0xBCFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1270 | `_o__strtime` | `0xBD010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1271 | `_o__strtime_s` | `0xBD030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1272 | `_o__strtod_l` | `0xBD050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1277 | `_o__strtold_l` | `0xBD050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1273 | `_o__strtof_l` | `0xBD070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1275 | `_o__strtoi64_l` | `0xBD090` | 35 | UnwindData |  |
| 1278 | `_o__strtoll_l` | `0xBD090` | 35 | UnwindData |  |
| 1276 | `_o__strtol_l` | `0xBD0C0` | 28 | UnwindData |  |
| 1280 | `_o__strtoui64_l` | `0xBD0F0` | 35 | UnwindData |  |
| 1282 | `_o__strtoull_l` | `0xBD0F0` | 35 | UnwindData |  |
| 1281 | `_o__strtoul_l` | `0xBD120` | 28 | UnwindData |  |
| 1283 | `_o__strupr` | `0xBD150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `_o__strupr_l` | `0xBD170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1286 | `_o__strupr_s_l` | `0xBD190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `_o__strxfrm_l` | `0xBD1B0` | 28 | UnwindData |  |
| 1288 | `_o__swab` | `0xBD1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `_o__telli64` | `0xBD200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1291 | `_o__timespec32_get` | `0xBD220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1292 | `_o__timespec64_get` | `0xBD240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1294 | `_o__tolower_l` | `0xBD260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1295 | `_o__toupper` | `0xBD280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1296 | `_o__toupper_l` | `0xBD2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1298 | `_o__towupper_l` | `0xBD2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `_o__tzset` | `0xBD2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1300 | `_o__ui64toa` | `0xBD300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `_o__ui64tow` | `0xBD320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `_o__ultoa` | `0xBD340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1308 | `_o__umask` | `0xBD360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1310 | `_o__ungetc_nolock` | `0xBD380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `_o__ungetch` | `0xBD3A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1312 | `_o__ungetch_nolock` | `0xBD3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `_o__ungetwc_nolock` | `0xBD3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1314 | `_o__ungetwch` | `0xBD400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1315 | `_o__ungetwch_nolock` | `0xBD420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1316 | `_o__unlink` | `0xBD440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `_o__unloaddll` | `0xBD460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `_o__utime32` | `0xBD480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `_o__utime64` | `0xBD4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1322 | `_o__waccess_s` | `0xBD4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `_o__wasctime` | `0xBD4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1324 | `_o__wasctime_s` | `0xBD4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1325 | `_o__wchdir` | `0xBD510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `_o__wchmod` | `0xBD530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1327 | `_o__wcreat` | `0xBD550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1329 | `_o__wcscoll_l` | `0xBD570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `_o__wcserror` | `0xBD590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `_o__wcserror_s` | `0xBD5A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1333 | `_o__wcsftime_l` | `0xBD5C0` | 38 | UnwindData |  |
| 1336 | `_o__wcsicoll` | `0xBD5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `_o__wcsicoll_l` | `0xBD610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1341 | `_o__wcslwr_s_l` | `0xBD630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1342 | `_o__wcsncoll` | `0xBD650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1343 | `_o__wcsncoll_l` | `0xBD670` | 35 | UnwindData |  |
| 1345 | `_o__wcsnicmp_l` | `0xBD6A0` | 35 | UnwindData |  |
| 1347 | `_o__wcsnicoll_l` | `0xBD6D0` | 35 | UnwindData |  |
| 1349 | `_o__wcsnset_s` | `0xBD700` | 29 | UnwindData |  |
| 1350 | `_o__wcsset` | `0xBD730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1351 | `_o__wcsset_s` | `0xBD750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1353 | `_o__wcstof_l` | `0xBD770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `_o__wcstoi64_l` | `0xBD790` | 35 | UnwindData |  |
| 1358 | `_o__wcstoll_l` | `0xBD790` | 35 | UnwindData |  |
| 1356 | `_o__wcstol_l` | `0xBD7C0` | 28 | UnwindData |  |
| 1359 | `_o__wcstombs_l` | `0xBD7F0` | 28 | UnwindData |  |
| 1362 | `_o__wcstoui64_l` | `0xBD820` | 35 | UnwindData |  |
| 1364 | `_o__wcstoull_l` | `0xBD820` | 35 | UnwindData |  |
| 1363 | `_o__wcstoul_l` | `0xBD850` | 28 | UnwindData |  |
| 1366 | `_o__wcsupr_l` | `0xBD880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1368 | `_o__wcsupr_s_l` | `0xBD8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1369 | `_o__wcsxfrm_l` | `0xBD8C0` | 28 | UnwindData |  |
| 1370 | `_o__wctime32` | `0xBD8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1371 | `_o__wctime32_s` | `0xBD900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1372 | `_o__wctime64` | `0xBD920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1373 | `_o__wctime64_s` | `0xBD930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1374 | `_o__wctomb_l` | `0xBD950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1375 | `_o__wctomb_s_l` | `0xBD970` | 39 | UnwindData |  |
| 1376 | `_o__wdupenv_s` | `0xBD9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1377 | `_o__wexecv` | `0xBD9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1378 | `_o__wexecve` | `0xBD9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1379 | `_o__wexecvp` | `0xBDA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1380 | `_o__wexecvpe` | `0xBDA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1381 | `_o__wfdopen` | `0xBDA40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1382 | `_o__wfindfirst32` | `0xBDA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1383 | `_o__wfindfirst32i64` | `0xBDA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `_o__wfindfirst64` | `0xBDA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1385 | `_o__wfindfirst64i32` | `0xBDAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1386 | `_o__wfindnext32` | `0xBDAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `_o__wfindnext32i64` | `0xBDAF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1388 | `_o__wfindnext64` | `0xBDB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1389 | `_o__wfindnext64i32` | `0xBDB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1390 | `_o__wfopen` | `0xBDB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1391 | `_o__wfopen_s` | `0xBDB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1392 | `_o__wfreopen` | `0xBDB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1393 | `_o__wfreopen_s` | `0xBDBB0` | 28 | UnwindData |  |
| 1396 | `_o__wgetcwd` | `0xBDBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1397 | `_o__wgetdcwd` | `0xBDC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1400 | `_o__wmakepath` | `0xBDC20` | 38 | UnwindData |  |
| 1403 | `_o__wmktemp` | `0xBDC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1404 | `_o__wmktemp_s` | `0xBDC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1405 | `_o__wperror` | `0xBDC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `_o__wputenv` | `0xBDCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1409 | `_o__wremove` | `0xBDCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1410 | `_o__wrename` | `0xBDCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1411 | `_o__write` | `0xBDD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1412 | `_o__wrmdir` | `0xBDD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1413 | `_o__wsearchenv` | `0xBDD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1414 | `_o__wsearchenv_s` | `0xBDD60` | 28 | UnwindData |  |
| 1416 | `_o__wsopen_dispatch` | `0xBDD90` | 46 | UnwindData |  |
| 1417 | `_o__wsopen_s` | `0xBDDD0` | 36 | UnwindData |  |
| 1418 | `_o__wspawnv` | `0xBDE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1419 | `_o__wspawnve` | `0xBDE20` | 34 | UnwindData |  |
| 1420 | `_o__wspawnvp` | `0xBDE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1421 | `_o__wspawnvpe` | `0xBDE70` | 34 | UnwindData |  |
| 1422 | `_o__wsplitpath` | `0xBDEA0` | 38 | UnwindData |  |
| 1424 | `_o__wstat32` | `0xBDED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `_o__wstat32i64` | `0xBDEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1426 | `_o__wstat64` | `0xBDF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1427 | `_o__wstat64i32` | `0xBDF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1428 | `_o__wstrdate` | `0xBDF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1429 | `_o__wstrdate_s` | `0xBDF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `_o__wstrtime` | `0xBDF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `_o__wstrtime_s` | `0xBDFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1433 | `_o__wtmpnam_s` | `0xBDFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1435 | `_o__wtof_l` | `0xBDFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1438 | `_o__wtoi64_l` | `0xBE010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1443 | `_o__wtoll_l` | `0xBE010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1439 | `_o__wtoi_l` | `0xBE030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1441 | `_o__wtol_l` | `0xBE030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `_o__wunlink` | `0xBE050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1445 | `_o__wutime32` | `0xBE070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1447 | `_o__y0` | `0xBE090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `_o__y1` | `0xBE0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1449 | `_o__yn` | `0xBE0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1450 | `_o_abort` | `0xBE0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1453 | `_o_acosh` | `0xBE110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1454 | `_o_acoshf` | `0xBE130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1455 | `_o_acoshl` | `0xBE150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1456 | `_o_asctime` | `0xBE170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1457 | `_o_asctime_s` | `0xBE180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1460 | `_o_asinh` | `0xBE1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1461 | `_o_asinhf` | `0xBE1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1462 | `_o_asinhl` | `0xBE1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1467 | `_o_atanh` | `0xBE200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1468 | `_o_atanhf` | `0xBE220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1469 | `_o_atanhl` | `0xBE240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1478 | `_o_cbrt` | `0xBE260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `_o_cbrtf` | `0xBE280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1482 | `_o_clearerr` | `0xBE2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1483 | `_o_clearerr_s` | `0xBE2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1487 | `_o_coshf` | `0xBE2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1488 | `_o_erf` | `0xBE300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1489 | `_o_erfc` | `0xBE320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1490 | `_o_erfcf` | `0xBE340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1491 | `_o_erfcl` | `0xBE360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1492 | `_o_erff` | `0xBE380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1493 | `_o_erfl` | `0xBE3A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1496 | `_o_exp2` | `0xBE3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1497 | `_o_exp2f` | `0xBE3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1498 | `_o_exp2l` | `0xBE400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1500 | `_o_fabs` | `0xBE420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1508 | `_o_fgetwc` | `0xBE440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `_o_fma` | `0xBE460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1513 | `_o_fmaf` | `0xBE480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1514 | `_o_fmal` | `0xBE4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1517 | `_o_fopen` | `0xBE4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1518 | `_o_fopen_s` | `0xBE4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `_o_fputws` | `0xBE500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1524 | `_o_fread_s` | `0xBE520` | 45 | UnwindData |  |
| 1527 | `_o_freopen_s` | `0xBE560` | 28 | UnwindData |  |
| 1530 | `_o_fsetpos` | `0xBE590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `_o_ftell` | `0xBE5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1533 | `_o_getc` | `0xBE5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1537 | `_o_gets` | `0xBE5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `_o_gets_s` | `0xBE610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `_o_getwc` | `0xBE630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1541 | `_o_hypot` | `0xBE650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1542 | `_o_is_wctype` | `0xBE670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1545 | `_o_isblank` | `0xBE690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1548 | `_o_isgraph` | `0xBE6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1549 | `_o_isleadbyte` | `0xBE6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1550 | `_o_islower` | `0xBE6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1558 | `_o_iswblank` | `0xBE710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1562 | `_o_iswgraph` | `0xBE730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1571 | `_o_lgamma` | `0xBE750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1572 | `_o_lgammaf` | `0xBE770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1573 | `_o_lgammal` | `0xBE790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1574 | `_o_llrint` | `0xBE7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1575 | `_o_llrintf` | `0xBE7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1576 | `_o_llrintl` | `0xBE7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `_o_llroundf` | `0xBE810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1584 | `_o_log1p` | `0xBE830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1585 | `_o_log1pf` | `0xBE850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1586 | `_o_log1pl` | `0xBE870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1589 | `_o_log2l` | `0xBE890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1590 | `_o_logb` | `0xBE8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1591 | `_o_logbf` | `0xBE8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1592 | `_o_logbl` | `0xBE8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1594 | `_o_lrint` | `0xBE910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1596 | `_o_lrintl` | `0xBE930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1601 | `_o_mblen` | `0xBE950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1602 | `_o_mbrlen` | `0xBE970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1603 | `_o_mbrtoc16` | `0xBE990` | 28 | UnwindData |  |
| 1604 | `_o_mbrtoc32` | `0xBE9C0` | 28 | UnwindData |  |
| 1605 | `_o_mbrtowc` | `0xBE9F0` | 28 | UnwindData |  |
| 1606 | `_o_mbsrtowcs` | `0xBEA20` | 28 | UnwindData |  |
| 1607 | `_o_mbsrtowcs_s` | `0xBEA50` | 48 | UnwindData |  |
| 1615 | `_o_nan` | `0xBEA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1616 | `_o_nanf` | `0xBEAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `_o_nanl` | `0xBEAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1618 | `_o_nearbyint` | `0xBEAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1619 | `_o_nearbyintf` | `0xBEAF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1620 | `_o_nearbyintl` | `0xBEB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1624 | `_o_nexttoward` | `0xBEB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1625 | `_o_nexttowardf` | `0xBEB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1629 | `_o_putc` | `0xBEB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `_o_putchar` | `0xBEB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1631 | `_o_puts` | `0xBEBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1632 | `_o_putwc` | `0xBEBD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1633 | `_o_putwchar` | `0xBEBF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1636 | `_o_raise` | `0xBEC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1640 | `_o_remainder` | `0xBEC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1641 | `_o_remainderf` | `0xBEC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `_o_remainderl` | `0xBEC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1643 | `_o_remove` | `0xBEC90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `_o_remquo` | `0xBECB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1645 | `_o_remquof` | `0xBECD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1646 | `_o_remquol` | `0xBECF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1647 | `_o_rename` | `0xBED10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1649 | `_o_rint` | `0xBED30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1650 | `_o_rintf` | `0xBED50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1651 | `_o_rintl` | `0xBED70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1655 | `_o_scalbln` | `0xBED90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1656 | `_o_scalblnf` | `0xBEDB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1657 | `_o_scalblnl` | `0xBEDD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1658 | `_o_scalbn` | `0xBEDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1660 | `_o_scalbnl` | `0xBEDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1659 | `_o_scalbnf` | `0xBEE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1662 | `_o_setbuf` | `0xBEE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1664 | `_o_setvbuf` | `0xBEE50` | 28 | UnwindData |  |
| 1667 | `_o_sinh` | `0xBEE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `_o_sinhf` | `0xBEEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1673 | `_o_strcoll` | `0xBEEC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1675 | `_o_strerror` | `0xBEEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1676 | `_o_strerror_s` | `0xBEEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1689 | `_o_system` | `0xBEF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1694 | `_o_terminate` | `0xBEF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1695 | `_o_tgamma` | `0xBEF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1696 | `_o_tgammaf` | `0xBEF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1697 | `_o_tgammal` | `0xBEF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1698 | `_o_tmpfile_s` | `0xBEFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1699 | `_o_tmpnam_s` | `0xBEFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1704 | `_o_ungetc` | `0xBEFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1705 | `_o_ungetwc` | `0xBEFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1706 | `_o_wcrtomb` | `0xBF010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1707 | `_o_wcrtomb_s` | `0xBF030` | 39 | UnwindData |  |
| 1709 | `_o_wcscoll` | `0xBF060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1710 | `_o_wcscpy` | `0xBF080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1715 | `_o_wcsrtombs` | `0xBF0A0` | 28 | UnwindData |  |
| 1716 | `_o_wcsrtombs_s` | `0xBF0D0` | 48 | UnwindData |  |
| 1728 | `_o_wctob` | `0xBF110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1729 | `_o_wctomb` | `0xBF130` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `_atodbl_l` | `0xBF2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `_atoflt` | `0xBF2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `_atoflt_l` | `0xBF2E0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `_atoldbl` | `0xBF440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `_atoi64_l` | `0xBF450` | 76 | UnwindData |  |
| 164 | `_atoll_l` | `0xBF450` | 76 | UnwindData |  |
| 160 | `_atoi_l` | `0xBF4B0` | 74 | UnwindData |  |
| 161 | `_atol_l` | `0xBF4B0` | 74 | UnwindData |  |
| 2026 | `_wtoi64_l` | `0xBF500` | 76 | UnwindData |  |
| 2031 | `_wtoll_l` | `0xBF500` | 76 | UnwindData |  |
| 2066 | `c16rtomb` | `0xBF560` | 64 | UnwindData |  |
| 2067 | `c32rtomb` | `0xBF5B0` | 62 | UnwindData |  |
| 454 | `_ismbstrail` | `0xBF700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `_ismbstrail_l` | `0xBF710` | 162 | UnwindData |  |
| 468 | `_iswctype_l` | `0xBF7C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2234 | `is_wctype` | `0xBF7C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `_mblen_l` | `0xBF7D0` | 61 | UnwindData |  |
| 2300 | `mbrtoc16` | `0xBF920` | 67 | UnwindData |  |
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
| 171 | `_c_exit` | `0xC2CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2342 | `quick_exit` | `0xC2CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `_crt_at_quick_exit` | `0xC2CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `_endthread` | `0xC2D10` | 12 | UnwindData |  |
| 263 | `_fgetchar` | `0xC2D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2221 | `getchar` | `0xC2D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `_fputc_nolock` | `0xC2D50` | 60 | UnwindData |  |
| 286 | `_fputchar` | `0xC2DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `_putc_nolock` | `0xC2DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2336 | `putchar` | `0xC2DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `_fputwc_nolock` | `0xC2DE0` | 64 | UnwindData |  |
| 288 | `_fputwchar` | `0xC2E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1745 | `_putwc_nolock` | `0xC2E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2338 | `putwc` | `0xC2E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2339 | `putwchar` | `0xC2E70` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1972 | `_wfreopen` | `0xC2F90` | 47 | UnwindData |  |
| 1973 | `_wfreopen_s` | `0xC2FD0` | 22 | UnwindData |  |
| 2214 | `freopen_s` | `0xC2FF0` | 22 | UnwindData |  |
| 293 | `_fseek_nolock` | `0xC3010` | 60 | UnwindData |  |
| 295 | `_fseeki64_nolock` | `0xC3060` | 60 | UnwindData |  |
| 301 | `_ftell_nolock` | `0xC3240` | 54 | UnwindData |  |
| 303 | `_ftelli64_nolock` | `0xC3280` | 56 | UnwindData |  |
| 359 | `_getws` | `0xC3440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `_getws_s` | `0xC3460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2224 | `gets` | `0xC3470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2225 | `gets_s` | `0xC3490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `_getw` | `0xC34A0` | 170 | UnwindData |  |
| 109 | `__stdio_common_vfprintf_p` | `0xC5850` | 74 | UnwindData |  |
| 113 | `__stdio_common_vfwprintf_p` | `0xC58A0` | 74 | UnwindData |  |
| 1781 | `_set_printf_count_output` | `0xC58F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1744 | `_putw` | `0xC5920` | 152 | UnwindData |  |
| 1748 | `_putws` | `0xC5B20` | 163 | UnwindData |  |
| 349 | `_getmaxstdio` | `0xC5D50` | 37 | UnwindData |  |
| 1786 | `_setmaxstdio` | `0xC5D80` | 87 | UnwindData |  |
| 1858 | `_tempnam` | `0xC62D0` | 14 | UnwindData |  |
| 2019 | `_wtempnam` | `0xC62F0` | 14 | UnwindData |  |
| 2020 | `_wtmpnam` | `0xC6A90` | 38 | UnwindData |  |
| 2021 | `_wtmpnam_s` | `0xC6AC0` | 59 | UnwindData |  |
| 2425 | `tmpfile` | `0xC6B10` | 35 | UnwindData |  |
| 2426 | `tmpfile_s` | `0xC6B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2427 | `tmpnam` | `0xC6B50` | 38 | UnwindData |  |
| 497 | `_lfind` | `0xC6B80` | 155 | UnwindData |  |
| 498 | `_lfind_s` | `0xC6C30` | 159 | UnwindData |  |
| 512 | `_lsearch` | `0xC6CE0` | 216 | UnwindData |  |
| 513 | `_lsearch_s` | `0xC6DC0` | 222 | UnwindData |  |
| 1761 | `_rotl64` | `0xC6EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1763 | `_rotr64` | `0xC6ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1818 | `_stricoll` | `0xC6EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1819 | `_stricoll_l` | `0xC6F10` | 209 | UnwindData |  |
| 1821 | `_strlwr_l` | `0xC6FF0` | 30 | UnwindData |  |
| 1824 | `_strncoll` | `0xC7020` | 79 | UnwindData |  |
| 1825 | `_strncoll_l` | `0xC7080` | 247 | UnwindData |  |
| 1831 | `_strnset_s` | `0xC7180` | 116 | UnwindData |  |
| 1834 | `_strset_s` | `0xC7200` | 73 | UnwindData |  |
| 1851 | `_strupr_l` | `0xC7250` | 30 | UnwindData |  |
| 1911 | `_wcslwr_l` | `0xC7280` | 30 | UnwindData |  |
| 140 | `__wcsncnt` | `0xC72B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1914 | `_wcsncoll` | `0xC72E0` | 79 | UnwindData |  |
| 1921 | `_wcsnset_s` | `0xC7340` | 122 | UnwindData |  |
| 1923 | `_wcsset` | `0xC73C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1941 | `_wcsupr_l` | `0xC73E0` | 30 | UnwindData |  |
| 1944 | `_wcsxfrm_l` | `0xC7410` | 370 | UnwindData |  |
| 2477 | `wcsxfrm` | `0xC7590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `_j0` | `0xC75A0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `_j1` | `0xC77A0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `_jn` | `0xC79D0` | 372 | UnwindData |  |
| 2035 | `_y0` | `0xC7B50` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2069 | `cabsf` | `0xC8040` | 30 | UnwindData |  |
| 2068 | `cabs` | `0xC8070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2070 | `cabsl` | `0xC8070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2071 | `cacos` | `0xC8090` | 828 | UnwindData |  |
| 2076 | `cacosl` | `0xC83E0` | 818 | UnwindData |  |
| 2079 | `cargf` | `0xC8720` | 30 | UnwindData |  |
| 2086 | `casinl` | `0xC8750` | 84 | UnwindData |  |
| 2087 | `catan` | `0xC87B0` | 84 | UnwindData |  |
| 2088 | `catanf` | `0xC8810` | 78 | UnwindData |  |
| 2089 | `catanh` | `0xC8870` | 951 | UnwindData |  |
| 2091 | `catanhl` | `0xC8C30` | 951 | UnwindData |  |
| 2092 | `catanl` | `0xC8FF0` | 84 | UnwindData |  |
| 2096 | `ccos` | `0xC9050` | 66 | UnwindData |  |
| 2097 | `ccosf` | `0xC90A0` | 45 | UnwindData |  |
| 2098 | `ccosh` | `0xC90E0` | 574 | UnwindData |  |
| 2099 | `ccoshf` | `0xC9330` | 502 | UnwindData |  |
| 2100 | `ccoshl` | `0xC9530` | 574 | UnwindData |  |
| 2101 | `ccosl` | `0xC9780` | 66 | UnwindData |  |
| 2105 | `cexpf` | `0xC97D0` | 538 | UnwindData |  |
| 2114 | `clog10` | `0xC99F0` | 56 | UnwindData |  |
| 2115 | `clog10f` | `0xC9A30` | 55 | UnwindData |  |
| 2116 | `clog10l` | `0xC9A70` | 56 | UnwindData |  |
| 2117 | `clogf` | `0xC9AB0` | 710 | UnwindData |  |
| 3 | `_Cmulcr` | `0xC9D80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `_LCmulcr` | `0xC9D80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `_FCmulcr` | `0xC9DB0` | 40 | UnwindData |  |
| 2130 | `cpowf` | `0xC9DE0` | 169 | UnwindData |  |
| 2131 | `cpowl` | `0xC9E90` | 196 | UnwindData |  |
| 2132 | `cproj` | `0xC9F60` | 300 | UnwindData |  |
| 2134 | `cprojl` | `0xC9F60` | 300 | UnwindData |  |
| 2133 | `cprojf` | `0xCA0A0` | 230 | UnwindData |  |
| 2138 | `csin` | `0xCA190` | 84 | UnwindData |  |
| 2139 | `csinf` | `0xCA1F0` | 78 | UnwindData |  |
| 2143 | `csinl` | `0xCA250` | 84 | UnwindData |  |
| 2147 | `ctan` | `0xCA2B0` | 84 | UnwindData |  |
| 2152 | `ctanl` | `0xCA2B0` | 84 | UnwindData |  |
| 2148 | `ctanf` | `0xCA310` | 78 | UnwindData |  |
| 2149 | `ctanh` | `0xCA370` | 570 | UnwindData |  |
| 2151 | `ctanhl` | `0xCA370` | 570 | UnwindData |  |
| 2150 | `ctanhf` | `0xCA5B0` | 463 | UnwindData |  |
| 2154 | `erf` | `0xCA790` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2155 | `erfc` | `0xCA940` | 1,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2156 | `erfcf` | `0xCAEB0` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2157 | `erfcl` | `0xCB190` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2158 | `erff` | `0xCB360` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2159 | `erfl` | `0xCB510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `_ldexp` | `0xCB530` | 1,122 | UnwindData |  |
| 314 | `_get_FMA3_enable` | `0xCC3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1770 | `_set_FMA3_enable` | `0xCC410` | 7,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2195 | `fmal` | `0xCE0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `_dsin` | `0xCE100` | 401 | UnwindData |  |
| 2265 | `lgamma` | `0xCE330` | 2,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2266 | `lgammaf` | `0xCEE40` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `_ldsin` | `0xCF4D0` | 401 | UnwindData |  |
| 2267 | `lgammal` | `0xCF950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2272 | `llrintl` | `0xCF970` | 106 | UnwindData |  |
| 2274 | `llroundf` | `0xCF9E0` | 84 | UnwindData |  |
| 2293 | `lrintl` | `0xCFA40` | 105 | UnwindData |  |
| 100 | `__setusermatherr` | `0xCFAB0` | 56 | UnwindData |  |
| 2329 | `norm` | `0xCFBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2331 | `norml` | `0xCFBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2330 | `normf` | `0xCFBC0` | 36 | UnwindData |  |
| 2349 | `remainderl` | `0xCFBF0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2422 | `tgamma` | `0xCFC90` | 2,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2423 | `tgammaf` | `0xD0570` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2424 | `tgammal` | `0xD0A20` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `_cgets` | `0xD0B10` | 115 | UnwindData |  |
| 177 | `_cgets_s` | `0xD0B90` | 272 | UnwindData |  |
| 178 | `_cgetws` | `0xD0CB0` | 116 | UnwindData |  |
| 179 | `_cgetws_s` | `0xD0D30` | 420 | UnwindData |  |
| 57 | `__conio_common_vcprintf` | `0xD39B0` | 61 | UnwindData |  |
| 58 | `__conio_common_vcprintf_p` | `0xD3A00` | 61 | UnwindData |  |
| 59 | `__conio_common_vcprintf_s` | `0xD3A50` | 61 | UnwindData |  |
| 61 | `__conio_common_vcwprintf` | `0xD3AA0` | 61 | UnwindData |  |
| 62 | `__conio_common_vcwprintf_p` | `0xD3AF0` | 61 | UnwindData |  |
| 63 | `__conio_common_vcwprintf_s` | `0xD3B40` | 61 | UnwindData |  |
| 198 | `_cputs` | `0xD3B90` | 120 | UnwindData |  |
| 60 | `__conio_common_vcscanf` | `0xD6730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `__conio_common_vcwscanf` | `0xD6740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `_getch` | `0xD6750` | 48 | UnwindData |  |
| 340 | `_getch_nolock` | `0xD6790` | 365 | UnwindData |  |
| 341 | `_getche` | `0xD6910` | 48 | UnwindData |  |
| 1881 | `_ungetch` | `0xD6A20` | 52 | UnwindData |  |
| 1882 | `_ungetch_nolock` | `0xD6A60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `_getwch` | `0xD6AA0` | 50 | UnwindData |  |
| 356 | `_getwch_nolock` | `0xD6AE0` | 229 | UnwindData |  |
| 357 | `_getwche` | `0xD6BD0` | 50 | UnwindData |  |
| 1884 | `_ungetwch` | `0xD6C10` | 56 | UnwindData |  |
| 1885 | `_ungetwch_nolock` | `0xD6C50` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `_popen` | `0xD7140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1987 | `_wpopen` | `0xD7150` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1740 | `_putch` | `0xD71D0` | 54 | UnwindData |  |
| 1741 | `_putch_nolock` | `0xD7210` | 54 | UnwindData |  |
| 1746 | `_putwch` | `0xD72C0` | 55 | UnwindData |  |
| 270 | `_findfirst32` | `0xD7C00` | 45 | UnwindData |  |
| 271 | `_findfirst32i64` | `0xD7C40` | 45 | UnwindData |  |
| 274 | `_findnext32` | `0xD7C80` | 45 | UnwindData |  |
| 275 | `_findnext32i64` | `0xD7CC0` | 45 | UnwindData |  |
| 276 | `_findnext64` | `0xD7D00` | 45 | UnwindData |  |
| 1962 | `_wfindfirst32` | `0xD7D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1963 | `_wfindfirst32i64` | `0xD7D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1964 | `_wfindfirst64` | `0xD7D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1966 | `_wfindnext32` | `0xD7D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1967 | `_wfindnext32i64` | `0xD7D80` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `_fstat32` | `0xD8430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1804 | `_stat32` | `0xD8440` | 143 | UnwindData |  |
| 1805 | `_stat32i64` | `0xD84E0` | 143 | UnwindData |  |
| 2010 | `_wstat32` | `0xD8580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2011 | `_wstat32i64` | `0xD8590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `_chsize` | `0xD85A0` | 21 | UnwindData |  |
| 186 | `_chsize_s` | `0xD85C0` | 60 | UnwindData |  |
| 200 | `_creat` | `0xD8610` | 63 | UnwindData |  |
| 1899 | `_wcreat` | `0xD8660` | 63 | UnwindData |  |
| 230 | `_eof` | `0xD87E0` | 156 | UnwindData |  |
| 266 | `_filelength` | `0xD89B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `_filelengthi64` | `0xD89C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 666 | `_mktemp_s` | `0xD8A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1983 | `_wmktemp` | `0xD8A20` | 82 | UnwindData |  |
| 1984 | `_wmktemp_s` | `0xD8A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1791 | `_sopen` | `0xD8A90` | 68 | UnwindData |  |
| 204 | `_ctime32` | `0xD8DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `_ctime32_s` | `0xD8DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1945 | `_wctime32` | `0xD8DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1946 | `_wctime32_s` | `0xD8DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1947 | `_wctime64` | `0xD8E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 663 | `_mkgmtime32` | `0xD8E10` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1810 | `_strdate` | `0xD8F50` | 36 | UnwindData |  |
| 1811 | `_strdate_s` | `0xD8F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2014 | `_wstrdate` | `0xD8F90` | 36 | UnwindData |  |
| 1835 | `_strtime` | `0xD90D0` | 36 | UnwindData |  |
| 1836 | `_strtime_s` | `0xD9100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2016 | `_wstrtime` | `0xD9110` | 36 | UnwindData |  |
| 1861 | `_timespec32_get` | `0xD91E0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `_futime32` | `0xD9430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1890 | `_utime32` | `0xD9440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2033 | `_wutime32` | `0xD9450` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1905 | `_wcsftime_l` | `0xD94D0` | 30 | UnwindData |  |
| 1766 | `_searchenv` | `0xD96B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1767 | `_searchenv_s` | `0xD96D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1995 | `_wsearchenv_s` | `0xD96E0` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `_getdllprocaddr` | `0xD9BF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `_loaddll` | `0xD9C20` | 109 | UnwindData |  |
| 1887 | `_unloaddll` | `0xD9CA0` | 32 | UnwindData |  |
| 233 | `_execl` | `0xD9EE0` | 50 | UnwindData |  |
| 234 | `_execle` | `0xD9F20` | 50 | UnwindData |  |
| 1794 | `_spawnl` | `0xD9F60` | 43 | UnwindData |  |
| 1795 | `_spawnle` | `0xD9FA0` | 43 | UnwindData |  |
| 1953 | `_wexecl` | `0xD9FE0` | 50 | UnwindData |  |
| 1954 | `_wexecle` | `0xDA020` | 50 | UnwindData |  |
| 2000 | `_wspawnl` | `0xDA060` | 43 | UnwindData |  |
| 2001 | `_wspawnle` | `0xDA0A0` | 43 | UnwindData |  |
| 235 | `_execlp` | `0xDA1E0` | 50 | UnwindData |  |
| 236 | `_execlpe` | `0xDA220` | 50 | UnwindData |  |
| 1796 | `_spawnlp` | `0xDA260` | 43 | UnwindData |  |
| 1797 | `_spawnlpe` | `0xDA2A0` | 43 | UnwindData |  |
| 1955 | `_wexeclp` | `0xDA2E0` | 50 | UnwindData |  |
| 1956 | `_wexeclpe` | `0xDA320` | 50 | UnwindData |  |
| 2002 | `_wspawnlp` | `0xDA360` | 43 | UnwindData |  |
| 2003 | `_wspawnlpe` | `0xDA3A0` | 43 | UnwindData |  |
| 238 | `_execv` | `0xDA6E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `_execve` | `0xDA700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1798 | `_spawnv` | `0xDA720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1799 | `_spawnve` | `0xDA730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1957 | `_wexecv` | `0xDA740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1958 | `_wexecve` | `0xDA760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2004 | `_wspawnv` | `0xDA780` | 1,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `_execvp` | `0xDAF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `_execvpe` | `0xDAF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1800 | `_spawnvp` | `0xDAF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1801 | `_spawnvpe` | `0xDAF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1959 | `_wexecvp` | `0xDAFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1960 | `_wexecvpe` | `0xDAFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2006 | `_wspawnvp` | `0xDAFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2007 | `_wspawnvpe` | `0xDAFF0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2018 | `_wsystem` | `0xDB150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2416 | `system` | `0xDB160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `_heapchk` | `0xDB170` | 37 | UnwindData |  |
| 366 | `_heapmin` | `0xDB1A0` | 33 | UnwindData |  |
| 418 | `_ismbcalnum` | `0xDB1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `_ismbcalnum_l` | `0xDB1E0` | 129 | UnwindData |  |
| 394 | `_ismbbalnum` | `0xDB270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `_ismbbalnum_l` | `0xDB290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `_ismbbalpha` | `0xDB2B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `_ismbbalpha_l` | `0xDB2D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `_ismbbblank` | `0xDB2F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `_ismbbblank_l` | `0xDB320` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `_ismbbgraph` | `0xDB350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `_ismbbgraph_l` | `0xDB370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `_ismbbkalnum` | `0xDB390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `_ismbbkalnum_l` | `0xDB3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `_ismbbkana` | `0xDB3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `_ismbbkana_l` | `0xDB3E0` | 116 | UnwindData |  |
| 406 | `_ismbbkprint` | `0xDB460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `_ismbbkprint_l` | `0xDB480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `_ismbbkpunct` | `0xDB4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `_ismbbkpunct_l` | `0xDB4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `_ismbblead_l` | `0xDB4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `_ismbbprint` | `0xDB500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `_ismbbprint_l` | `0xDB520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `_ismbbpunct` | `0xDB540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `_ismbbpunct_l` | `0xDB560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `_ismbbtrail` | `0xDB580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `_ismbbtrail_l` | `0xDB5A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `_ismbcgraph` | `0xDB5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `_ismbcgraph_l` | `0xDB5D0` | 137 | UnwindData |  |
| 428 | `_ismbchira` | `0xDB660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `_ismbchira_l` | `0xDB670` | 77 | UnwindData |  |
| 430 | `_ismbckata` | `0xDB6D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `_ismbckata_l` | `0xDB6E0` | 85 | UnwindData |  |
| 448 | `_ismbcsymbol` | `0xDB740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `_ismbcsymbol_l` | `0xDB750` | 85 | UnwindData |  |
| 438 | `_ismbclegal` | `0xDB7B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `_ismbclegal_l` | `0xDB7C0` | 80 | UnwindData |  |
| 442 | `_ismbcprint` | `0xDB820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `_ismbcprint_l` | `0xDB830` | 114 | UnwindData |  |
| 422 | `_ismbcblank` | `0xDB8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `_ismbcblank_l` | `0xDB8C0` | 145 | UnwindData |  |
| 444 | `_ismbcpunct` | `0xDB960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `_ismbcpunct_l` | `0xDB970` | 134 | UnwindData |  |
| 452 | `_ismbslead` | `0xDBA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `_ismbslead_l` | `0xDBA10` | 165 | UnwindData |  |
| 450 | `_ismbcupper` | `0xDBAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `_ismbcupper_l` | `0xDBAD0` | 93 | UnwindData |  |
| 525 | `_mbbtype` | `0xDBB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | `_mbbtype_l` | `0xDBB50` | 231 | UnwindData |  |
| 529 | `_mbccpy_l` | `0xDBC40` | 29 | UnwindData |  |
| 537 | `_mbclen_l` | `0xDBC70` | 58 | UnwindData |  |
| 432 | `_ismbcl0` | `0xDBCB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `_ismbcl0_l` | `0xDBCC0` | 97 | UnwindData |  |
| 434 | `_ismbcl1` | `0xDBD30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `_ismbcl1_l` | `0xDBD40` | 102 | UnwindData |  |
| 436 | `_ismbcl2` | `0xDBDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `_ismbcl2_l` | `0xDBDC0` | 102 | UnwindData |  |
| 550 | `_mbsbtype_l` | `0xDBE30` | 234 | UnwindData |  |
| 551 | `_mbscat_s` | `0xDBF20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `_mbscoll` | `0xDBF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `_mbscoll_l` | `0xDBF40` | 227 | UnwindData |  |
| 559 | `_mbscpy_s` | `0xDC030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `_mbscpy_s_l` | `0xDC040` | 461 | UnwindData |  |
| 568 | `_mbsicoll` | `0xDC220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `_mbsicoll_l` | `0xDC230` | 227 | UnwindData |  |
| 571 | `_mbsinc_l` | `0xDC320` | 54 | UnwindData |  |
| 622 | `_mbsnlen` | `0xDC360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 623 | `_mbsnlen_l` | `0xDC370` | 477 | UnwindData |  |
| 575 | `_mbslwr_l` | `0xDC560` | 43 | UnwindData |  |
| 578 | `_mbsnbcat` | `0xDC5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `_mbsnbcat_l` | `0xDC5B0` | 362 | UnwindData |  |
| 584 | `_mbsnbcnt` | `0xDC720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 585 | `_mbsnbcnt_l` | `0xDC730` | 165 | UnwindData |  |
| 586 | `_mbsnbcoll` | `0xDC7E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 587 | `_mbsnbcoll_l` | `0xDC7F0` | 265 | UnwindData |  |
| 594 | `_mbsnbicoll` | `0xDC900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 595 | `_mbsnbicoll_l` | `0xDC910` | 280 | UnwindData |  |
| 596 | `_mbsnbset` | `0xDCA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `_mbsnbset_l` | `0xDCA40` | 283 | UnwindData |  |
| 598 | `_mbsnbset_s` | `0xDCB70` | 20 | UnwindData |  |
| 599 | `_mbsnbset_s_l` | `0xDCB90` | 768 | UnwindData |  |
| 600 | `_mbsncat` | `0xDCEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `_mbsncat_l` | `0xDCEB0` | 340 | UnwindData |  |
| 602 | `_mbsncat_s` | `0xDD010` | 20 | UnwindData |  |
| 604 | `_mbsnccnt` | `0xDD030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `_mbsnccnt_l` | `0xDD040` | 171 | UnwindData |  |
| 606 | `_mbsncmp` | `0xDD100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `_mbsncoll` | `0xDD110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `_mbsncoll_l` | `0xDD120` | 332 | UnwindData |  |
| 610 | `_mbsncpy` | `0xDD280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `_mbsncpy_l` | `0xDD290` | 266 | UnwindData |  |
| 612 | `_mbsncpy_s` | `0xDD3A0` | 20 | UnwindData |  |
| 613 | `_mbsncpy_s_l` | `0xDD3C0` | 613 | UnwindData |  |
| 616 | `_mbsnicmp` | `0xDD630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 618 | `_mbsnicoll` | `0xDD640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `_mbsnicoll_l` | `0xDD650` | 332 | UnwindData |  |
| 620 | `_mbsninc` | `0xDD7B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 621 | `_mbsninc_l` | `0xDD7C0` | 34 | UnwindData |  |
| 624 | `_mbsnset` | `0xDD7F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `_mbsnset_l` | `0xDD800` | 386 | UnwindData |  |
| 626 | `_mbsnset_s` | `0xDD990` | 20 | UnwindData |  |
| 627 | `_mbsnset_s_l` | `0xDD9B0` | 748 | UnwindData |  |
| 634 | `_mbsset` | `0xDDCB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 635 | `_mbsset_l` | `0xDDCC0` | 259 | UnwindData |  |
| 636 | `_mbsset_s` | `0xDDDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 637 | `_mbsset_s_l` | `0xDDDE0` | 470 | UnwindData |  |
| 644 | `_mbstok` | `0xDDFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `_mbstok_l` | `0xDDFD0` | 62 | UnwindData |  |
| 654 | `_mbsupr` | `0xDE020` | 43 | UnwindData |  |
| 655 | `_mbsupr_l` | `0xDE060` | 43 | UnwindData |  |
| 538 | `_mbctohira` | `0xDE0A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `_mbctohira_l` | `0xDE0B0` | 55 | UnwindData |  |
| 540 | `_mbctokata` | `0xDE0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `_mbctokata_l` | `0xDE100` | 41 | UnwindData |  |
| 546 | `_mbctoupper` | `0xDE130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `_mbctoupper_l` | `0xDE140` | 232 | UnwindData |  |
| 532 | `_mbcjistojms` | `0xDE230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 533 | `_mbcjistojms_l` | `0xDE240` | 213 | UnwindData |  |
| 534 | `_mbcjmstojis` | `0xDE320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `_mbcjmstojis_l` | `0xDE330` | 237 | UnwindData |  |
| 523 | `_mbbtombc` | `0xDE430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `_mbbtombc_l` | `0xDE440` | 185 | UnwindData |  |
| 544 | `_mbctombb` | `0xDE500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `_mbctombb_l` | `0xDE510` | 221 | UnwindData |  |
| 180 | `_chdir` | `0xDE890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `_getdrives` | `0xDE8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `_getdcwd` | `0xDE8B0` | 14 | UnwindData |  |
| 1757 | `_resetstkoflw` | `0xDE8D0` | 397 | UnwindData |  |
| 1785 | `_seterrormode` | `0xDEA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `_beep` | `0xDEA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `_getsystime` | `0xDEA90` | 168 | UnwindData |  |
| 1789 | `_setsystime` | `0xDEB40` | 179 | UnwindData |  |
| 172 | `_cabs` | `0xDEC00` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2128 | `coshf` | `0xDED50` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `_logbf` | `0xDF120` | 194 | UnwindData |  |
| 182 | `_chgsign` | `0xDF560` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `_chgsignf` | `0xDF590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `_copysignf` | `0xDF5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `_finitef` | `0xDF5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1830 | `_strnset` | `0xDF5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1832 | `_strrev` | `0xDF610` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1833 | `_strset` | `0xDF650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `_fpieee_flt` | `0xDF670` | 11,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `_fpclassf` | `0xE2410` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `_isnanf` | `0xE2480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1764 | `_scalb` | `0xE24A0` | 434 | UnwindData |  |
| 1765 | `_scalbf` | `0xE2660` | 386 | UnwindData |  |
| 211 | `_dexp` | `0xE7850` | 1,122 | UnwindData |  |
| 250 | `_fdexp` | `0xE7CC0` | 982 | UnwindData |  |
| 385 | `_isatty` | `0xECF90` | 18 | UnwindData |  |
| 75 | `__intrinsic_setjmp` | `0xECFC0` | 144 | UnwindData |  |
| 2371 | `setjmp` | `0xED060` | 5 | UnwindData |  |
| 76 | `__intrinsic_setjmpex` | `0xED080` | 144 | UnwindData |  |
| 2382 | `strcat` | `0xED290` | 144 | UnwindData |  |
| 2387 | `strcpy` | `0xED330` | 183 | UnwindData |  |
| 2385 | `strcmp` | `0xED400` | 103 | UnwindData |  |
| 2393 | `strlen` | `0xED480` | 168 | UnwindData |  |
| 2394 | `strncat` | `0xED540` | 405 | UnwindData |  |
| 2396 | `strncmp` | `0xED6F0` | 125 | UnwindData |  |
| 2397 | `strncpy` | `0xED780` | 354 | UnwindData |  |
| 1612 | `_o_memset` | `0xED920` | 904 | UnwindData |  |
| 2314 | `memset` | `0xED920` | 904 | UnwindData |  |
| 2308 | `memchr` | `0xEDCC0` | 144 | UnwindData |  |
| 2309 | `memcmp` | `0xEDD60` | 199 | UnwindData |  |
| 2310 | `memcpy` | `0xEDE60` | 1,645 | UnwindData |  |
| 2312 | `memmove` | `0xEDE60` | 1,645 | UnwindData |  |
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
| 2436 | `truncl` | `0xF70E0` | 36,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1951 | `_wctype` | `0xFFEB0` | 227,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `_mbcasemap` | `0x1377F0` | 2,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `__dcrt_initial_narrow_environment` | `0x1382B0` | 0 | Indeterminate |  |
