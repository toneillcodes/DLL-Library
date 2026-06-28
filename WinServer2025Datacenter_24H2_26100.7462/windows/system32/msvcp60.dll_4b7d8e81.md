# Binary Specification: msvcp60.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msvcp60.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4b7d8e819274e42f4fd61a8f06ed6c8b5aaf9154a1881e2012da5a3200118b96`
* **Total Exported Functions:** 2422

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2413 | `btowc` | `0x0` | - | Forwarded | Forwarded to: `msvcrt.btowc` |
| 2414 | `mbrlen` | `0x0` | - | Forwarded | Forwarded to: `msvcrt.mbrlen` |
| 2415 | `mbrtowc` | `0x0` | - | Forwarded | Forwarded to: `msvcrt.mbrtowc` |
| 2416 | `mbsrtowcs` | `0x0` | - | Forwarded | Forwarded to: `msvcrt.mbsrtowcs` |
| 2418 | `wcrtomb` | `0x0` | - | Forwarded | Forwarded to: `msvcrt.wcrtomb` |
| 2419 | `wcsrtombs` | `0x0` | - | Forwarded | Forwarded to: `msvcrt.wcsrtombs` |
| 2420 | `wctob` | `0x0` | - | Forwarded | Forwarded to: `msvcrt.wctob` |
| 2380 | `_Getctype` | `0x1350` | 190 | UnwindData |  |
| 2408 | `_Tolower` | `0x1420` | 271 | UnwindData |  |
| 2409 | `_Toupper` | `0x1540` | 271 | UnwindData |  |
| 2417 | `towctrans` | `0x1660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2421 | `wctrans` | `0x1680` | 117 | UnwindData |  |
| 2422 | `wctype` | `0x1700` | 117 | UnwindData |  |
| 2359 | `_Cosh` | `0x1780` | 290 | UnwindData |  |
| 2361 | `_Dnorm` | `0x18B0` | 385 | UnwindData |  |
| 2362 | `_Dscale` | `0x1A40` | 489 | UnwindData |  |
| 2363 | `_Dtest` | `0x1C30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2365 | `_Exp` | `0x1CA0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2366 | `_FCosh` | `0x1DD0` | 300 | UnwindData |  |
| 2368 | `_FDnorm` | `0x1F10` | 220 | UnwindData |  |
| 2369 | `_FDscale` | `0x2000` | 360 | UnwindData |  |
| 2370 | `_FDtest` | `0x2170` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2372 | `_FExp` | `0x21C0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2376 | `_FSinh` | `0x22E0` | 409 | UnwindData |  |
| 2384 | `_LCosh` | `0x2480` | 271 | UnwindData |  |
| 2386 | `_LDscale` | `0x25A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2387 | `_LDtest` | `0x25B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2389 | `_LExp` | `0x25C0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2392 | `_LPoly` | `0x2700` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2394 | `_LSinh` | `0x2730` | 379 | UnwindData |  |
| 2397 | `_Mbrtowc` | `0x28C0` | 424 | UnwindData |  |
| 2399 | `_Poly` | `0x2A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2401 | `_Sinh` | `0x2AA0` | 379 | UnwindData |  |
| 2403 | `_Stod` | `0x2C30` | 57 | UnwindData |  |
| 2404 | `_Stof` | `0x2C70` | 18 | UnwindData |  |
| 2405 | `_Stold` | `0x2C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2379 | `_Getcoll` | `0x2CA0` | 37 | UnwindData |  |
| 2406 | `_Strcoll` | `0x2CD0` | 199 | UnwindData |  |
| 2407 | `_Strxfrm` | `0x2DA0` | 256 | UnwindData |  |
| 2381 | `_Getcvt` | `0x2EB0` | 37 | UnwindData |  |
| 2410 | `_Wcrtomb` | `0x2EE0` | 177 | UnwindData |  |
| 2412 | `__Wcrtomb_lk` | `0x2FA0` | 6,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `??0?$_Mpunct@D@std@@QEAA@AEBV_Locinfo@1@_K_N@Z` | `0x4A90` | 55 | UnwindData |  |
| 291 | `??0?$_Mpunct@D@std@@QEAA@_K_N@Z` | `0x4AD0` | 96 | UnwindData |  |
| 292 | `??0?$_Mpunct@G@std@@QEAA@AEBV_Locinfo@1@_K_N@Z` | `0x4B40` | 55 | UnwindData |  |
| 293 | `??0?$_Mpunct@G@std@@QEAA@_K_N@Z` | `0x4B80` | 96 | UnwindData |  |
| 294 | `??0?$basic_filebuf@DU?$char_traits@D@std@@@std@@QEAA@AEBV01@@Z` | `0x4BF0` | 171 | UnwindData |  |
| 295 | `??0?$basic_filebuf@DU?$char_traits@D@std@@@std@@QEAA@PEAU_iobuf@@@Z` | `0x4CB0` | 71 | UnwindData |  |
| 296 | `??0?$basic_filebuf@DU?$char_traits@D@std@@@std@@QEAA@W4_Uninitialized@1@@Z` | `0x4D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `??0?$basic_filebuf@GU?$char_traits@G@std@@@std@@QEAA@AEBV01@@Z` | `0x4D20` | 171 | UnwindData |  |
| 298 | `??0?$basic_filebuf@GU?$char_traits@G@std@@@std@@QEAA@PEAU_iobuf@@@Z` | `0x4DE0` | 71 | UnwindData |  |
| 299 | `??0?$basic_filebuf@GU?$char_traits@G@std@@@std@@QEAA@W4_Uninitialized@1@@Z` | `0x4E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `??0?$basic_fstream@DU?$char_traits@D@std@@@std@@QEAA@AEBV01@@Z` | `0x4E50` | 190 | UnwindData |  |
| 301 | `??0?$basic_fstream@DU?$char_traits@D@std@@@std@@QEAA@PEBDH@Z` | `0x4F20` | 323 | UnwindData |  |
| 302 | `??0?$basic_fstream@DU?$char_traits@D@std@@@std@@QEAA@XZ` | `0x5070` | 219 | UnwindData |  |
| 303 | `??0?$basic_fstream@GU?$char_traits@G@std@@@std@@QEAA@AEBV01@@Z` | `0x5160` | 190 | UnwindData |  |
| 304 | `??0?$basic_fstream@GU?$char_traits@G@std@@@std@@QEAA@PEBDH@Z` | `0x5230` | 323 | UnwindData |  |
| 305 | `??0?$basic_fstream@GU?$char_traits@G@std@@@std@@QEAA@XZ` | `0x5380` | 219 | UnwindData |  |
| 306 | `??0?$basic_ifstream@DU?$char_traits@D@std@@@std@@QEAA@AEBV01@@Z` | `0x5470` | 141 | UnwindData |  |
| 307 | `??0?$basic_ifstream@DU?$char_traits@D@std@@@std@@QEAA@PEBDH@Z` | `0x5510` | 277 | UnwindData |  |
| 308 | `??0?$basic_ifstream@DU?$char_traits@D@std@@@std@@QEAA@XZ` | `0x5630` | 169 | UnwindData |  |
| 309 | `??0?$basic_ifstream@GU?$char_traits@G@std@@@std@@QEAA@AEBV01@@Z` | `0x56E0` | 141 | UnwindData |  |
| 310 | `??0?$basic_ifstream@GU?$char_traits@G@std@@@std@@QEAA@PEBDH@Z` | `0x5780` | 277 | UnwindData |  |
| 311 | `??0?$basic_ifstream@GU?$char_traits@G@std@@@std@@QEAA@XZ` | `0x58A0` | 169 | UnwindData |  |
| 312 | `??0?$basic_ios@DU?$char_traits@D@std@@@std@@IEAA@XZ` | `0x5950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `??0?$basic_ios@DU?$char_traits@D@std@@@std@@QEAA@AEBV01@@Z` | `0x5970` | 146 | UnwindData |  |
| 314 | `??0?$basic_ios@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@@Z` | `0x5A10` | 89 | UnwindData |  |
| 315 | `??0?$basic_ios@GU?$char_traits@G@std@@@std@@IEAA@XZ` | `0x5A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `??0?$basic_ios@GU?$char_traits@G@std@@@std@@QEAA@AEBV01@@Z` | `0x5A90` | 162 | UnwindData |  |
| 317 | `??0?$basic_ios@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@@Z` | `0x5B40` | 103 | UnwindData |  |
| 318 | `??0?$basic_iostream@DU?$char_traits@D@std@@@std@@QEAA@AEBV01@@Z` | `0x5BB0` | 155 | UnwindData |  |
| 319 | `??0?$basic_iostream@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@@Z` | `0x5C60` | 136 | UnwindData |  |
| 320 | `??0?$basic_iostream@GU?$char_traits@G@std@@@std@@QEAA@AEBV01@@Z` | `0x5CF0` | 155 | UnwindData |  |
| 321 | `??0?$basic_iostream@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@@Z` | `0x5DA0` | 136 | UnwindData |  |
| 322 | `??0?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA@AEBV01@@Z` | `0x5E30` | 90 | UnwindData |  |
| 323 | `??0?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@_N@Z` | `0x5E90` | 188 | UnwindData |  |
| 324 | `??0?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA@W4_Uninitialized@1@@Z` | `0x5F60` | 109 | UnwindData |  |
| 325 | `??0?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA@AEBV01@@Z` | `0x5FE0` | 90 | UnwindData |  |
| 326 | `??0?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@_N@Z` | `0x6040` | 199 | UnwindData |  |
| 327 | `??0?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA@W4_Uninitialized@1@@Z` | `0x6110` | 109 | UnwindData |  |
| 334 | `??0?$basic_ofstream@DU?$char_traits@D@std@@@std@@QEAA@AEBV01@@Z` | `0x6190` | 133 | UnwindData |  |
| 335 | `??0?$basic_ofstream@DU?$char_traits@D@std@@@std@@QEAA@PEBDH@Z` | `0x6220` | 282 | UnwindData |  |
| 336 | `??0?$basic_ofstream@DU?$char_traits@D@std@@@std@@QEAA@XZ` | `0x6340` | 176 | UnwindData |  |
| 337 | `??0?$basic_ofstream@GU?$char_traits@G@std@@@std@@QEAA@AEBV01@@Z` | `0x6400` | 133 | UnwindData |  |
| 338 | `??0?$basic_ofstream@GU?$char_traits@G@std@@@std@@QEAA@PEBDH@Z` | `0x6490` | 282 | UnwindData |  |
| 339 | `??0?$basic_ofstream@GU?$char_traits@G@std@@@std@@QEAA@XZ` | `0x65B0` | 176 | UnwindData |  |
| 340 | `??0?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA@AEBV01@@Z` | `0x6670` | 73 | UnwindData |  |
| 341 | `??0?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@_N1@Z` | `0x66C0` | 190 | UnwindData |  |
| 342 | `??0?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA@W4_Uninitialized@1@@Z` | `0x6790` | 109 | UnwindData |  |
| 343 | `??0?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA@AEBV01@@Z` | `0x6810` | 73 | UnwindData |  |
| 344 | `??0?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@_N1@Z` | `0x6860` | 201 | UnwindData |  |
| 345 | `??0?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA@W4_Uninitialized@1@@Z` | `0x6930` | 109 | UnwindData |  |
| 352 | `??0?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAA@W4_Uninitialized@1@@Z` | `0x69B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `??0?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAA@XZ` | `0x69D0` | 106 | UnwindData |  |
| 354 | `??0?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA@AEBV01@@Z` | `0x6A40` | 185 | UnwindData |  |
| 355 | `??0?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAA@W4_Uninitialized@1@@Z` | `0x6B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `??0?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAA@XZ` | `0x6B20` | 106 | UnwindData |  |
| 357 | `??0?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA@AEBV01@@Z` | `0x6B90` | 185 | UnwindData |  |
| 358 | `??0?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@AEBV01@@Z` | `0x6C50` | 44 | UnwindData |  |
| 359 | `??0?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@AEBV01@_K1AEBV?$allocator@D@1@@Z` | `0x6C90` | 37 | UnwindData |  |
| 360 | `??0?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@AEBV?$allocator@D@1@@Z` | `0x6CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `??0?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@PEBD0AEBV?$allocator@D@1@@Z` | `0x6CE0` | 37 | UnwindData |  |
| 362 | `??0?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@PEBDAEBV?$allocator@D@1@@Z` | `0x6D10` | 110 | UnwindData |  |
| 363 | `??0?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@PEBD_KAEBV?$allocator@D@1@@Z` | `0x6D90` | 100 | UnwindData |  |
| 364 | `??0?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@_KDAEBV?$allocator@D@1@@Z` | `0x6E00` | 114 | UnwindData |  |
| 365 | `??0?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@AEBV01@@Z` | `0x6E80` | 44 | UnwindData |  |
| 366 | `??0?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@AEBV01@_K1AEBV?$allocator@G@1@@Z` | `0x6EC0` | 37 | UnwindData |  |
| 367 | `??0?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@AEBV?$allocator@G@1@@Z` | `0x6EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `??0?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@PEBG0AEBV?$allocator@G@1@@Z` | `0x6F10` | 37 | UnwindData |  |
| 369 | `??0?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@PEBGAEBV?$allocator@G@1@@Z` | `0x6F40` | 51 | UnwindData |  |
| 370 | `??0?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@PEBG_KAEBV?$allocator@G@1@@Z` | `0x6F80` | 37 | UnwindData |  |
| 371 | `??0?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@_KGAEBV?$allocator@G@1@@Z` | `0x6FB0` | 37 | UnwindData |  |
| 384 | `??0?$codecvt@DDH@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x6FE0` | 41 | UnwindData |  |
| 385 | `??0?$codecvt@DDH@std@@QEAA@_K@Z` | `0x7010` | 88 | UnwindData |  |
| 386 | `??0?$codecvt@GDH@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7070` | 41 | UnwindData |  |
| 387 | `??0?$codecvt@GDH@std@@QEAA@_K@Z` | `0x70A0` | 88 | UnwindData |  |
| 388 | `??0?$collate@D@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7100` | 41 | UnwindData |  |
| 389 | `??0?$collate@D@std@@QEAA@_K@Z` | `0x7130` | 88 | UnwindData |  |
| 390 | `??0?$collate@G@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7190` | 41 | UnwindData |  |
| 391 | `??0?$collate@G@std@@QEAA@_K@Z` | `0x71C0` | 88 | UnwindData |  |
| 401 | `??0?$ctype@D@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7220` | 130 | UnwindData |  |
| 402 | `??0?$ctype@D@std@@QEAA@PEBF_N_K@Z` | `0x72B0` | 252 | UnwindData |  |
| 403 | `??0?$ctype@G@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x73C0` | 59 | UnwindData |  |
| 404 | `??0?$ctype@G@std@@QEAA@_K@Z` | `0x7410` | 106 | UnwindData |  |
| 405 | `??0?$messages@D@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7480` | 51 | UnwindData |  |
| 406 | `??0?$messages@D@std@@QEAA@_K@Z` | `0x74C0` | 92 | UnwindData |  |
| 407 | `??0?$messages@G@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7530` | 81 | UnwindData |  |
| 408 | `??0?$messages@G@std@@QEAA@_K@Z` | `0x7590` | 116 | UnwindData |  |
| 409 | `??0?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `??0?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x7630` | 79 | UnwindData |  |
| 411 | `??0?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `??0?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x76B0` | 79 | UnwindData |  |
| 413 | `??0?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `??0?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x7730` | 79 | UnwindData |  |
| 415 | `??0?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `??0?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x77B0` | 79 | UnwindData |  |
| 417 | `??0?$moneypunct@D$00@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7810` | 65 | UnwindData |  |
| 418 | `??0?$moneypunct@D$00@std@@QEAA@_K@Z` | `0x7860` | 106 | UnwindData |  |
| 419 | `??0?$moneypunct@D$0A@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x78D0` | 65 | UnwindData |  |
| 420 | `??0?$moneypunct@D$0A@@std@@QEAA@_K@Z` | `0x7920` | 106 | UnwindData |  |
| 421 | `??0?$moneypunct@G$00@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7990` | 65 | UnwindData |  |
| 422 | `??0?$moneypunct@G$00@std@@QEAA@_K@Z` | `0x79E0` | 106 | UnwindData |  |
| 423 | `??0?$moneypunct@G$0A@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7A50` | 65 | UnwindData |  |
| 424 | `??0?$moneypunct@G$0A@@std@@QEAA@_K@Z` | `0x7AA0` | 106 | UnwindData |  |
| 425 | `??0?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `??0?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x7B30` | 79 | UnwindData |  |
| 427 | `??0?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `??0?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x7BB0` | 79 | UnwindData |  |
| 429 | `??0?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `??0?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x7C30` | 79 | UnwindData |  |
| 431 | `??0?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `??0?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x7CB0` | 79 | UnwindData |  |
| 433 | `??0?$numpunct@D@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7D10` | 51 | UnwindData |  |
| 434 | `??0?$numpunct@D@std@@QEAA@_K@Z` | `0x7D50` | 92 | UnwindData |  |
| 435 | `??0?$numpunct@G@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7DC0` | 51 | UnwindData |  |
| 436 | `??0?$numpunct@G@std@@QEAA@_K@Z` | `0x7E00` | 92 | UnwindData |  |
| 437 | `??0?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7E70` | 51 | UnwindData |  |
| 438 | `??0?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x7EB0` | 92 | UnwindData |  |
| 439 | `??0?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7F20` | 102 | UnwindData |  |
| 440 | `??0?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x7F90` | 140 | UnwindData |  |
| 441 | `??0?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x8030` | 54 | UnwindData |  |
| 442 | `??0?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x8070` | 101 | UnwindData |  |
| 443 | `??0?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x80E0` | 54 | UnwindData |  |
| 444 | `??0?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x8120` | 101 | UnwindData |  |
| 446 | `??0_Locinfo@std@@QEAA@AEBV01@@Z` | `0x8190` | 188 | UnwindData |  |
| 450 | `??0_Timevec@std@@QEAA@AEBV01@@Z` | `0x8260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `??0_Timevec@std@@QEAA@PEAX@Z` | `0x8280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `??0__non_rtti_object@std@@QEAA@$$QEAV01@@Z` | `0x8290` | 34 | UnwindData |  |
| 454 | `??0__non_rtti_object@std@@QEAA@AEBV01@@Z` | `0x82C0` | 34 | UnwindData |  |
| 455 | `??0__non_rtti_object@std@@QEAA@PEBD@Z` | `0x82F0` | 57 | UnwindData |  |
| 456 | `??0bad_alloc@std@@QEAA@AEBV01@@Z` | `0x8330` | 34 | UnwindData |  |
| 457 | `??0bad_alloc@std@@QEAA@PEBD@Z` | `0x8360` | 52 | UnwindData |  |
| 458 | `??0bad_alloc@std@@QEAA@XZ` | `0x83A0` | 56 | UnwindData |  |
| 459 | `??0bad_cast@std@@QEAA@AEBV01@@Z` | `0x83E0` | 34 | UnwindData |  |
| 460 | `??0bad_cast@std@@QEAA@PEBD@Z` | `0x8410` | 52 | UnwindData |  |
| 461 | `??0bad_exception@std@@QEAA@AEBV01@@Z` | `0x8450` | 34 | UnwindData |  |
| 462 | `??0bad_exception@std@@QEAA@PEBD@Z` | `0x8480` | 52 | UnwindData |  |
| 463 | `??0bad_typeid@std@@QEAA@AEBV01@@Z` | `0x84C0` | 34 | UnwindData |  |
| 464 | `??0bad_typeid@std@@QEAA@PEBD@Z` | `0x84F0` | 52 | UnwindData |  |
| 465 | `??0codecvt_base@std@@QEAA@_K@Z` | `0x8530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `??0ctype_base@std@@QEAA@_K@Z` | `0x8550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `??0domain_error@std@@QEAA@AEBV01@@Z` | `0x8570` | 106 | UnwindData |  |
| 468 | `??0domain_error@std@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@@Z` | `0x85E0` | 33 | UnwindData |  |
| 469 | `??0facet@locale@std@@IEAA@_K@Z` | `0x8610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `??0ios_base@std@@IEAA@XZ` | `0x8630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `??0ios_base@std@@QEAA@AEBV01@@Z` | `0x8650` | 158 | UnwindData |  |
| 472 | `??0length_error@std@@QEAA@AEBV01@@Z` | `0x8700` | 106 | UnwindData |  |
| 473 | `??0length_error@std@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@@Z` | `0x8770` | 33 | UnwindData |  |
| 474 | `??0locale@std@@AEAA@PEAV_Locimp@01@@Z` | `0x87A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 476 | `??0locale@std@@QEAA@AEBV01@@Z` | `0x87B0` | 80 | UnwindData |  |
| 479 | `??0locale@std@@QEAA@W4_Uninitialized@1@@Z` | `0x8810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 480 | `??0locale@std@@QEAA@XZ` | `0x8820` | 109 | UnwindData |  |
| 481 | `??0logic_error@std@@QEAA@AEBV01@@Z` | `0x88A0` | 96 | UnwindData |  |
| 482 | `??0logic_error@std@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@@Z` | `0x8910` | 110 | UnwindData |  |
| 483 | `??0messages_base@std@@QEAA@_K@Z` | `0x8990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `??0money_base@std@@QEAA@_K@Z` | `0x89B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `??0out_of_range@std@@QEAA@AEBV01@@Z` | `0x89D0` | 106 | UnwindData |  |
| 487 | `??0out_of_range@std@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@@Z` | `0x8A40` | 33 | UnwindData |  |
| 488 | `??0overflow_error@std@@QEAA@AEBV01@@Z` | `0x8A70` | 106 | UnwindData |  |
| 489 | `??0overflow_error@std@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@@Z` | `0x8AE0` | 33 | UnwindData |  |
| 490 | `??0range_error@std@@QEAA@AEBV01@@Z` | `0x8B10` | 106 | UnwindData |  |
| 491 | `??0range_error@std@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@@Z` | `0x8B80` | 33 | UnwindData |  |
| 492 | `??0runtime_error@std@@QEAA@AEBV01@@Z` | `0x8BB0` | 96 | UnwindData |  |
| 493 | `??0runtime_error@std@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@@Z` | `0x8C20` | 110 | UnwindData |  |
| 495 | `??0time_base@std@@QEAA@_K@Z` | `0x8CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `??0underflow_error@std@@QEAA@AEBV01@@Z` | `0x8CC0` | 106 | UnwindData |  |
| 497 | `??0underflow_error@std@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@@Z` | `0x8D30` | 33 | UnwindData |  |
| 498 | `??1?$_Mpunct@D@std@@UEAA@XZ` | `0x8D60` | 71 | UnwindData |  |
| 499 | `??1?$_Mpunct@G@std@@UEAA@XZ` | `0x8DB0` | 71 | UnwindData |  |
| 500 | `??1?$basic_filebuf@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x8E00` | 176 | UnwindData |  |
| 501 | `??1?$basic_filebuf@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x8EC0` | 176 | UnwindData |  |
| 502 | `??1?$basic_fstream@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x8F80` | 131 | UnwindData |  |
| 503 | `??1?$basic_fstream@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x9010` | 131 | UnwindData |  |
| 504 | `??1?$basic_ifstream@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x90A0` | 79 | UnwindData |  |
| 505 | `??1?$basic_ifstream@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x9100` | 79 | UnwindData |  |
| 506 | `??1?$basic_ios@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x9160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `??1?$basic_ios@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x9180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `??1?$basic_iostream@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x91A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `??1?$basic_iostream@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x91F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `??1?$basic_istream@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x9240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `??1?$basic_istream@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x9260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `??1?$basic_ofstream@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x9280` | 79 | UnwindData |  |
| 515 | `??1?$basic_ofstream@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x92E0` | 79 | UnwindData |  |
| 516 | `??1?$basic_ostream@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x9340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `??1?$basic_ostream@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x9360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `??1?$basic_streambuf@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x9380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `??1?$basic_streambuf@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x93A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | `??1?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@XZ` | `0x93C0` | 65 | UnwindData |  |
| 523 | `??1?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@XZ` | `0x9410` | 65 | UnwindData |  |
| 528 | `??1?$codecvt@DDH@std@@UEAA@XZ` | `0x9460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 529 | `??1?$codecvt@GDH@std@@UEAA@XZ` | `0x9480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `??1?$collate@D@std@@UEAA@XZ` | `0x94A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 531 | `??1?$collate@G@std@@UEAA@XZ` | `0x94C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | `??1?$ctype@D@std@@UEAA@XZ` | `0x94E0` | 51 | UnwindData |  |
| 533 | `??1?$ctype@G@std@@UEAA@XZ` | `0x9520` | 51 | UnwindData |  |
| 534 | `??1?$messages@D@std@@UEAA@XZ` | `0x9560` | 53 | UnwindData |  |
| 535 | `??1?$messages@G@std@@UEAA@XZ` | `0x95A0` | 53 | UnwindData |  |
| 536 | `??1?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@UEAA@XZ` | `0x95E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `??1?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@UEAA@XZ` | `0x9600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `??1?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@UEAA@XZ` | `0x9620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `??1?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@UEAA@XZ` | `0x9640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `??1?$moneypunct@D$00@std@@UEAA@XZ` | `0x9660` | 71 | UnwindData |  |
| 541 | `??1?$moneypunct@D$0A@@std@@UEAA@XZ` | `0x96B0` | 71 | UnwindData |  |
| 542 | `??1?$moneypunct@G$00@std@@UEAA@XZ` | `0x9700` | 71 | UnwindData |  |
| 543 | `??1?$moneypunct@G$0A@@std@@UEAA@XZ` | `0x9750` | 71 | UnwindData |  |
| 544 | `??1?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@UEAA@XZ` | `0x97A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `??1?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@UEAA@XZ` | `0x97C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | `??1?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@UEAA@XZ` | `0x97E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `??1?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@UEAA@XZ` | `0x9800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `??1?$numpunct@D@std@@UEAA@XZ` | `0x9820` | 62 | UnwindData |  |
| 549 | `??1?$numpunct@G@std@@UEAA@XZ` | `0x9870` | 62 | UnwindData |  |
| 550 | `??1?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@UEAA@XZ` | `0x98C0` | 53 | UnwindData |  |
| 551 | `??1?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@UEAA@XZ` | `0x9900` | 53 | UnwindData |  |
| 552 | `??1?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@UEAA@XZ` | `0x9940` | 45 | UnwindData |  |
| 553 | `??1?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@UEAA@XZ` | `0x9980` | 45 | UnwindData |  |
| 557 | `??1_Timevec@std@@QEAA@XZ` | `0x99C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 559 | `??1__non_rtti_object@std@@UEAA@XZ` | `0x99D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `??1bad_alloc@std@@UEAA@XZ` | `0x99F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `??1bad_cast@std@@UEAA@XZ` | `0x9A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 562 | `??1bad_exception@std@@UEAA@XZ` | `0x9A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `??1bad_typeid@std@@UEAA@XZ` | `0x9A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `??1codecvt_base@std@@UEAA@XZ` | `0x9A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 565 | `??1ctype_base@std@@UEAA@XZ` | `0x9A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 566 | `??1domain_error@std@@UEAA@XZ` | `0x9AB0` | 84 | UnwindData |  |
| 567 | `??1facet@locale@std@@UEAA@XZ` | `0x9B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `??1length_error@std@@UEAA@XZ` | `0x9B30` | 84 | UnwindData |  |
| 571 | `??1locale@std@@QEAA@XZ` | `0x9B90` | 116 | UnwindData |  |
| 572 | `??1logic_error@std@@UEAA@XZ` | `0x9C10` | 84 | UnwindData |  |
| 573 | `??1messages_base@std@@UEAA@XZ` | `0x9C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `??1money_base@std@@UEAA@XZ` | `0x9C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `??1out_of_range@std@@UEAA@XZ` | `0x9CB0` | 84 | UnwindData |  |
| 577 | `??1overflow_error@std@@UEAA@XZ` | `0x9D10` | 84 | UnwindData |  |
| 578 | `??1range_error@std@@UEAA@XZ` | `0x9D70` | 84 | UnwindData |  |
| 579 | `??1runtime_error@std@@UEAA@XZ` | `0x9DD0` | 84 | UnwindData |  |
| 582 | `??1time_base@std@@UEAA@XZ` | `0x9EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `??1underflow_error@std@@UEAA@XZ` | `0x9ED0` | 84 | UnwindData |  |
| 596 | `??4?$allocator@X@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x9F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `??4?$allocator@X@std@@QEAAAEAV01@AEBV01@@Z` | `0x9F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `??4?$basic_filebuf@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0x9F50` | 108 | UnwindData |  |
| 599 | `??4?$basic_filebuf@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0x9FD0` | 108 | UnwindData |  |
| 600 | `??4?$basic_fstream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA050` | 48 | UnwindData |  |
| 601 | `??4?$basic_fstream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA090` | 48 | UnwindData |  |
| 602 | `??4?$basic_ifstream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA0D0` | 48 | UnwindData |  |
| 603 | `??4?$basic_ifstream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA110` | 48 | UnwindData |  |
| 604 | `??4?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA150` | 68 | UnwindData |  |
| 605 | `??4?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA1A0` | 70 | UnwindData |  |
| 606 | `??4?$basic_iostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA1F0` | 127 | UnwindData |  |
| 607 | `??4?$basic_iostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA280` | 129 | UnwindData |  |
| 608 | `??4?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA310` | 124 | UnwindData |  |
| 609 | `??4?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA3A0` | 126 | UnwindData |  |
| 612 | `??4?$basic_ofstream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA430` | 129 | UnwindData |  |
| 613 | `??4?$basic_ofstream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA4C0` | 131 | UnwindData |  |
| 614 | `??4?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA550` | 101 | UnwindData |  |
| 615 | `??4?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA5C0` | 103 | UnwindData |  |
| 618 | `??4?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA630` | 123 | UnwindData |  |
| 619 | `??4?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA6C0` | 123 | UnwindData |  |
| 620 | `??4?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 621 | `??4?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV01@D@Z` | `0xA770` | 73 | UnwindData |  |
| 622 | `??4?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV01@PEBD@Z` | `0xA7C0` | 95 | UnwindData |  |
| 623 | `??4?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV01@AEBV01@@Z` | `0xA830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 624 | `??4?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV01@G@Z` | `0xA850` | 72 | UnwindData |  |
| 625 | `??4?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV01@PEBG@Z` | `0xA8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `??4?$char_traits@D@std@@QEAAAEAU01@$$QEAU01@@Z` | `0xA8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | `??4?$char_traits@D@std@@QEAAAEAU01@AEBU01@@Z` | `0xA8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 632 | `??4?$char_traits@G@std@@QEAAAEAU01@$$QEAU01@@Z` | `0xA8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `??4?$char_traits@G@std@@QEAAAEAU01@AEBU01@@Z` | `0xA8F0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 669 | `??4Init@ios_base@std@@QEAAAEAV012@AEBV012@@Z` | `0xAA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 670 | `??4_Locinfo@std@@QEAAAEAV01@AEBV01@@Z` | `0xAA10` | 112 | UnwindData |  |
| 671 | `??4_Lockit@std@@QEAAAEAV01@AEBV01@@Z` | `0xAA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 678 | `??4_Timevec@std@@QEAAAEAV01@AEBV01@@Z` | `0xAAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `??4__non_rtti_object@std@@QEAAAEAV01@$$QEAV01@@Z` | `0xAAC0` | 24 | UnwindData |  |
| 681 | `??4__non_rtti_object@std@@QEAAAEAV01@AEBV01@@Z` | `0xAAE0` | 24 | UnwindData |  |
| 682 | `??4bad_alloc@std@@QEAAAEAV01@AEBV01@@Z` | `0xAB00` | 24 | UnwindData |  |
| 683 | `??4bad_cast@std@@QEAAAEAV01@AEBV01@@Z` | `0xAB20` | 24 | UnwindData |  |
| 684 | `??4bad_exception@std@@QEAAAEAV01@AEBV01@@Z` | `0xAB40` | 24 | UnwindData |  |
| 685 | `??4bad_typeid@std@@QEAAAEAV01@AEBV01@@Z` | `0xAB60` | 24 | UnwindData |  |
| 686 | `??4domain_error@std@@QEAAAEAV01@AEBV01@@Z` | `0xAB80` | 56 | UnwindData |  |
| 687 | `??4id@locale@std@@QEAAAEAV012@$$QEAV012@@Z` | `0xABC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 688 | `??4id@locale@std@@QEAAAEAV012@AEBV012@@Z` | `0xABD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 689 | `??4ios_base@std@@QEAAAEAV01@AEBV01@@Z` | `0xABE0` | 34 | UnwindData |  |
| 690 | `??4length_error@std@@QEAAAEAV01@AEBV01@@Z` | `0xAC10` | 56 | UnwindData |  |
| 691 | `??4locale@std@@QEAAAEAV01@AEBV01@@Z` | `0xAC50` | 186 | UnwindData |  |
| 692 | `??4logic_error@std@@QEAAAEAV01@AEBV01@@Z` | `0xAD10` | 56 | UnwindData |  |
| 693 | `??4out_of_range@std@@QEAAAEAV01@AEBV01@@Z` | `0xAD50` | 56 | UnwindData |  |
| 694 | `??4overflow_error@std@@QEAAAEAV01@AEBV01@@Z` | `0xAD90` | 56 | UnwindData |  |
| 695 | `??4range_error@std@@QEAAAEAV01@AEBV01@@Z` | `0xADD0` | 56 | UnwindData |  |
| 696 | `??4runtime_error@std@@QEAAAEAV01@AEBV01@@Z` | `0xAE10` | 56 | UnwindData |  |
| 697 | `??4underflow_error@std@@QEAAAEAV01@AEBV01@@Z` | `0xAE50` | 56 | UnwindData |  |
| 698 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAF@Z` | `0xAE90` | 396 | UnwindData |  |
| 699 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAG@Z` | `0xB030` | 323 | UnwindData |  |
| 700 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAH@Z` | `0xB180` | 382 | UnwindData |  |
| 701 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAI@Z` | `0xB310` | 323 | UnwindData |  |
| 702 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAJ@Z` | `0xB460` | 323 | UnwindData |  |
| 703 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAK@Z` | `0xB5B0` | 323 | UnwindData |  |
| 704 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAM@Z` | `0xB700` | 323 | UnwindData |  |
| 705 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAN@Z` | `0xB850` | 323 | UnwindData |  |
| 706 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAO@Z` | `0xB9A0` | 323 | UnwindData |  |
| 707 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAPEAX@Z` | `0xBAF0` | 323 | UnwindData |  |
| 708 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEA_J@Z` | `0xBC40` | 323 | UnwindData |  |
| 709 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEA_K@Z` | `0xBD90` | 323 | UnwindData |  |
| 710 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEA_N@Z` | `0xBEE0` | 323 | UnwindData |  |
| 711 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0xC030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@DU?$char_traits@D@std@@@1@AEAV21@@Z@Z` | `0xC040` | 43 | UnwindData |  |
| 713 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0xC080` | 43 | UnwindData |  |
| 714 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@@Z` | `0xC0C0` | 334 | UnwindData |  |
| 715 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAF@Z` | `0xC220` | 396 | UnwindData |  |
| 716 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAG@Z` | `0xC3C0` | 323 | UnwindData |  |
| 717 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAH@Z` | `0xC510` | 382 | UnwindData |  |
| 718 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAI@Z` | `0xC6A0` | 323 | UnwindData |  |
| 719 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAJ@Z` | `0xC7F0` | 323 | UnwindData |  |
| 720 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAK@Z` | `0xC940` | 323 | UnwindData |  |
| 721 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAM@Z` | `0xCA90` | 323 | UnwindData |  |
| 722 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAN@Z` | `0xCBE0` | 323 | UnwindData |  |
| 723 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAO@Z` | `0xCD30` | 323 | UnwindData |  |
| 724 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAPEAX@Z` | `0xCE80` | 323 | UnwindData |  |
| 725 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEA_J@Z` | `0xCFD0` | 323 | UnwindData |  |
| 726 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEA_K@Z` | `0xD120` | 323 | UnwindData |  |
| 727 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEA_N@Z` | `0xD270` | 323 | UnwindData |  |
| 728 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0xD3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 729 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@GU?$char_traits@G@std@@@1@AEAV21@@Z@Z` | `0xD3D0` | 43 | UnwindData |  |
| 730 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0xD410` | 43 | UnwindData |  |
| 731 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@@Z` | `0xD450` | 353 | UnwindData |  |
| 749 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@F@Z` | `0xD5C0` | 430 | UnwindData |  |
| 750 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@G@Z` | `0xD780` | 397 | UnwindData |  |
| 751 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@H@Z` | `0xD920` | 399 | UnwindData |  |
| 752 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@I@Z` | `0xDAC0` | 396 | UnwindData |  |
| 753 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@J@Z` | `0xDC60` | 396 | UnwindData |  |
| 754 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@K@Z` | `0xDE00` | 396 | UnwindData |  |
| 755 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@M@Z` | `0xDFA0` | 402 | UnwindData |  |
| 756 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@N@Z` | `0xE140` | 395 | UnwindData |  |
| 757 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@O@Z` | `0xE2E0` | 395 | UnwindData |  |
| 758 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0xE480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@DU?$char_traits@D@std@@@1@AEAV21@@Z@Z` | `0xE490` | 43 | UnwindData |  |
| 760 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0xE4D0` | 43 | UnwindData |  |
| 761 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@@Z` | `0xE510` | 488 | UnwindData |  |
| 762 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@PEBX@Z` | `0xE700` | 396 | UnwindData |  |
| 763 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@_J@Z` | `0xE8A0` | 396 | UnwindData |  |
| 764 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@_K@Z` | `0xEA40` | 396 | UnwindData |  |
| 765 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@_N@Z` | `0xEBE0` | 396 | UnwindData |  |
| 766 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@F@Z` | `0xED80` | 432 | UnwindData |  |
| 767 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@G@Z` | `0xEF40` | 399 | UnwindData |  |
| 768 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@H@Z` | `0xF0E0` | 401 | UnwindData |  |
| 769 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@I@Z` | `0xF280` | 398 | UnwindData |  |
| 770 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@J@Z` | `0xF420` | 398 | UnwindData |  |
| 771 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@K@Z` | `0xF5C0` | 398 | UnwindData |  |
| 772 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@M@Z` | `0xF760` | 404 | UnwindData |  |
| 773 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@N@Z` | `0xF900` | 397 | UnwindData |  |
| 774 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@O@Z` | `0xFAA0` | 397 | UnwindData |  |
| 775 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0xFC40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@GU?$char_traits@G@std@@@1@AEAV21@@Z@Z` | `0xFC50` | 43 | UnwindData |  |
| 777 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0xFC90` | 43 | UnwindData |  |
| 778 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@@Z` | `0xFCD0` | 506 | UnwindData |  |
| 779 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@PEBX@Z` | `0xFED0` | 398 | UnwindData |  |
| 780 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@_J@Z` | `0x10070` | 398 | UnwindData |  |
| 781 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@_K@Z` | `0x10210` | 398 | UnwindData |  |
| 782 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@_N@Z` | `0x103B0` | 398 | UnwindData |  |
| 800 | `??7ios_base@std@@QEBA_NXZ` | `0x10550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `??9locale@std@@QEBA_NAEBV01@@Z` | `0x10560` | 16 | UnwindData |  |
| 833 | `??A?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAD_K@Z` | `0x10580` | 91 | UnwindData |  |
| 834 | `??A?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAAEBD_K@Z` | `0x105F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 835 | `??A?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAG_K@Z` | `0x10610` | 92 | UnwindData |  |
| 836 | `??A?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAAEBG_K@Z` | `0x10680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 837 | `??Bid@locale@std@@QEAA_KXZ` | `0x106A0` | 75 | UnwindData |  |
| 838 | `??Bios_base@std@@QEBAPEAXXZ` | `0x10700` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 915 | `??Rlocale@std@@QEBA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@0@Z` | `0x10810` | 119 | UnwindData |  |
| 925 | `??Y?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV01@AEBV01@@Z` | `0x10890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `??Y?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV01@D@Z` | `0x108B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `??Y?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV01@PEBD@Z` | `0x108D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | `??Y?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV01@AEBV01@@Z` | `0x108F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `??Y?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV01@G@Z` | `0x10910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | `??Y?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV01@PEBG@Z` | `0x10930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1044 | `??_D?$basic_fstream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x10950` | 44 | UnwindData |  |
| 1045 | `??_D?$basic_fstream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x10990` | 44 | UnwindData |  |
| 1046 | `??_D?$basic_ifstream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x109D0` | 104 | UnwindData |  |
| 1047 | `??_D?$basic_ifstream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x10A40` | 104 | UnwindData |  |
| 1048 | `??_D?$basic_iostream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x10AB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1049 | `??_D?$basic_iostream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x10B10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1050 | `??_D?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x10B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1051 | `??_D?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x10BA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `??_D?$basic_ofstream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x10BD0` | 104 | UnwindData |  |
| 1055 | `??_D?$basic_ofstream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x10C40` | 104 | UnwindData |  |
| 1056 | `??_D?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x10CB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `??_D?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x10CE0` | 10,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1062 | `??_F?$basic_filebuf@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x134C0` | 54 | UnwindData |  |
| 1063 | `??_F?$basic_filebuf@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x13500` | 54 | UnwindData |  |
| 1068 | `??_F?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXXZ` | `0x13540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1069 | `??_F?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXXZ` | `0x13560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `??_F?$codecvt@DDH@std@@QEAAXXZ` | `0x13580` | 86 | UnwindData |  |
| 1075 | `??_F?$codecvt@GDH@std@@QEAAXXZ` | `0x135E0` | 86 | UnwindData |  |
| 1076 | `??_F?$collate@D@std@@QEAAXXZ` | `0x13640` | 86 | UnwindData |  |
| 1077 | `??_F?$collate@G@std@@QEAAXXZ` | `0x136A0` | 86 | UnwindData |  |
| 1081 | `??_F?$ctype@D@std@@QEAAXXZ` | `0x13700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1082 | `??_F?$ctype@G@std@@QEAAXXZ` | `0x13720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1083 | `??_F?$messages@D@std@@QEAAXXZ` | `0x13730` | 90 | UnwindData |  |
| 1084 | `??_F?$messages@G@std@@QEAAXXZ` | `0x13790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `??_F?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x137A0` | 72 | UnwindData |  |
| 1086 | `??_F?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x137F0` | 72 | UnwindData |  |
| 1087 | `??_F?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x13840` | 72 | UnwindData |  |
| 1088 | `??_F?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x13890` | 72 | UnwindData |  |
| 1089 | `??_F?$moneypunct@D$00@std@@QEAAXXZ` | `0x138E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `??_F?$moneypunct@D$0A@@std@@QEAAXXZ` | `0x138F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1091 | `??_F?$moneypunct@G$00@std@@QEAAXXZ` | `0x13900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `??_F?$moneypunct@G$0A@@std@@QEAAXXZ` | `0x13910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `??_F?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x13920` | 72 | UnwindData |  |
| 1094 | `??_F?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x13970` | 72 | UnwindData |  |
| 1095 | `??_F?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x139C0` | 72 | UnwindData |  |
| 1096 | `??_F?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x13A10` | 72 | UnwindData |  |
| 1097 | `??_F?$numpunct@D@std@@QEAAXXZ` | `0x13A60` | 90 | UnwindData |  |
| 1098 | `??_F?$numpunct@G@std@@QEAAXXZ` | `0x13AC0` | 90 | UnwindData |  |
| 1099 | `??_F?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x13B20` | 90 | UnwindData |  |
| 1100 | `??_F?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x13B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `??_F?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x13B90` | 99 | UnwindData |  |
| 1102 | `??_F?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x13C00` | 99 | UnwindData |  |
| 1103 | `??_F_Locinfo@std@@QEAAXXZ` | `0x13C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `??_F_Timevec@std@@QEAAXXZ` | `0x13C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `??_Fbad_cast@std@@QEAAXXZ` | `0x13CA0` | 57 | UnwindData |  |
| 1106 | `??_Fbad_exception@std@@QEAAXXZ` | `0x13CE0` | 57 | UnwindData |  |
| 1107 | `??_Fbad_typeid@std@@QEAAXXZ` | `0x13D20` | 57 | UnwindData |  |
| 1108 | `??_Fcodecvt_base@std@@QEAAXXZ` | `0x13D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1109 | `??_Fctype_base@std@@QEAAXXZ` | `0x13D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1110 | `??_Ffacet@locale@std@@QEAAXXZ` | `0x13DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1111 | `??_Fmessages_base@std@@QEAAXXZ` | `0x13DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1112 | `??_Fmoney_base@std@@QEAAXXZ` | `0x13DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1113 | `??_Ftime_base@std@@QEAAXXZ` | `0x13E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1125 | `?_Copy@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAAX_K@Z` | `0x13E20` | 222 | UnwindData |  |
| 1126 | `?_Copy@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAAX_K@Z` | `0x13F10` | 253 | UnwindData |  |
| 1130 | `?_Decref@facet@locale@std@@QEAAPEAV123@XZ` | `0x14020` | 92 | UnwindData |  |
| 1131 | `?_Doraise@bad_alloc@std@@MEBAXXZ` | `0x14090` | 35 | UnwindData |  |
| 1132 | `?_Doraise@bad_cast@std@@MEBAXXZ` | `0x140C0` | 35 | UnwindData |  |
| 1133 | `?_Doraise@bad_exception@std@@MEBAXXZ` | `0x140F0` | 35 | UnwindData |  |
| 1134 | `?_Doraise@bad_typeid@std@@MEBAXXZ` | `0x14120` | 35 | UnwindData |  |
| 1135 | `?_Doraise@domain_error@std@@MEBAXXZ` | `0x14150` | 35 | UnwindData |  |
| 1136 | `?_Doraise@length_error@std@@MEBAXXZ` | `0x14180` | 35 | UnwindData |  |
| 1137 | `?_Doraise@logic_error@std@@MEBAXXZ` | `0x141B0` | 35 | UnwindData |  |
| 1138 | `?_Doraise@out_of_range@std@@MEBAXXZ` | `0x141E0` | 35 | UnwindData |  |
| 1139 | `?_Doraise@overflow_error@std@@MEBAXXZ` | `0x14210` | 35 | UnwindData |  |
| 1140 | `?_Doraise@range_error@std@@MEBAXXZ` | `0x14240` | 35 | UnwindData |  |
| 1141 | `?_Doraise@runtime_error@std@@MEBAXXZ` | `0x14270` | 35 | UnwindData |  |
| 1142 | `?_Doraise@underflow_error@std@@MEBAXXZ` | `0x142A0` | 35 | UnwindData |  |
| 1143 | `?_Eos@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAAX_K@Z` | `0x142D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `?_Eos@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAAX_K@Z` | `0x142F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `?_Ffmt@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@KAPEADPEADDH@Z` | `0x14310` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1152 | `?_Ffmt@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@KAPEADPEADDH@Z` | `0x14390` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `?_Fput@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@KA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBD_K3@Z` | `0x14410` | 800 | UnwindData |  |
| 1155 | `?_Fput@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@KA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBD_K3@Z` | `0x14740` | 879 | UnwindData |  |
| 1157 | `?_Freeze@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAAXXZ` | `0x14AC0` | 58 | UnwindData |  |
| 1158 | `?_Freeze@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAAXXZ` | `0x14B00` | 58 | UnwindData |  |
| 1159 | `?_Getcat@?$_Mpunct@D@std@@SA_KXZ` | `0x14B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1160 | `?_Getcat@?$_Mpunct@G@std@@SA_KXZ` | `0x14B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1161 | `?_Getcat@?$codecvt@DDH@std@@SA_KXZ` | `0x14B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1162 | `?_Getcat@?$codecvt@GDH@std@@SA_KXZ` | `0x14B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1163 | `?_Getcat@?$collate@D@std@@SA_KXZ` | `0x14B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1164 | `?_Getcat@?$collate@G@std@@SA_KXZ` | `0x14B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1165 | `?_Getcat@?$ctype@D@std@@SA_KXZ` | `0x14BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1166 | `?_Getcat@?$ctype@G@std@@SA_KXZ` | `0x14BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `?_Getcat@?$messages@D@std@@SA_KXZ` | `0x14BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1168 | `?_Getcat@?$messages@G@std@@SA_KXZ` | `0x14BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1169 | `?_Getcat@?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KXZ` | `0x14BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1170 | `?_Getcat@?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KXZ` | `0x14BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `?_Getcat@?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KXZ` | `0x14C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1172 | `?_Getcat@?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KXZ` | `0x14C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `?_Getcat@?$moneypunct@D$00@std@@SA_KXZ` | `0x14C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `?_Getcat@?$moneypunct@D$0A@@std@@SA_KXZ` | `0x14C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `?_Getcat@?$moneypunct@G$00@std@@SA_KXZ` | `0x14C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1176 | `?_Getcat@?$moneypunct@G$0A@@std@@SA_KXZ` | `0x14C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `?_Getcat@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KXZ` | `0x14C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `?_Getcat@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KXZ` | `0x14C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1179 | `?_Getcat@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KXZ` | `0x14C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `?_Getcat@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KXZ` | `0x14C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `?_Getcat@?$numpunct@D@std@@SA_KXZ` | `0x14CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1182 | `?_Getcat@?$numpunct@G@std@@SA_KXZ` | `0x14CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `?_Getcat@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KXZ` | `0x14CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1184 | `?_Getcat@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KXZ` | `0x14CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `?_Getcat@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KXZ` | `0x14CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1186 | `?_Getcat@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KXZ` | `0x14CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `?_Getcat@facet@locale@std@@SA_KXZ` | `0x14D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1188 | `?_Getcoll@_Locinfo@std@@QEBA?AU_Collvec@@XZ` | `0x14D10` | 26 | UnwindData |  |
| 1189 | `?_Getctype@_Locinfo@std@@QEBA?AU_Ctypevec@@XZ` | `0x14D30` | 44 | UnwindData |  |
| 1190 | `?_Getcvt@_Locinfo@std@@QEBA?AU_Cvtvec@@XZ` | `0x14D70` | 26 | UnwindData |  |
| 1191 | `?_Getdays@_Locinfo@std@@QEBAPEBDXZ` | `0x14D90` | 147 | UnwindData |  |
| 1193 | `?_Getfalse@_Locinfo@std@@QEBAPEBDXZ` | `0x14E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `?_Getffld@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@CAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@1AEBVlocale@2@@Z` | `0x14E40` | 965 | UnwindData |  |
| 1195 | `?_Getffld@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@CAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@1AEBVlocale@2@@Z` | `0x15210` | 1,431 | UnwindData |  |
| 1196 | `?_Getifld@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@CAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@1HAEBVlocale@2@@Z` | `0x157B0` | 1,311 | UnwindData |  |
| 1197 | `?_Getifld@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@CAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@1HAEBVlocale@2@@Z` | `0x15CE0` | 1,603 | UnwindData |  |
| 1198 | `?_Getint@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@CAHAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@0HHAEAH@Z` | `0x16330` | 391 | UnwindData |  |
| 1199 | `?_Getint@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@CAHAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@0HHAEAH@Z` | `0x164C0` | 637 | UnwindData |  |
| 1200 | `?_Getlconv@_Locinfo@std@@QEBAPEBUlconv@@XZ` | `0x16750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1201 | `?_Getmfld@?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@AEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@0_NAEAVios_base@2@@Z` | `0x16760` | 3,549 | UnwindData |  |
| 1202 | `?_Getmfld@?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@AEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@0_NAEAVios_base@2@@Z` | `0x17550` | 4,210 | UnwindData |  |
| 1203 | `?_Getmonths@_Locinfo@std@@QEBAPEBDXZ` | `0x185D0` | 158 | UnwindData |  |
| 1204 | `?_Getname@_Locinfo@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x18680` | 51 | UnwindData |  |
| 1205 | `?_Getno@_Locinfo@std@@QEBAPEBDXZ` | `0x186C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1206 | `?_Getptr@_Timevec@std@@QEBAPEAXXZ` | `0x186D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `?_Gettnames@_Locinfo@std@@QEBA?AV_Timevec@2@XZ` | `0x186E0` | 26 | UnwindData |  |
| 1208 | `?_Gettrue@_Locinfo@std@@QEBAPEBDXZ` | `0x18700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `?_Getyes@_Locinfo@std@@QEBAPEBDXZ` | `0x18710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `?_Gndec@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAPEADXZ` | `0x18720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `?_Gndec@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAPEAGXZ` | `0x18740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `?_Gninc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAPEADXZ` | `0x18760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1214 | `?_Gninc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAPEAGXZ` | `0x18780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `?_Grow@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAA_N_K_N@Z` | `0x187A0` | 257 | UnwindData |  |
| 1216 | `?_Grow@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAA_N_K_N@Z` | `0x188B0` | 262 | UnwindData |  |
| 1218 | `?_Ifmt@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@KAPEADPEADDH@Z` | `0x189C0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1219 | `?_Ifmt@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@KAPEADPEADPEBDH@Z` | `0x18A40` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `?_Ifmt@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@KAPEADPEADDH@Z` | `0x18AB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `?_Ifmt@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@KAPEADPEADPEBDH@Z` | `0x18B30` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1222 | `?_Incref@facet@locale@std@@QEAAXXZ` | `0x18CA0` | 52 | UnwindData |  |
| 1227 | `?_Init@?$_Mpunct@D@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x18CE0` | 537 | UnwindData |  |
| 1228 | `?_Init@?$_Mpunct@G@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x18F00` | 425 | UnwindData |  |
| 1229 | `?_Init@?$basic_filebuf@DU?$char_traits@D@std@@@std@@IEAAXPEAU_iobuf@@W4_Initfl@12@@Z` | `0x190B0` | 229 | UnwindData |  |
| 1230 | `?_Init@?$basic_filebuf@GU?$char_traits@G@std@@@std@@IEAAXPEAU_iobuf@@W4_Initfl@12@@Z` | `0x191A0` | 183 | UnwindData |  |
| 1231 | `?_Init@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXPEAPEAD0PEAH001@Z` | `0x19260` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `?_Init@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXXZ` | `0x19290` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1233 | `?_Init@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXPEAPEAG0PEAH001@Z` | `0x192E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `?_Init@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXXZ` | `0x19310` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1237 | `?_Init@?$codecvt@DDH@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19360` | 24 | UnwindData |  |
| 1238 | `?_Init@?$codecvt@GDH@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19380` | 24 | UnwindData |  |
| 1239 | `?_Init@?$collate@D@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x193A0` | 24 | UnwindData |  |
| 1240 | `?_Init@?$collate@G@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x193C0` | 24 | UnwindData |  |
| 1241 | `?_Init@?$ctype@D@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x193E0` | 99 | UnwindData |  |
| 1242 | `?_Init@?$ctype@G@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19450` | 42 | UnwindData |  |
| 1243 | `?_Init@?$messages@D@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19480` | 120 | UnwindData |  |
| 1244 | `?_Init@?$messages@G@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19500` | 51 | UnwindData |  |
| 1245 | `?_Init@?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1246 | `?_Init@?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1247 | `?_Init@?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `?_Init@?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `?_Init@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1250 | `?_Init@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1251 | `?_Init@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x195A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1252 | `?_Init@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x195B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `?_Init@?$numpunct@D@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x195C0` | 204 | UnwindData |  |
| 1254 | `?_Init@?$numpunct@G@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x196A0` | 169 | UnwindData |  |
| 1255 | `?_Init@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19750` | 185 | UnwindData |  |
| 1256 | `?_Init@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19810` | 71 | UnwindData |  |
| 1257 | `?_Init@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19860` | 32 | UnwindData |  |
| 1258 | `?_Init@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x19890` | 32 | UnwindData |  |
| 1264 | `?_Initcvt@?$basic_filebuf@DU?$char_traits@D@std@@@std@@IEAAXXZ` | `0x198C0` | 267 | UnwindData |  |
| 1265 | `?_Initcvt@?$basic_filebuf@GU?$char_traits@G@std@@@std@@IEAAXXZ` | `0x199E0` | 267 | UnwindData |  |
| 1266 | `?_Iput@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@KA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEAD_K@Z` | `0x19B00` | 786 | UnwindData |  |
| 1267 | `?_Iput@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@KA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEAD_K@Z` | `0x19E20` | 852 | UnwindData |  |
| 1275 | `?_Makpat@?$_Mpunct@D@std@@AEAAXAEAUpattern@money_base@2@DDD@Z` | `0x1A180` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1276 | `?_Makpat@?$_Mpunct@G@std@@AEAAXAEAUpattern@money_base@2@DDD@Z` | `0x1A1E0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1283 | `?_Nullstr@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@CAPEBDXZ` | `0x1A240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `?_Nullstr@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@CAPEBGXZ` | `0x1A250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `?_Pdif@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@CA_KPEBD0@Z` | `0x1A260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1286 | `?_Pdif@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@CA_KPEBG0@Z` | `0x1A280` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `?_Pninc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAPEADXZ` | `0x1A310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1288 | `?_Pninc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAPEAGXZ` | `0x1A330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `?_Psum@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@CAPEADPEAD_K@Z` | `0x1A350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `?_Psum@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@CAPEBDPEBD_K@Z` | `0x1A370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1291 | `?_Psum@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@CAPEAGPEAG_K@Z` | `0x1A390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1292 | `?_Psum@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@CAPEBGPEBG_K@Z` | `0x1A3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1293 | `?_Put@?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@CA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@PEBD_K@Z` | `0x1A3D0` | 88 | UnwindData |  |
| 1294 | `?_Put@?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@CA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@PEBG_K@Z` | `0x1A430` | 90 | UnwindData |  |
| 1295 | `?_Put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@KA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@PEBD_K@Z` | `0x1A490` | 88 | UnwindData |  |
| 1296 | `?_Put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@KA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@PEBG_K@Z` | `0x1A4F0` | 90 | UnwindData |  |
| 1297 | `?_Putc@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@KA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@PEBD_K@Z` | `0x1A550` | 88 | UnwindData |  |
| 1298 | `?_Putc@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@KA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@PEBD_K@Z` | `0x1A5B0` | 98 | UnwindData |  |
| 1299 | `?_Putmfld@?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@_NAEAVios_base@2@D1V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@@Z` | `0x1A620` | 2,121 | UnwindData |  |
| 1300 | `?_Putmfld@?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@_NAEAVios_base@2@G1V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@@Z` | `0x1AE70` | 2,270 | UnwindData |  |
| 1304 | `?_Refcnt@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAAAEAEPEBD@Z` | `0x1B760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1305 | `?_Refcnt@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAAAEAEPEBG@Z` | `0x1B770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1306 | `?_Rep@?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@CA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@D_K@Z` | `0x1B780` | 85 | UnwindData |  |
| 1307 | `?_Rep@?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@CA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@G_K@Z` | `0x1B7E0` | 86 | UnwindData |  |
| 1308 | `?_Rep@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@KA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@D_K@Z` | `0x1B840` | 85 | UnwindData |  |
| 1309 | `?_Rep@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@KA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@G_K@Z` | `0x1B8A0` | 86 | UnwindData |  |
| 1313 | `?_Split@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAAXXZ` | `0x1BF90` | 134 | UnwindData |  |
| 1314 | `?_Split@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAAXXZ` | `0x1C020` | 71 | UnwindData |  |
| 1318 | `?_Term@?$ctype@D@std@@KAXXZ` | `0x1C070` | 2,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `?_Tidy@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAAX_N@Z` | `0x1C9F0` | 70 | UnwindData |  |
| 1320 | `?_Tidy@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAAX_N@Z` | `0x1CA40` | 69 | UnwindData |  |
| 1334 | `?__Fiopen@std@@YAPEAU_iobuf@@PEBDH@Z` | `0x1CA90` | 143 | UnwindData |  |
| 1338 | `?always_noconv@codecvt_base@std@@QEBA_NXZ` | `0x1CB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1339 | `?append@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@AEBV12@@Z` | `0x1CB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1340 | `?append@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@AEBV12@_K1@Z` | `0x1CB70` | 188 | UnwindData |  |
| 1341 | `?append@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@PEBD0@Z` | `0x1CC40` | 195 | UnwindData |  |
| 1342 | `?append@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@PEBD@Z` | `0x1CD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1343 | `?append@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@PEBD_K@Z` | `0x1CD30` | 131 | UnwindData |  |
| 1344 | `?append@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_KD@Z` | `0x1CDC0` | 131 | UnwindData |  |
| 1345 | `?append@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@AEBV12@@Z` | `0x1CE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1346 | `?append@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@AEBV12@_K1@Z` | `0x1CE70` | 193 | UnwindData |  |
| 1347 | `?append@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@PEBG0@Z` | `0x1CF40` | 196 | UnwindData |  |
| 1348 | `?append@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@PEBG@Z` | `0x1D010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1349 | `?append@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@PEBG_K@Z` | `0x1D030` | 151 | UnwindData |  |
| 1350 | `?append@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_KG@Z` | `0x1D0D0` | 146 | UnwindData |  |
| 1354 | `?assign@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@AEBV12@@Z` | `0x1D170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `?assign@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@AEBV12@_K1@Z` | `0x1D190` | 310 | UnwindData |  |
| 1356 | `?assign@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@PEBD0@Z` | `0x1D2D0` | 179 | UnwindData |  |
| 1357 | `?assign@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@PEBD@Z` | `0x1D390` | 95 | UnwindData |  |
| 1358 | `?assign@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@PEBD_K@Z` | `0x1D400` | 85 | UnwindData |  |
| 1359 | `?assign@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_KD@Z` | `0x1D460` | 99 | UnwindData |  |
| 1360 | `?assign@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@AEBV12@@Z` | `0x1D4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1361 | `?assign@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@AEBV12@_K1@Z` | `0x1D4F0` | 309 | UnwindData |  |
| 1362 | `?assign@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@PEBG0@Z` | `0x1D630` | 179 | UnwindData |  |
| 1363 | `?assign@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@PEBG@Z` | `0x1D6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1364 | `?assign@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@PEBG_K@Z` | `0x1D710` | 114 | UnwindData |  |
| 1365 | `?assign@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_KG@Z` | `0x1D790` | 105 | UnwindData |  |
| 1366 | `?assign@?$char_traits@D@std@@SAPEADPEAD_KAEBD@Z` | `0x1D800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1367 | `?assign@?$char_traits@D@std@@SAXAEADAEBD@Z` | `0x1D820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1368 | `?assign@?$char_traits@G@std@@SAPEAGPEAG_KAEBG@Z` | `0x1D830` | 35 | UnwindData |  |
| 1369 | `?assign@?$char_traits@G@std@@SAXAEAGAEBG@Z` | `0x1D860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1370 | `?at@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAD_K@Z` | `0x1D870` | 91 | UnwindData |  |
| 1371 | `?at@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAAEBD_K@Z` | `0x1D8E0` | 45 | UnwindData |  |
| 1372 | `?at@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAG_K@Z` | `0x1D920` | 92 | UnwindData |  |
| 1373 | `?at@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAAEBG_K@Z` | `0x1D990` | 46 | UnwindData |  |
| 1377 | `?bad@ios_base@std@@QEBA_NXZ` | `0x1D9D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1378 | `?begin@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAPEADXZ` | `0x1D9E0` | 62 | UnwindData |  |
| 1379 | `?begin@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAPEBDXZ` | `0x1DA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1380 | `?begin@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAPEAGXZ` | `0x1DA40` | 62 | UnwindData |  |
| 1381 | `?begin@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAPEBGXZ` | `0x1DA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1382 | `?c_str@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAPEBDXZ` | `0x1DAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1383 | `?c_str@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAPEBGXZ` | `0x1DAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `?capacity@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KXZ` | `0x1DAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1385 | `?capacity@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KXZ` | `0x1DAF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1389 | `?classic_table@?$ctype@D@std@@KAPEBFXZ` | `0x1DB00` | 68 | UnwindData |  |
| 1390 | `?clear@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXF@Z` | `0x1DB50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1391 | `?clear@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXH_N@Z` | `0x1DB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1392 | `?clear@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXF@Z` | `0x1DB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1393 | `?clear@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXH_N@Z` | `0x1DBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1394 | `?clear@ios_base@std@@QEAAXF@Z` | `0x1DBD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1397 | `?close@?$basic_filebuf@DU?$char_traits@D@std@@@std@@QEAAPEAV12@XZ` | `0x1DBF0` | 58 | UnwindData |  |
| 1398 | `?close@?$basic_filebuf@GU?$char_traits@G@std@@@std@@QEAAPEAV12@XZ` | `0x1DC30` | 58 | UnwindData |  |
| 1399 | `?close@?$basic_fstream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x1DC70` | 106 | UnwindData |  |
| 1400 | `?close@?$basic_fstream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x1DCE0` | 106 | UnwindData |  |
| 1401 | `?close@?$basic_ifstream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x1DD50` | 106 | UnwindData |  |
| 1402 | `?close@?$basic_ifstream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x1DDC0` | 106 | UnwindData |  |
| 1403 | `?close@?$basic_ofstream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x1DE30` | 106 | UnwindData |  |
| 1404 | `?close@?$basic_ofstream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x1DEA0` | 106 | UnwindData |  |
| 1405 | `?close@?$messages@D@std@@QEBAXH@Z` | `0x1DF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1406 | `?close@?$messages@G@std@@QEBAXH@Z` | `0x1DF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `?compare@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAHAEBV12@@Z` | `0x1DF50` | 46 | UnwindData |  |
| 1408 | `?compare@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAHPEBD@Z` | `0x1DF90` | 41 | UnwindData |  |
| 1409 | `?compare@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAH_K0AEBV12@00@Z` | `0x1DFC0` | 137 | UnwindData |  |
| 1410 | `?compare@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAH_K0AEBV12@@Z` | `0x1E050` | 26 | UnwindData |  |
| 1411 | `?compare@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAH_K0PEBD0@Z` | `0x1E070` | 144 | UnwindData |  |
| 1412 | `?compare@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAH_K0PEBD@Z` | `0x1E110` | 33 | UnwindData |  |
| 1413 | `?compare@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAHAEBV12@@Z` | `0x1E140` | 46 | UnwindData |  |
| 1414 | `?compare@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAHPEBG@Z` | `0x1E180` | 42 | UnwindData |  |
| 1415 | `?compare@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAH_K0AEBV12@00@Z` | `0x1E1B0` | 138 | UnwindData |  |
| 1416 | `?compare@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAH_K0AEBV12@@Z` | `0x1E240` | 26 | UnwindData |  |
| 1417 | `?compare@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAH_K0PEBG0@Z` | `0x1E260` | 174 | UnwindData |  |
| 1418 | `?compare@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAH_K0PEBG@Z` | `0x1E320` | 34 | UnwindData |  |
| 1419 | `?compare@?$char_traits@D@std@@SAHPEBD0_K@Z` | `0x1E350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1420 | `?compare@?$char_traits@G@std@@SAHPEBG0_K@Z` | `0x1E360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1421 | `?compare@?$collate@D@std@@QEBAHPEBD000@Z` | `0x1E390` | 31 | UnwindData |  |
| 1422 | `?compare@?$collate@G@std@@QEBAHPEBG000@Z` | `0x1E3C0` | 31 | UnwindData |  |
| 1426 | `?copy@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEAD_K1@Z` | `0x1E3F0` | 104 | UnwindData |  |
| 1427 | `?copy@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEAG_K1@Z` | `0x1E460` | 106 | UnwindData |  |
| 1428 | `?copy@?$char_traits@D@std@@SAPEADPEADPEBD_K@Z` | `0x1E4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1429 | `?copy@?$char_traits@G@std@@SAPEAGPEAGPEBG_K@Z` | `0x1E4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `?copyfmt@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAAEAV12@AEBV12@@Z` | `0x1E4F0` | 37 | UnwindData |  |
| 1431 | `?copyfmt@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAAEAV12@AEBV12@@Z` | `0x1E520` | 39 | UnwindData |  |
| 1443 | `?curr_symbol@?$_Mpunct@D@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x1E550` | 30 | UnwindData |  |
| 1444 | `?curr_symbol@?$_Mpunct@G@std@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x1E580` | 30 | UnwindData |  |
| 1445 | `?data@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAPEBDXZ` | `0x1E5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1446 | `?data@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAPEBGXZ` | `0x1E5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1447 | `?date_order@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBAHXZ` | `0x1E5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `?date_order@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBAHXZ` | `0x1E610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1449 | `?decimal_point@?$_Mpunct@D@std@@QEBADXZ` | `0x1E630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1450 | `?decimal_point@?$_Mpunct@G@std@@QEBAGXZ` | `0x1E650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1451 | `?decimal_point@?$numpunct@D@std@@QEBADXZ` | `0x1E670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1452 | `?decimal_point@?$numpunct@G@std@@QEBAGXZ` | `0x1E690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1466 | `?do_always_noconv@?$codecvt@GDH@std@@MEBA_NXZ` | `0x1E6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1467 | `?do_always_noconv@codecvt_base@std@@MEBA_NXZ` | `0x1E6C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1468 | `?do_close@?$messages@D@std@@MEBAXH@Z` | `0x1E6D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1469 | `?do_close@?$messages@G@std@@MEBAXH@Z` | `0x1E6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1470 | `?do_compare@?$collate@D@std@@MEBAHPEBD000@Z` | `0x1E6F0` | 40 | UnwindData |  |
| 1471 | `?do_compare@?$collate@G@std@@MEBAHPEBG000@Z` | `0x1E720` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1472 | `?do_curr_symbol@?$_Mpunct@D@std@@MEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x1E770` | 35 | UnwindData |  |
| 1473 | `?do_curr_symbol@?$_Mpunct@G@std@@MEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x1E7A0` | 58 | UnwindData |  |
| 1474 | `?do_date_order@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBAHXZ` | `0x1E7E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1475 | `?do_date_order@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBAHXZ` | `0x1E7F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1476 | `?do_decimal_point@?$_Mpunct@D@std@@MEBADXZ` | `0x1E800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1477 | `?do_decimal_point@?$_Mpunct@G@std@@MEBAGXZ` | `0x1E810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1478 | `?do_decimal_point@?$numpunct@D@std@@MEBADXZ` | `0x1E820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `?do_decimal_point@?$numpunct@G@std@@MEBAGXZ` | `0x1E830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1480 | `?do_encoding@?$codecvt@GDH@std@@MEBAHXZ` | `0x1E840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1481 | `?do_encoding@codecvt_base@std@@MEBAHXZ` | `0x1E850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1482 | `?do_falsename@?$numpunct@D@std@@MEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x1E860` | 35 | UnwindData |  |
| 1483 | `?do_falsename@?$numpunct@G@std@@MEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x1E890` | 58 | UnwindData |  |
| 1484 | `?do_frac_digits@?$_Mpunct@D@std@@MEBAHXZ` | `0x1E8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1485 | `?do_frac_digits@?$_Mpunct@G@std@@MEBAHXZ` | `0x1E8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1486 | `?do_get@?$messages@D@std@@MEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@HHHAEBV32@@Z` | `0x1E8F0` | 90 | UnwindData |  |
| 1487 | `?do_get@?$messages@G@std@@MEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@HHHAEBV32@@Z` | `0x1E950` | 130 | UnwindData |  |
| 1488 | `?do_get@?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0_NAEAVios_base@2@AEAHAEAO@Z` | `0x1E9E0` | 450 | UnwindData |  |
| 1489 | `?do_get@?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0_NAEAVios_base@2@AEAHAEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@@Z` | `0x1EBB0` | 192 | UnwindData |  |
| 1490 | `?do_get@?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0_NAEAVios_base@2@AEAHAEAO@Z` | `0x1EC80` | 498 | UnwindData |  |
| 1491 | `?do_get@?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0_NAEAVios_base@2@AEAHAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@@Z` | `0x1EE80` | 225 | UnwindData |  |
| 1492 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x1EF70` | 319 | UnwindData |  |
| 1493 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x1F0C0` | 307 | UnwindData |  |
| 1494 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x1F200` | 282 | UnwindData |  |
| 1495 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x1F320` | 282 | UnwindData |  |
| 1496 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x1F440` | 276 | UnwindData |  |
| 1497 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x1F560` | 276 | UnwindData |  |
| 1498 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x1F680` | 276 | UnwindData |  |
| 1499 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x1F7A0` | 356 | UnwindData |  |
| 1500 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x1F910` | 258 | UnwindData |  |
| 1501 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x1FA20` | 258 | UnwindData |  |
| 1502 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x1FB30` | 701 | UnwindData |  |
| 1503 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x1FE00` | 358 | UnwindData |  |
| 1504 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x1FF70` | 346 | UnwindData |  |
| 1505 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x200D0` | 319 | UnwindData |  |
| 1506 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x20220` | 319 | UnwindData |  |
| 1507 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x20370` | 310 | UnwindData |  |
| 1508 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x204B0` | 310 | UnwindData |  |
| 1509 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x205F0` | 310 | UnwindData |  |
| 1510 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x20730` | 434 | UnwindData |  |
| 1511 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x208F0` | 292 | UnwindData |  |
| 1512 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x20A20` | 292 | UnwindData |  |
| 1513 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x20B50` | 730 | UnwindData |  |
| 1514 | `?do_get_date@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x20E30` | 373 | UnwindData |  |
| 1515 | `?do_get_date@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x20FB0` | 531 | UnwindData |  |
| 1516 | `?do_get_monthname@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x211D0` | 84 | UnwindData |  |
| 1517 | `?do_get_monthname@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x21230` | 84 | UnwindData |  |
| 1518 | `?do_get_time@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x21290` | 229 | UnwindData |  |
| 1519 | `?do_get_time@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x21380` | 280 | UnwindData |  |
| 1520 | `?do_get_weekday@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x214A0` | 84 | UnwindData |  |
| 1521 | `?do_get_weekday@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x21500` | 84 | UnwindData |  |
| 1522 | `?do_get_year@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x21560` | 140 | UnwindData |  |
| 1523 | `?do_get_year@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x21600` | 140 | UnwindData |  |
| 1524 | `?do_grouping@?$_Mpunct@D@std@@MEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x216A0` | 35 | UnwindData |  |
| 1525 | `?do_grouping@?$_Mpunct@G@std@@MEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x216D0` | 35 | UnwindData |  |
| 1526 | `?do_grouping@?$numpunct@D@std@@MEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x21700` | 35 | UnwindData |  |
| 1527 | `?do_grouping@?$numpunct@G@std@@MEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x21730` | 35 | UnwindData |  |
| 1528 | `?do_hash@?$collate@D@std@@MEBAJPEBD0@Z` | `0x21760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `?do_hash@?$collate@G@std@@MEBAJPEBG0@Z` | `0x21780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1530 | `?do_in@?$codecvt@DDH@std@@MEBAHAEAHPEBD1AEAPEBDPEAD3AEAPEAD@Z` | `0x217A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `?do_in@?$codecvt@GDH@std@@MEBAHAEAHPEBD1AEAPEBDPEAG3AEAPEAG@Z` | `0x217D0` | 197 | UnwindData |  |
| 1532 | `?do_is@?$ctype@G@std@@MEBAPEBGPEBG0PEAF@Z` | `0x218A0` | 124 | UnwindData |  |
| 1533 | `?do_is@?$ctype@G@std@@MEBA_NFG@Z` | `0x21930` | 65 | UnwindData |  |
| 1534 | `?do_length@?$codecvt@DDH@std@@MEBAHAEAHPEBD1_K@Z` | `0x21980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1535 | `?do_length@?$codecvt@GDH@std@@MEBAHAEAHPEBG1_K@Z` | `0x219A0` | 146 | UnwindData |  |
| 1536 | `?do_max_length@?$codecvt@GDH@std@@MEBAHXZ` | `0x21A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1537 | `?do_max_length@codecvt_base@std@@MEBAHXZ` | `0x21A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `?do_narrow@?$ctype@G@std@@MEBADGD@Z` | `0x21A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `?do_narrow@?$ctype@G@std@@MEBAPEBGPEBG0DPEAD@Z` | `0x21A70` | 73 | UnwindData |  |
| 1540 | `?do_neg_format@?$_Mpunct@D@std@@MEBA?AUpattern@money_base@2@XZ` | `0x21AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1541 | `?do_neg_format@?$_Mpunct@G@std@@MEBA?AUpattern@money_base@2@XZ` | `0x21AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1542 | `?do_negative_sign@?$_Mpunct@D@std@@MEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x21AE0` | 35 | UnwindData |  |
| 1543 | `?do_negative_sign@?$_Mpunct@G@std@@MEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x21B10` | 58 | UnwindData |  |
| 1544 | `?do_open@?$messages@D@std@@MEBAHAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@AEBVlocale@2@@Z` | `0x21B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1545 | `?do_open@?$messages@G@std@@MEBAHAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@AEBVlocale@2@@Z` | `0x21B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1546 | `?do_out@?$codecvt@DDH@std@@MEBAHAEAHPEBD1AEAPEBDPEAD3AEAPEAD@Z` | `0x21B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1547 | `?do_out@?$codecvt@GDH@std@@MEBAHAEAHPEBG1AEAPEBGPEAD3AEAPEAD@Z` | `0x21BA0` | 305 | UnwindData |  |
| 1548 | `?do_pos_format@?$_Mpunct@D@std@@MEBA?AUpattern@money_base@2@XZ` | `0x21CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1549 | `?do_pos_format@?$_Mpunct@G@std@@MEBA?AUpattern@money_base@2@XZ` | `0x21CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1550 | `?do_positive_sign@?$_Mpunct@D@std@@MEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x21D00` | 35 | UnwindData |  |
| 1551 | `?do_positive_sign@?$_Mpunct@G@std@@MEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x21D30` | 58 | UnwindData |  |
| 1552 | `?do_put@?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@_NAEAVios_base@2@DAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@@Z` | `0x21D70` | 428 | UnwindData |  |
| 1553 | `?do_put@?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@_NAEAVios_base@2@DO@Z` | `0x21F30` | 405 | UnwindData |  |
| 1554 | `?do_put@?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@_NAEAVios_base@2@GAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@@Z` | `0x220D0` | 429 | UnwindData |  |
| 1555 | `?do_put@?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@_NAEAVios_base@2@GO@Z` | `0x22290` | 429 | UnwindData |  |
| 1556 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DJ@Z` | `0x22450` | 156 | UnwindData |  |
| 1557 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DK@Z` | `0x22500` | 156 | UnwindData |  |
| 1558 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DN@Z` | `0x225B0` | 310 | UnwindData |  |
| 1559 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DO@Z` | `0x226F0` | 314 | UnwindData |  |
| 1560 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBX@Z` | `0x22830` | 266 | UnwindData |  |
| 1561 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_J@Z` | `0x22940` | 240 | UnwindData |  |
| 1562 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_K@Z` | `0x22A40` | 240 | UnwindData |  |
| 1563 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_N@Z` | `0x22B40` | 525 | UnwindData |  |
| 1564 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GJ@Z` | `0x22D60` | 157 | UnwindData |  |
| 1565 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GK@Z` | `0x22E10` | 157 | UnwindData |  |
| 1566 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GN@Z` | `0x22EC0` | 311 | UnwindData |  |
| 1567 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GO@Z` | `0x23000` | 315 | UnwindData |  |
| 1568 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBX@Z` | `0x23150` | 279 | UnwindData |  |
| 1569 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_J@Z` | `0x23270` | 241 | UnwindData |  |
| 1570 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_K@Z` | `0x23370` | 241 | UnwindData |  |
| 1571 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_N@Z` | `0x23470` | 538 | UnwindData |  |
| 1572 | `?do_put@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@PEBUtm@@DD@Z` | `0x23690` | 403 | UnwindData |  |
| 1573 | `?do_put@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@PEBUtm@@DD@Z` | `0x23830` | 413 | UnwindData |  |
| 1574 | `?do_scan_is@?$ctype@G@std@@MEBAPEBGFPEBG0@Z` | `0x239E0` | 96 | UnwindData |  |
| 1575 | `?do_scan_not@?$ctype@G@std@@MEBAPEBGFPEBG0@Z` | `0x23A50` | 96 | UnwindData |  |
| 1576 | `?do_thousands_sep@?$_Mpunct@D@std@@MEBADXZ` | `0x23AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1577 | `?do_thousands_sep@?$_Mpunct@G@std@@MEBAGXZ` | `0x23AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `?do_thousands_sep@?$numpunct@D@std@@MEBADXZ` | `0x23AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1579 | `?do_thousands_sep@?$numpunct@G@std@@MEBAGXZ` | `0x23AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1580 | `?do_tolower@?$ctype@D@std@@MEBADD@Z` | `0x23B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `?do_tolower@?$ctype@D@std@@MEBAPEBDPEADPEBD@Z` | `0x23B20` | 70 | UnwindData |  |
| 1582 | `?do_tolower@?$ctype@G@std@@MEBAGG@Z` | `0x23B70` | 58 | UnwindData |  |
| 1583 | `?do_tolower@?$ctype@G@std@@MEBAPEBGPEAGPEBG@Z` | `0x23BB0` | 72 | UnwindData |  |
| 1584 | `?do_toupper@?$ctype@D@std@@MEBADD@Z` | `0x23C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1585 | `?do_toupper@?$ctype@D@std@@MEBAPEBDPEADPEBD@Z` | `0x23C20` | 70 | UnwindData |  |
| 1586 | `?do_toupper@?$ctype@G@std@@MEBAGG@Z` | `0x23C70` | 58 | UnwindData |  |
| 1587 | `?do_toupper@?$ctype@G@std@@MEBAPEBGPEAGPEBG@Z` | `0x23CB0` | 72 | UnwindData |  |
| 1588 | `?do_transform@?$collate@D@std@@MEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@PEBD0@Z` | `0x23D00` | 275 | UnwindData |  |
| 1589 | `?do_transform@?$collate@G@std@@MEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@PEBG0@Z` | `0x23E20` | 281 | UnwindData |  |
| 1590 | `?do_truename@?$numpunct@D@std@@MEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x23F40` | 35 | UnwindData |  |
| 1591 | `?do_truename@?$numpunct@G@std@@MEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x23F70` | 58 | UnwindData |  |
| 1592 | `?do_widen@?$ctype@G@std@@MEBAGD@Z` | `0x23FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `?do_widen@?$ctype@G@std@@MEBAPEBDPEBD0PEAG@Z` | `0x23FC0` | 72 | UnwindData |  |
| 1594 | `?eback@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x24010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `?eback@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x24020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1596 | `?egptr@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x24030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1597 | `?egptr@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x24050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1598 | `?empty@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_NXZ` | `0x24070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1599 | `?empty@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_NXZ` | `0x24080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1601 | `?encoding@codecvt_base@std@@QEBAHXZ` | `0x24090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1602 | `?end@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAPEADXZ` | `0x240B0` | 78 | UnwindData |  |
| 1603 | `?end@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAPEBDXZ` | `0x24110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1604 | `?end@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAPEAGXZ` | `0x24130` | 79 | UnwindData |  |
| 1605 | `?end@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAPEBGXZ` | `0x24190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1606 | `?endl@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@1@AEAV21@@Z` | `0x241B0` | 33 | UnwindData |  |
| 1607 | `?endl@std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@1@AEAV21@@Z` | `0x241E0` | 36 | UnwindData |  |
| 1608 | `?ends@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@1@AEAV21@@Z` | `0x24210` | 25 | UnwindData |  |
| 1609 | `?ends@std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@1@AEAV21@@Z` | `0x24230` | 25 | UnwindData |  |
| 1610 | `?eof@?$char_traits@D@std@@SAHXZ` | `0x24250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1611 | `?eof@?$char_traits@G@std@@SAGXZ` | `0x24260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1612 | `?eof@ios_base@std@@QEBA_NXZ` | `0x24270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1613 | `?epptr@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x24280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1614 | `?epptr@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x242A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1628 | `?eq@?$char_traits@D@std@@SA_NAEBD0@Z` | `0x242C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1629 | `?eq@?$char_traits@G@std@@SA_NAEBG0@Z` | `0x242D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `?eq_int_type@?$char_traits@D@std@@SA_NAEBH0@Z` | `0x242E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1631 | `?eq_int_type@?$char_traits@G@std@@SA_NAEBG0@Z` | `0x242F0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1632 | `?erase@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_K0@Z` | `0x243F0` | 137 | UnwindData |  |
| 1633 | `?erase@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAPEADPEAD0@Z` | `0x24480` | 155 | UnwindData |  |
| 1634 | `?erase@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAPEADPEAD@Z` | `0x24530` | 120 | UnwindData |  |
| 1635 | `?erase@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_K0@Z` | `0x245B0` | 207 | UnwindData |  |
| 1636 | `?erase@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAPEAGPEAG0@Z` | `0x24690` | 161 | UnwindData |  |
| 1637 | `?erase@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAPEAGPEAG@Z` | `0x24740` | 123 | UnwindData |  |
| 1638 | `?exceptions@ios_base@std@@QEAAXF@Z` | `0x247D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1639 | `?exceptions@ios_base@std@@QEAAXH@Z` | `0x247F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1640 | `?exceptions@ios_base@std@@QEBAHXZ` | `0x24810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1647 | `?fail@ios_base@std@@QEBA_NXZ` | `0x24820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1648 | `?falsename@?$numpunct@D@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x24830` | 30 | UnwindData |  |
| 1649 | `?falsename@?$numpunct@G@std@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x24860` | 30 | UnwindData |  |
| 1650 | `?fill@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAADD@Z` | `0x24890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1651 | `?fill@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBADXZ` | `0x248A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1652 | `?fill@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAGG@Z` | `0x248B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1653 | `?fill@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBAGXZ` | `0x248C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1654 | `?find@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KAEBV12@_K@Z` | `0x248D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1655 | `?find@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KD_K@Z` | `0x24900` | 29 | UnwindData |  |
| 1656 | `?find@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEBD_K1@Z` | `0x24930` | 181 | UnwindData |  |
| 1657 | `?find@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEBD_K@Z` | `0x249F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1658 | `?find@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KAEBV12@_K@Z` | `0x24A10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1659 | `?find@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KG_K@Z` | `0x24A40` | 30 | UnwindData |  |
| 1660 | `?find@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEBG_K1@Z` | `0x24A70` | 204 | UnwindData |  |
| 1661 | `?find@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEBG_K@Z` | `0x24B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1662 | `?find@?$char_traits@D@std@@SAPEBDPEBD_KAEBD@Z` | `0x24B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1663 | `?find@?$char_traits@G@std@@SAPEBGPEBG_KAEBG@Z` | `0x24B90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1664 | `?find_first_not_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KAEBV12@_K@Z` | `0x24BC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1665 | `?find_first_not_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KD_K@Z` | `0x24BF0` | 29 | UnwindData |  |
| 1666 | `?find_first_not_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEBD_K1@Z` | `0x24C20` | 120 | UnwindData |  |
| 1667 | `?find_first_not_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEBD_K@Z` | `0x24CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `?find_first_not_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KAEBV12@_K@Z` | `0x24CC0` | 112 | UnwindData |  |
| 1669 | `?find_first_not_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KG_K@Z` | `0x24D40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1670 | `?find_first_not_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEBG_K1@Z` | `0x24DA0` | 94 | UnwindData |  |
| 1671 | `?find_first_not_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEBG_K@Z` | `0x24E10` | 120 | UnwindData |  |
| 1672 | `?find_first_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KAEBV12@_K@Z` | `0x24E90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1673 | `?find_first_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KD_K@Z` | `0x24EC0` | 29 | UnwindData |  |
| 1674 | `?find_first_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEBD_K1@Z` | `0x24EF0` | 125 | UnwindData |  |
| 1675 | `?find_first_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEBD_K@Z` | `0x24F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1676 | `?find_first_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KAEBV12@_K@Z` | `0x24FA0` | 114 | UnwindData |  |
| 1677 | `?find_first_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KG_K@Z` | `0x25020` | 30 | UnwindData |  |
| 1678 | `?find_first_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEBG_K1@Z` | `0x25050` | 96 | UnwindData |  |
| 1679 | `?find_first_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEBG_K@Z` | `0x250C0` | 122 | UnwindData |  |
| 1680 | `?find_last_not_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KAEBV12@_K@Z` | `0x25140` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1681 | `?find_last_not_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KD_K@Z` | `0x25170` | 29 | UnwindData |  |
| 1682 | `?find_last_not_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEBD_K1@Z` | `0x251A0` | 114 | UnwindData |  |
| 1683 | `?find_last_not_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEBD_K@Z` | `0x25220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1684 | `?find_last_not_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KAEBV12@_K@Z` | `0x25240` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1685 | `?find_last_not_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KG_K@Z` | `0x252C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `?find_last_not_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEBG_K1@Z` | `0x25320` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1687 | `?find_last_not_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEBG_K@Z` | `0x25390` | 121 | UnwindData |  |
| 1688 | `?find_last_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KAEBV12@_K@Z` | `0x25410` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1689 | `?find_last_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KD_K@Z` | `0x25440` | 29 | UnwindData |  |
| 1690 | `?find_last_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEBD_K1@Z` | `0x25470` | 119 | UnwindData |  |
| 1691 | `?find_last_of@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEBD_K@Z` | `0x254F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1692 | `?find_last_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KAEBV12@_K@Z` | `0x25510` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1693 | `?find_last_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KG_K@Z` | `0x25590` | 30 | UnwindData |  |
| 1694 | `?find_last_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEBG_K1@Z` | `0x255C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1695 | `?find_last_of@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEBG_K@Z` | `0x25630` | 117 | UnwindData |  |
| 1696 | `?flags@ios_base@std@@QEAAHH@Z` | `0x256B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1697 | `?flags@ios_base@std@@QEBAHXZ` | `0x256D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1698 | `?flush@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@XZ` | `0x256E0` | 118 | UnwindData |  |
| 1699 | `?flush@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@XZ` | `0x25760` | 118 | UnwindData |  |
| 1700 | `?flush@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@1@AEAV21@@Z` | `0x257E0` | 23 | UnwindData |  |
| 1701 | `?flush@std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@1@AEAV21@@Z` | `0x25800` | 23 | UnwindData |  |
| 1702 | `?frac_digits@?$_Mpunct@D@std@@QEBAHXZ` | `0x25820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1703 | `?frac_digits@?$_Mpunct@G@std@@QEBAHXZ` | `0x25840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1705 | `?gbump@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXH@Z` | `0x25860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1706 | `?gbump@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXH@Z` | `0x25880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1707 | `?gcount@?$basic_istream@DU?$char_traits@D@std@@@std@@QEBA_JXZ` | `0x258A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1708 | `?gcount@?$basic_istream@GU?$char_traits@G@std@@@std@@QEBA_JXZ` | `0x258B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1709 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@AEAD@Z` | `0x258C0` | 42 | UnwindData |  |
| 1710 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@@Z` | `0x258F0` | 57 | UnwindData |  |
| 1711 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@D@Z` | `0x25930` | 368 | UnwindData |  |
| 1712 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_J@Z` | `0x25AB0` | 73 | UnwindData |  |
| 1713 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_JD@Z` | `0x25B00` | 305 | UnwindData |  |
| 1714 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x25C40` | 225 | UnwindData |  |
| 1715 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@AEAG@Z` | `0x25D30` | 48 | UnwindData |  |
| 1716 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@@Z` | `0x25D70` | 58 | UnwindData |  |
| 1717 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@G@Z` | `0x25DB0` | 382 | UnwindData |  |
| 1718 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_J@Z` | `0x25F40` | 74 | UnwindData |  |
| 1719 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_JG@Z` | `0x25F90` | 334 | UnwindData |  |
| 1720 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x260F0` | 263 | UnwindData |  |
| 1721 | `?get@?$messages@D@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@HHHAEBV32@@Z` | `0x26200` | 56 | UnwindData |  |
| 1722 | `?get@?$messages@G@std@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@HHHAEBV32@@Z` | `0x26240` | 56 | UnwindData |  |
| 1723 | `?get@?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0_NAEAVios_base@2@AEAHAEAO@Z` | `0x26280` | 113 | UnwindData |  |
| 1724 | `?get@?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0_NAEAVios_base@2@AEAHAEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@@Z` | `0x26300` | 113 | UnwindData |  |
| 1725 | `?get@?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0_NAEAVios_base@2@AEAHAEAO@Z` | `0x26380` | 113 | UnwindData |  |
| 1726 | `?get@?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0_NAEAVios_base@2@AEAHAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@@Z` | `0x26400` | 113 | UnwindData |  |
| 1727 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x26480` | 96 | UnwindData |  |
| 1728 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x264F0` | 96 | UnwindData |  |
| 1729 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x26560` | 96 | UnwindData |  |
| 1730 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x265D0` | 96 | UnwindData |  |
| 1731 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x26640` | 96 | UnwindData |  |
| 1732 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x266B0` | 96 | UnwindData |  |
| 1733 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x26720` | 96 | UnwindData |  |
| 1734 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x26790` | 96 | UnwindData |  |
| 1735 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x26800` | 96 | UnwindData |  |
| 1736 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x26870` | 96 | UnwindData |  |
| 1737 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x268E0` | 96 | UnwindData |  |
| 1738 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x26950` | 96 | UnwindData |  |
| 1739 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x269C0` | 96 | UnwindData |  |
| 1740 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x26A30` | 96 | UnwindData |  |
| 1741 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x26AA0` | 96 | UnwindData |  |
| 1742 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x26B10` | 96 | UnwindData |  |
| 1743 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x26B80` | 96 | UnwindData |  |
| 1744 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x26BF0` | 96 | UnwindData |  |
| 1745 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x26C60` | 96 | UnwindData |  |
| 1746 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x26CD0` | 96 | UnwindData |  |
| 1747 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x26D40` | 96 | UnwindData |  |
| 1748 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x26DB0` | 96 | UnwindData |  |
| 1749 | `?get_allocator@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA?AV?$allocator@D@2@XZ` | `0x26E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1750 | `?get_allocator@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA?AV?$allocator@G@2@XZ` | `0x26E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1751 | `?get_date@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x26E40` | 96 | UnwindData |  |
| 1752 | `?get_date@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x26EB0` | 96 | UnwindData |  |
| 1753 | `?get_monthname@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x26F20` | 96 | UnwindData |  |
| 1754 | `?get_monthname@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x26F90` | 96 | UnwindData |  |
| 1755 | `?get_time@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x27000` | 96 | UnwindData |  |
| 1756 | `?get_time@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x27070` | 96 | UnwindData |  |
| 1757 | `?get_weekday@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x270E0` | 96 | UnwindData |  |
| 1758 | `?get_weekday@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x27150` | 96 | UnwindData |  |
| 1759 | `?get_year@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x271C0` | 96 | UnwindData |  |
| 1760 | `?get_year@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x27230` | 96 | UnwindData |  |
| 1761 | `?getline@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_J@Z` | `0x272A0` | 73 | UnwindData |  |
| 1762 | `?getline@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_JD@Z` | `0x272F0` | 391 | UnwindData |  |
| 1763 | `?getline@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_J@Z` | `0x27480` | 74 | UnwindData |  |
| 1764 | `?getline@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_JG@Z` | `0x274D0` | 420 | UnwindData |  |
| 1769 | `?getloc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AVlocale@2@XZ` | `0x27680` | 85 | UnwindData |  |
| 1770 | `?getloc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AVlocale@2@XZ` | `0x276E0` | 85 | UnwindData |  |
| 1771 | `?getloc@ios_base@std@@QEBA?AVlocale@2@XZ` | `0x27740` | 85 | UnwindData |  |
| 1773 | `?good@ios_base@std@@QEBA_NXZ` | `0x277A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1774 | `?gptr@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x277B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1775 | `?gptr@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x277C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1776 | `?grouping@?$_Mpunct@D@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x277D0` | 30 | UnwindData |  |
| 1777 | `?grouping@?$_Mpunct@G@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x27800` | 30 | UnwindData |  |
| 1778 | `?grouping@?$numpunct@D@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x27830` | 30 | UnwindData |  |
| 1779 | `?grouping@?$numpunct@G@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x27860` | 30 | UnwindData |  |
| 1780 | `?hash@?$collate@D@std@@QEBAJPEBD0@Z` | `0x27890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1781 | `?hash@?$collate@G@std@@QEBAJPEBG0@Z` | `0x278B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1808 | `?ignore@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@_JH@Z` | `0x278D0` | 250 | UnwindData |  |
| 1809 | `?ignore@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@_JG@Z` | `0x279D0` | 266 | UnwindData |  |
| 1819 | `?imbue@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x27AE0` | 90 | UnwindData |  |
| 1820 | `?imbue@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x27B40` | 90 | UnwindData |  |
| 1821 | `?imbue@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAXAEBVlocale@2@@Z` | `0x27BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1822 | `?imbue@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAXAEBVlocale@2@@Z` | `0x27BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1824 | `?in@?$codecvt@DDH@std@@QEBAHAEAHPEBD1AEAPEBDPEAD3AEAPEAD@Z` | `0x27BC0` | 79 | UnwindData |  |
| 1825 | `?in@?$codecvt@GDH@std@@QEBAHAEAHPEBD1AEAPEBDPEAG3AEAPEAG@Z` | `0x27C20` | 79 | UnwindData |  |
| 1826 | `?in_avail@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA_JXZ` | `0x27C80` | 55 | UnwindData |  |
| 1827 | `?in_avail@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA_JXZ` | `0x27CC0` | 63 | UnwindData |  |
| 1841 | `?init@?$basic_ios@DU?$char_traits@D@std@@@std@@IEAAXPEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@_N@Z` | `0x27D10` | 82 | UnwindData |  |
| 1842 | `?init@?$basic_ios@GU?$char_traits@G@std@@@std@@IEAAXPEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@_N@Z` | `0x27D70` | 96 | UnwindData |  |
| 1843 | `?insert@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_K0D@Z` | `0x27DE0` | 179 | UnwindData |  |
| 1844 | `?insert@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_KAEBV12@00@Z` | `0x27EA0` | 241 | UnwindData |  |
| 1845 | `?insert@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_KAEBV12@@Z` | `0x27FA0` | 23 | UnwindData |  |
| 1846 | `?insert@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_KPEBD0@Z` | `0x27FC0` | 179 | UnwindData |  |
| 1847 | `?insert@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_KPEBD@Z` | `0x28080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1848 | `?insert@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAPEADPEADD@Z` | `0x280A0` | 172 | UnwindData |  |
| 1849 | `?insert@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXPEADPEBD1@Z` | `0x28160` | 25 | UnwindData |  |
| 1850 | `?insert@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXPEAD_KD@Z` | `0x28180` | 125 | UnwindData |  |
| 1851 | `?insert@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_K0G@Z` | `0x28210` | 187 | UnwindData |  |
| 1852 | `?insert@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_KAEBV12@00@Z` | `0x282E0` | 254 | UnwindData |  |
| 1853 | `?insert@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_KAEBV12@@Z` | `0x283F0` | 23 | UnwindData |  |
| 1854 | `?insert@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_KPEBG0@Z` | `0x28410` | 189 | UnwindData |  |
| 1855 | `?insert@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_KPEBG@Z` | `0x284E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1856 | `?insert@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAPEAGPEAGG@Z` | `0x28500` | 178 | UnwindData |  |
| 1857 | `?insert@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXPEAGPEBG1@Z` | `0x285C0` | 25 | UnwindData |  |
| 1858 | `?insert@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXPEAG_KG@Z` | `0x285E0` | 130 | UnwindData |  |
| 1863 | `?ipfx@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA_N_N@Z` | `0x28670` | 335 | UnwindData |  |
| 1864 | `?ipfx@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA_N_N@Z` | `0x287D0` | 362 | UnwindData |  |
| 1865 | `?is@?$ctype@D@std@@QEBAPEBDPEBD0PEAF@Z` | `0x28940` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1866 | `?is@?$ctype@D@std@@QEBA_NFD@Z` | `0x28970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1867 | `?is@?$ctype@G@std@@QEBAPEBGPEBG0PEAF@Z` | `0x28990` | 21 | UnwindData |  |
| 1868 | `?is@?$ctype@G@std@@QEBA_NFG@Z` | `0x289B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1869 | `?is_open@?$basic_filebuf@DU?$char_traits@D@std@@@std@@QEBA_NXZ` | `0x289D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1870 | `?is_open@?$basic_filebuf@GU?$char_traits@G@std@@@std@@QEBA_NXZ` | `0x289F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1871 | `?is_open@?$basic_fstream@DU?$char_traits@D@std@@@std@@QEBA_NXZ` | `0x28A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1872 | `?is_open@?$basic_fstream@GU?$char_traits@G@std@@@std@@QEBA_NXZ` | `0x28A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1873 | `?is_open@?$basic_ifstream@DU?$char_traits@D@std@@@std@@QEBA_NXZ` | `0x28A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1874 | `?is_open@?$basic_ifstream@GU?$char_traits@G@std@@@std@@QEBA_NXZ` | `0x28A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1875 | `?is_open@?$basic_ofstream@DU?$char_traits@D@std@@@std@@QEBA_NXZ` | `0x28A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1876 | `?is_open@?$basic_ofstream@GU?$char_traits@G@std@@@std@@QEBA_NXZ` | `0x28AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1877 | `?isfx@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x28AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1878 | `?isfx@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x28AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1879 | `?iword@ios_base@std@@QEAAAEAJH@Z` | `0x28AF0` | 18 | UnwindData |  |
| 1883 | `?length@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KXZ` | `0x28B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1884 | `?length@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KXZ` | `0x28B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1885 | `?length@?$char_traits@D@std@@SA_KPEBD@Z` | `0x28B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1886 | `?length@?$char_traits@G@std@@SA_KPEBG@Z` | `0x28B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1887 | `?length@?$codecvt@DDH@std@@QEBAHAEAHPEBD1_K@Z` | `0x28B70` | 31 | UnwindData |  |
| 1888 | `?length@?$codecvt@GDH@std@@QEBAHAEAHPEBG1_K@Z` | `0x28BA0` | 31 | UnwindData |  |
| 1898 | `?lt@?$char_traits@D@std@@SA_NAEBD0@Z` | `0x28BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1899 | `?lt@?$char_traits@G@std@@SA_NAEBG0@Z` | `0x28BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1913 | `?max_length@codecvt_base@std@@QEBAHXZ` | `0x28BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1914 | `?max_size@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KXZ` | `0x28C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1915 | `?max_size@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KXZ` | `0x28C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1929 | `?move@?$char_traits@D@std@@SAPEADPEADPEBD_K@Z` | `0x28C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1930 | `?move@?$char_traits@G@std@@SAPEAGPEAGPEBG_K@Z` | `0x28C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1931 | `?name@locale@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x28C60` | 54 | UnwindData |  |
| 1932 | `?narrow@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBADDD@Z` | `0x28CA0` | 108 | UnwindData |  |
| 1933 | `?narrow@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBADGD@Z` | `0x28D20` | 140 | UnwindData |  |
| 1934 | `?narrow@?$ctype@D@std@@QEBADDD@Z` | `0x28DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1935 | `?narrow@?$ctype@D@std@@QEBAPEBDPEBD0DPEAD@Z` | `0x28DD0` | 31 | UnwindData |  |
| 1936 | `?narrow@?$ctype@G@std@@QEBADGD@Z` | `0x28E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1937 | `?narrow@?$ctype@G@std@@QEBAPEBGPEBG0DPEAD@Z` | `0x28E20` | 31 | UnwindData |  |
| 1938 | `?neg_format@?$_Mpunct@D@std@@QEBA?AUpattern@money_base@2@XZ` | `0x28E50` | 30 | UnwindData |  |
| 1939 | `?neg_format@?$_Mpunct@G@std@@QEBA?AUpattern@money_base@2@XZ` | `0x28E80` | 30 | UnwindData |  |
| 1940 | `?negative_sign@?$_Mpunct@D@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x28EB0` | 30 | UnwindData |  |
| 1941 | `?negative_sign@?$_Mpunct@G@std@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x28EE0` | 30 | UnwindData |  |
| 1945 | `?not_eof@?$char_traits@D@std@@SAHAEBH@Z` | `0x28F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1946 | `?not_eof@?$char_traits@G@std@@SAGAEBG@Z` | `0x28F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1950 | `?open@?$basic_filebuf@DU?$char_traits@D@std@@@std@@QEAAPEAV12@PEBDF@Z` | `0x28F50` | 77 | UnwindData |  |
| 1951 | `?open@?$basic_filebuf@DU?$char_traits@D@std@@@std@@QEAAPEAV12@PEBDH@Z` | `0x28FB0` | 76 | UnwindData |  |
| 1952 | `?open@?$basic_filebuf@GU?$char_traits@G@std@@@std@@QEAAPEAV12@PEBDF@Z` | `0x29010` | 77 | UnwindData |  |
| 1953 | `?open@?$basic_filebuf@GU?$char_traits@G@std@@@std@@QEAAPEAV12@PEBDH@Z` | `0x29070` | 76 | UnwindData |  |
| 1954 | `?open@?$basic_fstream@DU?$char_traits@D@std@@@std@@QEAAXPEBDF@Z` | `0x290D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1955 | `?open@?$basic_fstream@DU?$char_traits@D@std@@@std@@QEAAXPEBDH@Z` | `0x290E0` | 124 | UnwindData |  |
| 1956 | `?open@?$basic_fstream@GU?$char_traits@G@std@@@std@@QEAAXPEBDF@Z` | `0x29170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1957 | `?open@?$basic_fstream@GU?$char_traits@G@std@@@std@@QEAAXPEBDH@Z` | `0x29180` | 124 | UnwindData |  |
| 1958 | `?open@?$basic_ifstream@DU?$char_traits@D@std@@@std@@QEAAXPEBDF@Z` | `0x29210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1959 | `?open@?$basic_ifstream@DU?$char_traits@D@std@@@std@@QEAAXPEBDH@Z` | `0x29220` | 128 | UnwindData |  |
| 1960 | `?open@?$basic_ifstream@GU?$char_traits@G@std@@@std@@QEAAXPEBDF@Z` | `0x292B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1961 | `?open@?$basic_ifstream@GU?$char_traits@G@std@@@std@@QEAAXPEBDH@Z` | `0x292C0` | 128 | UnwindData |  |
| 1962 | `?open@?$basic_ofstream@DU?$char_traits@D@std@@@std@@QEAAXPEBDF@Z` | `0x29350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1963 | `?open@?$basic_ofstream@DU?$char_traits@D@std@@@std@@QEAAXPEBDH@Z` | `0x29360` | 128 | UnwindData |  |
| 1964 | `?open@?$basic_ofstream@GU?$char_traits@G@std@@@std@@QEAAXPEBDF@Z` | `0x293F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1965 | `?open@?$basic_ofstream@GU?$char_traits@G@std@@@std@@QEAAXPEBDH@Z` | `0x29400` | 128 | UnwindData |  |
| 1966 | `?open@?$messages@D@std@@QEBAHAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@AEBVlocale@2@@Z` | `0x29490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1967 | `?open@?$messages@G@std@@QEBAHAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@AEBVlocale@2@@Z` | `0x294B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1968 | `?opfx@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA_NXZ` | `0x294D0` | 59 | UnwindData |  |
| 1969 | `?opfx@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA_NXZ` | `0x29520` | 59 | UnwindData |  |
| 1970 | `?osfx@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x29570` | 28 | UnwindData |  |
| 1971 | `?osfx@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x295A0` | 28 | UnwindData |  |
| 1972 | `?out@?$codecvt@DDH@std@@QEBAHAEAHPEBD1AEAPEBDPEAD3AEAPEAD@Z` | `0x295D0` | 79 | UnwindData |  |
| 1973 | `?out@?$codecvt@GDH@std@@QEBAHAEAHPEBG1AEAPEBGPEAD3AEAPEAD@Z` | `0x29630` | 79 | UnwindData |  |
| 1974 | `?overflow@?$basic_filebuf@DU?$char_traits@D@std@@@std@@MEAAHH@Z` | `0x29690` | 611 | UnwindData |  |
| 1975 | `?overflow@?$basic_filebuf@GU?$char_traits@G@std@@@std@@MEAAGG@Z` | `0x29900` | 633 | UnwindData |  |
| 1976 | `?overflow@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHH@Z` | `0x29B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1977 | `?overflow@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAGG@Z` | `0x29B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1981 | `?pbackfail@?$basic_filebuf@DU?$char_traits@D@std@@@std@@MEAAHH@Z` | `0x29BA0` | 289 | UnwindData |  |
| 1982 | `?pbackfail@?$basic_filebuf@GU?$char_traits@G@std@@@std@@MEAAGG@Z` | `0x29CD0` | 300 | UnwindData |  |
| 1983 | `?pbackfail@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHH@Z` | `0x29E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1984 | `?pbackfail@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAGG@Z` | `0x29E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1988 | `?pbase@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x29E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1989 | `?pbase@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x29E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1990 | `?pbump@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXH@Z` | `0x29E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1991 | `?pbump@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXH@Z` | `0x29E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1992 | `?peek@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x29E90` | 215 | UnwindData |  |
| 1993 | `?peek@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x29F70` | 231 | UnwindData |  |
| 2000 | `?pos_format@?$_Mpunct@D@std@@QEBA?AUpattern@money_base@2@XZ` | `0x2A060` | 30 | UnwindData |  |
| 2001 | `?pos_format@?$_Mpunct@G@std@@QEBA?AUpattern@money_base@2@XZ` | `0x2A090` | 30 | UnwindData |  |
| 2002 | `?positive_sign@?$_Mpunct@D@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x2A0C0` | 30 | UnwindData |  |
| 2003 | `?positive_sign@?$_Mpunct@G@std@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x2A0F0` | 30 | UnwindData |  |
| 2019 | `?pptr@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x2A120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2020 | `?pptr@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x2A130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2021 | `?precision@ios_base@std@@QEAA_JH@Z` | `0x2A140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2022 | `?precision@ios_base@std@@QEBA_JXZ` | `0x2A150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2023 | `?pubimbue@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x2A160` | 149 | UnwindData |  |
| 2024 | `?pubimbue@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x2A200` | 149 | UnwindData |  |
| 2025 | `?pubseekoff@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@H@2@_JFF@Z` | `0x2A2A0` | 45 | UnwindData |  |
| 2026 | `?pubseekoff@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@H@2@_JW4seekdir@ios_base@2@H@Z` | `0x2A2E0` | 40 | UnwindData |  |
| 2027 | `?pubseekoff@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@H@2@_JFF@Z` | `0x2A310` | 45 | UnwindData |  |
| 2028 | `?pubseekoff@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@H@2@_JW4seekdir@ios_base@2@H@Z` | `0x2A350` | 40 | UnwindData |  |
| 2029 | `?pubseekpos@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@H@2@V32@F@Z` | `0x2A380` | 60 | UnwindData |  |
| 2030 | `?pubseekpos@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@H@2@V32@H@Z` | `0x2A3D0` | 56 | UnwindData |  |
| 2031 | `?pubseekpos@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@H@2@V32@F@Z` | `0x2A410` | 60 | UnwindData |  |
| 2032 | `?pubseekpos@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@H@2@V32@H@Z` | `0x2A460` | 56 | UnwindData |  |
| 2033 | `?pubsetbuf@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAPEAV12@PEAD_J@Z` | `0x2A4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2034 | `?pubsetbuf@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAPEAV12@PEAG_J@Z` | `0x2A4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2035 | `?pubsync@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x2A4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2036 | `?pubsync@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAHXZ` | `0x2A500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2037 | `?put@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@D@Z` | `0x2A520` | 291 | UnwindData |  |
| 2038 | `?put@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@G@Z` | `0x2A650` | 302 | UnwindData |  |
| 2039 | `?put@?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@_NAEAVios_base@2@DAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@@Z` | `0x2A790` | 82 | UnwindData |  |
| 2040 | `?put@?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@_NAEAVios_base@2@DO@Z` | `0x2A7F0` | 86 | UnwindData |  |
| 2041 | `?put@?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@_NAEAVios_base@2@GAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@@Z` | `0x2A850` | 84 | UnwindData |  |
| 2042 | `?put@?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@_NAEAVios_base@2@GO@Z` | `0x2A8B0` | 88 | UnwindData |  |
| 2043 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DJ@Z` | `0x2A910` | 71 | UnwindData |  |
| 2044 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DK@Z` | `0x2A960` | 71 | UnwindData |  |
| 2045 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DN@Z` | `0x2A9B0` | 73 | UnwindData |  |
| 2046 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DO@Z` | `0x2AA00` | 73 | UnwindData |  |
| 2047 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBX@Z` | `0x2AA50` | 71 | UnwindData |  |
| 2048 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_J@Z` | `0x2AAA0` | 71 | UnwindData |  |
| 2049 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_K@Z` | `0x2AAF0` | 71 | UnwindData |  |
| 2050 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_N@Z` | `0x2AB40` | 71 | UnwindData |  |
| 2051 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GJ@Z` | `0x2AB90` | 73 | UnwindData |  |
| 2052 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GK@Z` | `0x2ABE0` | 73 | UnwindData |  |
| 2053 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GN@Z` | `0x2AC30` | 75 | UnwindData |  |
| 2054 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GO@Z` | `0x2AC90` | 75 | UnwindData |  |
| 2055 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBX@Z` | `0x2ACF0` | 73 | UnwindData |  |
| 2056 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_J@Z` | `0x2AD40` | 73 | UnwindData |  |
| 2057 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_K@Z` | `0x2AD90` | 73 | UnwindData |  |
| 2058 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_N@Z` | `0x2ADE0` | 73 | UnwindData |  |
| 2059 | `?put@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@PEBUtm@@DD@Z` | `0x2AE30` | 82 | UnwindData |  |
| 2060 | `?put@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@PEBUtm@@PEBD3@Z` | `0x2AE90` | 296 | UnwindData |  |
| 2061 | `?put@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@PEBUtm@@DD@Z` | `0x2AFC0` | 82 | UnwindData |  |
| 2062 | `?put@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@PEBUtm@@PEBG3@Z` | `0x2B020` | 345 | UnwindData |  |
| 2063 | `?putback@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@D@Z` | `0x2B180` | 225 | UnwindData |  |
| 2064 | `?putback@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@G@Z` | `0x2B270` | 229 | UnwindData |  |
| 2065 | `?pword@ios_base@std@@QEAAAEAPEAXH@Z` | `0x2B360` | 18 | UnwindData |  |
| 2079 | `?rbegin@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA?AV?$reverse_iterator@PEADDAEADPEAD_J@2@XZ` | `0x2B380` | 96 | UnwindData |  |
| 2080 | `?rbegin@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA?AV?$reverse_iterator@PEBDDAEBDPEBD_J@2@XZ` | `0x2B3F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2081 | `?rbegin@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA?AV?$reverse_iterator@PEAGGAEAGPEAG_J@2@XZ` | `0x2B420` | 97 | UnwindData |  |
| 2082 | `?rbegin@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA?AV?$reverse_iterator@PEBGGAEBGPEBG_J@2@XZ` | `0x2B490` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2083 | `?rdbuf@?$basic_fstream@DU?$char_traits@D@std@@@std@@QEBAPEAV?$basic_filebuf@DU?$char_traits@D@std@@@2@XZ` | `0x2B4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2084 | `?rdbuf@?$basic_fstream@GU?$char_traits@G@std@@@std@@QEBAPEAV?$basic_filebuf@GU?$char_traits@G@std@@@2@XZ` | `0x2B4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2085 | `?rdbuf@?$basic_ifstream@DU?$char_traits@D@std@@@std@@QEBAPEAV?$basic_filebuf@DU?$char_traits@D@std@@@2@XZ` | `0x2B4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2086 | `?rdbuf@?$basic_ifstream@GU?$char_traits@G@std@@@std@@QEBAPEAV?$basic_filebuf@GU?$char_traits@G@std@@@2@XZ` | `0x2B4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2087 | `?rdbuf@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAPEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@PEAV32@@Z` | `0x2B500` | 41 | UnwindData |  |
| 2088 | `?rdbuf@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBAPEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@XZ` | `0x2B530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2089 | `?rdbuf@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAPEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@PEAV32@@Z` | `0x2B540` | 41 | UnwindData |  |
| 2090 | `?rdbuf@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBAPEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@XZ` | `0x2B570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2093 | `?rdbuf@?$basic_ofstream@DU?$char_traits@D@std@@@std@@QEBAPEAV?$basic_filebuf@DU?$char_traits@D@std@@@2@XZ` | `0x2B580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2094 | `?rdbuf@?$basic_ofstream@GU?$char_traits@G@std@@@std@@QEBAPEAV?$basic_filebuf@GU?$char_traits@G@std@@@2@XZ` | `0x2B590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2099 | `?rdstate@ios_base@std@@QEBAHXZ` | `0x2B5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2100 | `?read@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_J@Z` | `0x2B5B0` | 172 | UnwindData |  |
| 2101 | `?read@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_J@Z` | `0x2B670` | 172 | UnwindData |  |
| 2102 | `?readsome@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA_JPEAD_J@Z` | `0x2B730` | 205 | UnwindData |  |
| 2103 | `?readsome@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA_JPEAG_J@Z` | `0x2B810` | 213 | UnwindData |  |
| 2114 | `?rend@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA?AV?$reverse_iterator@PEADDAEADPEAD_J@2@XZ` | `0x2B8F0` | 80 | UnwindData |  |
| 2115 | `?rend@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA?AV?$reverse_iterator@PEBDDAEBDPEBD_J@2@XZ` | `0x2B950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2116 | `?rend@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA?AV?$reverse_iterator@PEAGGAEAGPEAG_J@2@XZ` | `0x2B970` | 80 | UnwindData |  |
| 2117 | `?rend@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA?AV?$reverse_iterator@PEBGGAEBGPEBG_J@2@XZ` | `0x2B9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2118 | `?replace@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@PEAD0AEBV12@@Z` | `0x2B9F0` | 150 | UnwindData |  |
| 2119 | `?replace@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@PEAD0PEBD1@Z` | `0x2BA90` | 242 | UnwindData |  |
| 2120 | `?replace@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@PEAD0PEBD@Z` | `0x2BB90` | 156 | UnwindData |  |
| 2121 | `?replace@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@PEAD0PEBD_K@Z` | `0x2BC40` | 137 | UnwindData |  |
| 2122 | `?replace@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@PEAD0_KD@Z` | `0x2BCD0` | 137 | UnwindData |  |
| 2123 | `?replace@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_K00D@Z` | `0x2BD60` | 254 | UnwindData |  |
| 2124 | `?replace@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_K0AEBV12@00@Z` | `0x2BE70` | 319 | UnwindData |  |
| 2125 | `?replace@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_K0AEBV12@@Z` | `0x2BFC0` | 26 | UnwindData |  |
| 2126 | `?replace@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_K0PEBD0@Z` | `0x2BFE0` | 268 | UnwindData |  |
| 2127 | `?replace@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV12@_K0PEBD@Z` | `0x2C100` | 33 | UnwindData |  |
| 2128 | `?replace@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@PEAG0AEBV12@@Z` | `0x2C130` | 156 | UnwindData |  |
| 2129 | `?replace@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@PEAG0PEBG1@Z` | `0x2C1E0` | 271 | UnwindData |  |
| 2130 | `?replace@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@PEAG0PEBG@Z` | `0x2C300` | 177 | UnwindData |  |
| 2131 | `?replace@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@PEAG0PEBG_K@Z` | `0x2C3C0` | 143 | UnwindData |  |
| 2132 | `?replace@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@PEAG0_KG@Z` | `0x2C460` | 153 | UnwindData |  |
| 2133 | `?replace@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_K00G@Z` | `0x2C500` | 329 | UnwindData |  |
| 2134 | `?replace@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_K0AEBV12@00@Z` | `0x2C650` | 381 | UnwindData |  |
| 2135 | `?replace@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_K0AEBV12@@Z` | `0x2C7E0` | 26 | UnwindData |  |
| 2136 | `?replace@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_K0PEBG0@Z` | `0x2C800` | 337 | UnwindData |  |
| 2137 | `?replace@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV12@_K0PEBG@Z` | `0x2C960` | 34 | UnwindData |  |
| 2138 | `?reserve@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAX_K@Z` | `0x2C990` | 23 | UnwindData |  |
| 2139 | `?reserve@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAX_K@Z` | `0x2C9B0` | 23 | UnwindData |  |
| 2141 | `?resize@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAX_K@Z` | `0x2C9D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2142 | `?resize@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAX_KD@Z` | `0x2CA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2143 | `?resize@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAX_K@Z` | `0x2CA20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2144 | `?resize@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAX_KG@Z` | `0x2CA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2145 | `?rfind@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KAEBV12@_K@Z` | `0x2CA70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2146 | `?rfind@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KD_K@Z` | `0x2CAA0` | 29 | UnwindData |  |
| 2147 | `?rfind@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEBD_K1@Z` | `0x2CAD0` | 147 | UnwindData |  |
| 2148 | `?rfind@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KPEBD_K@Z` | `0x2CB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2149 | `?rfind@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KAEBV12@_K@Z` | `0x2CB90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2150 | `?rfind@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KG_K@Z` | `0x2CBC0` | 30 | UnwindData |  |
| 2151 | `?rfind@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEBG_K1@Z` | `0x2CBF0` | 140 | UnwindData |  |
| 2152 | `?rfind@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KPEBG_K@Z` | `0x2CC90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2166 | `?sbumpc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x2CCB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2167 | `?sbumpc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x2CD00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2168 | `?scan_is@?$ctype@D@std@@QEBAPEBDFPEBD0@Z` | `0x2CD50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2169 | `?scan_is@?$ctype@G@std@@QEBAPEBGFPEBG0@Z` | `0x2CD80` | 21 | UnwindData |  |
| 2170 | `?scan_not@?$ctype@D@std@@QEBAPEBDFPEBD0@Z` | `0x2CDA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2171 | `?scan_not@?$ctype@G@std@@QEBAPEBGFPEBG0@Z` | `0x2CDD0` | 21 | UnwindData |  |
| 2172 | `?seekg@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@V?$fpos@H@2@@Z` | `0x2CDF0` | 84 | UnwindData |  |
| 2173 | `?seekg@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@_JW4seekdir@ios_base@2@@Z` | `0x2CE50` | 68 | UnwindData |  |
| 2174 | `?seekg@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@V?$fpos@H@2@@Z` | `0x2CEA0` | 84 | UnwindData |  |
| 2175 | `?seekg@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@_JW4seekdir@ios_base@2@@Z` | `0x2CF00` | 68 | UnwindData |  |
| 2176 | `?seekoff@?$basic_filebuf@DU?$char_traits@D@std@@@std@@MEAA?AV?$fpos@H@2@_JW4seekdir@ios_base@2@H@Z` | `0x2CF50` | 147 | UnwindData |  |
| 2177 | `?seekoff@?$basic_filebuf@GU?$char_traits@G@std@@@std@@MEAA?AV?$fpos@H@2@_JW4seekdir@ios_base@2@H@Z` | `0x2CFF0` | 147 | UnwindData |  |
| 2178 | `?seekoff@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA?AV?$fpos@H@2@_JW4seekdir@ios_base@2@H@Z` | `0x2D090` | 56 | UnwindData |  |
| 2179 | `?seekoff@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA?AV?$fpos@H@2@_JW4seekdir@ios_base@2@H@Z` | `0x2D0D0` | 56 | UnwindData |  |
| 2183 | `?seekp@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@V?$fpos@H@2@@Z` | `0x2D110` | 84 | UnwindData |  |
| 2184 | `?seekp@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@_JW4seekdir@ios_base@2@@Z` | `0x2D170` | 68 | UnwindData |  |
| 2185 | `?seekp@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@V?$fpos@H@2@@Z` | `0x2D1C0` | 84 | UnwindData |  |
| 2186 | `?seekp@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@_JW4seekdir@ios_base@2@@Z` | `0x2D220` | 68 | UnwindData |  |
| 2187 | `?seekpos@?$basic_filebuf@DU?$char_traits@D@std@@@std@@MEAA?AV?$fpos@H@2@V32@H@Z` | `0x2D270` | 220 | UnwindData |  |
| 2188 | `?seekpos@?$basic_filebuf@GU?$char_traits@G@std@@@std@@MEAA?AV?$fpos@H@2@V32@H@Z` | `0x2D360` | 220 | UnwindData |  |
| 2189 | `?seekpos@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA?AV?$fpos@H@2@V32@H@Z` | `0x2D450` | 56 | UnwindData |  |
| 2190 | `?seekpos@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA?AV?$fpos@H@2@V32@H@Z` | `0x2D490` | 56 | UnwindData |  |
| 2195 | `?setbuf@?$basic_filebuf@DU?$char_traits@D@std@@@std@@MEAAPEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@PEAD_J@Z` | `0x2D4D0` | 48 | UnwindData |  |
| 2196 | `?setbuf@?$basic_filebuf@GU?$char_traits@G@std@@@std@@MEAAPEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@PEAG_J@Z` | `0x2D510` | 49 | UnwindData |  |
| 2197 | `?setbuf@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAPEAV12@PEAD_J@Z` | `0x2D550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2198 | `?setbuf@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAPEAV12@PEAG_J@Z` | `0x2D560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2199 | `?setf@ios_base@std@@QEAAHH@Z` | `0x2D570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2200 | `?setf@ios_base@std@@QEAAHHH@Z` | `0x2D590` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2201 | `?setg@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXPEAD00@Z` | `0x2D5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2202 | `?setg@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXPEAG00@Z` | `0x2D5E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2204 | `?setp@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXPEAD00@Z` | `0x2D610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2205 | `?setp@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXPEAD0@Z` | `0x2D630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2206 | `?setp@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXPEAG00@Z` | `0x2D650` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2207 | `?setp@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXPEAG0@Z` | `0x2D680` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2209 | `?setstate@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXF@Z` | `0x2D6B0` | 40 | UnwindData |  |
| 2210 | `?setstate@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXH_N@Z` | `0x2D6E0` | 34 | UnwindData |  |
| 2211 | `?setstate@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXF@Z` | `0x2D710` | 40 | UnwindData |  |
| 2212 | `?setstate@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXH_N@Z` | `0x2D740` | 34 | UnwindData |  |
| 2213 | `?setstate@ios_base@std@@QEAAXF@Z` | `0x2D770` | 27 | UnwindData |  |
| 2214 | `?setstate@ios_base@std@@QEAAXH_N@Z` | `0x2D7A0` | 21 | UnwindData |  |
| 2216 | `?sgetc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x2D7C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2217 | `?sgetc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x2D800` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2218 | `?sgetn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA_JPEAD_J@Z` | `0x2D840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2219 | `?sgetn@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA_JPEAG_J@Z` | `0x2D860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2220 | `?showmanyc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x2D880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2221 | `?showmanyc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAHXZ` | `0x2D890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2244 | `?size@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA_KXZ` | `0x2D8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2245 | `?size@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA_KXZ` | `0x2D8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2246 | `?snextc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x2D8C0` | 148 | UnwindData |  |
| 2247 | `?snextc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x2D960` | 154 | UnwindData |  |
| 2248 | `?sputbackc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHD@Z` | `0x2DA00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2249 | `?sputbackc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGG@Z` | `0x2DA50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2250 | `?sputc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHD@Z` | `0x2DAA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2251 | `?sputc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGG@Z` | `0x2DAF0` | 92 | UnwindData |  |
| 2252 | `?sputn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA_JPEBD_J@Z` | `0x2DB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2253 | `?sputn@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA_JPEBG_J@Z` | `0x2DB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2260 | `?stossc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x2DBA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2261 | `?stossc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x2DBE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2278 | `?substr@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA?AV12@_K0@Z` | `0x2DC20` | 43 | UnwindData |  |
| 2279 | `?substr@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA?AV12@_K0@Z` | `0x2DC60` | 43 | UnwindData |  |
| 2280 | `?sungetc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x2DCA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2281 | `?sungetc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x2DCF0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2282 | `?swap@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXAEAV12@@Z` | `0x2DD40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2283 | `?swap@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXAEAV12@@Z` | `0x2DD80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2284 | `?sync@?$basic_filebuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x2DDC0` | 41 | UnwindData |  |
| 2285 | `?sync@?$basic_filebuf@GU?$char_traits@G@std@@@std@@MEAAHXZ` | `0x2DDF0` | 41 | UnwindData |  |
| 2286 | `?sync@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x2DE20` | 129 | UnwindData |  |
| 2287 | `?sync@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAHXZ` | `0x2DEB0` | 129 | UnwindData |  |
| 2288 | `?sync@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x2DF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2289 | `?sync@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAHXZ` | `0x2DF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2290 | `?sync_with_stdio@ios_base@std@@SA_N_N@Z` | `0x2DF60` | 59 | UnwindData |  |
| 2291 | `?table@?$ctype@D@std@@IEBAPEBFXZ` | `0x2DFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2293 | `?tellg@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@H@2@XZ` | `0x2DFC0` | 106 | UnwindData |  |
| 2294 | `?tellg@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@H@2@XZ` | `0x2E030` | 106 | UnwindData |  |
| 2295 | `?tellp@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@H@2@XZ` | `0x2E0A0` | 109 | UnwindData |  |
| 2296 | `?tellp@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@H@2@XZ` | `0x2E120` | 109 | UnwindData |  |
| 2297 | `?thousands_sep@?$_Mpunct@D@std@@QEBADXZ` | `0x2E1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2298 | `?thousands_sep@?$_Mpunct@G@std@@QEBAGXZ` | `0x2E1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2299 | `?thousands_sep@?$numpunct@D@std@@QEBADXZ` | `0x2E1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2300 | `?thousands_sep@?$numpunct@G@std@@QEBAGXZ` | `0x2E200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2301 | `?tie@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAPEAV?$basic_ostream@DU?$char_traits@D@std@@@2@PEAV32@@Z` | `0x2E220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2302 | `?tie@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBAPEAV?$basic_ostream@DU?$char_traits@D@std@@@2@XZ` | `0x2E230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2303 | `?tie@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAPEAV?$basic_ostream@GU?$char_traits@G@std@@@2@PEAV32@@Z` | `0x2E240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2304 | `?tie@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBAPEAV?$basic_ostream@GU?$char_traits@G@std@@@2@XZ` | `0x2E250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2305 | `?to_char_type@?$char_traits@D@std@@SADAEBH@Z` | `0x2E260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2306 | `?to_char_type@?$char_traits@G@std@@SAGAEBG@Z` | `0x2E270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2307 | `?to_int_type@?$char_traits@D@std@@SAHAEBD@Z` | `0x2E280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2308 | `?to_int_type@?$char_traits@G@std@@SAGAEBG@Z` | `0x2E290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2309 | `?tolower@?$ctype@D@std@@QEBADD@Z` | `0x2E2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2310 | `?tolower@?$ctype@D@std@@QEBAPEBDPEADPEBD@Z` | `0x2E2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2311 | `?tolower@?$ctype@G@std@@QEBAGG@Z` | `0x2E2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2312 | `?tolower@?$ctype@G@std@@QEBAPEBGPEAGPEBG@Z` | `0x2E300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2313 | `?toupper@?$ctype@D@std@@QEBADD@Z` | `0x2E320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2314 | `?toupper@?$ctype@D@std@@QEBAPEBDPEADPEBD@Z` | `0x2E340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2315 | `?toupper@?$ctype@G@std@@QEBAGG@Z` | `0x2E360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2316 | `?toupper@?$ctype@G@std@@QEBAPEBGPEAGPEBG@Z` | `0x2E380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2317 | `?transform@?$collate@D@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@PEBD0@Z` | `0x2E3A0` | 30 | UnwindData |  |
| 2318 | `?transform@?$collate@G@std@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@PEBG0@Z` | `0x2E3D0` | 30 | UnwindData |  |
| 2319 | `?truename@?$numpunct@D@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x2E400` | 30 | UnwindData |  |
| 2320 | `?truename@?$numpunct@G@std@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x2E430` | 30 | UnwindData |  |
| 2321 | `?uflow@?$basic_filebuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x2E460` | 536 | UnwindData |  |
| 2322 | `?uflow@?$basic_filebuf@GU?$char_traits@G@std@@@std@@MEAAGXZ` | `0x2E680` | 548 | UnwindData |  |
| 2323 | `?uflow@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x2E8B0` | 59 | UnwindData |  |
| 2324 | `?uflow@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAGXZ` | `0x2E900` | 63 | UnwindData |  |
| 2326 | `?underflow@?$basic_filebuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x2E950` | 83 | UnwindData |  |
| 2327 | `?underflow@?$basic_filebuf@GU?$char_traits@G@std@@@std@@MEAAGXZ` | `0x2E9B0` | 84 | UnwindData |  |
| 2328 | `?underflow@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x2EA10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2329 | `?underflow@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAGXZ` | `0x2EA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2333 | `?unget@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@XZ` | `0x2EA30` | 208 | UnwindData |  |
| 2334 | `?unget@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@XZ` | `0x2EB10` | 220 | UnwindData |  |
| 2335 | `?unsetf@ios_base@std@@QEAAXH@Z` | `0x2EC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2340 | `?what@logic_error@std@@UEBAPEBDXZ` | `0x2EC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2341 | `?what@runtime_error@std@@UEBAPEBDXZ` | `0x2EC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2342 | `?widen@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBADD@Z` | `0x2EC50` | 108 | UnwindData |  |
| 2343 | `?widen@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBAGD@Z` | `0x2ECD0` | 125 | UnwindData |  |
| 2344 | `?widen@?$ctype@D@std@@QEBADD@Z` | `0x2ED60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2345 | `?widen@?$ctype@D@std@@QEBAPEBDPEBD0PEAD@Z` | `0x2ED70` | 29 | UnwindData |  |
| 2346 | `?widen@?$ctype@G@std@@QEBAGD@Z` | `0x2EDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2347 | `?widen@?$ctype@G@std@@QEBAPEBDPEBD0PEAG@Z` | `0x2EDC0` | 21 | UnwindData |  |
| 2348 | `?width@ios_base@std@@QEAA_J_J@Z` | `0x2EDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2349 | `?width@ios_base@std@@QEBA_JXZ` | `0x2EDF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2350 | `?write@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEBD_J@Z` | `0x2EE00` | 253 | UnwindData |  |
| 2351 | `?write@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEBG_J@Z` | `0x2EF10` | 253 | UnwindData |  |
| 2352 | `?ws@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@1@AEAV21@@Z` | `0x2F020` | 296 | UnwindData |  |
| 2353 | `?ws@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@1@AEAV21@@Z` | `0x2F150` | 325 | UnwindData |  |
| 2354 | `?xalloc@ios_base@std@@SAHXZ` | `0x2F2A0` | 49 | UnwindData |  |
| 2355 | `?xsgetn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA_JPEAD_J@Z` | `0x2F2E0` | 179 | UnwindData |  |
| 2356 | `?xsgetn@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA_JPEAG_J@Z` | `0x2F3A0` | 194 | UnwindData |  |
| 2357 | `?xsputn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA_JPEBD_J@Z` | `0x2F470` | 180 | UnwindData |  |
| 2358 | `?xsputn@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA_JPEBG_J@Z` | `0x2F530` | 194 | UnwindData |  |
| 2140 | `?resetiosflags@std@@YA?AU?$_Smanip@H@1@H@Z` | `0x2F600` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2194 | `?setbase@std@@YA?AU?$_Smanip@H@1@H@Z` | `0x2F670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2203 | `?setiosflags@std@@YA?AU?$_Smanip@H@1@H@Z` | `0x2F690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2208 | `?setprecision@std@@YA?AU?$_Smanip@_J@1@_J@Z` | `0x2F6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2215 | `?setw@std@@YA?AU?$_Smanip@_J@1@_J@Z` | `0x2F6D0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 568 | `??1ios_base@std@@UEAA@XZ` | `0x2F820` | 75 | UnwindData |  |
| 1116 | `?_Addstd@ios_base@std@@IEAAXXZ` | `0x2F900` | 106 | UnwindData |  |
| 1119 | `?_Callfns@ios_base@std@@AEAAXW4event@12@@Z` | `0x2F970` | 68 | UnwindData |  |
| 1153 | `?_Findarr@ios_base@std@@AEAAAEAU_Iosarray@12@H@Z` | `0x2F9F0` | 248 | UnwindData |  |
| 1259 | `?_Init@ios_base@std@@IEAAXXZ` | `0x2FAF0` | 64 | UnwindData |  |
| 1323 | `?_Tidy@ios_base@std@@AEAAXXZ` | `0x2FB40` | 91 | UnwindData |  |
| 1395 | `?clear@ios_base@std@@QEAAXH_N@Z` | `0x2FBB0` | 139 | UnwindData |  |
| 1432 | `?copyfmt@ios_base@std@@QEAAAEAV12@AEBV12@@Z` | `0x2FC50` | 209 | UnwindData |  |
| 1823 | `?imbue@ios_base@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x2FD30` | 142 | UnwindData |  |
| 2113 | `?register_callback@ios_base@std@@QEAAXP6AXW4event@12@AEAV12@H@ZH@Z` | `0x2FDD0` | 88 | UnwindData |  |
| 445 | `??0Init@ios_base@std@@QEAA@XZ` | `0x2FE30` | 465 | UnwindData |  |
| 554 | `??1Init@ios_base@std@@QEAA@XZ` | `0x30010` | 96 | UnwindData |  |
| 447 | `??0_Locinfo@std@@QEAA@HPEBD@Z` | `0x301E0` | 140 | UnwindData |  |
| 448 | `??0_Locinfo@std@@QEAA@PEBD@Z` | `0x30280` | 300 | UnwindData |  |
| 475 | `??0locale@std@@QEAA@AEBV01@0H@Z` | `0x303C0` | 206 | UnwindData |  |
| 477 | `??0locale@std@@QEAA@AEBV01@PEBDH@Z` | `0x304A0` | 354 | UnwindData |  |
| 478 | `??0locale@std@@QEAA@PEBDH@Z` | `0x30610` | 326 | UnwindData |  |
| 555 | `??1_Locinfo@std@@QEAA@XZ` | `0x30760` | 255 | UnwindData |  |
| 1114 | `?_Addcats@_Locinfo@std@@QEAAAEAV12@HPEBD@Z` | `0x308B0` | 193 | UnwindData |  |
| 1115 | `?_Addfac@locale@std@@QEAAAEAV12@PEAVfacet@12@_K1@Z` | `0x30AB0` | 219 | UnwindData |  |
| 1772 | `?global@locale@std@@SA?AV12@AEBV12@@Z` | `0x31000` | 332 | UnwindData |  |
| 801 | `??8locale@std@@QEBA_NAEBV01@@Z` | `0x312F0` | 452 | UnwindData |  |
| 1192 | `?_Getfacet@locale@std@@QEBAPEBVfacet@12@_K_N@Z` | `0x314C0` | 134 | UnwindData |  |
| 1260 | `?_Init@locale@std@@CAPEAV_Locimp@12@XZ` | `0x31550` | 246 | UnwindData |  |
| 1268 | `?_Iscloc@locale@std@@QEBA_NXZ` | `0x31650` | 70 | UnwindData |  |
| 1324 | `?_Tidy@locale@std@@CAXXZ` | `0x316A0` | 144 | UnwindData |  |
| 1388 | `?classic@locale@std@@SAAEBV12@XZ` | `0x31740` | 41 | UnwindData |  |
| 1600 | `?empty@locale@std@@SA?AV12@XZ` | `0x31770` | 82 | UnwindData |  |
| 1282 | `?_Nomemory@std@@YAXXZ` | `0x31830` | 32 | UnwindData |  |
| 1332 | `?_Xlen@std@@YAXXZ` | `0x31860` | 72 | UnwindData |  |
| 1333 | `?_Xran@std@@YAXXZ` | `0x318B0` | 72 | UnwindData |  |
| 485 | `??0ostrstream@std@@QEAA@PEAD_JH@Z` | `0x31900` | 231 | UnwindData |  |
| 494 | `??0strstream@std@@QEAA@PEAD_JH@Z` | `0x319F0` | 277 | UnwindData |  |
| 569 | `??1istrstream@std@@UEAA@XZ` | `0x31B10` | 79 | UnwindData |  |
| 575 | `??1ostrstream@std@@UEAA@XZ` | `0x31B70` | 79 | UnwindData |  |
| 580 | `??1strstream@std@@UEAA@XZ` | `0x31BD0` | 131 | UnwindData |  |
| 581 | `??1strstreambuf@std@@UEAA@XZ` | `0x31C60` | 57 | UnwindData |  |
| 1261 | `?_Init@strstreambuf@std@@IEAAXHPEAD0H@Z` | `0x31FC0` | 301 | UnwindData |  |
| 1325 | `?_Tidy@strstreambuf@std@@IEAAXXZ` | `0x32100` | 64 | UnwindData |  |
| 1704 | `?freeze@strstreambuf@std@@QEAAX_N@Z` | `0x32150` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1980 | `?overflow@strstreambuf@std@@MEAAHH@Z` | `0x321C0` | 481 | UnwindData |  |
| 1987 | `?pbackfail@strstreambuf@std@@MEAAHH@Z` | `0x323B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2182 | `?seekoff@strstreambuf@std@@MEAA?AV?$fpos@H@2@_JW4seekdir@ios_base@2@H@Z` | `0x32410` | 406 | UnwindData |  |
| 2193 | `?seekpos@strstreambuf@std@@MEAA?AV?$fpos@H@2@V32@H@Z` | `0x325B0` | 291 | UnwindData |  |
| 2332 | `?underflow@strstreambuf@std@@MEAAHXZ` | `0x326E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2325 | `?uncaught_exception@std@@YA_NXZ` | `0x32760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `??0_Winit@std@@QEAA@XZ` | `0x32770` | 478 | UnwindData |  |
| 558 | `??1_Winit@std@@QEAA@XZ` | `0x32960` | 96 | UnwindData |  |
| 679 | `??4_Winit@std@@QEAAAEAV01@AEBV01@@Z` | `0x329D0` | 10,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `??0_Lockit@std@@QEAA@XZ` | `0x35490` | 152 | UnwindData |  |
| 556 | `??1_Lockit@std@@QEAA@XZ` | `0x35530` | 31 | UnwindData |  |
| 1 | `??$?5DU?$char_traits@D@std@@@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAC@Z` | `0x35590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `??5std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAC@Z` | `0x35590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??$?5DU?$char_traits@D@std@@@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAD@Z` | `0x355A0` | 215 | UnwindData |  |
| 733 | `??5std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAD@Z` | `0x355A0` | 215 | UnwindData |  |
| 3 | `??$?5DU?$char_traits@D@std@@@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAE@Z` | `0x35680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `??5std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAE@Z` | `0x35680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??$?5DU?$char_traits@D@std@@@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@PEAC@Z` | `0x35690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 739 | `??5std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@PEAC@Z` | `0x35690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??$?5DU?$char_traits@D@std@@@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@PEAD@Z` | `0x356A0` | 418 | UnwindData |  |
| 740 | `??5std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@PEAD@Z` | `0x356A0` | 418 | UnwindData |  |
| 6 | `??$?5DU?$char_traits@D@std@@@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@PEAE@Z` | `0x35850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `??5std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@PEAE@Z` | `0x35850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??$?5DU?$char_traits@D@std@@M@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAV?$complex@M@0@@Z` | `0x35860` | 315 | UnwindData |  |
| 736 | `??5std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAV?$complex@M@0@@Z` | `0x35860` | 315 | UnwindData |  |
| 8 | `??$?5DU?$char_traits@D@std@@N@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAV?$complex@N@0@@Z` | `0x359B0` | 309 | UnwindData |  |
| 737 | `??5std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAV?$complex@N@0@@Z` | `0x359B0` | 309 | UnwindData |  |
| 9 | `??$?5DU?$char_traits@D@std@@O@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAV?$complex@O@0@@Z` | `0x35AF0` | 309 | UnwindData |  |
| 738 | `??5std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAV?$complex@O@0@@Z` | `0x35AF0` | 309 | UnwindData |  |
| 10 | `??$?5DU?$char_traits@D@std@@V?$allocator@D@1@@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x35C30` | 436 | UnwindData |  |
| 735 | `??5std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x35C30` | 436 | UnwindData |  |
| 11 | `??$?5GU?$char_traits@G@std@@@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@AEAG@Z` | `0x35DF0` | 226 | UnwindData |  |
| 742 | `??5std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@AEAG@Z` | `0x35DF0` | 226 | UnwindData |  |
| 12 | `??$?5GU?$char_traits@G@std@@@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@PEAF@Z` | `0x35EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `??5std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@PEAF@Z` | `0x35EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??$?5GU?$char_traits@G@std@@@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@PEAG@Z` | `0x35EF0` | 466 | UnwindData |  |
| 748 | `??5std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@PEAG@Z` | `0x35EF0` | 466 | UnwindData |  |
| 14 | `??$?5GU?$char_traits@G@std@@M@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@AEAV?$complex@M@0@@Z` | `0x360D0` | 345 | UnwindData |  |
| 744 | `??5std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@AEAV?$complex@M@0@@Z` | `0x360D0` | 345 | UnwindData |  |
| 15 | `??$?5GU?$char_traits@G@std@@N@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@AEAV?$complex@N@0@@Z` | `0x36230` | 339 | UnwindData |  |
| 745 | `??5std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@AEAV?$complex@N@0@@Z` | `0x36230` | 339 | UnwindData |  |
| 16 | `??$?5GU?$char_traits@G@std@@O@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@AEAV?$complex@O@0@@Z` | `0x36390` | 339 | UnwindData |  |
| 746 | `??5std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@AEAV?$complex@O@0@@Z` | `0x36390` | 339 | UnwindData |  |
| 17 | `??$?5GU?$char_traits@G@std@@V?$allocator@G@1@@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x364F0` | 472 | UnwindData |  |
| 743 | `??5std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x364F0` | 472 | UnwindData |  |
| 18 | `??$?6DU?$char_traits@D@std@@@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@C@Z` | `0x366D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | `??6std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@C@Z` | `0x366D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??$?6DU?$char_traits@D@std@@@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@D@Z` | `0x366E0` | 615 | UnwindData |  |
| 788 | `??6std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@D@Z` | `0x366E0` | 615 | UnwindData |  |
| 20 | `??$?6DU?$char_traits@D@std@@@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@E@Z` | `0x36950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `??6std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@E@Z` | `0x36950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??$?6DU?$char_traits@D@std@@@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@PEBC@Z` | `0x36960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 790 | `??6std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@PEBC@Z` | `0x36960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??$?6DU?$char_traits@D@std@@@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@PEBD@Z` | `0x36970` | 567 | UnwindData |  |
| 791 | `??6std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@PEBD@Z` | `0x36970` | 567 | UnwindData |  |
| 23 | `??$?6DU?$char_traits@D@std@@@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@PEBE@Z` | `0x36BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 792 | `??6std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@PEBE@Z` | `0x36BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??$?6DU?$char_traits@D@std@@M@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@AEBV?$complex@M@0@@Z` | `0x36BC0` | 439 | UnwindData |  |
| 784 | `??6std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@AEBV?$complex@M@0@@Z` | `0x36BC0` | 439 | UnwindData |  |
| 25 | `??$?6DU?$char_traits@D@std@@N@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@AEBV?$complex@N@0@@Z` | `0x36D80` | 439 | UnwindData |  |
| 785 | `??6std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@AEBV?$complex@N@0@@Z` | `0x36D80` | 439 | UnwindData |  |
| 26 | `??$?6DU?$char_traits@D@std@@O@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@AEBV?$complex@O@0@@Z` | `0x36F40` | 439 | UnwindData |  |
| 786 | `??6std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@AEBV?$complex@O@0@@Z` | `0x36F40` | 439 | UnwindData |  |
| 27 | `??$?6DU?$char_traits@D@std@@V?$allocator@D@1@@std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x37100` | 43 | UnwindData |  |
| 783 | `??6std@@YAAEAV?$basic_ostream@DU?$char_traits@D@std@@@0@AEAV10@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x37100` | 43 | UnwindData |  |
| 28 | `??$?6GU?$char_traits@G@std@@@std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@G@Z` | `0x37140` | 664 | UnwindData |  |
| 797 | `??6std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@G@Z` | `0x37140` | 664 | UnwindData |  |
| 29 | `??$?6GU?$char_traits@G@std@@@std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@PEBF@Z` | `0x373E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `??6std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@PEBF@Z` | `0x373E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??$?6GU?$char_traits@G@std@@@std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@PEBG@Z` | `0x373F0` | 604 | UnwindData |  |
| 799 | `??6std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@PEBG@Z` | `0x373F0` | 604 | UnwindData |  |
| 31 | `??$?6GU?$char_traits@G@std@@M@std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@AEBV?$complex@M@0@@Z` | `0x37660` | 478 | UnwindData |  |
| 794 | `??6std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@AEBV?$complex@M@0@@Z` | `0x37660` | 478 | UnwindData |  |
| 32 | `??$?6GU?$char_traits@G@std@@N@std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@AEBV?$complex@N@0@@Z` | `0x37850` | 478 | UnwindData |  |
| 795 | `??6std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@AEBV?$complex@N@0@@Z` | `0x37850` | 478 | UnwindData |  |
| 33 | `??$?6GU?$char_traits@G@std@@O@std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@AEBV?$complex@O@0@@Z` | `0x37A40` | 478 | UnwindData |  |
| 796 | `??6std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@AEBV?$complex@O@0@@Z` | `0x37A40` | 478 | UnwindData |  |
| 34 | `??$?6GU?$char_traits@G@std@@V?$allocator@G@1@@std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x37C30` | 43 | UnwindData |  |
| 793 | `??6std@@YAAEAV?$basic_ostream@GU?$char_traits@G@std@@@0@AEAV10@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x37C30` | 43 | UnwindData |  |
| 35 | `??$?8DU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@0@Z` | `0x37C70` | 51 | UnwindData |  |
| 805 | `??8std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@0@Z` | `0x37C70` | 51 | UnwindData |  |
| 36 | `??$?8DU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBD@Z` | `0x37CB0` | 46 | UnwindData |  |
| 806 | `??8std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBD@Z` | `0x37CB0` | 46 | UnwindData |  |
| 37 | `??$?8DU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NPEBDAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x37CF0` | 52 | UnwindData |  |
| 815 | `??8std@@YA_NPEBDAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x37CF0` | 52 | UnwindData |  |
| 38 | `??$?8GU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@0@Z` | `0x37D30` | 51 | UnwindData |  |
| 807 | `??8std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@0@Z` | `0x37D30` | 51 | UnwindData |  |
| 39 | `??$?8GU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBG@Z` | `0x37D70` | 51 | UnwindData |  |
| 808 | `??8std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBG@Z` | `0x37D70` | 51 | UnwindData |  |
| 40 | `??$?8GU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NPEBGAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x37DB0` | 57 | UnwindData |  |
| 816 | `??8std@@YA_NPEBGAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x37DB0` | 57 | UnwindData |  |
| 41 | `??$?8M@std@@YA_NAEBMAEBV?$complex@M@0@@Z` | `0x37DF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `??8std@@YA_NAEBMAEBV?$complex@M@0@@Z` | `0x37DF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??$?8M@std@@YA_NAEBV?$complex@M@0@0@Z` | `0x37E20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 809 | `??8std@@YA_NAEBV?$complex@M@0@0@Z` | `0x37E20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `??$?8M@std@@YA_NAEBV?$complex@M@0@AEBM@Z` | `0x37E50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `??8std@@YA_NAEBV?$complex@M@0@AEBM@Z` | `0x37E50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `??$?8N@std@@YA_NAEBNAEBV?$complex@N@0@@Z` | `0x37E80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 803 | `??8std@@YA_NAEBNAEBV?$complex@N@0@@Z` | `0x37E80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??$?8N@std@@YA_NAEBV?$complex@N@0@0@Z` | `0x37EB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 811 | `??8std@@YA_NAEBV?$complex@N@0@0@Z` | `0x37EB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??$?8N@std@@YA_NAEBV?$complex@N@0@AEBN@Z` | `0x37EE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 812 | `??8std@@YA_NAEBV?$complex@N@0@AEBN@Z` | `0x37EE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `??$?8O@std@@YA_NAEBOAEBV?$complex@O@0@@Z` | `0x37F10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 804 | `??8std@@YA_NAEBOAEBV?$complex@O@0@@Z` | `0x37F10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??$?8O@std@@YA_NAEBV?$complex@O@0@0@Z` | `0x37F40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `??8std@@YA_NAEBV?$complex@O@0@0@Z` | `0x37F40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??$?8O@std@@YA_NAEBV?$complex@O@0@AEBO@Z` | `0x37F70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `??8std@@YA_NAEBV?$complex@O@0@AEBO@Z` | `0x37F70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `??$?9DU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@0@Z` | `0x37FA0` | 51 | UnwindData |  |
| 821 | `??9std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@0@Z` | `0x37FA0` | 51 | UnwindData |  |
| 51 | `??$?9DU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBD@Z` | `0x37FE0` | 46 | UnwindData |  |
| 822 | `??9std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBD@Z` | `0x37FE0` | 46 | UnwindData |  |
| 52 | `??$?9DU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NPEBDAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x38020` | 52 | UnwindData |  |
| 831 | `??9std@@YA_NPEBDAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x38020` | 52 | UnwindData |  |
| 53 | `??$?9GU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@0@Z` | `0x38060` | 51 | UnwindData |  |
| 823 | `??9std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@0@Z` | `0x38060` | 51 | UnwindData |  |
| 54 | `??$?9GU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBG@Z` | `0x380A0` | 51 | UnwindData |  |
| 824 | `??9std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBG@Z` | `0x380A0` | 51 | UnwindData |  |
| 55 | `??$?9GU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NPEBGAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x380E0` | 57 | UnwindData |  |
| 832 | `??9std@@YA_NPEBGAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x380E0` | 57 | UnwindData |  |
| 56 | `??$?9M@std@@YA_NAEBMAEBV?$complex@M@0@@Z` | `0x38120` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `??9std@@YA_NAEBMAEBV?$complex@M@0@@Z` | `0x38120` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??$?9M@std@@YA_NAEBV?$complex@M@0@0@Z` | `0x38150` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `??9std@@YA_NAEBV?$complex@M@0@0@Z` | `0x38150` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??$?9M@std@@YA_NAEBV?$complex@M@0@AEBM@Z` | `0x38180` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 826 | `??9std@@YA_NAEBV?$complex@M@0@AEBM@Z` | `0x38180` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `??$?9N@std@@YA_NAEBNAEBV?$complex@N@0@@Z` | `0x381B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `??9std@@YA_NAEBNAEBV?$complex@N@0@@Z` | `0x381B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `??$?9N@std@@YA_NAEBV?$complex@N@0@0@Z` | `0x381E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `??9std@@YA_NAEBV?$complex@N@0@0@Z` | `0x381E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `??$?9N@std@@YA_NAEBV?$complex@N@0@AEBN@Z` | `0x38210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 828 | `??9std@@YA_NAEBV?$complex@N@0@AEBN@Z` | `0x38210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `??$?9O@std@@YA_NAEBOAEBV?$complex@O@0@@Z` | `0x38240` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 820 | `??9std@@YA_NAEBOAEBV?$complex@O@0@@Z` | `0x38240` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `??$?9O@std@@YA_NAEBV?$complex@O@0@0@Z` | `0x38270` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 829 | `??9std@@YA_NAEBV?$complex@O@0@0@Z` | `0x38270` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `??$?9O@std@@YA_NAEBV?$complex@O@0@AEBO@Z` | `0x382A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `??9std@@YA_NAEBV?$complex@O@0@AEBO@Z` | `0x382A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `??$?DM@std@@YA?AV?$complex@M@0@AEBMAEBV10@@Z` | `0x382D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 839 | `??Dstd@@YA?AV?$complex@M@0@AEBMAEBV10@@Z` | `0x382D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `??$?DM@std@@YA?AV?$complex@M@0@AEBV10@0@Z` | `0x38310` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | `??Dstd@@YA?AV?$complex@M@0@AEBV10@0@Z` | `0x38310` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `??$?DM@std@@YA?AV?$complex@M@0@AEBV10@AEBM@Z` | `0x38350` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 841 | `??Dstd@@YA?AV?$complex@M@0@AEBV10@AEBM@Z` | `0x38350` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `??$?DN@std@@YA?AV?$complex@N@0@AEBNAEBV10@@Z` | `0x38380` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `??Dstd@@YA?AV?$complex@N@0@AEBNAEBV10@@Z` | `0x38380` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `??$?DN@std@@YA?AV?$complex@N@0@AEBV10@0@Z` | `0x383D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `??Dstd@@YA?AV?$complex@N@0@AEBV10@0@Z` | `0x383D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `??$?DN@std@@YA?AV?$complex@N@0@AEBV10@AEBN@Z` | `0x38420` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `??Dstd@@YA?AV?$complex@N@0@AEBV10@AEBN@Z` | `0x38420` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `??$?DO@std@@YA?AV?$complex@O@0@AEBOAEBV10@@Z` | `0x38450` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `??Dstd@@YA?AV?$complex@O@0@AEBOAEBV10@@Z` | `0x38450` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `??$?DO@std@@YA?AV?$complex@O@0@AEBV10@0@Z` | `0x384A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `??Dstd@@YA?AV?$complex@O@0@AEBV10@0@Z` | `0x384A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `??$?DO@std@@YA?AV?$complex@O@0@AEBV10@AEBO@Z` | `0x384F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `??Dstd@@YA?AV?$complex@O@0@AEBV10@AEBO@Z` | `0x384F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??$?GM@std@@YA?AV?$complex@M@0@AEBMAEBV10@@Z` | `0x38520` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 848 | `??Gstd@@YA?AV?$complex@M@0@AEBMAEBV10@@Z` | `0x38520` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `??$?GM@std@@YA?AV?$complex@M@0@AEBV10@0@Z` | `0x38550` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `??Gstd@@YA?AV?$complex@M@0@AEBV10@0@Z` | `0x38550` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `??$?GM@std@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x38580` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | `??Gstd@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x38580` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `??$?GM@std@@YA?AV?$complex@M@0@AEBV10@AEBM@Z` | `0x385B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `??Gstd@@YA?AV?$complex@M@0@AEBV10@AEBM@Z` | `0x385B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `??$?GN@std@@YA?AV?$complex@N@0@AEBNAEBV10@@Z` | `0x385D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `??Gstd@@YA?AV?$complex@N@0@AEBNAEBV10@@Z` | `0x385D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `??$?GN@std@@YA?AV?$complex@N@0@AEBV10@0@Z` | `0x38600` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `??Gstd@@YA?AV?$complex@N@0@AEBV10@0@Z` | `0x38600` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `??$?GN@std@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x38630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 854 | `??Gstd@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x38630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `??$?GN@std@@YA?AV?$complex@N@0@AEBV10@AEBN@Z` | `0x38650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 855 | `??Gstd@@YA?AV?$complex@N@0@AEBV10@AEBN@Z` | `0x38650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `??$?GO@std@@YA?AV?$complex@O@0@AEBOAEBV10@@Z` | `0x38670` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 856 | `??Gstd@@YA?AV?$complex@O@0@AEBOAEBV10@@Z` | `0x38670` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `??$?GO@std@@YA?AV?$complex@O@0@AEBV10@0@Z` | `0x386A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 857 | `??Gstd@@YA?AV?$complex@O@0@AEBV10@0@Z` | `0x386A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `??$?GO@std@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x386D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 858 | `??Gstd@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x386D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `??$?GO@std@@YA?AV?$complex@O@0@AEBV10@AEBO@Z` | `0x386F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 859 | `??Gstd@@YA?AV?$complex@O@0@AEBV10@AEBO@Z` | `0x386F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `??$?HDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@AEBV10@0@Z` | `0x38710` | 172 | UnwindData |  |
| 860 | `??Hstd@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@AEBV10@0@Z` | `0x38710` | 172 | UnwindData |  |
| 87 | `??$?HDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@AEBV10@D@Z` | `0x387D0` | 160 | UnwindData |  |
| 861 | `??Hstd@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@AEBV10@D@Z` | `0x387D0` | 160 | UnwindData |  |
| 88 | `??$?HDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@AEBV10@PEBD@Z` | `0x38880` | 179 | UnwindData |  |
| 862 | `??Hstd@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@AEBV10@PEBD@Z` | `0x38880` | 179 | UnwindData |  |
| 89 | `??$?HDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@DAEBV10@@Z` | `0x38940` | 209 | UnwindData |  |
| 863 | `??Hstd@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@DAEBV10@@Z` | `0x38940` | 209 | UnwindData |  |
| 90 | `??$?HDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBDAEBV10@@Z` | `0x38A20` | 142 | UnwindData |  |
| 864 | `??Hstd@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBDAEBV10@@Z` | `0x38A20` | 142 | UnwindData |  |
| 91 | `??$?HGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@AEBV10@0@Z` | `0x38AC0` | 172 | UnwindData |  |
| 865 | `??Hstd@@YA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@AEBV10@0@Z` | `0x38AC0` | 172 | UnwindData |  |
| 92 | `??$?HGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@AEBV10@G@Z` | `0x38B80` | 162 | UnwindData |  |
| 866 | `??Hstd@@YA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@AEBV10@G@Z` | `0x38B80` | 162 | UnwindData |  |
| 93 | `??$?HGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@AEBV10@PEBG@Z` | `0x38C30` | 184 | UnwindData |  |
| 867 | `??Hstd@@YA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@AEBV10@PEBG@Z` | `0x38C30` | 184 | UnwindData |  |
| 94 | `??$?HGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@GAEBV10@@Z` | `0x38CF0` | 209 | UnwindData |  |
| 868 | `??Hstd@@YA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@GAEBV10@@Z` | `0x38CF0` | 209 | UnwindData |  |
| 95 | `??$?HGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBGAEBV10@@Z` | `0x38DD0` | 185 | UnwindData |  |
| 869 | `??Hstd@@YA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBGAEBV10@@Z` | `0x38DD0` | 185 | UnwindData |  |
| 96 | `??$?HM@std@@YA?AV?$complex@M@0@AEBMAEBV10@@Z` | `0x38E90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | `??Hstd@@YA?AV?$complex@M@0@AEBMAEBV10@@Z` | `0x38E90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `??$?HM@std@@YA?AV?$complex@M@0@AEBV10@0@Z` | `0x38EC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 871 | `??Hstd@@YA?AV?$complex@M@0@AEBV10@0@Z` | `0x38EC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `??$?HM@std@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x38EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `??Hstd@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x38EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `??$?HM@std@@YA?AV?$complex@M@0@AEBV10@AEBM@Z` | `0x38F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `??Hstd@@YA?AV?$complex@M@0@AEBV10@AEBM@Z` | `0x38F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `??$?HN@std@@YA?AV?$complex@N@0@AEBNAEBV10@@Z` | `0x38F30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `??Hstd@@YA?AV?$complex@N@0@AEBNAEBV10@@Z` | `0x38F30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `??$?HN@std@@YA?AV?$complex@N@0@AEBV10@0@Z` | `0x38F60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `??Hstd@@YA?AV?$complex@N@0@AEBV10@0@Z` | `0x38F60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `??$?HN@std@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x38F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 876 | `??Hstd@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x38F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `??$?HN@std@@YA?AV?$complex@N@0@AEBV10@AEBN@Z` | `0x38FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `??Hstd@@YA?AV?$complex@N@0@AEBV10@AEBN@Z` | `0x38FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `??$?HO@std@@YA?AV?$complex@O@0@AEBOAEBV10@@Z` | `0x38FD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 878 | `??Hstd@@YA?AV?$complex@O@0@AEBOAEBV10@@Z` | `0x38FD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `??$?HO@std@@YA?AV?$complex@O@0@AEBV10@0@Z` | `0x39000` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `??Hstd@@YA?AV?$complex@O@0@AEBV10@0@Z` | `0x39000` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `??$?HO@std@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x39030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `??Hstd@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x39030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `??$?HO@std@@YA?AV?$complex@O@0@AEBV10@AEBO@Z` | `0x39050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 881 | `??Hstd@@YA?AV?$complex@O@0@AEBV10@AEBO@Z` | `0x39050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `??$?KM@std@@YA?AV?$complex@M@0@AEBMAEBV10@@Z` | `0x39070` | 54 | UnwindData |  |
| 882 | `??Kstd@@YA?AV?$complex@M@0@AEBMAEBV10@@Z` | `0x39070` | 54 | UnwindData |  |
| 109 | `??$?KM@std@@YA?AV?$complex@M@0@AEBV10@0@Z` | `0x390B0` | 49 | UnwindData |  |
| 883 | `??Kstd@@YA?AV?$complex@M@0@AEBV10@0@Z` | `0x390B0` | 49 | UnwindData |  |
| 110 | `??$?KM@std@@YA?AV?$complex@M@0@AEBV10@AEBM@Z` | `0x390F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 884 | `??Kstd@@YA?AV?$complex@M@0@AEBV10@AEBM@Z` | `0x390F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `??$?KN@std@@YA?AV?$complex@N@0@AEBNAEBV10@@Z` | `0x39120` | 57 | UnwindData |  |
| 885 | `??Kstd@@YA?AV?$complex@N@0@AEBNAEBV10@@Z` | `0x39120` | 57 | UnwindData |  |
| 112 | `??$?KN@std@@YA?AV?$complex@N@0@AEBV10@0@Z` | `0x39160` | 47 | UnwindData |  |
| 886 | `??Kstd@@YA?AV?$complex@N@0@AEBV10@0@Z` | `0x39160` | 47 | UnwindData |  |
| 113 | `??$?KN@std@@YA?AV?$complex@N@0@AEBV10@AEBN@Z` | `0x391A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | `??Kstd@@YA?AV?$complex@N@0@AEBV10@AEBN@Z` | `0x391A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `??$?KO@std@@YA?AV?$complex@O@0@AEBOAEBV10@@Z` | `0x391D0` | 57 | UnwindData |  |
| 888 | `??Kstd@@YA?AV?$complex@O@0@AEBOAEBV10@@Z` | `0x391D0` | 57 | UnwindData |  |
| 115 | `??$?KO@std@@YA?AV?$complex@O@0@AEBV10@0@Z` | `0x39210` | 47 | UnwindData |  |
| 889 | `??Kstd@@YA?AV?$complex@O@0@AEBV10@0@Z` | `0x39210` | 47 | UnwindData |  |
| 116 | `??$?KO@std@@YA?AV?$complex@O@0@AEBV10@AEBO@Z` | `0x39250` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `??Kstd@@YA?AV?$complex@O@0@AEBV10@AEBO@Z` | `0x39250` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `??$?MDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@0@Z` | `0x39280` | 49 | UnwindData |  |
| 891 | `??Mstd@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@0@Z` | `0x39280` | 49 | UnwindData |  |
| 118 | `??$?MDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBD@Z` | `0x392C0` | 44 | UnwindData |  |
| 892 | `??Mstd@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBD@Z` | `0x392C0` | 44 | UnwindData |  |
| 119 | `??$?MDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NPEBDAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x39300` | 52 | UnwindData |  |
| 895 | `??Mstd@@YA_NPEBDAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x39300` | 52 | UnwindData |  |
| 120 | `??$?MGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@0@Z` | `0x39340` | 49 | UnwindData |  |
| 893 | `??Mstd@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@0@Z` | `0x39340` | 49 | UnwindData |  |
| 121 | `??$?MGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBG@Z` | `0x39380` | 45 | UnwindData |  |
| 894 | `??Mstd@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBG@Z` | `0x39380` | 45 | UnwindData |  |
| 122 | `??$?MGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NPEBGAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x393C0` | 57 | UnwindData |  |
| 896 | `??Mstd@@YA_NPEBGAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x393C0` | 57 | UnwindData |  |
| 123 | `??$?NDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@0@Z` | `0x39400` | 57 | UnwindData |  |
| 897 | `??Nstd@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@0@Z` | `0x39400` | 57 | UnwindData |  |
| 124 | `??$?NDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBD@Z` | `0x39440` | 46 | UnwindData |  |
| 898 | `??Nstd@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBD@Z` | `0x39440` | 46 | UnwindData |  |
| 125 | `??$?NDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NPEBDAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x39480` | 52 | UnwindData |  |
| 901 | `??Nstd@@YA_NPEBDAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x39480` | 52 | UnwindData |  |
| 126 | `??$?NGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@0@Z` | `0x394C0` | 57 | UnwindData |  |
| 899 | `??Nstd@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@0@Z` | `0x394C0` | 57 | UnwindData |  |
| 127 | `??$?NGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBG@Z` | `0x39500` | 51 | UnwindData |  |
| 900 | `??Nstd@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBG@Z` | `0x39500` | 51 | UnwindData |  |
| 128 | `??$?NGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NPEBGAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x39540` | 53 | UnwindData |  |
| 902 | `??Nstd@@YA_NPEBGAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x39540` | 53 | UnwindData |  |
| 129 | `??$?ODU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@0@Z` | `0x39580` | 55 | UnwindData |  |
| 903 | `??Ostd@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@0@Z` | `0x39580` | 55 | UnwindData |  |
| 130 | `??$?ODU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBD@Z` | `0x395C0` | 46 | UnwindData |  |
| 904 | `??Ostd@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBD@Z` | `0x395C0` | 46 | UnwindData |  |
| 131 | `??$?ODU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NPEBDAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x39600` | 50 | UnwindData |  |
| 907 | `??Ostd@@YA_NPEBDAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x39600` | 50 | UnwindData |  |
| 132 | `??$?OGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@0@Z` | `0x39640` | 55 | UnwindData |  |
| 905 | `??Ostd@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@0@Z` | `0x39640` | 55 | UnwindData |  |
| 133 | `??$?OGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBG@Z` | `0x39680` | 51 | UnwindData |  |
| 906 | `??Ostd@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBG@Z` | `0x39680` | 51 | UnwindData |  |
| 134 | `??$?OGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NPEBGAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x396C0` | 51 | UnwindData |  |
| 908 | `??Ostd@@YA_NPEBGAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x396C0` | 51 | UnwindData |  |
| 135 | `??$?PDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@0@Z` | `0x39700` | 51 | UnwindData |  |
| 909 | `??Pstd@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@0@Z` | `0x39700` | 51 | UnwindData |  |
| 136 | `??$?PDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBD@Z` | `0x39740` | 46 | UnwindData |  |
| 910 | `??Pstd@@YA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@PEBD@Z` | `0x39740` | 46 | UnwindData |  |
| 137 | `??$?PDU?$char_traits@D@std@@V?$allocator@D@1@@std@@YA_NPEBDAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x39780` | 52 | UnwindData |  |
| 913 | `??Pstd@@YA_NPEBDAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x39780` | 52 | UnwindData |  |
| 138 | `??$?PGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@0@Z` | `0x397C0` | 51 | UnwindData |  |
| 911 | `??Pstd@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@0@Z` | `0x397C0` | 51 | UnwindData |  |
| 139 | `??$?PGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBG@Z` | `0x39800` | 47 | UnwindData |  |
| 912 | `??Pstd@@YA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@PEBG@Z` | `0x39800` | 47 | UnwindData |  |
| 140 | `??$?PGU?$char_traits@G@std@@V?$allocator@G@1@@std@@YA_NPEBGAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x39840` | 57 | UnwindData |  |
| 914 | `??Pstd@@YA_NPEBGAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x39840` | 57 | UnwindData |  |
| 141 | `??$?XMM@std@@YAAEAV?$complex@M@0@AEAV10@AEBV10@@Z` | `0x39880` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `??Xstd@@YAAEAV?$complex@M@0@AEAV10@AEBV10@@Z` | `0x39880` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `??$?XNN@std@@YAAEAV?$complex@N@0@AEAV10@AEBV10@@Z` | `0x398D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `??Xstd@@YAAEAV?$complex@N@0@AEAV10@AEBV10@@Z` | `0x398D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `??$?XOO@std@@YAAEAV?$complex@O@0@AEAV10@AEBV10@@Z` | `0x39920` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 921 | `??Xstd@@YAAEAV?$complex@O@0@AEAV10@AEBV10@@Z` | `0x39920` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `??$?YMM@std@@YAAEAV?$complex@M@0@AEAV10@AEBV10@@Z` | `0x39970` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 931 | `??Ystd@@YAAEAV?$complex@M@0@AEAV10@AEBV10@@Z` | `0x39970` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `??$?YNN@std@@YAAEAV?$complex@N@0@AEAV10@AEBV10@@Z` | `0x399A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 932 | `??Ystd@@YAAEAV?$complex@N@0@AEAV10@AEBV10@@Z` | `0x399A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `??$?YOO@std@@YAAEAV?$complex@O@0@AEAV10@AEBV10@@Z` | `0x399D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 933 | `??Ystd@@YAAEAV?$complex@O@0@AEAV10@AEBV10@@Z` | `0x399D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `??$?ZMM@std@@YAAEAV?$complex@M@0@AEAV10@AEBV10@@Z` | `0x39A00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 937 | `??Zstd@@YAAEAV?$complex@M@0@AEAV10@AEBV10@@Z` | `0x39A00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `??$?ZNN@std@@YAAEAV?$complex@N@0@AEAV10@AEBV10@@Z` | `0x39A30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 938 | `??Zstd@@YAAEAV?$complex@N@0@AEAV10@AEBV10@@Z` | `0x39A30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `??$?ZOO@std@@YAAEAV?$complex@O@0@AEAV10@AEBV10@@Z` | `0x39A60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 939 | `??Zstd@@YAAEAV?$complex@O@0@AEAV10@AEBV10@@Z` | `0x39A60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `??$?_0MM@std@@YAAEAV?$complex@M@0@AEAV10@AEBV10@@Z` | `0x39A90` | 400 | UnwindData |  |
| 943 | `??_0std@@YAAEAV?$complex@M@0@AEAV10@AEBV10@@Z` | `0x39A90` | 400 | UnwindData |  |
| 151 | `??$?_0NN@std@@YAAEAV?$complex@N@0@AEAV10@AEBV10@@Z` | `0x39C30` | 404 | UnwindData |  |
| 944 | `??_0std@@YAAEAV?$complex@N@0@AEAV10@AEBV10@@Z` | `0x39C30` | 404 | UnwindData |  |
| 152 | `??$?_0OO@std@@YAAEAV?$complex@O@0@AEAV10@AEBV10@@Z` | `0x39DD0` | 404 | UnwindData |  |
| 945 | `??_0std@@YAAEAV?$complex@O@0@AEAV10@AEBV10@@Z` | `0x39DD0` | 404 | UnwindData |  |
| 153 | `??$_Fabs@M@std@@YAMAEBV?$complex@M@0@PEAH@Z` | `0x39F70` | 503 | UnwindData |  |
| 154 | `??$_Fabs@M@std@@YAMAEBV?$complex@M@1@PEAH@Z` | `0x39F70` | 503 | UnwindData |  |
| 1148 | `?_Fabs@std@@YAMAEBV?$complex@M@1@PEAH@Z` | `0x39F70` | 503 | UnwindData |  |
| 155 | `??$_Fabs@N@std@@YANAEBV?$complex@N@0@PEAH@Z` | `0x3A170` | 481 | UnwindData |  |
| 156 | `??$_Fabs@N@std@@YANAEBV?$complex@N@1@PEAH@Z` | `0x3A170` | 481 | UnwindData |  |
| 1149 | `?_Fabs@std@@YANAEBV?$complex@N@1@PEAH@Z` | `0x3A170` | 481 | UnwindData |  |
| 157 | `??$_Fabs@O@std@@YAOAEBV?$complex@O@0@PEAH@Z` | `0x3A360` | 481 | UnwindData |  |
| 158 | `??$_Fabs@O@std@@YAOAEBV?$complex@O@1@PEAH@Z` | `0x3A360` | 481 | UnwindData |  |
| 1150 | `?_Fabs@std@@YAOAEBV?$complex@O@1@PEAH@Z` | `0x3A360` | 481 | UnwindData |  |
| 159 | `??$abs@M@std@@YAMAEBV?$complex@M@0@@Z` | `0x3A820` | 46 | UnwindData |  |
| 160 | `??$abs@M@std@@YAMAEBV?$complex@M@1@@Z` | `0x3A820` | 46 | UnwindData |  |
| 1335 | `?abs@std@@YAMAEBV?$complex@M@1@@Z` | `0x3A820` | 46 | UnwindData |  |
| 161 | `??$abs@N@std@@YANAEBV?$complex@N@0@@Z` | `0x3A860` | 38 | UnwindData |  |
| 162 | `??$abs@N@std@@YANAEBV?$complex@N@1@@Z` | `0x3A860` | 38 | UnwindData |  |
| 1336 | `?abs@std@@YANAEBV?$complex@N@1@@Z` | `0x3A860` | 38 | UnwindData |  |
| 163 | `??$abs@O@std@@YAOAEBV?$complex@O@0@@Z` | `0x3A890` | 38 | UnwindData |  |
| 164 | `??$abs@O@std@@YAOAEBV?$complex@O@1@@Z` | `0x3A890` | 38 | UnwindData |  |
| 1337 | `?abs@std@@YAOAEBV?$complex@O@1@@Z` | `0x3A890` | 38 | UnwindData |  |
| 165 | `??$arg@M@std@@YAMAEBV?$complex@M@0@@Z` | `0x3A8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `??$arg@M@std@@YAMAEBV?$complex@M@1@@Z` | `0x3A8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1351 | `?arg@std@@YAMAEBV?$complex@M@1@@Z` | `0x3A8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `??$arg@N@std@@YANAEBV?$complex@N@0@@Z` | `0x3A8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `??$arg@N@std@@YANAEBV?$complex@N@1@@Z` | `0x3A8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1352 | `?arg@std@@YANAEBV?$complex@N@1@@Z` | `0x3A8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `??$arg@O@std@@YAOAEBV?$complex@O@0@@Z` | `0x3A900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `??$arg@O@std@@YAOAEBV?$complex@O@1@@Z` | `0x3A900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1353 | `?arg@std@@YAOAEBV?$complex@O@1@@Z` | `0x3A900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `??$conj@M@std@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x3A920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `??$conj@M@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3A920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1423 | `?conj@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3A920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `??$conj@N@std@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x3A940` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `??$conj@N@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3A940` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1424 | `?conj@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3A940` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `??$conj@O@std@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x3A970` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `??$conj@O@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3A970` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `?conj@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3A970` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `??$cos@M@std@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x3A9A0` | 103 | UnwindData |  |
| 178 | `??$cos@M@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3A9A0` | 103 | UnwindData |  |
| 1436 | `?cos@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3A9A0` | 103 | UnwindData |  |
| 179 | `??$cos@N@std@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x3AA10` | 103 | UnwindData |  |
| 180 | `??$cos@N@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3AA10` | 103 | UnwindData |  |
| 1437 | `?cos@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3AA10` | 103 | UnwindData |  |
| 181 | `??$cos@O@std@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x3AA80` | 103 | UnwindData |  |
| 182 | `??$cos@O@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3AA80` | 103 | UnwindData |  |
| 1438 | `?cos@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3AA80` | 103 | UnwindData |  |
| 183 | `??$cosh@M@std@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x3AAF0` | 96 | UnwindData |  |
| 184 | `??$cosh@M@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3AAF0` | 96 | UnwindData |  |
| 1439 | `?cosh@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3AAF0` | 96 | UnwindData |  |
| 185 | `??$cosh@N@std@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x3AB60` | 96 | UnwindData |  |
| 186 | `??$cosh@N@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3AB60` | 96 | UnwindData |  |
| 1440 | `?cosh@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3AB60` | 96 | UnwindData |  |
| 187 | `??$cosh@O@std@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x3ABD0` | 96 | UnwindData |  |
| 188 | `??$cosh@O@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3ABD0` | 96 | UnwindData |  |
| 1441 | `?cosh@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3ABD0` | 96 | UnwindData |  |
| 189 | `??$exp@M@std@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x3AC40` | 132 | UnwindData |  |
| 190 | `??$exp@M@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3AC40` | 132 | UnwindData |  |
| 1644 | `?exp@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3AC40` | 132 | UnwindData |  |
| 191 | `??$exp@N@std@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x3ACD0` | 132 | UnwindData |  |
| 192 | `??$exp@N@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3ACD0` | 132 | UnwindData |  |
| 1645 | `?exp@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3ACD0` | 132 | UnwindData |  |
| 193 | `??$exp@O@std@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x3AD60` | 132 | UnwindData |  |
| 194 | `??$exp@O@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3AD60` | 132 | UnwindData |  |
| 1646 | `?exp@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3AD60` | 132 | UnwindData |  |
| 195 | `??$getline@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@@Z` | `0x3ADF0` | 57 | UnwindData |  |
| 197 | `??$getline@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@1@AEAV21@AEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@@Z` | `0x3ADF0` | 57 | UnwindData |  |
| 1765 | `?getline@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@1@AEAV21@AEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@@Z` | `0x3ADF0` | 57 | UnwindData |  |
| 196 | `??$getline@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@0@AEAV10@AEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@0@D@Z` | `0x3AE30` | 334 | UnwindData |  |
| 198 | `??$getline@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@1@AEAV21@AEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@D@Z` | `0x3AE30` | 334 | UnwindData |  |
| 1766 | `?getline@std@@YAAEAV?$basic_istream@DU?$char_traits@D@std@@@1@AEAV21@AEAV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@D@Z` | `0x3AE30` | 334 | UnwindData |  |
| 199 | `??$getline@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@@Z` | `0x3AF90` | 58 | UnwindData |  |
| 201 | `??$getline@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@1@AEAV21@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@1@@Z` | `0x3AF90` | 58 | UnwindData |  |
| 1767 | `?getline@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@1@AEAV21@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@1@@Z` | `0x3AF90` | 58 | UnwindData |  |
| 200 | `??$getline@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@0@AEAV10@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@0@G@Z` | `0x3AFD0` | 354 | UnwindData |  |
| 202 | `??$getline@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@1@AEAV21@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@1@G@Z` | `0x3AFD0` | 354 | UnwindData |  |
| 1768 | `?getline@std@@YAAEAV?$basic_istream@GU?$char_traits@G@std@@@1@AEAV21@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@1@G@Z` | `0x3AFD0` | 354 | UnwindData |  |
| 203 | `??$imag@M@std@@YAMAEBV?$complex@M@0@@Z` | `0x3B140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `??$imag@M@std@@YAMAEBV?$complex@M@1@@Z` | `0x3B140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1816 | `?imag@std@@YAMAEBV?$complex@M@1@@Z` | `0x3B140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `??$imag@N@std@@YANAEBV?$complex@N@0@@Z` | `0x3B150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `??$imag@N@std@@YANAEBV?$complex@N@1@@Z` | `0x3B150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1817 | `?imag@std@@YANAEBV?$complex@N@1@@Z` | `0x3B150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `??$imag@O@std@@YAOAEBV?$complex@O@0@@Z` | `0x3B160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `??$imag@O@std@@YAOAEBV?$complex@O@1@@Z` | `0x3B160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1818 | `?imag@std@@YAOAEBV?$complex@O@1@@Z` | `0x3B160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `??$log10@M@std@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x3B170` | 70 | UnwindData |  |
| 210 | `??$log10@M@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3B170` | 70 | UnwindData |  |
| 1889 | `?log10@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3B170` | 70 | UnwindData |  |
| 211 | `??$log10@N@std@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x3B1C0` | 49 | UnwindData |  |
| 212 | `??$log10@N@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3B1C0` | 49 | UnwindData |  |
| 1890 | `?log10@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3B1C0` | 49 | UnwindData |  |
| 213 | `??$log10@O@std@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x3B200` | 49 | UnwindData |  |
| 214 | `??$log10@O@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3B200` | 49 | UnwindData |  |
| 1891 | `?log10@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3B200` | 49 | UnwindData |  |
| 215 | `??$log@M@std@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x3B240` | 253 | UnwindData |  |
| 216 | `??$log@M@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3B240` | 253 | UnwindData |  |
| 1895 | `?log@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3B240` | 253 | UnwindData |  |
| 217 | `??$log@N@std@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x3B350` | 255 | UnwindData |  |
| 218 | `??$log@N@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3B350` | 255 | UnwindData |  |
| 1896 | `?log@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3B350` | 255 | UnwindData |  |
| 219 | `??$log@O@std@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x3B460` | 255 | UnwindData |  |
| 220 | `??$log@O@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3B460` | 255 | UnwindData |  |
| 1897 | `?log@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3B460` | 255 | UnwindData |  |
| 221 | `??$norm@M@std@@YAMAEBV?$complex@M@0@@Z` | `0x3B570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `??$norm@M@std@@YAMAEBV?$complex@M@1@@Z` | `0x3B570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1942 | `?norm@std@@YAMAEBV?$complex@M@1@@Z` | `0x3B570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `??$norm@N@std@@YANAEBV?$complex@N@0@@Z` | `0x3B590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `??$norm@N@std@@YANAEBV?$complex@N@1@@Z` | `0x3B590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1943 | `?norm@std@@YANAEBV?$complex@N@1@@Z` | `0x3B590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `??$norm@O@std@@YAOAEBV?$complex@O@0@@Z` | `0x3B5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `??$norm@O@std@@YAOAEBV?$complex@O@1@@Z` | `0x3B5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1944 | `?norm@std@@YAOAEBV?$complex@O@1@@Z` | `0x3B5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `??$polar@M@std@@YA?AV?$complex@M@0@AEBM0@Z` | `0x3B5D0` | 79 | UnwindData |  |
| 229 | `??$polar@M@std@@YA?AV?$complex@M@1@AEBM0@Z` | `0x3B5D0` | 79 | UnwindData |  |
| 1994 | `?polar@std@@YA?AV?$complex@M@1@AEBM0@Z` | `0x3B5D0` | 79 | UnwindData |  |
| 228 | `??$polar@M@std@@YA?AV?$complex@M@0@AEBM@Z` | `0x3B630` | 63 | UnwindData |  |
| 230 | `??$polar@M@std@@YA?AV?$complex@M@1@AEBM@Z` | `0x3B630` | 63 | UnwindData |  |
| 1995 | `?polar@std@@YA?AV?$complex@M@1@AEBM@Z` | `0x3B630` | 63 | UnwindData |  |
| 231 | `??$polar@N@std@@YA?AV?$complex@N@0@AEBN0@Z` | `0x3B680` | 79 | UnwindData |  |
| 233 | `??$polar@N@std@@YA?AV?$complex@N@1@AEBN0@Z` | `0x3B680` | 79 | UnwindData |  |
| 1996 | `?polar@std@@YA?AV?$complex@N@1@AEBN0@Z` | `0x3B680` | 79 | UnwindData |  |
| 232 | `??$polar@N@std@@YA?AV?$complex@N@0@AEBN@Z` | `0x3B6E0` | 63 | UnwindData |  |
| 234 | `??$polar@N@std@@YA?AV?$complex@N@1@AEBN@Z` | `0x3B6E0` | 63 | UnwindData |  |
| 1997 | `?polar@std@@YA?AV?$complex@N@1@AEBN@Z` | `0x3B6E0` | 63 | UnwindData |  |
| 235 | `??$polar@O@std@@YA?AV?$complex@O@0@AEBO0@Z` | `0x3B730` | 79 | UnwindData |  |
| 237 | `??$polar@O@std@@YA?AV?$complex@O@1@AEBO0@Z` | `0x3B730` | 79 | UnwindData |  |
| 1998 | `?polar@std@@YA?AV?$complex@O@1@AEBO0@Z` | `0x3B730` | 79 | UnwindData |  |
| 236 | `??$polar@O@std@@YA?AV?$complex@O@0@AEBO@Z` | `0x3B790` | 63 | UnwindData |  |
| 238 | `??$polar@O@std@@YA?AV?$complex@O@1@AEBO@Z` | `0x3B790` | 63 | UnwindData |  |
| 1999 | `?polar@std@@YA?AV?$complex@O@1@AEBO@Z` | `0x3B790` | 63 | UnwindData |  |
| 239 | `??$pow@M@std@@YA?AV?$complex@M@0@AEBMAEBV10@@Z` | `0x3B7E0` | 135 | UnwindData |  |
| 243 | `??$pow@M@std@@YA?AV?$complex@M@1@AEBMAEBV21@@Z` | `0x3B7E0` | 135 | UnwindData |  |
| 2007 | `?pow@std@@YA?AV?$complex@M@1@AEBMAEBV21@@Z` | `0x3B7E0` | 135 | UnwindData |  |
| 240 | `??$pow@M@std@@YA?AV?$complex@M@0@AEBV10@0@Z` | `0x3B870` | 179 | UnwindData |  |
| 244 | `??$pow@M@std@@YA?AV?$complex@M@1@AEBV21@0@Z` | `0x3B870` | 179 | UnwindData |  |
| 2008 | `?pow@std@@YA?AV?$complex@M@1@AEBV21@0@Z` | `0x3B870` | 179 | UnwindData |  |
| 241 | `??$pow@M@std@@YA?AV?$complex@M@0@AEBV10@AEBM@Z` | `0x3B930` | 149 | UnwindData |  |
| 245 | `??$pow@M@std@@YA?AV?$complex@M@1@AEBV21@AEBM@Z` | `0x3B930` | 149 | UnwindData |  |
| 2009 | `?pow@std@@YA?AV?$complex@M@1@AEBV21@AEBM@Z` | `0x3B930` | 149 | UnwindData |  |
| 242 | `??$pow@M@std@@YA?AV?$complex@M@0@AEBV10@H@Z` | `0x3B9D0` | 69 | UnwindData |  |
| 246 | `??$pow@M@std@@YA?AV?$complex@M@1@AEBV21@H@Z` | `0x3B9D0` | 69 | UnwindData |  |
| 2010 | `?pow@std@@YA?AV?$complex@M@1@AEBV21@H@Z` | `0x3B9D0` | 69 | UnwindData |  |
| 247 | `??$pow@N@std@@YA?AV?$complex@N@0@AEBNAEBV10@@Z` | `0x3BA20` | 130 | UnwindData |  |
| 251 | `??$pow@N@std@@YA?AV?$complex@N@1@AEBNAEBV21@@Z` | `0x3BA20` | 130 | UnwindData |  |
| 2011 | `?pow@std@@YA?AV?$complex@N@1@AEBNAEBV21@@Z` | `0x3BA20` | 130 | UnwindData |  |
| 248 | `??$pow@N@std@@YA?AV?$complex@N@0@AEBV10@0@Z` | `0x3BAB0` | 190 | UnwindData |  |
| 252 | `??$pow@N@std@@YA?AV?$complex@N@1@AEBV21@0@Z` | `0x3BAB0` | 190 | UnwindData |  |
| 2012 | `?pow@std@@YA?AV?$complex@N@1@AEBV21@0@Z` | `0x3BAB0` | 190 | UnwindData |  |
| 249 | `??$pow@N@std@@YA?AV?$complex@N@0@AEBV10@AEBN@Z` | `0x3BB80` | 154 | UnwindData |  |
| 253 | `??$pow@N@std@@YA?AV?$complex@N@1@AEBV21@AEBN@Z` | `0x3BB80` | 154 | UnwindData |  |
| 2013 | `?pow@std@@YA?AV?$complex@N@1@AEBV21@AEBN@Z` | `0x3BB80` | 154 | UnwindData |  |
| 250 | `??$pow@N@std@@YA?AV?$complex@N@0@AEBV10@H@Z` | `0x3BC20` | 83 | UnwindData |  |
| 254 | `??$pow@N@std@@YA?AV?$complex@N@1@AEBV21@H@Z` | `0x3BC20` | 83 | UnwindData |  |
| 2014 | `?pow@std@@YA?AV?$complex@N@1@AEBV21@H@Z` | `0x3BC20` | 83 | UnwindData |  |
| 255 | `??$pow@O@std@@YA?AV?$complex@O@0@AEBOAEBV10@@Z` | `0x3BC80` | 130 | UnwindData |  |
| 259 | `??$pow@O@std@@YA?AV?$complex@O@1@AEBOAEBV21@@Z` | `0x3BC80` | 130 | UnwindData |  |
| 2015 | `?pow@std@@YA?AV?$complex@O@1@AEBOAEBV21@@Z` | `0x3BC80` | 130 | UnwindData |  |
| 256 | `??$pow@O@std@@YA?AV?$complex@O@0@AEBV10@0@Z` | `0x3BD10` | 190 | UnwindData |  |
| 260 | `??$pow@O@std@@YA?AV?$complex@O@1@AEBV21@0@Z` | `0x3BD10` | 190 | UnwindData |  |
| 2016 | `?pow@std@@YA?AV?$complex@O@1@AEBV21@0@Z` | `0x3BD10` | 190 | UnwindData |  |
| 257 | `??$pow@O@std@@YA?AV?$complex@O@0@AEBV10@AEBO@Z` | `0x3BDE0` | 154 | UnwindData |  |
| 261 | `??$pow@O@std@@YA?AV?$complex@O@1@AEBV21@AEBO@Z` | `0x3BDE0` | 154 | UnwindData |  |
| 2017 | `?pow@std@@YA?AV?$complex@O@1@AEBV21@AEBO@Z` | `0x3BDE0` | 154 | UnwindData |  |
| 258 | `??$pow@O@std@@YA?AV?$complex@O@0@AEBV10@H@Z` | `0x3BE80` | 83 | UnwindData |  |
| 262 | `??$pow@O@std@@YA?AV?$complex@O@1@AEBV21@H@Z` | `0x3BE80` | 83 | UnwindData |  |
| 2018 | `?pow@std@@YA?AV?$complex@O@1@AEBV21@H@Z` | `0x3BE80` | 83 | UnwindData |  |
| 263 | `??$real@M@std@@YAMAEBV?$complex@M@0@@Z` | `0x3BEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `??$real@M@std@@YAMAEBV?$complex@M@1@@Z` | `0x3BEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2110 | `?real@std@@YAMAEBV?$complex@M@1@@Z` | `0x3BEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `??$real@N@std@@YANAEBV?$complex@N@0@@Z` | `0x3BEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `??$real@N@std@@YANAEBV?$complex@N@1@@Z` | `0x3BEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2111 | `?real@std@@YANAEBV?$complex@N@1@@Z` | `0x3BEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `??$real@O@std@@YAOAEBV?$complex@O@0@@Z` | `0x3BF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `??$real@O@std@@YAOAEBV?$complex@O@1@@Z` | `0x3BF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2112 | `?real@std@@YAOAEBV?$complex@O@1@@Z` | `0x3BF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `??$sin@M@std@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x3BF10` | 96 | UnwindData |  |
| 270 | `??$sin@M@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3BF10` | 96 | UnwindData |  |
| 2238 | `?sin@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3BF10` | 96 | UnwindData |  |
| 271 | `??$sin@N@std@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x3BF80` | 96 | UnwindData |  |
| 272 | `??$sin@N@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3BF80` | 96 | UnwindData |  |
| 2239 | `?sin@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3BF80` | 96 | UnwindData |  |
| 273 | `??$sin@O@std@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x3BFF0` | 96 | UnwindData |  |
| 274 | `??$sin@O@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3BFF0` | 96 | UnwindData |  |
| 2240 | `?sin@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3BFF0` | 96 | UnwindData |  |
| 275 | `??$sinh@M@std@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x3C060` | 96 | UnwindData |  |
| 276 | `??$sinh@M@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3C060` | 96 | UnwindData |  |
| 2241 | `?sinh@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3C060` | 96 | UnwindData |  |
| 277 | `??$sinh@N@std@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x3C0D0` | 96 | UnwindData |  |
| 278 | `??$sinh@N@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3C0D0` | 96 | UnwindData |  |
| 2242 | `?sinh@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3C0D0` | 96 | UnwindData |  |
| 279 | `??$sinh@O@std@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x3C140` | 96 | UnwindData |  |
| 280 | `??$sinh@O@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3C140` | 96 | UnwindData |  |
| 2243 | `?sinh@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3C140` | 96 | UnwindData |  |
| 281 | `??$sqrt@M@std@@YA?AV?$complex@M@0@AEBV10@@Z` | `0x3C1B0` | 253 | UnwindData |  |
| 282 | `??$sqrt@M@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3C1B0` | 253 | UnwindData |  |
| 2257 | `?sqrt@std@@YA?AV?$complex@M@1@AEBV21@@Z` | `0x3C1B0` | 253 | UnwindData |  |
| 283 | `??$sqrt@N@std@@YA?AV?$complex@N@0@AEBV10@@Z` | `0x3C2C0` | 235 | UnwindData |  |
| 284 | `??$sqrt@N@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3C2C0` | 235 | UnwindData |  |
| 2258 | `?sqrt@std@@YA?AV?$complex@N@1@AEBV21@@Z` | `0x3C2C0` | 235 | UnwindData |  |
| 285 | `??$sqrt@O@std@@YA?AV?$complex@O@0@AEBV10@@Z` | `0x3C3C0` | 235 | UnwindData |  |
| 286 | `??$sqrt@O@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3C3C0` | 235 | UnwindData |  |
| 2259 | `?sqrt@std@@YA?AV?$complex@O@1@AEBV21@@Z` | `0x3C3C0` | 235 | UnwindData |  |
| 287 | `??0?$_Complex_base@M@std@@QEAA@AEBM0@Z` | `0x3C4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `??0?$_Complex_base@N@std@@QEAA@AEBN0@Z` | `0x3C4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `??0?$_Complex_base@O@std@@QEAA@AEBO0@Z` | `0x3C500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `??0?$basic_istringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@AEBV01@@Z` | `0x3C520` | 205 | UnwindData |  |
| 329 | `??0?$basic_istringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@H@Z` | `0x3C600` | 153 | UnwindData |  |
| 330 | `??0?$basic_istringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@H@Z` | `0x3C6A0` | 150 | UnwindData |  |
| 331 | `??0?$basic_istringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@AEBV01@@Z` | `0x3C740` | 205 | UnwindData |  |
| 332 | `??0?$basic_istringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@1@H@Z` | `0x3C820` | 153 | UnwindData |  |
| 333 | `??0?$basic_istringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@H@Z` | `0x3C8C0` | 150 | UnwindData |  |
| 346 | `??0?$basic_ostringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@AEBV01@@Z` | `0x3C960` | 191 | UnwindData |  |
| 347 | `??0?$basic_ostringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@H@Z` | `0x3CA30` | 160 | UnwindData |  |
| 348 | `??0?$basic_ostringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@H@Z` | `0x3CAE0` | 157 | UnwindData |  |
| 349 | `??0?$basic_ostringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@AEBV01@@Z` | `0x3CB90` | 191 | UnwindData |  |
| 350 | `??0?$basic_ostringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@1@H@Z` | `0x3CC60` | 160 | UnwindData |  |
| 351 | `??0?$basic_ostringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@H@Z` | `0x3CD10` | 157 | UnwindData |  |
| 372 | `??0?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@AEBV01@@Z` | `0x3CDC0` | 73 | UnwindData |  |
| 373 | `??0?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@H@Z` | `0x3CE10` | 126 | UnwindData |  |
| 374 | `??0?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@H@Z` | `0x3CEA0` | 142 | UnwindData |  |
| 375 | `??0?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@AEBV01@@Z` | `0x3CF40` | 73 | UnwindData |  |
| 376 | `??0?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@1@H@Z` | `0x3CF90` | 126 | UnwindData |  |
| 377 | `??0?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@H@Z` | `0x3D020` | 142 | UnwindData |  |
| 378 | `??0?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@AEBV01@@Z` | `0x3D0C0` | 260 | UnwindData |  |
| 379 | `??0?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@1@H@Z` | `0x3D1D0` | 199 | UnwindData |  |
| 380 | `??0?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAA@H@Z` | `0x3D2A0` | 196 | UnwindData |  |
| 381 | `??0?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@AEBV01@@Z` | `0x3D370` | 260 | UnwindData |  |
| 382 | `??0?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@1@H@Z` | `0x3D480` | 199 | UnwindData |  |
| 383 | `??0?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAA@H@Z` | `0x3D550` | 196 | UnwindData |  |
| 392 | `??0?$complex@M@std@@QEAA@AEBM0@Z` | `0x3D620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `??0?$complex@M@std@@QEAA@AEBV?$complex@N@1@@Z` | `0x3D640` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `??0?$complex@M@std@@QEAA@AEBV?$complex@O@1@@Z` | `0x3D670` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `??0?$complex@N@std@@QEAA@AEBN0@Z` | `0x3D6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `??0?$complex@N@std@@QEAA@AEBV?$complex@M@1@@Z` | `0x3D6C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `??0?$complex@N@std@@QEAA@AEBV?$complex@O@1@@Z` | `0x3D6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `??0?$complex@O@std@@QEAA@AEBO0@Z` | `0x3D710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `??0?$complex@O@std@@QEAA@AEBV?$complex@M@1@@Z` | `0x3D730` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `??0?$complex@O@std@@QEAA@AEBV?$complex@N@1@@Z` | `0x3D760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `??1?$basic_istringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@UEAA@XZ` | `0x3D780` | 131 | UnwindData |  |
| 513 | `??1?$basic_istringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@UEAA@XZ` | `0x3D810` | 131 | UnwindData |  |
| 518 | `??1?$basic_ostringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@UEAA@XZ` | `0x3D8A0` | 131 | UnwindData |  |
| 519 | `??1?$basic_ostringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@UEAA@XZ` | `0x3D930` | 131 | UnwindData |  |
| 524 | `??1?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@UEAA@XZ` | `0x3D9C0` | 70 | UnwindData |  |
| 525 | `??1?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@UEAA@XZ` | `0x3DA10` | 70 | UnwindData |  |
| 526 | `??1?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@UEAA@XZ` | `0x3DA60` | 183 | UnwindData |  |
| 527 | `??1?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@UEAA@XZ` | `0x3DB20` | 183 | UnwindData |  |
| 584 | `??4?$_Complex_base@M@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3DBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 585 | `??4?$_Complex_base@M@std@@QEAAAEAV01@AEBV01@@Z` | `0x3DC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 586 | `??4?$_Complex_base@N@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3DC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 587 | `??4?$_Complex_base@N@std@@QEAAAEAV01@AEBV01@@Z` | `0x3DC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `??4?$_Complex_base@O@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3DC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 589 | `??4?$_Complex_base@O@std@@QEAAAEAV01@AEBV01@@Z` | `0x3DC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `??4?$_Ctr@M@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3DCA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 591 | `??4?$_Ctr@M@std@@QEAAAEAV01@AEBV01@@Z` | `0x3DCB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `??4?$_Ctr@N@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3DCC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `??4?$_Ctr@N@std@@QEAAAEAV01@AEBV01@@Z` | `0x3DCD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `??4?$_Ctr@O@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3DCE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 595 | `??4?$_Ctr@O@std@@QEAAAEAV01@AEBV01@@Z` | `0x3DCF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 610 | `??4?$basic_istringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV01@AEBV01@@Z` | `0x3DD00` | 104 | UnwindData |  |
| 611 | `??4?$basic_istringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV01@AEBV01@@Z` | `0x3DD70` | 104 | UnwindData |  |
| 616 | `??4?$basic_ostringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV01@AEBV01@@Z` | `0x3DDE0` | 171 | UnwindData |  |
| 617 | `??4?$basic_ostringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV01@AEBV01@@Z` | `0x3DEA0` | 173 | UnwindData |  |
| 626 | `??4?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV01@AEBV01@@Z` | `0x3DF60` | 63 | UnwindData |  |
| 627 | `??4?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV01@AEBV01@@Z` | `0x3DFB0` | 63 | UnwindData |  |
| 628 | `??4?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E000` | 110 | UnwindData |  |
| 629 | `??4?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E080` | 110 | UnwindData |  |
| 634 | `??4?$complex@M@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 635 | `??4?$complex@M@std@@QEAAAEAV01@AEBM@Z` | `0x3E120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 636 | `??4?$complex@M@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 637 | `??4?$complex@N@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | `??4?$complex@N@std@@QEAAAEAV01@AEBN@Z` | `0x3E180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `??4?$complex@N@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 640 | `??4?$complex@O@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 641 | `??4?$complex@O@std@@QEAAAEAV01@AEBO@Z` | `0x3E1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 642 | `??4?$complex@O@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 643 | `??4?$numeric_limits@C@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `??4?$numeric_limits@C@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 645 | `??4?$numeric_limits@D@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 646 | `??4?$numeric_limits@D@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 647 | `??4?$numeric_limits@E@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 648 | `??4?$numeric_limits@E@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 649 | `??4?$numeric_limits@F@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `??4?$numeric_limits@F@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | `??4?$numeric_limits@G@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `??4?$numeric_limits@G@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `??4?$numeric_limits@H@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `??4?$numeric_limits@H@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 655 | `??4?$numeric_limits@I@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 656 | `??4?$numeric_limits@I@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 657 | `??4?$numeric_limits@J@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 658 | `??4?$numeric_limits@J@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 659 | `??4?$numeric_limits@K@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | `??4?$numeric_limits@K@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 661 | `??4?$numeric_limits@M@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 662 | `??4?$numeric_limits@M@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 663 | `??4?$numeric_limits@N@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `??4?$numeric_limits@N@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `??4?$numeric_limits@O@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 666 | `??4?$numeric_limits@O@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 667 | `??4?$numeric_limits@_N@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x3E3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 668 | `??4?$numeric_limits@_N@std@@QEAAAEAV01@AEBV01@@Z` | `0x3E3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 672 | `??4_Num_base@std@@QEAAAEAU01@$$QEAU01@@Z` | `0x3E3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 673 | `??4_Num_base@std@@QEAAAEAU01@AEBU01@@Z` | `0x3E3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `??4_Num_float_base@std@@QEAAAEAU01@$$QEAU01@@Z` | `0x3E3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 675 | `??4_Num_float_base@std@@QEAAAEAU01@AEBU01@@Z` | `0x3E3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 676 | `??4_Num_int_base@std@@QEAAAEAU01@$$QEAU01@@Z` | `0x3E400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 677 | `??4_Num_int_base@std@@QEAAAEAU01@AEBU01@@Z` | `0x3E410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 916 | `??X?$_Complex_base@M@std@@QEAAAEAV01@AEBM@Z` | `0x3E420` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 917 | `??X?$_Complex_base@N@std@@QEAAAEAV01@AEBN@Z` | `0x3E450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 918 | `??X?$_Complex_base@O@std@@QEAAAEAV01@AEBO@Z` | `0x3E480` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 922 | `??Y?$_Complex_base@M@std@@QEAAAEAV01@AEBM@Z` | `0x3E4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 923 | `??Y?$_Complex_base@N@std@@QEAAAEAV01@AEBN@Z` | `0x3E4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 924 | `??Y?$_Complex_base@O@std@@QEAAAEAV01@AEBO@Z` | `0x3E4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 934 | `??Z?$_Complex_base@M@std@@QEAAAEAV01@AEBM@Z` | `0x3E510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 935 | `??Z?$_Complex_base@N@std@@QEAAAEAV01@AEBN@Z` | `0x3E530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `??Z?$_Complex_base@O@std@@QEAAAEAV01@AEBO@Z` | `0x3E550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 940 | `??_0?$_Complex_base@M@std@@QEAAAEAV01@AEBM@Z` | `0x3E570` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 941 | `??_0?$_Complex_base@N@std@@QEAAAEAV01@AEBN@Z` | `0x3E5A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `??_0?$_Complex_base@O@std@@QEAAAEAV01@AEBO@Z` | `0x3E5D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `??_D?$basic_istringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXXZ` | `0x3E600` | 44 | UnwindData |  |
| 1053 | `??_D?$basic_istringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXXZ` | `0x3E640` | 44 | UnwindData |  |
| 1058 | `??_D?$basic_ostringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXXZ` | `0x3E680` | 44 | UnwindData |  |
| 1059 | `??_D?$basic_ostringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXXZ` | `0x3E6C0` | 44 | UnwindData |  |
| 1060 | `??_D?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXXZ` | `0x3E700` | 44 | UnwindData |  |
| 1061 | `??_D?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXXZ` | `0x3E740` | 44 | UnwindData |  |
| 1064 | `??_F?$basic_istringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXXZ` | `0x3ECA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1065 | `??_F?$basic_istringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXXZ` | `0x3ECC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `??_F?$basic_ostringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXXZ` | `0x3ECE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1067 | `??_F?$basic_ostringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXXZ` | `0x3ED00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1070 | `??_F?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXXZ` | `0x3ED20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1071 | `??_F?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXXZ` | `0x3ED30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `??_F?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXXZ` | `0x3ED40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `??_F?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXXZ` | `0x3ED60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `??_F?$complex@M@std@@QEAAXXZ` | `0x3ED80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1079 | `??_F?$complex@N@std@@QEAAXXZ` | `0x3ED90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1080 | `??_F?$complex@O@std@@QEAAXXZ` | `0x3EDA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1127 | `?_Cosh@?$_Ctr@M@std@@SAMMM@Z` | `0x3EDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `?_Cosh@?$_Ctr@N@std@@SANNN@Z` | `0x3EDC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1129 | `?_Cosh@?$_Ctr@O@std@@SAOOO@Z` | `0x3EDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1145 | `?_Exp@?$_Ctr@M@std@@SAFPEAMMF@Z` | `0x3EDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `?_Exp@?$_Ctr@N@std@@SAFPEANNF@Z` | `0x3EDF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1147 | `?_Exp@?$_Ctr@O@std@@SAFPEAOOF@Z` | `0x3EE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1224 | `?_Infv@?$_Ctr@M@std@@SAMM@Z` | `0x3EE10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `?_Infv@?$_Ctr@N@std@@SANN@Z` | `0x3EE20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `?_Infv@?$_Ctr@O@std@@SAOO@Z` | `0x3EE30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1235 | `?_Init@?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@IEAAXPEBD_KH@Z` | `0x3EE40` | 268 | UnwindData |  |
| 1236 | `?_Init@?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@IEAAXPEBG_KH@Z` | `0x3EF60` | 277 | UnwindData |  |
| 1269 | `?_Isinf@?$_Ctr@M@std@@SA_NM@Z` | `0x3F080` | 32 | UnwindData |  |
| 1270 | `?_Isinf@?$_Ctr@N@std@@SA_NN@Z` | `0x3F0B0` | 32 | UnwindData |  |
| 1271 | `?_Isinf@?$_Ctr@O@std@@SA_NO@Z` | `0x3F0E0` | 32 | UnwindData |  |
| 1272 | `?_Isnan@?$_Ctr@M@std@@SA_NM@Z` | `0x3F110` | 32 | UnwindData |  |
| 1273 | `?_Isnan@?$_Ctr@N@std@@SA_NN@Z` | `0x3F140` | 32 | UnwindData |  |
| 1274 | `?_Isnan@?$_Ctr@O@std@@SA_NO@Z` | `0x3F170` | 32 | UnwindData |  |
| 1277 | `?_Mode@?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAAHH@Z` | `0x3F1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `?_Mode@?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAAHH@Z` | `0x3F1C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1279 | `?_Nanv@?$_Ctr@M@std@@SAMM@Z` | `0x3F1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1280 | `?_Nanv@?$_Ctr@N@std@@SANN@Z` | `0x3F1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1281 | `?_Nanv@?$_Ctr@O@std@@SAOO@Z` | `0x3F200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1310 | `?_Sinh@?$_Ctr@M@std@@SAMMM@Z` | `0x3F210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `?_Sinh@?$_Ctr@N@std@@SANNN@Z` | `0x3F220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1312 | `?_Sinh@?$_Ctr@O@std@@SAOOO@Z` | `0x3F230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `?_Tidy@?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@IEAAXXZ` | `0x3F240` | 42 | UnwindData |  |
| 1322 | `?_Tidy@?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@IEAAXXZ` | `0x3F270` | 42 | UnwindData |  |
| 1374 | `?atan2@?$_Ctr@M@std@@SAMMM@Z` | `0x3F2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1375 | `?atan2@?$_Ctr@N@std@@SANNN@Z` | `0x3F2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1376 | `?atan2@?$_Ctr@O@std@@SAOOO@Z` | `0x3F2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1433 | `?cos@?$_Ctr@M@std@@SAMM@Z` | `0x3F2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1434 | `?cos@?$_Ctr@N@std@@SANN@Z` | `0x3F2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1435 | `?cos@?$_Ctr@O@std@@SAOO@Z` | `0x3F2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1453 | `?denorm_min@?$numeric_limits@C@std@@SACXZ` | `0x3F300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1454 | `?denorm_min@?$numeric_limits@D@std@@SADXZ` | `0x3F310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1455 | `?denorm_min@?$numeric_limits@E@std@@SAEXZ` | `0x3F320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1456 | `?denorm_min@?$numeric_limits@F@std@@SAFXZ` | `0x3F330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1457 | `?denorm_min@?$numeric_limits@G@std@@SAGXZ` | `0x3F340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1458 | `?denorm_min@?$numeric_limits@H@std@@SAHXZ` | `0x3F350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1459 | `?denorm_min@?$numeric_limits@I@std@@SAIXZ` | `0x3F360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1460 | `?denorm_min@?$numeric_limits@J@std@@SAJXZ` | `0x3F370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1461 | `?denorm_min@?$numeric_limits@K@std@@SAKXZ` | `0x3F380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1462 | `?denorm_min@?$numeric_limits@M@std@@SAMXZ` | `0x3F390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1463 | `?denorm_min@?$numeric_limits@N@std@@SANXZ` | `0x3F3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1464 | `?denorm_min@?$numeric_limits@O@std@@SAOXZ` | `0x3F3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1465 | `?denorm_min@?$numeric_limits@_N@std@@SA_NXZ` | `0x3F3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1615 | `?epsilon@?$numeric_limits@C@std@@SACXZ` | `0x3F3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1616 | `?epsilon@?$numeric_limits@D@std@@SADXZ` | `0x3F3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `?epsilon@?$numeric_limits@E@std@@SAEXZ` | `0x3F3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1618 | `?epsilon@?$numeric_limits@F@std@@SAFXZ` | `0x3F400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1619 | `?epsilon@?$numeric_limits@G@std@@SAGXZ` | `0x3F410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1620 | `?epsilon@?$numeric_limits@H@std@@SAHXZ` | `0x3F420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `?epsilon@?$numeric_limits@I@std@@SAIXZ` | `0x3F430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1622 | `?epsilon@?$numeric_limits@J@std@@SAJXZ` | `0x3F440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1623 | `?epsilon@?$numeric_limits@K@std@@SAKXZ` | `0x3F450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1624 | `?epsilon@?$numeric_limits@M@std@@SAMXZ` | `0x3F460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1625 | `?epsilon@?$numeric_limits@N@std@@SANXZ` | `0x3F470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1626 | `?epsilon@?$numeric_limits@O@std@@SAOXZ` | `0x3F480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1627 | `?epsilon@?$numeric_limits@_N@std@@SA_NXZ` | `0x3F490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1641 | `?exp@?$_Ctr@M@std@@SAMM@Z` | `0x3F4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `?exp@?$_Ctr@N@std@@SANN@Z` | `0x3F4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1643 | `?exp@?$_Ctr@O@std@@SAOO@Z` | `0x3F4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1810 | `?imag@?$_Complex_base@M@std@@QEAAMAEBM@Z` | `0x3F4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1811 | `?imag@?$_Complex_base@M@std@@QEBAMXZ` | `0x3F4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1812 | `?imag@?$_Complex_base@N@std@@QEAANAEBN@Z` | `0x3F4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1813 | `?imag@?$_Complex_base@N@std@@QEBANXZ` | `0x3F500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1814 | `?imag@?$_Complex_base@O@std@@QEAAOAEBO@Z` | `0x3F510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1815 | `?imag@?$_Complex_base@O@std@@QEBAOXZ` | `0x3F520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1828 | `?infinity@?$numeric_limits@C@std@@SACXZ` | `0x3F530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1829 | `?infinity@?$numeric_limits@D@std@@SADXZ` | `0x3F540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1830 | `?infinity@?$numeric_limits@E@std@@SAEXZ` | `0x3F550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1831 | `?infinity@?$numeric_limits@F@std@@SAFXZ` | `0x3F560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1832 | `?infinity@?$numeric_limits@G@std@@SAGXZ` | `0x3F570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1833 | `?infinity@?$numeric_limits@H@std@@SAHXZ` | `0x3F580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1834 | `?infinity@?$numeric_limits@I@std@@SAIXZ` | `0x3F590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1835 | `?infinity@?$numeric_limits@J@std@@SAJXZ` | `0x3F5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1836 | `?infinity@?$numeric_limits@K@std@@SAKXZ` | `0x3F5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1837 | `?infinity@?$numeric_limits@M@std@@SAMXZ` | `0x3F5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1838 | `?infinity@?$numeric_limits@N@std@@SANXZ` | `0x3F5D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1839 | `?infinity@?$numeric_limits@O@std@@SAOXZ` | `0x3F5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1840 | `?infinity@?$numeric_limits@_N@std@@SA_NXZ` | `0x3F5F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1880 | `?ldexp@?$_Ctr@M@std@@SAMMH@Z` | `0x3F600` | 23 | UnwindData |  |
| 1881 | `?ldexp@?$_Ctr@N@std@@SANNH@Z` | `0x3F620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1882 | `?ldexp@?$_Ctr@O@std@@SAOOH@Z` | `0x3F630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1892 | `?log@?$_Ctr@M@std@@SAMM@Z` | `0x3F640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1893 | `?log@?$_Ctr@N@std@@SANN@Z` | `0x3F650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1894 | `?log@?$_Ctr@O@std@@SAOO@Z` | `0x3F660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1900 | `?max@?$numeric_limits@C@std@@SACXZ` | `0x3F670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1901 | `?max@?$numeric_limits@D@std@@SADXZ` | `0x3F680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1902 | `?max@?$numeric_limits@E@std@@SAEXZ` | `0x3F690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1903 | `?max@?$numeric_limits@F@std@@SAFXZ` | `0x3F6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1904 | `?max@?$numeric_limits@G@std@@SAGXZ` | `0x3F6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1905 | `?max@?$numeric_limits@H@std@@SAHXZ` | `0x3F6C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1906 | `?max@?$numeric_limits@I@std@@SAIXZ` | `0x3F6D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1907 | `?max@?$numeric_limits@J@std@@SAJXZ` | `0x3F6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1908 | `?max@?$numeric_limits@K@std@@SAKXZ` | `0x3F6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1909 | `?max@?$numeric_limits@M@std@@SAMXZ` | `0x3F700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1910 | `?max@?$numeric_limits@N@std@@SANXZ` | `0x3F710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1911 | `?max@?$numeric_limits@O@std@@SAOXZ` | `0x3F720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1912 | `?max@?$numeric_limits@_N@std@@SA_NXZ` | `0x3F730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1916 | `?min@?$numeric_limits@C@std@@SACXZ` | `0x3F740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1917 | `?min@?$numeric_limits@D@std@@SADXZ` | `0x3F750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1918 | `?min@?$numeric_limits@E@std@@SAEXZ` | `0x3F760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1919 | `?min@?$numeric_limits@F@std@@SAFXZ` | `0x3F770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1920 | `?min@?$numeric_limits@G@std@@SAGXZ` | `0x3F780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1921 | `?min@?$numeric_limits@H@std@@SAHXZ` | `0x3F790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1922 | `?min@?$numeric_limits@I@std@@SAIXZ` | `0x3F7A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1923 | `?min@?$numeric_limits@J@std@@SAJXZ` | `0x3F7B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1924 | `?min@?$numeric_limits@K@std@@SAKXZ` | `0x3F7C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1925 | `?min@?$numeric_limits@M@std@@SAMXZ` | `0x3F7D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1926 | `?min@?$numeric_limits@N@std@@SANXZ` | `0x3F7E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1927 | `?min@?$numeric_limits@O@std@@SAOXZ` | `0x3F7F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1928 | `?min@?$numeric_limits@_N@std@@SA_NXZ` | `0x3F800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1978 | `?overflow@?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@MEAAHH@Z` | `0x3F810` | 461 | UnwindData |  |
| 1979 | `?overflow@?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@MEAAGG@Z` | `0x3F9F0` | 538 | UnwindData |  |
| 1985 | `?pbackfail@?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@MEAAHH@Z` | `0x3FC10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1986 | `?pbackfail@?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@MEAAGG@Z` | `0x3FC70` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2004 | `?pow@?$_Ctr@M@std@@SAMMM@Z` | `0x3FCE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2005 | `?pow@?$_Ctr@N@std@@SANNN@Z` | `0x3FCF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2006 | `?pow@?$_Ctr@O@std@@SAOOO@Z` | `0x3FD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2066 | `?quiet_NaN@?$numeric_limits@C@std@@SACXZ` | `0x3FD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2067 | `?quiet_NaN@?$numeric_limits@D@std@@SADXZ` | `0x3FD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2068 | `?quiet_NaN@?$numeric_limits@E@std@@SAEXZ` | `0x3FD30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2069 | `?quiet_NaN@?$numeric_limits@F@std@@SAFXZ` | `0x3FD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2070 | `?quiet_NaN@?$numeric_limits@G@std@@SAGXZ` | `0x3FD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2071 | `?quiet_NaN@?$numeric_limits@H@std@@SAHXZ` | `0x3FD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2072 | `?quiet_NaN@?$numeric_limits@I@std@@SAIXZ` | `0x3FD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2073 | `?quiet_NaN@?$numeric_limits@J@std@@SAJXZ` | `0x3FD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2074 | `?quiet_NaN@?$numeric_limits@K@std@@SAKXZ` | `0x3FD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2075 | `?quiet_NaN@?$numeric_limits@M@std@@SAMXZ` | `0x3FDA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2076 | `?quiet_NaN@?$numeric_limits@N@std@@SANXZ` | `0x3FDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2077 | `?quiet_NaN@?$numeric_limits@O@std@@SAOXZ` | `0x3FDC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2078 | `?quiet_NaN@?$numeric_limits@_N@std@@SA_NXZ` | `0x3FDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2091 | `?rdbuf@?$basic_istringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAPEAV?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x3FDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2092 | `?rdbuf@?$basic_istringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAPEAV?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x3FDF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2095 | `?rdbuf@?$basic_ostringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAPEAV?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x3FE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2096 | `?rdbuf@?$basic_ostringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAPEAV?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x3FE10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2097 | `?rdbuf@?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBAPEAV?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x3FE20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2098 | `?rdbuf@?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBAPEAV?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x3FE30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2104 | `?real@?$_Complex_base@M@std@@QEAAMAEBM@Z` | `0x3FE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2105 | `?real@?$_Complex_base@M@std@@QEBAMXZ` | `0x3FE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2106 | `?real@?$_Complex_base@N@std@@QEAANAEBN@Z` | `0x3FE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2107 | `?real@?$_Complex_base@N@std@@QEBANXZ` | `0x3FE70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2108 | `?real@?$_Complex_base@O@std@@QEAAOAEBO@Z` | `0x3FE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2109 | `?real@?$_Complex_base@O@std@@QEBAOXZ` | `0x3FE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2153 | `?round_error@?$numeric_limits@C@std@@SACXZ` | `0x3FEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2154 | `?round_error@?$numeric_limits@D@std@@SADXZ` | `0x3FEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2155 | `?round_error@?$numeric_limits@E@std@@SAEXZ` | `0x3FEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2156 | `?round_error@?$numeric_limits@F@std@@SAFXZ` | `0x3FED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2157 | `?round_error@?$numeric_limits@G@std@@SAGXZ` | `0x3FEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2158 | `?round_error@?$numeric_limits@H@std@@SAHXZ` | `0x3FEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2159 | `?round_error@?$numeric_limits@I@std@@SAIXZ` | `0x3FF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2160 | `?round_error@?$numeric_limits@J@std@@SAJXZ` | `0x3FF10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2161 | `?round_error@?$numeric_limits@K@std@@SAKXZ` | `0x3FF20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2162 | `?round_error@?$numeric_limits@M@std@@SAMXZ` | `0x3FF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2163 | `?round_error@?$numeric_limits@N@std@@SANXZ` | `0x3FF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2164 | `?round_error@?$numeric_limits@O@std@@SAOXZ` | `0x3FF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2165 | `?round_error@?$numeric_limits@_N@std@@SA_NXZ` | `0x3FF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2180 | `?seekoff@?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@MEAA?AV?$fpos@H@2@_JW4seekdir@ios_base@2@H@Z` | `0x3FF70` | 390 | UnwindData |  |
| 2181 | `?seekoff@?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@MEAA?AV?$fpos@H@2@_JW4seekdir@ios_base@2@H@Z` | `0x40100` | 435 | UnwindData |  |
| 2191 | `?seekpos@?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@MEAA?AV?$fpos@H@2@V32@H@Z` | `0x402C0` | 291 | UnwindData |  |
| 2192 | `?seekpos@?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@MEAA?AV?$fpos@H@2@V32@H@Z` | `0x403F0` | 323 | UnwindData |  |
| 2222 | `?signaling_NaN@?$numeric_limits@C@std@@SACXZ` | `0x40540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2223 | `?signaling_NaN@?$numeric_limits@D@std@@SADXZ` | `0x40550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2224 | `?signaling_NaN@?$numeric_limits@E@std@@SAEXZ` | `0x40560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2225 | `?signaling_NaN@?$numeric_limits@F@std@@SAFXZ` | `0x40570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2226 | `?signaling_NaN@?$numeric_limits@G@std@@SAGXZ` | `0x40580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2227 | `?signaling_NaN@?$numeric_limits@H@std@@SAHXZ` | `0x40590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2228 | `?signaling_NaN@?$numeric_limits@I@std@@SAIXZ` | `0x405A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2229 | `?signaling_NaN@?$numeric_limits@J@std@@SAJXZ` | `0x405B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2230 | `?signaling_NaN@?$numeric_limits@K@std@@SAKXZ` | `0x405C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2231 | `?signaling_NaN@?$numeric_limits@M@std@@SAMXZ` | `0x405D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2232 | `?signaling_NaN@?$numeric_limits@N@std@@SANXZ` | `0x405E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2233 | `?signaling_NaN@?$numeric_limits@O@std@@SAOXZ` | `0x405F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2234 | `?signaling_NaN@?$numeric_limits@_N@std@@SA_NXZ` | `0x40600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2235 | `?sin@?$_Ctr@M@std@@SAMM@Z` | `0x40610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2236 | `?sin@?$_Ctr@N@std@@SANN@Z` | `0x40620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2237 | `?sin@?$_Ctr@O@std@@SAOO@Z` | `0x40630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2254 | `?sqrt@?$_Ctr@M@std@@SAMM@Z` | `0x40640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2255 | `?sqrt@?$_Ctr@N@std@@SANN@Z` | `0x40650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2256 | `?sqrt@?$_Ctr@O@std@@SAOO@Z` | `0x40660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2262 | `?str@?$basic_istringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@@Z` | `0x40670` | 87 | UnwindData |  |
| 2263 | `?str@?$basic_istringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x406D0` | 27 | UnwindData |  |
| 2264 | `?str@?$basic_istringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@@Z` | `0x40700` | 87 | UnwindData |  |
| 2265 | `?str@?$basic_istringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x40760` | 27 | UnwindData |  |
| 2266 | `?str@?$basic_ostringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@@Z` | `0x40790` | 87 | UnwindData |  |
| 2267 | `?str@?$basic_ostringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x407F0` | 27 | UnwindData |  |
| 2268 | `?str@?$basic_ostringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@@Z` | `0x40820` | 87 | UnwindData |  |
| 2269 | `?str@?$basic_ostringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x40880` | 27 | UnwindData |  |
| 2270 | `?str@?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@@Z` | `0x408B0` | 86 | UnwindData |  |
| 2271 | `?str@?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x40910` | 216 | UnwindData |  |
| 2272 | `?str@?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@@Z` | `0x409F0` | 86 | UnwindData |  |
| 2273 | `?str@?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x40A50` | 145 | UnwindData |  |
| 2274 | `?str@?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@@Z` | `0x40AF0` | 87 | UnwindData |  |
| 2275 | `?str@?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@QEBA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@2@XZ` | `0x40B50` | 27 | UnwindData |  |
| 2276 | `?str@?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@@Z` | `0x40B80` | 87 | UnwindData |  |
| 2277 | `?str@?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@2@XZ` | `0x40BE0` | 27 | UnwindData |  |
| 2330 | `?underflow@?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@MEAAHXZ` | `0x40C10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2331 | `?underflow@?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@MEAAGXZ` | `0x40C90` | 33,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `??_7bad_exception@std@@6B@` | `0x490F8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `??_7bad_alloc@std@@6B@` | `0x49118` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `??_7logic_error@std@@6B@` | `0x49138` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `??_7domain_error@std@@6B@` | `0x49158` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `??_7length_error@std@@6B@` | `0x49178` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `??_7out_of_range@std@@6B@` | `0x49198` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `??_7runtime_error@std@@6B@` | `0x491B8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `??_7overflow_error@std@@6B@` | `0x491D8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `??_7underflow_error@std@@6B@` | `0x491F8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `??_7range_error@std@@6B@` | `0x49218` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `??_7bad_cast@std@@6B@` | `0x49238` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `??_7bad_typeid@std@@6B@` | `0x49258` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `??_7__non_rtti_object@std@@6B@` | `0x49278` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1008 | `??_7facet@locale@std@@6B@` | `0x49298` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `??_7codecvt_base@std@@6B@` | `0x492A8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `??_7?$codecvt@GDH@std@@6B@` | `0x492D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `??_7ctype_base@std@@6B@` | `0x49310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `??_7?$ctype@D@std@@6B@` | `0x49320` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 979 | `??_7?$ctype@G@std@@6B@` | `0x49350` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 974 | `??_7?$codecvt@DDH@std@@6B@` | `0x493C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `??_7ios_base@std@@6B@` | `0x49400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 994 | `??_7?$numpunct@D@std@@6B@` | `0x49410` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 995 | `??_7?$numpunct@G@std@@6B@` | `0x49448` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `??_7?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x49480` | 104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `??_7?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x494E8` | 104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `??_7?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x49550` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `??_7?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x495A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 968 | `??_7?$basic_streambuf@DU?$char_traits@D@std@@@std@@6B@` | `0x495F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 969 | `??_7?$basic_streambuf@GU?$char_traits@G@std@@@std@@6B@` | `0x49660` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 954 | `??_7?$basic_ios@DU?$char_traits@D@std@@@std@@6B@` | `0x496D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `??_7?$basic_ios@GU?$char_traits@G@std@@@std@@6B@` | `0x496E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 964 | `??_7?$basic_ostream@DU?$char_traits@D@std@@@std@@6B@` | `0x496F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 965 | `??_7?$basic_ostream@GU?$char_traits@G@std@@@std@@6B@` | `0x49700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 958 | `??_7?$basic_istream@DU?$char_traits@D@std@@@std@@6B@` | `0x49710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 959 | `??_7?$basic_istream@GU?$char_traits@G@std@@@std@@6B@` | `0x49720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 956 | `??_7?$basic_iostream@DU?$char_traits@D@std@@@std@@6B@` | `0x49730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `??_7?$basic_iostream@GU?$char_traits@G@std@@@std@@6B@` | `0x49740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | `??_7money_base@std@@6B@` | `0x49750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 946 | `??_7?$_Mpunct@D@std@@6B@` | `0x49760` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 947 | `??_7?$_Mpunct@G@std@@6B@` | `0x497B8` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `??_7?$moneypunct@D$00@std@@6B@` | `0x49810` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 987 | `??_7?$moneypunct@D$0A@@std@@6B@` | `0x49868` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `??_7?$moneypunct@G$00@std@@6B@` | `0x498C0` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `??_7?$moneypunct@G$0A@@std@@6B@` | `0x49918` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 982 | `??_7?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x49970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 983 | `??_7?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x49990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 984 | `??_7?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x499B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `??_7?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x499D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `??_7time_base@std@@6B@` | `0x499F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `??_7?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x49A00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 997 | `??_7?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x49A40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `??_7?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x49A80` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `??_7?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x49A98` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `??_7?$collate@D@std@@6B@` | `0x49AB0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `??_7?$collate@G@std@@6B@` | `0x49AD8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `??_7messages_base@std@@6B@` | `0x49B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `??_7?$messages@D@std@@6B@` | `0x49B10` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `??_7?$messages@G@std@@6B@` | `0x49B38` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 948 | `??_7?$basic_filebuf@DU?$char_traits@D@std@@@std@@6B@` | `0x49B60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 949 | `??_7?$basic_filebuf@GU?$char_traits@G@std@@@std@@6B@` | `0x49BD0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 952 | `??_7?$basic_ifstream@DU?$char_traits@D@std@@@std@@6B@` | `0x49C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 953 | `??_7?$basic_ifstream@GU?$char_traits@G@std@@@std@@6B@` | `0x49C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 962 | `??_7?$basic_ofstream@DU?$char_traits@D@std@@@std@@6B@` | `0x49C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 963 | `??_7?$basic_ofstream@GU?$char_traits@G@std@@@std@@6B@` | `0x49C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 950 | `??_7?$basic_fstream@DU?$char_traits@D@std@@@std@@6B@` | `0x49C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 951 | `??_7?$basic_fstream@GU?$char_traits@G@std@@@std@@6B@` | `0x49C90` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 970 | `??_7?$basic_stringbuf@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@6B@` | `0x49D70` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 971 | `??_7?$basic_stringbuf@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@6B@` | `0x49DE0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 960 | `??_7?$basic_istringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@6B@` | `0x49E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 961 | `??_7?$basic_istringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@6B@` | `0x49E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 966 | `??_7?$basic_ostringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@6B@` | `0x49E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 967 | `??_7?$basic_ostringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@6B@` | `0x49E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `??_7?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@6B@` | `0x49E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `??_7?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@6B@` | `0x49EA0` | 12,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2367 | `_FDenorm` | `0x4D0C8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2373 | `_FInf` | `0x4D0D8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2374 | `_FNan` | `0x4D0E8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2377 | `_FSnan` | `0x4D0F8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2371 | `_FEps` | `0x4D108` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2375 | `_FRteps` | `0x4D118` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2378 | `_FXbig` | `0x4D128` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2385 | `_LDenorm` | `0x4D1B8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2390 | `_LInf` | `0x4D1C8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2391 | `_LNan` | `0x4D1D8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2395 | `_LSnan` | `0x4D1E8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2388 | `_LEps` | `0x4D1F8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2393 | `_LRteps` | `0x4D208` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2396 | `_LXbig` | `0x4D218` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2360 | `_Denorm` | `0x4D260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2382 | `_Hugeval` | `0x4D270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2383 | `_Inf` | `0x4D280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2398 | `_Nan` | `0x4D290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2402 | `_Snan` | `0x4D2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2364 | `_Eps` | `0x4D2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2400 | `_Rteps` | `0x4D2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2411 | `_Xbig` | `0x4D2D0` | 23 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1859 | `?intl@?$moneypunct@D$00@std@@2_NB` | `0x4D2E7` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1860 | `?intl@?$moneypunct@D$0A@@std@@2_NB` | `0x4D2E8` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1861 | `?intl@?$moneypunct@G$00@std@@2_NB` | `0x4D2E9` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1862 | `?intl@?$moneypunct@G$0A@@std@@2_NB` | `0x4D2EA` | 6 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1948 | `?npos@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@2_KB` | `0x4D2F0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1949 | `?npos@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@2_KB` | `0x4D2F8` | 15,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `??_8?$basic_ostream@DU?$char_traits@D@std@@@std@@7B@` | `0x50FC8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `??_8?$basic_ostream@GU?$char_traits@G@std@@@std@@7B@` | `0x50FD0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1030 | `??_8?$basic_istream@DU?$char_traits@D@std@@@std@@7B@` | `0x50FD8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1031 | `??_8?$basic_istream@GU?$char_traits@G@std@@@std@@7B@` | `0x50FE0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `??_8?$basic_iostream@DU?$char_traits@D@std@@@std@@7B?$basic_istream@DU?$char_traits@D@std@@@1@@` | `0x50FE8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `??_8?$basic_iostream@DU?$char_traits@D@std@@@std@@7B?$basic_ostream@DU?$char_traits@D@std@@@1@@` | `0x50FF0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1028 | `??_8?$basic_iostream@GU?$char_traits@G@std@@@std@@7B?$basic_istream@GU?$char_traits@G@std@@@1@@` | `0x50FF8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1029 | `??_8?$basic_iostream@GU?$char_traits@G@std@@@std@@7B?$basic_ostream@GU?$char_traits@G@std@@@1@@` | `0x51000` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `??_8?$basic_ifstream@DU?$char_traits@D@std@@@std@@7B@` | `0x51008` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `??_8?$basic_ifstream@GU?$char_traits@G@std@@@std@@7B@` | `0x51010` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1034 | `??_8?$basic_ofstream@DU?$char_traits@D@std@@@std@@7B@` | `0x51018` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `??_8?$basic_ofstream@GU?$char_traits@G@std@@@std@@7B@` | `0x51020` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `??_8?$basic_fstream@DU?$char_traits@D@std@@@std@@7B?$basic_istream@DU?$char_traits@D@std@@@1@@` | `0x51028` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `??_8?$basic_fstream@DU?$char_traits@D@std@@@std@@7B?$basic_ostream@DU?$char_traits@D@std@@@1@@` | `0x51030` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `??_8?$basic_fstream@GU?$char_traits@G@std@@@std@@7B?$basic_istream@GU?$char_traits@G@std@@@1@@` | `0x51038` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `??_8?$basic_fstream@GU?$char_traits@G@std@@@std@@7B?$basic_ostream@GU?$char_traits@G@std@@@1@@` | `0x51040` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1118 | `?_C@?1??_Nullstr@?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@CAPEBGXZ@4GB` | `0x51150` | 2 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1117 | `?_C@?1??_Nullstr@?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@CAPEBDXZ@4DB` | `0x51152` | 46 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1156 | `?_Fpz@std@@3_JB` | `0x51180` | 920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2292 | `?table_size@?$ctype@D@std@@2_KB` | `0x51518` | 4,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `??_8?$basic_istringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@7B@` | `0x52708` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1033 | `??_8?$basic_istringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@7B@` | `0x52710` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `??_8?$basic_ostringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@7B@` | `0x52718` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `??_8?$basic_ostringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@7B@` | `0x52720` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1040 | `??_8?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@7B?$basic_istream@DU?$char_traits@D@std@@@1@@` | `0x52728` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | `??_8?$basic_stringstream@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@7B?$basic_ostream@DU?$char_traits@D@std@@@1@@` | `0x52730` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1042 | `??_8?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@7B?$basic_istream@GU?$char_traits@G@std@@@1@@` | `0x52738` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1043 | `??_8?$basic_stringstream@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@7B?$basic_ostream@GU?$char_traits@G@std@@@1@@` | `0x52740` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1301 | `?_R2@?BN@???$_Fabs@M@std@@YAMAEBV?$complex@M@1@PEAH@Z@4MB` | `0x52748` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `?_Xh@?BN@???$_Fabs@M@std@@YAMAEBV?$complex@M@1@PEAH@Z@4MB` | `0x5274C` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1329 | `?_Xl@?BN@???$_Fabs@M@std@@YAMAEBV?$complex@M@1@PEAH@Z@4MB` | `0x52750` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1120 | `?_Cl@?5???$log@M@std@@YA?AV?$complex@M@1@AEBV21@@Z@4MB` | `0x52754` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `?_R2@?BN@???$_Fabs@N@std@@YANAEBV?$complex@N@1@PEAH@Z@4NB` | `0x52758` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1327 | `?_Xh@?BN@???$_Fabs@N@std@@YANAEBV?$complex@N@1@PEAH@Z@4NB` | `0x52760` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `?_Xl@?BN@???$_Fabs@N@std@@YANAEBV?$complex@N@1@PEAH@Z@4NB` | `0x52768` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1121 | `?_Cl@?5???$log@N@std@@YA?AV?$complex@N@1@AEBV21@@Z@4NB` | `0x52770` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `?_R2@?BN@???$_Fabs@O@std@@YAOAEBV?$complex@O@1@PEAH@Z@4OB` | `0x52778` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `?_Xh@?BN@???$_Fabs@O@std@@YAOAEBV?$complex@O@1@PEAH@Z@4OB` | `0x52780` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `?_Xl@?BN@???$_Fabs@O@std@@YAOAEBV?$complex@O@1@PEAH@Z@4OB` | `0x52788` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `?_Cl@?5???$log@O@std@@YA?AV?$complex@O@1@AEBV21@@Z@4OB` | `0x52790` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1947 | `?nothrow@std@@3Unothrow_t@1@B` | `0x52860` | 256,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `?cin@std@@3V?$basic_istream@DU?$char_traits@D@std@@@1@A` | `0x911D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1442 | `?cout@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A` | `0x91240` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1386 | `?cerr@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A` | `0x91340` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1396 | `?clog@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A` | `0x913A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2337 | `?wcin@std@@3V?$basic_istream@GU?$char_traits@G@std@@@1@A` | `0x91400` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2339 | `?wcout@std@@3V?$basic_ostream@GU?$char_traits@G@std@@@1@A` | `0x91470` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2336 | `?wcerr@std@@3V?$basic_ostream@GU?$char_traits@G@std@@@1@A` | `0x914D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2338 | `?wclog@std@@3V?$basic_ostream@GU?$char_traits@G@std@@@1@A` | `0x91530` | 5,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `?_Sync@ios_base@std@@0_NA` | `0x92BC0` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1262 | `?_Init_cnt@Init@ios_base@std@@0HA` | `0x92BC4` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1263 | `?_Init_cnt@_Winit@std@@0HA` | `0x92BC8` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1787 | `?id@?$ctype@G@std@@2V0locale@2@A` | `0x92C60` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1782 | `?id@?$codecvt@DDH@std@@2V0locale@2@A` | `0x92C68` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1802 | `?id@?$numpunct@D@std@@2V0locale@2@A` | `0x92C70` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1803 | `?id@?$numpunct@G@std@@2V0locale@2@A` | `0x92C78` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1798 | `?id@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0x92C80` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1799 | `?id@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0x92C88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1800 | `?id@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0x92C90` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1801 | `?id@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0x92C98` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1794 | `?id@?$moneypunct@D$00@std@@2V0locale@2@A` | `0x92CA0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1795 | `?id@?$moneypunct@D$0A@@std@@2V0locale@2@A` | `0x92CA8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1796 | `?id@?$moneypunct@G$00@std@@2V0locale@2@A` | `0x92CB0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1797 | `?id@?$moneypunct@G$0A@@std@@2V0locale@2@A` | `0x92CB8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1790 | `?id@?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0x92CC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1791 | `?id@?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0x92CC8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1792 | `?id@?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0x92CD0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1793 | `?id@?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0x92CD8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1804 | `?id@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0x92CE0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1805 | `?id@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0x92CE8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1806 | `?id@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0x92CF0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1807 | `?id@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0x92CF8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1784 | `?id@?$collate@D@std@@2V0locale@2@A` | `0x92D00` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1785 | `?id@?$collate@G@std@@2V0locale@2@A` | `0x92D08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1788 | `?id@?$messages@D@std@@2V0locale@2@A` | `0x92D10` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1789 | `?id@?$messages@G@std@@2V0locale@2@A` | `0x92D18` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1316 | `?_Stinit@?1??_Init@?$basic_filebuf@GU?$char_traits@G@std@@@std@@IEAAXPEAU_iobuf@@W4_Initfl@23@@Z@4HA` | `0x92D20` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1315 | `?_Stinit@?1??_Init@?$basic_filebuf@DU?$char_traits@D@std@@@std@@IEAAXPEAU_iobuf@@W4_Initfl@23@@Z@4HA` | `0x92D28` | 248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `?_Index@ios_base@std@@0HA` | `0x92E20` | 104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1786 | `?id@?$ctype@D@std@@2V0locale@2@A` | `0x92E88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `?_Id_cnt@id@locale@std@@0HA` | `0x92E90` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1123 | `?_Clocptr@_Locimp@locale@std@@0PEAV123@EA` | `0x92E98` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `?_Global@_Locimp@locale@std@@0PEAV123@EA` | `0x92EA0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `?_Cltab@?$ctype@D@std@@0PEBFEB` | `0x92EA8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1783 | `?id@?$codecvt@GDH@std@@2V0locale@2@A` | `0x92EC0` | 0 | Indeterminate |  |
