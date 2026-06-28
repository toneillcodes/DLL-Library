# Binary Specification: fastprox.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\fastprox.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `271c396438319bd993ca3fd2d2fc3aec01985634f3bd8484f05942daae50206c`
* **Total Exported Functions:** 1572

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 674 | `?Get@CWbemObject@@UEAAJPEBGJPEAUtagVARIANT@@PEAJ2@Z` | `0x1300` | 934 | UnwindData |  |
| 686 | `?GetArrayPropAddrByHandle@CWbemObject@@UEAAJJJPEAKPEAPEAX@Z` | `0x16B0` | 456 | UnwindData |  |
| 685 | `?GetArrayByHandle@CWbemObject@@QEAAPEAVCUntypedArray@@J@Z` | `0x1880` | 190 | UnwindData |  |
| 1226 | `?Put@CWbemInstance@@UEAAJPEBGJPEAUtagVARIANT@@J@Z` | `0x24C0` | 837 | UnwindData |  |
| 1247 | `?ReadPropertyValue@CWbemObject@@UEAAJJJPEAJPEAE@Z` | `0x2810` | 1,124 | UnwindData |  |
| 602 | `?ElementMaxSize@CFastHeap@@QEAAHK@Z` | `0x2C80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1015 | `?GetStringLength@CCompressedString@@QEBAHXZ` | `0x2CB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 900 | `?GetObjectW@CWbemClassCache@@QEAAJAEAU_GUID@@PEAPEAUIWbemClassObject@@@Z` | `0x2D30` | 342 | UnwindData |  |
| 1245 | `?ReadDWORD@CWbemObject@@UEAAJJPEAK@Z` | `0x2E90` | 542 | UnwindData |  |
| 733 | `?GetDefaultByHandle@CClassPart@@QEAAJJJPEAJPEAE@Z` | `0x30C0` | 232 | UnwindData |  |
| 489 | `?CompareTo@CQualifierSet@@UEAAJJPEAUIWbemQualifierSet@@@Z` | `0x3230` | 1,719 | UnwindData |  |
| 95 | `??0CWbemSmartEnumNextPacket@@QEAA@PEAEK_N@Z` | `0x4D30` | 32 | UnwindData |  |
| 1370 | `?SetData@CWbemSmartEnumNextPacket@@QEAAXPEAEK_N@Z` | `0x4D60` | 614 | UnwindData |  |
| 1365 | `?SetData@CWbemDataPacket@@QEAAXPEAEK_N@Z` | `0x4FD0` | 184 | UnwindData |  |
| 1492 | `?UnmarshalPacket@CWbemSmartEnumNextPacket@@QEAAJAEAJAEAPEAPEAUIWbemClassObject@@AEAVCWbemClassCache@@@Z` | `0x5090` | 683 | UnwindData |  |
| 1157 | `?IsValid@CWbemDataPacket@@QEAAJJ@Z` | `0x5A70` | 213 | UnwindData |  |
| 1491 | `?UnmarshalPacket@CWbemObjectArrayPacket@@QEAAJAEAJAEAPEAPEAUIWbemClassObject@@AEAVCWbemClassCache@@@Z` | `0x6CA0` | 3,037 | UnwindData |  |
| 725 | `?GetClasslessInstanceObject@CWbemObjectArrayPacket@@AEAAJAEAVCWbemObjectPacket@@PEAPEAUIWbemClassObject@@AEAVCWbemClassCache@@@Z` | `0x7E70` | 1,375 | UnwindData |  |
| 642 | `?ExtendHeapSize@CInstancePart@@UEAAHPEAEKK@Z` | `0x8770` | 66 | UnwindData |  |
| 1158 | `?IsValid@CWbemObjectArrayPacket@@QEAA_NPEAVCWbemClassCache@@@Z` | `0x8B00` | 2,331 | UnwindData |  |
| 641 | `?ExtendHeapSize@CClassPart@@UEAAHPEAEKK@Z` | `0x9460` | 155 | UnwindData |  |
| 1249 | `?ReallocAndCompact@CClassPart@@QEAAHK@Z` | `0x9550` | 90 | UnwindData |  |
| 646 | `?ExtendPropertyTableSpace@CClassPart@@UEAAHPEAEKK@Z` | `0x98D0` | 253 | UnwindData |  |
| 787 | `?GetInstanceObject@CWbemObjectArrayPacket@@AEAAJAEAVCWbemObjectPacket@@PEAPEAUIWbemClassObject@@AEAVCWbemClassCache@@@Z` | `0x9A70` | 543 | UnwindData |  |
| 1366 | `?SetData@CWbemInstance@@QEAAXPEAEHK@Z` | `0x9D30` | 300 | UnwindData |  |
| 360 | `?AddObject@CWbemClassCache@@QEAAJAEAU_GUID@@PEAUIWbemClassObject@@@Z` | `0x9E70` | 377 | UnwindData |  |
| 639 | `?ExtendDataTableSpace@CClassPart@@UEAAHPEAEKK@Z` | `0x9FF0` | 228 | UnwindData |  |
| 648 | `?ExtendQualifierSetSpace@CClassPart@@UEAAHPEAVCBasicQualifierSet@@K@Z` | `0xA5A0` | 304 | UnwindData |  |
| 1203 | `?Merge@CDataTable@@SAPEAEPEAV1@PEAVCFastHeap@@01PEAVCPropertyLookupTable@@PEAE1@Z` | `0xA6E0` | 459 | UnwindData |  |
| 1201 | `?Merge@CClassAndMethods@@SAPEAEAEAV1@0PEAEH@Z` | `0xA8C0` | 129 | UnwindData |  |
| 1202 | `?Merge@CClassPart@@SAPEAEAEAV1@0PEAEH@Z` | `0xA950` | 565 | UnwindData |  |
| 1205 | `?Merge@CMethodPart@@SAPEAEAEAV1@0PEAEK@Z` | `0xAB90` | 1,263 | UnwindData |  |
| 1204 | `?Merge@CDerivationList@@SAPEAEAEAVCCompressedStringList@@0PEAE@Z` | `0xB090` | 123 | UnwindData |  |
| 1200 | `?Merge@CBasicQualifierSet@@SAPEAEPEAEPEAVCFastHeap@@0101H@Z` | `0xB120` | 329 | UnwindData |  |
| 943 | `?GetPropertyString@CWbemObject@@QEAAPEAVCCompressedString@@J@Z` | `0xB270` | 195 | UnwindData |  |
| 926 | `?GetPropertyCount@CClassPart@@QEAAJPEAVCVar@@@Z` | `0xB340` | 178 | UnwindData |  |
| 968 | `?GetQualifierLocally@CBasicQualifierSet@@SAPEAUCQualifier@@PEAEPEAVCFastHeap@@PEAVCCompressedString@@@Z` | `0xB400` | 124 | UnwindData |  |
| 784 | `?GetIndexedProps@CClassPart@@QEAAHAEAVCWStringArray@@@Z` | `0xB490` | 370 | UnwindData |  |
| 875 | `?GetNames@CWbemObject@@UEAAJPEBGJPEAUtagVARIANT@@PEAPEAUtagSAFEARRAY@@@Z` | `0xB610` | 3,062 | UnwindData |  |
| 1552 | `?WritePropertyValue@CWbemObject@@UEAAJJJPEBE@Z` | `0xC290` | 1,674 | UnwindData |  |
| 1215 | `?NValidateSize@CCompressedString@@QEBA_NH@Z` | `0xC920` | 21 | UnwindData |  |
| 1206 | `?Merge@CPropertyLookupTable@@SAPEAEPEAV1@PEAVCFastHeap@@01PEAE1H@Z` | `0xC940` | 818 | UnwindData |  |
| 800 | `?GetKeyProps@CClassPart@@QEAAHAEAVCWStringArray@@@Z` | `0xCC80` | 440 | UnwindData |  |
| 1189 | `?MapLimitation@CPropertyLookupTable@@QEAAHJPEAVCWStringArray@@PEAVCLimitationMapping@@@Z` | `0xCE40` | 399 | UnwindData |  |
| 1330 | `?ResolveString@CFastHeap@@QEAAPEAVCCompressedString@@K@Z` | `0xD0D0` | 200 | UnwindData |  |
| 574 | `?CreateWStringCopy@CCompressedString@@QEBA?AVWString@@XZ` | `0xD1A0` | 377 | UnwindData |  |
| 1460 | `?StartsWithNoCase@CCompressedString@@QEBAHPEBG@Z` | `0xD320` | 184 | UnwindData |  |
| 627 | `?EstimateMergeSpace@CWbemClass@@QEAAKPEAEJ@Z` | `0xD470` | 199 | UnwindData |  |
| 523 | `?CopyToNewHeap@CEmbeddedObject@@SAHKPEAVCFastHeap@@0AEFAK@Z` | `0xD540` | 136 | UnwindData |  |
| 747 | `?GetEmbeddedObj@CWbemObject@@QEAAPEAV1@J@Z` | `0xD5D0` | 203 | UnwindData |  |
| 1468 | `?StripClassPart@CWbemInstance@@UEAAJXZ` | `0xD6B0` | 568 | UnwindData |  |
| 658 | `?FindMethod@CMethodPart@@IEAAHPEBG@Z` | `0xD9C0` | 151 | UnwindData |  |
| 979 | `?GetQualifierSetStart@CMethodQualifierSetContainer@@UEAAPEAEXZ` | `0xDA60` | 121 | UnwindData |  |
| 567 | `?CreateLimitedRepresentation@CQualifierSetList@@QEAAPEAEPEAVCLimitationMapping@@PEAVCFastHeap@@1PEAE@Z` | `0xDE70` | 291 | UnwindData |  |
| 503 | `?ComputeNecessarySpaceForPropagation@CBasicQualifierSet@@SAKPEAEE@Z` | `0xE050` | 102 | UnwindData |  |
| 1548 | `?WritePropagatedVersion@CBasicQualifierSet@@SAPEAEPEAVCPtrSource@@E0PEAVCFastHeap@@1@Z` | `0xE0C0` | 407 | UnwindData |  |
| 565 | `?CreateLimitedRepresentation@CInstancePart@@QEAAPEAEPEAVCLimitationMapping@@HPEAE@Z` | `0xE2A0` | 500 | UnwindData |  |
| 1322 | `?RemoveSpecific@CLimitationMapping@@QEAAXXZ` | `0xE4A0` | 108 | UnwindData |  |
| 562 | `?CreateLimitedRepresentation@CDataTable@@QEAAPEAEPEAVCLimitationMapping@@HPEAVCFastHeap@@1PEAE@Z` | `0xE520` | 883 | UnwindData |  |
| 749 | `?GetFirstQualifier@CBasicQualifierSet@@QEAAPEAUCQualifier@@XZ` | `0xE8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `?GetStart@CMethodPart@@QEAAPEAEXZ` | `0xE8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `?GetStart@CQualifierSetList@@QEAAPEAEXZ` | `0xE8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `?CopyToNewHeap@CUntypedArray@@SAHKVCType@@PEAVCFastHeap@@1AEFAK@Z` | `0xE8B0` | 275 | UnwindData |  |
| 566 | `?CreateLimitedRepresentation@CPropertyLookupTable@@QEAAPEAEPEAVCLimitationMapping@@PEAVCFastHeap@@PEAEAEAH@Z` | `0xEA70` | 888 | UnwindData |  |
| 522 | `?CopyToNewHeap@CCompressedString@@SAHKPEAVCFastHeap@@0AEFAK@Z` | `0xEDF0` | 560 | UnwindData |  |
| 1477 | `?TranslateToNewHeap@CUntypedArray@@SAHPEAVCPtrSource@@VCType@@PEAVCFastHeap@@2@Z` | `0xF030` | 773 | UnwindData |  |
| 1259 | `?Rebase@CDecorationPart@@QEAAXPEAE@Z` | `0xF340` | 61 | UnwindData |  |
| 1328 | `?ResolveHeapPointer@CFastHeap@@QEAAPEAEK@Z` | `0xF3E0` | 42 | UnwindData |  |
| 384 | `?Allocate@CFastHeap@@QEAAHKAEFAK@Z` | `0xF410` | 297 | UnwindData |  |
| 22 | `??0CClassAndMethods@@QEAA@XZ` | `0xF540` | 68 | UnwindData |  |
| 561 | `?CreateLimitedRepresentation@CClassPart@@QEAAPEAEPEAVCLimitationMapping@@HPEAEAEAH@Z` | `0xF590` | 724 | UnwindData |  |
| 1472 | `?TranslateToNewHeap@CBasicQualifierSet@@SAHPEAVCPtrSource@@PEAVCFastHeap@@1@Z` | `0xF870` | 204 | UnwindData |  |
| 1008 | `?GetStart@CFastHeap@@QEAAPEAEXZ` | `0x10BB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??0CWbemClass@@QEAA@XZ` | `0x10BE0` | 370 | UnwindData |  |
| 452 | `?Clone@CWbemClass@@UEAAJPEAPEAUIWbemClassObject@@@Z` | `0x10D60` | 683 | UnwindData |  |
| 813 | `?GetLength@CCompressedString@@QEBAHXZ` | `0x11020` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1364 | `?SetData@CWbemClass@@UEAAXPEAEH@Z` | `0x11080` | 1,772 | UnwindData |  |
| 1267 | `?Rebase@CWbemInstance@@QEAAXPEAE@Z` | `0x11780` | 283 | UnwindData |  |
| 644 | `?ExtendInstancePartSpace@CWbemInstance@@UEAAHPEAVCInstancePart@@K@Z` | `0x119F0` | 43 | UnwindData |  |
| 1261 | `?Rebase@CInstancePart@@QEAAXPEAE@Z` | `0x11D90` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `?Clone@CWbemInstance@@UEAAJPEAPEAUIWbemClassObject@@@Z` | `0x11E10` | 1,569 | UnwindData |  |
| 461 | `?Compact@CClassAndMethods@@QEAAXXZ` | `0x12480` | 148 | UnwindData |  |
| 462 | `?Compact@CClassPart@@QEAAXXZ` | `0x12520` | 405 | UnwindData |  |
| 455 | `?CloneAndDecorate@CWbemInstance@@UEAAJJPEAG0PEAPEAUIWbemClassObject@@@Z` | `0x126C0` | 2,741 | UnwindData |  |
| 1479 | `?Trim@CFastHeap@@QEAAXXZ` | `0x13180` | 23 | UnwindData |  |
| 816 | `?GetLength@CDecorationPart@@QEAAKXZ` | `0x13300` | 33 | UnwindData |  |
| 1560 | `?fast_wcslen@CCompressedString@@SAHPEBG@Z` | `0x133D0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `?SetNullness@CDataTable@@QEAAXHH@Z` | `0x13480` | 147 | UnwindData |  |
| 1133 | `?IsNull@CDataTable@@QEAAHH@Z` | `0x13520` | 124 | UnwindData |  |
| 1456 | `?SpawnInstance@CWbemClass@@UEAAJJPEAPEAUIWbemClassObject@@@Z` | `0x135B0` | 3,850 | UnwindData |  |
| 1069 | `?InitEmptyInstance@CWbemInstance@@QEAAJAEAVCClassPart@@PEAEHPEAVCDecorationPart@@@Z` | `0x144C0` | 2,316 | UnwindData |  |
| 530 | `?Create@CInstancePart@@QEAAPEAEPEAEPEAVCClassPart@@PEAVCInstancePartContainer@@@Z` | `0x14DE0` | 100 | UnwindData |  |
| 1070 | `?InitNew@CWbemInstance@@QEAAJPEAVCWbemClass@@HPEAVCDecorationPart@@@Z` | `0x15510` | 45 | UnwindData |  |
| 1335 | `?SetAllToDefault@CDataTable@@QEAAXXZ` | `0x16020` | 20 | UnwindData |  |
| 520 | `?CopyNullness@CDataTable@@QEAAXPEAV1@@Z` | `0x160E0` | 27 | UnwindData |  |
| 1380 | `?SetDefaultness@CDataTable@@QEAAXHH@Z` | `0x16260` | 150 | UnwindData |  |
| 1102 | `?IsDefault@CDataTable@@QEAAHH@Z` | `0x16300` | 127 | UnwindData |  |
| 46 | `??0CInstanceQualifierSet@@QEAA@H@Z` | `0x164E0` | 107 | UnwindData |  |
| 1160 | `?IsValidInstancePart@CInstancePart@@QEAAJPEAVCClassPart@@AEAV?$vector@UEmbeddedObj@@V?$wbem_allocator@UEmbeddedObj@@@@@std@@@Z` | `0x16560` | 2,715 | UnwindData |  |
| 1168 | `?IsValidQualifierSet@CBasicQualifierSet@@QEAAJXZ` | `0x17030` | 1,115 | UnwindData |  |
| 1356 | `?SetData@CInstancePart@@QEAAXPEAEPEAVCInstancePartContainer@@AEAVCClassPart@@_K@Z` | `0x17550` | 52 | UnwindData |  |
| 1351 | `?SetData@CClassPart@@QEAAXPEAEPEAVCClassPartContainer@@PEAV1@@Z` | `0x17A20` | 481 | UnwindData |  |
| 86 | `??0CWbemInstance@@QEAA@XZ` | `0x17C10` | 1,234 | UnwindData |  |
| 1353 | `?SetData@CDataTable@@QEAAXPEAEHHPEAVCDataTableContainer@@@Z` | `0x180F0` | 163 | UnwindData |  |
| 25 | `??0CClassPart@@QEAA@XZ` | `0x181A0` | 176 | UnwindData |  |
| 40 | `??0CInstancePart@@QEAA@XZ` | `0x18260` | 176 | UnwindData |  |
| 65 | `??0CQualifierSet@@QEAA@HH@Z` | `0x18320` | 94 | UnwindData |  |
| 31 | `??0CClassQualifierSet@@QEAA@H@Z` | `0x18390` | 107 | UnwindData |  |
| 1214 | `?MergeClassPart@CWbemInstance@@UEAAJPEAUIWbemClassObject@@@Z` | `0x18410` | 1,526 | UnwindData |  |
| 1525 | `?ValidateBuffer@CInstancePart@@SA_KPEAE_KAEAVCClassPart@@AEAV?$vector@UEmbeddedObj@@V?$wbem_allocator@UEmbeddedObj@@@@@std@@@Z` | `0x18A10` | 2,485 | UnwindData |  |
| 1540 | `?ValidateSize@CCompressedString@@QEBAHH@Z` | `0x19CD0` | 612 | UnwindData |  |
| 1523 | `?ValidateBuffer@CEmbeddedObject@@SAXPEAE_KAEAV?$vector@UEmbeddedObj@@V?$wbem_allocator@UEmbeddedObj@@@@@std@@@Z` | `0x19F40` | 143 | UnwindData |  |
| 1522 | `?ValidateBuffer@CDecorationPart@@SA_KPEAE_K@Z` | `0x19FE0` | 111 | UnwindData |  |
| 1520 | `?ValidateBuffer@CCompressedStringList@@SA_KPEAE_K@Z` | `0x1A060` | 606 | UnwindData |  |
| 1531 | `?ValidateBuffer@CWbemInstance@@SA_KPEAEHPEAV1@AEAV?$vector@UEmbeddedObj@@V?$wbem_allocator@UEmbeddedObj@@@@@std@@@Z` | `0x1A360` | 240 | UnwindData |  |
| 1532 | `?ValidateBuffer@CWbemInstance@@SA_KPEAE_KAEAV?$vector@UEmbeddedObj@@V?$wbem_allocator@UEmbeddedObj@@@@@std@@@Z` | `0x1A460` | 631 | UnwindData |  |
| 1519 | `?ValidateBuffer@CClassPart@@SA_KPEAE_K@Z` | `0x1A6E0` | 2,283 | UnwindData |  |
| 1524 | `?ValidateBuffer@CFastHeap@@SA_KPEAE_K@Z` | `0x1AFE0` | 488 | UnwindData |  |
| 1159 | `?IsValidClassPart@CClassPart@@QEAAJXZ` | `0x1B1D0` | 2,183 | UnwindData |  |
| 147 | `??1CWbemClass@@UEAA@XZ` | `0x1BAE0` | 177 | UnwindData |  |
| 135 | `??1CClassPart@@QEAA@XZ` | `0x1BBA0` | 184 | UnwindData |  |
| 556 | `?CreateFromMemory@CWbemObject@@SAPEAV1@PEAEHHAEAVCBlobControl@@@Z` | `0x1BC90` | 1,042 | UnwindData |  |
| 557 | `?CreateFromStream@CWbemObject@@SAPEAV1@PEAUIStream@@@Z` | `0x1C1D0` | 385 | UnwindData |  |
| 835 | `?GetLimitedVersion@CWbemInstance@@QEAAJPEAVCLimitationMapping@@PEAPEAV1@@Z` | `0x1C3E0` | 1,001 | UnwindData |  |
| 563 | `?CreateLimitedRepresentation@CDecorationPart@@QEAAPEAEPEAVCLimitationMapping@@PEAE@Z` | `0x1C7D0` | 156 | UnwindData |  |
| 1526 | `?ValidateBuffer@CMethodPart@@SA_KPEAE_K@Z` | `0x1C880` | 769 | UnwindData |  |
| 1162 | `?IsValidMethodPart@CMethodPart@@QEAAJXZ` | `0x1CB90` | 529 | UnwindData |  |
| 1518 | `?ValidateBuffer@CClassAndMethods@@SA_KPEAE_K@Z` | `0x1CDB0` | 111 | UnwindData |  |
| 1211 | `?MergeAndDecorate@CWbemClass@@UEAAJJKPEAXPEAG1PEAPEAU_IWmiObject@@@Z` | `0x1CE30` | 674 | UnwindData |  |
| 553 | `?CreateFromBlob2@CWbemInstance@@SAPEAV1@PEAVCWbemClass@@PEAEPEAG2@Z` | `0x1D0E0` | 1,395 | UnwindData |  |
| 552 | `?CreateFromBlob2@CWbemClass@@SAPEAV1@PEAV1@PEAEPEAG2@Z` | `0x1D660` | 891 | UnwindData |  |
| 1350 | `?SetData@CClassAndMethods@@QEAAXPEAEPEAVCWbemClass@@PEAV1@@Z` | `0x1D9F0` | 591 | UnwindData |  |
| 1529 | `?ValidateBuffer@CWbemClass@@SA_KPEAE_K@Z` | `0x1DC50` | 130 | UnwindData |  |
| 746 | `?GetEmbedded@CEmbeddedObject@@QEAAPEAVCWbemObject@@XZ` | `0x1DD20` | 309 | UnwindData |  |
| 997 | `?GetSignature@CMethodPart@@IEAAXHHPEAPEAVCWbemObject@@@Z` | `0x1DE60` | 63 | UnwindData |  |
| 1207 | `?Merge@CWbemClass@@QEAAPEAEPEAE0HH@Z` | `0x1DEB0` | 242 | UnwindData |  |
| 1383 | `?SetFromUnicode@CCompressedString@@QEAAXHPEBG@Z` | `0x1DFB0` | 99 | UnwindData |  |
| 497 | `?ComputeNecessarySpace@CCompressedString@@SAHPEBGAEAH@Z` | `0x1E020` | 88 | UnwindData |  |
| 848 | `?GetMethod@CWbemClass@@UEAAJPEBGJPEAPEAUIWbemClassObject@@1@Z` | `0x1E080` | 673 | UnwindData |  |
| 847 | `?GetMethod@CMethodPart@@QEAAJPEBGJPEAPEAVCWbemObject@@1@Z` | `0x1E330` | 95 | UnwindData |  |
| 1466 | `?StoreToCVar@CEmbeddedObject@@QEAAXAEAVCVar@@@Z` | `0x1E3A0` | 71 | UnwindData |  |
| 454 | `?CloneAndDecorate@CWbemClass@@UEAAJJPEAG0PEAPEAUIWbemClassObject@@@Z` | `0x1E3F0` | 924 | UnwindData |  |
| 1221 | `?NextMethod@CWbemClass@@UEAAJJPEAPEAGPEAPEAUIWbemClassObject@@1@Z` | `0x1E7A0` | 926 | UnwindData |  |
| 850 | `?GetMethodAt@CMethodPart@@QEAAJHPEAPEAGPEAPEAVCWbemObject@@1@Z` | `0x1EB50` | 529 | UnwindData |  |
| 1060 | `?HasLocalQualifiers@CBasicQualifierSet@@SAHPEAE@Z` | `0x1ED70` | 25 | UnwindData |  |
| 505 | `?ComputeUnmergedSpace@CBasicQualifierSet@@SAKPEAE@Z` | `0x1F030` | 92 | UnwindData |  |
| 1219 | `?Next@CWbemObject@@UEAAJJPEAPEAGPEAUtagVARIANT@@PEAJ2@Z` | `0x1F0A0` | 2,575 | UnwindData |  |
| 736 | `?GetDefaultValue@CClassPart@@QEAAJPEBGPEAVCVar@@@Z` | `0x1FAC0` | 59 | UnwindData |  |
| 752 | `?GetFullPath@CWbemObject@@QEAAPEAGXZ` | `0x1FB10` | 683 | UnwindData |  |
| 908 | `?GetPropAddrByHandle@CWbemObject@@UEAAJJJPEAKPEAPEAX@Z` | `0x1FE20` | 735 | UnwindData |  |
| 1023 | `?GetSystemProperty@CWbemObject@@QEAAJHPEAVCVar@@@Z` | `0x20110` | 303 | UnwindData |  |
| 656 | `?Find@CCompressedStringList@@QEAAHPEBG@Z` | `0x20250` | 131 | UnwindData |  |
| 876 | `?GetNamespace@CWbemObject@@QEAAJPEAVCVar@@@Z` | `0x20330` | 146 | UnwindData |  |
| 905 | `?GetPath@CWbemObject@@QEAAJPEAVCVar@@@Z` | `0x203D0` | 121 | UnwindData |  |
| 950 | `?GetPropertyType@CWbemInstance@@UEAAJPEBGPEAJ1@Z` | `0x20450` | 188 | UnwindData |  |
| 993 | `?GetServer@CWbemObject@@QEAAJPEAVCVar@@@Z` | `0x20520` | 148 | UnwindData |  |
| 1024 | `?GetSystemPropertyByName@CWbemObject@@QEAAJPEBGPEAVCVar@@@Z` | `0x205C0` | 828 | UnwindData |  |
| 738 | `?GetDerivation@CWbemObject@@QEAAJPEAVCVar@@@Z` | `0x20910` | 40 | UnwindData |  |
| 945 | `?GetPropertyType@CClassPart@@QEAAJPEBGPEAJ1@Z` | `0x20940` | 234 | UnwindData |  |
| 948 | `?GetPropertyType@CWbemClass@@UEAAJPEBGPEAJ1@Z` | `0x20A30` | 239 | UnwindData |  |
| 1065 | `?InheritsFrom@CWbemObject@@UEAAJPEBG@Z` | `0x20B30` | 460 | UnwindData |  |
| 713 | `?GetClassNameW@CClassPart@@QEAAPEAVCCompressedString@@XZ` | `0x20D10` | 85 | UnwindData |  |
| 946 | `?GetPropertyType@CSystemProperties@@SAJPEBGPEAJ1@Z` | `0x20E10` | 100 | UnwindData |  |
| 923 | `?GetProperty@CWbemClass@@UEAAJPEBGPEAVCVar@@@Z` | `0x20E80` | 957 | UnwindData |  |
| 661 | `?FindName@CSystemProperties@@SAHPEBG@Z` | `0x21250` | 387 | UnwindData |  |
| 735 | `?GetDefaultValue@CClassPart@@QEAAJPEAVCPropertyInformation@@PEAVCVar@@@Z` | `0x213E0` | 281 | UnwindData |  |
| 921 | `?GetPropQualifier@CWbemInstance@@UEAAJPEBG0PEAVCVar@@PEAJ2@Z` | `0x21500` | 508 | UnwindData |  |
| 1064 | `?InheritsFrom@CClassPart@@QEAAHPEBG@Z` | `0x21710` | 330 | UnwindData |  |
| 878 | `?GetNonsystemPropertyValue@CWbemInstance@@QEAAJPEBGPEAVCVar@@@Z` | `0x21860` | 525 | UnwindData |  |
| 925 | `?GetProperty@CWbemInstance@@UEAAJPEBGPEAVCVar@@@Z` | `0x21A80` | 1,460 | UnwindData |  |
| 919 | `?GetPropQualifier@CWbemInstance@@UEAAJPEAVCPropertyInformation@@PEBGPEAVCVar@@PEAJ3@Z` | `0x22040` | 2,389 | UnwindData |  |
| 808 | `?GetKnownStringIndex@CKnownStringTable@@SAHPEBG@Z` | `0x22A00` | 421 | UnwindData |  |
| 614 | `?EnumPrimaryQualifiers@CBasicQualifierSet@@QEAAJEEAEAVCFixedBSTRArray@@0@Z` | `0x22C80` | 1,076 | UnwindData |  |
| 737 | `?GetDerivation@CClassPart@@QEAAJPEAVCVar@@@Z` | `0x230C0` | 917 | UnwindData |  |
| 501 | `?ComputeNecessarySpace@CInstancePart@@SAKPEAVCClassPart@@@Z` | `0x23460` | 269 | UnwindData |  |
| 987 | `?GetRelPath@CWbemInstance@@UEAAPEAGH@Z` | `0x23580` | 1,985 | UnwindData |  |
| 682 | `?GetActualValue@CInstancePart@@QEAAJPEAVCPropertyInformation@@PEAVCVar@@@Z` | `0x23D50` | 290 | UnwindData |  |
| 924 | `?GetProperty@CWbemInstance@@MEAAJPEAVCPropertyInformation@@PEAVCVar@@@Z` | `0x23E80` | 590 | UnwindData |  |
| 1465 | `?StoreToCVar@CCompressedString@@QEBAHAEAVCVar@@@Z` | `0x243C0` | 63 | UnwindData |  |
| 533 | `?CreateBSTRCopy@CCompressedString@@QEBAPEAGXZ` | `0x24410` | 282 | UnwindData |  |
| 807 | `?GetKnownString@CKnownStringTable@@SAAEAVCCompressedString@@H@Z` | `0x24530` | 162 | UnwindData |  |
| 528 | `?Create@CFixedBSTRArray@@QEAAXH@Z` | `0x245E0` | 308 | UnwindData |  |
| 672 | `?Get@CQualifierSet@@UEAAJPEBGJPEAUtagVARIANT@@PEAJ@Z` | `0x247E0` | 4,162 | UnwindData |  |
| 622 | `?EstimateInstanceSpace@CWbemInstance@@SAKAEAVCClassPart@@PEAVCDecorationPart@@@Z` | `0x25830` | 227 | UnwindData |  |
| 663 | `?FindPropertyByName@CPropertyLookupTable@@QEAAPEAUCPropertyLookup@@PEAVCCompressedString@@@Z` | `0x25920` | 571 | UnwindData |  |
| 483 | `?CompareNoCase@CCompressedString@@QEBAHAEBV1@@Z` | `0x25B70` | 325 | UnwindData |  |
| 484 | `?CompareNoCase@CCompressedString@@QEBAHPEBD@Z` | `0x25CC0` | 301 | UnwindData |  |
| 485 | `?CompareNoCase@CCompressedString@@QEBAHPEBG@Z` | `0x26260` | 69 | UnwindData |  |
| 493 | `?CompareUnicodeToAsciiNoCase@CCompressedString@@KAHPEBGPEBDH@Z` | `0x26400` | 308 | UnwindData |  |
| 1077 | `?InsertProperty@CPropertyLookupTable@@QEAAJAEBUCPropertyLookup@@AEAH@Z` | `0x26540` | 879 | UnwindData |  |
| 828 | `?GetLength@CType@@SAKK@Z` | `0x268C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1433 | `?SetQualifierValue@CQualifierSet@@QEAAJPEBGEPEAVCTypedValue@@HH@Z` | `0x26900` | 5,645 | UnwindData |  |
| 956 | `?GetQualifier@CQualifierSet@@QEAAJPEBGPEAVCVar@@PEAJ2@Z` | `0x27F20` | 265 | UnwindData |  |
| 985 | `?GetRegularQualifierLocally@CBasicQualifierSet@@SAPEAUCQualifier@@PEAEPEAVCFastHeap@@PEBG@Z` | `0x28030` | 766 | UnwindData |  |
| 970 | `?GetQualifierLocally@CBasicQualifierSet@@SAPEAUCQualifier@@PEAEPEAVCFastHeap@@PEBGAEAH@Z` | `0x28340` | 1,248 | UnwindData |  |
| 962 | `?GetQualifier@CWbemInstance@@UEAAJPEBGPEAVCVar@@PEAJ2@Z` | `0x28830` | 311 | UnwindData |  |
| 967 | `?GetQualifierLocally@CBasicQualifierSet@@QEAAPEAUCQualifier@@PEBGAEAH@Z` | `0x28970` | 1,253 | UnwindData |  |
| 958 | `?GetQualifier@CQualifierSet@@QEAAPEAUCQualifier@@PEBGAEAH@Z` | `0x28E60` | 2,193 | UnwindData |  |
| 984 | `?GetRegularQualifierLocally@CBasicQualifierSet@@QEAAPEAUCQualifier@@PEBG@Z` | `0x29700` | 766 | UnwindData |  |
| 662 | `?FindProperty@CPropertyLookupTable@@QEAAPEAUCPropertyLookup@@PEBG@Z` | `0x29A10` | 785 | UnwindData |  |
| 666 | `?FindPropertyInfo@CClassPart@@QEAAPEAVCPropertyInformation@@PEBG@Z` | `0x29D30` | 850 | UnwindData |  |
| 1424 | `?SetPropValue@CWbemInstance@@UEAAJPEBGPEAVCVar@@J@Z` | `0x2A110` | 2,331 | UnwindData |  |
| 1333 | `?SetActualValue@CInstancePart@@QEAAJPEAVCPropertyInformation@@PEAVCVar@@@Z` | `0x2AA40` | 1,671 | UnwindData |  |
| 600 | `?DoesCIMTYPEMatchVARTYPE@CType@@SAHJG@Z` | `0x2C7C0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1048 | `?GetVARTYPE@CType@@SAGK@Z` | `0x2C980` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `?LoadFromCVarVector@CUntypedArray@@SAJPEAVCPtrSource@@AEAVCVarVector@@KPEAVCFastHeap@@AEAKH@Z` | `0x2CAB0` | 842 | UnwindData |  |
| 1224 | `?Put@CQualifierSet@@UEAAJPEBGPEAUtagVARIANT@@J@Z` | `0x2CEB0` | 1,549 | UnwindData |  |
| 1169 | `?IsValidQualifierType@CBasicQualifierSet@@SAHG@Z` | `0x2D4D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `?GetNames@CQualifierSet@@UEAAJJPEAPEAUtagSAFEARRAY@@@Z` | `0x2D510` | 980 | UnwindData |  |
| 615 | `?EnumQualifiers@CQualifierSet@@QEAAJEEAEAVCFixedBSTRArray@@@Z` | `0x2D8F0` | 1,150 | UnwindData |  |
| 670 | `?Free@CFixedBSTRArray@@QEAAXXZ` | `0x2DDC0` | 35 | UnwindData |  |
| 1471 | `?ThreeWayMergeOrdered@CFixedBSTRArray@@QEAAXAEAV1@00@Z` | `0x2DE50` | 834 | UnwindData |  |
| 1332 | `?SelfRebase@CQualifierSet@@QEAAHXZ` | `0x2E1A0` | 52 | UnwindData |  |
| 606 | `?EndEnumeration@CQualifierSet@@UEAAJXZ` | `0x2E220` | 98 | UnwindData |  |
| 439 | `?CheckCVarVector@CUntypedArray@@SAHAEAVCVarVector@@K@Z` | `0x2E290` | 373 | UnwindData |  |
| 1141 | `?IsPointerType@CType@@SAHK@Z` | `0x2E410` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1218 | `?Next@CQualifierSet@@UEAAJJPEAPEAGPEAUtagVARIANT@@PEAJ@Z` | `0x2E440` | 738 | UnwindData |  |
| 534 | `?CreateCVarVector@CUntypedArray@@QEAAPEAVCVarVector@@VCType@@PEAVCFastHeap@@@Z` | `0x2E770` | 852 | UnwindData |  |
| 1418 | `?SetPropQualifier@CClassPart@@QEAAJPEBG0JPEAVCVar@@@Z` | `0x2EAD0` | 501 | UnwindData |  |
| 940 | `?GetPropertyQualifierSet@CWbemClass@@UEAAJPEBGPEAPEAUIWbemQualifierSet@@@Z` | `0x2ECD0` | 816 | UnwindData |  |
| 1071 | `?InitPropertyQualifierSet@CClassPart@@QEAAJPEBGPEAVCClassPropertyQualifierSet@@@Z` | `0x2F010` | 220 | UnwindData |  |
| 136 | `??1CClassQualifierSet@@UEAA@XZ` | `0x2F190` | 189 | UnwindData |  |
| 140 | `??1CInstanceQualifierSet@@UEAA@XZ` | `0x2F190` | 189 | UnwindData |  |
| 1225 | `?Put@CWbemClass@@UEAAJPEBGJPEAUtagVARIANT@@J@Z` | `0x2F580` | 1,769 | UnwindData |  |
| 1146 | `?IsReservedWord@CReservedWordTable@@SAHPEBG@Z` | `0x2FC70` | 313 | UnwindData |  |
| 1423 | `?SetPropValue@CWbemClass@@UEAAJPEBGPEAVCVar@@J@Z` | `0x2FDB0` | 354 | UnwindData |  |
| 570 | `?CreateNoCaseStringHeapPtr@CFastHeap@@QEAAHPEBGAEFAK@Z` | `0x30060` | 87 | UnwindData |  |
| 610 | `?EnsureProperty@CClassPart@@QEAAJPEBGGJH@Z` | `0x300C0` | 1,172 | UnwindData |  |
| 1078 | `?InsertProperty@CPropertyLookupTable@@QEAAJPEBGKAEAH@Z` | `0x30560` | 1,275 | UnwindData |  |
| 653 | `?ExtendTo@CDataTable@@QEAAHGK@Z` | `0x30A70` | 194 | UnwindData |  |
| 386 | `?AllocateString@CFastHeap@@QEAAHPEBGAEFAK@Z` | `0x30B40` | 90 | UnwindData |  |
| 1379 | `?SetDefaultValue@CClassPart@@QEAAJPEBGPEAVCVar@@@Z` | `0x30DA0` | 59 | UnwindData |  |
| 1022 | `?GetSyntax@CType@@SAPEAGK@Z` | `0x30DF0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1378 | `?SetDefaultValue@CClassPart@@IEAAJPEAVCPropertyInformation@@PEAVCVar@@@Z` | `0x30F20` | 655 | UnwindData |  |
| 409 | `?CanBeKey@CType@@SAHK@Z` | `0x313E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `?CanContainKeyedProps@CClassPart@@QEAAHXZ` | `0x31410` | 64 | UnwindData |  |
| 1121 | `?IsKeyed@CClassPart@@QEAAHXZ` | `0x31460` | 236 | UnwindData |  |
| 437 | `?CheckBoolQualifier@CClassPart@@QEAAHPEBG@Z` | `0x31560` | 59 | UnwindData |  |
| 1340 | `?SetClassName@CClassPart@@QEAAJPEAVCVar@@@Z` | `0x315B0` | 715 | UnwindData |  |
| 1017 | `?GetSuperclassName@CClassPart@@QEAAJPEAVCVar@@@Z` | `0x31890` | 202 | UnwindData |  |
| 1190 | `?MapLimitation@CWbemClass@@QEAAHJPEAVCWStringArray@@PEAVCLimitationMapping@@@Z` | `0x31960` | 112 | UnwindData |  |
| 1188 | `?MapLimitation@CDecorationPart@@SAHPEAVCWStringArray@@PEAVCLimitationMapping@@@Z` | `0x319E0` | 161 | UnwindData |  |
| 1341 | `?SetClassObject@CLimitationMapping@@QEAAXPEAVCWbemClass@@@Z` | `0x31A90` | 81 | UnwindData |  |
| 1187 | `?MapLimitation@CClassPart@@QEAAHJPEAVCWStringArray@@PEAVCLimitationMapping@@@Z` | `0x31AF0` | 216 | UnwindData |  |
| 428 | `?CanContainSingleton@CClassPart@@UEAAJXZ` | `0x31BD0` | 76 | UnwindData |  |
| 591 | `?DeleteProperty@CPropertyLookupTable@@QEAAXPEAUCPropertyLookup@@H@Z` | `0x31C30` | 442 | UnwindData |  |
| 1113 | `?IsIllegalDerivedClass@CSystemProperties@@SAHPEBG@Z` | `0x31DF0` | 97 | UnwindData |  |
| 655 | `?Filter@CFixedBSTRArray@@QEAAXPEBGH@Z` | `0x31E60` | 193 | UnwindData |  |
| 723 | `?GetClassSubset@CWbemClass@@UEAAJKPEAPEBGPEAPEAU_IWmiObject@@@Z` | `0x31F30` | 646 | UnwindData |  |
| 834 | `?GetLimitedVersion@CWbemClass@@QEAAJPEAVCLimitationMapping@@PEAPEAV1@@Z` | `0x321C0` | 888 | UnwindData |  |
| 51 | `??0CLimitationMapping@@QEAA@XZ` | `0x32540` | 65 | UnwindData |  |
| 1367 | `?SetData@CWbemInstance@@UEAAXPEAEH@Z` | `0x32590` | 34 | UnwindData |  |
| 613 | `?EnsureReal@CQualifierSetList@@QEAAHXZ` | `0x32C40` | 108 | UnwindData |  |
| 649 | `?ExtendQualifierSetSpace@CInstancePQSContainer@@UEAAHPEAVCBasicQualifierSet@@K@Z` | `0x32CC0` | 125 | UnwindData |  |
| 652 | `?ExtendQualifierSetSpace@CQualifierSetList@@QEAAHPEAVCBasicQualifierSet@@K@Z` | `0x32D50` | 155 | UnwindData |  |
| 898 | `?GetObjectText@CWbemClass@@UEAAJJPEAPEAG@Z` | `0x32E00` | 1,815 | UnwindData |  |
| 366 | `?AddPropertyText@CWbemClass@@QEAAJAEAVWString@@PEAUCPropertyLookup@@PEAVCPropertyInformation@@J@Z` | `0x33520` | 1,389 | UnwindData |  |
| 899 | `?GetObjectText@CWbemInstance@@UEAAJJPEAPEAG@Z` | `0x33AA0` | 2,292 | UnwindData |  |
| 507 | `?ConvertToClass@CWbemInstance@@QEAAJPEAVCWbemClass@@PEAPEAV1@@Z` | `0x343D0` | 488 | UnwindData |  |
| 506 | `?ConvertToClass@CInstancePart@@QEAAPEAEAEAVCClassPart@@KPEAE@Z` | `0x345C0` | 243 | UnwindData |  |
| 1554 | `?WriteSmallerVersion@CDataTable@@QEAAPEAEHKPEAE@Z` | `0x346C0` | 139 | UnwindData |  |
| 1555 | `?WriteSmallerVersion@CQualifierSetList@@QEAAPEAEHPEAE@Z` | `0x34780` | 94 | UnwindData |  |
| 974 | `?GetQualifierSetData@CQualifierSetList@@SAPEAEPEAEH@Z` | `0x347F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1049 | `?GetValueText@CWbemObject@@SAPEAGJAEAVCVar@@K@Z` | `0x34860` | 1,105 | UnwindData |  |
| 1026 | `?GetText@CBasicQualifierSet@@SAJPEAEPEAVCFastHeap@@JAEAVWString@@@Z` | `0x34CC0` | 1,481 | UnwindData |  |
| 712 | `?GetClassNameW@CClassPart@@QEAAJPEAVCVar@@@Z` | `0x352E0` | 255 | UnwindData |  |
| 576 | `?CreateWStringCopy@CCompressedString@@QEBAXAEAVWString@@@Z` | `0x353F0` | 81 | UnwindData |  |
| 367 | `?AddPropertyType@CType@@SAXAEAVWString@@PEBG@Z` | `0x35590` | 330 | UnwindData |  |
| 1504 | `?Update@CClassAndMethods@@SAJAEAV1@0J@Z` | `0x356E0` | 184 | UnwindData |  |
| 1505 | `?Update@CClassPart@@SAJAEAV1@0J@Z` | `0x357A0` | 289 | UnwindData |  |
| 382 | `?AddText@CMethodDescription@@SAJPEFAU1@AEAVWString@@PEAVCFastHeap@@J@Z` | `0x358D0` | 1,388 | UnwindData |  |
| 76 | `??0CWbemClassCache@@QEAA@K@Z` | `0x36E40` | 87 | UnwindData |  |
| 153 | `??1CWbemInstance@@UEAA@XZ` | `0x37470` | 1,123 | UnwindData |  |
| 599 | `?DoSignaturesMatch@CMethodPart@@IEAAHHW4METHOD_SIGNATURE_TYPE@@PEAVCWbemObject@@@Z` | `0x3ABA0` | 109 | UnwindData |  |
| 487 | `?CompareTo@CDecorationPart@@QEAAHAEAV1@@Z` | `0x3AC20` | 146 | UnwindData |  |
| 480 | `?CompareExactMatch@CMethodPart@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x3ACC0` | 461 | UnwindData |  |
| 1228 | `?PutMethod@CWbemClass@@UEAAJPEBGJPEAUIWbemClassObject@@1@Z` | `0x3AEA0` | 563 | UnwindData |  |
| 490 | `?CompareTo@CWbemClass@@UEAAJJPEAUIWbemClassObject@@@Z` | `0x3B0E0` | 731 | UnwindData |  |
| 1541 | `?WbemObjectFromCOMPtr@CWbemObject@@SAJPEAUIUnknown@@PEAPEAV1@@Z` | `0x3B3D0` | 245 | UnwindData |  |
| 491 | `?CompareTo@CWbemObject@@UEAAJJPEAUIWbemClassObject@@@Z` | `0x3B4D0` | 4,080 | UnwindData |  |
| 1227 | `?PutMethod@CMethodPart@@QEAAJPEBGJPEAVCWbemObject@@1@Z` | `0x3C4D0` | 1,264 | UnwindData |  |
| 611 | `?EnsureQualifier@CMethodPart@@QEAAJPEAVCWbemObject@@PEBGPEAPEAV2@@Z` | `0x3C9D0` | 228 | UnwindData |  |
| 1535 | `?ValidateOutParams@CMethodPart@@IEAAJPEAVCWbemObject@@@Z` | `0x3CAC0` | 180 | UnwindData |  |
| 612 | `?EnsureQualifier@CWbemClass@@QEAAJPEBG@Z` | `0x3CB80` | 372 | UnwindData |  |
| 776 | `?GetIds@CWbemClass@@QEAAJAEAVCFlexArray@@PEAV1@@Z` | `0x3CD00` | 1,646 | UnwindData |  |
| 575 | `?CreateWStringCopy@CCompressedString@@QEBAXAEAVWString2@@@Z` | `0x3D380` | 102 | UnwindData |  |
| 440 | `?CheckDuplicateParameters@CMethodPart@@IEAAJPEAVCWbemObject@@0@Z` | `0x3D3F0` | 833 | UnwindData |  |
| 441 | `?CheckIds@CMethodPart@@IEAAJPEAVCWbemClass@@0@Z` | `0x3D740` | 490 | UnwindData |  |
| 476 | `?CompareDefs@CClassPart@@QEAAHAEAV1@@Z` | `0x3D930` | 190 | UnwindData |  |
| 1440 | `?SetSignature@CMethodPart@@IEAAJHW4METHOD_SIGNATURE_TYPE@@PEAVCWbemObject@@@Z` | `0x3DA00` | 348 | UnwindData |  |
| 390 | `?AreEqual@CWbemObject@@SAHPEAV1@0J@Z` | `0x3DB70` | 76 | UnwindData |  |
| 1463 | `?StoreEmbedded@CEmbeddedObject@@QEAAXKPEAVCWbemObject@@@Z` | `0x3DBD0` | 323 | UnwindData |  |
| 1338 | `?SetArrayPropRangeByHandle@CWbemObject@@UEAAJJJKKKPEAX@Z` | `0x3E120` | 753 | UnwindData |  |
| 1086 | `?IsArrayPropertyHandle@CWbemObject@@QEAAJJPEAJPEAK@Z` | `0x3E420` | 164 | UnwindData |  |
| 1434 | `?SetRange@CUntypedArray@@SAJPEAVCPtrSource@@JKKPEAVCFastHeap@@KKKPEAX@Z` | `0x3E4D0` | 997 | UnwindData |  |
| 444 | `?CheckRangeSize@CUntypedArray@@SAJKKKKPEAX@Z` | `0x3E8C0` | 269 | UnwindData |  |
| 911 | `?GetPropQual@CWbemObject@@UEAAJPEBG0JKPEAJPEAK2PEAX@Z` | `0x3E9E0` | 700 | UnwindData |  |
| 1132 | `?IsNonArrayPointerType@CType@@SAHK@Z` | `0x3EEF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1151 | `?IsStringType@CType@@SAHK@Z` | `0x3EF20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1321 | `?RemoveRange@CUntypedArray@@SAJPEAVCPtrSource@@KKPEAVCFastHeap@@KK@Z` | `0x3EF80` | 567 | UnwindData |  |
| 1251 | `?ReallocArray@CUntypedArray@@KAJPEAVCPtrSource@@KPEAVCFastHeap@@KPEAK22@Z` | `0x3F1C0` | 295 | UnwindData |  |
| 651 | `?ExtendQualifierSetSpace@CMethodQualifierSetContainer@@UEAAHPEAVCBasicQualifierSet@@K@Z` | `0x3F2F0` | 178 | UnwindData |  |
| 1252 | `?Reallocate@CFastHeap@@QEAAHKKKAEFAK@Z` | `0x3F3B0` | 546 | UnwindData |  |
| 629 | `?EstimateNecessarySpace@CEmbeddedObject@@SAKPEAVCWbemObject@@@Z` | `0x3F5E0` | 174 | UnwindData |  |
| 1547 | `?WriteProp@CWbemObject@@UEAAJPEBGJKKJPEAX@Z` | `0x3F6A0` | 647 | UnwindData |  |
| 1246 | `?ReadProp@CWbemObject@@UEAAJPEBGJKPEAJ1PEAHPEAKPEAX@Z` | `0x3F930` | 725 | UnwindData |  |
| 569 | `?CreateMethod@CMethodPart@@IEAAJPEBGPEAVCWbemObject@@1@Z` | `0x3FC10` | 1,067 | UnwindData |  |
| 1483 | `?Undecorate@CWbemInstance@@UEAAXXZ` | `0x40050` | 125 | UnwindData |  |
| 1482 | `?Undecorate@CWbemClass@@UEAAXXZ` | `0x400E0` | 148 | UnwindData |  |
| 578 | `?Decorate@CWbemClass@@UEAAJPEBG0@Z` | `0x40180` | 488 | UnwindData |  |
| 500 | `?ComputeNecessarySpace@CDecorationPart@@SAKPEBG0@Z` | `0x40370` | 44 | UnwindData |  |
| 48 | `??0CInternalString@@QEAA@PEBG@Z` | `0x403B0` | 182 | UnwindData |  |
| 579 | `?Decorate@CWbemInstance@@UEAAJPEBG0@Z` | `0x404B0` | 465 | UnwindData |  |
| 496 | `?ComputeNecessarySpace@CCompressedString@@SAHPEBG@Z` | `0x40690` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `?Create@CDecorationPart@@QEAAXEPEBG0PEAE@Z` | `0x40700` | 92 | UnwindData |  |
| 1256 | `?Rebase@CClassPart@@QEAAXPEAE@Z` | `0x40770` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `?SetFromUnicode@CCompressedString@@QEAAXPEBG@Z` | `0x40810` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `?Reallocate@CWbemObject@@IEAAPEAEK@Z` | `0x40890` | 96 | UnwindData |  |
| 463 | `?Compact@CInstancePart@@QEAAX_N@Z` | `0x40900` | 721 | UnwindData |  |
| 637 | `?ExtendClassPartSpace@CClassAndMethods@@UEAAHPEAVCClassPart@@K@Z` | `0x40C30` | 199 | UnwindData |  |
| 636 | `?ExtendClassAndMethodsSpace@CWbemClass@@QEAAHK@Z` | `0x40D00` | 275 | UnwindData |  |
| 1255 | `?Rebase@CClassAndMethods@@QEAAXPEAE@Z` | `0x40E20` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1336 | `?SetAllocatedDataLength@CFastHeap@@QEAAXK@Z` | `0x40F20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `?ExtendQualifierSetSpace@CInstancePart@@UEAAHPEAVCBasicQualifierSet@@K@Z` | `0x40F50` | 278 | UnwindData |  |
| 1266 | `?Rebase@CWbemClass@@QEAAXPEAE@Z` | `0x41070` | 130 | UnwindData |  |
| 1250 | `?ReallocAndCompact@CInstancePart@@QEAAHK@Z` | `0x41140` | 143 | UnwindData |  |
| 647 | `?ExtendQualifierSetListSpace@CInstancePart@@UEAAHPEAEKK@Z` | `0x41450` | 246 | UnwindData |  |
| 1176 | `?Lock@CWbemObject@@UEAAJJ@Z` | `0x41550` | 60 | UnwindData |  |
| 806 | `?GetKnownQualifierLocally@CBasicQualifierSet@@SAPEAUCQualifier@@PEAEH@Z` | `0x41670` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1375 | `?SetDataWithNumProps@CClassAndMethods@@QEAAXPEAEPEAVCWbemClass@@KPEAV1@@Z` | `0x416E0` | 121 | UnwindData |  |
| 482 | `?CompareMostDerivedClass@CWbemClass@@QEAAJPEAV1@@Z` | `0x41760` | 973 | UnwindData |  |
| 1357 | `?SetData@CMethodPart@@QEAAXPEAEPEAVCMethodPartContainer@@PEAV1@@Z` | `0x41B40` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1376 | `?SetDataWithNumProps@CClassPart@@QEAAXPEAEPEAVCClassPartContainer@@KPEAV1@@Z` | `0x41BB0` | 257 | UnwindData |  |
| 479 | `?CompareExactMatch@CClassPart@@QEAA?AW4EReconciliation@@AEAV1@H@Z` | `0x41CC0` | 1,511 | UnwindData |  |
| 1361 | `?SetData@CQualifierSet@@QEAAXPEAEPEAVCQualifierSetContainer@@PEAVCBasicQualifierSet@@@Z` | `0x422B0` | 114 | UnwindData |  |
| 508 | `?ConvertToMergedInstance@CWbemInstance@@QEAAJXZ` | `0x43360` | 425 | UnwindData |  |
| 1175 | `?Lock@CSharedLock@@QEAAHK@Z` | `0x45C60` | 58 | UnwindData |  |
| 1487 | `?Unlock@CSharedLock@@QEAAHXZ` | `0x45DB0` | 9,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `?GetRelPath@CWbemObject@@QEAAJPEAVCVar@@@Z` | `0x48460` | 107 | UnwindData |  |
| 1445 | `?SetupDataPacketHeader@CWbemDataPacket@@IEAAJKEKK@Z` | `0x494C0` | 228 | UnwindData |  |
| 839 | `?GetMarshalPacket@CWbemEnumMarshaling@@QEAAJAEBU_GUID@@KPEAPEAUIWbemClassObject@@PEAKPEAPEAE@Z` | `0x495B0` | 1,335 | UnwindData |  |
| 1197 | `?MarshalPacket@CWbemSmartEnumNextPacket@@QEAAJJPEAPEAUIWbemClassObject@@PEAU_GUID@@PEAH@Z` | `0x49AF0` | 572 | UnwindData |  |
| 1195 | `?MarshalPacket@CWbemObjectArrayPacket@@QEAAJJPEAPEAUIWbemClassObject@@PEAU_GUID@@PEAH@Z` | `0x49D40` | 1,887 | UnwindData |  |
| 359 | `?AddMap@CWbemGuidToClassMap@@QEAAJAEAVCGUID@@PEAPEAVCWbemClassToIdMap@@@Z` | `0x4A560` | 523 | UnwindData |  |
| 406 | `?CalculateLength@CWbemSmartEnumNextPacket@@QEAAJJPEAPEAUIWbemClassObject@@PEAKAEAVCWbemClassToIdMap@@PEAU_GUID@@PEAH@Z` | `0x4A840` | 186 | UnwindData |  |
| 405 | `?CalculateLength@CWbemObjectArrayPacket@@QEAAJJPEAPEAUIWbemClassObject@@PEAKAEAVCWbemClassToIdMap@@PEAU_GUID@@PEAH@Z` | `0x4A900` | 1,758 | UnwindData |  |
| 145 | `??1CQualifierSet@@UEAA@XZ` | `0x4C010` | 189 | UnwindData |  |
| 1075 | `?InitializePropQualifierSet@CWbemInstance@@IEAAJPEBGAEAVCInstancePropertyQualifierSet@@@Z` | `0x4C0E0` | 226 | UnwindData |  |
| 941 | `?GetPropertyQualifierSet@CWbemInstance@@UEAAJPEBGPEAPEAUIWbemQualifierSet@@@Z` | `0x4C1D0` | 991 | UnwindData |  |
| 977 | `?GetQualifierSetStart@CInstancePQSContainer@@UEAAPEAEXZ` | `0x4C5C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 896 | `?GetObjectParts@CWbemInstance@@UEAAJPEAXKKPEAK@Z` | `0x4C620` | 1,094 | UnwindData |  |
| 827 | `?GetLength@CType@@QEAAKXZ` | `0x4CA70` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1240 | `?QueryInterface@CWbemObject@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x4CDD0` | 378 | UnwindData |  |
| 1534 | `?ValidateObject@CWbemObject@@UEAAJJ@Z` | `0x4CFE0` | 189 | UnwindData |  |
| 529 | `?Create@CInstancePQSContainer@@QEAAXPEAVCQualifierSetList@@HPEAVCClassPart@@K@Z` | `0x4D130` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `?Release@CWbemObject@@UEAAKXZ` | `0x4D170` | 57 | UnwindData |  |
| 509 | `?ConvertToUnicode@CCompressedString@@QEBAHPEAGK@Z` | `0x4D1F0` | 146 | UnwindData |  |
| 1088 | `?IsAsciiable@CCompressedString@@KAHPEBG@Z` | `0x4D290` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `?FindPropertyByPtr@CPropertyLookupTable@@QEAAPEAUCPropertyLookup@@K@Z` | `0x4D2C0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `?CompactAll@CWbemInstance@@UEAAXXZ` | `0x4D340` | 748 | UnwindData |  |
| 1161 | `?IsValidKey@CWbemInstance@@QEAAHPEBG@Z` | `0x4D640` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1435 | `?SetSecondarySetData@CInstancePQSContainer@@QEAAXXZ` | `0x4D670` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1450 | `?Skip@CBasicQualifierSet@@QEAAPEAEXZ` | `0x4D6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `?IsOutOfLine@CFastHeap@@IEAAHXZ` | `0x4D6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1087 | `?IsArrayValid@CUntypedArray@@QEAAJVCType@@PEAVCFastHeap@@@Z` | `0x4D6E0` | 382 | UnwindData |  |
| 1355 | `?SetData@CFastHeap@@QEAAHPEAEPEAVCHeapContainer@@@Z` | `0x4D990` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1501 | `?Unmerge@CWbemInstance@@UEAAJPEAEHPEAK@Z` | `0x4D9E0` | 615 | UnwindData |  |
| 139 | `??1CInstancePart@@QEAA@XZ` | `0x4DC50` | 179 | UnwindData |  |
| 1475 | `?TranslateToNewHeap@CInstancePart@@QEAAHAEAVCClassPart@@PEAVCFastHeap@@1@Z` | `0x4DD10` | 202 | UnwindData |  |
| 1474 | `?TranslateToNewHeap@CDataTable@@QEAAHPEAVCPropertyLookupTable@@HPEAVCFastHeap@@1@Z` | `0x4DDE0` | 252 | UnwindData |  |
| 1476 | `?TranslateToNewHeap@CQualifierSetList@@QEAAHPEAVCFastHeap@@0@Z` | `0x4DEF0` | 134 | UnwindData |  |
| 759 | `?GetHeaderLength@CFastHeap@@IEAAKXZ` | `0x4DF80` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `??1CFixedBSTRArray@@QEAA@XZ` | `0x4E310` | 27 | UnwindData |  |
| 155 | `??1CWbemObject@@UEAA@XZ` | `0x4E340` | 112 | UnwindData |  |
| 1349 | `?SetData@CBasicQualifierSet@@QEAAXPEAEPEAVCFastHeap@@@Z` | `0x4E3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `?GetQualifierSetData@CQualifierSetList@@QEAAPEAEH@Z` | `0x4E3E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??0CFixedBSTRArray@@QEAA@XZ` | `0x4E420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1053 | `?GetWbemObjectUnknown@CInstancePQSContainer@@UEAAPEAUIUnknown@@XZ` | `0x4E440` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `?GetActualType@CType@@SAKK@Z` | `0x4E480` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `?GetWbemObjectUnknown@CInstancePart@@UEAAPEAUIUnknown@@XZ` | `0x4E4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | `?GetHeap@CInstancePQSContainer@@UEAAPEAVCFastHeap@@XZ` | `0x4E4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `?GetBasic@CType@@SAKK@Z` | `0x4E4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `?GetLength@CCompressedStringList@@QEAAKXZ` | `0x4E500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | `?GetNumProperties@CPropertyLookupTable@@QEAAHXZ` | `0x4E500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `?GetIndexFromFake@CFastHeap@@SAHK@Z` | `0x4E510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1156 | `?IsUnicode@CCompressedString@@QEBAHXZ` | `0x4E520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1057 | `?GetWbemObjectUnknown@CQualifierSetList@@QEAAPEAUIUnknown@@XZ` | `0x4E530` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1362 | `?SetData@CQualifierSetList@@QEAAXPEAEHPEAVCQualifierSetListContainer@@@Z` | `0x4E570` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `?GetHeap@CQualifierSetList@@QEAAPEAVCFastHeap@@XZ` | `0x4E5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1354 | `?SetData@CDecorationPart@@QEAAXPEAE@Z` | `0x4E5E0` | 34 | UnwindData |  |
| 695 | `?GetAt@CPropertyLookupTable@@QEAAPEAUCPropertyLookup@@H@Z` | `0x4E670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 901 | `?GetOffset@CDataTable@@QEAAPEAVCUntypedValue@@K@Z` | `0x4E690` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `?GetObjectMemory@CWbemObject@@UEAAJPEAXKPEAK@Z` | `0x4E6F0` | 316 | UnwindData |  |
| 951 | `?GetPropertyValue@CWbemObject@@UEAAJPEAU_tag_WbemPropertyName@@JPEAPEAGPEAUtagVARIANT@@@Z` | `0x4E840` | 2,020 | UnwindData |  |
| 1453 | `?SortInPlace@CFixedBSTRArray@@QEAAXXZ` | `0x4F030` | 31 | UnwindData |  |
| 780 | `?GetInLineLength@CFastHeap@@IEAAPEFAKXZ` | `0x4F240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `?AddRef@CWbemObject@@UEAAKXZ` | `0x4F250` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1042 | `?GetUsedLength@CFastHeap@@QEAAKXZ` | `0x4F2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `?GetLength@CFastHeap@@QEAAKXZ` | `0x4F300` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1074 | `?InitializePropQualifierSet@CWbemInstance@@IEAAJPEAVCPropertyInformation@@AEAVCInstancePropertyQualifierSet@@@Z` | `0x4F330` | 269 | UnwindData |  |
| 89 | `??0CWbemObject@@IEAA@AEAVCDataTable@@AEAVCFastHeap@@AEAVCDerivationList@@@Z` | `0x4F460` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1100 | `?IsDecorated@CDecorationPart@@QEAAHXZ` | `0x4F500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `?GetStart@CBasicQualifierSet@@QEAAPEAEXZ` | `0x4F520` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `?GetHeap@CClassPart@@UEAAPEAVCFastHeap@@XZ` | `0x4F5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `?GetHeap@CInstancePart@@UEAAPEAVCFastHeap@@XZ` | `0x4F5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1134 | `?IsObjectInstance@CWbemObject@@UEAAJXZ` | `0x4F5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `?CloneRpcContext@CWbemThreadSecurityHandle@@QEAAJPEAUIServerSecurity@@@Z` | `0x4F5F0` | 530 | UnwindData |  |
| 1029 | `?GetThreadSecurity@CWbemCallSecurity@@UEAAJW4tag_WMI_THREAD_SECURITY_ORIGIN@@PEAPEAU_IWmiThreadSecHandle@@@Z` | `0x4F9C0` | 1,025 | UnwindData |  |
| 460 | `?CloneThreadContext@CWbemThreadSecurityHandle@@QEAAJK@Z` | `0x4FDD0` | 329 | UnwindData |  |
| 1306 | `?Release@CWbemCallSecurity@@UEAAKXZ` | `0x4FF20` | 67 | UnwindData |  |
| 1239 | `?QueryInterface@CWbemCallSecurity@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x4FF70` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `??1CWbemCallSecurity@@QEAA@XZ` | `0x50020` | 99 | UnwindData |  |
| 1308 | `?Release@CWbemThreadSecurityHandle@@UEAAKXZ` | `0x50090` | 65 | UnwindData |  |
| 159 | `??1CWbemThreadSecurityHandle@@QEAA@XZ` | `0x500E0` | 116 | UnwindData |  |
| 96 | `??0CWbemThreadSecurityHandle@@QEAA@AEBV0@@Z` | `0x50160` | 66 | UnwindData |  |
| 256 | `??4CWbemThreadSecurityHandle@@QEAAAEAV0@AEBV0@@Z` | `0x501B0` | 453 | UnwindData |  |
| 458 | `?CloneProcessContext@CWbemThreadSecurityHandle@@QEAAJXZ` | `0x50380` | 269 | UnwindData |  |
| 97 | `??0CWbemThreadSecurityHandle@@QEAA@PEAVCLifeControl@@@Z` | `0x50670` | 86 | UnwindData |  |
| 1068 | `?InitEmpty@CWbemClass@@QEAAJHH@Z` | `0x50830` | 285 | UnwindData |  |
| 551 | `?CreateEmpty@CWbemClass@@SAPEAEPEAE@Z` | `0x509A0` | 135 | UnwindData |  |
| 1117 | `?IsInstance@CWbemObject@@QEAAHXZ` | `0x50A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1559 | `?_GetCoreInfo@CWbemObject@@UEAAJJPEAPEAX@Z` | `0x50A50` | 45 | UnwindData |  |
| 1514 | `?UpperByte@CCompressedString@@KADG@Z` | `0x50A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1488 | `?Unlock@CWbemObject@@UEAAJJ@Z` | `0x50AA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1385 | `?SetInLineLength@CFastHeap@@IEAAXK@Z` | `0x50AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1116 | `?IsInstance@CDecorationPart@@QEAAHXZ` | `0x50AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1260 | `?Rebase@CFastHeap@@QEAAXPEAE@Z` | `0x50B10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `?IsArray@CType@@SAHK@Z` | `0x50B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1528 | `?ValidateBuffer@CQualifierSetList@@SA_KPEAE_KH@Z` | `0x50B50` | 241 | UnwindData |  |
| 1517 | `?ValidateBuffer@CBasicQualifierSet@@SA_KPEAE_K@Z` | `0x50C50` | 257 | UnwindData |  |
| 419 | `?CanContainDynamic@CClassPart@@UEAAJXZ` | `0x50D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `?CanContainDynamic@CInstancePQSContainer@@UEAAJXZ` | `0x50D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `?CanHaveCimtype@CClassPart@@UEAAHPEBG@Z` | `0x50D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `?CanHaveCimtype@CInstancePQSContainer@@UEAAHPEBG@Z` | `0x50D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `?CanHaveCimtype@CInstancePart@@UEAAHPEBG@Z` | `0x50D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `?CanHaveCimtype@CMethodQualifierSetContainer@@UEAAHPEBG@Z` | `0x50D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `?ClearWriteOnlyProperties@CWbemInstance@@UEAAJXZ` | `0x50D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 596 | `?DisabledValidateObject@CWbemObject@@KAJPEAV1@@Z` | `0x50D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 598 | `?DisconnectObject@CWbemObject@@UEAAJK@Z` | `0x50D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `?GetMinLength@CDataTable@@SAKXZ` | `0x50D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1473 | `?TranslateToNewHeap@CCompressedString@@QEAAHPEAVCFastHeap@@0@Z` | `0x50D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 932 | `?GetPropertyHandleEx@CWbemObject@@UEAAJPEBGJPEAJ1@Z` | `0x50DB0` | 171 | UnwindData |  |
| 931 | `?GetPropertyHandleEx@CClassPart@@QEAAJPEBGPEAJ1@Z` | `0x50E70` | 166 | UnwindData |  |
| 930 | `?GetPropertyHandle@CWbemObject@@UEAAJPEBGPEAJ1@Z` | `0x50F20` | 348 | UnwindData |  |
| 929 | `?GetPropertyHandle@CClassPart@@QEAAJPEBGPEAJ1@Z` | `0x51090` | 298 | UnwindData |  |
| 826 | `?GetLength@CQualifierSetList@@SAHPEAEH@Z` | `0x51270` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1568 | `DllCanUnloadNow` | `0x51700` | 205 | UnwindData |  |
| 1569 | `DllGetClassObject` | `0x517E0` | 310 | UnwindData |  |
| 820 | `?GetLength@CInstancePart@@QEAAHXZ` | `0x51C30` | 6,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1542 | `WbemStringCopy` | `0x53440` | 126 | UnwindData |  |
| 972 | `?GetQualifierSet@CWbemInstance@@UEAAJPEAPEAUIWbemQualifierSet@@@Z` | `0x539C0` | 225 | UnwindData |  |
| 890 | `?GetNumStrings@CCompressedStringList@@QEAAHXZ` | `0x53B00` | 84 | UnwindData |  |
| 877 | `?GetNext@CCompressedStringList@@QEAAPEAVCCompressedString@@PEAV2@@Z` | `0x53B60` | 125 | UnwindData |  |
| 1521 | `?ValidateBuffer@CDataTable@@SA_KPEAE_KH@Z` | `0x53BF0` | 243 | UnwindData |  |
| 824 | `?GetLength@CPropertyLookupTable@@QEAAHXZ` | `0x53CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `?IsClassPartInternal@CWbemInstance@@IEAAHXZ` | `0x53D10` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `?Rebase@CBasicQualifierSet@@QEAAXPEAE@Z` | `0x53DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `?Rebase@CDataTable@@QEAAXPEAE@Z` | `0x53E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `?GetTotalRealLength@CInstancePart@@QEAAKXZ` | `0x53E20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `?GetMemoryLimit@CInstancePart@@UEAAPEAEXZ` | `0x53E60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 860 | `?GetMethodQualifierSet@CWbemClass@@UEAAJPEBGPEAPEAUIWbemQualifierSet@@@Z` | `0x53EB0` | 229 | UnwindData |  |
| 856 | `?GetMethodQualifier@CWbemClass@@UEAAJPEBG0PEAVCVar@@PEAJ2@Z` | `0x53FA0` | 419 | UnwindData |  |
| 859 | `?GetMethodQualifierSet@CMethodPart@@QEAAJPEBGPEAPEAUIWbemQualifierSet@@@Z` | `0x54150` | 273 | UnwindData |  |
| 1238 | `?QueryInterface@CQualifierSet@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x54270` | 112 | UnwindData |  |
| 1358 | `?SetData@CMethodQualifierSet@@QEAAXPEAVCMethodPart@@0PEBG@Z` | `0x542F0` | 83 | UnwindData |  |
| 60 | `??0CMethodQualifierSet@@QEAA@XZ` | `0x54350` | 51 | UnwindData |  |
| 63 | `??0CMethodQualifierSetContainer@@QEAA@XZ` | `0x54390` | 50 | UnwindData |  |
| 1359 | `?SetData@CMethodQualifierSetContainer@@QEAAXPEAVCMethodPart@@0PEBG@Z` | `0x543D0` | 156 | UnwindData |  |
| 906 | `?GetPointer@CUntypedArray@@SAPEAV1@PEAVCPtrSource@@@Z` | `0x54480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `?GetMapped@CLimitationMapping@@QEAAPEAVCPropertyInformation@@PEAV2@@Z` | `0x544A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1545 | `?WriteDWORD@CWbemObject@@UEAAJJK@Z` | `0x544D0` | 455 | UnwindData |  |
| 1553 | `?WriteQWORD@CWbemObject@@UEAAJJ_K@Z` | `0x546A0` | 455 | UnwindData |  |
| 448 | `?ClearCachedKey@CWbemInstance@@QEAAXXZ` | `0x549A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `?ClearCachedKeyValue@CWbemInstance@@UEAAXXZ` | `0x549C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | `?EstimateUnmergeSpace@CClassPart@@QEAAKXZ` | `0x549E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 812 | `?GetLength@CClassPart@@QEAAKXZ` | `0x549E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `??0SHARED_LOCK_DATA@@QEAA@XZ` | `0x549F0` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `?GetBlockLength@CWbemInstance@@MEAAKXZ` | `0x54C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `?GetLength@CWbemInstance@@QEAAKXZ` | `0x54C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??0CInstancePQSContainer@@QEAA@XZ` | `0x54CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `?GetWbemObjectUnknown@CClassPart@@UEAAPEAUIUnknown@@XZ` | `0x54CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `?CreateOutOfLine@CFastHeap@@QEAAPEAEPEAEK@Z` | `0x54CE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `?GetNullnessLength@CDataTable@@QEAAKXZ` | `0x54D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `?GetClassNameW@CWbemClass@@UEAAJPEAVCVar@@@Z` | `0x54D30` | 267 | UnwindData |  |
| 739 | `?GetDerivation@CWbemObject@@UEAAJJKPEAK0PEAG@Z` | `0x54E50` | 806 | UnwindData |  |
| 148 | `??1CWbemClassCache@@QEAA@XZ` | `0x55240` | 54 | UnwindData |  |
| 446 | `?Clear@CWbemClassCache@@AEAAXXZ` | `0x55280` | 176 | UnwindData |  |
| 954 | `?GetQualifier@CInstancePart@@QEAAJPEBGPEAVCVar@@PEAJ2@Z` | `0x55510` | 308 | UnwindData |  |
| 1360 | `?SetData@CPropertyLookupTable@@QEAAXPEAEPEAVCPropertyTableContainer@@@Z` | `0x55680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `?IsComplete@CQualifierSet@@QEAAHXZ` | `0x55690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `?GetElement@CUntypedArray@@QEAAPEAEHH@Z` | `0x556B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 982 | `?GetRealLength@CFastHeap@@QEAAKXZ` | `0x556D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1352 | `?SetData@CCompressedStringList@@QEAAXPEAE@Z` | `0x55700` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `??1CWbemEnumMarshaling@@UEAA@XZ` | `0x55810` | 92 | UnwindData |  |
| 152 | `??1CWbemGuidToClassMap@@QEAA@XZ` | `0x55880` | 54 | UnwindData |  |
| 447 | `?Clear@CWbemGuidToClassMap@@AEAAXXZ` | `0x558E0` | 169 | UnwindData |  |
| 788 | `?GetInstanceObjectUnknown@CWbemInstance@@UEAAPEAUIUnknown@@XZ` | `0x55CE0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `?GetKnownQualifierLocally@CBasicQualifierSet@@QEAAPEAUCQualifier@@H@Z` | `0x55D30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `?EstimateDerivedPartSpace@CMethodPart@@QEAAKXZ` | `0x55DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 632 | `?EstimateUnmergeSpace@CMethodPart@@QEAAKXZ` | `0x55DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `?GetAllocatedDataLength@CFastHeap@@QEAAKXZ` | `0x55DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 823 | `?GetLength@CMethodPart@@QEAAKXZ` | `0x55DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `?GetPropertyLookup@CClassPart@@QEAAPEAUCPropertyLookup@@H@Z` | `0x55DB0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `?IsClassPartAvailable@CWbemInstance@@IEAAHXZ` | `0x55E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 949 | `?GetPropertyType@CWbemInstance@@UEAAJPEAVCPropertyInformation@@PEAJ1@Z` | `0x55E30` | 220 | UnwindData |  |
| 1110 | `?IsFakeAddress@CFastHeap@@SAHK@Z` | `0x55F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `?AugmentRequest@CFastHeap@@IEAAKKK@Z` | `0x55F30` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `?NextMapping@CLimitationMapping@@QEAAHPEAVCPropertyInformation@@0@Z` | `0x55F90` | 151 | UnwindData |  |
| 846 | `?GetMemoryLimit@CMethodPart@@UEAAPEAEXZ` | `0x56030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `?BeginEnumeration@CWbemObject@@UEAAJJ@Z` | `0x56050` | 465 | UnwindData |  |
| 1556 | `?WriteToStream@CWbemInstance@@UEAAJPEAUIStream@@@Z` | `0x56230` | 832 | UnwindData |  |
| 1557 | `?WriteToStream@CWbemObject@@UEAAJPEAUIStream@@@Z` | `0x56580` | 518 | UnwindData |  |
| 1119 | `?IsInstancePartAvailable@CWbemInstance@@IEAAHXZ` | `0x56790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `??ACFixedBSTRArray@@QEAAAEAPEAGH@Z` | `0x567A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 694 | `?GetAt@CFixedBSTRArray@@QEAAAEAPEAGH@Z` | `0x567A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `?IsDecorationPartAvailable@CWbemInstance@@IEAAHXZ` | `0x567C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1084 | `?IsArray@CType@@QEAAHXZ` | `0x567D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1059 | `?GetWbemObjectUnknown@CWbemInstance@@UEAAPEAUIUnknown@@XZ` | `0x567E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `?AreKeysRemoved@CDecorationPart@@QEAAHXZ` | `0x56850` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `?GetSuperclassName@CWbemClass@@UEAAJPEAVCVar@@@Z` | `0x56890` | 214 | UnwindData |  |
| 680 | `?GetActualType@CType@@QEAAKXZ` | `0x56970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `?GetQualifierSetStart@CInstancePart@@UEAAPEAEXZ` | `0x56980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `?GetMemoryLimit@CClassPart@@UEAAPEAEXZ` | `0x56990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `?Release@CClassQualifierSet@@UEAAKXZ` | `0x569B0` | 40 | UnwindData |  |
| 1303 | `?Release@CInstanceQualifierSet@@UEAAKXZ` | `0x569B0` | 40 | UnwindData |  |
| 841 | `?GetMarshalSizeMax@CWbemObject@@UEAAJAEBU_GUID@@PEAXK1KPEAK@Z` | `0x56A50` | 117 | UnwindData |  |
| 1242 | `?QueryObjectFlags@CWbemObject@@UEAAJJ_KPEA_K@Z` | `0x56AD0` | 724 | UnwindData |  |
| 1442 | `?SetThreadSecurity@CWbemCallSecurity@@UEAAJPEAU_IWmiThreadSecHandle@@@Z` | `0x56DB0` | 415 | UnwindData |  |
| 514 | `?CopyBlobOf@CWbemInstance@@UEAAJPEAVCWbemObject@@@Z` | `0x56F60` | 499 | UnwindData |  |
| 811 | `?GetLength@CClassAndMethods@@QEAAKXZ` | `0x57160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `?GetNumUpperBound@CBasicQualifierSet@@QEAAHXZ` | `0x57180` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??0CDecorationPart@@QEAA@XZ` | `0x571C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??0CInternalString@@QEAA@XZ` | `0x571C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `?AddRef@CQualifierSet@@UEAAKXZ` | `0x571D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1192 | `?MarshalInterface@CWbemObject@@UEAAJPEAUIStream@@AEBU_GUID@@PEAXK2K@Z` | `0x571F0` | 271 | UnwindData |  |
| 1268 | `?RebaseSecondarySet@CInstancePQSContainer@@QEAAXXZ` | `0x57310` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 836 | `?GetMap@CWbemGuidToClassMap@@QEAAJAEAVCGUID@@PEAPEAVCWbemClassToIdMap@@@Z` | `0x573F0` | 204 | UnwindData |  |
| 915 | `?GetPropQualifier@CWbemClass@@UEAAJPEAVCPropertyInformation@@PEBGPEAVCVar@@PEAJ3@Z` | `0x574D0` | 266 | UnwindData |  |
| 91 | `??0CWbemObjectArrayPacket@@QEAA@PEAEK_N@Z` | `0x59510` | 176 | UnwindData |  |
| 1094 | `?IsClassPartShared@CWbemInstance@@IEAAHXZ` | `0x595D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1062 | `?ImpersonateClient@CWbemCallSecurity@@UEAAJXZ` | `0x595F0` | 259 | UnwindData |  |
| 1369 | `?SetData@CWbemObjectArrayPacket@@QEAAXPEAEK_N@Z` | `0x59700` | 170 | UnwindData |  |
| 669 | `?Free@CFastHeap@@QEAAXKK@Z` | `0x59870` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 582 | `?Delete@CUntypedArray@@QEAAXVCType@@PEAVCFastHeap@@@Z` | `0x598A0` | 151 | UnwindData |  |
| 671 | `?FreeString@CFastHeap@@QEAAXK@Z` | `0x59940` | 86 | UnwindData |  |
| 580 | `?Delete@CBasicQualifierSet@@SAXPEAEPEAVCFastHeap@@@Z` | `0x599A0` | 89 | UnwindData |  |
| 944 | `?GetPropertyType@CClassPart@@QEAAJPEAVCPropertyInformation@@PEAJ1@Z` | `0x59A00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 947 | `?GetPropertyType@CWbemClass@@UEAAJPEAVCPropertyInformation@@PEAJ1@Z` | `0x59A00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1331 | `?RevertToSelf@CWbemCallSecurity@@UEAAJXZ` | `0x59A30` | 104 | UnwindData |  |
| 66 | `??0CQualifierSetListContainer@@QEAA@$$QEAV0@@Z` | `0x59AA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `??0CQualifierSetListContainer@@QEAA@AEBV0@@Z` | `0x59AA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `??0CQualifierSetListContainer@@QEAA@XZ` | `0x59AA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `?ComputeNecessarySpace@CDataTable@@SAKHH@Z` | `0x59AF0` | 22 | UnwindData |  |
| 516 | `?CopyInfo@CLimitationMapping@@IEAAXAEAVCPropertyInformation@@AEBV2@@Z` | `0x59B10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `?GetMaxMarshalStreamSize@CWbemInstance@@UEAAJPEAK@Z` | `0x59B40` | 213 | UnwindData |  |
| 722 | `?GetClassQualifier@CClassPart@@QEAAJPEBGPEAVCVar@@PEAJ2@Z` | `0x59C20` | 241 | UnwindData |  |
| 464 | `?Compact@CMethodPart@@QEAAXXZ` | `0x59D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1561 | `?fast_wcsncpy@CCompressedString@@SAPEAGPEAGPEBGH@Z` | `0x59D80` | 35 | UnwindData |  |
| 568 | `?CreateListOfEmpties@CQualifierSetList@@SAPEAEPEAEH@Z` | `0x59E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 912 | `?GetPropQualifier@CClassPart@@QEAAJPEAVCPropertyInformation@@PEBGPEAVCVar@@PEAJ3@Z` | `0x59E10` | 232 | UnwindData |  |
| 971 | `?GetQualifierSet@CWbemClass@@UEAAJPEAPEAUIWbemQualifierSet@@@Z` | `0x59F00` | 217 | UnwindData |  |
| 133 | `??1CBasicQualifierSet@@QEAA@XZ` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `??1CInstancePQSContainer@@QEAA@XZ` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `??1CWbemDataPacket@@QEAA@XZ` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `??1CWbemMtgtDeliverEventPacket@@QEAA@XZ` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `??1CWbemObjectArrayPacket@@QEAA@XZ` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `??1CWbemSmartEnumNextPacket@@QEAA@XZ` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `?ReduceClassAndMethodsSpace@CWbemClass@@QEAAXK@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1279 | `?ReduceClassPartSpace@CClassAndMethods@@UEAAXPEAVCClassPart@@K@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1280 | `?ReduceClassPartSpace@CWbemInstance@@UEAAXPEAVCClassPart@@K@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1282 | `?ReduceDataTableSpace@CInstancePart@@UEAAXPEAEKK@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1283 | `?ReduceHeapSize@CClassPart@@UEAAXPEAEKK@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1284 | `?ReduceHeapSize@CInstancePart@@UEAAXPEAEKK@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `?ReduceHeapSize@CMethodPart@@UEAAXPEAEKK@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1286 | `?ReduceInstancePartSpace@CWbemInstance@@UEAAXPEAVCInstancePart@@K@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `?ReduceMethodPartSpace@CClassAndMethods@@UEAAXPEAVCMethodPart@@K@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1288 | `?ReducePropertyTableSpace@CClassPart@@UEAAXPEAEKK@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `?ReduceQualifierSetListSpace@CInstancePart@@UEAAXPEAEKK@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `?ReduceQualifierSetSpace@CClassPart@@UEAAXPEAVCBasicQualifierSet@@K@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1293 | `?ReduceQualifierSetSpace@CMethodQualifierSetContainer@@UEAAXPEAVCBasicQualifierSet@@K@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1373 | `?SetDataLength@CInstancePart@@QEAAXK@Z` | `0x5A000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `?CheckLocalBoolQualifier@CClassPart@@QEAAHPEBG@Z` | `0x5A010` | 65 | UnwindData |  |
| 794 | `?GetKeyOrigin@CClassPart@@QEAAJAEAVWString2@@@Z` | `0x5A060` | 295 | UnwindData |  |
| 939 | `?GetPropertyOrigin@CWbemObject@@UEAAJPEBGPEAPEAG@Z` | `0x5A190` | 415 | UnwindData |  |
| 938 | `?GetPropertyOrigin@CClassPart@@QEAAJPEBGPEAPEAG@Z` | `0x5A340` | 350 | UnwindData |  |
| 696 | `?GetAtFromLast@CCompressedStringList@@QEAAPEAVCCompressedString@@H@Z` | `0x5A4B0` | 92 | UnwindData |  |
| 741 | `?GetDynasty@CClassPart@@QEAAJPEAVCVar@@@Z` | `0x5A520` | 304 | UnwindData |  |
| 742 | `?GetDynasty@CClassPart@@QEAAPEAVCCompressedString@@XZ` | `0x5A660` | 43 | UnwindData |  |
| 809 | `?GetLast@CCompressedStringList@@QEAAPEAVCCompressedString@@XZ` | `0x5A6A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1262 | `?Rebase@CMethodPart@@QEAAXPEAE@Z` | `0x5A6D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `?Copy@CFastHeap@@QEAAXKKK@Z` | `0x5A720` | 94 | UnwindData |  |
| 917 | `?GetPropQualifier@CWbemClass@@UEAAJPEBG0PEAVCVar@@PEAJ2@Z` | `0x5A790` | 112 | UnwindData |  |
| 1104 | `?IsDynamic@CWbemClass@@QEAAHXZ` | `0x5A810` | 75 | UnwindData |  |
| 238 | `??4CSharedLock@@QEAAAEAV0@$$QEAV0@@Z` | `0x5CA00` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `??4CSharedLock@@QEAAAEAV0@AEBV0@@Z` | `0x5CA00` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `??4SHMEM_HANDLE@@QEAAAEAU0@AEBU0@@Z` | `0x5CA00` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `??1CClassAndMethods@@QEAA@XZ` | `0x5CB10` | 22 | UnwindData |  |
| 1081 | `?IsAbstract@CWbemClass@@QEAAHXZ` | `0x5CBB0` | 69 | UnwindData |  |
| 748 | `?GetFirst@CCompressedStringList@@QEAAPEAVCCompressedString@@XZ` | `0x5CC00` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `??0CWbemEnumMarshaling@@QEAA@PEAVCLifeControl@@PEAUIUnknown@@@Z` | `0x5CDE0` | 89 | UnwindData |  |
| 108 | `??0XEnumMarshaling@CWbemEnumMarshaling@@QEAA@PEAV1@@Z` | `0x5CE40` | 39 | UnwindData |  |
| 84 | `??0CWbemGuidToClassMap@@QEAA@XZ` | `0x5CE70` | 72 | UnwindData |  |
| 8 | `??0?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@QEAA@PEAVCWbemRefreshingSvc@@@Z` | `0x5CF30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@QEAA@PEAVCWbemEnumMarshaling@@@Z` | `0x5CF30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??0?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@QEAA@PEAVCWmiObjectFactory@@@Z` | `0x5CF30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1122 | `?IsKeyed@CWbemClass@@UEAAHXZ` | `0x5CFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??0CMethodPart@@QEAA@XZ` | `0x5CFD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `?GetMaxMarshalStreamSize@CWbemObject@@UEAAJPEAK@Z` | `0x5D010` | 38 | UnwindData |  |
| 1527 | `?ValidateBuffer@CPropertyLookupTable@@SA_KPEAE_K@Z` | `0x5D040` | 266 | UnwindData |  |
| 607 | `?EndEnumeration@CWbemObject@@UEAAJXZ` | `0x5D1A0` | 72 | UnwindData |  |
| 717 | `?GetClassPart@CWbemClass@@MEAAPEAVCClassPart@@XZ` | `0x5D200` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1103 | `?IsDynamic@CClassPart@@QEAAHXZ` | `0x5D240` | 72 | UnwindData |  |
| 1083 | `?IsAmendment@CWbemClass@@QEAAHXZ` | `0x5D290` | 69 | UnwindData |  |
| 1080 | `?IsAbstract@CClassPart@@QEAAHXZ` | `0x5D2E0` | 66 | UnwindData |  |
| 635 | `?Extend@CFastHeap@@QEAAHKKK@Z` | `0x5D3C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1051 | `?GetWbemObjectUnknown@CClassAndMethods@@UEAAPEAUIUnknown@@XZ` | `0x5D400` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `??0CWbemCallSecurity@@QEAA@PEAVCLifeControl@@@Z` | `0x5D440` | 83 | UnwindData |  |
| 1241 | `?QueryInterface@CWbemThreadSecurityHandle@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x5D6E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1041 | `?GetUnmarshalClass@CWbemObject@@UEAAJAEBU_GUID@@PEAXK1KPEAU2@@Z` | `0x5D750` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `?MarshalPacket@CWbemSmartEnumNextPacket@@QEAAJPEAEKJPEAPEAUIWbemClassObject@@PEAU_GUID@@PEAH@Z` | `0x5D7A0` | 200 | UnwindData |  |
| 1082 | `?IsAmendment@CClassPart@@QEAAHXZ` | `0x5D8F0` | 66 | UnwindData |  |
| 541 | `?CreateEmpty@CBasicQualifierSet@@SAPEAEPEAE@Z` | `0x5D940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `?CreateEmpty@CCompressedStringList@@SAPEAEPEAE@Z` | `0x5D940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??0CClassPartContainer@@QEAA@$$QEAV0@@Z` | `0x5D960` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??0CClassPartContainer@@QEAA@AEBV0@@Z` | `0x5D960` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??0CClassPartContainer@@QEAA@XZ` | `0x5D960` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `?GetQualifier@CQualifierSet@@QEAAPEAUCQualifier@@PEBG@Z` | `0x5D9C0` | 20 | UnwindData |  |
| 1107 | `?IsEmpty@CCompressedStringList@@QEAAHXZ` | `0x5D9E0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `??4CInternalString@@QEAAAEAV0@AEBV0@@Z` | `0x5DDC0` | 58 | UnwindData |  |
| 47 | `??0CInternalString@@QEAA@AEBV0@@Z` | `0x5DE00` | 207 | UnwindData |  |
| 1018 | `?GetSuperclassName@CClassPart@@QEAAPEAVCCompressedString@@XZ` | `0x5DEE0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 698 | `?GetAuthentication@CWbemThreadSecurityHandle@@UEAAJPEAK@Z` | `0x5E130` | 120 | UnwindData |  |
| 77 | `??0CWbemDataPacket@@IEAA@XZ` | `0x5E1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??0CWbemMtgtDeliverEventPacket@@AEAA@XZ` | `0x5E1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `??0CWbemSmartEnumNextPacket@@AEAA@XZ` | `0x5E1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `?GetQualifierSetStart@CClassPart@@UEAAPEAEXZ` | `0x5E1D0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1415 | `?SetPropByHandle@CWbemObject@@UEAAJJJKPEAX@Z` | `0x5E290` | 1,478 | UnwindData |  |
| 141 | `??1CInternalString@@QEAA@XZ` | `0x5E890` | 26 | UnwindData |  |
| 1034 | `?GetTotalRealLength@CClassPart@@QEAAKXZ` | `0x5E8B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `?ReadQWORD@CWbemObject@@UEAAJJPEA_K@Z` | `0x5E900` | 397 | UnwindData |  |
| 907 | `?GetPrevious@CCompressedStringList@@QEAAPEAVCCompressedString@@PEAV2@@Z` | `0x5EAA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `?CalculateNecessarySpaceByType@CUntypedArray@@SAKVCType@@H@Z` | `0x5EAD0` | 26 | UnwindData |  |
| 884 | `?GetNumMethods@CMethodPart@@IEAAHXZ` | `0x5EBE0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `?GetClassPart@CWbemInstance@@MEAAPEAVCClassPart@@XZ` | `0x5ECF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `?CreateLimitedRepresentation@CDerivationList@@QEAAPEAEPEAVCLimitationMapping@@PEAE@Z` | `0x5ED20` | 69 | UnwindData |  |
| 395 | `?BeginEnumeration@CQualifierSet@@UEAAJJ@Z` | `0x5EDA0` | 512 | UnwindData |  |
| 1182 | `?MakeNotArray@CType@@SAKK@Z` | `0x5EFB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 969 | `?GetQualifierLocally@CBasicQualifierSet@@SAPEAUCQualifier@@PEAEPEAVCFastHeap@@PEBG@Z` | `0x5EFF0` | 25 | UnwindData |  |
| 1063 | `?IncrementLength@CBasicQualifierSet@@QEAAXK@Z` | `0x5F060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `?CompactAll@CWbemClass@@UEAAXXZ` | `0x5F080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `?GetBasic@CType@@QEAAKXZ` | `0x5F0A0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `?AddObjectToRefresher@CWbemRefreshingSvc@@MEAAJPEAU_WBEM_REFRESHER_ID@@PEBGJPEAUIWbemContext@@KPEAU_WBEM_REFRESH_INFO@@PEAK@Z` | `0x5F1C0` | 568 | UnwindData |  |
| 572 | `?CreateRefreshableObjectTemplate@CWbemRefreshingSvc@@IEAAJPEBGJPEAPEAUIWbemClassObject@@@Z` | `0x5F400` | 2,011 | UnwindData |  |
| 365 | `?AddObjectToRefresher_@CWbemRefreshingSvc@@IEAAJHPEAU_WBEM_REFRESHER_ID@@PEAVCWbemObject@@JPEAUIWbemContext@@PEAU_WBEM_REFRESH_INFO@@@Z` | `0x5FBF0` | 985 | UnwindData |  |
| 356 | `?AddEnumToRefresher@CWbemRefreshingSvc@@MEAAJPEAU_WBEM_REFRESHER_ID@@PEBGJPEAUIWbemContext@@KPEAU_WBEM_REFRESH_INFO@@PEAK@Z` | `0x5FFD0` | 1,141 | UnwindData |  |
| 1170 | `?IsWinmgmt@CWbemRefreshingSvc@@IEAAHPEAU_WBEM_REFRESHER_ID@@@Z` | `0x60450` | 38 | UnwindData |  |
| 358 | `?AddEnumToRefresher_@CWbemRefreshingSvc@@IEAAJHPEAU_WBEM_REFRESHER_ID@@PEAVCWbemObject@@PEBGJPEAUIWbemContext@@PEAU_WBEM_REFRESH_INFO@@@Z` | `0x60480` | 761 | UnwindData |  |
| 983 | `?GetRefrMgr@CWbemRefreshingSvc@@IEAAJPEAPEAU_IWbemRefresherMgr@@@Z` | `0x60780` | 247 | UnwindData |  |
| 1538 | `?ValidateRange@CWbemObject@@QEAAHPEAPEAG@Z` | `0x60880` | 88 | UnwindData |  |
| 1537 | `?ValidateRange@CPropertyLookupTable@@QEAAJPEAPEAGPEAVCDataTable@@PEAVCFastHeap@@@Z` | `0x608E0` | 439 | UnwindData |  |
| 1458 | `?SpawnKeyedInstance@CWbemClass@@UEAAJJPEBGPEAPEAU_IWmiObject@@@Z` | `0x61900` | 1,612 | UnwindData |  |
| 436 | `?CheapCompare@CCompressedString@@QEBAHAEBV1@@Z` | `0x62F00` | 87 | UnwindData |  |
| 1139 | `?IsParents@CType@@SAHK@Z` | `0x62F60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `??0CInstancePartContainer@@QEAA@$$QEAV0@@Z` | `0x62F90` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??0CInstancePartContainer@@QEAA@AEBV0@@Z` | `0x62F90` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `??0CInstancePartContainer@@QEAA@XZ` | `0x62F90` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `??0CMethodPartContainer@@QEAA@$$QEAV0@@Z` | `0x62F90` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??0CMethodPartContainer@@QEAA@AEBV0@@Z` | `0x62F90` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??0CMethodPartContainer@@QEAA@XZ` | `0x62F90` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `??1CLimitationMapping@@QEAA@XZ` | `0x63030` | 158 | UnwindData |  |
| 1178 | `?MakeArray@CType@@SAKK@Z` | `0x630E0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 832 | `?GetLengthByType@CUntypedArray@@QEAAKVCType@@@Z` | `0x631F0` | 29 | UnwindData |  |
| 706 | `?GetBlockLength@CWbemClass@@MEAAKXZ` | `0x63220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 829 | `?GetLength@CWbemClass@@QEAAKXZ` | `0x63220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `?GetSig@CMethodDescription@@QEAAKH@Z` | `0x63230` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `?AddRef@CWbemThreadSecurityHandle@@UEAAKXZ` | `0x63260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `?AddRef@CWbemCallSecurity@@UEAAKXZ` | `0x63280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 743 | `?GetDynasty@CWbemClass@@UEAAJPEAVCVar@@@Z` | `0x632A0` | 52 | UnwindData |  |
| 1130 | `?IsMemCopyAble@CType@@SAHGJ@Z` | `0x63310` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `?Release@CMethodQualifierSet@@UEAAKXZ` | `0x633A0` | 79 | UnwindData |  |
| 143 | `??1CMethodQualifierSet@@UEAA@XZ` | `0x63400` | 36 | UnwindData |  |
| 144 | `??1CMethodQualifierSetContainer@@QEAA@XZ` | `0x63430` | 29 | UnwindData |  |
| 1295 | `?Release@?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@UEAAKXZ` | `0x63460` | 42 | UnwindData |  |
| 1296 | `?Release@?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@UEAAKXZ` | `0x63460` | 42 | UnwindData |  |
| 1297 | `?Release@?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@UEAAKXZ` | `0x63460` | 42 | UnwindData |  |
| 1298 | `?Release@?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@UEAAKXZ` | `0x63460` | 42 | UnwindData |  |
| 1299 | `?Release@?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@UEAAKXZ` | `0x63460` | 42 | UnwindData |  |
| 1300 | `?Release@?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@UEAAKXZ` | `0x63460` | 42 | UnwindData |  |
| 1301 | `?Release@?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@UEAAKXZ` | `0x63460` | 42 | UnwindData |  |
| 754 | `?GetGenus@CWbemClass@@UEAAJPEAVCVar@@@Z` | `0x63490` | 32 | UnwindData |  |
| 369 | `?AddRef@?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@UEAAKXZ` | `0x634F0` | 42 | UnwindData |  |
| 370 | `?AddRef@?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@UEAAKXZ` | `0x634F0` | 42 | UnwindData |  |
| 371 | `?AddRef@?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@UEAAKXZ` | `0x634F0` | 42 | UnwindData |  |
| 372 | `?AddRef@?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@UEAAKXZ` | `0x634F0` | 42 | UnwindData |  |
| 373 | `?AddRef@?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@UEAAKXZ` | `0x634F0` | 42 | UnwindData |  |
| 374 | `?AddRef@?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@UEAAKXZ` | `0x634F0` | 42 | UnwindData |  |
| 375 | `?AddRef@?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@UEAAKXZ` | `0x634F0` | 42 | UnwindData |  |
| 966 | `?GetQualifierLocally@CBasicQualifierSet@@QEAAPEAUCQualifier@@PEBG@Z` | `0x639C0` | 25 | UnwindData |  |
| 70 | `??0CType@@QEAA@XZ` | `0x63A00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 755 | `?GetGenus@CWbemInstance@@UEAAJPEAVCVar@@@Z` | `0x63A80` | 32 | UnwindData |  |
| 1186 | `?Map@CLimitationMapping@@QEAAXPEAVCPropertyInformation@@0H@Z` | `0x63E60` | 442 | UnwindData |  |
| 768 | `?GetHeap@CPropertyLookupTable@@QEAAPEAVCFastHeap@@XZ` | `0x640A0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??0CWbemRefreshingSvc@@QEAA@PEAVCLifeControl@@PEAUIUnknown@@@Z` | `0x64240` | 162 | UnwindData |  |
| 120 | `??0XWbemRefrSvc@CWbemRefreshingSvc@@QEAA@PEAV1@@Z` | `0x642F0` | 39 | UnwindData |  |
| 105 | `??0XCfgRefrSrvc@CWbemRefreshingSvc@@QEAA@PEAV1@@Z` | `0x64320` | 39 | UnwindData |  |
| 4 | `??0?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@QEAA@PEAVCWbemRefreshingSvc@@@Z` | `0x64350` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1047 | `?GetVARTYPE@CType@@QEAAGXZ` | `0x643A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `?QueryInterface@?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x643B0` | 65 | UnwindData |  |
| 1232 | `?QueryInterface@?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x643B0` | 65 | UnwindData |  |
| 1233 | `?QueryInterface@?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x643B0` | 65 | UnwindData |  |
| 1234 | `?QueryInterface@?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x643B0` | 65 | UnwindData |  |
| 1235 | `?QueryInterface@?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x643B0` | 65 | UnwindData |  |
| 1236 | `?QueryInterface@?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x643B0` | 65 | UnwindData |  |
| 1237 | `?QueryInterface@?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x643B0` | 65 | UnwindData |  |
| 1377 | `?SetDecoration@CWbemObject@@UEAAJPEBG0@Z` | `0x64600` | 119 | UnwindData |  |
| 1124 | `?IsLimited@CDecorationPart@@QEAAHXZ` | `0x64680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `?GetInterface@CWbemEnumMarshaling@@MEAAPEAXAEBU_GUID@@@Z` | `0x646A0` | 1,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1142 | `?IsPossibleSystemPropertyName@CSystemProperties@@SAHPEBG@Z` | `0x64D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 922 | `?GetProperty@CWbemClass@@MEAAJPEAVCPropertyInformation@@PEAVCVar@@@Z` | `0x64DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | `?GetMarshalPacket@XEnumMarshaling@CWbemEnumMarshaling@@UEAAJAEBU_GUID@@KPEAPEAUIWbemClassObject@@PEAKPEAPEAE@Z` | `0x64DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `?SetVtableLength@CLimitationMapping@@QEAAXKH@Z` | `0x64DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 657 | `?FindLimitationError@CWbemClass@@QEAA?AVWString@@JPEAVCWStringArray@@@Z` | `0x64E00` | 218 | UnwindData |  |
| 960 | `?GetQualifier@CWbemClass@@UEAAJPEBGPEAVCVar@@PEAJ2@Z` | `0x64F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `??MCInternalString@@QEBA_NAEBV0@@Z` | `0x64F50` | 24 | UnwindData |  |
| 1223 | `?PlugKeyHoles@CWbemInstance@@QEAAJXZ` | `0x64F70` | 453 | UnwindData |  |
| 1243 | `?QueryPartInfo@CWbemObject@@UEAAJPEAK@Z` | `0x652E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `?BeginMethodEnumeration@CWbemClass@@UEAAJJ@Z` | `0x652F0` | 211 | UnwindData |  |
| 1013 | `?GetStart@CWbemInstance@@QEAAPEAEXZ` | `0x653F0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1014 | `?GetStart@CWbemObject@@QEAAPEAEXZ` | `0x653F0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `?EndMethodEnumeration@CWbemClass@@UEAAJXZ` | `0x655D0` | 208 | UnwindData |  |
| 1543 | `WbemStringFree` | `0x656E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | `?GetKeyProps@CWbemClass@@UEAAHAEAVCWStringArray@@@Z` | `0x65700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `?AcquireCompressedString@CInternalString@@QEAAXPEAVCCompressedString@@@Z` | `0x65720` | 46 | UnwindData |  |
| 1137 | `?IsParentClass@CWbemInstance@@UEAAJJPEAU_IWmiObject@@@Z` | `0x65760` | 207 | UnwindData |  |
| 1118 | `?IsInstanceOf@CWbemInstance@@QEAAHPEAVCWbemClass@@@Z` | `0x65840` | 184 | UnwindData |  |
| 400 | `?Build@CLimitationMapping@@QEAAXH@Z` | `0x65920` | 241 | UnwindData |  |
| 515 | `?CopyData@CCompressedStringList@@QEAAPEAEPEAE@Z` | `0x65A20` | 55 | UnwindData |  |
| 730 | `?GetDataTable@CClassPart@@UEAAPEAVCDataTable@@XZ` | `0x65A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `?CreateDerivedClass@CWbemClass@@QEAAJPEAV1@HPEAVCDecorationPart@@@Z` | `0x65A70` | 280 | UnwindData |  |
| 1454 | `?SpawnDerivedClass@CWbemClass@@UEAAJJPEAPEAUIWbemClassObject@@@Z` | `0x65B90` | 624 | UnwindData |  |
| 535 | `?CreateDerivedClass@CWbemClass@@QEAAJPEAPEAV1@@Z` | `0x65E10` | 747 | UnwindData |  |
| 1546 | `?WriteDerivedClass@CWbemClass@@QEAAJPEAEHPEAVCDecorationPart@@@Z` | `0x66110` | 295 | UnwindData |  |
| 537 | `?CreateDerivedPart@CClassAndMethods@@QEAAPEAEPEAEK@Z` | `0x66240` | 88 | UnwindData |  |
| 616 | `?EstimateDerivedClassSpace@CWbemClass@@QEAAKPEAVCDecorationPart@@@Z` | `0x662A0` | 88 | UnwindData |  |
| 617 | `?EstimateDerivedPartSpace@CClassAndMethods@@QEAAKXZ` | `0x66300` | 33 | UnwindData |  |
| 618 | `?EstimateDerivedPartSpace@CClassPart@@QEAAKXZ` | `0x66330` | 34 | UnwindData |  |
| 620 | `?EstimateExtraSpace@CCompressedStringList@@SAKPEAVCCompressedString@@@Z` | `0x66360` | 27 | UnwindData |  |
| 538 | `?CreateDerivedPart@CClassPart@@QEAAPEAEPEAEH@Z` | `0x66390` | 343 | UnwindData |  |
| 577 | `?CreateWithExtra@CCompressedStringList@@QEAAPEAEPEAEPEAVCCompressedString@@@Z` | `0x664F0` | 158 | UnwindData |  |
| 1550 | `?WritePropagatedVersion@CPropertyLookupTable@@QEAAPEAEPEAVCFastHeap@@PEAE0@Z` | `0x665A0` | 152 | UnwindData |  |
| 539 | `?CreateDerivedPart@CMethodPart@@QEAAPEAEPEAEK@Z` | `0x66640` | 314 | UnwindData |  |
| 1549 | `?WritePropagatedVersion@CDataTable@@QEAAPEAEPEAVCPropertyLookupTable@@PEAVCFastHeap@@PEAE1@Z` | `0x66780` | 242 | UnwindData |  |
| 540 | `?CreateDerivedVersion@CMethodDescription@@SAHPEFAU1@0PEAVCFastHeap@@1@Z` | `0x66880` | 257 | UnwindData |  |
| 716 | `?GetClassObject@CWbemObjectArrayPacket@@AEAAJAEAVCWbemObjectPacket@@PEAPEAUIWbemClassObject@@@Z` | `0x669A0` | 180 | UnwindData |  |
| 69 | `??0CType@@QEAA@K@Z` | `0x66A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1140 | `?IsPointerType@CType@@QEAAHXZ` | `0x66A70` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `?MakeParents@CType@@SAKK@Z` | `0x66BB0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `??1CWbemRefreshingSvc@@UEAA@XZ` | `0x66C40` | 114 | UnwindData |  |
| 1309 | `?ReleaseElement@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@IEAAXPEAVCWmiTextSource@@@Z` | `0x66F20` | 23 | UnwindData |  |
| 131 | `??1?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAA@XZ` | `0x66F90` | 39 | UnwindData |  |
| 1312 | `?RemoveAll@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXXZ` | `0x66FC0` | 142 | UnwindData |  |
| 355 | `?Add@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAHPEAVCWmiTextSource@@@Z` | `0x67890` | 74 | UnwindData |  |
| 626 | `?EstimateMergeSpace@CMethodPart@@SAKAEAV1@0@Z` | `0x679B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 715 | `?GetClassNameW@CWbemInstance@@UEAAJPEAVCVar@@@Z` | `0x67A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `?Lock@CHiPerfLock@@QEAAHK@Z` | `0x67A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1437 | `?SetServiceData@CWbemRefreshingSvc@@MEAAJPEAG0@Z` | `0x67A30` | 406 | UnwindData |  |
| 393 | `?AsymmetricMerge@CWbemInstance@@SAJPEAV1@0@Z` | `0x67C10` | 665 | UnwindData |  |
| 624 | `?EstimateMergeSpace@CClassAndMethods@@SAKAEAV1@0@Z` | `0x67EB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | `?GetInterface@CWbemRefreshingSvc@@MEAAPEAXAEBU_GUID@@@Z` | `0x67EE0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1503 | `?Unmerge@CWbemObject@@UEAAJJKPEAKPEAX@Z` | `0x67F50` | 400 | UnwindData |  |
| 277 | `??8CInternalString@@QEBA_NAEBV0@@Z` | `0x680F0` | 26 | UnwindData |  |
| 1179 | `?MakeFakeFromIndex@CFastHeap@@SAKH@Z` | `0x68160` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `?CreateEmpty@CDecorationPart@@QEAAPEAEEPEAE@Z` | `0x68190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `?GetPropName@CWbemClass@@UEAAJHPEAVCVar@@@Z` | `0x681B0` | 72 | UnwindData |  |
| 1486 | `?Unlock@CHiPerfLock@@QEAAHXZ` | `0x68200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `?EstimateMergeSpace@CClassPart@@SAKAEAV1@0@Z` | `0x68210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 883 | `?GetNumMappings@CLimitationMapping@@QEAAHXZ` | `0x68240` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 998 | `?GetSize@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEBAHXZ` | `0x68240` | 1,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `??0CWmiObjectFactory@@QEAA@PEAVCLifeControl@@PEAUIUnknown@@@Z` | `0x68940` | 59 | UnwindData |  |
| 114 | `??0XObjectFactory@CWmiObjectFactory@@QEAA@PEAV1@@Z` | `0x68990` | 39 | UnwindData |  |
| 573 | `?CreateUnmergedVersion@CMethodDescription@@SAHPEFAU1@0PEAVCFastHeap@@1@Z` | `0x68A10` | 232 | UnwindData |  |
| 1500 | `?Unmerge@CWbemClass@@UEAAJPEAEHPEAK@Z` | `0x68B00` | 285 | UnwindData |  |
| 1494 | `?Unmerge@CClassAndMethods@@QEAAPEAEPEAEK@Z` | `0x68C30` | 88 | UnwindData |  |
| 1498 | `?Unmerge@CMethodPart@@QEAAPEAEPEAEK@Z` | `0x68C90` | 395 | UnwindData |  |
| 1495 | `?Unmerge@CClassPart@@QEAAPEAEPEAEH@Z` | `0x68E30` | 443 | UnwindData |  |
| 1499 | `?Unmerge@CPropertyLookupTable@@QEAAPEAEPEAVCDataTable@@PEAVCFastHeap@@PEAE1@Z` | `0x69000` | 210 | UnwindData |  |
| 1493 | `?Unmerge@CBasicQualifierSet@@SAPEAEPEAEPEAVCFastHeap@@01@Z` | `0x69190` | 185 | UnwindData |  |
| 1497 | `?Unmerge@CDerivationList@@QEAAPEAEPEAE@Z` | `0x69250` | 110 | UnwindData |  |
| 1496 | `?Unmerge@CDataTable@@QEAAPEAEPEAVCPropertyLookupTable@@PEAVCFastHeap@@PEAE1@Z` | `0x692D0` | 240 | UnwindData |  |
| 1153 | `?IsTouched@CMethodDescription@@SAHPEFAU1@PEAVCFastHeap@@@Z` | `0x693D0` | 55 | UnwindData |  |
| 1515 | `?VARTYPEToType@CType@@SA?AV1@G@Z` | `0x69660` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1112 | `?IsIdenticalWith@CClassPart@@QEAAHAEAV1@@Z` | `0x69810` | 216 | UnwindData |  |
| 965 | `?GetQualifierLocally@CBasicQualifierSet@@QEAAPEAUCQualifier@@PEAVCCompressedString@@@Z` | `0x69940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `?IsPropagated@CMethodPart@@IEAAHH@Z` | `0x69960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1125 | `?IsLimited@CWbemObject@@QEAAHXZ` | `0x69980` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `?GetLength@CEmbeddedObject@@QEAAKXZ` | `0x69BD0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `?MarkKeyRemoval@CDecorationPart@@SAXPEAE@Z` | `0x69D10` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 902 | `?GetParentAtIndex@CWbemObject@@QEAAPEAVCCompressedString@@H@Z` | `0x69E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `?GetWbemObjectUnknown@CMethodQualifierSetContainer@@UEAAPEAUIUnknown@@XZ` | `0x69E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1129 | `?IsLocalized@CWbemInstance@@UEAAHXZ` | `0x69E70` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `?GetRelPath@CWbemClass@@UEAAPEAGH@Z` | `0x69FA0` | 101 | UnwindData |  |
| 1126 | `?IsLocalized@CClassPart@@QEAAHXZ` | `0x6A010` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `?GetSecondarySet@CMethodQualifierSetContainer@@QEAAPEAVCBasicQualifierSet@@XZ` | `0x6A050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1055 | `?GetWbemObjectUnknown@CMethodPart@@QEAAPEAUIUnknown@@XZ` | `0x6A080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 727 | `?GetCurrentOrigin@CClassPart@@UEAAKXZ` | `0x6A0A0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1216 | `?New@CWbemCallSecurity@@SAPEAV1@XZ` | `0x6A1D0` | 81 | UnwindData |  |
| 1154 | `?IsTouched@CMethodPart@@QEAAHHPEAH@Z` | `0x6A230` | 111 | UnwindData |  |
| 543 | `?CreateEmpty@CClassPart@@SAPEAEPEAE@Z` | `0x6A2B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `?GetHeap@CMethodQualifierSetContainer@@UEAAPEAVCFastHeap@@XZ` | `0x6A2F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `??0CWmiTextSourceArray@@QEAA@XZ` | `0x6A380` | 29 | UnwindData |  |
| 18 | `??0?$CRefedPointerArray@VCWmiTextSource@@@@QEAA@XZ` | `0x6A3B0` | 45 | UnwindData |  |
| 494 | `?ComputeMergeSpace@CBasicQualifierSet@@SAKPEAEPEAVCFastHeap@@01H@Z` | `0x6A3F0` | 175 | UnwindData |  |
| 1396 | `?SetLocalized@CClassPart@@QEAAXH@Z` | `0x6A4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 673 | `?Get@CWbemFetchRefrMgr@@QEAAJPEAPEAU_IWbemRefresherMgr@@@Z` | `0x6A4D0` | 396 | UnwindData |  |
| 1480 | `?Unbind@CInternalString@@QEAAXXZ` | `0x6A680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `?GetNameAsBSTR@CSystemProperties@@SAPEAGH@Z` | `0x6A690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 729 | `?GetDataLength@CDataTable@@QEAAKXZ` | `0x6A6B0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1398 | `?SetLocalized@CWbemClass@@UEAAXH@Z` | `0x6A740` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `??0CWbemFetchRefrMgr@@QEAA@PEAVCLifeControl@@PEAUIUnknown@@@Z` | `0x6A980` | 59 | UnwindData |  |
| 111 | `??0XFetchRefrMgr@CWbemFetchRefrMgr@@QEAA@PEAV1@@Z` | `0x6A9D0` | 39 | UnwindData |  |
| 6 | `??0?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@QEAA@PEAVCWbemRemoteRefresher@@@Z` | `0x6AA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@QEAA@PEAVCWbemFetchRefrMgr@@@Z` | `0x6AA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 634 | `?EstimateUnmergeSpace@CWbemInstance@@UEAAKXZ` | `0x6AA20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `?IsClientOnly@CDecorationPart@@QEAAHXZ` | `0x6AA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `?IsClientOnly@CWbemObject@@QEAAHXZ` | `0x6AA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `?GetIndexedProps@CWbemClass@@UEAAHAEAVCWStringArray@@@Z` | `0x6AAB0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `?CreateEmpty@CClassAndMethods@@SAPEAEPEAE@Z` | `0x6AC20` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `?Init@CWbemFetchRefrMgr@@QEAAJPEAU_IWmiProvSS@@PEAUIWbemServices@@@Z` | `0x6AD90` | 351 | UnwindData |  |
| 549 | `?CreateEmpty@CMethodPart@@SAPEAEPEAE@Z` | `0x6AF00` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `?CreateEmpty@CFastHeap@@SAPEAEPEAE@Z` | `0x6AFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1123 | `?IsKeyed@CWbemInstance@@UEAAHXZ` | `0x6B000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `?Compare@CBasicQualifierSet@@QEAAHAEAV1@EPEAPEBGK@Z` | `0x6B020` | 1,554 | UnwindData |  |
| 887 | `?GetNumProperties@CWbemClass@@UEAAHXZ` | `0x6B640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1136 | `?IsParentClass@CWbemClass@@UEAAJJPEAU_IWmiObject@@@Z` | `0x6B660` | 198 | UnwindData |  |
| 1091 | `?IsChildOf@CWbemClass@@QEAAHPEAV1@@Z` | `0x6B730` | 184 | UnwindData |  |
| 872 | `?GetName@CMethodPart@@IEAAPEAVCCompressedString@@H@Z` | `0x6B840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `??1XCfgRefrSrvc@CWbemRefreshingSvc@@QEAA@XZ` | `0x6B860` | 17 | UnwindData |  |
| 163 | `??1XEnumMarshaling@CWbemEnumMarshaling@@QEAA@XZ` | `0x6B860` | 17 | UnwindData |  |
| 165 | `??1XObjectFactory@CWmiObjectFactory@@QEAA@XZ` | `0x6B860` | 17 | UnwindData |  |
| 744 | `?GetDynasty@CWbemInstance@@UEAAJPEAVCVar@@@Z` | `0x6B8A0` | 52 | UnwindData |  |
| 151 | `??1CWbemFetchRefrMgr@@UEAA@XZ` | `0x6B960` | 54 | UnwindData |  |
| 1127 | `?IsLocalized@CInstancePart@@QEAAHXZ` | `0x6BA50` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `??1XWbemRefrSvc@CWbemRefreshingSvc@@QEAA@XZ` | `0x6BAF0` | 17 | UnwindData |  |
| 117 | `??0XObjectTextSrc@CWmiObjectTextSrc@@QEAA@PEAV1@@Z` | `0x6BCB0` | 39 | UnwindData |  |
| 1507 | `?Update@CQualifierSet@@QEAAJAEAVCBasicQualifierSet@@JPEAVCFixedBSTRArray@@@Z` | `0x6BF70` | 1,056 | UnwindData |  |
| 1184 | `?MakeSubsetInst@CWbemClass@@UEAAJPEAU_IWmiObject@@PEAPEAU2@@Z` | `0x6C3C0` | 256 | UnwindData |  |
| 1438 | `?SetServiceData@XCfgRefrSrvc@CWbemRefreshingSvc@@UEAAJPEAG0@Z` | `0x6C4E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1114 | `?IsImpersonating@CWbemCallSecurity@@UEAAHXZ` | `0x6C520` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1109 | `?IsEmpty@CQualifierSetList@@QEAAHXZ` | `0x6CDA0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1148 | `?IsSingleton@CClassPart@@QEAAHXZ` | `0x6CE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `?Compare@CQualifierSet@@QEAAHAEAV1@PEAVCFixedBSTRArray@@H@Z` | `0x6CE50` | 1,310 | UnwindData |  |
| 927 | `?GetPropertyCount@CWbemClass@@UEAAJPEAVCVar@@@Z` | `0x6D390` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1277 | `?Reduce@CFastHeap@@QEAAXKKK@Z` | `0x6D3F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1345 | `?SetClassQualifier@CClassPart@@QEAAJPEBGPEAVCVar@@J@Z` | `0x6D420` | 366 | UnwindData |  |
| 550 | `?CreateEmpty@CPropertyLookupTable@@SAPEAEPEAE@Z` | `0x6D7B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `?GetText@CBasicQualifierSet@@QEAAJJAEAVWString@@@Z` | `0x6D810` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 790 | `?GetInterface@CWbemFetchRefrMgr@@MEAAPEAXAEBU_GUID@@@Z` | `0x6D960` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `?DoesSignatureMatchOther@CMethodPart@@IEAAHAEAV1@HW4METHOD_SIGNATURE_TYPE@@@Z` | `0x6DA60` | 166 | UnwindData |  |
| 603 | `?Empty@CFastHeap@@QEAAXXZ` | `0x6DB70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1420 | `?SetPropQualifier@CWbemClass@@UEAAJPEBG0JPEAVCVar@@@Z` | `0x6DBD0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `?QueryBlanket@CWbemCallSecurity@@UEAAJPEAK0PEAPEAG00PEAPEAX0@Z` | `0x6E180` | 261 | UnwindData |  |
| 645 | `?ExtendMethodPartSpace@CClassAndMethods@@UEAAHPEAVCMethodPart@@K@Z` | `0x6E290` | 51 | UnwindData |  |
| 416 | `?CanContainAbstract@CInstancePQSContainer@@UEAAJH@Z` | `0x6E2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `?CanContainAbstract@CInstancePart@@UEAAJH@Z` | `0x6E2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `?CanContainAbstract@CMethodQualifierSetContainer@@UEAAJH@Z` | `0x6E2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `?CanContainDynamic@CInstancePart@@UEAAJXZ` | `0x6E2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `?CanContainDynamic@CMethodQualifierSetContainer@@UEAAJXZ` | `0x6E2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `?CanContainKey@CClassPart@@UEAAJXZ` | `0x6E2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `?CanContainKey@CInstancePQSContainer@@UEAAJXZ` | `0x6E2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `?CanContainKey@CInstancePart@@UEAAJXZ` | `0x6E2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `?CanContainKey@CMethodQualifierSetContainer@@UEAAJXZ` | `0x6E2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `?CanContainSingleton@CInstancePQSContainer@@UEAAJXZ` | `0x6E2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `?CanContainSingleton@CInstancePart@@UEAAJXZ` | `0x6E2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `?CanContainSingleton@CMethodQualifierSetContainer@@UEAAJXZ` | `0x6E2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??0?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAA@AEBV?$CReferenceManager@VCWmiTextSource@@@@@Z` | `0x6E350` | 45 | UnwindData |  |
| 928 | `?GetPropertyCount@CWbemInstance@@UEAAJPEAVCVar@@@Z` | `0x6E3E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `?CalculateNecessarySpaceByLength@CUntypedArray@@SAKHH@Z` | `0x6E420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `?CanContainAbstract@CClassPart@@UEAAJH@Z` | `0x6E430` | 368 | UnwindData |  |
| 831 | `?GetLengthByActualLength@CUntypedArray@@QEAAKH@Z` | `0x6E5B0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1439 | `?SetSig@CMethodDescription@@QEAAXHK@Z` | `0x6E6F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1020 | `?GetSuperclassName@CWbemInstance@@UEAAJPEAVCVar@@@Z` | `0x6E720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 643 | `?ExtendHeapSize@CMethodPart@@UEAAHPEAEKK@Z` | `0x6E740` | 66 | UnwindData |  |
| 792 | `?GetInterface@CWmiObjectFactory@@MEAAPEAXAEBU_GUID@@@Z` | `0x6E7B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??0CHiPerfLock@@QEAA@XZ` | `0x6E820` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `?CanBeReconciledWith@CBasicQualifierSet@@QEAAHAEAV1@@Z` | `0x6E880` | 571 | UnwindData |  |
| 675 | `?Get@XFetchRefrMgr@CWbemFetchRefrMgr@@UEAAJPEAPEAU_IWbemRefresherMgr@@@Z` | `0x6EE70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1397 | `?SetLocalized@CInstancePart@@QEAAXH@Z` | `0x6EEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1429 | `?SetQualifier@CWbemClass@@UEAAJPEBGPEAVCVar@@J@Z` | `0x6EEC0` | 127 | UnwindData |  |
| 740 | `?GetDescription@CWbemObject@@UEAAJPEAPEAG@Z` | `0x6EF50` | 219 | UnwindData |  |
| 1346 | `?SetClientOnly@CDecorationPart@@QEAAXXZ` | `0x6F040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1347 | `?SetClientOnly@CWbemObject@@QEAAXXZ` | `0x6F060` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `?AddText@CMethodPart@@QEAAJAEAVWString@@J@Z` | `0x6F0B0` | 233 | UnwindData |  |
| 160 | `??1CWmiObjectFactory@@UEAA@XZ` | `0x6F220` | 54 | UnwindData |  |
| 1399 | `?SetLocalized@CWbemInstance@@UEAAXH@Z` | `0x6F260` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `??BCInternalString@@QEBA?AVWString@@XZ` | `0x6F440` | 45 | UnwindData |  |
| 161 | `??1CWmiTextSourceArray@@QEAA@XZ` | `0x6F480` | 18 | UnwindData |  |
| 132 | `??1?$CRefedPointerArray@VCWmiTextSource@@@@QEAA@XZ` | `0x6F4A0` | 18 | UnwindData |  |
| 399 | `?BeginMethodEnumeration@CWbemInstance@@UEAAJJ@Z` | `0x6F4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 587 | `?DeleteMethod@CWbemInstance@@UEAAJPEBG@Z` | `0x6F4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `?EndMethodEnumeration@CWbemInstance@@UEAAJXZ` | `0x6F4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `?GetMethod@CWbemInstance@@UEAAJPEBGJPEAPEAUIWbemClassObject@@1@Z` | `0x6F4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `?GetMethodOrigin@CWbemInstance@@UEAAJPEBGPEAPEAG@Z` | `0x6F4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 861 | `?GetMethodQualifierSet@CWbemInstance@@UEAAJPEBGPEAPEAUIWbemQualifierSet@@@Z` | `0x6F4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1222 | `?NextMethod@CWbemInstance@@UEAAJJPEAPEAGPEAPEAUIWbemClassObject@@1@Z` | `0x6F4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `?PutMethod@CWbemInstance@@UEAAJPEBGJPEAUIWbemClassObject@@1@Z` | `0x6F4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1391 | `?SetInheritanceChain@CWbemInstance@@UEAAJJPEAPEAG@Z` | `0x6F4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `?SetMethodOrigin@CWbemInstance@@UEAAJPEBGJ@Z` | `0x6F4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1427 | `?SetPropertyOrigin@CWbemInstance@@UEAAJPEBGJ@Z` | `0x6F4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `?AddEnumToRefresher@XWbemRefrSvc@CWbemRefreshingSvc@@UEAAJPEAU_WBEM_REFRESHER_ID@@PEBGJPEAUIWbemContext@@KPEAU_WBEM_REFRESH_INFO@@PEAK@Z` | `0x6F4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `?EstimateUnmergeSpace@CWbemClass@@UEAAKXZ` | `0x6F4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `?EstimateUnmergeSpace@CClassAndMethods@@QEAAKXZ` | `0x6F500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `?Delete@CWbemInstance@@UEAAJPEBG@Z` | `0x6F520` | 561 | UnwindData |  |
| 718 | `?GetClassPart@CWbemClass@@UEAAJPEAXKPEAK@Z` | `0x6F810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `?GetObjectParts@CWbemClass@@UEAAJPEAXKKPEAK@Z` | `0x6F810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | `?GetPropQualifier@CWbemClass@@UEAAJPEAVCPropertyInformation@@PEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x6F810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `?MergeClassPart@CWbemClass@@UEAAJPEAUIWbemClassObject@@@Z` | `0x6F810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1342 | `?SetClassPart@CWbemClass@@UEAAJPEAXK@Z` | `0x6F810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1412 | `?SetObjectParts@CWbemClass@@UEAAJPEAXKK@Z` | `0x6F810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1467 | `?StripClassPart@CWbemClass@@UEAAJXZ` | `0x6F810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `??1XFetchRefrMgr@CWbemFetchRefrMgr@@QEAA@XZ` | `0x6F820` | 17 | UnwindData |  |
| 168 | `??1XWbemRemoteRefr@CWbemRemoteRefresher@@QEAA@XZ` | `0x6F820` | 17 | UnwindData |  |
| 1067 | `?Init@XFetchRefrMgr@CWbemFetchRefrMgr@@UEAAJPEAU_IWmiProvSS@@PEAUIWbemServices@@@Z` | `0x6FEE0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 726 | `?GetCurrentOrigin@CClassAndMethods@@UEAAKXZ` | `0x70030` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `??OCInternalString@@QEBA_NAEBV0@@Z` | `0x701D0` | 26 | UnwindData |  |
| 166 | `??1XObjectTextSrc@CWmiObjectTextSrc@@QEAA@XZ` | `0x70220` | 17 | UnwindData |  |
| 1028 | `?GetText@XObjectTextSrc@CWmiObjectTextSrc@@UEAAJJPEAUIWbemClassObject@@KPEAUIWbemContext@@PEAPEAG@Z` | `0x70240` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `?GetCurrentOrigin@CWbemClass@@QEAAKXZ` | `0x703B0` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `?GetMethodOrigin@CMethodPart@@QEAAJPEBGPEAK@Z` | `0x708C0` | 62 | UnwindData |  |
| 281 | `??A?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAPEAVCWmiTextSource@@H@Z` | `0x709E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `??A?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEBAPEBVCWmiTextSource@@H@Z` | `0x709E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 692 | `?GetAt@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAPEAVCWmiTextSource@@H@Z` | `0x709E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 693 | `?GetAt@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEBAPEBVCWmiTextSource@@H@Z` | `0x709E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `?GetMethodOrigin@CWbemClass@@UEAAJPEBGPEAPEAG@Z` | `0x70A50` | 528 | UnwindData |  |
| 1457 | `?SpawnInstance@CWbemInstance@@UEAAJJPEAPEAUIWbemClassObject@@@Z` | `0x70CD0` | 664 | UnwindData |  |
| 380 | `?AddRefElement@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@IEAAXPEAVCWmiTextSource@@@Z` | `0x70F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `?GetNormalizedPath@CWbemObject@@UEAAJJPEAPEAG@Z` | `0x70F80` | 324 | UnwindData |  |
| 1152 | `?IsTopLevel@CClassPart@@QEAAHXZ` | `0x71230` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `?AddObjectToRefresher@XWbemRefrSvc@CWbemRefreshingSvc@@UEAAJPEAU_WBEM_REFRESHER_ID@@PEBGJPEAUIWbemContext@@KPEAU_WBEM_REFRESH_INFO@@PEAK@Z` | `0x71380` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `??4CInternalString@@QEAAHPEAVCCompressedString@@@Z` | `0x71460` | 117 | UnwindData |  |
| 1108 | `?IsEmpty@CInternalString@@QEAA_NXZ` | `0x715D0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `?GetDefaultPtrByHandle@CClassPart@@QEAAJJPEAPEAX@Z` | `0x716A0` | 60 | UnwindData |  |
| 1098 | `?IsCompressed@CClassPart@@QEAAHXZ` | `0x716F0` | 41 | UnwindData |  |
| 999 | `?GetSource@CWbemObject@@UEAAJPEAPEAG@Z` | `0x71720` | 40 | UnwindData |  |
| 559 | `?CreateLPWSTRCopy@CInternalString@@QEBAPEAGXZ` | `0x717A0` | 65 | UnwindData |  |
| 676 | `?GetAbstractFlavor@CClassPart@@QEAAEXZ` | `0x74B70` | 39 | UnwindData |  |
| 1551 | `?WritePropertyAsMethodParam@CWbemClass@@QEAAJAEAVWString@@HJPEAV1@H@Z` | `0x74CC0` | 927 | UnwindData |  |
| 492 | `?CompareUnicodeToAscii@CCompressedString@@KAHPEBGPEBD@Z` | `0x75170` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `?CompareTo@CClassAndMethods@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x75440` | 68 | UnwindData |  |
| 127 | `??1?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@QEAA@XZ` | `0x75560` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `??1?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@QEAA@XZ` | `0x75560` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `??1?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@QEAA@XZ` | `0x75560` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `??1?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@QEAA@XZ` | `0x755A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `?IsEmpty@CBasicQualifierSet@@QEAAHXZ` | `0x755E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `?IsEmpty@CBasicQualifierSet@@SAHPEAE@Z` | `0x755E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??0CBasicQualifierSet@@QEAA@XZ` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `??4CClassPartContainer@@QEAAAEAV0@$$QEAV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `??4CClassPartContainer@@QEAAAEAV0@AEBV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `??4CInstancePartContainer@@QEAAAEAV0@$$QEAV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `??4CInstancePartContainer@@QEAAAEAV0@AEBV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `??4CKnownStringTable@@QEAAAEAV0@$$QEAV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `??4CKnownStringTable@@QEAAAEAV0@AEBV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `??4CMethodPartContainer@@QEAAAEAV0@$$QEAV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `??4CMethodPartContainer@@QEAAAEAV0@AEBV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `??4CQualifierSetListContainer@@QEAAAEAV0@$$QEAV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `??4CQualifierSetListContainer@@QEAAAEAV0@AEBV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 236 | `??4CReservedWordTable@@QEAAAEAV0@$$QEAV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `??4CReservedWordTable@@QEAAAEAV0@AEBV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `??4CSystemProperties@@QEAAAEAV0@$$QEAV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `??4CSystemProperties@@QEAAAEAV0@AEBV0@@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | `?CreateEmpty@CDataTable@@SAPEAEPEAE@Z` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `?GetArray@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAAEAVCFlexArray@@XZ` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `?GetStart@CCompressedString@@QEAAPEAEXZ` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `?GetStart@CEmbeddedObject@@QEAAPEAEXZ` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1058 | `?GetWbemObjectUnknown@CWbemClass@@QEAAPEAUIUnknown@@XZ` | `0x755F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `??BCInternalString@@AEAAPEAVCCompressedString@@XZ` | `0x75600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `??BCInternalString@@AEBAPEAVCCompressedString@@XZ` | `0x75600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `?GetHeapData@CFastHeap@@QEAAPEAEXZ` | `0x75600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `?GetStart@CCompressedStringList@@QEAAPEAEXZ` | `0x75600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1005 | `?GetStart@CDataTable@@QEAAPEAEXZ` | `0x75600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1006 | `?GetStart@CDecorationPart@@QEAAPEAEXZ` | `0x75600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1011 | `?GetStart@CPropertyLookupTable@@QEAAPEAEXZ` | `0x75600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `?GetHeaderLength@CCompressedStringList@@SAKXZ` | `0x75610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `?GetHeaderLength@CUntypedArray@@SAKXZ` | `0x75610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `?GetMinLength@CBasicQualifierSet@@SAKXZ` | `0x75610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `?GetMinLength@CFastHeap@@SAKXZ` | `0x75610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | `?GetMinLength@CPropertyLookupTable@@SAKXZ` | `0x75610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `?GetSeparatorLength@CCompressedStringList@@KAKXZ` | `0x75610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 762 | `?GetHeap@CBasicQualifierSet@@QEAAPEAVCFastHeap@@XZ` | `0x75620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1031 | `?GetThreadToken@CWbemThreadSecurityHandle@@QEAAPEAXXZ` | `0x75620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `?GetFlags@CLimitationMapping@@QEAAJXZ` | `0x75630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `?Rebase@CCompressedStringList@@QEAAXPEAE@Z` | `0x75640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1263 | `?Rebase@CPropertyLookupTable@@QEAAXPEAE@Z` | `0x75640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1363 | `?SetData@CSharedLock@@QEAAXPEAUSHARED_LOCK_DATA@@@Z` | `0x75640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1072 | `?Initialize@CKnownStringTable@@SAXXZ` | `0x75650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1371 | `?SetDataLength@CBasicQualifierSet@@KAXPEAEK@Z` | `0x75670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1394 | `?SetLength@CFixedBSTRArray@@QEAAXH@Z` | `0x75670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 699 | `?GetAuthenticationLevel@CWbemThreadSecurityHandle@@QEAAKXZ` | `0x75680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `?GetStart@CClassAndMethods@@QEAAPEAEXZ` | `0x75690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1414 | `?SetOrigin@CWbemThreadSecurityHandle@@QEAAXW4tag_WMI_THREAD_SECURITY_ORIGIN@@@Z` | `0x756A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `?GetImpersonationLevel@CWbemThreadSecurityHandle@@QEAAKXZ` | `0x756B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `??BCType@@QEAAKXZ` | `0x756C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `?GetLength@CBasicQualifierSet@@QEAAKXZ` | `0x756C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `?GetLength@CFixedBSTRArray@@QEAAHXZ` | `0x756C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 821 | `?GetLength@CInstancePart@@SAHPEAE@Z` | `0x756C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | `?GetLengthFromData@CBasicQualifierSet@@SAKPEAE@Z` | `0x756C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 882 | `?GetNumElements@CUntypedArray@@QEAAHXZ` | `0x756C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `?GetNumSets@CQualifierSetList@@QEAAHXZ` | `0x756C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 995 | `?GetServerPrincipalName@CWbemThreadSecurityHandle@@QEAAPEAGXZ` | `0x756D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `?GetStart@CInstancePart@@QEAAPEAEXZ` | `0x756D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `?SetAddChildKeys@CLimitationMapping@@QEAAXH@Z` | `0x756E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1386 | `?SetIncludeDerivation@CLimitationMapping@@QEAAXH@Z` | `0x756F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `?GetFirstQualifierFromData@CBasicQualifierSet@@SAPEAUCQualifier@@PEAE@Z` | `0x75700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1387 | `?SetIncludeNamespace@CLimitationMapping@@QEAAXH@Z` | `0x75710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `?ComputeNecessarySpace@CQualifierSetList@@SAKH@Z` | `0x75720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | `?ExtendClassPartSpace@CWbemInstance@@UEAAHPEAVCClassPart@@K@Z` | `0x75720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 640 | `?ExtendDataTableSpace@CInstancePart@@UEAAHPEAEKK@Z` | `0x75720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 760 | `?GetHeaderLength@CQualifierSetList@@SAHXZ` | `0x75720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 782 | `?GetIndexOfKey@CKnownStringTable@@SAHXZ` | `0x75720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `?GetMinLength@CDecorationPart@@SAKXZ` | `0x75720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1073 | `?Initialize@CWbemRefreshingSvc@@UEAAHXZ` | `0x75720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1348 | `?SetContainer@CFastHeap@@QEAAXPEAVCHeapContainer@@@Z` | `0x75730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 871 | `?GetMinLength@CWbemClass@@SAKXZ` | `0x75740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `?GetLength@CDataTable@@QEAAKXZ` | `0x75750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 981 | `?GetRawData@CCompressedString@@QEBAPEAEXZ` | `0x75760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `?MaxNumProperties@CSystemProperties@@SAHXZ` | `0x75770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 775 | `?GetIdentity@CWbemThreadSecurityHandle@@QEAAPEAGXZ` | `0x75780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `?GetStart@CClassPart@@QEAAPEAEXZ` | `0x75780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `?ShouldIncludeNamespace@CLimitationMapping@@QEAAHXZ` | `0x75790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1374 | `?SetDataToNone@CBasicQualifierSet@@SAXPEAE@Z` | `0x757A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1446 | `?ShouldAddChildKeys@CLimitationMapping@@QEAAHXZ` | `0x757B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1325 | `?Reset@CLimitationMapping@@QEAAXXZ` | `0x757C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1264 | `?Rebase@CQualifierSetList@@QEAAXPEAE@Z` | `0x757D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `?GetLength@CQualifierSetList@@QEAAHXZ` | `0x757E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 891 | `?GetNumSystemProperties@CSystemProperties@@SAHXZ` | `0x757F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1177 | `?LowerByte@CCompressedString@@KADG@Z` | `0x75800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1381 | `?SetFlags@CLimitationMapping@@QEAAXJ@Z` | `0x75810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | `?GetMinLength@CClassPart@@SAHXZ` | `0x75820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1447 | `?ShouldIncludeDerivation@CLimitationMapping@@QEAAHXZ` | `0x75830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `?GetMinLength@CMethodPart@@SAKXZ` | `0x75840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1388 | `?SetIncludeServer@CLimitationMapping@@QEAAXH@Z` | `0x75850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1050 | `?GetVtableLength@CLimitationMapping@@QEAAKXZ` | `0x75860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1449 | `?ShouldIncludeServer@CLimitationMapping@@QEAAHXZ` | `0x75870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `?GetMinLength@CClassAndMethods@@SAKXZ` | `0x75880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `??1?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@QEAA@XZ` | `0x75890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `??1?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@QEAA@XZ` | `0x75890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `??1?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@QEAA@XZ` | `0x758B0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1030 | `?GetThreadSecurityHandle@CWbemCallSecurity@@QEAAPEAVCWbemThreadSecurityHandle@@XZ` | `0x75930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@QEAA@PEAVCWmiObjectTextSrc@@@Z` | `0x75940` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | `?GetAuthenticationService@CWbemThreadSecurityHandle@@QEAAKXZ` | `0x759E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `?GetAuthorizationService@CWbemThreadSecurityHandle@@QEAAKXZ` | `0x759F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `?ComputeRealSpace@CQualifierSetList@@SAKH@Z` | `0x75A00` | 6,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0CClassAndMethods@@QEAA@$$QEAV0@@Z` | `0x77380` | 199 | UnwindData |  |
| 21 | `??0CClassAndMethods@@QEAA@AEBV0@@Z` | `0x77380` | 199 | UnwindData |  |
| 23 | `??0CClassPart@@QEAA@$$QEAV0@@Z` | `0x77450` | 220 | UnwindData |  |
| 24 | `??0CClassPart@@QEAA@AEBV0@@Z` | `0x77450` | 220 | UnwindData |  |
| 29 | `??0CClassQualifierSet@@QEAA@$$QEAV0@@Z` | `0x77540` | 39 | UnwindData |  |
| 30 | `??0CClassQualifierSet@@QEAA@AEBV0@@Z` | `0x77540` | 39 | UnwindData |  |
| 44 | `??0CInstanceQualifierSet@@QEAA@$$QEAV0@@Z` | `0x77540` | 39 | UnwindData |  |
| 45 | `??0CInstanceQualifierSet@@QEAA@AEBV0@@Z` | `0x77540` | 39 | UnwindData |  |
| 35 | `??0CInstancePQSContainer@@QEAA@$$QEAV0@@Z` | `0x77570` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??0CInstancePQSContainer@@QEAA@AEBV0@@Z` | `0x77570` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??0CInstancePart@@QEAA@$$QEAV0@@Z` | `0x775C0` | 199 | UnwindData |  |
| 39 | `??0CInstancePart@@QEAA@AEBV0@@Z` | `0x775C0` | 199 | UnwindData |  |
| 50 | `??0CLimitationMapping@@QEAA@AEAV0@@Z` | `0x77690` | 143 | UnwindData |  |
| 52 | `??0CMethodPart@@QEAA@$$QEAV0@@Z` | `0x77730` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `??0CMethodPart@@QEAA@AEBV0@@Z` | `0x77730` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??0CMethodQualifierSet@@QEAA@$$QEAV0@@Z` | `0x77780` | 66 | UnwindData |  |
| 59 | `??0CMethodQualifierSet@@QEAA@AEBV0@@Z` | `0x77780` | 66 | UnwindData |  |
| 61 | `??0CMethodQualifierSetContainer@@QEAA@$$QEAV0@@Z` | `0x777D0` | 107 | UnwindData |  |
| 62 | `??0CMethodQualifierSetContainer@@QEAA@AEBV0@@Z` | `0x777D0` | 107 | UnwindData |  |
| 64 | `??0CQualifierSet@@QEAA@AEBV0@@Z` | `0x77850` | 109 | UnwindData |  |
| 73 | `??0CWbemClass@@QEAA@AEBV0@@Z` | `0x778D0` | 186 | UnwindData |  |
| 85 | `??0CWbemInstance@@QEAA@AEBV0@@Z` | `0x77990` | 203 | UnwindData |  |
| 90 | `??0CWbemObject@@QEAA@AEBV0@@Z` | `0x77A70` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `??4CBasicQualifierSet@@QEAAAEAV0@AEBV0@@Z` | `0x77B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `??4CDecorationPart@@QEAAAEAV0@AEBV0@@Z` | `0x77B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `??4CHiPerfLock@@QEAAAEAV0@AEBV0@@Z` | `0x77B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `??4CMethodDescription@@QEAAAEAU0@AEBU0@@Z` | `0x77B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `??4CQualifierSetList@@QEAAAEAV0@AEBV0@@Z` | `0x77B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `??4CWbemMtgtDeliverEventPacket@@QEAAAEAV0@AEBV0@@Z` | `0x77B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `??4CWbemSmartEnumNextPacket@@QEAAAEAV0@AEBV0@@Z` | `0x77B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `??4CClassAndMethods@@QEAAAEAV0@$$QEAV0@@Z` | `0x77B60` | 158 | UnwindData |  |
| 181 | `??4CClassAndMethods@@QEAAAEAV0@AEBV0@@Z` | `0x77B60` | 158 | UnwindData |  |
| 182 | `??4CClassPart@@QEAAAEAV0@$$QEAV0@@Z` | `0x77C10` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `??4CClassPart@@QEAAAEAV0@AEBV0@@Z` | `0x77C10` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `??4CClassQualifierSet@@QEAAAEAV0@$$QEAV0@@Z` | `0x77D00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `??4CClassQualifierSet@@QEAAAEAV0@AEBV0@@Z` | `0x77D00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `??4CInstanceQualifierSet@@QEAAAEAV0@$$QEAV0@@Z` | `0x77D00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `??4CInstanceQualifierSet@@QEAAAEAV0@AEBV0@@Z` | `0x77D00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `??4CQualifierSet@@QEAAAEAV0@AEBV0@@Z` | `0x77D00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `??4CCompressedString@@QEAAAEAV0@$$QEAV0@@Z` | `0x77D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `??4CCompressedString@@QEAAAEAV0@AEBV0@@Z` | `0x77D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `??4CCompressedStringList@@QEAAAEAV0@$$QEAV0@@Z` | `0x77DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `??4CCompressedStringList@@QEAAAEAV0@AEBV0@@Z` | `0x77DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `??4CDerivationList@@QEAAAEAV0@$$QEAV0@@Z` | `0x77DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `??4CDerivationList@@QEAAAEAV0@AEBV0@@Z` | `0x77DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `??4CFixedBSTRArray@@QEAAAEAV0@AEBV0@@Z` | `0x77DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `??4SHARED_LOCK_DATA@@QEAAAEAU0@AEBU0@@Z` | `0x77DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `??4CDataTable@@QEAAAEAV0@$$QEAV0@@Z` | `0x77DE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `??4CDataTable@@QEAAAEAV0@AEBV0@@Z` | `0x77E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `??4CDecorationPart@@QEAAAEAV0@$$QEAV0@@Z` | `0x77E30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `??4CEmbeddedObject@@QEAAAEAV0@$$QEAV0@@Z` | `0x77E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `??4CEmbeddedObject@@QEAAAEAV0@AEBV0@@Z` | `0x77E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `??4CFastHeap@@QEAAAEAV0@$$QEAV0@@Z` | `0x77E80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `??4CFastHeap@@QEAAAEAV0@AEBV0@@Z` | `0x77EC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `??4CHiPerfLock@@QEAAAEAV0@$$QEAV0@@Z` | `0x77EF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `??4CInstancePQSContainer@@QEAAAEAV0@$$QEAV0@@Z` | `0x77F20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `??4CInstancePQSContainer@@QEAAAEAV0@AEBV0@@Z` | `0x77F20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `??4CInstancePart@@QEAAAEAV0@$$QEAV0@@Z` | `0x77F60` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `??4CInstancePart@@QEAAAEAV0@AEBV0@@Z` | `0x77F60` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `??4CLimitationMapping@@QEAAAEAV0@AEAV0@@Z` | `0x78040` | 137 | UnwindData |  |
| 219 | `??4CMethodDescription@@QEAAAEAU0@$$QEAU0@@Z` | `0x780D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `??4CMethodPart@@QEAAAEAV0@$$QEAV0@@Z` | `0x78110` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `??4CMethodPart@@QEAAAEAV0@AEBV0@@Z` | `0x78110` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `??4CMethodQualifierSet@@QEAAAEAV0@$$QEAV0@@Z` | `0x78160` | 108 | UnwindData |  |
| 226 | `??4CMethodQualifierSet@@QEAAAEAV0@AEBV0@@Z` | `0x78160` | 108 | UnwindData |  |
| 227 | `??4CMethodQualifierSetContainer@@QEAAAEAV0@$$QEAV0@@Z` | `0x781E0` | 91 | UnwindData |  |
| 228 | `??4CMethodQualifierSetContainer@@QEAAAEAV0@AEBV0@@Z` | `0x781E0` | 91 | UnwindData |  |
| 229 | `??4CPropertyLookupTable@@QEAAAEAV0@$$QEAV0@@Z` | `0x78250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `??4CPropertyLookupTable@@QEAAAEAV0@AEBV0@@Z` | `0x78270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `??4CWbemDataPacket@@QEAAAEAV0@AEBV0@@Z` | `0x78270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `??4CWbemObjectArrayPacket@@QEAAAEAV0@AEBV0@@Z` | `0x78270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `??4CQualifierSetList@@QEAAAEAV0@$$QEAV0@@Z` | `0x78290` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `??4CType@@QEAAAEAV0@$$QEAV0@@Z` | `0x782C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `??4CType@@QEAAAEAV0@AEBV0@@Z` | `0x782C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `??4CUntypedArray@@QEAAAEAV0@$$QEAV0@@Z` | `0x782C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `??4CUntypedArray@@QEAAAEAV0@AEBV0@@Z` | `0x782C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `??4SHARED_LOCK_DATA@@QEAAAEAU0@$$QEAU0@@Z` | `0x782D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `??4SHMEM_HANDLE@@QEAAAEAU0@$$QEAU0@@Z` | `0x782F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `??8CInternalString@@QEBA_NPEBG@Z` | `0x78310` | 23 | UnwindData |  |
| 279 | `??8CQualifierSet@@QEAAHAEAV0@@Z` | `0x78330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `??9CInternalString@@QEBA_NAEBV0@@Z` | `0x78350` | 26 | UnwindData |  |
| 350 | `??_FCClassQualifierSet@@QEAAXXZ` | `0x78570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `??_FCInstanceQualifierSet@@QEAAXXZ` | `0x78580` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `?AbsoluteToHeap@CFastHeap@@IEAAKPEAE@Z` | `0x78610` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `?AddString@CCompressedStringList@@QEAAXPEBG@Z` | `0x786D0` | 106 | UnwindData |  |
| 392 | `?ArePropertiesLimited@CLimitationMapping@@QEAAHXZ` | `0x78740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `?CVarToType@CType@@SA?AV1@AEAVCVar@@@Z` | `0x78760` | 127 | UnwindData |  |
| 450 | `?ClearWriteOnlyProperties@CWbemClass@@UEAAJXZ` | `0x78850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `?Compare@CInternalString@@QEBAHAEBV1@@Z` | `0x78860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `?Compare@CInternalString@@QEBAHPEBG@Z` | `0x78880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `?ComputeNecessarySpace@CCompressedStringList@@QEAAKPEAVCCompressedString@@@Z` | `0x78890` | 29 | UnwindData |  |
| 589 | `?DeleteProperty@CClassPart@@QEAAXH@Z` | `0x78A80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 604 | `?Empty@CInternalString@@QEAAXXZ` | `0x78AB0` | 35 | UnwindData |  |
| 621 | `?EstimateExtraSpace@CCompressedStringList@@SAKPEBG@Z` | `0x78AE0` | 18 | UnwindData |  |
| 623 | `?EstimateLimitedRepresentationSpace@CWbemObject@@QEAAKJPEAVCWStringArray@@@Z` | `0x78B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `?FindPropertyByOffset@CPropertyLookupTable@@QEAAPEAUCPropertyLookup@@K@Z` | `0x78B20` | 127 | UnwindData |  |
| 677 | `?GetAbstractFlavor@CWbemClass@@QEAAEXZ` | `0x78BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 679 | `?GetActualTransferBlobSize@CWbemInstance@@QEAAJXZ` | `0x78BD0` | 79 | UnwindData |  |
| 708 | `?GetClassIndex@CClassPart@@QEAAKPEBG@Z` | `0x78C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 731 | `?GetDataTable@CInstancePart@@QEAAPEAVCDataTable@@XZ` | `0x78C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `?GetDataTableData@CInstancePart@@SAPEAEPEAE@Z` | `0x78C50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `?GetHeap@CMethodPart@@QEAAPEAVCFastHeap@@XZ` | `0x78CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `?GetHeapPtrByHandle@CClassPart@@QEAAKJ@Z` | `0x78CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 786 | `?GetIndexedProps@CWbemInstance@@UEAAHAEAVCWStringArray@@@Z` | `0x78CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `?GetKey@CWbemInstance@@QEAAPEAVCVar@@XZ` | `0x78CF0` | 64 | UnwindData |  |
| 796 | `?GetKeyOrigin@CWbemClass@@UEAAJAEAVWString@@@Z` | `0x78D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `?GetKeyOrigin@CWbemInstance@@QEAAJAEAVWString2@@@Z` | `0x78D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `?GetKeyOrigin@CWbemInstance@@UEAAJAEAVWString@@@Z` | `0x78D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `?GetKeyProps@CWbemInstance@@UEAAHAEAVCWStringArray@@@Z` | `0x78DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 822 | `?GetLength@CInternalString@@QEBAHXZ` | `0x78DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 881 | `?GetNumDecorationIndependentProperties@CSystemProperties@@SAHXZ` | `0x78DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `?GetNumParents@CWbemObject@@QEAAHXZ` | `0x78DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 888 | `?GetNumProperties@CWbemInstance@@UEAAHXZ` | `0x78E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | `?GetPropName@CWbemInstance@@UEAAJHPEAVCVar@@@Z` | `0x78E20` | 72 | UnwindData |  |
| 920 | `?GetPropQualifier@CWbemInstance@@UEAAJPEBG0PEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x78E70` | 123 | UnwindData |  |
| 961 | `?GetQualifier@CWbemInstance@@UEAAJPEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x78F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `?GetQualifierSetListStart@CInstancePart@@UEAAPEAEXZ` | `0x78F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `?GetSyntax@CType@@QEAAPEAGXZ` | `0x78F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `?GetText@CInternalString@@QEBAPEBDXZ` | `0x78F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `?GetTransferArrayBlobSize@CWbemInstance@@QEAAJXZ` | `0x78F50` | 79 | UnwindData |  |
| 1038 | `?GetTransferArrayHeaderSize@CWbemInstance@@SAJXZ` | `0x78FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1040 | `?GetTransferBlobSize@CWbemInstance@@QEAAJXZ` | `0x78FC0` | 79 | UnwindData |  |
| 1089 | `?IsAssociation@CClassPart@@QEAAHXZ` | `0x79050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `?IsAutocook@CClassPart@@QEAAHXZ` | `0x79070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1099 | `?IsCompressed@CWbemClass@@QEAAHXZ` | `0x79090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1111 | `?IsHiPerf@CClassPart@@QEAAHXZ` | `0x790B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1131 | `?IsNonArrayPointerType@CType@@QEAAHXZ` | `0x790D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `?IsParents@CType@@QEAAHXZ` | `0x790E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `?IsSingleton@CWbemClass@@QEAAHXZ` | `0x790F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1150 | `?IsStringType@CType@@QEAAHXZ` | `0x79110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `?IsValidPtr@CFastHeap@@QEAA_NK@Z` | `0x79120` | 29 | UnwindData |  |
| 1180 | `?MakeLocal@CType@@SAKK@Z` | `0x79150` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1265 | `?Rebase@CQualifierSetList@@QEAAXXZ` | `0x791A0` | 36 | UnwindData |  |
| 1291 | `?ReduceQualifierSetSpace@CInstancePQSContainer@@UEAAXPEAVCBasicQualifierSet@@K@Z` | `0x791D0` | 44 | UnwindData |  |
| 1305 | `?Release@CQualifierSet@@UEAAKXZ` | `0x79210` | 78 | UnwindData |  |
| 1324 | `?Reset@CCompressedStringList@@QEAAXXZ` | `0x79420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1327 | `?ResolveHeapPointer@CClassPart@@QEAAPEAEK@Z` | `0x79440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1329 | `?ResolveHeapString@CClassPart@@QEAAPEAVCCompressedString@@K@Z` | `0x79460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1372 | `?SetDataLength@CClassPart@@QEAAXK@Z` | `0x79480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1395 | `?SetLimited@CDecorationPart@@QEAAXXZ` | `0x79490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1430 | `?SetQualifier@CWbemInstance@@UEAAJPEBGJPEAVCTypedValue@@@Z` | `0x794B0` | 48 | UnwindData |  |
| 1431 | `?SetQualifier@CWbemInstance@@UEAAJPEBGPEAVCVar@@J@Z` | `0x794F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1443 | `?SetUsedLength@CFastHeap@@QEAAXK@Z` | `0x79510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1451 | `?Skip@CFastHeap@@QEAAPEAEXZ` | `0x79520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1452 | `?Skip@CPropertyLookupTable@@QEAAPEAEXZ` | `0x79540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1470 | `?TestCircularReference@CClassPart@@QEAAJPEBG@Z` | `0x79560` | 31 | UnwindData |  |
| 1558 | `?WriteTransferArrayHeader@CWbemInstance@@SAXJPEAPEAE@Z` | `0x79590` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `??0CWbemClassCache@@QEAA@AEBV0@@Z` | `0x79E10` | 85 | UnwindData |  |
| 247 | `??4CWbemClassCache@@QEAAAEAV0@AEBV0@@Z` | `0x7A1B0` | 118 | UnwindData |  |
| 352 | `??_FCWbemClassCache@@QEAAXXZ` | `0x7A230` | 7,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 862 | `?GetMinHeaderSize@CWbemDataPacket@@QEAAKXZ` | `0x7BDA0` | 10,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `?CanBeReconciledWith@CClassAndMethods@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x7E600` | 64 | UnwindData |  |
| 412 | `?CanBeReconciledWith@CClassPart@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x7E650` | 1,556 | UnwindData |  |
| 414 | `?CanBeReconciledWith@CWbemClass@@QEAA?AW4EReconciliation@@PEAV1@@Z` | `0x7EC70` | 36 | UnwindData |  |
| 456 | `?CloneEx@CWbemClass@@UEAAJJPEAU_IWmiObject@@@Z` | `0x7ECA0` | 415 | UnwindData |  |
| 477 | `?CompareDerivedMostClass@CWbemClass@@UEAAJJPEAU_IWmiObject@@@Z` | `0x7EE50` | 335 | UnwindData |  |
| 513 | `?CopyBlobOf@CWbemClass@@UEAAJPEAVCWbemObject@@@Z` | `0x7EFB0` | 265 | UnwindData |  |
| 517 | `?CopyInstanceData@CWbemClass@@UEAAJJPEAU_IWmiObject@@@Z` | `0x7F0C0` | 105 | UnwindData |  |
| 521 | `?CopyParentProperty@CClassPart@@QEAAJAEAV1@PEBG@Z` | `0x7F130` | 903 | UnwindData |  |
| 554 | `?CreateFromBlob@CWbemClass@@SAPEAV1@PEAV1@PEAE_K@Z` | `0x7F4C0` | 789 | UnwindData |  |
| 560 | `?CreateLimitedRepresentation@CClassAndMethods@@QEAAPEAEPEAVCLimitationMapping@@HPEAEAEAH@Z` | `0x7F7E0` | 109 | UnwindData |  |
| 583 | `?Delete@CWbemClass@@UEAAJPEBG@Z` | `0x7F860` | 706 | UnwindData |  |
| 586 | `?DeleteMethod@CWbemClass@@UEAAJPEBG@Z` | `0x7FB30` | 338 | UnwindData |  |
| 588 | `?DeleteProperty@CClassPart@@QEAAJPEBG@Z` | `0x7FC90` | 59 | UnwindData |  |
| 659 | `?FindMethod@CWbemClass@@UEAAJPEBG@Z` | `0x7FCE0` | 27 | UnwindData |  |
| 667 | `?ForcePropValue@CWbemClass@@QEAAJPEBGPEAVCVar@@J@Z` | `0x7FD10` | 357 | UnwindData |  |
| 668 | `?ForcePut@CWbemClass@@QEAAJPEBGJPEAUtagVARIANT@@J@Z` | `0x7FE80` | 440 | UnwindData |  |
| 711 | `?GetClassNameW@CClassAndMethods@@SAJAEAVWString@@PEAE@Z` | `0x80040` | 299 | UnwindData |  |
| 721 | `?GetClassQualifier@CClassPart@@QEAAJPEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x80180` | 292 | UnwindData |  |
| 783 | `?GetIndexedProps@CClassAndMethods@@SAHAEAVCWStringArray@@PEAE@Z` | `0x802B0` | 128 | UnwindData |  |
| 795 | `?GetKeyOrigin@CClassPart@@QEAAJAEAVWString@@@Z` | `0x80340` | 334 | UnwindData |  |
| 855 | `?GetMethodQualifier@CWbemClass@@UEAAJPEBG0PEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x804A0` | 369 | UnwindData |  |
| 903 | `?GetParentClassFromBlob@CWbemClass@@UEAAJJKPEAXPEAPEAG@Z` | `0x80620` | 327 | UnwindData |  |
| 913 | `?GetPropQualifier@CClassPart@@QEAAJPEBG0PEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x80790` | 271 | UnwindData |  |
| 916 | `?GetPropQualifier@CWbemClass@@UEAAJPEBG0PEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x808B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 934 | `?GetPropertyInfoByHandle@CClassPart@@QEAAJJPEAPEAGPEAJ@Z` | `0x808D0` | 249 | UnwindData |  |
| 942 | `?GetPropertyQualifierSetData@CClassPart@@QEAAPEAEPEBG@Z` | `0x809D0` | 28 | UnwindData |  |
| 952 | `?GetQualifier@CClassPart@@QEAAJPEBGPEAVCVar@@PEAJ2@Z` | `0x80A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 959 | `?GetQualifier@CWbemClass@@UEAAJPEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x80A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1016 | `?GetSuperclassName@CClassAndMethods@@SAJAEAVWString@@PEAE@Z` | `0x80A30` | 377 | UnwindData |  |
| 1115 | `?IsIndexLocal@CWbemClass@@QEAAHPEBG@Z` | `0x80BB0` | 83 | UnwindData |  |
| 1120 | `?IsKeyLocal@CWbemClass@@QEAAHPEBG@Z` | `0x80C10` | 83 | UnwindData |  |
| 1128 | `?IsLocalized@CWbemClass@@UEAAHXZ` | `0x80C70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `?IsPropertyIndexed@CClassPart@@QEAAHPEBG@Z` | `0x80CA0` | 109 | UnwindData |  |
| 1145 | `?IsPropertyKeyed@CClassPart@@QEAAHPEBG@Z` | `0x80D20` | 88 | UnwindData |  |
| 1163 | `?IsValidObj@CWbemClass@@UEAAJXZ` | `0x80D80` | 143 | UnwindData |  |
| 1165 | `?IsValidPropertyHandle@CClassPart@@QEAAJJ@Z` | `0x80E20` | 145 | UnwindData |  |
| 1208 | `?Merge@CWbemClass@@UEAAJJKPEAXPEAPEAU_IWmiObject@@@Z` | `0x80EC0` | 163 | UnwindData |  |
| 1269 | `?ReconcileWith@CClassAndMethods@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x80F70` | 64 | UnwindData |  |
| 1270 | `?ReconcileWith@CClassPart@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x80FC0` | 138 | UnwindData |  |
| 1272 | `?ReconcileWith@CWbemClass@@QEAA?AW4EReconciliation@@PEAV1@@Z` | `0x81050` | 36 | UnwindData |  |
| 1273 | `?ReconcileWith@CWbemClass@@UEAAJJPEAU_IWmiObject@@@Z` | `0x81080` | 406 | UnwindData |  |
| 1281 | `?ReduceDataTableSpace@CClassPart@@UEAAXPEAEKK@Z` | `0x81220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1344 | `?SetClassQualifier@CClassPart@@QEAAJPEBGJPEAVCTypedValue@@@Z` | `0x81230` | 32 | UnwindData |  |
| 1389 | `?SetInheritanceChain@CClassPart@@QEAAJJPEAPEAG@Z` | `0x81260` | 484 | UnwindData |  |
| 1390 | `?SetInheritanceChain@CWbemClass@@UEAAJJPEAPEAG@Z` | `0x81450` | 92 | UnwindData |  |
| 1401 | `?SetMethodOrigin@CWbemClass@@UEAAJPEBGJ@Z` | `0x814C0` | 94 | UnwindData |  |
| 1404 | `?SetMethodQualifier@CWbemClass@@UEAAJPEBG0JPEAVCTypedValue@@@Z` | `0x81530` | 274 | UnwindData |  |
| 1405 | `?SetMethodQualifier@CWbemClass@@UEAAJPEBG0JPEAVCVar@@@Z` | `0x81650` | 371 | UnwindData |  |
| 1417 | `?SetPropQualifier@CClassPart@@QEAAJPEBG0JPEAVCTypedValue@@@Z` | `0x817D0` | 241 | UnwindData |  |
| 1419 | `?SetPropQualifier@CWbemClass@@UEAAJPEBG0JPEAVCTypedValue@@@Z` | `0x818D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `?SetPropertyOrigin@CClassPart@@QEAAJPEBGJ@Z` | `0x818F0` | 38 | UnwindData |  |
| 1426 | `?SetPropertyOrigin@CWbemClass@@UEAAJPEBGJ@Z` | `0x81920` | 94 | UnwindData |  |
| 1428 | `?SetQualifier@CWbemClass@@UEAAJPEBGJPEAVCTypedValue@@@Z` | `0x81990` | 141 | UnwindData |  |
| 1508 | `?Update@CWbemClass@@QEAAJPEAV1@JPEAPEAV1@@Z` | `0x81A30` | 747 | UnwindData |  |
| 1509 | `?Update@CWbemClass@@UEAAJPEAU_IWmiObject@@JPEAPEAU2@@Z` | `0x81D30` | 402 | UnwindData |  |
| 1511 | `?UpdateProperties@CClassPart@@SAJAEAV1@0J@Z` | `0x81ED0` | 703 | UnwindData |  |
| 1512 | `?Upgrade@CWbemClass@@UEAAJPEAU_IWmiObject@@JPEAPEAU2@@Z` | `0x821A0` | 456 | UnwindData |  |
| 628 | `?EstimateNecessarySpace@CEmbeddedObject@@SAKAEAVCVar@@@Z` | `0x823C0` | 69 | UnwindData |  |
| 1462 | `?StoreEmbedded@CEmbeddedObject@@QEAAXKAEAVCVar@@@Z` | `0x82410` | 88 | UnwindData |  |
| 385 | `?AllocateString@CFastHeap@@QEAAHPEBDAEFAK@Z` | `0x82470` | 118 | UnwindData |  |
| 403 | `?CalculateCachedKey@CWbemInstance@@QEAAPEAVCVar@@XZ` | `0x82520` | 106 | UnwindData |  |
| 457 | `?CloneEx@CWbemInstance@@UEAAJJPEAU_IWmiObject@@@Z` | `0x82590` | 126 | UnwindData |  |
| 467 | `?CompactClass@CWbemInstance@@QEAAXXZ` | `0x82620` | 94 | UnwindData |  |
| 478 | `?CompareDerivedMostClass@CWbemInstance@@UEAAJJPEAU_IWmiObject@@@Z` | `0x82690` | 105 | UnwindData |  |
| 511 | `?CopyActualTransferBlob@CWbemInstance@@QEAAJJPEAE@Z` | `0x82700` | 459 | UnwindData |  |
| 512 | `?CopyBlob@CWbemInstance@@QEAAJPEAEH@Z` | `0x828E0` | 383 | UnwindData |  |
| 518 | `?CopyInstanceData@CWbemInstance@@UEAAJJPEAU_IWmiObject@@@Z` | `0x82A70` | 131 | UnwindData |  |
| 525 | `?CopyTransferArrayBlob@CWbemInstance@@SAJPEAV1@JJPEAEAEAVCFlexArray@@PEAJ@Z` | `0x82B00` | 832 | UnwindData |  |
| 526 | `?CopyTransferBlob@CWbemInstance@@QEAAJJJPEAE@Z` | `0x82E50` | 134 | UnwindData |  |
| 555 | `?CreateFromBlob@CWbemInstance@@SAPEAV1@PEAVCWbemClass@@PEAE_K@Z` | `0x82EE0` | 613 | UnwindData |  |
| 590 | `?DeleteProperty@CInstancePart@@QEAAXPEAVCPropertyInformation@@@Z` | `0x83150` | 79 | UnwindData |  |
| 592 | `?DeleteProperty@CWbemInstance@@QEAAJH@Z` | `0x831B0` | 602 | UnwindData |  |
| 654 | `?FastClone@CWbemInstance@@QEAAJPEAV1@@Z` | `0x83410` | 557 | UnwindData |  |
| 678 | `?GetActualTransferBlob@CWbemInstance@@QEAAXPEAE@Z` | `0x83650` | 182 | UnwindData |  |
| 720 | `?GetClassPart@CWbemInstance@@UEAAJPEAXKPEAK@Z` | `0x83710` | 252 | UnwindData |  |
| 724 | `?GetClassSubset@CWbemInstance@@UEAAJKPEAPEBGPEAPEAU_IWmiObject@@@Z` | `0x83820` | 105 | UnwindData |  |
| 803 | `?GetKeyStr@CWbemInstance@@QEAAPEAGXZ` | `0x83890` | 1,058 | UnwindData |  |
| 857 | `?GetMethodQualifier@CWbemInstance@@UEAAJPEBG0PEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x83CC0` | 105 | UnwindData |  |
| 858 | `?GetMethodQualifier@CWbemInstance@@UEAAJPEBG0PEAVCVar@@PEAJ2@Z` | `0x83D30` | 105 | UnwindData |  |
| 897 | `?GetObjectQualifier@CInstancePart@@QEAAJPEBGPEAVCVar@@PEAJ@Z` | `0x83DA0` | 217 | UnwindData |  |
| 918 | `?GetPropQualifier@CWbemInstance@@UEAAJPEAVCPropertyInformation@@PEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x83E80` | 483 | UnwindData |  |
| 953 | `?GetQualifier@CInstancePart@@QEAAJPEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x84070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `?GetTransferArrayBlob@CWbemInstance@@QEAAJJPEAPEAEPEAJ@Z` | `0x84080` | 343 | UnwindData |  |
| 1039 | `?GetTransferBlob@CWbemInstance@@QEAAJPEAJ0PEAPEAE@Z` | `0x841E0` | 274 | UnwindData |  |
| 1164 | `?IsValidObj@CWbemInstance@@UEAAJXZ` | `0x84300` | 283 | UnwindData |  |
| 1185 | `?MakeSubsetInst@CWbemInstance@@UEAAJPEAU_IWmiObject@@PEAPEAU2@@Z` | `0x84430` | 105 | UnwindData |  |
| 1209 | `?Merge@CWbemInstance@@UEAAJJKPEAXPEAPEAU_IWmiObject@@@Z` | `0x844A0` | 105 | UnwindData |  |
| 1212 | `?MergeAndDecorate@CWbemInstance@@UEAAJJKPEAXPEAG1PEAPEAU_IWmiObject@@@Z` | `0x84510` | 105 | UnwindData |  |
| 1274 | `?ReconcileWith@CWbemInstance@@UEAAJJPEAU_IWmiObject@@@Z` | `0x84580` | 105 | UnwindData |  |
| 1292 | `?ReduceQualifierSetSpace@CInstancePart@@UEAAXPEAVCBasicQualifierSet@@K@Z` | `0x845F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1323 | `?Reparent@CWbemInstance@@QEAAJPEAVCWbemClass@@PEAPEAV1@@Z` | `0x84610` | 812 | UnwindData |  |
| 1343 | `?SetClassPart@CWbemInstance@@UEAAJPEAXK@Z` | `0x84950` | 658 | UnwindData |  |
| 1392 | `?SetInstanceQualifier@CInstancePart@@QEAAJPEBGJPEAVCTypedValue@@@Z` | `0x84BF0` | 32 | UnwindData |  |
| 1393 | `?SetInstanceQualifier@CInstancePart@@QEAAJPEBGPEAVCVar@@J@Z` | `0x84C20` | 352 | UnwindData |  |
| 1406 | `?SetMethodQualifier@CWbemInstance@@UEAAJPEBG0JPEAVCTypedValue@@@Z` | `0x84D90` | 105 | UnwindData |  |
| 1407 | `?SetMethodQualifier@CWbemInstance@@UEAAJPEBG0JPEAVCVar@@@Z` | `0x84E00` | 105 | UnwindData |  |
| 1413 | `?SetObjectParts@CWbemInstance@@UEAAJPEAXKK@Z` | `0x84E70` | 239 | UnwindData |  |
| 1421 | `?SetPropQualifier@CWbemInstance@@UEAAJPEBG0JPEAVCTypedValue@@@Z` | `0x84F70` | 234 | UnwindData |  |
| 1422 | `?SetPropQualifier@CWbemInstance@@UEAAJPEBG0JPEAVCVar@@@Z` | `0x85060` | 523 | UnwindData |  |
| 1455 | `?SpawnDerivedClass@CWbemInstance@@UEAAJJPEAPEAUIWbemClassObject@@@Z` | `0x85280` | 105 | UnwindData |  |
| 1459 | `?SpawnKeyedInstance@CWbemInstance@@UEAAJJPEBGPEAPEAU_IWmiObject@@@Z` | `0x852F0` | 105 | UnwindData |  |
| 1510 | `?Update@CWbemInstance@@UEAAJPEAU_IWmiObject@@JPEAPEAU2@@Z` | `0x85360` | 105 | UnwindData |  |
| 1513 | `?Upgrade@CWbemInstance@@UEAAJPEAU_IWmiObject@@JPEAPEAU2@@Z` | `0x853D0` | 349 | UnwindData |  |
| 1516 | `?Validate@CWbemInstance@@QEAAJXZ` | `0x85540` | 244 | UnwindData |  |
| 1530 | `?ValidateBuffer@CWbemInstance@@SA_KPEAEHKAEAV?$vector@UEmbeddedObj@@V?$wbem_allocator@UEmbeddedObj@@@@@std@@@Z` | `0x85640` | 287 | UnwindData |  |
| 413 | `?CanBeReconciledWith@CMethodPart@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x85770` | 400 | UnwindData |  |
| 488 | `?CompareTo@CMethodPart@@QEAAJJAEAV1@@Z` | `0x85910` | 245 | UnwindData |  |
| 585 | `?DeleteMethod@CMethodPart@@QEAAJPEBG@Z` | `0x85A10` | 652 | UnwindData |  |
| 595 | `?DeleteSignature@CMethodPart@@IEAAXHH@Z` | `0x85CB0` | 88 | UnwindData |  |
| 1155 | `?IsTouched@CMethodPart@@QEAAHPEBGPEAH@Z` | `0x85D10` | 128 | UnwindData |  |
| 1271 | `?ReconcileWith@CMethodPart@@QEAA?AW4EReconciliation@@AEAV1@@Z` | `0x85DA0` | 130 | UnwindData |  |
| 1400 | `?SetMethodOrigin@CMethodPart@@QEAAJPEBGJ@Z` | `0x85E30` | 60 | UnwindData |  |
| 1506 | `?Update@CMethodPart@@SAJAEAV1@0J@Z` | `0x85E80` | 495 | UnwindData |  |
| 387 | `?AppendArrayPropRangeByHandle@CWbemObject@@UEAAJJJKKPEAX@Z` | `0x861B0` | 539 | UnwindData |  |
| 388 | `?AppendQualifierArrayRange@CWbemObject@@QEAAJPEBG0HJJKKPEAX@Z` | `0x863E0` | 794 | UnwindData |  |
| 397 | `?BeginEnumerationEx@CWbemObject@@UEAAJJJ@Z` | `0x86700` | 307 | UnwindData |  |
| 401 | `?CIMTYPEToVARTYPE@CWbemObject@@UEAAJJPEAG@Z` | `0x86840` | 28 | UnwindData |  |
| 438 | `?CheckBooleanPropQual@CWbemObject@@QEAAHPEBG0@Z` | `0x86870` | 182 | UnwindData |  |
| 475 | `?CompareClassParts@CWbemObject@@UEAAJPEAUIWbemClassObject@@J@Z` | `0x86930` | 573 | UnwindData |  |
| 605 | `?EnabledValidateObject@CWbemObject@@KAJPEAV1@@Z` | `0x86BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | `?FindMethod@CWbemObject@@UEAAJPEBG@Z` | `0x86BC0` | 105 | UnwindData |  |
| 687 | `?GetArrayPropElementByHandle@CWbemObject@@UEAAJJJKPEAK0PEAPEAX@Z` | `0x86C30` | 753 | UnwindData |  |
| 688 | `?GetArrayPropInfoByHandle@CWbemObject@@UEAAJJJPEAPEAGPEAJPEAK@Z` | `0x86F30` | 411 | UnwindData |  |
| 689 | `?GetArrayPropRangeByHandle@CWbemObject@@UEAAJJJKKKPEAK0PEAX@Z` | `0x870E0` | 731 | UnwindData |  |
| 690 | `?GetArrayPropertyHandle@CWbemObject@@QEAAJPEBGPEAJ1@Z` | `0x873D0` | 71 | UnwindData |  |
| 709 | `?GetClassIndex@CWbemObject@@QEAAKPEBG@Z` | `0x87420` | 41 | UnwindData |  |
| 710 | `?GetClassInternal@CWbemObject@@QEAAPEAVCCompressedString@@XZ` | `0x87450` | 31 | UnwindData |  |
| 753 | `?GetGUID@CWbemObject@@UEAAJPEAU_GUID@@@Z` | `0x87480` | 125 | UnwindData |  |
| 772 | `?GetHeapPtrByHandle@CWbemObject@@QEAAKJ@Z` | `0x87510` | 121 | UnwindData |  |
| 773 | `?GetHelpContext@CWbemObject@@UEAAJPEAK@Z` | `0x87590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 774 | `?GetHelpFile@CWbemObject@@UEAAJPEAPEAG@Z` | `0x875A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `?GetKeyOrigin@CWbemObject@@UEAAJJKPEAKPEAG@Z` | `0x875B0` | 433 | UnwindData |  |
| 804 | `?GetKeyString@CWbemObject@@UEAAJJPEAPEAG@Z` | `0x87770` | 482 | UnwindData |  |
| 854 | `?GetMethodQual@CWbemObject@@UEAAJPEBG0JKPEAJPEAK2PEAX@Z` | `0x87960` | 599 | UnwindData |  |
| 893 | `?GetObjQual@CWbemObject@@UEAAJPEBGJKPEAJPEAK2PEAX@Z` | `0x87BC0` | 597 | UnwindData |  |
| 904 | `?GetParentClassFromBlob@CWbemObject@@UEAAJJKPEAXPEAPEAG@Z` | `0x87E20` | 105 | UnwindData |  |
| 933 | `?GetPropertyIndex@CWbemObject@@QEAAJPEBGPEAH@Z` | `0x87E90` | 106 | UnwindData |  |
| 935 | `?GetPropertyInfoByHandle@CWbemObject@@UEAAJJPEAPEAGPEAJ@Z` | `0x87F00` | 69 | UnwindData |  |
| 937 | `?GetPropertyNameFromIndex@CWbemObject@@QEAAJHPEAPEAG@Z` | `0x87F50` | 244 | UnwindData |  |
| 963 | `?GetQualifierArrayInfo@CWbemObject@@QEAAJPEBG0HJPEAJPEAK@Z` | `0x88050` | 320 | UnwindData |  |
| 964 | `?GetQualifierArrayRange@CWbemObject@@QEAAJPEBG0HJKKKPEAK1PEAX@Z` | `0x881A0` | 501 | UnwindData |  |
| 994 | `?GetServerAndNamespace@CWbemObject@@QEAAJPEAVCVar@@@Z` | `0x883A0` | 368 | UnwindData |  |
| 1061 | `?HasRefs@CWbemObject@@QEAAHXZ` | `0x88520` | 115 | UnwindData |  |
| 1147 | `?IsSameClass@CWbemObject@@QEAAHPEAV1@@Z` | `0x885A0` | 190 | UnwindData |  |
| 1166 | `?IsValidPropertyHandle@CWbemObject@@QEAAJJ@Z` | `0x88670` | 38 | UnwindData |  |
| 1172 | `?LocalizeProperties@CWbemObject@@IEAAJH_NPEAUIWbemClassObject@@1AEA_N@Z` | `0x886A0` | 707 | UnwindData |  |
| 1173 | `?LocalizeQualifiers@CWbemObject@@IEAAJH_NPEAUIWbemQualifierSet@@1AEA_N@Z` | `0x88970` | 691 | UnwindData |  |
| 1210 | `?MergeAmended@CWbemObject@@UEAAJJPEAU_IWmiObject@@@Z` | `0x88C30` | 1,836 | UnwindData |  |
| 1244 | `?QueryPropertyFlags@CWbemObject@@UEAAJJPEBG_KPEA_K@Z` | `0x89370` | 306 | UnwindData |  |
| 1310 | `?ReleaseMarshalData@CWbemObject@@UEAAJPEAUIStream@@@Z` | `0x89530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1489 | `?UnmarshalInterface@CWbemObject@@UEAAJPEAUIStream@@AEBU_GUID@@PEAPEAX@Z` | `0x89530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `?RemoveArrayPropElementByHandle@CWbemObject@@UEAAJJJK@Z` | `0x89540` | 33 | UnwindData |  |
| 1314 | `?RemoveArrayPropRangeByHandle@CWbemObject@@UEAAJJJKK@Z` | `0x89570` | 593 | UnwindData |  |
| 1316 | `?RemoveDecoration@CWbemObject@@UEAAJXZ` | `0x897D0` | 71 | UnwindData |  |
| 1320 | `?RemoveQualifierArrayRange@CWbemObject@@QEAAJPEBG0HJKK@Z` | `0x89820` | 622 | UnwindData |  |
| 1337 | `?SetArrayPropElementByHandle@CWbemObject@@UEAAJJJKKPEAX@Z` | `0x89AA0` | 53 | UnwindData |  |
| 1403 | `?SetMethodQual@CWbemObject@@UEAAJPEBG0JKKJKPEAX@Z` | `0x89AE0` | 645 | UnwindData |  |
| 1409 | `?SetObjQual@CWbemObject@@UEAAJPEBGJKKJKPEAX@Z` | `0x89D70` | 621 | UnwindData |  |
| 1410 | `?SetObjectFlags@CWbemObject@@UEAAJJ_K0@Z` | `0x89FF0` | 179 | UnwindData |  |
| 1411 | `?SetObjectMemory@CWbemObject@@UEAAJPEAXK@Z` | `0x8A0B0` | 248 | UnwindData |  |
| 1416 | `?SetPropQual@CWbemObject@@UEAAJPEBG0JKKJKPEAX@Z` | `0x8A1B0` | 642 | UnwindData |  |
| 1432 | `?SetQualifierArrayRange@CWbemObject@@QEAAJPEBG0HJKJKKKPEAX@Z` | `0x8A440` | 1,019 | UnwindData |  |
| 1436 | `?SetServerNamespace@CWbemObject@@UEAAJPEBG0@Z` | `0x8A850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `?Unmerge@CWbemObject@@QEAAKPEAPEAE@Z` | `0x8A870` | 383 | UnwindData |  |
| 1536 | `?ValidatePath@CWbemObject@@QEAAJPEAUParsedObjectPath@@@Z` | `0x8AA00` | 856 | UnwindData |  |
| 837 | `?GetMapped@CLimitationMapping@@QEAAGG@Z` | `0x8ADE0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1319 | `?RemoveProperty@CDataTable@@QEAAXGKK@Z` | `0x8AEE0` | 292 | UnwindData |  |
| 1533 | `?ValidateInstance@CLimitationMapping@@QEAAJPEAVCWbemInstance@@@Z` | `0x8B010` | 206 | UnwindData |  |
| 368 | `?AddQualifierConflicts@CQualifierSet@@IEAAJAEAVCVarVector@@@Z` | `0x8B150` | 718 | UnwindData |  |
| 481 | `?CompareLocalizedSet@CBasicQualifierSet@@QEAAHAEAV1@@Z` | `0x8B510` | 869 | UnwindData |  |
| 519 | `?CopyLocalQualifiers@CQualifierSet@@QEAAJAEAV1@@Z` | `0x8B880` | 690 | UnwindData |  |
| 581 | `?Delete@CQualifierSet@@UEAAJPEBG@Z` | `0x8BB80` | 1,272 | UnwindData |  |
| 593 | `?DeleteQualifier@CQualifierSet@@QEAAJPEBGH@Z` | `0x8C080` | 305 | UnwindData |  |
| 594 | `?DeleteQualifierSet@CQualifierSetList@@QEAAXH@Z` | `0x8C1C0` | 138 | UnwindData |  |
| 955 | `?GetQualifier@CQualifierSet@@QEAAJPEBGPEAJPEAVCTypedValue@@PEAPEAVCFastHeap@@H@Z` | `0x8C250` | 325 | UnwindData |  |
| 1079 | `?InsertQualifierSet@CQualifierSetList@@QEAAJH@Z` | `0x8C3A0` | 481 | UnwindData |  |
| 1294 | `?ReduceQualifierSetSpace@CQualifierSetList@@QEAAXPEAVCBasicQualifierSet@@K@Z` | `0x8C590` | 90 | UnwindData |  |
| 1464 | `?StoreQualifierConflicts@CQualifierSet@@IEAAJPEBGAEAVCVar@@AEAVCQualifierFlavor@@AEAVCVarVector@@@Z` | `0x8C5F0` | 631 | UnwindData |  |
| 1539 | `?ValidateSet@CQualifierSet@@QEAAJPEBGEPEAVCTypedValue@@HH@Z` | `0x8C870` | 2,244 | UnwindData |  |
| 469 | `?Compare@CCompressedString@@QEBAHAEBV1@@Z` | `0x8D140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `?Compare@CCompressedString@@QEBAHPEBD@Z` | `0x8D160` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `?Compare@CCompressedString@@QEBAHPEBG@Z` | `0x8D1A0` | 65 | UnwindData |  |
| 495 | `?ComputeNecessarySpace@CCompressedString@@SAHPEBD@Z` | `0x8D1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `?CreateEmpty@CCompressedString@@SAPEAEPEAE@Z` | `0x8D210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1181 | `?MakeLowercase@CCompressedString@@QEAAXXZ` | `0x8D220` | 68 | UnwindData |  |
| 1382 | `?SetFromAscii@CCompressedString@@QEAAXPEBD_K@Z` | `0x8D270` | 66 | UnwindData |  |
| 389 | `?AppendRange@CUntypedArray@@SAJPEAVCPtrSource@@KKPEAVCFastHeap@@KKPEAX@Z` | `0x8D2C0` | 624 | UnwindData |  |
| 442 | `?CheckIntervalDateTime@CUntypedArray@@SAHAEAVCVarVector@@@Z` | `0x8D540` | 161 | UnwindData |  |
| 445 | `?CheckRangeSizeForGet@CUntypedArray@@KAJKKKKPEAK@Z` | `0x8D680` | 202 | UnwindData |  |
| 980 | `?GetRange@CUntypedArray@@SAJPEAVCPtrSource@@KKPEAVCFastHeap@@KKKPEAKPEAX@Z` | `0x8D750` | 661 | UnwindData |  |
| 1194 | `?MarshalPacket@CWbemMtgtDeliverEventPacket@@QEAAJPEAEKJPEAPEAUIWbemClassObject@@PEAU_GUID@@PEAH@Z` | `0x8E0F0` | 64 | UnwindData |  |
| 88 | `??0CWbemMtgtDeliverEventPacket@@QEAA@PEAEK_N@Z` | `0x8E630` | 32 | UnwindData |  |
| 404 | `?CalculateLength@CWbemMtgtDeliverEventPacket@@QEAAJJPEAPEAUIWbemClassObject@@PEAKAEAVCWbemClassToIdMap@@PEAU_GUID@@PEAH@Z` | `0x8E660` | 184 | UnwindData |  |
| 1193 | `?MarshalPacket@CWbemMtgtDeliverEventPacket@@QEAAJJPEAPEAUIWbemClassObject@@PEAU_GUID@@PEAH@Z` | `0x8E720` | 249 | UnwindData |  |
| 1196 | `?MarshalPacket@CWbemObjectArrayPacket@@QEAAJPEAEKJPEAPEAUIWbemClassObject@@PEAU_GUID@@PEAH@Z` | `0x8E820` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1368 | `?SetData@CWbemMtgtDeliverEventPacket@@QEAAXPEAEK_N@Z` | `0x8E850` | 422 | UnwindData |  |
| 1490 | `?UnmarshalPacket@CWbemMtgtDeliverEventPacket@@QEAAJAEAJAEAPEAPEAUIWbemClassObject@@AEAVCWbemClassCache@@@Z` | `0x8EA00` | 416 | UnwindData |  |
| 1 | `??0?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@QEAA@AEBV0@@Z` | `0x8ECF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@QEAA@AEBV0@@Z` | `0x8ED10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@QEAA@AEBV0@@Z` | `0x8ED30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@QEAA@AEBV0@@Z` | `0x8ED30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@QEAA@AEBV0@@Z` | `0x8ED50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@QEAA@AEBV0@@Z` | `0x8ED50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@QEAA@AEBV0@@Z` | `0x8ED50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??0?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAA@AEAV0@@Z` | `0x8ED70` | 36 | UnwindData |  |
| 17 | `??0?$CRefedPointerArray@VCWmiTextSource@@@@QEAA@AEAV0@@Z` | `0x8EDA0` | 29 | UnwindData |  |
| 71 | `??0CWbemCallSecurity@@QEAA@AEBV0@@Z` | `0x8EE10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `??0CWbemEnumMarshaling@@QEAA@AEBV0@@Z` | `0x8EE60` | 119 | UnwindData |  |
| 81 | `??0CWbemFetchRefrMgr@@QEAA@AEBV0@@Z` | `0x8EEE0` | 73 | UnwindData |  |
| 83 | `??0CWbemGuidToClassMap@@QEAA@AEBV0@@Z` | `0x8EF30` | 66 | UnwindData |  |
| 92 | `??0CWbemRefreshingSvc@@QEAA@AEBV0@@Z` | `0x8EF80` | 111 | UnwindData |  |
| 98 | `??0CWmiObjectFactory@@QEAA@AEBV0@@Z` | `0x8F000` | 73 | UnwindData |  |
| 100 | `??0CWmiTextSourceArray@@QEAA@AEAV0@@Z` | `0x8F050` | 29 | UnwindData |  |
| 103 | `??0XCfgRefrSrvc@CWbemRefreshingSvc@@QEAA@$$QEAV01@@Z` | `0x8F080` | 39 | UnwindData |  |
| 104 | `??0XCfgRefrSrvc@CWbemRefreshingSvc@@QEAA@AEBV01@@Z` | `0x8F080` | 39 | UnwindData |  |
| 106 | `??0XEnumMarshaling@CWbemEnumMarshaling@@QEAA@$$QEAV01@@Z` | `0x8F0B0` | 39 | UnwindData |  |
| 107 | `??0XEnumMarshaling@CWbemEnumMarshaling@@QEAA@AEBV01@@Z` | `0x8F0B0` | 39 | UnwindData |  |
| 109 | `??0XFetchRefrMgr@CWbemFetchRefrMgr@@QEAA@$$QEAV01@@Z` | `0x8F0E0` | 39 | UnwindData |  |
| 110 | `??0XFetchRefrMgr@CWbemFetchRefrMgr@@QEAA@AEBV01@@Z` | `0x8F0E0` | 39 | UnwindData |  |
| 112 | `??0XObjectFactory@CWmiObjectFactory@@QEAA@$$QEAV01@@Z` | `0x8F110` | 39 | UnwindData |  |
| 113 | `??0XObjectFactory@CWmiObjectFactory@@QEAA@AEBV01@@Z` | `0x8F110` | 39 | UnwindData |  |
| 115 | `??0XObjectTextSrc@CWmiObjectTextSrc@@QEAA@$$QEAV01@@Z` | `0x8F140` | 39 | UnwindData |  |
| 116 | `??0XObjectTextSrc@CWmiObjectTextSrc@@QEAA@AEBV01@@Z` | `0x8F140` | 39 | UnwindData |  |
| 118 | `??0XWbemRefrSvc@CWbemRefreshingSvc@@QEAA@$$QEAV01@@Z` | `0x8F170` | 39 | UnwindData |  |
| 119 | `??0XWbemRefrSvc@CWbemRefreshingSvc@@QEAA@AEBV01@@Z` | `0x8F170` | 39 | UnwindData |  |
| 121 | `??0XWbemRemoteRefr@CWbemRemoteRefresher@@QEAA@$$QEAV01@@Z` | `0x8F1A0` | 39 | UnwindData |  |
| 122 | `??0XWbemRemoteRefr@CWbemRemoteRefresher@@QEAA@AEBV01@@Z` | `0x8F1A0` | 39 | UnwindData |  |
| 123 | `??0XWbemRemoteRefr@CWbemRemoteRefresher@@QEAA@PEAV1@@Z` | `0x8F1D0` | 39 | UnwindData |  |
| 169 | `??4?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@QEAAAEAV0@AEBV0@@Z` | `0x8F200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `??4?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@QEAAAEAV0@AEBV0@@Z` | `0x8F200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `??4?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@QEAAAEAV0@AEBV0@@Z` | `0x8F200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `??4?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@QEAAAEAV0@AEBV0@@Z` | `0x8F200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `??4?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@QEAAAEAV0@AEBV0@@Z` | `0x8F200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `??4?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@QEAAAEAV0@AEBV0@@Z` | `0x8F200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `??4?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@QEAAAEAV0@AEBV0@@Z` | `0x8F200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `??4?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAAEAV0@AEAV0@@Z` | `0x8F220` | 31 | UnwindData |  |
| 177 | `??4?$CRefedPointerArray@VCWmiTextSource@@@@QEAAAEAV0@$$QEAV0@@Z` | `0x8F220` | 31 | UnwindData |  |
| 178 | `??4?$CRefedPointerArray@VCWmiTextSource@@@@QEAAAEAV0@AEAV0@@Z` | `0x8F220` | 31 | UnwindData |  |
| 258 | `??4CWmiTextSourceArray@@QEAAAEAV0@AEAV0@@Z` | `0x8F220` | 31 | UnwindData |  |
| 249 | `??4CWbemEnumMarshaling@@QEAAAEAV0@AEBV0@@Z` | `0x8F250` | 171 | UnwindData |  |
| 250 | `??4CWbemFetchRefrMgr@@QEAAAEAV0@AEBV0@@Z` | `0x8F310` | 56 | UnwindData |  |
| 257 | `??4CWmiObjectFactory@@QEAAAEAV0@AEBV0@@Z` | `0x8F310` | 56 | UnwindData |  |
| 251 | `??4CWbemGuidToClassMap@@QEAAAEAV0@AEBV0@@Z` | `0x8F350` | 99 | UnwindData |  |
| 254 | `??4CWbemRefreshingSvc@@QEAAAEAV0@AEBV0@@Z` | `0x8F3C0` | 93 | UnwindData |  |
| 263 | `??4XCfgRefrSrvc@CWbemRefreshingSvc@@QEAAAEAV01@$$QEAV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 264 | `??4XCfgRefrSrvc@CWbemRefreshingSvc@@QEAAAEAV01@AEBV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 265 | `??4XEnumMarshaling@CWbemEnumMarshaling@@QEAAAEAV01@$$QEAV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 266 | `??4XEnumMarshaling@CWbemEnumMarshaling@@QEAAAEAV01@AEBV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 267 | `??4XFetchRefrMgr@CWbemFetchRefrMgr@@QEAAAEAV01@$$QEAV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 268 | `??4XFetchRefrMgr@CWbemFetchRefrMgr@@QEAAAEAV01@AEBV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 269 | `??4XObjectFactory@CWmiObjectFactory@@QEAAAEAV01@$$QEAV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 270 | `??4XObjectFactory@CWmiObjectFactory@@QEAAAEAV01@AEBV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 271 | `??4XObjectTextSrc@CWmiObjectTextSrc@@QEAAAEAV01@$$QEAV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 272 | `??4XObjectTextSrc@CWmiObjectTextSrc@@QEAAAEAV01@AEBV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 273 | `??4XWbemRefrSvc@CWbemRefreshingSvc@@QEAAAEAV01@$$QEAV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 274 | `??4XWbemRefrSvc@CWbemRefreshingSvc@@QEAAAEAV01@AEBV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 275 | `??4XWbemRemoteRefr@CWbemRemoteRefresher@@QEAAAEAV01@$$QEAV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 276 | `??4XWbemRemoteRefr@CWbemRemoteRefresher@@QEAAAEAV01@AEBV01@@Z` | `0x8F430` | 24 | UnwindData |  |
| 349 | `??_F?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXXZ` | `0x8F450` | 1,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `?Discard@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXH@Z` | `0x8FAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 691 | `?GetArrayPtr@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAPEAPEAVCWmiTextSource@@XZ` | `0x8FAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `?GetHandleType@CWbemThreadSecurityHandle@@UEAAJPEAK@Z` | `0x8FB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1033 | `?GetTokenOrigin@CWbemThreadSecurityHandle@@UEAAJPEAW4tag_WMI_THREAD_SECURITY_ORIGIN@@@Z` | `0x8FB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `?InsertAt@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAA_NHPEAVCWmiTextSource@@@Z` | `0x8FB20` | 46 | UnwindData |  |
| 1315 | `?RemoveAt@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAA_NHPEAPEAVCWmiTextSource@@@Z` | `0x8FFF0` | 117 | UnwindData |  |
| 1339 | `?SetAt@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXHPEAVCWmiTextSource@@PEAPEAV2@@Z` | `0x90070` | 131 | UnwindData |  |
| 1441 | `?SetSize@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXH@Z` | `0x90100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1469 | `?Swap@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXHH@Z` | `0x90120` | 120 | UnwindData |  |
| 1478 | `?Trim@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAXXZ` | `0x901A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1481 | `?UnbindPtr@?$CPointerArray@VCWmiTextSource@@V?$CReferenceManager@VCWmiTextSource@@@@VCFlexArray@@@@QEAAPEAPEAVCWmiTextSource@@XZ` | `0x901C0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1572 | `GetObjectCount` | `0x90590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1484 | `?Uninit@CWbemFetchRefrMgr@@QEAAJXZ` | `0x905A0` | 102 | UnwindData |  |
| 1485 | `?Uninit@XFetchRefrMgr@CWbemFetchRefrMgr@@UEAAJXZ` | `0x90610` | 22,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `?AddObjectToRefresherByTemplate@CWbemRefreshingSvc@@MEAAJPEAU_WBEM_REFRESHER_ID@@PEAUIWbemClassObject@@JPEAUIWbemContext@@KPEAU_WBEM_REFRESH_INFO@@PEAK@Z` | `0x95D10` | 462 | UnwindData |  |
| 364 | `?AddObjectToRefresherByTemplate@XWbemRefrSvc@CWbemRefreshingSvc@@UEAAJPEAU_WBEM_REFRESHER_ID@@PEAUIWbemClassObject@@JPEAUIWbemContext@@KPEAU_WBEM_REFRESH_INFO@@PEAK@Z` | `0x95EF0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `?GetGuid@XWbemRemoteRefr@CWbemRemoteRefresher@@UEAAJJPEAU_GUID@@@Z` | `0x96010` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 989 | `?GetRemoteRefresher@CWbemRefreshingSvc@@MEAAJPEAU_WBEM_REFRESHER_ID@@JKPEAPEAUIWbemRemoteRefresher@@PEAU_GUID@@PEAK@Z` | `0x96070` | 564 | UnwindData |  |
| 990 | `?GetRemoteRefresher@XWbemRefrSvc@CWbemRefreshingSvc@@UEAAJPEAU_WBEM_REFRESHER_ID@@JKPEAPEAUIWbemRemoteRefresher@@PEAU_GUID@@PEAK@Z` | `0x962B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1275 | `?ReconnectRemoteRefresher@CWbemRefreshingSvc@@MEAAJPEAU_WBEM_REFRESHER_ID@@JJKPEAU_WBEM_RECONNECT_INFO@@PEAU_WBEM_RECONNECT_RESULTS@@PEAK@Z` | `0x962C0` | 856 | UnwindData |  |
| 1276 | `?ReconnectRemoteRefresher@XWbemRefrSvc@CWbemRefreshingSvc@@UEAAJPEAU_WBEM_REFRESHER_ID@@JJKPEAU_WBEM_RECONNECT_INFO@@PEAU_WBEM_RECONNECT_RESULTS@@PEAK@Z` | `0x96620` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `?RemoteRefresh@XWbemRemoteRefr@CWbemRemoteRefresher@@UEAAJJPEAJPEAPEAU_WBEM_REFRESHED_OBJECT@@@Z` | `0x96750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1317 | `?RemoveObjectFromRefresher@CWbemRefreshingSvc@@MEAAJPEAU_WBEM_REFRESHER_ID@@JJKPEAK@Z` | `0x96760` | 303 | UnwindData |  |
| 1318 | `?RemoveObjectFromRefresher@XWbemRefrSvc@CWbemRefreshingSvc@@UEAAJPEAU_WBEM_REFRESHER_ID@@JJKPEAK@Z` | `0x968A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `?ResetRefreshInfo@CWbemRefreshingSvc@@IEAAJPEAU_WBEM_REFRESH_INFO@@@Z` | `0x968B0` | 121 | UnwindData |  |
| 1461 | `?StopRefreshing@XWbemRemoteRefr@CWbemRemoteRefresher@@UEAAJJPEAJJ@Z` | `0x96A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1544 | `?WrapRemoteRefresher@CWbemRefreshingSvc@@IEAAJPEAPEAUIWbemRemoteRefresher@@@Z` | `0x96A60` | 322 | UnwindData |  |
| 78 | `??0CWbemDataPacket@@QEAA@PEAEK_N@Z` | `0x9A050` | 24 | UnwindData |  |
| 215 | `??4CInternalString@@QEAAHPEBG@Z` | `0x9A220` | 155 | UnwindData |  |
| 531 | `?Create@CWmiObjectFactory@@QEAAJPEAUIUnknown@@KAEBU_GUID@@1PEAPEAX@Z` | `0x9B170` | 579 | UnwindData |  |
| 532 | `?Create@XObjectFactory@CWmiObjectFactory@@UEAAJPEAUIUnknown@@KAEBU_GUID@@1PEAPEAX@Z` | `0x9B3C0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `?CreateFromText@XObjectTextSrc@CWmiObjectTextSrc@@UEAAJJPEAGKPEAUIWbemContext@@PEAPEAUIWbemClassObject@@@Z` | `0x9B590` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `??4CWbemCallSecurity@@QEAAAEAV0@AEBV0@@Z` | `0x9B7D0` | 153 | UnwindData |  |
| 697 | `?GetAuthentication@CWbemCallSecurity@@QEAAJPEAK@Z` | `0x9B910` | 134 | UnwindData |  |
| 700 | `?GetAuthenticationLuid@CWbemCallSecurity@@UEAAJPEAX@Z` | `0x9BAA0` | 289 | UnwindData |  |
| 701 | `?GetAuthenticationLuid@CWbemThreadSecurityHandle@@UEAAJPEAX@Z` | `0x9BBD0` | 126 | UnwindData |  |
| 777 | `?GetImpersonation@CWbemCallSecurity@@UEAAJPEAK@Z` | `0x9BC60` | 324 | UnwindData |  |
| 778 | `?GetImpersonation@CWbemThreadSecurityHandle@@UEAAJPEAK@Z` | `0x9BDB0` | 233 | UnwindData |  |
| 1032 | `?GetToken@CWbemThreadSecurityHandle@@UEAAJPEAPEAX@Z` | `0x9C1A0` | 263 | UnwindData |  |
| 1043 | `?GetUser@CWbemCallSecurity@@UEAAJPEAKPEAG@Z` | `0x9C5C0` | 305 | UnwindData |  |
| 1044 | `?GetUser@CWbemThreadSecurityHandle@@UEAAJPEAKPEAG@Z` | `0x9C700` | 126 | UnwindData |  |
| 1045 | `?GetUserSid@CWbemCallSecurity@@UEAAJPEAKPEAX@Z` | `0x9C920` | 305 | UnwindData |  |
| 1046 | `?GetUserSid@CWbemThreadSecurityHandle@@UEAAJPEAKPEAX@Z` | `0x9CA60` | 126 | UnwindData |  |
| 1217 | `?New@CWbemThreadSecurityHandle@@SAPEAV1@XZ` | `0x9CAF0` | 50 | UnwindData |  |
| 1570 | `DllRegisterServer` | `0x9E340` | 412 | UnwindData |  |
| 1571 | `DllUnregisterServer` | `0x9E4F0` | 452 | UnwindData |  |
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
| 324 | `??_7CWbemClass@@6B_IWmiObject@@@` | `0xADB48` | 2,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `??_7CWbemObject@@6BIWbemConstructClassObject@@@` | `0xAE640` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `??_7CWbemObject@@6B_IWmiObject@@@` | `0xAE678` | 1,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `??_7CWbemCallSecurity@@6B_IWmiCallSec@@@` | `0xAEB00` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `??_7CWbemCallSecurity@@6BIServerSecurity@@@` | `0xAEB48` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `??_7CWbemThreadSecurityHandle@@6B@` | `0xAEB80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `??_7CMethodQualifierSet@@6B@` | `0xAEBE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `??_7CMethodQualifierSetContainer@@6B@` | `0xAEC40` | 264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `??_7?$CImpl@U_IWbemConfigureRefreshingSvcs@@VCWbemRefreshingSvc@@@@6B@` | `0xAED48` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `??_7?$CImpl@U_IWbemEnumMarshaling@@VCWbemEnumMarshaling@@@@6B@` | `0xAED48` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `??_7?$CImpl@U_IWmiObjectFactory@@VCWmiObjectFactory@@@@6B@` | `0xAED48` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `??_7CWbemEnumMarshaling@@6B@` | `0xAED68` | 1,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `??_7XEnumMarshaling@CWbemEnumMarshaling@@6B@` | `0xAF430` | 232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `??_7XCfgRefrSrvc@CWbemRefreshingSvc@@6B@` | `0xAF518` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `??_7XWbemRefrSvc@CWbemRefreshingSvc@@6B@` | `0xAF538` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `??_7CWbemRefreshingSvc@@6B@` | `0xAF5B8` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `??_7?$CImpl@UIWbemRefreshingServices@@VCWbemRefreshingSvc@@@@6B@` | `0xAF628` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `??_7CWmiObjectFactory@@6B@` | `0xAF6D0` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `??_7XObjectFactory@CWmiObjectFactory@@6B@` | `0xAF708` | 136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `??_7XFetchRefrMgr@CWbemFetchRefrMgr@@6B@` | `0xAF790` | 152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `??_7CWbemFetchRefrMgr@@6B@` | `0xAF828` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `??_7?$CImpl@UIWbemRemoteRefresher@@VCWbemRemoteRefresher@@@@6B@` | `0xAF860` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `??_7?$CImpl@U_IWbemFetchRefresherMgr@@VCWbemFetchRefrMgr@@@@6B@` | `0xAF860` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `??_7XObjectTextSrc@CWmiObjectTextSrc@@6B@` | `0xAF890` | 328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `??_7?$CImpl@UIWbemObjectTextSrc@@VCWmiObjectTextSrc@@@@6B@` | `0xAF9D8` | 3,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `??_7XWbemRemoteRefr@CWbemRemoteRefresher@@6B@` | `0xB0650` | 219,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1566 | `?s_pszStartingCharsLCase@CReservedWordTable@@0PEBGEB` | `0xE6020` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1567 | `?s_pszStartingCharsUCase@CReservedWordTable@@0PEBGEB` | `0xE6028` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1563 | `?s_apwszReservedWords@CReservedWordTable@@0PAPEBGA` | `0xE6030` | 1,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1562 | `?s_abSignature@CWbemDataPacket@@1PAEA` | `0xE6428` | 2,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1565 | `?s_pRefrMgr@CWbemFetchRefrMgr@@1PEAU_IWbemRefresherMgr@@EA` | `0xE6F40` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1564 | `?s_cs@CWbemFetchRefrMgr@@1VCStaticCritSec@@A` | `0xE6FE0` | 0 | Indeterminate |  |
