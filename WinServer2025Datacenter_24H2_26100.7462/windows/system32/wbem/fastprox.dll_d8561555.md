# Binary Specification: fastprox.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\fastprox.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d8561555e6667e631043716619d4494d1ec0b0a83b30a6055514a0286474e821`
* **Total Exported Functions:** 1572

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1192 | `?MarshalInterface@CWbemObject@@UEAAJPEAUIStream@@AEBU_GUID@@PEAXK2K@Z` | `0x1070` | 271 | UnwindData |  |
| 686 | `?GetArrayPropAddrByHandle@CWbemObject@@UEAAJJJPEAKPEAPEAX@Z` | `0x1240` | 456 | UnwindData |  |
| 685 | `?GetArrayByHandle@CWbemObject@@QEAAPEAVCUntypedArray@@J@Z` | `0x1410` | 190 | UnwindData |  |
| 1226 | `?Put@CWbemInstance@@UEAAJPEBGJPEAUtagVARIANT@@J@Z` | `0x2050` | 837 | UnwindData |  |
| 1247 | `?ReadPropertyValue@CWbemObject@@UEAAJJJPEAJPEAE@Z` | `0x23A0` | 1,124 | UnwindData |  |
| 602 | `?ElementMaxSize@CFastHeap@@QEAAHK@Z` | `0x2810` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `?GetStringLength@CCompressedString@@QEBAHXZ` | `0x2840` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 900 | `?GetObjectW@CWbemClassCache@@QEAAJAEAU_GUID@@PEAPEAUIWbemClassObject@@@Z` | `0x28C0` | 342 | UnwindData |  |
| 1245 | `?ReadDWORD@CWbemObject@@UEAAJJPEAK@Z` | `0x2A20` | 542 | UnwindData |  |
| 733 | `?GetDefaultByHandle@CClassPart@@QEAAJJJPEAJPEAE@Z` | `0x2C50` | 232 | UnwindData |  |
| 489 | `?CompareTo@CQualifierSet@@UEAAJJPEAUIWbemQualifierSet@@@Z` | `0x2DC0` | 1,719 | UnwindData |  |
| 1365 | `?SetData@CWbemDataPacket@@QEAAXPEAEK_N@Z` | `0x48C0` | 184 | UnwindData |  |
| 95 | `??0CWbemSmartEnumNextPacket@@QEAA@PEAEK_N@Z` | `0x4980` | 32 | UnwindData |  |
| 1370 | `?SetData@CWbemSmartEnumNextPacket@@QEAAXPEAEK_N@Z` | `0x49B0` | 614 | UnwindData |  |
| 1492 | `?UnmarshalPacket@CWbemSmartEnumNextPacket@@QEAAJAEAJAEAPEAPEAUIWbemClassObject@@AEAVCWbemClassCache@@@Z` | `0x4FF0` | 683 | UnwindData |  |
| 1157 | `?IsValid@CWbemDataPacket@@QEAAJJ@Z` | `0x59D0` | 213 | UnwindData |  |
| 1491 | `?UnmarshalPacket@CWbemObjectArrayPacket@@QEAAJAEAJAEAPEAPEAUIWbemClassObject@@AEAVCWbemClassCache@@@Z` | `0x6C00` | 3,037 | UnwindData |  |
| 725 | `?GetClasslessInstanceObject@CWbemObjectArrayPacket@@AEAAJAEAVCWbemObjectPacket@@PEAPEAUIWbemClassObject@@AEAVCWbemClassCache@@@Z` | `0x7DD0` | 1,375 | UnwindData |  |
| 642 | `?ExtendHeapSize@CInstancePart@@UEAAHPEAEKK@Z` | `0x86D0` | 66 | UnwindData |  |
| 1158 | `?IsValid@CWbemObjectArrayPacket@@QEAA_NPEAVCWbemClassCache@@@Z` | `0x8A60` | 2,331 | UnwindData |  |
| 641 | `?ExtendHeapSize@CClassPart@@UEAAHPEAEKK@Z` | `0x93C0` | 155 | UnwindData |  |
| 1249 | `?ReallocAndCompact@CClassPart@@QEAAHK@Z` | `0x94B0` | 90 | UnwindData |  |
| 646 | `?ExtendPropertyTableSpace@CClassPart@@UEAAHPEAEKK@Z` | `0x9830` | 253 | UnwindData |  |
| 787 | `?GetInstanceObject@CWbemObjectArrayPacket@@AEAAJAEAVCWbemObjectPacket@@PEAPEAUIWbemClassObject@@AEAVCWbemClassCache@@@Z` | `0x99D0` | 543 | UnwindData |  |
| 1366 | `?SetData@CWbemInstance@@QEAAXPEAEHK@Z` | `0x9C90` | 300 | UnwindData |  |
| 360 | `?AddObject@CWbemClassCache@@QEAAJAEAU_GUID@@PEAUIWbemClassObject@@@Z` | `0x9DD0` | 377 | UnwindData |  |
| 639 | `?ExtendDataTableSpace@CClassPart@@UEAAHPEAEKK@Z` | `0x9F50` | 228 | UnwindData |  |
| 648 | `?ExtendQualifierSetSpace@CClassPart@@UEAAHPEAVCBasicQualifierSet@@K@Z` | `0xA500` | 304 | UnwindData |  |
| 1203 | `?Merge@CDataTable@@SAPEAEPEAV1@PEAVCFastHeap@@01PEAVCPropertyLookupTable@@PEAE1@Z` | `0xA640` | 459 | UnwindData |  |
| 1201 | `?Merge@CClassAndMethods@@SAPEAEAEAV1@0PEAEH@Z` | `0xA820` | 129 | UnwindData |  |
| 1202 | `?Merge@CClassPart@@SAPEAEAEAV1@0PEAEH@Z` | `0xA8B0` | 565 | UnwindData |  |
| 1205 | `?Merge@CMethodPart@@SAPEAEAEAV1@0PEAEK@Z` | `0xAAF0` | 1,263 | UnwindData |  |
| 1204 | `?Merge@CDerivationList@@SAPEAEAEAVCCompressedStringList@@0PEAE@Z` | `0xAFF0` | 123 | UnwindData |  |
| 1200 | `?Merge@CBasicQualifierSet@@SAPEAEPEAEPEAVCFastHeap@@0101H@Z` | `0xB080` | 329 | UnwindData |  |
| 943 | `?GetPropertyString@CWbemObject@@QEAAPEAVCCompressedString@@J@Z` | `0xB1D0` | 195 | UnwindData |  |
| 926 | `?GetPropertyCount@CClassPart@@QEAAJPEAVCVar@@@Z` | `0xB2A0` | 178 | UnwindData |  |
| 968 | `?GetQualifierLocally@CBasicQualifierSet@@SAPEAUCQualifier@@PEAEPEAVCFastHeap@@PEAVCCompressedString@@@Z` | `0xB360` | 124 | UnwindData |  |
| 784 | `?GetIndexedProps@CClassPart@@QEAAHAEAVCWStringArray@@@Z` | `0xB3F0` | 370 | UnwindData |  |
| 875 | `?GetNames@CWbemObject@@UEAAJPEBGJPEAUtagVARIANT@@PEAPEAUtagSAFEARRAY@@@Z` | `0xB570` | 3,062 | UnwindData |  |
| 1552 | `?WritePropertyValue@CWbemObject@@UEAAJJJPEBE@Z` | `0xC1F0` | 1,674 | UnwindData |  |
| 1215 | `?NValidateSize@CCompressedString@@QEBA_NH@Z` | `0xC880` | 21 | UnwindData |  |
| 1206 | `?Merge@CPropertyLookupTable@@SAPEAEPEAV1@PEAVCFastHeap@@01PEAE1H@Z` | `0xC8A0` | 818 | UnwindData |  |
| 800 | `?GetKeyProps@CClassPart@@QEAAHAEAVCWStringArray@@@Z` | `0xCBE0` | 440 | UnwindData |  |
| 1189 | `?MapLimitation@CPropertyLookupTable@@QEAAHJPEAVCWStringArray@@PEAVCLimitationMapping@@@Z` | `0xCDA0` | 399 | UnwindData |  |
| 1330 | `?ResolveString@CFastHeap@@QEAAPEAVCCompressedString@@K@Z` | `0xD030` | 200 | UnwindData |  |
| 574 | `?CreateWStringCopy@CCompressedString@@QEBA?AVWString@@XZ` | `0xD100` | 377 | UnwindData |  |
| 1460 | `?StartsWithNoCase@CCompressedString@@QEBAHPEBG@Z` | `0xD280` | 184 | UnwindData |  |
| 627 | `?EstimateMergeSpace@CWbemClass@@QEAAKPEAEJ@Z` | `0xD3D0` | 199 | UnwindData |  |
| 523 | `?CopyToNewHeap@CEmbeddedObject@@SAHKPEAVCFastHeap@@0AEFAK@Z` | `0xD4A0` | 136 | UnwindData |  |
| 747 | `?GetEmbeddedObj@CWbemObject@@QEAAPEAV1@J@Z` | `0xD530` | 203 | UnwindData |  |
| 1468 | `?StripClassPart@CWbemInstance@@UEAAJXZ` | `0xD610` | 568 | UnwindData |  |
| 658 | `?FindMethod@CMethodPart@@IEAAHPEBG@Z` | `0xD920` | 151 | UnwindData |  |
| 979 | `?GetQualifierSetStart@CMethodQualifierSetContainer@@UEAAPEAEXZ` | `0xD9C0` | 121 | UnwindData |  |
| 567 | `?CreateLimitedRepresentation@CQualifierSetList@@QEAAPEAEPEAVCLimitationMapping@@PEAVCFastHeap@@1PEAE@Z` | `0xDDD0` | 291 | UnwindData |  |
| 503 | `?ComputeNecessarySpaceForPropagation@CBasicQualifierSet@@SAKPEAEE@Z` | `0xDFB0` | 102 | UnwindData |  |
| 1548 | `?WritePropagatedVersion@CBasicQualifierSet@@SAPEAEPEAVCPtrSource@@E0PEAVCFastHeap@@1@Z` | `0xE020` | 407 | UnwindData |  |
| 565 | `?CreateLimitedRepresentation@CInstancePart@@QEAAPEAEPEAVCLimitationMapping@@HPEAE@Z` | `0xE200` | 500 | UnwindData |  |
| 1322 | `?RemoveSpecific@CLimitationMapping@@QEAAXXZ` | `0xE400` | 108 | UnwindData |  |
| 562 | `?CreateLimitedRepresentation@CDataTable@@QEAAPEAEPEAVCLimitationMapping@@HPEAVCFastHeap@@1PEAE@Z` | `0xE480` | 883 | UnwindData |  |
| 749 | `?GetFirstQualifier@CBasicQualifierSet@@QEAAPEAUCQualifier@@XZ` | `0xE800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `?GetStart@CMethodPart@@QEAAPEAEXZ` | `0xE800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `?GetStart@CQualifierSetList@@QEAAPEAEXZ` | `0xE800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `?CopyToNewHeap@CUntypedArray@@SAHKVCType@@PEAVCFastHeap@@1AEFAK@Z` | `0xE810` | 275 | UnwindData |  |
| 566 | `?CreateLimitedRepresentation@CPropertyLookupTable@@QEAAPEAEPEAVCLimitationMapping@@PEAVCFastHeap@@PEAEAEAH@Z` | `0xE9D0` | 888 | UnwindData |  |
| 522 | `?CopyToNewHeap@CCompressedString@@SAHKPEAVCFastHeap@@0AEFAK@Z` | `0xED50` | 560 | UnwindData |  |
| 1477 | `?TranslateToNewHeap@CUntypedArray@@SAHPEAVCPtrSource@@VCType@@PEAVCFastHeap@@2@Z` | `0xEF90` | 773 | UnwindData |  |
| 1259 | `?Rebase@CDecorationPart@@QEAAXPEAE@Z` | `0xF2A0` | 61 | UnwindData |  |
| 1328 | `?ResolveHeapPointer@CFastHeap@@QEAAPEAEK@Z` | `0xF340` | 42 | UnwindData |  |
| 384 | `?Allocate@CFastHeap@@QEAAHKAEFAK@Z` | `0xF370` | 297 | UnwindData |  |
| 22 | `??0CClassAndMethods@@QEAA@XZ` | `0xF4A0` | 68 | UnwindData |  |
| 561 | `?CreateLimitedRepresentation@CClassPart@@QEAAPEAEPEAVCLimitationMapping@@HPEAEAEAH@Z` | `0xF4F0` | 724 | UnwindData |  |
| 1472 | `?TranslateToNewHeap@CBasicQualifierSet@@SAHPEAVCPtrSource@@PEAVCFastHeap@@1@Z` | `0xF7D0` | 204 | UnwindData |  |
| 1008 | `?GetStart@CFastHeap@@QEAAPEAEXZ` | `0x10B10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??0CWbemClass@@QEAA@XZ` | `0x10B40` | 370 | UnwindData |  |
| 452 | `?Clone@CWbemClass@@UEAAJPEAPEAUIWbemClassObject@@@Z` | `0x10CC0` | 683 | UnwindData |  |
| 813 | `?GetLength@CCompressedString@@QEBAHXZ` | `0x10F80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1364 | `?SetData@CWbemClass@@UEAAXPEAEH@Z` | `0x10FE0` | 1,772 | UnwindData |  |
| 1267 | `?Rebase@CWbemInstance@@QEAAXPEAE@Z` | `0x116E0` | 283 | UnwindData |  |
| 644 | `?ExtendInstancePartSpace@CWbemInstance@@UEAAHPEAVCInstancePart@@K@Z` | `0x11950` | 43 | UnwindData |  |
| 1261 | `?Rebase@CInstancePart@@QEAAXPEAE@Z` | `0x11CF0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `?Clone@CWbemInstance@@UEAAJPEAPEAUIWbemClassObject@@@Z` | `0x11D70` | 1,569 | UnwindData |  |
| 461 | `?Compact@CClassAndMethods@@QEAAXXZ` | `0x123E0` | 148 | UnwindData |  |
| 462 | `?Compact@CClassPart@@QEAAXXZ` | `0x12480` | 405 | UnwindData |  |
| 455 | `?CloneAndDecorate@CWbemInstance@@UEAAJJPEAG0PEAPEAUIWbemClassObject@@@Z` | `0x12620` | 2,741 | UnwindData |  |
| 1479 | `?Trim@CFastHeap@@QEAAXXZ` | `0x130E0` | 23 | UnwindData |  |
| 816 | `?GetLength@CDecorationPart@@QEAAKXZ` | `0x13260` | 33 | UnwindData |  |
| 1560 | `?fast_wcslen@CCompressedString@@SAHPEBG@Z` | `0x13330` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `?SetNullness@CDataTable@@QEAAXHH@Z` | `0x133E0` | 147 | UnwindData |  |
| 1133 | `?IsNull@CDataTable@@QEAAHH@Z` | `0x13480` | 124 | UnwindData |  |
| 1456 | `?SpawnInstance@CWbemClass@@UEAAJJPEAPEAUIWbemClassObject@@@Z` | `0x13510` | 3,850 | UnwindData |  |
| 1069 | `?InitEmptyInstance@CWbemInstance@@QEAAJAEAVCClassPart@@PEAEHPEAVCDecorationPart@@@Z` | `0x14420` | 2,316 | UnwindData |  |
| 530 | `?Create@CInstancePart@@QEAAPEAEPEAEPEAVCClassPart@@PEAVCInstancePartContainer@@@Z` | `0x14D40` | 100 | UnwindData |  |
| 1070 | `?InitNew@CWbemInstance@@QEAAJPEAVCWbemClass@@HPEAVCDecorationPart@@@Z` | `0x15470` | 45 | UnwindData |  |
| 1335 | `?SetAllToDefault@CDataTable@@QEAAXXZ` | `0x15F80` | 20 | UnwindData |  |
| 520 | `?CopyNullness@CDataTable@@QEAAXPEAV1@@Z` | `0x16040` | 27 | UnwindData |  |
| 1380 | `?SetDefaultness@CDataTable@@QEAAXHH@Z` | `0x161C0` | 150 | UnwindData |  |
| 1102 | `?IsDefault@CDataTable@@QEAAHH@Z` | `0x16260` | 127 | UnwindData |  |
| 46 | `??0CInstanceQualifierSet@@QEAA@H@Z` | `0x16440` | 107 | UnwindData |  |
| 1160 | `?IsValidInstancePart@CInstancePart@@QEAAJPEAVCClassPart@@AEAV?$vector@UEmbeddedObj@@V?$wbem_allocator@UEmbeddedObj@@@@@std@@@Z` | `0x164C0` | 2,715 | UnwindData |  |
| 1168 | `?IsValidQualifierSet@CBasicQualifierSet@@QEAAJXZ` | `0x16F90` | 1,115 | UnwindData |  |
| 1356 | `?SetData@CInstancePart@@QEAAXPEAEPEAVCInstancePartContainer@@AEAVCClassPart@@_K@Z` | `0x174B0` | 52 | UnwindData |  |
| 1351 | `?SetData@CClassPart@@QEAAXPEAEPEAVCClassPartContainer@@PEAV1@@Z` | `0x17980` | 481 | UnwindData |  |
| 86 | `??0CWbemInstance@@QEAA@XZ` | `0x17B70` | 1,238 | UnwindData |  |
| 1353 | `?SetData@CDataTable@@QEAAXPEAEHHPEAVCDataTableContainer@@@Z` | `0x18050` | 163 | UnwindData |  |
| 25 | `??0CClassPart@@QEAA@XZ` | `0x18100` | 176 | UnwindData |  |
| 40 | `??0CInstancePart@@QEAA@XZ` | `0x181C0` | 176 | UnwindData |  |
| 65 | `??0CQualifierSet@@QEAA@HH@Z` | `0x18280` | 94 | UnwindData |  |
| 31 | `??0CClassQualifierSet@@QEAA@H@Z` | `0x182F0` | 107 | UnwindData |  |
| 1214 | `?MergeClassPart@CWbemInstance@@UEAAJPEAUIWbemClassObject@@@Z` | `0x18370` | 1,526 | UnwindData |  |
| 1525 | `?ValidateBuffer@CInstancePart@@SA_KPEAE_KAEAVCClassPart@@AEAV?$vector@UEmbeddedObj@@V?$wbem_allocator@UEmbeddedObj@@@@@std@@@Z` | `0x18970` | 2,485 | UnwindData |  |
| 1540 | `?ValidateSize@CCompressedString@@QEBAHH@Z` | `0x19C30` | 612 | UnwindData |  |
| 1523 | `?ValidateBuffer@CEmbeddedObject@@SAXPEAE_KAEAV?$vector@UEmbeddedObj@@V?$wbem_allocator@UEmbeddedObj@@@@@std@@@Z` | `0x19EA0` | 143 | UnwindData |  |
| 1522 | `?ValidateBuffer@CDecorationPart@@SA_KPEAE_K@Z` | `0x19F40` | 111 | UnwindData |  |
| 1520 | `?ValidateBuffer@CCompressedStringList@@SA_KPEAE_K@Z` | `0x19FC0` | 606 | UnwindData |  |
| 1531 | `?ValidateBuffer@CWbemInstance@@SA_KPEAEHPEAV1@AEAV?$vector@UEmbeddedObj@@V?$wbem_allocator@UEmbeddedObj@@@@@std@@@Z` | `0x1A2C0` | 240 | UnwindData |  |
| 1532 | `?ValidateBuffer@CWbemInstance@@SA_KPEAE_KAEAV?$vector@UEmbeddedObj@@V?$wbem_allocator@UEmbeddedObj@@@@@std@@@Z` | `0x1A3C0` | 631 | UnwindData |  |
| 1519 | `?ValidateBuffer@CClassPart@@SA_KPEAE_K@Z` | `0x1A640` | 2,283 | UnwindData |  |
| 1524 | `?ValidateBuffer@CFastHeap@@SA_KPEAE_K@Z` | `0x1AF40` | 488 | UnwindData |  |
| 1159 | `?IsValidClassPart@CClassPart@@QEAAJXZ` | `0x1B130` | 2,183 | UnwindData |  |
| 147 | `??1CWbemClass@@UEAA@XZ` | `0x1BA40` | 177 | UnwindData |  |
| 135 | `??1CClassPart@@QEAA@XZ` | `0x1BB00` | 184 | UnwindData |  |
| 556 | `?CreateFromMemory@CWbemObject@@SAPEAV1@PEAEHHAEAVCBlobControl@@@Z` | `0x1BBF0` | 1,042 | UnwindData |  |
| 557 | `?CreateFromStream@CWbemObject@@SAPEAV1@PEAUIStream@@@Z` | `0x1C130` | 385 | UnwindData |  |
| 835 | `?GetLimitedVersion@CWbemInstance@@QEAAJPEAVCLimitationMapping@@PEAPEAV1@@Z` | `0x1C340` | 1,001 | UnwindData |  |
| 563 | `?CreateLimitedRepresentation@CDecorationPart@@QEAAPEAEPEAVCLimitationMapping@@PEAE@Z` | `0x1C730` | 156 | UnwindData |  |
| 1526 | `?ValidateBuffer@CMethodPart@@SA_KPEAE_K@Z` | `0x1C7E0` | 769 | UnwindData |  |
| 1162 | `?IsValidMethodPart@CMethodPart@@QEAAJXZ` | `0x1CAF0` | 529 | UnwindData |  |
| 1518 | `?ValidateBuffer@CClassAndMethods@@SA_KPEAE_K@Z` | `0x1CD10` | 111 | UnwindData |  |
| 1211 | `?MergeAndDecorate@CWbemClass@@UEAAJJKPEAXPEAG1PEAPEAU_IWmiObject@@@Z` | `0x1CD90` | 674 | UnwindData |  |
| 553 | `?CreateFromBlob2@CWbemInstance@@SAPEAV1@PEAVCWbemClass@@PEAEPEAG2@Z` | `0x1D040` | 1,395 | UnwindData |  |
| 552 | `?CreateFromBlob2@CWbemClass@@SAPEAV1@PEAV1@PEAEPEAG2@Z` | `0x1D5C0` | 891 | UnwindData |  |
| 1350 | `?SetData@CClassAndMethods@@QEAAXPEAEPEAVCWbemClass@@PEAV1@@Z` | `0x1D950` | 591 | UnwindData |  |
| 1529 | `?ValidateBuffer@CWbemClass@@SA_KPEAE_K@Z` | `0x1DBB0` | 130 | UnwindData |  |
| 746 | `?GetEmbedded@CEmbeddedObject@@QEAAPEAVCWbemObject@@XZ` | `0x1DC80` | 309 | UnwindData |  |
| 997 | `?GetSignature@CMethodPart@@IEAAXHHPEAPEAVCWbemObject@@@Z` | `0x1DDC0` | 63 | UnwindData |  |
| 1207 | `?Merge@CWbemClass@@QEAAPEAEPEAE0HH@Z` | `0x1DE10` | 242 | UnwindData |  |
| 1383 | `?SetFromUnicode@CCompressedString@@QEAAXHPEBG@Z` | `0x1DF10` | 99 | UnwindData |  |
| 497 | `?ComputeNecessarySpace@CCompressedString@@SAHPEBGAEAH@Z` | `0x1DF80` | 88 | UnwindData |  |
| 848 | `?GetMethod@CWbemClass@@UEAAJPEBGJPEAPEAUIWbemClassObject@@1@Z` | `0x1DFE0` | 673 | UnwindData |  |
| 847 | `?GetMethod@CMethodPart@@QEAAJPEBGJPEAPEAVCWbemObject@@1@Z` | `0x1E290` | 95 | UnwindData |  |
| 1466 | `?StoreToCVar@CEmbeddedObject@@QEAAXAEAVCVar@@@Z` | `0x1E300` | 71 | UnwindData |  |
| 454 | `?CloneAndDecorate@CWbemClass@@UEAAJJPEAG0PEAPEAUIWbemClassObject@@@Z` | `0x1E350` | 924 | UnwindData |  |
| 1221 | `?NextMethod@CWbemClass@@UEAAJJPEAPEAGPEAPEAUIWbemClassObject@@1@Z` | `0x1E700` | 926 | UnwindData |  |
| 850 | `?GetMethodAt@CMethodPart@@QEAAJHPEAPEAGPEAPEAVCWbemObject@@1@Z` | `0x1EAB0` | 529 | UnwindData |  |
| 1060 | `?HasLocalQualifiers@CBasicQualifierSet@@SAHPEAE@Z` | `0x1ECD0` | 25 | UnwindData |  |
| 505 | `?ComputeUnmergedSpace@CBasicQualifierSet@@SAKPEAE@Z` | `0x1EF90` | 92 | UnwindData |  |
| 1219 | `?Next@CWbemObject@@UEAAJJPEAPEAGPEAUtagVARIANT@@PEAJ2@Z` | `0x1F000` | 2,575 | UnwindData |  |
| 736 | `?GetDefaultValue@CClassPart@@QEAAJPEBGPEAVCVar@@@Z` | `0x1FA20` | 59 | UnwindData |  |
| 752 | `?GetFullPath@CWbemObject@@QEAAPEAGXZ` | `0x1FA70` | 683 | UnwindData |  |
| 908 | `?GetPropAddrByHandle@CWbemObject@@UEAAJJJPEAKPEAPEAX@Z` | `0x1FDA0` | 735 | UnwindData |  |
| 1023 | `?GetSystemProperty@CWbemObject@@QEAAJHPEAVCVar@@@Z` | `0x20090` | 303 | UnwindData |  |
| 656 | `?Find@CCompressedStringList@@QEAAHPEBG@Z` | `0x201D0` | 131 | UnwindData |  |
| 876 | `?GetNamespace@CWbemObject@@QEAAJPEAVCVar@@@Z` | `0x202B0` | 146 | UnwindData |  |
| 905 | `?GetPath@CWbemObject@@QEAAJPEAVCVar@@@Z` | `0x20350` | 121 | UnwindData |  |
| 950 | `?GetPropertyType@CWbemInstance@@UEAAJPEBGPEAJ1@Z` | `0x203D0` | 188 | UnwindData |  |
| 993 | `?GetServer@CWbemObject@@QEAAJPEAVCVar@@@Z` | `0x204A0` | 148 | UnwindData |  |
| 1024 | `?GetSystemPropertyByName@CWbemObject@@QEAAJPEBGPEAVCVar@@@Z` | `0x20540` | 828 | UnwindData |  |
| 738 | `?GetDerivation@CWbemObject@@QEAAJPEAVCVar@@@Z` | `0x20890` | 40 | UnwindData |  |
| 945 | `?GetPropertyType@CClassPart@@QEAAJPEBGPEAJ1@Z` | `0x208C0` | 234 | UnwindData |  |
| 948 | `?GetPropertyType@CWbemClass@@UEAAJPEBGPEAJ1@Z` | `0x209B0` | 239 | UnwindData |  |
| 1065 | `?InheritsFrom@CWbemObject@@UEAAJPEBG@Z` | `0x20AB0` | 460 | UnwindData |  |
| 713 | `?GetClassNameW@CClassPart@@QEAAPEAVCCompressedString@@XZ` | `0x20C90` | 85 | UnwindData |  |
| 946 | `?GetPropertyType@CSystemProperties@@SAJPEBGPEAJ1@Z` | `0x20D90` | 100 | UnwindData |  |
| 923 | `?GetProperty@CWbemClass@@UEAAJPEBGPEAVCVar@@@Z` | `0x20E00` | 957 | UnwindData |  |
| 661 | `?FindName@CSystemProperties@@SAHPEBG@Z` | `0x211D0` | 387 | UnwindData |  |
| 735 | `?GetDefaultValue@CClassPart@@QEAAJPEAVCPropertyInformation@@PEAVCVar@@@Z` | `0x21360` | 281 | UnwindData |  |
| 921 | `?GetPropQualifier@CWbemInstance@@UEAAJPEBG0PEAVCVar@@PEAJ2@Z` | `0x21480` | 508 | UnwindData |  |
| 1064 | `?InheritsFrom@CClassPart@@QEAAHPEBG@Z` | `0x21690` | 330 | UnwindData |  |
| 878 | `?GetNonsystemPropertyValue@CWbemInstance@@QEAAJPEBGPEAVCVar@@@Z` | `0x217E0` | 525 | UnwindData |  |
| 925 | `?GetProperty@CWbemInstance@@UEAAJPEBGPEAVCVar@@@Z` | `0x21A00` | 1,460 | UnwindData |  |
| 919 | `?GetPropQualifier@CWbemInstance@@UEAAJPEAVCPropertyInformation@@PEBGPEAVCVar@@PEAJ3@Z` | `0x21FC0` | 2,389 | UnwindData |  |
| 808 | `?GetKnownStringIndex@CKnownStringTable@@SAHPEBG@Z` | `0x22980` | 421 | UnwindData |  |
| 614 | `?EnumPrimaryQualifiers@CBasicQualifierSet@@QEAAJEEAEAVCFixedBSTRArray@@0@Z` | `0x22C00` | 1,076 | UnwindData |  |
| 737 | `?GetDerivation@CClassPart@@QEAAJPEAVCVar@@@Z` | `0x23040` | 917 | UnwindData |  |
| 501 | `?ComputeNecessarySpace@CInstancePart@@SAKPEAVCClassPart@@@Z` | `0x233E0` | 269 | UnwindData |  |
| 987 | `?GetRelPath@CWbemInstance@@UEAAPEAGH@Z` | `0x23500` | 2,030 | UnwindData |  |
| 682 | `?GetActualValue@CInstancePart@@QEAAJPEAVCPropertyInformation@@PEAVCVar@@@Z` | `0x23D00` | 277 | UnwindData |  |
| 924 | `?GetProperty@CWbemInstance@@MEAAJPEAVCPropertyInformation@@PEAVCVar@@@Z` | `0x23E20` | 590 | UnwindData |  |
| 1465 | `?StoreToCVar@CCompressedString@@QEBAHAEAVCVar@@@Z` | `0x24360` | 63 | UnwindData |  |
| 533 | `?CreateBSTRCopy@CCompressedString@@QEBAPEAGXZ` | `0x243B0` | 282 | UnwindData |  |
| 807 | `?GetKnownString@CKnownStringTable@@SAAEAVCCompressedString@@H@Z` | `0x244D0` | 162 | UnwindData |  |
| 528 | `?Create@CFixedBSTRArray@@QEAAXH@Z` | `0x24580` | 308 | UnwindData |  |
| 672 | `?Get@CQualifierSet@@UEAAJPEBGJPEAUtagVARIANT@@PEAJ@Z` | `0x24780` | 4,162 | UnwindData |  |
| 622 | `?EstimateInstanceSpace@CWbemInstance@@SAKAEAVCClassPart@@PEAVCDecorationPart@@@Z` | `0x257D0` | 227 | UnwindData |  |
| 663 | `?FindPropertyByName@CPropertyLookupTable@@QEAAPEAUCPropertyLookup@@PEAVCCompressedString@@@Z` | `0x258C0` | 571 | UnwindData |  |
| 483 | `?CompareNoCase@CCompressedString@@QEBAHAEBV1@@Z` | `0x25B10` | 325 | UnwindData |  |
| 484 | `?CompareNoCase@CCompressedString@@QEBAHPEBD@Z` | `0x25C60` | 301 | UnwindData |  |
| 485 | `?CompareNoCase@CCompressedString@@QEBAHPEBG@Z` | `0x26200` | 69 | UnwindData |  |
| 493 | `?CompareUnicodeToAsciiNoCase@CCompressedString@@KAHPEBGPEBDH@Z` | `0x263A0` | 308 | UnwindData |  |
| 1077 | `?InsertProperty@CPropertyLookupTable@@QEAAJAEBUCPropertyLookup@@AEAH@Z` | `0x264E0` | 879 | UnwindData |  |
| 828 | `?GetLength@CType@@SAKK@Z` | `0x26860` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1433 | `?SetQualifierValue@CQualifierSet@@QEAAJPEBGEPEAVCTypedValue@@HH@Z` | `0x268A0` | 5,645 | UnwindData |  |
| 956 | `?GetQualifier@CQualifierSet@@QEAAJPEBGPEAVCVar@@PEAJ2@Z` | `0x27EC0` | 265 | UnwindData |  |
| 985 | `?GetRegularQualifierLocally@CBasicQualifierSet@@SAPEAUCQualifier@@PEAEPEAVCFastHeap@@PEBG@Z` | `0x27FD0` | 766 | UnwindData |  |
| 970 | `?GetQualifierLocally@CBasicQualifierSet@@SAPEAUCQualifier@@PEAEPEAVCFastHeap@@PEBGAEAH@Z` | `0x282E0` | 1,248 | UnwindData |  |
| 962 | `?GetQualifier@CWbemInstance@@UEAAJPEBGPEAVCVar@@PEAJ2@Z` | `0x287D0` | 311 | UnwindData |  |
| 967 | `?GetQualifierLocally@CBasicQualifierSet@@QEAAPEAUCQualifier@@PEBGAEAH@Z` | `0x28910` | 1,253 | UnwindData |  |
| 958 | `?GetQualifier@CQualifierSet@@QEAAPEAUCQualifier@@PEBGAEAH@Z` | `0x28E00` | 2,193 | UnwindData |  |
| 984 | `?GetRegularQualifierLocally@CBasicQualifierSet@@QEAAPEAUCQualifier@@PEBG@Z` | `0x296A0` | 766 | UnwindData |  |
| 662 | `?FindProperty@CPropertyLookupTable@@QEAAPEAUCPropertyLookup@@PEBG@Z` | `0x299B0` | 785 | UnwindData |  |
| 666 | `?FindPropertyInfo@CClassPart@@QEAAPEAVCPropertyInformation@@PEBG@Z` | `0x29CD0` | 850 | UnwindData |  |
| 1424 | `?SetPropValue@CWbemInstance@@UEAAJPEBGPEAVCVar@@J@Z` | `0x2A0B0` | 2,338 | UnwindData |  |
| 1333 | `?SetActualValue@CInstancePart@@QEAAJPEAVCPropertyInformation@@PEAVCVar@@@Z` | `0x2A9E0` | 1,671 | UnwindData |  |
| 600 | `?DoesCIMTYPEMatchVARTYPE@CType@@SAHJG@Z` | `0x2C760` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1048 | `?GetVARTYPE@CType@@SAGK@Z` | `0x2C920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `?LoadFromCVarVector@CUntypedArray@@SAJPEAVCPtrSource@@AEAVCVarVector@@KPEAVCFastHeap@@AEAKH@Z` | `0x2CA50` | 842 | UnwindData |  |
| 1224 | `?Put@CQualifierSet@@UEAAJPEBGPEAUtagVARIANT@@J@Z` | `0x2CE50` | 1,549 | UnwindData |  |
| 1169 | `?IsValidQualifierType@CBasicQualifierSet@@SAHG@Z` | `0x2D470` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `?GetNames@CQualifierSet@@UEAAJJPEAPEAUtagSAFEARRAY@@@Z` | `0x2D4B0` | 980 | UnwindData |  |
| 615 | `?EnumQualifiers@CQualifierSet@@QEAAJEEAEAVCFixedBSTRArray@@@Z` | `0x2D890` | 1,150 | UnwindData |  |
| 670 | `?Free@CFixedBSTRArray@@QEAAXXZ` | `0x2DD60` | 35 | UnwindData |  |
| 1471 | `?ThreeWayMergeOrdered@CFixedBSTRArray@@QEAAXAEAV1@00@Z` | `0x2DDF0` | 834 | UnwindData |  |
| 1332 | `?SelfRebase@CQualifierSet@@QEAAHXZ` | `0x2E140` | 52 | UnwindData |  |
| 606 | `?EndEnumeration@CQualifierSet@@UEAAJXZ` | `0x2E1C0` | 98 | UnwindData |  |
| 439 | `?CheckCVarVector@CUntypedArray@@SAHAEAVCVarVector@@K@Z` | `0x2E230` | 373 | UnwindData |  |
| 1141 | `?IsPointerType@CType@@SAHK@Z` | `0x2E3B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1218 | `?Next@CQualifierSet@@UEAAJJPEAPEAGPEAUtagVARIANT@@PEAJ@Z` | `0x2E3E0` | 738 | UnwindData |  |
| 534 | `?CreateCVarVector@CUntypedArray@@QEAAPEAVCVarVector@@VCType@@PEAVCFastHeap@@@Z` | `0x2E710` | 852 | UnwindData |  |
| 1418 | `?SetPropQualifier@CClassPart@@QEAAJPEBG0JPEAVCVar@@@Z` | `0x2EA70` | 501 | UnwindData |  |
| 940 | `?GetPropertyQualifierSet@CWbemClass@@UEAAJPEBGPEAPEAUIWbemQualifierSet@@@Z` | `0x2EC70` | 816 | UnwindData |  |
| 1071 | `?InitPropertyQualifierSet@CClassPart@@QEAAJPEBGPEAVCClassPropertyQualifierSet@@@Z` | `0x2EFB0` | 220 | UnwindData |  |
| 136 | `??1CClassQualifierSet@@UEAA@XZ` | `0x2F130` | 189 | UnwindData |  |
| 140 | `??1CInstanceQualifierSet@@UEAA@XZ` | `0x2F130` | 189 | UnwindData |  |
| 1225 | `?Put@CWbemClass@@UEAAJPEBGJPEAUtagVARIANT@@J@Z` | `0x2F520` | 1,769 | UnwindData |  |
| 1146 | `?IsReservedWord@CReservedWordTable@@SAHPEBG@Z` | `0x2FC10` | 313 | UnwindData |  |
| 1423 | `?SetPropValue@CWbemClass@@UEAAJPEBGPEAVCVar@@J@Z` | `0x2FD50` | 354 | UnwindData |  |
| 570 | `?CreateNoCaseStringHeapPtr@CFastHeap@@QEAAHPEBGAEFAK@Z` | `0x30000` | 87 | UnwindData |  |
| 610 | `?EnsureProperty@CClassPart@@QEAAJPEBGGJH@Z` | `0x30060` | 1,172 | UnwindData |  |
| 1078 | `?InsertProperty@CPropertyLookupTable@@QEAAJPEBGKAEAH@Z` | `0x30500` | 1,275 | UnwindData |  |
| 653 | `?ExtendTo@CDataTable@@QEAAHGK@Z` | `0x30A10` | 194 | UnwindData |  |
| 386 | `?AllocateString@CFastHeap@@QEAAHPEBGAEFAK@Z` | `0x30AE0` | 90 | UnwindData |  |
| 1379 | `?SetDefaultValue@CClassPart@@QEAAJPEBGPEAVCVar@@@Z` | `0x30D40` | 59 | UnwindData |  |
| 1022 | `?GetSyntax@CType@@SAPEAGK@Z` | `0x30D90` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1378 | `?SetDefaultValue@CClassPart@@IEAAJPEAVCPropertyInformation@@PEAVCVar@@@Z` | `0x30EC0` | 655 | UnwindData |  |
| 409 | `?CanBeKey@CType@@SAHK@Z` | `0x31380` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `?CanContainKeyedProps@CClassPart@@QEAAHXZ` | `0x313B0` | 64 | UnwindData |  |
| 1121 | `?IsKeyed@CClassPart@@QEAAHXZ` | `0x31400` | 236 | UnwindData |  |
| 437 | `?CheckBoolQualifier@CClassPart@@QEAAHPEBG@Z` | `0x31500` | 59 | UnwindData |  |
| 1340 | `?SetClassName@CClassPart@@QEAAJPEAVCVar@@@Z` | `0x31550` | 715 | UnwindData |  |
| 1017 | `?GetSuperclassName@CClassPart@@QEAAJPEAVCVar@@@Z` | `0x31830` | 202 | UnwindData |  |
| 1190 | `?MapLimitation@CWbemClass@@QEAAHJPEAVCWStringArray@@PEAVCLimitationMapping@@@Z` | `0x31900` | 112 | UnwindData |  |
| 1188 | `?MapLimitation@CDecorationPart@@SAHPEAVCWStringArray@@PEAVCLimitationMapping@@@Z` | `0x31980` | 161 | UnwindData |  |
| 1341 | `?SetClassObject@CLimitationMapping@@QEAAXPEAVCWbemClass@@@Z` | `0x31A30` | 81 | UnwindData |  |
| 1187 | `?MapLimitation@CClassPart@@QEAAHJPEAVCWStringArray@@PEAVCLimitationMapping@@@Z` | `0x31A90` | 216 | UnwindData |  |
| 428 | `?CanContainSingleton@CClassPart@@UEAAJXZ` | `0x31B70` | 76 | UnwindData |  |
| 591 | `?DeleteProperty@CPropertyLookupTable@@QEAAXPEAUCPropertyLookup@@H@Z` | `0x31BD0` | 442 | UnwindData |  |
| 1113 | `?IsIllegalDerivedClass@CSystemProperties@@SAHPEBG@Z` | `0x31D90` | 97 | UnwindData |  |
| 655 | `?Filter@CFixedBSTRArray@@QEAAXPEBGH@Z` | `0x31E00` | 193 | UnwindData |  |
| 723 | `?GetClassSubset@CWbemClass@@UEAAJKPEAPEBGPEAPEAU_IWmiObject@@@Z` | `0x31ED0` | 646 | UnwindData |  |
| 834 | `?GetLimitedVersion@CWbemClass@@QEAAJPEAVCLimitationMapping@@PEAPEAV1@@Z` | `0x32160` | 888 | UnwindData |  |
| 51 | `??0CLimitationMapping@@QEAA@XZ` | `0x324E0` | 65 | UnwindData |  |
| 1367 | `?SetData@CWbemInstance@@UEAAXPEAEH@Z` | `0x32530` | 34 | UnwindData |  |
| 613 | `?EnsureReal@CQualifierSetList@@QEAAHXZ` | `0x32BE0` | 108 | UnwindData |  |
| 649 | `?ExtendQualifierSetSpace@CInstancePQSContainer@@UEAAHPEAVCBasicQualifierSet@@K@Z` | `0x32C60` | 125 | UnwindData |  |
| 652 | `?ExtendQualifierSetSpace@CQualifierSetList@@QEAAHPEAVCBasicQualifierSet@@K@Z` | `0x32CF0` | 155 | UnwindData |  |
| 898 | `?GetObjectText@CWbemClass@@UEAAJJPEAPEAG@Z` | `0x32DA0` | 1,815 | UnwindData |  |
| 366 | `?AddPropertyText@CWbemClass@@QEAAJAEAVWString@@PEAUCPropertyLookup@@PEAVCPropertyInformation@@J@Z` | `0x334C0` | 1,389 | UnwindData |  |
| 899 | `?GetObjectText@CWbemInstance@@UEAAJJPEAPEAG@Z` | `0x33A40` | 2,292 | UnwindData |  |
| 507 | `?ConvertToClass@CWbemInstance@@QEAAJPEAVCWbemClass@@PEAPEAV1@@Z` | `0x34370` | 488 | UnwindData |  |
| 506 | `?ConvertToClass@CInstancePart@@QEAAPEAEAEAVCClassPart@@KPEAE@Z` | `0x34560` | 243 | UnwindData |  |
| 1554 | `?WriteSmallerVersion@CDataTable@@QEAAPEAEHKPEAE@Z` | `0x34660` | 139 | UnwindData |  |
| 1555 | `?WriteSmallerVersion@CQualifierSetList@@QEAAPEAEHPEAE@Z` | `0x34720` | 94 | UnwindData |  |
| 974 | `?GetQualifierSetData@CQualifierSetList@@SAPEAEPEAEH@Z` | `0x34790` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1049 | `?GetValueText@CWbemObject@@SAPEAGJAEAVCVar@@K@Z` | `0x34800` | 1,105 | UnwindData |  |
| 1026 | `?GetText@CBasicQualifierSet@@SAJPEAEPEAVCFastHeap@@JAEAVWString@@@Z` | `0x34C60` | 1,481 | UnwindData |  |
| 712 | `?GetClassNameW@CClassPart@@QEAAJPEAVCVar@@@Z` | `0x35280` | 255 | UnwindData |  |
| 576 | `?CreateWStringCopy@CCompressedString@@QEBAXAEAVWString@@@Z` | `0x35390` | 81 | UnwindData |  |
| 367 | `?AddPropertyType@CType@@SAXAEAVWString@@PEBG@Z` | `0x35530` | 330 | UnwindData |  |
| 1504 | `?Update@CClassAndMethods@@SAJAEAV1@0J@Z` | `0x35680` | 184 | UnwindData |  |
| 1505 | `?Update@CClassPart@@SAJAEAV1@0J@Z` | `0x35740` | 289 | UnwindData |  |
| 382 | `?AddText@CMethodDescription@@SAJPEFAU1@AEAVWString@@PEAVCFastHeap@@J@Z` | `0x35870` | 1,388 | UnwindData |  |
| 76 | `??0CWbemClassCache@@QEAA@K@Z` | `0x36E40` | 87 | UnwindData |  |
| 153 | `??1CWbemInstance@@UEAA@XZ` | `0x37420` | 1,127 | UnwindData |  |
| 238 | `??4CSharedLock@@QEAAAEAV0@$$QEAV0@@Z` | `0x3C000` | 7,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `??4CSharedLock@@QEAAAEAV0@AEBV0@@Z` | `0x3C000` | 7,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `??4SHMEM_HANDLE@@QEAAAEAU0@AEBU0@@Z` | `0x3C000` | 7,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `?SetArrayPropRangeByHandle@CWbemObject@@UEAAJJJKKKPEAX@Z` | `0x3DD40` | 753 | UnwindData |  |
| 1086 | `?IsArrayPropertyHandle@CWbemObject@@QEAAJJPEAJPEAK@Z` | `0x3E040` | 164 | UnwindData |  |
| 1434 | `?SetRange@CUntypedArray@@SAJPEAVCPtrSource@@JKKPEAVCFastHeap@@KKKPEAX@Z` | `0x3E0F0` | 997 | UnwindData |  |
| 444 | `?CheckRangeSize@CUntypedArray@@SAJKKKKPEAX@Z` | `0x3E4E0` | 269 | UnwindData |  |
| 911 | `?GetPropQual@CWbemObject@@UEAAJPEBG0JKPEAJPEAK2PEAX@Z` | `0x3E600` | 700 | UnwindData |  |
| 1132 | `?IsNonArrayPointerType@CType@@SAHK@Z` | `0x3EB10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `?IsStringType@CType@@SAHK@Z` | `0x3EB40` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `?RemoveRange@CUntypedArray@@SAJPEAVCPtrSource@@KKPEAVCFastHeap@@KK@Z` | `0x3EE40` | 567 | UnwindData |  |
| 1251 | `?ReallocArray@CUntypedArray@@KAJPEAVCPtrSource@@KPEAVCFastHeap@@KPEAK22@Z` | `0x3F080` | 295 | UnwindData |  |
| 651 | `?ExtendQualifierSetSpace@CMethodQualifierSetContainer@@UEAAHPEAVCBasicQualifierSet@@K@Z` | `0x3F1B0` | 178 | UnwindData |  |
| 1252 | `?Reallocate@CFastHeap@@QEAAHKKKAEFAK@Z` | `0x3F270` | 546 | UnwindData |  |
| 1440 | `?SetSignature@CMethodPart@@IEAAJHW4METHOD_SIGNATURE_TYPE@@PEAVCWbemObject@@@Z` | `0x3F8A0` | 348 | UnwindData |  |
| 390 | `?AreEqual@CWbemObject@@SAHPEAV1@0J@Z` | `0x3FA10` | 76 | UnwindData |  |
| 1463 | `?StoreEmbedded@CEmbeddedObject@@QEAAXKPEAVCWbemObject@@@Z` | `0x3FA70` | 323 | UnwindData |  |
| 629 | `?EstimateNecessarySpace@CEmbeddedObject@@SAKPEAVCWbemObject@@@Z` | `0x3FBC0` | 174 | UnwindData |  |
| 480 | `?CompareExactMatch@CMethodPart@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x3FC80` | 461 | UnwindData |  |
| 1228 | `?PutMethod@CWbemClass@@UEAAJPEBGJPEAUIWbemClassObject@@1@Z` | `0x3FE60` | 563 | UnwindData |  |
| 490 | `?CompareTo@CWbemClass@@UEAAJJPEAUIWbemClassObject@@@Z` | `0x400A0` | 731 | UnwindData |  |
| 1541 | `?WbemObjectFromCOMPtr@CWbemObject@@SAJPEAUIUnknown@@PEAPEAV1@@Z` | `0x40390` | 245 | UnwindData |  |
| 491 | `?CompareTo@CWbemObject@@UEAAJJPEAUIWbemClassObject@@@Z` | `0x40490` | 4,080 | UnwindData |  |
| 1227 | `?PutMethod@CMethodPart@@QEAAJPEBGJPEAVCWbemObject@@1@Z` | `0x41490` | 1,264 | UnwindData |  |
| 611 | `?EnsureQualifier@CMethodPart@@QEAAJPEAVCWbemObject@@PEBGPEAPEAV2@@Z` | `0x41990` | 228 | UnwindData |  |
| 1535 | `?ValidateOutParams@CMethodPart@@IEAAJPEAVCWbemObject@@@Z` | `0x41A80` | 180 | UnwindData |  |
| 612 | `?EnsureQualifier@CWbemClass@@QEAAJPEBG@Z` | `0x41B40` | 372 | UnwindData |  |
| 776 | `?GetIds@CWbemClass@@QEAAJAEAVCFlexArray@@PEAV1@@Z` | `0x41CC0` | 1,646 | UnwindData |  |
| 575 | `?CreateWStringCopy@CCompressedString@@QEBAXAEAVWString2@@@Z` | `0x42340` | 102 | UnwindData |  |
| 440 | `?CheckDuplicateParameters@CMethodPart@@IEAAJPEAVCWbemObject@@0@Z` | `0x423B0` | 833 | UnwindData |  |
| 441 | `?CheckIds@CMethodPart@@IEAAJPEAVCWbemClass@@0@Z` | `0x42700` | 490 | UnwindData |  |
| 476 | `?CompareDefs@CClassPart@@QEAAHAEAV1@@Z` | `0x428F0` | 190 | UnwindData |  |
| 487 | `?CompareTo@CDecorationPart@@QEAAHAEAV1@@Z` | `0x429C0` | 146 | UnwindData |  |
| 650 | `?ExtendQualifierSetSpace@CInstancePart@@UEAAHPEAVCBasicQualifierSet@@K@Z` | `0x42A60` | 278 | UnwindData |  |
| 569 | `?CreateMethod@CMethodPart@@IEAAJPEBGPEAVCWbemObject@@1@Z` | `0x42B80` | 1,067 | UnwindData |  |
| 1483 | `?Undecorate@CWbemInstance@@UEAAXXZ` | `0x42FC0` | 125 | UnwindData |  |
| 1482 | `?Undecorate@CWbemClass@@UEAAXXZ` | `0x43050` | 148 | UnwindData |  |
| 578 | `?Decorate@CWbemClass@@UEAAJPEBG0@Z` | `0x430F0` | 488 | UnwindData |  |
| 500 | `?ComputeNecessarySpace@CDecorationPart@@SAKPEBG0@Z` | `0x432E0` | 44 | UnwindData |  |
| 48 | `??0CInternalString@@QEAA@PEBG@Z` | `0x43320` | 182 | UnwindData |  |
| 579 | `?Decorate@CWbemInstance@@UEAAJPEBG0@Z` | `0x43420` | 465 | UnwindData |  |
| 496 | `?ComputeNecessarySpace@CCompressedString@@SAHPEBG@Z` | `0x43600` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `?Create@CDecorationPart@@QEAAXEPEBG0PEAE@Z` | `0x43670` | 92 | UnwindData |  |
| 1256 | `?Rebase@CClassPart@@QEAAXPEAE@Z` | `0x436E0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `?SetFromUnicode@CCompressedString@@QEAAXPEBG@Z` | `0x43780` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `?Reallocate@CWbemObject@@IEAAPEAEK@Z` | `0x43800` | 96 | UnwindData |  |
| 463 | `?Compact@CInstancePart@@QEAAX_N@Z` | `0x43870` | 721 | UnwindData |  |
| 637 | `?ExtendClassPartSpace@CClassAndMethods@@UEAAHPEAVCClassPart@@K@Z` | `0x43BA0` | 199 | UnwindData |  |
| 636 | `?ExtendClassAndMethodsSpace@CWbemClass@@QEAAHK@Z` | `0x43C70` | 275 | UnwindData |  |
| 1255 | `?Rebase@CClassAndMethods@@QEAAXPEAE@Z` | `0x43D90` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1336 | `?SetAllocatedDataLength@CFastHeap@@QEAAXK@Z` | `0x43E90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1266 | `?Rebase@CWbemClass@@QEAAXPEAE@Z` | `0x43EC0` | 130 | UnwindData |  |
| 1250 | `?ReallocAndCompact@CInstancePart@@QEAAHK@Z` | `0x43F90` | 143 | UnwindData |  |
| 647 | `?ExtendQualifierSetListSpace@CInstancePart@@UEAAHPEAEKK@Z` | `0x442A0` | 246 | UnwindData |  |
| 474 | `?Compare@CQualifierSet@@QEAAHAEAV1@PEAVCFixedBSTRArray@@H@Z` | `0x443A0` | 1,310 | UnwindData |  |
| 988 | `?GetRelPath@CWbemObject@@QEAAJPEAVCVar@@@Z` | `0x45110` | 107 | UnwindData |  |
| 508 | `?ConvertToMergedInstance@CWbemInstance@@QEAAJXZ` | `0x466B0` | 425 | UnwindData |  |
| 1175 | `?Lock@CSharedLock@@QEAAHK@Z` | `0x48FB0` | 58 | UnwindData |  |
| 1487 | `?Unlock@CSharedLock@@QEAAHXZ` | `0x49100` | 4,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1445 | `?SetupDataPacketHeader@CWbemDataPacket@@IEAAJKEKK@Z` | `0x4A1A0` | 228 | UnwindData |  |
| 406 | `?CalculateLength@CWbemSmartEnumNextPacket@@QEAAJJPEAPEAUIWbemClassObject@@PEAKAEAVCWbemClassToIdMap@@PEAU_GUID@@PEAH@Z` | `0x4A290` | 186 | UnwindData |  |
| 405 | `?CalculateLength@CWbemObjectArrayPacket@@QEAAJJPEAPEAUIWbemClassObject@@PEAKAEAVCWbemClassToIdMap@@PEAU_GUID@@PEAH@Z` | `0x4AD70` | 1,758 | UnwindData |  |
| 839 | `?GetMarshalPacket@CWbemEnumMarshaling@@QEAAJAEBU_GUID@@KPEAPEAUIWbemClassObject@@PEAKPEAPEAE@Z` | `0x4B460` | 1,335 | UnwindData |  |
| 1197 | `?MarshalPacket@CWbemSmartEnumNextPacket@@QEAAJJPEAPEAUIWbemClassObject@@PEAU_GUID@@PEAH@Z` | `0x4B9A0` | 572 | UnwindData |  |
| 1195 | `?MarshalPacket@CWbemObjectArrayPacket@@QEAAJJPEAPEAUIWbemClassObject@@PEAU_GUID@@PEAH@Z` | `0x4BBF0` | 1,887 | UnwindData |  |
| 359 | `?AddMap@CWbemGuidToClassMap@@QEAAJAEAVCGUID@@PEAPEAVCWbemClassToIdMap@@@Z` | `0x4C410` | 523 | UnwindData |  |
| 1176 | `?Lock@CWbemObject@@UEAAJJ@Z` | `0x4E590` | 60 | UnwindData |  |
| 806 | `?GetKnownQualifierLocally@CBasicQualifierSet@@SAPEAUCQualifier@@PEAEH@Z` | `0x4E6B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1375 | `?SetDataWithNumProps@CClassAndMethods@@QEAAXPEAEPEAVCWbemClass@@KPEAV1@@Z` | `0x4E720` | 121 | UnwindData |  |
| 482 | `?CompareMostDerivedClass@CWbemClass@@QEAAJPEAV1@@Z` | `0x4E7A0` | 973 | UnwindData |  |
| 1357 | `?SetData@CMethodPart@@QEAAXPEAEPEAVCMethodPartContainer@@PEAV1@@Z` | `0x4EB80` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1376 | `?SetDataWithNumProps@CClassPart@@QEAAXPEAEPEAVCClassPartContainer@@KPEAV1@@Z` | `0x4EBF0` | 257 | UnwindData |  |
| 479 | `?CompareExactMatch@CClassPart@@QEAA?AW4EReconciliation@@AEAV1@H@Z` | `0x4ED00` | 1,511 | UnwindData |  |
| 1361 | `?SetData@CQualifierSet@@QEAAXPEAEPEAVCQualifierSetContainer@@PEAVCBasicQualifierSet@@@Z` | `0x4F2F0` | 114 | UnwindData |  |
| 145 | `??1CQualifierSet@@UEAA@XZ` | `0x4F370` | 189 | UnwindData |  |
| 1075 | `?InitializePropQualifierSet@CWbemInstance@@IEAAJPEBGAEAVCInstancePropertyQualifierSet@@@Z` | `0x4F440` | 226 | UnwindData |  |
| 941 | `?GetPropertyQualifierSet@CWbemInstance@@UEAAJPEBGPEAPEAUIWbemQualifierSet@@@Z` | `0x4F530` | 991 | UnwindData |  |
| 977 | `?GetQualifierSetStart@CInstancePQSContainer@@UEAAPEAEXZ` | `0x4F920` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 896 | `?GetObjectParts@CWbemInstance@@UEAAJPEAXKKPEAK@Z` | `0x4F980` | 1,094 | UnwindData |  |
| 827 | `?GetLength@CType@@QEAAKXZ` | `0x4FDD0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1240 | `?QueryInterface@CWbemObject@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x50130` | 378 | UnwindData |  |
| 1534 | `?ValidateObject@CWbemObject@@UEAAJJ@Z` | `0x50340` | 189 | UnwindData |  |
| 529 | `?Create@CInstancePQSContainer@@QEAAXPEAVCQualifierSetList@@HPEAVCClassPart@@K@Z` | `0x50490` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `?Release@CWbemObject@@UEAAKXZ` | `0x504D0` | 57 | UnwindData |  |
| 509 | `?ConvertToUnicode@CCompressedString@@QEBAHPEAGK@Z` | `0x50550` | 146 | UnwindData |  |
| 1088 | `?IsAsciiable@CCompressedString@@KAHPEBG@Z` | `0x505F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `?FindPropertyByPtr@CPropertyLookupTable@@QEAAPEAUCPropertyLookup@@K@Z` | `0x50620` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `?CompactAll@CWbemInstance@@UEAAXXZ` | `0x506A0` | 748 | UnwindData |  |
| 1161 | `?IsValidKey@CWbemInstance@@QEAAHPEBG@Z` | `0x509A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1435 | `?SetSecondarySetData@CInstancePQSContainer@@QEAAXXZ` | `0x509D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1450 | `?Skip@CBasicQualifierSet@@QEAAPEAEXZ` | `0x50A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `?IsOutOfLine@CFastHeap@@IEAAHXZ` | `0x50A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1087 | `?IsArrayValid@CUntypedArray@@QEAAJVCType@@PEAVCFastHeap@@@Z` | `0x50A40` | 382 | UnwindData |  |
| 1355 | `?SetData@CFastHeap@@QEAAHPEAEPEAVCHeapContainer@@@Z` | `0x50CF0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1501 | `?Unmerge@CWbemInstance@@UEAAJPEAEHPEAK@Z` | `0x50D40` | 615 | UnwindData |  |
| 139 | `??1CInstancePart@@QEAA@XZ` | `0x50FB0` | 179 | UnwindData |  |
| 1475 | `?TranslateToNewHeap@CInstancePart@@QEAAHAEAVCClassPart@@PEAVCFastHeap@@1@Z` | `0x51070` | 202 | UnwindData |  |
| 1474 | `?TranslateToNewHeap@CDataTable@@QEAAHPEAVCPropertyLookupTable@@HPEAVCFastHeap@@1@Z` | `0x51140` | 252 | UnwindData |  |
| 1476 | `?TranslateToNewHeap@CQualifierSetList@@QEAAHPEAVCFastHeap@@0@Z` | `0x51250` | 134 | UnwindData |  |
| 759 | `?GetHeaderLength@CFastHeap@@IEAAKXZ` | `0x512E0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `??1CFixedBSTRArray@@QEAA@XZ` | `0x51670` | 27 | UnwindData |  |
| 155 | `??1CWbemObject@@UEAA@XZ` | `0x516A0` | 112 | UnwindData |  |
| 1349 | `?SetData@CBasicQualifierSet@@QEAAXPEAEPEAVCFastHeap@@@Z` | `0x51720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `?GetQualifierSetData@CQualifierSetList@@QEAAPEAEH@Z` | `0x51740` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??0CFixedBSTRArray@@QEAA@XZ` | `0x51780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1053 | `?GetWbemObjectUnknown@CInstancePQSContainer@@UEAAPEAUIUnknown@@XZ` | `0x517A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `?GetActualType@CType@@SAKK@Z` | `0x517E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `?GetWbemObjectUnknown@CInstancePart@@UEAAPEAUIUnknown@@XZ` | `0x51810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | `?GetHeap@CInstancePQSContainer@@UEAAPEAVCFastHeap@@XZ` | `0x51830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `?GetBasic@CType@@SAKK@Z` | `0x51850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `?GetLength@CCompressedStringList@@QEAAKXZ` | `0x51860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | `?GetNumProperties@CPropertyLookupTable@@QEAAHXZ` | `0x51860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 951 | `?GetPropertyValue@CWbemObject@@UEAAJPEAU_tag_WbemPropertyName@@JPEAPEAGPEAUtagVARIANT@@@Z` | `0x51870` | 2,211 | UnwindData |  |
| 781 | `?GetIndexFromFake@CFastHeap@@SAHK@Z` | `0x52120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `?Get@CWbemObject@@UEAAJPEBGJPEAUtagVARIANT@@PEAJ2@Z` | `0x52130` | 934 | UnwindData |  |
| 1156 | `?IsUnicode@CCompressedString@@QEBAHXZ` | `0x524E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `?GetWbemObjectUnknown@CQualifierSetList@@QEAAPEAUIUnknown@@XZ` | `0x524F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1362 | `?SetData@CQualifierSetList@@QEAAXPEAEHPEAVCQualifierSetListContainer@@@Z` | `0x52530` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `?GetHeap@CQualifierSetList@@QEAAPEAVCFastHeap@@XZ` | `0x52580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1354 | `?SetData@CDecorationPart@@QEAAXPEAE@Z` | `0x525A0` | 34 | UnwindData |  |
| 695 | `?GetAt@CPropertyLookupTable@@QEAAPEAUCPropertyLookup@@H@Z` | `0x52630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 901 | `?GetOffset@CDataTable@@QEAAPEAVCUntypedValue@@K@Z` | `0x52650` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `?GetObjectMemory@CWbemObject@@UEAAJPEAXKPEAK@Z` | `0x526B0` | 316 | UnwindData |  |
| 1453 | `?SortInPlace@CFixedBSTRArray@@QEAAXXZ` | `0x52800` | 31 | UnwindData |  |
| 780 | `?GetInLineLength@CFastHeap@@IEAAPEFAKXZ` | `0x52A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `?AddRef@CWbemObject@@UEAAKXZ` | `0x52A20` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1042 | `?GetUsedLength@CFastHeap@@QEAAKXZ` | `0x52AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `?GetLength@CFastHeap@@QEAAKXZ` | `0x52AD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `?InitializePropQualifierSet@CWbemInstance@@IEAAJPEAVCPropertyInformation@@AEAVCInstancePropertyQualifierSet@@@Z` | `0x52B00` | 269 | UnwindData |  |
| 89 | `??0CWbemObject@@IEAA@AEAVCDataTable@@AEAVCFastHeap@@AEAVCDerivationList@@@Z` | `0x52C30` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1100 | `?IsDecorated@CDecorationPart@@QEAAHXZ` | `0x52CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `?GetStart@CBasicQualifierSet@@QEAAPEAEXZ` | `0x52CF0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `?GetHeap@CClassPart@@UEAAPEAVCFastHeap@@XZ` | `0x52D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `?GetHeap@CInstancePart@@UEAAPEAVCFastHeap@@XZ` | `0x52D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `?CloneRpcContext@CWbemThreadSecurityHandle@@QEAAJPEAUIServerSecurity@@@Z` | `0x52DA0` | 561 | UnwindData |  |
| 1029 | `?GetThreadSecurity@CWbemCallSecurity@@UEAAJW4tag_WMI_THREAD_SECURITY_ORIGIN@@PEAPEAU_IWmiThreadSecHandle@@@Z` | `0x53190` | 1,025 | UnwindData |  |
| 460 | `?CloneThreadContext@CWbemThreadSecurityHandle@@QEAAJK@Z` | `0x535A0` | 329 | UnwindData |  |
| 1306 | `?Release@CWbemCallSecurity@@UEAAKXZ` | `0x536F0` | 67 | UnwindData |  |
| 1239 | `?QueryInterface@CWbemCallSecurity@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x53740` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `??1CWbemCallSecurity@@QEAA@XZ` | `0x537F0` | 99 | UnwindData |  |
| 1308 | `?Release@CWbemThreadSecurityHandle@@UEAAKXZ` | `0x53860` | 65 | UnwindData |  |
| 159 | `??1CWbemThreadSecurityHandle@@QEAA@XZ` | `0x538B0` | 116 | UnwindData |  |
| 96 | `??0CWbemThreadSecurityHandle@@QEAA@AEBV0@@Z` | `0x53930` | 66 | UnwindData |  |
| 256 | `??4CWbemThreadSecurityHandle@@QEAAAEAV0@AEBV0@@Z` | `0x53980` | 453 | UnwindData |  |
| 458 | `?CloneProcessContext@CWbemThreadSecurityHandle@@QEAAJXZ` | `0x53B50` | 269 | UnwindData |  |
| 97 | `??0CWbemThreadSecurityHandle@@QEAA@PEAVCLifeControl@@@Z` | `0x53E40` | 86 | UnwindData |  |
| 1134 | `?IsObjectInstance@CWbemObject@@UEAAJXZ` | `0x53EA0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1068 | `?InitEmpty@CWbemClass@@QEAAJHH@Z` | `0x54020` | 285 | UnwindData |  |
| 551 | `?CreateEmpty@CWbemClass@@SAPEAEPEAE@Z` | `0x54190` | 135 | UnwindData |  |
| 1117 | `?IsInstance@CWbemObject@@QEAAHXZ` | `0x54220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1559 | `?_GetCoreInfo@CWbemObject@@UEAAJJPEAPEAX@Z` | `0x54240` | 45 | UnwindData |  |
| 1514 | `?UpperByte@CCompressedString@@KADG@Z` | `0x54280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1488 | `?Unlock@CWbemObject@@UEAAJJ@Z` | `0x54290` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1385 | `?SetInLineLength@CFastHeap@@IEAAXK@Z` | `0x542C0` | 6,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1542 | `WbemStringCopy` | `0x55AA0` | 167 | UnwindData |  |
| 1116 | `?IsInstance@CDecorationPart@@QEAAHXZ` | `0x56050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1260 | `?Rebase@CFastHeap@@QEAAXPEAE@Z` | `0x56070` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `?IsArray@CType@@SAHK@Z` | `0x560A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1528 | `?ValidateBuffer@CQualifierSetList@@SA_KPEAE_KH@Z` | `0x560B0` | 241 | UnwindData |  |
| 1517 | `?ValidateBuffer@CBasicQualifierSet@@SA_KPEAE_K@Z` | `0x561B0` | 257 | UnwindData |  |
| 419 | `?CanContainDynamic@CClassPart@@UEAAJXZ` | `0x562C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `?CanContainDynamic@CInstancePQSContainer@@UEAAJXZ` | `0x562C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `?CanHaveCimtype@CClassPart@@UEAAHPEBG@Z` | `0x562C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `?CanHaveCimtype@CInstancePQSContainer@@UEAAHPEBG@Z` | `0x562C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `?CanHaveCimtype@CInstancePart@@UEAAHPEBG@Z` | `0x562C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `?CanHaveCimtype@CMethodQualifierSetContainer@@UEAAHPEBG@Z` | `0x562C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `?ClearWriteOnlyProperties@CWbemInstance@@UEAAJXZ` | `0x562C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 596 | `?DisabledValidateObject@CWbemObject@@KAJPEAV1@@Z` | `0x562C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `?DisconnectObject@CWbemObject@@UEAAJK@Z` | `0x562C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `?GetMinLength@CDataTable@@SAKXZ` | `0x562C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1473 | `?TranslateToNewHeap@CCompressedString@@QEAAHPEAVCFastHeap@@0@Z` | `0x562C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 932 | `?GetPropertyHandleEx@CWbemObject@@UEAAJPEBGJPEAJ1@Z` | `0x56310` | 171 | UnwindData |  |
| 931 | `?GetPropertyHandleEx@CClassPart@@QEAAJPEBGPEAJ1@Z` | `0x563D0` | 166 | UnwindData |  |
| 930 | `?GetPropertyHandle@CWbemObject@@UEAAJPEBGPEAJ1@Z` | `0x56480` | 348 | UnwindData |  |
| 929 | `?GetPropertyHandle@CClassPart@@QEAAJPEBGPEAJ1@Z` | `0x565F0` | 298 | UnwindData |  |
| 1309 | `?ReleaseElement@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@IEAAXPEAVCWmiTextSource@@@Z` | `0x567D0` | 23 | UnwindData |  |
| 131 | `??1?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAA@XZ` | `0x56840` | 39 | UnwindData |  |
| 1312 | `?RemoveAll@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXXZ` | `0x56870` | 142 | UnwindData |  |
| 355 | `?Add@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAHPEAVCWmiTextSource@@@Z` | `0x57290` | 74 | UnwindData |  |
| 826 | `?GetLength@CQualifierSetList@@SAHPEAEH@Z` | `0x573B0` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1568 | `DllCanUnloadNow` | `0x57840` | 205 | UnwindData |  |
| 1569 | `DllGetClassObject` | `0x57920` | 310 | UnwindData |  |
| 820 | `?GetLength@CInstancePart@@QEAAHXZ` | `0x57D70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `?GetQualifierSet@CWbemInstance@@UEAAJPEAPEAUIWbemQualifierSet@@@Z` | `0x57DC0` | 225 | UnwindData |  |
| 890 | `?GetNumStrings@CCompressedStringList@@QEAAHXZ` | `0x57F00` | 84 | UnwindData |  |
| 877 | `?GetNext@CCompressedStringList@@QEAAPEAVCCompressedString@@PEAV2@@Z` | `0x57F60` | 125 | UnwindData |  |
| 1521 | `?ValidateBuffer@CDataTable@@SA_KPEAE_KH@Z` | `0x57FF0` | 243 | UnwindData |  |
| 824 | `?GetLength@CPropertyLookupTable@@QEAAHXZ` | `0x580F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `?IsClassPartInternal@CWbemInstance@@IEAAHXZ` | `0x58110` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `?Rebase@CBasicQualifierSet@@QEAAXPEAE@Z` | `0x581F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `?Rebase@CDataTable@@QEAAXPEAE@Z` | `0x58200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `?GetTotalRealLength@CInstancePart@@QEAAKXZ` | `0x58220` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `?GetMemoryLimit@CInstancePart@@UEAAPEAEXZ` | `0x58260` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 860 | `?GetMethodQualifierSet@CWbemClass@@UEAAJPEBGPEAPEAUIWbemQualifierSet@@@Z` | `0x582B0` | 229 | UnwindData |  |
| 856 | `?GetMethodQualifier@CWbemClass@@UEAAJPEBG0PEAVCVar@@PEAJ2@Z` | `0x583A0` | 419 | UnwindData |  |
| 859 | `?GetMethodQualifierSet@CMethodPart@@QEAAJPEBGPEAPEAUIWbemQualifierSet@@@Z` | `0x58550` | 273 | UnwindData |  |
| 1238 | `?QueryInterface@CQualifierSet@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x58670` | 112 | UnwindData |  |
| 1358 | `?SetData@CMethodQualifierSet@@QEAAXPEAVCMethodPart@@0PEBG@Z` | `0x586F0` | 83 | UnwindData |  |
| 60 | `??0CMethodQualifierSet@@QEAA@XZ` | `0x58750` | 51 | UnwindData |  |
| 63 | `??0CMethodQualifierSetContainer@@QEAA@XZ` | `0x58790` | 50 | UnwindData |  |
| 1359 | `?SetData@CMethodQualifierSetContainer@@QEAAXPEAVCMethodPart@@0PEBG@Z` | `0x587D0` | 156 | UnwindData |  |
| 906 | `?GetPointer@CUntypedArray@@SAPEAV1@PEAVCPtrSource@@@Z` | `0x58880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `?GetMapped@CLimitationMapping@@QEAAPEAVCPropertyInformation@@PEAV2@@Z` | `0x588A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1545 | `?WriteDWORD@CWbemObject@@UEAAJJK@Z` | `0x588D0` | 455 | UnwindData |  |
| 1553 | `?WriteQWORD@CWbemObject@@UEAAJJ_K@Z` | `0x58AA0` | 455 | UnwindData |  |
| 448 | `?ClearCachedKey@CWbemInstance@@QEAAXXZ` | `0x58DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `?ClearCachedKeyValue@CWbemInstance@@UEAAXXZ` | `0x58DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | `?EstimateUnmergeSpace@CClassPart@@QEAAKXZ` | `0x58DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 812 | `?GetLength@CClassPart@@QEAAKXZ` | `0x58DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `??0SHARED_LOCK_DATA@@QEAA@XZ` | `0x58DF0` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `?GetBlockLength@CWbemInstance@@MEAAKXZ` | `0x59090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `?GetLength@CWbemInstance@@QEAAKXZ` | `0x59090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??0CInstancePQSContainer@@QEAA@XZ` | `0x590A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `?GetWbemObjectUnknown@CClassPart@@UEAAPEAUIUnknown@@XZ` | `0x590C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `?CreateOutOfLine@CFastHeap@@QEAAPEAEPEAEK@Z` | `0x590E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `?GetNullnessLength@CDataTable@@QEAAKXZ` | `0x59120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `?GetClassNameW@CWbemClass@@UEAAJPEAVCVar@@@Z` | `0x59130` | 267 | UnwindData |  |
| 739 | `?GetDerivation@CWbemObject@@UEAAJJKPEAK0PEAG@Z` | `0x59250` | 806 | UnwindData |  |
| 148 | `??1CWbemClassCache@@QEAA@XZ` | `0x59640` | 54 | UnwindData |  |
| 446 | `?Clear@CWbemClassCache@@AEAAXXZ` | `0x59680` | 176 | UnwindData |  |
| 954 | `?GetQualifier@CInstancePart@@QEAAJPEBGPEAVCVar@@PEAJ2@Z` | `0x59910` | 308 | UnwindData |  |
| 1360 | `?SetData@CPropertyLookupTable@@QEAAXPEAEPEAVCPropertyTableContainer@@@Z` | `0x59A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `?IsComplete@CQualifierSet@@QEAAHXZ` | `0x59A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `?GetElement@CUntypedArray@@QEAAPEAEHH@Z` | `0x59AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 982 | `?GetRealLength@CFastHeap@@QEAAKXZ` | `0x59AD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1352 | `?SetData@CCompressedStringList@@QEAAXPEAE@Z` | `0x59B00` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `??1CWbemEnumMarshaling@@UEAA@XZ` | `0x59C10` | 92 | UnwindData |  |
| 152 | `??1CWbemGuidToClassMap@@QEAA@XZ` | `0x59C80` | 54 | UnwindData |  |
| 447 | `?Clear@CWbemGuidToClassMap@@AEAAXXZ` | `0x59CE0` | 169 | UnwindData |  |
| 788 | `?GetInstanceObjectUnknown@CWbemInstance@@UEAAPEAUIUnknown@@XZ` | `0x5A0E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `?GetKnownQualifierLocally@CBasicQualifierSet@@QEAAPEAUCQualifier@@H@Z` | `0x5A130` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `?EstimateDerivedPartSpace@CMethodPart@@QEAAKXZ` | `0x5A1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 632 | `?EstimateUnmergeSpace@CMethodPart@@QEAAKXZ` | `0x5A1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `?GetAllocatedDataLength@CFastHeap@@QEAAKXZ` | `0x5A1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 823 | `?GetLength@CMethodPart@@QEAAKXZ` | `0x5A1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `?GetPropertyLookup@CClassPart@@QEAAPEAUCPropertyLookup@@H@Z` | `0x5A1B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `?IsClassPartAvailable@CWbemInstance@@IEAAHXZ` | `0x5A220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 949 | `?GetPropertyType@CWbemInstance@@UEAAJPEAVCPropertyInformation@@PEAJ1@Z` | `0x5A230` | 220 | UnwindData |  |
| 1110 | `?IsFakeAddress@CFastHeap@@SAHK@Z` | `0x5A320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `?AugmentRequest@CFastHeap@@IEAAKKK@Z` | `0x5A330` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `?NextMapping@CLimitationMapping@@QEAAHPEAVCPropertyInformation@@0@Z` | `0x5A390` | 151 | UnwindData |  |
| 846 | `?GetMemoryLimit@CMethodPart@@UEAAPEAEXZ` | `0x5A430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `?BeginEnumeration@CWbemObject@@UEAAJJ@Z` | `0x5A450` | 465 | UnwindData |  |
| 1556 | `?WriteToStream@CWbemInstance@@UEAAJPEAUIStream@@@Z` | `0x5A630` | 832 | UnwindData |  |
| 1557 | `?WriteToStream@CWbemObject@@UEAAJPEAUIStream@@@Z` | `0x5A980` | 518 | UnwindData |  |
| 1119 | `?IsInstancePartAvailable@CWbemInstance@@IEAAHXZ` | `0x5AB90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `??ACFixedBSTRArray@@QEAAAEAPEAGH@Z` | `0x5ABA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 694 | `?GetAt@CFixedBSTRArray@@QEAAAEAPEAGH@Z` | `0x5ABA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `?IsDecorationPartAvailable@CWbemInstance@@IEAAHXZ` | `0x5ABC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1084 | `?IsArray@CType@@QEAAHXZ` | `0x5ABD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `?GetWbemObjectUnknown@CWbemInstance@@UEAAPEAUIUnknown@@XZ` | `0x5ABE0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `?AreKeysRemoved@CDecorationPart@@QEAAHXZ` | `0x5AC50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `?GetSuperclassName@CWbemClass@@UEAAJPEAVCVar@@@Z` | `0x5AC90` | 214 | UnwindData |  |
| 680 | `?GetActualType@CType@@QEAAKXZ` | `0x5AD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `?GetQualifierSetStart@CInstancePart@@UEAAPEAEXZ` | `0x5AD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `?GetMemoryLimit@CClassPart@@UEAAPEAEXZ` | `0x5AD90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `?Release@CClassQualifierSet@@UEAAKXZ` | `0x5ADB0` | 40 | UnwindData |  |
| 1303 | `?Release@CInstanceQualifierSet@@UEAAKXZ` | `0x5ADB0` | 40 | UnwindData |  |
| 841 | `?GetMarshalSizeMax@CWbemObject@@UEAAJAEBU_GUID@@PEAXK1KPEAK@Z` | `0x5AE50` | 117 | UnwindData |  |
| 1242 | `?QueryObjectFlags@CWbemObject@@UEAAJJ_KPEA_K@Z` | `0x5AED0` | 724 | UnwindData |  |
| 1442 | `?SetThreadSecurity@CWbemCallSecurity@@UEAAJPEAU_IWmiThreadSecHandle@@@Z` | `0x5B1B0` | 415 | UnwindData |  |
| 514 | `?CopyBlobOf@CWbemInstance@@UEAAJPEAVCWbemObject@@@Z` | `0x5B360` | 499 | UnwindData |  |
| 811 | `?GetLength@CClassAndMethods@@QEAAKXZ` | `0x5B560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `?GetNumUpperBound@CBasicQualifierSet@@QEAAHXZ` | `0x5B580` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??0CDecorationPart@@QEAA@XZ` | `0x5B5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??0CInternalString@@QEAA@XZ` | `0x5B5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `?AddRef@CQualifierSet@@UEAAKXZ` | `0x5B5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1268 | `?RebaseSecondarySet@CInstancePQSContainer@@QEAAXXZ` | `0x5B5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 836 | `?GetMap@CWbemGuidToClassMap@@QEAAJAEAVCGUID@@PEAPEAVCWbemClassToIdMap@@@Z` | `0x5B610` | 204 | UnwindData |  |
| 915 | `?GetPropQualifier@CWbemClass@@UEAAJPEAVCPropertyInformation@@PEBGPEAVCVar@@PEAJ3@Z` | `0x5B6F0` | 266 | UnwindData |  |
| 91 | `??0CWbemObjectArrayPacket@@QEAA@PEAEK_N@Z` | `0x5B800` | 176 | UnwindData |  |
| 1094 | `?IsClassPartShared@CWbemInstance@@IEAAHXZ` | `0x5B8C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1062 | `?ImpersonateClient@CWbemCallSecurity@@UEAAJXZ` | `0x5B8E0` | 259 | UnwindData |  |
| 1369 | `?SetData@CWbemObjectArrayPacket@@QEAAXPEAEK_N@Z` | `0x5B9F0` | 170 | UnwindData |  |
| 669 | `?Free@CFastHeap@@QEAAXKK@Z` | `0x5BBD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 582 | `?Delete@CUntypedArray@@QEAAXVCType@@PEAVCFastHeap@@@Z` | `0x5BC00` | 151 | UnwindData |  |
| 671 | `?FreeString@CFastHeap@@QEAAXK@Z` | `0x5BCA0` | 86 | UnwindData |  |
| 580 | `?Delete@CBasicQualifierSet@@SAXPEAEPEAVCFastHeap@@@Z` | `0x5BD00` | 89 | UnwindData |  |
| 944 | `?GetPropertyType@CClassPart@@QEAAJPEAVCPropertyInformation@@PEAJ1@Z` | `0x5BD60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 947 | `?GetPropertyType@CWbemClass@@UEAAJPEAVCPropertyInformation@@PEAJ1@Z` | `0x5BD60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `?RevertToSelf@CWbemCallSecurity@@UEAAJXZ` | `0x5BD90` | 104 | UnwindData |  |
| 66 | `??0CQualifierSetListContainer@@QEAA@$$QEAV0@@Z` | `0x5BE00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `??0CQualifierSetListContainer@@QEAA@AEBV0@@Z` | `0x5BE00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `??0CQualifierSetListContainer@@QEAA@XZ` | `0x5BE00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `?ComputeNecessarySpace@CDataTable@@SAKHH@Z` | `0x5BE50` | 22 | UnwindData |  |
| 516 | `?CopyInfo@CLimitationMapping@@IEAAXAEAVCPropertyInformation@@AEBV2@@Z` | `0x5BE70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `?GetMaxMarshalStreamSize@CWbemInstance@@UEAAJPEAK@Z` | `0x5BEA0` | 213 | UnwindData |  |
| 722 | `?GetClassQualifier@CClassPart@@QEAAJPEBGPEAVCVar@@PEAJ2@Z` | `0x5BF80` | 241 | UnwindData |  |
| 464 | `?Compact@CMethodPart@@QEAAXXZ` | `0x5C0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1561 | `?fast_wcsncpy@CCompressedString@@SAPEAGPEAGPEBGH@Z` | `0x5C0E0` | 35 | UnwindData |  |
| 568 | `?CreateListOfEmpties@CQualifierSetList@@SAPEAEPEAEH@Z` | `0x5C160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 912 | `?GetPropQualifier@CClassPart@@QEAAJPEAVCPropertyInformation@@PEBGPEAVCVar@@PEAJ3@Z` | `0x5C170` | 232 | UnwindData |  |
| 971 | `?GetQualifierSet@CWbemClass@@UEAAJPEAPEAUIWbemQualifierSet@@@Z` | `0x5C260` | 217 | UnwindData |  |
| 133 | `??1CBasicQualifierSet@@QEAA@XZ` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `??1CInstancePQSContainer@@QEAA@XZ` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `??1CWbemDataPacket@@QEAA@XZ` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `??1CWbemMtgtDeliverEventPacket@@QEAA@XZ` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `??1CWbemObjectArrayPacket@@QEAA@XZ` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `??1CWbemSmartEnumNextPacket@@QEAA@XZ` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `?ReduceClassAndMethodsSpace@CWbemClass@@QEAAXK@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1279 | `?ReduceClassPartSpace@CClassAndMethods@@UEAAXPEAVCClassPart@@K@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1280 | `?ReduceClassPartSpace@CWbemInstance@@UEAAXPEAVCClassPart@@K@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1282 | `?ReduceDataTableSpace@CInstancePart@@UEAAXPEAEKK@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1283 | `?ReduceHeapSize@CClassPart@@UEAAXPEAEKK@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `?ReduceHeapSize@CInstancePart@@UEAAXPEAEKK@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `?ReduceHeapSize@CMethodPart@@UEAAXPEAEKK@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1286 | `?ReduceInstancePartSpace@CWbemInstance@@UEAAXPEAVCInstancePart@@K@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `?ReduceMethodPartSpace@CClassAndMethods@@UEAAXPEAVCMethodPart@@K@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1288 | `?ReducePropertyTableSpace@CClassPart@@UEAAXPEAEKK@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `?ReduceQualifierSetListSpace@CInstancePart@@UEAAXPEAEKK@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `?ReduceQualifierSetSpace@CClassPart@@UEAAXPEAVCBasicQualifierSet@@K@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1293 | `?ReduceQualifierSetSpace@CMethodQualifierSetContainer@@UEAAXPEAVCBasicQualifierSet@@K@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1373 | `?SetDataLength@CInstancePart@@QEAAXK@Z` | `0x5C360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `?CheckLocalBoolQualifier@CClassPart@@QEAAHPEBG@Z` | `0x5C370` | 65 | UnwindData |  |
| 794 | `?GetKeyOrigin@CClassPart@@QEAAJAEAVWString2@@@Z` | `0x5C3C0` | 295 | UnwindData |  |
| 939 | `?GetPropertyOrigin@CWbemObject@@UEAAJPEBGPEAPEAG@Z` | `0x5C4F0` | 415 | UnwindData |  |
| 938 | `?GetPropertyOrigin@CClassPart@@QEAAJPEBGPEAPEAG@Z` | `0x5C6A0` | 350 | UnwindData |  |
| 696 | `?GetAtFromLast@CCompressedStringList@@QEAAPEAVCCompressedString@@H@Z` | `0x5C810` | 92 | UnwindData |  |
| 741 | `?GetDynasty@CClassPart@@QEAAJPEAVCVar@@@Z` | `0x5C880` | 304 | UnwindData |  |
| 742 | `?GetDynasty@CClassPart@@QEAAPEAVCCompressedString@@XZ` | `0x5C9C0` | 43 | UnwindData |  |
| 809 | `?GetLast@CCompressedStringList@@QEAAPEAVCCompressedString@@XZ` | `0x5CA00` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1262 | `?Rebase@CMethodPart@@QEAAXPEAE@Z` | `0x5CA70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `?Copy@CFastHeap@@QEAAXKKK@Z` | `0x5CAC0` | 94 | UnwindData |  |
| 917 | `?GetPropQualifier@CWbemClass@@UEAAJPEBG0PEAVCVar@@PEAJ2@Z` | `0x5CB30` | 112 | UnwindData |  |
| 1104 | `?IsDynamic@CWbemClass@@QEAAHXZ` | `0x5CBB0` | 75 | UnwindData |  |
| 134 | `??1CClassAndMethods@@QEAA@XZ` | `0x5CC10` | 22 | UnwindData |  |
| 1081 | `?IsAbstract@CWbemClass@@QEAAHXZ` | `0x5CCB0` | 69 | UnwindData |  |
| 748 | `?GetFirst@CCompressedStringList@@QEAAPEAVCCompressedString@@XZ` | `0x5CD00` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `??0CWbemEnumMarshaling@@QEAA@PEAVCLifeControl@@PEAUIUnknown@@@Z` | `0x5CEE0` | 89 | UnwindData |  |
| 108 | `??0XEnumMarshaling@CWbemEnumMarshaling@@QEAA@PEAV1@@Z` | `0x5CF40` | 39 | UnwindData |  |
| 84 | `??0CWbemGuidToClassMap@@QEAA@XZ` | `0x5CF70` | 72 | UnwindData |  |
| 8 | `??0?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@QEAA@PEAVCWbemRefreshingSvc@@@Z` | `0x5D030` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@QEAA@PEAVCWbemEnumMarshaling@@@Z` | `0x5D030` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??0?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@QEAA@PEAVCWmiObjectFactory@@@Z` | `0x5D030` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `?IsKeyed@CWbemClass@@UEAAHXZ` | `0x5D0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??0CMethodPart@@QEAA@XZ` | `0x5D0D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `?GetMaxMarshalStreamSize@CWbemObject@@UEAAJPEAK@Z` | `0x5D110` | 38 | UnwindData |  |
| 1527 | `?ValidateBuffer@CPropertyLookupTable@@SA_KPEAE_K@Z` | `0x5D140` | 266 | UnwindData |  |
| 607 | `?EndEnumeration@CWbemObject@@UEAAJXZ` | `0x5D310` | 72 | UnwindData |  |
| 717 | `?GetClassPart@CWbemClass@@MEAAPEAVCClassPart@@XZ` | `0x5D370` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1103 | `?IsDynamic@CClassPart@@QEAAHXZ` | `0x5D3B0` | 72 | UnwindData |  |
| 1083 | `?IsAmendment@CWbemClass@@QEAAHXZ` | `0x5D400` | 69 | UnwindData |  |
| 1080 | `?IsAbstract@CClassPart@@QEAAHXZ` | `0x5D450` | 66 | UnwindData |  |
| 635 | `?Extend@CFastHeap@@QEAAHKKK@Z` | `0x5D530` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1051 | `?GetWbemObjectUnknown@CClassAndMethods@@UEAAPEAUIUnknown@@XZ` | `0x5D570` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `??0CWbemCallSecurity@@QEAA@PEAVCLifeControl@@@Z` | `0x5D5B0` | 83 | UnwindData |  |
| 1241 | `?QueryInterface@CWbemThreadSecurityHandle@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x5D850` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | `?GetUnmarshalClass@CWbemObject@@UEAAJAEBU_GUID@@PEAXK1KPEAU2@@Z` | `0x5D8C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `?MarshalPacket@CWbemSmartEnumNextPacket@@QEAAJPEAEKJPEAPEAUIWbemClassObject@@PEAU_GUID@@PEAH@Z` | `0x5D910` | 200 | UnwindData |  |
| 1082 | `?IsAmendment@CClassPart@@QEAAHXZ` | `0x5DA60` | 66 | UnwindData |  |
| 541 | `?CreateEmpty@CBasicQualifierSet@@SAPEAEPEAE@Z` | `0x5DAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `?CreateEmpty@CCompressedStringList@@SAPEAEPEAE@Z` | `0x5DAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??0CClassPartContainer@@QEAA@$$QEAV0@@Z` | `0x5DAD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??0CClassPartContainer@@QEAA@AEBV0@@Z` | `0x5DAD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??0CClassPartContainer@@QEAA@XZ` | `0x5DAD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `?GetQualifier@CQualifierSet@@QEAAPEAUCQualifier@@PEBG@Z` | `0x5DB30` | 20 | UnwindData |  |
| 1107 | `?IsEmpty@CCompressedStringList@@QEAAHXZ` | `0x5DB50` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `??4CInternalString@@QEAAAEAV0@AEBV0@@Z` | `0x5DF30` | 58 | UnwindData |  |
| 47 | `??0CInternalString@@QEAA@AEBV0@@Z` | `0x5DF70` | 207 | UnwindData |  |
| 1018 | `?GetSuperclassName@CClassPart@@QEAAPEAVCCompressedString@@XZ` | `0x5E050` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 698 | `?GetAuthentication@CWbemThreadSecurityHandle@@UEAAJPEAK@Z` | `0x5E2A0` | 120 | UnwindData |  |
| 77 | `??0CWbemDataPacket@@IEAA@XZ` | `0x5E320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??0CWbemMtgtDeliverEventPacket@@AEAA@XZ` | `0x5E320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `??0CWbemSmartEnumNextPacket@@AEAA@XZ` | `0x5E320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `?GetQualifierSetStart@CClassPart@@UEAAPEAEXZ` | `0x5E340` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1415 | `?SetPropByHandle@CWbemObject@@UEAAJJJKPEAX@Z` | `0x5E400` | 1,478 | UnwindData |  |
| 141 | `??1CInternalString@@QEAA@XZ` | `0x5EA00` | 26 | UnwindData |  |
| 1034 | `?GetTotalRealLength@CClassPart@@QEAAKXZ` | `0x5EA20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `?ReadQWORD@CWbemObject@@UEAAJJPEA_K@Z` | `0x5EA70` | 397 | UnwindData |  |
| 907 | `?GetPrevious@CCompressedStringList@@QEAAPEAVCCompressedString@@PEAV2@@Z` | `0x5EC10` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `?CalculateNecessarySpaceByType@CUntypedArray@@SAKVCType@@H@Z` | `0x5EE30` | 26 | UnwindData |  |
| 884 | `?GetNumMethods@CMethodPart@@IEAAHXZ` | `0x5EF40` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `?GetClassPart@CWbemInstance@@MEAAPEAVCClassPart@@XZ` | `0x5F050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `?CreateLimitedRepresentation@CDerivationList@@QEAAPEAEPEAVCLimitationMapping@@PEAE@Z` | `0x5F080` | 69 | UnwindData |  |
| 395 | `?BeginEnumeration@CQualifierSet@@UEAAJJ@Z` | `0x5F100` | 512 | UnwindData |  |
| 1182 | `?MakeNotArray@CType@@SAKK@Z` | `0x5F310` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 969 | `?GetQualifierLocally@CBasicQualifierSet@@SAPEAUCQualifier@@PEAEPEAVCFastHeap@@PEBG@Z` | `0x5F350` | 25 | UnwindData |  |
| 1063 | `?IncrementLength@CBasicQualifierSet@@QEAAXK@Z` | `0x5F3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `?CompactAll@CWbemClass@@UEAAXXZ` | `0x5F3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `?GetBasic@CType@@QEAAKXZ` | `0x5F400` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `?AddObjectToRefresher@CWbemRefreshingSvc@@MEAAJPEAU_WBEM_REFRESHER_ID@@PEBGJPEAUIWbemContext@@KPEAU_WBEM_REFRESH_INFO@@PEAK@Z` | `0x5F520` | 568 | UnwindData |  |
| 572 | `?CreateRefreshableObjectTemplate@CWbemRefreshingSvc@@IEAAJPEBGJPEAPEAUIWbemClassObject@@@Z` | `0x5F760` | 2,011 | UnwindData |  |
| 365 | `?AddObjectToRefresher_@CWbemRefreshingSvc@@IEAAJHPEAU_WBEM_REFRESHER_ID@@PEAVCWbemObject@@JPEAUIWbemContext@@PEAU_WBEM_REFRESH_INFO@@@Z` | `0x5FF50` | 985 | UnwindData |  |
| 356 | `?AddEnumToRefresher@CWbemRefreshingSvc@@MEAAJPEAU_WBEM_REFRESHER_ID@@PEBGJPEAUIWbemContext@@KPEAU_WBEM_REFRESH_INFO@@PEAK@Z` | `0x60330` | 1,141 | UnwindData |  |
| 1170 | `?IsWinmgmt@CWbemRefreshingSvc@@IEAAHPEAU_WBEM_REFRESHER_ID@@@Z` | `0x607B0` | 38 | UnwindData |  |
| 358 | `?AddEnumToRefresher_@CWbemRefreshingSvc@@IEAAJHPEAU_WBEM_REFRESHER_ID@@PEAVCWbemObject@@PEBGJPEAUIWbemContext@@PEAU_WBEM_REFRESH_INFO@@@Z` | `0x607E0` | 761 | UnwindData |  |
| 983 | `?GetRefrMgr@CWbemRefreshingSvc@@IEAAJPEAPEAU_IWbemRefresherMgr@@@Z` | `0x60AE0` | 247 | UnwindData |  |
| 1538 | `?ValidateRange@CWbemObject@@QEAAHPEAPEAG@Z` | `0x60BE0` | 88 | UnwindData |  |
| 1537 | `?ValidateRange@CPropertyLookupTable@@QEAAJPEAPEAGPEAVCDataTable@@PEAVCFastHeap@@@Z` | `0x60C40` | 439 | UnwindData |  |
| 1458 | `?SpawnKeyedInstance@CWbemClass@@UEAAJJPEBGPEAPEAU_IWmiObject@@@Z` | `0x61C60` | 1,612 | UnwindData |  |
| 436 | `?CheapCompare@CCompressedString@@QEBAHAEBV1@@Z` | `0x63260` | 87 | UnwindData |  |
| 1139 | `?IsParents@CType@@SAHK@Z` | `0x632C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `??0CInstancePartContainer@@QEAA@$$QEAV0@@Z` | `0x632F0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??0CInstancePartContainer@@QEAA@AEBV0@@Z` | `0x632F0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `??0CInstancePartContainer@@QEAA@XZ` | `0x632F0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `??0CMethodPartContainer@@QEAA@$$QEAV0@@Z` | `0x632F0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??0CMethodPartContainer@@QEAA@AEBV0@@Z` | `0x632F0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??0CMethodPartContainer@@QEAA@XZ` | `0x632F0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `??1CLimitationMapping@@QEAA@XZ` | `0x63390` | 158 | UnwindData |  |
| 1178 | `?MakeArray@CType@@SAKK@Z` | `0x634F0` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 832 | `?GetLengthByType@CUntypedArray@@QEAAKVCType@@@Z` | `0x63B40` | 29 | UnwindData |  |
| 706 | `?GetBlockLength@CWbemClass@@MEAAKXZ` | `0x63B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 829 | `?GetLength@CWbemClass@@QEAAKXZ` | `0x63B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `?GetSig@CMethodDescription@@QEAAKH@Z` | `0x63B80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `?AddRef@CWbemThreadSecurityHandle@@UEAAKXZ` | `0x63BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `?AddRef@CWbemCallSecurity@@UEAAKXZ` | `0x63BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 743 | `?GetDynasty@CWbemClass@@UEAAJPEAVCVar@@@Z` | `0x63BF0` | 52 | UnwindData |  |
| 1130 | `?IsMemCopyAble@CType@@SAHGJ@Z` | `0x63C60` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `?Release@CMethodQualifierSet@@UEAAKXZ` | `0x63CF0` | 79 | UnwindData |  |
| 143 | `??1CMethodQualifierSet@@UEAA@XZ` | `0x63D50` | 36 | UnwindData |  |
| 144 | `??1CMethodQualifierSetContainer@@QEAA@XZ` | `0x63D80` | 29 | UnwindData |  |
| 1295 | `?Release@?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@UEAAKXZ` | `0x63DB0` | 42 | UnwindData |  |
| 1296 | `?Release@?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@UEAAKXZ` | `0x63DB0` | 42 | UnwindData |  |
| 1297 | `?Release@?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@UEAAKXZ` | `0x63DB0` | 42 | UnwindData |  |
| 1298 | `?Release@?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@UEAAKXZ` | `0x63DB0` | 42 | UnwindData |  |
| 1299 | `?Release@?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@UEAAKXZ` | `0x63DB0` | 42 | UnwindData |  |
| 1300 | `?Release@?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@UEAAKXZ` | `0x63DB0` | 42 | UnwindData |  |
| 1301 | `?Release@?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@UEAAKXZ` | `0x63DB0` | 42 | UnwindData |  |
| 754 | `?GetGenus@CWbemClass@@UEAAJPEAVCVar@@@Z` | `0x63DE0` | 32 | UnwindData |  |
| 369 | `?AddRef@?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@UEAAKXZ` | `0x63E40` | 42 | UnwindData |  |
| 370 | `?AddRef@?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@UEAAKXZ` | `0x63E40` | 42 | UnwindData |  |
| 371 | `?AddRef@?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@UEAAKXZ` | `0x63E40` | 42 | UnwindData |  |
| 372 | `?AddRef@?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@UEAAKXZ` | `0x63E40` | 42 | UnwindData |  |
| 373 | `?AddRef@?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@UEAAKXZ` | `0x63E40` | 42 | UnwindData |  |
| 374 | `?AddRef@?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@UEAAKXZ` | `0x63E40` | 42 | UnwindData |  |
| 375 | `?AddRef@?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@UEAAKXZ` | `0x63E40` | 42 | UnwindData |  |
| 966 | `?GetQualifierLocally@CBasicQualifierSet@@QEAAPEAUCQualifier@@PEBG@Z` | `0x63E70` | 25 | UnwindData |  |
| 70 | `??0CType@@QEAA@XZ` | `0x63EB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 755 | `?GetGenus@CWbemInstance@@UEAAJPEAVCVar@@@Z` | `0x63F30` | 32 | UnwindData |  |
| 1186 | `?Map@CLimitationMapping@@QEAAXPEAVCPropertyInformation@@0H@Z` | `0x64310` | 442 | UnwindData |  |
| 768 | `?GetHeap@CPropertyLookupTable@@QEAAPEAVCFastHeap@@XZ` | `0x64550` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??0CWbemRefreshingSvc@@QEAA@PEAVCLifeControl@@PEAUIUnknown@@@Z` | `0x646F0` | 162 | UnwindData |  |
| 120 | `??0XWbemRefrSvc@CWbemRefreshingSvc@@QEAA@PEAV1@@Z` | `0x647A0` | 39 | UnwindData |  |
| 105 | `??0XCfgRefrSrvc@CWbemRefreshingSvc@@QEAA@PEAV1@@Z` | `0x647D0` | 39 | UnwindData |  |
| 4 | `??0?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@QEAA@PEAVCWbemRefreshingSvc@@@Z` | `0x64800` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1047 | `?GetVARTYPE@CType@@QEAAGXZ` | `0x64850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `?QueryInterface@?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x64860` | 65 | UnwindData |  |
| 1232 | `?QueryInterface@?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x64860` | 65 | UnwindData |  |
| 1233 | `?QueryInterface@?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x64860` | 65 | UnwindData |  |
| 1234 | `?QueryInterface@?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x64860` | 65 | UnwindData |  |
| 1235 | `?QueryInterface@?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x64860` | 65 | UnwindData |  |
| 1236 | `?QueryInterface@?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x64860` | 65 | UnwindData |  |
| 1237 | `?QueryInterface@?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x64860` | 65 | UnwindData |  |
| 1377 | `?SetDecoration@CWbemObject@@UEAAJPEBG0@Z` | `0x64BF0` | 119 | UnwindData |  |
| 1124 | `?IsLimited@CDecorationPart@@QEAAHXZ` | `0x64C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `?GetInterface@CWbemEnumMarshaling@@MEAAPEAXAEBU_GUID@@@Z` | `0x64C90` | 1,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `?IsPossibleSystemPropertyName@CSystemProperties@@SAHPEBG@Z` | `0x65380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 922 | `?GetProperty@CWbemClass@@MEAAJPEAVCPropertyInformation@@PEAVCVar@@@Z` | `0x653A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | `?GetMarshalPacket@XEnumMarshaling@CWbemEnumMarshaling@@UEAAJAEBU_GUID@@KPEAPEAUIWbemClassObject@@PEAKPEAPEAE@Z` | `0x653C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `?SetVtableLength@CLimitationMapping@@QEAAXKH@Z` | `0x653D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 657 | `?FindLimitationError@CWbemClass@@QEAA?AVWString@@JPEAVCWStringArray@@@Z` | `0x653F0` | 218 | UnwindData |  |
| 960 | `?GetQualifier@CWbemClass@@UEAAJPEBGPEAVCVar@@PEAJ2@Z` | `0x65520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `??MCInternalString@@QEBA_NAEBV0@@Z` | `0x65540` | 24 | UnwindData |  |
| 1223 | `?PlugKeyHoles@CWbemInstance@@QEAAJXZ` | `0x65560` | 453 | UnwindData |  |
| 1243 | `?QueryPartInfo@CWbemObject@@UEAAJPEAK@Z` | `0x65860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `?BeginMethodEnumeration@CWbemClass@@UEAAJJ@Z` | `0x65870` | 211 | UnwindData |  |
| 1013 | `?GetStart@CWbemInstance@@QEAAPEAEXZ` | `0x65970` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `?GetStart@CWbemObject@@QEAAPEAEXZ` | `0x65970` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `?EndMethodEnumeration@CWbemClass@@UEAAJXZ` | `0x65B50` | 208 | UnwindData |  |
| 1543 | `WbemStringFree` | `0x65CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | `?GetKeyProps@CWbemClass@@UEAAHAEAVCWStringArray@@@Z` | `0x65CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `?AcquireCompressedString@CInternalString@@QEAAXPEAVCCompressedString@@@Z` | `0x65CE0` | 46 | UnwindData |  |
| 1137 | `?IsParentClass@CWbemInstance@@UEAAJJPEAU_IWmiObject@@@Z` | `0x65E80` | 207 | UnwindData |  |
| 1118 | `?IsInstanceOf@CWbemInstance@@QEAAHPEAVCWbemClass@@@Z` | `0x65F60` | 184 | UnwindData |  |
| 400 | `?Build@CLimitationMapping@@QEAAXH@Z` | `0x66040` | 241 | UnwindData |  |
| 515 | `?CopyData@CCompressedStringList@@QEAAPEAEPEAE@Z` | `0x66140` | 55 | UnwindData |  |
| 730 | `?GetDataTable@CClassPart@@UEAAPEAVCDataTable@@XZ` | `0x66180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `?CreateDerivedClass@CWbemClass@@QEAAJPEAV1@HPEAVCDecorationPart@@@Z` | `0x66190` | 280 | UnwindData |  |
| 1454 | `?SpawnDerivedClass@CWbemClass@@UEAAJJPEAPEAUIWbemClassObject@@@Z` | `0x662B0` | 624 | UnwindData |  |
| 535 | `?CreateDerivedClass@CWbemClass@@QEAAJPEAPEAV1@@Z` | `0x66530` | 747 | UnwindData |  |
| 1546 | `?WriteDerivedClass@CWbemClass@@QEAAJPEAEHPEAVCDecorationPart@@@Z` | `0x66830` | 295 | UnwindData |  |
| 537 | `?CreateDerivedPart@CClassAndMethods@@QEAAPEAEPEAEK@Z` | `0x66960` | 88 | UnwindData |  |
| 616 | `?EstimateDerivedClassSpace@CWbemClass@@QEAAKPEAVCDecorationPart@@@Z` | `0x669C0` | 88 | UnwindData |  |
| 617 | `?EstimateDerivedPartSpace@CClassAndMethods@@QEAAKXZ` | `0x66A20` | 33 | UnwindData |  |
| 618 | `?EstimateDerivedPartSpace@CClassPart@@QEAAKXZ` | `0x66A50` | 34 | UnwindData |  |
| 620 | `?EstimateExtraSpace@CCompressedStringList@@SAKPEAVCCompressedString@@@Z` | `0x66A80` | 27 | UnwindData |  |
| 538 | `?CreateDerivedPart@CClassPart@@QEAAPEAEPEAEH@Z` | `0x66AB0` | 343 | UnwindData |  |
| 577 | `?CreateWithExtra@CCompressedStringList@@QEAAPEAEPEAEPEAVCCompressedString@@@Z` | `0x66C10` | 158 | UnwindData |  |
| 1550 | `?WritePropagatedVersion@CPropertyLookupTable@@QEAAPEAEPEAVCFastHeap@@PEAE0@Z` | `0x66CC0` | 152 | UnwindData |  |
| 539 | `?CreateDerivedPart@CMethodPart@@QEAAPEAEPEAEK@Z` | `0x66D60` | 314 | UnwindData |  |
| 1549 | `?WritePropagatedVersion@CDataTable@@QEAAPEAEPEAVCPropertyLookupTable@@PEAVCFastHeap@@PEAE1@Z` | `0x66EA0` | 242 | UnwindData |  |
| 540 | `?CreateDerivedVersion@CMethodDescription@@SAHPEFAU1@0PEAVCFastHeap@@1@Z` | `0x66FA0` | 257 | UnwindData |  |
| 716 | `?GetClassObject@CWbemObjectArrayPacket@@AEAAJAEAVCWbemObjectPacket@@PEAPEAUIWbemClassObject@@@Z` | `0x670C0` | 180 | UnwindData |  |
| 69 | `??0CType@@QEAA@K@Z` | `0x67180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1140 | `?IsPointerType@CType@@QEAAHXZ` | `0x67190` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `?MakeParents@CType@@SAKK@Z` | `0x672D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `??1CWbemRefreshingSvc@@UEAA@XZ` | `0x67360` | 114 | UnwindData |  |
| 626 | `?EstimateMergeSpace@CMethodPart@@SAKAEAV1@0@Z` | `0x67640` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 715 | `?GetClassNameW@CWbemInstance@@UEAAJPEAVCVar@@@Z` | `0x67690` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `?Lock@CHiPerfLock@@QEAAHK@Z` | `0x67840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1437 | `?SetServiceData@CWbemRefreshingSvc@@MEAAJPEAG0@Z` | `0x67850` | 406 | UnwindData |  |
| 393 | `?AsymmetricMerge@CWbemInstance@@SAJPEAV1@0@Z` | `0x67A30` | 665 | UnwindData |  |
| 624 | `?EstimateMergeSpace@CClassAndMethods@@SAKAEAV1@0@Z` | `0x67CD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | `?GetInterface@CWbemRefreshingSvc@@MEAAPEAXAEBU_GUID@@@Z` | `0x67D00` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1503 | `?Unmerge@CWbemObject@@UEAAJJKPEAKPEAX@Z` | `0x67D70` | 400 | UnwindData |  |
| 277 | `??8CInternalString@@QEBA_NAEBV0@@Z` | `0x67F10` | 26 | UnwindData |  |
| 1179 | `?MakeFakeFromIndex@CFastHeap@@SAKH@Z` | `0x67F80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `?CreateEmpty@CDecorationPart@@QEAAPEAEEPEAE@Z` | `0x67FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `?GetPropName@CWbemClass@@UEAAJHPEAVCVar@@@Z` | `0x67FD0` | 72 | UnwindData |  |
| 1486 | `?Unlock@CHiPerfLock@@QEAAHXZ` | `0x68020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `?EstimateMergeSpace@CClassPart@@SAKAEAV1@0@Z` | `0x68030` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 883 | `?GetNumMappings@CLimitationMapping@@QEAAHXZ` | `0x68550` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `?GetSize@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEBAHXZ` | `0x68550` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `??0CWmiObjectFactory@@QEAA@PEAVCLifeControl@@PEAUIUnknown@@@Z` | `0x68C50` | 59 | UnwindData |  |
| 114 | `??0XObjectFactory@CWmiObjectFactory@@QEAA@PEAV1@@Z` | `0x68CA0` | 39 | UnwindData |  |
| 573 | `?CreateUnmergedVersion@CMethodDescription@@SAHPEFAU1@0PEAVCFastHeap@@1@Z` | `0x68D20` | 232 | UnwindData |  |
| 1500 | `?Unmerge@CWbemClass@@UEAAJPEAEHPEAK@Z` | `0x68E10` | 285 | UnwindData |  |
| 1494 | `?Unmerge@CClassAndMethods@@QEAAPEAEPEAEK@Z` | `0x68F40` | 88 | UnwindData |  |
| 1498 | `?Unmerge@CMethodPart@@QEAAPEAEPEAEK@Z` | `0x68FA0` | 395 | UnwindData |  |
| 1495 | `?Unmerge@CClassPart@@QEAAPEAEPEAEH@Z` | `0x69140` | 443 | UnwindData |  |
| 1499 | `?Unmerge@CPropertyLookupTable@@QEAAPEAEPEAVCDataTable@@PEAVCFastHeap@@PEAE1@Z` | `0x69310` | 210 | UnwindData |  |
| 1493 | `?Unmerge@CBasicQualifierSet@@SAPEAEPEAEPEAVCFastHeap@@01@Z` | `0x694A0` | 185 | UnwindData |  |
| 1497 | `?Unmerge@CDerivationList@@QEAAPEAEPEAE@Z` | `0x69560` | 110 | UnwindData |  |
| 1496 | `?Unmerge@CDataTable@@QEAAPEAEPEAVCPropertyLookupTable@@PEAVCFastHeap@@PEAE1@Z` | `0x695E0` | 240 | UnwindData |  |
| 1153 | `?IsTouched@CMethodDescription@@SAHPEFAU1@PEAVCFastHeap@@@Z` | `0x696E0` | 55 | UnwindData |  |
| 1515 | `?VARTYPEToType@CType@@SA?AV1@G@Z` | `0x69970` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1112 | `?IsIdenticalWith@CClassPart@@QEAAHAEAV1@@Z` | `0x69B20` | 216 | UnwindData |  |
| 965 | `?GetQualifierLocally@CBasicQualifierSet@@QEAAPEAUCQualifier@@PEAVCCompressedString@@@Z` | `0x69C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `?IsPropagated@CMethodPart@@IEAAHH@Z` | `0x69C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1125 | `?IsLimited@CWbemObject@@QEAAHXZ` | `0x69C90` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `?GetLength@CEmbeddedObject@@QEAAKXZ` | `0x69FA0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `?MarkKeyRemoval@CDecorationPart@@SAXPEAE@Z` | `0x6A0E0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 902 | `?GetParentAtIndex@CWbemObject@@QEAAPEAVCCompressedString@@H@Z` | `0x6A200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `?GetWbemObjectUnknown@CMethodQualifierSetContainer@@UEAAPEAUIUnknown@@XZ` | `0x6A220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1129 | `?IsLocalized@CWbemInstance@@UEAAHXZ` | `0x6A240` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `?GetRelPath@CWbemClass@@UEAAPEAGH@Z` | `0x6A3A0` | 101 | UnwindData |  |
| 1126 | `?IsLocalized@CClassPart@@QEAAHXZ` | `0x6A410` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `?GetSecondarySet@CMethodQualifierSetContainer@@QEAAPEAVCBasicQualifierSet@@XZ` | `0x6A450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1055 | `?GetWbemObjectUnknown@CMethodPart@@QEAAPEAUIUnknown@@XZ` | `0x6A480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 727 | `?GetCurrentOrigin@CClassPart@@UEAAKXZ` | `0x6A4A0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1216 | `?New@CWbemCallSecurity@@SAPEAV1@XZ` | `0x6A5D0` | 81 | UnwindData |  |
| 1154 | `?IsTouched@CMethodPart@@QEAAHHPEAH@Z` | `0x6A630` | 111 | UnwindData |  |
| 543 | `?CreateEmpty@CClassPart@@SAPEAEPEAE@Z` | `0x6A6B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `?GetHeap@CMethodQualifierSetContainer@@UEAAPEAVCFastHeap@@XZ` | `0x6A6F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `??0CWmiTextSourceArray@@QEAA@XZ` | `0x6A780` | 29 | UnwindData |  |
| 18 | `??0?$CRefedPointerArray@VCWmiTextSource@@@@QEAA@XZ` | `0x6A7B0` | 45 | UnwindData |  |
| 494 | `?ComputeMergeSpace@CBasicQualifierSet@@SAKPEAEPEAVCFastHeap@@01H@Z` | `0x6A7F0` | 175 | UnwindData |  |
| 1396 | `?SetLocalized@CClassPart@@QEAAXH@Z` | `0x6A910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 673 | `?Get@CWbemFetchRefrMgr@@QEAAJPEAPEAU_IWbemRefresherMgr@@@Z` | `0x6A930` | 396 | UnwindData |  |
| 1480 | `?Unbind@CInternalString@@QEAAXXZ` | `0x6AB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `?GetNameAsBSTR@CSystemProperties@@SAPEAGH@Z` | `0x6AB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1246 | `?ReadProp@CWbemObject@@UEAAJPEBGJKPEAJ1PEAHPEAKPEAX@Z` | `0x6AB30` | 725 | UnwindData |  |
| 729 | `?GetDataLength@CDataTable@@QEAAKXZ` | `0x6AE10` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1398 | `?SetLocalized@CWbemClass@@UEAAXH@Z` | `0x6AEA0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `??0CWbemFetchRefrMgr@@QEAA@PEAVCLifeControl@@PEAUIUnknown@@@Z` | `0x6B0E0` | 59 | UnwindData |  |
| 111 | `??0XFetchRefrMgr@CWbemFetchRefrMgr@@QEAA@PEAV1@@Z` | `0x6B130` | 39 | UnwindData |  |
| 6 | `??0?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@QEAA@PEAVCWbemRemoteRefresher@@@Z` | `0x6B160` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@QEAA@PEAVCWbemFetchRefrMgr@@@Z` | `0x6B160` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 634 | `?EstimateUnmergeSpace@CWbemInstance@@UEAAKXZ` | `0x6B1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `?IsClientOnly@CDecorationPart@@QEAAHXZ` | `0x6B1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `?IsClientOnly@CWbemObject@@QEAAHXZ` | `0x6B210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1547 | `?WriteProp@CWbemObject@@UEAAJPEBGJKKJPEAX@Z` | `0x6B230` | 647 | UnwindData |  |
| 785 | `?GetIndexedProps@CWbemClass@@UEAAHAEAVCWStringArray@@@Z` | `0x6B4C0` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `?CreateEmpty@CClassAndMethods@@SAPEAEPEAE@Z` | `0x6B7A0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `?Init@CWbemFetchRefrMgr@@QEAAJPEAU_IWmiProvSS@@PEAUIWbemServices@@@Z` | `0x6B9F0` | 351 | UnwindData |  |
| 549 | `?CreateEmpty@CMethodPart@@SAPEAEPEAE@Z` | `0x6BB60` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `?CreateEmpty@CFastHeap@@SAPEAEPEAE@Z` | `0x6BF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1123 | `?IsKeyed@CWbemInstance@@UEAAHXZ` | `0x6BF30` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `?Compare@CBasicQualifierSet@@QEAAHAEAV1@EPEAPEBGK@Z` | `0x6C140` | 1,554 | UnwindData |  |
| 887 | `?GetNumProperties@CWbemClass@@UEAAHXZ` | `0x6CF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `?IsParentClass@CWbemClass@@UEAAJJPEAU_IWmiObject@@@Z` | `0x6CFB0` | 198 | UnwindData |  |
| 1091 | `?IsChildOf@CWbemClass@@QEAAHPEAV1@@Z` | `0x6D080` | 184 | UnwindData |  |
| 872 | `?GetName@CMethodPart@@IEAAPEAVCCompressedString@@H@Z` | `0x6D1D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `??1XCfgRefrSrvc@CWbemRefreshingSvc@@QEAA@XZ` | `0x6D260` | 17 | UnwindData |  |
| 163 | `??1XEnumMarshaling@CWbemEnumMarshaling@@QEAA@XZ` | `0x6D260` | 17 | UnwindData |  |
| 165 | `??1XObjectFactory@CWmiObjectFactory@@QEAA@XZ` | `0x6D260` | 17 | UnwindData |  |
| 744 | `?GetDynasty@CWbemInstance@@UEAAJPEAVCVar@@@Z` | `0x6D2A0` | 52 | UnwindData |  |
| 151 | `??1CWbemFetchRefrMgr@@UEAA@XZ` | `0x6D410` | 54 | UnwindData |  |
| 1127 | `?IsLocalized@CInstancePart@@QEAAHXZ` | `0x6D500` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `??1XWbemRefrSvc@CWbemRefreshingSvc@@QEAA@XZ` | `0x6D5A0` | 17 | UnwindData |  |
| 117 | `??0XObjectTextSrc@CWmiObjectTextSrc@@QEAA@PEAV1@@Z` | `0x6D760` | 39 | UnwindData |  |
| 1507 | `?Update@CQualifierSet@@QEAAJAEAVCBasicQualifierSet@@JPEAVCFixedBSTRArray@@@Z` | `0x6DA70` | 1,056 | UnwindData |  |
| 1184 | `?MakeSubsetInst@CWbemClass@@UEAAJPEAU_IWmiObject@@PEAPEAU2@@Z` | `0x6DEC0` | 256 | UnwindData |  |
| 1438 | `?SetServiceData@XCfgRefrSrvc@CWbemRefreshingSvc@@UEAAJPEAG0@Z` | `0x6DFE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1114 | `?IsImpersonating@CWbemCallSecurity@@UEAAHXZ` | `0x6E020` | 2,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1109 | `?IsEmpty@CQualifierSetList@@QEAAHXZ` | `0x6E8E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1148 | `?IsSingleton@CClassPart@@QEAAHXZ` | `0x6E950` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `?GetPropertyCount@CWbemClass@@UEAAJPEAVCVar@@@Z` | `0x6E980` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1277 | `?Reduce@CFastHeap@@QEAAXKKK@Z` | `0x6EA10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1345 | `?SetClassQualifier@CClassPart@@QEAAJPEBGPEAVCVar@@J@Z` | `0x6EA40` | 366 | UnwindData |  |
| 550 | `?CreateEmpty@CPropertyLookupTable@@SAPEAEPEAE@Z` | `0x6EE40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `?GetText@CBasicQualifierSet@@QEAAJJAEAVWString@@@Z` | `0x6EEA0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 790 | `?GetInterface@CWbemFetchRefrMgr@@MEAAPEAXAEBU_GUID@@@Z` | `0x6EFF0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `?DoesSignatureMatchOther@CMethodPart@@IEAAHAEAV1@HW4METHOD_SIGNATURE_TYPE@@@Z` | `0x6F0F0` | 166 | UnwindData |  |
| 603 | `?Empty@CFastHeap@@QEAAXXZ` | `0x6F200` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1420 | `?SetPropQualifier@CWbemClass@@UEAAJPEBG0JPEAVCVar@@@Z` | `0x6F280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 599 | `?DoSignaturesMatch@CMethodPart@@IEAAHHW4METHOD_SIGNATURE_TYPE@@PEAVCWbemObject@@@Z` | `0x6F2A0` | 109 | UnwindData |  |
| 1230 | `?QueryBlanket@CWbemCallSecurity@@UEAAJPEAK0PEAPEAG00PEAPEAX0@Z` | `0x6F8B0` | 261 | UnwindData |  |
| 645 | `?ExtendMethodPartSpace@CClassAndMethods@@UEAAHPEAVCMethodPart@@K@Z` | `0x6F9C0` | 51 | UnwindData |  |
| 416 | `?CanContainAbstract@CInstancePQSContainer@@UEAAJH@Z` | `0x6FA00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `?CanContainAbstract@CInstancePart@@UEAAJH@Z` | `0x6FA00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `?CanContainAbstract@CMethodQualifierSetContainer@@UEAAJH@Z` | `0x6FA00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `?CanContainDynamic@CInstancePart@@UEAAJXZ` | `0x6FA00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `?CanContainDynamic@CMethodQualifierSetContainer@@UEAAJXZ` | `0x6FA00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `?CanContainKey@CClassPart@@UEAAJXZ` | `0x6FA00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `?CanContainKey@CInstancePQSContainer@@UEAAJXZ` | `0x6FA00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `?CanContainKey@CInstancePart@@UEAAJXZ` | `0x6FA00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `?CanContainKey@CMethodQualifierSetContainer@@UEAAJXZ` | `0x6FA00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `?CanContainSingleton@CInstancePQSContainer@@UEAAJXZ` | `0x6FA00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `?CanContainSingleton@CInstancePart@@UEAAJXZ` | `0x6FA00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `?CanContainSingleton@CMethodQualifierSetContainer@@UEAAJXZ` | `0x6FA00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??0?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAA@AEBV?$CReferenceManager@VCWmiTextSource@@@@@Z` | `0x6FA80` | 45 | UnwindData |  |
| 928 | `?GetPropertyCount@CWbemInstance@@UEAAJPEAVCVar@@@Z` | `0x703F0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `?CalculateNecessarySpaceByLength@CUntypedArray@@SAKHH@Z` | `0x70630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `?CanContainAbstract@CClassPart@@UEAAJH@Z` | `0x70640` | 368 | UnwindData |  |
| 831 | `?GetLengthByActualLength@CUntypedArray@@QEAAKH@Z` | `0x707C0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1439 | `?SetSig@CMethodDescription@@QEAAXHK@Z` | `0x70980` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `?GetSuperclassName@CWbemInstance@@UEAAJPEAVCVar@@@Z` | `0x709B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 643 | `?ExtendHeapSize@CMethodPart@@UEAAHPEAEKK@Z` | `0x709D0` | 66 | UnwindData |  |
| 792 | `?GetInterface@CWmiObjectFactory@@MEAAPEAXAEBU_GUID@@@Z` | `0x70E50` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??0CHiPerfLock@@QEAA@XZ` | `0x70EC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `?CanBeReconciledWith@CBasicQualifierSet@@QEAAHAEAV1@@Z` | `0x70F20` | 571 | UnwindData |  |
| 675 | `?Get@XFetchRefrMgr@CWbemFetchRefrMgr@@UEAAJPEAPEAU_IWbemRefresherMgr@@@Z` | `0x715D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1397 | `?SetLocalized@CInstancePart@@QEAAXH@Z` | `0x71600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1429 | `?SetQualifier@CWbemClass@@UEAAJPEBGPEAVCVar@@J@Z` | `0x71620` | 127 | UnwindData |  |
| 740 | `?GetDescription@CWbemObject@@UEAAJPEAPEAG@Z` | `0x716B0` | 219 | UnwindData |  |
| 1346 | `?SetClientOnly@CDecorationPart@@QEAAXXZ` | `0x717A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1347 | `?SetClientOnly@CWbemObject@@QEAAXXZ` | `0x717C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `?AddText@CMethodPart@@QEAAJAEAVWString@@J@Z` | `0x71830` | 233 | UnwindData |  |
| 160 | `??1CWmiObjectFactory@@UEAA@XZ` | `0x719A0` | 54 | UnwindData |  |
| 1399 | `?SetLocalized@CWbemInstance@@UEAAXH@Z` | `0x71AC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `??BCInternalString@@QEBA?AVWString@@XZ` | `0x71AF0` | 45 | UnwindData |  |
| 161 | `??1CWmiTextSourceArray@@QEAA@XZ` | `0x71B30` | 18 | UnwindData |  |
| 132 | `??1?$CRefedPointerArray@VCWmiTextSource@@@@QEAA@XZ` | `0x71B50` | 18 | UnwindData |  |
| 399 | `?BeginMethodEnumeration@CWbemInstance@@UEAAJJ@Z` | `0x71B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 587 | `?DeleteMethod@CWbemInstance@@UEAAJPEBG@Z` | `0x71B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `?EndMethodEnumeration@CWbemInstance@@UEAAJXZ` | `0x71B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `?GetMethod@CWbemInstance@@UEAAJPEBGJPEAPEAUIWbemClassObject@@1@Z` | `0x71B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `?GetMethodOrigin@CWbemInstance@@UEAAJPEBGPEAPEAG@Z` | `0x71B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 861 | `?GetMethodQualifierSet@CWbemInstance@@UEAAJPEBGPEAPEAUIWbemQualifierSet@@@Z` | `0x71B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1222 | `?NextMethod@CWbemInstance@@UEAAJJPEAPEAGPEAPEAUIWbemClassObject@@1@Z` | `0x71B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `?PutMethod@CWbemInstance@@UEAAJPEBGJPEAUIWbemClassObject@@1@Z` | `0x71B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1391 | `?SetInheritanceChain@CWbemInstance@@UEAAJJPEAPEAG@Z` | `0x71B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `?SetMethodOrigin@CWbemInstance@@UEAAJPEBGJ@Z` | `0x71B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1427 | `?SetPropertyOrigin@CWbemInstance@@UEAAJPEBGJ@Z` | `0x71B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `?AddEnumToRefresher@XWbemRefrSvc@CWbemRefreshingSvc@@UEAAJPEAU_WBEM_REFRESHER_ID@@PEBGJPEAUIWbemContext@@KPEAU_WBEM_REFRESH_INFO@@PEAK@Z` | `0x71B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `?EstimateUnmergeSpace@CWbemClass@@UEAAKXZ` | `0x71B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `?EstimateUnmergeSpace@CClassAndMethods@@QEAAKXZ` | `0x71BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `?Delete@CWbemInstance@@UEAAJPEBG@Z` | `0x71BD0` | 561 | UnwindData |  |
| 718 | `?GetClassPart@CWbemClass@@UEAAJPEAXKPEAK@Z` | `0x71EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `?GetObjectParts@CWbemClass@@UEAAJPEAXKKPEAK@Z` | `0x71EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | `?GetPropQualifier@CWbemClass@@UEAAJPEAVCPropertyInformation@@PEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x71EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `?MergeClassPart@CWbemClass@@UEAAJPEAUIWbemClassObject@@@Z` | `0x71EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1342 | `?SetClassPart@CWbemClass@@UEAAJPEAXK@Z` | `0x71EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1412 | `?SetObjectParts@CWbemClass@@UEAAJPEAXKK@Z` | `0x71EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1467 | `?StripClassPart@CWbemClass@@UEAAJXZ` | `0x71EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `??1XFetchRefrMgr@CWbemFetchRefrMgr@@QEAA@XZ` | `0x71EF0` | 17 | UnwindData |  |
| 168 | `??1XWbemRemoteRefr@CWbemRemoteRefresher@@QEAA@XZ` | `0x71EF0` | 17 | UnwindData |  |
| 1067 | `?Init@XFetchRefrMgr@CWbemFetchRefrMgr@@UEAAJPEAU_IWmiProvSS@@PEAUIWbemServices@@@Z` | `0x72600` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 726 | `?GetCurrentOrigin@CClassAndMethods@@UEAAKXZ` | `0x726D0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `??OCInternalString@@QEBA_NAEBV0@@Z` | `0x72920` | 26 | UnwindData |  |
| 166 | `??1XObjectTextSrc@CWmiObjectTextSrc@@QEAA@XZ` | `0x72940` | 17 | UnwindData |  |
| 1028 | `?GetText@XObjectTextSrc@CWmiObjectTextSrc@@UEAAJJPEAUIWbemClassObject@@KPEAUIWbemContext@@PEAPEAG@Z` | `0x72960` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `?GetCurrentOrigin@CWbemClass@@QEAAKXZ` | `0x72B30` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `?GetMethodOrigin@CMethodPart@@QEAAJPEBGPEAK@Z` | `0x72FB0` | 62 | UnwindData |  |
| 281 | `??A?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAPEAVCWmiTextSource@@H@Z` | `0x73280` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `??A?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEBAPEBVCWmiTextSource@@H@Z` | `0x73280` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 692 | `?GetAt@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAPEAVCWmiTextSource@@H@Z` | `0x73280` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 693 | `?GetAt@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEBAPEBVCWmiTextSource@@H@Z` | `0x73280` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `?GetMethodOrigin@CWbemClass@@UEAAJPEBGPEAPEAG@Z` | `0x732F0` | 528 | UnwindData |  |
| 1457 | `?SpawnInstance@CWbemInstance@@UEAAJJPEAPEAUIWbemClassObject@@@Z` | `0x73570` | 664 | UnwindData |  |
| 380 | `?AddRefElement@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@IEAAXPEAVCWmiTextSource@@@Z` | `0x73810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `?GetNormalizedPath@CWbemObject@@UEAAJJPEAPEAG@Z` | `0x73820` | 324 | UnwindData |  |
| 1152 | `?IsTopLevel@CClassPart@@QEAAHXZ` | `0x73970` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `?AddObjectToRefresher@XWbemRefrSvc@CWbemRefreshingSvc@@UEAAJPEAU_WBEM_REFRESHER_ID@@PEBGJPEAUIWbemContext@@KPEAU_WBEM_REFRESH_INFO@@PEAK@Z` | `0x73AC0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `??4CInternalString@@QEAAHPEAVCCompressedString@@@Z` | `0x73BA0` | 117 | UnwindData |  |
| 1108 | `?IsEmpty@CInternalString@@QEAA_NXZ` | `0x73D10` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `?GetDefaultPtrByHandle@CClassPart@@QEAAJJPEAPEAX@Z` | `0x73DE0` | 60 | UnwindData |  |
| 1098 | `?IsCompressed@CClassPart@@QEAAHXZ` | `0x73E30` | 41 | UnwindData |  |
| 999 | `?GetSource@CWbemObject@@UEAAJPEAPEAG@Z` | `0x73E60` | 40 | UnwindData |  |
| 559 | `?CreateLPWSTRCopy@CInternalString@@QEBAPEAGXZ` | `0x73EE0` | 65 | UnwindData |  |
| 676 | `?GetAbstractFlavor@CClassPart@@QEAAEXZ` | `0x74870` | 39 | UnwindData |  |
| 1551 | `?WritePropertyAsMethodParam@CWbemClass@@QEAAJAEAVWString@@HJPEAV1@H@Z` | `0x749C0` | 927 | UnwindData |  |
| 492 | `?CompareUnicodeToAscii@CCompressedString@@KAHPEBGPEBD@Z` | `0x74E70` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `?CompareTo@CClassAndMethods@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x75140` | 68 | UnwindData |  |
| 127 | `??1?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@QEAA@XZ` | `0x75260` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `??1?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@QEAA@XZ` | `0x75260` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `??1?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@QEAA@XZ` | `0x75260` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `??1?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@QEAA@XZ` | `0x752A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `?IsEmpty@CBasicQualifierSet@@QEAAHXZ` | `0x752E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `?IsEmpty@CBasicQualifierSet@@SAHPEAE@Z` | `0x752E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??0CBasicQualifierSet@@QEAA@XZ` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `??4CClassPartContainer@@QEAAAEAV0@$$QEAV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `??4CClassPartContainer@@QEAAAEAV0@AEBV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `??4CInstancePartContainer@@QEAAAEAV0@$$QEAV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `??4CInstancePartContainer@@QEAAAEAV0@AEBV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `??4CKnownStringTable@@QEAAAEAV0@$$QEAV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `??4CKnownStringTable@@QEAAAEAV0@AEBV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `??4CMethodPartContainer@@QEAAAEAV0@$$QEAV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `??4CMethodPartContainer@@QEAAAEAV0@AEBV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `??4CQualifierSetListContainer@@QEAAAEAV0@$$QEAV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `??4CQualifierSetListContainer@@QEAAAEAV0@AEBV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `??4CReservedWordTable@@QEAAAEAV0@$$QEAV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `??4CReservedWordTable@@QEAAAEAV0@AEBV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `??4CSystemProperties@@QEAAAEAV0@$$QEAV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `??4CSystemProperties@@QEAAAEAV0@AEBV0@@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | `?CreateEmpty@CDataTable@@SAPEAEPEAE@Z` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `?GetArray@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAAEAVCFlexArray@@XZ` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `?GetStart@CCompressedString@@QEAAPEAEXZ` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `?GetStart@CEmbeddedObject@@QEAAPEAEXZ` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `?GetWbemObjectUnknown@CWbemClass@@QEAAPEAUIUnknown@@XZ` | `0x752F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `??BCInternalString@@AEAAPEAVCCompressedString@@XZ` | `0x75300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `??BCInternalString@@AEBAPEAVCCompressedString@@XZ` | `0x75300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `?GetHeapData@CFastHeap@@QEAAPEAEXZ` | `0x75300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `?GetStart@CCompressedStringList@@QEAAPEAEXZ` | `0x75300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `?GetStart@CDataTable@@QEAAPEAEXZ` | `0x75300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `?GetStart@CDecorationPart@@QEAAPEAEXZ` | `0x75300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `?GetStart@CPropertyLookupTable@@QEAAPEAEXZ` | `0x75300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `?GetHeaderLength@CCompressedStringList@@SAKXZ` | `0x75310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `?GetHeaderLength@CUntypedArray@@SAKXZ` | `0x75310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `?GetMinLength@CBasicQualifierSet@@SAKXZ` | `0x75310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `?GetMinLength@CFastHeap@@SAKXZ` | `0x75310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | `?GetMinLength@CPropertyLookupTable@@SAKXZ` | `0x75310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `?GetSeparatorLength@CCompressedStringList@@KAKXZ` | `0x75310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 762 | `?GetHeap@CBasicQualifierSet@@QEAAPEAVCFastHeap@@XZ` | `0x75320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1031 | `?GetThreadToken@CWbemThreadSecurityHandle@@QEAAPEAXXZ` | `0x75320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `?GetFlags@CLimitationMapping@@QEAAJXZ` | `0x75330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `?Rebase@CCompressedStringList@@QEAAXPEAE@Z` | `0x75340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1263 | `?Rebase@CPropertyLookupTable@@QEAAXPEAE@Z` | `0x75340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1363 | `?SetData@CSharedLock@@QEAAXPEAUSHARED_LOCK_DATA@@@Z` | `0x75340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `?Initialize@CKnownStringTable@@SAXXZ` | `0x75350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1371 | `?SetDataLength@CBasicQualifierSet@@KAXPEAEK@Z` | `0x75370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1394 | `?SetLength@CFixedBSTRArray@@QEAAXH@Z` | `0x75370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 699 | `?GetAuthenticationLevel@CWbemThreadSecurityHandle@@QEAAKXZ` | `0x75380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `?GetStart@CClassAndMethods@@QEAAPEAEXZ` | `0x75390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1414 | `?SetOrigin@CWbemThreadSecurityHandle@@QEAAXW4tag_WMI_THREAD_SECURITY_ORIGIN@@@Z` | `0x753A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `?GetImpersonationLevel@CWbemThreadSecurityHandle@@QEAAKXZ` | `0x753B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `??BCType@@QEAAKXZ` | `0x753C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `?GetLength@CBasicQualifierSet@@QEAAKXZ` | `0x753C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `?GetLength@CFixedBSTRArray@@QEAAHXZ` | `0x753C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 821 | `?GetLength@CInstancePart@@SAHPEAE@Z` | `0x753C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | `?GetLengthFromData@CBasicQualifierSet@@SAKPEAE@Z` | `0x753C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 882 | `?GetNumElements@CUntypedArray@@QEAAHXZ` | `0x753C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `?GetNumSets@CQualifierSetList@@QEAAHXZ` | `0x753C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 995 | `?GetServerPrincipalName@CWbemThreadSecurityHandle@@QEAAPEAGXZ` | `0x753D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `?GetStart@CInstancePart@@QEAAPEAEXZ` | `0x753D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `?SetAddChildKeys@CLimitationMapping@@QEAAXH@Z` | `0x753E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1386 | `?SetIncludeDerivation@CLimitationMapping@@QEAAXH@Z` | `0x753F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `?GetFirstQualifierFromData@CBasicQualifierSet@@SAPEAUCQualifier@@PEAE@Z` | `0x75400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `?SetIncludeNamespace@CLimitationMapping@@QEAAXH@Z` | `0x75410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `?ComputeNecessarySpace@CQualifierSetList@@SAKH@Z` | `0x75420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | `?ExtendClassPartSpace@CWbemInstance@@UEAAHPEAVCClassPart@@K@Z` | `0x75420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 640 | `?ExtendDataTableSpace@CInstancePart@@UEAAHPEAEKK@Z` | `0x75420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 760 | `?GetHeaderLength@CQualifierSetList@@SAHXZ` | `0x75420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 782 | `?GetIndexOfKey@CKnownStringTable@@SAHXZ` | `0x75420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `?GetMinLength@CDecorationPart@@SAKXZ` | `0x75420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `?Initialize@CWbemRefreshingSvc@@UEAAHXZ` | `0x75420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1348 | `?SetContainer@CFastHeap@@QEAAXPEAVCHeapContainer@@@Z` | `0x75430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 871 | `?GetMinLength@CWbemClass@@SAKXZ` | `0x75440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `?GetLength@CDataTable@@QEAAKXZ` | `0x75450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `?GetRawData@CCompressedString@@QEBAPEAEXZ` | `0x75460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `?MaxNumProperties@CSystemProperties@@SAHXZ` | `0x75470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 775 | `?GetIdentity@CWbemThreadSecurityHandle@@QEAAPEAGXZ` | `0x75480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `?GetStart@CClassPart@@QEAAPEAEXZ` | `0x75480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `?ShouldIncludeNamespace@CLimitationMapping@@QEAAHXZ` | `0x75490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1374 | `?SetDataToNone@CBasicQualifierSet@@SAXPEAE@Z` | `0x754A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1446 | `?ShouldAddChildKeys@CLimitationMapping@@QEAAHXZ` | `0x754B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1325 | `?Reset@CLimitationMapping@@QEAAXXZ` | `0x754C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1264 | `?Rebase@CQualifierSetList@@QEAAXPEAE@Z` | `0x754D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `?GetLength@CQualifierSetList@@QEAAHXZ` | `0x754E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 891 | `?GetNumSystemProperties@CSystemProperties@@SAHXZ` | `0x754F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `?LowerByte@CCompressedString@@KADG@Z` | `0x75500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1381 | `?SetFlags@CLimitationMapping@@QEAAXJ@Z` | `0x75510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | `?GetMinLength@CClassPart@@SAHXZ` | `0x75520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1447 | `?ShouldIncludeDerivation@CLimitationMapping@@QEAAHXZ` | `0x75530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `?GetMinLength@CMethodPart@@SAKXZ` | `0x75540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1388 | `?SetIncludeServer@CLimitationMapping@@QEAAXH@Z` | `0x75550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1050 | `?GetVtableLength@CLimitationMapping@@QEAAKXZ` | `0x75560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1449 | `?ShouldIncludeServer@CLimitationMapping@@QEAAHXZ` | `0x75570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `?GetMinLength@CClassAndMethods@@SAKXZ` | `0x75580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `??1?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@QEAA@XZ` | `0x75590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `??1?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@QEAA@XZ` | `0x75590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `??1?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@QEAA@XZ` | `0x755B0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1030 | `?GetThreadSecurityHandle@CWbemCallSecurity@@QEAAPEAVCWbemThreadSecurityHandle@@XZ` | `0x75630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@QEAA@PEAVCWmiObjectTextSrc@@@Z` | `0x75640` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | `?GetAuthenticationService@CWbemThreadSecurityHandle@@QEAAKXZ` | `0x756E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `?GetAuthorizationService@CWbemThreadSecurityHandle@@QEAAKXZ` | `0x756F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `?ComputeRealSpace@CQualifierSetList@@SAKH@Z` | `0x75700` | 6,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0CClassAndMethods@@QEAA@$$QEAV0@@Z` | `0x77080` | 199 | UnwindData |  |
| 21 | `??0CClassAndMethods@@QEAA@AEBV0@@Z` | `0x77080` | 199 | UnwindData |  |
| 23 | `??0CClassPart@@QEAA@$$QEAV0@@Z` | `0x77150` | 220 | UnwindData |  |
| 24 | `??0CClassPart@@QEAA@AEBV0@@Z` | `0x77150` | 220 | UnwindData |  |
| 29 | `??0CClassQualifierSet@@QEAA@$$QEAV0@@Z` | `0x77240` | 39 | UnwindData |  |
| 30 | `??0CClassQualifierSet@@QEAA@AEBV0@@Z` | `0x77240` | 39 | UnwindData |  |
| 44 | `??0CInstanceQualifierSet@@QEAA@$$QEAV0@@Z` | `0x77240` | 39 | UnwindData |  |
| 45 | `??0CInstanceQualifierSet@@QEAA@AEBV0@@Z` | `0x77240` | 39 | UnwindData |  |
| 35 | `??0CInstancePQSContainer@@QEAA@$$QEAV0@@Z` | `0x77270` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??0CInstancePQSContainer@@QEAA@AEBV0@@Z` | `0x77270` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??0CInstancePart@@QEAA@$$QEAV0@@Z` | `0x772C0` | 199 | UnwindData |  |
| 39 | `??0CInstancePart@@QEAA@AEBV0@@Z` | `0x772C0` | 199 | UnwindData |  |
| 50 | `??0CLimitationMapping@@QEAA@AEAV0@@Z` | `0x77390` | 143 | UnwindData |  |
| 52 | `??0CMethodPart@@QEAA@$$QEAV0@@Z` | `0x77430` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `??0CMethodPart@@QEAA@AEBV0@@Z` | `0x77430` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??0CMethodQualifierSet@@QEAA@$$QEAV0@@Z` | `0x77480` | 66 | UnwindData |  |
| 59 | `??0CMethodQualifierSet@@QEAA@AEBV0@@Z` | `0x77480` | 66 | UnwindData |  |
| 61 | `??0CMethodQualifierSetContainer@@QEAA@$$QEAV0@@Z` | `0x774D0` | 107 | UnwindData |  |
| 62 | `??0CMethodQualifierSetContainer@@QEAA@AEBV0@@Z` | `0x774D0` | 107 | UnwindData |  |
| 64 | `??0CQualifierSet@@QEAA@AEBV0@@Z` | `0x77550` | 109 | UnwindData |  |
| 73 | `??0CWbemClass@@QEAA@AEBV0@@Z` | `0x775D0` | 186 | UnwindData |  |
| 85 | `??0CWbemInstance@@QEAA@AEBV0@@Z` | `0x77690` | 203 | UnwindData |  |
| 90 | `??0CWbemObject@@QEAA@AEBV0@@Z` | `0x77770` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `??4CBasicQualifierSet@@QEAAAEAV0@AEBV0@@Z` | `0x77840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `??4CDecorationPart@@QEAAAEAV0@AEBV0@@Z` | `0x77840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `??4CHiPerfLock@@QEAAAEAV0@AEBV0@@Z` | `0x77840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `??4CMethodDescription@@QEAAAEAU0@AEBU0@@Z` | `0x77840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `??4CQualifierSetList@@QEAAAEAV0@AEBV0@@Z` | `0x77840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `??4CWbemMtgtDeliverEventPacket@@QEAAAEAV0@AEBV0@@Z` | `0x77840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `??4CWbemSmartEnumNextPacket@@QEAAAEAV0@AEBV0@@Z` | `0x77840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `??4CClassAndMethods@@QEAAAEAV0@$$QEAV0@@Z` | `0x77860` | 158 | UnwindData |  |
| 181 | `??4CClassAndMethods@@QEAAAEAV0@AEBV0@@Z` | `0x77860` | 158 | UnwindData |  |
| 182 | `??4CClassPart@@QEAAAEAV0@$$QEAV0@@Z` | `0x77910` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `??4CClassPart@@QEAAAEAV0@AEBV0@@Z` | `0x77910` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `??4CClassQualifierSet@@QEAAAEAV0@$$QEAV0@@Z` | `0x77A00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `??4CClassQualifierSet@@QEAAAEAV0@AEBV0@@Z` | `0x77A00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `??4CInstanceQualifierSet@@QEAAAEAV0@$$QEAV0@@Z` | `0x77A00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `??4CInstanceQualifierSet@@QEAAAEAV0@AEBV0@@Z` | `0x77A00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `??4CQualifierSet@@QEAAAEAV0@AEBV0@@Z` | `0x77A00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `??4CCompressedString@@QEAAAEAV0@$$QEAV0@@Z` | `0x77A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `??4CCompressedString@@QEAAAEAV0@AEBV0@@Z` | `0x77A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `??4CCompressedStringList@@QEAAAEAV0@$$QEAV0@@Z` | `0x77AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `??4CCompressedStringList@@QEAAAEAV0@AEBV0@@Z` | `0x77AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `??4CDerivationList@@QEAAAEAV0@$$QEAV0@@Z` | `0x77AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `??4CDerivationList@@QEAAAEAV0@AEBV0@@Z` | `0x77AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `??4CFixedBSTRArray@@QEAAAEAV0@AEBV0@@Z` | `0x77AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `??4SHARED_LOCK_DATA@@QEAAAEAU0@AEBU0@@Z` | `0x77AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `??4CDataTable@@QEAAAEAV0@$$QEAV0@@Z` | `0x77AE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `??4CDataTable@@QEAAAEAV0@AEBV0@@Z` | `0x77B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `??4CDecorationPart@@QEAAAEAV0@$$QEAV0@@Z` | `0x77B30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `??4CEmbeddedObject@@QEAAAEAV0@$$QEAV0@@Z` | `0x77B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `??4CEmbeddedObject@@QEAAAEAV0@AEBV0@@Z` | `0x77B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `??4CFastHeap@@QEAAAEAV0@$$QEAV0@@Z` | `0x77B80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `??4CFastHeap@@QEAAAEAV0@AEBV0@@Z` | `0x77BC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `??4CHiPerfLock@@QEAAAEAV0@$$QEAV0@@Z` | `0x77BF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `??4CInstancePQSContainer@@QEAAAEAV0@$$QEAV0@@Z` | `0x77C20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `??4CInstancePQSContainer@@QEAAAEAV0@AEBV0@@Z` | `0x77C20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `??4CInstancePart@@QEAAAEAV0@$$QEAV0@@Z` | `0x77C60` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `??4CInstancePart@@QEAAAEAV0@AEBV0@@Z` | `0x77C60` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `??4CLimitationMapping@@QEAAAEAV0@AEAV0@@Z` | `0x77D40` | 137 | UnwindData |  |
| 219 | `??4CMethodDescription@@QEAAAEAU0@$$QEAU0@@Z` | `0x77DD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `??4CMethodPart@@QEAAAEAV0@$$QEAV0@@Z` | `0x77E10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `??4CMethodPart@@QEAAAEAV0@AEBV0@@Z` | `0x77E10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `??4CMethodQualifierSet@@QEAAAEAV0@$$QEAV0@@Z` | `0x77E60` | 108 | UnwindData |  |
| 226 | `??4CMethodQualifierSet@@QEAAAEAV0@AEBV0@@Z` | `0x77E60` | 108 | UnwindData |  |
| 227 | `??4CMethodQualifierSetContainer@@QEAAAEAV0@$$QEAV0@@Z` | `0x77EE0` | 91 | UnwindData |  |
| 228 | `??4CMethodQualifierSetContainer@@QEAAAEAV0@AEBV0@@Z` | `0x77EE0` | 91 | UnwindData |  |
| 229 | `??4CPropertyLookupTable@@QEAAAEAV0@$$QEAV0@@Z` | `0x77F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `??4CPropertyLookupTable@@QEAAAEAV0@AEBV0@@Z` | `0x77F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `??4CWbemDataPacket@@QEAAAEAV0@AEBV0@@Z` | `0x77F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `??4CWbemObjectArrayPacket@@QEAAAEAV0@AEBV0@@Z` | `0x77F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `??4CQualifierSetList@@QEAAAEAV0@$$QEAV0@@Z` | `0x77F90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `??4CType@@QEAAAEAV0@$$QEAV0@@Z` | `0x77FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `??4CType@@QEAAAEAV0@AEBV0@@Z` | `0x77FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `??4CUntypedArray@@QEAAAEAV0@$$QEAV0@@Z` | `0x77FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `??4CUntypedArray@@QEAAAEAV0@AEBV0@@Z` | `0x77FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `??4SHARED_LOCK_DATA@@QEAAAEAU0@$$QEAU0@@Z` | `0x77FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `??4SHMEM_HANDLE@@QEAAAEAU0@$$QEAU0@@Z` | `0x77FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `??8CInternalString@@QEBA_NPEBG@Z` | `0x78010` | 23 | UnwindData |  |
| 279 | `??8CQualifierSet@@QEAAHAEAV0@@Z` | `0x78030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `??9CInternalString@@QEBA_NAEBV0@@Z` | `0x78050` | 26 | UnwindData |  |
| 350 | `??_FCClassQualifierSet@@QEAAXXZ` | `0x78270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `??_FCInstanceQualifierSet@@QEAAXXZ` | `0x78280` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `?AbsoluteToHeap@CFastHeap@@IEAAKPEAE@Z` | `0x78310` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `?AddString@CCompressedStringList@@QEAAXPEBG@Z` | `0x783D0` | 106 | UnwindData |  |
| 392 | `?ArePropertiesLimited@CLimitationMapping@@QEAAHXZ` | `0x78440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `?CVarToType@CType@@SA?AV1@AEAVCVar@@@Z` | `0x78460` | 127 | UnwindData |  |
| 450 | `?ClearWriteOnlyProperties@CWbemClass@@UEAAJXZ` | `0x78550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `?Compare@CInternalString@@QEBAHAEBV1@@Z` | `0x78560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `?Compare@CInternalString@@QEBAHPEBG@Z` | `0x78580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `?ComputeNecessarySpace@CCompressedStringList@@QEAAKPEAVCCompressedString@@@Z` | `0x78590` | 29 | UnwindData |  |
| 589 | `?DeleteProperty@CClassPart@@QEAAXH@Z` | `0x78780` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 604 | `?Empty@CInternalString@@QEAAXXZ` | `0x787B0` | 35 | UnwindData |  |
| 621 | `?EstimateExtraSpace@CCompressedStringList@@SAKPEBG@Z` | `0x787E0` | 18 | UnwindData |  |
| 623 | `?EstimateLimitedRepresentationSpace@CWbemObject@@QEAAKJPEAVCWStringArray@@@Z` | `0x78800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `?FindPropertyByOffset@CPropertyLookupTable@@QEAAPEAUCPropertyLookup@@K@Z` | `0x78820` | 127 | UnwindData |  |
| 677 | `?GetAbstractFlavor@CWbemClass@@QEAAEXZ` | `0x788B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `?GetActualTransferBlobSize@CWbemInstance@@QEAAJXZ` | `0x788D0` | 79 | UnwindData |  |
| 708 | `?GetClassIndex@CClassPart@@QEAAKPEBG@Z` | `0x78930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 731 | `?GetDataTable@CInstancePart@@QEAAPEAVCDataTable@@XZ` | `0x78940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `?GetDataTableData@CInstancePart@@SAPEAEPEAE@Z` | `0x78950` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `?GetHeap@CMethodPart@@QEAAPEAVCFastHeap@@XZ` | `0x789A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `?GetHeapPtrByHandle@CClassPart@@QEAAKJ@Z` | `0x789B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 786 | `?GetIndexedProps@CWbemInstance@@UEAAHAEAVCWStringArray@@@Z` | `0x789D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `?GetKey@CWbemInstance@@QEAAPEAVCVar@@XZ` | `0x789F0` | 64 | UnwindData |  |
| 796 | `?GetKeyOrigin@CWbemClass@@UEAAJAEAVWString@@@Z` | `0x78A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `?GetKeyOrigin@CWbemInstance@@QEAAJAEAVWString2@@@Z` | `0x78A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `?GetKeyOrigin@CWbemInstance@@UEAAJAEAVWString@@@Z` | `0x78A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `?GetKeyProps@CWbemInstance@@UEAAHAEAVCWStringArray@@@Z` | `0x78AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 822 | `?GetLength@CInternalString@@QEBAHXZ` | `0x78AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 881 | `?GetNumDecorationIndependentProperties@CSystemProperties@@SAHXZ` | `0x78AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `?GetNumParents@CWbemObject@@QEAAHXZ` | `0x78AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 888 | `?GetNumProperties@CWbemInstance@@UEAAHXZ` | `0x78B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | `?GetPropName@CWbemInstance@@UEAAJHPEAVCVar@@@Z` | `0x78B20` | 72 | UnwindData |  |
| 920 | `?GetPropQualifier@CWbemInstance@@UEAAJPEBG0PEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x78B70` | 123 | UnwindData |  |
| 961 | `?GetQualifier@CWbemInstance@@UEAAJPEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x78C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `?GetQualifierSetListStart@CInstancePart@@UEAAPEAEXZ` | `0x78C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `?GetSyntax@CType@@QEAAPEAGXZ` | `0x78C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `?GetText@CInternalString@@QEBAPEBDXZ` | `0x78C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `?GetTransferArrayBlobSize@CWbemInstance@@QEAAJXZ` | `0x78C50` | 79 | UnwindData |  |
| 1038 | `?GetTransferArrayHeaderSize@CWbemInstance@@SAJXZ` | `0x78CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1040 | `?GetTransferBlobSize@CWbemInstance@@QEAAJXZ` | `0x78CC0` | 79 | UnwindData |  |
| 1089 | `?IsAssociation@CClassPart@@QEAAHXZ` | `0x78D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `?IsAutocook@CClassPart@@QEAAHXZ` | `0x78D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1099 | `?IsCompressed@CWbemClass@@QEAAHXZ` | `0x78D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1111 | `?IsHiPerf@CClassPart@@QEAAHXZ` | `0x78DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1131 | `?IsNonArrayPointerType@CType@@QEAAHXZ` | `0x78DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `?IsParents@CType@@QEAAHXZ` | `0x78DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `?IsSingleton@CWbemClass@@QEAAHXZ` | `0x78DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1150 | `?IsStringType@CType@@QEAAHXZ` | `0x78E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `?IsValidPtr@CFastHeap@@QEAA_NK@Z` | `0x78E20` | 29 | UnwindData |  |
| 1180 | `?MakeLocal@CType@@SAKK@Z` | `0x78E50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1265 | `?Rebase@CQualifierSetList@@QEAAXXZ` | `0x78EA0` | 36 | UnwindData |  |
| 1291 | `?ReduceQualifierSetSpace@CInstancePQSContainer@@UEAAXPEAVCBasicQualifierSet@@K@Z` | `0x78ED0` | 44 | UnwindData |  |
| 1305 | `?Release@CQualifierSet@@UEAAKXZ` | `0x78F10` | 78 | UnwindData |  |
| 1324 | `?Reset@CCompressedStringList@@QEAAXXZ` | `0x79120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1327 | `?ResolveHeapPointer@CClassPart@@QEAAPEAEK@Z` | `0x79140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1329 | `?ResolveHeapString@CClassPart@@QEAAPEAVCCompressedString@@K@Z` | `0x79160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1372 | `?SetDataLength@CClassPart@@QEAAXK@Z` | `0x79180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1395 | `?SetLimited@CDecorationPart@@QEAAXXZ` | `0x79190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `?SetQualifier@CWbemInstance@@UEAAJPEBGJPEAVCTypedValue@@@Z` | `0x791B0` | 48 | UnwindData |  |
| 1431 | `?SetQualifier@CWbemInstance@@UEAAJPEBGPEAVCVar@@J@Z` | `0x791F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1443 | `?SetUsedLength@CFastHeap@@QEAAXK@Z` | `0x79210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1451 | `?Skip@CFastHeap@@QEAAPEAEXZ` | `0x79220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1452 | `?Skip@CPropertyLookupTable@@QEAAPEAEXZ` | `0x79240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1470 | `?TestCircularReference@CClassPart@@QEAAJPEBG@Z` | `0x79260` | 31 | UnwindData |  |
| 1558 | `?WriteTransferArrayHeader@CWbemInstance@@SAXJPEAPEAE@Z` | `0x79290` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `??0CWbemClassCache@@QEAA@AEBV0@@Z` | `0x79550` | 85 | UnwindData |  |
| 247 | `??4CWbemClassCache@@QEAAAEAV0@AEBV0@@Z` | `0x795B0` | 118 | UnwindData |  |
| 352 | `??_FCWbemClassCache@@QEAAXXZ` | `0x79630` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 862 | `?GetMinHeaderSize@CWbemDataPacket@@QEAAKXZ` | `0x79690` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `?CanBeReconciledWith@CClassAndMethods@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x79AC0` | 64 | UnwindData |  |
| 412 | `?CanBeReconciledWith@CClassPart@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x79B10` | 1,556 | UnwindData |  |
| 414 | `?CanBeReconciledWith@CWbemClass@@QEAA?AW4EReconciliation@@PEAV1@@Z` | `0x7A130` | 36 | UnwindData |  |
| 456 | `?CloneEx@CWbemClass@@UEAAJJPEAU_IWmiObject@@@Z` | `0x7A160` | 415 | UnwindData |  |
| 477 | `?CompareDerivedMostClass@CWbemClass@@UEAAJJPEAU_IWmiObject@@@Z` | `0x7A310` | 335 | UnwindData |  |
| 513 | `?CopyBlobOf@CWbemClass@@UEAAJPEAVCWbemObject@@@Z` | `0x7A470` | 265 | UnwindData |  |
| 517 | `?CopyInstanceData@CWbemClass@@UEAAJJPEAU_IWmiObject@@@Z` | `0x7A580` | 105 | UnwindData |  |
| 521 | `?CopyParentProperty@CClassPart@@QEAAJAEAV1@PEBG@Z` | `0x7A5F0` | 903 | UnwindData |  |
| 554 | `?CreateFromBlob@CWbemClass@@SAPEAV1@PEAV1@PEAE_K@Z` | `0x7A980` | 789 | UnwindData |  |
| 560 | `?CreateLimitedRepresentation@CClassAndMethods@@QEAAPEAEPEAVCLimitationMapping@@HPEAEAEAH@Z` | `0x7ACA0` | 109 | UnwindData |  |
| 583 | `?Delete@CWbemClass@@UEAAJPEBG@Z` | `0x7AD20` | 706 | UnwindData |  |
| 586 | `?DeleteMethod@CWbemClass@@UEAAJPEBG@Z` | `0x7AFF0` | 338 | UnwindData |  |
| 588 | `?DeleteProperty@CClassPart@@QEAAJPEBG@Z` | `0x7B150` | 59 | UnwindData |  |
| 659 | `?FindMethod@CWbemClass@@UEAAJPEBG@Z` | `0x7B1A0` | 27 | UnwindData |  |
| 667 | `?ForcePropValue@CWbemClass@@QEAAJPEBGPEAVCVar@@J@Z` | `0x7B1D0` | 357 | UnwindData |  |
| 668 | `?ForcePut@CWbemClass@@QEAAJPEBGJPEAUtagVARIANT@@J@Z` | `0x7B340` | 440 | UnwindData |  |
| 711 | `?GetClassNameW@CClassAndMethods@@SAJAEAVWString@@PEAE@Z` | `0x7B500` | 299 | UnwindData |  |
| 721 | `?GetClassQualifier@CClassPart@@QEAAJPEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x7B640` | 292 | UnwindData |  |
| 783 | `?GetIndexedProps@CClassAndMethods@@SAHAEAVCWStringArray@@PEAE@Z` | `0x7B770` | 128 | UnwindData |  |
| 795 | `?GetKeyOrigin@CClassPart@@QEAAJAEAVWString@@@Z` | `0x7B800` | 334 | UnwindData |  |
| 855 | `?GetMethodQualifier@CWbemClass@@UEAAJPEBG0PEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x7B960` | 369 | UnwindData |  |
| 903 | `?GetParentClassFromBlob@CWbemClass@@UEAAJJKPEAXPEAPEAG@Z` | `0x7BAE0` | 327 | UnwindData |  |
| 913 | `?GetPropQualifier@CClassPart@@QEAAJPEBG0PEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x7BC50` | 271 | UnwindData |  |
| 916 | `?GetPropQualifier@CWbemClass@@UEAAJPEBG0PEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x7BD70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 934 | `?GetPropertyInfoByHandle@CClassPart@@QEAAJJPEAPEAGPEAJ@Z` | `0x7BD90` | 249 | UnwindData |  |
| 942 | `?GetPropertyQualifierSetData@CClassPart@@QEAAPEAEPEBG@Z` | `0x7BE90` | 28 | UnwindData |  |
| 952 | `?GetQualifier@CClassPart@@QEAAJPEBGPEAVCVar@@PEAJ2@Z` | `0x7BEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 959 | `?GetQualifier@CWbemClass@@UEAAJPEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x7BED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `?GetSuperclassName@CClassAndMethods@@SAJAEAVWString@@PEAE@Z` | `0x7BEF0` | 377 | UnwindData |  |
| 1115 | `?IsIndexLocal@CWbemClass@@QEAAHPEBG@Z` | `0x7C070` | 83 | UnwindData |  |
| 1120 | `?IsKeyLocal@CWbemClass@@QEAAHPEBG@Z` | `0x7C0D0` | 83 | UnwindData |  |
| 1128 | `?IsLocalized@CWbemClass@@UEAAHXZ` | `0x7C130` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `?IsPropertyIndexed@CClassPart@@QEAAHPEBG@Z` | `0x7C160` | 109 | UnwindData |  |
| 1145 | `?IsPropertyKeyed@CClassPart@@QEAAHPEBG@Z` | `0x7C1E0` | 88 | UnwindData |  |
| 1163 | `?IsValidObj@CWbemClass@@UEAAJXZ` | `0x7C240` | 143 | UnwindData |  |
| 1165 | `?IsValidPropertyHandle@CClassPart@@QEAAJJ@Z` | `0x7C2E0` | 145 | UnwindData |  |
| 1208 | `?Merge@CWbemClass@@UEAAJJKPEAXPEAPEAU_IWmiObject@@@Z` | `0x7C380` | 163 | UnwindData |  |
| 1269 | `?ReconcileWith@CClassAndMethods@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x7C430` | 64 | UnwindData |  |
| 1270 | `?ReconcileWith@CClassPart@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x7C480` | 138 | UnwindData |  |
| 1272 | `?ReconcileWith@CWbemClass@@QEAA?AW4EReconciliation@@PEAV1@@Z` | `0x7C510` | 36 | UnwindData |  |
| 1273 | `?ReconcileWith@CWbemClass@@UEAAJJPEAU_IWmiObject@@@Z` | `0x7C540` | 406 | UnwindData |  |
| 1281 | `?ReduceDataTableSpace@CClassPart@@UEAAXPEAEKK@Z` | `0x7C6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1344 | `?SetClassQualifier@CClassPart@@QEAAJPEBGJPEAVCTypedValue@@@Z` | `0x7C6F0` | 32 | UnwindData |  |
| 1389 | `?SetInheritanceChain@CClassPart@@QEAAJJPEAPEAG@Z` | `0x7C720` | 484 | UnwindData |  |
| 1390 | `?SetInheritanceChain@CWbemClass@@UEAAJJPEAPEAG@Z` | `0x7C910` | 92 | UnwindData |  |
| 1401 | `?SetMethodOrigin@CWbemClass@@UEAAJPEBGJ@Z` | `0x7C980` | 94 | UnwindData |  |
| 1404 | `?SetMethodQualifier@CWbemClass@@UEAAJPEBG0JPEAVCTypedValue@@@Z` | `0x7C9F0` | 274 | UnwindData |  |
| 1405 | `?SetMethodQualifier@CWbemClass@@UEAAJPEBG0JPEAVCVar@@@Z` | `0x7CB10` | 371 | UnwindData |  |
| 1417 | `?SetPropQualifier@CClassPart@@QEAAJPEBG0JPEAVCTypedValue@@@Z` | `0x7CC90` | 241 | UnwindData |  |
| 1419 | `?SetPropQualifier@CWbemClass@@UEAAJPEBG0JPEAVCTypedValue@@@Z` | `0x7CD90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `?SetPropertyOrigin@CClassPart@@QEAAJPEBGJ@Z` | `0x7CDB0` | 38 | UnwindData |  |
| 1426 | `?SetPropertyOrigin@CWbemClass@@UEAAJPEBGJ@Z` | `0x7CDE0` | 94 | UnwindData |  |
| 1428 | `?SetQualifier@CWbemClass@@UEAAJPEBGJPEAVCTypedValue@@@Z` | `0x7CE50` | 141 | UnwindData |  |
| 1508 | `?Update@CWbemClass@@QEAAJPEAV1@JPEAPEAV1@@Z` | `0x7CEF0` | 747 | UnwindData |  |
| 1509 | `?Update@CWbemClass@@UEAAJPEAU_IWmiObject@@JPEAPEAU2@@Z` | `0x7D1F0` | 402 | UnwindData |  |
| 1511 | `?UpdateProperties@CClassPart@@SAJAEAV1@0J@Z` | `0x7D390` | 703 | UnwindData |  |
| 1512 | `?Upgrade@CWbemClass@@UEAAJPEAU_IWmiObject@@JPEAPEAU2@@Z` | `0x7D660` | 456 | UnwindData |  |
| 628 | `?EstimateNecessarySpace@CEmbeddedObject@@SAKAEAVCVar@@@Z` | `0x7D880` | 69 | UnwindData |  |
| 1462 | `?StoreEmbedded@CEmbeddedObject@@QEAAXKAEAVCVar@@@Z` | `0x7D8D0` | 88 | UnwindData |  |
| 385 | `?AllocateString@CFastHeap@@QEAAHPEBDAEFAK@Z` | `0x7D930` | 118 | UnwindData |  |
| 403 | `?CalculateCachedKey@CWbemInstance@@QEAAPEAVCVar@@XZ` | `0x7E4A0` | 106 | UnwindData |  |
| 457 | `?CloneEx@CWbemInstance@@UEAAJJPEAU_IWmiObject@@@Z` | `0x7E5D0` | 126 | UnwindData |  |
| 467 | `?CompactClass@CWbemInstance@@QEAAXXZ` | `0x7E660` | 94 | UnwindData |  |
| 478 | `?CompareDerivedMostClass@CWbemInstance@@UEAAJJPEAU_IWmiObject@@@Z` | `0x7E6D0` | 105 | UnwindData |  |
| 511 | `?CopyActualTransferBlob@CWbemInstance@@QEAAJJPEAE@Z` | `0x7E740` | 459 | UnwindData |  |
| 512 | `?CopyBlob@CWbemInstance@@QEAAJPEAEH@Z` | `0x7E920` | 383 | UnwindData |  |
| 518 | `?CopyInstanceData@CWbemInstance@@UEAAJJPEAU_IWmiObject@@@Z` | `0x7EAB0` | 131 | UnwindData |  |
| 525 | `?CopyTransferArrayBlob@CWbemInstance@@SAJPEAV1@JJPEAEAEAVCFlexArray@@PEAJ@Z` | `0x7EB40` | 832 | UnwindData |  |
| 526 | `?CopyTransferBlob@CWbemInstance@@QEAAJJJPEAE@Z` | `0x7EE90` | 134 | UnwindData |  |
| 555 | `?CreateFromBlob@CWbemInstance@@SAPEAV1@PEAVCWbemClass@@PEAE_K@Z` | `0x7EF20` | 613 | UnwindData |  |
| 590 | `?DeleteProperty@CInstancePart@@QEAAXPEAVCPropertyInformation@@@Z` | `0x7F2D0` | 79 | UnwindData |  |
| 592 | `?DeleteProperty@CWbemInstance@@QEAAJH@Z` | `0x7F330` | 602 | UnwindData |  |
| 654 | `?FastClone@CWbemInstance@@QEAAJPEAV1@@Z` | `0x7F5E0` | 557 | UnwindData |  |
| 678 | `?GetActualTransferBlob@CWbemInstance@@QEAAXPEAE@Z` | `0x7F880` | 182 | UnwindData |  |
| 720 | `?GetClassPart@CWbemInstance@@UEAAJPEAXKPEAK@Z` | `0x7F940` | 252 | UnwindData |  |
| 724 | `?GetClassSubset@CWbemInstance@@UEAAJKPEAPEBGPEAPEAU_IWmiObject@@@Z` | `0x7FA50` | 105 | UnwindData |  |
| 803 | `?GetKeyStr@CWbemInstance@@QEAAPEAGXZ` | `0x7FF60` | 1,058 | UnwindData |  |
| 857 | `?GetMethodQualifier@CWbemInstance@@UEAAJPEBG0PEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x80390` | 105 | UnwindData |  |
| 858 | `?GetMethodQualifier@CWbemInstance@@UEAAJPEBG0PEAVCVar@@PEAJ2@Z` | `0x80400` | 105 | UnwindData |  |
| 897 | `?GetObjectQualifier@CInstancePart@@QEAAJPEBGPEAVCVar@@PEAJ@Z` | `0x80570` | 217 | UnwindData |  |
| 918 | `?GetPropQualifier@CWbemInstance@@UEAAJPEAVCPropertyInformation@@PEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x80650` | 483 | UnwindData |  |
| 953 | `?GetQualifier@CInstancePart@@QEAAJPEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x80840` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `?GetTransferArrayBlob@CWbemInstance@@QEAAJJPEAPEAEPEAJ@Z` | `0x80A20` | 343 | UnwindData |  |
| 1039 | `?GetTransferBlob@CWbemInstance@@QEAAJPEAJ0PEAPEAE@Z` | `0x80B80` | 274 | UnwindData |  |
| 1164 | `?IsValidObj@CWbemInstance@@UEAAJXZ` | `0x80CA0` | 283 | UnwindData |  |
| 1185 | `?MakeSubsetInst@CWbemInstance@@UEAAJPEAU_IWmiObject@@PEAPEAU2@@Z` | `0x81130` | 105 | UnwindData |  |
| 1209 | `?Merge@CWbemInstance@@UEAAJJKPEAXPEAPEAU_IWmiObject@@@Z` | `0x811A0` | 105 | UnwindData |  |
| 1212 | `?MergeAndDecorate@CWbemInstance@@UEAAJJKPEAXPEAG1PEAPEAU_IWmiObject@@@Z` | `0x81210` | 105 | UnwindData |  |
| 1274 | `?ReconcileWith@CWbemInstance@@UEAAJJPEAU_IWmiObject@@@Z` | `0x81370` | 105 | UnwindData |  |
| 1292 | `?ReduceQualifierSetSpace@CInstancePart@@UEAAXPEAVCBasicQualifierSet@@K@Z` | `0x814B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `?Reparent@CWbemInstance@@QEAAJPEAVCWbemClass@@PEAPEAV1@@Z` | `0x81550` | 812 | UnwindData |  |
| 1343 | `?SetClassPart@CWbemInstance@@UEAAJPEAXK@Z` | `0x81AB0` | 658 | UnwindData |  |
| 1392 | `?SetInstanceQualifier@CInstancePart@@QEAAJPEBGJPEAVCTypedValue@@@Z` | `0x81FC0` | 32 | UnwindData |  |
| 1393 | `?SetInstanceQualifier@CInstancePart@@QEAAJPEBGPEAVCVar@@J@Z` | `0x81FF0` | 352 | UnwindData |  |
| 1406 | `?SetMethodQualifier@CWbemInstance@@UEAAJPEBG0JPEAVCTypedValue@@@Z` | `0x82260` | 105 | UnwindData |  |
| 1407 | `?SetMethodQualifier@CWbemInstance@@UEAAJPEBG0JPEAVCVar@@@Z` | `0x822D0` | 105 | UnwindData |  |
| 1413 | `?SetObjectParts@CWbemInstance@@UEAAJPEAXKK@Z` | `0x82340` | 239 | UnwindData |  |
| 1421 | `?SetPropQualifier@CWbemInstance@@UEAAJPEBG0JPEAVCTypedValue@@@Z` | `0x82440` | 234 | UnwindData |  |
| 1422 | `?SetPropQualifier@CWbemInstance@@UEAAJPEBG0JPEAVCVar@@@Z` | `0x82530` | 523 | UnwindData |  |
| 1455 | `?SpawnDerivedClass@CWbemInstance@@UEAAJJPEAPEAUIWbemClassObject@@@Z` | `0x82750` | 105 | UnwindData |  |
| 1459 | `?SpawnKeyedInstance@CWbemInstance@@UEAAJJPEBGPEAPEAU_IWmiObject@@@Z` | `0x827C0` | 105 | UnwindData |  |
| 1510 | `?Update@CWbemInstance@@UEAAJPEAU_IWmiObject@@JPEAPEAU2@@Z` | `0x82920` | 105 | UnwindData |  |
| 1513 | `?Upgrade@CWbemInstance@@UEAAJPEAU_IWmiObject@@JPEAPEAU2@@Z` | `0x82990` | 349 | UnwindData |  |
| 1516 | `?Validate@CWbemInstance@@QEAAJXZ` | `0x82B00` | 244 | UnwindData |  |
| 1530 | `?ValidateBuffer@CWbemInstance@@SA_KPEAEHKAEAV?$vector@UEmbeddedObj@@V?$wbem_allocator@UEmbeddedObj@@@@@std@@@Z` | `0x82C00` | 287 | UnwindData |  |
| 413 | `?CanBeReconciledWith@CMethodPart@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x83AE0` | 400 | UnwindData |  |
| 488 | `?CompareTo@CMethodPart@@QEAAJJAEAV1@@Z` | `0x83C80` | 245 | UnwindData |  |
| 585 | `?DeleteMethod@CMethodPart@@QEAAJPEBG@Z` | `0x83D80` | 652 | UnwindData |  |
| 595 | `?DeleteSignature@CMethodPart@@IEAAXHH@Z` | `0x84020` | 88 | UnwindData |  |
| 1155 | `?IsTouched@CMethodPart@@QEAAHPEBGPEAH@Z` | `0x84080` | 128 | UnwindData |  |
| 1271 | `?ReconcileWith@CMethodPart@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x84110` | 130 | UnwindData |  |
| 1400 | `?SetMethodOrigin@CMethodPart@@QEAAJPEBGJ@Z` | `0x841A0` | 60 | UnwindData |  |
| 1506 | `?Update@CMethodPart@@SAJAEAV1@0J@Z` | `0x841F0` | 495 | UnwindData |  |
| 387 | `?AppendArrayPropRangeByHandle@CWbemObject@@UEAAJJJKKPEAX@Z` | `0x84520` | 539 | UnwindData |  |
| 388 | `?AppendQualifierArrayRange@CWbemObject@@QEAAJPEBG0HJJKKPEAX@Z` | `0x84750` | 794 | UnwindData |  |
| 397 | `?BeginEnumerationEx@CWbemObject@@UEAAJJJ@Z` | `0x84A70` | 307 | UnwindData |  |
| 401 | `?CIMTYPEToVARTYPE@CWbemObject@@UEAAJJPEAG@Z` | `0x84BB0` | 28 | UnwindData |  |
| 438 | `?CheckBooleanPropQual@CWbemObject@@QEAAHPEBG0@Z` | `0x84BE0` | 182 | UnwindData |  |
| 475 | `?CompareClassParts@CWbemObject@@UEAAJPEAUIWbemClassObject@@J@Z` | `0x84CA0` | 573 | UnwindData |  |
| 605 | `?EnabledValidateObject@CWbemObject@@KAJPEAV1@@Z` | `0x84F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | `?FindMethod@CWbemObject@@UEAAJPEBG@Z` | `0x84F30` | 105 | UnwindData |  |
| 687 | `?GetArrayPropElementByHandle@CWbemObject@@UEAAJJJKPEAK0PEAPEAX@Z` | `0x84FA0` | 753 | UnwindData |  |
| 688 | `?GetArrayPropInfoByHandle@CWbemObject@@UEAAJJJPEAPEAGPEAJPEAK@Z` | `0x852A0` | 411 | UnwindData |  |
| 689 | `?GetArrayPropRangeByHandle@CWbemObject@@UEAAJJJKKKPEAK0PEAX@Z` | `0x85450` | 731 | UnwindData |  |
| 690 | `?GetArrayPropertyHandle@CWbemObject@@QEAAJPEBGPEAJ1@Z` | `0x85740` | 71 | UnwindData |  |
| 709 | `?GetClassIndex@CWbemObject@@QEAAKPEBG@Z` | `0x85790` | 41 | UnwindData |  |
| 710 | `?GetClassInternal@CWbemObject@@QEAAPEAVCCompressedString@@XZ` | `0x857C0` | 31 | UnwindData |  |
| 753 | `?GetGUID@CWbemObject@@UEAAJPEAU_GUID@@@Z` | `0x857F0` | 125 | UnwindData |  |
| 772 | `?GetHeapPtrByHandle@CWbemObject@@QEAAKJ@Z` | `0x85880` | 121 | UnwindData |  |
| 773 | `?GetHelpContext@CWbemObject@@UEAAJPEAK@Z` | `0x85900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 774 | `?GetHelpFile@CWbemObject@@UEAAJPEAPEAG@Z` | `0x85910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `?GetKeyOrigin@CWbemObject@@UEAAJJKPEAKPEAG@Z` | `0x85920` | 433 | UnwindData |  |
| 804 | `?GetKeyString@CWbemObject@@UEAAJJPEAPEAG@Z` | `0x85AE0` | 482 | UnwindData |  |
| 854 | `?GetMethodQual@CWbemObject@@UEAAJPEBG0JKPEAJPEAK2PEAX@Z` | `0x85CD0` | 599 | UnwindData |  |
| 893 | `?GetObjQual@CWbemObject@@UEAAJPEBGJKPEAJPEAK2PEAX@Z` | `0x85F30` | 597 | UnwindData |  |
| 904 | `?GetParentClassFromBlob@CWbemObject@@UEAAJJKPEAXPEAPEAG@Z` | `0x86190` | 105 | UnwindData |  |
| 933 | `?GetPropertyIndex@CWbemObject@@QEAAJPEBGPEAH@Z` | `0x86200` | 106 | UnwindData |  |
| 935 | `?GetPropertyInfoByHandle@CWbemObject@@UEAAJJPEAPEAGPEAJ@Z` | `0x86270` | 69 | UnwindData |  |
| 937 | `?GetPropertyNameFromIndex@CWbemObject@@QEAAJHPEAPEAG@Z` | `0x862C0` | 244 | UnwindData |  |
| 963 | `?GetQualifierArrayInfo@CWbemObject@@QEAAJPEBG0HJPEAJPEAK@Z` | `0x863C0` | 320 | UnwindData |  |
| 964 | `?GetQualifierArrayRange@CWbemObject@@QEAAJPEBG0HJKKKPEAK1PEAX@Z` | `0x86510` | 501 | UnwindData |  |
| 994 | `?GetServerAndNamespace@CWbemObject@@QEAAJPEAVCVar@@@Z` | `0x86710` | 368 | UnwindData |  |
| 1061 | `?HasRefs@CWbemObject@@QEAAHXZ` | `0x86890` | 115 | UnwindData |  |
| 1147 | `?IsSameClass@CWbemObject@@QEAAHPEAV1@@Z` | `0x86910` | 190 | UnwindData |  |
| 1166 | `?IsValidPropertyHandle@CWbemObject@@QEAAJJ@Z` | `0x869E0` | 38 | UnwindData |  |
| 1172 | `?LocalizeProperties@CWbemObject@@IEAAJH_NPEAUIWbemClassObject@@1AEA_N@Z` | `0x86A10` | 707 | UnwindData |  |
| 1173 | `?LocalizeQualifiers@CWbemObject@@IEAAJH_NPEAUIWbemQualifierSet@@1AEA_N@Z` | `0x86CE0` | 691 | UnwindData |  |
| 1210 | `?MergeAmended@CWbemObject@@UEAAJJPEAU_IWmiObject@@@Z` | `0x86FA0` | 1,836 | UnwindData |  |
| 1244 | `?QueryPropertyFlags@CWbemObject@@UEAAJJPEBG_KPEA_K@Z` | `0x876E0` | 306 | UnwindData |  |
| 1310 | `?ReleaseMarshalData@CWbemObject@@UEAAJPEAUIStream@@@Z` | `0x878A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1489 | `?UnmarshalInterface@CWbemObject@@UEAAJPEAUIStream@@AEBU_GUID@@PEAPEAX@Z` | `0x878A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `?RemoveArrayPropElementByHandle@CWbemObject@@UEAAJJJK@Z` | `0x878B0` | 33 | UnwindData |  |
| 1314 | `?RemoveArrayPropRangeByHandle@CWbemObject@@UEAAJJJKK@Z` | `0x878E0` | 593 | UnwindData |  |
| 1316 | `?RemoveDecoration@CWbemObject@@UEAAJXZ` | `0x87B40` | 71 | UnwindData |  |
| 1320 | `?RemoveQualifierArrayRange@CWbemObject@@QEAAJPEBG0HJKK@Z` | `0x87B90` | 622 | UnwindData |  |
| 1337 | `?SetArrayPropElementByHandle@CWbemObject@@UEAAJJJKKPEAX@Z` | `0x87E10` | 53 | UnwindData |  |
| 1403 | `?SetMethodQual@CWbemObject@@UEAAJPEBG0JKKJKPEAX@Z` | `0x87E50` | 645 | UnwindData |  |
| 1409 | `?SetObjQual@CWbemObject@@UEAAJPEBGJKKJKPEAX@Z` | `0x880E0` | 621 | UnwindData |  |
| 1410 | `?SetObjectFlags@CWbemObject@@UEAAJJ_K0@Z` | `0x88360` | 179 | UnwindData |  |
| 1411 | `?SetObjectMemory@CWbemObject@@UEAAJPEAXK@Z` | `0x88420` | 248 | UnwindData |  |
| 1416 | `?SetPropQual@CWbemObject@@UEAAJPEBG0JKKJKPEAX@Z` | `0x88520` | 642 | UnwindData |  |
| 1432 | `?SetQualifierArrayRange@CWbemObject@@QEAAJPEBG0HJKJKKKPEAX@Z` | `0x887B0` | 1,019 | UnwindData |  |
| 1436 | `?SetServerNamespace@CWbemObject@@UEAAJPEBG0@Z` | `0x88BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `?Unmerge@CWbemObject@@QEAAKPEAPEAE@Z` | `0x88BE0` | 383 | UnwindData |  |
| 1536 | `?ValidatePath@CWbemObject@@QEAAJPEAUParsedObjectPath@@@Z` | `0x88D70` | 856 | UnwindData |  |
| 837 | `?GetMapped@CLimitationMapping@@QEAAGG@Z` | `0x89150` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `?RemoveProperty@CDataTable@@QEAAXGKK@Z` | `0x89250` | 292 | UnwindData |  |
| 1533 | `?ValidateInstance@CLimitationMapping@@QEAAJPEAVCWbemInstance@@@Z` | `0x89380` | 206 | UnwindData |  |
| 368 | `?AddQualifierConflicts@CQualifierSet@@IEAAJAEAVCVarVector@@@Z` | `0x894C0` | 718 | UnwindData |  |
| 481 | `?CompareLocalizedSet@CBasicQualifierSet@@QEAAHAEAV1@@Z` | `0x89880` | 869 | UnwindData |  |
| 519 | `?CopyLocalQualifiers@CQualifierSet@@QEAAJAEAV1@@Z` | `0x89BF0` | 690 | UnwindData |  |
| 581 | `?Delete@CQualifierSet@@UEAAJPEBG@Z` | `0x89EF0` | 1,272 | UnwindData |  |
| 593 | `?DeleteQualifier@CQualifierSet@@QEAAJPEBGH@Z` | `0x8A3F0` | 305 | UnwindData |  |
| 594 | `?DeleteQualifierSet@CQualifierSetList@@QEAAXH@Z` | `0x8A530` | 138 | UnwindData |  |
| 955 | `?GetQualifier@CQualifierSet@@QEAAJPEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x8A5C0` | 325 | UnwindData |  |
| 1079 | `?InsertQualifierSet@CQualifierSetList@@QEAAJH@Z` | `0x8A710` | 481 | UnwindData |  |
| 1294 | `?ReduceQualifierSetSpace@CQualifierSetList@@QEAAXPEAVCBasicQualifierSet@@K@Z` | `0x8A900` | 90 | UnwindData |  |
| 1464 | `?StoreQualifierConflicts@CQualifierSet@@IEAAJPEBGAEAVCVar@@AEAVCQualifierFlavor@@AEAVCVarVector@@@Z` | `0x8A960` | 631 | UnwindData |  |
| 1539 | `?ValidateSet@CQualifierSet@@QEAAJPEBGEPEAVCTypedValue@@HH@Z` | `0x8ABE0` | 2,244 | UnwindData |  |
| 469 | `?Compare@CCompressedString@@QEBAHAEBV1@@Z` | `0x8B4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `?Compare@CCompressedString@@QEBAHPEBD@Z` | `0x8B4D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `?Compare@CCompressedString@@QEBAHPEBG@Z` | `0x8B510` | 65 | UnwindData |  |
| 495 | `?ComputeNecessarySpace@CCompressedString@@SAHPEBD@Z` | `0x8B560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `?CreateEmpty@CCompressedString@@SAPEAEPEAE@Z` | `0x8B580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `?MakeLowercase@CCompressedString@@QEAAXXZ` | `0x8B590` | 68 | UnwindData |  |
| 1382 | `?SetFromAscii@CCompressedString@@QEAAXPEBD_K@Z` | `0x8B5E0` | 66 | UnwindData |  |
| 389 | `?AppendRange@CUntypedArray@@SAJPEAVCPtrSource@@KKPEAVCFastHeap@@KKPEAX@Z` | `0x8B630` | 624 | UnwindData |  |
| 442 | `?CheckIntervalDateTime@CUntypedArray@@SAHAEAVCVarVector@@@Z` | `0x8B8B0` | 161 | UnwindData |  |
| 445 | `?CheckRangeSizeForGet@CUntypedArray@@KAJKKKKPEAK@Z` | `0x8B9F0` | 202 | UnwindData |  |
| 980 | `?GetRange@CUntypedArray@@SAJPEAVCPtrSource@@KKPEAVCFastHeap@@KKKPEAKPEAX@Z` | `0x8BAC0` | 661 | UnwindData |  |
| 1194 | `?MarshalPacket@CWbemMtgtDeliverEventPacket@@QEAAJPEAEKJPEAPEAUIWbemClassObject@@PEAU_GUID@@PEAH@Z` | `0x8C2F0` | 64 | UnwindData |  |
| 88 | `??0CWbemMtgtDeliverEventPacket@@QEAA@PEAEK_N@Z` | `0x8C740` | 32 | UnwindData |  |
| 404 | `?CalculateLength@CWbemMtgtDeliverEventPacket@@QEAAJJPEAPEAUIWbemClassObject@@PEAKAEAVCWbemClassToIdMap@@PEAU_GUID@@PEAH@Z` | `0x8C770` | 184 | UnwindData |  |
| 1193 | `?MarshalPacket@CWbemMtgtDeliverEventPacket@@QEAAJJPEAPEAUIWbemClassObject@@PEAU_GUID@@PEAH@Z` | `0x8C830` | 249 | UnwindData |  |
| 1196 | `?MarshalPacket@CWbemObjectArrayPacket@@QEAAJPEAEKJPEAPEAUIWbemClassObject@@PEAU_GUID@@PEAH@Z` | `0x8C930` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1368 | `?SetData@CWbemMtgtDeliverEventPacket@@QEAAXPEAEK_N@Z` | `0x8C960` | 422 | UnwindData |  |
| 1490 | `?UnmarshalPacket@CWbemMtgtDeliverEventPacket@@QEAAJAEAJAEAPEAPEAUIWbemClassObject@@AEAVCWbemClassCache@@@Z` | `0x8CB10` | 416 | UnwindData |  |
| 1 | `??0?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@QEAA@AEBV0@@Z` | `0x8CE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@QEAA@AEBV0@@Z` | `0x8CE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@QEAA@AEBV0@@Z` | `0x8CE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@QEAA@AEBV0@@Z` | `0x8CE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@QEAA@AEBV0@@Z` | `0x8CE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@QEAA@AEBV0@@Z` | `0x8CE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@QEAA@AEBV0@@Z` | `0x8CE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??0?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAA@AEAV0@@Z` | `0x8CE80` | 36 | UnwindData |  |
| 17 | `??0?$CRefedPointerArray@VCWmiTextSource@@@@QEAA@AEAV0@@Z` | `0x8CEB0` | 29 | UnwindData |  |
| 71 | `??0CWbemCallSecurity@@QEAA@AEBV0@@Z` | `0x8CF20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `??0CWbemEnumMarshaling@@QEAA@AEBV0@@Z` | `0x8CF70` | 119 | UnwindData |  |
| 81 | `??0CWbemFetchRefrMgr@@QEAA@AEBV0@@Z` | `0x8CFF0` | 73 | UnwindData |  |
| 83 | `??0CWbemGuidToClassMap@@QEAA@AEBV0@@Z` | `0x8D040` | 66 | UnwindData |  |
| 92 | `??0CWbemRefreshingSvc@@QEAA@AEBV0@@Z` | `0x8D090` | 111 | UnwindData |  |
| 98 | `??0CWmiObjectFactory@@QEAA@AEBV0@@Z` | `0x8D110` | 73 | UnwindData |  |
| 100 | `??0CWmiTextSourceArray@@QEAA@AEAV0@@Z` | `0x8D160` | 29 | UnwindData |  |
| 103 | `??0XCfgRefrSrvc@CWbemRefreshingSvc@@QEAA@$$QEAV01@@Z` | `0x8D190` | 39 | UnwindData |  |
| 104 | `??0XCfgRefrSrvc@CWbemRefreshingSvc@@QEAA@AEBV01@@Z` | `0x8D190` | 39 | UnwindData |  |
| 106 | `??0XEnumMarshaling@CWbemEnumMarshaling@@QEAA@$$QEAV01@@Z` | `0x8D1C0` | 39 | UnwindData |  |
| 107 | `??0XEnumMarshaling@CWbemEnumMarshaling@@QEAA@AEBV01@@Z` | `0x8D1C0` | 39 | UnwindData |  |
| 109 | `??0XFetchRefrMgr@CWbemFetchRefrMgr@@QEAA@$$QEAV01@@Z` | `0x8D1F0` | 39 | UnwindData |  |
| 110 | `??0XFetchRefrMgr@CWbemFetchRefrMgr@@QEAA@AEBV01@@Z` | `0x8D1F0` | 39 | UnwindData |  |
| 112 | `??0XObjectFactory@CWmiObjectFactory@@QEAA@$$QEAV01@@Z` | `0x8D220` | 39 | UnwindData |  |
| 113 | `??0XObjectFactory@CWmiObjectFactory@@QEAA@AEBV01@@Z` | `0x8D220` | 39 | UnwindData |  |
| 115 | `??0XObjectTextSrc@CWmiObjectTextSrc@@QEAA@$$QEAV01@@Z` | `0x8D250` | 39 | UnwindData |  |
| 116 | `??0XObjectTextSrc@CWmiObjectTextSrc@@QEAA@AEBV01@@Z` | `0x8D250` | 39 | UnwindData |  |
| 118 | `??0XWbemRefrSvc@CWbemRefreshingSvc@@QEAA@$$QEAV01@@Z` | `0x8D280` | 39 | UnwindData |  |
| 119 | `??0XWbemRefrSvc@CWbemRefreshingSvc@@QEAA@AEBV01@@Z` | `0x8D280` | 39 | UnwindData |  |
| 121 | `??0XWbemRemoteRefr@CWbemRemoteRefresher@@QEAA@$$QEAV01@@Z` | `0x8D2B0` | 39 | UnwindData |  |
| 122 | `??0XWbemRemoteRefr@CWbemRemoteRefresher@@QEAA@AEBV01@@Z` | `0x8D2B0` | 39 | UnwindData |  |
| 123 | `??0XWbemRemoteRefr@CWbemRemoteRefresher@@QEAA@PEAV1@@Z` | `0x8D2E0` | 39 | UnwindData |  |
| 169 | `??4?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@QEAAAEAV0@AEBV0@@Z` | `0x8D310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `??4?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@QEAAAEAV0@AEBV0@@Z` | `0x8D310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `??4?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@QEAAAEAV0@AEBV0@@Z` | `0x8D310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `??4?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@QEAAAEAV0@AEBV0@@Z` | `0x8D310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `??4?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@QEAAAEAV0@AEBV0@@Z` | `0x8D310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `??4?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@QEAAAEAV0@AEBV0@@Z` | `0x8D310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `??4?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@QEAAAEAV0@AEBV0@@Z` | `0x8D310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `??4?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAAEAV0@AEAV0@@Z` | `0x8D330` | 31 | UnwindData |  |
| 177 | `??4?$CRefedPointerArray@VCWmiTextSource@@@@QEAAAEAV0@$$QEAV0@@Z` | `0x8D330` | 31 | UnwindData |  |
| 178 | `??4?$CRefedPointerArray@VCWmiTextSource@@@@QEAAAEAV0@AEAV0@@Z` | `0x8D330` | 31 | UnwindData |  |
| 258 | `??4CWmiTextSourceArray@@QEAAAEAV0@AEAV0@@Z` | `0x8D330` | 31 | UnwindData |  |
| 249 | `??4CWbemEnumMarshaling@@QEAAAEAV0@AEBV0@@Z` | `0x8D360` | 171 | UnwindData |  |
| 250 | `??4CWbemFetchRefrMgr@@QEAAAEAV0@AEBV0@@Z` | `0x8D420` | 56 | UnwindData |  |
| 257 | `??4CWmiObjectFactory@@QEAAAEAV0@AEBV0@@Z` | `0x8D420` | 56 | UnwindData |  |
| 251 | `??4CWbemGuidToClassMap@@QEAAAEAV0@AEBV0@@Z` | `0x8D460` | 99 | UnwindData |  |
| 254 | `??4CWbemRefreshingSvc@@QEAAAEAV0@AEBV0@@Z` | `0x8D4D0` | 93 | UnwindData |  |
| 263 | `??4XCfgRefrSrvc@CWbemRefreshingSvc@@QEAAAEAV01@$$QEAV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 264 | `??4XCfgRefrSrvc@CWbemRefreshingSvc@@QEAAAEAV01@AEBV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 265 | `??4XEnumMarshaling@CWbemEnumMarshaling@@QEAAAEAV01@$$QEAV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 266 | `??4XEnumMarshaling@CWbemEnumMarshaling@@QEAAAEAV01@AEBV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 267 | `??4XFetchRefrMgr@CWbemFetchRefrMgr@@QEAAAEAV01@$$QEAV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 268 | `??4XFetchRefrMgr@CWbemFetchRefrMgr@@QEAAAEAV01@AEBV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 269 | `??4XObjectFactory@CWmiObjectFactory@@QEAAAEAV01@$$QEAV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 270 | `??4XObjectFactory@CWmiObjectFactory@@QEAAAEAV01@AEBV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 271 | `??4XObjectTextSrc@CWmiObjectTextSrc@@QEAAAEAV01@$$QEAV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 272 | `??4XObjectTextSrc@CWmiObjectTextSrc@@QEAAAEAV01@AEBV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 273 | `??4XWbemRefrSvc@CWbemRefreshingSvc@@QEAAAEAV01@$$QEAV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 274 | `??4XWbemRefrSvc@CWbemRefreshingSvc@@QEAAAEAV01@AEBV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 275 | `??4XWbemRemoteRefr@CWbemRemoteRefresher@@QEAAAEAV01@$$QEAV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 276 | `??4XWbemRemoteRefr@CWbemRemoteRefresher@@QEAAAEAV01@AEBV01@@Z` | `0x8D540` | 24 | UnwindData |  |
| 349 | `??_F?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXXZ` | `0x8D560` | 1,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `?Discard@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXH@Z` | `0x8DBD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `?GetArrayPtr@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAPEAPEAVCWmiTextSource@@XZ` | `0x8DBF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `?GetHandleType@CWbemThreadSecurityHandle@@UEAAJPEAK@Z` | `0x8DC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1033 | `?GetTokenOrigin@CWbemThreadSecurityHandle@@UEAAJPEAW4tag_WMI_THREAD_SECURITY_ORIGIN@@@Z` | `0x8DC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `?InsertAt@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAA_NHPEAVCWmiTextSource@@@Z` | `0x8DC30` | 46 | UnwindData |  |
| 1315 | `?RemoveAt@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAA_NHPEAPEAVCWmiTextSource@@@Z` | `0x8E100` | 117 | UnwindData |  |
| 1339 | `?SetAt@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXHPEAVCWmiTextSource@@PEAPEAV2@@Z` | `0x8E180` | 131 | UnwindData |  |
| 1441 | `?SetSize@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXH@Z` | `0x8E210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1469 | `?Swap@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXHH@Z` | `0x8E230` | 120 | UnwindData |  |
| 1478 | `?Trim@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXXZ` | `0x8E2B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1481 | `?UnbindPtr@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAPEAPEAVCWmiTextSource@@XZ` | `0x8E2D0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1572 | `GetObjectCount` | `0x8E6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1484 | `?Uninit@CWbemFetchRefrMgr@@QEAAJXZ` | `0x8E6B0` | 102 | UnwindData |  |
| 1485 | `?Uninit@XFetchRefrMgr@CWbemFetchRefrMgr@@UEAAJXZ` | `0x8E720` | 22,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `?AddObjectToRefresherByTemplate@CWbemRefreshingSvc@@MEAAJPEAU_WBEM_REFRESHER_ID@@PEAUIWbemClassObject@@JPEAUIWbemContext@@KPEAU_WBEM_REFRESH_INFO@@PEAK@Z` | `0x93E20` | 462 | UnwindData |  |
| 364 | `?AddObjectToRefresherByTemplate@XWbemRefrSvc@CWbemRefreshingSvc@@UEAAJPEAU_WBEM_REFRESHER_ID@@PEAUIWbemClassObject@@JPEAUIWbemContext@@KPEAU_WBEM_REFRESH_INFO@@PEAK@Z` | `0x94000` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `?GetGuid@XWbemRemoteRefr@CWbemRemoteRefresher@@UEAAJJPEAU_GUID@@@Z` | `0x94120` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `?GetRemoteRefresher@CWbemRefreshingSvc@@MEAAJPEAU_WBEM_REFRESHER_ID@@JKPEAPEAUIWbemRemoteRefresher@@PEAU_GUID@@PEAK@Z` | `0x94180` | 564 | UnwindData |  |
| 990 | `?GetRemoteRefresher@XWbemRefrSvc@CWbemRefreshingSvc@@UEAAJPEAU_WBEM_REFRESHER_ID@@JKPEAPEAUIWbemRemoteRefresher@@PEAU_GUID@@PEAK@Z` | `0x943C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1275 | `?ReconnectRemoteRefresher@CWbemRefreshingSvc@@MEAAJPEAU_WBEM_REFRESHER_ID@@JJKPEAU_WBEM_RECONNECT_INFO@@PEAU_WBEM_RECONNECT_RESULTS@@PEAK@Z` | `0x943D0` | 856 | UnwindData |  |
| 1276 | `?ReconnectRemoteRefresher@XWbemRefrSvc@CWbemRefreshingSvc@@UEAAJPEAU_WBEM_REFRESHER_ID@@JJKPEAU_WBEM_RECONNECT_INFO@@PEAU_WBEM_RECONNECT_RESULTS@@PEAK@Z` | `0x94730` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `?RemoteRefresh@XWbemRemoteRefr@CWbemRemoteRefresher@@UEAAJJPEAJPEAPEAU_WBEM_REFRESHED_OBJECT@@@Z` | `0x94860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `?RemoveObjectFromRefresher@CWbemRefreshingSvc@@MEAAJPEAU_WBEM_REFRESHER_ID@@JJKPEAK@Z` | `0x94870` | 303 | UnwindData |  |
| 1318 | `?RemoveObjectFromRefresher@XWbemRefrSvc@CWbemRefreshingSvc@@UEAAJPEAU_WBEM_REFRESHER_ID@@JJKPEAK@Z` | `0x949B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `?ResetRefreshInfo@CWbemRefreshingSvc@@IEAAJPEAU_WBEM_REFRESH_INFO@@@Z` | `0x949C0` | 121 | UnwindData |  |
| 1461 | `?StopRefreshing@XWbemRemoteRefr@CWbemRemoteRefresher@@UEAAJJPEAJJ@Z` | `0x94B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1544 | `?WrapRemoteRefresher@CWbemRefreshingSvc@@IEAAJPEAPEAUIWbemRemoteRefresher@@@Z` | `0x94B70` | 322 | UnwindData |  |
| 78 | `??0CWbemDataPacket@@QEAA@PEAEK_N@Z` | `0x97F70` | 24 | UnwindData |  |
| 215 | `??4CInternalString@@QEAAHPEBG@Z` | `0x98140` | 155 | UnwindData |  |
| 531 | `?Create@CWmiObjectFactory@@QEAAJPEAUIUnknown@@KAEBU_GUID@@1PEAPEAX@Z` | `0x99090` | 579 | UnwindData |  |
| 532 | `?Create@XObjectFactory@CWmiObjectFactory@@UEAAJPEAUIUnknown@@KAEBU_GUID@@1PEAPEAX@Z` | `0x992E0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `?CreateFromText@XObjectTextSrc@CWmiObjectTextSrc@@UEAAJJPEAGKPEAUIWbemContext@@PEAPEAUIWbemClassObject@@@Z` | `0x994B0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `??4CWbemCallSecurity@@QEAAAEAV0@AEBV0@@Z` | `0x996F0` | 153 | UnwindData |  |
| 697 | `?GetAuthentication@CWbemCallSecurity@@QEAAJPEAK@Z` | `0x99830` | 134 | UnwindData |  |
| 700 | `?GetAuthenticationLuid@CWbemCallSecurity@@UEAAJPEAX@Z` | `0x999C0` | 289 | UnwindData |  |
| 701 | `?GetAuthenticationLuid@CWbemThreadSecurityHandle@@UEAAJPEAX@Z` | `0x99AF0` | 126 | UnwindData |  |
| 777 | `?GetImpersonation@CWbemCallSecurity@@UEAAJPEAK@Z` | `0x99B80` | 324 | UnwindData |  |
| 778 | `?GetImpersonation@CWbemThreadSecurityHandle@@UEAAJPEAK@Z` | `0x99CD0` | 233 | UnwindData |  |
| 1032 | `?GetToken@CWbemThreadSecurityHandle@@UEAAJPEAPEAX@Z` | `0x9A0C0` | 263 | UnwindData |  |
| 1043 | `?GetUser@CWbemCallSecurity@@UEAAJPEAKPEAG@Z` | `0x9A4E0` | 305 | UnwindData |  |
| 1044 | `?GetUser@CWbemThreadSecurityHandle@@UEAAJPEAKPEAG@Z` | `0x9A620` | 126 | UnwindData |  |
| 1045 | `?GetUserSid@CWbemCallSecurity@@UEAAJPEAKPEAX@Z` | `0x9A840` | 305 | UnwindData |  |
| 1046 | `?GetUserSid@CWbemThreadSecurityHandle@@UEAAJPEAKPEAX@Z` | `0x9A980` | 126 | UnwindData |  |
| 1217 | `?New@CWbemThreadSecurityHandle@@SAPEAV1@XZ` | `0x9AA10` | 50 | UnwindData |  |
| 1570 | `DllRegisterServer` | `0x9DE00` | 412 | UnwindData |  |
| 1571 | `DllUnregisterServer` | `0x9DFB0` | 452 | UnwindData |  |
| 297 | `??_7CClassAndMethods@@6BCClassPartContainer@@@` | `0xAD118` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `??_7CClassAndMethods@@6BCMethodPartContainer@@@` | `0xAD130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `??_7CMethodPart@@6B@` | `0xAD150` | 104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `??_7CClassQualifierSet@@6B@` | `0xAD1B8` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `??_7CInstanceQualifierSet@@6B@` | `0xAD1B8` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `??_7CInstancePQSContainer@@6B@` | `0xAD218` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `??_7CQualifierSet@@6B@` | `0xAD2C8` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `??_7CClassPartContainer@@6B@` | `0xAD380` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `??_7CWbemClass@@6BIMarshal@@@` | `0xAD398` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `??_7CWbemInstance@@6BIMarshal@@@` | `0xAD398` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `??_7CWbemObject@@6BIMarshal@@@` | `0xAD398` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `??_7CWbemInstance@@6B_IWmiObject@@@` | `0xAD3E0` | 1,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `??_7CWbemInstance@@6BCInstancePartContainer@@@` | `0xAD868` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `??_7CInstancePart@@6BCQualifierSetListContainer@@@` | `0xAD888` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `??_7CInstancePartContainer@@6B@` | `0xAD8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `??_7CMethodPartContainer@@6B@` | `0xAD8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `??_7CClassPart@@6BCHeapContainer@@@` | `0xAD8D0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `??_7CWbemInstance@@6BIWbemConstructClassObject@@@` | `0xAD8E8` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `??_7CWbemClass@@6BIWbemPropertySource@@@` | `0xAD920` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `??_7CWbemInstance@@6BIWbemPropertySource@@@` | `0xAD920` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `??_7CWbemObject@@6BIWbemPropertySource@@@` | `0xAD920` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `??_7CInstancePart@@6BCHeapContainer@@@` | `0xAD948` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `??_7CQualifierSetListContainer@@6B@` | `0xAD960` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `??_7CClassPart@@6BCQualifierSetContainer@@@` | `0xAD988` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `??_7CClassPart@@6BCDataTableContainer@@@` | `0xAD9D8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `??_7CWbemClass@@6BIErrorInfo@@@` | `0xAD9F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `??_7CWbemInstance@@6BIErrorInfo@@@` | `0xAD9F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `??_7CWbemObject@@6BIErrorInfo@@@` | `0xAD9F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `??_7CWbemInstance@@6BCClassPartContainer@@@` | `0xADA30` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `??_7CInstancePart@@6BCQualifierSetContainer@@@` | `0xADA48` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `??_7CInstancePart@@6BCDataTableContainer@@@` | `0xADA98` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `??_7CClassPart@@6BCPropertyTableContainer@@@` | `0xADAB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `??_7CWbemClass@@6BIWbemConstructClassObject@@@` | `0xADB10` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `??_7CWbemClass@@6B_IWmiObject@@@` | `0xADB48` | 4,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `??_7CWbemObject@@6BIWbemConstructClassObject@@@` | `0xAEC68` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `??_7CWbemObject@@6B_IWmiObject@@@` | `0xAECA0` | 1,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `??_7CWbemCallSecurity@@6B_IWmiCallSec@@@` | `0xAF128` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `??_7CWbemCallSecurity@@6BIServerSecurity@@@` | `0xAF170` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `??_7CWbemThreadSecurityHandle@@6B@` | `0xAF1A8` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `??_7CMethodQualifierSet@@6B@` | `0xAF208` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `??_7CMethodQualifierSetContainer@@6B@` | `0xAF268` | 264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `??_7?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@6B@` | `0xAF370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `??_7?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@6B@` | `0xAF370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `??_7?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@6B@` | `0xAF370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `??_7CWbemEnumMarshaling@@6B@` | `0xAF390` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `??_7XEnumMarshaling@CWbemEnumMarshaling@@6B@` | `0xAF490` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `??_7XCfgRefrSrvc@CWbemRefreshingSvc@@6B@` | `0xAF530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `??_7XWbemRefrSvc@CWbemRefreshingSvc@@6B@` | `0xAF550` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `??_7CWbemRefreshingSvc@@6B@` | `0xAF5D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `??_7?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@6B@` | `0xAF640` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `??_7CWmiObjectFactory@@6B@` | `0xAF6E8` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `??_7XObjectFactory@CWmiObjectFactory@@6B@` | `0xAF720` | 136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `??_7XFetchRefrMgr@CWbemFetchRefrMgr@@6B@` | `0xAF7A8` | 216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `??_7CWbemFetchRefrMgr@@6B@` | `0xAF880` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `??_7?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@6B@` | `0xAF8B8` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `??_7?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@6B@` | `0xAF8B8` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `??_7XObjectTextSrc@CWmiObjectTextSrc@@6B@` | `0xAF8E8` | 328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `??_7?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@6B@` | `0xAFA30` | 3,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `??_7XWbemRemoteRefr@CWbemRemoteRefresher@@6B@` | `0xB0650` | 215,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1566 | `?s_pszStartingCharsLCase@CReservedWordTable@@0PEBGEB` | `0xE5020` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1567 | `?s_pszStartingCharsUCase@CReservedWordTable@@0PEBGEB` | `0xE5028` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1563 | `?s_apwszReservedWords@CReservedWordTable@@0PAPEBGA` | `0xE5030` | 1,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1562 | `?s_abSignature@CWbemDataPacket@@1PAEA` | `0xE5428` | 2,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1565 | `?s_pRefrMgr@CWbemFetchRefrMgr@@1PEAU_IWbemRefresherMgr@@EA` | `0xE5E58` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1564 | `?s_cs@CWbemFetchRefrMgr@@1VCStaticCritSec@@A` | `0xE5EF0` | 0 | Indeterminate |  |
