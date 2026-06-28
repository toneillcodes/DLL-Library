# Binary Specification: msvcp140d.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msvcp140d.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `342e5c13fd61f6130f61d85c00a7dfb10289ea7e89740f43efdabe4db16333a5`
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
| 5 | `??0?$_Yarn@D@std@@QEAA@PEBD@Z` | `0x6EC0` | 61 | UnwindData |  |
| 6 | `??0?$_Yarn@D@std@@QEAA@XZ` | `0x6F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0?$_Yarn@_W@std@@QEAA@XZ` | `0x6F20` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0?$basic_ios@DU?$char_traits@D@std@@@std@@IEAA@XZ` | `0x6FB0` | 79 | UnwindData |  |
| 38 | `??0?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@_N@Z` | `0x7000` | 208 | UnwindData |  |
| 48 | `??0?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAA@XZ` | `0x70D0` | 262 | UnwindData |  |
| 55 | `??0?$codecvt@DDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7400` | 76 | UnwindData |  |
| 57 | `??0?$codecvt@GDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7450` | 76 | UnwindData |  |
| 58 | `??0?$codecvt@GDU_Mbstatet@@@std@@QEAA@_K@Z` | `0x74A0` | 121 | UnwindData |  |
| 59 | `??0?$codecvt@_SDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@KW4_Codecvt_mode@1@_K@Z` | `0x7520` | 105 | UnwindData |  |
| 60 | `??0?$codecvt@_SDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7590` | 100 | UnwindData |  |
| 61 | `??0?$codecvt@_SDU_Mbstatet@@@std@@QEAA@_K@Z` | `0x7600` | 151 | UnwindData |  |
| 62 | `??0?$codecvt@_UDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@KW4_Codecvt_mode@1@_K@Z` | `0x76A0` | 105 | UnwindData |  |
| 63 | `??0?$codecvt@_UDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7710` | 100 | UnwindData |  |
| 64 | `??0?$codecvt@_UDU_Mbstatet@@@std@@QEAA@_K@Z` | `0x7780` | 151 | UnwindData |  |
| 65 | `??0?$codecvt@_WDU_Mbstatet@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7820` | 76 | UnwindData |  |
| 66 | `??0?$codecvt@_WDU_Mbstatet@@@std@@QEAA@_K@Z` | `0x7870` | 121 | UnwindData |  |
| 67 | `??0?$ctype@D@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x78F0` | 76 | UnwindData |  |
| 68 | `??0?$ctype@D@std@@QEAA@PEBF_N_K@Z` | `0x7940` | 255 | UnwindData |  |
| 69 | `??0?$ctype@G@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7A40` | 76 | UnwindData |  |
| 70 | `??0?$ctype@G@std@@QEAA@_K@Z` | `0x7A90` | 121 | UnwindData |  |
| 71 | `??0?$ctype@_W@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x7B10` | 76 | UnwindData |  |
| 72 | `??0?$ctype@_W@std@@QEAA@_K@Z` | `0x7B60` | 121 | UnwindData |  |
| 102 | `??0Init@ios_base@std@@QEAA@XZ` | `0x7C70` | 30 | UnwindData |  |
| 103 | `??0_Facet_base@std@@QEAA@AEBV01@@Z` | `0x7D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `??0_Facet_base@std@@QEAA@XZ` | `0x7D40` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `??0_Locimp@locale@std@@AEAA@AEBV012@@Z` | `0x7E70` | 180 | UnwindData |  |
| 107 | `??0_Locimp@locale@std@@AEAA@_N@Z` | `0x7F30` | 136 | UnwindData |  |
| 108 | `??0_Locinfo@std@@QEAA@HPEBD@Z` | `0x7FC0` | 202 | UnwindData |  |
| 109 | `??0_Locinfo@std@@QEAA@PEBD@Z` | `0x8090` | 194 | UnwindData |  |
| 112 | `??0_Timevec@std@@QEAA@AEBV01@@Z` | `0x82E0` | 52 | UnwindData |  |
| 113 | `??0_Timevec@std@@QEAA@PEAX@Z` | `0x8320` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `??0codecvt_base@std@@QEAA@_K@Z` | `0x8480` | 54 | UnwindData |  |
| 117 | `??0ctype_base@std@@QEAA@_K@Z` | `0x84C0` | 54 | UnwindData |  |
| 118 | `??0facet@locale@std@@IEAA@_K@Z` | `0x85D0` | 61 | UnwindData |  |
| 119 | `??0id@locale@std@@QEAA@_K@Z` | `0x86B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `??0ios_base@std@@IEAA@XZ` | `0x86D0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `??0time_base@std@@QEAA@_K@Z` | `0x8950` | 54 | UnwindData |  |
| 123 | `??1?$_Yarn@D@std@@QEAA@XZ` | `0x8A00` | 25 | UnwindData |  |
| 125 | `??1?$_Yarn@_W@std@@QEAA@XZ` | `0x8A20` | 25 | UnwindData |  |
| 126 | `??1?$basic_ios@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x8AA0` | 40 | UnwindData |  |
| 135 | `??1?$basic_ostream@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x8AD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `??1?$basic_streambuf@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x8B20` | 82 | UnwindData |  |
| 141 | `??1?$codecvt@DDU_Mbstatet@@@std@@MEAA@XZ` | `0x8BF0` | 40 | UnwindData |  |
| 142 | `??1?$codecvt@GDU_Mbstatet@@@std@@MEAA@XZ` | `0x8C20` | 40 | UnwindData |  |
| 143 | `??1?$codecvt@_SDU_Mbstatet@@@std@@MEAA@XZ` | `0x8C50` | 40 | UnwindData |  |
| 144 | `??1?$codecvt@_UDU_Mbstatet@@@std@@MEAA@XZ` | `0x8C80` | 40 | UnwindData |  |
| 145 | `??1?$codecvt@_WDU_Mbstatet@@@std@@MEAA@XZ` | `0x8CB0` | 40 | UnwindData |  |
| 146 | `??1?$ctype@D@std@@MEAA@XZ` | `0x8CE0` | 51 | UnwindData |  |
| 147 | `??1?$ctype@G@std@@MEAA@XZ` | `0x8D20` | 83 | UnwindData |  |
| 148 | `??1?$ctype@_W@std@@MEAA@XZ` | `0x8D80` | 83 | UnwindData |  |
| 161 | `??1Init@ios_base@std@@QEAA@XZ` | `0x8E30` | 25 | UnwindData |  |
| 162 | `??1_Facet_base@std@@UEAA@XZ` | `0x8E60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `??1_Locimp@locale@std@@MEAA@XZ` | `0x8EA0` | 68 | UnwindData |  |
| 165 | `??1_Locinfo@std@@QEAA@XZ` | `0x8EF0` | 141 | UnwindData |  |
| 167 | `??1_Timevec@std@@QEAA@XZ` | `0x8FA0` | 29 | UnwindData |  |
| 170 | `??1codecvt_base@std@@UEAA@XZ` | `0x9000` | 40 | UnwindData |  |
| 171 | `??1ctype_base@std@@UEAA@XZ` | `0x9030` | 40 | UnwindData |  |
| 172 | `??1facet@locale@std@@MEAA@XZ` | `0x9070` | 40 | UnwindData |  |
| 173 | `??1ios_base@std@@UEAA@XZ` | `0x90C0` | 40 | UnwindData |  |
| 174 | `??1time_base@std@@UEAA@XZ` | `0x91C0` | 40 | UnwindData |  |
| 175 | `??2_Crt_new_delete@std@@SAPEAX_K@Z` | `0x91F0` | 55 | UnwindData |  |
| 176 | `??2_Crt_new_delete@std@@SAPEAX_KAEBUnothrow_t@1@@Z` | `0x9230` | 77 | UnwindData |  |
| 177 | `??2_Crt_new_delete@std@@SAPEAX_KPEAX@Z` | `0x9280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `??3_Crt_new_delete@std@@SAXPEAX0@Z` | `0x9290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `??3_Crt_new_delete@std@@SAXPEAX@Z` | `0x92A0` | 26 | UnwindData |  |
| 180 | `??3_Crt_new_delete@std@@SAXPEAXAEBUnothrow_t@1@@Z` | `0x92C0` | 30 | UnwindData |  |
| 181 | `??4?$_Iosb@H@std@@QEAAAEAV01@$$QEAV01@@Z` | `0x92E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `??4?$_Iosb@H@std@@QEAAAEAV01@AEBV01@@Z` | `0x92F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `??4?$_Yarn@D@std@@QEAAAEAV01@PEBD@Z` | `0x9300` | 209 | UnwindData |  |
| 188 | `??4?$_Yarn@_W@std@@QEAAAEAV01@PEB_W@Z` | `0x93E0` | 217 | UnwindData |  |
| 201 | `??4Init@ios_base@std@@QEAAAEAV012@AEBV012@@Z` | `0x94C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `??4_Crt_new_delete@std@@QEAAAEAU01@$$QEAU01@@Z` | `0x94D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `??4_Crt_new_delete@std@@QEAAAEAU01@AEBU01@@Z` | `0x94E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `??4_Facet_base@std@@QEAAAEAV01@AEBV01@@Z` | `0x94F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `??4_Init_locks@std@@QEAAAEAV01@AEBV01@@Z` | `0x9500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `??4_Timevec@std@@QEAAAEAV01@AEBV01@@Z` | `0x9510` | 78 | UnwindData |  |
| 208 | `??4_Winit@std@@QEAAAEAV01@AEBV01@@Z` | `0x9560` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `??7ios_base@std@@QEBA_NXZ` | `0x9660` | 24 | UnwindData |  |
| 312 | `??Bid@locale@std@@QEAA_KXZ` | `0x9780` | 24 | UnwindData |  |
| 313 | `??Bios_base@std@@QEBA_NXZ` | `0x97A0` | 54 | UnwindData |  |
| 374 | `??_D?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x9960` | 49 | UnwindData |  |
| 378 | `??_F?$codecvt@GDU_Mbstatet@@@std@@QEAAXXZ` | `0xA3F0` | 27 | UnwindData |  |
| 379 | `??_F?$codecvt@_SDU_Mbstatet@@@std@@QEAAXXZ` | `0xA410` | 27 | UnwindData |  |
| 380 | `??_F?$codecvt@_UDU_Mbstatet@@@std@@QEAAXXZ` | `0xA430` | 27 | UnwindData |  |
| 381 | `??_F?$codecvt@_WDU_Mbstatet@@@std@@QEAAXXZ` | `0xA450` | 27 | UnwindData |  |
| 382 | `??_F?$ctype@D@std@@QEAAXXZ` | `0xA470` | 33 | UnwindData |  |
| 383 | `??_F?$ctype@G@std@@QEAAXXZ` | `0xA4A0` | 27 | UnwindData |  |
| 384 | `??_F?$ctype@_W@std@@QEAAXXZ` | `0xA4C0` | 27 | UnwindData |  |
| 397 | `??_F_Locinfo@std@@QEAAXXZ` | `0xA4E0` | 32 | UnwindData |  |
| 398 | `??_F_Timevec@std@@QEAAXXZ` | `0xA500` | 27 | UnwindData |  |
| 399 | `??_Fcodecvt_base@std@@QEAAXXZ` | `0xA520` | 27 | UnwindData |  |
| 400 | `??_Fctype_base@std@@QEAAXXZ` | `0xA540` | 27 | UnwindData |  |
| 401 | `??_Ffacet@locale@std@@QEAAXXZ` | `0xA560` | 27 | UnwindData |  |
| 402 | `??_Fid@locale@std@@QEAAXXZ` | `0xA580` | 27 | UnwindData |  |
| 403 | `??_Ftime_base@std@@QEAAXXZ` | `0xA5A0` | 27 | UnwindData |  |
| 408 | `?_Addcats@_Locinfo@std@@QEAAAEAV12@HPEBD@Z` | `0xA870` | 65 | UnwindData |  |
| 409 | `?_Addfac@_Locimp@locale@std@@AEAAXPEAVfacet@23@_K@Z` | `0xA8C0` | 45 | UnwindData |  |
| 414 | `?_C_str@?$_Yarn@D@std@@QEBAPEBDXZ` | `0xAA60` | 56 | UnwindData |  |
| 416 | `?_C_str@?$_Yarn@_W@std@@QEBAPEB_WXZ` | `0xAAA0` | 56 | UnwindData |  |
| 418 | `?_Callfns@ios_base@std@@AEAAXW4event@12@@Z` | `0xAC20` | 111 | UnwindData |  |
| 423 | `?_Decref@facet@locale@std@@UEAAPEAV_Facet_base@3@XZ` | `0xADD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `?_Donarrow@?$ctype@G@std@@IEBADGD@Z` | `0xAE00` | 142 | UnwindData |  |
| 425 | `?_Donarrow@?$ctype@_W@std@@IEBAD_WD@Z` | `0xAE90` | 142 | UnwindData |  |
| 426 | `?_Dowiden@?$ctype@G@std@@IEBAGD@Z` | `0xAF20` | 93 | UnwindData |  |
| 427 | `?_Dowiden@?$ctype@_W@std@@IEBA_WD@Z` | `0xAF80` | 108 | UnwindData |  |
| 428 | `?_Empty@?$_Yarn@D@std@@QEBA_NXZ` | `0xAFF0` | 45 | UnwindData |  |
| 430 | `?_Empty@?$_Yarn@_W@std@@QEBA_NXZ` | `0xB020` | 45 | UnwindData |  |
| 435 | `?_Findarr@ios_base@std@@AEAAAEAU_Iosarray@12@H@Z` | `0xB2F0` | 255 | UnwindData |  |
| 442 | `?_Getcat@?$codecvt@DDU_Mbstatet@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xB460` | 243 | UnwindData |  |
| 443 | `?_Getcat@?$codecvt@GDU_Mbstatet@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xB560` | 243 | UnwindData |  |
| 444 | `?_Getcat@?$codecvt@_SDU_Mbstatet@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xB660` | 243 | UnwindData |  |
| 445 | `?_Getcat@?$codecvt@_UDU_Mbstatet@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xB760` | 243 | UnwindData |  |
| 446 | `?_Getcat@?$codecvt@_WDU_Mbstatet@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xB860` | 243 | UnwindData |  |
| 447 | `?_Getcat@?$ctype@D@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xB960` | 243 | UnwindData |  |
| 448 | `?_Getcat@?$ctype@G@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xBA60` | 243 | UnwindData |  |
| 449 | `?_Getcat@?$ctype@_W@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0xBB60` | 243 | UnwindData |  |
| 462 | `?_Getcat@facet@locale@std@@SA_KPEAPEBV123@PEBV23@@Z` | `0xBC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `?_Getcoll@_Locinfo@std@@QEBA?AU_Collvec@@XZ` | `0xBC80` | 53 | UnwindData |  |
| 464 | `?_Getctype@_Locinfo@std@@QEBA?AU_Ctypevec@@XZ` | `0xBCC0` | 53 | UnwindData |  |
| 465 | `?_Getcvt@_Locinfo@std@@QEBA?AU_Cvtvec@@XZ` | `0xBD00` | 53 | UnwindData |  |
| 466 | `?_Getdateorder@_Locinfo@std@@QEBAHXZ` | `0xBD40` | 19 | UnwindData |  |
| 467 | `?_Getdays@_Locinfo@std@@QEBAPEBDXZ` | `0xBD60` | 132 | UnwindData |  |
| 468 | `?_Getfalse@_Locinfo@std@@QEBAPEBDXZ` | `0xBEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `?_Getlconv@_Locinfo@std@@QEBAPEBUlconv@@XZ` | `0xBEB0` | 20 | UnwindData |  |
| 486 | `?_Getmonths@_Locinfo@std@@QEBAPEBDXZ` | `0xBED0` | 132 | UnwindData |  |
| 487 | `?_Getname@_Locinfo@std@@QEBAPEBDXZ` | `0xBF60` | 31 | UnwindData |  |
| 488 | `?_Getptr@_Timevec@std@@QEBAPEAXXZ` | `0xBF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 489 | `?_Gettnames@_Locinfo@std@@QEBA?AV_Timevec@2@XZ` | `0xBF90` | 62 | UnwindData |  |
| 490 | `?_Gettrue@_Locinfo@std@@QEBAPEBDXZ` | `0xBFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `?_Gnavail@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBA_JXZ` | `0xBFE0` | 56 | UnwindData |  |
| 494 | `?_Gndec@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAPEADXZ` | `0xC020` | 77 | UnwindData |  |
| 497 | `?_Gninc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAPEADXZ` | `0xC070` | 85 | UnwindData |  |
| 507 | `?_Incref@facet@locale@std@@UEAAXXZ` | `0xC0D0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `?_Init@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXPEAPEAD0PEAH001@Z` | `0xC220` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `?_Init@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXXZ` | `0xC290` | 156 | UnwindData |  |
| 515 | `?_Init@?$codecvt@DDU_Mbstatet@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `?_Init@?$codecvt@GDU_Mbstatet@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC340` | 91 | UnwindData |  |
| 517 | `?_Init@?$codecvt@_SDU_Mbstatet@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `?_Init@?$codecvt@_UDU_Mbstatet@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `?_Init@?$codecvt@_WDU_Mbstatet@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC3C0` | 91 | UnwindData |  |
| 520 | `?_Init@?$ctype@D@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC420` | 57 | UnwindData |  |
| 521 | `?_Init@?$ctype@G@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC460` | 137 | UnwindData |  |
| 522 | `?_Init@?$ctype@_W@std@@IEAAXAEBV_Locinfo@2@@Z` | `0xC4F0` | 137 | UnwindData |  |
| 535 | `?_Init@ios_base@std@@IEAAXXZ` | `0xC580` | 192 | UnwindData |  |
| 561 | `?_Lock@?$basic_streambuf@DU?$char_traits@D@std@@@std@@UEAAXXZ` | `0xC700` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `?_Pnavail@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBA_JXZ` | `0xC990` | 56 | UnwindData |  |
| 595 | `?_Pninc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAPEADXZ` | `0xC9D0` | 85 | UnwindData |  |
| 640 | `?_Tidy@?$_Yarn@D@std@@AEAAXXZ` | `0xCF30` | 57 | UnwindData |  |
| 642 | `?_Tidy@?$_Yarn@_W@std@@AEAAXXZ` | `0xCF70` | 57 | UnwindData |  |
| 643 | `?_Tidy@?$ctype@D@std@@IEAAXXZ` | `0xCFB0` | 95 | UnwindData |  |
| 647 | `?_Tidy@ios_base@std@@AEAAXXZ` | `0xD010` | 193 | UnwindData |  |
| 648 | `?_Unlock@?$basic_streambuf@DU?$char_traits@D@std@@@std@@UEAAXXZ` | `0xD1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | `?_W_Getdays@_Locinfo@std@@QEBAPEBGXZ` | `0xD1E0` | 132 | UnwindData |  |
| 652 | `?_W_Getmonths@_Locinfo@std@@QEBAPEBGXZ` | `0xD270` | 132 | UnwindData |  |
| 653 | `?_W_Gettnames@_Locinfo@std@@QEBA?AV_Timevec@2@XZ` | `0xD300` | 62 | UnwindData |  |
| 678 | `?always_noconv@codecvt_base@std@@QEBA_NXZ` | `0xD410` | 47 | UnwindData |  |
| 679 | `?bad@ios_base@std@@QEBA_NXZ` | `0xD620` | 48 | UnwindData |  |
| 680 | `?c_str@?$_Yarn@D@std@@QEBAPEBDXZ` | `0xD650` | 56 | UnwindData |  |
| 686 | `?classic_table@?$ctype@D@std@@SAPEBFXZ` | `0xD6D0` | 31 | UnwindData |  |
| 687 | `?clear@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXH_N@Z` | `0xD6F0` | 101 | UnwindData |  |
| 693 | `?clear@ios_base@std@@QEAAXH@Z` | `0xD760` | 36 | UnwindData |  |
| 694 | `?clear@ios_base@std@@QEAAXH_N@Z` | `0xD790` | 230 | UnwindData |  |
| 695 | `?clear@ios_base@std@@QEAAXI@Z` | `0xD880` | 33 | UnwindData |  |
| 700 | `?copyfmt@ios_base@std@@QEAAAEAV12@AEBV12@@Z` | `0xD9D0` | 383 | UnwindData |  |
| 705 | `?do_always_noconv@?$codecvt@DDU_Mbstatet@@@std@@MEBA_NXZ` | `0xDD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 706 | `?do_always_noconv@?$codecvt@GDU_Mbstatet@@@std@@MEBA_NXZ` | `0xDD30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `?do_always_noconv@?$codecvt@_SDU_Mbstatet@@@std@@MEBA_NXZ` | `0xDD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 708 | `?do_always_noconv@?$codecvt@_UDU_Mbstatet@@@std@@MEBA_NXZ` | `0xDD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `?do_always_noconv@?$codecvt@_WDU_Mbstatet@@@std@@MEBA_NXZ` | `0xDD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `?do_always_noconv@codecvt_base@std@@MEBA_NXZ` | `0xDD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `?do_encoding@?$codecvt@GDU_Mbstatet@@@std@@MEBAHXZ` | `0xDD80` | 44 | UnwindData |  |
| 715 | `?do_encoding@?$codecvt@_SDU_Mbstatet@@@std@@MEBAHXZ` | `0xDDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `?do_encoding@?$codecvt@_UDU_Mbstatet@@@std@@MEBAHXZ` | `0xDDC0` | 48 | UnwindData |  |
| 717 | `?do_encoding@?$codecvt@_WDU_Mbstatet@@@std@@MEBAHXZ` | `0xDDF0` | 44 | UnwindData |  |
| 718 | `?do_encoding@codecvt_base@std@@MEBAHXZ` | `0xDE20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `?do_in@?$codecvt@DDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAD3AEAPEAD@Z` | `0xDE30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `?do_in@?$codecvt@GDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAG3AEAPEAG@Z` | `0xDE70` | 337 | UnwindData |  |
| 772 | `?do_in@?$codecvt@_SDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_S3AEAPEA_S@Z` | `0xDFD0` | 1,532 | UnwindData |  |
| 773 | `?do_in@?$codecvt@_UDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_U3AEAPEA_U@Z` | `0xE5D0` | 971 | UnwindData |  |
| 774 | `?do_in@?$codecvt@_WDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_W3AEAPEA_W@Z` | `0xE9A0` | 337 | UnwindData |  |
| 775 | `?do_is@?$ctype@G@std@@MEBAPEBGPEBG0PEAF@Z` | `0xEB00` | 76 | UnwindData |  |
| 776 | `?do_is@?$ctype@G@std@@MEBA_NFG@Z` | `0xEB50` | 82 | UnwindData |  |
| 777 | `?do_is@?$ctype@_W@std@@MEBAPEB_WPEB_W0PEAF@Z` | `0xEBB0` | 76 | UnwindData |  |
| 778 | `?do_is@?$ctype@_W@std@@MEBA_NF_W@Z` | `0xEC00` | 82 | UnwindData |  |
| 779 | `?do_length@?$codecvt@DDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0xEC60` | 99 | UnwindData |  |
| 780 | `?do_length@?$codecvt@GDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0xECD0` | 252 | UnwindData |  |
| 781 | `?do_length@?$codecvt@_SDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0xEDD0` | 64 | UnwindData |  |
| 782 | `?do_length@?$codecvt@_UDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0xEE10` | 64 | UnwindData |  |
| 783 | `?do_length@?$codecvt@_WDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0xEE50` | 252 | UnwindData |  |
| 784 | `?do_max_length@?$codecvt@GDU_Mbstatet@@@std@@MEBAHXZ` | `0xEF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `?do_max_length@?$codecvt@_SDU_Mbstatet@@@std@@MEBAHXZ` | `0xEF60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 786 | `?do_max_length@?$codecvt@_UDU_Mbstatet@@@std@@MEBAHXZ` | `0xEFA0` | 48 | UnwindData |  |
| 787 | `?do_max_length@?$codecvt@_WDU_Mbstatet@@@std@@MEBAHXZ` | `0xEFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 788 | `?do_max_length@codecvt_base@std@@MEBAHXZ` | `0xEFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `?do_narrow@?$ctype@D@std@@MEBADDD@Z` | `0xEFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 790 | `?do_narrow@?$ctype@D@std@@MEBAPEBDPEBD0DPEAD@Z` | `0xF010` | 83 | UnwindData |  |
| 791 | `?do_narrow@?$ctype@G@std@@MEBADGD@Z` | `0xF070` | 45 | UnwindData |  |
| 792 | `?do_narrow@?$ctype@G@std@@MEBAPEBGPEBG0DPEAD@Z` | `0xF0A0` | 124 | UnwindData |  |
| 793 | `?do_narrow@?$ctype@_W@std@@MEBAD_WD@Z` | `0xF120` | 45 | UnwindData |  |
| 794 | `?do_narrow@?$ctype@_W@std@@MEBAPEB_WPEB_W0DPEAD@Z` | `0xF150` | 124 | UnwindData |  |
| 795 | `?do_out@?$codecvt@DDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAD3AEAPEAD@Z` | `0xF1D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `?do_out@?$codecvt@GDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEBG1AEAPEBGPEAD3AEAPEAD@Z` | `0xF210` | 560 | UnwindData |  |
| 797 | `?do_out@?$codecvt@_SDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEB_S1AEAPEB_SPEAD3AEAPEAD@Z` | `0xF440` | 884 | UnwindData |  |
| 798 | `?do_out@?$codecvt@_UDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEB_U1AEAPEB_UPEAD3AEAPEAD@Z` | `0xF7C0` | 717 | UnwindData |  |
| 799 | `?do_out@?$codecvt@_WDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEB_W1AEAPEB_WPEAD3AEAPEAD@Z` | `0xFA90` | 560 | UnwindData |  |
| 827 | `?do_scan_is@?$ctype@G@std@@MEBAPEBGFPEBG0@Z` | `0xFCC0` | 109 | UnwindData |  |
| 828 | `?do_scan_is@?$ctype@_W@std@@MEBAPEB_WFPEB_W0@Z` | `0xFD30` | 109 | UnwindData |  |
| 829 | `?do_scan_not@?$ctype@G@std@@MEBAPEBGFPEBG0@Z` | `0xFDA0` | 109 | UnwindData |  |
| 830 | `?do_scan_not@?$ctype@_W@std@@MEBAPEB_WFPEB_W0@Z` | `0xFE10` | 109 | UnwindData |  |
| 831 | `?do_tolower@?$ctype@D@std@@MEBADD@Z` | `0xFE80` | 40 | UnwindData |  |
| 832 | `?do_tolower@?$ctype@D@std@@MEBAPEBDPEADPEBD@Z` | `0xFEB0` | 106 | UnwindData |  |
| 833 | `?do_tolower@?$ctype@G@std@@MEBAGG@Z` | `0xFF20` | 41 | UnwindData |  |
| 834 | `?do_tolower@?$ctype@G@std@@MEBAPEBGPEAGPEBG@Z` | `0xFF50` | 108 | UnwindData |  |
| 835 | `?do_tolower@?$ctype@_W@std@@MEBAPEB_WPEA_WPEB_W@Z` | `0xFFC0` | 108 | UnwindData |  |
| 836 | `?do_tolower@?$ctype@_W@std@@MEBA_W_W@Z` | `0x10030` | 41 | UnwindData |  |
| 837 | `?do_toupper@?$ctype@D@std@@MEBADD@Z` | `0x10060` | 40 | UnwindData |  |
| 838 | `?do_toupper@?$ctype@D@std@@MEBAPEBDPEADPEBD@Z` | `0x10090` | 106 | UnwindData |  |
| 839 | `?do_toupper@?$ctype@G@std@@MEBAGG@Z` | `0x10100` | 41 | UnwindData |  |
| 840 | `?do_toupper@?$ctype@G@std@@MEBAPEBGPEAGPEBG@Z` | `0x10130` | 108 | UnwindData |  |
| 841 | `?do_toupper@?$ctype@_W@std@@MEBAPEB_WPEA_WPEB_W@Z` | `0x101A0` | 108 | UnwindData |  |
| 842 | `?do_toupper@?$ctype@_W@std@@MEBA_W_W@Z` | `0x10210` | 41 | UnwindData |  |
| 843 | `?do_unshift@?$codecvt@DDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x10240` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `?do_unshift@?$codecvt@GDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x10270` | 276 | UnwindData |  |
| 845 | `?do_unshift@?$codecvt@_SDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x10390` | 84 | UnwindData |  |
| 846 | `?do_unshift@?$codecvt@_UDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x103F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `?do_unshift@?$codecvt@_WDU_Mbstatet@@@std@@MEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x10420` | 276 | UnwindData |  |
| 848 | `?do_widen@?$ctype@D@std@@MEBADD@Z` | `0x10540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `?do_widen@?$ctype@D@std@@MEBAPEBDPEBD0PEAD@Z` | `0x10550` | 83 | UnwindData |  |
| 850 | `?do_widen@?$ctype@G@std@@MEBAGD@Z` | `0x105B0` | 33 | UnwindData |  |
| 851 | `?do_widen@?$ctype@G@std@@MEBAPEBDPEBD0PEAG@Z` | `0x105E0` | 119 | UnwindData |  |
| 852 | `?do_widen@?$ctype@_W@std@@MEBAPEBDPEBD0PEA_W@Z` | `0x10660` | 119 | UnwindData |  |
| 853 | `?do_widen@?$ctype@_W@std@@MEBA_WD@Z` | `0x106E0` | 33 | UnwindData |  |
| 854 | `?eback@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x10710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 857 | `?egptr@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x10730` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `?encoding@codecvt_base@std@@QEBAHXZ` | `0x10790` | 47 | UnwindData |  |
| 865 | `?eof@ios_base@std@@QEBA_NXZ` | `0x107D0` | 27 | UnwindData |  |
| 866 | `?epptr@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x107F0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `?exceptions@ios_base@std@@QEAAXH@Z` | `0x10960` | 56 | UnwindData |  |
| 870 | `?exceptions@ios_base@std@@QEAAXI@Z` | `0x109A0` | 33 | UnwindData |  |
| 871 | `?exceptions@ios_base@std@@QEBAHXZ` | `0x109D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `?fail@ios_base@std@@QEBA_NXZ` | `0x109E0` | 48 | UnwindData |  |
| 879 | `?flags@ios_base@std@@QEAAHH@Z` | `0x10A10` | 49 | UnwindData |  |
| 880 | `?flags@ios_base@std@@QEBAHXZ` | `0x10A50` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 884 | `?gbump@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXH@Z` | `0x10AF0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `?getloc@ios_base@std@@QEBA?AVlocale@2@XZ` | `0x10B40` | 43 | UnwindData |  |
| 974 | `?good@ios_base@std@@QEBA_NXZ` | `0x10B70` | 51 | UnwindData |  |
| 975 | `?gptr@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x10BB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `?imbue@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAXAEBVlocale@2@@Z` | `0x10C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `?imbue@ios_base@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x10C10` | 107 | UnwindData |  |
| 1027 | `?in@?$codecvt@DDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAD3AEAPEAD@Z` | `0x10C80` | 145 | UnwindData |  |
| 1028 | `?in@?$codecvt@GDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAG3AEAPEAG@Z` | `0x10D20` | 145 | UnwindData |  |
| 1029 | `?in@?$codecvt@_SDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_S3AEAPEA_S@Z` | `0x10DC0` | 145 | UnwindData |  |
| 1030 | `?in@?$codecvt@_UDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_U3AEAPEA_U@Z` | `0x10E60` | 145 | UnwindData |  |
| 1031 | `?in@?$codecvt@_WDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEA_W3AEAPEA_W@Z` | `0x10F00` | 145 | UnwindData |  |
| 1035 | `?init@?$basic_ios@DU?$char_traits@D@std@@@std@@IEAAXPEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@_N@Z` | `0x10FA0` | 132 | UnwindData |  |
| 1047 | `?is@?$ctype@D@std@@QEBAPEBDPEBD0PEAF@Z` | `0x11040` | 122 | UnwindData |  |
| 1048 | `?is@?$ctype@D@std@@QEBA_NFD@Z` | `0x110C0` | 73 | UnwindData |  |
| 1049 | `?is@?$ctype@G@std@@QEBAPEBGPEBG0PEAF@Z` | `0x11110` | 87 | UnwindData |  |
| 1050 | `?is@?$ctype@G@std@@QEBA_NFG@Z` | `0x11170` | 79 | UnwindData |  |
| 1051 | `?is@?$ctype@_W@std@@QEBAPEB_WPEB_W0PEAF@Z` | `0x111C0` | 87 | UnwindData |  |
| 1052 | `?is@?$ctype@_W@std@@QEBA_NF_W@Z` | `0x11220` | 79 | UnwindData |  |
| 1056 | `?iword@ios_base@std@@QEAAAEAJH@Z` | `0x11280` | 36 | UnwindData |  |
| 1058 | `?length@?$codecvt@GDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0x112D0` | 97 | UnwindData |  |
| 1059 | `?length@?$codecvt@_SDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0x11340` | 97 | UnwindData |  |
| 1060 | `?length@?$codecvt@_UDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0x113B0` | 97 | UnwindData |  |
| 1061 | `?length@?$codecvt@_WDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0x11420` | 97 | UnwindData |  |
| 1062 | `?max_length@codecvt_base@std@@QEBAHXZ` | `0x114C0` | 47 | UnwindData |  |
| 1072 | `?narrow@?$ctype@D@std@@QEBADDD@Z` | `0x117D0` | 77 | UnwindData |  |
| 1073 | `?narrow@?$ctype@D@std@@QEBAPEBDPEBD0DPEAD@Z` | `0x11820` | 98 | UnwindData |  |
| 1074 | `?narrow@?$ctype@G@std@@QEBADGD@Z` | `0x11890` | 78 | UnwindData |  |
| 1075 | `?narrow@?$ctype@G@std@@QEBAPEBGPEBG0DPEAD@Z` | `0x118E0` | 98 | UnwindData |  |
| 1076 | `?narrow@?$ctype@_W@std@@QEBAD_WD@Z` | `0x11950` | 78 | UnwindData |  |
| 1077 | `?narrow@?$ctype@_W@std@@QEBAPEB_WPEB_W0DPEAD@Z` | `0x119A0` | 98 | UnwindData |  |
| 1084 | `?out@?$codecvt@DDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAD3AEAPEAD@Z` | `0x11A60` | 145 | UnwindData |  |
| 1085 | `?out@?$codecvt@GDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBG1AEAPEBGPEAD3AEAPEAD@Z` | `0x11B00` | 145 | UnwindData |  |
| 1086 | `?out@?$codecvt@_SDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEB_S1AEAPEB_SPEAD3AEAPEAD@Z` | `0x11BA0` | 145 | UnwindData |  |
| 1087 | `?out@?$codecvt@_UDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEB_U1AEAPEB_UPEAD3AEAPEAD@Z` | `0x11C40` | 145 | UnwindData |  |
| 1088 | `?out@?$codecvt@_WDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEB_W1AEAPEB_WPEAD3AEAPEAD@Z` | `0x11CE0` | 145 | UnwindData |  |
| 1089 | `?overflow@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHH@Z` | `0x12040` | 23 | UnwindData |  |
| 1092 | `?pbackfail@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHH@Z` | `0x121D0` | 23 | UnwindData |  |
| 1098 | `?pbump@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXH@Z` | `0x121F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `?pptr@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x12240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `?precision@ios_base@std@@QEAA_J_J@Z` | `0x12260` | 50 | UnwindData |  |
| 1108 | `?precision@ios_base@std@@QEBA_JXZ` | `0x122A0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1166 | `?pword@ios_base@std@@QEAAAEAPEAXH@Z` | `0x12370` | 36 | UnwindData |  |
| 1173 | `?rdstate@ios_base@std@@QEBAHXZ` | `0x123A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `?register_callback@ios_base@std@@QEAAXP6AXW4event@12@AEAV12@H@ZH@Z` | `0x123B0` | 115 | UnwindData |  |
| 1185 | `?scan_is@?$ctype@D@std@@QEBAPEBDFPEBD0@Z` | `0x12460` | 108 | UnwindData |  |
| 1186 | `?scan_is@?$ctype@G@std@@QEBAPEBGFPEBG0@Z` | `0x124D0` | 87 | UnwindData |  |
| 1187 | `?scan_is@?$ctype@_W@std@@QEBAPEB_WFPEB_W0@Z` | `0x12530` | 87 | UnwindData |  |
| 1188 | `?scan_not@?$ctype@D@std@@QEBAPEBDFPEBD0@Z` | `0x12590` | 108 | UnwindData |  |
| 1189 | `?scan_not@?$ctype@G@std@@QEBAPEBGFPEBG0@Z` | `0x12600` | 87 | UnwindData |  |
| 1190 | `?scan_not@?$ctype@_W@std@@QEBAPEB_WFPEB_W0@Z` | `0x12660` | 87 | UnwindData |  |
| 1197 | `?seekoff@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA?AV?$fpos@U_Mbstatet@@@2@_JHH@Z` | `0x127C0` | 51 | UnwindData |  |
| 1206 | `?seekpos@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA?AV?$fpos@U_Mbstatet@@@2@V32@H@Z` | `0x128D0` | 51 | UnwindData |  |
| 1214 | `?setbuf@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAPEAV12@PEAD_J@Z` | `0x129C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1217 | `?setf@ios_base@std@@QEAAHH@Z` | `0x129E0` | 61 | UnwindData |  |
| 1218 | `?setf@ios_base@std@@QEAAHHH@Z` | `0x12A20` | 78 | UnwindData |  |
| 1219 | `?setg@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXPEAD00@Z` | `0x12A70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1224 | `?setp@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXPEAD0@Z` | `0x12AD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `?setstate@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXH_N@Z` | `0x12B20` | 56 | UnwindData |  |
| 1236 | `?setstate@ios_base@std@@QEAAXH@Z` | `0x12B60` | 48 | UnwindData |  |
| 1237 | `?setstate@ios_base@std@@QEAAXH_N@Z` | `0x12B90` | 56 | UnwindData |  |
| 1238 | `?setstate@ios_base@std@@QEAAXI@Z` | `0x12BD0` | 33 | UnwindData |  |
| 1246 | `?showmanyc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA_JXZ` | `0x12C00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1282 | `?swap@ios_base@std@@QEAAXAEAV12@@Z` | `0x12C50` | 249 | UnwindData |  |
| 1286 | `?sync@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x12DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `?sync_with_stdio@ios_base@std@@SA_N_N@Z` | `0x12E00` | 74 | UnwindData |  |
| 1290 | `?table@?$ctype@D@std@@QEBAPEBFXZ` | `0x12E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1298 | `?tie@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAPEAV?$basic_ostream@DU?$char_traits@D@std@@@2@PEAV32@@Z` | `0x12E60` | 50 | UnwindData |  |
| 1304 | `?tolower@?$ctype@D@std@@QEBADD@Z` | `0x12EC0` | 66 | UnwindData |  |
| 1305 | `?tolower@?$ctype@D@std@@QEBAPEBDPEADPEBD@Z` | `0x12F10` | 77 | UnwindData |  |
| 1306 | `?tolower@?$ctype@G@std@@QEBAGG@Z` | `0x12F60` | 67 | UnwindData |  |
| 1307 | `?tolower@?$ctype@G@std@@QEBAPEBGPEAGPEBG@Z` | `0x12FB0` | 77 | UnwindData |  |
| 1308 | `?tolower@?$ctype@_W@std@@QEBAPEB_WPEA_WPEB_W@Z` | `0x13000` | 77 | UnwindData |  |
| 1309 | `?tolower@?$ctype@_W@std@@QEBA_W_W@Z` | `0x13050` | 67 | UnwindData |  |
| 1310 | `?toupper@?$ctype@D@std@@QEBADD@Z` | `0x130A0` | 66 | UnwindData |  |
| 1311 | `?toupper@?$ctype@D@std@@QEBAPEBDPEADPEBD@Z` | `0x130F0` | 77 | UnwindData |  |
| 1312 | `?toupper@?$ctype@G@std@@QEBAGG@Z` | `0x13140` | 67 | UnwindData |  |
| 1313 | `?toupper@?$ctype@G@std@@QEBAPEBGPEAGPEBG@Z` | `0x13190` | 77 | UnwindData |  |
| 1314 | `?toupper@?$ctype@_W@std@@QEBAPEB_WPEA_WPEB_W@Z` | `0x131E0` | 77 | UnwindData |  |
| 1315 | `?toupper@?$ctype@_W@std@@QEBA_W_W@Z` | `0x13230` | 67 | UnwindData |  |
| 1316 | `?uflow@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x135F0` | 117 | UnwindData |  |
| 1321 | `?underflow@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAAHXZ` | `0x13760` | 19 | UnwindData |  |
| 1327 | `?unsetf@ios_base@std@@QEAAXH@Z` | `0x13780` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `?unshift@?$codecvt@DDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x137B0` | 97 | UnwindData |  |
| 1329 | `?unshift@?$codecvt@GDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x13820` | 97 | UnwindData |  |
| 1330 | `?unshift@?$codecvt@_SDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x13890` | 97 | UnwindData |  |
| 1331 | `?unshift@?$codecvt@_UDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x13900` | 97 | UnwindData |  |
| 1332 | `?unshift@?$codecvt@_WDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEAD1AEAPEAD@Z` | `0x13970` | 97 | UnwindData |  |
| 1341 | `?widen@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBADD@Z` | `0x13A00` | 97 | UnwindData |  |
| 1344 | `?widen@?$ctype@D@std@@QEBADD@Z` | `0x13A70` | 66 | UnwindData |  |
| 1345 | `?widen@?$ctype@D@std@@QEBAPEBDPEBD0PEAD@Z` | `0x13AC0` | 87 | UnwindData |  |
| 1346 | `?widen@?$ctype@G@std@@QEBAGD@Z` | `0x13B20` | 66 | UnwindData |  |
| 1347 | `?widen@?$ctype@G@std@@QEBAPEBDPEBD0PEAG@Z` | `0x13B70` | 87 | UnwindData |  |
| 1348 | `?widen@?$ctype@_W@std@@QEBAPEBDPEBD0PEA_W@Z` | `0x13BD0` | 87 | UnwindData |  |
| 1349 | `?widen@?$ctype@_W@std@@QEBA_WD@Z` | `0x13C30` | 66 | UnwindData |  |
| 1350 | `?width@ios_base@std@@QEAA_J_J@Z` | `0x13C80` | 50 | UnwindData |  |
| 1351 | `?width@ios_base@std@@QEBA_JXZ` | `0x13CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `?xalloc@ios_base@std@@SAHXZ` | `0x13CD0` | 71 | UnwindData |  |
| 1356 | `?xsgetn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA_JPEAD_J@Z` | `0x13F10` | 303 | UnwindData |  |
| 1359 | `?xsputn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA_JPEBD_J@Z` | `0x14170` | 326 | UnwindData |  |
| 27 | `??0?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@_N@Z` | `0x142C0` | 221 | UnwindData |  |
| 132 | `??1?$basic_istream@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x143F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `??_D?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x14440` | 49 | UnwindData |  |
| 1362 | `_Chmod` | `0x15B60` | 192 | UnwindData |  |
| 1363 | `_Close_dir` | `0x15C20` | 26 | UnwindData |  |
| 1375 | `_Copy_file` | `0x15C40` | 66 | UnwindData |  |
| 1377 | `_Current_get` | `0x15C90` | 75 | UnwindData |  |
| 1378 | `_Current_set` | `0x15CE0` | 52 | UnwindData |  |
| 1381 | `_Equivalent` | `0x15D20` | 417 | UnwindData |  |
| 1391 | `_File_size` | `0x15ED0` | 90 | UnwindData |  |
| 1398 | `_Hard_links` | `0x15F30` | 176 | UnwindData |  |
| 1409 | `_Last_write_time` | `0x15FE0` | 114 | UnwindData |  |
| 1410 | `_Link` | `0x16060` | 66 | UnwindData |  |
| 1412 | `_Lstat` | `0x160B0` | 34 | UnwindData |  |
| 1413 | `_Make_dir` | `0x160E0` | 69 | UnwindData |  |
| 1432 | `_Open_dir` | `0x16130` | 543 | UnwindData |  |
| 1435 | `_Read_dir` | `0x16350` | 256 | UnwindData |  |
| 1436 | `_Remove_dir` | `0x16450` | 53 | UnwindData |  |
| 1437 | `_Rename` | `0x16490` | 63 | UnwindData |  |
| 1438 | `_Resize` | `0x164D0` | 141 | UnwindData |  |
| 1439 | `_Set_last_write_time` | `0x16560` | 156 | UnwindData |  |
| 1442 | `_Stat` | `0x16600` | 388 | UnwindData |  |
| 1443 | `_Statvfs` | `0x16790` | 280 | UnwindData |  |
| 1459 | `_Symlink` | `0x168B0` | 69 | UnwindData |  |
| 1460 | `_Symlink_get` | `0x16900` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1461 | `_Temp_get` | `0x16930` | 116 | UnwindData |  |
| 1474 | `_To_byte` | `0x169B0` | 82 | UnwindData |  |
| 1475 | `_To_wide` | `0x16A10` | 64 | UnwindData |  |
| 1480 | `_Unlink` | `0x16A50` | 53 | UnwindData |  |
| 436 | `?_Fiopen@std@@YAPEAU_iobuf@@PEBDHH@Z` | `0x16CB0` | 42 | UnwindData |  |
| 437 | `?_Fiopen@std@@YAPEAU_iobuf@@PEBGHH@Z` | `0x16CE0` | 42 | UnwindData |  |
| 438 | `?_Fiopen@std@@YAPEAU_iobuf@@PEB_WHH@Z` | `0x16D10` | 42 | UnwindData |  |
| 622 | `?_Rethrow_future_exception@std@@YAXVexception_ptr@1@@Z` | `0x17090` | 67 | UnwindData |  |
| 639 | `?_Throw_future_error@std@@YAXAEBVerror_code@1@@Z` | `0x170E0` | 74 | UnwindData |  |
| 1181 | `?resetiosflags@std@@YA?AU?$_Smanip@H@1@H@Z` | `0x171F0` | 45 | UnwindData |  |
| 1213 | `?setbase@std@@YA?AU?$_Smanip@H@1@H@Z` | `0x172D0` | 45 | UnwindData |  |
| 1222 | `?setiosflags@std@@YA?AU?$_Smanip@H@1@H@Z` | `0x17300` | 45 | UnwindData |  |
| 1229 | `?setprecision@std@@YA?AU?$_Smanip@_J@1@_J@Z` | `0x17330` | 46 | UnwindData |  |
| 1239 | `?setw@std@@YA?AU?$_Smanip@_J@1@_J@Z` | `0x17360` | 46 | UnwindData |  |
| 410 | `?_Addstd@ios_base@std@@SAXPEAV12@@Z` | `0x17420` | 209 | UnwindData |  |
| 545 | `?_Ios_base_dtor@ios_base@std@@CAXPEAV12@@Z` | `0x17500` | 151 | UnwindData |  |
| 412 | `?_Atexit@@YAXP6AXXZ@Z` | `0x17610` | 89 | UnwindData |  |
| 540 | `?_Init_cnt_func@Init@ios_base@std@@CAAEAHXZ` | `0x178B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `?_Init_ctor@Init@ios_base@std@@CAXPEAV123@@Z` | `0x178C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `?_Init_dtor@Init@ios_base@std@@CAXPEAV123@@Z` | `0x178F0` | 106 | UnwindData |  |
| 589 | `?_Osfx@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x17960` | 193 | UnwindData |  |
| 881 | `?flush@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@XZ` | `0x17A30` | 199 | UnwindData |  |
| 1127 | `?pubsync@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x17B00` | 47 | UnwindData |  |
| 1168 | `?rdbuf@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBAPEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@XZ` | `0x17B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `?tie@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBAPEAV?$basic_ostream@DU?$char_traits@D@std@@@2@XZ` | `0x17B40` | 13,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `??0?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x1B1A0` | 76 | UnwindData |  |
| 79 | `??0?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x1B1F0` | 76 | UnwindData |  |
| 149 | `??1?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEAA@XZ` | `0x1B2D0` | 40 | UnwindData |  |
| 152 | `??1?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEAA@XZ` | `0x1B300` | 40 | UnwindData |  |
| 432 | `?_Ffmt@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAPEADPEADDH@Z` | `0x1B8D0` | 367 | UnwindData |  |
| 450 | `?_Getcat@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x1BA40` | 243 | UnwindData |  |
| 453 | `?_Getcat@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x1BB40` | 243 | UnwindData |  |
| 504 | `?_Ifmt@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAPEADPEADPEBDH@Z` | `0x1BD40` | 390 | UnwindData |  |
| 523 | `?_Init@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x1BF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | `?_Init@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x1BF50` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `?_Iput@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEAD_K@Z` | `0x1C140` | 1,859 | UnwindData |  |
| 554 | `?_Locimp_Addfac@_Locimp@locale@std@@CAXPEAV123@PEAVfacet@23@_K@Z` | `0x1C890` | 541 | UnwindData |  |
| 555 | `?_Locimp_ctor@_Locimp@locale@std@@CAXPEAV123@AEBV123@@Z` | `0x1CAB0` | 356 | UnwindData |  |
| 557 | `?_Locinfo_Addcats@_Locinfo@std@@SAAEAV12@PEAV12@HPEBD@Z` | `0x1CC20` | 347 | UnwindData |  |
| 558 | `?_Locinfo_ctor@_Locinfo@std@@SAXPEAV12@HPEBD@Z` | `0x1CD80` | 112 | UnwindData |  |
| 579 | `?_Makeloc@_Locimp@locale@std@@CAPEAV123@AEBV_Locinfo@3@HPEAV123@PEBV23@@Z` | `0x1CDF0` | 1,586 | UnwindData |  |
| 610 | `?_Put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@PEBD_K@Z` | `0x1D4B0` | 139 | UnwindData |  |
| 616 | `?_Rep@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@D_K@Z` | `0x1D540` | 115 | UnwindData |  |
| 719 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x1D980` | 611 | UnwindData |  |
| 720 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x1DBF0` | 212 | UnwindData |  |
| 721 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x1DCD0` | 442 | UnwindData |  |
| 722 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x1DE90` | 442 | UnwindData |  |
| 723 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x1E050` | 420 | UnwindData |  |
| 724 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x1E200` | 420 | UnwindData |  |
| 725 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x1E3B0` | 216 | UnwindData |  |
| 726 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x1E490` | 448 | UnwindData |  |
| 727 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x1E650` | 444 | UnwindData |  |
| 728 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x1E810` | 444 | UnwindData |  |
| 729 | `?do_get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x1E9D0` | 1,003 | UnwindData |  |
| 800 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DJ@Z` | `0x1EE00` | 274 | UnwindData |  |
| 801 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DK@Z` | `0x1EF20` | 274 | UnwindData |  |
| 802 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DN@Z` | `0x1F040` | 760 | UnwindData |  |
| 803 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DO@Z` | `0x1F340` | 759 | UnwindData |  |
| 804 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBX@Z` | `0x1F640` | 231 | UnwindData |  |
| 805 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_J@Z` | `0x1F730` | 274 | UnwindData |  |
| 806 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_K@Z` | `0x1F850` | 274 | UnwindData |  |
| 807 | `?do_put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_N@Z` | `0x1F970` | 1,001 | UnwindData |  |
| 973 | `?global@locale@std@@SA?AV12@AEBV12@@Z` | `0x1FEE0` | 441 | UnwindData |  |
| 1182 | `?sbumpc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x202B0` | 94 | UnwindData |  |
| 1240 | `?sgetc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x20310` | 94 | UnwindData |  |
| 1255 | `?sputc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHD@Z` | `0x20370` | 135 | UnwindData |  |
| 478 | `?_Getgloballocale@locale@std@@CAPEAV_Locimp@12@XZ` | `0x20880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `?_Init@locale@std@@CAPEAV_Locimp@12@_N@Z` | `0x20890` | 287 | UnwindData |  |
| 556 | `?_Locimp_dtor@_Locimp@locale@std@@CAXPEAV123@@Z` | `0x209B0` | 257 | UnwindData |  |
| 559 | `?_Locinfo_ctor@_Locinfo@std@@SAXPEAV12@PEBD@Z` | `0x20AC0` | 170 | UnwindData |  |
| 560 | `?_Locinfo_dtor@_Locinfo@std@@SAXPEAV12@@Z` | `0x20B70` | 67 | UnwindData |  |
| 587 | `?_New_Locimp@_Locimp@locale@std@@CAPEAV123@AEBV123@@Z` | `0x20BC0` | 83 | UnwindData |  |
| 588 | `?_New_Locimp@_Locimp@locale@std@@CAPEAV123@_N@Z` | `0x20C20` | 82 | UnwindData |  |
| 625 | `?_Setgloballocale@locale@std@@CAXPEAX@Z` | `0x20C80` | 57 | UnwindData |  |
| 685 | `?classic@locale@std@@SAAEBV12@XZ` | `0x20CC0` | 68 | UnwindData |  |
| 863 | `?empty@locale@std@@SA?AV12@XZ` | `0x20D10` | 87 | UnwindData |  |
| 575 | `?_MP_Add@std@@YAXQEA_K_K@Z` | `0x20E40` | 99 | UnwindData |  |
| 576 | `?_MP_Get@std@@YA_KQEA_K@Z` | `0x20EB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 577 | `?_MP_Mul@std@@YAXQEA_K_K1@Z` | `0x20EE0` | 490 | UnwindData |  |
| 578 | `?_MP_Rem@std@@YAXQEA_K_K@Z` | `0x210D0` | 1,158 | UnwindData |  |
| 953 | `?get_new_handler@std@@YAP6AXXZXZ` | `0x218A0` | 54 | UnwindData |  |
| 1209 | `?set_new_handler@std@@YAP6AXXZP6AXXZ@Z` | `0x21930` | 122 | UnwindData |  |
| 421 | `?_Debug_message@std@@YAXPEBG0I@Z` | `0x219E0` | 45 | UnwindData |  |
| 422 | `?_Debug_message@std@@YAXPEB_W0I@Z` | `0x21A10` | 76 | UnwindData |  |
| 636 | `?_Syserror_map@std@@YAPEBDH@Z` | `0x21A60` | 117 | UnwindData |  |
| 654 | `?_Winerror_map@std@@YAHH@Z` | `0x21B00` | 111 | UnwindData |  |
| 655 | `?_Winerror_message@std@@YAKKPEADK@Z` | `0x21B70` | 91 | UnwindData |  |
| 1364 | `_Cnd_broadcast` | `0x21E80` | 26 | UnwindData |  |
| 1365 | `_Cnd_destroy` | `0x21EA0` | 39 | UnwindData |  |
| 1366 | `_Cnd_destroy_in_situ` | `0x21ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1368 | `_Cnd_init` | `0x21EE0` | 108 | UnwindData |  |
| 1369 | `_Cnd_init_in_situ` | `0x21F50` | 45 | UnwindData |  |
| 1371 | `_Cnd_signal` | `0x21F80` | 26 | UnwindData |  |
| 1372 | `_Cnd_timedwait` | `0x21FA0` | 220 | UnwindData |  |
| 1374 | `_Cnd_wait` | `0x22080` | 56 | UnwindData |  |
| 1415 | `_Mtx_clear_owner` | `0x220C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1423 | `_Mtx_reset_owner` | `0x220F0` | 46 | UnwindData |  |
| 1463 | `_Thrd_create` | `0x221B0` | 329 | UnwindData |  |
| 1464 | `_Thrd_current` | `0x22300` | 45 | UnwindData |  |
| 1465 | `_Thrd_detach` | `0x22330` | 54 | UnwindData |  |
| 1466 | `_Thrd_equal` | `0x22370` | 56 | UnwindData |  |
| 1467 | `_Thrd_exit` | `0x223B0` | 24 | UnwindData |  |
| 1468 | `_Thrd_hardware_concurrency` | `0x223D0` | 24 | UnwindData |  |
| 1469 | `_Thrd_id` | `0x223F0` | 15 | UnwindData |  |
| 1470 | `_Thrd_join` | `0x22400` | 142 | UnwindData |  |
| 1471 | `_Thrd_sleep` | `0x22490` | 131 | UnwindData |  |
| 1472 | `_Thrd_start` | `0x22520` | 107 | UnwindData |  |
| 1473 | `_Thrd_yield` | `0x22590` | 16 | UnwindData |  |
| 1416 | `_Mtx_current_owns` | `0x225D0` | 63 | UnwindData |  |
| 1417 | `_Mtx_destroy` | `0x22610` | 49 | UnwindData |  |
| 1418 | `_Mtx_destroy_in_situ` | `0x22650` | 40 | UnwindData |  |
| 1419 | `_Mtx_getconcrtcs` | `0x22680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1420 | `_Mtx_init` | `0x22690` | 116 | UnwindData |  |
| 1421 | `_Mtx_init_in_situ` | `0x22710` | 91 | UnwindData |  |
| 1422 | `_Mtx_lock` | `0x22770` | 26 | UnwindData |  |
| 1424 | `_Mtx_timedlock` | `0x22790` | 96 | UnwindData |  |
| 1425 | `_Mtx_trylock` | `0x227F0` | 103 | UnwindData |  |
| 1426 | `_Mtx_unlock` | `0x22860` | 145 | UnwindData |  |
| 1462 | `_Thrd_abort` | `0x22900` | 71 | UnwindData |  |
| 1522 | `__set_stl_sync_api_mode` | `0x22950` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `?ReportUnhandledError@_ExceptionHolder@details@Concurrency@@AEAAXXZ` | `0x22BB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `??0task_continuation_context@Concurrency@@AEAA@XZ` | `0x22C00` | 40 | UnwindData |  |
| 404 | `?CaptureCallstack@platform@details@Concurrency@@YA_KPEAPEAX_K1@Z` | `0x22CD0` | 55 | UnwindData |  |
| 405 | `?GetCurrentThreadId@platform@details@Concurrency@@YAJXZ` | `0x22D10` | 15 | UnwindData |  |
| 406 | `?GetNextAsyncId@platform@details@Concurrency@@YAIXZ` | `0x22D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `?_Assign@_ContextCallback@details@Concurrency@@AEAAXPEAX@Z` | `0x22D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `?_CallInContext@_ContextCallback@details@Concurrency@@QEBAXV?$function@$$A6AXXZ@std@@_N@Z` | `0x22D50` | 46 | UnwindData |  |
| 419 | `?_Capture@_ContextCallback@details@Concurrency@@AEAAXXZ` | `0x22D80` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `?_IsCurrentOriginSTA@_ContextCallback@details@Concurrency@@CA_NXZ` | `0x22DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `?_IsNonBlockingThread@_Task_impl_base@details@Concurrency@@SA_NXZ` | `0x22E00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `?_LogCancelTask@_TaskEventLogger@details@Concurrency@@QEAAXXZ` | `0x22E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `?_LogScheduleTask@_TaskEventLogger@details@Concurrency@@QEAAX_N@Z` | `0x22E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `?_LogTaskCompleted@_TaskEventLogger@details@Concurrency@@QEAAXXZ` | `0x22E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 572 | `?_LogTaskExecutionCompleted@_TaskEventLogger@details@Concurrency@@QEAAXXZ` | `0x22E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 573 | `?_LogWorkItemCompleted@_TaskEventLogger@details@Concurrency@@QEAAXXZ` | `0x22E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `?_LogWorkItemStarted@_TaskEventLogger@details@Concurrency@@QEAAXXZ` | `0x22EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `?_ReportUnobservedException@details@Concurrency@@YAXXZ` | `0x22EB0` | 38 | UnwindData |  |
| 621 | `?_Reset@_ContextCallback@details@Concurrency@@AEAAXXZ` | `0x22EE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 615 | `?_Release_chore@details@Concurrency@@YAXPEAU_Threadpool_chore@12@@Z` | `0x23020` | 51 | UnwindData |  |
| 620 | `?_Reschedule_chore@details@Concurrency@@YAHPEBU_Threadpool_chore@12@@Z` | `0x23060` | 126 | UnwindData |  |
| 624 | `?_Schedule_chore@details@Concurrency@@YAHPEAU_Threadpool_chore@12@@Z` | `0x230E0` | 209 | UnwindData |  |
| 1367 | `_Cnd_do_broadcast_at_thread_exit` | `0x23260` | 343 | UnwindData |  |
| 1370 | `_Cnd_register_at_thread_exit` | `0x233C0` | 350 | UnwindData |  |
| 1373 | `_Cnd_unregister_at_thread_exit` | `0x23520` | 205 | UnwindData |  |
| 1433 | `_Query_perf_counter` | `0x23A20` | 25 | UnwindData |  |
| 1434 | `_Query_perf_frequency` | `0x23A40` | 83 | UnwindData |  |
| 1491 | `_Xtime_diff_to_millis` | `0x23B00` | 67 | UnwindData |  |
| 1492 | `_Xtime_diff_to_millis2` | `0x23B50` | 136 | UnwindData |  |
| 1493 | `_Xtime_get_ticks` | `0x23BE0` | 62 | UnwindData |  |
| 1523 | `xtime_get` | `0x23C20` | 58 | UnwindData |  |
| 637 | `?_Throw_C_error@std@@YAXH@Z` | `0x23D90` | 88 | UnwindData |  |
| 638 | `?_Throw_Cpp_error@std@@YAXH@Z` | `0x23DF0` | 105 | UnwindData |  |
| 1319 | `?uncaught_exception@std@@YA_NXZ` | `0x23ED0` | 14 | UnwindData |  |
| 1320 | `?uncaught_exceptions@std@@YAHXZ` | `0x23EE0` | 14 | UnwindData |  |
| 15 | `??0?$basic_ios@GU?$char_traits@G@std@@@std@@IEAA@XZ` | `0x24280` | 81 | UnwindData |  |
| 41 | `??0?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@_N@Z` | `0x242E0` | 208 | UnwindData |  |
| 51 | `??0?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAA@XZ` | `0x243B0` | 262 | UnwindData |  |
| 127 | `??1?$basic_ios@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x245A0` | 40 | UnwindData |  |
| 136 | `??1?$basic_ostream@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x245D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `??1?$basic_streambuf@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x24620` | 82 | UnwindData |  |
| 207 | `??4_UShinit@std@@QEAAAEAV01@AEBV01@@Z` | `0x24680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `??_D?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x24690` | 49 | UnwindData |  |
| 492 | `?_Gnavail@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBA_JXZ` | `0x248F0` | 56 | UnwindData |  |
| 495 | `?_Gndec@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAPEAGXZ` | `0x24930` | 78 | UnwindData |  |
| 498 | `?_Gninc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAPEAGXZ` | `0x24980` | 86 | UnwindData |  |
| 511 | `?_Init@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXPEAPEAG0PEAH001@Z` | `0x24B10` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `?_Init@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXXZ` | `0x24B80` | 156 | UnwindData |  |
| 562 | `?_Lock@?$basic_streambuf@GU?$char_traits@G@std@@@std@@UEAAXXZ` | `0x24CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `?_Pnavail@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBA_JXZ` | `0x24CC0` | 56 | UnwindData |  |
| 596 | `?_Pninc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAPEAGXZ` | `0x24D00` | 86 | UnwindData |  |
| 649 | `?_Unlock@?$basic_streambuf@GU?$char_traits@G@std@@@std@@UEAAXXZ` | `0x24E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 689 | `?clear@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXH_N@Z` | `0x24E80` | 101 | UnwindData |  |
| 855 | `?eback@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x25010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 858 | `?egptr@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x25030` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `?epptr@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x25070` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `?gbump@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXH@Z` | `0x250E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `?gptr@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x25130` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `?imbue@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAXAEBVlocale@2@@Z` | `0x25180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `?init@?$basic_ios@GU?$char_traits@G@std@@@std@@IEAAXPEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@_N@Z` | `0x25190` | 133 | UnwindData |  |
| 1090 | `?overflow@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAGG@Z` | `0x25570` | 24 | UnwindData |  |
| 1093 | `?pbackfail@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAGG@Z` | `0x25710` | 24 | UnwindData |  |
| 1099 | `?pbump@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXH@Z` | `0x25730` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `?pptr@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x25780` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `?seekoff@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA?AV?$fpos@U_Mbstatet@@@2@_JHH@Z` | `0x258A0` | 51 | UnwindData |  |
| 1207 | `?seekpos@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA?AV?$fpos@U_Mbstatet@@@2@V32@H@Z` | `0x259B0` | 51 | UnwindData |  |
| 1215 | `?setbuf@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAPEAV12@PEAG_J@Z` | `0x25A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `?setg@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXPEAG00@Z` | `0x25AB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `?setp@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXPEAG0@Z` | `0x25B10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `?setstate@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXH_N@Z` | `0x25B60` | 56 | UnwindData |  |
| 1247 | `?showmanyc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA_JXZ` | `0x25BA0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `?sync@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAHXZ` | `0x25C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1300 | `?tie@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAPEAV?$basic_ostream@GU?$char_traits@G@std@@@2@PEAV32@@Z` | `0x25C60` | 50 | UnwindData |  |
| 1317 | `?uflow@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAGXZ` | `0x26040` | 124 | UnwindData |  |
| 1322 | `?underflow@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAAGXZ` | `0x261B0` | 19 | UnwindData |  |
| 1342 | `?widen@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBAGD@Z` | `0x261D0` | 98 | UnwindData |  |
| 1357 | `?xsgetn@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA_JPEAG_J@Z` | `0x26270` | 307 | UnwindData |  |
| 1360 | `?xsputn@?$basic_streambuf@GU?$char_traits@G@std@@@std@@MEAA_JPEBG_J@Z` | `0x263E0` | 334 | UnwindData |  |
| 31 | `??0?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@_N@Z` | `0x26530` | 221 | UnwindData |  |
| 133 | `??1?$basic_istream@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x26660` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `??_D?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x266B0` | 49 | UnwindData |  |
| 114 | `??0_UShinit@std@@QEAA@XZ` | `0x26850` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `??1_UShinit@std@@QEAA@XZ` | `0x269D0` | 106 | UnwindData |  |
| 590 | `?_Osfx@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x26AA0` | 193 | UnwindData |  |
| 882 | `?flush@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@XZ` | `0x26B70` | 199 | UnwindData |  |
| 1128 | `?pubsync@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAHXZ` | `0x26C40` | 47 | UnwindData |  |
| 1170 | `?rdbuf@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBAPEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@XZ` | `0x26C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1301 | `?tie@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBAPEAV?$basic_ostream@GU?$char_traits@G@std@@@2@XZ` | `0x26C80` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??0?$basic_ios@_WU?$char_traits@_W@std@@@std@@IEAA@XZ` | `0x27020` | 81 | UnwindData |  |
| 44 | `??0?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAA@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@_N@Z` | `0x27080` | 208 | UnwindData |  |
| 54 | `??0?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAA@XZ` | `0x27150` | 262 | UnwindData |  |
| 128 | `??1?$basic_ios@_WU?$char_traits@_W@std@@@std@@UEAA@XZ` | `0x27340` | 40 | UnwindData |  |
| 137 | `??1?$basic_ostream@_WU?$char_traits@_W@std@@@std@@UEAA@XZ` | `0x27370` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `??1?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@UEAA@XZ` | `0x273C0` | 82 | UnwindData |  |
| 376 | `??_D?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x27420` | 49 | UnwindData |  |
| 493 | `?_Gnavail@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBA_JXZ` | `0x27680` | 56 | UnwindData |  |
| 496 | `?_Gndec@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAPEA_WXZ` | `0x276C0` | 78 | UnwindData |  |
| 499 | `?_Gninc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAPEA_WXZ` | `0x27710` | 86 | UnwindData |  |
| 513 | `?_Init@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXPEAPEA_W0PEAH001@Z` | `0x278A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `?_Init@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXXZ` | `0x27910` | 156 | UnwindData |  |
| 563 | `?_Lock@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@UEAAXXZ` | `0x27A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `?_Pnavail@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBA_JXZ` | `0x27A50` | 56 | UnwindData |  |
| 597 | `?_Pninc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAPEA_WXZ` | `0x27A90` | 86 | UnwindData |  |
| 650 | `?_Unlock@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@UEAAXXZ` | `0x27C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `?clear@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXH_N@Z` | `0x27C10` | 101 | UnwindData |  |
| 856 | `?eback@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBAPEA_WXZ` | `0x27D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 859 | `?egptr@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBAPEA_WXZ` | `0x27D30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `?epptr@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBAPEA_WXZ` | `0x27D70` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | `?gbump@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXH@Z` | `0x27DE0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 977 | `?gptr@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBAPEA_WXZ` | `0x27E30` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `?imbue@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAXAEBVlocale@2@@Z` | `0x27E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `?init@?$basic_ios@_WU?$char_traits@_W@std@@@std@@IEAAXPEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@2@_N@Z` | `0x27E90` | 133 | UnwindData |  |
| 1091 | `?overflow@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAGG@Z` | `0x28270` | 24 | UnwindData |  |
| 1094 | `?pbackfail@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAGG@Z` | `0x28410` | 24 | UnwindData |  |
| 1100 | `?pbump@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXH@Z` | `0x28430` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `?pptr@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBAPEA_WXZ` | `0x28480` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `?seekoff@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA?AV?$fpos@U_Mbstatet@@@2@_JHH@Z` | `0x285A0` | 51 | UnwindData |  |
| 1208 | `?seekpos@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA?AV?$fpos@U_Mbstatet@@@2@V32@H@Z` | `0x286B0` | 51 | UnwindData |  |
| 1216 | `?setbuf@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAPEAV12@PEA_W_J@Z` | `0x28790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `?setg@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXPEA_W00@Z` | `0x287B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1228 | `?setp@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXPEA_W0@Z` | `0x28810` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `?setstate@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXH_N@Z` | `0x28860` | 56 | UnwindData |  |
| 1248 | `?showmanyc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA_JXZ` | `0x288A0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1288 | `?sync@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAHXZ` | `0x28950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `?tie@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAPEAV?$basic_ostream@_WU?$char_traits@_W@std@@@2@PEAV32@@Z` | `0x28960` | 50 | UnwindData |  |
| 1318 | `?uflow@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAGXZ` | `0x28D40` | 124 | UnwindData |  |
| 1323 | `?underflow@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAAGXZ` | `0x28EB0` | 19 | UnwindData |  |
| 1343 | `?widen@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEBA_WD@Z` | `0x28ED0` | 98 | UnwindData |  |
| 1358 | `?xsgetn@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA_JPEA_W_J@Z` | `0x28F70` | 307 | UnwindData |  |
| 1361 | `?xsputn@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@MEAA_JPEB_W_J@Z` | `0x290E0` | 334 | UnwindData |  |
| 35 | `??0?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@_N@Z` | `0x29230` | 221 | UnwindData |  |
| 134 | `??1?$basic_istream@_WU?$char_traits@_W@std@@@std@@UEAA@XZ` | `0x29360` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `??_D?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x293B0` | 49 | UnwindData |  |
| 115 | `??0_Winit@std@@QEAA@XZ` | `0x29550` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `??1_Winit@std@@QEAA@XZ` | `0x296D0` | 106 | UnwindData |  |
| 591 | `?_Osfx@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x297A0` | 193 | UnwindData |  |
| 883 | `?flush@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@XZ` | `0x29870` | 199 | UnwindData |  |
| 1129 | `?pubsync@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAHXZ` | `0x29940` | 47 | UnwindData |  |
| 1172 | `?rdbuf@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEBAPEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@2@XZ` | `0x29970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `?tie@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEBAPEAV?$basic_ostream@_WU?$char_traits@_W@std@@@2@XZ` | `0x29980` | 15,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??$_Getvals@_W@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAAX_WAEBV_Locinfo@1@@Z` | `0x2D5F0` | 186 | UnwindData |  |
| 75 | `??0?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x34770` | 76 | UnwindData |  |
| 77 | `??0?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x347C0` | 76 | UnwindData |  |
| 81 | `??0?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x34810` | 76 | UnwindData |  |
| 83 | `??0?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x34860` | 76 | UnwindData |  |
| 89 | `??0?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x34970` | 76 | UnwindData |  |
| 92 | `??0?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x349C0` | 76 | UnwindData |  |
| 97 | `??0?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x34A10` | 103 | UnwindData |  |
| 100 | `??0?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x34A80` | 103 | UnwindData |  |
| 150 | `??1?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEAA@XZ` | `0x35140` | 40 | UnwindData |  |
| 151 | `??1?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEAA@XZ` | `0x35170` | 40 | UnwindData |  |
| 153 | `??1?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEAA@XZ` | `0x351A0` | 40 | UnwindData |  |
| 154 | `??1?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEAA@XZ` | `0x351D0` | 40 | UnwindData |  |
| 156 | `??1?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEAA@XZ` | `0x35280` | 51 | UnwindData |  |
| 157 | `??1?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEAA@XZ` | `0x352C0` | 51 | UnwindData |  |
| 159 | `??1?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEAA@XZ` | `0x35300` | 57 | UnwindData |  |
| 160 | `??1?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEAA@XZ` | `0x35340` | 57 | UnwindData |  |
| 433 | `?_Ffmt@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAPEADPEADDH@Z` | `0x37700` | 367 | UnwindData |  |
| 434 | `?_Ffmt@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAPEADPEADDH@Z` | `0x37870` | 367 | UnwindData |  |
| 451 | `?_Getcat@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x387A0` | 243 | UnwindData |  |
| 452 | `?_Getcat@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x388A0` | 243 | UnwindData |  |
| 454 | `?_Getcat@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x389A0` | 243 | UnwindData |  |
| 455 | `?_Getcat@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x38AA0` | 243 | UnwindData |  |
| 457 | `?_Getcat@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x38DA0` | 243 | UnwindData |  |
| 458 | `?_Getcat@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x38EA0` | 243 | UnwindData |  |
| 460 | `?_Getcat@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x38FA0` | 243 | UnwindData |  |
| 461 | `?_Getcat@?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x390A0` | 243 | UnwindData |  |
| 476 | `?_Getfmt@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@PEBD@Z` | `0x391E0` | 720 | UnwindData |  |
| 477 | `?_Getfmt@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@PEBD@Z` | `0x394B0` | 720 | UnwindData |  |
| 483 | `?_Getint@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@0HHAEAHAEBV?$ctype@G@2@@Z` | `0x39780` | 93 | UnwindData |  |
| 484 | `?_Getint@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@0HHAEAHAEBV?$ctype@_W@2@@Z` | `0x397E0` | 93 | UnwindData |  |
| 505 | `?_Ifmt@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAPEADPEADPEBDH@Z` | `0x3BBE0` | 390 | UnwindData |  |
| 506 | `?_Ifmt@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAPEADPEADPEBDH@Z` | `0x3BD70` | 390 | UnwindData |  |
| 524 | `?_Init@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3C800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `?_Init@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3C810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `?_Init@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3C820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `?_Init@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3C830` | 960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `?_Init@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3CBF0` | 123 | UnwindData |  |
| 531 | `?_Init@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3CC70` | 123 | UnwindData |  |
| 533 | `?_Init@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3CCF0` | 83 | UnwindData |  |
| 534 | `?_Init@?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x3CD50` | 83 | UnwindData |  |
| 550 | `?_Iput@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEAD_K@Z` | `0x3CDB0` | 1,854 | UnwindData |  |
| 551 | `?_Iput@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEAD_K@Z` | `0x3D4F0` | 1,854 | UnwindData |  |
| 580 | `?_Makeushloc@_Locimp@locale@std@@CAXAEBV_Locinfo@3@HPEAV123@PEBV23@@Z` | `0x3DC60` | 3,768 | UnwindData |  |
| 581 | `?_Makewloc@_Locimp@locale@std@@CAXAEBV_Locinfo@3@HPEAV123@PEBV23@@Z` | `0x3EB20` | 3,768 | UnwindData |  |
| 611 | `?_Put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@PEBG_K@Z` | `0x3FFC0` | 141 | UnwindData |  |
| 612 | `?_Put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@PEB_W_K@Z` | `0x40050` | 141 | UnwindData |  |
| 617 | `?_Rep@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@G_K@Z` | `0x42620` | 116 | UnwindData |  |
| 618 | `?_Rep@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@_W_K@Z` | `0x426A0` | 116 | UnwindData |  |
| 645 | `?_Tidy@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEAAXXZ` | `0x42D00` | 60 | UnwindData |  |
| 646 | `?_Tidy@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEAAXXZ` | `0x42D40` | 60 | UnwindData |  |
| 703 | `?date_order@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AW4dateorder@time_base@2@XZ` | `0x43A30` | 47 | UnwindData |  |
| 704 | `?date_order@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AW4dateorder@time_base@2@XZ` | `0x43A60` | 47 | UnwindData |  |
| 712 | `?do_date_order@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AW4dateorder@time_base@2@XZ` | `0x43DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | `?do_date_order@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AW4dateorder@time_base@2@XZ` | `0x43DE0` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 730 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x44690` | 611 | UnwindData |  |
| 731 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x44900` | 212 | UnwindData |  |
| 732 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x449E0` | 442 | UnwindData |  |
| 733 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x44BA0` | 442 | UnwindData |  |
| 734 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x44D60` | 420 | UnwindData |  |
| 735 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x44F10` | 420 | UnwindData |  |
| 736 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x450C0` | 216 | UnwindData |  |
| 737 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x451A0` | 448 | UnwindData |  |
| 738 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x45360` | 444 | UnwindData |  |
| 739 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x45520` | 444 | UnwindData |  |
| 740 | `?do_get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x456E0` | 1,003 | UnwindData |  |
| 741 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x45AD0` | 611 | UnwindData |  |
| 742 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x45D40` | 212 | UnwindData |  |
| 743 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x45E20` | 442 | UnwindData |  |
| 744 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x45FE0` | 442 | UnwindData |  |
| 745 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x461A0` | 420 | UnwindData |  |
| 746 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x46350` | 420 | UnwindData |  |
| 747 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x46500` | 216 | UnwindData |  |
| 748 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x465E0` | 448 | UnwindData |  |
| 749 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x467A0` | 444 | UnwindData |  |
| 750 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x46960` | 444 | UnwindData |  |
| 751 | `?do_get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x46B20` | 1,003 | UnwindData |  |
| 753 | `?do_get@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@DD@Z` | `0x46F10` | 3,769 | UnwindData |  |
| 754 | `?do_get@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@DD@Z` | `0x47DD0` | 3,769 | UnwindData |  |
| 756 | `?do_get_date@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x48C90` | 2,660 | UnwindData |  |
| 757 | `?do_get_date@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x49700` | 2,660 | UnwindData |  |
| 759 | `?do_get_monthname@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4A170` | 140 | UnwindData |  |
| 760 | `?do_get_monthname@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4A200` | 140 | UnwindData |  |
| 762 | `?do_get_time@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4A290` | 670 | UnwindData |  |
| 763 | `?do_get_time@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4A530` | 670 | UnwindData |  |
| 765 | `?do_get_weekday@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4A7D0` | 140 | UnwindData |  |
| 766 | `?do_get_weekday@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4A860` | 140 | UnwindData |  |
| 768 | `?do_get_year@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4A8F0` | 316 | UnwindData |  |
| 769 | `?do_get_year@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4AA30` | 316 | UnwindData |  |
| 808 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GJ@Z` | `0x4BAD0` | 275 | UnwindData |  |
| 809 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GK@Z` | `0x4BBF0` | 275 | UnwindData |  |
| 810 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GN@Z` | `0x4BD10` | 761 | UnwindData |  |
| 811 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GO@Z` | `0x4C010` | 760 | UnwindData |  |
| 812 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBX@Z` | `0x4C310` | 232 | UnwindData |  |
| 813 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_J@Z` | `0x4C400` | 275 | UnwindData |  |
| 814 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_K@Z` | `0x4C520` | 275 | UnwindData |  |
| 815 | `?do_put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_N@Z` | `0x4C640` | 1,002 | UnwindData |  |
| 816 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WJ@Z` | `0x4CA30` | 275 | UnwindData |  |
| 817 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WK@Z` | `0x4CB50` | 275 | UnwindData |  |
| 818 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WN@Z` | `0x4CC70` | 761 | UnwindData |  |
| 819 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WO@Z` | `0x4CF70` | 760 | UnwindData |  |
| 820 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEBX@Z` | `0x4D270` | 232 | UnwindData |  |
| 821 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_W_J@Z` | `0x4D360` | 275 | UnwindData |  |
| 822 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_W_K@Z` | `0x4D480` | 275 | UnwindData |  |
| 823 | `?do_put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_W_N@Z` | `0x4D5A0` | 1,002 | UnwindData |  |
| 825 | `?do_put@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBUtm@@DD@Z` | `0x4D990` | 667 | UnwindData |  |
| 826 | `?do_put@?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEBUtm@@DD@Z` | `0x4DC30` | 667 | UnwindData |  |
| 951 | `?get_monthname@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4E660` | 193 | UnwindData |  |
| 952 | `?get_monthname@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4E730` | 193 | UnwindData |  |
| 958 | `?get_weekday@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4E800` | 193 | UnwindData |  |
| 959 | `?get_weekday@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4E8D0` | 193 | UnwindData |  |
| 961 | `?get_year@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4E9A0` | 193 | UnwindData |  |
| 962 | `?get_year@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x4EA70` | 193 | UnwindData |  |
| 1183 | `?sbumpc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x4F6E0` | 97 | UnwindData |  |
| 1184 | `?sbumpc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAGXZ` | `0x4F750` | 97 | UnwindData |  |
| 1241 | `?sgetc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x4F7E0` | 97 | UnwindData |  |
| 1242 | `?sgetc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAGXZ` | `0x4F850` | 97 | UnwindData |  |
| 1256 | `?sputc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGG@Z` | `0x4F8E0` | 142 | UnwindData |  |
| 1257 | `?sputc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAG_W@Z` | `0x4F970` | 142 | UnwindData |  |
| 583 | `?_Mtx_delete@threads@stdext@@YAXPEAX@Z` | `0x4FC80` | 52 | UnwindData |  |
| 584 | `?_Mtx_lock@threads@stdext@@YAXPEAX@Z` | `0x4FCC0` | 26 | UnwindData |  |
| 585 | `?_Mtx_new@threads@stdext@@YAXAEAPEAX@Z` | `0x4FCE0` | 65 | UnwindData |  |
| 586 | `?_Mtx_unlock@threads@stdext@@YAXPEAX@Z` | `0x4FD30` | 26 | UnwindData |  |
| 1376 | `_Cosh` | `0x4FD50` | 293 | UnwindData |  |
| 1395 | `_Getdateorder` | `0x4FE80` | 160 | UnwindData |  |
| 1380 | `_Dtest` | `0x50F80` | 323 | UnwindData |  |
| 1382 | `_Exp` | `0x512C0` | 730 | UnwindData |  |
| 1383 | `_FCosh` | `0x515A0` | 296 | UnwindData |  |
| 1385 | `_FDtest` | `0x52240` | 229 | UnwindData |  |
| 1386 | `_FExp` | `0x52550` | 670 | UnwindData |  |
| 1389 | `_FSinh` | `0x537E0` | 727 | UnwindData |  |
| 1396 | `_Getwctype` | `0x53AC0` | 74 | UnwindData |  |
| 1397 | `_Getwctypes` | `0x53B10` | 77 | UnwindData |  |
| 1401 | `_LCosh` | `0x53B60` | 293 | UnwindData |  |
| 1403 | `_LDtest` | `0x53F20` | 24 | UnwindData |  |
| 1404 | `_LExp` | `0x54040` | 757 | UnwindData |  |
| 657 | `?_XLgamma@std@@YAMM@Z` | `0x54340` | 287 | UnwindData |  |
| 658 | `?_XLgamma@std@@YANN@Z` | `0x54460` | 283 | UnwindData |  |
| 659 | `?_XLgamma@std@@YAOO@Z` | `0x54580` | 283 | UnwindData |  |
| 86 | `??0?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x55C30` | 76 | UnwindData |  |
| 94 | `??0?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@AEBV_Locinfo@1@_K@Z` | `0x55C80` | 103 | UnwindData |  |
| 155 | `??1?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEAA@XZ` | `0x55F00` | 51 | UnwindData |  |
| 158 | `??1?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEAA@XZ` | `0x55F40` | 57 | UnwindData |  |
| 456 | `?_Getcat@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x56E60` | 243 | UnwindData |  |
| 459 | `?_Getcat@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z` | `0x56F60` | 243 | UnwindData |  |
| 475 | `?_Getfmt@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@PEBD@Z` | `0x57060` | 720 | UnwindData |  |
| 482 | `?_Getint@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@0HHAEAHAEBV?$ctype@D@2@@Z` | `0x57330` | 93 | UnwindData |  |
| 529 | `?_Init@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x589A0` | 123 | UnwindData |  |
| 532 | `?_Init@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAXAEBV_Locinfo@2@@Z` | `0x58A20` | 83 | UnwindData |  |
| 582 | `?_Makexloc@_Locimp@locale@std@@CAXAEBV_Locinfo@3@HPEAV123@PEBV23@@Z` | `0x58A80` | 2,288 | UnwindData |  |
| 644 | `?_Tidy@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEAAXXZ` | `0x5A7A0` | 60 | UnwindData |  |
| 702 | `?date_order@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AW4dateorder@time_base@2@XZ` | `0x5AAC0` | 47 | UnwindData |  |
| 711 | `?do_date_order@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AW4dateorder@time_base@2@XZ` | `0x5AC10` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | `?do_get@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@DD@Z` | `0x5B020` | 3,769 | UnwindData |  |
| 755 | `?do_get_date@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5BEE0` | 2,660 | UnwindData |  |
| 758 | `?do_get_monthname@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5C950` | 140 | UnwindData |  |
| 761 | `?do_get_time@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5C9E0` | 670 | UnwindData |  |
| 764 | `?do_get_weekday@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5CC80` | 140 | UnwindData |  |
| 767 | `?do_get_year@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5CD10` | 316 | UnwindData |  |
| 824 | `?do_put@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@MEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBUtm@@DD@Z` | `0x5D5B0` | 661 | UnwindData |  |
| 950 | `?get_monthname@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5DA60` | 193 | UnwindData |  |
| 957 | `?get_weekday@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5DB30` | 193 | UnwindData |  |
| 960 | `?get_year@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x5DC00` | 193 | UnwindData |  |
| 105 | `??0_Init_locks@std@@QEAA@XZ` | `0x5DEC0` | 132 | UnwindData |  |
| 110 | `??0_Lockit@std@@QEAA@H@Z` | `0x5DF50` | 97 | UnwindData |  |
| 111 | `??0_Lockit@std@@QEAA@XZ` | `0x5DFC0` | 80 | UnwindData |  |
| 163 | `??1_Init_locks@std@@QEAA@XZ` | `0x5E010` | 127 | UnwindData |  |
| 166 | `??1_Lockit@std@@QEAA@XZ` | `0x5E090` | 77 | UnwindData |  |
| 543 | `?_Init_locks_ctor@_Init_locks@std@@CAXPEAV12@@Z` | `0x5E0E0` | 127 | UnwindData |  |
| 544 | `?_Init_locks_dtor@_Init_locks@std@@CAXPEAV12@@Z` | `0x5E160` | 127 | UnwindData |  |
| 564 | `?_Lockit_ctor@_Lockit@std@@CAXPEAV12@@Z` | `0x5E1E0` | 45 | UnwindData |  |
| 565 | `?_Lockit_ctor@_Lockit@std@@CAXPEAV12@H@Z` | `0x5E210` | 82 | UnwindData |  |
| 566 | `?_Lockit_ctor@_Lockit@std@@SAXH@Z` | `0x5E270` | 64 | UnwindData |  |
| 567 | `?_Lockit_dtor@_Lockit@std@@CAXPEAV12@@Z` | `0x5E2B0` | 48 | UnwindData |  |
| 568 | `?_Lockit_dtor@_Lockit@std@@SAXH@Z` | `0x5E2E0` | 64 | UnwindData |  |
| 1407 | `_LSinh` | `0x5F540` | 836 | UnwindData |  |
| 1414 | `_Mbrtowc` | `0x5F8E0` | 806 | UnwindData |  |
| 1427 | `_Mtxdst` | `0x5FCB0` | 26 | UnwindData |  |
| 1428 | `_Mtxinit` | `0x5FCD0` | 34 | UnwindData |  |
| 1429 | `_Mtxlock` | `0x5FD00` | 26 | UnwindData |  |
| 1430 | `_Mtxunlock` | `0x5FD20` | 26 | UnwindData |  |
| 431 | `?_Execute_once@std@@YAHAEAUonce_flag@1@P6AHPEAX1PEAPEAX@Z1@Z` | `0x5FF10` | 51 | UnwindData |  |
| 656 | `?_XGetLastError@std@@YAXXZ` | `0x5FF50` | 116 | UnwindData |  |
| 623 | `?_Rng_abort@std@@YAXPEBD@Z` | `0x61340` | 71 | UnwindData |  |
| 614 | `?_Random_device@std@@YAIXZ` | `0x61390` | 41 | UnwindData |  |
| 1440 | `_Sinh` | `0x613C0` | 836 | UnwindData |  |
| 1444 | `_Stod` | `0x61710` | 47 | UnwindData |  |
| 1445 | `_Stodx` | `0x61740` | 940 | UnwindData |  |
| 1446 | `_Stof` | `0x61AF0` | 47 | UnwindData |  |
| 1447 | `_Stofx` | `0x61B20` | 925 | UnwindData |  |
| 1452 | `_Stolx` | `0x624E0` | 377 | UnwindData |  |
| 1448 | `_Stold` | `0x62660` | 47 | UnwindData |  |
| 1449 | `_Stoldx` | `0x62690` | 940 | UnwindData |  |
| 1450 | `_Stoll` | `0x62A40` | 47 | UnwindData |  |
| 1451 | `_Stollx` | `0x62A70` | 413 | UnwindData |  |
| 1453 | `_Stoul` | `0x63010` | 47 | UnwindData |  |
| 1456 | `_Stoulx` | `0x63040` | 917 | UnwindData |  |
| 1454 | `_Stoull` | `0x633E0` | 47 | UnwindData |  |
| 1455 | `_Stoullx` | `0x63410` | 952 | UnwindData |  |
| 1392 | `_Getcoll` | `0x63E90` | 114 | UnwindData |  |
| 1457 | `_Strcoll` | `0x63F10` | 418 | UnwindData |  |
| 1458 | `_Strxfrm` | `0x640C0` | 402 | UnwindData |  |
| 660 | `?_Xbad_alloc@std@@YAXXZ` | `0x64940` | 37 | UnwindData |  |
| 661 | `?_Xbad_function_call@std@@YAXXZ` | `0x64970` | 37 | UnwindData |  |
| 662 | `?_Xinvalid_argument@std@@YAXPEBD@Z` | `0x649A0` | 47 | UnwindData |  |
| 663 | `?_Xlength_error@std@@YAXPEBD@Z` | `0x649D0` | 47 | UnwindData |  |
| 664 | `?_Xout_of_range@std@@YAXPEBD@Z` | `0x64A00` | 47 | UnwindData |  |
| 665 | `?_Xoverflow_error@std@@YAXPEBD@Z` | `0x64A30` | 47 | UnwindData |  |
| 666 | `?_Xregex_error@std@@YAXW4error_type@regex_constants@1@@Z` | `0x64A60` | 45 | UnwindData |  |
| 667 | `?_Xruntime_error@std@@YAXPEBD@Z` | `0x64A90` | 47 | UnwindData |  |
| 1478 | `_Towlower` | `0x64AD0` | 167 | UnwindData |  |
| 1479 | `_Towupper` | `0x64B80` | 167 | UnwindData |  |
| 1489 | `_Wcscoll` | `0x64C30` | 380 | UnwindData |  |
| 1490 | `_Wcsxfrm` | `0x64F40` | 499 | UnwindData |  |
| 1394 | `_Getcvt` | `0x65140` | 263 | UnwindData |  |
| 1488 | `_Wcrtomb` | `0x65250` | 366 | UnwindData |  |
| 1494 | `__Wcrtomb_lk` | `0x653C0` | 54 | UnwindData |  |
| 1482 | `_WStod` | `0x65400` | 47 | UnwindData |  |
| 1483 | `_WStodx` | `0x65430` | 940 | UnwindData |  |
| 1484 | `_WStof` | `0x657E0` | 47 | UnwindData |  |
| 1485 | `_WStofx` | `0x65810` | 925 | UnwindData |  |
| 1486 | `_WStold` | `0x661F0` | 47 | UnwindData |  |
| 1487 | `_WStoldx` | `0x66220` | 940 | UnwindData |  |
| 1495 | `__crtCloseThreadpoolTimer` | `0x67100` | 26 | UnwindData |  |
| 1496 | `__crtCloseThreadpoolWait` | `0x67120` | 26 | UnwindData |  |
| 1500 | `__crtCreateEventExW` | `0x67140` | 55 | UnwindData |  |
| 1501 | `__crtCreateSemaphoreExW` | `0x67180` | 69 | UnwindData |  |
| 1502 | `__crtCreateSymbolicLinkW` | `0x671D0` | 45 | UnwindData |  |
| 1503 | `__crtCreateThreadpoolTimer` | `0x67200` | 45 | UnwindData |  |
| 1504 | `__crtCreateThreadpoolWait` | `0x67230` | 45 | UnwindData |  |
| 1505 | `__crtFlushProcessWriteBuffers` | `0x67260` | 16 | UnwindData |  |
| 1506 | `__crtFreeLibraryWhenCallbackReturns` | `0x67270` | 36 | UnwindData |  |
| 1507 | `__crtGetCurrentProcessorNumber` | `0x672A0` | 15 | UnwindData |  |
| 1508 | `__crtGetFileInformationByHandleEx` | `0x672B0` | 53 | UnwindData |  |
| 1510 | `__crtGetSystemTimePreciseAsFileTime` | `0x672F0` | 85 | UnwindData |  |
| 1511 | `__crtGetTickCount64` | `0x673B0` | 15 | UnwindData |  |
| 1512 | `__crtInitOnceExecuteOnce` | `0x673C0` | 55 | UnwindData |  |
| 1513 | `__crtInitializeCriticalSectionEx` | `0x67400` | 43 | UnwindData |  |
| 1514 | `__crtIsPackagedApp` | `0x67430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1518 | `__crtSetFileInformationByHandle` | `0x67440` | 53 | UnwindData |  |
| 1519 | `__crtSetThreadpoolTimer` | `0x67480` | 56 | UnwindData |  |
| 1520 | `__crtSetThreadpoolWait` | `0x674C0` | 46 | UnwindData |  |
| 1521 | `__crtWaitForThreadpoolTimerCallbacks` | `0x674F0` | 34 | UnwindData |  |
| 1 | `??$_Getvals@_W@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAAX_WAEBV_Locinfo@1@@Z` | `0x6CBE0` | 186 | UnwindData |  |
| 2 | `??$_Getvals@_W@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAAX_WAEBV_Locinfo@1@@Z` | `0x6CCA0` | 186 | UnwindData |  |
| 4 | `??0?$_Yarn@D@std@@QEAA@AEBV01@@Z` | `0x6D020` | 61 | UnwindData |  |
| 7 | `??0?$_Yarn@G@std@@QEAA@AEBV01@@Z` | `0x6D060` | 63 | UnwindData |  |
| 8 | `??0?$_Yarn@G@std@@QEAA@PEBG@Z` | `0x6D0A0` | 63 | UnwindData |  |
| 9 | `??0?$_Yarn@G@std@@QEAA@XZ` | `0x6D0E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0?$_Yarn@_W@std@@QEAA@AEBV01@@Z` | `0x6D110` | 63 | UnwindData |  |
| 11 | `??0?$_Yarn@_W@std@@QEAA@PEB_W@Z` | `0x6D150` | 63 | UnwindData |  |
| 14 | `??0?$basic_ios@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@@Z` | `0x6D190` | 104 | UnwindData |  |
| 16 | `??0?$basic_ios@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@@Z` | `0x6D200` | 106 | UnwindData |  |
| 18 | `??0?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAA@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@@Z` | `0x6D270` | 106 | UnwindData |  |
| 19 | `??0?$basic_iostream@DU?$char_traits@D@std@@@std@@IEAA@$$QEAV01@@Z` | `0x6D2E0` | 361 | UnwindData |  |
| 20 | `??0?$basic_iostream@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@@Z` | `0x6D450` | 223 | UnwindData |  |
| 21 | `??0?$basic_iostream@GU?$char_traits@G@std@@@std@@IEAA@$$QEAV01@@Z` | `0x6D530` | 361 | UnwindData |  |
| 22 | `??0?$basic_iostream@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@@Z` | `0x6D6A0` | 223 | UnwindData |  |
| 23 | `??0?$basic_iostream@_WU?$char_traits@_W@std@@@std@@IEAA@$$QEAV01@@Z` | `0x6D780` | 361 | UnwindData |  |
| 24 | `??0?$basic_iostream@_WU?$char_traits@_W@std@@@std@@QEAA@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@@Z` | `0x6D8F0` | 223 | UnwindData |  |
| 25 | `??0?$basic_istream@DU?$char_traits@D@std@@@std@@IEAA@$$QEAV01@@Z` | `0x6D9D0` | 291 | UnwindData |  |
| 26 | `??0?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@_N1@Z` | `0x6DB00` | 230 | UnwindData |  |
| 28 | `??0?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA@W4_Uninitialized@1@@Z` | `0x6DBF0` | 223 | UnwindData |  |
| 29 | `??0?$basic_istream@GU?$char_traits@G@std@@@std@@IEAA@$$QEAV01@@Z` | `0x6DCD0` | 291 | UnwindData |  |
| 30 | `??0?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@_N1@Z` | `0x6DE00` | 230 | UnwindData |  |
| 32 | `??0?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA@W4_Uninitialized@1@@Z` | `0x6DEF0` | 223 | UnwindData |  |
| 33 | `??0?$basic_istream@_WU?$char_traits@_W@std@@@std@@IEAA@$$QEAV01@@Z` | `0x6DFD0` | 291 | UnwindData |  |
| 34 | `??0?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@_N1@Z` | `0x6E100` | 230 | UnwindData |  |
| 36 | `??0?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA@W4_Uninitialized@1@@Z` | `0x6E1F0` | 223 | UnwindData |  |
| 37 | `??0?$basic_ostream@DU?$char_traits@D@std@@@std@@IEAA@$$QEAV01@@Z` | `0x6E2D0` | 261 | UnwindData |  |
| 39 | `??0?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA@W4_Uninitialized@1@_N@Z` | `0x6E3E0` | 224 | UnwindData |  |
| 40 | `??0?$basic_ostream@GU?$char_traits@G@std@@@std@@IEAA@$$QEAV01@@Z` | `0x6E4C0` | 261 | UnwindData |  |
| 42 | `??0?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA@W4_Uninitialized@1@_N@Z` | `0x6E5D0` | 224 | UnwindData |  |
| 43 | `??0?$basic_ostream@_WU?$char_traits@_W@std@@@std@@IEAA@$$QEAV01@@Z` | `0x6E6B0` | 261 | UnwindData |  |
| 45 | `??0?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAA@W4_Uninitialized@1@_N@Z` | `0x6E7C0` | 224 | UnwindData |  |
| 46 | `??0?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAA@AEBV01@@Z` | `0x6E8A0` | 412 | UnwindData |  |
| 47 | `??0?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAA@W4_Uninitialized@1@@Z` | `0x6EA40` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??0?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAA@AEBV01@@Z` | `0x6EB10` | 412 | UnwindData |  |
| 50 | `??0?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAA@W4_Uninitialized@1@@Z` | `0x6ECB0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??0?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAA@AEBV01@@Z` | `0x6ED80` | 412 | UnwindData |  |
| 53 | `??0?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAA@W4_Uninitialized@1@@Z` | `0x6EF20` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??0?$codecvt@DDU_Mbstatet@@@std@@QEAA@_K@Z` | `0x6EFF0` | 135 | UnwindData |  |
| 74 | `??0?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x6F290` | 121 | UnwindData |  |
| 76 | `??0?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x6F310` | 121 | UnwindData |  |
| 78 | `??0?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@_K@Z` | `0x6F390` | 121 | UnwindData |  |
| 80 | `??0?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x6F410` | 121 | UnwindData |  |
| 82 | `??0?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x6F490` | 121 | UnwindData |  |
| 84 | `??0?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@_K@Z` | `0x6F510` | 121 | UnwindData |  |
| 85 | `??0?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@IEAA@PEBD_K@Z` | `0x6F620` | 127 | UnwindData |  |
| 87 | `??0?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x6F6A0` | 121 | UnwindData |  |
| 88 | `??0?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAA@PEBD_K@Z` | `0x6F720` | 127 | UnwindData |  |
| 90 | `??0?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x6F7A0` | 121 | UnwindData |  |
| 91 | `??0?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAA@PEBD_K@Z` | `0x6F820` | 127 | UnwindData |  |
| 93 | `??0?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@_K@Z` | `0x6F8A0` | 121 | UnwindData |  |
| 95 | `??0?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAA@_K@Z` | `0x6F920` | 151 | UnwindData |  |
| 96 | `??0?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@IEAA@PEBD_K@Z` | `0x6F9C0` | 157 | UnwindData |  |
| 98 | `??0?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAA@_K@Z` | `0x6FA60` | 151 | UnwindData |  |
| 99 | `??0?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@IEAA@PEBD_K@Z` | `0x6FB00` | 157 | UnwindData |  |
| 101 | `??0?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAA@_K@Z` | `0x6FBA0` | 151 | UnwindData |  |
| 124 | `??1?$_Yarn@G@std@@QEAA@XZ` | `0x6FF60` | 25 | UnwindData |  |
| 129 | `??1?$basic_iostream@DU?$char_traits@D@std@@@std@@UEAA@XZ` | `0x6FF80` | 114 | UnwindData |  |
| 130 | `??1?$basic_iostream@GU?$char_traits@G@std@@@std@@UEAA@XZ` | `0x70000` | 114 | UnwindData |  |
| 131 | `??1?$basic_iostream@_WU?$char_traits@_W@std@@@std@@UEAA@XZ` | `0x70080` | 114 | UnwindData |  |
| 183 | `??4?$_Yarn@D@std@@QEAAAEAV01@AEBV01@@Z` | `0x702B0` | 37 | UnwindData |  |
| 185 | `??4?$_Yarn@G@std@@QEAAAEAV01@AEBV01@@Z` | `0x702E0` | 37 | UnwindData |  |
| 186 | `??4?$_Yarn@G@std@@QEAAAEAV01@PEBG@Z` | `0x70310` | 217 | UnwindData |  |
| 187 | `??4?$_Yarn@_W@std@@QEAAAEAV01@AEBV01@@Z` | `0x703F0` | 37 | UnwindData |  |
| 189 | `??4?$basic_iostream@DU?$char_traits@D@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x70420` | 39 | UnwindData |  |
| 190 | `??4?$basic_iostream@GU?$char_traits@G@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x70450` | 39 | UnwindData |  |
| 191 | `??4?$basic_iostream@_WU?$char_traits@_W@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x70480` | 39 | UnwindData |  |
| 192 | `??4?$basic_istream@DU?$char_traits@D@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x704B0` | 39 | UnwindData |  |
| 193 | `??4?$basic_istream@GU?$char_traits@G@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x704E0` | 39 | UnwindData |  |
| 194 | `??4?$basic_istream@_WU?$char_traits@_W@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x70510` | 39 | UnwindData |  |
| 195 | `??4?$basic_ostream@DU?$char_traits@D@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x70540` | 39 | UnwindData |  |
| 196 | `??4?$basic_ostream@GU?$char_traits@G@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x70570` | 39 | UnwindData |  |
| 197 | `??4?$basic_ostream@_WU?$char_traits@_W@std@@@std@@IEAAAEAV01@$$QEAV01@@Z` | `0x705A0` | 39 | UnwindData |  |
| 198 | `??4?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAAEAV01@AEBV01@@Z` | `0x705D0` | 303 | UnwindData |  |
| 199 | `??4?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAAEAV01@AEBV01@@Z` | `0x70700` | 303 | UnwindData |  |
| 200 | `??4?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAAEAV01@AEBV01@@Z` | `0x70830` | 303 | UnwindData |  |
| 209 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAF@Z` | `0x70960` | 758 | UnwindData |  |
| 210 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAG@Z` | `0x70C60` | 34 | UnwindData |  |
| 211 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAH@Z` | `0x70C90` | 61 | UnwindData |  |
| 212 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAI@Z` | `0x70CD0` | 34 | UnwindData |  |
| 213 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAJ@Z` | `0x70D00` | 34 | UnwindData |  |
| 214 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAK@Z` | `0x70D30` | 34 | UnwindData |  |
| 215 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAM@Z` | `0x70D60` | 34 | UnwindData |  |
| 216 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAN@Z` | `0x70D90` | 34 | UnwindData |  |
| 217 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAO@Z` | `0x70DC0` | 34 | UnwindData |  |
| 218 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEAPEAX@Z` | `0x70DF0` | 34 | UnwindData |  |
| 219 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEA_J@Z` | `0x70E20` | 34 | UnwindData |  |
| 220 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEA_K@Z` | `0x70E50` | 34 | UnwindData |  |
| 221 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@AEA_N@Z` | `0x70E80` | 34 | UnwindData |  |
| 222 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0x70EB0` | 55 | UnwindData |  |
| 223 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@DU?$char_traits@D@std@@@1@AEAV21@@Z@Z` | `0x70EF0` | 81 | UnwindData |  |
| 224 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0x70F50` | 81 | UnwindData |  |
| 225 | `??5?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@@Z` | `0x70FB0` | 454 | UnwindData |  |
| 226 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAF@Z` | `0x71180` | 758 | UnwindData |  |
| 227 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAG@Z` | `0x71480` | 34 | UnwindData |  |
| 228 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAH@Z` | `0x714B0` | 61 | UnwindData |  |
| 229 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAI@Z` | `0x714F0` | 34 | UnwindData |  |
| 230 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAJ@Z` | `0x71520` | 34 | UnwindData |  |
| 231 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAK@Z` | `0x71550` | 34 | UnwindData |  |
| 232 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAM@Z` | `0x71580` | 34 | UnwindData |  |
| 233 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAN@Z` | `0x715B0` | 34 | UnwindData |  |
| 234 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAO@Z` | `0x715E0` | 34 | UnwindData |  |
| 235 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEAPEAX@Z` | `0x71610` | 34 | UnwindData |  |
| 236 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEA_J@Z` | `0x71640` | 34 | UnwindData |  |
| 237 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEA_K@Z` | `0x71670` | 34 | UnwindData |  |
| 238 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@AEA_N@Z` | `0x716A0` | 34 | UnwindData |  |
| 239 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0x716D0` | 55 | UnwindData |  |
| 240 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@GU?$char_traits@G@std@@@1@AEAV21@@Z@Z` | `0x71710` | 81 | UnwindData |  |
| 241 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0x71770` | 81 | UnwindData |  |
| 242 | `??5?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@@Z` | `0x717D0` | 430 | UnwindData |  |
| 243 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAF@Z` | `0x71980` | 758 | UnwindData |  |
| 244 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAG@Z` | `0x71C80` | 34 | UnwindData |  |
| 245 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAH@Z` | `0x71CB0` | 61 | UnwindData |  |
| 246 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAI@Z` | `0x71CF0` | 34 | UnwindData |  |
| 247 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAJ@Z` | `0x71D20` | 34 | UnwindData |  |
| 248 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAK@Z` | `0x71D50` | 34 | UnwindData |  |
| 249 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAM@Z` | `0x71D80` | 34 | UnwindData |  |
| 250 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAN@Z` | `0x71DB0` | 34 | UnwindData |  |
| 251 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAO@Z` | `0x71DE0` | 34 | UnwindData |  |
| 252 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEAPEAX@Z` | `0x71E10` | 34 | UnwindData |  |
| 253 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEA_J@Z` | `0x71E40` | 34 | UnwindData |  |
| 254 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEA_K@Z` | `0x71E70` | 34 | UnwindData |  |
| 255 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@AEA_N@Z` | `0x71EA0` | 34 | UnwindData |  |
| 256 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0x71ED0` | 55 | UnwindData |  |
| 257 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@_WU?$char_traits@_W@std@@@1@AEAV21@@Z@Z` | `0x71F10` | 81 | UnwindData |  |
| 258 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0x71F70` | 81 | UnwindData |  |
| 259 | `??5?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@@Z` | `0x71FD0` | 430 | UnwindData |  |
| 260 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@F@Z` | `0x72180` | 650 | UnwindData |  |
| 261 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@G@Z` | `0x72410` | 556 | UnwindData |  |
| 262 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@H@Z` | `0x72640` | 647 | UnwindData |  |
| 263 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@I@Z` | `0x728D0` | 554 | UnwindData |  |
| 264 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@J@Z` | `0x72B00` | 554 | UnwindData |  |
| 265 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@K@Z` | `0x72D30` | 554 | UnwindData |  |
| 266 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@M@Z` | `0x72F60` | 560 | UnwindData |  |
| 267 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@N@Z` | `0x73190` | 560 | UnwindData |  |
| 268 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@O@Z` | `0x733C0` | 560 | UnwindData |  |
| 269 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0x735F0` | 55 | UnwindData |  |
| 270 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@DU?$char_traits@D@std@@@1@AEAV21@@Z@Z` | `0x73630` | 81 | UnwindData |  |
| 271 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0x73690` | 81 | UnwindData |  |
| 272 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@@Z` | `0x736F0` | 531 | UnwindData |  |
| 273 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@PEBX@Z` | `0x73910` | 557 | UnwindData |  |
| 274 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@_J@Z` | `0x73B40` | 557 | UnwindData |  |
| 275 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@_K@Z` | `0x73D70` | 557 | UnwindData |  |
| 276 | `??6?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV01@_N@Z` | `0x73FA0` | 555 | UnwindData |  |
| 277 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@F@Z` | `0x741D0` | 652 | UnwindData |  |
| 278 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@G@Z` | `0x74460` | 558 | UnwindData |  |
| 279 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@H@Z` | `0x74690` | 649 | UnwindData |  |
| 280 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@I@Z` | `0x74920` | 556 | UnwindData |  |
| 281 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@J@Z` | `0x74B50` | 556 | UnwindData |  |
| 282 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@K@Z` | `0x74D80` | 556 | UnwindData |  |
| 283 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@M@Z` | `0x74FB0` | 562 | UnwindData |  |
| 284 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@N@Z` | `0x751F0` | 562 | UnwindData |  |
| 285 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@O@Z` | `0x75430` | 562 | UnwindData |  |
| 286 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0x75670` | 55 | UnwindData |  |
| 287 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@GU?$char_traits@G@std@@@1@AEAV21@@Z@Z` | `0x756B0` | 81 | UnwindData |  |
| 288 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0x75710` | 81 | UnwindData |  |
| 289 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@GU?$char_traits@G@std@@@1@@Z` | `0x75770` | 552 | UnwindData |  |
| 290 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@PEBX@Z` | `0x759A0` | 559 | UnwindData |  |
| 291 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@_J@Z` | `0x75BD0` | 559 | UnwindData |  |
| 292 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@_K@Z` | `0x75E00` | 559 | UnwindData |  |
| 293 | `??6?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV01@_N@Z` | `0x76030` | 557 | UnwindData |  |
| 294 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@F@Z` | `0x76260` | 652 | UnwindData |  |
| 295 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@G@Z` | `0x764F0` | 558 | UnwindData |  |
| 296 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@H@Z` | `0x76720` | 649 | UnwindData |  |
| 297 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@I@Z` | `0x769B0` | 556 | UnwindData |  |
| 298 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@J@Z` | `0x76BE0` | 556 | UnwindData |  |
| 299 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@K@Z` | `0x76E10` | 556 | UnwindData |  |
| 300 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@M@Z` | `0x77040` | 562 | UnwindData |  |
| 301 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@N@Z` | `0x77280` | 562 | UnwindData |  |
| 302 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@O@Z` | `0x774C0` | 562 | UnwindData |  |
| 303 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@P6AAEAV01@AEAV01@@Z@Z` | `0x77700` | 55 | UnwindData |  |
| 304 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@P6AAEAV?$basic_ios@_WU?$char_traits@_W@std@@@1@AEAV21@@Z@Z` | `0x77740` | 81 | UnwindData |  |
| 305 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@P6AAEAVios_base@1@AEAV21@@Z@Z` | `0x777A0` | 81 | UnwindData |  |
| 306 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@PEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@1@@Z` | `0x77800` | 552 | UnwindData |  |
| 307 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@PEBX@Z` | `0x77A30` | 559 | UnwindData |  |
| 308 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@_J@Z` | `0x77C60` | 559 | UnwindData |  |
| 309 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@_K@Z` | `0x77E90` | 559 | UnwindData |  |
| 310 | `??6?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV01@_N@Z` | `0x780C0` | 557 | UnwindData |  |
| 368 | `??_D?$basic_iostream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x78320` | 49 | UnwindData |  |
| 369 | `??_D?$basic_iostream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x78360` | 49 | UnwindData |  |
| 370 | `??_D?$basic_iostream@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x783A0` | 49 | UnwindData |  |
| 377 | `??_F?$codecvt@DDU_Mbstatet@@@std@@QEAAXXZ` | `0x79850` | 27 | UnwindData |  |
| 385 | `??_F?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x79870` | 27 | UnwindData |  |
| 386 | `??_F?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x79890` | 27 | UnwindData |  |
| 387 | `??_F?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAAXXZ` | `0x798B0` | 27 | UnwindData |  |
| 388 | `??_F?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x798D0` | 27 | UnwindData |  |
| 389 | `??_F?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x798F0` | 27 | UnwindData |  |
| 390 | `??_F?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAAXXZ` | `0x79910` | 27 | UnwindData |  |
| 391 | `??_F?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x79930` | 27 | UnwindData |  |
| 392 | `??_F?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x79950` | 27 | UnwindData |  |
| 393 | `??_F?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAAXXZ` | `0x79970` | 27 | UnwindData |  |
| 394 | `??_F?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEAAXXZ` | `0x79990` | 27 | UnwindData |  |
| 395 | `??_F?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEAAXXZ` | `0x799B0` | 27 | UnwindData |  |
| 396 | `??_F?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEAAXXZ` | `0x799D0` | 27 | UnwindData |  |
| 415 | `?_C_str@?$_Yarn@G@std@@QEBAPEBGXZ` | `0x799F0` | 56 | UnwindData |  |
| 429 | `?_Empty@?$_Yarn@G@std@@QEBA_NXZ` | `0x79A30` | 45 | UnwindData |  |
| 439 | `?_Fput@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBD_K@Z` | `0x79A60` | 132 | UnwindData |  |
| 440 | `?_Fput@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBD_K@Z` | `0x79AF0` | 133 | UnwindData |  |
| 441 | `?_Fput@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEBD_K@Z` | `0x79B80` | 133 | UnwindData |  |
| 469 | `?_Getffld@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@1AEAVios_base@2@PEAH@Z` | `0x79C10` | 255 | UnwindData |  |
| 470 | `?_Getffld@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@1AEAVios_base@2@PEAH@Z` | `0x79D10` | 255 | UnwindData |  |
| 471 | `?_Getffld@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@1AEAVios_base@2@PEAH@Z` | `0x79E10` | 255 | UnwindData |  |
| 472 | `?_Getffldx@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@1AEAVios_base@2@PEAH@Z` | `0x79F10` | 255 | UnwindData |  |
| 473 | `?_Getffldx@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@1AEAVios_base@2@PEAH@Z` | `0x7A010` | 255 | UnwindData |  |
| 474 | `?_Getffldx@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@1AEAVios_base@2@PEAH@Z` | `0x7A110` | 255 | UnwindData |  |
| 479 | `?_Getifld@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@1HAEBVlocale@2@@Z` | `0x7A210` | 158 | UnwindData |  |
| 480 | `?_Getifld@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@1HAEBVlocale@2@@Z` | `0x7A2B0` | 158 | UnwindData |  |
| 481 | `?_Getifld@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@1HAEBVlocale@2@@Z` | `0x7A350` | 158 | UnwindData |  |
| 500 | `?_Gnpreinc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAPEADXZ` | `0x7A3F0` | 77 | UnwindData |  |
| 501 | `?_Gnpreinc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAPEAGXZ` | `0x7A440` | 78 | UnwindData |  |
| 502 | `?_Gnpreinc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAPEA_WXZ` | `0x7A490` | 78 | UnwindData |  |
| 546 | `?_Ipfx@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA_N_N@Z` | `0x7A4E0` | 643 | UnwindData |  |
| 547 | `?_Ipfx@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA_N_N@Z` | `0x7A770` | 652 | UnwindData |  |
| 548 | `?_Ipfx@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA_N_N@Z` | `0x7AA00` | 652 | UnwindData |  |
| 641 | `?_Tidy@?$_Yarn@G@std@@AEAAXXZ` | `0x7B2C0` | 57 | UnwindData |  |
| 681 | `?c_str@?$_Yarn@G@std@@QEBAPEBGXZ` | `0x7B300` | 56 | UnwindData |  |
| 682 | `?c_str@?$_Yarn@_W@std@@QEBAPEB_WXZ` | `0x7B340` | 56 | UnwindData |  |
| 688 | `?clear@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXI@Z` | `0x7B380` | 36 | UnwindData |  |
| 690 | `?clear@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXI@Z` | `0x7B3B0` | 36 | UnwindData |  |
| 692 | `?clear@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXI@Z` | `0x7B3E0` | 36 | UnwindData |  |
| 697 | `?copyfmt@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAAEAV12@AEBV12@@Z` | `0x7B410` | 76 | UnwindData |  |
| 698 | `?copyfmt@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAAEAV12@AEBV12@@Z` | `0x7B460` | 77 | UnwindData |  |
| 699 | `?copyfmt@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@AEBV12@@Z` | `0x7B4B0` | 77 | UnwindData |  |
| 860 | `?empty@?$_Yarn@D@std@@QEBA_NXZ` | `0x7B500` | 45 | UnwindData |  |
| 861 | `?empty@?$_Yarn@G@std@@QEBA_NXZ` | `0x7B530` | 45 | UnwindData |  |
| 862 | `?empty@?$_Yarn@_W@std@@QEBA_NXZ` | `0x7B560` | 45 | UnwindData |  |
| 873 | `?fill@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAADD@Z` | `0x7B680` | 47 | UnwindData |  |
| 874 | `?fill@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBADXZ` | `0x7B6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `?fill@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAGG@Z` | `0x7B6C0` | 50 | UnwindData |  |
| 876 | `?fill@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBAGXZ` | `0x7B700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `?fill@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAA_W_W@Z` | `0x7B710` | 50 | UnwindData |  |
| 878 | `?fill@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEBA_WXZ` | `0x7B750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | `?gcount@?$basic_istream@DU?$char_traits@D@std@@@std@@QEBA_JXZ` | `0x7B760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 888 | `?gcount@?$basic_istream@GU?$char_traits@G@std@@@std@@QEBA_JXZ` | `0x7B770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `?gcount@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEBA_JXZ` | `0x7B780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@AEAD@Z` | `0x7B790` | 77 | UnwindData |  |
| 891 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@@Z` | `0x7B7E0` | 78 | UnwindData |  |
| 892 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@D@Z` | `0x7B830` | 469 | UnwindData |  |
| 893 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_J@Z` | `0x7BA10` | 88 | UnwindData |  |
| 894 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_JD@Z` | `0x7BA70` | 566 | UnwindData |  |
| 895 | `?get@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x7BCB0` | 303 | UnwindData |  |
| 896 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@AEAG@Z` | `0x7BDE0` | 82 | UnwindData |  |
| 897 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@@Z` | `0x7BE40` | 78 | UnwindData |  |
| 898 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@G@Z` | `0x7BE90` | 450 | UnwindData |  |
| 899 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_J@Z` | `0x7C060` | 88 | UnwindData |  |
| 900 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_JG@Z` | `0x7C0C0` | 579 | UnwindData |  |
| 901 | `?get@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x7C310` | 311 | UnwindData |  |
| 902 | `?get@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@2@@Z` | `0x7C450` | 78 | UnwindData |  |
| 903 | `?get@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@AEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@2@_W@Z` | `0x7C4A0` | 450 | UnwindData |  |
| 904 | `?get@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@AEA_W@Z` | `0x7C670` | 82 | UnwindData |  |
| 905 | `?get@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@PEA_W_J@Z` | `0x7C6D0` | 88 | UnwindData |  |
| 906 | `?get@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@PEA_W_J_W@Z` | `0x7C730` | 579 | UnwindData |  |
| 907 | `?get@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAGXZ` | `0x7C980` | 311 | UnwindData |  |
| 908 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x7CAC0` | 193 | UnwindData |  |
| 909 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x7CB90` | 193 | UnwindData |  |
| 910 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x7CC60` | 193 | UnwindData |  |
| 911 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x7CD30` | 193 | UnwindData |  |
| 912 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x7CE00` | 193 | UnwindData |  |
| 913 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x7CED0` | 193 | UnwindData |  |
| 914 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x7CFA0` | 193 | UnwindData |  |
| 915 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x7D070` | 193 | UnwindData |  |
| 916 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x7D140` | 193 | UnwindData |  |
| 917 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x7D210` | 193 | UnwindData |  |
| 918 | `?get@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x7D2E0` | 193 | UnwindData |  |
| 919 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x7D3B0` | 193 | UnwindData |  |
| 920 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x7D480` | 193 | UnwindData |  |
| 921 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x7D550` | 193 | UnwindData |  |
| 922 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x7D620` | 193 | UnwindData |  |
| 923 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x7D6F0` | 193 | UnwindData |  |
| 924 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x7D7C0` | 193 | UnwindData |  |
| 925 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x7D890` | 193 | UnwindData |  |
| 926 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x7D960` | 193 | UnwindData |  |
| 927 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x7DA30` | 193 | UnwindData |  |
| 928 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x7DB00` | 193 | UnwindData |  |
| 929 | `?get@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x7DBD0` | 193 | UnwindData |  |
| 930 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAG@Z` | `0x7DCA0` | 193 | UnwindData |  |
| 931 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAI@Z` | `0x7DD70` | 193 | UnwindData |  |
| 932 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAJ@Z` | `0x7DE40` | 193 | UnwindData |  |
| 933 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAK@Z` | `0x7DF10` | 193 | UnwindData |  |
| 934 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAM@Z` | `0x7DFE0` | 193 | UnwindData |  |
| 935 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAN@Z` | `0x7E0B0` | 193 | UnwindData |  |
| 936 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAO@Z` | `0x7E180` | 193 | UnwindData |  |
| 937 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEAPEAX@Z` | `0x7E250` | 193 | UnwindData |  |
| 938 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEA_J@Z` | `0x7E320` | 193 | UnwindData |  |
| 939 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEA_K@Z` | `0x7E3F0` | 193 | UnwindData |  |
| 940 | `?get@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHAEA_N@Z` | `0x7E4C0` | 193 | UnwindData |  |
| 941 | `?get@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@DD@Z` | `0x7E590` | 223 | UnwindData |  |
| 942 | `?get@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@PEBD4@Z` | `0x7E670` | 996 | UnwindData |  |
| 943 | `?get@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@DD@Z` | `0x7EA60` | 223 | UnwindData |  |
| 944 | `?get@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@PEBG4@Z` | `0x7EB40` | 999 | UnwindData |  |
| 945 | `?get@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@DD@Z` | `0x7EF30` | 223 | UnwindData |  |
| 946 | `?get@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@PEB_W4@Z` | `0x7F010` | 999 | UnwindData |  |
| 947 | `?get_date@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x7F400` | 193 | UnwindData |  |
| 948 | `?get_date@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x7F4D0` | 193 | UnwindData |  |
| 949 | `?get_date@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x7F5A0` | 193 | UnwindData |  |
| 954 | `?get_time@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@DU?$char_traits@D@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x7F670` | 193 | UnwindData |  |
| 955 | `?get_time@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@GU?$char_traits@G@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x7F740` | 193 | UnwindData |  |
| 956 | `?get_time@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@0AEAVios_base@2@AEAHPEAUtm@@@Z` | `0x7F810` | 193 | UnwindData |  |
| 963 | `?getline@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_J@Z` | `0x7F8E0` | 88 | UnwindData |  |
| 964 | `?getline@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_JD@Z` | `0x7F940` | 637 | UnwindData |  |
| 965 | `?getline@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_J@Z` | `0x7FBC0` | 88 | UnwindData |  |
| 966 | `?getline@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_JG@Z` | `0x7FC20` | 654 | UnwindData |  |
| 967 | `?getline@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@PEA_W_J@Z` | `0x7FEB0` | 88 | UnwindData |  |
| 968 | `?getline@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@PEA_W_J_W@Z` | `0x7FF10` | 654 | UnwindData |  |
| 969 | `?getloc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEBA?AVlocale@2@XZ` | `0x801A0` | 43 | UnwindData |  |
| 970 | `?getloc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEBA?AVlocale@2@XZ` | `0x801D0` | 43 | UnwindData |  |
| 971 | `?getloc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEBA?AVlocale@2@XZ` | `0x80200` | 43 | UnwindData |  |
| 1017 | `?ignore@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@_JH@Z` | `0x80230` | 347 | UnwindData |  |
| 1018 | `?ignore@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@_JG@Z` | `0x80390` | 360 | UnwindData |  |
| 1019 | `?ignore@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@_JG@Z` | `0x80500` | 360 | UnwindData |  |
| 1020 | `?imbue@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x80670` | 128 | UnwindData |  |
| 1021 | `?imbue@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x806F0` | 128 | UnwindData |  |
| 1022 | `?imbue@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x80770` | 128 | UnwindData |  |
| 1032 | `?in_avail@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA_JXZ` | `0x807F0` | 92 | UnwindData |  |
| 1033 | `?in_avail@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA_JXZ` | `0x80850` | 92 | UnwindData |  |
| 1034 | `?in_avail@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA_JXZ` | `0x808B0` | 92 | UnwindData |  |
| 1044 | `?ipfx@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA_N_N@Z` | `0x80910` | 33 | UnwindData |  |
| 1045 | `?ipfx@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA_N_N@Z` | `0x80940` | 33 | UnwindData |  |
| 1046 | `?ipfx@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA_N_N@Z` | `0x80970` | 33 | UnwindData |  |
| 1053 | `?isfx@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x809A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `?isfx@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x809B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1055 | `?isfx@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x809C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `?length@?$codecvt@DDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1_K@Z` | `0x809D0` | 97 | UnwindData |  |
| 1063 | `?move@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAX$$QEAV12@@Z` | `0x80A40` | 78 | UnwindData |  |
| 1064 | `?move@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXAEAV12@@Z` | `0x80A90` | 78 | UnwindData |  |
| 1065 | `?move@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAX$$QEAV12@@Z` | `0x80AE0` | 78 | UnwindData |  |
| 1066 | `?move@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXAEAV12@@Z` | `0x80B30` | 78 | UnwindData |  |
| 1067 | `?move@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAX$$QEAV12@@Z` | `0x80B80` | 78 | UnwindData |  |
| 1068 | `?move@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXAEAV12@@Z` | `0x80BD0` | 78 | UnwindData |  |
| 1069 | `?narrow@?$basic_ios@DU?$char_traits@D@std@@@std@@QEBADDD@Z` | `0x80C20` | 108 | UnwindData |  |
| 1070 | `?narrow@?$basic_ios@GU?$char_traits@G@std@@@std@@QEBADGD@Z` | `0x80C90` | 109 | UnwindData |  |
| 1071 | `?narrow@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEBAD_WD@Z` | `0x80D00` | 109 | UnwindData |  |
| 1078 | `?opfx@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA_NXZ` | `0x80D70` | 183 | UnwindData |  |
| 1079 | `?opfx@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA_NXZ` | `0x80E30` | 183 | UnwindData |  |
| 1080 | `?opfx@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAA_NXZ` | `0x80EF0` | 183 | UnwindData |  |
| 1081 | `?osfx@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x80FB0` | 25 | UnwindData |  |
| 1082 | `?osfx@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x80FD0` | 25 | UnwindData |  |
| 1083 | `?osfx@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x80FF0` | 25 | UnwindData |  |
| 1095 | `?pbase@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEBAPEADXZ` | `0x81010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `?pbase@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEBAPEAGXZ` | `0x81030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `?pbase@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEBAPEA_WXZ` | `0x81050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `?peek@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x81070` | 259 | UnwindData |  |
| 1102 | `?peek@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x81180` | 270 | UnwindData |  |
| 1103 | `?peek@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAGXZ` | `0x81290` | 270 | UnwindData |  |
| 1109 | `?pubimbue@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x813A0` | 140 | UnwindData |  |
| 1110 | `?pubimbue@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x81430` | 140 | UnwindData |  |
| 1111 | `?pubimbue@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA?AVlocale@2@AEBV32@@Z` | `0x814C0` | 140 | UnwindData |  |
| 1112 | `?pubseekoff@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@_JHH@Z` | `0x81550` | 100 | UnwindData |  |
| 1113 | `?pubseekoff@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@_JII@Z` | `0x815C0` | 67 | UnwindData |  |
| 1114 | `?pubseekoff@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@_JHH@Z` | `0x81610` | 100 | UnwindData |  |
| 1115 | `?pubseekoff@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@_JII@Z` | `0x81680` | 67 | UnwindData |  |
| 1116 | `?pubseekoff@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@_JHH@Z` | `0x816D0` | 100 | UnwindData |  |
| 1117 | `?pubseekoff@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@_JII@Z` | `0x81740` | 67 | UnwindData |  |
| 1118 | `?pubseekpos@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@V32@H@Z` | `0x81790` | 134 | UnwindData |  |
| 1119 | `?pubseekpos@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@V32@I@Z` | `0x81820` | 134 | UnwindData |  |
| 1120 | `?pubseekpos@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@V32@H@Z` | `0x818B0` | 134 | UnwindData |  |
| 1121 | `?pubseekpos@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@V32@I@Z` | `0x81940` | 134 | UnwindData |  |
| 1122 | `?pubseekpos@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@V32@H@Z` | `0x819D0` | 134 | UnwindData |  |
| 1123 | `?pubseekpos@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@V32@I@Z` | `0x81A60` | 134 | UnwindData |  |
| 1124 | `?pubsetbuf@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAPEAV12@PEAD_J@Z` | `0x81AF0` | 77 | UnwindData |  |
| 1125 | `?pubsetbuf@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAPEAV12@PEAG_J@Z` | `0x81B40` | 77 | UnwindData |  |
| 1126 | `?pubsetbuf@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAPEAV12@PEA_W_J@Z` | `0x81B90` | 77 | UnwindData |  |
| 1130 | `?put@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@D@Z` | `0x81BE0` | 248 | UnwindData |  |
| 1131 | `?put@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@G@Z` | `0x81CE0` | 255 | UnwindData |  |
| 1132 | `?put@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@_W@Z` | `0x81DE0` | 255 | UnwindData |  |
| 1133 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DJ@Z` | `0x81EE0` | 157 | UnwindData |  |
| 1134 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DK@Z` | `0x81F80` | 157 | UnwindData |  |
| 1135 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DN@Z` | `0x82020` | 161 | UnwindData |  |
| 1136 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DO@Z` | `0x820D0` | 161 | UnwindData |  |
| 1137 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBX@Z` | `0x82180` | 159 | UnwindData |  |
| 1138 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_J@Z` | `0x82220` | 159 | UnwindData |  |
| 1139 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_K@Z` | `0x822C0` | 159 | UnwindData |  |
| 1140 | `?put@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@D_N@Z` | `0x82360` | 158 | UnwindData |  |
| 1141 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GJ@Z` | `0x82400` | 158 | UnwindData |  |
| 1142 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GK@Z` | `0x824A0` | 158 | UnwindData |  |
| 1143 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GN@Z` | `0x82540` | 162 | UnwindData |  |
| 1144 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GO@Z` | `0x825F0` | 162 | UnwindData |  |
| 1145 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBX@Z` | `0x826A0` | 160 | UnwindData |  |
| 1146 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_J@Z` | `0x82740` | 160 | UnwindData |  |
| 1147 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_K@Z` | `0x827E0` | 160 | UnwindData |  |
| 1148 | `?put@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@G_N@Z` | `0x82880` | 159 | UnwindData |  |
| 1149 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WJ@Z` | `0x82920` | 158 | UnwindData |  |
| 1150 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WK@Z` | `0x829C0` | 158 | UnwindData |  |
| 1151 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WN@Z` | `0x82A60` | 162 | UnwindData |  |
| 1152 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WO@Z` | `0x82B10` | 162 | UnwindData |  |
| 1153 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEBX@Z` | `0x82BC0` | 160 | UnwindData |  |
| 1154 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_W_J@Z` | `0x82C60` | 160 | UnwindData |  |
| 1155 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_W_K@Z` | `0x82D00` | 160 | UnwindData |  |
| 1156 | `?put@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_W_N@Z` | `0x82DA0` | 159 | UnwindData |  |
| 1157 | `?put@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBUtm@@DD@Z` | `0x82E40` | 183 | UnwindData |  |
| 1158 | `?put@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@DU?$char_traits@D@std@@@2@V32@AEAVios_base@2@DPEBUtm@@PEBD3@Z` | `0x82F00` | 1,063 | UnwindData |  |
| 1159 | `?put@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBUtm@@DD@Z` | `0x83330` | 184 | UnwindData |  |
| 1160 | `?put@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@GU?$char_traits@G@std@@@2@V32@AEAVios_base@2@GPEBUtm@@PEBG3@Z` | `0x833F0` | 1,114 | UnwindData |  |
| 1161 | `?put@?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEBUtm@@DD@Z` | `0x83850` | 184 | UnwindData |  |
| 1162 | `?put@?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@QEBA?AV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@2@V32@AEAVios_base@2@_WPEBUtm@@PEB_W4@Z` | `0x83910` | 1,114 | UnwindData |  |
| 1163 | `?putback@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@D@Z` | `0x83D70` | 380 | UnwindData |  |
| 1164 | `?putback@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@G@Z` | `0x83EF0` | 391 | UnwindData |  |
| 1165 | `?putback@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@_W@Z` | `0x84080` | 391 | UnwindData |  |
| 1167 | `?rdbuf@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAPEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@PEAV32@@Z` | `0x84210` | 67 | UnwindData |  |
| 1169 | `?rdbuf@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAPEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@PEAV32@@Z` | `0x84260` | 67 | UnwindData |  |
| 1171 | `?rdbuf@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAPEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@2@PEAV32@@Z` | `0x842B0` | 67 | UnwindData |  |
| 1174 | `?read@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEAD_J@Z` | `0x84300` | 314 | UnwindData |  |
| 1175 | `?read@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEAG_J@Z` | `0x84440` | 314 | UnwindData |  |
| 1176 | `?read@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@PEA_W_J@Z` | `0x84580` | 314 | UnwindData |  |
| 1177 | `?readsome@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA_JPEAD_J@Z` | `0x846C0` | 318 | UnwindData |  |
| 1178 | `?readsome@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA_JPEAG_J@Z` | `0x84800` | 318 | UnwindData |  |
| 1179 | `?readsome@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA_JPEA_W_J@Z` | `0x84940` | 318 | UnwindData |  |
| 1191 | `?seekg@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@V?$fpos@U_Mbstatet@@@2@@Z` | `0x84A80` | 441 | UnwindData |  |
| 1192 | `?seekg@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@_JH@Z` | `0x84C40` | 396 | UnwindData |  |
| 1193 | `?seekg@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@V?$fpos@U_Mbstatet@@@2@@Z` | `0x84DD0` | 441 | UnwindData |  |
| 1194 | `?seekg@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@_JH@Z` | `0x84F90` | 396 | UnwindData |  |
| 1195 | `?seekg@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@V?$fpos@U_Mbstatet@@@2@@Z` | `0x85120` | 441 | UnwindData |  |
| 1196 | `?seekg@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@_JH@Z` | `0x852E0` | 396 | UnwindData |  |
| 1200 | `?seekp@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@V?$fpos@U_Mbstatet@@@2@@Z` | `0x85470` | 341 | UnwindData |  |
| 1201 | `?seekp@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@_JH@Z` | `0x855D0` | 300 | UnwindData |  |
| 1202 | `?seekp@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@V?$fpos@U_Mbstatet@@@2@@Z` | `0x85700` | 341 | UnwindData |  |
| 1203 | `?seekp@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@_JH@Z` | `0x85860` | 300 | UnwindData |  |
| 1204 | `?seekp@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@V?$fpos@U_Mbstatet@@@2@@Z` | `0x85990` | 341 | UnwindData |  |
| 1205 | `?seekp@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@_JH@Z` | `0x85AF0` | 300 | UnwindData |  |
| 1210 | `?set_rdbuf@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXPEAV?$basic_streambuf@DU?$char_traits@D@std@@@2@@Z` | `0x85C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `?set_rdbuf@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXPEAV?$basic_streambuf@GU?$char_traits@G@std@@@2@@Z` | `0x85C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1212 | `?set_rdbuf@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXPEAV?$basic_streambuf@_WU?$char_traits@_W@std@@@2@@Z` | `0x85C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `?setp@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXPEAD00@Z` | `0x85C80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `?setp@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXPEAG00@Z` | `0x85CE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `?setp@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXPEA_W00@Z` | `0x85D40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `?setstate@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXI@Z` | `0x85DA0` | 36 | UnwindData |  |
| 1233 | `?setstate@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXI@Z` | `0x85DD0` | 36 | UnwindData |  |
| 1235 | `?setstate@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXI@Z` | `0x85E00` | 36 | UnwindData |  |
| 1243 | `?sgetn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA_JPEAD_J@Z` | `0x85E30` | 77 | UnwindData |  |
| 1244 | `?sgetn@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA_JPEAG_J@Z` | `0x85E80` | 77 | UnwindData |  |
| 1245 | `?sgetn@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA_JPEA_W_J@Z` | `0x85ED0` | 77 | UnwindData |  |
| 1249 | `?snextc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x85F20` | 134 | UnwindData |  |
| 1250 | `?snextc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x85FB0` | 144 | UnwindData |  |
| 1251 | `?snextc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAGXZ` | `0x86040` | 144 | UnwindData |  |
| 1252 | `?sputbackc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHD@Z` | `0x860D0` | 189 | UnwindData |  |
| 1253 | `?sputbackc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGG@Z` | `0x86190` | 192 | UnwindData |  |
| 1254 | `?sputbackc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAG_W@Z` | `0x86250` | 192 | UnwindData |  |
| 1258 | `?sputn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAA_JPEBD_J@Z` | `0x86310` | 77 | UnwindData |  |
| 1259 | `?sputn@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAA_JPEBG_J@Z` | `0x86360` | 77 | UnwindData |  |
| 1260 | `?sputn@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAA_JPEB_W_J@Z` | `0x863B0` | 77 | UnwindData |  |
| 1261 | `?stossc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAXXZ` | `0x86400` | 76 | UnwindData |  |
| 1262 | `?stossc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAXXZ` | `0x86450` | 76 | UnwindData |  |
| 1263 | `?stossc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAXXZ` | `0x864A0` | 76 | UnwindData |  |
| 1264 | `?sungetc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x864F0` | 152 | UnwindData |  |
| 1265 | `?sungetc@?$basic_streambuf@GU?$char_traits@G@std@@@std@@QEAAGXZ` | `0x86590` | 157 | UnwindData |  |
| 1266 | `?sungetc@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@QEAAGXZ` | `0x86630` | 157 | UnwindData |  |
| 1267 | `?swap@?$basic_ios@DU?$char_traits@D@std@@@std@@QEAAXAEAV12@@Z` | `0x866D0` | 87 | UnwindData |  |
| 1268 | `?swap@?$basic_ios@GU?$char_traits@G@std@@@std@@QEAAXAEAV12@@Z` | `0x86730` | 87 | UnwindData |  |
| 1269 | `?swap@?$basic_ios@_WU?$char_traits@_W@std@@@std@@QEAAXAEAV12@@Z` | `0x86790` | 87 | UnwindData |  |
| 1270 | `?swap@?$basic_iostream@DU?$char_traits@D@std@@@std@@IEAAXAEAV12@@Z` | `0x867F0` | 101 | UnwindData |  |
| 1271 | `?swap@?$basic_iostream@GU?$char_traits@G@std@@@std@@IEAAXAEAV12@@Z` | `0x86860` | 101 | UnwindData |  |
| 1272 | `?swap@?$basic_iostream@_WU?$char_traits@_W@std@@@std@@IEAAXAEAV12@@Z` | `0x868D0` | 101 | UnwindData |  |
| 1273 | `?swap@?$basic_istream@DU?$char_traits@D@std@@@std@@IEAAXAEAV12@@Z` | `0x86940` | 110 | UnwindData |  |
| 1274 | `?swap@?$basic_istream@GU?$char_traits@G@std@@@std@@IEAAXAEAV12@@Z` | `0x869B0` | 110 | UnwindData |  |
| 1275 | `?swap@?$basic_istream@_WU?$char_traits@_W@std@@@std@@IEAAXAEAV12@@Z` | `0x86A20` | 110 | UnwindData |  |
| 1276 | `?swap@?$basic_ostream@DU?$char_traits@D@std@@@std@@IEAAXAEAV12@@Z` | `0x86A90` | 101 | UnwindData |  |
| 1277 | `?swap@?$basic_ostream@GU?$char_traits@G@std@@@std@@IEAAXAEAV12@@Z` | `0x86B00` | 101 | UnwindData |  |
| 1278 | `?swap@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@IEAAXAEAV12@@Z` | `0x86B70` | 101 | UnwindData |  |
| 1279 | `?swap@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IEAAXAEAV12@@Z` | `0x86BE0` | 413 | UnwindData |  |
| 1280 | `?swap@?$basic_streambuf@GU?$char_traits@G@std@@@std@@IEAAXAEAV12@@Z` | `0x86D80` | 413 | UnwindData |  |
| 1281 | `?swap@?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IEAAXAEAV12@@Z` | `0x86F20` | 413 | UnwindData |  |
| 1283 | `?sync@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAHXZ` | `0x870C0` | 266 | UnwindData |  |
| 1284 | `?sync@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAHXZ` | `0x871D0` | 266 | UnwindData |  |
| 1285 | `?sync@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAHXZ` | `0x872E0` | 266 | UnwindData |  |
| 1292 | `?tellg@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@XZ` | `0x873F0` | 197 | UnwindData |  |
| 1293 | `?tellg@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@XZ` | `0x874C0` | 197 | UnwindData |  |
| 1294 | `?tellg@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@XZ` | `0x87590` | 197 | UnwindData |  |
| 1295 | `?tellp@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@XZ` | `0x87660` | 194 | UnwindData |  |
| 1296 | `?tellp@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@XZ` | `0x87730` | 194 | UnwindData |  |
| 1297 | `?tellp@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAA?AV?$fpos@U_Mbstatet@@@2@XZ` | `0x87800` | 194 | UnwindData |  |
| 1324 | `?unget@?$basic_istream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@XZ` | `0x878D0` | 361 | UnwindData |  |
| 1325 | `?unget@?$basic_istream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@XZ` | `0x87A40` | 334 | UnwindData |  |
| 1326 | `?unget@?$basic_istream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@XZ` | `0x87B90` | 334 | UnwindData |  |
| 1352 | `?write@?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAAAEAV12@PEBD_J@Z` | `0x87CE0` | 252 | UnwindData |  |
| 1353 | `?write@?$basic_ostream@GU?$char_traits@G@std@@@std@@QEAAAEAV12@PEBG_J@Z` | `0x87DE0` | 252 | UnwindData |  |
| 1354 | `?write@?$basic_ostream@_WU?$char_traits@_W@std@@@std@@QEAAAEAV12@PEB_W_J@Z` | `0x87EE0` | 252 | UnwindData |  |
| 1291 | `?table_size@?$ctype@D@std@@2_KB` | `0x99378` | 376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `??_7_Facet_base@std@@6B@` | `0x994F0` | 824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `??_7facet@locale@std@@6B@` | `0x99828` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `??_7_Locimp@locale@std@@6B@` | `0x99848` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `??_7codecvt_base@std@@6B@` | `0x99870` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `??_7?$codecvt@_SDU_Mbstatet@@@std@@6B@` | `0x998A8` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `??_7?$codecvt@_UDU_Mbstatet@@@std@@6B@` | `0x99900` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `??_7?$codecvt@_WDU_Mbstatet@@@std@@6B@` | `0x99958` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `??_7?$codecvt@GDU_Mbstatet@@@std@@6B@` | `0x999B0` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `??_7ctype_base@std@@6B@` | `0x99A08` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `??_7?$ctype@D@std@@6B@` | `0x99A28` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `??_7?$ctype@_W@std@@6B@` | `0x99A88` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `??_7?$ctype@G@std@@6B@` | `0x99B08` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `??_7ios_base@std@@6B@` | `0x99BA0` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `??_7time_base@std@@6B@` | `0x99BF8` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `??_7?$basic_ios@DU?$char_traits@D@std@@@std@@6B@` | `0x99C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `??_7?$basic_ostream@DU?$char_traits@D@std@@@std@@6B@` | `0x99C80` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `??_8?$basic_ostream@DU?$char_traits@D@std@@@std@@7B@` | `0x99C88` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `??_7?$basic_streambuf@DU?$char_traits@D@std@@@std@@6B@` | `0x99C98` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `??_7?$codecvt@DDU_Mbstatet@@@std@@6B@` | `0x99E08` | 200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `??_7?$basic_istream@DU?$char_traits@D@std@@@std@@6B@` | `0x99ED0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `??_8?$basic_istream@DU?$char_traits@D@std@@@std@@7B@` | `0x99ED8` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `?_BADOFF@std@@3_JB` | `0x9A1B8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `??_7?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x9A1C8` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `??_7?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x9A240` | 5,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `??_7?$basic_streambuf@GU?$char_traits@G@std@@@std@@6B@` | `0x9B7C0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `??_7?$basic_ios@GU?$char_traits@G@std@@@std@@6B@` | `0x9B8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `??_7?$basic_ostream@GU?$char_traits@G@std@@@std@@6B@` | `0x9B8D0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `??_8?$basic_ostream@GU?$char_traits@G@std@@@std@@7B@` | `0x9B8D8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `??_7?$basic_istream@GU?$char_traits@G@std@@@std@@6B@` | `0x9B8E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `??_8?$basic_istream@GU?$char_traits@G@std@@@std@@7B@` | `0x9B8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `??_7?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@6B@` | `0x9B900` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `??_7?$basic_ios@_WU?$char_traits@_W@std@@@std@@6B@` | `0x9BA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `??_7?$basic_ostream@_WU?$char_traits@_W@std@@@std@@6B@` | `0x9BA10` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `??_8?$basic_ostream@_WU?$char_traits@_W@std@@@std@@7B@` | `0x9BA18` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `??_7?$basic_istream@_WU?$char_traits@_W@std@@@std@@6B@` | `0x9BA28` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `??_8?$basic_istream@_WU?$char_traits@_W@std@@@std@@7B@` | `0x9BA30` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `??_7?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@6B@` | `0x9BAD8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `??_7?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@6B@` | `0x9BB00` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `??_7?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@6B@` | `0x9BB78` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `??_7?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@6B@` | `0x9BE28` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `??_7?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x9BE80` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `??_7?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x9BEF8` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `??_7?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x9C1A8` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `??_7?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@6B@` | `0x9C200` | 3,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `??_7?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x9CDB8` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `??_7?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@6B@` | `0x9CE10` | 2,806 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `?intl@?$moneypunct@D$00@std@@2_NB` | `0x9D906` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `?intl@?$moneypunct@D$0A@@std@@2_NB` | `0x9D907` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1042 | `?intl@?$moneypunct@_W$00@std@@2_NB` | `0x9D908` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1043 | `?intl@?$moneypunct@_W$0A@@std@@2_NB` | `0x9D909` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1040 | `?intl@?$moneypunct@G$00@std@@2_NB` | `0x9D90A` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | `?intl@?$moneypunct@G$0A@@std@@2_NB` | `0x9D90B` | 13 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `??_7?$basic_iostream@DU?$char_traits@D@std@@@std@@6B@` | `0x9D918` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `??_8?$basic_iostream@DU?$char_traits@D@std@@@std@@7B?$basic_istream@DU?$char_traits@D@std@@@1@@` | `0x9D920` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `??_8?$basic_iostream@DU?$char_traits@D@std@@@std@@7B?$basic_ostream@DU?$char_traits@D@std@@@1@@` | `0x9D928` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `??_7?$basic_iostream@_WU?$char_traits@_W@std@@@std@@6B@` | `0x9D938` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `??_8?$basic_iostream@_WU?$char_traits@_W@std@@@std@@7B?$basic_istream@_WU?$char_traits@_W@std@@@1@@` | `0x9D940` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `??_8?$basic_iostream@_WU?$char_traits@_W@std@@@std@@7B?$basic_ostream@_WU?$char_traits@_W@std@@@1@@` | `0x9D948` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `??_7?$basic_iostream@GU?$char_traits@G@std@@@std@@6B@` | `0x9D958` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `??_8?$basic_iostream@GU?$char_traits@G@std@@@std@@7B?$basic_istream@GU?$char_traits@G@std@@@1@@` | `0x9D960` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `??_8?$basic_iostream@GU?$char_traits@G@std@@@std@@7B?$basic_ostream@GU?$char_traits@G@std@@@1@@` | `0x9D968` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `?_Src@?1??_Getffldx@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@3@1AEAVios_base@3@PEAH@Z@4QBDB` | `0x9D998` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 627 | `?_Src@?1??_Getffld@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@3@1AEAVios_base@3@PEAH@Z@4QBDB` | `0x9D9B8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `?_Src@?1??_Getifld@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@GU?$char_traits@G@std@@@3@1HAEBVlocale@3@@Z@4QBDB` | `0x9D9C8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | `?_Src@?1??_Getffldx@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@3@1AEAVios_base@3@PEAH@Z@4QBDB` | `0x9D9E8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 628 | `?_Src@?1??_Getffld@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@3@1AEAVios_base@3@PEAH@Z@4QBDB` | `0x9DA08` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 634 | `?_Src@?1??_Getifld@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@3@1HAEBVlocale@3@@Z@4QBDB` | `0x9DA18` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 629 | `?_Src@?1??_Getffldx@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@3@1AEAVios_base@3@PEAH@Z@4QBDB` | `0x9DA38` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 626 | `?_Src@?1??_Getffld@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@3@1AEAVios_base@3@PEAH@Z@4QBDB` | `0x9DA58` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 632 | `?_Src@?1??_Getifld@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@AEBAHPEADAEAV?$istreambuf_iterator@DU?$char_traits@D@std@@@3@1HAEBVlocale@3@@Z@4QBDB` | `0x9DA68` | 206,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 635 | `?_Sync@ios_base@std@@0_NA` | `0xD00B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `?_Init_cnt@Init@ios_base@std@@0HA` | `0xD00C0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | `?_Init_cnt@_UShinit@std@@0HA` | `0xD0180` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `?_Init_cnt@_Winit@std@@0HA` | `0xD0184` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `_FDenorm` | `0xD0188` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `_FInf` | `0xD0198` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1388 | `_FNan` | `0xD01A8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1390 | `_FSnan` | `0xD01B8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `_LDenorm` | `0xD01D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1405 | `_LInf` | `0xD01E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1406 | `_LNan` | `0xD01F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `_LSnan` | `0xD0200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1379 | `_Denorm` | `0xD0220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1399 | `_Hugeval` | `0xD0230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1400 | `_Inf` | `0xD0240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `_Nan` | `0xD0250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1441 | `_Snan` | `0xD0260` | 6,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `?cerr@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A` | `0xD1C30` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `?id@?$codecvt@DDU_Mbstatet@@@std@@2V0locale@2@A` | `0xD1D40` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `?cin@std@@3V?$basic_istream@DU?$char_traits@D@std@@@1@A` | `0xD1E10` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 696 | `?clog@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A` | `0xD1F40` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 701 | `?cout@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A` | `0xD1FC0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `?_Index@ios_base@std@@0HA` | `0xD20D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 599 | `?_Ptr_cin@std@@3PEAV?$basic_istream@DU?$char_traits@D@std@@@1@EA` | `0xD2140` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `?_Ptr_cout@std@@3PEAV?$basic_ostream@DU?$char_traits@D@std@@@1@EA` | `0xD2148` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `?_Ptr_cerr@std@@3PEAV?$basic_ostream@DU?$char_traits@D@std@@@1@EA` | `0xD2150` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 600 | `?_Ptr_clog@std@@3PEAV?$basic_ostream@DU?$char_traits@D@std@@@1@EA` | `0xD2158` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `?_Ptr_wcin@std@@3PEAV?$basic_istream@_WU?$char_traits@_W@std@@@1@EA` | `0xD2160` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `?_Ptr_wcout@std@@3PEAV?$basic_ostream@_WU?$char_traits@_W@std@@@1@EA` | `0xD2168` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `?_Ptr_wcerr@std@@3PEAV?$basic_ostream@_WU?$char_traits@_W@std@@@1@EA` | `0xD2170` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `?_Ptr_wclog@std@@3PEAV?$basic_ostream@_WU?$char_traits@_W@std@@@1@EA` | `0xD2178` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `?id@?$num_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0xD21E8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `?id@?$num_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0xD21F0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1008 | `?id@?$numpunct@D@std@@2V0locale@2@A` | `0xD21F8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `?_Id_cnt@id@locale@std@@0HA` | `0xD2218` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `?_Clocptr@_Locimp@locale@std@@0PEAV123@EA` | `0xD2220` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `?id@?$ctype@_W@std@@2V0locale@2@A` | `0xD2228` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 984 | `?id@?$ctype@D@std@@2V0locale@2@A` | `0xD2230` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 979 | `?id@?$codecvt@GDU_Mbstatet@@@std@@2V0locale@2@A` | `0xD2238` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `?id@?$ctype@G@std@@2V0locale@2@A` | `0xD2240` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `?id@?$codecvt@_WDU_Mbstatet@@@std@@2V0locale@2@A` | `0xD2258` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 613 | `?_Raise_handler@std@@3P6AXAEBVexception@stdext@@@ZEA` | `0xD2280` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1333 | `?wcerr@std@@3V?$basic_ostream@GU?$char_traits@G@std@@@1@A` | `0xD25F0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1335 | `?wcin@std@@3V?$basic_istream@GU?$char_traits@G@std@@@1@A` | `0xD27C0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `?wclog@std@@3V?$basic_ostream@GU?$char_traits@G@std@@@1@A` | `0xD2850` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1339 | `?wcout@std@@3V?$basic_ostream@GU?$char_traits@G@std@@@1@A` | `0xD2970` | 264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 604 | `?_Ptr_wcin@std@@3PEAV?$basic_istream@GU?$char_traits@G@std@@@1@EA` | `0xD2A78` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `?_Ptr_wcout@std@@3PEAV?$basic_ostream@GU?$char_traits@G@std@@@1@EA` | `0xD2A80` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `?_Ptr_wcerr@std@@3PEAV?$basic_ostream@GU?$char_traits@G@std@@@1@EA` | `0xD2A88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `?_Ptr_wclog@std@@3PEAV?$basic_ostream@GU?$char_traits@G@std@@@1@EA` | `0xD2A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `?wcerr@std@@3V?$basic_ostream@_WU?$char_traits@_W@std@@@1@A` | `0xD2AB0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1336 | `?wcin@std@@3V?$basic_istream@_WU?$char_traits@_W@std@@@1@A` | `0xD2C80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `?wclog@std@@3V?$basic_ostream@_WU?$char_traits@_W@std@@@1@A` | `0xD2D10` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1340 | `?wcout@std@@3V?$basic_ostream@_WU?$char_traits@_W@std@@@1@A` | `0xD2E30` | 264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `?id@?$time_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@2V0locale@2@A` | `0xD2F38` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `?id@?$num_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@2V0locale@2@A` | `0xD2F40` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `?id@?$num_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@2V0locale@2@A` | `0xD2F48` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `?id@?$numpunct@_W@std@@2V0locale@2@A` | `0xD2F50` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 983 | `?id@?$collate@_W@std@@2V0locale@2@A` | `0xD2F58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `?id@?$messages@_W@std@@2V0locale@2@A` | `0xD2F60` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `?id@?$money_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@2V0locale@2@A` | `0xD2F68` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 995 | `?id@?$money_put@_WV?$ostreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@2V0locale@2@A` | `0xD2F70` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `?id@?$moneypunct@_W$0A@@std@@2V0locale@2@A` | `0xD2F78` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `?id@?$moneypunct@_W$00@std@@2V0locale@2@A` | `0xD2F80` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | `?id@?$time_get@_WV?$istreambuf_iterator@_WU?$char_traits@_W@std@@@std@@@std@@2V0locale@2@A` | `0xD2F88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `?id@?$num_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0xD2F90` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `?id@?$num_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0xD2F98` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `?id@?$numpunct@G@std@@2V0locale@2@A` | `0xD2FA0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 982 | `?id@?$collate@G@std@@2V0locale@2@A` | `0xD2FA8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `?id@?$messages@G@std@@2V0locale@2@A` | `0xD2FB0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `?id@?$money_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0xD2FB8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 994 | `?id@?$money_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0xD2FC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `?id@?$moneypunct@G$0A@@std@@2V0locale@2@A` | `0xD2FC8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `?id@?$moneypunct@G$00@std@@2V0locale@2@A` | `0xD2FD0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `?id@?$time_get@GV?$istreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0xD2FD8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `?id@?$time_put@GV?$ostreambuf_iterator@GU?$char_traits@G@std@@@std@@@std@@2V0locale@2@A` | `0xD2FE0` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `?id@?$collate@D@std@@2V0locale@2@A` | `0xD3098` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 987 | `?id@?$messages@D@std@@2V0locale@2@A` | `0xD30A0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `?id@?$money_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0xD30A8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `?id@?$money_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0xD30B0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 997 | `?id@?$moneypunct@D$0A@@std@@2V0locale@2@A` | `0xD30B8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `?id@?$moneypunct@D$00@std@@2V0locale@2@A` | `0xD30C0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `?id@?$time_get@DV?$istreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0xD30C8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `?id@?$time_put@DV?$ostreambuf_iterator@DU?$char_traits@D@std@@@std@@@std@@2V0locale@2@A` | `0xD30D0` | 0 | Indeterminate |  |
