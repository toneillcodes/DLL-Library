# Binary Specification: esscli.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\esscli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eb3f9f4e011fc99a47e9571694f1e954cfacbae29a953a9f688a15348b838e44`
* **Total Exported Functions:** 169

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 155 | `?SetLength@CObjectInfo@@QEAA_NJ@Z` | `0x4540` | 138 | UnwindData |  |
| 80 | `?CombineWith@CEvalTree@@QEAAJAEAV1@PEAVCContextMetaData@@HJ@Z` | `0x45D0` | 1,296 | UnwindData |  |
| 78 | `?Combine@CEvalTree@@SAJPEAVCEvalNode@@0HPEAVCContextMetaData@@AEAVCImplicationList@@_N3PEAPEAV2@@Z` | `0x4AF0` | 3,231 | UnwindData |  |
| 118 | `?InnerCombine@CEvalTree@@KAJPEAVCEvalNode@@0HPEAVCContextMetaData@@AEAVCImplicationList@@_N3PEAPEAV2@@Z` | `0x57A0` | 3,524 | UnwindData |  |
| 89 | `?CreateFromQuery@CEvalTree@@QEAAJPEAVCContextMetaData@@PEAUQL_LEVEL_1_RPN_EXPRESSION@@JJ@Z` | `0x7180` | 45 | UnwindData |  |
| 90 | `?CreateFromQuery@CEvalTree@@QEAAJPEAVCContextMetaData@@PEBGHPEAUQL_LEVEL_1_TOKEN@@JJ@Z` | `0x71C0` | 4,608 | UnwindData |  |
| 87 | `?CreateFromConjunction@CEvalTree@@SAJPEAVCContextMetaData@@AEAVCImplicationList@@PEAVCConjunction@@PEAPEAVCEvalNode@@@Z` | `0x83D0` | 1,476 | UnwindData |  |
| 104 | `?GetClass@CContextMetaData@@QEAAJPEBGPEAPEAU_IWmiObject@@@Z` | `0x8A10` | 179 | UnwindData |  |
| 68 | `?BuildFromToken@CEvalTree@@SAJPEAVCContextMetaData@@AEAVCImplicationList@@AEAUQL_LEVEL_1_TOKEN@@PEAPEAVCEvalNode@@@Z` | `0x8AD0` | 7,618 | UnwindData |  |
| 110 | `?GetLimitingQueryForInstanceClass@CQueryAnalyser@@SAJPEAUQL_LEVEL_1_RPN_EXPRESSION@@AEAUCClassInformation@@AEAPEAG@Z` | `0xDA40` | 3,351 | UnwindData |  |
| 111 | `?GetNecessaryQueryForClass@CQueryAnalyser@@SAJPEAUQL_LEVEL_1_RPN_EXPRESSION@@PEAUIWbemClassObject@@AEAVCWStringArray@@AEAPEAU2@@Z` | `0xE760` | 3,110 | UnwindData |  |
| 160 | `?SimplifyQueryForChild@CQueryAnalyser@@SAJPEAUQL_LEVEL_1_RPN_EXPRESSION@@PEBGPEAUIWbemClassObject@@PEAVCContextMetaData@@AEAPEAU2@@Z` | `0xF830` | 2,509 | UnwindData |  |
| 161 | `?SimplifyTokenForChild@CQueryAnalyser@@KAHAEAUQL_LEVEL_1_TOKEN@@PEBGPEAUIWbemClassObject@@PEAVCContextMetaData@@@Z` | `0x10210` | 1,522 | UnwindData |  |
| 70 | `?CanPointToClass@CQueryAnalyser@@SAJPEAUIWbemClassObject@@PEBG1PEAVCContextMetaData@@@Z` | `0x10E50` | 1,441 | UnwindData |  |
| 165 | `?ValidateSQLDateTime@CQueryAnalyser@@KAHPEBG@Z` | `0x11400` | 196 | UnwindData |  |
| 62 | `?Allocate@CTempMemoryManager@@QEAAPEAX_K@Z` | `0x12CA0` | 631 | UnwindData |  |
| 95 | `?Evaluate@CEvalTree@@QEAAJPEAUIWbemObjectAccess@@AEAVCSortedArray@@@Z` | `0x13440` | 1,006 | UnwindData |  |
| 77 | `?CloneNode@CEvalNode@@SAPEAV1@PEBV1@@Z` | `0x14AF0` | 136 | UnwindData |  |
| 19 | `??0CStandardMetaData@@QEAA@PEAUIWbemServices@@@Z` | `0x14D00` | 77 | UnwindData |  |
| 10 | `??0CMetaData@@QEAA@XZ` | `0x14D60` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `?Evaluate@CEvalTree@@SAJAEAVCObjectInfo@@PEAVCEvalNode@@AEAVCSortedArray@@@Z` | `0x14EB0` | 201 | UnwindData |  |
| 117 | `?GetType@CEvalNode@@SAHPEAV1@@Z` | `0x15140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0CContextMetaData@@QEAA@PEAVCMetaData@@PEAUIWbemContext@@@Z` | `0x15160` | 69 | UnwindData |  |
| 24 | `??1CContextMetaData@@QEAA@XZ` | `0x15340` | 60 | UnwindData |  |
| 131 | `?IsTokenAboutClass@CQueryAnalyser@@KAHAEAUQL_LEVEL_1_TOKEN@@PEAUIWbemClassObject@@AEAVCWStringArray@@@Z` | `0x18F40` | 214 | UnwindData |  |
| 157 | `?SetObjectAt@CObjectInfo@@QEAAXJPEAU_IWmiObject@@@Z` | `0x19370` | 27 | UnwindData |  |
| 149 | `?Release@CMetaData@@UEAAKXZ` | `0x19520` | 54 | UnwindData |  |
| 140 | `?Optimize@CEvalTree@@QEAAJPEAVCContextMetaData@@@Z` | `0x19790` | 427 | UnwindData |  |
| 166 | `DllCanUnloadNow` | `0x1A810` | 210 | UnwindData |  |
| 32 | `??1CStandardMetaData@@UEAA@XZ` | `0x1AC90` | 62 | UnwindData |  |
| 73 | `?Clear@CObjectInfo@@QEAAXXZ` | `0x1B160` | 16 | UnwindData |  |
| 28 | `??1CObjectInfo@@QEAA@XZ` | `0x1B800` | 102 | UnwindData |  |
| 79 | `?CombineLeafWithBranch@CEvalTree@@KAJPEAVCValueNode@@PEAVCBranchingNode@@HPEAVCContextMetaData@@AEAVCImplicationList@@_N4PEAPEAVCEvalNode@@@Z` | `0x1B870` | 486 | UnwindData |  |
| 143 | `?OrQueryExpressions@CQueryAnalyser@@KAJPEAUQL_LEVEL_1_RPN_EXPRESSION@@00@Z` | `0x1BA80` | 326 | UnwindData |  |
| 127 | `?IsMergeAdvisable@CEvalTree@@SAJPEAVCEvalNode@@0AEAVCImplicationList@@@Z` | `0x1BBD0` | 371 | UnwindData |  |
| 81 | `?Compare@CEvalTree@@SAHPEAVCEvalNode@@0@Z` | `0x1C1D0` | 61 | UnwindData |  |
| 93 | `?DecorateObject@CTimeKeeper@@QEAA_NPEAU_IWmiObject@@@Z` | `0x1C9B0` | 302 | UnwindData |  |
| 88 | `?CreateFromDNF@CEvalTree@@QEAAJPEAVCContextMetaData@@AEAVCImplicationList@@PEAVCDNFExpression@@PEAPEAVCEvalNode@@@Z` | `0x1CBA0` | 104 | UnwindData |  |
| 26 | `??1CEvalTree@@QEAA@XZ` | `0x1CDF0` | 150 | UnwindData |  |
| 66 | `?AppendQueryExpression@CQueryAnalyser@@KAXPEAUQL_LEVEL_1_RPN_EXPRESSION@@0@Z` | `0x1D2B0` | 78 | UnwindData |  |
| 106 | `?GetClass@CStandardMetaData@@UEAAJPEBGPEAUIWbemContext@@PEAPEAU_IWmiObject@@@Z` | `0x1D490` | 347 | UnwindData |  |
| 124 | `?IsInvalid@CEvalNode@@SA_NPEAV1@@Z` | `0x1DEB0` | 2,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0CEvalTree@@QEAA@XZ` | `0x1E8A0` | 68 | UnwindData |  |
| 105 | `?GetClass@CMetaData@@UEAAJPEBGPEAUIWbemContext@@PEAPEAUIWbemClassObject@@@Z` | `0x1F840` | 165 | UnwindData |  |
| 130 | `?IsPropertyInClass@CQueryAnalyser@@KAHAEAVCPropertyName@@PEAUIWbemClassObject@@AEAVCWStringArray@@@Z` | `0x1FAF0` | 162 | UnwindData |  |
| 114 | `?GetObjectAt@CObjectInfo@@QEAAPEAU_IWmiObject@@J@Z` | `0x1FBA0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `?Free@CTempMemoryManager@@QEAAXPEAX_K@Z` | `0x1FCC0` | 304 | UnwindData |  |
| 16 | `??0CSortedArray@@QEAA@HH@Z` | `0x20230` | 36 | UnwindData |  |
| 139 | `?Optimize@CEvalNode@@UEAAJPEAVCContextMetaData@@PEAPEAV1@@Z` | `0x202F0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?AddRef@CMetaData@@UEAAKXZ` | `0x20620` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??1CMetaData@@UEAA@XZ` | `0x20710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??1CSortedArray@@QEAA@XZ` | `0x20730` | 25 | UnwindData |  |
| 107 | `?GetDefiniteInstanceClasses@CQueryAnalyser@@SAJPEAUQL_LEVEL_1_RPN_EXPRESSION@@AEAPEAVCClassInfoArray@@@Z` | `0x20970` | 1,304 | UnwindData |  |
| 120 | `?IsAllFalse@CEvalNode@@SA_NPEAV1@@Z` | `0x20E90` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `?IsAllFalse@CEvalNode@@UEAA_NXZ` | `0x20F40` | 2,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `?IsInvalid@CEvalNode@@UEAA_NXZ` | `0x20F40` | 2,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `?IsNoop@CEvalNode@@UEAA_NH@Z` | `0x20F40` | 2,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `?Size@CSortedArray@@QEBAHXZ` | `0x21730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `?UtilizeGuarantee@CEvalTree@@QEAAJAEAV1@PEAVCContextMetaData@@@Z` | `0x21750` | 528 | UnwindData |  |
| 65 | `?AndQueryExpressions@CQueryAnalyser@@KAJPEAUQL_LEVEL_1_RPN_EXPRESSION@@00@Z` | `0x21C80` | 164 | UnwindData |  |
| 91 | `?CreateFromQuery@CEvalTree@@QEAAJPEAVCContextMetaData@@PEBGJJ@Z` | `0x21D70` | 419 | UnwindData |  |
| 11 | `??0CObjectInfo@@QEAA@XZ` | `0x22040` | 1,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `?ApplyPredicate@CEvalTree@@QEAAJPEAVCLeafPredicate@@@Z` | `0x22770` | 94 | UnwindData |  |
| 1 | `??0CClassInfoArray@@QEAA@XZ` | `0x238C0` | 209 | UnwindData |  |
| 113 | `?GetNumClasses@CClassInfoArray@@QEAAHXZ` | `0x23A60` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0CTempMemoryManager@@QEAA@XZ` | `0x23FC0` | 130 | UnwindData |  |
| 85 | `?CopyDataFrom@CSortedArray@@QEAAJPEB_KI@Z` | `0x24050` | 209 | UnwindData |  |
| 153 | `?RoundUp@CTempMemoryManager@@IEAA_K_K@Z` | `0x24130` | 29 | UnwindData |  |
| 33 | `??1CTempMemoryManager@@QEAA@XZ` | `0x24180` | 81 | UnwindData |  |
| 76 | `?Clear@CTempMemoryManager@@QEAAXXZ` | `0x241E0` | 124 | UnwindData |  |
| 147 | `?Rebase@CEvalTree@@QEAAX_K@Z` | `0x243B0` | 99 | UnwindData |  |
| 152 | `?RemoveIndex@CEvalTree@@QEAAJH@Z` | `0x24520` | 113 | UnwindData |  |
| 21 | `??0CTimeKeeper@@QEAA@XZ` | `0x24AE0` | 45 | UnwindData |  |
| 5 | `??0CEvalNode@@QEAA@AEBV0@@Z` | `0x25110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0CEvalNode@@QEAA@XZ` | `0x25110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `?IsFalse@CEvalTree@@QEAA_NXZ` | `0x25130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??1CEvalNode@@UEAA@XZ` | `0x25140` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??1CTimeKeeper@@QEAA@XZ` | `0x251C0` | 25 | UnwindData |  |
| 109 | `?GetLength@CObjectInfo@@QEAAJXZ` | `0x251E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `?IsLimited@CClassInfoArray@@QEAAHXZ` | `0x251E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `?SetLimited@CClassInfoArray@@QEAAXH@Z` | `0x251F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `?SetSize@CSortedArray@@QEAAXH@Z` | `0x25250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `?GetArrayPtr@CSortedArray@@QEAAPEA_KXZ` | `0x25270` | 6,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0CMetaData@@QEAA@AEBV0@@Z` | `0x26C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0CStandardMetaData@@QEAA@AEBV0@@Z` | `0x26C40` | 60 | UnwindData |  |
| 37 | `??4CContextMetaData@@QEAAAEAV0@AEBV0@@Z` | `0x26C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `??4CObjectInfo@@QEAAAEAV0@AEBV0@@Z` | `0x26C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `??4CMetaData@@QEAAAEAV0@AEBV0@@Z` | `0x26CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??4CStandardMetaData@@QEAAAEAV0@AEBV0@@Z` | `0x26CD0` | 44 | UnwindData |  |
| 75 | `?Clear@CStandardMetaData@@QEAAXXZ` | `0x26D90` | 42 | UnwindData |  |
| 146 | `?QueryInterface@CMetaData@@UEAAJAEBU_GUID@@PEAPEAX@Z` | `0x26DC0` | 94 | UnwindData |  |
| 14 | `??0CReuseMemoryManager@@QEAA@_K0@Z` | `0x26E50` | 101 | UnwindData |  |
| 30 | `??1CReuseMemoryManager@@QEAA@XZ` | `0x26EC0` | 56 | UnwindData |  |
| 44 | `??4CReuseMemoryManager@@QEAAAEAV0@AEBV0@@Z` | `0x26F00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `??4CTempMemoryManager@@QEAAAEAV0@AEBV0@@Z` | `0x26F40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?Allocate@CReuseMemoryManager@@QEAAPEAXXZ` | `0x26F70` | 123 | UnwindData |  |
| 74 | `?Clear@CReuseMemoryManager@@QEAAXXZ` | `0x27000` | 109 | UnwindData |  |
| 98 | `?Free@CReuseMemoryManager@@QEAAXPEAX@Z` | `0x27080` | 134 | UnwindData |  |
| 7 | `??0CEvalTree@@QEAA@AEBV0@@Z` | `0x2AFF0` | 86 | UnwindData |  |
| 12 | `??0CPropertyProjectionFilter@@QEAA@AEBV0@@Z` | `0x2B310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0CPropertyProjectionFilter@@QEAA@XZ` | `0x2B330` | 206 | UnwindData |  |
| 15 | `??0CSortedArray@@QEAA@AEAV0@@Z` | `0x2B410` | 36 | UnwindData |  |
| 17 | `??0CSortedArray@@QEAA@IPEA_K@Z` | `0x2B440` | 118 | UnwindData |  |
| 29 | `??1CPropertyProjectionFilter@@QEAA@XZ` | `0x2BB70` | 61 | UnwindData |  |
| 38 | `??4CEvalTree@@QEAAXAEBV0@@Z` | `0x2BBF0` | 374 | UnwindData |  |
| 41 | `??4CPropertyProjectionFilter@@QEAAAEAV0@AEBV0@@Z` | `0x2BEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??4CSortedArray@@QEAAXAEBV0@@Z` | `0x2BF00` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??_FCSortedArray@@QEAAXXZ` | `0x2C0B0` | 2,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `?Add@CSortedArray@@QEAAH_K@Z` | `0x2C970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?AddDataFrom@CSortedArray@@QEAAJAEBV1@@Z` | `0x2C990` | 520 | UnwindData |  |
| 58 | `?AddDataFrom@CSortedArray@@QEAAJPEB_KI@Z` | `0x2CBA0` | 469 | UnwindData |  |
| 59 | `?AddProperty@CPropertyProjectionFilter@@QEAA_NAEBVCPropertyName@@@Z` | `0x2CD80` | 156 | UnwindData |  |
| 69 | `?BuildTwoPropFromToken@CEvalTree@@SAJPEAVCContextMetaData@@AEAVCImplicationList@@AEAUQL_LEVEL_1_TOKEN@@PEAPEAVCEvalNode@@@Z` | `0x2D0E0` | 3,793 | UnwindData |  |
| 72 | `?Clear@CEvalTree@@QEAA_NXZ` | `0x2DFC0` | 119 | UnwindData |  |
| 82 | `?Compare@CSortedArray@@QEAAHAEAV1@@Z` | `0x31460` | 144 | UnwindData |  |
| 84 | `?CopyDataFrom@CSortedArray@@QEAAJAEBV1@@Z` | `0x31640` | 37 | UnwindData |  |
| 86 | `?CopyTo@CSortedArray@@QEAAIPEA_KI@Z` | `0x31670` | 109 | UnwindData |  |
| 92 | `?CreateProjection@CEvalTree@@QEAAJAEAV1@PEAVCContextMetaData@@PEAVCProjectionFilter@@W4EProjectionType@@_N@Z` | `0x31770` | 174 | UnwindData |  |
| 94 | `?Empty@CSortedArray@@QEAAXXZ` | `0x31900` | 5,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `?Find@CSortedArray@@QEAAI_K@Z` | `0x33000` | 271 | UnwindData |  |
| 102 | `?GetAt@CSortedArray@@QEAA_KH@Z` | `0x33120` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `?Insert@CSortedArray@@QEAAX_K@Z` | `0x332B0` | 389 | UnwindData |  |
| 123 | `?IsInSet@CPropertyProjectionFilter@@UEAA_NPEAVCEvalNode@@@Z` | `0x34E30` | 280 | UnwindData |  |
| 128 | `?IsNoop@CEvalNode@@SA_NPEAV1@H@Z` | `0x34F60` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `?IsValid@CEvalTree@@QEAA_NXZ` | `0x34FF0` | 21 | UnwindData |  |
| 144 | `?PrintOffset@CEvalNode@@SAXPEAU_iobuf@@H@Z` | `0x35530` | 59 | UnwindData |  |
| 145 | `?Project@CEvalTree@@SAJPEAVCContextMetaData@@AEAVCImplicationList@@PEAVCEvalNode@@PEAVCProjectionFilter@@W4EProjectionType@@_NPEAPEAV4@@Z` | `0x35C80` | 86 | UnwindData |  |
| 148 | `?Rebase@CSortedArray@@QEAAX_K@Z` | `0x36090` | 115 | UnwindData |  |
| 150 | `?Remove@CSortedArray@@QEAA_N_K@Z` | `0x36140` | 49 | UnwindData |  |
| 154 | `?SetBool@CEvalTree@@QEAA_NH@Z` | `0x362A0` | 161 | UnwindData |  |
| 163 | `?UnbindPtr@CSortedArray@@QEAAPEA_KXZ` | `0x38AB0` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0CClassInformation@@QEAA@AEBU0@@Z` | `0x39080` | 102 | UnwindData |  |
| 3 | `??0CClassInformation@@QEAA@XZ` | `0x390F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??1CClassInfoArray@@QEAA@XZ` | `0x39160` | 51 | UnwindData |  |
| 23 | `??1CClassInformation@@QEAA@XZ` | `0x391A0` | 53 | UnwindData |  |
| 35 | `??4CClassInfoArray@@QEAA_NAEAV0@@Z` | `0x391E0` | 168 | UnwindData |  |
| 36 | `??4CClassInformation@@QEAAAEAU0@AEBU0@@Z` | `0x39290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??4CQueryAnalyser@@QEAAAEAV0@$$QEAV0@@Z` | `0x392B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `??4CQueryAnalyser@@QEAAAEAV0@AEBV0@@Z` | `0x392B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??4CTimeKeeper@@QEAAAEAV0@$$QEAV0@@Z` | `0x392C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??4CTimeKeeper@@QEAAAEAV0@AEBV0@@Z` | `0x39300` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `?AddClass@CClassInfoArray@@QEAA_NPEAUCClassInformation@@@Z` | `0x393C0` | 24 | UnwindData |  |
| 63 | `?AndDefiniteClassArrays@CQueryAnalyser@@KAJPEAVCClassInfoArray@@00@Z` | `0x393E0` | 37 | UnwindData |  |
| 64 | `?AndPossibleClassArrays@CQueryAnalyser@@KAJPEAVCClassInfoArray@@00@Z` | `0x39410` | 30 | UnwindData |  |
| 71 | `?Clear@CClassInfoArray@@QEAAXXZ` | `0x39490` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `?CompareRequestedToProvided@CQueryAnalyser@@SAHAEAVCClassInfoArray@@0@Z` | `0x39520` | 241 | UnwindData |  |
| 103 | `?GetClass@CClassInfoArray@@QEAAPEAUCClassInformation@@H@Z` | `0x39620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `?GetInstanceClasses@CQueryAnalyser@@KAJAEAUQL_LEVEL_1_TOKEN@@AEAVCClassInfoArray@@@Z` | `0x39640` | 521 | UnwindData |  |
| 112 | `?GetNecessaryQueryForProperty@CQueryAnalyser@@SAJPEAUQL_LEVEL_1_RPN_EXPRESSION@@AEAVCPropertyName@@AEAPEAU2@@Z` | `0x39850` | 1,069 | UnwindData |  |
| 115 | `?GetPossibleInstanceClasses@CQueryAnalyser@@SAJPEAUQL_LEVEL_1_RPN_EXPRESSION@@AEAPEAVCClassInfoArray@@@Z` | `0x39C90` | 2,461 | UnwindData |  |
| 116 | `?GetPropertiesThatMustDiffer@CQueryAnalyser@@KAJPEAUQL_LEVEL_1_RPN_EXPRESSION@@AEAUCClassInformation@@AEAVCWStringArray@@@Z` | `0x3A640` | 2,400 | UnwindData |  |
| 132 | `?IsTokenAboutProperty@CQueryAnalyser@@KAHAEAUQL_LEVEL_1_TOKEN@@AEAVCPropertyName@@@Z` | `0x3AFB0` | 181 | UnwindData |  |
| 136 | `?NegateDefiniteClassArray@CQueryAnalyser@@KAJPEAVCClassInfoArray@@0@Z` | `0x3B070` | 36 | UnwindData |  |
| 137 | `?NegatePossibleClassArray@CQueryAnalyser@@KAJPEAVCClassInfoArray@@0@Z` | `0x3B0A0` | 24 | UnwindData |  |
| 138 | `?NegateQueryExpression@CQueryAnalyser@@KAJPEAUQL_LEVEL_1_RPN_EXPRESSION@@0@Z` | `0x3B0C0` | 117 | UnwindData |  |
| 141 | `?OrDefiniteClassArrays@CQueryAnalyser@@KAJPEAVCClassInfoArray@@00@Z` | `0x3B140` | 681 | UnwindData |  |
| 142 | `?OrPossibleClassArrays@CQueryAnalyser@@KAJPEAVCClassInfoArray@@00@Z` | `0x3B3F0` | 681 | UnwindData |  |
| 151 | `?RemoveClass@CClassInfoArray@@QEAAXH@Z` | `0x3B6A0` | 90 | UnwindData |  |
| 158 | `?SetOne@CClassInfoArray@@QEAA_NPEBGH@Z` | `0x3B700` | 166 | UnwindData |  |
| 100 | `GetAccessMask` | `0x44550` | 388 | UnwindData |  |
| 133 | `IsUserAdministrator` | `0x44970` | 32 | UnwindData |  |
| 134 | `IsUserInGroup` | `0x449A0` | 413 | UnwindData |  |
| 167 | `DllGetClassObject` | `0x45C90` | 301 | UnwindData |  |
| 168 | `DllRegisterServer` | `0x45F90` | 412 | UnwindData |  |
| 169 | `DllUnregisterServer` | `0x46140` | 452 | UnwindData |  |
| 50 | `??_7CEvalNode@@6B@` | `0x4F398` | 312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `??_7CMetaData@@6B@` | `0x4F4D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `??_7CStandardMetaData@@6B@` | `0x4F500` | 11,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??_7CPropertyProjectionFilter@@6B@` | `0x523C8` | 0 | Indeterminate |  |
