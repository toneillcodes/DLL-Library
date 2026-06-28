# Binary Specification: framedynos.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\framedynos.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dc691532ab99909b19b4ca4ff35a701c2c3c42160a049b21c712e4d4db401fc5`
* **Total Exported Functions:** 611

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 303 | `?GetCurrentSubKeyName@CRegistry@@QEAAKAEAVCHString@@@Z` | `0x1490` | 172 | UnwindData |  |
| 304 | `?GetCurrentSubKeyPath@CRegistry@@QEAAKAEAVCHString@@@Z` | `0x1550` | 408 | UnwindData |  |
| 306 | `?GetCurrentSubKeyValue@CRegistry@@QEAAKPEBGAEAVCHString@@@Z` | `0x16F0` | 68 | UnwindData |  |
| 456 | `?OpenSubKey@CRegistry@@AEAAKXZ` | `0x1740` | 123 | UnwindData |  |
| 454 | `?OpenLocalMachineKeyAndReadValue@CRegistry@@QEAAJPEBG0AEAVCHString@@@Z` | `0x17D0` | 84 | UnwindData |  |
| 451 | `?Open@CRegistry@@QEAAJPEAUHKEY__@@PEBGK@Z` | `0x1830` | 274 | UnwindData |  |
| 459 | `?PrepareToReOpen@CRegistry@@AEAAXXZ` | `0x1950` | 27 | UnwindData |  |
| 295 | `?GetCurrentKeyValue@CRegistry@@QEAAKPEAUHKEY__@@PEBGAEAVCHString@@@Z` | `0x1980` | 805 | UnwindData |  |
| 61 | `??1CRegistry@@QEAA@XZ` | `0x1CB0` | 50 | UnwindData |  |
| 191 | `?Close@CRegistry@@QEAAXXZ` | `0x1CF0` | 108 | UnwindData |  |
| 283 | `?GetBufferSetLength@CHString@@QEAAPEAGH@Z` | `0x1D70` | 75 | UnwindData |  |
| 282 | `?GetBuffer@CHString@@QEAAPEAGH@Z` | `0x1DD0` | 415 | UnwindData |  |
| 32 | `??0CreateMutexAsProcess@@QEAA@PEBG@Z` | `0x1F80` | 841 | UnwindData |  |
| 333 | `?GetLocalInstancePath@Provider@@IEAA_NPEBVCInstance@@AEAVCHString@@@Z` | `0x22D0` | 211 | UnwindData |  |
| 439 | `?MakeLocalPath@Provider@@IEAA?AVCHString@@AEBV2@@Z` | `0x23B0` | 129 | UnwindData |  |
| 413 | `?IsExtended@CFrameworkQueryEx@@UEAA_NXZ` | `0x2440` | 24 | UnwindData |  |
| 412 | `?IsEmpty@CHString@@QEBAHXZ` | `0x2460` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `?IsPropertyRequired@CFrameworkQuery@@QEAA_NPEBG@Z` | `0x2720` | 108 | UnwindData |  |
| 414 | `?IsInList@CFrameworkQuery@@IEAAKAEBVCHStringArray@@PEBG@Z` | `0x27A0` | 303 | UnwindData |  |
| 126 | `??H@YA?AVCHString@@AEBV0@PEBG@Z` | `0x28E0` | 131 | UnwindData |  |
| 128 | `??H@YA?AVCHString@@PEBGAEBV0@@Z` | `0x2970` | 140 | UnwindData |  |
| 488 | `?SafeStrlen@CHString@@KAHPEBG@Z` | `0x2A10` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `??0Provider@@QEAA@PEBG0@Z` | `0x2E10` | 197 | UnwindData |  |
| 401 | `?InitComputerName@Provider@@CAXXZ` | `0x2EE0` | 205 | UnwindData |  |
| 261 | `?FrameworkLogin@CWbemProviderGlue@@SAXPEBGPEAVProvider@@0@Z` | `0x2FC0` | 241 | UnwindData |  |
| 166 | `?AddProviderToMap@CWbemProviderGlue@@CAPEAVProvider@@PEBG0PEAV2@@Z` | `0x30C0` | 282 | UnwindData |  |
| 11 | `??0CHString@@QEAA@PEBG@Z` | `0x32B0` | 254 | UnwindData |  |
| 501 | `?SetCharSplat@CInstance@@QEAA_NPEBG0@Z` | `0x33C0` | 334 | UnwindData |  |
| 505 | `?SetCreationClassName@Provider@@IEAA_NPEAVCInstance@@@Z` | `0x3520` | 329 | UnwindData |  |
| 187 | `?CheckImpersonationLevel@CWbemProviderGlue@@CAJXZ` | `0x36D0` | 643 | UnwindData |  |
| 531 | `?SetWBEMINT64@CInstance@@QEAA_NPEBG_J@Z` | `0x3960` | 131 | UnwindData |  |
| 535 | `?Setbool@CInstance@@QEAA_NPEBG_N@Z` | `0x39F0` | 768 | UnwindData |  |
| 516 | `?SetDateTime@CInstance@@QEAA_NPEBGAEBVWBEMTime@@@Z` | `0x3D00` | 1,270 | UnwindData |  |
| 308 | `?GetDMTF@WBEMTime@@QEBAPEAGH@Z` | `0x4200` | 307 | UnwindData |  |
| 336 | `?GetLocalOffsetForDate@WBEMTime@@SAJPEBU_SYSTEMTIME@@@Z` | `0x4450` | 878 | UnwindData |  |
| 532 | `?SetWBEMINT64@CInstance@@QEAA_NPEBG_K@Z` | `0x4860` | 853 | UnwindData |  |
| 515 | `?SetDWORD@CInstance@@QEAA_NPEBGK@Z` | `0x4BC0` | 743 | UnwindData |  |
| 438 | `?LogError@CInstance@@IEBAXPEBG00J@Z` | `0x4EB0` | 530 | UnwindData |  |
| 533 | `?SetWCHARSplat@CInstance@@QEAA_NPEBG0@Z` | `0x50D0` | 828 | UnwindData |  |
| 417 | `?IsLoggingOn@ProviderLog@@QEAA?AW4LogLevel@1@PEAVCHString@@@Z` | `0x5420` | 1,201 | UnwindData |  |
| 498 | `?SetCHString@CInstance@@QEAA_NPEBGAEBVCHString@@@Z` | `0x58E0` | 846 | UnwindData |  |
| 476 | `?Release@CWbemProviderGlue@@UEAAKXZ` | `0x5C40` | 165 | UnwindData |  |
| 170 | `?AddRef@CWbemProviderGlue@@UEAAKXZ` | `0x5CF0` | 98 | UnwindData |  |
| 325 | `?GetInstanceFromCIMOM@CWbemProviderGlue@@CAJPEBG0PEAVMethodContext@@PEAPEAVCInstance@@@Z` | `0x5D60` | 959 | UnwindData |  |
| 264 | `?FrameworkLogoff@CWbemProviderGlue@@SAXPEBG0@Z` | `0x6130` | 799 | UnwindData |  |
| 285 | `?GetCHString@CInstance@@QEBA_NPEBGAEAVCHString@@@Z` | `0x6460` | 399 | UnwindData |  |
| 83 | `??4CHString@@QEAAAEBV0@PEBG@Z` | `0x6600` | 512 | UnwindData |  |
| 324 | `?GetInstanceByPath@CWbemProviderGlue@@SAJPEBGPEAPEAVCInstance@@PEAVMethodContext@@@Z` | `0x6830` | 812 | UnwindData |  |
| 142 | `??YCHString@@QEAAAEBV0@PEBG@Z` | `0x6B70` | 52 | UnwindData |  |
| 487 | `?Right@CHString@@QEBA?AV1@H@Z` | `0x6BB0` | 473 | UnwindData |  |
| 141 | `??YCHString@@QEAAAEBV0@G@Z` | `0x6D90` | 68 | UnwindData |  |
| 176 | `?AllocCopy@CHString@@IEBAXAEAV1@HHH@Z` | `0x6FE0` | 100 | UnwindData |  |
| 427 | `?Left@CHString@@QEBA?AV1@H@Z` | `0x71D0` | 383 | UnwindData |  |
| 139 | `??YCHString@@QEAAAEBV0@AEBV0@@Z` | `0x7360` | 46 | UnwindData |  |
| 198 | `?ConcatCopy@CHString@@IEAAXHPEBGH0@Z` | `0x7690` | 31 | UnwindData |  |
| 199 | `?ConcatInPlace@CHString@@IEAAXHPEBG@Z` | `0x7830` | 17 | UnwindData |  |
| 290 | `?GetComputerNameW@CWbemProviderGlue@@CAXAEAVCHString@@@Z` | `0x7BA0` | 83 | UnwindData |  |
| 69 | `??1MethodContext@@UEAA@XZ` | `0x7C40` | 106 | UnwindData |  |
| 7 | `??0CHString@@QEAA@AEBV0@@Z` | `0x8010` | 102 | UnwindData |  |
| 55 | `??1CFrameworkQueryEx@@QEAA@XZ` | `0x8200` | 42 | UnwindData |  |
| 296 | `?GetCurrentKeyValue@CRegistry@@QEAAKPEAUHKEY__@@PEBGAEAVCHStringArray@@@Z` | `0x8260` | 400 | UnwindData |  |
| 522 | `?SetSize@CHPtrArray@@QEAAXHH@Z` | `0x8400` | 138 | UnwindData |  |
| 37 | `??0ParsedObjectPath@@QEAA@XZ` | `0x85E0` | 109 | UnwindData |  |
| 9 | `??0CHString@@QEAA@PEBD@Z` | `0x8660` | 382 | UnwindData |  |
| 442 | `?MakeUpper@CHString@@QEAAXXZ` | `0x87F0` | 34 | UnwindData |  |
| 257 | `?Format@CHString@@QEAAXPEBGZZ` | `0x8820` | 34 | UnwindData |  |
| 490 | `?SearchMapForProvider@CWbemProviderGlue@@CAPEAVProvider@@PEBG0@Z` | `0x8850` | 1,104 | UnwindData |  |
| 260 | `?FormatV@CHString@@QEAAXPEBGPEAD@Z` | `0x8CB0` | 1,590 | UnwindData |  |
| 202 | `?CopyBeforeWrite@CHString@@IEAAXXZ` | `0x92F0` | 64 | UnwindData |  |
| 77 | `??4CHString@@QEAAAEBV0@AEBV0@@Z` | `0x9420` | 758 | UnwindData |  |
| 480 | `?RemoveAll@CHStringArray@@QEAAXXZ` | `0x9720` | 82 | UnwindData |  |
| 160 | `?Add@CHStringArray@@QEAAHPEBG@Z` | `0x97B0` | 28 | UnwindData |  |
| 58 | `??1CHStringArray@@QEAA@XZ` | `0x97E0` | 70 | UnwindData |  |
| 523 | `?SetSize@CHStringArray@@QEAAXHH@Z` | `0x9830` | 26 | UnwindData |  |
| 495 | `?SetAtGrow@CHStringArray@@QEAAXHPEBG@Z` | `0x9A70` | 1,040 | UnwindData |  |
| 57 | `??1CHString@@QEAA@XZ` | `0x9E90` | 100 | UnwindData |  |
| 81 | `??4CHString@@QEAAAEBV0@PEBD@Z` | `0x9F00` | 853 | UnwindData |  |
| 478 | `?ReleaseBuffer@CHString@@QEAAXH@Z` | `0xA260` | 387 | UnwindData |  |
| 471 | `?Release@CHString@@QEAAXXZ` | `0xA3F0` | 108 | UnwindData |  |
| 568 | `?keyref@CObjectPathParser@@AEAAHXZ` | `0xA4B0` | 336 | UnwindData |  |
| 165 | `?AddNamespace@ParsedObjectPath@@QEAAHPEBG@Z` | `0xA610` | 167 | UnwindData |  |
| 591 | `?ns_list@CObjectPathParser@@AEAAHXZ` | `0xA6C0` | 210 | UnwindData |  |
| 567 | `?key_const@CObjectPathParser@@AEAAHXZ` | `0xA7A0` | 545 | UnwindData |  |
| 598 | `?propname@CObjectPathParser@@AEAAHXZ` | `0xA9D0` | 88 | UnwindData |  |
| 447 | `?NextToken@CObjectPathParser@@AEAAHXZ` | `0xAB10` | 38 | UnwindData |  |
| 354 | `?GetObjectAsync@CWbemProviderGlue@@UEAAJQEAGJPEAUIWbemContext@@PEAUIWbemObjectSink@@@Z` | `0xADB0` | 1,989 | UnwindData |  |
| 457 | `?Parse@CObjectPathParser@@QEAAHPEBGPEAPEAUParsedObjectPath@@@Z` | `0xB580` | 1,279 | UnwindData |  |
| 234 | `?Empty@CObjectPathParser@@AEAAXXZ` | `0xBA90` | 69 | UnwindData |  |
| 70 | `??1ParsedObjectPath@@QEAA@XZ` | `0xBB10` | 127 | UnwindData |  |
| 369 | `?GetStatusObject@MethodContext@@QEAAPEAUIWbemClassObject@@XZ` | `0xBBA0` | 88 | UnwindData |  |
| 474 | `?Release@CThreadBase@@QEAAJXZ` | `0xBD10` | 42 | UnwindData |  |
| 560 | `?begin_parse@CObjectPathParser@@AEAAHXZ` | `0xBD40` | 138 | UnwindData |  |
| 494 | `?SetAtGrow@CHPtrArray@@QEAAXHPEAX@Z` | `0xBF90` | 457 | UnwindData |  |
| 596 | `?objref_rest@CObjectPathParser@@AEAAHXZ` | `0xC160` | 229 | UnwindData |  |
| 159 | `?Add@CHPtrArray@@QEAAHPEAX@Z` | `0xC290` | 440 | UnwindData |  |
| 397 | `?Init@CFrameworkQuery@@QEAAJPEAUParsedObjectPath@@PEAUIWbemContext@@PEBGAEAVCHString@@@Z` | `0xC450` | 1,160 | UnwindData |  |
| 484 | `?Reset@CFrameworkQuery@@AEAAXXZ` | `0xC8E0` | 156 | UnwindData |  |
| 233 | `?Empty@CHString@@QEAAXXZ` | `0xC990` | 83 | UnwindData |  |
| 54 | `??1CFrameworkQuery@@QEAA@XZ` | `0xCA30` | 104 | UnwindData |  |
| 161 | `?AddFlushPtr@CWbemProviderGlue@@AEAAXPEAX@Z` | `0xCAA0` | 113 | UnwindData |  |
| 519 | `?SetKeyFromParsedObjectPath@Provider@@AEAAHPEAVCInstance@@PEAUParsedObjectPath@@@Z` | `0xCB20` | 367 | UnwindData |  |
| 213 | `?CreateNewInstance@Provider@@IEAAPEAVCInstance@@PEAVMethodContext@@@Z` | `0xCCA0` | 847 | UnwindData |  |
| 473 | `?Release@CInstance@@QEAAJXZ` | `0xD000` | 348 | UnwindData |  |
| 431 | `?LocalLogMessage@ProviderLog@@QEAAXPEBGHW4LogLevel@1@0ZZ` | `0xD170` | 135 | UnwindData |  |
| 210 | `?CreateInstanceEnumAsync@CWbemProviderGlue@@UEAAJQEAGJPEAUIWbemContext@@PEAUIWbemObjectSink@@@Z` | `0xD200` | 1,546 | UnwindData |  |
| 5 | `??0CFrameworkQueryEx@@QEAA@XZ` | `0xD810` | 49 | UnwindData |  |
| 3 | `??0CFrameworkQuery@@QEAA@XZ` | `0xD850` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `?GetObject@Provider@@AEAAJPEAUParsedObjectPath@@PEAVMethodContext@@J@Z` | `0xD8D0` | 444 | UnwindData |  |
| 326 | `?GetInstanceKeysByPath@CWbemProviderGlue@@SAJPEBGPEAPEAVCInstance@@PEAVMethodContext@@@Z` | `0xDAA0` | 458 | UnwindData |  |
| 528 | `?SetVariant@CInstance@@QEAA_NPEBGAEBUtagVARIANT@@@Z` | `0xDC70` | 186 | UnwindData |  |
| 396 | `?Init2@CFrameworkQuery@@QEAAXPEAUIWbemClassObject@@@Z` | `0xDD30` | 969 | UnwindData |  |
| 288 | `?GetClassObjectInterface@CInstance@@QEAAPEAUIWbemClassObject@@XZ` | `0xE100` | 36 | UnwindData |  |
| 68 | `??1KeyRef@@QEAA@XZ` | `0xE160` | 50 | UnwindData |  |
| 328 | `?GetInstancesByQuery@CWbemProviderGlue@@SAJPEBGPEAV?$TRefPointerCollection@VCInstance@@@@PEAVMethodContext@@0@Z` | `0xE1A0` | 1,358 | UnwindData |  |
| 194 | `?Commit@CInstance@@QEAAJXZ` | `0xE790` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `?ExecQueryAsync@CWbemProviderGlue@@UEAAJQEAG0JPEAUIWbemContext@@PEAUIWbemObjectSink@@@Z` | `0xE870` | 1,450 | UnwindData |  |
| 361 | `?GetQueryClassName@CFrameworkQuery@@QEAAPEAGXZ` | `0xEEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `?GetClassObjectInterface@Provider@@AEAAPEAUIWbemClassObject@@PEAVMethodContext@@@Z` | `0xEF10` | 562 | UnwindData |  |
| 398 | `?Init@CFrameworkQuery@@QEAAJQEAG0JAEAVCHString@@@Z` | `0xF150` | 730 | UnwindData |  |
| 248 | `?ExecuteQuery@Provider@@AEAAJPEAVMethodContext@@AEAVCFrameworkQuery@@J@Z` | `0xF4A0` | 196 | UnwindData |  |
| 209 | `?CreateInstanceEnum@Provider@@AEAAJPEAVMethodContext@@J@Z` | `0xF7D0` | 83 | UnwindData |  |
| 378 | `?GetValuesForProp@CFrameworkQuery@@QEAAJPEBGAEAV?$vector@V_bstr_t@@V?$allocator@V_bstr_t@@@std@@@std@@@Z` | `0x11580` | 729 | UnwindData |  |
| 379 | `?GetValuesForProp@CFrameworkQuery@@QEAAJPEBGAEAVCHStringArray@@@Z` | `0x122D0` | 688 | UnwindData |  |
| 381 | `?GetValuesForProp@CFrameworkQueryEx@@QEAAJPEBGAEAV?$vector@V_variant_t@@V?$allocator@V_variant_t@@@std@@@std@@@Z` | `0x12750` | 711 | UnwindData |  |
| 424 | `?IsReference@CFrameworkQuery@@IEAAHPEBG@Z` | `0x12CF0` | 75 | UnwindData |  |
| 448 | `?NormalizePath@@YAKPEBG00KAEAVCHString@@@Z` | `0x12DE0` | 358 | UnwindData |  |
| 425 | `?IsRelative@ParsedObjectPath@@QEAAHPEBG0@Z` | `0x12F50` | 323 | UnwindData |  |
| 548 | `?Unparse@CObjectPathParser@@SAHPEAUParsedObjectPath@@PEAPEAG@Z` | `0x130A0` | 831 | UnwindData |  |
| 416 | `?IsLocal@ParsedObjectPath@@QEAAHPEBG@Z` | `0x133F0` | 102 | UnwindData |  |
| 380 | `?GetValuesForProp@CFrameworkQueryEx@@QEAAJPEBGAEAV?$vector@HV?$allocator@H@std@@@std@@@Z` | `0x13960` | 217 | UnwindData |  |
| 180 | `?AssignCopy@CHString@@IEAAXHPEBG@Z` | `0x13CD0` | 56 | UnwindData |  |
| 8 | `??0CHString@@QEAA@GH@Z` | `0x13EC0` | 165 | UnwindData |  |
| 175 | `?AllocBuffer@CHString@@IEAAXH@Z` | `0x13F70` | 20 | UnwindData |  |
| 327 | `?GetInstancePropertiesByPath@CWbemProviderGlue@@SAJPEBGPEAPEAVCInstance@@PEAVMethodContext@@AEAVCHStringArray@@@Z` | `0x14050` | 799 | UnwindData |  |
| 29 | `??0CWbemProviderGlue@@QEAA@XZ` | `0x14490` | 83 | UnwindData |  |
| 400 | `?Init@CWbemProviderGlue@@CAXXZ` | `0x144F0` | 249 | UnwindData |  |
| 207 | `?CreateInstance@CWbemGlueFactory@@UEAAJPEAUIUnknown@@AEBU_GUID@@PEAPEAX@Z` | `0x145F0` | 334 | UnwindData |  |
| 541 | `?UnInit@CWbemProviderGlue@@CAXXZ` | `0x14750` | 50 | UnwindData |  |
| 169 | `?AddRef@CWbemGlueFactory@@UEAAKXZ` | `0x14790` | 72 | UnwindData |  |
| 475 | `?Release@CWbemGlueFactory@@UEAAKXZ` | `0x147E0` | 118 | UnwindData |  |
| 466 | `?QueryInterface@CWbemGlueFactory@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x14860` | 179 | UnwindData |  |
| 65 | `??1CWbemProviderGlue@@QEAA@XZ` | `0x14950` | 142 | UnwindData |  |
| 467 | `?QueryInterface@CWbemProviderGlue@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x149F0` | 345 | UnwindData |  |
| 430 | `?LocalLogMessage@ProviderLog@@QEAAXPEBG0HW4LogLevel@1@@Z` | `0x14B50` | 1,030 | UnwindData |  |
| 342 | `?GetMapCountPtr@CWbemProviderGlue@@KAPEAJPEBVCWbemGlueFactory@@@Z` | `0x14F60` | 195 | UnwindData |  |
| 216 | `?DecrementMapCount@CWbemProviderGlue@@KAJPEAJ@Z` | `0x15030` | 77 | UnwindData |  |
| 64 | `??1CWbemGlueFactory@@QEAA@XZ` | `0x150B0` | 98 | UnwindData |  |
| 217 | `?DecrementMapCount@CWbemProviderGlue@@KAJPEBVCWbemGlueFactory@@@Z` | `0x15120` | 238 | UnwindData |  |
| 483 | `?RemoveFromFactoryMap@CWbemProviderGlue@@KAXPEBVCWbemGlueFactory@@@Z` | `0x15220` | 211 | UnwindData |  |
| 255 | `?FlushAll@CWbemProviderGlue@@AEAAXXZ` | `0x15300` | 355 | UnwindData |  |
| 186 | `?CheckFileSize@ProviderLog@@AEAAXAEAT_LARGE_INTEGER@@AEBVCHString@@@Z` | `0x15AC0` | 156 | UnwindData |  |
| 319 | `?GetEmptyInstance@CWbemProviderGlue@@SAJPEAVMethodContext@@PEBGPEAPEAVCInstance@@1@Z` | `0x15B70` | 394 | UnwindData |  |
| 411 | `?IsDerivedFrom@CWbemProviderGlue@@SA_NPEBG0PEAVMethodContext@@0@Z` | `0x15D00` | 694 | UnwindData |  |
| 410 | `?IsClass@ParsedObjectPath@@QEAAHXZ` | `0x15FC0` | 50 | UnwindData |  |
| 242 | `?ExecMethodAsync@CWbemProviderGlue@@UEAAJQEAG0JPEAUIWbemContext@@PEAUIWbemClassObject@@PEAUIWbemObjectSink@@@Z` | `0x16000` | 2,319 | UnwindData |  |
| 240 | `?ExecMethod@Provider@@AEAAJPEAUParsedObjectPath@@PEAGJPEAVCInstance@@2PEAVMethodContext@@@Z` | `0x16920` | 222 | UnwindData |  |
| 415 | `?IsInstance@ParsedObjectPath@@QEAAHXZ` | `0x16A10` | 53 | UnwindData |  |
| 420 | `?IsObject@ParsedObjectPath@@QEAAHXZ` | `0x16A50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `?GetInstancesByQueryAsynch@CWbemProviderGlue@@SAJPEBGPEAVProvider@@P6AJ1PEAVCInstance@@PEAVMethodContext@@PEAX@Z034@Z` | `0x16A80` | 1,355 | UnwindData |  |
| 16 | `??0CInstance@@QEAA@PEAUIWbemClassObject@@PEAVMethodContext@@@Z` | `0x16FE0` | 85 | UnwindData |  |
| 347 | `?GetNamespaceConnection@CWbemProviderGlue@@SAPEAUIWbemServices@@PEBGPEAVMethodContext@@@Z` | `0x17270` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??0MethodContext@@QEAA@PEAUIWbemContext@@PEAVCWbemProviderGlue@@@Z` | `0x172D0` | 143 | UnwindData |  |
| 174 | `?AllocBeforeWrite@CHString@@IEAAXH@Z` | `0x17370` | 93 | UnwindData |  |
| 357 | `?GetPropertyBitMask@CFrameworkQueryEx@@QEAAXAEBVCHPtrArray@@PEAX@Z` | `0x174E0` | 1,447 | UnwindData |  |
| 314 | `?GetData@CHString@@IEBAPEAUCHStringData@@XZ` | `0x17B30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `?Compare@CHString@@QEBAHPEBG@Z` | `0x17B60` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0CHString@@QEAA@XZ` | `0x17CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `??1CInstance@@UEAA@XZ` | `0x17CF0` | 93 | UnwindData |  |
| 364 | `?GetSYSTEMTIME@WBEMTime@@QEBAHPEAU_SYSTEMTIME@@@Z` | `0x17D60` | 70 | UnwindData |  |
| 50 | `??0WBEMTimeSpan@@QEAA@HHHHHHH@Z` | `0x17DB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `?GetFILETIME@WBEMTime@@QEBAHPEAU_FILETIME@@@Z` | `0x17E30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `?GetLength@CHString@@QEBAHXZ` | `0x17E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `?Find@CHString@@QEBAHPEBG@Z` | `0x17E80` | 49 | UnwindData |  |
| 251 | `?Find@CHString@@QEBAHG@Z` | `0x17EC0` | 54 | UnwindData |  |
| 119 | `??ACHStringArray@@QEBA?AVCHString@@H@Z` | `0x17F30` | 130 | UnwindData |  |
| 279 | `?GetAt@CHStringArray@@QEBA?AVCHString@@H@Z` | `0x17F30` | 130 | UnwindData |  |
| 472 | `?Release@CHString@@SAXPEAUCHStringData@@@Z` | `0x18030` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `?BeginRead@CThreadBase@@QEAAHK@Z` | `0x18070` | 31 | UnwindData |  |
| 182 | `?BeginWrite@CThreadBase@@QEAAHK@Z` | `0x18070` | 31 | UnwindData |  |
| 129 | `??HWBEMTime@@QEBA?AV0@AEBVWBEMTimeSpan@@@Z` | `0x180D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??0WBEMTime@@QEAA@AEBU_FILETIME@@@Z` | `0x18100` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `??4WBEMTime@@QEAAAEBV0@AEBU_FILETIME@@@Z` | `0x18100` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `?AddRef@CThreadBase@@QEAAJXZ` | `0x18150` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `?AddRef@MethodContext@@QEAAJXZ` | `0x18150` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 477 | `?Release@MethodContext@@QEAAJXZ` | `0x182F0` | 40 | UnwindData |  |
| 120 | `??BCHString@@QEBAPEBGXZ` | `0x18320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `?GetData@CHPtrArray@@QEAAPEAPEAXXZ` | `0x18320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `?GetData@CHPtrArray@@QEBAPEAPEBXXZ` | `0x18320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `?GetData@CHStringArray@@QEAAPEAVCHString@@XZ` | `0x18320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `?GetData@CHStringArray@@QEBAPEBVCHString@@XZ` | `0x18320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `?GetTime@WBEMTime@@QEBA_KXZ` | `0x18320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `?GetTime@WBEMTimeSpan@@QEBA_KXZ` | `0x18320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `?IsOk@WBEMTime@@QEBA_NXZ` | `0x18330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `?IsOk@WBEMTimeSpan@@QEBA_NXZ` | `0x18330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 479 | `?RemoveAll@CHPtrArray@@QEAAXXZ` | `0x18340` | 48 | UnwindData |  |
| 323 | `?GetIWBEMContext@MethodContext@@UEAAPEAUIWbemContext@@XZ` | `0x18380` | 86 | UnwindData |  |
| 116 | `??ACHPtrArray@@QEBAPEAXH@Z` | `0x183E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `?GetAt@CHPtrArray@@QEBAPEAXH@Z` | `0x183E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `?GetLocalComputerName@Provider@@IEAAAEBVCHString@@XZ` | `0x18400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `?EndRead@CThreadBase@@QEAAXXZ` | `0x18410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `?EndWrite@CThreadBase@@QEAAXXZ` | `0x18410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `?Unlock@CThreadBase@@AEAAXXZ` | `0x18410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `?Mid@CHString@@QEBA?AV1@H@Z` | `0x18430` | 209 | UnwindData |  |
| 121 | `??GWBEMTime@@QEAA?AVWBEMTimeSpan@@AEBV0@@Z` | `0x18510` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `??GWBEMTime@@QEBA?AV0@AEBVWBEMTimeSpan@@@Z` | `0x18510` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `??GWBEMTimeSpan@@QEBA?AV0@AEBV0@@Z` | `0x18510` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `?AddKeyRef@ParsedObjectPath@@QEAAHPEAUKeyRef@@@Z` | `0x18540` | 159 | UnwindData |  |
| 444 | `?Mid@CHString@@QEBA?AV1@HH@Z` | `0x18610` | 186 | UnwindData |  |
| 593 | `?ns_or_class@CObjectPathParser@@AEAAHXZ` | `0x186D0` | 132 | UnwindData |  |
| 563 | `?ident_becomes_class@CObjectPathParser@@AEAAHXZ` | `0x18760` | 46 | UnwindData |  |
| 594 | `?ns_or_server@CObjectPathParser@@AEAAHXZ` | `0x187A0` | 81 | UnwindData |  |
| 56 | `??1CHPtrArray@@QEAA@XZ` | `0x18820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0CHPtrArray@@QEAA@XZ` | `0x18840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??0CHStringArray@@QEAA@XZ` | `0x18840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `??ACHPtrArray@@QEAAAEAPEAXH@Z` | `0x18860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `??ACHStringArray@@QEAAAEAVCHString@@H@Z` | `0x18860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `?ElementAt@CHPtrArray@@QEAAAEAPEAXH@Z` | `0x18860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `?ElementAt@CHStringArray@@QEAAAEAVCHString@@H@Z` | `0x18860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `?ns_list_rest@CObjectPathParser@@AEAAHXZ` | `0x18880` | 53 | UnwindData |  |
| 551 | `?ValidateFlags@Provider@@IEAAJJW4FlagDefs@1@@Z` | `0x188C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 529 | `?SetWBEMINT16@CInstance@@QEAA_NPEBGAEBF@Z` | `0x188E0` | 283 | UnwindData |  |
| 47 | `??0WBEMTime@@QEAA@XZ` | `0x18A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??0WBEMTimeSpan@@QEAA@XZ` | `0x18A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `?SetByte@CInstance@@QEAA_NPEBGE@Z` | `0x18A20` | 279 | UnwindData |  |
| 124 | `??H@YA?AVCHString@@AEBV0@0@Z` | `0x18B40` | 122 | UnwindData |  |
| 559 | `?Zero@CObjectPathParser@@AEAAXXZ` | `0x18BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `??H@YA?AVCHString@@AEBV0@G@Z` | `0x18BE0` | 106 | UnwindData |  |
| 450 | `?OnFinalRelease@CThreadBase@@MEAAXXZ` | `0x18C50` | 31 | UnwindData |  |
| 365 | `?GetSize@CHPtrArray@@QEBAHXZ` | `0x18C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `?GetSize@CHStringArray@@QEBAHXZ` | `0x18C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `?optional_objref@CObjectPathParser@@AEAAHXZ` | `0x18C90` | 59 | UnwindData |  |
| 595 | `?objref@CObjectPathParser@@AEAAHXZ` | `0x18CE0` | 72 | UnwindData |  |
| 23 | `??0CThreadBase@@QEAA@W4THREAD_SAFETY_MECHANISM@0@@Z` | `0x18D30` | 55 | UnwindData |  |
| 19 | `??0CRegistry@@QEAA@XZ` | `0x18D70` | 90 | UnwindData |  |
| 517 | `?SetDefaultValues@CRegistry@@AEAAXXZ` | `0x18DD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `?SetPlatformID@CRegistry@@CAHXZ` | `0x18E10` | 103 | UnwindData |  |
| 63 | `??1CThreadBase@@UEAA@XZ` | `0x18E80` | 46 | UnwindData |  |
| 569 | `?keyref_list@CObjectPathParser@@AEAAHXZ` | `0x18EC0` | 33 | UnwindData |  |
| 570 | `?keyref_term@CObjectPathParser@@AEAAHXZ` | `0x18EF0` | 53 | UnwindData |  |
| 589 | `?myRegQueryValueEx@CRegistry@@AEAAJPEAUHKEY__@@PEBGPEAK2PEAE2@Z` | `0x19030` | 65 | UnwindData |  |
| 34 | `??0KeyRef@@QEAA@XZ` | `0x19130` | 39 | UnwindData |  |
| 419 | `?IsNull@CInstance@@QEBA_NPEBG@Z` | `0x19160` | 254 | UnwindData |  |
| 197 | `?CompareNoCase@CHString@@QEBAHPEBG@Z` | `0x19270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `?myRegQueryInfoKey@CRegistry@@AEAAJPEAUHKEY__@@PEAGPEAK22222222PEAU_FILETIME@@@Z` | `0x19290` | 152 | UnwindData |  |
| 550 | `?ValidateEnumerationFlags@Provider@@MEAAJJ@Z` | `0x19380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `?ValidateGetObjFlags@Provider@@MEAAJJ@Z` | `0x19380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 556 | `?ValidateQueryFlags@Provider@@MEAAJJ@Z` | `0x19380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??0CObjectPathParser@@QEAA@W4ObjectParserFlags@@@Z` | `0x193A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `?Free@CObjectPathParser@@QEAAXPEAUParsedObjectPath@@@Z` | `0x193D0` | 23 | UnwindData |  |
| 300 | `?GetCurrentRawKeyValue@CRegistry@@AEAAKPEAUHKEY__@@PEBGPEAXPEAK3@Z` | `0x19420` | 54 | UnwindData |  |
| 71 | `??1Provider@@UEAA@XZ` | `0x194C0` | 114 | UnwindData |  |
| 294 | `?GetCurrentKeyValue@CRegistry@@QEAAKPEAUHKEY__@@PEBGAEAK@Z` | `0x19570` | 201 | UnwindData |  |
| 526 | `?SetStringArray@CInstance@@QEAA_NPEBGAEBUtagSAFEARRAY@@@Z` | `0x19640` | 328 | UnwindData |  |
| 343 | `?GetMethodContext@CInstance@@QEBAPEAVMethodContext@@XZ` | `0x197C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `?AddRef@CInstance@@QEAAJXZ` | `0x197D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 492 | `?SetAt@CHString@@QEAAXHG@Z` | `0x19810` | 54 | UnwindData |  |
| 237 | `?EnumerateAndGetValues@CRegistry@@QEAAJAEAKAEAPEAGAEAPEAE@Z` | `0x19850` | 373 | UnwindData |  |
| 497 | `?SetCHString@CInstance@@QEAA_NPEBG0@Z` | `0x199D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `?GetVariant@CInstance@@QEBA_NPEBGAEAUtagVARIANT@@@Z` | `0x199E0` | 183 | UnwindData |  |
| 298 | `?GetCurrentKeyValue@CRegistry@@QEAAKPEBGAEAVCHString@@@Z` | `0x19E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `?NextSubKey@CRegistry@@QEAAKXZ` | `0x19E30` | 60 | UnwindData |  |
| 192 | `?CloseSubKey@CRegistry@@AEAAXXZ` | `0x19E80` | 42 | UnwindData |  |
| 311 | `?GetDWORD@CInstance@@QEBA_NPEBGAEAK@Z` | `0x19EF0` | 363 | UnwindData |  |
| 587 | `?myRegOpenKeyEx@CRegistry@@AEAAJPEAUHKEY__@@PEBGKKPEAPEAU2@@Z` | `0x1A070` | 45 | UnwindData |  |
| 359 | `?GetProviderName@Provider@@IEAAAEBVCHString@@XZ` | `0x1A0B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `?UnlockProviderMap@CWbemProviderGlue@@CAXXZ` | `0x1A0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `??YCHString@@QEAAAEBV0@D@Z` | `0x1A0E0` | 42 | UnwindData |  |
| 436 | `?LockProviderMap@CWbemProviderGlue@@CAXXZ` | `0x1A110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `?SetWORD@CInstance@@QEAA_NPEBGG@Z` | `0x1A130` | 296 | UnwindData |  |
| 585 | `?myRegEnumKey@CRegistry@@AEAAJPEAUHKEY__@@KPEAGK@Z` | `0x1A260` | 67 | UnwindData |  |
| 499 | `?SetCHString@CInstance@@QEAA_NPEBGPEBD@Z` | `0x1A2B0` | 80 | UnwindData |  |
| 204 | `?Create@CWbemGlueFactory@@SAPEAV1@XZ` | `0x1A320` | 60 | UnwindData |  |
| 26 | `??0CWbemGlueFactory@@QEAA@XZ` | `0x1A370` | 97 | UnwindData |  |
| 203 | `?Create@CWbemGlueFactory@@SAPEAV1@PEAJ@Z` | `0x1A3E0` | 68 | UnwindData |  |
| 25 | `??0CWbemGlueFactory@@QEAA@PEAJ@Z` | `0x1A430` | 114 | UnwindData |  |
| 172 | `?AddToFactoryMap@CWbemProviderGlue@@KAXPEBVCWbemGlueFactory@@PEAJ@Z` | `0x1A4B0` | 114 | UnwindData |  |
| 394 | `?IncrementMapCount@CWbemProviderGlue@@KAJPEBVCWbemGlueFactory@@@Z` | `0x1A840` | 207 | UnwindData |  |
| 485 | `?ReverseFind@CHString@@QEBAHG@Z` | `0x1AB10` | 47 | UnwindData |  |
| 173 | `?AllPropertiesAreRequired@CFrameworkQuery@@QEAA_NXZ` | `0x1AB50` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `?Initialize@CWbemProviderGlue@@UEAAJPEAGJ00PEAUIWbemServices@@PEAUIWbemContext@@PEAUIWbemProviderInitSink@@@Z` | `0x1AC70` | 641 | UnwindData |  |
| 586 | `?myRegEnumValue@CRegistry@@AEAAJPEAUHKEY__@@KPEAGPEAK22PEAE2@Z` | `0x1AF00` | 94 | UnwindData |  |
| 254 | `?Flush@Provider@@MEAAXXZ` | `0x1AF70` | 109 | UnwindData |  |
| 386 | `?GetWBEMINT64@CInstance@@QEBA_NPEBGAEA_K@Z` | `0x1B150` | 98 | UnwindData |  |
| 60 | `??1CObjectPathParser@@QEAA@XZ` | `0x1B1C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `?GetCurrentKeyValue@CRegistry@@QEAAKPEBGAEAK@Z` | `0x1B1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `?GetCurrentBinaryKeyValue@CRegistry@@QEAAKPEBGPEAEPEAK@Z` | `0x1B1F0` | 48 | UnwindData |  |
| 266 | `?FrameworkLogoffDLL@CWbemProviderGlue@@SAHPEBGPEAJ@Z` | `0x1B230` | 96 | UnwindData |  |
| 527 | `?SetTimeSpan@CInstance@@QEAA_NPEBGAEBVWBEMTimeSpan@@@Z` | `0x1B2A0` | 293 | UnwindData |  |
| 281 | `?GetBSTR@WBEMTimeSpan@@QEBAPEAGXZ` | `0x1B3D0` | 269 | UnwindData |  |
| 513 | `?SetDMTF@WBEMTime@@QEAAHQEAG@Z` | `0x1B4F0` | 721 | UnwindData |  |
| 43 | `??0WBEMTime@@QEAA@AEBU_SYSTEMTIME@@@Z` | `0x1B7D0` | 24 | UnwindData |  |
| 102 | `??4WBEMTime@@QEAAAEBV0@AEBU_SYSTEMTIME@@@Z` | `0x1B7F0` | 74 | UnwindData |  |
| 426 | `?KeysOnly@CFrameworkQuery@@QEAA_NXZ` | `0x1B840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `?SpanExcluding@CHString@@QEBA?AV1@PEBG@Z` | `0x1B850` | 63 | UnwindData |  |
| 299 | `?GetCurrentKeyValue@CRegistry@@QEAAKPEBGAEAVCHStringArray@@@Z` | `0x1BAE0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??0WBEMTime@@QEAA@AEB_J@Z` | `0x1BB30` | 24 | UnwindData |  |
| 104 | `??4WBEMTime@@QEAAAEBV0@AEB_J@Z` | `0x1BB50` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `?MsgWndProc@CWinMsgEvent@@CA_JPEAUHWND__@@I_K_J@Z` | `0x1BD40` | 459 | UnwindData |  |
| 41 | `??0ProviderLog@@QEAA@XZ` | `0x1BF50` | 119 | UnwindData |  |
| 263 | `?FrameworkLoginDLL@CWbemProviderGlue@@SAHPEBGPEAJ@Z` | `0x1C000` | 89 | UnwindData |  |
| 390 | `?GethKey@CRegistry@@QEAAPEAUHKEY__@@XZ` | `0x1C100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `?DeleteInstance@Provider@@MEAAJAEBVCInstance@@J@Z` | `0x1C110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `?EnumerateInstances@Provider@@MEAAJPEAVMethodContext@@J@Z` | `0x1C110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `?ExecMethod@Provider@@MEAAJAEBVCInstance@@QEAGPEAV2@2J@Z` | `0x1C110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `?ExecQuery@Provider@@MEAAJPEAVMethodContext@@AEAVCFrameworkQuery@@J@Z` | `0x1C110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `?GetObject@Provider@@MEAAJPEAVCInstance@@J@Z` | `0x1C110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `?PutInstance@Provider@@MEAAJAEBVCInstance@@J@Z` | `0x1C110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `??1ProviderLog@@UEAA@XZ` | `0x1C120` | 79 | UnwindData |  |
| 367 | `?GetStatus@CInstance@@QEBA_NPEBGAEA_NAEAG@Z` | `0x1C1D0` | 235 | UnwindData |  |
| 345 | `?GetNamespace@Provider@@IEAAAEBVCHString@@XZ` | `0x1C2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `?GetWCHAR@CInstance@@QEBA_NPEBGPEAPEAG@Z` | `0x1C2E0` | 475 | UnwindData |  |
| 514 | `?SetDOUBLE@CInstance@@QEAA_NPEBGN@Z` | `0x1C4D0` | 308 | UnwindData |  |
| 549 | `?ValidateDeletionFlags@Provider@@MEAAJJ@Z` | `0x1C6C0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `?ValidateMethodFlags@Provider@@MEAAJJ@Z` | `0x1C6C0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0CAutoEvent@@QEAA@XZ` | `0x1C740` | 44 | UnwindData |  |
| 530 | `?SetWBEMINT64@CInstance@@QEAA_NPEBGAEBVCHString@@@Z` | `0x1C810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `?FrameworkLogoffDLL@CWbemProviderGlue@@SAHPEBG@Z` | `0x1C820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `??1CreateMutexAsProcess@@QEAA@XZ` | `0x1C830` | 61 | UnwindData |  |
| 195 | `?Commit@Provider@@IEAAJPEAVCInstance@@_N@Z` | `0x1C880` | 45 | UnwindData |  |
| 452 | `?OpenAndEnumerateSubKeys@CRegistry@@QEAAJPEAUHKEY__@@PEBGK@Z` | `0x1C950` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `?GetByte@CInstance@@QEBA_NPEBGAEAE@Z` | `0x1CA70` | 359 | UnwindData |  |
| 53 | `??1CAutoEvent@@QEAA@XZ` | `0x1CBE0` | 35 | UnwindData |  |
| 377 | `?GetValueCount@CRegistry@@QEAAKXZ` | `0x1CC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `?CreateOpen@CRegistry@@QEAAJPEAUHKEY__@@PEBGPEAGKKPEAU_SECURITY_ATTRIBUTES@@PEAK@Z` | `0x1CC20` | 329 | UnwindData |  |
| 280 | `?GetBSTR@WBEMTime@@QEBAPEAGXZ` | `0x1CD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??0CWbemProviderGlue@@QEAA@PEAJ@Z` | `0x1CD80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `?WindowsDispatch@CWinMsgEvent@@CAXXZ` | `0x1CDC0` | 94 | UnwindData |  |
| 262 | `?FrameworkLoginDLL@CWbemProviderGlue@@SAHPEBG@Z` | `0x1CED0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `??4WBEMTime@@QEAAAEBV0@QEAG@Z` | `0x1CF10` | 102 | UnwindData |  |
| 340 | `?GetLongestValueData@CRegistry@@QEAAKXZ` | `0x1CF80` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `?GetObject@Provider@@MEAAJPEAVCInstance@@JAEAVCFrameworkQuery@@@Z` | `0x1D030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `?LockFactoryMap@CWbemProviderGlue@@CAXXZ` | `0x1D050` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 565 | `?initFailed@Provider@@SAHXZ` | `0x1D0F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `?CancelAsyncCall@CWbemProviderGlue@@UEAAJPEAUIWbemObjectSink@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `?CancelAsyncRequest@CWbemProviderGlue@@UEAAJJ@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `?CreateClassEnum@CWbemProviderGlue@@UEAAJQEAGJPEAUIWbemContext@@PEAPEAUIEnumWbemClassObject@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `?CreateClassEnumAsync@CWbemProviderGlue@@UEAAJQEAGJPEAUIWbemContext@@PEAUIWbemObjectSink@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `?CreateInstanceEnum@CWbemProviderGlue@@UEAAJQEAGJPEAUIWbemContext@@PEAPEAUIEnumWbemClassObject@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?DeleteClass@CWbemProviderGlue@@UEAAJQEAGJPEAUIWbemContext@@PEAPEAUIWbemCallResult@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `?DeleteClassAsync@CWbemProviderGlue@@UEAAJQEAGJPEAUIWbemContext@@PEAUIWbemObjectSink@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `?DeleteInstance@CWbemProviderGlue@@UEAAJQEAGJPEAUIWbemContext@@PEAPEAUIWbemCallResult@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `?ExecMethod@CWbemProviderGlue@@UEAAJQEAG0JPEAUIWbemContext@@PEAUIWbemClassObject@@PEAPEAU3@PEAPEAUIWbemCallResult@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `?ExecNotificationQuery@CWbemProviderGlue@@UEAAJQEAG0JPEAUIWbemContext@@PEAPEAUIEnumWbemClassObject@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `?ExecNotificationQueryAsync@CWbemProviderGlue@@UEAAJQEAG0JPEAUIWbemContext@@PEAUIWbemObjectSink@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `?ExecQuery@CWbemProviderGlue@@UEAAJQEAG0JPEAUIWbemContext@@PEAPEAUIEnumWbemClassObject@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `?GetObject@CWbemProviderGlue@@UEAAJQEAGJPEAUIWbemContext@@PEAPEAUIWbemClassObject@@PEAPEAUIWbemCallResult@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `?OpenNamespace@CWbemProviderGlue@@UEAAJQEAGJPEAUIWbemContext@@PEAPEAUIWbemServices@@PEAPEAUIWbemCallResult@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 460 | `?PutClass@CWbemProviderGlue@@UEAAJPEAUIWbemClassObject@@JPEAUIWbemContext@@PEAPEAUIWbemCallResult@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 461 | `?PutClassAsync@CWbemProviderGlue@@UEAAJPEAUIWbemClassObject@@JPEAUIWbemContext@@PEAUIWbemObjectSink@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `?PutInstance@CWbemProviderGlue@@UEAAJPEAUIWbemClassObject@@JPEAUIWbemContext@@PEAPEAUIWbemCallResult@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `?QueryObjectSink@CWbemProviderGlue@@UEAAJJPEAPEAUIWbemObjectSink@@@Z` | `0x1D120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `?GetWBEMINT64@CInstance@@QEBA_NPEBGAEAVCHString@@@Z` | `0x1D160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | `?UnlockFactoryMap@CWbemProviderGlue@@CAXXZ` | `0x1D170` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `?IncrementMapCount@CWbemProviderGlue@@KAJPEAJ@Z` | `0x1D1B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `?Getbool@CInstance@@QEBA_NPEBGAEA_N@Z` | `0x1D1F0` | 361 | UnwindData |  |
| 117 | `??ACHString@@QEBAGH@Z` | `0x1D360` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `?GetAt@CHString@@QEBAGH@Z` | `0x1D360` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `??4WBEMTime@@QEAAAEBV0@AEBUtm@@@Z` | `0x1D3A0` | 148 | UnwindData |  |
| 309 | `?GetDMTFNonNtfs@WBEMTime@@QEBAPEAGXZ` | `0x1D470` | 133 | UnwindData |  |
| 409 | `?Is3TokenOR@CFrameworkQueryEx@@QEAAHPEBG0AEAUtagVARIANT@@1@Z` | `0x1D500` | 498 | UnwindData |  |
| 211 | `?CreateMsgProvider@CWinMsgEvent@@CAXXZ` | `0x1D710` | 188 | UnwindData |  |
| 543 | `?UnRegisterMessage@CWinMsgEvent@@IEAA_NIH@Z` | `0x1DAD0` | 340 | UnwindData |  |
| 582 | `?myRegCreateKeyEx@CRegistry@@AEAAJPEAUHKEY__@@PEBGKPEAGKKQEAU_SECURITY_ATTRIBUTES@@PEAPEAU2@PEAK@Z` | `0x1DC30` | 109 | UnwindData |  |
| 440 | `?MakeLower@CHString@@QEAAXXZ` | `0x1DCB0` | 34 | UnwindData |  |
| 346 | `?GetNamespaceConnection@CWbemProviderGlue@@SAPEAUIWbemServices@@PEBG@Z` | `0x1DD50` | 451 | UnwindData |  |
| 408 | `?InternalGetNamespaceConnection@CWbemProviderGlue@@AEAAPEAUIWbemServices@@PEBG@Z` | `0x1DF20` | 552 | UnwindData |  |
| 48 | `??0WBEMTimeSpan@@QEAA@AEBU_FILETIME@@@Z` | `0x1E150` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `??4WBEMTimeSpan@@QEAAAEBV0@AEBU_FILETIME@@@Z` | `0x1E150` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `?GetStructtm@WBEMTime@@QEBAHPEAUtm@@@Z` | `0x1E3C0` | 134 | UnwindData |  |
| 212 | `?CreateMsgWindow@CWinMsgEvent@@CAPEAUHWND__@@XZ` | `0x1E510` | 270 | UnwindData |  |
| 493 | `?SetAt@CHStringArray@@QEAAXHPEBG@Z` | `0x1E6A0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `?GetCurrentSubKeyCount@CRegistry@@QEAAKXZ` | `0x1E820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `?RegisterForMessage@CWinMsgEvent@@IEAAXIH@Z` | `0x1E830` | 549 | UnwindData |  |
| 564 | `?ident_becomes_ns@CObjectPathParser@@AEAAHXZ` | `0x1EAB0` | 42 | UnwindData |  |
| 399 | `?Init@CHString@@IEAAXXZ` | `0x1EC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `?ValidateIMOSPointer@Provider@@AEAAHXZ` | `0x1EC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `?GetProviderGlue@MethodContext@@AEAAPEAVCWbemProviderGlue@@XZ` | `0x1EC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `?GetPlatform@CWbemProviderGlue@@SAKXZ` | `0x1ECA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `?Clear@WBEMTime@@QEAAXXZ` | `0x1ECB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `?Clear@WBEMTimeSpan@@QEAAXXZ` | `0x1ECB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `?RewindSubKeys@CRegistry@@QEAAXXZ` | `0x1ECC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `?GetNamespace@CFrameworkQuery@@IEAAAEBVCHString@@XZ` | `0x1ECD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `?QueryPostProcess@MethodContext@@UEAAXXZ` | `0x1ECE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 500 | `?SetCHStringResourceHandle@@YAXPEAUHINSTANCE__@@@Z` | `0x1ECE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `?Wait@CAutoEvent@@QEAAKK@Z` | `0x1ECF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `?Signal@CAutoEvent@@QEAAHXZ` | `0x1ED10` | 7,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0CFrameworkQuery@@QEAA@AEBV0@@Z` | `0x20A10` | 159 | UnwindData |  |
| 10 | `??0CHString@@QEAA@PEBE@Z` | `0x20AC0` | 34 | UnwindData |  |
| 15 | `??0CInstance@@QEAA@AEBV0@@Z` | `0x20AF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??0CThreadBase@@QEAA@AEBV0@@Z` | `0x20B20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??0CWbemGlueFactory@@QEAA@AEBV0@@Z` | `0x20B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??0CWbemProviderGlue@@QEAA@AEBV0@@Z` | `0x20B80` | 87 | UnwindData |  |
| 35 | `??0MethodContext@@QEAA@AEBV0@@Z` | `0x20BE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??0Provider@@QEAA@AEBV0@@Z` | `0x20C40` | 146 | UnwindData |  |
| 44 | `??0WBEMTime@@QEAA@AEBUtm@@@Z` | `0x20CE0` | 24 | UnwindData |  |
| 46 | `??0WBEMTime@@QEAA@QEAG@Z` | `0x20D00` | 24 | UnwindData |  |
| 51 | `??0WBEMTimeSpan@@QEAA@QEAG@Z` | `0x20D20` | 24 | UnwindData |  |
| 74 | `??4CFrameworkQuery@@QEAAAEAV0@AEBV0@@Z` | `0x20D40` | 139 | UnwindData |  |
| 76 | `??4CHPtrArray@@QEAAAEAV0@AEBV0@@Z` | `0x20DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `??4CHStringArray@@QEAAAEAV0@AEBV0@@Z` | `0x20DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `??4CHString@@QEAAAEBV0@D@Z` | `0x20E00` | 42 | UnwindData |  |
| 80 | `??4CHString@@QEAAAEBV0@PEAV0@@Z` | `0x20E30` | 24 | UnwindData |  |
| 82 | `??4CHString@@QEAAAEBV0@PEBE@Z` | `0x20E50` | 24 | UnwindData |  |
| 85 | `??4CInstance@@QEAAAEAV0@AEBV0@@Z` | `0x20E70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `??4CObjectPathParser@@QEAAAEAV0@AEBV0@@Z` | `0x20EA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `??4CThreadBase@@QEAAAEAV0@AEBV0@@Z` | `0x20ED0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `??4CWbemGlueFactory@@QEAAAEAV0@AEBV0@@Z` | `0x20F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `??4CWbemProviderGlue@@QEAAAEAV0@AEBV0@@Z` | `0x20F30` | 66 | UnwindData |  |
| 94 | `??4KeyRef@@QEAAAEAU0@AEBU0@@Z` | `0x20F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `??4MethodContext@@QEAAAEAV0@AEBV0@@Z` | `0x20FA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `??4ParsedObjectPath@@QEAAAEAU0@AEBU0@@Z` | `0x20FF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `??4Provider@@QEAAAEAV0@AEBV0@@Z` | `0x21020` | 111 | UnwindData |  |
| 73 | `??4CAutoEvent@@QEAAAEAV0@AEBV0@@Z` | `0x210A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??4CreateMutexAsProcess@@QEAAAEAV0@AEBV0@@Z` | `0x210A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `??4WBEMTime@@QEAAAEAV0@$$QEAV0@@Z` | `0x210A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `??4WBEMTime@@QEAAAEAV0@AEBV0@@Z` | `0x210A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `??4WBEMTimeSpan@@QEAAAEAV0@$$QEAV0@@Z` | `0x210A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `??4WBEMTimeSpan@@QEAAAEAV0@AEBV0@@Z` | `0x210A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `??8WBEMTime@@QEBAHAEBV0@@Z` | `0x210F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `??8WBEMTimeSpan@@QEBAHAEBV0@@Z` | `0x210F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `??9WBEMTime@@QEBAHAEBV0@@Z` | `0x21110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `??9WBEMTimeSpan@@QEBAHAEBV0@@Z` | `0x21110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `??MWBEMTime@@QEBAHAEBV0@@Z` | `0x21130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `??MWBEMTimeSpan@@QEBAHAEBV0@@Z` | `0x21130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `??NWBEMTime@@QEBAHAEBV0@@Z` | `0x21150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `??NWBEMTimeSpan@@QEBAHAEBV0@@Z` | `0x21150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `??OWBEMTime@@QEBAHAEBV0@@Z` | `0x21170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `??OWBEMTimeSpan@@QEBAHAEBV0@@Z` | `0x21170` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `??PWBEMTime@@QEBAHAEBV0@@Z` | `0x21190` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `??PWBEMTimeSpan@@QEBAHAEBV0@@Z` | `0x21190` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `??_FCObjectPathParser@@QEAAXXZ` | `0x21340` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `??_FCThreadBase@@QEAAXXZ` | `0x21370` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `?Collate@CHString@@QEBAHPEBG@Z` | `0x213B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `?GetAllocLength@CHString@@QEBAHXZ` | `0x213D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `?GetCSDVersion@CWbemProviderGlue@@SAPEBGXZ` | `0x21400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `?GetOSMajorVersion@CWbemProviderGlue@@SAKXZ` | `0x21410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `?GetUpperBound@CHPtrArray@@QEBAHXZ` | `0x21420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `?GetUpperBound@CHStringArray@@QEBAHXZ` | `0x21420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `?Lock@CThreadBase@@AEAAXXZ` | `0x21430` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0CRegistry@@QEAA@AEBV0@@Z` | `0x214A0` | 285 | UnwindData |  |
| 20 | `??0CRegistrySearch@@QEAA@AEBV0@@Z` | `0x215D0` | 66 | UnwindData |  |
| 40 | `??0ProviderLog@@QEAA@AEBV0@@Z` | `0x21620` | 126 | UnwindData |  |
| 87 | `??4CRegistry@@QEAAAEAV0@AEBV0@@Z` | `0x216B0` | 221 | UnwindData |  |
| 88 | `??4CRegistrySearch@@QEAAAEAV0@AEBV0@@Z` | `0x217A0` | 66 | UnwindData |  |
| 98 | `??4ProviderLog@@QEAAAEAV0@AEBV0@@Z` | `0x217F0` | 92 | UnwindData |  |
| 287 | `?GetClassNameW@CRegistry@@QEAAPEAGXZ` | `0x218E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `?GetLongestClassStringSize@CRegistry@@QEAAKXZ` | `0x218F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `?GetLongestSubKeySize@CRegistry@@QEAAKXZ` | `0x21900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `?GetLongestValueName@CRegistry@@QEAAKXZ` | `0x21910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `?Destroy@CWbemGlueFactory@@QEAAXXZ` | `0x21920` | 20 | UnwindData |  |
| 437 | `?LockServer@CWbemGlueFactory@@UEAAJH@Z` | `0x21940` | 123 | UnwindData |  |
| 360 | `?GetQuery@CFrameworkQuery@@QEAAAEBVCHString@@XZ` | `0x21A20` | 384 | UnwindData |  |
| 363 | `?GetRequiredProperties@CFrameworkQuery@@QEAAXAEAVCHStringArray@@@Z` | `0x21BB0` | 52 | UnwindData |  |
| 4 | `??0CFrameworkQueryEx@@QEAA@AEBV0@@Z` | `0x21CC0` | 83 | UnwindData |  |
| 75 | `??4CFrameworkQueryEx@@QEAAAEAV0@AEBV0@@Z` | `0x21D20` | 57 | UnwindData |  |
| 402 | `?InitEx@CFrameworkQueryEx@@UEAAJQEAG0JAEAVCHString@@@Z` | `0x21FC0` | 462 | UnwindData |  |
| 418 | `?IsNTokenAnd@CFrameworkQueryEx@@QEAAHAEAVCHStringArray@@AEAVCHPtrArray@@@Z` | `0x221A0` | 357 | UnwindData |  |
| 310 | `?GetDOUBLE@CInstance@@QEBA_NPEBGAEAN@Z` | `0x22360` | 338 | UnwindData |  |
| 317 | `?GetDateTime@CInstance@@QEBA_NPEBGAEAVWBEMTime@@@Z` | `0x224C0` | 362 | UnwindData |  |
| 318 | `?GetEmbeddedObject@CInstance@@QEBA_NPEBGPEAPEAV1@PEAVMethodContext@@@Z` | `0x22630` | 496 | UnwindData |  |
| 370 | `?GetStringArray@CInstance@@QEBA_NPEBGAEAPEAUtagSAFEARRAY@@@Z` | `0x22830` | 382 | UnwindData |  |
| 374 | `?GetTimeSpan@CInstance@@QEBA_NPEBGAEAVWBEMTimeSpan@@@Z` | `0x229C0` | 362 | UnwindData |  |
| 383 | `?GetWBEMINT16@CInstance@@QEBA_NPEBGAEAF@Z` | `0x22B30` | 359 | UnwindData |  |
| 385 | `?GetWBEMINT64@CInstance@@QEBA_NPEBGAEA_J@Z` | `0x22CA0` | 93 | UnwindData |  |
| 388 | `?GetWORD@CInstance@@QEBA_NPEBGAEAG@Z` | `0x22D10` | 336 | UnwindData |  |
| 502 | `?SetCharSplat@CInstance@@QEAA_NPEBGK@Z` | `0x22E70` | 29 | UnwindData |  |
| 503 | `?SetCharSplat@CInstance@@QEAA_NPEBGPEBD@Z` | `0x22EA0` | 80 | UnwindData |  |
| 518 | `?SetEmbeddedObject@CInstance@@QEAA_NPEBGAEAV1@@Z` | `0x22F00` | 289 | UnwindData |  |
| 520 | `?SetNull@CInstance@@QEAA_NPEBG@Z` | `0x23030` | 259 | UnwindData |  |
| 525 | `?SetStatusObject@MethodContext@@QEAA_NPEAUIWbemClassObject@@@Z` | `0x23170` | 111 | UnwindData |  |
| 224 | `?DeleteInstance@Provider@@AEAAJPEAUParsedObjectPath@@JPEAVMethodContext@@@Z` | `0x231F0` | 170 | UnwindData |  |
| 463 | `?PutInstance@Provider@@AEAAJPEAUIWbemClassObject@@JPEAVMethodContext@@@Z` | `0x232A0` | 197 | UnwindData |  |
| 555 | `?ValidatePutInstanceFlags@Provider@@MEAAJJ@Z` | `0x23370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `DoCmd` | `0x23390` | 756 | UnwindData |  |
| 218 | `?DecrementObjectCount@CWbemProviderGlue@@SAJXZ` | `0x237B0` | 99 | UnwindData |  |
| 226 | `?DeleteInstanceAsync@CWbemProviderGlue@@UEAAJQEAGJPEAUIWbemContext@@PEAUIWbemObjectSink@@@Z` | `0x23820` | 1,252 | UnwindData |  |
| 249 | `?FillInstance@CWbemProviderGlue@@SAJPEAVCInstance@@PEBG@Z` | `0x23D10` | 180 | UnwindData |  |
| 250 | `?FillInstance@CWbemProviderGlue@@SAJPEAVMethodContext@@PEAVCInstance@@@Z` | `0x23DD0` | 152 | UnwindData |  |
| 272 | `?GetAllDerivedInstances@CWbemProviderGlue@@SAJPEBGPEAV?$TRefPointerCollection@VCInstance@@@@PEAVMethodContext@@0@Z` | `0x23E70` | 125 | UnwindData |  |
| 273 | `?GetAllDerivedInstancesAsynch@CWbemProviderGlue@@SAJPEBGPEAVProvider@@P6AJ1PEAVCInstance@@PEAVMethodContext@@PEAX@Z034@Z` | `0x23F00` | 145 | UnwindData |  |
| 274 | `?GetAllInstances@CWbemProviderGlue@@SAJPEBGPEAV?$TRefPointerCollection@VCInstance@@@@0PEAVMethodContext@@@Z` | `0x23FA0` | 128 | UnwindData |  |
| 275 | `?GetAllInstancesAsynch@CWbemProviderGlue@@SAJPEBGPEAVProvider@@P6AJ1PEAVCInstance@@PEAVMethodContext@@PEAX@Z034@Z` | `0x24030` | 148 | UnwindData |  |
| 320 | `?GetEmptyInstance@CWbemProviderGlue@@SAJPEBGPEAPEAVCInstance@@0@Z` | `0x240D0` | 259 | UnwindData |  |
| 368 | `?GetStatusObject@CWbemProviderGlue@@CAPEAUIWbemClassObject@@PEAVMethodContext@@PEBG@Z` | `0x241E0` | 373 | UnwindData |  |
| 395 | `?IncrementObjectCount@CWbemProviderGlue@@SAXXZ` | `0x24360` | 89 | UnwindData |  |
| 449 | `?NullOutUnsetProperties@CWbemProviderGlue@@AEAAJPEAUIWbemClassObject@@PEAPEAU2@AEBUtagVARIANT@@@Z` | `0x243C0` | 750 | UnwindData |  |
| 458 | `?PreProcessPutInstanceParms@CWbemProviderGlue@@AEAAJPEAUIWbemClassObject@@PEAPEAU2@PEAUIWbemContext@@@Z` | `0x246C0` | 444 | UnwindData |  |
| 465 | `?PutInstanceAsync@CWbemProviderGlue@@UEAAJPEAUIWbemClassObject@@JPEAUIWbemContext@@PEAUIWbemObjectSink@@@Z` | `0x24890` | 1,194 | UnwindData |  |
| 524 | `?SetStatusObject@CWbemProviderGlue@@SA_NPEAVMethodContext@@PEBG1JPEBUtagSAFEARRAY@@2@Z` | `0x24D40` | 593 | UnwindData |  |
| 33 | `??0KeyRef@@QEAA@PEBGPEBUtagVARIANT@@@Z` | `0x25070` | 130 | UnwindData |  |
| 163 | `?AddKeyRef@ParsedObjectPath@@QEAAHPEBGPEBUtagVARIANT@@@Z` | `0x25100` | 204 | UnwindData |  |
| 164 | `?AddKeyRefEx@ParsedObjectPath@@QEAAHPEBGPEBUtagVARIANT@@@Z` | `0x251E0` | 716 | UnwindData |  |
| 190 | `?ClearKeys@ParsedObjectPath@@QEAAXXZ` | `0x254C0` | 124 | UnwindData |  |
| 330 | `?GetKeyString@ParsedObjectPath@@QEAAPEAGXZ` | `0x25550` | 573 | UnwindData |  |
| 348 | `?GetNamespacePart@ParsedObjectPath@@QEAAPEAGXZ` | `0x257A0` | 237 | UnwindData |  |
| 355 | `?GetParentNamespacePart@ParsedObjectPath@@QEAAPEAGXZ` | `0x258A0` | 241 | UnwindData |  |
| 362 | `?GetRelativePath@CObjectPathParser@@SAPEAGPEAG@Z` | `0x259A0` | 40 | UnwindData |  |
| 504 | `?SetClassName@ParsedObjectPath@@QEAAHPEBG@Z` | `0x259D0` | 61 | UnwindData |  |
| 30 | `??0CWinMsgEvent@@QEAA@AEBV0@@Z` | `0x25A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??0CWinMsgEvent@@QEAA@XZ` | `0x25A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `??1CWinMsgEvent@@QEAA@XZ` | `0x25A40` | 91 | UnwindData |  |
| 92 | `??4CWinMsgEvent@@QEAAAEAV0@AEBV0@@Z` | `0x25AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `?CtrlHandlerRoutine@CWinMsgEvent@@CAHK@Z` | `0x25AC0` | 49 | UnwindData |  |
| 230 | `?DestroyMsgWindow@CWinMsgEvent@@CAXXZ` | `0x25B00` | 174 | UnwindData |  |
| 542 | `?UnRegisterAllMessages@CWinMsgEvent@@IEAAXXZ` | `0x25BC0` | 312 | UnwindData |  |
| 562 | `?dwThreadProc@CWinMsgEvent@@CAKPEAX@Z` | `0x25D00` | 73 | UnwindData |  |
| 12 | `??0CHString@@QEAA@PEBGH@Z` | `0x264F0` | 88 | UnwindData |  |
| 79 | `??4CHString@@QEAAAEBV0@G@Z` | `0x26560` | 38 | UnwindData |  |
| 127 | `??H@YA?AVCHString@@GAEBV0@@Z` | `0x26590` | 101 | UnwindData |  |
| 177 | `?AllocSysString@CHString@@QEBAPEAGXZ` | `0x26600` | 75 | UnwindData |  |
| 253 | `?FindOneOf@CHString@@QEBAHPEBG@Z` | `0x26660` | 47 | UnwindData |  |
| 256 | `?Format@CHString@@QEAAXIZZ` | `0x266A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `?FormatMessageW@CHString@@QEAAXIZZ` | `0x266A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `?FormatMessageW@CHString@@QEAAXPEBGZZ` | `0x266C0` | 187 | UnwindData |  |
| 269 | `?FreeExtra@CHString@@QEAAXXZ` | `0x26790` | 121 | UnwindData |  |
| 428 | `?LoadStringW@CHString@@IEAAHIPEAGI@Z` | `0x26810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `?LoadStringW@CHString@@QEAAHI@Z` | `0x26810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `?LockBuffer@CHString@@QEAAPEAGXZ` | `0x26820` | 51 | UnwindData |  |
| 441 | `?MakeReverse@CHString@@QEAAXXZ` | `0x26860` | 34 | UnwindData |  |
| 538 | `?SpanIncluding@CHString@@QEBA?AV1@PEBG@Z` | `0x26890` | 63 | UnwindData |  |
| 539 | `?TrimLeft@CHString@@QEAAXXZ` | `0x268E0` | 154 | UnwindData |  |
| 540 | `?TrimRight@CHString@@QEAAXXZ` | `0x26980` | 155 | UnwindData |  |
| 545 | `?UnlockBuffer@CHString@@QEAAXXZ` | `0x26A30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??0WBEMTimeSpan@@QEAA@AEB_J@Z` | `0x26A60` | 24 | UnwindData |  |
| 109 | `??4WBEMTimeSpan@@QEAAAEBV0@AEB_J@Z` | `0x26A80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `??4WBEMTimeSpan@@QEAAAEBV0@QEAG@Z` | `0x26AB0` | 243 | UnwindData |  |
| 130 | `??HWBEMTimeSpan@@QEBA?AV0@AEBV0@@Z` | `0x26BB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `??YWBEMTime@@QEAAAEBV0@AEBVWBEMTimeSpan@@@Z` | `0x26BE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `??YWBEMTimeSpan@@QEAAAEBV0@AEBV0@@Z` | `0x26BE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `??ZWBEMTime@@QEAAAEBV0@AEBVWBEMTimeSpan@@@Z` | `0x26C10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `??ZWBEMTimeSpan@@QEAAAEBV0@AEBV0@@Z` | `0x26C10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `?GetFILETIME@WBEMTimeSpan@@QEBAHPEAU_FILETIME@@@Z` | `0x26C40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `?GetLocalOffsetForDate@WBEMTime@@SAJAEB_J@Z` | `0x26C70` | 55 | UnwindData |  |
| 335 | `?GetLocalOffsetForDate@WBEMTime@@SAJPEBU_FILETIME@@@Z` | `0x26CB0` | 73 | UnwindData |  |
| 337 | `?GetLocalOffsetForDate@WBEMTime@@SAJPEBUtm@@@Z` | `0x26D00` | 66 | UnwindData |  |
| 391 | `?Gettime_t@WBEMTime@@QEBAHPEA_J@Z` | `0x26D50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `?Gettime_t@WBEMTimeSpan@@QEBAHPEA_J@Z` | `0x26DB0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `?Append@CHStringArray@@QEAAHAEBV1@@Z` | `0x26E50` | 77 | UnwindData |  |
| 201 | `?Copy@CHStringArray@@QEAAXAEBV1@@Z` | `0x26EB0` | 53 | UnwindData |  |
| 268 | `?FreeExtra@CHPtrArray@@QEAAXXZ` | `0x26F40` | 119 | UnwindData |  |
| 270 | `?FreeExtra@CHStringArray@@QEAAXXZ` | `0x26F40` | 119 | UnwindData |  |
| 406 | `?InsertAt@CHStringArray@@QEAAXHPEAV1@@Z` | `0x26FC0` | 178 | UnwindData |  |
| 407 | `?InsertAt@CHStringArray@@QEAAXHPEBGH@Z` | `0x27080` | 194 | UnwindData |  |
| 482 | `?RemoveAt@CHStringArray@@QEAAXHH@Z` | `0x27150` | 120 | UnwindData |  |
| 178 | `?Append@CHPtrArray@@QEAAHAEBV1@@Z` | `0x271D0` | 81 | UnwindData |  |
| 200 | `?Copy@CHPtrArray@@QEAAXAEBV1@@Z` | `0x27230` | 57 | UnwindData |  |
| 404 | `?InsertAt@CHPtrArray@@QEAAXHPEAV1@@Z` | `0x27270` | 114 | UnwindData |  |
| 405 | `?InsertAt@CHPtrArray@@QEAAXHPEAXH@Z` | `0x272F0` | 417 | UnwindData |  |
| 481 | `?RemoveAt@CHPtrArray@@QEAAXHH@Z` | `0x274A0` | 75 | UnwindData |  |
| 491 | `?SetAt@CHPtrArray@@QEAAXHPEAX@Z` | `0x27500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??0CRegistrySearch@@QEAA@XZ` | `0x27520` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `??1CRegistrySearch@@QEAA@XZ` | `0x27550` | 32 | UnwindData |  |
| 185 | `?CheckAndAddToList@CRegistrySearch@@AEAAXPEAVCRegistry@@VCHString@@1AEAVCHPtrArray@@11H@Z` | `0x27580` | 366 | UnwindData |  |
| 221 | `?DeleteCurrentKeyValue@CRegistry@@QEAAKPEAUHKEY__@@PEBG@Z` | `0x27700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `?myRegDeleteValue@CRegistry@@AEAAJPEAUHKEY__@@PEBG@Z` | `0x27700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `?DeleteCurrentKeyValue@CRegistry@@QEAAKPEBG@Z` | `0x27720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `?DeleteValue@CRegistry@@QEAAJPEBG@Z` | `0x27720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `?DeleteKey@CRegistry@@QEAAJPEAVCHString@@@Z` | `0x27740` | 61 | UnwindData |  |
| 271 | `?FreeSearchList@CRegistrySearch@@QEAAHHAEAVCHPtrArray@@@Z` | `0x27790` | 114 | UnwindData |  |
| 291 | `?GetCurrentBinaryKeyValue@CRegistry@@QEAAKPEAUHKEY__@@PEBGPEAEPEAK@Z` | `0x27810` | 40 | UnwindData |  |
| 292 | `?GetCurrentBinaryKeyValue@CRegistry@@QEAAKPEBGAEAVCHString@@@Z` | `0x27840` | 265 | UnwindData |  |
| 301 | `?GetCurrentRawSubKeyValue@CRegistry@@AEAAKPEBGPEAXPEAK2@Z` | `0x27950` | 96 | UnwindData |  |
| 305 | `?GetCurrentSubKeyValue@CRegistry@@QEAAKPEBGAEAK@Z` | `0x279C0` | 68 | UnwindData |  |
| 307 | `?GetCurrentSubKeyValue@CRegistry@@QEAAKPEBGPEAXPEAK@Z` | `0x27A10` | 85 | UnwindData |  |
| 432 | `?LocateKeyByNameOrValueName@CRegistrySearch@@QEAAHPEAUHKEY__@@PEBG1PEAPEBGKAEAVCHString@@3@Z` | `0x27A70` | 588 | UnwindData |  |
| 453 | `?OpenCurrentUser@CRegistry@@QEAAKPEBGK@Z` | `0x27CD0` | 298 | UnwindData |  |
| 489 | `?SearchAndBuildList@CRegistrySearch@@QEAAHVCHString@@AEAVCHPtrArray@@00HPEAUHKEY__@@@Z` | `0x27E00` | 644 | UnwindData |  |
| 506 | `?SetCurrentKeyValue@CRegistry@@QEAAKPEAUHKEY__@@PEBGAEAK@Z` | `0x28090` | 54 | UnwindData |  |
| 507 | `?SetCurrentKeyValue@CRegistry@@QEAAKPEAUHKEY__@@PEBGAEAVCHString@@@Z` | `0x280D0` | 85 | UnwindData |  |
| 508 | `?SetCurrentKeyValue@CRegistry@@QEAAKPEAUHKEY__@@PEBGAEAVCHStringArray@@@Z` | `0x28130` | 409 | UnwindData |  |
| 509 | `?SetCurrentKeyValue@CRegistry@@QEAAKPEBGAEAK@Z` | `0x282D0` | 45 | UnwindData |  |
| 510 | `?SetCurrentKeyValue@CRegistry@@QEAAKPEBGAEAVCHString@@@Z` | `0x28310` | 84 | UnwindData |  |
| 511 | `?SetCurrentKeyValue@CRegistry@@QEAAKPEBGAEAVCHStringArray@@@Z` | `0x28370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `?SetCurrentKeyValueExpand@CRegistry@@QEAAKPEAUHKEY__@@PEBGAEAVCHString@@@Z` | `0x28390` | 85 | UnwindData |  |
| 583 | `?myRegDeleteKey@CRegistry@@AEAAJPEAUHKEY__@@PEBG@Z` | `0x283F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `?myRegSetValueEx@CRegistry@@AEAAJPEAUHKEY__@@PEBGKKPEBEK@Z` | `0x28420` | 63 | UnwindData |  |
| 149 | `??_7CThreadBase@@6B@` | `0x2C008` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `??_7MethodContext@@6B@` | `0x2C020` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `??_7CFrameworkQueryEx@@6B@` | `0x2C080` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `??_7CWbemProviderGlue@@6BIWbemServices@@@` | `0x2C0D8` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `??_7CWbemProviderGlue@@6BIWbemProviderInit@@@` | `0x2C1B8` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `??_7CInstance@@6B@` | `0x2C210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `??_7Provider@@6B@` | `0x2C240` | 136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `??_7CWbemGlueFactory@@6B@` | `0x2C2C8` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `??_7ProviderLog@@6B@` | `0x2C2F8` | 2,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `??_7CWinMsgEvent@@6B@` | `0x2CE18` | 111,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `?captainsLog@@3VProviderLog@@A` | `0x482C0` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `?s_strComputerName@Provider@@0VCHString@@A` | `0x48318` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `?s_providersmap@CWbemProviderGlue@@0V?$map@VCHString@@PEAXU?$less@VCHString@@@std@@V?$allocator@U?$pair@$$CBVCHString@@PEAX@std@@@3@@std@@A` | `0x48320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 600 | `?s_csFactoryMap@CWbemProviderGlue@@0VCCritSec@@A` | `0x48330` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `?s_factorymap@CWbemProviderGlue@@0V?$map@PEBXPEAJU?$less@PEBX@std@@V?$allocator@U?$pair@QEBXPEAJ@std@@@2@@std@@A` | `0x48358` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `?s_csProviderMap@CWbemProviderGlue@@0VCCritSec@@A` | `0x48368` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 573 | `?m_csStatusObject@CWbemProviderGlue@@0VCCritSec@@A` | `0x48390` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `?m_FlushPtrs@CWbemProviderGlue@@0V?$set@PEAXU?$less@PEAX@std@@V?$allocator@PEAX@2@@std@@A` | `0x483B8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 572 | `?m_csFlushPtrs@CWbemProviderGlue@@0VCCritSec@@A` | `0x483C8` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `?mg_csMapLock@CWinMsgEvent@@0VCCritSec@@A` | `0x48420` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 577 | `?mg_csWindowLock@CWinMsgEvent@@0VCCritSec@@A` | `0x48448` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 575 | `?mg_aeCreateWindow@CWinMsgEvent@@0VCAutoEvent@@A` | `0x48470` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 581 | `?mg_oSinkMap@CWinMsgEvent@@0V?$multimap@IPEAVCWinMsgEvent@@U?$less@I@std@@V?$allocator@U?$pair@$$CBIPEAVCWinMsgEvent@@@std@@@3@@std@@A` | `0x48478` | 200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 566 | `?initFailed_@Provider@@0HA` | `0x48540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 610 | `?s_wstrCSDVersion@CWbemProviderGlue@@0PAGA` | `0x48550` | 520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 602 | `?s_dwMajorVersion@CWbemProviderGlue@@0KA` | `0x48758` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 604 | `?s_dwPlatform@CWbemProviderGlue@@0KA` | `0x4875C` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `?s_lObjects@CWbemProviderGlue@@0JA` | `0x48760` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 599 | `?s_bInitted@CWbemProviderGlue@@0HA` | `0x48764` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `?m_pStatusObject@CWbemProviderGlue@@0PEAUIWbemClassObject@@EA` | `0x48768` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `?mg_hDevNotify@CWinMsgEvent@@0PEAXEA` | `0x48770` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `?mg_hWnd@CWinMsgEvent@@0PEAUHWND__@@EA` | `0x48778` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `?mg_hThreadPumpHandle@CWinMsgEvent@@0PEAXEA` | `0x48780` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `?s_fPlatformSet@CRegistry@@0HA` | `0x48798` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | `?s_dwPlatform@CRegistry@@0KA` | `0x4879C` | 0 | Indeterminate |  |
