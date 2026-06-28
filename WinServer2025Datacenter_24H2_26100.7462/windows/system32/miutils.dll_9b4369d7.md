# Binary Specification: miutils.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\miutils.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9b4369d7bd191b2988a379e2238fe8d6cdc2f79ae3fd50e335ddf05900720fbf`
* **Total Exported Functions:** 148

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 126 | `SetProperties` | `0x1050` | 46 | UnwindData |  |
| 51 | `InstanceToWMIExtendedStatus` | `0x10E0` | 1,524 | UnwindData |  |
| 15 | `?CreateInstance@StaticSchema@@UEAAJPEBGPEAUIWbemClassObject@@KPEBU_MI_PropertySet@@_NAEAPEAU_MI_Instance@@PEAUIConversionContext@@@Z` | `0x1810` | 207 | UnwindData |  |
| 77 | `ParametersToWMIObject` | `0x1C90` | 1,256 | UnwindData |  |
| 23 | `?GetWmiIWbemServices@WMISchema@@UEAAJPEBGAEAV?$CComPtr@UIWbemServices@@@ATL@@@Z` | `0x2180` | 505 | UnwindData |  |
| 47 | `GetCorrelationId` | `0x2380` | 38 | UnwindData |  |
| 21 | `?GetNoneCachedWmiClass@WMISchema@@UEAAJPEBGPEAUIWbemServices@@AEAV?$CComPtr@UIWbemClassObject@@@ATL@@PEAUIConversionContext@@@Z` | `0x26A0` | 231 | UnwindData |  |
| 49 | `GetReferenceFromWMIObjectPath` | `0x2790` | 2,319 | UnwindData |  |
| 129 | `TypeToCimType` | `0x3180` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `ValueClear` | `0x3510` | 276 | UnwindData |  |
| 75 | `OptionsValueToContextValue` | `0x37E0` | 165 | UnwindData |  |
| 83 | `PublishProviderResult` | `0x3980` | 592 | UnwindData |  |
| 1 | `??0CAutoSetActivityId@@QEAA@XZ` | `0x3BE0` | 121 | UnwindData |  |
| 82 | `PublishDebugMessage` | `0x3C60` | 1,099 | UnwindData |  |
| 131 | `ValueToVariant` | `0x4370` | 40 | UnwindData |  |
| 52 | `InstanceToWMIObject` | `0x4690` | 40 | UnwindData |  |
| 106 | `ResultToHRESULT` | `0x63B0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `VariantToValue` | `0x6500` | 57 | UnwindData |  |
| 30 | `CimTypeToType` | `0x8960` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `RCClass_AddElementQualifierArrayItem` | `0x8CA0` | 33 | UnwindData |  |
| 69 | `OSC_Batch_Strdup` | `0x8E70` | 143 | UnwindData |  |
| 98 | `RCClass_AddMethodParameterQualifier` | `0x8FD0` | 108 | UnwindData |  |
| 93 | `RCClass_AddElementQualifier` | `0x9AE0` | 97 | UnwindData |  |
| 68 | `OSC_Batch_Get` | `0x9E80` | 64 | UnwindData |  |
| 35 | `Class_New` | `0xA0A0` | 388 | UnwindData |  |
| 59 | `Instance_New` | `0xA230` | 156 | UnwindData |  |
| 63 | `Instance_SetServerName` | `0xBE80` | 165 | UnwindData |  |
| 20 | `?GetMiClass@StaticSchema@@UEAAJPEBG00PEAPEBU_MI_Class@@@Z` | `0xC490` | 409 | UnwindData |  |
| 94 | `RCClass_AddElementQualifierArray` | `0xC630` | 185 | UnwindData |  |
| 13 | `?CreateInstance@DynamicSchema@@UEAAJPEBGPEAUIWbemClassObject@@KPEBU_MI_PropertySet@@_NAEAPEAU_MI_Instance@@PEAUIConversionContext@@@Z` | `0xC6F0` | 686 | UnwindData |  |
| 31 | `ClassCache_AddClass` | `0xD3D0` | 562 | UnwindData |  |
| 22 | `?GetWmiClass@WMISchema@@UEAAJPEBG0AEAV?$CComPtr@UIWbemClassObject@@@ATL@@PEAUIConversionContext@@@Z` | `0xDD40` | 1,356 | UnwindData |  |
| 33 | `ClassCache_GetClass` | `0xE2A0` | 636 | UnwindData |  |
| 105 | `ResultFromHRESULT` | `0xE590` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `ClassCache_Delete` | `0xE740` | 60 | UnwindData |  |
| 10 | `??1WMISchema@@UEAA@XZ` | `0xE7C0` | 79 | UnwindData |  |
| 108 | `RtlInitializeCachedFastLock` | `0xE900` | 323 | UnwindData |  |
| 107 | `RtlDeleteCachedFastLock` | `0xEAB0` | 144 | UnwindData |  |
| 111 | `RtlQueueAcquireCachedFastLockExclusive` | `0xEB50` | 103 | UnwindData |  |
| 120 | `RtlTryAcquireFastLockExclusive` | `0xEDB0` | 111 | UnwindData |  |
| 7 | `??0WMISchema@@QEAA@_N@Z` | `0xFA80` | 46 | UnwindData |  |
| 56 | `Instance_InitDynamic` | `0xFDB0` | 113 | UnwindData |  |
| 16 | `?DeInitialize@WMISchema@@QEAAJXZ` | `0x10050` | 56 | UnwindData |  |
| 115 | `RtlReleaseCachedFastLockExclusive` | `0x10090` | 29 | UnwindData |  |
| 117 | `RtlReleaseFastLockExclusive` | `0x100C0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `RtlInterlockedWakeAll` | `0x10250` | 52 | UnwindData |  |
| 109 | `RtlInterlockedCompareWait` | `0x102F0` | 171 | UnwindData |  |
| 67 | `OSC_Batch_Destroy` | `0x11570` | 29 | UnwindData |  |
| 27 | `CimErrorFromErrorCode` | `0x116A0` | 143 | UnwindData |  |
| 66 | `MiErrorCategoryFromWindowsError` | `0x11740` | 183 | UnwindData |  |
| 43 | `DestinationOptions_MigrateOptions` | `0x11AF0` | 655 | UnwindData |  |
| 141 | `XMLDOM_Parse` | `0x11D90` | 1,139 | UnwindData |  |
| 144 | `XML_Next` | `0x12210` | 525 | UnwindData |  |
| 54 | `Instance_Construct` | `0x13C30` | 445 | UnwindData |  |
| 44 | `FindClassDecl` | `0x140F0` | 122 | UnwindData |  |
| 136 | `WMIObjectToClass` | `0x14530` | 75 | UnwindData |  |
| 96 | `RCClass_AddMethod` | `0x14A00` | 543 | UnwindData |  |
| 90 | `RCClass_AddElement` | `0x15710` | 133 | UnwindData |  |
| 97 | `RCClass_AddMethodParameter` | `0x15A70` | 675 | UnwindData |  |
| 104 | `RCClass_New` | `0x16170` | 1,535 | UnwindData |  |
| 41 | `DestinationOptions_Create` | `0x16E20` | 275 | UnwindData |  |
| 74 | `OperationOptions_MigrateOptions` | `0x16F40` | 390 | UnwindData |  |
| 73 | `OperationOptions_Create` | `0x17B20` | 218 | UnwindData |  |
| 71 | `OSC_Type_GetSize` | `0x180A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `WMIQualifierFlavorToMI` | `0x180C0` | 89 | UnwindData |  |
| 80 | `PublishClientOperationInfo` | `0x18210` | 77 | UnwindData |  |
| 119 | `RtlTryAcquireCachedFastLockShared` | `0x184D0` | 134 | UnwindData |  |
| 76 | `Options_FindValue` | `0x18560` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `CreateConversionContext` | `0x18660` | 162 | UnwindData |  |
| 39 | `Config_GetRegString` | `0x187A0` | 327 | UnwindData |  |
| 38 | `Config_GetProtocolHandlerDetails` | `0x188F0` | 468 | UnwindData |  |
| 116 | `RtlReleaseCachedFastLockShared` | `0x196E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `WMIExtendedObjectToInstance` | `0x19720` | 829 | UnwindData |  |
| 137 | `WMIObjectToInstance` | `0x19CF0` | 676 | UnwindData |  |
| 102 | `RCClass_AddMethodQualifierArray` | `0x19FA0` | 185 | UnwindData |  |
| 101 | `RCClass_AddMethodQualifier` | `0x1A060` | 97 | UnwindData |  |
| 88 | `RCClass_AddClassQualifierArray` | `0x1A340` | 156 | UnwindData |  |
| 87 | `RCClass_AddClassQualifier` | `0x1A3F0` | 80 | UnwindData |  |
| 72 | `OperationOptions_CopyOptions` | `0x1A710` | 243 | UnwindData |  |
| 103 | `RCClass_AddMethodQualifierArrayItem` | `0x1AE90` | 96 | UnwindData |  |
| 113 | `RtlQueueAcquireFastLockExclusive` | `0x1B1B0` | 689 | UnwindData |  |
| 8 | `??1CAutoSetActivityId@@QEAA@XZ` | `0x1B520` | 38 | UnwindData |  |
| 46 | `FindQualifierInWMIObject` | `0x1B5C0` | 159 | UnwindData |  |
| 70 | `OSC_StringToMiValue` | `0x1BBD0` | 594 | UnwindData |  |
| 5 | `??0StaticSchema@@QEAA@XZ` | `0x1C8A0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0DynamicSchema@@QEAA@XZ` | `0x1C980` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `RCClass_AddMethodParameterQualifierArray` | `0x1CA70` | 211 | UnwindData |  |
| 100 | `RCClass_AddMethodParameterQualifierArrayItem` | `0x1CC00` | 113 | UnwindData |  |
| 122 | `RtlpInitFastLock` | `0x1CC80` | 174 | UnwindData |  |
| 24 | `?Initialize@StaticSchema@@QEAAJPEBU_MI_Module@@@Z` | `0x1CD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `?GetMiClass@DynamicSchema@@UEAAJPEBG00PEAPEBU_MI_Class@@@Z` | `0x1CD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `Instance_GetResourceURI` | `0x1CD60` | 76 | UnwindData |  |
| 34 | `ClassCache_New` | `0x1D390` | 110 | UnwindData |  |
| 124 | `SetCorrelationIdToWbemContext` | `0x1D410` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `GetMethodParameters` | `0x1D6C0` | 385 | UnwindData |  |
| 65 | `MI_Hash` | `0x1D850` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `Instance_IsDynamic` | `0x1D910` | 22 | UnwindData |  |
| 62 | `Instance_SetResourceURI` | `0x1D930` | 247 | UnwindData |  |
| 42 | `DestinationOptions_Duplicate` | `0x1DB00` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0WMISchema@@QEAA@XZ` | `0x1DCD0` | 48 | UnwindData |  |
| 50 | `InstanceToWMIEvent` | `0x1DEC0` | 186 | UnwindData |  |
| 147 | `XML_SetText` | `0x1E190` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `XML_Init` | `0x1E360` | 37 | UnwindData |  |
| 2 | `??0CCritSec@@QEAA@XZ` | `0x1E3B0` | 31 | UnwindData |  |
| 125 | `SetModifiedPropertyNamesToContext` | `0x1E460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `?CreateInstance@IndicationSchema@@UEAAJPEBGPEAUIWbemClassObject@@KPEBU_MI_PropertySet@@_NAEAPEAU_MI_Instance@@PEAUIConversionContext@@@Z` | `0x1E470` | 264 | UnwindData |  |
| 89 | `RCClass_AddClassQualifierArrayItem` | `0x1E620` | 88 | UnwindData |  |
| 19 | `?GetMiClass@IndicationSchema@@UEAAJPEBG00PEAPEBU_MI_Class@@@Z` | `0x1E960` | 189 | UnwindData |  |
| 121 | `RtlTryAcquireFastLockShared` | `0x1EB70` | 139 | UnwindData |  |
| 45 | `FindMethodDecl` | `0x1ED30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??1CCritSec@@QEAA@XZ` | `0x1ED40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `Instance_MatchKeys` | `0x1ED60` | 4,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `RtlQueueAcquireCachedFastLockShared` | `0x1FD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `RtlQueueAcquireFastLockShared` | `0x1FD30` | 808 | UnwindData |  |
| 118 | `RtlReleaseFastLockShared` | `0x20060` | 51 | UnwindData |  |
| 123 | `RtlpReleaseIdleSlots` | `0x200A0` | 52 | UnwindData |  |
| 28 | `CimError_Construct` | `0x20200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `Instance_Clone` | `0x20220` | 115 | UnwindData |  |
| 60 | `Instance_SetElementArray` | `0x202A0` | 305 | UnwindData |  |
| 61 | `Instance_SetElementArrayItem` | `0x203E0` | 129 | UnwindData |  |
| 91 | `RCClass_AddElementArray` | `0x20610` | 231 | UnwindData |  |
| 92 | `RCClass_AddElementArrayItem` | `0x20700` | 88 | UnwindData |  |
| 78 | `PropertySet_New` | `0x20A70` | 117 | UnwindData |  |
| 142 | `XML_FormatError` | `0x20AF0` | 65 | UnwindData |  |
| 145 | `XML_PutError` | `0x20B40` | 71 | UnwindData |  |
| 146 | `XML_RegisterNameSpace` | `0x20B90` | 123 | UnwindData |  |
| 148 | `XML_StripWhitespace` | `0x20C20` | 117 | UnwindData |  |
| 140 | `XMLDOM_Free` | `0x21260` | 24 | UnwindData |  |
| 11 | `??4CAutoSetActivityId@@QEAAAEAV0@AEBV0@@Z` | `0x21360` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??4CCritSec@@QEAAAEAV0@AEBV0@@Z` | `0x213E0` | 9,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `CompareInstance` | `0x23870` | 525 | UnwindData |  |
| 37 | `CompareValue` | `0x23A90` | 1,654 | UnwindData |  |
| 79 | `PropertyToVariant` | `0x24110` | 2,010 | UnwindData |  |
| 86 | `QualifierFlavorToWMI` | `0x248F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `VariantArrayToSafeArray` | `0x24920` | 788 | UnwindData |  |
| 4 | `??0IndicationSchema@@QEAA@XZ` | `0x24F20` | 2,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `?GetFlags@MiSchema@@UEBAJXZ` | `0x257B0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?Initialize@WMISchema@@QEAAX_N@Z` | `0x258A0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?SetFlags@MiSchema@@MEAAJJ@Z` | `0x25980` | 4,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `IsLifeCycleIndicationQuery` | `0x26A80` | 1,257 | UnwindData |  |
| 134 | `WMIEventToCIMIndication` | `0x26F70` | 385 | UnwindData |  |
| 127 | `SubscriptionDeliveryOptions_Create` | `0x27CE0` | 83 | UnwindData |  |
| 128 | `SubscriptionDeliveryOptions_MigrateOptions` | `0x27D40` | 397 | UnwindData |  |
| 81 | `PublishDebugInfo` | `0x283C0` | 120 | UnwindData |  |
| 84 | `PublishProviderWriteError` | `0x28440` | 78 | UnwindData |  |
| 85 | `PublishProviderWriteMessage` | `0x284A0` | 48 | UnwindData |  |
| 139 | `WriteWBEM_MC_CLIENT_REQUEST_FAILURE` | `0x284E0` | 196 | UnwindData |  |
| 29 | `CimStatusCodeFromWindowsError` | `0x285B0` | 146 | UnwindData |  |
