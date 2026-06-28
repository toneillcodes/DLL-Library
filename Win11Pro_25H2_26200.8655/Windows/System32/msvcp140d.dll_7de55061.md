# Binary Specification: msvcp140d.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msvcp140d.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7de55061770829e3958576f4c737b9805f7153a0e5933bb2ecd9ab9adc61b3e3`
* **Total Exported Functions:** 1523

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 668 | `?__ExceptionPtrAssign@@YAXPEAXPEBX@Z` | `0x3470` | 35 | UnwindData |  |
| 669 | `?__ExceptionPtrCompare@@YA_NPEBX0@Z` | `0x34A0` | 34 | UnwindData |  |
| 670 | `?__ExceptionPtrCopy@@YAXPEAXPEBX@Z` | `0x34D0` | 55 | UnwindData |  |
| 671 | `?__ExceptionPtrCopyException@@YAXPEAXPEBX1@Z` | `0x3510` | 109 | UnwindData |  |
| 672 | `?__ExceptionPtrCreate@@YAXPEAX@Z` | `0x3580` | 61 | UnwindData |  |
| 673 | `?__ExceptionPtrCurrentException@@YAXPEAX@Z` | `0x35C0` | 204 | UnwindData |  |
| 674 | `?__ExceptionPtrDestroy@@YAXPEAX@Z` | `0x3690` | 27 | UnwindData |  |
| 675 | `?__ExceptionPtrRethrow@@YAXPEBX@Z` | `0x36B0` | 471 | UnwindData |  |
| 676 | `?__ExceptionPtrSwap@@YAXPEAX0@Z` | `0x3890` | 35 | UnwindData |  |
| 677 | `?__ExceptionPtrToBool@@YA_NPEBX@Z` | `0x38C0` | 24 | UnwindData |  |
| 1497 | `__crtCompareStringA` | `0x3A40` | 1,732 | UnwindData |  |
| 1499 | `__crtCompareStringW` | `0x41B0` | 300 | UnwindData |  |
| 1515 | `__crtLCMapStringA` | `0x4310` | 1,408 | UnwindData |  |
| 1517 | `__crtLCMapStringW` | `0x4890` | 188 | UnwindData |  |
| 1498 | `__crtCompareStringEx` | `0x4950` | 104 | UnwindData |  |
| 1509 | `__crtGetLocaleInfoEx` | `0x49C0` | 53 | UnwindData |  |
| 1516 | `__crtLCMapStringEx` | `0x4A00` | 104 | UnwindData |  |
| 1393 | `_Getctype` | `0x4A70` | 242 | UnwindData |  |
| 1476 | `_Tolower` | `0x4B70` | 677 | UnwindData |  |
| 1477 | `_Toupper` | `0x4E20` | 677 | UnwindData |  |
| 1411 | `_Lock_shared_ptr_spin_lock` | `0x50D0` | 23 | UnwindData |  |
| 1481 | `_Unlock_shared_ptr_spin_lock` | `0x50F0` | 23 | UnwindData |  |
| 5 | `??0?$_Yarn@D@std@@QEAA@PEBD@Z` | `0x7050` | 61 | UnwindData |  |
| 6 | `??0?$_Yarn@D@std@@QEAA@XZ` | `0x7090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0?$_Yarn@_W@std@@QEAA@XZ` | `0x70B0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0?$basic_ios@DU?$char_traits@D@std@@@std@@IEAA@XZ` | `0x7140` | 79 | UnwindData |  |
| 38 | `??0?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@_N@Z` | `0x7190` | 208 | UnwindData |  |
| 48 | `??0?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAA@XZ` | `0x7260` | 262 | UnwindData |  |
| 55 | `??0?$codecvt@DDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7590` | 76 | UnwindData |  |
| 57 | `??0?$codecvt@GDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x75E0` | 76 | UnwindData |  |
| 58 | `??0?$codecvt@GDU_Mbstatet@@@std@@QEAA@_K@Z` | `0x7630` | 121 | UnwindData |  |
| 59 | `??0?$codecvt@_SDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@KW4_Codecvt_mode@1@_K@Z` | `0x76B0` | 105 | UnwindData |  |
| 60 | `??0?$codecvt@_SDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7720` | 100 | UnwindData |  |
| 61 | `??0?$codecvt@_SDU_Mbstatet@@@std@@QEAA@_K@Z` | `0x7790` | 151 | UnwindData |  |
| 62 | `??0?$codecvt@_UDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@KW4_Codecvt_mode@1@_K@Z` | `0x7830` | 105 | UnwindData |  |
| 63 | `??0?$codecvt@_UDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x78A0` | 100 | UnwindData |  |
| 64 | `??0?$codecvt@_UDU_Mbstatet@@@std@@QEAA@_K@Z` | `0x7910` | 151 | UnwindData |  |
| 65 | `??0?$codecvt@_WDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x79B0` | 76 | UnwindData |  |
| 66 | `??0?$codecvt@_WDU_Mbstatet@@@std@@QEAA@_K@Z` | `0x7A00` | 121 | UnwindData |  |
| 67 | `??0?$ctype@D@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7A80` | 76 | UnwindData |  |
| 68 | `??0?$ctype@D@std@@QEAA@PEBF_N_K@Z` | `0x7AD0` | 255 | UnwindData |  |
| 69 | `??0?$ctype@G@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7BD0` | 76 | UnwindData |  |
| 70 | `??0?$ctype@G@std@@QEAA@_K@Z` | `0x7C20` | 121 | UnwindData |  |
| 71 | `??0?$ctype@_W@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7CA0` | 76 | UnwindData |  |
| 72 | `??0?$ctype@_W@std@@QEAA@_K@Z` | `0x7CF0` | 121 | UnwindData |  |
| 102 | `??0Init@ios_base@std@@QEAA@XZ` | `0x7E00` | 30 | UnwindData |  |
| 103 | `??0_Facet_base@std@@QEAA@AEBV01@@Z` | `0x7EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `??0_Facet_base@std@@QEAA@XZ` | `0x7ED0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `??0_Locimp@locale@std@@AEAA@AEBV012@@Z` | `0x8000` | 180 | UnwindData |  |
| 107 | `??0_Locimp@locale@std@@AEAA@_N@Z` | `0x80C0` | 136 | UnwindData |  |
| 108 | `??0_Locinfo@std@@QEAA@HPEBD@Z` | `0x8150` | 202 | UnwindData |  |
| 109 | `??0_Locinfo@std@@QEAA@PEBD@Z` | `0x8220` | 194 | UnwindData |  |
| 112 | `??0_Timevec@std@@QEAA@AEBV01@@Z` | `0x8470` | 52 | UnwindData |  |
| 113 | `??0_Timevec@std@@QEAA@PEAX@Z` | `0x84B0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `??0codecvt_base@std@@QEAA@_K@Z` | `0x8610` | 54 | UnwindData |  |
| 117 | `??0ctype_base@std@@QEAA@_K@Z` | `0x8650` | 54 | UnwindData |  |
| 118 | `??0facet@locale@std@@IEAA@_K@Z` | `0x8760` | 61 | UnwindData |  |
| 119 | `??0id@locale@std@@QEAA@_K@Z` | `0x8840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `??0ios_base@std@@IEAA@XZ` | `0x8860` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `??0time_base@std@@QEAA@_K@Z` | `0x8AE0` | 54 | UnwindData |  |
| 123 | `??1?$_Yarn@D@std@@QEAA@XZ` | `0x8B90` | 25 | UnwindData |  |
| 125 | `??1?$_Yarn@_W@std@@QEAA@XZ` | `0x8BB0` | 25 | UnwindData |  |
| 126 | `??1?$basic_ios@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x8C30` | 40 | UnwindData |  |
| 135 | `??1?$basic_ostream@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x8C60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `??1?$basic_streambuf@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x8CB0` | 82 | UnwindData |  |
| 141 | `??1?$codecvt@DDU_Mbstatet@@@std@@MEAA@XZ` | `0x8D80` | 40 | UnwindData |  |
| 142 | `??1?$codecvt@GDU_Mbstatet@@@std@@MEAA@XZ` | `0x8DB0` | 40 | UnwindData |  |
| 143 | `??1?$codecvt@_SDU_Mbstatet@@@std@@MEAA@XZ` | `0x8DE0` | 40 | UnwindData |  |
| 144 | `??1?$codecvt@_UDU_Mbstatet@@@std@@MEAA@XZ` | `0x8E10` | 40 | UnwindData |  |
| 145 | `??1?$codecvt@_WDU_Mbstatet@@@std@@MEAA@XZ` | `0x8E40` | 40 | UnwindData |  |
| 146 | `??1?$ctype@D@std@@MEAA@XZ` | `0x8E70` | 51 | UnwindData |  |
| 147 | `??1?$ctype@G@std@@MEAA@XZ` | `0x8EB0` | 83 | UnwindData |  |
| 148 | `??1?$ctype@_W@std@@MEAA@XZ` | `0x8F10` | 83 | UnwindData |  |
| 161 | `??1Init@ios_base@std@@QEAA@XZ` | `0x8FC0` | 25 | UnwindData |  |
| 162 | `??1_Facet_base@std@@UEAA@XZ` | `0x8FF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `??1_Locimp@locale@std@@MEAA@XZ` | `0x9030` | 68 | UnwindData |  |
| 165 | `??1_Locinfo@std@@QEAA@XZ` | `0x9080` | 141 | UnwindData |  |
| 167 | `??1_Timevec@std@@QEAA@XZ` | `0x9130` | 29 | UnwindData |  |
| 170 | `??1codecvt_base@std@@UEAA@XZ` | `0x9190` | 40 | UnwindData |  |
| 171 | `??1ctype_base@std@@UEAA@XZ` | `0x91C0` | 40 | UnwindData |  |
| 172 | `??1facet@locale@std@@MEAA@XZ` | `0x9200` | 40 | UnwindData |  |
| 173 | `??1ios_base@std@@UEAA@XZ` | `0x9250` | 40 | UnwindData |  |
| 174 | `??1time_base@std@@UEAA@XZ` | `0x9350` | 40 | UnwindData |  |
| 175 | `??2_Crt_new_delete@std@@SAPEAX_K@Z` | `0x9380` | 55 | UnwindData |  |
| 176 | `??2_Crt_new_delete@std@@SAPEAX_KAEBUnothrow_t@1@@Z` | `0x93C0` | 77 | UnwindData |  |
| 177 | `??2_Crt_new_delete@std@@SAPEAX_KPEAX@Z` | `0x9410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `??3_Crt_new_delete@std@@SAXPEAX0@Z` | `0x9420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `??3_Crt_new_delete@std@@SAXPEAX@Z` | `0x9430` | 26 | UnwindData |  |
| 180 | `??3_Crt_new_delete@std@@SAXPEAXAEBUnothrow_t@1@@Z` | `0x9450` | 30 | UnwindData |  |
| 181 | `??4?$_Iosb@H@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x9470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `??4?$_Iosb@H@std@@QEAAAEAV01@AEBV01@@Z` | `0x9480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `??4?$_Yarn@D@std@@QEAAAEAV01@PEBD@Z` | `0x9490` | 76 | UnwindData |  |
| 188 | `??4?$_Yarn@_W@std@@QEAAAEAV01@PEB_W@Z` | `0x94E0` | 76 | UnwindData |  |
| 201 | `??4Init@ios_base@std@@QEAAAEAV012@AEBV012@@Z` | `0x9530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `??4_Crt_new_delete@std@@QEAAAEAU01@$$QEAU01@@Z` | `0x9540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `??4_Crt_new_delete@std@@QEAAAEAU01@AEBU01@@Z` | `0x9550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `??4_Facet_base@std@@QEAAAEAV01@AEBV01@@Z` | `0x9560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `??4_Init_locks@std@@QEAAAEAV01@AEBV01@@Z` | `0x9570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `??4_Timevec@std@@QEAAAEAV01@AEBV01@@Z` | `0x9580` | 78 | UnwindData |  |
| 208 | `??4_Winit@std@@QEAAAEAV01@AEBV01@@Z` | `0x95D0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `??7ios_base@std@@QEBA_NXZ` | `0x96D0` | 24 | UnwindData |  |
| 312 | `??Bid@locale@std@@QEAA_KXZ` | `0x97F0` | 24 | UnwindData |  |
| 313 | `??Bios_base@std@@QEBA_NXZ` | `0x9810` | 54 | UnwindData |  |
| 374 | `??_D?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x99D0` | 49 | UnwindData |  |
| 378 | `??_F?$codecvt@GDU_Mbstatet@@@std@@QEAAXXZ` | `0xA460` | 27 | UnwindData |  |
| 379 | `??_F?$codecvt@_SDU_Mbstatet@@@std@@QEAAXXZ` | `0xA480` | 27 | UnwindData |  |
| 380 | `??_F?$codecvt@_UDU_Mbstatet@@@std@@QEAAXXZ` | `0xA4A0` | 27 | UnwindData |  |
| 381 | `??_F?$codecvt@_WDU_Mbstatet@@@std@@QEAAXXZ` | `0xA4C0` | 27 | UnwindData |  |
| 382 | `??_F?$ctype@D@std@@QEAAXXZ` | `0xA4E0` | 33 | UnwindData |  |
| 383 | `??_F?$ctype@G@std@@QEAAXXZ` | `0xA510` | 27 | UnwindData |  |
| 384 | `??_F?$ctype@_W@std@@QEAAXXZ` | `0xA530` | 27 | UnwindData |  |
| 397 | `??_F_Locinfo@std@@QEAAXXZ` | `0xA550` | 32 | UnwindData |  |
| 398 | `??_F_Timevec@std@@QEAAXXZ` | `0xA570` | 27 | UnwindData |  |
| 399 | `??_Fcodecvt_base@std@@QEAAXXZ` | `0xA590` | 27 | UnwindData |  |
| 400 | `??_Fctype_base@std@@QEAAXXZ` | `0xA5B0` | 27 | UnwindData |  |
| 401 | `??_Ffacet@locale@std@@QEAAXXZ` | `0xA5D0` | 27 | UnwindData |  |
| 402 | `??_Fid@locale@std@@QEAAXXZ` | `0xA5F0` | 27 | UnwindData |  |
| 403 | `??_Ftime_base@std@@QEAAXXZ` | `0xA610` | 27 | UnwindData |  |
| 408 | `?_Addcats@_Locinfo@std@@QEAAAEAV12@HPEBD@Z` | `0xA8E0` | 65 | UnwindData |  |
| 409 | `?_Addfac@_Locimp@locale@std@@AEAAXPEAVfacet@23@_K@Z` | `0xA930` | 45 | UnwindData |  |
| 414 | `?_C_str@?$_Yarn@D@std@@QEBAPEBDXZ` | `0xAAB0` | 56 | UnwindData |  |
| 416 | `?_C_str@?$_Yarn@_W@std@@QEBAPEB_WXZ` | `0xAAF0` | 56 | UnwindData |  |
| 418 | `?_Callfns@ios_base@std@@AEAAXW4event@12@@Z` | `0xAC70` | 111 | UnwindData |  |
| 423 | `?_Decref@facet@locale@std@@UEAAPEAV_Facet_base@3@XZ` | `0xAE20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `?_Donarrow@?$ctype@G@std@@IEBADGD@Z` | `0xAE50` | 142 | UnwindData |  |
| 425 | `?_Donarrow@?$ctype@_W@std@@IEBAD_WD@Z` | `0xAEE0` | 142 | UnwindData |  |
| 426 | `?_Dowiden@?$ctype@G@std@@IEBAGD@Z` | `0xAF70` | 93 | UnwindData |  |
| 427 | `?_Dowiden@?$ctype@_W@std@@IEBA_WD@Z` | `0xAFD0` | 108 | UnwindData |  |
| 428 | `?_Empty@?$_Yarn@D@std@@QEBA_NXZ` | `0xB040` | 45 | UnwindData |  |
| 430 | `?_Empty@?$_Yarn@_W@std@@QEBA_NXZ` | `0xB070` | 45 | UnwindData |  |
| 435 | `?_Findarr@ios_base@std@@AEAAAEAU_Iosarray@12@H@Z` | `0xB340` | 255 | UnwindData |  |
| 442 | `?_Getcat@?$codecvt@DDU_Mbstatet@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xB4B0` | 243 | UnwindData |  |
| 443 | `?_Getcat@?$codecvt@GDU_Mbstatet@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xB5B0` | 243 | UnwindData |  |
| 444 | `?_Getcat@?$codecvt@_SDU_Mbstatet@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xB6B0` | 243 | UnwindData |  |
| 445 | `?_Getcat@?$codecvt@_UDU_Mbstatet@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xB7B0` | 243 | UnwindData |  |
| 446 | `?_Getcat@?$codecvt@_WDU_Mbstatet@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xB8B0` | 243 | UnwindData |  |
| 447 | `?_Getcat@?$ctype@D@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xB9B0` | 243 | UnwindData |  |
| 448 | `?_Getcat@?$ctype@G@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xBAB0` | 243 | UnwindData |  |
| 449 | `?_Getcat@?$ctype@_W@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xBBB0` | 243 | UnwindData |  |
| 462 | `?_Getcat@facet@locale@std@@SA_KPEAPEBV123@PEBV23@@Z` | `0xBCB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `?_Getcoll@_Locinfo@std@@QEBA?AU_Collvec@@XZ` | `0xBCD0` | 53 | UnwindData |  |
| 464 | `?_Getctype@_Locinfo@std@@QEBA?AU_Ctypevec@@XZ` | `0xBD10` | 53 | UnwindData |  |
| 465 | `?_Getcvt@_Locinfo@std@@QEBA?AU_Cvtvec@@XZ` | `0xBD50` | 53 | UnwindData |  |
| 466 | `?_Getdateorder@_Locinfo@std@@QEBAHXZ` | `0xBD90` | 19 | UnwindData |  |
| 467 | `?_Getdays@_Locinfo@std@@QEBAPEBDXZ` | `0xBDB0` | 132 | UnwindData |  |
| 468 | `?_Getfalse@_Locinfo@std@@QEBAPEBDXZ` | `0xBEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `?_Getlconv@_Locinfo@std@@QEBAPEBUlconv@@XZ` | `0xBF00` | 20 | UnwindData |  |
| 486 | `?_Getmonths@_Locinfo@std@@QEBAPEBDXZ` | `0xBF20` | 132 | UnwindData |  |
| 487 | `?_Getname@_Locinfo@std@@QEBAPEBDXZ` | `0xBFB0` | 31 | UnwindData |  |
| 488 | `?_Getptr@_Timevec@std@@QEBAPEAXXZ` | `0xBFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 489 | `?_Gettnames@_Locinfo@std@@QEBA?AV_Timevec@2@XZ` | `0xBFE0` | 62 | UnwindData |  |
| 490 | `?_Gettrue@_Locinfo@std@@QEBAPEBDXZ` | `0xC020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `?_Gnavail@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBA_JXZ` | `0xC030` | 56 | UnwindData |  |
| 494 | `?_Gndec@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAPEADXZ` | `0xC070` | 77 | UnwindData |  |
| 497 | `?_Gninc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAPEADXZ` | `0xC0C0` | 85 | UnwindData |  |
| 507 | `?_Incref@facet@locale@std@@UEAAXXZ` | `0xC120` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `?_Init@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXPEAPEAD0PEAH001@Z` | `0xC270` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `?_Init@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXXZ` | `0xC2E0` | 156 | UnwindData |  |
| 515 | `?_Init@?$codecvt@DDU_Mbstatet@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `?_Init@?$codecvt@GDU_Mbstatet@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC390` | 91 | UnwindData |  |
| 517 | `?_Init@?$codecvt@_SDU_Mbstatet@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `?_Init@?$codecvt@_UDU_Mbstatet@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `?_Init@?$codecvt@_WDU_Mbstatet@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC410` | 91 | UnwindData |  |
| 520 | `?_Init@?$ctype@D@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC470` | 57 | UnwindData |  |
| 521 | `?_Init@?$ctype@G@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC4B0` | 137 | UnwindData |  |
| 522 | `?_Init@?$ctype@_W@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC540` | 137 | UnwindData |  |
| 535 | `?_Init@ios_base@std@@IEAAXXZ` | `0xC5D0` | 192 | UnwindData |  |
| 561 | `?_Lock@?$basic_streambuf@DU?$char_traits@D@std@@@std@@UEAAXXZ` | `0xC760` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `?_Pnavail@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBA_JXZ` | `0xC9F0` | 56 | UnwindData |  |
| 595 | `?_Pninc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAPEADXZ` | `0xCA30` | 85 | UnwindData |  |
| 640 | `?_Tidy@?$_Yarn@D@std@@AEAAXXZ` | `0xCF90` | 57 | UnwindData |  |
| 642 | `?_Tidy@?$_Yarn@_W@std@@AEAAXXZ` | `0xCFD0` | 57 | UnwindData |  |
| 643 | `?_Tidy@?$ctype@D@std@@IEAAXXZ` | `0xD010` | 95 | UnwindData |  |
| 647 | `?_Tidy@ios_base@std@@AEAAXXZ` | `0xD070` | 193 | UnwindData |  |
| 648 | `?_Unlock@?$basic_streambuf@DU?$char_traits@D@std@@@std@@UEAAXXZ` | `0xD230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | `?_W_Getdays@_Locinfo@std@@QEBAPEBGXZ` | `0xD240` | 132 | UnwindData |  |
| 652 | `?_W_Getmonths@_Locinfo@std@@QEBAPEBGXZ` | `0xD2D0` | 132 | UnwindData |  |
| 653 | `?_W_Gettnames@_Locinfo@std@@QEBA?AV_Timevec@2@XZ` | `0xD360` | 62 | UnwindData |  |
| 678 | `?always_noconv@codecvt_base@std@@QEBA_NXZ` | `0xD470` | 47 | UnwindData |  |
| 679 | `?bad@ios_base@std@@QEBA_NXZ` | `0xD550` | 48 | UnwindData |  |
| 680 | `?c_str@?$_Yarn@D@std@@QEBAPEBDXZ` | `0xD580` | 56 | UnwindData |  |
| 686 | `?classic_table@?$ctype@D@std@@SAPEBFXZ` | `0xD600` | 31 | UnwindData |  |
| 687 | `?clear@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXH_N@Z` | `0xD620` | 101 | UnwindData |  |
| 693 | `?clear@ios_base@std@@QEAAXH@Z` | `0xD690` | 36 | UnwindData |  |
| 694 | `?clear@ios_base@std@@QEAAXH_N@Z` | `0xD6C0` | 230 | UnwindData |  |
| 695 | `?clear@ios_base@std@@QEAAXI@Z` | `0xD7B0` | 33 | UnwindData |  |
| 700 | `?copyfmt@ios_base@std@@QEAAAEAV12@AEBV12@@Z` | `0xD900` | 383 | UnwindData |  |
| 705 | `?do_always_noconv@?$codecvt@DDU_Mbstatet@@@std@@MEBA_NXZ` | `0xDC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 706 | `?do_always_noconv@?$codecvt@GDU_Mbstatet@@@std@@MEBA_NXZ` | `0xDC30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `?do_always_noconv@?$codecvt@_SDU_Mbstatet@@@std@@MEBA_NXZ` | `0xDC40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 708 | `?do_always_noconv@?$codecvt@_UDU_Mbstatet@@@std@@MEBA_NXZ` | `0xDC50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `?do_always_noconv@?$codecvt@_WDU_Mbstatet@@@std@@MEBA_NXZ` | `0xDC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `?do_always_noconv@codecvt_base@std@@MEBA_NXZ` | `0xDC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `?do_encoding@?$codecvt@GDU_Mbstatet@@@std@@MEBAHXZ` | `0xDC80` | 44 | UnwindData |  |
| 715 | `?do_encoding@?$codecvt@_SDU_Mbstatet@@@std@@MEBAHXZ` | `0xDCB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `?do_encoding@?$codecvt@_UDU_Mbstatet@@@std@@MEBAHXZ` | `0xDCC0` | 48 | UnwindData |  |
| 717 | `?do_encoding@?$codecvt@_WDU_Mbstatet@@@std@@MEBAHXZ` | `0xDCF0` | 44 | UnwindData |  |
| 718 | `?do_encoding@codecvt_base@std@@MEBAHXZ` | `0xDD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `?do_in@?$codecvt@DDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAD3AEAPEAD@Z` | `0xDD30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `?do_in@?$codecvt@GDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAG3AEAPEAG@Z` | `0xDD70` | 337 | UnwindData |  |
| 772 | `?do_in@?$codecvt@_SDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_S3AEAPEA_S@Z` | `0xDED0` | 1,532 | UnwindData |  |
| 773 | `?do_in@?$codecvt@_UDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_U3AEAPEA_U@Z` | `0xE4D0` | 971 | UnwindData |  |
| 774 | `?do_in@?$codecvt@_WDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_W3AEAPEA_W@Z` | `0xE8A0` | 337 | UnwindData |  |
| 775 | `?do_is@?$ctype@G@std@@MEBAPEBGPEBG0PEAF@Z` | `0xEA00` | 76 | UnwindData |  |
| 776 | `?do_is@?$ctype@G@std@@MEBA_NFG@Z` | `0xEA50` | 82 | UnwindData |  |
| 777 | `?do_is@?$ctype@_W@std@@MEBAPEB_WPEB_W0PEAF@Z` | `0xEAB0` | 76 | UnwindData |  |
| 778 | `?do_is@?$ctype@_W@std@@MEBA_NF_W@Z` | `0xEB00` | 82 | UnwindData |  |
| 779 | `?do_length@?$codecvt@DDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0xEB60` | 99 | UnwindData |  |
| 780 | `?do_length@?$codecvt@GDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0xEBD0` | 252 | UnwindData |  |
| 781 | `?do_length@?$codecvt@_SDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0xECD0` | 64 | UnwindData |  |
| 782 | `?do_length@?$codecvt@_UDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0xED10` | 64 | UnwindData |  |
| 783 | `?do_length@?$codecvt@_WDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0xED50` | 252 | UnwindData |  |
| 784 | `?do_max_length@?$codecvt@GDU_Mbstatet@@@std@@MEBAHXZ` | `0xEE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `?do_max_length@?$codecvt@_SDU_Mbstatet@@@std@@MEBAHXZ` | `0xEE60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 786 | `?do_max_length@?$codecvt@_UDU_Mbstatet@@@std@@MEBAHXZ` | `0xEEA0` | 48 | UnwindData |  |
| 787 | `?do_max_length@?$codecvt@_WDU_Mbstatet@@@std@@MEBAHXZ` | `0xEED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 788 | `?do_max_length@codecvt_base@std@@MEBAHXZ` | `0xEEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `?do_narrow@?$ctype@D@std@@MEBADDD@Z` | `0xEEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 790 | `?do_narrow@?$ctype@D@std@@MEBAPEBDPEBD0DPEAD@Z` | `0xEF10` | 83 | UnwindData |  |
| 791 | `?do_narrow@?$ctype@G@std@@MEBADGD@Z` | `0xEF70` | 45 | UnwindData |  |
| 792 | `?do_narrow@?$ctype@G@std@@MEBAPEBGPEBG0DPEAD@Z` | `0xEFA0` | 124 | UnwindData |  |
| 793 | `?do_narrow@?$ctype@_W@std@@MEBAD_WD@Z` | `0xF020` | 45 | UnwindData |  |
| 794 | `?do_narrow@?$ctype@_W@std@@MEBAPEB_WPEB_W0DPEAD@Z` | `0xF050` | 124 | UnwindData |  |
| 795 | `?do_out@?$codecvt@DDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAD3AEAPEAD@Z` | `0xF0D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `?do_out@?$codecvt@GDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBG1AEAPEBGPEAD3AEAPEAD@Z` | `0xF110` | 560 | UnwindData |  |
| 797 | `?do_out@?$codecvt@_SDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEB_S1AEAPEB_SPEAD3AEAPEAD@Z` | `0xF340` | 884 | UnwindData |  |
| 798 | `?do_out@?$codecvt@_UDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEB_U1AEAPEB_UPEAD3AEAPEAD@Z` | `0xF6C0` | 717 | UnwindData |  |
| 799 | `?do_out@?$codecvt@_WDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEB_W1AEAPEB_WPEAD3AEAPEAD@Z` | `0xF990` | 560 | UnwindData |  |
| 827 | `?do_scan_is@?$ctype@G@std@@MEBAPEBGFPEBG0@Z` | `0xFBC0` | 109 | UnwindData |  |
| 828 | `?do_scan_is@?$ctype@_W@std@@MEBAPEB_WFPEB_W0@Z` | `0xFC30` | 109 | UnwindData |  |
| 829 | `?do_scan_not@?$ctype@G@std@@MEBAPEBGFPEBG0@Z` | `0xFCA0` | 109 | UnwindData |  |
| 830 | `?do_scan_not@?$ctype@_W@std@@MEBAPEB_WFPEB_W0@Z` | `0xFD10` | 109 | UnwindData |  |
| 831 | `?do_tolower@?$ctype@D@std@@MEBADD@Z` | `0xFD80` | 40 | UnwindData |  |
| 832 | `?do_tolower@?$ctype@D@std@@MEBAPEBDPEADPEBD@Z` | `0xFDB0` | 106 | UnwindData |  |
| 833 | `?do_tolower@?$ctype@G@std@@MEBAGG@Z` | `0xFE20` | 41 | UnwindData |  |
| 834 | `?do_tolower@?$ctype@G@std@@MEBAPEBGPEAGPEBG@Z` | `0xFE50` | 108 | UnwindData |  |
| 835 | `?do_tolower@?$ctype@_W@std@@MEBAPEB_WPEA_WPEB_W@Z` | `0xFEC0` | 108 | UnwindData |  |
| 836 | `?do_tolower@?$ctype@_W@std@@MEBA_W_W@Z` | `0xFF30` | 41 | UnwindData |  |
| 837 | `?do_toupper@?$ctype@D@std@@MEBADD@Z` | `0xFF60` | 40 | UnwindData |  |
| 838 | `?do_toupper@?$ctype@D@std@@MEBAPEBDPEADPEBD@Z` | `0xFF90` | 106 | UnwindData |  |
| 839 | `?do_toupper@?$ctype@G@std@@MEBAGG@Z` | `0x10000` | 41 | UnwindData |  |
| 840 | `?do_toupper@?$ctype@G@std@@MEBAPEBGPEAGPEBG@Z` | `0x10030` | 108 | UnwindData |  |
| 841 | `?do_toupper@?$ctype@_W@std@@MEBAPEB_WPEA_WPEB_W@Z` | `0x100A0` | 108 | UnwindData |  |
| 842 | `?do_toupper@?$ctype@_W@std@@MEBA_W_W@Z` | `0x10110` | 41 | UnwindData |  |
| 843 | `?do_unshift@?$codecvt@DDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x10140` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `?do_unshift@?$codecvt@GDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x10170` | 276 | UnwindData |  |
| 845 | `?do_unshift@?$codecvt@_SDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x10290` | 84 | UnwindData |  |
| 846 | `?do_unshift@?$codecvt@_UDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x102F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `?do_unshift@?$codecvt@_WDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x10320` | 276 | UnwindData |  |
| 848 | `?do_widen@?$ctype@D@std@@MEBADD@Z` | `0x10440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `?do_widen@?$ctype@D@std@@MEBAPEBDPEBD0PEAD@Z` | `0x10450` | 83 | UnwindData |  |
| 850 | `?do_widen@?$ctype@G@std@@MEBAGD@Z` | `0x104B0` | 33 | UnwindData |  |
| 851 | `?do_widen@?$ctype@G@std@@MEBAPEBDPEBD0PEAG@Z` | `0x104E0` | 119 | UnwindData |  |
| 852 | `?do_widen@?$ctype@_W@std@@MEBAPEBDPEBD0PEA_W@Z` | `0x10560` | 119 | UnwindData |  |
| 853 | `?do_widen@?$ctype@_W@std@@MEBA_WD@Z` | `0x105E0` | 33 | UnwindData |  |
| 854 | `?eback@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x10610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 857 | `?egptr@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x10630` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `?encoding@codecvt_base@std@@QEBAHXZ` | `0x10690` | 47 | UnwindData |  |
| 865 | `?eof@ios_base@std@@QEBA_NXZ` | `0x106D0` | 27 | UnwindData |  |
| 866 | `?epptr@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x106F0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `?exceptions@ios_base@std@@QEAAXH@Z` | `0x10860` | 56 | UnwindData |  |
| 870 | `?exceptions@ios_base@std@@QEAAXI@Z` | `0x108A0` | 33 | UnwindData |  |
| 871 | `?exceptions@ios_base@std@@QEBAHXZ` | `0x108D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `?fail@ios_base@std@@QEBA_NXZ` | `0x108E0` | 48 | UnwindData |  |
| 879 | `?flags@ios_base@std@@QEAAHH@Z` | `0x10910` | 49 | UnwindData |  |
| 880 | `?flags@ios_base@std@@QEBAHXZ` | `0x10950` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 884 | `?gbump@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXH@Z` | `0x109E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `?getloc@ios_base@std@@QEBA?AVlocale@2@XZ` | `0x10A30` | 43 | UnwindData |  |
| 974 | `?good@ios_base@std@@QEBA_NXZ` | `0x10A60` | 51 | UnwindData |  |
| 975 | `?gptr@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x10AA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `?imbue@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAXAEBVlocale@2@@Z` | `0x10AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `?imbue@ios_base@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x10B00` | 107 | UnwindData |  |
| 1027 | `?in@?$codecvt@DDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAD3AEAPEAD@Z` | `0x10B70` | 145 | UnwindData |  |
| 1028 | `?in@?$codecvt@GDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAG3AEAPEAG@Z` | `0x10C10` | 145 | UnwindData |  |
| 1029 | `?in@?$codecvt@_SDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_S3AEAPEA_S@Z` | `0x10CB0` | 145 | UnwindData |  |
| 1030 | `?in@?$codecvt@_UDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_U3AEAPEA_U@Z` | `0x10D50` | 145 | UnwindData |  |
| 1031 | `?in@?$codecvt@_WDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_W3AEAPEA_W@Z` | `0x10DF0` | 145 | UnwindData |  |
| 1035 | `?init@?$basic_ios@DU?$char_traits@D@std@@@std@@IEAAXPEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@_N@Z` | `0x10E90` | 132 | UnwindData |  |
| 1047 | `?is@?$ctype@D@std@@QEBAPEBDPEBD0PEAF@Z` | `0x10F30` | 122 | UnwindData |  |
| 1048 | `?is@?$ctype@D@std@@QEBA_NFD@Z` | `0x10FB0` | 73 | UnwindData |  |
| 1049 | `?is@?$ctype@G@std@@QEBAPEBGPEBG0PEAF@Z` | `0x11000` | 87 | UnwindData |  |
| 1050 | `?is@?$ctype@G@std@@QEBA_NFG@Z` | `0x11060` | 79 | UnwindData |  |
| 1051 | `?is@?$ctype@_W@std@@QEBAPEB_WPEB_W0PEAF@Z` | `0x110B0` | 87 | UnwindData |  |
| 1052 | `?is@?$ctype@_W@std@@QEBA_NF_W@Z` | `0x11110` | 79 | UnwindData |  |
| 1056 | `?iword@ios_base@std@@QEAAAEAJH@Z` | `0x11170` | 36 | UnwindData |  |
| 1058 | `?length@?$codecvt@GDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0x11240` | 97 | UnwindData |  |
| 1059 | `?length@?$codecvt@_SDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0x112B0` | 97 | UnwindData |  |
| 1060 | `?length@?$codecvt@_UDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0x11320` | 97 | UnwindData |  |
| 1061 | `?length@?$codecvt@_WDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0x11390` | 97 | UnwindData |  |
| 1062 | `?max_length@codecvt_base@std@@QEBAHXZ` | `0x11430` | 47 | UnwindData |  |
| 1072 | `?narrow@?$ctype@D@std@@QEBADDD@Z` | `0x11740` | 77 | UnwindData |  |
| 1073 | `?narrow@?$ctype@D@std@@QEBAPEBDPEBD0DPEAD@Z` | `0x11790` | 98 | UnwindData |  |
| 1074 | `?narrow@?$ctype@G@std@@QEBADGD@Z` | `0x11800` | 78 | UnwindData |  |
| 1075 | `?narrow@?$ctype@G@std@@QEBAPEBGPEBG0DPEAD@Z` | `0x11850` | 98 | UnwindData |  |
| 1076 | `?narrow@?$ctype@_W@std@@QEBAD_WD@Z` | `0x118C0` | 78 | UnwindData |  |
| 1077 | `?narrow@?$ctype@_W@std@@QEBAPEB_WPEB_W0DPEAD@Z` | `0x11910` | 98 | UnwindData |  |
| 1084 | `?out@?$codecvt@DDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAD3AEAPEAD@Z` | `0x119D0` | 145 | UnwindData |  |
| 1085 | `?out@?$codecvt@GDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBG1AEAPEBGPEAD3AEAPEAD@Z` | `0x11A70` | 145 | UnwindData |  |
| 1086 | `?out@?$codecvt@_SDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEB_S1AEAPEB_SPEAD3AEAPEAD@Z` | `0x11B10` | 145 | UnwindData |  |
| 1087 | `?out@?$codecvt@_UDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEB_U1AEAPEB_UPEAD3AEAPEAD@Z` | `0x11BB0` | 145 | UnwindData |  |
| 1088 | `?out@?$codecvt@_WDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEB_W1AEAPEB_WPEAD3AEAPEAD@Z` | `0x11C50` | 145 | UnwindData |  |
| 1089 | `?overflow@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHH@Z` | `0x11FB0` | 23 | UnwindData |  |
| 1092 | `?pbackfail@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHH@Z` | `0x12140` | 23 | UnwindData |  |
| 1098 | `?pbump@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXH@Z` | `0x12160` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `?pptr@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x121B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `?precision@ios_base@std@@QEAA_J_J@Z` | `0x121D0` | 50 | UnwindData |  |
| 1108 | `?precision@ios_base@std@@QEBA_JXZ` | `0x12210` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1166 | `?pword@ios_base@std@@QEAAAEAPEAXH@Z` | `0x122E0` | 36 | UnwindData |  |
| 1173 | `?rdstate@ios_base@std@@QEBAHXZ` | `0x12310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `?register_callback@ios_base@std@@QEAAXP6AXW4event@12@AEAV12@H@ZH@Z` | `0x12320` | 115 | UnwindData |  |
| 1185 | `?scan_is@?$ctype@D@std@@QEBAPEBDFPEBD0@Z` | `0x123D0` | 108 | UnwindData |  |
| 1186 | `?scan_is@?$ctype@G@std@@QEBAPEBGFPEBG0@Z` | `0x12440` | 87 | UnwindData |  |
| 1187 | `?scan_is@?$ctype@_W@std@@QEBAPEB_WFPEB_W0@Z` | `0x124A0` | 87 | UnwindData |  |
| 1188 | `?scan_not@?$ctype@D@std@@QEBAPEBDFPEBD0@Z` | `0x12500` | 108 | UnwindData |  |
| 1189 | `?scan_not@?$ctype@G@std@@QEBAPEBGFPEBG0@Z` | `0x12570` | 87 | UnwindData |  |
| 1190 | `?scan_not@?$ctype@_W@std@@QEBAPEB_WFPEB_W0@Z` | `0x125D0` | 87 | UnwindData |  |
| 1197 | `?seekoff@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA?AV?$fpos@U_Mbstatet@@@2@_JHH@Z` | `0x12730` | 51 | UnwindData |  |
| 1206 | `?seekpos@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA?AV?$fpos@U_Mbstatet@@@2@V32@H@Z` | `0x12840` | 51 | UnwindData |  |
| 1214 | `?setbuf@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAPEAV12@PEAD_J@Z` | `0x12930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `?setf@ios_base@std@@QEAAHH@Z` | `0x12950` | 61 | UnwindData |  |
| 1218 | `?setf@ios_base@std@@QEAAHHH@Z` | `0x12990` | 78 | UnwindData |  |
| 1219 | `?setg@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXPEAD00@Z` | `0x129E0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1224 | `?setp@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXPEAD0@Z` | `0x12A40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `?setstate@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXH_N@Z` | `0x12A90` | 56 | UnwindData |  |
| 1236 | `?setstate@ios_base@std@@QEAAXH@Z` | `0x12AD0` | 48 | UnwindData |  |
| 1237 | `?setstate@ios_base@std@@QEAAXH_N@Z` | `0x12B00` | 56 | UnwindData |  |
| 1238 | `?setstate@ios_base@std@@QEAAXI@Z` | `0x12B40` | 33 | UnwindData |  |
| 1246 | `?showmanyc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA_JXZ` | `0x12B70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1282 | `?swap@ios_base@std@@QEAAXAEAV12@@Z` | `0x12BC0` | 249 | UnwindData |  |
| 1286 | `?sync@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x12D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `?sync_with_stdio@ios_base@std@@SA_N_N@Z` | `0x12D70` | 74 | UnwindData |  |
| 1290 | `?table@?$ctype@D@std@@QEBAPEBFXZ` | `0x12DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1298 | `?tie@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAPEAV?$basic_ostream@DU?$char_traits@D@std@@@2@PEAV32@@Z` | `0x12DD0` | 50 | UnwindData |  |
| 1304 | `?tolower@?$ctype@D@std@@QEBADD@Z` | `0x12E30` | 66 | UnwindData |  |
| 1305 | `?tolower@?$ctype@D@std@@QEBAPEBDPEADPEBD@Z` | `0x12E80` | 77 | UnwindData |  |
| 1306 | `?tolower@?$ctype@G@std@@QEBAGG@Z` | `0x12ED0` | 67 | UnwindData |  |
| 1307 | `?tolower@?$ctype@G@std@@QEBAPEBGPEAGPEBG@Z` | `0x12F20` | 77 | UnwindData |  |
| 1308 | `?tolower@?$ctype@_W@std@@QEBAPEB_WPEA_WPEB_W@Z` | `0x12F70` | 77 | UnwindData |  |
| 1309 | `?tolower@?$ctype@_W@std@@QEBA_W_W@Z` | `0x12FC0` | 67 | UnwindData |  |
| 1310 | `?toupper@?$ctype@D@std@@QEBADD@Z` | `0x13010` | 66 | UnwindData |  |
| 1311 | `?toupper@?$ctype@D@std@@QEBAPEBDPEADPEBD@Z` | `0x13060` | 77 | UnwindData |  |
| 1312 | `?toupper@?$ctype@G@std@@QEBAGG@Z` | `0x130B0` | 67 | UnwindData |  |
| 1313 | `?toupper@?$ctype@G@std@@QEBAPEBGPEAGPEBG@Z` | `0x13100` | 77 | UnwindData |  |
| 1314 | `?toupper@?$ctype@_W@std@@QEBAPEB_WPEA_WPEB_W@Z` | `0x13150` | 77 | UnwindData |  |
| 1315 | `?toupper@?$ctype@_W@std@@QEBA_W_W@Z` | `0x131A0` | 67 | UnwindData |  |
| 1316 | `?uflow@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x13560` | 117 | UnwindData |  |
| 1321 | `?underflow@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x136D0` | 19 | UnwindData |  |
| 1327 | `?unsetf@ios_base@std@@QEAAXH@Z` | `0x136F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `?unshift@?$codecvt@DDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x13720` | 97 | UnwindData |  |
| 1329 | `?unshift@?$codecvt@GDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x13790` | 97 | UnwindData |  |
| 1330 | `?unshift@?$codecvt@_SDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x13800` | 97 | UnwindData |  |
| 1331 | `?unshift@?$codecvt@_UDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x13870` | 97 | UnwindData |  |
| 1332 | `?unshift@?$codecvt@_WDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x138E0` | 97 | UnwindData |  |
| 1341 | `?widen@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBADD@Z` | `0x13970` | 97 | UnwindData |  |
| 1344 | `?widen@?$ctype@D@std@@QEBADD@Z` | `0x139E0` | 66 | UnwindData |  |
| 1345 | `?widen@?$ctype@D@std@@QEBAPEBDPEBD0PEAD@Z` | `0x13A30` | 87 | UnwindData |  |
| 1346 | `?widen@?$ctype@G@std@@QEBAGD@Z` | `0x13A90` | 66 | UnwindData |  |
| 1347 | `?widen@?$ctype@G@std@@QEBAPEBDPEBD0PEAG@Z` | `0x13AE0` | 87 | UnwindData |  |
| 1348 | `?widen@?$ctype@_W@std@@QEBAPEBDPEBD0PEA_W@Z` | `0x13B40` | 87 | UnwindData |  |
| 1349 | `?widen@?$ctype@_W@std@@QEBA_WD@Z` | `0x13BA0` | 66 | UnwindData |  |
| 1350 | `?width@ios_base@std@@QEAA_J_J@Z` | `0x13BF0` | 50 | UnwindData |  |
| 1351 | `?width@ios_base@std@@QEBA_JXZ` | `0x13C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `?xalloc@ios_base@std@@SAHXZ` | `0x13C40` | 71 | UnwindData |  |
| 1356 | `?xsgetn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA_JPEAD_J@Z` | `0x13E80` | 303 | UnwindData |  |
| 1359 | `?xsputn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA_JPEBD_J@Z` | `0x140E0` | 326 | UnwindData |  |
| 27 | `??0?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@_N@Z` | `0x14230` | 221 | UnwindData |  |
| 132 | `??1?$basic_istream@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x14360` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `??_D?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x143B0` | 49 | UnwindData |  |
| 1362 | `_Chmod` | `0x15A60` | 192 | UnwindData |  |
| 1363 | `_Close_dir` | `0x15B20` | 26 | UnwindData |  |
| 1375 | `_Copy_file` | `0x15B40` | 99 | UnwindData |  |
| 1377 | `_Current_get` | `0x15BB0` | 75 | UnwindData |  |
| 1378 | `_Current_set` | `0x15C00` | 52 | UnwindData |  |
| 1381 | `_Equivalent` | `0x15C40` | 731 | UnwindData |  |
| 1391 | `_File_size` | `0x15F20` | 90 | UnwindData |  |
| 1398 | `_Hard_links` | `0x15F80` | 186 | UnwindData |  |
| 1409 | `_Last_write_time` | `0x16040` | 114 | UnwindData |  |
| 1410 | `_Link` | `0x160C0` | 66 | UnwindData |  |
| 1412 | `_Lstat` | `0x16110` | 34 | UnwindData |  |
| 1413 | `_Make_dir` | `0x16140` | 69 | UnwindData |  |
| 1432 | `_Open_dir` | `0x16190` | 543 | UnwindData |  |
| 1435 | `_Read_dir` | `0x163B0` | 256 | UnwindData |  |
| 1436 | `_Remove_dir` | `0x164B0` | 53 | UnwindData |  |
| 1437 | `_Rename` | `0x164F0` | 63 | UnwindData |  |
| 1438 | `_Resize` | `0x16530` | 141 | UnwindData |  |
| 1439 | `_Set_last_write_time` | `0x165C0` | 156 | UnwindData |  |
| 1442 | `_Stat` | `0x16660` | 388 | UnwindData |  |
| 1443 | `_Statvfs` | `0x167F0` | 280 | UnwindData |  |
| 1459 | `_Symlink` | `0x16910` | 69 | UnwindData |  |
| 1460 | `_Symlink_get` | `0x16960` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1461 | `_Temp_get` | `0x16990` | 116 | UnwindData |  |
| 1474 | `_To_byte` | `0x16A10` | 82 | UnwindData |  |
| 1475 | `_To_wide` | `0x16A70` | 64 | UnwindData |  |
| 1480 | `_Unlink` | `0x16AB0` | 53 | UnwindData |  |
| 436 | `?_Fiopen@std@@YAPEAU_iobuf@@PEBDHH@Z` | `0x16D10` | 42 | UnwindData |  |
| 437 | `?_Fiopen@std@@YAPEAU_iobuf@@PEBGHH@Z` | `0x16D40` | 42 | UnwindData |  |
| 438 | `?_Fiopen@std@@YAPEAU_iobuf@@PEB_WHH@Z` | `0x16D70` | 42 | UnwindData |  |
| 622 | `?_Rethrow_future_exception@std@@YAXVexception_ptr@1@@Z` | `0x170F0` | 67 | UnwindData |  |
| 639 | `?_Throw_future_error@std@@YAXAEBVerror_code@1@@Z` | `0x17140` | 74 | UnwindData |  |
| 1181 | `?resetiosflags@std@@YA?AU?$_Smanip@H@1@H@Z` | `0x17250` | 45 | UnwindData |  |
| 1213 | `?setbase@std@@YA?AU?$_Smanip@H@1@H@Z` | `0x17330` | 45 | UnwindData |  |
| 1222 | `?setiosflags@std@@YA?AU?$_Smanip@H@1@H@Z` | `0x17360` | 45 | UnwindData |  |
| 1229 | `?setprecision@std@@YA?AU?$_Smanip@_J@1@_J@Z` | `0x17390` | 46 | UnwindData |  |
| 1239 | `?setw@std@@YA?AU?$_Smanip@_J@1@_J@Z` | `0x173C0` | 46 | UnwindData |  |
| 410 | `?_Addstd@ios_base@std@@SAXPEAV12@@Z` | `0x17480` | 209 | UnwindData |  |
| 545 | `?_Ios_base_dtor@ios_base@std@@CAXPEAV12@@Z` | `0x17560` | 151 | UnwindData |  |
| 412 | `?_Atexit@@YAXP6AXXZ@Z` | `0x17670` | 89 | UnwindData |  |
| 540 | `?_Init_cnt_func@Init@ios_base@std@@CAAEAHXZ` | `0x17910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `?_Init_ctor@Init@ios_base@std@@CAXPEAV123@@Z` | `0x17920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `?_Init_dtor@Init@ios_base@std@@CAXPEAV123@@Z` | `0x17950` | 106 | UnwindData |  |
| 589 | `?_Osfx@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x179C0` | 193 | UnwindData |  |
| 881 | `?flush@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@XZ` | `0x17A90` | 199 | UnwindData |  |
| 1127 | `?pubsync@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x17B60` | 47 | UnwindData |  |
| 1168 | `?rdbuf@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBAPEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@XZ` | `0x17B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `?tie@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBAPEAV?$basic_ostream@DU?$char_traits@D@std@@@2@XZ` | `0x17BA0` | 13,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `??0?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x1B1F0` | 76 | UnwindData |  |
| 79 | `??0?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x1B240` | 76 | UnwindData |  |
| 149 | `??1?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEAA@XZ` | `0x1B320` | 40 | UnwindData |  |
| 152 | `??1?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEAA@XZ` | `0x1B350` | 40 | UnwindData |  |
| 432 | `?_Ffmt@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAPEADPEADDH@Z` | `0x1B8E0` | 367 | UnwindData |  |
| 450 | `?_Getcat@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x1BA50` | 243 | UnwindData |  |
| 453 | `?_Getcat@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x1BB50` | 243 | UnwindData |  |
| 504 | `?_Ifmt@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAPEADPEADPEBDH@Z` | `0x1BD50` | 390 | UnwindData |  |
| 523 | `?_Init@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x1BF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | `?_Init@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x1BF60` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `?_Iput@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEAD_K@Z` | `0x1C140` | 1,859 | UnwindData |  |
| 554 | `?_Locimp_Addfac@_Locimp@locale@std@@CAXPEAV123@PEAVfacet@23@_K@Z` | `0x1C890` | 541 | UnwindData |  |
| 555 | `?_Locimp_ctor@_Locimp@locale@std@@CAXPEAV123@AEBV123@@Z` | `0x1CAB0` | 356 | UnwindData |  |
| 557 | `?_Locinfo_Addcats@_Locinfo@std@@SAAEAV12@PEAV12@HPEBD@Z` | `0x1CC20` | 347 | UnwindData |  |
| 558 | `?_Locinfo_ctor@_Locinfo@std@@SAXPEAV12@HPEBD@Z` | `0x1CD80` | 80 | UnwindData |  |
| 579 | `?_Makeloc@_Locimp@locale@std@@CAPEAV123@AEBV_Locinfo@3@HPEAV123@PEBV23@@Z` | `0x1CDD0` | 1,586 | UnwindData |  |
| 610 | `?_Put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@PEBD_K@Z` | `0x1D490` | 139 | UnwindData |  |
| 616 | `?_Rep@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@D_K@Z` | `0x1D520` | 115 | UnwindData |  |
| 719 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x1D970` | 611 | UnwindData |  |
| 720 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x1DBE0` | 212 | UnwindData |  |
| 721 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x1DCC0` | 442 | UnwindData |  |
| 722 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x1DE80` | 442 | UnwindData |  |
| 723 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x1E040` | 420 | UnwindData |  |
| 724 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x1E1F0` | 420 | UnwindData |  |
| 725 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x1E3A0` | 216 | UnwindData |  |
| 726 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x1E480` | 448 | UnwindData |  |
| 727 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x1E640` | 444 | UnwindData |  |
| 728 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x1E800` | 444 | UnwindData |  |
| 729 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x1E9C0` | 976 | UnwindData |  |
| 800 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DJ@Z` | `0x1EDD0` | 283 | UnwindData |  |
| 801 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DK@Z` | `0x1EEF0` | 283 | UnwindData |  |
| 802 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DN@Z` | `0x1F010` | 816 | UnwindData |  |
| 803 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DO@Z` | `0x1F340` | 815 | UnwindData |  |
| 804 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBX@Z` | `0x1F670` | 244 | UnwindData |  |
| 805 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_J@Z` | `0x1F770` | 283 | UnwindData |  |
| 806 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_K@Z` | `0x1F890` | 283 | UnwindData |  |
| 807 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_N@Z` | `0x1F9B0` | 1,001 | UnwindData |  |
| 973 | `?global@locale@std@@SA?AV12@AEBV12@@Z` | `0x1FF20` | 441 | UnwindData |  |
| 1182 | `?sbumpc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x202F0` | 94 | UnwindData |  |
| 1240 | `?sgetc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x20350` | 94 | UnwindData |  |
| 1255 | `?sputc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHD@Z` | `0x203B0` | 135 | UnwindData |  |
| 478 | `?_Getgloballocale@locale@std@@CAPEAV_Locimp@12@XZ` | `0x208C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `?_Init@locale@std@@CAPEAV_Locimp@12@_N@Z` | `0x208D0` | 287 | UnwindData |  |
| 556 | `?_Locimp_dtor@_Locimp@locale@std@@CAXPEAV123@@Z` | `0x209F0` | 257 | UnwindData |  |
| 559 | `?_Locinfo_ctor@_Locinfo@std@@SAXPEAV12@PEBD@Z` | `0x20B00` | 138 | UnwindData |  |
| 560 | `?_Locinfo_dtor@_Locinfo@std@@SAXPEAV12@@Z` | `0x20B90` | 85 | UnwindData |  |
| 587 | `?_New_Locimp@_Locimp@locale@std@@CAPEAV123@AEBV123@@Z` | `0x20BF0` | 83 | UnwindData |  |
| 588 | `?_New_Locimp@_Locimp@locale@std@@CAPEAV123@_N@Z` | `0x20C50` | 82 | UnwindData |  |
| 625 | `?_Setgloballocale@locale@std@@CAXPEAX@Z` | `0x20CB0` | 57 | UnwindData |  |
| 685 | `?classic@locale@std@@SAAEBV12@XZ` | `0x20CF0` | 68 | UnwindData |  |
| 863 | `?empty@locale@std@@SA?AV12@XZ` | `0x20D40` | 87 | UnwindData |  |
| 575 | `?_MP_Add@std@@YAXQEA_K_K@Z` | `0x21950` | 132 | UnwindData |  |
| 576 | `?_MP_Get@std@@YA_KQEA_K@Z` | `0x219E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 577 | `?_MP_Mul@std@@YAXQEA_K_K1@Z` | `0x21A10` | 137 | UnwindData |  |
| 578 | `?_MP_Rem@std@@YAXQEA_K_K@Z` | `0x21AA0` | 108 | UnwindData |  |
| 953 | `?get_new_handler@std@@YAP6AXXZXZ` | `0x22190` | 54 | UnwindData |  |
| 1209 | `?set_new_handler@std@@YAP6AXXZP6AXXZ@Z` | `0x22220` | 122 | UnwindData |  |
| 421 | `?_Debug_message@std@@YAXPEBG0I@Z` | `0x222D0` | 45 | UnwindData |  |
| 422 | `?_Debug_message@std@@YAXPEB_W0I@Z` | `0x22300` | 76 | UnwindData |  |
| 636 | `?_Syserror_map@std@@YAPEBDH@Z` | `0x22350` | 117 | UnwindData |  |
| 654 | `?_Winerror_map@std@@YAHH@Z` | `0x223F0` | 111 | UnwindData |  |
| 655 | `?_Winerror_message@std@@YAKKPEADK@Z` | `0x22460` | 91 | UnwindData |  |
| 1364 | `_Cnd_broadcast` | `0x22770` | 26 | UnwindData |  |
| 1365 | `_Cnd_destroy` | `0x22790` | 39 | UnwindData |  |
| 1366 | `_Cnd_destroy_in_situ` | `0x227C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1368 | `_Cnd_init` | `0x227D0` | 108 | UnwindData |  |
| 1369 | `_Cnd_init_in_situ` | `0x22840` | 45 | UnwindData |  |
| 1371 | `_Cnd_signal` | `0x22870` | 26 | UnwindData |  |
| 1372 | `_Cnd_timedwait` | `0x22890` | 220 | UnwindData |  |
| 1374 | `_Cnd_wait` | `0x22970` | 56 | UnwindData |  |
| 1415 | `_Mtx_clear_owner` | `0x229B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1423 | `_Mtx_reset_owner` | `0x229E0` | 46 | UnwindData |  |
| 1463 | `_Thrd_create` | `0x22DE0` | 329 | UnwindData |  |
| 1464 | `_Thrd_current` | `0x22F30` | 45 | UnwindData |  |
| 1465 | `_Thrd_detach` | `0x22F60` | 54 | UnwindData |  |
| 1466 | `_Thrd_equal` | `0x22FA0` | 56 | UnwindData |  |
| 1467 | `_Thrd_exit` | `0x22FE0` | 24 | UnwindData |  |
| 1468 | `_Thrd_hardware_concurrency` | `0x23000` | 448 | UnwindData |  |
| 1469 | `_Thrd_id` | `0x231C0` | 15 | UnwindData |  |
| 1470 | `_Thrd_join` | `0x231D0` | 142 | UnwindData |  |
| 1471 | `_Thrd_sleep` | `0x23260` | 131 | UnwindData |  |
| 1472 | `_Thrd_start` | `0x232F0` | 107 | UnwindData |  |
| 1473 | `_Thrd_yield` | `0x23360` | 16 | UnwindData |  |
| 1416 | `_Mtx_current_owns` | `0x233A0` | 63 | UnwindData |  |
| 1417 | `_Mtx_destroy` | `0x233E0` | 49 | UnwindData |  |
| 1418 | `_Mtx_destroy_in_situ` | `0x23420` | 40 | UnwindData |  |
| 1419 | `_Mtx_getconcrtcs` | `0x23450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1420 | `_Mtx_init` | `0x23460` | 116 | UnwindData |  |
| 1421 | `_Mtx_init_in_situ` | `0x234E0` | 91 | UnwindData |  |
| 1422 | `_Mtx_lock` | `0x23540` | 26 | UnwindData |  |
| 1424 | `_Mtx_timedlock` | `0x23560` | 96 | UnwindData |  |
| 1425 | `_Mtx_trylock` | `0x235C0` | 103 | UnwindData |  |
| 1426 | `_Mtx_unlock` | `0x23630` | 145 | UnwindData |  |
| 1462 | `_Thrd_abort` | `0x236D0` | 71 | UnwindData |  |
| 1522 | `__set_stl_sync_api_mode` | `0x23720` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `?ReportUnhandledError@_ExceptionHolder@details@Concurrency@@AEAAXXZ` | `0x23980` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `??0task_continuation_context@Concurrency@@AEAA@XZ` | `0x239D0` | 40 | UnwindData |  |
| 404 | `?CaptureCallstack@platform@details@Concurrency@@YA_KPEAPEAX_K1@Z` | `0x23AA0` | 55 | UnwindData |  |
| 405 | `?GetCurrentThreadId@platform@details@Concurrency@@YAJXZ` | `0x23AE0` | 15 | UnwindData |  |
| 406 | `?GetNextAsyncId@platform@details@Concurrency@@YAIXZ` | `0x23AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `?_Assign@_ContextCallback@details@Concurrency@@AEAAXPEAX@Z` | `0x23B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `?_CallInContext@_ContextCallback@details@Concurrency@@QEBAXV?$function@$$A6AXXZ@std@@_N@Z` | `0x23B20` | 46 | UnwindData |  |
| 419 | `?_Capture@_ContextCallback@details@Concurrency@@AEAAXXZ` | `0x23B50` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `?_IsCurrentOriginSTA@_ContextCallback@details@Concurrency@@CA_NXZ` | `0x23BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `?_IsNonBlockingThread@_Task_impl_base@details@Concurrency@@SA_NXZ` | `0x23BD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `?_LogCancelTask@_TaskEventLogger@details@Concurrency@@QEAAXXZ` | `0x23C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `?_LogScheduleTask@_TaskEventLogger@details@Concurrency@@QEAAX_N@Z` | `0x23C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `?_LogTaskCompleted@_TaskEventLogger@details@Concurrency@@QEAAXXZ` | `0x23C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 572 | `?_LogTaskExecutionCompleted@_TaskEventLogger@details@Concurrency@@QEAAXXZ` | `0x23C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 573 | `?_LogWorkItemCompleted@_TaskEventLogger@details@Concurrency@@QEAAXXZ` | `0x23C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `?_LogWorkItemStarted@_TaskEventLogger@details@Concurrency@@QEAAXXZ` | `0x23C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `?_ReportUnobservedException@details@Concurrency@@YAXXZ` | `0x23C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 621 | `?_Reset@_ContextCallback@details@Concurrency@@AEAAXXZ` | `0x23C90` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 615 | `?_Release_chore@details@Concurrency@@YAXPEAU_Threadpool_chore@12@@Z` | `0x23DD0` | 51 | UnwindData |  |
| 620 | `?_Reschedule_chore@details@Concurrency@@YAHPEBU_Threadpool_chore@12@@Z` | `0x23E10` | 126 | UnwindData |  |
| 624 | `?_Schedule_chore@details@Concurrency@@YAHPEAU_Threadpool_chore@12@@Z` | `0x23E90` | 209 | UnwindData |  |
| 1367 | `_Cnd_do_broadcast_at_thread_exit` | `0x24010` | 343 | UnwindData |  |
| 1370 | `_Cnd_register_at_thread_exit` | `0x24170` | 350 | UnwindData |  |
| 1373 | `_Cnd_unregister_at_thread_exit` | `0x242D0` | 205 | UnwindData |  |
| 1433 | `_Query_perf_counter` | `0x247A0` | 25 | UnwindData |  |
| 1434 | `_Query_perf_frequency` | `0x247C0` | 83 | UnwindData |  |
| 1491 | `_Xtime_diff_to_millis` | `0x24880` | 67 | UnwindData |  |
| 1492 | `_Xtime_diff_to_millis2` | `0x248D0` | 136 | UnwindData |  |
| 1493 | `_Xtime_get_ticks` | `0x24960` | 63 | UnwindData |  |
| 1523 | `xtime_get` | `0x249A0` | 58 | UnwindData |  |
| 637 | `?_Throw_C_error@std@@YAXH@Z` | `0x24B10` | 88 | UnwindData |  |
| 638 | `?_Throw_Cpp_error@std@@YAXH@Z` | `0x24B70` | 105 | UnwindData |  |
| 1319 | `?uncaught_exception@std@@YA_NXZ` | `0x24C50` | 14 | UnwindData |  |
| 1320 | `?uncaught_exceptions@std@@YAHXZ` | `0x24C60` | 14 | UnwindData |  |
| 15 | `??0?$basic_ios@GU?$char_traits@G@std@@@std@@IEAA@XZ` | `0x25000` | 81 | UnwindData |  |
| 41 | `??0?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@_N@Z` | `0x25060` | 208 | UnwindData |  |
| 51 | `??0?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAA@XZ` | `0x25130` | 262 | UnwindData |  |
| 127 | `??1?$basic_ios@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x25320` | 40 | UnwindData |  |
| 136 | `??1?$basic_ostream@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x25350` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `??1?$basic_streambuf@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x253A0` | 82 | UnwindData |  |
| 207 | `??4_UShinit@std@@QEAAAEAV01@AEBV01@@Z` | `0x25400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `??_D?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x25410` | 49 | UnwindData |  |
| 492 | `?_Gnavail@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBA_JXZ` | `0x25670` | 56 | UnwindData |  |
| 495 | `?_Gndec@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAPEAGXZ` | `0x256B0` | 78 | UnwindData |  |
| 498 | `?_Gninc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAPEAGXZ` | `0x25700` | 86 | UnwindData |  |
| 511 | `?_Init@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXPEAPEAG0PEAH001@Z` | `0x25890` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `?_Init@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXXZ` | `0x25900` | 156 | UnwindData |  |
| 562 | `?_Lock@?$basic_streambuf@GU?$char_traits@G@std@@@std@@UEAAXXZ` | `0x25A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `?_Pnavail@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBA_JXZ` | `0x25A40` | 56 | UnwindData |  |
| 596 | `?_Pninc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAPEAGXZ` | `0x25A80` | 86 | UnwindData |  |
| 649 | `?_Unlock@?$basic_streambuf@GU?$char_traits@G@std@@@std@@UEAAXXZ` | `0x25BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 689 | `?clear@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXH_N@Z` | `0x25C00` | 101 | UnwindData |  |
| 855 | `?eback@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x25D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 858 | `?egptr@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x25DB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `?epptr@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x25DF0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `?gbump@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXH@Z` | `0x25E60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `?gptr@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x25EB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `?imbue@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAXAEBVlocale@2@@Z` | `0x25F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `?init@?$basic_ios@GU?$char_traits@G@std@@@std@@IEAAXPEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@_N@Z` | `0x25F10` | 133 | UnwindData |  |
| 1090 | `?overflow@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAGG@Z` | `0x262F0` | 24 | UnwindData |  |
| 1093 | `?pbackfail@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAGG@Z` | `0x26490` | 24 | UnwindData |  |
| 1099 | `?pbump@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXH@Z` | `0x264B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `?pptr@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x26500` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `?seekoff@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA?AV?$fpos@U_Mbstatet@@@2@_JHH@Z` | `0x26620` | 51 | UnwindData |  |
| 1207 | `?seekpos@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA?AV?$fpos@U_Mbstatet@@@2@V32@H@Z` | `0x26730` | 51 | UnwindData |  |
| 1215 | `?setbuf@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAPEAV12@PEAG_J@Z` | `0x26810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `?setg@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXPEAG00@Z` | `0x26830` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `?setp@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXPEAG0@Z` | `0x26890` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `?setstate@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXH_N@Z` | `0x268E0` | 56 | UnwindData |  |
| 1247 | `?showmanyc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA_JXZ` | `0x26920` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `?sync@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAHXZ` | `0x269D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1300 | `?tie@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAPEAV?$basic_ostream@GU?$char_traits@G@std@@@2@PEAV32@@Z` | `0x269E0` | 50 | UnwindData |  |
| 1317 | `?uflow@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAGXZ` | `0x26DC0` | 124 | UnwindData |  |
| 1322 | `?underflow@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAGXZ` | `0x26F30` | 19 | UnwindData |  |
| 1342 | `?widen@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBAGD@Z` | `0x26F50` | 98 | UnwindData |  |
| 1357 | `?xsgetn@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA_JPEAG_J@Z` | `0x26FF0` | 307 | UnwindData |  |
| 1360 | `?xsputn@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA_JPEBG_J@Z` | `0x27160` | 334 | UnwindData |  |
| 31 | `??0?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@_N@Z` | `0x272B0` | 221 | UnwindData |  |
| 133 | `??1?$basic_istream@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x273E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `??_D?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x27430` | 49 | UnwindData |  |
| 114 | `??0_UShinit@std@@QEAA@XZ` | `0x275D0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `??1_UShinit@std@@QEAA@XZ` | `0x27750` | 106 | UnwindData |  |
| 590 | `?_Osfx@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x27820` | 193 | UnwindData |  |
| 882 | `?flush@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@XZ` | `0x278F0` | 199 | UnwindData |  |
| 1128 | `?pubsync@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAHXZ` | `0x279C0` | 47 | UnwindData |  |
| 1170 | `?rdbuf@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBAPEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@XZ` | `0x279F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1301 | `?tie@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBAPEAV?$basic_ostream@GU?$char_traits@G@std@@@2@XZ` | `0x27A00` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??0?$basic_ios@_WU?$char_traits@_W@std@@@std@@IEAA@XZ` | `0x27DA0` | 81 | UnwindData |  |
| 44 | `??0?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAA@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@_N@Z` | `0x27E00` | 208 | UnwindData |  |
| 54 | `??0?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAA@XZ` | `0x27ED0` | 262 | UnwindData |  |
| 128 | `??1?$basic_ios@_WU?$char_traits@_W@std@@@std@@UEAA@XZ` | `0x280C0` | 40 | UnwindData |  |
| 137 | `??1?$basic_ostream@_WU?$char_traits@_W@std@@@std@@UEAA@XZ` | `0x280F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `??1?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@UEAA@XZ` | `0x28140` | 82 | UnwindData |  |
| 376 | `??_D?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x281A0` | 49 | UnwindData |  |
| 493 | `?_Gnavail@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBA_JXZ` | `0x28400` | 56 | UnwindData |  |
| 496 | `?_Gndec@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAPEA_WXZ` | `0x28440` | 78 | UnwindData |  |
| 499 | `?_Gninc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAPEA_WXZ` | `0x28490` | 86 | UnwindData |  |
| 513 | `?_Init@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXPEAPEA_W0PEAH001@Z` | `0x28620` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `?_Init@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXXZ` | `0x28690` | 156 | UnwindData |  |
| 563 | `?_Lock@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@UEAAXXZ` | `0x287C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `?_Pnavail@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBA_JXZ` | `0x287D0` | 56 | UnwindData |  |
| 597 | `?_Pninc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAPEA_WXZ` | `0x28810` | 86 | UnwindData |  |
| 650 | `?_Unlock@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@UEAAXXZ` | `0x28980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `?clear@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXH_N@Z` | `0x28990` | 101 | UnwindData |  |
| 856 | `?eback@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBAPEA_WXZ` | `0x28A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 859 | `?egptr@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBAPEA_WXZ` | `0x28AB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `?epptr@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBAPEA_WXZ` | `0x28AF0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | `?gbump@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXH@Z` | `0x28B60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `?gptr@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBAPEA_WXZ` | `0x28BB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `?imbue@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAXAEBVlocale@2@@Z` | `0x28C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `?init@?$basic_ios@_WU?$char_traits@_W@std@@@std@@IEAAXPEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@2@_N@Z` | `0x28C10` | 133 | UnwindData |  |
| 1091 | `?overflow@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAGG@Z` | `0x28FF0` | 24 | UnwindData |  |
| 1094 | `?pbackfail@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAGG@Z` | `0x29190` | 24 | UnwindData |  |
| 1100 | `?pbump@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXH@Z` | `0x291B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `?pptr@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBAPEA_WXZ` | `0x29200` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `?seekoff@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA?AV?$fpos@U_Mbstatet@@@2@_JHH@Z` | `0x29320` | 51 | UnwindData |  |
| 1208 | `?seekpos@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA?AV?$fpos@U_Mbstatet@@@2@V32@H@Z` | `0x29430` | 51 | UnwindData |  |
| 1216 | `?setbuf@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAPEAV12@PEA_W_J@Z` | `0x29510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `?setg@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXPEA_W00@Z` | `0x29530` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1228 | `?setp@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXPEA_W0@Z` | `0x29590` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `?setstate@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXH_N@Z` | `0x295E0` | 56 | UnwindData |  |
| 1248 | `?showmanyc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA_JXZ` | `0x29620` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1288 | `?sync@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAHXZ` | `0x296D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `?tie@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAPEAV?$basic_ostream@_WU?$char_traits@_W@std@@@2@PEAV32@@Z` | `0x296E0` | 50 | UnwindData |  |
| 1318 | `?uflow@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAGXZ` | `0x29AC0` | 124 | UnwindData |  |
| 1323 | `?underflow@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAGXZ` | `0x29C30` | 19 | UnwindData |  |
| 1343 | `?widen@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEBA_WD@Z` | `0x29C50` | 98 | UnwindData |  |
| 1358 | `?xsgetn@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA_JPEA_W_J@Z` | `0x29CF0` | 307 | UnwindData |  |
| 1361 | `?xsputn@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA_JPEB_W_J@Z` | `0x29E60` | 334 | UnwindData |  |
| 35 | `??0?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@_N@Z` | `0x29FB0` | 221 | UnwindData |  |
| 134 | `??1?$basic_istream@_WU?$char_traits@_W@std@@@std@@UEAA@XZ` | `0x2A0E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `??_D?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x2A130` | 49 | UnwindData |  |
| 115 | `??0_Winit@std@@QEAA@XZ` | `0x2A2D0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `??1_Winit@std@@QEAA@XZ` | `0x2A450` | 106 | UnwindData |  |
| 591 | `?_Osfx@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x2A520` | 193 | UnwindData |  |
| 883 | `?flush@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@XZ` | `0x2A5F0` | 199 | UnwindData |  |
| 1129 | `?pubsync@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAHXZ` | `0x2A6C0` | 47 | UnwindData |  |
| 1172 | `?rdbuf@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEBAPEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@2@XZ` | `0x2A6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `?tie@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEBAPEAV?$basic_ostream@_WU?$char_traits@_W@std@@@2@XZ` | `0x2A700` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??$_Getvals@_W@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAAX_WAEBV_Locinfo@1@@Z` | `0x2E450` | 186 | UnwindData |  |
| 75 | `??0?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x35480` | 76 | UnwindData |  |
| 77 | `??0?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x354D0` | 76 | UnwindData |  |
| 81 | `??0?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x35520` | 76 | UnwindData |  |
| 83 | `??0?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x35570` | 76 | UnwindData |  |
| 89 | `??0?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x35680` | 76 | UnwindData |  |
| 92 | `??0?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x356D0` | 76 | UnwindData |  |
| 97 | `??0?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x35720` | 103 | UnwindData |  |
| 100 | `??0?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x35790` | 103 | UnwindData |  |
| 150 | `??1?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEAA@XZ` | `0x35E50` | 40 | UnwindData |  |
| 151 | `??1?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEAA@XZ` | `0x35E80` | 40 | UnwindData |  |
| 153 | `??1?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEAA@XZ` | `0x35EB0` | 40 | UnwindData |  |
| 154 | `??1?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEAA@XZ` | `0x35EE0` | 40 | UnwindData |  |
| 156 | `??1?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEAA@XZ` | `0x35F90` | 51 | UnwindData |  |
| 157 | `??1?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEAA@XZ` | `0x35FD0` | 51 | UnwindData |  |
| 159 | `??1?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEAA@XZ` | `0x36010` | 57 | UnwindData |  |
| 160 | `??1?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEAA@XZ` | `0x36050` | 57 | UnwindData |  |
| 433 | `?_Ffmt@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAPEADPEADDH@Z` | `0x382B0` | 367 | UnwindData |  |
| 434 | `?_Ffmt@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAPEADPEADDH@Z` | `0x38420` | 367 | UnwindData |  |
| 451 | `?_Getcat@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x39350` | 243 | UnwindData |  |
| 452 | `?_Getcat@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x39450` | 243 | UnwindData |  |
| 454 | `?_Getcat@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x39550` | 243 | UnwindData |  |
| 455 | `?_Getcat@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x39650` | 243 | UnwindData |  |
| 457 | `?_Getcat@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x39950` | 243 | UnwindData |  |
| 458 | `?_Getcat@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x39A50` | 243 | UnwindData |  |
| 460 | `?_Getcat@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x39B50` | 243 | UnwindData |  |
| 461 | `?_Getcat@?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x39C50` | 243 | UnwindData |  |
| 476 | `?_Getfmt@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@PEBD@Z` | `0x39D90` | 720 | UnwindData |  |
| 477 | `?_Getfmt@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@PEBD@Z` | `0x3A060` | 720 | UnwindData |  |
| 483 | `?_Getint@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@0HHAEAHAEBV?$ctype@G@2@@Z` | `0x3A330` | 93 | UnwindData |  |
| 484 | `?_Getint@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@0HHAEAHAEBV?$ctype@_W@2@@Z` | `0x3A390` | 93 | UnwindData |  |
| 505 | `?_Ifmt@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAPEADPEADPEBDH@Z` | `0x3C770` | 390 | UnwindData |  |
| 506 | `?_Ifmt@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAPEADPEADPEBDH@Z` | `0x3C900` | 390 | UnwindData |  |
| 524 | `?_Init@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3D380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `?_Init@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3D390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `?_Init@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3D3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `?_Init@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3D3B0` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `?_Init@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3D750` | 123 | UnwindData |  |
| 531 | `?_Init@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3D7D0` | 123 | UnwindData |  |
| 533 | `?_Init@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3D850` | 83 | UnwindData |  |
| 534 | `?_Init@?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3D8B0` | 83 | UnwindData |  |
| 550 | `?_Iput@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEAD_K@Z` | `0x3D910` | 1,854 | UnwindData |  |
| 551 | `?_Iput@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEAD_K@Z` | `0x3E050` | 1,854 | UnwindData |  |
| 580 | `?_Makeushloc@_Locimp@locale@std@@CAXAEBV_Locinfo@3@HPEAV123@PEBV23@@Z` | `0x3E7C0` | 3,768 | UnwindData |  |
| 581 | `?_Makewloc@_Locimp@locale@std@@CAXAEBV_Locinfo@3@HPEAV123@PEBV23@@Z` | `0x3F680` | 3,768 | UnwindData |  |
| 611 | `?_Put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@PEBG_K@Z` | `0x40B10` | 141 | UnwindData |  |
| 612 | `?_Put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@PEB_W_K@Z` | `0x40BA0` | 141 | UnwindData |  |
| 617 | `?_Rep@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@G_K@Z` | `0x43130` | 116 | UnwindData |  |
| 618 | `?_Rep@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@_W_K@Z` | `0x431B0` | 116 | UnwindData |  |
| 645 | `?_Tidy@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEAAXXZ` | `0x43810` | 60 | UnwindData |  |
| 646 | `?_Tidy@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEAAXXZ` | `0x43850` | 60 | UnwindData |  |
| 703 | `?date_order@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AW4dateorder@time_base@2@XZ` | `0x443C0` | 47 | UnwindData |  |
| 704 | `?date_order@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AW4dateorder@time_base@2@XZ` | `0x443F0` | 47 | UnwindData |  |
| 712 | `?do_date_order@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AW4dateorder@time_base@2@XZ` | `0x44740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | `?do_date_order@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AW4dateorder@time_base@2@XZ` | `0x44750` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x45000` | 611 | UnwindData |  |
| 731 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x45270` | 212 | UnwindData |  |
| 732 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x45350` | 442 | UnwindData |  |
| 733 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x45510` | 442 | UnwindData |  |
| 734 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x456D0` | 420 | UnwindData |  |
| 735 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x45880` | 420 | UnwindData |  |
| 736 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x45A30` | 216 | UnwindData |  |
| 737 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x45B10` | 448 | UnwindData |  |
| 738 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x45CD0` | 444 | UnwindData |  |
| 739 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x45E90` | 444 | UnwindData |  |
| 740 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x46050` | 976 | UnwindData |  |
| 741 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x46420` | 611 | UnwindData |  |
| 742 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x46690` | 212 | UnwindData |  |
| 743 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x46770` | 442 | UnwindData |  |
| 744 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x46930` | 442 | UnwindData |  |
| 745 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x46AF0` | 420 | UnwindData |  |
| 746 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x46CA0` | 420 | UnwindData |  |
| 747 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x46E50` | 216 | UnwindData |  |
| 748 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x46F30` | 448 | UnwindData |  |
| 749 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x470F0` | 444 | UnwindData |  |
| 750 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x472B0` | 444 | UnwindData |  |
| 751 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x47470` | 976 | UnwindData |  |
| 753 | `?do_get@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@DD@Z` | `0x47840` | 3,905 | UnwindData |  |
| 754 | `?do_get@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@DD@Z` | `0x48790` | 3,905 | UnwindData |  |
| 756 | `?do_get_date@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x496E0` | 2,660 | UnwindData |  |
| 757 | `?do_get_date@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4A150` | 2,660 | UnwindData |  |
| 759 | `?do_get_monthname@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4ABC0` | 140 | UnwindData |  |
| 760 | `?do_get_monthname@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4AC50` | 140 | UnwindData |  |
| 762 | `?do_get_time@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4ACE0` | 670 | UnwindData |  |
| 763 | `?do_get_time@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4AF80` | 670 | UnwindData |  |
| 765 | `?do_get_weekday@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4B220` | 140 | UnwindData |  |
| 766 | `?do_get_weekday@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4B2B0` | 140 | UnwindData |  |
| 768 | `?do_get_year@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4B340` | 316 | UnwindData |  |
| 769 | `?do_get_year@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4B480` | 316 | UnwindData |  |
| 808 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GJ@Z` | `0x4C5C0` | 284 | UnwindData |  |
| 809 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GK@Z` | `0x4C6E0` | 284 | UnwindData |  |
| 810 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GN@Z` | `0x4C800` | 817 | UnwindData |  |
| 811 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GO@Z` | `0x4CB40` | 816 | UnwindData |  |
| 812 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBX@Z` | `0x4CE70` | 245 | UnwindData |  |
| 813 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_J@Z` | `0x4CF70` | 284 | UnwindData |  |
| 814 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_K@Z` | `0x4D090` | 284 | UnwindData |  |
| 815 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_N@Z` | `0x4D1B0` | 1,002 | UnwindData |  |
| 816 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WJ@Z` | `0x4D5A0` | 284 | UnwindData |  |
| 817 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WK@Z` | `0x4D6C0` | 284 | UnwindData |  |
| 818 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WN@Z` | `0x4D7E0` | 817 | UnwindData |  |
| 819 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WO@Z` | `0x4DB20` | 816 | UnwindData |  |
| 820 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEBX@Z` | `0x4DE50` | 245 | UnwindData |  |
| 821 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_W_J@Z` | `0x4DF50` | 284 | UnwindData |  |
| 822 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_W_K@Z` | `0x4E070` | 284 | UnwindData |  |
| 823 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_W_N@Z` | `0x4E190` | 1,002 | UnwindData |  |
| 825 | `?do_put@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBUtm@@DD@Z` | `0x4E580` | 667 | UnwindData |  |
| 826 | `?do_put@?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEBUtm@@DD@Z` | `0x4E820` | 667 | UnwindData |  |
| 951 | `?get_monthname@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4F270` | 193 | UnwindData |  |
| 952 | `?get_monthname@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4F340` | 193 | UnwindData |  |
| 958 | `?get_weekday@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4F410` | 193 | UnwindData |  |
| 959 | `?get_weekday@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4F4E0` | 193 | UnwindData |  |
| 961 | `?get_year@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4F5B0` | 193 | UnwindData |  |
| 962 | `?get_year@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4F680` | 193 | UnwindData |  |
| 1183 | `?sbumpc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x50310` | 97 | UnwindData |  |
| 1184 | `?sbumpc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAGXZ` | `0x50380` | 97 | UnwindData |  |
| 1241 | `?sgetc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x50410` | 97 | UnwindData |  |
| 1242 | `?sgetc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAGXZ` | `0x50480` | 97 | UnwindData |  |
| 1256 | `?sputc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGG@Z` | `0x50510` | 142 | UnwindData |  |
| 1257 | `?sputc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAG_W@Z` | `0x505A0` | 142 | UnwindData |  |
| 583 | `?_Mtx_delete@threads@stdext@@YAXPEAX@Z` | `0x50B80` | 52 | UnwindData |  |
| 584 | `?_Mtx_lock@threads@stdext@@YAXPEAX@Z` | `0x50BC0` | 26 | UnwindData |  |
| 585 | `?_Mtx_new@threads@stdext@@YAXAEAPEAX@Z` | `0x50BE0` | 65 | UnwindData |  |
| 586 | `?_Mtx_unlock@threads@stdext@@YAXPEAX@Z` | `0x50C30` | 26 | UnwindData |  |
| 1376 | `_Cosh` | `0x50C70` | 295 | UnwindData |  |
| 1383 | `_FCosh` | `0x50DA0` | 298 | UnwindData |  |
| 1401 | `_LCosh` | `0x50ED0` | 38 | UnwindData |  |
| 1395 | `_Getdateorder` | `0x50F00` | 160 | UnwindData |  |
| 1380 | `_Dtest` | `0x50FA0` | 28 | UnwindData |  |
| 1385 | `_FDtest` | `0x50FC0` | 28 | UnwindData |  |
| 1403 | `_LDtest` | `0x50FE0` | 24 | UnwindData |  |
| 1382 | `_Exp` | `0x52330` | 858 | UnwindData |  |
| 1386 | `_FExp` | `0x52690` | 729 | UnwindData |  |
| 1404 | `_LExp` | `0x52970` | 48 | UnwindData |  |
| 1396 | `_Getwctype` | `0x529A0` | 74 | UnwindData |  |
| 1397 | `_Getwctypes` | `0x529F0` | 77 | UnwindData |  |
| 657 | `?_XLgamma@std@@YAMM@Z` | `0x52A40` | 26 | UnwindData |  |
| 658 | `?_XLgamma@std@@YANN@Z` | `0x52A60` | 27 | UnwindData |  |
| 659 | `?_XLgamma@std@@YAOO@Z` | `0x52A80` | 26 | UnwindData |  |
| 86 | `??0?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x54010` | 76 | UnwindData |  |
| 94 | `??0?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x54060` | 103 | UnwindData |  |
| 155 | `??1?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEAA@XZ` | `0x542E0` | 51 | UnwindData |  |
| 158 | `??1?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEAA@XZ` | `0x54320` | 57 | UnwindData |  |
| 456 | `?_Getcat@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x551C0` | 243 | UnwindData |  |
| 459 | `?_Getcat@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x552C0` | 243 | UnwindData |  |
| 475 | `?_Getfmt@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@PEBD@Z` | `0x553C0` | 720 | UnwindData |  |
| 482 | `?_Getint@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@0HHAEAHAEBV?$ctype@D@2@@Z` | `0x55690` | 93 | UnwindData |  |
| 529 | `?_Init@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x56CD0` | 123 | UnwindData |  |
| 532 | `?_Init@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x56D50` | 83 | UnwindData |  |
| 582 | `?_Makexloc@_Locimp@locale@std@@CAXAEBV_Locinfo@3@HPEAV123@PEBV23@@Z` | `0x56DB0` | 2,288 | UnwindData |  |
| 644 | `?_Tidy@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEAAXXZ` | `0x58AA0` | 60 | UnwindData |  |
| 702 | `?date_order@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AW4dateorder@time_base@2@XZ` | `0x58D70` | 47 | UnwindData |  |
| 711 | `?do_date_order@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AW4dateorder@time_base@2@XZ` | `0x58EC0` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | `?do_get@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@DD@Z` | `0x592D0` | 3,905 | UnwindData |  |
| 755 | `?do_get_date@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5A220` | 2,660 | UnwindData |  |
| 758 | `?do_get_monthname@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5AC90` | 140 | UnwindData |  |
| 761 | `?do_get_time@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5AD20` | 670 | UnwindData |  |
| 764 | `?do_get_weekday@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5AFC0` | 140 | UnwindData |  |
| 767 | `?do_get_year@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5B050` | 316 | UnwindData |  |
| 824 | `?do_put@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBUtm@@DD@Z` | `0x5B940` | 661 | UnwindData |  |
| 950 | `?get_monthname@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5BDF0` | 193 | UnwindData |  |
| 957 | `?get_weekday@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5BEC0` | 193 | UnwindData |  |
| 960 | `?get_year@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5BF90` | 193 | UnwindData |  |
| 105 | `??0_Init_locks@std@@QEAA@XZ` | `0x5C250` | 132 | UnwindData |  |
| 110 | `??0_Lockit@std@@QEAA@H@Z` | `0x5C2E0` | 97 | UnwindData |  |
| 111 | `??0_Lockit@std@@QEAA@XZ` | `0x5C350` | 80 | UnwindData |  |
| 163 | `??1_Init_locks@std@@QEAA@XZ` | `0x5C3A0` | 127 | UnwindData |  |
| 166 | `??1_Lockit@std@@QEAA@XZ` | `0x5C420` | 77 | UnwindData |  |
| 543 | `?_Init_locks_ctor@_Init_locks@std@@CAXPEAV12@@Z` | `0x5C470` | 127 | UnwindData |  |
| 544 | `?_Init_locks_dtor@_Init_locks@std@@CAXPEAV12@@Z` | `0x5C4F0` | 127 | UnwindData |  |
| 564 | `?_Lockit_ctor@_Lockit@std@@CAXPEAV12@@Z` | `0x5C570` | 45 | UnwindData |  |
| 565 | `?_Lockit_ctor@_Lockit@std@@CAXPEAV12@H@Z` | `0x5C5A0` | 82 | UnwindData |  |
| 566 | `?_Lockit_ctor@_Lockit@std@@SAXH@Z` | `0x5C600` | 64 | UnwindData |  |
| 567 | `?_Lockit_dtor@_Lockit@std@@CAXPEAV12@@Z` | `0x5C640` | 48 | UnwindData |  |
| 568 | `?_Lockit_dtor@_Lockit@std@@SAXH@Z` | `0x5C670` | 64 | UnwindData |  |
| 1414 | `_Mbrtowc` | `0x5C700` | 862 | UnwindData |  |
| 1427 | `_Mtxdst` | `0x5CB00` | 26 | UnwindData |  |
| 1428 | `_Mtxinit` | `0x5CB20` | 34 | UnwindData |  |
| 1429 | `_Mtxlock` | `0x5CB50` | 26 | UnwindData |  |
| 1430 | `_Mtxunlock` | `0x5CB70` | 26 | UnwindData |  |
| 431 | `?_Execute_once@std@@YAHAEAUonce_flag@1@P6AHPEAX1PEAPEAX@Z1@Z` | `0x5CD60` | 51 | UnwindData |  |
| 656 | `?_XGetLastError@std@@YAXXZ` | `0x5CDA0` | 116 | UnwindData |  |
| 623 | `?_Rng_abort@std@@YAXPEBD@Z` | `0x5CF90` | 71 | UnwindData |  |
| 614 | `?_Random_device@std@@YAIXZ` | `0x5CFE0` | 41 | UnwindData |  |
| 1389 | `_FSinh` | `0x5D100` | 738 | UnwindData |  |
| 1407 | `_LSinh` | `0x5D3F0` | 38 | UnwindData |  |
| 1440 | `_Sinh` | `0x5D420` | 865 | UnwindData |  |
| 1444 | `_Stod` | `0x5D790` | 47 | UnwindData |  |
| 1445 | `_Stodx` | `0x5D7C0` | 163 | UnwindData |  |
| 1448 | `_Stold` | `0x5D870` | 47 | UnwindData |  |
| 1449 | `_Stoldx` | `0x5D8A0` | 54 | UnwindData |  |
| 1446 | `_Stof` | `0x5D8E0` | 47 | UnwindData |  |
| 1447 | `_Stofx` | `0x5D910` | 164 | UnwindData |  |
| 1452 | `_Stolx` | `0x5D9C0` | 377 | UnwindData |  |
| 1450 | `_Stoll` | `0x5DB40` | 47 | UnwindData |  |
| 1451 | `_Stollx` | `0x5DB70` | 413 | UnwindData |  |
| 1453 | `_Stoul` | `0x5DD10` | 47 | UnwindData |  |
| 1456 | `_Stoulx` | `0x5DD40` | 925 | UnwindData |  |
| 1454 | `_Stoull` | `0x5E0E0` | 47 | UnwindData |  |
| 1455 | `_Stoullx` | `0x5E110` | 966 | UnwindData |  |
| 1392 | `_Getcoll` | `0x5E4E0` | 114 | UnwindData |  |
| 1457 | `_Strcoll` | `0x5E560` | 418 | UnwindData |  |
| 1458 | `_Strxfrm` | `0x5E710` | 402 | UnwindData |  |
| 660 | `?_Xbad_alloc@std@@YAXXZ` | `0x5EF90` | 37 | UnwindData |  |
| 661 | `?_Xbad_function_call@std@@YAXXZ` | `0x5EFC0` | 37 | UnwindData |  |
| 662 | `?_Xinvalid_argument@std@@YAXPEBD@Z` | `0x5EFF0` | 47 | UnwindData |  |
| 663 | `?_Xlength_error@std@@YAXPEBD@Z` | `0x5F020` | 47 | UnwindData |  |
| 664 | `?_Xout_of_range@std@@YAXPEBD@Z` | `0x5F050` | 47 | UnwindData |  |
| 665 | `?_Xoverflow_error@std@@YAXPEBD@Z` | `0x5F080` | 47 | UnwindData |  |
| 666 | `?_Xregex_error@std@@YAXW4error_type@regex_constants@1@@Z` | `0x5F0B0` | 45 | UnwindData |  |
| 667 | `?_Xruntime_error@std@@YAXPEBD@Z` | `0x5F0E0` | 47 | UnwindData |  |
| 1478 | `_Towlower` | `0x5F120` | 167 | UnwindData |  |
| 1479 | `_Towupper` | `0x5F1D0` | 167 | UnwindData |  |
| 1489 | `_Wcscoll` | `0x5F280` | 380 | UnwindData |  |
| 1490 | `_Wcsxfrm` | `0x5F8B0` | 499 | UnwindData |  |
| 1394 | `_Getcvt` | `0x5FAB0` | 263 | UnwindData |  |
| 1488 | `_Wcrtomb` | `0x5FBC0` | 366 | UnwindData |  |
| 1494 | `__Wcrtomb_lk` | `0x5FD30` | 54 | UnwindData |  |
| 1482 | `_WStod` | `0x5FD70` | 47 | UnwindData |  |
| 1483 | `_WStodx` | `0x5FDA0` | 163 | UnwindData |  |
| 1486 | `_WStold` | `0x5FE50` | 47 | UnwindData |  |
| 1487 | `_WStoldx` | `0x5FE80` | 54 | UnwindData |  |
| 1484 | `_WStof` | `0x5FEC0` | 47 | UnwindData |  |
| 1485 | `_WStofx` | `0x5FEF0` | 164 | UnwindData |  |
| 1495 | `__crtCloseThreadpoolTimer` | `0x5FFE0` | 26 | UnwindData |  |
| 1496 | `__crtCloseThreadpoolWait` | `0x60000` | 26 | UnwindData |  |
| 1500 | `__crtCreateEventExW` | `0x60020` | 55 | UnwindData |  |
| 1501 | `__crtCreateSemaphoreExW` | `0x60060` | 69 | UnwindData |  |
| 1502 | `__crtCreateSymbolicLinkW` | `0x600B0` | 45 | UnwindData |  |
| 1503 | `__crtCreateThreadpoolTimer` | `0x600E0` | 45 | UnwindData |  |
| 1504 | `__crtCreateThreadpoolWait` | `0x60110` | 45 | UnwindData |  |
| 1505 | `__crtFlushProcessWriteBuffers` | `0x60140` | 16 | UnwindData |  |
| 1506 | `__crtFreeLibraryWhenCallbackReturns` | `0x60150` | 36 | UnwindData |  |
| 1507 | `__crtGetCurrentProcessorNumber` | `0x60180` | 15 | UnwindData |  |
| 1508 | `__crtGetFileInformationByHandleEx` | `0x60190` | 53 | UnwindData |  |
| 1510 | `__crtGetSystemTimePreciseAsFileTime` | `0x601D0` | 26 | UnwindData |  |
| 1511 | `__crtGetTickCount64` | `0x60250` | 15 | UnwindData |  |
| 1512 | `__crtInitOnceExecuteOnce` | `0x60260` | 55 | UnwindData |  |
| 1513 | `__crtInitializeCriticalSectionEx` | `0x602A0` | 43 | UnwindData |  |
| 1514 | `__crtIsPackagedApp` | `0x602D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1518 | `__crtSetFileInformationByHandle` | `0x602E0` | 53 | UnwindData |  |
| 1519 | `__crtSetThreadpoolTimer` | `0x60320` | 56 | UnwindData |  |
| 1520 | `__crtSetThreadpoolWait` | `0x60360` | 46 | UnwindData |  |
| 1521 | `__crtWaitForThreadpoolTimerCallbacks` | `0x60390` | 34 | UnwindData |  |
| 1 | `??$_Getvals@_W@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAX_WAEBV_Locinfo@1@@Z` | `0x65A80` | 186 | UnwindData |  |
| 2 | `??$_Getvals@_W@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAX_WAEBV_Locinfo@1@@Z` | `0x65B40` | 186 | UnwindData |  |
| 4 | `??0?$_Yarn@D@std@@QEAA@AEBV01@@Z` | `0x65F30` | 61 | UnwindData |  |
| 7 | `??0?$_Yarn@G@std@@QEAA@AEBV01@@Z` | `0x65F70` | 63 | UnwindData |  |
| 8 | `??0?$_Yarn@G@std@@QEAA@PEBG@Z` | `0x65FB0` | 63 | UnwindData |  |
| 9 | `??0?$_Yarn@G@std@@QEAA@XZ` | `0x65FF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0?$_Yarn@_W@std@@QEAA@AEBV01@@Z` | `0x66020` | 63 | UnwindData |  |
| 11 | `??0?$_Yarn@_W@std@@QEAA@PEB_W@Z` | `0x66060` | 63 | UnwindData |  |
| 14 | `??0?$basic_ios@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@@Z` | `0x660A0` | 104 | UnwindData |  |
| 16 | `??0?$basic_ios@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@@Z` | `0x66110` | 106 | UnwindData |  |
| 18 | `??0?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAA@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@@Z` | `0x66180` | 106 | UnwindData |  |
| 19 | `??0?$basic_iostream@DU?$char_traits@D@std@@@std@@IEAA@$$QEAV01@@Z` | `0x661F0` | 361 | UnwindData |  |
| 20 | `??0?$basic_iostream@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@@Z` | `0x66360` | 223 | UnwindData |  |
| 21 | `??0?$basic_iostream@GU?$char_traits@G@std@@@std@@IEAA@$$QEAV01@@Z` | `0x66440` | 361 | UnwindData |  |
| 22 | `??0?$basic_iostream@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@@Z` | `0x665B0` | 223 | UnwindData |  |
| 23 | `??0?$basic_iostream@_WU?$char_traits@_W@std@@@std@@IEAA@$$QEAV01@@Z` | `0x66690` | 361 | UnwindData |  |
| 24 | `??0?$basic_iostream@_WU?$char_traits@_W@std@@@std@@QEAA@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@@Z` | `0x66800` | 223 | UnwindData |  |
| 25 | `??0?$basic_istream@DU?$char_traits@D@std@@@std@@IEAA@$$QEAV01@@Z` | `0x668E0` | 291 | UnwindData |  |
| 26 | `??0?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@_N1@Z` | `0x66A10` | 230 | UnwindData |  |
| 28 | `??0?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA@W4_Uninitialized@1@@Z` | `0x66B00` | 223 | UnwindData |  |
| 29 | `??0?$basic_istream@GU?$char_traits@G@std@@@std@@IEAA@$$QEAV01@@Z` | `0x66BE0` | 291 | UnwindData |  |
| 30 | `??0?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@_N1@Z` | `0x66D10` | 230 | UnwindData |  |
| 32 | `??0?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA@W4_Uninitialized@1@@Z` | `0x66E00` | 223 | UnwindData |  |
| 33 | `??0?$basic_istream@_WU?$char_traits@_W@std@@@std@@IEAA@$$QEAV01@@Z` | `0x66EE0` | 291 | UnwindData |  |
| 34 | `??0?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@_N1@Z` | `0x67010` | 230 | UnwindData |  |
| 36 | `??0?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA@W4_Uninitialized@1@@Z` | `0x67100` | 223 | UnwindData |  |
| 37 | `??0?$basic_ostream@DU?$char_traits@D@std@@@std@@IEAA@$$QEAV01@@Z` | `0x671E0` | 261 | UnwindData |  |
| 39 | `??0?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA@W4_Uninitialized@1@_N@Z` | `0x672F0` | 224 | UnwindData |  |
| 40 | `??0?$basic_ostream@GU?$char_traits@G@std@@@std@@IEAA@$$QEAV01@@Z` | `0x673D0` | 261 | UnwindData |  |
| 42 | `??0?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA@W4_Uninitialized@1@_N@Z` | `0x674E0` | 224 | UnwindData |  |
| 43 | `??0?$basic_ostream@_WU?$char_traits@_W@std@@@std@@IEAA@$$QEAV01@@Z` | `0x675C0` | 261 | UnwindData |  |
| 45 | `??0?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAA@W4_Uninitialized@1@_N@Z` | `0x676D0` | 224 | UnwindData |  |
| 46 | `??0?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAA@AEBV01@@Z` | `0x677B0` | 412 | UnwindData |  |
| 47 | `??0?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAA@W4_Uninitialized@1@@Z` | `0x67950` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??0?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAA@AEBV01@@Z` | `0x67A20` | 412 | UnwindData |  |
| 50 | `??0?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAA@W4_Uninitialized@1@@Z` | `0x67BC0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??0?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAA@AEBV01@@Z` | `0x67C90` | 412 | UnwindData |  |
| 53 | `??0?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAA@W4_Uninitialized@1@@Z` | `0x67E30` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??0?$codecvt@DDU_Mbstatet@@@std@@QEAA@_K@Z` | `0x67F00` | 135 | UnwindData |  |
| 74 | `??0?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x681A0` | 121 | UnwindData |  |
| 76 | `??0?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x68220` | 121 | UnwindData |  |
| 78 | `??0?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@_K@Z` | `0x682A0` | 121 | UnwindData |  |
| 80 | `??0?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x68320` | 121 | UnwindData |  |
| 82 | `??0?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x683A0` | 121 | UnwindData |  |
| 84 | `??0?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@_K@Z` | `0x68420` | 121 | UnwindData |  |
| 85 | `??0?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAA@PEBD_K@Z` | `0x68530` | 127 | UnwindData |  |
| 87 | `??0?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x685B0` | 121 | UnwindData |  |
| 88 | `??0?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAA@PEBD_K@Z` | `0x68630` | 127 | UnwindData |  |
| 90 | `??0?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x686B0` | 121 | UnwindData |  |
| 91 | `??0?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAA@PEBD_K@Z` | `0x68730` | 127 | UnwindData |  |
| 93 | `??0?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@_K@Z` | `0x687B0` | 121 | UnwindData |  |
| 95 | `??0?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x68830` | 151 | UnwindData |  |
| 96 | `??0?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAA@PEBD_K@Z` | `0x688D0` | 157 | UnwindData |  |
| 98 | `??0?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x68970` | 151 | UnwindData |  |
| 99 | `??0?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAA@PEBD_K@Z` | `0x68A10` | 157 | UnwindData |  |
| 101 | `??0?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@_K@Z` | `0x68AB0` | 151 | UnwindData |  |
| 124 | `??1?$_Yarn@G@std@@QEAA@XZ` | `0x68E70` | 25 | UnwindData |  |
| 129 | `??1?$basic_iostream@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x68E90` | 114 | UnwindData |  |
| 130 | `??1?$basic_iostream@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x68F10` | 114 | UnwindData |  |
| 131 | `??1?$basic_iostream@_WU?$char_traits@_W@std@@@std@@UEAA@XZ` | `0x68F90` | 114 | UnwindData |  |
| 183 | `??4?$_Yarn@D@std@@QEAAAEAV01@AEBV01@@Z` | `0x691C0` | 37 | UnwindData |  |
| 185 | `??4?$_Yarn@G@std@@QEAAAEAV01@AEBV01@@Z` | `0x691F0` | 37 | UnwindData |  |
| 186 | `??4?$_Yarn@G@std@@QEAAAEAV01@PEBG@Z` | `0x69220` | 76 | UnwindData |  |
| 187 | `??4?$_Yarn@_W@std@@QEAAAEAV01@AEBV01@@Z` | `0x69270` | 37 | UnwindData |  |
| 189 | `??4?$basic_iostream@DU?$char_traits@D@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x692A0` | 39 | UnwindData |  |
| 190 | `??4?$basic_iostream@GU?$char_traits@G@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x692D0` | 39 | UnwindData |  |
| 191 | `??4?$basic_iostream@_WU?$char_traits@_W@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x69300` | 39 | UnwindData |  |
| 192 | `??4?$basic_istream@DU?$char_traits@D@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x69330` | 39 | UnwindData |  |
| 193 | `??4?$basic_istream@GU?$char_traits@G@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x69360` | 39 | UnwindData |  |
| 194 | `??4?$basic_istream@_WU?$char_traits@_W@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x69390` | 39 | UnwindData |  |
| 195 | `??4?$basic_ostream@DU?$char_traits@D@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x693C0` | 39 | UnwindData |  |
| 196 | `??4?$basic_ostream@GU?$char_traits@G@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x693F0` | 39 | UnwindData |  |
| 197 | `??4?$basic_ostream@_WU?$char_traits@_W@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x69420` | 39 | UnwindData |  |
| 198 | `??4?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAAEAV01@AEBV01@@Z` | `0x69450` | 303 | UnwindData |  |
| 199 | `??4?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAAEAV01@AEBV01@@Z` | `0x69580` | 303 | UnwindData |  |
| 200 | `??4?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAAEAV01@AEBV01@@Z` | `0x696B0` | 303 | UnwindData |  |
| 209 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAF@Z` | `0x697E0` | 758 | UnwindData |  |
| 210 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAG@Z` | `0x69AE0` | 34 | UnwindData |  |
| 211 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAH@Z` | `0x69B10` | 61 | UnwindData |  |
| 212 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAI@Z` | `0x69B50` | 34 | UnwindData |  |
| 213 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAJ@Z` | `0x69B80` | 34 | UnwindData |  |
| 214 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAK@Z` | `0x69BB0` | 34 | UnwindData |  |
| 215 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAM@Z` | `0x69BE0` | 34 | UnwindData |  |
| 216 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAN@Z` | `0x69C10` | 34 | UnwindData |  |
| 217 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAO@Z` | `0x69C40` | 34 | UnwindData |  |
| 218 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAPEAX@Z` | `0x69C70` | 34 | UnwindData |  |
| 219 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEA_J@Z` | `0x69CA0` | 34 | UnwindData |  |
| 220 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEA_K@Z` | `0x69CD0` | 34 | UnwindData |  |
| 221 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEA_N@Z` | `0x69D00` | 34 | UnwindData |  |
| 222 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0x69D30` | 55 | UnwindData |  |
| 223 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@DU?$char_traits@D@std@@@1@AEAV21@@Z@Z` | `0x69D70` | 81 | UnwindData |  |
| 224 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0x69DD0` | 81 | UnwindData |  |
| 225 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@@Z` | `0x69E30` | 454 | UnwindData |  |
| 226 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAF@Z` | `0x6A000` | 758 | UnwindData |  |
| 227 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAG@Z` | `0x6A300` | 34 | UnwindData |  |
| 228 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAH@Z` | `0x6A330` | 61 | UnwindData |  |
| 229 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAI@Z` | `0x6A370` | 34 | UnwindData |  |
| 230 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAJ@Z` | `0x6A3A0` | 34 | UnwindData |  |
| 231 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAK@Z` | `0x6A3D0` | 34 | UnwindData |  |
| 232 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAM@Z` | `0x6A400` | 34 | UnwindData |  |
| 233 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAN@Z` | `0x6A430` | 34 | UnwindData |  |
| 234 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAO@Z` | `0x6A460` | 34 | UnwindData |  |
| 235 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAPEAX@Z` | `0x6A490` | 34 | UnwindData |  |
| 236 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEA_J@Z` | `0x6A4C0` | 34 | UnwindData |  |
| 237 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEA_K@Z` | `0x6A4F0` | 34 | UnwindData |  |
| 238 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEA_N@Z` | `0x6A520` | 34 | UnwindData |  |
| 239 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0x6A550` | 55 | UnwindData |  |
| 240 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@GU?$char_traits@G@std@@@1@AEAV21@@Z@Z` | `0x6A590` | 81 | UnwindData |  |
| 241 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0x6A5F0` | 81 | UnwindData |  |
| 242 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@@Z` | `0x6A650` | 430 | UnwindData |  |
| 243 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAF@Z` | `0x6A800` | 758 | UnwindData |  |
| 244 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAG@Z` | `0x6AB00` | 34 | UnwindData |  |
| 245 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAH@Z` | `0x6AB30` | 61 | UnwindData |  |
| 246 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAI@Z` | `0x6AB70` | 34 | UnwindData |  |
| 247 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAJ@Z` | `0x6ABA0` | 34 | UnwindData |  |
| 248 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAK@Z` | `0x6ABD0` | 34 | UnwindData |  |
| 249 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAM@Z` | `0x6AC00` | 34 | UnwindData |  |
| 250 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAN@Z` | `0x6AC30` | 34 | UnwindData |  |
| 251 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAO@Z` | `0x6AC60` | 34 | UnwindData |  |
| 252 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAPEAX@Z` | `0x6AC90` | 34 | UnwindData |  |
| 253 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEA_J@Z` | `0x6ACC0` | 34 | UnwindData |  |
| 254 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEA_K@Z` | `0x6ACF0` | 34 | UnwindData |  |
| 255 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEA_N@Z` | `0x6AD20` | 34 | UnwindData |  |
| 256 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0x6AD50` | 55 | UnwindData |  |
| 257 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@_WU?$char_traits@_W@std@@@1@AEAV21@@Z@Z` | `0x6AD90` | 81 | UnwindData |  |
| 258 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0x6ADF0` | 81 | UnwindData |  |
| 259 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@@Z` | `0x6AE50` | 430 | UnwindData |  |
| 260 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@F@Z` | `0x6B000` | 650 | UnwindData |  |
| 261 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@G@Z` | `0x6B290` | 556 | UnwindData |  |
| 262 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@H@Z` | `0x6B4C0` | 647 | UnwindData |  |
| 263 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@I@Z` | `0x6B750` | 554 | UnwindData |  |
| 264 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@J@Z` | `0x6B980` | 554 | UnwindData |  |
| 265 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@K@Z` | `0x6BBB0` | 554 | UnwindData |  |
| 266 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@M@Z` | `0x6BDE0` | 560 | UnwindData |  |
| 267 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@N@Z` | `0x6C010` | 560 | UnwindData |  |
| 268 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@O@Z` | `0x6C240` | 560 | UnwindData |  |
| 269 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0x6C470` | 55 | UnwindData |  |
| 270 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@DU?$char_traits@D@std@@@1@AEAV21@@Z@Z` | `0x6C4B0` | 81 | UnwindData |  |
| 271 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0x6C510` | 81 | UnwindData |  |
| 272 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@@Z` | `0x6C570` | 531 | UnwindData |  |
| 273 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@PEBX@Z` | `0x6C790` | 557 | UnwindData |  |
| 274 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@_J@Z` | `0x6C9C0` | 557 | UnwindData |  |
| 275 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@_K@Z` | `0x6CBF0` | 557 | UnwindData |  |
| 276 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@_N@Z` | `0x6CE20` | 555 | UnwindData |  |
| 277 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@F@Z` | `0x6D050` | 652 | UnwindData |  |
| 278 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@G@Z` | `0x6D2E0` | 558 | UnwindData |  |
| 279 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@H@Z` | `0x6D510` | 649 | UnwindData |  |
| 280 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@I@Z` | `0x6D7A0` | 556 | UnwindData |  |
| 281 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@J@Z` | `0x6D9D0` | 556 | UnwindData |  |
| 282 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@K@Z` | `0x6DC00` | 556 | UnwindData |  |
| 283 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@M@Z` | `0x6DE30` | 562 | UnwindData |  |
| 284 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@N@Z` | `0x6E070` | 562 | UnwindData |  |
| 285 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@O@Z` | `0x6E2B0` | 562 | UnwindData |  |
| 286 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0x6E4F0` | 55 | UnwindData |  |
| 287 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@GU?$char_traits@G@std@@@1@AEAV21@@Z@Z` | `0x6E530` | 81 | UnwindData |  |
| 288 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0x6E590` | 81 | UnwindData |  |
| 289 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@@Z` | `0x6E5F0` | 552 | UnwindData |  |
| 290 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@PEBX@Z` | `0x6E820` | 559 | UnwindData |  |
| 291 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@_J@Z` | `0x6EA50` | 559 | UnwindData |  |
| 292 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@_K@Z` | `0x6EC80` | 559 | UnwindData |  |
| 293 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@_N@Z` | `0x6EEB0` | 557 | UnwindData |  |
| 294 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@F@Z` | `0x6F0E0` | 652 | UnwindData |  |
| 295 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@G@Z` | `0x6F370` | 558 | UnwindData |  |
| 296 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@H@Z` | `0x6F5A0` | 649 | UnwindData |  |
| 297 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@I@Z` | `0x6F830` | 556 | UnwindData |  |
| 298 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@J@Z` | `0x6FA60` | 556 | UnwindData |  |
| 299 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@K@Z` | `0x6FC90` | 556 | UnwindData |  |
| 300 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@M@Z` | `0x6FEC0` | 562 | UnwindData |  |
| 301 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@N@Z` | `0x70100` | 562 | UnwindData |  |
| 302 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@O@Z` | `0x70340` | 562 | UnwindData |  |
| 303 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0x70580` | 55 | UnwindData |  |
| 304 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@_WU?$char_traits@_W@std@@@1@AEAV21@@Z@Z` | `0x705C0` | 81 | UnwindData |  |
| 305 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0x70620` | 81 | UnwindData |  |
| 306 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@@Z` | `0x70680` | 552 | UnwindData |  |
| 307 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@PEBX@Z` | `0x708B0` | 559 | UnwindData |  |
| 308 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@_J@Z` | `0x70AE0` | 559 | UnwindData |  |
| 309 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@_K@Z` | `0x70D10` | 559 | UnwindData |  |
| 310 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@_N@Z` | `0x70F40` | 557 | UnwindData |  |
| 368 | `??_D?$basic_iostream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x711A0` | 49 | UnwindData |  |
| 369 | `??_D?$basic_iostream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x711E0` | 49 | UnwindData |  |
| 370 | `??_D?$basic_iostream@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x71220` | 49 | UnwindData |  |
| 377 | `??_F?$codecvt@DDU_Mbstatet@@@std@@QEAAXXZ` | `0x726D0` | 27 | UnwindData |  |
| 385 | `??_F?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x726F0` | 27 | UnwindData |  |
| 386 | `??_F?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x72710` | 27 | UnwindData |  |
| 387 | `??_F?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAAXXZ` | `0x72730` | 27 | UnwindData |  |
| 388 | `??_F?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x72750` | 27 | UnwindData |  |
| 389 | `??_F?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x72770` | 27 | UnwindData |  |
| 390 | `??_F?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAAXXZ` | `0x72790` | 27 | UnwindData |  |
| 391 | `??_F?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x727B0` | 27 | UnwindData |  |
| 392 | `??_F?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x727D0` | 27 | UnwindData |  |
| 393 | `??_F?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAAXXZ` | `0x727F0` | 27 | UnwindData |  |
| 394 | `??_F?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x72810` | 27 | UnwindData |  |
| 395 | `??_F?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x72830` | 27 | UnwindData |  |
| 396 | `??_F?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAAXXZ` | `0x72850` | 27 | UnwindData |  |
| 415 | `?_C_str@?$_Yarn@G@std@@QEBAPEBGXZ` | `0x72870` | 56 | UnwindData |  |
| 429 | `?_Empty@?$_Yarn@G@std@@QEBA_NXZ` | `0x728B0` | 45 | UnwindData |  |
| 439 | `?_Fput@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBD_K@Z` | `0x728E0` | 132 | UnwindData |  |
| 440 | `?_Fput@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBD_K@Z` | `0x72970` | 133 | UnwindData |  |
| 441 | `?_Fput@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEBD_K@Z` | `0x72A00` | 133 | UnwindData |  |
| 469 | `?_Getffld@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@1AEAVios_base@2@PEAH@Z` | `0x72A90` | 255 | UnwindData |  |
| 470 | `?_Getffld@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@1AEAVios_base@2@PEAH@Z` | `0x72B90` | 255 | UnwindData |  |
| 471 | `?_Getffld@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@1AEAVios_base@2@PEAH@Z` | `0x72C90` | 255 | UnwindData |  |
| 472 | `?_Getffldx@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@1AEAVios_base@2@PEAH@Z` | `0x72D90` | 255 | UnwindData |  |
| 473 | `?_Getffldx@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@1AEAVios_base@2@PEAH@Z` | `0x72E90` | 255 | UnwindData |  |
| 474 | `?_Getffldx@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@1AEAVios_base@2@PEAH@Z` | `0x72F90` | 255 | UnwindData |  |
| 479 | `?_Getifld@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@1HAEBVlocale@2@@Z` | `0x73090` | 158 | UnwindData |  |
| 480 | `?_Getifld@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@1HAEBVlocale@2@@Z` | `0x73130` | 158 | UnwindData |  |
| 481 | `?_Getifld@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@1HAEBVlocale@2@@Z` | `0x731D0` | 158 | UnwindData |  |
| 500 | `?_Gnpreinc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAPEADXZ` | `0x73270` | 77 | UnwindData |  |
| 501 | `?_Gnpreinc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAPEAGXZ` | `0x732C0` | 78 | UnwindData |  |
| 502 | `?_Gnpreinc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAPEA_WXZ` | `0x73310` | 78 | UnwindData |  |
| 546 | `?_Ipfx@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA_N_N@Z` | `0x73360` | 643 | UnwindData |  |
| 547 | `?_Ipfx@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA_N_N@Z` | `0x735F0` | 652 | UnwindData |  |
| 548 | `?_Ipfx@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA_N_N@Z` | `0x73880` | 652 | UnwindData |  |
| 641 | `?_Tidy@?$_Yarn@G@std@@AEAAXXZ` | `0x74140` | 57 | UnwindData |  |
| 681 | `?c_str@?$_Yarn@G@std@@QEBAPEBGXZ` | `0x74180` | 56 | UnwindData |  |
| 682 | `?c_str@?$_Yarn@_W@std@@QEBAPEB_WXZ` | `0x741C0` | 56 | UnwindData |  |
| 688 | `?clear@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXI@Z` | `0x74200` | 36 | UnwindData |  |
| 690 | `?clear@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXI@Z` | `0x74230` | 36 | UnwindData |  |
| 692 | `?clear@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXI@Z` | `0x74260` | 36 | UnwindData |  |
| 697 | `?copyfmt@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAAEAV12@AEBV12@@Z` | `0x74290` | 76 | UnwindData |  |
| 698 | `?copyfmt@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAAEAV12@AEBV12@@Z` | `0x742E0` | 77 | UnwindData |  |
| 699 | `?copyfmt@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@AEBV12@@Z` | `0x74330` | 77 | UnwindData |  |
| 860 | `?empty@?$_Yarn@D@std@@QEBA_NXZ` | `0x74380` | 45 | UnwindData |  |
| 861 | `?empty@?$_Yarn@G@std@@QEBA_NXZ` | `0x743B0` | 45 | UnwindData |  |
| 862 | `?empty@?$_Yarn@_W@std@@QEBA_NXZ` | `0x743E0` | 45 | UnwindData |  |
| 873 | `?fill@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAADD@Z` | `0x74500` | 47 | UnwindData |  |
| 874 | `?fill@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBADXZ` | `0x74530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `?fill@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAGG@Z` | `0x74540` | 50 | UnwindData |  |
| 876 | `?fill@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBAGXZ` | `0x74580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `?fill@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAA_W_W@Z` | `0x74590` | 50 | UnwindData |  |
| 878 | `?fill@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEBA_WXZ` | `0x745D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | `?gcount@?$basic_istream@DU?$char_traits@D@std@@@std@@QEBA_JXZ` | `0x745E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 888 | `?gcount@?$basic_istream@GU?$char_traits@G@std@@@std@@QEBA_JXZ` | `0x745F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `?gcount@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEBA_JXZ` | `0x74600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@AEAD@Z` | `0x74610` | 77 | UnwindData |  |
| 891 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@@Z` | `0x74660` | 78 | UnwindData |  |
| 892 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@D@Z` | `0x746B0` | 469 | UnwindData |  |
| 893 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_J@Z` | `0x74890` | 88 | UnwindData |  |
| 894 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_JD@Z` | `0x748F0` | 566 | UnwindData |  |
| 895 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x74B30` | 303 | UnwindData |  |
| 896 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@AEAG@Z` | `0x74C60` | 82 | UnwindData |  |
| 897 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@@Z` | `0x74CC0` | 78 | UnwindData |  |
| 898 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@G@Z` | `0x74D10` | 450 | UnwindData |  |
| 899 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_J@Z` | `0x74EE0` | 88 | UnwindData |  |
| 900 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_JG@Z` | `0x74F40` | 579 | UnwindData |  |
| 901 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x75190` | 311 | UnwindData |  |
| 902 | `?get@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@2@@Z` | `0x752D0` | 78 | UnwindData |  |
| 903 | `?get@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@2@_W@Z` | `0x75320` | 450 | UnwindData |  |
| 904 | `?get@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@AEA_W@Z` | `0x754F0` | 82 | UnwindData |  |
| 905 | `?get@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@PEA_W_J@Z` | `0x75550` | 88 | UnwindData |  |
| 906 | `?get@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@PEA_W_J_W@Z` | `0x755B0` | 579 | UnwindData |  |
| 907 | `?get@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAGXZ` | `0x75800` | 311 | UnwindData |  |
| 908 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x75940` | 193 | UnwindData |  |
| 909 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x75A10` | 193 | UnwindData |  |
| 910 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x75AE0` | 193 | UnwindData |  |
| 911 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x75BB0` | 193 | UnwindData |  |
| 912 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x75C80` | 193 | UnwindData |  |
| 913 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x75D50` | 193 | UnwindData |  |
| 914 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x75E20` | 193 | UnwindData |  |
| 915 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x75EF0` | 193 | UnwindData |  |
| 916 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x75FC0` | 193 | UnwindData |  |
| 917 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x76090` | 193 | UnwindData |  |
| 918 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x76160` | 193 | UnwindData |  |
| 919 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x76230` | 193 | UnwindData |  |
| 920 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x76300` | 193 | UnwindData |  |
| 921 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x763D0` | 193 | UnwindData |  |
| 922 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x764A0` | 193 | UnwindData |  |
| 923 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x76570` | 193 | UnwindData |  |
| 924 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x76640` | 193 | UnwindData |  |
| 925 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x76710` | 193 | UnwindData |  |
| 926 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x767E0` | 193 | UnwindData |  |
| 927 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x768B0` | 193 | UnwindData |  |
| 928 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x76980` | 193 | UnwindData |  |
| 929 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x76A50` | 193 | UnwindData |  |
| 930 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x76B20` | 193 | UnwindData |  |
| 931 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x76BF0` | 193 | UnwindData |  |
| 932 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x76CC0` | 193 | UnwindData |  |
| 933 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x76D90` | 193 | UnwindData |  |
| 934 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x76E60` | 193 | UnwindData |  |
| 935 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x76F30` | 193 | UnwindData |  |
| 936 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x77000` | 193 | UnwindData |  |
| 937 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x770D0` | 193 | UnwindData |  |
| 938 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x771A0` | 193 | UnwindData |  |
| 939 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x77270` | 193 | UnwindData |  |
| 940 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x77340` | 193 | UnwindData |  |
| 941 | `?get@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@DD@Z` | `0x77410` | 223 | UnwindData |  |
| 942 | `?get@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@PEBD4@Z` | `0x774F0` | 996 | UnwindData |  |
| 943 | `?get@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@DD@Z` | `0x778E0` | 223 | UnwindData |  |
| 944 | `?get@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@PEBG4@Z` | `0x779C0` | 999 | UnwindData |  |
| 945 | `?get@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@DD@Z` | `0x77DB0` | 223 | UnwindData |  |
| 946 | `?get@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@PEB_W4@Z` | `0x77E90` | 999 | UnwindData |  |
| 947 | `?get_date@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x78280` | 193 | UnwindData |  |
| 948 | `?get_date@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x78350` | 193 | UnwindData |  |
| 949 | `?get_date@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x78420` | 193 | UnwindData |  |
| 954 | `?get_time@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x784F0` | 193 | UnwindData |  |
| 955 | `?get_time@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x785C0` | 193 | UnwindData |  |
| 956 | `?get_time@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x78690` | 193 | UnwindData |  |
| 963 | `?getline@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_J@Z` | `0x78760` | 88 | UnwindData |  |
| 964 | `?getline@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_JD@Z` | `0x787C0` | 637 | UnwindData |  |
| 965 | `?getline@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_J@Z` | `0x78A40` | 88 | UnwindData |  |
| 966 | `?getline@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_JG@Z` | `0x78AA0` | 654 | UnwindData |  |
| 967 | `?getline@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@PEA_W_J@Z` | `0x78D30` | 88 | UnwindData |  |
| 968 | `?getline@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@PEA_W_J_W@Z` | `0x78D90` | 654 | UnwindData |  |
| 969 | `?getloc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEBA?AVlocale@2@XZ` | `0x79020` | 43 | UnwindData |  |
| 970 | `?getloc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEBA?AVlocale@2@XZ` | `0x79050` | 43 | UnwindData |  |
| 971 | `?getloc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEBA?AVlocale@2@XZ` | `0x79080` | 43 | UnwindData |  |
| 1017 | `?ignore@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@_JH@Z` | `0x790B0` | 347 | UnwindData |  |
| 1018 | `?ignore@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@_JG@Z` | `0x79210` | 360 | UnwindData |  |
| 1019 | `?ignore@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@_JG@Z` | `0x79380` | 360 | UnwindData |  |
| 1020 | `?imbue@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x794F0` | 128 | UnwindData |  |
| 1021 | `?imbue@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x79570` | 128 | UnwindData |  |
| 1022 | `?imbue@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x795F0` | 128 | UnwindData |  |
| 1032 | `?in_avail@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA_JXZ` | `0x79670` | 92 | UnwindData |  |
| 1033 | `?in_avail@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA_JXZ` | `0x796D0` | 92 | UnwindData |  |
| 1034 | `?in_avail@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA_JXZ` | `0x79730` | 92 | UnwindData |  |
| 1044 | `?ipfx@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA_N_N@Z` | `0x79790` | 33 | UnwindData |  |
| 1045 | `?ipfx@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA_N_N@Z` | `0x797C0` | 33 | UnwindData |  |
| 1046 | `?ipfx@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA_N_N@Z` | `0x797F0` | 33 | UnwindData |  |
| 1053 | `?isfx@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x79820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `?isfx@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x79830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1055 | `?isfx@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x79840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `?length@?$codecvt@DDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0x79850` | 97 | UnwindData |  |
| 1063 | `?move@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAX$$QEAV12@@Z` | `0x798C0` | 78 | UnwindData |  |
| 1064 | `?move@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXAEAV12@@Z` | `0x79910` | 78 | UnwindData |  |
| 1065 | `?move@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAX$$QEAV12@@Z` | `0x79960` | 78 | UnwindData |  |
| 1066 | `?move@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXAEAV12@@Z` | `0x799B0` | 78 | UnwindData |  |
| 1067 | `?move@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAX$$QEAV12@@Z` | `0x79A00` | 78 | UnwindData |  |
| 1068 | `?move@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXAEAV12@@Z` | `0x79A50` | 78 | UnwindData |  |
| 1069 | `?narrow@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBADDD@Z` | `0x79AA0` | 108 | UnwindData |  |
| 1070 | `?narrow@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBADGD@Z` | `0x79B10` | 109 | UnwindData |  |
| 1071 | `?narrow@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEBAD_WD@Z` | `0x79B80` | 109 | UnwindData |  |
| 1078 | `?opfx@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA_NXZ` | `0x79BF0` | 183 | UnwindData |  |
| 1079 | `?opfx@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA_NXZ` | `0x79CB0` | 183 | UnwindData |  |
| 1080 | `?opfx@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAA_NXZ` | `0x79D70` | 183 | UnwindData |  |
| 1081 | `?osfx@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x79E30` | 25 | UnwindData |  |
| 1082 | `?osfx@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x79E50` | 25 | UnwindData |  |
| 1083 | `?osfx@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x79E70` | 25 | UnwindData |  |
| 1095 | `?pbase@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x79E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `?pbase@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x79EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `?pbase@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBAPEA_WXZ` | `0x79ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `?peek@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x79EF0` | 259 | UnwindData |  |
| 1102 | `?peek@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x7A000` | 270 | UnwindData |  |
| 1103 | `?peek@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAGXZ` | `0x7A110` | 270 | UnwindData |  |
| 1109 | `?pubimbue@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x7A220` | 140 | UnwindData |  |
| 1110 | `?pubimbue@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x7A2B0` | 140 | UnwindData |  |
| 1111 | `?pubimbue@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x7A340` | 140 | UnwindData |  |
| 1112 | `?pubseekoff@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@_JHH@Z` | `0x7A3D0` | 100 | UnwindData |  |
| 1113 | `?pubseekoff@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@_JII@Z` | `0x7A440` | 67 | UnwindData |  |
| 1114 | `?pubseekoff@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@_JHH@Z` | `0x7A490` | 100 | UnwindData |  |
| 1115 | `?pubseekoff@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@_JII@Z` | `0x7A500` | 67 | UnwindData |  |
| 1116 | `?pubseekoff@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@_JHH@Z` | `0x7A550` | 100 | UnwindData |  |
| 1117 | `?pubseekoff@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@_JII@Z` | `0x7A5C0` | 67 | UnwindData |  |
| 1118 | `?pubseekpos@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@V32@H@Z` | `0x7A610` | 134 | UnwindData |  |
| 1119 | `?pubseekpos@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@V32@I@Z` | `0x7A6A0` | 134 | UnwindData |  |
| 1120 | `?pubseekpos@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@V32@H@Z` | `0x7A730` | 134 | UnwindData |  |
| 1121 | `?pubseekpos@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@V32@I@Z` | `0x7A7C0` | 134 | UnwindData |  |
| 1122 | `?pubseekpos@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@V32@H@Z` | `0x7A850` | 134 | UnwindData |  |
| 1123 | `?pubseekpos@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@V32@I@Z` | `0x7A8E0` | 134 | UnwindData |  |
| 1124 | `?pubsetbuf@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAPEAV12@PEAD_J@Z` | `0x7A970` | 77 | UnwindData |  |
| 1125 | `?pubsetbuf@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAPEAV12@PEAG_J@Z` | `0x7A9C0` | 77 | UnwindData |  |
| 1126 | `?pubsetbuf@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAPEAV12@PEA_W_J@Z` | `0x7AA10` | 77 | UnwindData |  |
| 1130 | `?put@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@D@Z` | `0x7AA60` | 248 | UnwindData |  |
| 1131 | `?put@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@G@Z` | `0x7AB60` | 255 | UnwindData |  |
| 1132 | `?put@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@_W@Z` | `0x7AC60` | 255 | UnwindData |  |
| 1133 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DJ@Z` | `0x7AD60` | 157 | UnwindData |  |
| 1134 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DK@Z` | `0x7AE00` | 157 | UnwindData |  |
| 1135 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DN@Z` | `0x7AEA0` | 161 | UnwindData |  |
| 1136 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DO@Z` | `0x7AF50` | 161 | UnwindData |  |
| 1137 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBX@Z` | `0x7B000` | 159 | UnwindData |  |
| 1138 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_J@Z` | `0x7B0A0` | 159 | UnwindData |  |
| 1139 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_K@Z` | `0x7B140` | 159 | UnwindData |  |
| 1140 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_N@Z` | `0x7B1E0` | 158 | UnwindData |  |
| 1141 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GJ@Z` | `0x7B280` | 158 | UnwindData |  |
| 1142 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GK@Z` | `0x7B320` | 158 | UnwindData |  |
| 1143 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GN@Z` | `0x7B3C0` | 162 | UnwindData |  |
| 1144 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GO@Z` | `0x7B470` | 162 | UnwindData |  |
| 1145 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBX@Z` | `0x7B520` | 160 | UnwindData |  |
| 1146 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_J@Z` | `0x7B5C0` | 160 | UnwindData |  |
| 1147 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_K@Z` | `0x7B660` | 160 | UnwindData |  |
| 1148 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_N@Z` | `0x7B700` | 159 | UnwindData |  |
| 1149 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WJ@Z` | `0x7B7A0` | 158 | UnwindData |  |
| 1150 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WK@Z` | `0x7B840` | 158 | UnwindData |  |
| 1151 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WN@Z` | `0x7B8E0` | 162 | UnwindData |  |
| 1152 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WO@Z` | `0x7B990` | 162 | UnwindData |  |
| 1153 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEBX@Z` | `0x7BA40` | 160 | UnwindData |  |
| 1154 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_W_J@Z` | `0x7BAE0` | 160 | UnwindData |  |
| 1155 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_W_K@Z` | `0x7BB80` | 160 | UnwindData |  |
| 1156 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_W_N@Z` | `0x7BC20` | 159 | UnwindData |  |
| 1157 | `?put@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBUtm@@DD@Z` | `0x7BCC0` | 183 | UnwindData |  |
| 1158 | `?put@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBUtm@@PEBD3@Z` | `0x7BD80` | 1,063 | UnwindData |  |
| 1159 | `?put@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBUtm@@DD@Z` | `0x7C1B0` | 184 | UnwindData |  |
| 1160 | `?put@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBUtm@@PEBG3@Z` | `0x7C270` | 1,114 | UnwindData |  |
| 1161 | `?put@?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEBUtm@@DD@Z` | `0x7C6D0` | 184 | UnwindData |  |
| 1162 | `?put@?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEBUtm@@PEB_W4@Z` | `0x7C790` | 1,114 | UnwindData |  |
| 1163 | `?putback@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@D@Z` | `0x7CBF0` | 380 | UnwindData |  |
| 1164 | `?putback@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@G@Z` | `0x7CD70` | 391 | UnwindData |  |
| 1165 | `?putback@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@_W@Z` | `0x7CF00` | 391 | UnwindData |  |
| 1167 | `?rdbuf@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAPEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@PEAV32@@Z` | `0x7D090` | 67 | UnwindData |  |
| 1169 | `?rdbuf@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAPEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@PEAV32@@Z` | `0x7D0E0` | 67 | UnwindData |  |
| 1171 | `?rdbuf@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAPEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@2@PEAV32@@Z` | `0x7D130` | 67 | UnwindData |  |
| 1174 | `?read@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_J@Z` | `0x7D180` | 314 | UnwindData |  |
| 1175 | `?read@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_J@Z` | `0x7D2C0` | 314 | UnwindData |  |
| 1176 | `?read@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@PEA_W_J@Z` | `0x7D400` | 314 | UnwindData |  |
| 1177 | `?readsome@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA_JPEAD_J@Z` | `0x7D540` | 318 | UnwindData |  |
| 1178 | `?readsome@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA_JPEAG_J@Z` | `0x7D680` | 318 | UnwindData |  |
| 1179 | `?readsome@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA_JPEA_W_J@Z` | `0x7D7C0` | 318 | UnwindData |  |
| 1191 | `?seekg@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@V?$fpos@U_Mbstatet@@@2@@Z` | `0x7D900` | 441 | UnwindData |  |
| 1192 | `?seekg@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@_JH@Z` | `0x7DAC0` | 396 | UnwindData |  |
| 1193 | `?seekg@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@V?$fpos@U_Mbstatet@@@2@@Z` | `0x7DC50` | 441 | UnwindData |  |
| 1194 | `?seekg@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@_JH@Z` | `0x7DE10` | 396 | UnwindData |  |
| 1195 | `?seekg@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@V?$fpos@U_Mbstatet@@@2@@Z` | `0x7DFA0` | 441 | UnwindData |  |
| 1196 | `?seekg@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@_JH@Z` | `0x7E160` | 396 | UnwindData |  |
| 1200 | `?seekp@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@V?$fpos@U_Mbstatet@@@2@@Z` | `0x7E2F0` | 341 | UnwindData |  |
| 1201 | `?seekp@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@_JH@Z` | `0x7E450` | 300 | UnwindData |  |
| 1202 | `?seekp@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@V?$fpos@U_Mbstatet@@@2@@Z` | `0x7E580` | 341 | UnwindData |  |
| 1203 | `?seekp@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@_JH@Z` | `0x7E6E0` | 300 | UnwindData |  |
| 1204 | `?seekp@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@V?$fpos@U_Mbstatet@@@2@@Z` | `0x7E810` | 341 | UnwindData |  |
| 1205 | `?seekp@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@_JH@Z` | `0x7E970` | 300 | UnwindData |  |
| 1210 | `?set_rdbuf@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXPEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@@Z` | `0x7EAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `?set_rdbuf@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXPEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@@Z` | `0x7EAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `?set_rdbuf@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXPEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@2@@Z` | `0x7EAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `?setp@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXPEAD00@Z` | `0x7EB00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `?setp@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXPEAG00@Z` | `0x7EB60` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `?setp@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXPEA_W00@Z` | `0x7EBC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `?setstate@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXI@Z` | `0x7EC20` | 36 | UnwindData |  |
| 1233 | `?setstate@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXI@Z` | `0x7EC50` | 36 | UnwindData |  |
| 1235 | `?setstate@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXI@Z` | `0x7EC80` | 36 | UnwindData |  |
| 1243 | `?sgetn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA_JPEAD_J@Z` | `0x7ECB0` | 77 | UnwindData |  |
| 1244 | `?sgetn@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA_JPEAG_J@Z` | `0x7ED00` | 77 | UnwindData |  |
| 1245 | `?sgetn@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA_JPEA_W_J@Z` | `0x7ED50` | 77 | UnwindData |  |
| 1249 | `?snextc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x7EDA0` | 134 | UnwindData |  |
| 1250 | `?snextc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x7EE30` | 144 | UnwindData |  |
| 1251 | `?snextc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAGXZ` | `0x7EEC0` | 144 | UnwindData |  |
| 1252 | `?sputbackc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHD@Z` | `0x7EF50` | 189 | UnwindData |  |
| 1253 | `?sputbackc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGG@Z` | `0x7F010` | 192 | UnwindData |  |
| 1254 | `?sputbackc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAG_W@Z` | `0x7F0D0` | 192 | UnwindData |  |
| 1258 | `?sputn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA_JPEBD_J@Z` | `0x7F190` | 77 | UnwindData |  |
| 1259 | `?sputn@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA_JPEBG_J@Z` | `0x7F1E0` | 77 | UnwindData |  |
| 1260 | `?sputn@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA_JPEB_W_J@Z` | `0x7F230` | 77 | UnwindData |  |
| 1261 | `?stossc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x7F280` | 76 | UnwindData |  |
| 1262 | `?stossc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x7F2D0` | 76 | UnwindData |  |
| 1263 | `?stossc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x7F320` | 76 | UnwindData |  |
| 1264 | `?sungetc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x7F370` | 152 | UnwindData |  |
| 1265 | `?sungetc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x7F410` | 157 | UnwindData |  |
| 1266 | `?sungetc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAGXZ` | `0x7F4B0` | 157 | UnwindData |  |
| 1267 | `?swap@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXAEAV12@@Z` | `0x7F550` | 87 | UnwindData |  |
| 1268 | `?swap@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXAEAV12@@Z` | `0x7F5B0` | 87 | UnwindData |  |
| 1269 | `?swap@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXAEAV12@@Z` | `0x7F610` | 87 | UnwindData |  |
| 1270 | `?swap@?$basic_iostream@DU?$char_traits@D@std@@@std@@IEAAXAEAV12@@Z` | `0x7F670` | 101 | UnwindData |  |
| 1271 | `?swap@?$basic_iostream@GU?$char_traits@G@std@@@std@@IEAAXAEAV12@@Z` | `0x7F6E0` | 101 | UnwindData |  |
| 1272 | `?swap@?$basic_iostream@_WU?$char_traits@_W@std@@@std@@IEAAXAEAV12@@Z` | `0x7F750` | 101 | UnwindData |  |
| 1273 | `?swap@?$basic_istream@DU?$char_traits@D@std@@@std@@IEAAXAEAV12@@Z` | `0x7F7C0` | 110 | UnwindData |  |
| 1274 | `?swap@?$basic_istream@GU?$char_traits@G@std@@@std@@IEAAXAEAV12@@Z` | `0x7F830` | 110 | UnwindData |  |
| 1275 | `?swap@?$basic_istream@_WU?$char_traits@_W@std@@@std@@IEAAXAEAV12@@Z` | `0x7F8A0` | 110 | UnwindData |  |
| 1276 | `?swap@?$basic_ostream@DU?$char_traits@D@std@@@std@@IEAAXAEAV12@@Z` | `0x7F910` | 101 | UnwindData |  |
| 1277 | `?swap@?$basic_ostream@GU?$char_traits@G@std@@@std@@IEAAXAEAV12@@Z` | `0x7F980` | 101 | UnwindData |  |
| 1278 | `?swap@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@IEAAXAEAV12@@Z` | `0x7F9F0` | 101 | UnwindData |  |
| 1279 | `?swap@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXAEAV12@@Z` | `0x7FA60` | 413 | UnwindData |  |
| 1280 | `?swap@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXAEAV12@@Z` | `0x7FC00` | 413 | UnwindData |  |
| 1281 | `?swap@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXAEAV12@@Z` | `0x7FDA0` | 413 | UnwindData |  |
| 1283 | `?sync@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x7FF40` | 266 | UnwindData |  |
| 1284 | `?sync@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAHXZ` | `0x80050` | 266 | UnwindData |  |
| 1285 | `?sync@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAHXZ` | `0x80160` | 266 | UnwindData |  |
| 1292 | `?tellg@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@XZ` | `0x80270` | 197 | UnwindData |  |
| 1293 | `?tellg@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@XZ` | `0x80340` | 197 | UnwindData |  |
| 1294 | `?tellg@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@XZ` | `0x80410` | 197 | UnwindData |  |
| 1295 | `?tellp@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@XZ` | `0x804E0` | 194 | UnwindData |  |
| 1296 | `?tellp@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@XZ` | `0x805B0` | 194 | UnwindData |  |
| 1297 | `?tellp@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@XZ` | `0x80680` | 194 | UnwindData |  |
| 1324 | `?unget@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@XZ` | `0x80750` | 361 | UnwindData |  |
| 1325 | `?unget@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@XZ` | `0x808C0` | 334 | UnwindData |  |
| 1326 | `?unget@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@XZ` | `0x80A10` | 334 | UnwindData |  |
| 1352 | `?write@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEBD_J@Z` | `0x80B60` | 252 | UnwindData |  |
| 1353 | `?write@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEBG_J@Z` | `0x80C60` | 252 | UnwindData |  |
| 1354 | `?write@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@PEB_W_J@Z` | `0x80D60` | 252 | UnwindData |  |
| 1291 | `?table_size@?$ctype@D@std@@2_KB` | `0x92338` | 376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `??_7_Facet_base@std@@6B@` | `0x924B0` | 824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `??_7facet@locale@std@@6B@` | `0x927E8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `??_7_Locimp@locale@std@@6B@` | `0x92808` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `??_7codecvt_base@std@@6B@` | `0x92830` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `??_7?$codecvt@_SDU_Mbstatet@@@std@@6B@` | `0x92868` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `??_7?$codecvt@_UDU_Mbstatet@@@std@@6B@` | `0x928C0` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `??_7?$codecvt@_WDU_Mbstatet@@@std@@6B@` | `0x92918` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `??_7?$codecvt@GDU_Mbstatet@@@std@@6B@` | `0x92970` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `??_7ctype_base@std@@6B@` | `0x929C8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `??_7?$ctype@D@std@@6B@` | `0x929E8` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `??_7?$ctype@_W@std@@6B@` | `0x92A48` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `??_7?$ctype@G@std@@6B@` | `0x92AC8` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `??_7ios_base@std@@6B@` | `0x92B60` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `??_7time_base@std@@6B@` | `0x92BF0` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `??_7?$basic_ios@DU?$char_traits@D@std@@@std@@6B@` | `0x92C68` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `??_7?$basic_ostream@DU?$char_traits@D@std@@@std@@6B@` | `0x92C78` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `??_8?$basic_ostream@DU?$char_traits@D@std@@@std@@7B@` | `0x92C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `??_7?$basic_streambuf@DU?$char_traits@D@std@@@std@@6B@` | `0x92C90` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `??_7?$codecvt@DDU_Mbstatet@@@std@@6B@` | `0x92D90` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `??_7?$basic_istream@DU?$char_traits@D@std@@@std@@6B@` | `0x92E90` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `??_8?$basic_istream@DU?$char_traits@D@std@@@std@@7B@` | `0x92E98` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `?_BADOFF@std@@3_JB` | `0x93178` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `??_7?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x931A8` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `??_7?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x93220` | 5,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `??_7?$basic_streambuf@GU?$char_traits@G@std@@@std@@6B@` | `0x94780` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `??_7?$basic_ios@GU?$char_traits@G@std@@@std@@6B@` | `0x94880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `??_7?$basic_ostream@GU?$char_traits@G@std@@@std@@6B@` | `0x94890` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `??_8?$basic_ostream@GU?$char_traits@G@std@@@std@@7B@` | `0x94898` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `??_7?$basic_istream@GU?$char_traits@G@std@@@std@@6B@` | `0x948A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `??_8?$basic_istream@GU?$char_traits@G@std@@@std@@7B@` | `0x948B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `??_7?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@6B@` | `0x948C0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `??_7?$basic_ios@_WU?$char_traits@_W@std@@@std@@6B@` | `0x949C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `??_7?$basic_ostream@_WU?$char_traits@_W@std@@@std@@6B@` | `0x949D0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `??_8?$basic_ostream@_WU?$char_traits@_W@std@@@std@@7B@` | `0x949D8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `??_7?$basic_istream@_WU?$char_traits@_W@std@@@std@@6B@` | `0x949E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `??_8?$basic_istream@_WU?$char_traits@_W@std@@@std@@7B@` | `0x949F0` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `??_7?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@6B@` | `0x94A98` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `??_7?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@6B@` | `0x94AC0` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `??_7?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@6B@` | `0x94B38` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `??_7?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@6B@` | `0x94DE8` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `??_7?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x94E40` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `??_7?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x94EB8` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `??_7?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x95168` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `??_7?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x951C0` | 2,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `??_7?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x95BC0` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `??_7?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x95C18` | 2,526 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `?intl@?$moneypunct@D$00@std@@2_NB` | `0x965F6` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `?intl@?$moneypunct@D$0A@@std@@2_NB` | `0x965F7` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1042 | `?intl@?$moneypunct@_W$00@std@@2_NB` | `0x965F8` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1043 | `?intl@?$moneypunct@_W$0A@@std@@2_NB` | `0x965F9` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1040 | `?intl@?$moneypunct@G$00@std@@2_NB` | `0x965FA` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | `?intl@?$moneypunct@G$0A@@std@@2_NB` | `0x965FB` | 13 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `??_7?$basic_iostream@DU?$char_traits@D@std@@@std@@6B@` | `0x96608` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `??_8?$basic_iostream@DU?$char_traits@D@std@@@std@@7B?$basic_istream@DU?$char_traits@D@std@@@1@@` | `0x96610` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `??_8?$basic_iostream@DU?$char_traits@D@std@@@std@@7B?$basic_ostream@DU?$char_traits@D@std@@@1@@` | `0x96618` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `??_7?$basic_iostream@_WU?$char_traits@_W@std@@@std@@6B@` | `0x96628` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `??_8?$basic_iostream@_WU?$char_traits@_W@std@@@std@@7B?$basic_istream@_WU?$char_traits@_W@std@@@1@@` | `0x96630` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `??_8?$basic_iostream@_WU?$char_traits@_W@std@@@std@@7B?$basic_ostream@_WU?$char_traits@_W@std@@@1@@` | `0x96638` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `??_7?$basic_iostream@GU?$char_traits@G@std@@@std@@6B@` | `0x96648` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `??_8?$basic_iostream@GU?$char_traits@G@std@@@std@@7B?$basic_istream@GU?$char_traits@G@std@@@1@@` | `0x96650` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `??_8?$basic_iostream@GU?$char_traits@G@std@@@std@@7B?$basic_ostream@GU?$char_traits@G@std@@@1@@` | `0x96658` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `?_Src@?1??_Getffldx@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@3@1AEAVios_base@3@PEAH@Z@4QBDB` | `0x96688` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 627 | `?_Src@?1??_Getffld@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@3@1AEAVios_base@3@PEAH@Z@4QBDB` | `0x966A8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `?_Src@?1??_Getifld@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@3@1HAEBVlocale@3@@Z@4QBDB` | `0x966B8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | `?_Src@?1??_Getffldx@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@3@1AEAVios_base@3@PEAH@Z@4QBDB` | `0x966D8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 628 | `?_Src@?1??_Getffld@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@3@1AEAVios_base@3@PEAH@Z@4QBDB` | `0x966F8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 634 | `?_Src@?1??_Getifld@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@3@1HAEBVlocale@3@@Z@4QBDB` | `0x96708` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 629 | `?_Src@?1??_Getffldx@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@3@1AEAVios_base@3@PEAH@Z@4QBDB` | `0x96728` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 626 | `?_Src@?1??_Getffld@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@3@1AEAVios_base@3@PEAH@Z@4QBDB` | `0x96748` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 632 | `?_Src@?1??_Getifld@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@3@1HAEBVlocale@3@@Z@4QBDB` | `0x96758` | 207,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 635 | `?_Sync@ios_base@std@@0_NA` | `0xC90B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `?_Init_cnt@Init@ios_base@std@@0HA` | `0xC90C0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `?_Init_cnt@_UShinit@std@@0HA` | `0xC9180` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `?_Init_cnt@_Winit@std@@0HA` | `0xC9184` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1379 | `_Denorm` | `0xC91A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `_LDenorm` | `0xC91B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1399 | `_Hugeval` | `0xC91C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1400 | `_Inf` | `0xC91D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1405 | `_LInf` | `0xC91E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `_Nan` | `0xC91F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1406 | `_LNan` | `0xC9200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1441 | `_Snan` | `0xC9210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `_LSnan` | `0xC9220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `_FDenorm` | `0xC9230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `_FInf` | `0xC9240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1388 | `_FNan` | `0xC9250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1390 | `_FSnan` | `0xC9260` | 6,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `?cerr@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A` | `0xCACB0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `?id@?$codecvt@DDU_Mbstatet@@@std@@2V0locale@2@A` | `0xCADC0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `?cin@std@@3V?$basic_istream@DU?$char_traits@D@std@@@1@A` | `0xCAE90` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 696 | `?clog@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A` | `0xCAFC0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 701 | `?cout@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A` | `0xCB040` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `?_Index@ios_base@std@@0HA` | `0xCB150` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 599 | `?_Ptr_cin@std@@3PEAV?$basic_istream@DU?$char_traits@D@std@@@1@EA` | `0xCB1C0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `?_Ptr_cout@std@@3PEAV?$basic_ostream@DU?$char_traits@D@std@@@1@EA` | `0xCB1C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `?_Ptr_cerr@std@@3PEAV?$basic_ostream@DU?$char_traits@D@std@@@1@EA` | `0xCB1D0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 600 | `?_Ptr_clog@std@@3PEAV?$basic_ostream@DU?$char_traits@D@std@@@1@EA` | `0xCB1D8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `?_Ptr_wcin@std@@3PEAV?$basic_istream@_WU?$char_traits@_W@std@@@1@EA` | `0xCB1E0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `?_Ptr_wcout@std@@3PEAV?$basic_ostream@_WU?$char_traits@_W@std@@@1@EA` | `0xCB1E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `?_Ptr_wcerr@std@@3PEAV?$basic_ostream@_WU?$char_traits@_W@std@@@1@EA` | `0xCB1F0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `?_Ptr_wclog@std@@3PEAV?$basic_ostream@_WU?$char_traits@_W@std@@@1@EA` | `0xCB1F8` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `?id@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0xCB268` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `?id@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0xCB270` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1008 | `?id@?$numpunct@D@std@@2V0locale@2@A` | `0xCB278` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `?_Id_cnt@id@locale@std@@0HA` | `0xCB298` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `?_Clocptr@_Locimp@locale@std@@0PEAV123@EA` | `0xCB2A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `?id@?$ctype@_W@std@@2V0locale@2@A` | `0xCB2A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 984 | `?id@?$ctype@D@std@@2V0locale@2@A` | `0xCB2B0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 979 | `?id@?$codecvt@GDU_Mbstatet@@@std@@2V0locale@2@A` | `0xCB2B8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `?id@?$ctype@G@std@@2V0locale@2@A` | `0xCB2C0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `?id@?$codecvt@_WDU_Mbstatet@@@std@@2V0locale@2@A` | `0xCB2D8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 613 | `?_Raise_handler@std@@3P6AXAEBVexception@stdext@@@ZEA` | `0xCB300` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1333 | `?wcerr@std@@3V?$basic_ostream@GU?$char_traits@G@std@@@1@A` | `0xCB670` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1335 | `?wcin@std@@3V?$basic_istream@GU?$char_traits@G@std@@@1@A` | `0xCB840` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `?wclog@std@@3V?$basic_ostream@GU?$char_traits@G@std@@@1@A` | `0xCB8D0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1339 | `?wcout@std@@3V?$basic_ostream@GU?$char_traits@G@std@@@1@A` | `0xCB9F0` | 264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 604 | `?_Ptr_wcin@std@@3PEAV?$basic_istream@GU?$char_traits@G@std@@@1@EA` | `0xCBAF8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `?_Ptr_wcout@std@@3PEAV?$basic_ostream@GU?$char_traits@G@std@@@1@EA` | `0xCBB00` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `?_Ptr_wcerr@std@@3PEAV?$basic_ostream@GU?$char_traits@G@std@@@1@EA` | `0xCBB08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `?_Ptr_wclog@std@@3PEAV?$basic_ostream@GU?$char_traits@G@std@@@1@EA` | `0xCBB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `?wcerr@std@@3V?$basic_ostream@_WU?$char_traits@_W@std@@@1@A` | `0xCBB30` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1336 | `?wcin@std@@3V?$basic_istream@_WU?$char_traits@_W@std@@@1@A` | `0xCBD00` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `?wclog@std@@3V?$basic_ostream@_WU?$char_traits@_W@std@@@1@A` | `0xCBD90` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1340 | `?wcout@std@@3V?$basic_ostream@_WU?$char_traits@_W@std@@@1@A` | `0xCBEB0` | 264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `?id@?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@2V0locale@2@A` | `0xCBFB8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `?id@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@2V0locale@2@A` | `0xCBFC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `?id@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@2V0locale@2@A` | `0xCBFC8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `?id@?$numpunct@_W@std@@2V0locale@2@A` | `0xCBFD0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 983 | `?id@?$collate@_W@std@@2V0locale@2@A` | `0xCBFD8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `?id@?$messages@_W@std@@2V0locale@2@A` | `0xCBFE0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `?id@?$money_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@2V0locale@2@A` | `0xCBFE8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 995 | `?id@?$money_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@2V0locale@2@A` | `0xCBFF0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `?id@?$moneypunct@_W$0A@@std@@2V0locale@2@A` | `0xCBFF8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `?id@?$moneypunct@_W$00@std@@2V0locale@2@A` | `0xCC000` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | `?id@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@2V0locale@2@A` | `0xCC008` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `?id@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0xCC010` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `?id@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0xCC018` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `?id@?$numpunct@G@std@@2V0locale@2@A` | `0xCC020` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 982 | `?id@?$collate@G@std@@2V0locale@2@A` | `0xCC028` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `?id@?$messages@G@std@@2V0locale@2@A` | `0xCC030` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `?id@?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0xCC038` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 994 | `?id@?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0xCC040` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `?id@?$moneypunct@G$0A@@std@@2V0locale@2@A` | `0xCC048` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `?id@?$moneypunct@G$00@std@@2V0locale@2@A` | `0xCC050` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `?id@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0xCC058` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `?id@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0xCC060` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `?id@?$collate@D@std@@2V0locale@2@A` | `0xCC118` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 987 | `?id@?$messages@D@std@@2V0locale@2@A` | `0xCC120` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `?id@?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0xCC128` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `?id@?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0xCC130` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 997 | `?id@?$moneypunct@D$0A@@std@@2V0locale@2@A` | `0xCC138` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `?id@?$moneypunct@D$00@std@@2V0locale@2@A` | `0xCC140` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `?id@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0xCC148` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `?id@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0xCC150` | 0 | Indeterminate |  |
