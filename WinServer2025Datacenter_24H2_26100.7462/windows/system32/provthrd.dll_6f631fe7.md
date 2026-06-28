# Binary Specification: provthrd.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\provthrd.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6f631fe798c04f4022dba29faf005c65a2a9f32eaf1b9b283a4097feb76765a8`
* **Total Exported Functions:** 965

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 697 | `?GetRange@WmiOperatorEqualOrGreaterNode@@UEAAPEAVWmiRangeNode@@XZ` | `0x1010` | 634 | UnwindData |  |
| 696 | `?GetRange@WmiOperatorEqualNode@@UEAAPEAVWmiRangeNode@@XZ` | `0x1290` | 822 | UnwindData |  |
| 869 | `?Query@QueryPreprocessor@@QEAA?AW4QuadState@1@PEAGAEAPEAUSQL_LEVEL_1_RPN_EXPRESSION@@@Z` | `0x16D0` | 229 | UnwindData |  |
| 924 | `?SortRanges@QueryPreprocessor@@IEAAXKPEAKPEAPEAVWmiRangeNode@@@Z` | `0x3300` | 34 | UnwindData |  |
| 870 | `?QuickSort@QueryPreprocessor@@IEAAXPEAPEAVWmiRangeNode@@PEAKK@Z` | `0x3330` | 29 | UnwindData |  |
| 599 | `?CreateDisjunctionContainer@QueryPreprocessor@@IEAA?AW4WmiTriState@@PEAXPEAVWmiTreeNode@@KPEAPEAGAEAPEAVDisjunctions@@@Z` | `0x3420` | 511 | UnwindData |  |
| 923 | `?SortConditionals@QueryPreprocessor@@IEAA?AW4WmiTriState@@AEAPEAVWmiTreeNode@@@Z` | `0x3630` | 139 | UnwindData |  |
| 838 | `?PreProcess@QueryPreprocessor@@QEAA?AW4QuadState@1@PEAXPEAUSQL_LEVEL_1_RPN_EXPRESSION@@PEAVWmiTreeNode@@KPEAPEAGAEAPEAVPartitionSet@@@Z` | `0x36D0` | 1,518 | UnwindData |  |
| 883 | `?RecursiveSort@QueryPreprocessor@@IEAA?AW4WmiTriState@@AEAPEAVWmiTreeNode@@@Z` | `0x3CD0` | 256 | UnwindData |  |
| 229 | `??1Conjunctions@@QEAA@XZ` | `0x3DE0` | 95 | UnwindData |  |
| 886 | `?RemoveNonOverlappingRanges@QueryPreprocessor@@IEAA?AW4QuadState@1@AEAPEAVWmiTreeNode@@@Z` | `0x3E50` | 107 | UnwindData |  |
| 872 | `?RecursiveConvertToRanges@QueryPreprocessor@@IEAA?AW4WmiTriState@@AEAPEAVWmiTreeNode@@@Z` | `0x3ED0` | 462 | UnwindData |  |
| 602 | `?CreatePartitionSet@QueryPreprocessor@@IEAA?AW4WmiTriState@@PEAVDisjunctions@@AEAPEAVPartitionSet@@@Z` | `0x40B0` | 447 | UnwindData |  |
| 885 | `?RemoveInvariants@QueryPreprocessor@@IEAA?AW4QuadState@1@PEAXAEAPEAVWmiTreeNode@@@Z` | `0x4280` | 113 | UnwindData |  |
| 862 | `?PrintTree@QueryPreprocessor@@IEAAXPEAVWmiTreeNode@@@Z` | `0x4300` | 103 | UnwindData |  |
| 884 | `?RecursiveSortConditionals@QueryPreprocessor@@IEAA?AW4WmiTriState@@AEAPEAVWmiTreeNode@@0@Z` | `0x4370` | 473 | UnwindData |  |
| 230 | `??1Disjunctions@@QEAA@XZ` | `0x4550` | 189 | UnwindData |  |
| 779 | `?Initialize@Disjunctions@@QEAA?AW4WmiTriState@@XZ` | `0x4620` | 295 | UnwindData |  |
| 598 | `?CountDisjunctions@QueryPreprocessor@@IEAAXPEAVWmiTreeNode@@AEAK@Z` | `0x4750` | 85 | UnwindData |  |
| 600 | `?CreateDisjunctions@QueryPreprocessor@@IEAA?AW4WmiTriState@@PEAXPEAVWmiTreeNode@@PEAVDisjunctions@@KPEAPEAGAEAK@Z` | `0x47B0` | 846 | UnwindData |  |
| 879 | `?RecursivePartitionSet@QueryPreprocessor@@IEAA?AW4WmiTriState@@PEAVDisjunctions@@AEAPEAVPartitionSet@@KPEAKK@Z` | `0x4B10` | 1,784 | UnwindData |  |
| 880 | `?RecursiveQuickSort@QueryPreprocessor@@IEAAXPEAPEAVWmiRangeNode@@PEAKKK@Z` | `0x5210` | 471 | UnwindData |  |
| 887 | `?RemoveOverlaps@QueryPreprocessor@@IEAA?AW4WmiTriState@@PEAKK00PEAPEAVWmiRangeNode@@@Z` | `0x53F0` | 8 | UnwindData |  |
| 882 | `?RecursiveRemoveNonOverlappingRanges@QueryPreprocessor@@IEAA?AW4QuadState@1@AEAPEAVWmiTreeNode@@0@Z` | `0x5750` | 50 | UnwindData |  |
| 881 | `?RecursiveRemoveInvariants@QueryPreprocessor@@IEAA?AW4QuadState@1@PEAXAEAPEAVWmiTreeNode@@@Z` | `0x5B30` | 552 | UnwindData |  |
| 877 | `?RecursiveEvaluate@QueryPreprocessor@@IEAAHPEAXAEAUSQL_LEVEL_1_RPN_EXPRESSION@@PEAVWmiTreeNode@@PEAPEAV3@AEAH@Z` | `0x5F30` | 1,620 | UnwindData |  |
| 170 | `??0WmiAndNode@@QEAA@PEAVWmiTreeNode@@00@Z` | `0x6590` | 76 | UnwindData |  |
| 962 | `?WriteW@ProvDebugLog@@QEAAXPEBGZZ` | `0x65F0` | 241 | UnwindData |  |
| 876 | `?RecursiveDisjunctiveNormalForm@QueryPreprocessor@@IEAA?AW4QuadState@1@AEAPEAVWmiTreeNode@@@Z` | `0x66F0` | 438 | UnwindData |  |
| 203 | `??0WmiRangeNode@@QEAA@KPEAGKHHHHPEAVWmiTreeNode@@1@Z` | `0x68B0` | 183 | UnwindData |  |
| 596 | `?Copy@WmiUnsignedIntegerRangeNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x6970` | 252 | UnwindData |  |
| 783 | `?InsertNode@QueryPreprocessor@@IEAA?AW4WmiTriState@@AEAPEAVWmiTreeNode@@0@Z` | `0x6A80` | 234 | UnwindData |  |
| 878 | `?RecursiveInsertNode@QueryPreprocessor@@IEAA?AW4WmiTriState@@AEAPEAVWmiTreeNode@@0@Z` | `0x6B70` | 413 | UnwindData |  |
| 780 | `?Initialize@PartitionSet@@QEAA?AW4WmiTriState@@K@Z` | `0x6D20` | 108 | UnwindData |  |
| 213 | `??0WmiStringRangeNode@@QEAA@PEAGKHHHH00PEAVWmiTreeNode@@1@Z` | `0x6E20` | 319 | UnwindData |  |
| 591 | `?Copy@WmiStringNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x6F70` | 118 | UnwindData |  |
| 211 | `??0WmiStringNode@@QEAA@PEAG0W4WmiValueFunction@WmiValueNode@@1KPEAVWmiTreeNode@@@Z` | `0x6FF0` | 416 | UnwindData |  |
| 684 | `?GetOverlappingRange@WmiStringRangeNode@@QEAA?AW4WmiTriState@@AEAV1@AEAPEAV1@@Z` | `0x7290` | 2,889 | UnwindData |  |
| 215 | `??0WmiTreeNode@@QEAA@KPEAXPEAV0@11@Z` | `0x7DE0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `??1PartitionSet@@UEAA@XZ` | `0x7F20` | 132 | UnwindData |  |
| 225 | `??0WmiUnsignedIntegerRangeNode@@QEAA@PEAGKHHHHKKPEAVWmiTreeNode@@1@Z` | `0x8070` | 211 | UnwindData |  |
| 297 | `??1WmiStringRangeNode@@UEAA@XZ` | `0x8150` | 115 | UnwindData |  |
| 837 | `?PreProcess@QueryPreprocessor@@QEAA?AW4QuadState@1@PEAXPEAUSQL_LEVEL_1_RPN_EXPRESSION@@AEAPEAVWmiTreeNode@@@Z` | `0x81D0` | 321 | UnwindData |  |
| 679 | `?GetLogging@ProvDebugLog@@QEAAHXZ` | `0x8320` | 32 | UnwindData |  |
| 293 | `??1WmiRangeNode@@UEAA@XZ` | `0x83C0` | 62 | UnwindData |  |
| 592 | `?Copy@WmiStringRangeNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x84F0` | 374 | UnwindData |  |
| 778 | `?Initialize@Conjunctions@@QEAA?AW4WmiTriState@@XZ` | `0x8730` | 136 | UnwindData |  |
| 688 | `?GetPartition@PartitionSet@@QEAAPEAV1@K@Z` | `0x8820` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `?Copy@WmiAndNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x8870` | 300 | UnwindData |  |
| 651 | `?EvaluateAndExpression@QueryPreprocessor@@IEAA?AW4WmiTriState@@AEAPEAVWmiTreeNode@@@Z` | `0x89B0` | 87 | UnwindData |  |
| 167 | `??0QueryPreprocessor@@QEAA@AEBV0@@Z` | `0x8A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `??0QueryPreprocessor@@QEAA@XZ` | `0x8A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `?ComparePropertyName@WmiValueNode@@QEAAJAEAV1@@Z` | `0x8A30` | 60 | UnwindData |  |
| 277 | `??1WmiAndNode@@UEAA@XZ` | `0x8BC0` | 91 | UnwindData |  |
| 694 | `?GetRange@Conjunctions@@QEAAPEAVWmiRangeNode@@K@Z` | `0x8C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 945 | `?TransformOperatorToRange@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@@Z` | `0x8C50` | 121 | UnwindData |  |
| 222 | `??0WmiUnsignedIntegerNode@@QEAA@PEAGKKPEAVWmiTreeNode@@@Z` | `0x8CF0` | 174 | UnwindData |  |
| 903 | `?SetRange@Conjunctions@@QEAAXKPEAVWmiRangeNode@@@Z` | `0x8DB0` | 22 | UnwindData |  |
| 296 | `??1WmiStringNode@@UEAA@XZ` | `0x8F50` | 96 | UnwindData |  |
| 301 | `??1WmiUnsignedIntegerRangeNode@@UEAA@XZ` | `0x8FC0` | 62 | UnwindData |  |
| 227 | `??0WmiValueNode@@QEAA@KPEAGW4WmiValueFunction@0@1KPEAVWmiTreeNode@@@Z` | `0x90D0` | 154 | UnwindData |  |
| 956 | `?Write@ProvDebugLog@@QEAAXPEBGZZ` | `0x9170` | 233 | UnwindData |  |
| 193 | `??0WmiOperatorNode@@QEAA@KPEAVWmiTreeNode@@0@Z` | `0x92D0` | 73 | UnwindData |  |
| 276 | `??1QueryPreprocessor@@UEAA@XZ` | `0x9320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `??1WmiOperatorEqualOrGreaterNode@@UEAA@XZ` | `0x9340` | 78 | UnwindData |  |
| 288 | `??1WmiOperatorNode@@UEAA@XZ` | `0x93A0` | 27 | UnwindData |  |
| 579 | `?Copy@WmiOperatorEqualOrGreaterNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x93D0` | 149 | UnwindData |  |
| 181 | `??0WmiOperatorEqualOrGreaterNode@@QEAA@PEAVWmiTreeNode@@0@Z` | `0x9470` | 87 | UnwindData |  |
| 578 | `?Copy@WmiOperatorEqualNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x94D0` | 164 | UnwindData |  |
| 179 | `??0WmiOperatorEqualNode@@QEAA@PEAVWmiTreeNode@@0@Z` | `0x9580` | 87 | UnwindData |  |
| 595 | `?Copy@WmiUnsignedIntegerNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x95E0` | 221 | UnwindData |  |
| 665 | `?GetDisjunction@Disjunctions@@QEAAPEAVConjunctions@@K@Z` | `0x9710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 689 | `?GetPartitionCount@PartitionSet@@QEAAKXZ` | `0x9730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `?GetValue@ProvCounterType@@QEBAKXZ` | `0x9730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 762 | `?GetValue@ProvTimeTicksType@@QEBAKXZ` | `0x9730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `?GetValueLength@ProvOctetString@@QEBAKXZ` | `0x9730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `??1WmiValueNode@@UEAA@XZ` | `0x9740` | 64 | UnwindData |  |
| 283 | `??1WmiOperatorEqualOrLessNode@@UEAA@XZ` | `0x9790` | 76 | UnwindData |  |
| 690 | `?GetPropertyFunction@WmiValueNode@@QEAA?AW4WmiValueFunction@1@XZ` | `0x97F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 775 | `?InfiniteLowerBound@WmiRangeNode@@QEAAHXZ` | `0x97F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `??1WmiUnsignedIntegerNode@@UEAA@XZ` | `0x9800` | 64 | UnwindData |  |
| 901 | `?SetParent@WmiTreeNode@@QEAAPEAV1@PEAV1@@Z` | `0x9850` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 902 | `?SetPartition@PartitionSet@@QEAAXKPEAV1@@Z` | `0x9910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `?Evaluate@QueryPreprocessor@@IEAAHPEAXAEAUSQL_LEVEL_1_RPN_EXPRESSION@@PEAPEAVWmiTreeNode@@@Z` | `0x9930` | 111 | UnwindData |  |
| 897 | `?SetLeft@WmiTreeNode@@QEAAPEAV1@PEAV1@@Z` | `0x99B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 533 | `?ComparePropertyName@WmiRangeNode@@QEAAJAEAV1@@Z` | `0x9A20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0PartitionSet@@QEAA@XZ` | `0x9A50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 765 | `?GetValue@WmiStringNode@@QEAAPEAGXZ` | `0x9A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `??1WmiOperatorEqualNode@@UEAA@XZ` | `0x9A90` | 76 | UnwindData |  |
| 808 | `?LowerBound@WmiStringRangeNode@@QEAAPEAGXZ` | `0x9AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 953 | `?UpperBound@WmiStringRangeNode@@QEAAPEAGXZ` | `0x9B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 662 | `?GetConstantFunction@WmiValueNode@@QEAA?AW4WmiValueFunction@1@XZ` | `0x9B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `?InfiniteUpperBound@WmiRangeNode@@QEAAHXZ` | `0x9B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 663 | `?GetData@WmiTreeNode@@QEAAPEAXXZ` | `0x9B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 695 | `?GetRange@PartitionSet@@QEAAPEAVWmiRangeNode@@XZ` | `0x9B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `?GetValue@ProvOctetString@@QEBAPEAEXZ` | `0x9B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 905 | `?SetRight@WmiTreeNode@@QEAAPEAV1@PEAV1@@Z` | `0x9B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 529 | `?ClosedLowerBound@WmiRangeNode@@QEAAHXZ` | `0x9B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 581 | `?Copy@WmiOperatorGreaterNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x9B50` | 139 | UnwindData |  |
| 530 | `?ClosedUpperBound@WmiRangeNode@@QEAAHXZ` | `0x9BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | `?GetValue@WmiSignedIntegerNode@@QEAAJXZ` | `0x9BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `?GetValue@WmiUnsignedIntegerNode@@QEAAKXZ` | `0x9BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `??0WmiOperatorGreaterNode@@QEAA@PEAVWmiTreeNode@@0@Z` | `0x9C00` | 87 | UnwindData |  |
| 928 | `?TransformAndTrueEvaluation@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x9C60` | 108 | UnwindData |  |
| 946 | `?TransformOrFalseEvaluation@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x9C60` | 108 | UnwindData |  |
| 6 | `??0Conjunctions@@QEAA@K@Z` | `0x9CE0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `??1WmiOperatorGreaterNode@@UEAA@XZ` | `0x9EA0` | 76 | UnwindData |  |
| 691 | `?GetPropertyName@WmiRangeNode@@QEAAPEAGXZ` | `0x9F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 692 | `?GetPropertyName@WmiValueNode@@QEAAPEAGXZ` | `0x9F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `??0WmiSignedIntegerRangeNode@@QEAA@PEAGKHHHHJJPEAVWmiTreeNode@@1@Z` | `0x9F10` | 199 | UnwindData |  |
| 614 | `?DisjunctiveNormalForm@QueryPreprocessor@@IEAA?AW4QuadState@1@AEAPEAVWmiTreeNode@@@Z` | `0x9FE0` | 49 | UnwindData |  |
| 653 | `?EvaluateNotExpression@QueryPreprocessor@@IEAA?AW4WmiTriState@@AEAPEAVWmiTreeNode@@@Z` | `0xA080` | 224 | UnwindData |  |
| 922 | `?Sort@QueryPreprocessor@@IEAA?AW4WmiTriState@@AEAPEAVWmiTreeNode@@@Z` | `0xA180` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `??1WmiTreeNode@@UEAA@XZ` | `0xA1D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 666 | `?GetDisjunctionCount@Disjunctions@@QEAAKXZ` | `0xA250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 661 | `?GetConjunctionCount@Disjunctions@@QEAAKXZ` | `0xA260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 706 | `?GetRangeCount@Conjunctions@@QEAAKXZ` | `0xA260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 686 | `?GetParent@WmiTreeNode@@QEAAPEAV1@XZ` | `0xA270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0Disjunctions@@QEAA@KK@Z` | `0xA280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 708 | `?GetRight@WmiTreeNode@@QEAAXAEAPEAPEAV1@@Z` | `0xA2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 677 | `?GetLeft@WmiTreeNode@@QEAAXAEAPEAPEAV1@@Z` | `0xA2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `??1WmiSignedIntegerRangeNode@@UEAA@XZ` | `0xA2C0` | 18 | UnwindData |  |
| 896 | `?SetKeyIndex@PartitionSet@@QEAAXK@Z` | `0xA2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 900 | `?SetNull@ProvInstanceType@@QEAAXH@Z` | `0xA2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `?SetType@WmiTreeNode@@QEAAXK@Z` | `0xA2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | `?SetValue@ProvCounter@@QEAAXK@Z` | `0xA2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | `?SetValue@ProvGauge@@QEAAXK@Z` | `0xA2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 915 | `?SetValue@ProvInteger@@QEAAXJ@Z` | `0xA2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `?SetValue@ProvTimeTicks@@QEAAXK@Z` | `0xA2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 921 | `?SetValue@ProvUInteger32@@QEAAXK@Z` | `0xA2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 523 | `?AllocInfiniteRangeNode@QueryPreprocessor@@MEAAPEAVWmiRangeNode@@PEAXPEAG@Z` | `0xA2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | `?Analyse@ProvAnalyser@@MEAAHPEAVProvLexicon@@AEAKGPEBG1HHH@Z` | `0xA2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `?EvaluateOrExpression@QueryPreprocessor@@IEAA?AW4WmiTriState@@AEAPEAVWmiTreeNode@@@Z` | `0xA2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `?GetRange@WmiOperatorNotEqualNode@@UEAAPEAVWmiRangeNode@@XZ` | `0xA2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `?IsProvV1Type@ProvCounter64Type@@UEBAHXZ` | `0xA2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `?IsProvV2CType@ProvNullType@@UEBAHXZ` | `0xA2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 675 | `?GetKeyIndex@PartitionSet@@QEAAKXZ` | `0xA300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `?GetLowValue@ProvCounter64@@QEBAKXZ` | `0xA300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `?GetLowerBound@ProvNegativeRangeType@@QEAAJXZ` | `0xA300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 682 | `?GetLowerBound@ProvPositiveRangeType@@QEAAKXZ` | `0xA300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `?GetType@WmiTreeNode@@QEAAKXZ` | `0xA300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `?GetValue@ProvCounter@@QEBAKXZ` | `0xA300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 746 | `?GetValue@ProvGauge@@QEBAKXZ` | `0xA300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 748 | `?GetValue@ProvInteger@@QEBAJXZ` | `0xA300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `?GetValue@ProvTimeTicks@@QEBAKXZ` | `0xA300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `?GetValue@ProvUInteger32@@QEBAKXZ` | `0xA300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | `?IsNull@ProvInstanceType@@UEBAHXZ` | `0xA300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `?IsValid@ProvPositiveRangedType@@QEAAHXZ` | `0xA300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 669 | `?GetIndex@WmiRangeNode@@QEAAKXZ` | `0xA310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 670 | `?GetIndex@WmiValueNode@@QEAAKXZ` | `0xA310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `?GetRight@WmiTreeNode@@QEAAPEAV1@XZ` | `0xA320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `?SetRange@PartitionSet@@QEAAXPEAVWmiRangeNode@@@Z` | `0xA330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 676 | `?GetLeft@WmiTreeNode@@QEAAPEAV1@XZ` | `0xA340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `?Copy@WmiSignedIntegerRangeNode@@UEAAPEAVWmiTreeNode@@XZ` | `0xA350` | 107 | UnwindData |  |
| 34 | `??0ProvDebugLog@@QEAA@D@Z` | `0xAF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `??0ProvEventObject@@QEAA@AEBV0@@Z` | `0xAF60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `??4ProvDebugLog@@QEAAAEAV0@$$QEAV0@@Z` | `0xAF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `??4ProvDebugLog@@QEAAAEAV0@AEBV0@@Z` | `0xAF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `??4ProvEventObject@@QEAAAEAV0@AEBV0@@Z` | `0xAF90` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `??4WmiTreeNodeIterator@@QEAAAEAV0@AEBV0@@Z` | `0xAF90` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `??_FProvEventObject@@QEAAXXZ` | `0xB020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 531 | `?Closedown@ProvDebugLog@@SAXXZ` | `0xB030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 678 | `?GetLevel@ProvDebugLog@@QEAAKXZ` | `0xB040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 693 | `?GetProvDebugLog@ProvDebugLog@@SAPEAV1@D@Z` | `0xB050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 925 | `?Startup@ProvDebugLog@@SAHXZ` | `0xB070` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `?WriteA@ProvDebugLog@@QEAAXPEBDZZ` | `0xB1D0` | 152 | UnwindData |  |
| 958 | `?WriteFileAndLine@ProvDebugLog@@QEAAXPEBDKPEBGZZ` | `0xB270` | 212 | UnwindData |  |
| 959 | `?WriteFileAndLine@ProvDebugLog@@QEAAXPEBGK0ZZ` | `0xB350` | 212 | UnwindData |  |
| 960 | `?WriteFileAndLineA@ProvDebugLog@@QEAAXPEBDK0ZZ` | `0xB430` | 208 | UnwindData |  |
| 961 | `?WriteFileAndLineW@ProvDebugLog@@QEAAXPEBGK0ZZ` | `0xB510` | 212 | UnwindData |  |
| 45 | `??0ProvEventObject@@QEAA@PEBG@Z` | `0xB5F0` | 87 | UnwindData |  |
| 535 | `?Complete@ProvEventObject@@UEAAXXZ` | `0xB650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 777 | `?Initialise@ProvAnalyser@@MEAAXXZ` | `0xB650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 859 | `?Print@WmiTreeNode@@UEAAXXZ` | `0xB650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `?Process@ProvEventObject@@UEAAXXZ` | `0xB650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | `?TransformNonIntersectingRange@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0xB650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `??1ProvEventObject@@UEAA@XZ` | `0xB660` | 42 | UnwindData |  |
| 528 | `?Clear@ProvEventObject@@QEAAXXZ` | `0xB690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 667 | `?GetHandle@ProvEventObject@@QEAAPEAXXZ` | `0xB6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `?GetIterator@WmiTreeNodeIterator@@QEAAPEAVWmiTreeNode@@XZ` | `0xB6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 893 | `?Set@ProvEventObject@@QEAAXXZ` | `0xB6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `?Wait@ProvEventObject@@UEAAHXZ` | `0xB6E0` | 38 | UnwindData |  |
| 1 | `??$CompareElements@PEAGPEAG@@YAHPEBQEAG0@Z` | `0xB710` | 37 | UnwindData |  |
| 2 | `??$HashKey@PEAG@@YAIPEAG@Z` | `0xB740` | 164 | UnwindData |  |
| 3 | `??0CBString@@QEAA@H@Z` | `0xB7F0` | 40 | UnwindData |  |
| 4 | `??0CBString@@QEAA@PEBG@Z` | `0xB820` | 41 | UnwindData |  |
| 5 | `??0CBString@@QEAA@XZ` | `0xB850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0ProvAnalyser@@QEAA@AEBV0@@Z` | `0xB860` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0ProvAnalyser@@QEAA@PEBG@Z` | `0xB890` | 143 | UnwindData |  |
| 12 | `??0ProvBitStringType@@QEAA@AEBV0@@Z` | `0xB930` | 390 | UnwindData |  |
| 13 | `??0ProvBitStringType@@QEAA@PEBG@Z` | `0xBAC0` | 212 | UnwindData |  |
| 14 | `??0ProvBitStringType@@QEAA@PEBGAEBVProvOctetString@@@Z` | `0xBBA0` | 365 | UnwindData |  |
| 15 | `??0ProvBitStringType@@QEAA@PEBGPEAPEBGAEBK@Z` | `0xBD20` | 761 | UnwindData |  |
| 17 | `??0ProvCounter64@@QEAA@KK@Z` | `0xC020` | 37 | UnwindData |  |
| 18 | `??0ProvCounter64Type@@QEAA@AEBV0@@Z` | `0xC050` | 54 | UnwindData |  |
| 19 | `??0ProvCounter64Type@@QEAA@AEBVProvCounter64@@@Z` | `0xC090` | 53 | UnwindData |  |
| 20 | `??0ProvCounter64Type@@QEAA@KK@Z` | `0xC0D0` | 48 | UnwindData |  |
| 21 | `??0ProvCounter64Type@@QEAA@PEBG@Z` | `0xC110` | 64 | UnwindData |  |
| 22 | `??0ProvCounter64Type@@QEAA@XZ` | `0xC160` | 49 | UnwindData |  |
| 24 | `??0ProvCounter@@QEAA@K@Z` | `0xC1A0` | 33 | UnwindData |  |
| 25 | `??0ProvCounterType@@QEAA@AEBV0@@Z` | `0xC1D0` | 78 | UnwindData |  |
| 26 | `??0ProvCounterType@@QEAA@AEBVProvCounter@@@Z` | `0xC230` | 77 | UnwindData |  |
| 27 | `??0ProvCounterType@@QEAA@K@Z` | `0xC290` | 73 | UnwindData |  |
| 28 | `??0ProvCounterType@@QEAA@PEBG@Z` | `0xC2E0` | 94 | UnwindData |  |
| 29 | `??0ProvCounterType@@QEAA@XZ` | `0xC350` | 74 | UnwindData |  |
| 30 | `??0ProvDateTimeType@@QEAA@AEBV0@@Z` | `0xC3A0` | 80 | UnwindData |  |
| 31 | `??0ProvDateTimeType@@QEAA@AEBVProvOctetString@@@Z` | `0xC400` | 112 | UnwindData |  |
| 32 | `??0ProvDateTimeType@@QEAA@PEBG@Z` | `0xC480` | 113 | UnwindData |  |
| 33 | `??0ProvDateTimeType@@QEAA@XZ` | `0xC500` | 82 | UnwindData |  |
| 35 | `??0ProvDisplayStringType@@QEAA@AEBV0@@Z` | `0xC560` | 50 | UnwindData |  |
| 36 | `??0ProvDisplayStringType@@QEAA@AEBVProvOctetString@@PEBG@Z` | `0xC5A0` | 50 | UnwindData |  |
| 37 | `??0ProvDisplayStringType@@QEAA@PEBG0@Z` | `0xC5E0` | 146 | UnwindData |  |
| 38 | `??0ProvDisplayStringType@@QEAA@PEBG@Z` | `0xC680` | 65 | UnwindData |  |
| 39 | `??0ProvEnumeratedType@@QEAA@AEBV0@@Z` | `0xC6D0` | 390 | UnwindData |  |
| 40 | `??0ProvEnumeratedType@@QEAA@PEBG0@Z` | `0xC860` | 448 | UnwindData |  |
| 41 | `??0ProvEnumeratedType@@QEAA@PEBG@Z` | `0xCA30` | 212 | UnwindData |  |
| 42 | `??0ProvEnumeratedType@@QEAA@PEBGAEBJ@Z` | `0xCB10` | 262 | UnwindData |  |
| 43 | `??0ProvEnumeratedType@@QEAA@PEBGAEBVProvInteger@@@Z` | `0xCC20` | 264 | UnwindData |  |
| 46 | `??0ProvFixedLengthDisplayStringType@@QEAA@AEBK@Z` | `0xCD30` | 64 | UnwindData |  |
| 47 | `??0ProvFixedLengthDisplayStringType@@QEAA@AEBKAEBVProvOctetString@@@Z` | `0xCD80` | 64 | UnwindData |  |
| 48 | `??0ProvFixedLengthDisplayStringType@@QEAA@AEBKPEBG@Z` | `0xCDD0` | 139 | UnwindData |  |
| 49 | `??0ProvFixedLengthDisplayStringType@@QEAA@AEBV0@@Z` | `0xCE70` | 64 | UnwindData |  |
| 50 | `??0ProvFixedLengthOctetStringType@@QEAA@AEBK@Z` | `0xCEC0` | 114 | UnwindData |  |
| 51 | `??0ProvFixedLengthOctetStringType@@QEAA@AEBKAEBVProvOctetString@@@Z` | `0xCF40` | 126 | UnwindData |  |
| 52 | `??0ProvFixedLengthOctetStringType@@QEAA@AEBKPEBE@Z` | `0xCFD0` | 129 | UnwindData |  |
| 53 | `??0ProvFixedLengthOctetStringType@@QEAA@AEBKPEBG@Z` | `0xD060` | 152 | UnwindData |  |
| 54 | `??0ProvFixedLengthOctetStringType@@QEAA@AEBV0@@Z` | `0xD100` | 121 | UnwindData |  |
| 55 | `??0ProvFixedLengthOpaqueType@@QEAA@AEBK@Z` | `0xD180` | 114 | UnwindData |  |
| 56 | `??0ProvFixedLengthOpaqueType@@QEAA@AEBKAEBVProvOpaque@@@Z` | `0xD200` | 130 | UnwindData |  |
| 57 | `??0ProvFixedLengthOpaqueType@@QEAA@AEBKPEBEK@Z` | `0xD290` | 136 | UnwindData |  |
| 58 | `??0ProvFixedLengthOpaqueType@@QEAA@AEBKPEBG@Z` | `0xD320` | 156 | UnwindData |  |
| 59 | `??0ProvFixedLengthOpaqueType@@QEAA@AEBV0@@Z` | `0xD3D0` | 125 | UnwindData |  |
| 60 | `??0ProvFixedLengthPhysAddressType@@QEAA@AEBK@Z` | `0xD460` | 71 | UnwindData |  |
| 61 | `??0ProvFixedLengthPhysAddressType@@QEAA@AEBKAEBVProvOctetString@@@Z` | `0xD4B0` | 64 | UnwindData |  |
| 62 | `??0ProvFixedLengthPhysAddressType@@QEAA@AEBKPEBG@Z` | `0xD500` | 95 | UnwindData |  |
| 63 | `??0ProvFixedLengthPhysAddressType@@QEAA@AEBV0@@Z` | `0xD570` | 64 | UnwindData |  |
| 64 | `??0ProvFixedType@@QEAA@AEBV0@@Z` | `0xD5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `??0ProvFixedType@@QEAA@K@Z` | `0xD5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `??0ProvGauge@@QEAA@J@Z` | `0xD600` | 33 | UnwindData |  |
| 68 | `??0ProvGaugeType@@QEAA@AEBV0@@Z` | `0xD630` | 144 | UnwindData |  |
| 69 | `??0ProvGaugeType@@QEAA@AEBVProvGauge@@PEBG@Z` | `0xD6D0` | 177 | UnwindData |  |
| 70 | `??0ProvGaugeType@@QEAA@KPEBG@Z` | `0xD790` | 157 | UnwindData |  |
| 71 | `??0ProvGaugeType@@QEAA@PEBG0@Z` | `0xD840` | 197 | UnwindData |  |
| 72 | `??0ProvGaugeType@@QEAA@PEBG@Z` | `0xD910` | 127 | UnwindData |  |
| 73 | `??0ProvInstanceType@@IEAA@AEBV0@@Z` | `0xD9A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??0ProvInstanceType@@IEAA@HH@Z` | `0xD9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `??0ProvInteger@@QEAA@J@Z` | `0xD9F0` | 33 | UnwindData |  |
| 77 | `??0ProvIntegerType@@QEAA@AEBV0@@Z` | `0xDA20` | 144 | UnwindData |  |
| 78 | `??0ProvIntegerType@@QEAA@AEBVProvInteger@@PEBG@Z` | `0xDAC0` | 145 | UnwindData |  |
| 79 | `??0ProvIntegerType@@QEAA@JPEBG@Z` | `0xDB60` | 157 | UnwindData |  |
| 80 | `??0ProvIntegerType@@QEAA@PEBG0@Z` | `0xDC10` | 197 | UnwindData |  |
| 81 | `??0ProvIntegerType@@QEAA@PEBG@Z` | `0xDCE0` | 127 | UnwindData |  |
| 83 | `??0ProvIpAddress@@QEAA@K@Z` | `0xDD70` | 40 | UnwindData |  |
| 85 | `??0ProvIpAddressType@@QEAA@AEBV0@@Z` | `0xDDA0` | 69 | UnwindData |  |
| 86 | `??0ProvIpAddressType@@QEAA@AEBVProvIpAddress@@@Z` | `0xDDF0` | 64 | UnwindData |  |
| 87 | `??0ProvIpAddressType@@QEAA@K@Z` | `0xDE40` | 80 | UnwindData |  |
| 88 | `??0ProvIpAddressType@@QEAA@PEBG@Z` | `0xDEA0` | 98 | UnwindData |  |
| 89 | `??0ProvIpAddressType@@QEAA@XZ` | `0xDF10` | 81 | UnwindData |  |
| 90 | `??0ProvLexicon@@QEAA@XZ` | `0xDF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `??0ProvMacAddressType@@QEAA@AEBV0@@Z` | `0xDF90` | 64 | UnwindData |  |
| 92 | `??0ProvMacAddressType@@QEAA@AEBVProvOctetString@@@Z` | `0xDFE0` | 80 | UnwindData |  |
| 93 | `??0ProvMacAddressType@@QEAA@PEBE@Z` | `0xE040` | 80 | UnwindData |  |
| 94 | `??0ProvMacAddressType@@QEAA@PEBG@Z` | `0xE0A0` | 107 | UnwindData |  |
| 95 | `??0ProvMacAddressType@@QEAA@XZ` | `0xE120` | 77 | UnwindData |  |
| 96 | `??0ProvNegativeRangeType@@QEAA@AEBV0@@Z` | `0xE180` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `??0ProvNegativeRangeType@@QEAA@JJ@Z` | `0xE1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `??0ProvNegativeRangeType@@QEAA@XZ` | `0xE1D0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `??0ProvNetworkAddressType@@QEAA@AEBV0@@Z` | `0xE3A0` | 69 | UnwindData |  |
| 100 | `??0ProvNetworkAddressType@@QEAA@AEBVProvIpAddress@@@Z` | `0xE3F0` | 64 | UnwindData |  |
| 101 | `??0ProvNetworkAddressType@@QEAA@K@Z` | `0xE440` | 80 | UnwindData |  |
| 102 | `??0ProvNetworkAddressType@@QEAA@PEBG@Z` | `0xE4A0` | 98 | UnwindData |  |
| 103 | `??0ProvNetworkAddressType@@QEAA@XZ` | `0xE510` | 81 | UnwindData |  |
| 104 | `??0ProvNull@@QEAA@XZ` | `0xE570` | 30 | UnwindData |  |
| 105 | `??0ProvNullType@@QEAA@AEBV0@@Z` | `0xE5A0` | 70 | UnwindData |  |
| 106 | `??0ProvNullType@@QEAA@AEBVProvNull@@@Z` | `0xE5A0` | 70 | UnwindData |  |
| 107 | `??0ProvNullType@@QEAA@XZ` | `0xE5F0` | 70 | UnwindData |  |
| 108 | `??0ProvOSIAddressType@@QEAA@AEBV0@@Z` | `0xE640` | 50 | UnwindData |  |
| 109 | `??0ProvOSIAddressType@@QEAA@AEBVProvOctetString@@@Z` | `0xE680` | 88 | UnwindData |  |
| 110 | `??0ProvOSIAddressType@@QEAA@PEBEK@Z` | `0xE6E0` | 95 | UnwindData |  |
| 111 | `??0ProvOSIAddressType@@QEAA@PEBG@Z` | `0xE750` | 89 | UnwindData |  |
| 112 | `??0ProvOSIAddressType@@QEAA@XZ` | `0xE7B0` | 52 | UnwindData |  |
| 116 | `??0ProvObjectIdentifierType@@QEAA@AEBV0@@Z` | `0xE7F0` | 69 | UnwindData |  |
| 117 | `??0ProvObjectIdentifierType@@QEAA@AEBVProvObjectIdentifier@@@Z` | `0xE840` | 64 | UnwindData |  |
| 118 | `??0ProvObjectIdentifierType@@QEAA@PEBG@Z` | `0xE890` | 93 | UnwindData |  |
| 119 | `??0ProvObjectIdentifierType@@QEAA@PEBKK@Z` | `0xE900` | 64 | UnwindData |  |
| 120 | `??0ProvObjectIdentifierType@@QEAA@XZ` | `0xE950` | 69 | UnwindData |  |
| 123 | `??0ProvOctetStringType@@QEAA@AEBV0@@Z` | `0xE9A0` | 123 | UnwindData |  |
| 124 | `??0ProvOctetStringType@@QEAA@AEBVProvOctetString@@PEBG@Z` | `0xEA30` | 155 | UnwindData |  |
| 125 | `??0ProvOctetStringType@@QEAA@PEBEKPEBG@Z` | `0xEAE0` | 172 | UnwindData |  |
| 126 | `??0ProvOctetStringType@@QEAA@PEBG0@Z` | `0xEBA0` | 180 | UnwindData |  |
| 127 | `??0ProvOctetStringType@@QEAA@PEBG@Z` | `0xEC60` | 109 | UnwindData |  |
| 128 | `??0ProvOpaque@@QEAA@AEBV0@@Z` | `0xECE0` | 117 | UnwindData |  |
| 129 | `??0ProvOpaque@@QEAA@PEBEK@Z` | `0xED60` | 108 | UnwindData |  |
| 130 | `??0ProvOpaqueType@@QEAA@AEBV0@@Z` | `0xEDE0` | 123 | UnwindData |  |
| 131 | `??0ProvOpaqueType@@QEAA@AEBVProvOpaque@@PEBG@Z` | `0xEE70` | 159 | UnwindData |  |
| 132 | `??0ProvOpaqueType@@QEAA@PEBEKPEBG@Z` | `0xEF20` | 176 | UnwindData |  |
| 133 | `??0ProvOpaqueType@@QEAA@PEBG0@Z` | `0xEFE0` | 184 | UnwindData |  |
| 134 | `??0ProvOpaqueType@@QEAA@PEBG@Z` | `0xF0A0` | 109 | UnwindData |  |
| 135 | `??0ProvPhysAddressType@@QEAA@AEBV0@@Z` | `0xF120` | 50 | UnwindData |  |
| 136 | `??0ProvPhysAddressType@@QEAA@AEBVProvOctetString@@PEBG@Z` | `0xF160` | 50 | UnwindData |  |
| 137 | `??0ProvPhysAddressType@@QEAA@PEBEKPEBG@Z` | `0xF1A0` | 50 | UnwindData |  |
| 138 | `??0ProvPhysAddressType@@QEAA@PEBG0@Z` | `0xF1E0` | 89 | UnwindData |  |
| 139 | `??0ProvPhysAddressType@@QEAA@PEBG@Z` | `0xF240` | 65 | UnwindData |  |
| 140 | `??0ProvPositiveRangeType@@QEAA@AEBV0@@Z` | `0xF290` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `??0ProvPositiveRangeType@@QEAA@KJ@Z` | `0xF2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `??0ProvPositiveRangeType@@QEAA@XZ` | `0xF2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `??0ProvPositiveRangedType@@QEAA@AEBV0@@Z` | `0xF300` | 221 | UnwindData |  |
| 144 | `??0ProvPositiveRangedType@@QEAA@PEBG@Z` | `0xF3F0` | 153 | UnwindData |  |
| 145 | `??0ProvRowStatusType@@QEAA@AEBJ@Z` | `0xF490` | 60 | UnwindData |  |
| 146 | `??0ProvRowStatusType@@QEAA@AEBV0@@Z` | `0xF4E0` | 50 | UnwindData |  |
| 147 | `??0ProvRowStatusType@@QEAA@AEBVProvInteger@@@Z` | `0xF520` | 60 | UnwindData |  |
| 148 | `??0ProvRowStatusType@@QEAA@AEBW4ProvRowStatusEnum@0@@Z` | `0xF570` | 68 | UnwindData |  |
| 149 | `??0ProvRowStatusType@@QEAA@PEBG@Z` | `0xF5C0` | 60 | UnwindData |  |
| 150 | `??0ProvRowStatusType@@QEAA@XZ` | `0xF610` | 57 | UnwindData |  |
| 152 | `??0ProvTimeTicks@@QEAA@K@Z` | `0xF650` | 33 | UnwindData |  |
| 153 | `??0ProvTimeTicksType@@QEAA@AEBV0@@Z` | `0xF680` | 78 | UnwindData |  |
| 154 | `??0ProvTimeTicksType@@QEAA@AEBVProvTimeTicks@@@Z` | `0xF6E0` | 77 | UnwindData |  |
| 155 | `??0ProvTimeTicksType@@QEAA@K@Z` | `0xF740` | 73 | UnwindData |  |
| 156 | `??0ProvTimeTicksType@@QEAA@PEBG@Z` | `0xF790` | 94 | UnwindData |  |
| 157 | `??0ProvTimeTicksType@@QEAA@XZ` | `0xF800` | 74 | UnwindData |  |
| 158 | `??0ProvUDPAddressType@@QEAA@AEBV0@@Z` | `0xF850` | 64 | UnwindData |  |
| 159 | `??0ProvUDPAddressType@@QEAA@AEBVProvOctetString@@@Z` | `0xF8A0` | 80 | UnwindData |  |
| 160 | `??0ProvUDPAddressType@@QEAA@PEBE@Z` | `0xF900` | 80 | UnwindData |  |
| 161 | `??0ProvUDPAddressType@@QEAA@PEBG@Z` | `0xF960` | 107 | UnwindData |  |
| 162 | `??0ProvUDPAddressType@@QEAA@XZ` | `0xF9E0` | 77 | UnwindData |  |
| 164 | `??0ProvUInteger32@@QEAA@J@Z` | `0xFA40` | 33 | UnwindData |  |
| 165 | `??0ProvValue@@AEAA@AEBV0@@Z` | `0xFA70` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `??0ProvValue@@IEAA@XZ` | `0xFA70` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `??1CBString@@QEAA@XZ` | `0xFC50` | 40 | UnwindData |  |
| 232 | `??1ProvAnalyser@@UEAA@XZ` | `0xFCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `??1ProvBitStringType@@UEAA@XZ` | `0xFCC0` | 322 | UnwindData |  |
| 234 | `??1ProvCounter64@@UEAA@XZ` | `0xFE10` | 27 | UnwindData |  |
| 235 | `??1ProvCounter64Type@@UEAA@XZ` | `0xFE40` | 27 | UnwindData |  |
| 236 | `??1ProvCounter@@UEAA@XZ` | `0xFE70` | 27 | UnwindData |  |
| 237 | `??1ProvCounterType@@UEAA@XZ` | `0xFEA0` | 56 | UnwindData |  |
| 238 | `??1ProvDateTimeType@@UEAA@XZ` | `0xFEE0` | 74 | UnwindData |  |
| 239 | `??1ProvDisplayStringType@@UEAA@XZ` | `0xFF30` | 39 | UnwindData |  |
| 240 | `??1ProvEnumeratedType@@UEAA@XZ` | `0xFF60` | 322 | UnwindData |  |
| 242 | `??1ProvFixedLengthDisplayStringType@@UEAA@XZ` | `0x100B0` | 53 | UnwindData |  |
| 243 | `??1ProvFixedLengthOctetStringType@@UEAA@XZ` | `0x100F0` | 67 | UnwindData |  |
| 244 | `??1ProvFixedLengthOpaqueType@@UEAA@XZ` | `0x10140` | 67 | UnwindData |  |
| 245 | `??1ProvFixedLengthPhysAddressType@@UEAA@XZ` | `0x10190` | 53 | UnwindData |  |
| 246 | `??1ProvFixedType@@UEAA@XZ` | `0x101D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `??1ProvGauge@@UEAA@XZ` | `0x101F0` | 27 | UnwindData |  |
| 248 | `??1ProvGaugeType@@UEAA@XZ` | `0x10220` | 92 | UnwindData |  |
| 249 | `??1ProvInstanceType@@UEAA@XZ` | `0x10290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `??1ProvInteger@@UEAA@XZ` | `0x102B0` | 27 | UnwindData |  |
| 251 | `??1ProvIntegerType@@UEAA@XZ` | `0x102E0` | 92 | UnwindData |  |
| 252 | `??1ProvIpAddress@@UEAA@XZ` | `0x10350` | 27 | UnwindData |  |
| 253 | `??1ProvIpAddressType@@UEAA@XZ` | `0x10380` | 56 | UnwindData |  |
| 254 | `??1ProvLexicon@@QEAA@XZ` | `0x103C0` | 25 | UnwindData |  |
| 255 | `??1ProvMacAddressType@@UEAA@XZ` | `0x103E0` | 53 | UnwindData |  |
| 256 | `??1ProvNegativeRangeType@@UEAA@XZ` | `0x10420` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `??1ProvNetworkAddressType@@UEAA@XZ` | `0x104E0` | 56 | UnwindData |  |
| 258 | `??1ProvNull@@UEAA@XZ` | `0x10520` | 27 | UnwindData |  |
| 259 | `??1ProvNullType@@UEAA@XZ` | `0x10550` | 56 | UnwindData |  |
| 260 | `??1ProvOSIAddressType@@UEAA@XZ` | `0x10590` | 39 | UnwindData |  |
| 262 | `??1ProvObjectIdentifierType@@UEAA@XZ` | `0x105C0` | 50 | UnwindData |  |
| 264 | `??1ProvOctetStringType@@UEAA@XZ` | `0x10600` | 84 | UnwindData |  |
| 265 | `??1ProvOpaque@@UEAA@XZ` | `0x10660` | 67 | UnwindData |  |
| 266 | `??1ProvOpaqueType@@UEAA@XZ` | `0x106B0` | 84 | UnwindData |  |
| 267 | `??1ProvPhysAddressType@@UEAA@XZ` | `0x10710` | 39 | UnwindData |  |
| 268 | `??1ProvPositiveRangeType@@UEAA@XZ` | `0x10740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `??1ProvPositiveRangedType@@UEAA@XZ` | `0x10760` | 154 | UnwindData |  |
| 270 | `??1ProvRowStatusType@@UEAA@XZ` | `0x10800` | 39 | UnwindData |  |
| 271 | `??1ProvTimeTicks@@UEAA@XZ` | `0x10830` | 27 | UnwindData |  |
| 272 | `??1ProvTimeTicksType@@UEAA@XZ` | `0x10860` | 56 | UnwindData |  |
| 273 | `??1ProvUDPAddressType@@UEAA@XZ` | `0x108A0` | 53 | UnwindData |  |
| 274 | `??1ProvUInteger32@@UEAA@XZ` | `0x108E0` | 27 | UnwindData |  |
| 275 | `??1ProvValue@@UEAA@XZ` | `0x10910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `??4CBString@@QEAAAEAV0@AEBV0@@Z` | `0x10930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `??4CBString@@QEAAAEBV0@PEBG@Z` | `0x10950` | 69 | UnwindData |  |
| 308 | `??4ProvAnalyser@@QEAAAEAV0@AEBV0@@Z` | `0x109A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `??4ProvBitStringType@@QEAAAEAV0@AEBV0@@Z` | `0x109C0` | 216 | UnwindData |  |
| 310 | `??4ProvCounter64@@QEAAAEAVProvValue@@AEBV0@@Z` | `0x10AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `??4ProvCounter64Type@@QEAAAEAV0@AEBV0@@Z` | `0x10AC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `??4ProvCounter@@QEAAAEAVProvValue@@AEBV0@@Z` | `0x10AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `??4ProvFixedType@@QEAAAEAV0@AEBV0@@Z` | `0x10AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `??4ProvGauge@@QEAAAEAVProvValue@@AEBV0@@Z` | `0x10AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `??4ProvInteger@@QEAAAEAVProvValue@@AEBV0@@Z` | `0x10AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `??4ProvTimeTicks@@QEAAAEAVProvValue@@AEBV0@@Z` | `0x10AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `??4ProvUInteger32@@QEAAAEAVProvValue@@AEBV0@@Z` | `0x10AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `??4ProvCounterType@@QEAAAEAV0@AEBV0@@Z` | `0x10B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `??4ProvTimeTicksType@@QEAAAEAV0@AEBV0@@Z` | `0x10B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `??4ProvDateTimeType@@QEAAAEAV0@AEBV0@@Z` | `0x10B30` | 100 | UnwindData |  |
| 317 | `??4ProvDisplayStringType@@QEAAAEAV0@AEBV0@@Z` | `0x10BA0` | 24 | UnwindData |  |
| 338 | `??4ProvOSIAddressType@@QEAAAEAV0@AEBV0@@Z` | `0x10BA0` | 24 | UnwindData |  |
| 345 | `??4ProvPhysAddressType@@QEAAAEAV0@AEBV0@@Z` | `0x10BA0` | 24 | UnwindData |  |
| 318 | `??4ProvEnumeratedType@@QEAAAEAV0@AEBV0@@Z` | `0x10BC0` | 216 | UnwindData |  |
| 320 | `??4ProvFixedLengthDisplayStringType@@QEAAAEAV0@AEBV0@@Z` | `0x10CA0` | 24 | UnwindData |  |
| 323 | `??4ProvFixedLengthPhysAddressType@@QEAAAEAV0@AEBV0@@Z` | `0x10CA0` | 24 | UnwindData |  |
| 333 | `??4ProvMacAddressType@@QEAAAEAV0@AEBV0@@Z` | `0x10CA0` | 24 | UnwindData |  |
| 351 | `??4ProvUDPAddressType@@QEAAAEAV0@AEBV0@@Z` | `0x10CA0` | 24 | UnwindData |  |
| 321 | `??4ProvFixedLengthOctetStringType@@QEAAAEAV0@AEBV0@@Z` | `0x10CC0` | 48 | UnwindData |  |
| 322 | `??4ProvFixedLengthOpaqueType@@QEAAAEAV0@AEBV0@@Z` | `0x10D00` | 48 | UnwindData |  |
| 326 | `??4ProvGaugeType@@QEAAAEAV0@AEBV0@@Z` | `0x10D40` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `??4ProvIntegerType@@QEAAAEAV0@AEBV0@@Z` | `0x10D40` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `??4ProvInstanceType@@QEAAAEAV0@AEBV0@@Z` | `0x10DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `??4ProvNegativeRangeType@@QEAAAEAV0@AEBV0@@Z` | `0x10DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `??4ProvNullType@@QEAAAEAV0@AEBV0@@Z` | `0x10DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `??4ProvPositiveRangeType@@QEAAAEAV0@AEBV0@@Z` | `0x10DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `??4ProvIpAddress@@QEAAAEAVProvValue@@AEBV0@@Z` | `0x10DE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `??4ProvIpAddressType@@QEAAAEAV0@AEBV0@@Z` | `0x10E10` | 44 | UnwindData |  |
| 335 | `??4ProvNetworkAddressType@@QEAAAEAV0@AEBV0@@Z` | `0x10E10` | 44 | UnwindData |  |
| 332 | `??4ProvLexicon@@QEAAAEAV0@AEBV0@@Z` | `0x10E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `??4ProvNull@@QEAAAEAVProvValue@@AEBV0@@Z` | `0x10E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `??4ProvValue@@AEAAAEAV0@AEBV0@@Z` | `0x10E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `??4QueryPreprocessor@@QEAAAEAV0@AEBV0@@Z` | `0x10E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `??4ProvObjectIdentifier@@QEAAAEAVProvValue@@AEBV0@@Z` | `0x10E80` | 51 | UnwindData |  |
| 340 | `??4ProvObjectIdentifierType@@QEAAAEAV0@AEBV0@@Z` | `0x10EC0` | 44 | UnwindData |  |
| 341 | `??4ProvOctetString@@QEAAAEAVProvValue@@AEBV0@@Z` | `0x10F00` | 45 | UnwindData |  |
| 342 | `??4ProvOctetStringType@@QEAAAEAV0@AEBV0@@Z` | `0x10F40` | 128 | UnwindData |  |
| 343 | `??4ProvOpaque@@QEAAAEAVProvValue@@AEBV0@@Z` | `0x10FD0` | 53 | UnwindData |  |
| 344 | `??4ProvOpaqueType@@QEAAAEAV0@AEBV0@@Z` | `0x11010` | 128 | UnwindData |  |
| 347 | `??4ProvPositiveRangedType@@QEAAAEAV0@AEBV0@@Z` | `0x110A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `??4ProvRowStatusType@@QEAAAEAV0@AEBV0@@Z` | `0x11100` | 24 | UnwindData |  |
| 386 | `??8ProvInstanceType@@QEBAHAEBV0@@Z` | `0x11120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `??8ProvValue@@QEBAHAEBV0@@Z` | `0x11120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `??8ProvObjectIdentifier@@QEBAHAEBV0@@Z` | `0x11140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `??9ProvInstanceType@@QEBAHAEBV0@@Z` | `0x11160` | 30 | UnwindData |  |
| 391 | `??9ProvValue@@QEBAHAEBV0@@Z` | `0x11160` | 30 | UnwindData |  |
| 390 | `??9ProvObjectIdentifier@@QEBAHAEBV0@@Z` | `0x11190` | 45 | UnwindData |  |
| 393 | `??BProvAnalyser@@UEAAPEAXXZ` | `0x114C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `??BProvInstanceType@@UEAAPEAXXZ` | `0x114E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `??BProvPositiveRangedType@@UEAAPEAXXZ` | `0x11500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `??RProvIpAddress@@QEBAPEAXXZ` | `0x11500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `??RProvObjectIdentifier@@QEBAPEAXXZ` | `0x11500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `??RProvOctetString@@QEBAPEAXXZ` | `0x11500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `??MProvObjectIdentifier@@QEBAHAEBV0@@Z` | `0x11520` | 30 | UnwindData |  |
| 398 | `??NProvObjectIdentifier@@QEBAHAEBV0@@Z` | `0x11550` | 31 | UnwindData |  |
| 399 | `??OProvObjectIdentifier@@QEBAHAEBV0@@Z` | `0x11580` | 31 | UnwindData |  |
| 400 | `??PProvObjectIdentifier@@QEBAHAEBV0@@Z` | `0x115B0` | 30 | UnwindData |  |
| 404 | `??RProvOpaque@@QEBAPEAXXZ` | `0x116A0` | 5,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `??_FProvAnalyser@@QEAAXXZ` | `0x12CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 500 | `??_FProvDisplayStringType@@QEAAXXZ` | `0x12CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `??_FProvGaugeType@@QEAAXXZ` | `0x12CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `??_FProvInstanceType@@QEAAXXZ` | `0x12D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `??_FProvIntegerType@@QEAAXXZ` | `0x12D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `??_FProvOctetStringType@@QEAAXXZ` | `0x12D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 506 | `??_FProvOpaqueType@@QEAAXXZ` | `0x12D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `??_FProvPhysAddressType@@QEAAXXZ` | `0x12D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `??_FProvPositiveRangedType@@QEAAXXZ` | `0x12D60` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | `?BitStringDef@ProvBitStringType@@AEAAHXZ` | `0x131A0` | 278 | UnwindData |  |
| 527 | `?Check@ProvPositiveRangedType@@QEAAHAEBK@Z` | `0x13380` | 190 | UnwindData |  |
| 537 | `?Copy@ProvBitStringType@@UEBAPEAVProvInstanceType@@XZ` | `0x13450` | 50 | UnwindData |  |
| 539 | `?Copy@ProvCounter64Type@@UEBAPEAVProvInstanceType@@XZ` | `0x13490` | 90 | UnwindData |  |
| 541 | `?Copy@ProvCounterType@@UEBAPEAVProvInstanceType@@XZ` | `0x134F0` | 50 | UnwindData |  |
| 542 | `?Copy@ProvDateTimeType@@UEBAPEAVProvInstanceType@@XZ` | `0x13530` | 50 | UnwindData |  |
| 543 | `?Copy@ProvDisplayStringType@@UEBAPEAVProvInstanceType@@XZ` | `0x13570` | 50 | UnwindData |  |
| 544 | `?Copy@ProvEnumeratedType@@UEBAPEAVProvInstanceType@@XZ` | `0x135B0` | 50 | UnwindData |  |
| 545 | `?Copy@ProvFixedLengthDisplayStringType@@UEBAPEAVProvInstanceType@@XZ` | `0x135F0` | 50 | UnwindData |  |
| 546 | `?Copy@ProvFixedLengthOctetStringType@@UEBAPEAVProvInstanceType@@XZ` | `0x13630` | 50 | UnwindData |  |
| 547 | `?Copy@ProvFixedLengthOpaqueType@@UEBAPEAVProvInstanceType@@XZ` | `0x13670` | 50 | UnwindData |  |
| 548 | `?Copy@ProvFixedLengthPhysAddressType@@UEBAPEAVProvInstanceType@@XZ` | `0x136B0` | 50 | UnwindData |  |
| 550 | `?Copy@ProvGaugeType@@UEBAPEAVProvInstanceType@@XZ` | `0x136F0` | 50 | UnwindData |  |
| 552 | `?Copy@ProvIntegerType@@UEBAPEAVProvInstanceType@@XZ` | `0x13730` | 50 | UnwindData |  |
| 554 | `?Copy@ProvIpAddressType@@UEBAPEAVProvInstanceType@@XZ` | `0x13770` | 50 | UnwindData |  |
| 555 | `?Copy@ProvMacAddressType@@UEBAPEAVProvInstanceType@@XZ` | `0x137B0` | 50 | UnwindData |  |
| 556 | `?Copy@ProvNegativeRangeType@@UEAAPEAV1@XZ` | `0x137F0` | 68 | UnwindData |  |
| 557 | `?Copy@ProvNetworkAddressType@@UEBAPEAVProvInstanceType@@XZ` | `0x13840` | 50 | UnwindData |  |
| 558 | `?Copy@ProvNull@@UEBAPEAVProvValue@@XZ` | `0x13880` | 50 | UnwindData |  |
| 559 | `?Copy@ProvNullType@@UEBAPEAVProvInstanceType@@XZ` | `0x138C0` | 100 | UnwindData |  |
| 560 | `?Copy@ProvOSIAddressType@@UEBAPEAVProvInstanceType@@XZ` | `0x13930` | 50 | UnwindData |  |
| 562 | `?Copy@ProvObjectIdentifierType@@UEBAPEAVProvInstanceType@@XZ` | `0x13970` | 50 | UnwindData |  |
| 564 | `?Copy@ProvOctetStringType@@UEBAPEAVProvInstanceType@@XZ` | `0x139B0` | 50 | UnwindData |  |
| 565 | `?Copy@ProvOpaque@@UEBAPEAVProvValue@@XZ` | `0x139F0` | 62 | UnwindData |  |
| 566 | `?Copy@ProvOpaqueType@@UEBAPEAVProvInstanceType@@XZ` | `0x13A40` | 50 | UnwindData |  |
| 567 | `?Copy@ProvPhysAddressType@@UEBAPEAVProvInstanceType@@XZ` | `0x13A80` | 50 | UnwindData |  |
| 568 | `?Copy@ProvPositiveRangeType@@UEAAPEAV1@XZ` | `0x13AC0` | 68 | UnwindData |  |
| 569 | `?Copy@ProvRowStatusType@@UEBAPEAVProvInstanceType@@XZ` | `0x13B10` | 50 | UnwindData |  |
| 571 | `?Copy@ProvTimeTicksType@@UEBAPEAVProvInstanceType@@XZ` | `0x13B50` | 50 | UnwindData |  |
| 572 | `?Copy@ProvUDPAddressType@@UEBAPEAVProvInstanceType@@XZ` | `0x13B90` | 50 | UnwindData |  |
| 601 | `?CreateLexicon@ProvAnalyser@@MEAAPEAVProvLexicon@@XZ` | `0x13BD0` | 54 | UnwindData |  |
| 604 | `?DateTimeDef@ProvDateTimeType@@AEAAHXZ` | `0x13C10` | 769 | UnwindData |  |
| 605 | `?DbcsToUnicodeString@@YAPEAGPEBD@Z` | `0x13F20` | 144 | UnwindData |  |
| 606 | `?DecCharToDecInteger@ProvAnalyser@@SAKD@Z` | `0x13FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `?DecIntegerToDecChar@ProvAnalyser@@SADE@Z` | `0x13FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `?DecIntegerToDecWChar@ProvAnalyser@@SAGE@Z` | `0x14000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `?DecIntegerToHexChar@ProvAnalyser@@SADE@Z` | `0x14020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 610 | `?DecIntegerToHexWChar@ProvAnalyser@@SAGE@Z` | `0x14040` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `?DecIntegerToOctChar@ProvAnalyser@@SADE@Z` | `0x14070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 612 | `?DecIntegerToOctWChar@ProvAnalyser@@SAGE@Z` | `0x14090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 613 | `?DecWCharToDecInteger@ProvAnalyser@@SAKG@Z` | `0x140B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 615 | `?Encode@ProvDateTimeType@@AEAAXAEBK0000000000@Z` | `0x140E0` | 267 | UnwindData |  |
| 616 | `?EnumerationDef@ProvEnumeratedType@@AEAAHXZ` | `0x14200` | 278 | UnwindData |  |
| 618 | `?Equivalent@ProvCounter64@@QEBAHAEBV1@@Z` | `0x14320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `?Equivalent@ProvCounter64Type@@MEBAHAEBVProvInstanceType@@@Z` | `0x14340` | 125 | UnwindData |  |
| 621 | `?Equivalent@ProvCounter@@QEBAHAEBV1@@Z` | `0x143D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 624 | `?Equivalent@ProvGauge@@QEBAHAEBV1@@Z` | `0x143D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 627 | `?Equivalent@ProvInteger@@QEBAHAEBV1@@Z` | `0x143D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 646 | `?Equivalent@ProvTimeTicks@@QEBAHAEBV1@@Z` | `0x143D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 649 | `?Equivalent@ProvUInteger32@@QEBAHAEBV1@@Z` | `0x143D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 622 | `?Equivalent@ProvCounterType@@MEBAHAEBVProvInstanceType@@@Z` | `0x143F0` | 114 | UnwindData |  |
| 647 | `?Equivalent@ProvTimeTicksType@@MEBAHAEBVProvInstanceType@@@Z` | `0x143F0` | 114 | UnwindData |  |
| 625 | `?Equivalent@ProvGaugeType@@MEBAHAEBVProvInstanceType@@@Z` | `0x14470` | 120 | UnwindData |  |
| 628 | `?Equivalent@ProvIntegerType@@MEBAHAEBVProvInstanceType@@@Z` | `0x14470` | 120 | UnwindData |  |
| 630 | `?Equivalent@ProvIpAddress@@QEBAHAEBV1@@Z` | `0x144F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | `?Equivalent@ProvIpAddressType@@MEBAHAEBVProvInstanceType@@@Z` | `0x14520` | 114 | UnwindData |  |
| 632 | `?Equivalent@ProvNetworkAddressType@@MEBAHAEBVProvInstanceType@@@Z` | `0x14520` | 114 | UnwindData |  |
| 633 | `?Equivalent@ProvNull@@MEBAHAEBVProvValue@@@Z` | `0x145A0` | 82 | UnwindData |  |
| 634 | `?Equivalent@ProvNullType@@MEBAHAEBVProvInstanceType@@@Z` | `0x145A0` | 82 | UnwindData |  |
| 638 | `?Equivalent@ProvObjectIdentifierType@@MEBAHAEBVProvInstanceType@@@Z` | `0x14600` | 133 | UnwindData |  |
| 641 | `?Equivalent@ProvOctetStringType@@MEBAHAEBVProvInstanceType@@@Z` | `0x14690` | 125 | UnwindData |  |
| 643 | `?Equivalent@ProvOpaque@@QEBAHAEBV1@@Z` | `0x14720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `?Equivalent@ProvOpaqueType@@MEBAHAEBVProvInstanceType@@@Z` | `0x14740` | 125 | UnwindData |  |
| 655 | `?Get@ProvAnalyser@@QEAAPEAVProvLexicon@@HHH@Z` | `0x147D0` | 64 | UnwindData |  |
| 656 | `?Get@ProvBitStringType@@AEAAPEAVProvLexicon@@XZ` | `0x14820` | 96 | UnwindData |  |
| 657 | `?Get@ProvDateTimeType@@AEAAPEAVProvLexicon@@XZ` | `0x14890` | 96 | UnwindData |  |
| 658 | `?Get@ProvEnumeratedType@@AEAAPEAVProvLexicon@@XZ` | `0x14900` | 96 | UnwindData |  |
| 659 | `?Get@ProvPositiveRangedType@@IEAAPEAVProvLexicon@@XZ` | `0x149C0` | 75 | UnwindData |  |
| 709 | `?GetRowStatus@ProvRowStatusType@@QEBA?AW4ProvRowStatusEnum@1@XZ` | `0x14E60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `?GetValue@ProvGaugeType@@QEBAKXZ` | `0x14E60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `?GetValue@ProvIntegerType@@QEBAJXZ` | `0x14E60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `?GetString@CBString@@QEAAPEAGXZ` | `0x14ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 711 | `?GetStringValue@ProvBitStringType@@UEBAPEAGXZ` | `0x14EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `?GetStringValue@ProvCounter64Type@@UEBAPEAGXZ` | `0x14EF0` | 203 | UnwindData |  |
| 713 | `?GetStringValue@ProvCounterType@@UEBAPEAGXZ` | `0x14FD0` | 193 | UnwindData |  |
| 731 | `?GetStringValue@ProvTimeTicksType@@UEBAPEAGXZ` | `0x14FD0` | 193 | UnwindData |  |
| 714 | `?GetStringValue@ProvDateTimeType@@UEBAPEAGXZ` | `0x150A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 715 | `?GetStringValue@ProvDisplayStringType@@UEBAPEAGXZ` | `0x150B0` | 119 | UnwindData |  |
| 716 | `?GetStringValue@ProvEnumeratedType@@UEBAPEAGXZ` | `0x15130` | 159 | UnwindData |  |
| 744 | `?GetValue@ProvEnumeratedType@@QEBAPEAGXZ` | `0x15130` | 159 | UnwindData |  |
| 717 | `?GetStringValue@ProvFixedLengthDisplayStringType@@UEBAPEAGXZ` | `0x151E0` | 113 | UnwindData |  |
| 745 | `?GetValue@ProvFixedLengthDisplayStringType@@QEBAPEAGXZ` | `0x151E0` | 113 | UnwindData |  |
| 718 | `?GetStringValue@ProvFixedLengthPhysAddressType@@UEBAPEAGXZ` | `0x15260` | 482 | UnwindData |  |
| 719 | `?GetStringValue@ProvGaugeType@@UEBAPEAGXZ` | `0x15450` | 196 | UnwindData |  |
| 720 | `?GetStringValue@ProvIntegerType@@UEBAPEAGXZ` | `0x15520` | 196 | UnwindData |  |
| 721 | `?GetStringValue@ProvIpAddressType@@UEBAPEAGXZ` | `0x155F0` | 527 | UnwindData |  |
| 723 | `?GetStringValue@ProvNetworkAddressType@@UEBAPEAGXZ` | `0x155F0` | 527 | UnwindData |  |
| 722 | `?GetStringValue@ProvMacAddressType@@UEBAPEAGXZ` | `0x15810` | 313 | UnwindData |  |
| 724 | `?GetStringValue@ProvNullType@@UEBAPEAGXZ` | `0x15950` | 30 | UnwindData |  |
| 725 | `?GetStringValue@ProvOSIAddressType@@UEBAPEAGXZ` | `0x15980` | 827 | UnwindData |  |
| 726 | `?GetStringValue@ProvObjectIdentifierType@@UEBAPEAGXZ` | `0x15CD0` | 557 | UnwindData |  |
| 727 | `?GetStringValue@ProvOctetStringType@@UEBAPEAGXZ` | `0x15F10` | 282 | UnwindData |  |
| 728 | `?GetStringValue@ProvOpaqueType@@UEBAPEAGXZ` | `0x16030` | 465 | UnwindData |  |
| 729 | `?GetStringValue@ProvPhysAddressType@@UEBAPEAGXZ` | `0x16210` | 482 | UnwindData |  |
| 730 | `?GetStringValue@ProvRowStatusType@@UEBAPEAGXZ` | `0x16400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 760 | `?GetValue@ProvRowStatusType@@QEBAPEAGXZ` | `0x16400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `?GetStringValue@ProvUDPAddressType@@UEBAPEAGXZ` | `0x16410` | 276 | UnwindData |  |
| 733 | `?GetToken@ProvAnalyser@@AEAAPEAVProvLexicon@@HHH@Z` | `0x16530` | 1,528 | UnwindData |  |
| 668 | `?GetHighValue@ProvCounter64@@QEBAKXZ` | `0x16B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `?GetToken@ProvLexicon@@QEAA?AW4LexiconToken@1@XZ` | `0x16B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 736 | `?GetUpperBound@ProvNegativeRangeType@@QEAAJXZ` | `0x16B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `?GetUpperBound@ProvPositiveRangeType@@QEAAKXZ` | `0x16B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `?GetValue@ProvIpAddress@@QEBAKXZ` | `0x16B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `?IsValid@ProvInstanceType@@UEBAHXZ` | `0x16B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 738 | `?GetValue@ProvBitStringType@@QEBAKAEAPEAPEAG@Z` | `0x16B40` | 485 | UnwindData |  |
| 739 | `?GetValue@ProvCounter64Type@@QEBAXAEAK0@Z` | `0x16D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `?GetValue@ProvDateTimeType@@QEBAPEAGXZ` | `0x16D50` | 467 | UnwindData |  |
| 743 | `?GetValue@ProvDisplayStringType@@QEBAPEAGXZ` | `0x16F30` | 114 | UnwindData |  |
| 751 | `?GetValue@ProvIpAddressType@@QEBAKXZ` | `0x16FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `?GetValue@ProvNetworkAddressType@@QEBAKXZ` | `0x16FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | `?GetValue@ProvLexicon@@QEAAPEATProvLexiconValue@@XZ` | `0x16FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 755 | `?GetValue@ProvObjectIdentifierType@@QEBAPEAKXZ` | `0x16FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `?GetValue@ProvOctetStringType@@QEBAPEAEXZ` | `0x16FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `?GetValue@ProvOpaque@@QEBAPEAEXZ` | `0x16FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `?GetValue@ProvOpaqueType@@QEBAPEAEXZ` | `0x17000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 768 | `?GetValueLength@ProvObjectIdentifierType@@QEBAKXZ` | `0x17020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `?GetValueLength@ProvOctetStringType@@QEBAKXZ` | `0x17030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `?GetValueLength@ProvOpaque@@QEBAKXZ` | `0x17040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 772 | `?GetValueLength@ProvOpaqueType@@QEBAKXZ` | `0x17050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `?HexCharToDecInteger@ProvAnalyser@@SAKD@Z` | `0x17070` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 774 | `?HexWCharToDecInteger@ProvAnalyser@@SAKG@Z` | `0x170B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `?IsAlpha@ProvAnalyser@@SAHG@Z` | `0x17100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 786 | `?IsAlphaNumeric@ProvAnalyser@@SAHG@Z` | `0x17120` | 53 | UnwindData |  |
| 787 | `?IsDecimal@ProvAnalyser@@SAHG@Z` | `0x17160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 788 | `?IsEof@ProvAnalyser@@SAHG@Z` | `0x17180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `?IsHex@ProvAnalyser@@SAHG@Z` | `0x17190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 790 | `?IsLeadingDecimal@ProvAnalyser@@SAHG@Z` | `0x171B0` | 47 | UnwindData |  |
| 792 | `?IsOctal@ProvAnalyser@@SAHG@Z` | `0x171F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `?IsProvV1Type@ProvInstanceType@@UEBAHXZ` | `0x17210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 795 | `?IsProvV2CType@ProvInstanceType@@UEBAHXZ` | `0x17210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `?IsWhitespace@ProvAnalyser@@SAHG@Z` | `0x17220` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `?Match@ProvBitStringType@@AEAAPEAVProvLexicon@@W4LexiconToken@2@@Z` | `0x173A0` | 55 | UnwindData |  |
| 811 | `?Match@ProvDateTimeType@@AEAAPEAVProvLexicon@@W4LexiconToken@2@@Z` | `0x173E0` | 55 | UnwindData |  |
| 812 | `?Match@ProvEnumeratedType@@AEAAPEAVProvLexicon@@W4LexiconToken@2@@Z` | `0x17420` | 55 | UnwindData |  |
| 813 | `?Match@ProvPositiveRangedType@@IEAAPEAVProvLexicon@@W4LexiconToken@2@@Z` | `0x17460` | 55 | UnwindData |  |
| 814 | `?OctCharToDecInteger@ProvAnalyser@@SAKD@Z` | `0x175D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `?OctWCharToDecInteger@ProvAnalyser@@SAKG@Z` | `0x175E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `?Parse@ProvBitStringType@@AEAAHPEBG@Z` | `0x175F0` | 70 | UnwindData |  |
| 819 | `?Parse@ProvCounter64Type@@IEAAHPEBG@Z` | `0x17640` | 783 | UnwindData |  |
| 820 | `?Parse@ProvCounterType@@IEAAHPEBG@Z` | `0x17960` | 136 | UnwindData |  |
| 835 | `?Parse@ProvTimeTicksType@@IEAAHPEBG@Z` | `0x17960` | 136 | UnwindData |  |
| 821 | `?Parse@ProvDateTimeType@@AEAAHPEBG@Z` | `0x179F0` | 34 | UnwindData |  |
| 822 | `?Parse@ProvEnumeratedType@@AEAAHPEBG@Z` | `0x17A20` | 70 | UnwindData |  |
| 823 | `?Parse@ProvFixedLengthPhysAddressType@@IEAAHPEBG@Z` | `0x17A70` | 407 | UnwindData |  |
| 824 | `?Parse@ProvGaugeType@@IEAAHPEBG@Z` | `0x17C10` | 139 | UnwindData |  |
| 825 | `?Parse@ProvIntegerType@@IEAAHPEBG@Z` | `0x17CB0` | 138 | UnwindData |  |
| 826 | `?Parse@ProvIpAddressType@@IEAAHPEBG@Z` | `0x17D40` | 912 | UnwindData |  |
| 827 | `?Parse@ProvMacAddressType@@IEAAHPEBG@Z` | `0x180E0` | 264 | UnwindData |  |
| 828 | `?Parse@ProvNetworkAddressType@@IEAAHPEBG@Z` | `0x181F0` | 945 | UnwindData |  |
| 829 | `?Parse@ProvOSIAddressType@@IEAAHPEBG@Z` | `0x185B0` | 569 | UnwindData |  |
| 830 | `?Parse@ProvObjectIdentifierType@@IEAAHPEBG@Z` | `0x187F0` | 559 | UnwindData |  |
| 831 | `?Parse@ProvOctetStringType@@IEAAHPEBG@Z` | `0x18A30` | 357 | UnwindData |  |
| 832 | `?Parse@ProvOpaqueType@@IEAAHPEBG@Z` | `0x18BA0` | 357 | UnwindData |  |
| 833 | `?Parse@ProvPhysAddressType@@IEAAHPEBG@Z` | `0x18D10` | 391 | UnwindData |  |
| 834 | `?Parse@ProvPositiveRangedType@@IEAAHPEBG@Z` | `0x18EA0` | 67 | UnwindData |  |
| 836 | `?Parse@ProvUDPAddressType@@IEAAHPEBG@Z` | `0x18EF0` | 1,122 | UnwindData |  |
| 839 | `?Prefix@ProvObjectIdentifier@@QEBAHKAEAV1@@Z` | `0x19360` | 105 | UnwindData |  |
| 864 | `?PushBack@ProvBitStringType@@AEAAXXZ` | `0x193D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | `?PushBack@ProvDateTimeType@@AEAAXXZ` | `0x193F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `?PushBack@ProvEnumeratedType@@AEAAXXZ` | `0x19410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `?PushBack@ProvPositiveRangedType@@IEAAXXZ` | `0x19430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `?PutBack@ProvAnalyser@@QEAAXPEBVProvLexicon@@@Z` | `0x19440` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 871 | `?RangeDef@ProvPositiveRangedType@@IEAAHXZ` | `0x19550` | 572 | UnwindData |  |
| 873 | `?RecursiveDef@ProvBitStringType@@AEAAHXZ` | `0x197A0` | 102 | UnwindData |  |
| 874 | `?RecursiveDef@ProvEnumeratedType@@AEAAHXZ` | `0x19810` | 102 | UnwindData |  |
| 875 | `?RecursiveDef@ProvPositiveRangedType@@IEAAHXZ` | `0x198F0` | 96 | UnwindData |  |
| 892 | `?Set@ProvAnalyser@@QEAAXPEBG@Z` | `0x19A00` | 128 | UnwindData |  |
| 898 | `?SetLowerBound@ProvNegativeRangeType@@QEAAXAEBJ@Z` | `0x19A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 899 | `?SetLowerBound@ProvPositiveRangeType@@QEAAXAEBK@Z` | `0x19A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 907 | `?SetStatus@ProvPositiveRangedType@@QEAAXAEBH@Z` | `0x19A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 906 | `?SetStatus@ProvInstanceType@@QEAAXH@Z` | `0x19AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 908 | `?SetToken@ProvLexicon@@QEAAXW4LexiconToken@1@@Z` | `0x19AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | `?SetUpperBound@ProvNegativeRangeType@@QEAAXAEBJ@Z` | `0x19AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | `?SetUpperBound@ProvPositiveRangeType@@QEAAXAEBK@Z` | `0x19AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `?SetValue@ProvOpaque@@QEAAXPEBEK@Z` | `0x19AC0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `?Suffix@ProvObjectIdentifier@@QEBAHKAEAV1@@Z` | `0x19C20` | 115 | UnwindData |  |
| 949 | `?UnicodeStringAppend@@YAPEAGPEBG0@Z` | `0x19CA0` | 209 | UnwindData |  |
| 950 | `?UnicodeStringDuplicate@@YAPEAGPEBG@Z` | `0x19D80` | 112 | UnwindData |  |
| 951 | `?UnicodeToDbcsString@@YAPEADPEBG@Z` | `0x19E00` | 120 | UnwindData |  |
| 16 | `??0ProvCounter64@@QEAA@AEBV0@@Z` | `0x19FB0` | 42 | UnwindData |  |
| 23 | `??0ProvCounter@@QEAA@AEBV0@@Z` | `0x19FE0` | 36 | UnwindData |  |
| 66 | `??0ProvGauge@@QEAA@AEBV0@@Z` | `0x1A010` | 36 | UnwindData |  |
| 75 | `??0ProvInteger@@QEAA@AEBV0@@Z` | `0x1A040` | 36 | UnwindData |  |
| 82 | `??0ProvIpAddress@@QEAA@AEBV0@@Z` | `0x1A070` | 61 | UnwindData |  |
| 84 | `??0ProvIpAddress@@QEAA@PEBD@Z` | `0x1A0C0` | 254 | UnwindData |  |
| 113 | `??0ProvObjectIdentifier@@QEAA@AEBV0@@Z` | `0x1A1D0` | 85 | UnwindData |  |
| 114 | `??0ProvObjectIdentifier@@QEAA@PEBD@Z` | `0x1A230` | 204 | UnwindData |  |
| 115 | `??0ProvObjectIdentifier@@QEAA@PEBKK@Z` | `0x1A310` | 71 | UnwindData |  |
| 121 | `??0ProvOctetString@@QEAA@AEBV0@@Z` | `0x1A360` | 61 | UnwindData |  |
| 122 | `??0ProvOctetString@@QEAA@PEBEK@Z` | `0x1A3B0` | 53 | UnwindData |  |
| 151 | `??0ProvTimeTicks@@QEAA@AEBV0@@Z` | `0x1A3F0` | 36 | UnwindData |  |
| 163 | `??0ProvUInteger32@@QEAA@AEBV0@@Z` | `0x1A420` | 36 | UnwindData |  |
| 261 | `??1ProvObjectIdentifier@@UEAA@XZ` | `0x1A450` | 53 | UnwindData |  |
| 263 | `??1ProvOctetString@@UEAA@XZ` | `0x1A490` | 50 | UnwindData |  |
| 392 | `??AProvObjectIdentifier@@QEBAAEAKK@Z` | `0x1A4D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `??HProvObjectIdentifier@@QEBA?AV0@AEBV0@@Z` | `0x1A500` | 208 | UnwindData |  |
| 532 | `?Compare@ProvObjectIdentifier@@IEBA?AW4Comparison@1@AEBV1@0@Z` | `0x1A6C0` | 102 | UnwindData |  |
| 538 | `?Copy@ProvCounter64@@UEBAPEAVProvValue@@XZ` | `0x1A730` | 81 | UnwindData |  |
| 540 | `?Copy@ProvCounter@@UEBAPEAVProvValue@@XZ` | `0x1A790` | 72 | UnwindData |  |
| 549 | `?Copy@ProvGauge@@UEBAPEAVProvValue@@XZ` | `0x1A7E0` | 72 | UnwindData |  |
| 551 | `?Copy@ProvInteger@@UEBAPEAVProvValue@@XZ` | `0x1A830` | 72 | UnwindData |  |
| 553 | `?Copy@ProvIpAddress@@UEBAPEAVProvValue@@XZ` | `0x1A880` | 79 | UnwindData |  |
| 561 | `?Copy@ProvObjectIdentifier@@UEBAPEAVProvValue@@XZ` | `0x1A8E0` | 61 | UnwindData |  |
| 563 | `?Copy@ProvOctetString@@UEBAPEAVProvValue@@XZ` | `0x1A930` | 55 | UnwindData |  |
| 570 | `?Copy@ProvTimeTicks@@UEBAPEAVProvValue@@XZ` | `0x1A970` | 72 | UnwindData |  |
| 573 | `?Copy@ProvUInteger32@@UEBAPEAVProvValue@@XZ` | `0x1A9C0` | 72 | UnwindData |  |
| 603 | `?Cut@ProvObjectIdentifier@@QEBAPEAV1@AEAV1@@Z` | `0x1AA10` | 159 | UnwindData |  |
| 617 | `?Equivalent@ProvCounter64@@MEBAHAEBVProvValue@@@Z` | `0x1AAC0` | 125 | UnwindData |  |
| 620 | `?Equivalent@ProvCounter@@MEBAHAEBVProvValue@@@Z` | `0x1AB50` | 114 | UnwindData |  |
| 623 | `?Equivalent@ProvGauge@@MEBAHAEBVProvValue@@@Z` | `0x1AB50` | 114 | UnwindData |  |
| 626 | `?Equivalent@ProvInteger@@MEBAHAEBVProvValue@@@Z` | `0x1AB50` | 114 | UnwindData |  |
| 645 | `?Equivalent@ProvTimeTicks@@MEBAHAEBVProvValue@@@Z` | `0x1AB50` | 114 | UnwindData |  |
| 648 | `?Equivalent@ProvUInteger32@@MEBAHAEBVProvValue@@@Z` | `0x1AB50` | 114 | UnwindData |  |
| 629 | `?Equivalent@ProvIpAddress@@MEBAHAEBVProvValue@@@Z` | `0x1ABD0` | 117 | UnwindData |  |
| 635 | `?Equivalent@ProvObjectIdentifier@@IEBAHAEBV1@@Z` | `0x1AC50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 636 | `?Equivalent@ProvObjectIdentifier@@MEBAHAEBVProvValue@@@Z` | `0x1ACB0` | 117 | UnwindData |  |
| 637 | `?Equivalent@ProvObjectIdentifier@@QEBAHAEBV1@K@Z` | `0x1AD30` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 639 | `?Equivalent@ProvOctetString@@MEBAHAEBVProvValue@@@Z` | `0x1AD90` | 117 | UnwindData |  |
| 640 | `?Equivalent@ProvOctetString@@QEBAHAEBV1@@Z` | `0x1AE10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 642 | `?Equivalent@ProvOpaque@@MEBAHAEBVProvValue@@@Z` | `0x1AE60` | 119 | UnwindData |  |
| 660 | `?GetAllocatedString@ProvObjectIdentifier@@QEBAPEADXZ` | `0x1AEE0` | 252 | UnwindData |  |
| 754 | `?GetValue@ProvObjectIdentifier@@QEBAPEAKXZ` | `0x1AFF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `?GetValueLength@ProvObjectIdentifier@@QEBAKXZ` | `0x1B000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `?Initialize@ProvObjectIdentifier@@MEAAXPEBKK@Z` | `0x1B010` | 160 | UnwindData |  |
| 782 | `?Initialize@ProvOctetString@@MEAAXPEBEK@Z` | `0x1B0C0` | 68 | UnwindData |  |
| 816 | `?OverWrite@ProvObjectIdentifier@@AEAAXPEBK@Z` | `0x1B110` | 38 | UnwindData |  |
| 817 | `?OverWrite@ProvOctetString@@AEAAXPEBE@Z` | `0x1B140` | 34 | UnwindData |  |
| 888 | `?Replicate@ProvObjectIdentifier@@MEBAPEAKPEBKK0K@Z` | `0x1B170` | 270 | UnwindData |  |
| 889 | `?Replicate@ProvObjectIdentifier@@MEBAPEAKPEBKK@Z` | `0x1B290` | 110 | UnwindData |  |
| 890 | `?Replicate@ProvOctetString@@MEAAPEAEPEBEK@Z` | `0x1B310` | 75 | UnwindData |  |
| 912 | `?SetValue@ProvCounter64@@QEAAXKK@Z` | `0x1B370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 916 | `?SetValue@ProvIpAddress@@QEAAXK@Z` | `0x1B380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 917 | `?SetValue@ProvObjectIdentifier@@QEAAXPEBKK@Z` | `0x1B3A0` | 138 | UnwindData |  |
| 918 | `?SetValue@ProvOctetString@@QEAAXPEBEK@Z` | `0x1B430` | 91 | UnwindData |  |
| 947 | `?UnReplicate@ProvObjectIdentifier@@MEAAXPEAK@Z` | `0x1B4A0` | 47 | UnwindData |  |
| 948 | `?UnReplicate@ProvOctetString@@MEAAXPEAE@Z` | `0x1B4E0` | 25 | UnwindData |  |
| 8 | `??0PartitionSet@@QEAA@AEBV0@@Z` | `0x1B5C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `??0WmiAndNode@@QEAA@AEBV0@@Z` | `0x1B600` | 68 | UnwindData |  |
| 171 | `??0WmiNotNode@@QEAA@AEBV0@@Z` | `0x1B650` | 68 | UnwindData |  |
| 172 | `??0WmiNotNode@@QEAA@PEAVWmiTreeNode@@0@Z` | `0x1B6A0` | 60 | UnwindData |  |
| 173 | `??0WmiNullNode@@QEAA@$$QEAV0@@Z` | `0x1B6F0` | 39 | UnwindData |  |
| 174 | `??0WmiNullNode@@QEAA@AEBV0@@Z` | `0x1B6F0` | 39 | UnwindData |  |
| 175 | `??0WmiNullNode@@QEAA@PEAGKPEAVWmiTreeNode@@@Z` | `0x1B720` | 63 | UnwindData |  |
| 176 | `??0WmiNullRangeNode@@QEAA@AEBV0@@Z` | `0x1B770` | 39 | UnwindData |  |
| 177 | `??0WmiNullRangeNode@@QEAA@PEAGKPEAVWmiTreeNode@@1@Z` | `0x1B7A0` | 89 | UnwindData |  |
| 178 | `??0WmiOperatorEqualNode@@QEAA@AEBV0@@Z` | `0x1B800` | 78 | UnwindData |  |
| 180 | `??0WmiOperatorEqualOrGreaterNode@@QEAA@AEBV0@@Z` | `0x1B860` | 78 | UnwindData |  |
| 182 | `??0WmiOperatorEqualOrLessNode@@QEAA@AEBV0@@Z` | `0x1B8C0` | 78 | UnwindData |  |
| 183 | `??0WmiOperatorEqualOrLessNode@@QEAA@PEAVWmiTreeNode@@0@Z` | `0x1B920` | 50 | UnwindData |  |
| 184 | `??0WmiOperatorGreaterNode@@QEAA@AEBV0@@Z` | `0x1B960` | 78 | UnwindData |  |
| 186 | `??0WmiOperatorIsANode@@QEAA@AEBV0@@Z` | `0x1B9C0` | 78 | UnwindData |  |
| 187 | `??0WmiOperatorIsANode@@QEAA@PEAVWmiTreeNode@@0@Z` | `0x1BA20` | 50 | UnwindData |  |
| 188 | `??0WmiOperatorLessNode@@QEAA@AEBV0@@Z` | `0x1BA60` | 78 | UnwindData |  |
| 189 | `??0WmiOperatorLessNode@@QEAA@PEAVWmiTreeNode@@0@Z` | `0x1BAC0` | 50 | UnwindData |  |
| 190 | `??0WmiOperatorLikeNode@@QEAA@AEBV0@@Z` | `0x1BB00` | 78 | UnwindData |  |
| 191 | `??0WmiOperatorLikeNode@@QEAA@PEAVWmiTreeNode@@0@Z` | `0x1BB60` | 50 | UnwindData |  |
| 192 | `??0WmiOperatorNode@@QEAA@AEBV0@@Z` | `0x1BBA0` | 68 | UnwindData |  |
| 194 | `??0WmiOperatorNotEqualNode@@QEAA@AEBV0@@Z` | `0x1BBF0` | 78 | UnwindData |  |
| 195 | `??0WmiOperatorNotEqualNode@@QEAA@PEAVWmiTreeNode@@0@Z` | `0x1BC50` | 50 | UnwindData |  |
| 196 | `??0WmiOperatorNotIsANode@@QEAA@AEBV0@@Z` | `0x1BC90` | 78 | UnwindData |  |
| 197 | `??0WmiOperatorNotIsANode@@QEAA@PEAVWmiTreeNode@@0@Z` | `0x1BCF0` | 50 | UnwindData |  |
| 198 | `??0WmiOperatorNotLikeNode@@QEAA@AEBV0@@Z` | `0x1BD30` | 78 | UnwindData |  |
| 199 | `??0WmiOperatorNotLikeNode@@QEAA@PEAVWmiTreeNode@@0@Z` | `0x1BD90` | 50 | UnwindData |  |
| 200 | `??0WmiOrNode@@QEAA@AEBV0@@Z` | `0x1BDD0` | 68 | UnwindData |  |
| 201 | `??0WmiOrNode@@QEAA@PEAVWmiTreeNode@@00@Z` | `0x1BE20` | 59 | UnwindData |  |
| 202 | `??0WmiRangeNode@@QEAA@AEBV0@@Z` | `0x1BE70` | 106 | UnwindData |  |
| 204 | `??0WmiSignedIntegerNode@@QEAA@$$QEAV0@@Z` | `0x1BEE0` | 58 | UnwindData |  |
| 205 | `??0WmiSignedIntegerNode@@QEAA@AEBV0@@Z` | `0x1BEE0` | 58 | UnwindData |  |
| 206 | `??0WmiSignedIntegerNode@@QEAA@PEAGJKPEAVWmiTreeNode@@@Z` | `0x1BF20` | 84 | UnwindData |  |
| 207 | `??0WmiSignedIntegerRangeNode@@QEAA@$$QEAV0@@Z` | `0x1BF80` | 64 | UnwindData |  |
| 208 | `??0WmiSignedIntegerRangeNode@@QEAA@AEBV0@@Z` | `0x1BF80` | 64 | UnwindData |  |
| 210 | `??0WmiStringNode@@QEAA@AEBV0@@Z` | `0x1BFD0` | 60 | UnwindData |  |
| 212 | `??0WmiStringRangeNode@@QEAA@AEBV0@@Z` | `0x1C020` | 68 | UnwindData |  |
| 214 | `??0WmiTreeNode@@QEAA@AEBV0@@Z` | `0x1C070` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `??0WmiTreeNode@@QEAA@PEAV0@@Z` | `0x1C070` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `??0WmiTreeNodeIterator@@QEAA@AEBV0@@Z` | `0x1C0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `??0WmiTreeNodeIterator@@QEAA@PEAV0@@Z` | `0x1C0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `??0WmiTreeNodeIterator@@QEAA@PEAVWmiTreeNode@@@Z` | `0x1C0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `??0WmiUnsignedIntegerNode@@QEAA@$$QEAV0@@Z` | `0x1C0F0` | 58 | UnwindData |  |
| 221 | `??0WmiUnsignedIntegerNode@@QEAA@AEBV0@@Z` | `0x1C0F0` | 58 | UnwindData |  |
| 223 | `??0WmiUnsignedIntegerRangeNode@@QEAA@$$QEAV0@@Z` | `0x1C130` | 64 | UnwindData |  |
| 224 | `??0WmiUnsignedIntegerRangeNode@@QEAA@AEBV0@@Z` | `0x1C130` | 64 | UnwindData |  |
| 226 | `??0WmiValueNode@@QEAA@AEBV0@@Z` | `0x1C180` | 94 | UnwindData |  |
| 278 | `??1WmiNotNode@@UEAA@XZ` | `0x1C210` | 66 | UnwindData |  |
| 279 | `??1WmiNullNode@@UEAA@XZ` | `0x1C260` | 18 | UnwindData |  |
| 294 | `??1WmiSignedIntegerNode@@UEAA@XZ` | `0x1C260` | 18 | UnwindData |  |
| 280 | `??1WmiNullRangeNode@@UEAA@XZ` | `0x1C280` | 28 | UnwindData |  |
| 285 | `??1WmiOperatorIsANode@@UEAA@XZ` | `0x1C2B0` | 76 | UnwindData |  |
| 286 | `??1WmiOperatorLessNode@@UEAA@XZ` | `0x1C310` | 76 | UnwindData |  |
| 287 | `??1WmiOperatorLikeNode@@UEAA@XZ` | `0x1C370` | 76 | UnwindData |  |
| 289 | `??1WmiOperatorNotEqualNode@@UEAA@XZ` | `0x1C3D0` | 76 | UnwindData |  |
| 290 | `??1WmiOperatorNotIsANode@@UEAA@XZ` | `0x1C430` | 76 | UnwindData |  |
| 291 | `??1WmiOperatorNotLikeNode@@UEAA@XZ` | `0x1C490` | 76 | UnwindData |  |
| 292 | `??1WmiOrNode@@UEAA@XZ` | `0x1C4F0` | 91 | UnwindData |  |
| 299 | `??1WmiTreeNodeIterator@@UEAA@XZ` | `0x1C560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `??4Conjunctions@@QEAAAEAV0@AEBV0@@Z` | `0x1C580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `??4Disjunctions@@QEAAAEAV0@AEBV0@@Z` | `0x1C580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `??4PartitionSet@@QEAAAEAV0@AEBV0@@Z` | `0x1C5A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `??4WmiAndNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `??4WmiNotNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `??4WmiOperatorEqualNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `??4WmiOperatorEqualOrGreaterNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `??4WmiOperatorEqualOrLessNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `??4WmiOperatorGreaterNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `??4WmiOperatorIsANode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `??4WmiOperatorLessNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `??4WmiOperatorLikeNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `??4WmiOperatorNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `??4WmiOperatorNotEqualNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `??4WmiOperatorNotIsANode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `??4WmiOperatorNotLikeNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `??4WmiOrNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `??4WmiTreeNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C5D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `??4WmiNullNode@@QEAAAEAV0@$$QEAV0@@Z` | `0x1C610` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `??4WmiNullNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C610` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `??4WmiValueNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C610` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `??4WmiNullRangeNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C660` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `??4WmiRangeNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C660` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `??4WmiSignedIntegerNode@@QEAAAEAV0@$$QEAV0@@Z` | `0x1C6C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `??4WmiSignedIntegerNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C6C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `??4WmiUnsignedIntegerNode@@QEAAAEAV0@$$QEAV0@@Z` | `0x1C6C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `??4WmiUnsignedIntegerNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C6C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `??4WmiSignedIntegerRangeNode@@QEAAAEAV0@$$QEAV0@@Z` | `0x1C720` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `??4WmiSignedIntegerRangeNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C720` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `??4WmiUnsignedIntegerRangeNode@@QEAAAEAV0@$$QEAV0@@Z` | `0x1C720` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `??4WmiUnsignedIntegerRangeNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C720` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `??4WmiStringNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C790` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `??4WmiStringRangeNode@@QEAAAEAV0@AEBV0@@Z` | `0x1C7F0` | 2,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `??_FWmiAndNode@@QEAAXXZ` | `0x1CFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `??_FWmiNotNode@@QEAAXXZ` | `0x1CFF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `??_FWmiOperatorEqualNode@@QEAAXXZ` | `0x1D000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `??_FWmiOperatorEqualOrGreaterNode@@QEAAXXZ` | `0x1D010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | `??_FWmiOperatorEqualOrLessNode@@QEAAXXZ` | `0x1D020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `??_FWmiOperatorGreaterNode@@QEAAXXZ` | `0x1D030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 515 | `??_FWmiOperatorIsANode@@QEAAXXZ` | `0x1D040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `??_FWmiOperatorLessNode@@QEAAXXZ` | `0x1D050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | `??_FWmiOperatorLikeNode@@QEAAXXZ` | `0x1D060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 518 | `??_FWmiOperatorNotEqualNode@@QEAAXXZ` | `0x1D070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `??_FWmiOperatorNotIsANode@@QEAAXXZ` | `0x1D080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `??_FWmiOperatorNotLikeNode@@QEAAXXZ` | `0x1D090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `??_FWmiOrNode@@QEAAXXZ` | `0x1D0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | `??_FWmiTreeNode@@QEAAXXZ` | `0x1D0C0` | 35 | UnwindData |  |
| 524 | `?AllocTypeNode@QueryPreprocessor@@MEAAPEAVWmiTreeNode@@PEAXPEAGAEAUtagVARIANT@@W4WmiValueFunction@WmiValueNode@@3PEAV2@@Z` | `0x1D0F0` | 340 | UnwindData |  |
| 536 | `?ConvertToRanges@QueryPreprocessor@@IEAA?AW4WmiTriState@@AEAPEAVWmiTreeNode@@@Z` | `0x1D390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 575 | `?Copy@WmiNotNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x1D3A0` | 139 | UnwindData |  |
| 576 | `?Copy@WmiNullNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x1D440` | 71 | UnwindData |  |
| 577 | `?Copy@WmiNullRangeNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x1D490` | 63 | UnwindData |  |
| 580 | `?Copy@WmiOperatorEqualOrLessNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x1D4E0` | 139 | UnwindData |  |
| 582 | `?Copy@WmiOperatorIsANode@@UEAAPEAVWmiTreeNode@@XZ` | `0x1D580` | 139 | UnwindData |  |
| 583 | `?Copy@WmiOperatorLessNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x1D620` | 139 | UnwindData |  |
| 584 | `?Copy@WmiOperatorLikeNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x1D6C0` | 139 | UnwindData |  |
| 585 | `?Copy@WmiOperatorNotEqualNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x1D760` | 139 | UnwindData |  |
| 586 | `?Copy@WmiOperatorNotIsANode@@UEAAPEAVWmiTreeNode@@XZ` | `0x1D800` | 139 | UnwindData |  |
| 587 | `?Copy@WmiOperatorNotLikeNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x1D8A0` | 139 | UnwindData |  |
| 588 | `?Copy@WmiOrNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x1D940` | 247 | UnwindData |  |
| 589 | `?Copy@WmiSignedIntegerNode@@UEAAPEAVWmiTreeNode@@XZ` | `0x1DA40` | 77 | UnwindData |  |
| 594 | `?Copy@WmiTreeNodeIterator@@UEAAPEAV1@XZ` | `0x1DAA0` | 64 | UnwindData |  |
| 652 | `?EvaluateNotEqualExpression@QueryPreprocessor@@IEAA?AW4WmiTriState@@AEAPEAVWmiTreeNode@@@Z` | `0x1DAF0` | 41 | UnwindData |  |
| 664 | `?GetData@WmiTreeNode@@QEAAXPEAPEAX@Z` | `0x1DB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `?GetIntersectingRange@WmiSignedIntegerRangeNode@@QEAA?AW4WmiTriState@@AEAV1@AEAPEAV1@@Z` | `0x1DB30` | 1,662 | UnwindData |  |
| 672 | `?GetIntersectingRange@WmiStringRangeNode@@QEAA?AW4WmiTriState@@AEAV1@AEAPEAV1@@Z` | `0x1E1C0` | 1,793 | UnwindData |  |
| 673 | `?GetIntersectingRange@WmiUnsignedIntegerRangeNode@@QEAA?AW4WmiTriState@@AEAV1@AEAPEAV1@@Z` | `0x1E8D0` | 1,662 | UnwindData |  |
| 683 | `?GetOverlappingRange@WmiSignedIntegerRangeNode@@QEAA?AW4WmiTriState@@AEAV1@AEAPEAV1@@Z` | `0x1EF60` | 2,464 | UnwindData |  |
| 685 | `?GetOverlappingRange@WmiUnsignedIntegerRangeNode@@QEAA?AW4WmiTriState@@AEAV1@AEAPEAV1@@Z` | `0x1F910` | 2,466 | UnwindData |  |
| 687 | `?GetParent@WmiTreeNode@@QEAAXAEAPEAPEAV1@@Z` | `0x202C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 698 | `?GetRange@WmiOperatorEqualOrLessNode@@UEAAPEAVWmiRangeNode@@XZ` | `0x202D0` | 436 | UnwindData |  |
| 699 | `?GetRange@WmiOperatorGreaterNode@@UEAAPEAVWmiRangeNode@@XZ` | `0x20490` | 444 | UnwindData |  |
| 700 | `?GetRange@WmiOperatorIsANode@@UEAAPEAVWmiRangeNode@@XZ` | `0x20660` | 204 | UnwindData |  |
| 702 | `?GetRange@WmiOperatorLikeNode@@UEAAPEAVWmiRangeNode@@XZ` | `0x20660` | 204 | UnwindData |  |
| 704 | `?GetRange@WmiOperatorNotIsANode@@UEAAPEAVWmiRangeNode@@XZ` | `0x20660` | 204 | UnwindData |  |
| 705 | `?GetRange@WmiOperatorNotLikeNode@@UEAAPEAVWmiRangeNode@@XZ` | `0x20660` | 204 | UnwindData |  |
| 701 | `?GetRange@WmiOperatorLessNode@@UEAAPEAVWmiRangeNode@@XZ` | `0x20740` | 439 | UnwindData |  |
| 784 | `?InvariantEvaluate@QueryPreprocessor@@MEAA?AW4QuadState@1@PEAXPEAVWmiTreeNode@@1@Z` | `0x20900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 800 | `?Leaf@PartitionSet@@QEAAHXZ` | `0x20910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | `?LexicographicallyAfter@WmiSignedIntegerNode@@QEAAHAEAJ@Z` | `0x20930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `?LexicographicallyAfter@WmiStringNode@@QEAAHAEAPEAG@Z` | `0x20950` | 169 | UnwindData |  |
| 803 | `?LexicographicallyAfter@WmiUnsignedIntegerNode@@QEAAHAEAK@Z` | `0x20A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 804 | `?LexicographicallyBefore@WmiSignedIntegerNode@@QEAAHAEAJ@Z` | `0x20A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `?LexicographicallyBefore@WmiStringNode@@QEAAHAEAPEAG@Z` | `0x20A40` | 243 | UnwindData |  |
| 806 | `?LexicographicallyBefore@WmiUnsignedIntegerNode@@QEAAHAEAK@Z` | `0x20B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 807 | `?LowerBound@WmiSignedIntegerRangeNode@@QEAAJXZ` | `0x20B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 809 | `?LowerBound@WmiUnsignedIntegerRangeNode@@QEAAKXZ` | `0x20B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | `?Print@WmiAndNode@@UEAAXXZ` | `0x20B70` | 278 | UnwindData |  |
| 841 | `?Print@WmiNotNode@@UEAAXXZ` | `0x20C90` | 167 | UnwindData |  |
| 842 | `?Print@WmiNullNode@@UEAAXXZ` | `0x20D40` | 60 | UnwindData |  |
| 843 | `?Print@WmiNullRangeNode@@UEAAXXZ` | `0x20D40` | 60 | UnwindData |  |
| 844 | `?Print@WmiOperatorEqualNode@@UEAAXXZ` | `0x20D90` | 77 | UnwindData |  |
| 845 | `?Print@WmiOperatorEqualOrGreaterNode@@UEAAXXZ` | `0x20DF0` | 77 | UnwindData |  |
| 846 | `?Print@WmiOperatorEqualOrLessNode@@UEAAXXZ` | `0x20E50` | 77 | UnwindData |  |
| 847 | `?Print@WmiOperatorGreaterNode@@UEAAXXZ` | `0x20EB0` | 77 | UnwindData |  |
| 848 | `?Print@WmiOperatorIsANode@@UEAAXXZ` | `0x20F10` | 77 | UnwindData |  |
| 849 | `?Print@WmiOperatorLessNode@@UEAAXXZ` | `0x20F70` | 77 | UnwindData |  |
| 850 | `?Print@WmiOperatorLikeNode@@UEAAXXZ` | `0x20FD0` | 77 | UnwindData |  |
| 851 | `?Print@WmiOperatorNotEqualNode@@UEAAXXZ` | `0x21030` | 77 | UnwindData |  |
| 852 | `?Print@WmiOperatorNotIsANode@@UEAAXXZ` | `0x21090` | 77 | UnwindData |  |
| 853 | `?Print@WmiOperatorNotLikeNode@@UEAAXXZ` | `0x210F0` | 77 | UnwindData |  |
| 854 | `?Print@WmiOrNode@@UEAAXXZ` | `0x21150` | 278 | UnwindData |  |
| 855 | `?Print@WmiSignedIntegerNode@@UEAAXXZ` | `0x21270` | 64 | UnwindData |  |
| 856 | `?Print@WmiSignedIntegerRangeNode@@UEAAXXZ` | `0x212C0` | 209 | UnwindData |  |
| 857 | `?Print@WmiStringNode@@UEAAXXZ` | `0x213A0` | 64 | UnwindData |  |
| 858 | `?Print@WmiStringRangeNode@@UEAAXXZ` | `0x213F0` | 200 | UnwindData |  |
| 860 | `?Print@WmiUnsignedIntegerNode@@UEAAXXZ` | `0x214C0` | 64 | UnwindData |  |
| 861 | `?Print@WmiUnsignedIntegerRangeNode@@UEAAXXZ` | `0x21510` | 209 | UnwindData |  |
| 891 | `?Root@PartitionSet@@QEAAHXZ` | `0x21600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `?SetData@WmiTreeNode@@QEAAPEAXPEAX@Z` | `0x21620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `?SetIterator@WmiTreeNodeIterator@@QEAAPEAVWmiTreeNode@@PEAV2@@Z` | `0x21630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `?TransformAndOrExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@1@Z` | `0x21640` | 495 | UnwindData |  |
| 929 | `?TransformIntersectingRange@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@1@Z` | `0x21840` | 58 | UnwindData |  |
| 931 | `?TransformNotAndExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x21880` | 473 | UnwindData |  |
| 932 | `?TransformNotEqualExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x21A60` | 435 | UnwindData |  |
| 933 | `?TransformNotNotExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x21C20` | 166 | UnwindData |  |
| 934 | `?TransformNotOperatorEqualExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x21CD0` | 214 | UnwindData |  |
| 935 | `?TransformNotOperatorEqualOrGreaterExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x21DB0` | 214 | UnwindData |  |
| 937 | `?TransformNotOperatorGreaterExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x21DB0` | 214 | UnwindData |  |
| 936 | `?TransformNotOperatorEqualOrLessExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x21E90` | 214 | UnwindData |  |
| 939 | `?TransformNotOperatorLessExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x21E90` | 214 | UnwindData |  |
| 938 | `?TransformNotOperatorIsAExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x21F70` | 214 | UnwindData |  |
| 940 | `?TransformNotOperatorLikeExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x22050` | 214 | UnwindData |  |
| 941 | `?TransformNotOperatorNotEqualExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x22130` | 214 | UnwindData |  |
| 942 | `?TransformNotOperatorNotIsAExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x22210` | 214 | UnwindData |  |
| 943 | `?TransformNotOperatorNotLikeExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x222F0` | 214 | UnwindData |  |
| 944 | `?TransformNotOrExpression@QueryPreprocessor@@IEAAXAEAPEAVWmiTreeNode@@PEAV2@@Z` | `0x223D0` | 473 | UnwindData |  |
| 952 | `?UpperBound@WmiSignedIntegerRangeNode@@QEAAJXZ` | `0x225B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 954 | `?UpperBound@WmiUnsignedIntegerRangeNode@@QEAAKXZ` | `0x225B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `?Copy@WmiTreeNode@@UEAAPEAV1@XZ` | `0x225C0` | 176 | UnwindData |  |
| 597 | `?CopyNode@WmiTreeNode@@UEAAPEAV1@XZ` | `0x22680` | 94 | UnwindData |  |
| 489 | `??_7WmiRangeNode@@6B@` | `0x26008` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `??_7WmiTreeNode@@6B@` | `0x26030` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 497 | `??_7WmiUnsignedIntegerRangeNode@@6B@` | `0x26058` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 492 | `??_7WmiStringNode@@6B@` | `0x26080` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `??_7WmiValueNode@@6B@` | `0x260A8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `??_7PartitionSet@@6B@` | `0x260D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `??_7WmiStringRangeNode@@6B@` | `0x260E0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `??_7WmiAndNode@@6B@` | `0x26108` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 477 | `??_7WmiOperatorEqualNode@@6B@` | `0x26130` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `??_7QueryPreprocessor@@6B@` | `0x26160` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | `??_7WmiUnsignedIntegerNode@@6B@` | `0x26188` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 479 | `??_7WmiOperatorEqualOrLessNode@@6B@` | `0x261B8` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 478 | `??_7WmiOperatorEqualOrGreaterNode@@6B@` | `0x261E8` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `??_7WmiOperatorNode@@6B@` | `0x26218` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 480 | `??_7WmiOperatorGreaterNode@@6B@` | `0x26268` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `??_7WmiSignedIntegerRangeNode@@6B@` | `0x26298` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `??_7ProvEventObject@@6B@` | `0x262E0` | 136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `??_7ProvUDPAddressType@@6B@` | `0x26368` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `??_7ProvUDPAddressType@@6BProvPositiveRangedType@@@` | `0x26378` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `??_7ProvUDPAddressType@@6BProvInstanceType@@@` | `0x26390` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `??_7ProvOSIAddressType@@6BProvPositiveRangedType@@@` | `0x263E0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `??_7ProvOSIAddressType@@6BProvInstanceType@@@` | `0x263F8` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `??_7ProvDateTimeType@@6BProvPositiveRangedType@@@` | `0x26448` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `??_7ProvDateTimeType@@6BProvInstanceType@@@` | `0x26460` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `??_7ProvBitStringType@@6BProvPositiveRangedType@@@` | `0x264B0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `??_7ProvBitStringType@@6BProvInstanceType@@@` | `0x264C8` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `??_7ProvRowStatusType@@6BProvNegativeRangedType@@@` | `0x26518` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `??_7ProvRowStatusType@@6BProvInstanceType@@@` | `0x26530` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `??_7ProvEnumeratedType@@6BProvNegativeRangedType@@@` | `0x26580` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `??_7ProvEnumeratedType@@6BProvInstanceType@@@` | `0x26598` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `??_7ProvFixedLengthDisplayStringType@@6B@` | `0x265E8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `??_7ProvFixedLengthDisplayStringType@@6BProvPositiveRangedType@@@` | `0x265F8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `??_7ProvFixedLengthDisplayStringType@@6BProvInstanceType@@@` | `0x26610` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `??_7ProvDisplayStringType@@6BProvPositiveRangedType@@@` | `0x26660` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `??_7ProvDisplayStringType@@6BProvInstanceType@@@` | `0x26678` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `??_7ProvFixedLengthPhysAddressType@@6B@` | `0x266C8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `??_7ProvFixedLengthPhysAddressType@@6BProvPositiveRangedType@@@` | `0x266D8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `??_7ProvFixedLengthPhysAddressType@@6BProvInstanceType@@@` | `0x266F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 460 | `??_7ProvPhysAddressType@@6BProvPositiveRangedType@@@` | `0x26740` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `??_7ProvPhysAddressType@@6BProvInstanceType@@@` | `0x26758` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `??_7ProvMacAddressType@@6B@` | `0x267A8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `??_7ProvMacAddressType@@6BProvPositiveRangedType@@@` | `0x267B8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `??_7ProvMacAddressType@@6BProvInstanceType@@@` | `0x267D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `??_7ProvFixedLengthOctetStringType@@6B@` | `0x26820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `??_7ProvFixedLengthOctetStringType@@6BProvPositiveRangedType@@@` | `0x26830` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 424 | `??_7ProvFixedLengthOctetStringType@@6BProvInstanceType@@@` | `0x26848` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `??_7ProvOctetStringType@@6BProvPositiveRangedType@@@` | `0x26898` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `??_7ProvOctetStringType@@6BProvInstanceType@@@` | `0x268B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `??_7ProvFixedLengthOpaqueType@@6B@` | `0x26900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 428 | `??_7ProvFixedLengthOpaqueType@@6BProvPositiveRangedType@@@` | `0x26910` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `??_7ProvFixedLengthOpaqueType@@6BProvInstanceType@@@` | `0x26928` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `??_7ProvOpaqueType@@6BProvPositiveRangedType@@@` | `0x26978` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `??_7ProvOpaqueType@@6BProvInstanceType@@@` | `0x26990` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `??_7ProvObjectIdentifierType@@6B@` | `0x269E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `??_7ProvNetworkAddressType@@6B@` | `0x26A30` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 441 | `??_7ProvIpAddressType@@6B@` | `0x26A80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `??_7ProvCounter64Type@@6B@` | `0x26AD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `??_7ProvCounterType@@6B@` | `0x26B20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `??_7ProvTimeTicksType@@6B@` | `0x26B70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 435 | `??_7ProvGaugeType@@6BProvPositiveRangedType@@@` | `0x26BC0` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 434 | `??_7ProvGaugeType@@6BProvInstanceType@@@` | `0x26BD8` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 439 | `??_7ProvIntegerType@@6BProvNegativeRangedType@@@` | `0x26C28` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `??_7ProvIntegerType@@6BProvInstanceType@@@` | `0x26C40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `??_7ProvNullType@@6B@` | `0x26C90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `??_7ProvPositiveRangedType@@6B@` | `0x26CE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | `??_7ProvInstanceType@@6B@` | `0x26D10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `??_7ProvFixedType@@6B@` | `0x26D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 461 | `??_7ProvPositiveRangeType@@6B@` | `0x26D70` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `??_7ProvNegativeRangeType@@6B@` | `0x26D88` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `??_7ProvAnalyser@@6B@` | `0x26DA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `??_7ProvCounter64@@6B@` | `0x26DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 470 | `??_7ProvUInteger32@@6B@` | `0x26DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `??_7ProvIpAddress@@6B@` | `0x26E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `??_7ProvOpaque@@6B@` | `0x26E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `??_7ProvTimeTicks@@6B@` | `0x26E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `??_7ProvCounter@@6B@` | `0x26E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `??_7ProvGauge@@6B@` | `0x26E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `??_7ProvInteger@@6B@` | `0x26EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `??_7ProvNull@@6B@` | `0x26ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `??_7ProvValue@@6B@` | `0x26EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `??_7ProvObjectIdentifier@@6B@` | `0x26F10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `??_7ProvOctetString@@6B@` | `0x26F50` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 476 | `??_7WmiNullRangeNode@@6B@` | `0x26F88` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `??_7WmiNullNode@@6B@` | `0x26FB0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 490 | `??_7WmiSignedIntegerNode@@6B@` | `0x26FD8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 486 | `??_7WmiOperatorNotIsANode@@6B@` | `0x27000` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 481 | `??_7WmiOperatorIsANode@@6B@` | `0x27030` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 487 | `??_7WmiOperatorNotLikeNode@@6B@` | `0x27060` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `??_7WmiOperatorLikeNode@@6B@` | `0x27090` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `??_7WmiOperatorLessNode@@6B@` | `0x270C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `??_7WmiOperatorNotEqualNode@@6B@` | `0x270F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `??_7WmiNotNode@@6B@` | `0x27120` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 488 | `??_7WmiOrNode@@6B@` | `0x27148` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `??_7WmiTreeNodeIterator@@6B@` | `0x27170` | 93,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 963 | `?s_ProvDebugLog@ProvDebugLog@@2PEAV1@EA` | `0x3E000` | 4,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 965 | `?s_aLogs@ProvDebugLog@@2PAV1@A` | `0x3F190` | 1,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 964 | `?s_ReferenceCount@ProvDebugLog@@2JA` | `0x3F748` | 0 | Indeterminate |  |
