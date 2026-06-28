# Binary Specification: ntdll.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ntdll.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9e35cbb412da1af9c01180a942989e0b45d6a40375052535e3631a473a53c3e4`
* **Total Exported Functions:** 2517

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 827 | `RtlComputePrivatizedDllName_U` | `0x1230` | 956 | UnwindData |  |
| 1495 | `RtlSetCurrentDirectory_U` | `0x1600` | 552 | UnwindData |  |
| 1077 | `RtlGetCurrentDirectory_U` | `0x19A0` | 54 | UnwindData |  |
| 960 | `RtlDosSearchPath_Ustr` | `0x2810` | 2,336 | UnwindData |  |
| 1446 | `RtlReleaseRelativeName` | `0x3180` | 90 | UnwindData |  |
| 1100 | `RtlGetFullPathName_UstrEx` | `0x31E0` | 839 | UnwindData |  |
| 764 | `RtlAppendUnicodeStringToString` | `0x4400` | 54 | UnwindData |  |
| 820 | `RtlCompareString` | `0x7090` | 203 | UnwindData |  |
| 133 | `LdrGetDllHandleByName` | `0x71A0` | 162 | UnwindData |  |
| 1634 | `RtlUpperChar` | `0x74F0` | 30 | UnwindData |  |
| 1208 | `RtlInsertElementGenericTableFullAvl` | `0x80E0` | 340 | UnwindData |  |
| 917 | `RtlDeleteElementGenericTableAvl` | `0x8740` | 220 | UnwindData |  |
| 1206 | `RtlInsertElementGenericTableAvl` | `0x8830` | 534 | UnwindData |  |
| 1308 | `RtlLookupElementGenericTableFullAvl` | `0x8B40` | 242 | UnwindData |  |
| 1306 | `RtlLookupElementGenericTableAvl` | `0x8C40` | 43 | UnwindData |  |
| 822 | `RtlCompareUnicodeStrings` | `0x9150` | 338 | UnwindData |  |
| 918 | `RtlDeleteElementGenericTableAvlEx` | `0x92B0` | 85 | UnwindData |  |
| 8 | *Ordinal Only* | `0x9970` | 167 | UnwindData |  |
| 899 | `RtlDeactivateActivationContext` | `0xA020` | 67 | UnwindData |  |
| 720 | `RtlActivateActivationContextUnsafeFast` | `0xA5D0` | 351 | UnwindData |  |
| 1417 | `RtlRaiseException` | `0xA740` | 639 | UnwindData |  |
| 1549 | `RtlSleepConditionVariableCS` | `0xC1C0` | 575 | UnwindData |  |
| 977 | `RtlEnterCriticalSection` | `0xD780` | 244 | UnwindData |  |
| 1282 | `RtlLeaveCriticalSection` | `0xD880` | 777 | UnwindData |  |
| 1720 | `RtlpNotOwnerCriticalSection` | `0xDB90` | 211 | UnwindData |  |
| 1420 | `RtlRaiseStatus` | `0xDC70` | 107 | UnwindData |  |
| 1312 | `RtlLookupFunctionTable` | `0xDF10` | 131 | UnwindData |  |
| 1311 | `RtlLookupFunctionEntry` | `0xDFA0` | 160 | UnwindData |  |
| 1622 | `RtlUnwindEx` | `0xE310` | 2,711 | UnwindData |  |
| 1650 | `RtlVirtualUnwind2` | `0xEDB0` | 50 | UnwindData |  |
| 1649 | `RtlVirtualUnwind` | `0x11AB0` | 422 | UnwindData |  |
| 1292 | `RtlLocateExtendedFeature` | `0x11D90` | 345 | UnwindData |  |
| 902 | `RtlDecodePointer` | `0x132D0` | 108 | UnwindData |  |
| 130 | `LdrGetDllFullName` | `0x13350` | 252 | UnwindData |  |
| 1380 | `RtlQueryInformationActivationContext` | `0x13A60` | 1,904 | UnwindData |  |
| 185 | `LdrUnloadDll` | `0x14540` | 22 | UnwindData |  |
| 1586 | `RtlTryAcquireSRWLockExclusive` | `0x147E0` | 112 | UnwindData |  |
| 1761 | `TpAllocWork` | `0x14CE0` | 378 | UnwindData |  |
| 131 | `LdrGetDllHandle` | `0x154B0` | 471 | UnwindData |  |
| 134 | `LdrGetDllHandleEx` | `0x15690` | 587 | UnwindData |  |
| 1318 | `RtlMultiByteToUnicodeN` | `0x16E00` | 15 | UnwindData |  |
| 895 | `RtlCustomCPToUnicodeN` | `0x16FB0` | 192 | UnwindData |  |
| 1591 | `RtlUTF8ToUnicodeN` | `0x17120` | 57 | UnwindData |  |
| 760 | `RtlAnsiStringToUnicodeString` | `0x17C90` | 856 | UnwindData |  |
| 900 | `RtlDeactivateActivationContextUnsafeFast` | `0x1A2A0` | 251 | UnwindData |  |
| 717 | `RtlAcquireSRWLockShared` | `0x1AF50` | 85 | UnwindData |  |
| 1449 | `RtlReleaseSRWLockShared` | `0x1AFB0` | 300 | UnwindData |  |
| 1770 | `TpCallbackSendAlpcMessageOnCompletion` | `0x1C0D0` | 98 | UnwindData |  |
| 754 | `RtlAllocateHeap` | `0x1C1D0` | 2,846 | UnwindData |  |
| 1589 | `RtlTryEnterCriticalSection` | `0x23800` | 216 | UnwindData |  |
| 45 | `DbgPrint` | `0x24560` | 66 | UnwindData |  |
| 1518 | `RtlSetProcessPreferredUILanguages` | `0x25BA0` | 52 | UnwindData |  |
| 1279 | `RtlLCIDToCultureName` | `0x274D0` | 683 | UnwindData |  |
| 1304 | `RtlLookupAtomInAtomTable` | `0x27AE0` | 913 | UnwindData |  |
| 1599 | `RtlUnicodeStringToInteger` | `0x27E80` | 537 | UnwindData |  |
| 1291 | `RtlLocaleNameToLcid` | `0x280A0` | 337 | UnwindData |  |
| 894 | `RtlCultureNameToLCID` | `0x28200` | 199 | UnwindData |  |
| 1349 | `RtlOpenCurrentUser` | `0x29720` | 285 | UnwindData |  |
| 1142 | `RtlGetThreadPreferredUILanguages` | `0x29850` | 3,637 | UnwindData |  |
| 722 | `RtlAddAccessAllowedAceEx` | `0x2A690` | 118 | UnwindData |  |
| 728 | `RtlAddAce` | `0x2AE50` | 397 | UnwindData |  |
| 1288 | `RtlLengthSidAsUnicodeString` | `0x2AFF0` | 91 | UnwindData |  |
| 1047 | `RtlFormatCurrentUserKeyPath` | `0x2B300` | 85 | UnwindData |  |
| 721 | `RtlAddAccessAllowedAce` | `0x2B4E0` | 104 | UnwindData |  |
| 839 | `RtlConvertSidToUnicodeString` | `0x2B780` | 71 | UnwindData |  |
| 1642 | `RtlValidSid` | `0x2BB60` | 44 | UnwindData |  |
| 1638 | `RtlValidAcl` | `0x2BBA0` | 453 | UnwindData |  |
| 1641 | `RtlValidSecurityDescriptor` | `0x2BE60` | 251 | UnwindData |  |
| 799 | `RtlCheckTokenMembershipEx` | `0x2C030` | 177 | UnwindData |  |
| 1204 | `RtlInitializeSidEx` | `0x2C5B0` | 107 | UnwindData |  |
| 1285 | `RtlLengthRequiredSid` | `0x2C8B0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 739 | `RtlAddMandatoryAce` | `0x2C9B0` | 425 | UnwindData |  |
| 852 | `RtlCopySid` | `0x2CB60` | 55 | UnwindData |  |
| 1325 | `RtlNewSecurityObjectEx` | `0x2CBE0` | 100 | UnwindData |  |
| 989 | `RtlEqualPrefixSid` | `0x31570` | 237 | UnwindData |  |
| 908 | `RtlDefaultNpAcl` | `0x31990` | 1,014 | UnwindData |  |
| 858 | `RtlCreateAcl` | `0x31D90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 860 | `RtlCreateAndSetSD` | `0x31DD0` | 937 | UnwindData |  |
| 1513 | `RtlSetOwnerSecurityDescriptor` | `0x32180` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `RtlSetGroupSecurityDescriptor` | `0x321D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1521 | `RtlSetSaclSecurityDescriptor` | `0x32220` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | `RtlDeleteBoundaryDescriptor` | `0x32410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1493 | `RtlSetControlSecurityDescriptor` | `0x32430` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `RtlCreateSystemVolumeInformationFolder` | `0x32480` | 726 | UnwindData |  |
| 1065 | `RtlGetAce` | `0x32AE0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `RtlAbsoluteToSelfRelativeSD` | `0x32B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `RtlMakeSelfRelativeSD` | `0x32B50` | 80 | UnwindData |  |
| 1484 | `RtlSelfRelativeToAbsoluteSD2` | `0x32DB0` | 513 | UnwindData |  |
| 1038 | `RtlFlsAllocEx` | `0x33180` | 50 | UnwindData |  |
| 1575 | `RtlTlsFree` | `0x33640` | 192 | UnwindData |  |
| 805 | `RtlClearBits` | `0x33710` | 10 | UnwindData |  |
| 1574 | `RtlTlsAlloc` | `0x33F40` | 545 | UnwindData |  |
| 1037 | `RtlFlsAlloc` | `0x34240` | 33 | UnwindData |  |
| 1042 | `RtlFlsSetValue` | `0x34EC0` | 61 | UnwindData |  |
| 1576 | `RtlTlsSetValue` | `0x35210` | 154 | UnwindData |  |
| 1424 | `RtlRbRemoveNode` | `0x38450` | 40 | UnwindData |  |
| 1423 | `RtlRbInsertNodeEx` | `0x3B560` | 134 | UnwindData |  |
| 1081 | `RtlGetCurrentServiceSessionId` | `0x3C0D0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `RtlAcquireSRWLockExclusive` | `0x3C190` | 79 | UnwindData |  |
| 1448 | `RtlReleaseSRWLockExclusive` | `0x3CE60` | 167 | UnwindData |  |
| 1162 | `RtlImageNtHeaderEx` | `0x3F7A0` | 263 | UnwindData |  |
| 149 | `LdrLoadDll` | `0x3F8B0` | 313 | UnwindData |  |
| 1103 | `RtlGetImageFileMachines` | `0x3FB90` | 1,871 | UnwindData |  |
| 952 | `RtlDosApplyFileIsolationRedirection_Ustr` | `0x41870` | 47 | UnwindData |  |
| 1015 | `RtlFindActivationContextSectionString` | `0x44360` | 61 | UnwindData |  |
| 1441 | `RtlReleaseActivationContext` | `0x44B80` | 40 | UnwindData |  |
| 46 | `DbgPrintEx` | `0x45140` | 54 | UnwindData |  |
| 1014 | `RtlFindActivationContextSectionGuid` | `0x45180` | 82 | UnwindData |  |
| 172 | `LdrRscIsTypeExist` | `0x455B0` | 531 | UnwindData |  |
| 148 | `LdrLoadAlternateResourceModuleEx` | `0x465D0` | 5,455 | UnwindData |  |
| 184 | `LdrUnloadAlternateResourceModuleEx` | `0x47EB0` | 512 | UnwindData |  |
| 1027 | `RtlFindMessage` | `0x48300` | 276 | UnwindData |  |
| 113 | `LdrAddLoadAsDataTable` | `0x4A840` | 566 | UnwindData |  |
| 164 | `LdrRemoveLoadAsDataTable` | `0x4AA80` | 836 | UnwindData |  |
| 790 | `RtlCharToInteger` | `0x4AED0` | 454 | UnwindData |  |
| 748 | `RtlAddressInSectionTable` | `0x4B100` | 89 | UnwindData |  |
| 170 | `LdrResolveDelayLoadedAPI` | `0x4B7C0` | 666 | UnwindData |  |
| 1160 | `RtlImageDirectoryEntryToData` | `0x4C9E0` | 410 | UnwindData |  |
| 1468 | `RtlRestoreContext` | `0x4CE80` | 911 | UnwindData |  |
| 1153 | `RtlGuardCheckLongJumpTarget` | `0x4D290` | 462 | UnwindData |  |
| 117 | `LdrControlFlowGuardEnforced` | `0x4DCD0` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `RtlAddGrowableFunctionTable` | `0x4EBD0` | 73 | UnwindData |  |
| 777 | `RtlAvlInsertNodeEx` | `0x4EF40` | 34 | UnwindData |  |
| 1360 | `RtlProtectHeap` | `0x4F720` | 196 | UnwindData |  |
| 1491 | `RtlSetBits` | `0x4FCF0` | 10 | UnwindData |  |
| 1409 | `RtlQueryUnbiasedInterruptTime` | `0x530A0` | 12 | UnwindData |  |
| 1334 | `RtlNtStatusToDosErrorNoTeb` | `0x53150` | 54 | UnwindData |  |
| 1430 | `RtlReAllocateHeap` | `0x545A0` | 204 | UnwindData |  |
| 89 | `EtwRegisterTraceGuidsA` | `0x5E750` | 49 | UnwindData |  |
| 1511 | `RtlSetLastWin32ErrorAndNtStatusFromNtStatus` | `0x5E810` | 20 | UnwindData |  |
| 97 | `EtwUnregisterTraceGuids` | `0x5F130` | 71 | UnwindData |  |
| 90 | `EtwRegisterTraceGuidsW` | `0x5F180` | 103 | UnwindData |  |
| 71 | `EtwEventSetInformation` | `0x5F3A0` | 114 | UnwindData |  |
| 79 | `EtwEventWriteString` | `0x5F420` | 145 | UnwindData |  |
| 69 | `EtwEventProviderEnabled` | `0x5F8D0` | 204 | UnwindData |  |
| 70 | `EtwEventRegister` | `0x5FB20` | 20 | UnwindData |  |
| 85 | `EtwNotificationRegister` | `0x5FB70` | 528 | UnwindData |  |
| 86 | `EtwNotificationUnregister` | `0x60450` | 269 | UnwindData |  |
| 67 | `EtwEventActivityIdControl` | `0x60710` | 293 | UnwindData |  |
| 1469 | `RtlRestoreLastWin32Error` | `0x60840` | 72 | UnwindData |  |
| 1510 | `RtlSetLastWin32Error` | `0x60840` | 72 | UnwindData |  |
| 1333 | `RtlNtStatusToDosError` | `0x60890` | 400 | UnwindData |  |
| 65 | `EtwDeliverDataBlock` | `0x60E50` | 33 | UnwindData |  |
| 1587 | `RtlTryAcquireSRWLockShared` | `0x61510` | 373 | UnwindData |  |
| 95 | `EtwTraceMessage` | `0x61E70` | 231 | UnwindData |  |
| 96 | `EtwTraceMessageVa` | `0x61F60` | 228 | UnwindData |  |
| 92 | `EtwSendNotification` | `0x626F0` | 655 | UnwindData |  |
| 1657 | `RtlWakeAllConditionVariable` | `0x63110` | 54 | UnwindData |  |
| 87 | `EtwProcessPrivateLoggerRequest` | `0x640C0` | 44 | UnwindData |  |
| 1112 | `RtlGetMultiTimePrecise` | `0x65280` | 80 | UnwindData |  |
| 33 | `CsrCaptureMessageBuffer` | `0x65610` | 85 | UnwindData |  |
| 38 | `CsrClientConnectToServer` | `0x65A30` | 490 | UnwindData |  |
| 34 | `CsrCaptureMessageMultiUnicodeStringsInPlace` | `0x65CF0` | 285 | UnwindData |  |
| 35 | `CsrCaptureMessageString` | `0x65E20` | 17 | UnwindData |  |
| 31 | `CsrAllocateCaptureBuffer` | `0x65F60` | 200 | UnwindData |  |
| 39 | `CsrFreeCaptureBuffer` | `0x66030` | 36 | UnwindData |  |
| 37 | `CsrClientCallServer` | `0x66060` | 450 | UnwindData |  |
| 32 | `CsrAllocateMessagePointer` | `0x66230` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1200 | `RtlInitializeResource` | `0x66800` | 94 | UnwindData |  |
| 1192 | `RtlInitializeCriticalSectionEx` | `0x66C30` | 59 | UnwindData |  |
| 868 | `RtlCreateHeap` | `0x66E50` | 40 | UnwindData |  |
| 1401 | `RtlQueryResourcePolicy` | `0x69060` | 179 | UnwindData |  |
| 1563 | `RtlSwitchedVVI` | `0x69120` | 1,138 | UnwindData |  |
| 1748 | `SbSelectProcedure` | `0x69820` | 1,822 | UnwindData |  |
| 1151 | `RtlGetVersion` | `0x69F50` | 868 | UnwindData |  |
| 1118 | `RtlGetNtProductType` | `0x6A2C0` | 113 | UnwindData |  |
| 1133 | `RtlGetSuiteMask` | `0x6A340` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | `RtlConvertDeviceFamilyInfoToString` | `0x6A750` | 229 | UnwindData |  |
| 1706 | `RtlpGetDeviceFamilyInfoEnum` | `0x6A840` | 40 | UnwindData |  |
| 1792 | `TpReleaseWork` | `0x6AF10` | 353 | UnwindData |  |
| 1815 | `TpWaitForWork` | `0x6B080` | 104 | UnwindData |  |
| 1800 | `TpSetPoolThreadCpuSets` | `0x6B9A0` | 177 | UnwindData |  |
| 926 | `RtlDeleteTimer` | `0x6BB00` | 460 | UnwindData |  |
| 1808 | `TpTimerOutstandingCallbackCount` | `0x6BCE0` | 146 | UnwindData |  |
| 881 | `RtlCreateTimer` | `0x6BE20` | 672 | UnwindData |  |
| 1806 | `TpSimpleTryPost` | `0x6C360` | 368 | UnwindData |  |
| 1415 | `RtlQueueWorkItem` | `0x6C4E0` | 1,306 | UnwindData |  |
| 1440 | `RtlRegisterWait` | `0x6CA00` | 928 | UnwindData |  |
| 934 | `RtlDeregisterWaitEx` | `0x6CDB0` | 448 | UnwindData |  |
| 1791 | `TpReleaseWait` | `0x6CFC0` | 137 | UnwindData |  |
| 1760 | `TpAllocWait` | `0x6D2E0` | 110 | UnwindData |  |
| 1814 | `TpWaitForWait` | `0x6D630` | 91 | UnwindData |  |
| 1759 | `TpAllocTimer` | `0x6D7C0` | 102 | UnwindData |  |
| 1353 | `RtlPcToFileHeader` | `0x6DB60` | 102 | UnwindData |  |
| 114 | `LdrAddRefDll` | `0x6DDF0` | 27 | UnwindData |  |
| 1762 | `TpAlpcRegisterCompletionList` | `0x6EC60` | 138 | UnwindData |  |
| 1803 | `TpSetTimerEx` | `0x6EF50` | 129 | UnwindData |  |
| 1781 | `TpIsTimerSet` | `0x6F680` | 95 | UnwindData |  |
| 1782 | `TpPostWork` | `0x6F850` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1790 | `TpReleaseTimer` | `0x6F940` | 356 | UnwindData |  |
| 186 | `LdrUnlockLoaderLock` | `0x6FAB0` | 173 | UnwindData |  |
| 1813 | `TpWaitForTimer` | `0x70870` | 103 | UnwindData |  |
| 1807 | `TpStartAsyncIoOperation` | `0x719A0` | 79 | UnwindData |  |
| 1805 | `TpSetWaitEx` | `0x723D0` | 104 | UnwindData |  |
| 1767 | `TpCallbackMayRunLong` | `0x74330` | 73 | UnwindData |  |
| 1534 | `RtlSetThreadSubProcessTag` | `0x74450` | 243 | UnwindData |  |
| 175 | `LdrSetDllDirectory` | `0x783F0` | 104 | UnwindData |  |
| 1123 | `RtlGetPersistedStateLocation` | `0x78910` | 97 | UnwindData |  |
| 1053 | `RtlFreeHeap` | `0x78CE0` | 2,748 | UnwindData |  |
| 885 | `RtlCreateUnicodeString` | `0x7A340` | 129 | UnwindData |  |
| 1051 | `RtlFreeAnsiString` | `0x7B1F0` | 36 | UnwindData |  |
| 1059 | `RtlFreeUTF8String` | `0x7B1F0` | 36 | UnwindData |  |
| 1060 | `RtlFreeUnicodeString` | `0x7B1F0` | 36 | UnwindData |  |
| 1071 | `RtlGetAppContainerSidType` | `0x7C6D0` | 118 | UnwindData |  |
| 1069 | `RtlGetAppContainerNamedObjectPath` | `0x7C750` | 118 | UnwindData |  |
| 1070 | `RtlGetAppContainerParent` | `0x7CA00` | 215 | UnwindData |  |
| 1264 | `RtlIsParentOfChildAppContainer` | `0x7CAE0` | 110 | UnwindData |  |
| 990 | `RtlEqualSid` | `0x7CD70` | 51 | UnwindData |  |
| 1719 | `RtlpMuiRegLoadRegistryInfo` | `0x7D820` | 345 | UnwindData |  |
| 1718 | `RtlpMuiRegFreeRegistryInfo` | `0x7D980` | 32 | UnwindData |  |
| 1471 | `RtlRestoreThreadPreferredUILanguages` | `0x7DC50` | 218 | UnwindData |  |
| 800 | `RtlCleanUpTEBLangLists` | `0x7DDC0` | 196 | UnwindData |  |
| 1533 | `RtlSetThreadPreferredUILanguages2` | `0x7F110` | 414 | UnwindData |  |
| 1714 | `RtlpLoadUserUIByPolicy` | `0x7F2C0` | 548 | UnwindData |  |
| 1716 | `RtlpMuiFreeLangRegistryInfo` | `0x7F4F0` | 74 | UnwindData |  |
| 1137 | `RtlGetSystemPreferredUILanguages` | `0x7F9D0` | 1,343 | UnwindData |  |
| 1145 | `RtlGetUILanguageInfo` | `0x80930` | 156 | UnwindData |  |
| 1532 | `RtlSetThreadPreferredUILanguages` | `0x81B30` | 1,349 | UnwindData |  |
| 1703 | `RtlpCreateProcessRegistryInfo` | `0x82260` | 126 | UnwindData |  |
| 1727 | `RtlpQueryDefaultUILanguage` | `0x83DF0` | 7 | UnwindData |  |
| 785 | `RtlCapabilityCheck` | `0x84180` | 42 | UnwindData |  |
| 1388 | `RtlQueryPerformanceCounter` | `0x847B0` | 243 | UnwindData |  |
| 1476 | `RtlRunOnceBeginInitialize` | `0x848B0` | 62 | UnwindData |  |
| 935 | `RtlDeriveCapabilitySidsFromName` | `0x849B0` | 128 | UnwindData |  |
| 1256 | `RtlIsMultiSessionSku` | `0x84BD0` | 52 | UnwindData |  |
| 73 | `EtwEventWrite` | `0x84C10` | 160 | UnwindData |  |
| 80 | `EtwEventWriteTransfer` | `0x84F10` | 175 | UnwindData |  |
| 797 | `RtlCheckTokenCapability` | `0x86020` | 1,124 | UnwindData |  |
| 1242 | `RtlIsCapabilitySid` | `0x86490` | 66 | UnwindData |  |
| 789 | `RtlCaptureStackBackTrace` | `0x86890` | 147 | UnwindData |  |
| 1659 | `RtlWalkFrameChain` | `0x86930` | 61 | UnwindData |  |
| 1139 | `RtlGetSystemTimePrecise` | `0x87A90` | 385 | UnwindData |  |
| 1067 | `RtlGetActiveActivationContext` | `0x87C80` | 89 | UnwindData |  |
| 718 | `RtlActivateActivationContext` | `0x87DB0` | 39 | UnwindData |  |
| 719 | `RtlActivateActivationContextEx` | `0x87F20` | 84 | UnwindData |  |
| 741 | `RtlAddRefActivationContext` | `0x88610` | 3,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `RtlValidateHeap` | `0x892E0` | 535 | UnwindData |  |
| 1611 | `RtlUnlockHeap` | `0x89A00` | 335 | UnwindData |  |
| 1297 | `RtlLockHeap` | `0x89BF0` | 430 | UnwindData |  |
| 1548 | `RtlSizeHeap` | `0x8A1E0` | 64 | UnwindData |  |
| 1614 | `RtlUnlockMemoryZone` | `0x8BDC0` | 148 | UnwindData |  |
| 1612 | `RtlUnlockMemoryBlockLookaside` | `0x8BEA0` | 87 | UnwindData |  |
| 1298 | `RtlLockMemoryBlockLookaside` | `0x8BF00` | 117 | UnwindData |  |
| 1300 | `RtlLockMemoryZone` | `0x8BF80` | 274 | UnwindData |  |
| 1615 | `RtlUnlockModuleSection` | `0x8C200` | 162 | UnwindData |  |
| 1301 | `RtlLockModuleSection` | `0x8C2B0` | 298 | UnwindData |  |
| 122 | `LdrEnumerateLoadedModules` | `0x8C420` | 185 | UnwindData |  |
| 1636 | `RtlUserFiberStart` | `0x8C4E0` | 36 | UnwindData |  |
| 1637 | `RtlUserThreadStart` | `0x8C510` | 92 | UnwindData |  |
| 1001 | `RtlExitUserThread` | `0x8C580` | 88 | UnwindData |  |
| 1000 | `RtlExitUserProcess` | `0x8C5E0` | 224 | UnwindData |  |
| 1776 | `TpCheckTerminateWorker` | `0x8C6D0` | 138 | UnwindData |  |
| 180 | `LdrShutdownThread` | `0x8C8A0` | 885 | UnwindData |  |
| 1058 | `RtlFreeThreadActivationContextStack` | `0x8CCE0` | 48 | UnwindData |  |
| 1050 | `RtlFreeActivationContextStack` | `0x8CD20` | 206 | UnwindData |  |
| 1461 | `RtlReportSilentProcessExit` | `0x8D130` | 495 | UnwindData |  |
| 179 | `LdrShutdownProcess` | `0x8D330` | 962 | UnwindData |  |
| 1809 | `TpTrimPools` | `0x8E570` | 1,017 | UnwindData |  |
| 1459 | `RtlReportException` | `0x8E970` | 155 | UnwindData |  |
| 944 | `RtlDetectHeapLeaks` | `0x8EC70` | 465 | UnwindData |  |
| 1203 | `RtlInitializeSid` | `0x8EF80` | 2,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 943 | `RtlDestroyQueryDebugBuffer` | `0x8F800` | 51 | UnwindData |  |
| 1392 | `RtlQueryProcessDebugInformation` | `0x8F990` | 2,455 | UnwindData |  |
| 1368 | `RtlQueryCriticalSectionOwner` | `0x90E20` | 270 | UnwindData |  |
| 1393 | `RtlQueryProcessHeapInformation` | `0x91070` | 1,528 | UnwindData |  |
| 1377 | `RtlQueryHeapInformation` | `0x91800` | 460 | UnwindData |  |
| 1391 | `RtlQueryProcessBackTraceInformation` | `0x919E0` | 631 | UnwindData |  |
| 1394 | `RtlQueryProcessLockInformation` | `0x91C60` | 659 | UnwindData |  |
| 1660 | `RtlWalkHeap` | `0x92430` | 72 | UnwindData |  |
| 1550 | `RtlSleepConditionVariableSRW` | `0x94B70` | 49 | UnwindData |  |
| 1658 | `RtlWakeConditionVariable` | `0x95770` | 40 | UnwindData |  |
| 18 | `AlpcGetMessageFromCompletionList` | `0x95BC0` | 380 | UnwindData |  |
| 139 | `LdrGetProcedureAddress` | `0x960F0` | 30 | UnwindData |  |
| 140 | `LdrGetProcedureAddressEx` | `0x96BA0` | 33 | UnwindData |  |
| 141 | `LdrGetProcedureAddressForCaller` | `0x96BD0` | 130 | UnwindData |  |
| 1647 | `RtlValidateUserCallTarget` | `0x98630` | 149 | UnwindData |  |
| 151 | `LdrLockLoaderLock` | `0x986D0` | 447 | UnwindData |  |
| 1749 | `ShipAssert` | `0x99F30` | 494 | UnwindData |  |
| 1820 | `WerReportSQMEvent` | `0x9A300` | 73 | UnwindData |  |
| 1437 | `RtlRegisterForWnfMetaNotification` | `0x9A870` | 77 | UnwindData |  |
| 1651 | `RtlWaitForWnfMetaNotification` | `0x9A8D0` | 540 | UnwindData |  |
| 1560 | `RtlSubscribeWnfStateChangeNotification` | `0x9ADA0` | 68 | UnwindData |  |
| 1618 | `RtlUnsubscribeWnfNotificationWaitForCompletion` | `0x9BA60` | 122 | UnwindData |  |
| 1620 | `RtlUnsubscribeWnfStateChangeNotification` | `0x9BAE0` | 76 | UnwindData |  |
| 1652 | `RtlWaitOnAddress` | `0x9BFB0` | 101 | UnwindData |  |
| 1653 | `RtlWakeAddressAll` | `0x9C870` | 23 | UnwindData |  |
| 1412 | `RtlQueryWnfStateData` | `0x9C890` | 36 | UnwindData |  |
| 1413 | `RtlQueryWnfStateDataWithExplicitScope` | `0x9C8C0` | 210 | UnwindData |  |
| 1436 | `RtlRegisterFeatureConfigurationChangeNotification` | `0x9C9A0` | 147 | UnwindData |  |
| 1421 | `RtlRandom` | `0x9CC30` | 358 | UnwindData |  |
| 1422 | `RtlRandomEx` | `0x9CC30` | 358 | UnwindData |  |
| 1478 | `RtlRunOnceExecuteOnce` | `0x9D080` | 269 | UnwindData |  |
| 166 | `LdrResFindResourceDirectory` | `0x9D1A0` | 134 | UnwindData |  |
| 169 | `LdrResSearchResource` | `0x9D230` | 1,929 | UnwindData |  |
| 1477 | `RtlRunOnceComplete` | `0x9DAA0` | 147 | UnwindData |  |
| 191 | `LdrpResGetMappingSize` | `0x9DE40` | 805 | UnwindData |  |
| 167 | `LdrResGetRCConfig` | `0x9E170` | 1,548 | UnwindData |  |
| 192 | `LdrpResGetResourceDirectory` | `0xA06C0` | 1,306 | UnwindData |  |
| 1122 | `RtlGetParentLocaleName` | `0xA19A0` | 536 | UnwindData |  |
| 1281 | `RtlLcidToLocaleName` | `0xA1BC0` | 629 | UnwindData |  |
| 1709 | `RtlpGetSystemDefaultUILanguage` | `0xA2620` | 172 | UnwindData |  |
| 1275 | `RtlIsValidLocaleName` | `0xA2A20` | 165 | UnwindData |  |
| 1181 | `RtlInitUnicodeString` | `0xA3020` | 69 | UnwindData |  |
| 1150 | `RtlGetUserPreferredUILanguages` | `0xA3070` | 1,575 | UnwindData |  |
| 1712 | `RtlpIsQualifiedLanguage` | `0xA3840` | 366 | UnwindData |  |
| 1096 | `RtlGetFileMUIPath` | `0xA4060` | 222 | UnwindData |  |
| 1098 | `RtlGetFullPathName_U` | `0xA4BB0` | 132 | UnwindData |  |
| 859 | `RtlCreateActivationContext` | `0xA4FD0` | 398 | UnwindData |  |
| 1182 | `RtlInitUnicodeStringEx` | `0xA6A60` | 76 | UnwindData |  |
| 959 | `RtlDosSearchPath_U` | `0xA6CB0` | 566 | UnwindData |  |
| 1090 | `RtlGetExePath` | `0xA6EF0` | 77 | UnwindData |  |
| 865 | `RtlCreateEnvironmentEx` | `0xA7170` | 579 | UnwindData |  |
| 1129 | `RtlGetSearchPath` | `0xA73C0` | 66 | UnwindData |  |
| 937 | `RtlDestroyEnvironment` | `0xA7410` | 17 | UnwindData |  |
| 1502 | `RtlSetEnvironmentVariable` | `0xA7430` | 55 | UnwindData |  |
| 1501 | `RtlSetEnvironmentVar` | `0xA7470` | 2,369 | UnwindData |  |
| 945 | `RtlDetermineDosPathNameType_U` | `0xA8110` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `LdrGetDllPath` | `0xA82E0` | 35 | UnwindData |  |
| 1373 | `RtlQueryEnvironmentVariable_U` | `0xA9320` | 102 | UnwindData |  |
| 1003 | `RtlExpandEnvironmentStrings_U` | `0xA9390` | 139 | UnwindData |  |
| 1002 | `RtlExpandEnvironmentStrings` | `0xA9430` | 14 | UnwindData |  |
| 1372 | `RtlQueryEnvironmentVariable` | `0xA95F0` | 2,500 | UnwindData |  |
| 1386 | `RtlQueryPackageIdentity` | `0xAB470` | 84 | UnwindData |  |
| 1387 | `RtlQueryPackageIdentityEx` | `0xAB4D0` | 98 | UnwindData |  |
| 1385 | `RtlQueryPackageClaims` | `0xAB540` | 778 | UnwindData |  |
| 1171 | `RtlInitCodePageTable` | `0xABF00` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1363 | `RtlQueryActivationContextApplicationSettings` | `0xAC0F0` | 567 | UnwindData |  |
| 1378 | `RtlQueryImageMitigationPolicy` | `0xACB80` | 3,136 | UnwindData |  |
| 156 | `LdrQueryImageFileExecutionOptions` | `0xAEA90` | 54 | UnwindData |  |
| 157 | `LdrQueryImageFileExecutionOptionsEx` | `0xAEAD0` | 151 | UnwindData |  |
| 158 | `LdrQueryImageFileKeyOption` | `0xAEB70` | 890 | UnwindData |  |
| 1332 | `RtlNtPathNameToDosPathName` | `0xAF7A0` | 627 | UnwindData |  |
| 1357 | `RtlPrefixUnicodeString` | `0xAFA20` | 317 | UnwindData |  |
| 1317 | `RtlMultiAppendUnicodeStringBuffer` | `0xAFB70` | 97 | UnwindData |  |
| 1016 | `RtlFindCharInUnicodeString` | `0xAFC90` | 201 | UnwindData |  |
| 1704 | `RtlpEnsureBufferSize` | `0xB00E0` | 68 | UnwindData |  |
| 992 | `RtlEqualUnicodeString` | `0xB0A60` | 301 | UnwindData |  |
| 762 | `RtlAppendPathElement` | `0xB0C00` | 669 | UnwindData |  |
| 150 | `LdrLoadEnclaveModule` | `0xB1270` | 587 | UnwindData |  |
| 144 | `LdrInitializeEnclave` | `0xB1620` | 262 | UnwindData |  |
| 1555 | `RtlStringFromGUIDEx` | `0xB2050` | 131 | UnwindData |  |
| 1259 | `RtlIsNameInUnUpcasedExpression` | `0xB2170` | 173 | UnwindData |  |
| 966 | `RtlEmptyAtomTable` | `0xB2230` | 163 | UnwindData |  |
| 949 | `RtlDnsHostNameToComputerName` | `0xB22E0` | 576 | UnwindData |  |
| 1346 | `RtlOemStringToUnicodeString` | `0xB2530` | 231 | UnwindData |  |
| 1319 | `RtlMultiByteToUnicodeSize` | `0xB2620` | 173 | UnwindData |  |
| 1347 | `RtlOemToUnicodeN` | `0xB26E0` | 93 | UnwindData |  |
| 1627 | `RtlUpcaseUnicodeStringToOemString` | `0xB2750` | 257 | UnwindData |  |
| 1630 | `RtlUpcaseUnicodeToOemN` | `0xB2860` | 109 | UnwindData |  |
| 1367 | `RtlQueryAtomInAtomTable` | `0xB2BB0` | 510 | UnwindData |  |
| 912 | `RtlDeleteAtomFromAtomTable` | `0xB2DC0` | 155 | UnwindData |  |
| 753 | `RtlAllocateHandle` | `0xB3480` | 522 | UnwindData |  |
| 1273 | `RtlIsValidHandle` | `0xB3840` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `RtlIsNameInExpression` | `0xB3870` | 111 | UnwindData |  |
| 1034 | `RtlFindUnicodeSubstring` | `0xB3E60` | 220 | UnwindData |  |
| 1601 | `RtlUnicodeStringToOemString` | `0xB42E0` | 273 | UnwindData |  |
| 1458 | `RtlReplaceSystemDirectoryInPath` | `0xB4570` | 180 | UnwindData |  |
| 1674 | `RtlWow64GetProcessMachines` | `0xB4630` | 469 | UnwindData |  |
| 1596 | `RtlUnicodeStringToAnsiSize` | `0xB4F90` | 172 | UnwindData |  |
| 1600 | `RtlUnicodeStringToOemSize` | `0xB4F90` | 172 | UnwindData |  |
| 1745 | `RtlxUnicodeStringToAnsiSize` | `0xB4F90` | 172 | UnwindData |  |
| 1746 | `RtlxUnicodeStringToOemSize` | `0xB4F90` | 172 | UnwindData |  |
| 1597 | `RtlUnicodeStringToAnsiString` | `0xB5EA0` | 811 | UnwindData |  |
| 1605 | `RtlUnicodeToMultiByteSize` | `0xB61E0` | 171 | UnwindData |  |
| 1629 | `RtlUpcaseUnicodeToMultiByteN` | `0xB62A0` | 941 | UnwindData |  |
| 1603 | `RtlUnicodeToCustomCPN` | `0xB6660` | 90 | UnwindData |  |
| 1607 | `RtlUnicodeToUTF8N` | `0xB67C0` | 54 | UnwindData |  |
| 1604 | `RtlUnicodeToMultiByteN` | `0xB6D60` | 363 | UnwindData |  |
| 765 | `RtlAppendUnicodeToString` | `0xB74E0` | 74 | UnwindData |  |
| 1119 | `RtlGetNtSystemRoot` | `0xB75A0` | 1,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `RtlCheckRegistryKey` | `0xB7C60` | 58 | UnwindData |  |
| 1400 | `RtlQueryRegistryValuesEx` | `0xB8D10` | 30 | UnwindData |  |
| 1697 | `RtlpCheckDynamicTimeZoneInformation` | `0xB8EA0` | 416 | UnwindData |  |
| 793 | `RtlCheckPortableOperatingSystem` | `0xB9050` | 204 | UnwindData |  |
| 1690 | `RtlWriteRegistryValue` | `0xBA360` | 196 | UnwindData |  |
| 143 | `LdrInitShimEngineDynamic` | `0xBAC10` | 245 | UnwindData |  |
| 124 | `LdrFindEntryForAddress` | `0xBAED0` | 78 | UnwindData |  |
| 1140 | `RtlGetThreadErrorMode` | `0xBB1D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `EtwEventWriteNoRegistration` | `0xBB240` | 209 | UnwindData |  |
| 1155 | `RtlHeapTrkInitialize` | `0xBDBF0` | 1,094 | UnwindData |  |
| 1506 | `RtlSetHeapInformation` | `0xBE040` | 574 | UnwindData |  |
| 896 | `RtlCutoverTimeToSystemTime` | `0xBF7C0` | 559 | UnwindData |  |
| 1736 | `RtlpTimeToTimeFields` | `0xBFA00` | 55 | UnwindData |  |
| 1735 | `RtlpTimeFieldsToTime` | `0xC0030` | 54 | UnwindData |  |
| 1234 | `RtlIpv6AddressToStringExW` | `0xC0410` | 308 | UnwindData |  |
| 1159 | `RtlIdnToUnicode` | `0xC0550` | 134 | UnwindData |  |
| 1226 | `RtlIpv4AddressToStringExW` | `0xC0600` | 64 | UnwindData |  |
| 987 | `RtlEqualDomainName` | `0xC06E0` | 158 | UnwindData |  |
| 1227 | `RtlIpv4AddressToStringW` | `0xC0880` | 75 | UnwindData |  |
| 1235 | `RtlIpv6AddressToStringW` | `0xC08E0` | 38 | UnwindData |  |
| 1157 | `RtlIdnToAscii` | `0xC0BE0` | 219 | UnwindData |  |
| 1230 | `RtlIpv4StringToAddressExW` | `0xC0CD0` | 448 | UnwindData |  |
| 784 | `RtlCanonicalizeDomainName` | `0xC0EA0` | 1,493 | UnwindData |  |
| 1238 | `RtlIpv6StringToAddressExW` | `0xC1480` | 712 | UnwindData |  |
| 1239 | `RtlIpv6StringToAddressW` | `0xC1750` | 1,021 | UnwindData |  |
| 1231 | `RtlIpv4StringToAddressW` | `0xC2A20` | 748 | UnwindData |  |
| 1329 | `RtlNormalizeString` | `0xC36F0` | 130 | UnwindData |  |
| 1262 | `RtlIsNormalizedString` | `0xC3B80` | 134 | UnwindData |  |
| 814 | `RtlCompactHeap` | `0xC5720` | 311 | UnwindData |  |
| 1509 | `RtlSetIoCompletionCallback` | `0xC71A0` | 325 | UnwindData |  |
| 1757 | `TpAllocJobNotification` | `0xC7440` | 572 | UnwindData |  |
| 1753 | `TpAllocAlpcCompletion` | `0xC7690` | 30 | UnwindData |  |
| 1754 | `TpAllocAlpcCompletionEx` | `0xC7720` | 30 | UnwindData |  |
| 1756 | `TpAllocIoCompletion` | `0xC7A70` | 553 | UnwindData |  |
| 981 | `RtlEnumerateGenericTable` | `0xC7EA0` | 104 | UnwindData |  |
| 922 | `RtlDeleteNoSplay` | `0xC7F10` | 197 | UnwindData |  |
| 916 | `RtlDeleteElementGenericTable` | `0xC7FE0` | 193 | UnwindData |  |
| 910 | `RtlDelete` | `0xC80B0` | 157 | UnwindData |  |
| 1561 | `RtlSubtreePredecessor` | `0xC8160` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `RtlInsertElementGenericTable` | `0xC8310` | 374 | UnwindData |  |
| 1207 | `RtlInsertElementGenericTableFull` | `0xC8490` | 278 | UnwindData |  |
| 1307 | `RtlLookupElementGenericTableFull` | `0xC85B0` | 194 | UnwindData |  |
| 1305 | `RtlLookupElementGenericTable` | `0xC8680` | 111 | UnwindData |  |
| 1551 | `RtlSplay` | `0xC8700` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1435 | `RtlRealSuccessor` | `0xC8940` | 9,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | `PssNtDuplicateSnapshot` | `0xCADF0` | 120 | UnwindData |  |
| 704 | `PssNtFreeSnapshot` | `0xCAE70` | 441 | UnwindData |  |
| 706 | `PssNtQuerySnapshot` | `0xCB030` | 652 | UnwindData |  |
| 708 | `PssNtWalkSnapshot` | `0xCB2D0` | 632 | UnwindData |  |
| 707 | `PssNtValidateDescriptor` | `0xCB550` | 265 | UnwindData |  |
| 758 | `RtlAnsiCharToUnicodeChar` | `0xCBBA0` | 12 | UnwindData |  |
| 1017 | `RtlFindClearBits` | `0xCBDC0` | 55 | UnwindData |  |
| 1018 | `RtlFindClearBitsAndSet` | `0xCC190` | 22 | UnwindData |  |
| 74 | `EtwEventWriteEndScenario` | `0xCC5E0` | 300 | UnwindData |  |
| 78 | `EtwEventWriteStartScenario` | `0xCC720` | 501 | UnwindData |  |
| 68 | `EtwEventEnabled` | `0xCC920` | 18 | UnwindData |  |
| 878 | `RtlCreateServiceSid` | `0xCD5F0` | 318 | UnwindData |  |
| 893 | `RtlCreateVirtualAccountSid` | `0xCD740` | 340 | UnwindData |  |
| 1624 | `RtlUpcaseUnicodeString` | `0xCD8A0` | 283 | UnwindData |  |
| 1623 | `RtlUpcaseUnicodeChar` | `0xCE1B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1049 | `RtlFormatMessageEx` | `0xCE210` | 2,542 | UnwindData |  |
| 821 | `RtlCompareUnicodeString` | `0xCECE0` | 361 | UnwindData |  |
| 909 | `RtlDelayExecution` | `0xCEE50` | 280 | UnwindData |  |
| 1270 | `RtlIsTextUnicode` | `0xCEF70` | 2,179 | UnwindData |  |
| 1590 | `RtlUTF8StringToUnicodeString` | `0xCF800` | 56 | UnwindData |  |
| 713 | `RtlAcquireReleaseSRWLockExclusive` | `0xCFD20` | 46 | UnwindData |  |
| 1046 | `RtlFlushSecureMemoryCache` | `0xD0100` | 121 | UnwindData |  |
| 939 | `RtlDestroyHeap` | `0xD1790` | 996 | UnwindData |  |
| 924 | `RtlDeleteResource` | `0xD2040` | 128 | UnwindData |  |
| 915 | `RtlDeleteCriticalSection` | `0xD20D0` | 392 | UnwindData |  |
| 1154 | `RtlHashUnicodeString` | `0xD66C0` | 79 | UnwindData |  |
| 1672 | `RtlWow64GetCurrentMachine` | `0xD6A20` | 58 | UnwindData |  |
| 1621 | `RtlUnwind` | `0xD6A60` | 253 | UnwindData |  |
| 1194 | `RtlInitializeExtendedContext2` | `0xD6B70` | 429 | UnwindData |  |
| 1670 | `RtlWow64GetCpuAreaInfo` | `0xD6E40` | 360 | UnwindData |  |
| 1671 | `RtlWow64GetCurrentCpuArea` | `0xD6FB0` | 306 | UnwindData |  |
| 1092 | `RtlGetExtendedContextLength2` | `0xD70F0` | 204 | UnwindData |  |
| 1191 | `RtlInitializeCriticalSectionAndSpinCount` | `0xD7370` | 379 | UnwindData |  |
| 1190 | `RtlInitializeCriticalSection` | `0xD7A00` | 336 | UnwindData |  |
| 1041 | `RtlFlsGetValue2` | `0xD7D70` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1763 | `TpAlpcUnregisterCompletionList` | `0xD7ED0` | 50 | UnwindData |  |
| 1773 | `TpCallbackUnloadDllOnCompletion` | `0xD8700` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1810 | `TpWaitForAlpcCompletion` | `0xD8740` | 97 | UnwindData |  |
| 1786 | `TpReleaseCleanupGroupMembers` | `0xD87B0` | 786 | UnwindData |  |
| 1788 | `TpReleaseJobNotification` | `0xD8AD0` | 158 | UnwindData |  |
| 1812 | `TpWaitForJobNotification` | `0xD8B80` | 53 | UnwindData |  |
| 1784 | `TpReleaseAlpcCompletion` | `0xD8CE0` | 164 | UnwindData |  |
| 1787 | `TpReleaseIoCompletion` | `0xD8E50` | 160 | UnwindData |  |
| 1774 | `TpCancelAsyncIoOperation` | `0xD8FF0` | 267 | UnwindData |  |
| 759 | `RtlAnsiStringToUnicodeSize` | `0xD9470` | 152 | UnwindData |  |
| 1345 | `RtlOemStringToUnicodeSize` | `0xD9470` | 152 | UnwindData |  |
| 1743 | `RtlxAnsiStringToUnicodeSize` | `0xD9470` | 152 | UnwindData |  |
| 1744 | `RtlxOemStringToUnicodeSize` | `0xD9470` | 152 | UnwindData |  |
| 1293 | `RtlLocateExtendedFeature2` | `0xD9510` | 317 | UnwindData |  |
| 1817 | `TpWorkOnBehalfSetTicket` | `0xD9740` | 127 | UnwindData |  |
| 1765 | `TpCallbackIndependent` | `0xD9BB0` | 405 | UnwindData |  |
| 1105 | `RtlGetInterruptTimePrecise` | `0xDA080` | 401 | UnwindData |  |
| 1040 | `RtlFlsGetValue` | `0xDA220` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 958 | `RtlDosPathNameToRelativeNtPathName_U_WithStatus` | `0xDA290` | 140 | UnwindData |  |
| 1136 | `RtlGetSystemGlobalData` | `0xDA3A0` | 740 | UnwindData |  |
| 1572 | `RtlTimeToSecondsSince1980` | `0xDA690` | 58 | UnwindData |  |
| 1535 | `RtlSetThreadWorkOnBehalfTicket` | `0xDA850` | 106 | UnwindData |  |
| 953 | `RtlDosLongPathNameToNtPathName_U_WithStatus` | `0xDA990` | 34 | UnwindData |  |
| 129 | `LdrGetDllDirectory` | `0xDAB80` | 130 | UnwindData |  |
| 855 | `RtlCopyUnicodeString` | `0xDAC10` | 33 | UnwindData |  |
| 1186 | `RtlInitializeBitMapEx` | `0xDAE80` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `AlpcFreeCompletionListMessage` | `0xDB090` | 60 | UnwindData |  |
| 962 | `RtlDowncaseUnicodeString` | `0xDB1B0` | 284 | UnwindData |  |
| 715 | `RtlAcquireResourceShared` | `0xDB330` | 22 | UnwindData |  |
| 1646 | `RtlValidateUnicodeString` | `0xDB4B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1063 | `RtlGUIDFromString` | `0xDB510` | 269 | UnwindData |  |
| 1740 | `RtlpWow64CtxFromAmd64` | `0xDB8D0` | 758 | UnwindData |  |
| 842 | `RtlCopyContext` | `0xDC050` | 53 | UnwindData |  |
| 1036 | `RtlFirstFreeAce` | `0xDCD80` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1029 | `RtlFindNextForwardRunClear` | `0xDCE40` | 33 | UnwindData |  |
| 1356 | `RtlPrefixString` | `0xDCF50` | 164 | UnwindData |  |
| 1497 | `RtlSetCurrentTransaction` | `0xDD000` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 956 | `RtlDosPathNameToNtPathName_U_WithStatus` | `0xDD710` | 138 | UnwindData |  |
| 984 | `RtlEnumerateGenericTableWithoutSplaying` | `0xDD9E0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1169 | `RtlInitAnsiStringEx` | `0xDDA90` | 72 | UnwindData |  |
| 1093 | `RtlGetExtendedFeaturesMask` | `0xDDAE0` | 22 | UnwindData |  |
| 1494 | `RtlSetCriticalSectionSpinCount` | `0xDDB90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1542 | `RtlSidDominates` | `0xDDBE0` | 131 | UnwindData |  |
| 714 | `RtlAcquireResourceExclusive` | `0xDDD00` | 22 | UnwindData |  |
| 1447 | `RtlReleaseResource` | `0xDE0F0` | 211 | UnwindData |  |
| 1161 | `RtlImageNtHeader` | `0xDE1D0` | 44 | UnwindData |  |
| 1209 | `RtlInsertEntryHashTable` | `0xDE230` | 311 | UnwindData |  |
| 1172 | `RtlInitEnumerationHashTable` | `0xDE370` | 109 | UnwindData |  |
| 1089 | `RtlGetEnabledExtendedFeatures` | `0xDE550` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `RtlInstallFunctionTableCallback` | `0xDE580` | 793 | UnwindData |  |
| 1708 | `RtlpGetNameFromLangInfoNode` | `0xDE8A0` | 252 | UnwindData |  |
| 1289 | `RtlLoadString` | `0xDEA30` | 641 | UnwindData |  |
| 1379 | `RtlQueryInformationAcl` | `0xDED20` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1669 | `RtlWow64GetCpuAreaEnabledFeatures` | `0xDEDD0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1344 | `RtlNumberOfSetBitsUlongPtr` | `0xDEF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `RtlGetSystemTimeAndBias` | `0xDEF80` | 332 | UnwindData |  |
| 1143 | `RtlGetThreadWorkOnBehalfTicket` | `0xDF0E0` | 188 | UnwindData |  |
| 948 | `RtlDllShutdownInProgress` | `0xDF1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `RtlIntegerToUnicodeString` | `0xDF1D0` | 140 | UnwindData |  |
| 1212 | `RtlIntegerToChar` | `0xDF270` | 323 | UnwindData |  |
| 1099 | `RtlGetFullPathName_UEx` | `0xDF3C0` | 175 | UnwindData |  |
| 991 | `RtlEqualString` | `0xDF480` | 25 | UnwindData |  |
| 23 | `AlpcRegisterCompletionListWorkerThread` | `0xDF6E0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `RtlEnumerateEntryHashTable` | `0xDFA40` | 276 | UnwindData |  |
| 26 | `AlpcUnregisterCompletionListWorkerThread` | `0xDFB60` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `RtlDosPathNameToRelativeNtPathName_U` | `0xDFBC0` | 142 | UnwindData |  |
| 973 | `RtlEncodeSystemPointer` | `0xDFC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1309 | `RtlLookupEntryHashTable` | `0xDFC80` | 214 | UnwindData |  |
| 807 | `RtlClearThreadWorkOnBehalfTicket` | `0xDFE40` | 98 | UnwindData |  |
| 1168 | `RtlInitAnsiString` | `0xDFF20` | 65 | UnwindData |  |
| 1176 | `RtlInitString` | `0xDFF20` | 65 | UnwindData |  |
| 1245 | `RtlIsCriticalSectionLockedByThread` | `0xDFF70` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1314 | `RtlMapGenericMask` | `0xE0510` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1369 | `RtlQueryDepthSList` | `0xE0550` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1389 | `RtlQueryPerformanceFrequency` | `0xE06C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `RtlAllocateAndInitializeSid` | `0xE06E0` | 65 | UnwindData |  |
| 1164 | `RtlImageRvaToVa` | `0xE0810` | 124 | UnwindData |  |
| 1163 | `RtlImageRvaToSection` | `0xE08A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `RtlIsDosDeviceName_U` | `0xE08F0` | 73 | UnwindData |  |
| 1362 | `RtlPushFrame` | `0xE0940` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `RtlFindLongestRunClear` | `0xE0970` | 57 | UnwindData |  |
| 1021 | `RtlFindClearRuns` | `0xE09B0` | 733 | UnwindData |  |
| 1104 | `RtlGetIntegerAtom` | `0xE0CA0` | 199 | UnwindData |  |
| 20 | `AlpcInitializeMessageAttribute` | `0xE0D70` | 88 | UnwindData |  |
| 17 | `AlpcGetMessageAttribute` | `0xE0DD0` | 51 | UnwindData |  |
| 16 | `AlpcGetHeaderSize` | `0xE0E10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `RtlIsGenericTableEmpty` | `0xE0E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1498 | `RtlSetDaclSecurityDescriptor` | `0xE0E80` | 3,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `EtwLogTraceEvent` | `0xE1BA0` | 93 | UnwindData |  |
| 869 | `RtlCreateMemoryBlockLookaside` | `0xE1F70` | 516 | UnwindData |  |
| 1201 | `RtlInitializeSListHead` | `0xE2180` | 32 | UnwindData |  |
| 870 | `RtlCreateMemoryZone` | `0xE21B0` | 154 | UnwindData |  |
| 1348 | `RtlOpenCrossProcessEmulatorWorkConnection` | `0xE2250` | 361 | UnwindData |  |
| 1246 | `RtlIsCurrentProcess` | `0xE23C0` | 44 | UnwindData |  |
| 1771 | `TpCallbackSendPendingAlpcMessage` | `0xE2400` | 54 | UnwindData |  |
| 1556 | `RtlStronglyEnumerateEntryHashTable` | `0xE24F0` | 90 | UnwindData |  |
| 832 | `RtlContractHashTable` | `0xE2550` | 334 | UnwindData |  |
| 1004 | `RtlExpandHashTable` | `0xE26B0` | 492 | UnwindData |  |
| 921 | `RtlDeleteHashTable` | `0xE2A90` | 165 | UnwindData |  |
| 1355 | `RtlPopFrame` | `0xE2C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `RtlCreateProcessParametersEx` | `0xE2C70` | 106 | UnwindData |  |
| 873 | `RtlCreateProcessParametersWithTemplate` | `0xE2CE0` | 295 | UnwindData |  |
| 1287 | `RtlLengthSid` | `0xE34C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1083 | `RtlGetCurrentTransaction` | `0xE34E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `EtwpCreateEtwThread` | `0xE3500` | 118 | UnwindData |  |
| 892 | `RtlCreateUserThread` | `0xE3580` | 104 | UnwindData |  |
| 1085 | `RtlGetDaclSecurityDescriptor` | `0xE37A0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `RtlDosPathNameToNtPathName_U` | `0xE3A50` | 140 | UnwindData |  |
| 1525 | `RtlSetSecurityObjectEx` | `0xE3AF0` | 55 | UnwindData |  |
| 740 | `RtlAddProcessTrustLabelAce` | `0xE3B30` | 366 | UnwindData |  |
| 1524 | `RtlSetSecurityObject` | `0xE3CB0` | 50 | UnwindData |  |
| 1543 | `RtlSidDominatesForTrust` | `0xE5A80` | 134 | UnwindData |  |
| 1276 | `RtlIsValidProcessTrustLabelSid` | `0xE5B10` | 107 | UnwindData |  |
| 919 | `RtlDeleteFunctionTable` | `0xE5E70` | 508 | UnwindData |  |
| 920 | `RtlDeleteGrowableFunctionTable` | `0xE6080` | 408 | UnwindData |  |
| 778 | `RtlAvlRemoveNode` | `0xE6220` | 1,000 | UnwindData |  |
| 127 | `LdrFindResource_U` | `0xE6610` | 333 | UnwindData |  |
| 1715 | `RtlpMergeSecurityAttributeInformation` | `0xE6770` | 1,061 | UnwindData |  |
| 1789 | `TpReleasePool` | `0xE6DA0` | 566 | UnwindData |  |
| 886 | `RtlCreateUnicodeStringFromAsciiz` | `0xE71C0` | 94 | UnwindData |  |
| 1274 | `RtlIsValidIndexHandle` | `0xE7230` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1294 | `RtlLocateLegacyContext` | `0xE7270` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `RtlCreateSecurityDescriptor` | `0xE73F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1117 | `RtlGetNtGlobalFlags` | `0xE7420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1571 | `RtlTimeToSecondsSince1970` | `0xE7440` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `RtlAcquirePrivilege` | `0xE77A0` | 827 | UnwindData |  |
| 1166 | `RtlImpersonateSelfEx` | `0xE7AF0` | 113 | UnwindData |  |
| 1229 | `RtlIpv4StringToAddressExA` | `0xE7C90` | 455 | UnwindData |  |
| 1228 | `RtlIpv4StringToAddressA` | `0xE7E60` | 702 | UnwindData |  |
| 1818 | `VerSetConditionMask` | `0xE8130` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `RtlEnumerateGenericTableWithoutSplayingAvl` | `0xE8170` | 105 | UnwindData |  |
| 145 | `LdrInitializeThunk` | `0xE8EE0` | 32 | UnwindData |  |
| 1268 | `RtlIsProcessorFeaturePresent` | `0xE90D0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1286 | `RtlLengthSecurityDescriptor` | `0xE91A0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `RtlInitializeConditionVariable` | `0xE92D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `RtlInitializeSRWLock` | `0xE92D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `RtlRunOnceInitialize` | `0xE92D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1376 | `RtlQueryFeatureUsageNotificationSubscriptions` | `0xE92E0` | 114 | UnwindData |  |
| 1364 | `RtlQueryAllFeatureConfigurations` | `0xE9360` | 165 | UnwindData |  |
| 1331 | `RtlNotifyFeatureUsage` | `0xE9450` | 125 | UnwindData |  |
| 1374 | `RtlQueryFeatureConfiguration` | `0xE98A0` | 309 | UnwindData |  |
| 1214 | `RtlInterlockedClearBitRun` | `0xEA850` | 177 | UnwindData |  |
| 1057 | `RtlFreeSid` | `0xEA910` | 50 | UnwindData |  |
| 775 | `RtlAreLongPathsEnabled` | `0xEA980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1269 | `RtlIsStateSeparationEnabled` | `0xEA9A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `RtlSetUnhandledExceptionFilter` | `0xEA9F0` | 22 | UnwindData |  |
| 971 | `RtlEncodePointer` | `0xEAA10` | 96 | UnwindData |  |
| 1126 | `RtlGetProductInfo` | `0xEAB10` | 442 | UnwindData |  |
| 1608 | `RtlUniform` | `0xEAE30` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1816 | `TpWorkOnBehalfClearTicket` | `0xEAE80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1149 | `RtlGetUserInfoHeap` | `0xEAEA0` | 774 | UnwindData |  |
| 1128 | `RtlGetSaclSecurityDescriptor` | `0xEB370` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1691 | `RtlXRestore` | `0xEB3E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `RtlCopyLuid` | `0xEB430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `RtlDecodeSystemPointer` | `0xEB440` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `RtlTimeToElapsedTimeFields` | `0xEB470` | 247 | UnwindData |  |
| 1558 | `RtlSubAuthoritySid` | `0xEB580` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1648 | `RtlVerifyVersionInfo` | `0xEB690` | 952 | UnwindData |  |
| 1451 | `RtlRemoveEntryHashTable` | `0xEBA80` | 93 | UnwindData |  |
| 1640 | `RtlValidRelativeSecurityDescriptor` | `0xEC280` | 347 | UnwindData |  |
| 1483 | `RtlSelfRelativeToAbsoluteSD` | `0xEC4C0` | 595 | UnwindData |  |
| 1107 | `RtlGetLastWin32Error` | `0xEC720` | 960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 965 | `RtlDuplicateUnicodeString` | `0xECAE0` | 428 | UnwindData |  |
| 1121 | `RtlGetOwnerSecurityDescriptor` | `0xECCA0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1241 | `RtlIsApiSetImplemented` | `0xECF50` | 194 | UnwindData |  |
| 1528 | `RtlSetThreadErrorMode` | `0xED260` | 1,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `RtlFindExportedRoutineByName` | `0xED720` | 232 | UnwindData |  |
| 1434 | `RtlRealPredecessor` | `0xED810` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1530 | `RtlSetThreadPlaceholderCompatibilityMode` | `0xED860` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1775 | `TpCaptureCaller` | `0xED900` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1443 | `RtlReleasePath` | `0xED960` | 105 | UnwindData |  |
| 1541 | `RtlSetUserValueHeap` | `0xED9D0` | 744 | UnwindData |  |
| 1013 | `RtlFindAceByType` | `0xEDE80` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1218 | `RtlInterlockedPushEntrySList` | `0xEDEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `LdrUpdatePackageSearchPath` | `0xEDF00` | 245 | UnwindData |  |
| 120 | `LdrDisableThreadCalloutsForDll` | `0xEE070` | 82 | UnwindData |  |
| 1216 | `RtlInterlockedFlushSList` | `0xEE0D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1557 | `RtlSubAuthorityCountSid` | `0xEE160` | 2,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1573 | `RtlTimeToTimeFields` | `0xEEC20` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `RtlAreBitsClearEx` | `0xEEE90` | 205 | UnwindData |  |
| 1075 | `RtlGetControlSecurityDescriptor` | `0xEEF70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `LdrGetDllHandleByMapping` | `0xEEFA0` | 247 | UnwindData |  |
| 76 | `EtwEventWriteFull` | `0xEF2F0` | 68 | UnwindData |  |
| 1102 | `RtlGetGroupSecurityDescriptor` | `0xEF340` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `RtlFreeHandle` | `0xEF380` | 55 | UnwindData |  |
| 1794 | `TpSetDefaultPoolStackInformation` | `0xEF460` | 273 | UnwindData |  |
| 1798 | `TpSetPoolStackInformation` | `0xEF580` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `ApiSetQueryApiSetPresence` | `0xEF640` | 193 | UnwindData |  |
| 770 | `RtlAreAllAccessesGranted` | `0xEF710` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1237 | `RtlIpv6StringToAddressExA` | `0xEFA30` | 637 | UnwindData |  |
| 1236 | `RtlIpv6StringToAddressA` | `0xEFCC0` | 1,273 | UnwindData |  |
| 1655 | `RtlWakeAddressSingle` | `0xF05A0` | 23 | UnwindData |  |
| 1224 | `RtlIpv4AddressToStringA` | `0xF05C0` | 73 | UnwindData |  |
| 75 | `EtwEventWriteEx` | `0xF0DD0` | 73 | UnwindData |  |
| 1114 | `RtlGetNextEntryHashTable` | `0xF0F50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `RtlCheckTokenMembership` | `0xF0FA0` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `RtlIsCurrentThreadAttachExempt` | `0xF1850` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1404 | `RtlQueryThreadPlaceholderCompatibilityMode` | `0xF1890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1439 | `RtlRegisterThreadWithCsrss` | `0xF18B0` | 179 | UnwindData |  |
| 1233 | `RtlIpv6AddressToStringExA` | `0xF1970` | 275 | UnwindData |  |
| 1232 | `RtlIpv6AddressToStringA` | `0xF1A90` | 688 | UnwindData |  |
| 801 | `RtlClearAllBits` | `0xF1E70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `RtlCreateBoundaryDescriptor` | `0xF1EA0` | 203 | UnwindData |  |
| 1565 | `RtlTestAndPublishWnfStateData` | `0xF1F80` | 171 | UnwindData |  |
| 1361 | `RtlPublishWnfStateData` | `0xF2040` | 162 | UnwindData |  |
| 29 | `ApiSetQueryApiSetPresenceEx` | `0xF2190` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `LdrLoadAlternateResourceModule` | `0xF2230` | 1,044 | UnwindData |  |
| 1257 | `RtlIsMultiUsersInSessionSku` | `0xF26C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `EtwGetTraceLoggerHandle` | `0xF26E0` | 91 | UnwindData |  |
| 82 | `EtwGetTraceEnableLevel` | `0xF2750` | 65 | UnwindData |  |
| 81 | `EtwGetTraceEnableFlags` | `0xF27A0` | 65 | UnwindData |  |
| 749 | `RtlAdjustPrivilege` | `0xF2850` | 269 | UnwindData |  |
| 925 | `RtlDeleteSecurityObject` | `0xF2970` | 35 | UnwindData |  |
| 736 | `RtlAddFunctionTable` | `0xF2AC0` | 768 | UnwindData |  |
| 1359 | `RtlProcessFlsData` | `0xF2DD0` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `RtlAssert` | `0xF30A0` | 287 | UnwindData |  |
| 1033 | `RtlFindSetBitsEx` | `0xF31F0` | 917 | UnwindData |  |
| 1804 | `TpSetWait` | `0xF3590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `RtlSetSearchPathMode` | `0xF35A0` | 254 | UnwindData |  |
| 1156 | `RtlIdentifierAuthoritySid` | `0xF36B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `AlpcGetOutstandingCompletionListMessageCount` | `0xF36C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `RtlNumberOfClearBits` | `0xF36E0` | 27 | UnwindData |  |
| 1341 | `RtlNumberOfSetBits` | `0xF3710` | 348 | UnwindData |  |
| 792 | `RtlCheckForOrphanedCriticalSections` | `0xF38D0` | 29 | UnwindData |  |
| 1725 | `RtlpNtQueryValueKey` | `0xF3D60` | 269 | UnwindData |  |
| 1265 | `RtlIsPartialPlaceholder` | `0xF45F0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `EvtIntReportEventAndSourceAsync` | `0xF4740` | 103 | UnwindData |  |
| 98 | `EtwWriteUMSecurityEvent` | `0xF4C00` | 209 | UnwindData |  |
| 1486 | `RtlSetAllBits` | `0xF4CE0` | 95 | UnwindData |  |
| 1569 | `RtlTimeFieldsToTime` | `0xF4D50` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `RtlCreateTagHeap` | `0xF4E30` | 670 | UnwindData |  |
| 711 | `RtlAcquirePebLock` | `0xF52C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `RtlReleasePebLock` | `0xF52E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `RtlIpv4AddressToStringExA` | `0xF5300` | 254 | UnwindData |  |
| 1087 | `RtlGetElementGenericTable` | `0xF5410` | 154 | UnwindData |  |
| 1185 | `RtlInitializeBitMap` | `0xF54B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1397 | `RtlQueryProtectedPolicy` | `0xF54C0` | 137 | UnwindData |  |
| 851 | `RtlCopySecurityDescriptor` | `0xF5AA0` | 376 | UnwindData |  |
| 891 | `RtlCreateUserStack` | `0xF5D20` | 720 | UnwindData |  |
| 1243 | `RtlIsCloudFilesPlaceholder` | `0xF6000` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1722 | `RtlpNtEnumerateSubKey` | `0xF6170` | 262 | UnwindData |  |
| 1381 | `RtlQueryInformationActiveActivationContext` | `0xF6280` | 41 | UnwindData |  |
| 982 | `RtlEnumerateGenericTableAvl` | `0xF62E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1068 | `RtlGetActiveConsoleId` | `0xF6300` | 47 | UnwindData |  |
| 1310 | `RtlLookupFirstMatchingElementGenericTableAvl` | `0xF6340` | 146 | UnwindData |  |
| 774 | `RtlAreBitsSet` | `0xF6560` | 211 | UnwindData |  |
| 1678 | `RtlWow64IsWowGuestMachineSupported` | `0xF6850` | 282 | UnwindData |  |
| 1195 | `RtlInitializeGenericTable` | `0xF6A10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1696 | `RtlpApplyLengthFunction` | `0xF6A50` | 144 | UnwindData |  |
| 1005 | `RtlExtendCorrelationVector` | `0xF6AF0` | 62 | UnwindData |  |
| 1167 | `RtlIncrementCorrelationVector` | `0xF6B40` | 223 | UnwindData |  |
| 1643 | `RtlValidateCorrelationVector` | `0xF6C30` | 230 | UnwindData |  |
| 1024 | `RtlFindLastBackwardRunClear` | `0xF6E50` | 224 | UnwindData |  |
| 1165 | `RtlImpersonateSelf` | `0xF7090` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `RtlGetAcesBufferSize` | `0xF7220` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1802 | `TpSetTimer` | `0xF7270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `RtlCreateQueryDebugBuffer` | `0xF7280` | 671 | UnwindData |  |
| 911 | `RtlDeleteAce` | `0xF7800` | 144 | UnwindData |  |
| 1675 | `RtlWow64GetSharedInfoProcess` | `0xF78F0` | 122 | UnwindData |  |
| 1302 | `RtlLogStackBackTrace` | `0xF79D0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1780 | `TpDisassociateCallback` | `0xF7AF0` | 133 | UnwindData |  |
| 100 | `EtwpGetCpuSpeed` | `0xF7C50` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `RtlInterlockedClearBitRunEx` | `0xF7DA0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1585 | `RtlTryAcquirePebLock` | `0xF7E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1445 | `RtlReleasePrivilege` | `0xF7E80` | 184 | UnwindData |  |
| 961 | `RtlDowncaseUnicodeChar` | `0xF7F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `EtwEventUnregister` | `0xF7F60` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `RtlExtendMemoryZone` | `0xF8220` | 253 | UnwindData |  |
| 947 | `RtlDisownModuleHeapAllocation` | `0xF8330` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 974 | `RtlEndEnumerationHashTable` | `0xF85B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1546 | `RtlSidHashLookup` | `0xF8600` | 294 | UnwindData |  |
| 1795 | `TpSetPoolMaxThreads` | `0xF87D0` | 136 | UnwindData |  |
| 1196 | `RtlInitializeGenericTableAvl` | `0xF8860` | 89 | UnwindData |  |
| 1106 | `RtlGetLastNtStatus` | `0xF8C20` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `LdrFindResourceEx_U` | `0xF8C90` | 295 | UnwindData |  |
| 1148 | `RtlGetUnloadEventTraceEx` | `0xF8DC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 856 | `RtlCrc32` | `0xF8DF0` | 81 | UnwindData |  |
| 750 | `RtlAllocateActivationContextStack` | `0xF96E0` | 118 | UnwindData |  |
| 1271 | `RtlIsThreadWithinLoaderCallout` | `0xF9760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1724 | `RtlpNtOpenKey` | `0xF9780` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1554 | `RtlStringFromGUID` | `0xF9800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1811 | `TpWaitForIoCompletion` | `0xF9810` | 252 | UnwindData |  |
| 1152 | `RtlGrowFunctionTable` | `0xF9920` | 236 | UnwindData |  |
| 1616 | `RtlUnregisterFeatureConfigurationChangeNotification` | `0xF9A20` | 41 | UnwindData |  |
| 824 | `RtlCompressBuffer` | `0xF9AA0` | 131 | UnwindData |  |
| 1755 | `TpAllocCleanupGroup` | `0xF9B30` | 235 | UnwindData |  |
| 772 | `RtlAreBitsClear` | `0xF9C30` | 203 | UnwindData |  |
| 1711 | `RtlpInitializeLangRegistryInfo` | `0xF9D10` | 38 | UnwindData |  |
| 1545 | `RtlSidHashInitialize` | `0xF9EB0` | 177 | UnwindData |  |
| 1375 | `RtlQueryFeatureConfigurationChangeStamp` | `0xF9F70` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1758 | `TpAllocPool` | `0xFA0E0` | 60 | UnwindData |  |
| 1633 | `RtlUpdateTimer` | `0xFA1C0` | 252 | UnwindData |  |
| 1086 | `RtlGetDeviceFamilyInfoEnum` | `0xFA2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `RtlGetCurrentPeb` | `0xFA2E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `RtlCopyMappedMemory` | `0xFA300` | 24 | UnwindData |  |
| 906 | `RtlDecompressBufferEx` | `0xFA370` | 126 | UnwindData |  |
| 1337 | `RtlNumberGenericTableElementsAvl` | `0xFA400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `LdrAccessResource` | `0xFA480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `RtlSetProtectedPolicy` | `0xFA490` | 741 | UnwindData |  |
| 1296 | `RtlLockCurrentThread` | `0xFA780` | 264 | UnwindData |  |
| 1263 | `RtlIsPackageSid` | `0xFA910` | 66 | UnwindData |  |
| 1110 | `RtlGetLocaleFileMappingAddress` | `0xFA960` | 139 | UnwindData |  |
| 1280 | `RtlLargeIntegerToChar` | `0xFADF0` | 351 | UnwindData |  |
| 1489 | `RtlSetBit` | `0xFB100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1673 | `RtlWow64GetEquivalentMachineCHPE` | `0xFB120` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1336 | `RtlNumberGenericTableElements` | `0xFB270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `LdrStandardizeSystemPath` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 901 | `RtlDebugPrintTimes` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `RtlEndStrongEnumerationHashTable` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `RtlFinalReleaseOutOfProcessMemoryStream` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `RtlInitMemoryStream` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `RtlInitNlsTables` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `RtlInitOutOfProcessMemoryStream` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1466 | `RtlResetRtlTranslations` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `RtlpWaitForCriticalSection` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1778 | `TpDbgSetLogRoutine` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1821 | `WinSqmAddToAverageDWORD` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1822 | `WinSqmAddToStream` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1823 | `WinSqmAddToStreamEx` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1833 | `WinSqmEndSession` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1838 | `WinSqmIncrementDWORD` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1842 | `WinSqmSetDWORD` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1843 | `WinSqmSetDWORD64` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1845 | `WinSqmSetIfMaxDWORD` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1846 | `WinSqmSetIfMinDWORD` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1847 | `WinSqmSetString` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2345 | `__misaligned_access` | `0xFB280` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | `RtlDeleteTimerQueueEx` | `0xFB330` | 385 | UnwindData |  |
| 183 | `LdrUnloadAlternateResourceModule` | `0xFB8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1371 | `RtlQueryElevationFlags` | `0xFB8E0` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `RtlInitializeExtendedContext` | `0xFC390` | 261 | UnwindData |  |
| 1091 | `RtlGetExtendedContextLength` | `0xFC4A0` | 238 | UnwindData |  |
| 1567 | `RtlTestBitEx` | `0xFC650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `RtlDestroyProcessParameters` | `0xFC670` | 35 | UnwindData |  |
| 889 | `RtlCreateUserProcessEx` | `0xFC6A0` | 176 | UnwindData |  |
| 1327 | `RtlNormalizeProcessParams` | `0xFC760` | 44,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `RtlInitializeRXact` | `0x107340` | 1,090 | UnwindData |  |
| 767 | `RtlApplyRXact` | `0x107790` | 204 | UnwindData |  |
| 768 | `RtlApplyRXactNoFlush` | `0x107870` | 33 | UnwindData |  |
| 709 | `RtlAbortRXact` | `0x107A60` | 63 | UnwindData |  |
| 1111 | `RtlGetLongestNtPathLength` | `0x107AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1564 | `RtlSystemTimeToLocalTime` | `0x107AC0` | 112 | UnwindData |  |
| 803 | `RtlClearBit` | `0x107B40` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1713 | `RtlpLoadMachineUIByPolicy` | `0x107CA0` | 385 | UnwindData |  |
| 882 | `RtlCreateTimerQueue` | `0x107E30` | 180 | UnwindData |  |
| 838 | `RtlConvertSharedToExclusive` | `0x107EF0` | 77 | UnwindData |  |
| 1411 | `RtlQueryWnfMetaNotification` | `0x107F50` | 70 | UnwindData |  |
| 1707 | `RtlpGetLCIDFromLangInfoNode` | `0x108010` | 147 | UnwindData |  |
| 1797 | `TpSetPoolMinThreads` | `0x1080B0` | 157 | UnwindData |  |
| 1197 | `RtlInitializeHandleTable` | `0x108160` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | `RtlCreateUserFiberShadowStack` | `0x1081A0` | 223 | UnwindData |  |
| 1073 | `RtlGetCompressionWorkSpaceSize` | `0x108370` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1606 | `RtlUnicodeToOemN` | `0x1083C0` | 70 | UnwindData |  |
| 1796 | `TpSetPoolMaxThreadsSoftLimit` | `0x109C10` | 73 | UnwindData |  |
| 1785 | `TpReleaseCleanupGroup` | `0x109C60` | 94 | UnwindData |  |
| 1062 | `RtlFreeUserStack` | `0x109CD0` | 45 | UnwindData |  |
| 152 | `LdrOpenImageFileOptionsKey` | `0x109FA0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `RtlCreateEnvironment` | `0x10A190` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1801 | `TpSetPoolWorkerThreadIdleTimeout` | `0x10A290` | 80 | UnwindData |  |
| 1694 | `RtlZeroMemory` | `0x10A2F0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `RtlQueryTokenHostIdAsUlong64` | `0x10A380` | 173 | UnwindData |  |
| 1566 | `RtlTestBit` | `0x10A690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `LdrGetKnownDllSectionHandle` | `0x10A6B0` | 381 | UnwindData |  |
| 950 | `RtlDoesFileExists_U` | `0x10A840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `RtlAllocateWnfSerializationGroup` | `0x10A850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1433 | `RtlReadThreadProfilingData` | `0x10A870` | 359 | UnwindData |  |
| 1251 | `RtlIsElevatedRid` | `0x10ACE0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `AlpcMaxAllowedMessageLength` | `0x10AD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1552 | `RtlStartRXact` | `0x10AD70` | 91 | UnwindData |  |
| 162 | `LdrRegisterDllNotification` | `0x10AF80` | 195 | UnwindData |  |
| 1108 | `RtlGetLengthWithoutLastFullDosOrNtPathElement` | `0x10B210` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `RtlNewSecurityObjectWithMultipleInheritance` | `0x10B2B0` | 80 | UnwindData |  |
| 729 | `RtlAddActionToRXact` | `0x10B310` | 67 | UnwindData |  |
| 731 | `RtlAddAttributeActionToRXact` | `0x10B360` | 491 | UnwindData |  |
| 951 | `RtlDoesNameContainWildCards` | `0x10BA60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `RtlFlsFree` | `0x10BAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1247 | `RtlIsCurrentThread` | `0x10BAD0` | 40 | UnwindData |  |
| 747 | `RtlAddVectoredExceptionHandler` | `0x10BB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1568 | `RtlTestProtectedAccess` | `0x10BB10` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 744 | `RtlAddSIDToBoundaryDescriptor` | `0x10BC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `LdrResRelease` | `0x10BC90` | 630 | UnwindData |  |
| 41 | `CsrIdentifyAlertableThread` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `LdrSetAppCompatDllRedirectionCallback` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `RtlAddRefMemoryStream` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1184 | `RtlInitializeAtomPackage` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1442 | `RtlReleaseMemoryStream` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1462 | `RtlReportSqmEscalation` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `RtlSetThreadPoolStartFunc` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1824 | `WinSqmCheckEscalationAddToStreamEx` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1825 | `WinSqmCheckEscalationSetDWORD` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1826 | `WinSqmCheckEscalationSetDWORD64` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1827 | `WinSqmCheckEscalationSetString` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1834 | `WinSqmEventEnabled` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1835 | `WinSqmEventWrite` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1836 | `WinSqmGetEscalationRuleStatus` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1839 | `WinSqmIsOptedIn` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1840 | `WinSqmIsOptedInEx` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1850 | `WinSqmStartSqmOptinListener` | `0x10C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1261 | `RtlIsNonEmptyDirectoryReparsePointAllowed` | `0x10C080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `AlpcRegisterCompletionList` | `0x10C0A0` | 76 | UnwindData |  |
| 1631 | `RtlUpdateClonedCriticalSection` | `0x10C3F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `RtlGetTokenNamedObjectPath` | `0x10C420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1130 | `RtlGetSecurityDescriptorRMControl` | `0x10C440` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `LdrAddDllDirectory` | `0x10C470` | 612 | UnwindData |  |
| 1456 | `RtlRemoveVectoredExceptionHandler` | `0x10C6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `LdrSetDllManifestProber` | `0x10C6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1772 | `TpCallbackSetEventOnCompletion` | `0x10C710` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1799 | `TpSetPoolThreadBasePriority` | `0x10C750` | 78 | UnwindData |  |
| 1255 | `RtlIsGenericTableEmptyAvl` | `0x10C7B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `RtlFindLeastSignificantBit` | `0x10C7F0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1179 | `RtlInitUTF8String` | `0x10CB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `LdrSetDefaultDllDirectories` | `0x10CB60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 854 | `RtlCopyString` | `0x10CBA0` | 52 | UnwindData |  |
| 1082 | `RtlGetCurrentThreadPrimaryGroup` | `0x10CE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `RtlFreeUserFiberShadowStack` | `0x10CEB0` | 39 | UnwindData |  |
| 725 | `RtlAddAccessDeniedAceEx` | `0x10CEE0` | 30 | UnwindData |  |
| 1220 | `RtlInterlockedPushListSListEx` | `0x10CF10` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1278 | `RtlKnownExceptionFilter` | `0x10D070` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `LdrProcessInitializationComplete` | `0x10D0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `RtlCreateHashTable` | `0x10D100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1125 | `RtlGetProcessPreferredUILanguages` | `0x10D120` | 242 | UnwindData |  |
| 730 | `RtlAddAtomToAtomTable` | `0x10D3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `RtlComputeCrc32` | `0x10D3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1342 | `RtlNumberOfSetBitsEx` | `0x10D400` | 353 | UnwindData |  |
| 2348 | `_errno` | `0x10D570` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1520 | `RtlSetProxiedProcessId` | `0x10D670` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1523 | `RtlSetSecurityDescriptorRMControl` | `0x10D6A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 795 | `RtlCheckSandboxedToken` | `0x10D720` | 89 | UnwindData |  |
| 940 | `RtlDestroyMemoryBlockLookaside` | `0x10D780` | 84 | UnwindData |  |
| 941 | `RtlDestroyMemoryZone` | `0x10D7E0` | 93 | UnwindData |  |
| 199 | `MicrosoftTelemetryAssertTriggeredUM` | `0x10D850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `RtlQuerySecurityObject` | `0x10D870` | 813 | UnwindData |  |
| 933 | `RtlDeregisterWait` | `0x10E1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `LdrFlushAlternateResourceModules` | `0x10E200` | 255 | UnwindData |  |
| 1028 | `RtlFindMostSignificantBit` | `0x10E310` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1324 | `RtlNewSecurityObject` | `0x10E340` | 64 | UnwindData |  |
| 1610 | `RtlUnlockCurrentThread` | `0x10E390` | 168 | UnwindData |  |
| 1540 | `RtlSetUserFlagsHeap` | `0x10E620` | 847 | UnwindData |  |
| 733 | `RtlAddAuditAccessAceEx` | `0x10E9F0` | 62 | UnwindData |  |
| 1779 | `TpDisablePoolCallbackChecks` | `0x10EE00` | 64 | UnwindData |  |
| 1453 | `RtlRemovePrivileges` | `0x10EE50` | 254 | UnwindData |  |
| 123 | `LdrFastFailInLoaderCallout` | `0x10EF60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `DbgUiWaitStateChange` | `0x10EF90` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 835 | `RtlConvertHostPerfCounterToPerfCounter` | `0x10F000` | 157 | UnwindData |  |
| 1406 | `RtlQueryTimeZoneInformation` | `0x10F0B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1793 | `TpSetDefaultPoolMaxThreads` | `0x10F0C0` | 323 | UnwindData |  |
| 1664 | `RtlWow64CallFunction64` | `0x10F210` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1667 | `RtlWow64EnableFsRedirection` | `0x10F210` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `RtlWow64EnableFsRedirectionEx` | `0x10F210` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1741 | `RtlpWow64GetContextOnAmd64` | `0x10F210` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1742 | `RtlpWow64SetContextOnAmd64` | `0x10F210` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1490 | `RtlSetBitEx` | `0x10F370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1120 | `RtlGetNtVersionNumbers` | `0x10F380` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `EtwReplyNotification` | `0x10F3D0` | 68 | UnwindData |  |
| 834 | `RtlConvertExclusiveToShared` | `0x110480` | 71 | UnwindData |  |
| 1485 | `RtlSendMsgToSm` | `0x1104D0` | 172 | UnwindData |  |
| 116 | `LdrCallEnclave` | `0x110590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1109 | `RtlGetLengthWithoutTrailingPathSeperators` | `0x1105A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `AlpcAdjustCompletionListConcurrencyCount` | `0x110600` | 34 | UnwindData |  |
| 1189 | `RtlInitializeCorrelationVector` | `0x1106E0` | 122 | UnwindData |  |
| 1097 | `RtlGetFrame` | `0x110840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1687 | `RtlWow64SuspendThread` | `0x110860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `RtlSetThreadIsCritical` | `0x110870` | 159 | UnwindData |  |
| 1475 | `RtlRunEncodeUnicodeString` | `0x110920` | 169 | UnwindData |  |
| 137 | `LdrGetFileNameFromLoadAsDataTable` | `0x110A30` | 83 | UnwindData |  |
| 1480 | `RtlSecondsSince1970ToTime` | `0x110A90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `RtlEthernetAddressToStringW` | `0x110AC0` | 102 | UnwindData |  |
| 52 | `DbgUiContinue` | `0x110C30` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `EtwCheckCoverage` | `0x110D30` | 69 | UnwindData |  |
| 1828 | `WinSqmCommonDatapointDelete` | `0x110DF0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1829 | `WinSqmCommonDatapointSetDWORD` | `0x110DF0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1830 | `WinSqmCommonDatapointSetDWORD64` | `0x110DF0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1831 | `WinSqmCommonDatapointSetStreamEx` | `0x110DF0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1832 | `WinSqmCommonDatapointSetString` | `0x110DF0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1841 | `WinSqmIsSessionDisabled` | `0x110DF0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1844 | `WinSqmSetEscalationInfo` | `0x110DF0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `RtlEqualWnfChangeStamps` | `0x111000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1399 | `RtlQueryRegistryValues` | `0x111010` | 30 | UnwindData |  |
| 1766 | `TpCallbackLeaveCriticalSectionOnCompletion` | `0x111040` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `LdrVerifyImageMatchesChecksumEx` | `0x111070` | 968 | UnwindData |  |
| 163 | `LdrRemoveDllDirectory` | `0x111440` | 239 | UnwindData |  |
| 938 | `RtlDestroyHandleTable` | `0x111540` | 104 | UnwindData |  |
| 1030 | `RtlFindSetBits` | `0x1115B0` | 934 | UnwindData |  |
| 861 | `RtlCreateAtomTable` | `0x111960` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1008 | `RtlExtractBitMap` | `0x111A40` | 412 | UnwindData |  |
| 187 | `LdrUnregisterDllNotification` | `0x111E50` | 155 | UnwindData |  |
| 1504 | `RtlSetFeatureConfigurations` | `0x1120A0` | 248 | UnwindData |  |
| 1043 | `RtlFlushHeaps` | `0x1121A0` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `LdrCreateEnclave` | `0x112490` | 254 | UnwindData |  |
| 1619 | `RtlUnsubscribeWnfNotificationWithCompletionCallback` | `0x1126D0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1141 | `RtlGetThreadLangIdByIndex` | `0x1127D0` | 230 | UnwindData |  |
| 1474 | `RtlRunDecodeUnicodeString` | `0x112E00` | 87 | UnwindData |  |
| 161 | `LdrQueryProcessModuleInformation` | `0x112EF0` | 33 | UnwindData |  |
| 1666 | `RtlWow64ChangeThreadState` | `0x112F20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `PssNtFreeRemoteSnapshot` | `0x112F50` | 548 | UnwindData |  |
| 828 | `RtlConnectToSm` | `0x113180` | 465 | UnwindData |  |
| 1496 | `RtlSetCurrentEnvironment` | `0x113390` | 162 | UnwindData |  |
| 53 | `DbgUiConvertStateChangeStructure` | `0x113440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `RtlGetProcessHeaps` | `0x113450` | 121 | UnwindData |  |
| 1632 | `RtlUpdateClonedSRWLock` | `0x1138B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `AlpcRundownCompletionList` | `0x1138D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1500 | `RtlSetEnvironmentStrings` | `0x113950` | 296 | UnwindData |  |
| 786 | `RtlCapabilityCheckForSingleSessionSku` | `0x113C10` | 96 | UnwindData |  |
| 1009 | `RtlFillMemory` | `0x113D50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1266 | `RtlIsPartialPlaceholderFileHandle` | `0x113D90` | 87 | UnwindData |  |
| 1663 | `RtlWnfDllUnloadCallback` | `0x113E70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `AlpcUnregisterCompletionList` | `0x113EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `PssNtFreeWalkMarker` | `0x113EC0` | 42 | UnwindData |  |
| 1526 | `RtlSetSystemBootStatus` | `0x113EF0` | 90 | UnwindData |  |
| 746 | `RtlAddVectoredContinueHandler` | `0x113F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 724 | `RtlAddAccessDeniedAce` | `0x113F70` | 31 | UnwindData |  |
| 1072 | `RtlGetCallersAddress` | `0x114080` | 103 | UnwindData |  |
| 1517 | `RtlSetProcessPlaceholderCompatibilityMode` | `0x114110` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1134 | `RtlGetSystemBootStatus` | `0x114380` | 90 | UnwindData |  |
| 1006 | `RtlExtendMemoryBlockLookaside` | `0x1143E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `LdrFindResourceDirectory_U` | `0x1143F0` | 26 | UnwindData |  |
| 812 | `RtlCommitDebugInfo` | `0x114410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `RtlDeCommitDebugInfo` | `0x114420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `RtlCheckSystemBootStatusIntegrity` | `0x114430` | 92 | UnwindData |  |
| 998 | `RtlEthernetStringToAddressW` | `0x1144A0` | 305 | UnwindData |  |
| 40 | `CsrGetProcessId` | `0x1149E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `RtlDestroyAtomTable` | `0x114A00` | 170 | UnwindData |  |
| 994 | `RtlEraseUnicodeString` | `0x114E20` | 57 | UnwindData |  |
| 1352 | `RtlOwnerAcesPresent` | `0x114E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1848 | `WinSqmStartSession` | `0x114E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1849 | `WinSqmStartSessionForPartner` | `0x114E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 857 | `RtlCrc64` | `0x114E80` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `RtlGetCriticalSectionRecursionCount` | `0x114FF0` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1699 | `RtlpConvertAbsoluteToRelativeSecurityAttribute` | `0x115300` | 928 | UnwindData |  |
| 1710 | `RtlpGetUserOrMachineUILanguage4NLS` | `0x115920` | 480 | UnwindData |  |
| 771 | `RtlAreAnyAccessesGranted` | `0x115E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 923 | `RtlDeleteRegistryValue` | `0x115E50` | 141 | UnwindData |  |
| 115 | `LdrAppxHandleIntegrityFailure` | `0x1164B0` | 532 | UnwindData |  |
| 1717 | `RtlpMuiRegCreateRegistryInfo` | `0x117500` | 50 | UnwindData |  |
| 738 | `RtlAddIntegrityLabelToBoundaryDescriptor` | `0x117D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `DbgUiConvertStateChangeStructureEx` | `0x117DA0` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `LdrQueryOptionalDelayLoadedAPI` | `0x1182B0` | 188 | UnwindData |  |
| 51 | `DbgUiConnectToDbg` | `0x118380` | 110 | UnwindData |  |
| 1244 | `RtlIsCriticalSectionLocked` | `0x118A70` | 2,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1503 | `RtlSetExtendedFeaturesMask` | `0x119560` | 44 | UnwindData |  |
| 1252 | `RtlIsEnclaveFeaturePresent` | `0x119620` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `A_SHAFinal` | `0x119750` | 246 | UnwindData |  |
| 10 | `A_SHAInit` | `0x119850` | 221 | UnwindData |  |
| 11 | `A_SHAUpdate` | `0x119940` | 249 | UnwindData |  |
| 196 | `MD5Final` | `0x119A40` | 301 | UnwindData |  |
| 197 | `MD5Init` | `0x119B80` | 138 | UnwindData |  |
| 198 | `MD5Update` | `0x119C10` | 247 | UnwindData |  |
| 701 | `PssNtCaptureSnapshot` | `0x119D10` | 1,210 | UnwindData |  |
| 1383 | `RtlQueryInternalFeatureConfiguration` | `0x11C750` | 179 | UnwindData |  |
| 1284 | `RtlLengthCurrentClearRunForwardEx` | `0x11D480` | 219 | UnwindData |  |
| 1127 | `RtlGetReturnAddressHijackTarget` | `0x11EE00` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `RtlUnhandledExceptionFilter2` | `0x11F5B0` | 975 | UnwindData |  |
| 898 | `RtlDeNormalizeProcessParams` | `0x11FD20` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `RtlGetSystemBootStatusEx` | `0x11FE00` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1527 | `RtlSetSystemBootStatusEx` | `0x120310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1398 | `RtlQueryRegistryValueWithFallback` | `0x120330` | 355 | UnwindData |  |
| 1700 | `RtlpConvertCultureNamesToLCIDs` | `0x1204A0` | 497 | UnwindData |  |
| 1101 | `RtlGetFunctionTableListHead` | `0x1206C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `RtlInitializeNtUserPfn` | `0x120710` | 282 | UnwindData |  |
| 1465 | `RtlResetNtUserPfn` | `0x120830` | 112 | UnwindData |  |
| 1472 | `RtlRetrieveNtUserPfn` | `0x1208B0` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `DbgBreakPoint` | `0x120C50` | 2 | UnwindData |  |
| 62 | `DbgUserBreakPoint` | `0x120C60` | 2 | UnwindData |  |
| 787 | `RtlCaptureContext` | `0x120D70` | 175 | UnwindData |  |
| 788 | `RtlCaptureContext2` | `0x120EB0` | 256 | UnwindData |  |
| 1419 | `RtlRaiseNoncontinuableException` | `0x121540` | 112 | UnwindData |  |
| 2340 | `__C_specific_handler` | `0x121810` | 455 | UnwindData |  |
| 2342 | `__isascii` | `0x1219E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2343 | `__iscsym` | `0x121A00` | 45 | UnwindData |  |
| 2344 | `__iscsymf` | `0x121A40` | 58 | UnwindData |  |
| 2346 | `__toascii` | `0x121A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2428 | `isalnum` | `0x121A90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2429 | `isalpha` | `0x121AC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2430 | `iscntrl` | `0x121AF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2431 | `isdigit` | `0x121B20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2432 | `isgraph` | `0x121B50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2433 | `islower` | `0x121B80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2434 | `isprint` | `0x121BB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2435 | `ispunct` | `0x121BE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2436 | `isspace` | `0x121C10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2437 | `isupper` | `0x121C40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2448 | `isxdigit` | `0x121C70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2347 | `_atoi64` | `0x121CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2420 | `atoi` | `0x121CC0` | 31 | UnwindData |  |
| 2421 | `atol` | `0x121CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2350 | `_i64toa` | `0x121D10` | 41 | UnwindData |  |
| 2354 | `_itoa` | `0x121D40` | 40 | UnwindData |  |
| 2360 | `_ltoa` | `0x121D40` | 40 | UnwindData |  |
| 2387 | `_ui64toa` | `0x121D70` | 26 | UnwindData |  |
| 2391 | `_ultoa` | `0x121D90` | 26 | UnwindData |  |
| 2352 | `_i64tow` | `0x121EA0` | 41 | UnwindData |  |
| 2356 | `_itow` | `0x121ED0` | 40 | UnwindData |  |
| 2362 | `_ltow` | `0x121ED0` | 40 | UnwindData |  |
| 2389 | `_ui64tow` | `0x121F00` | 26 | UnwindData |  |
| 2393 | `_ultow` | `0x121F20` | 26 | UnwindData |  |
| 2358 | `_lfind` | `0x122070` | 164 | UnwindData |  |
| 2359 | `_local_unwind` | `0x122120` | 40 | UnwindData |  |
| 2365 | `_memccpy` | `0x122150` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2366 | `_memicmp` | `0x1221F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2369 | `_snprintf` | `0x122210` | 174 | UnwindData |  |
| 2372 | `_snwprintf` | `0x1222D0` | 229 | UnwindData |  |
| 2375 | `_splitpath` | `0x1223C0` | 136 | UnwindData |  |
| 2377 | `_strcmpi` | `0x122720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2378 | `_stricmp` | `0x122720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2379 | `_strlwr` | `0x122730` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2380 | `_strlwr_s` | `0x122760` | 98 | UnwindData |  |
| 2381 | `_strnicmp` | `0x122830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2384 | `_strupr` | `0x122840` | 70 | UnwindData |  |
| 2385 | `_strupr_s` | `0x122890` | 98 | UnwindData |  |
| 2386 | `_swprintf` | `0x122900` | 188 | UnwindData |  |
| 2490 | `swprintf` | `0x122900` | 188 | UnwindData |  |
| 2395 | `_vscprintf` | `0x1229D0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2500 | `vsprintf` | `0x122AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2396 | `_vscwprintf` | `0x122B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2401 | `_vswprintf` | `0x122B20` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2397 | `_vsnprintf` | `0x122BF0` | 22 | UnwindData |  |
| 2399 | `_vsnwprintf` | `0x122CD0` | 22 | UnwindData |  |
| 2402 | `_wcsicmp` | `0x122DE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2403 | `_wcslwr` | `0x122E40` | 78 | UnwindData |  |
| 2404 | `_wcslwr_s` | `0x122EA0` | 116 | UnwindData |  |
| 2405 | `_wcsnicmp` | `0x122F20` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2406 | `_wcsnset_s` | `0x122F90` | 137 | UnwindData |  |
| 2407 | `_wcsset_s` | `0x123020` | 86 | UnwindData |  |
| 2408 | `_wcstoi64` | `0x123080` | 41 | UnwindData |  |
| 2409 | `_wcstoui64` | `0x1230B0` | 44 | UnwindData |  |
| 2410 | `_wcsupr` | `0x123350` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2411 | `_wcsupr_s` | `0x123380` | 116 | UnwindData |  |
| 2414 | `_wtoi` | `0x123400` | 31 | UnwindData |  |
| 2415 | `_wtoi64` | `0x123430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2416 | `_wtol` | `0x123450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2417 | `abs` | `0x123470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2449 | `labs` | `0x123470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2418 | `atan` | `0x123480` | 608 | UnwindData |  |
| 2419 | `atan2` | `0x1236F0` | 307 | UnwindData |  |
| 2422 | `bsearch` | `0x123EB0` | 244 | UnwindData |  |
| 2423 | `bsearch_s` | `0x123FB0` | 262 | UnwindData |  |
| 2424 | `ceil` | `0x1240C0` | 273 | UnwindData |  |
| 2425 | `cos` | `0x1241E0` | 729 | UnwindData |  |
| 2463 | `sin` | `0x124570` | 359 | UnwindData |  |
| 2426 | `fabs` | `0x124990` | 248 | UnwindData |  |
| 2427 | `floor` | `0x124A90` | 255 | UnwindData |  |
| 2438 | `iswalnum` | `0x124BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2439 | `iswalpha` | `0x124BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2440 | `iswascii` | `0x124BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2442 | `iswdigit` | `0x124C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2443 | `iswgraph` | `0x124C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2444 | `iswlower` | `0x124C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2445 | `iswprint` | `0x124C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2446 | `iswspace` | `0x124C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2447 | `iswxdigit` | `0x124C50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2441 | `iswctype` | `0x124C90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2450 | `log` | `0x124CC0` | 764 | UnwindData |  |
| 2451 | `longjmp` | `0x124FD0` | 40 | UnwindData |  |
| 2452 | `mbstowcs` | `0x125000` | 197 | UnwindData |  |
| 2453 | `memchr` | `0x1250F0` | 144 | UnwindData |  |
| 2460 | `pow` | `0x125190` | 2,993 | UnwindData |  |
| 2461 | `qsort` | `0x125D50` | 126 | UnwindData |  |
| 2462 | `qsort_s` | `0x126110` | 141 | UnwindData |  |
| 2464 | `sprintf` | `0x126500` | 151 | UnwindData |  |
| 2466 | `sqrt` | `0x1265A0` | 273 | UnwindData |  |
| 2467 | `sscanf` | `0x1266D0` | 55 | UnwindData |  |
| 2471 | `strchr` | `0x1267C0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2475 | `strcspn` | `0x126850` | 134 | UnwindData |  |
| 2482 | `strnlen` | `0x1268F0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2483 | `strpbrk` | `0x126A40` | 112 | UnwindData |  |
| 2484 | `strrchr` | `0x126AC0` | 317 | UnwindData |  |
| 2485 | `strspn` | `0x126C10` | 138 | UnwindData |  |
| 2486 | `strstr` | `0x126CA0` | 492 | UnwindData |  |
| 2488 | `strtol` | `0x1270D0` | 40 | UnwindData |  |
| 2489 | `strtoul` | `0x127130` | 43 | UnwindData |  |
| 2493 | `tan` | `0x127170` | 796 | UnwindData |  |
| 2494 | `tolower` | `0x1276A0` | 45 | UnwindData |  |
| 2495 | `toupper` | `0x1276E0` | 97 | UnwindData |  |
| 2496 | `towlower` | `0x127750` | 37 | UnwindData |  |
| 2497 | `towupper` | `0x127780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2503 | `wcscat` | `0x127790` | 47 | UnwindData |  |
| 2507 | `wcscpy` | `0x1277D0` | 57 | UnwindData |  |
| 2505 | `wcschr` | `0x127810` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2506 | `wcscmp` | `0x127890` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2509 | `wcscspn` | `0x1278D0` | 94 | UnwindData |  |
| 2510 | `wcslen` | `0x127940` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2511 | `wcsncat` | `0x127A60` | 99 | UnwindData |  |
| 2513 | `wcsncmp` | `0x127AD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2514 | `wcsncpy` | `0x127B10` | 119 | UnwindData |  |
| 2516 | `wcsnlen` | `0x127B90` | 453 | UnwindData |  |
| 2517 | `wcspbrk` | `0x127D60` | 77 | UnwindData |  |
| 2518 | `wcsrchr` | `0x127DC0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2519 | `wcsspn` | `0x127E80` | 94 | UnwindData |  |
| 2520 | `wcsstr` | `0x127EF0` | 534 | UnwindData |  |
| 2522 | `wcstol` | `0x128340` | 40 | UnwindData |  |
| 2524 | `wcstoul` | `0x1283A0` | 43 | UnwindData |  |
| 2523 | `wcstombs` | `0x1283E0` | 118 | UnwindData |  |
| 2351 | `_i64toa_s` | `0x12C740` | 36 | UnwindData |  |
| 2355 | `_itoa_s` | `0x12C770` | 35 | UnwindData |  |
| 2361 | `_ltoa_s` | `0x12C770` | 35 | UnwindData |  |
| 2388 | `_ui64toa_s` | `0x12C7A0` | 20 | UnwindData |  |
| 2392 | `_ultoa_s` | `0x12C7C0` | 20 | UnwindData |  |
| 2353 | `_i64tow_s` | `0x12CA40` | 36 | UnwindData |  |
| 2357 | `_itow_s` | `0x12CA70` | 35 | UnwindData |  |
| 2363 | `_ltow_s` | `0x12CA70` | 35 | UnwindData |  |
| 2390 | `_ui64tow_s` | `0x12CAA0` | 20 | UnwindData |  |
| 2394 | `_ultow_s` | `0x12CAC0` | 20 | UnwindData |  |
| 2364 | `_makepath_s` | `0x12CD60` | 334 | UnwindData |  |
| 2370 | `_snprintf_s` | `0x12CEC0` | 30 | UnwindData |  |
| 2398 | `_vsnprintf_s` | `0x12CEF0` | 152 | UnwindData |  |
| 2371 | `_snscanf_s` | `0x12CF90` | 57 | UnwindData |  |
| 2373 | `_snwprintf_s` | `0x12CFD0` | 30 | UnwindData |  |
| 2400 | `_vsnwprintf_s` | `0x12D000` | 163 | UnwindData |  |
| 2374 | `_snwscanf_s` | `0x12D0B0` | 57 | UnwindData |  |
| 2376 | `_splitpath_s` | `0x12D0F0` | 654 | UnwindData |  |
| 2382 | `_strnset_s` | `0x12D390` | 131 | UnwindData |  |
| 2383 | `_strset_s` | `0x12D420` | 82 | UnwindData |  |
| 2412 | `_wmakepath_s` | `0x12D480` | 381 | UnwindData |  |
| 2413 | `_wsplitpath_s` | `0x12D610` | 687 | UnwindData |  |
| 2456 | `memcpy_s` | `0x12D8D0` | 140 | UnwindData |  |
| 2458 | `memmove_s` | `0x12D970` | 88 | UnwindData |  |
| 2465 | `sprintf_s` | `0x12D9D0` | 30 | UnwindData |  |
| 2501 | `vsprintf_s` | `0x12DA00` | 72 | UnwindData |  |
| 2468 | `sscanf_s` | `0x12DA50` | 77 | UnwindData |  |
| 2470 | `strcat_s` | `0x12DAB0` | 137 | UnwindData |  |
| 2474 | `strcpy_s` | `0x12DB40` | 127 | UnwindData |  |
| 2478 | `strncat_s` | `0x12DBD0` | 245 | UnwindData |  |
| 2481 | `strncpy_s` | `0x12DCD0` | 235 | UnwindData |  |
| 2487 | `strtok_s` | `0x12DDD0` | 348 | UnwindData |  |
| 2491 | `swprintf_s` | `0x12DF40` | 30 | UnwindData |  |
| 2502 | `vswprintf_s` | `0x12DF70` | 82 | UnwindData |  |
| 2492 | `swscanf_s` | `0x12DFD0` | 78 | UnwindData |  |
| 2504 | `wcscat_s` | `0x12E030` | 144 | UnwindData |  |
| 2508 | `wcscpy_s` | `0x12E0D0` | 132 | UnwindData |  |
| 2512 | `wcsncat_s` | `0x12E160` | 264 | UnwindData |  |
| 2515 | `wcsncpy_s` | `0x12E270` | 254 | UnwindData |  |
| 2521 | `wcstok_s` | `0x12E380` | 249 | UnwindData |  |
| 769 | `RtlAppxIsFileOwnedByTrustedInstaller` | `0x131CC0` | 367 | UnwindData |  |
| 36 | `CsrCaptureTimeout` | `0x131E40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `CsrVerifyRegion` | `0x131E70` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1250 | `RtlIsEcCode` | `0x131E70` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `RtlApplicationVerifierStop` | `0x132160` | 155 | UnwindData |  |
| 1665 | `RtlWow64ChangeProcessState` | `0x1322F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1676 | `RtlWow64GetThreadContext` | `0x132320` | 35 | UnwindData |  |
| 1677 | `RtlWow64GetThreadSelectorEntry` | `0x132350` | 426 | UnwindData |  |
| 1685 | `RtlWow64SetThreadContext` | `0x132500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `RtlWow64SuspendProcess` | `0x132520` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 946 | `RtlDisableThreadProfiling` | `0x1329C0` | 101 | UnwindData |  |
| 968 | `RtlEnableThreadProfiling` | `0x132A30` | 244 | UnwindData |  |
| 1405 | `RtlQueryThreadProfiling` | `0x132B30` | 34 | UnwindData |  |
| 55 | `DbgUiDebugActiveProcess` | `0x132B60` | 76 | UnwindData |  |
| 56 | `DbgUiGetThreadDebugObject` | `0x132BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `DbgUiIssueRemoteBreakin` | `0x132BE0` | 318 | UnwindData |  |
| 58 | `DbgUiRemoteBreakin` | `0x132D30` | 88 | UnwindData |  |
| 59 | `DbgUiSetThreadDebugObject` | `0x132D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `DbgUiStopDebugging` | `0x132DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `LdrDeleteEnclave` | `0x132DD0` | 238 | UnwindData |  |
| 808 | `RtlCloneMemoryStream` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `RtlCommitMemoryStream` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `RtlCopyMemoryStreamTo` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | `RtlCopyOutOfProcessMemoryStreamTo` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `RtlLockMemoryStreamRegion` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1382 | `RtlQueryInterfaceMemoryStream` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `RtlReadMemoryStream` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1432 | `RtlReadOutOfProcessMemoryStream` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1473 | `RtlRevertMemoryStream` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1482 | `RtlSeekMemoryStream` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `RtlSetMemoryStreamSize` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1553 | `RtlStatMemoryStream` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1613 | `RtlUnlockMemoryStreamRegion` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1688 | `RtlWriteMemoryStream` | `0x133070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `RtlCreateProcessReflection` | `0x133080` | 1,432 | UnwindData |  |
| 840 | `RtlConvertToAutoInheritSecurityObject` | `0x1339B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `RtlCreateUserSecurityObject` | `0x1339C0` | 148 | UnwindData |  |
| 1322 | `RtlNewInstanceSecurityObject` | `0x133A60` | 319 | UnwindData |  |
| 1323 | `RtlNewSecurityGrantedAccess` | `0x133BB0` | 349 | UnwindData |  |
| 1515 | `RtlSetProcessDebugInformation` | `0x133D20` | 488 | UnwindData |  |
| 1728 | `RtlpQueryProcessDebugInformationFromWow64` | `0x133FD0` | 152 | UnwindData |  |
| 1729 | `RtlpQueryProcessDebugInformationRemote` | `0x134070` | 233 | UnwindData |  |
| 1455 | `RtlRemoveVectoredContinueHandler` | `0x1341E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1414 | `RtlQueueApcWow64Thread` | `0x1341F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1460 | `RtlReportExceptionEx` | `0x134210` | 1,150 | UnwindData |  |
| 1662 | `RtlWerpReportException` | `0x1346A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1819 | `WerReportExceptionWorker` | `0x1346B0` | 163 | UnwindData |  |
| 1750 | `ShipAssertGetBufferInfo` | `0x134760` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1751 | `ShipAssertMsgA` | `0x134790` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1752 | `ShipAssertMsgW` | `0x134790` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1837 | `WinSqmGetInstrumentationProperty` | `0x1349B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1695 | `RtlZombifyActivationContext` | `0x1349D0` | 112 | UnwindData |  |
| 1240 | `RtlIsActivationContextActive` | `0x134A50` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 826 | `RtlComputeImportTableHash` | `0x134DE0` | 664 | UnwindData |  |
| 14 | `AlpcGetCompletionListLastMessageInformation` | `0x1366F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `AlpcGetCompletionListMessageAttributes` | `0x136710` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `DbgPrintReturnControlC` | `0x136750` | 64 | UnwindData |  |
| 48 | `DbgPrompt` | `0x1367A0` | 74 | UnwindData |  |
| 49 | `DbgQueryDebugFilterState` | `0x1367F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `DbgSetDebugFilterState` | `0x136800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2498 | `vDbgPrintEx` | `0x136810` | 40 | UnwindData |  |
| 2499 | `vDbgPrintExWithPrefix` | `0x136840` | 30 | UnwindData |  |
| 121 | `LdrEnumResources` | `0x136870` | 698 | UnwindData |  |
| 178 | `LdrSetMUICacheType` | `0x136B30` | 98 | UnwindData |  |
| 888 | `RtlCreateUserProcess` | `0x136C80` | 128 | UnwindData |  |
| 1507 | `RtlSetImageMitigationPolicy` | `0x136D10` | 4,357 | UnwindData |  |
| 1639 | `RtlValidProcessProtection` | `0x137E20` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `LdrProcessRelocationBlock` | `0x138150` | 37 | UnwindData |  |
| 155 | `LdrProcessRelocationBlockEx` | `0x138180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `RtlQueryModuleInformation` | `0x138190` | 659 | UnwindData |  |
| 165 | `LdrResFindResource` | `0x138430` | 160 | UnwindData |  |
| 829 | `RtlConsoleMultiByteToUnicodeN` | `0x1384E0` | 357 | UnwindData |  |
| 1628 | `RtlUpcaseUnicodeToCustomCPN` | `0x138650` | 359 | UnwindData |  |
| 697 | `PfxFindPrefix` | `0x138A10` | 203 | UnwindData |  |
| 698 | `PfxInitialize` | `0x138AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 699 | `PfxInsertPrefix` | `0x138B10` | 270 | UnwindData |  |
| 700 | `PfxRemovePrefix` | `0x138C30` | 183 | UnwindData |  |
| 752 | `RtlAllocateAndInitializeSidEx` | `0x138CF0` | 190 | UnwindData |  |
| 845 | `RtlCopyLuidAndAttributesArray` | `0x138DC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `RtlCopySidAndAttributesArray` | `0x138DF0` | 173 | UnwindData |  |
| 988 | `RtlEqualLuid` | `0x138EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1131 | `RtlGetSessionProperties` | `0x138ED0` | 188 | UnwindData |  |
| 1272 | `RtlIsUntrustedObject` | `0x138FA0` | 389 | UnwindData |  |
| 1315 | `RtlMapSecurityErrorToNtStatus` | `0x139130` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `RtlNormalizeSecurityDescriptor` | `0x139240` | 728 | UnwindData |  |
| 1457 | `RtlReplaceSidInSd` | `0x139520` | 748 | UnwindData |  |
| 1488 | `RtlSetAttributesSecurityDescriptor` | `0x139820` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1544 | `RtlSidEqualLevel` | `0x139850` | 127 | UnwindData |  |
| 1547 | `RtlSidIsHigherLevel` | `0x1398E0` | 127 | UnwindData |  |
| 837 | `RtlConvertSRWLockExclusiveToShared` | `0x13A8F0` | 69 | UnwindData |  |
| 1588 | `RtlTryConvertSRWLockSharedToExclusiveOrRelease` | `0x13A940` | 116 | UnwindData |  |
| 964 | `RtlDumpResource` | `0x13A9C0` | 74 | UnwindData |  |
| 967 | `RtlEnableEarlyCriticalSectionEventCreation` | `0x13AA10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `RtlpUnWaitCriticalSection` | `0x13AA40` | 82 | UnwindData |  |
| 723 | `RtlAddAccessAllowedObjectAce` | `0x13AAA0` | 90 | UnwindData |  |
| 726 | `RtlAddAccessDeniedObjectAce` | `0x13AB00` | 90 | UnwindData |  |
| 727 | `RtlAddAccessFilterAce` | `0x13AB60` | 506 | UnwindData |  |
| 732 | `RtlAddAuditAccessAce` | `0x13AD60` | 57 | UnwindData |  |
| 734 | `RtlAddAuditAccessObjectAce` | `0x13ADA0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `RtlAddCompoundAce` | `0x13AE10` | 365 | UnwindData |  |
| 743 | `RtlAddResourceAttributeAce` | `0x13AF90` | 903 | UnwindData |  |
| 745 | `RtlAddScopedPolicyIDAce` | `0x13B320` | 380 | UnwindData |  |
| 1508 | `RtlSetInformationAcl` | `0x13B4B0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1702 | `RtlpConvertRelativeToAbsoluteSecurityAttribute` | `0x13B6A0` | 1,258 | UnwindData |  |
| 1354 | `RtlPinAtomInAtomTable` | `0x13BF10` | 173 | UnwindData |  |
| 1463 | `RtlResetMemoryBlockLookaside` | `0x13BFF0` | 83 | UnwindData |  |
| 1464 | `RtlResetMemoryZone` | `0x13C050` | 75 | UnwindData |  |
| 986 | `RtlEqualComputerName` | `0x13C0B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `RtlFreeOemString` | `0x13C0C0` | 24 | UnwindData |  |
| 1598 | `RtlUnicodeStringToCountedOemString` | `0x13C0E0` | 257 | UnwindData |  |
| 1625 | `RtlUpcaseUnicodeStringToAnsiString` | `0x13C1F0` | 225 | UnwindData |  |
| 1626 | `RtlUpcaseUnicodeStringToCountedOemString` | `0x13C2E0` | 257 | UnwindData |  |
| 761 | `RtlAppendAsciizToString` | `0x13C3F0` | 109 | UnwindData |  |
| 763 | `RtlAppendStringToString` | `0x13C470` | 77 | UnwindData |  |
| 1177 | `RtlInitStringEx` | `0x13C4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `RtlInitUTF8StringEx` | `0x13C4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1635 | `RtlUpperString` | `0x13C4E0` | 80 | UnwindData |  |
| 802 | `RtlClearAllBitsEx` | `0x13C540` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 804 | `RtlClearBitEx` | `0x13C570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 806 | `RtlClearBitsEx` | `0x13C580` | 177 | UnwindData |  |
| 841 | `RtlCopyBitMap` | `0x13C640` | 519 | UnwindData |  |
| 1019 | `RtlFindClearBitsAndSetEx` | `0x13C850` | 878 | UnwindData |  |
| 1020 | `RtlFindClearBitsEx` | `0x13CBD0` | 821 | UnwindData |  |
| 1031 | `RtlFindSetBitsAndClear` | `0x13CF10` | 955 | UnwindData |  |
| 1032 | `RtlFindSetBitsAndClearEx` | `0x13D2E0` | 944 | UnwindData |  |
| 1221 | `RtlInterlockedSetBitRun` | `0x13D6A0` | 177 | UnwindData |  |
| 1283 | `RtlLengthCurrentClearRunBackwardEx` | `0x13D760` | 157 | UnwindData |  |
| 1339 | `RtlNumberOfClearBitsEx` | `0x13D810` | 30 | UnwindData |  |
| 1340 | `RtlNumberOfClearBitsInRange` | `0x13D840` | 33 | UnwindData |  |
| 1343 | `RtlNumberOfSetBitsInRange` | `0x13D870` | 422 | UnwindData |  |
| 1487 | `RtlSetAllBitsEx` | `0x13DA20` | 102 | UnwindData |  |
| 1492 | `RtlSetBitsEx` | `0x13DA90` | 174 | UnwindData |  |
| 779 | `RtlBarrier` | `0x13DD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 780 | `RtlBarrierForDelete` | `0x13DD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | `RtlDeleteBarrier` | `0x13DD20` | 41 | UnwindData |  |
| 1170 | `RtlInitBarrier` | `0x13DD50` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `RtlInt64ToUnicodeString` | `0x13DE60` | 158 | UnwindData |  |
| 791 | `RtlCheckBootStatusIntegrity` | `0x13DF40` | 355 | UnwindData |  |
| 862 | `RtlCreateBootStatusDataFile` | `0x13E0B0` | 461 | UnwindData |  |
| 1132 | `RtlGetSetBootStatusData` | `0x13E290` | 379 | UnwindData |  |
| 1295 | `RtlLockBootStatusData` | `0x13E420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1467 | `RtlRestoreBootStatusDefaults` | `0x13E440` | 241 | UnwindData |  |
| 1470 | `RtlRestoreSystemBootStatusDefaults` | `0x13E540` | 54 | UnwindData |  |
| 1609 | `RtlUnlockBootStatusData` | `0x13E580` | 59 | UnwindData |  |
| 1514 | `RtlSetPortableOperatingSystem` | `0x13E8F0` | 59 | UnwindData |  |
| 876 | `RtlCreateRegistryKey` | `0x13E940` | 56 | UnwindData |  |
| 1370 | `RtlQueryDynamicTimeZoneInformation` | `0x13E980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1499 | `RtlSetDynamicTimeZoneInformation` | `0x13E990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1536 | `RtlSetTimeZoneInformation` | `0x13E9A0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 836 | `RtlConvertLCIDToString` | `0x13ED70` | 260 | UnwindData |  |
| 1698 | `RtlpCleanupRegistryKeys` | `0x13F380` | 1,100 | UnwindData |  |
| 1701 | `RtlpConvertLCIDsToCultureNames` | `0x13F7E0` | 539 | UnwindData |  |
| 1732 | `RtlpSetInstallLanguage` | `0x13FF50` | 1,176 | UnwindData |  |
| 1733 | `RtlpSetPreferredUILanguages` | `0x140560` | 3,030 | UnwindData |  |
| 1734 | `RtlpSetUserPreferredUILanguages` | `0x140560` | 3,030 | UnwindData |  |
| 1738 | `RtlpVerifyAndCommitUILanguageSettings` | `0x141140` | 368 | UnwindData |  |
| 810 | `RtlCmDecodeMemIoResource` | `0x141300` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 811 | `RtlCmEncodeMemIoResource` | `0x141370` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `RtlFindClosestEncodableLength` | `0x141450` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1222 | `RtlIoDecodeMemIoResource` | `0x141500` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `RtlIoEncodeMemIoResource` | `0x1415A0` | 394 | UnwindData |  |
| 979 | `RtlEnumProcessHeaps` | `0x141750` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `RtlMultipleAllocateHeap` | `0x141810` | 104 | UnwindData |  |
| 1321 | `RtlMultipleFreeHeap` | `0x141880` | 98 | UnwindData |  |
| 1403 | `RtlQueryTagHeap` | `0x1418F0` | 439 | UnwindData |  |
| 1645 | `RtlValidateProcessHeaps` | `0x141B90` | 32 | UnwindData |  |
| 815 | `RtlCompareAltitudes` | `0x142AF0` | 490 | UnwindData |  |
| 816 | `RtlCompareExchangePointerMapping` | `0x142CE0` | 318 | UnwindData |  |
| 817 | `RtlCompareExchangePropertyStore` | `0x142E30` | 546 | UnwindData |  |
| 1390 | `RtlQueryPointerMapping` | `0x143060` | 172 | UnwindData |  |
| 1396 | `RtlQueryPropertyStore` | `0x143120` | 128 | UnwindData |  |
| 1452 | `RtlRemovePointerMapping` | `0x1431B0` | 208 | UnwindData |  |
| 1454 | `RtlRemovePropertyStore` | `0x143290` | 202 | UnwindData |  |
| 905 | `RtlDecompressBuffer` | `0x143360` | 119 | UnwindData |  |
| 907 | `RtlDecompressFragment` | `0x1433E0` | 143 | UnwindData |  |
| 830 | `RtlConstructCrossVmEventPath` | `0x143560` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `RtlConstructCrossVmMutexPath` | `0x143560` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `RtlCreateHashTableEx` | `0x1436D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `RtlEndWeakEnumerationHashTable` | `0x1436E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `RtlInitStrongEnumerationHashTable` | `0x1436F0` | 65 | UnwindData |  |
| 1183 | `RtlInitWeakEnumerationHashTable` | `0x143740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1661 | `RtlWeaklyEnumerateEntryHashTable` | `0x143750` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `RtlLocalTimeToSystemTime` | `0x143780` | 112 | UnwindData |  |
| 1481 | `RtlSecondsSince1980ToTime` | `0x143800` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `RtlCopyExtendedContext` | `0x143830` | 26 | UnwindData |  |
| 1693 | `RtlZeroHeap` | `0x143D80` | 1,272 | UnwindData |  |
| 883 | `RtlCreateUmsCompletionList` | `0x144420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 884 | `RtlCreateUmsThreadContext` | `0x144420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `RtlDeleteUmsCompletionList` | `0x144420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | `RtlDeleteUmsThreadContext` | `0x144420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 931 | `RtlDequeueUmsCompletionListItems` | `0x144420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `RtlEnterUmsSchedulingMode` | `0x144420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `RtlExecuteUmsThread` | `0x144420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1115 | `RtlGetNextUmsListItem` | `0x144420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `RtlGetUmsCompletionListEvent` | `0x144420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `RtlQueryUmsThreadInformation` | `0x144420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `RtlSetUmsThreadInformation` | `0x144420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `RtlUmsThreadYield` | `0x144420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1084 | `RtlGetCurrentUmsThread` | `0x144430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1562 | `RtlSubtreeSuccessor` | `0x144450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 983 | `RtlEnumerateGenericTableLikeADirectory` | `0x144480` | 252 | UnwindData |  |
| 1088 | `RtlGetElementGenericTableAvl` | `0x144590` | 285 | UnwindData |  |
| 932 | `RtlDeregisterSecureMemoryCacheCallback` | `0x1446C0` | 172 | UnwindData |  |
| 1438 | `RtlRegisterSecureMemoryCacheCallback` | `0x144780` | 171 | UnwindData |  |
| 963 | `RtlDrainNonVolatileFlush` | `0x144B50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1044 | `RtlFlushNonVolatileMemory` | `0x144B80` | 126 | UnwindData |  |
| 995 | `RtlEthernetAddressToStringA` | `0x144C10` | 100 | UnwindData |  |
| 997 | `RtlEthernetStringToAddressA` | `0x144C80` | 298 | UnwindData |  |
| 1011 | `RtlFillNonVolatileMemory` | `0x144DB0` | 165 | UnwindData |  |
| 1045 | `RtlFlushNonVolatileMemoryRanges` | `0x144E60` | 136 | UnwindData |  |
| 1055 | `RtlFreeNonVolatileToken` | `0x144EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1116 | `RtlGetNonVolatileToken` | `0x144F10` | 130 | UnwindData |  |
| 1689 | `RtlWriteNonVolatileMemory` | `0x144FA0` | 172 | UnwindData |  |
| 1048 | `RtlFormatMessage` | `0x145060` | 81 | UnwindData |  |
| 1064 | `RtlGenerate8dot3Name` | `0x145230` | 1,227 | UnwindData |  |
| 1260 | `RtlIsNameLegalDOS8Dot3` | `0x145710` | 463 | UnwindData |  |
| 1074 | `RtlGetConsoleSessionForegroundProcessId` | `0x1459E0` | 49 | UnwindData |  |
| 1516 | `RtlSetProcessIsCritical` | `0x145A20` | 151 | UnwindData |  |
| 1692 | `RtlXSave` | `0x145AC0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `RtlGetFeatureToggleConfiguration` | `0x145B10` | 334 | UnwindData |  |
| 1095 | `RtlGetFeatureTogglesChangeToken` | `0x145C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `RtlNotifyFeatureToggleUsage` | `0x145C80` | 202 | UnwindData |  |
| 1158 | `RtlIdnToNameprepUnicode` | `0x1466A0` | 30 | UnwindData |  |
| 1188 | `RtlInitializeContext` | `0x1466E0` | 285 | UnwindData |  |
| 1450 | `RtlRemoteCall` | `0x146810` | 380 | UnwindData |  |
| 1267 | `RtlIsPartialPlaceholderFileInfo` | `0x1469A0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1395 | `RtlQueryProcessPlaceholderCompatibilityMode` | `0x146A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1277 | `RtlIsZeroMemory` | `0x146A50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `RtlIsFeatureEnabledForEnterprise` | `0x146AA0` | 119 | UnwindData |  |
| 1594 | `RtlUnhandledExceptionFilter` | `0x146FD0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `RtlLogUnexpectedCodepath` | `0x147040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1351 | `RtlOverwriteFeatureConfigurationBuffer` | `0x147050` | 168 | UnwindData |  |
| 1365 | `RtlQueryAllInternalFeatureConfigurations` | `0x147100` | 163 | UnwindData |  |
| 1366 | `RtlQueryAllInternalRuntimeFeatureConfigurations` | `0x1471B0` | 237 | UnwindData |  |
| 1559 | `RtlSubscribeForFeatureUsageNotification` | `0x1472B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `RtlUnsubscribeFromFeatureUsageNotifications` | `0x1472C0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1350 | `RtlOsDeploymentState` | `0x147380` | 322 | UnwindData |  |
| 1410 | `RtlQueryValidationRunlevel` | `0x1474D0` | 204 | UnwindData |  |
| 1416 | `RtlRaiseCustomSystemEventTrigger` | `0x1475B0` | 575 | UnwindData |  |
| 1425 | `RtlRcuAllocate` | `0x147990` | 196 | UnwindData |  |
| 1426 | `RtlRcuFree` | `0x147A60` | 166 | UnwindData |  |
| 1427 | `RtlRcuReadLock` | `0x147B10` | 99 | UnwindData |  |
| 1428 | `RtlRcuReadUnlock` | `0x147B80` | 76 | UnwindData |  |
| 1429 | `RtlRcuSynchronize` | `0x147BE0` | 193 | UnwindData |  |
| 1577 | `RtlTraceDatabaseAdd` | `0x147F20` | 112 | UnwindData |  |
| 1578 | `RtlTraceDatabaseCreate` | `0x147FA0` | 302 | UnwindData |  |
| 1579 | `RtlTraceDatabaseDestroy` | `0x1480E0` | 120 | UnwindData |  |
| 1580 | `RtlTraceDatabaseEnumerate` | `0x148160` | 203 | UnwindData |  |
| 1581 | `RtlTraceDatabaseFind` | `0x148240` | 120 | UnwindData |  |
| 1582 | `RtlTraceDatabaseLock` | `0x1482C0` | 30 | UnwindData |  |
| 1583 | `RtlTraceDatabaseUnlock` | `0x1482F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1584 | `RtlTraceDatabaseValidate` | `0x148310` | 50 | UnwindData |  |
| 1602 | `RtlUnicodeStringToUTF8String` | `0x148630` | 277 | UnwindData |  |
| 1592 | `RtlUdiv128` | `0x148750` | 111 | UnwindData |  |
| 1654 | `RtlWakeAddressAllNoFence` | `0x1487D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1656 | `RtlWakeAddressSingleNoFence` | `0x1487E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1680 | `RtlWow64PopAllCrossProcessWorkFromWorkList` | `0x1487F0` | 207 | UnwindData |  |
| 1681 | `RtlWow64PopCrossProcessWorkFromFreeList` | `0x1488D0` | 184 | UnwindData |  |
| 1682 | `RtlWow64PushCrossProcessWorkOntoFreeList` | `0x148990` | 201 | UnwindData |  |
| 1683 | `RtlWow64PushCrossProcessWorkOntoWorkList` | `0x148A60` | 648 | UnwindData |  |
| 1684 | `RtlWow64RequestCrossProcessHeavyFlush` | `0x148CF0` | 88 | UnwindData |  |
| 1730 | `RtlpRefreshCachedUILanguage` | `0x149A30` | 233 | UnwindData |  |
| 1721 | `RtlpNtCreateKey` | `0x14B370` | 49 | UnwindData |  |
| 1723 | `RtlpNtMakeTemporaryKey` | `0x14B3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1726 | `RtlpNtSetValueKey` | `0x14B3C0` | 43 | UnwindData |  |
| 193 | `MD4Final` | `0x15B860` | 301 | UnwindData |  |
| 194 | `MD4Init` | `0x15B9A0` | 138 | UnwindData |  |
| 195 | `MD4Update` | `0x15BA30` | 201 | UnwindData |  |
| 66 | `EtwEnumerateProcessRegGuids` | `0x15BBB0` | 203 | UnwindData |  |
| 88 | `EtwRegisterSecurityProvider` | `0x15BC90` | 79 | UnwindData |  |
| 64 | `EtwCreateTraceInstanceId` | `0x15BDE0` | 73 | UnwindData |  |
| 93 | `EtwSetMark` | `0x15BE30` | 36 | UnwindData |  |
| 94 | `EtwTraceEventInstance` | `0x15BE60` | 448 | UnwindData |  |
| 101 | `EvtIntReportAuthzEventAndSourceAsync` | `0x15C200` | 106 | UnwindData |  |
| 1783 | `TpQueryPoolStackInformation` | `0x15C310` | 127 | UnwindData |  |
| 1764 | `TpCallbackDetectedUnrecoverableError` | `0x15C420` | 40 | UnwindData |  |
| 1768 | `TpCallbackReleaseMutexOnCompletion` | `0x15C450` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1769 | `TpCallbackReleaseSemaphoreOnCompletion` | `0x15C490` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1777 | `TpDbgDumpHeapUsage` | `0x15C4D0` | 181 | UnwindData |  |
| 783 | `RtlCancelTimer` | `0x15C820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `RtlDeleteTimerQueue` | `0x15C830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1537 | `RtlSetTimer` | `0x15C840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1747 | `SbExecuteProcedure` | `0x15C850` | 34 | UnwindData |  |
| 27 | `ApiSetGetImplementationHost` | `0x15E170` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `ApiSetQuerySchema` | `0x15E1A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `CsrSetPriorityClass` | `0x15E1D0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `LdrGetFailureData` | `0x15E4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `LdrHotPatchNotify` | `0x15E4E0` | 464 | UnwindData |  |
| 146 | `LdrIsModuleSxsRedirected` | `0x15E6C0` | 58 | UnwindData |  |
| 159 | `LdrQueryModuleServiceTags` | `0x15E700` | 161 | UnwindData |  |
| 177 | `LdrSetImplicitPathOptions` | `0x15E7B0` | 100 | UnwindData |  |
| 189 | `LdrVerifyImageMatchesChecksum` | `0x15E820` | 147 | UnwindData |  |
| 1147 | `RtlGetUnloadEventTrace` | `0x15EC50` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `LdrResolveDelayLoadsFromDll` | `0x15EED0` | 64 | UnwindData |  |
| 954 | `RtlDosLongPathNameToRelativeNtPathName_U_WithStatus` | `0x15F0E0` | 34 | UnwindData |  |
| 809 | `RtlCloneUserProcess` | `0x15F110` | 763 | UnwindData |  |
| 823 | `RtlCompleteProcessCloning` | `0x15F420` | 301 | UnwindData |  |
| 871 | `RtlCreateProcessParameters` | `0x15F560` | 100 | UnwindData |  |
| 1358 | `RtlPrepareForProcessCloning` | `0x15F5D0` | 284 | UnwindData |  |
| 1679 | `RtlWow64LogMessageInEventLogger` | `0x15F700` | 30 | UnwindData |  |
| 903 | `RtlDecodeRemotePointer` | `0x15F730` | 103 | UnwindData |  |
| 972 | `RtlEncodeRemotePointer` | `0x15F7A0` | 98 | UnwindData |  |
| 693 | `NtdllDefWindowProc_A` | `0x161870` | 6 | UnwindData |  |
| 694 | `NtdllDefWindowProc_W` | `0x161880` | 6 | UnwindData |  |
| 695 | `NtdllDialogWndProc_A` | `0x161930` | 6 | UnwindData |  |
| 696 | `NtdllDialogWndProc_W` | `0x161940` | 6 | UnwindData |  |
| 204 | `NtAccessCheck` | `0x161BB0` | 24 | UnwindData |  |
| 1852 | `ZwAccessCheck` | `0x161BB0` | 24 | UnwindData |  |
| 687 | `NtWorkerFactoryWorkerReady` | `0x161BD0` | 24 | UnwindData |  |
| 2334 | `ZwWorkerFactoryWorkerReady` | `0x161BD0` | 24 | UnwindData |  |
| 203 | `NtAcceptConnectPort` | `0x161BF0` | 24 | UnwindData |  |
| 1851 | `ZwAcceptConnectPort` | `0x161BF0` | 24 | UnwindData |  |
| 424 | `NtMapUserPhysicalPagesScatter` | `0x161C10` | 24 | UnwindData |  |
| 2071 | `ZwMapUserPhysicalPagesScatter` | `0x161C10` | 24 | UnwindData |  |
| 683 | `NtWaitForSingleObject` | `0x161C30` | 24 | UnwindData |  |
| 2330 | `ZwWaitForSingleObject` | `0x161C30` | 24 | UnwindData |  |
| 260 | `NtCallbackReturn` | `0x161C50` | 24 | UnwindData |  |
| 1908 | `ZwCallbackReturn` | `0x161C50` | 24 | UnwindData |  |
| 545 | `NtReadFile` | `0x161C70` | 24 | UnwindData |  |
| 2192 | `ZwReadFile` | `0x161C70` | 24 | UnwindData |  |
| 352 | `NtDeviceIoControlFile` | `0x161C90` | 24 | UnwindData |  |
| 2000 | `ZwDeviceIoControlFile` | `0x161C90` | 24 | UnwindData |  |
| 688 | `NtWriteFile` | `0x161CB0` | 24 | UnwindData |  |
| 2335 | `ZwWriteFile` | `0x161CB0` | 24 | UnwindData |  |
| 560 | `NtRemoveIoCompletion` | `0x161CD0` | 24 | UnwindData |  |
| 2207 | `ZwRemoveIoCompletion` | `0x161CD0` | 24 | UnwindData |  |
| 558 | `NtReleaseSemaphore` | `0x161CF0` | 24 | UnwindData |  |
| 2205 | `ZwReleaseSemaphore` | `0x161CF0` | 24 | UnwindData |  |
| 568 | `NtReplyWaitReceivePort` | `0x161D10` | 24 | UnwindData |  |
| 2215 | `ZwReplyWaitReceivePort` | `0x161D10` | 24 | UnwindData |  |
| 567 | `NtReplyPort` | `0x161D30` | 24 | UnwindData |  |
| 2214 | `ZwReplyPort` | `0x161D30` | 24 | UnwindData |  |
| 617 | `NtSetInformationThread` | `0x161D50` | 24 | UnwindData |  |
| 2264 | `ZwSetInformationThread` | `0x161D50` | 24 | UnwindData |  |
| 600 | `NtSetEvent` | `0x161D70` | 24 | UnwindData |  |
| 2247 | `ZwSetEvent` | `0x161D70` | 24 | UnwindData |  |
| 270 | `NtClose` | `0x161D90` | 24 | UnwindData |  |
| 1918 | `ZwClose` | `0x161D90` | 24 | UnwindData |  |
| 516 | `NtQueryObject` | `0x161DB0` | 24 | UnwindData |  |
| 2163 | `ZwQueryObject` | `0x161DB0` | 24 | UnwindData |  |
| 498 | `NtQueryInformationFile` | `0x161DD0` | 24 | UnwindData |  |
| 2145 | `ZwQueryInformationFile` | `0x161DD0` | 24 | UnwindData |  |
| 442 | `NtOpenKey` | `0x161DF0` | 24 | UnwindData |  |
| 2089 | `ZwOpenKey` | `0x161DF0` | 24 | UnwindData |  |
| 365 | `NtEnumerateValueKey` | `0x161E10` | 24 | UnwindData |  |
| 2013 | `ZwEnumerateValueKey` | `0x161E10` | 24 | UnwindData |  |
| 370 | `NtFindAtom` | `0x161E30` | 24 | UnwindData |  |
| 2018 | `ZwFindAtom` | `0x161E30` | 24 | UnwindData |  |
| 485 | `NtQueryDefaultLocale` | `0x161E50` | 24 | UnwindData |  |
| 2132 | `ZwQueryDefaultLocale` | `0x161E50` | 24 | UnwindData |  |
| 512 | `NtQueryKey` | `0x161E70` | 24 | UnwindData |  |
| 2159 | `ZwQueryKey` | `0x161E70` | 24 | UnwindData |  |
| 535 | `NtQueryValueKey` | `0x161E90` | 24 | UnwindData |  |
| 2182 | `ZwQueryValueKey` | `0x161E90` | 24 | UnwindData |  |
| 230 | `NtAllocateVirtualMemory` | `0x161EB0` | 24 | UnwindData |  |
| 1878 | `ZwAllocateVirtualMemory` | `0x161EB0` | 24 | UnwindData |  |
| 501 | `NtQueryInformationProcess` | `0x161ED0` | 24 | UnwindData |  |
| 2148 | `ZwQueryInformationProcess` | `0x161ED0` | 24 | UnwindData |  |
| 682 | `NtWaitForMultipleObjects32` | `0x161EF0` | 24 | UnwindData |  |
| 2329 | `ZwWaitForMultipleObjects32` | `0x161EF0` | 24 | UnwindData |  |
| 689 | `NtWriteFileGather` | `0x161F10` | 24 | UnwindData |  |
| 2336 | `ZwWriteFileGather` | `0x161F10` | 24 | UnwindData |  |
| 614 | `NtSetInformationProcess` | `0x161F30` | 24 | UnwindData |  |
| 2261 | `ZwSetInformationProcess` | `0x161F30` | 24 | UnwindData |  |
| 303 | `NtCreateKey` | `0x161F50` | 24 | UnwindData |  |
| 1951 | `ZwCreateKey` | `0x161F50` | 24 | UnwindData |  |
| 380 | `NtFreeVirtualMemory` | `0x161F70` | 24 | UnwindData |  |
| 2028 | `ZwFreeVirtualMemory` | `0x161F70` | 24 | UnwindData |  |
| 398 | `NtImpersonateClientOfPort` | `0x161F90` | 24 | UnwindData |  |
| 2045 | `ZwImpersonateClientOfPort` | `0x161F90` | 24 | UnwindData |  |
| 557 | `NtReleaseMutant` | `0x161FB0` | 24 | UnwindData |  |
| 2204 | `ZwReleaseMutant` | `0x161FB0` | 24 | UnwindData |  |
| 504 | `NtQueryInformationToken` | `0x161FD0` | 24 | UnwindData |  |
| 2151 | `ZwQueryInformationToken` | `0x161FD0` | 24 | UnwindData |  |
| 572 | `NtRequestWaitReplyPort` | `0x161FF0` | 24 | UnwindData |  |
| 2219 | `ZwRequestWaitReplyPort` | `0x161FF0` | 24 | UnwindData |  |
| 536 | `NtQueryVirtualMemory` | `0x162010` | 24 | UnwindData |  |
| 2183 | `ZwQueryVirtualMemory` | `0x162010` | 24 | UnwindData |  |
| 461 | `NtOpenThreadToken` | `0x162030` | 24 | UnwindData |  |
| 2108 | `ZwOpenThreadToken` | `0x162030` | 24 | UnwindData |  |
| 503 | `NtQueryInformationThread` | `0x162050` | 24 | UnwindData |  |
| 2150 | `ZwQueryInformationThread` | `0x162050` | 24 | UnwindData |  |
| 451 | `NtOpenProcess` | `0x162070` | 24 | UnwindData |  |
| 2098 | `ZwOpenProcess` | `0x162070` | 24 | UnwindData |  |
| 609 | `NtSetInformationFile` | `0x162090` | 24 | UnwindData |  |
| 2256 | `ZwSetInformationFile` | `0x162090` | 24 | UnwindData |  |
| 425 | `NtMapViewOfSection` | `0x1620B0` | 24 | UnwindData |  |
| 2072 | `ZwMapViewOfSection` | `0x1620B0` | 24 | UnwindData |  |
| 205 | `NtAccessCheckAndAuditAlarm` | `0x1620D0` | 24 | UnwindData |  |
| 1853 | `ZwAccessCheckAndAuditAlarm` | `0x1620D0` | 24 | UnwindData |  |
| 673 | `NtUnmapViewOfSection` | `0x1620F0` | 24 | UnwindData |  |
| 2320 | `ZwUnmapViewOfSection` | `0x1620F0` | 24 | UnwindData |  |
| 569 | `NtReplyWaitReceivePortEx` | `0x162110` | 24 | UnwindData |  |
| 2216 | `ZwReplyWaitReceivePortEx` | `0x162110` | 24 | UnwindData |  |
| 658 | `NtTerminateProcess` | `0x162130` | 24 | UnwindData |  |
| 2305 | `ZwTerminateProcess` | `0x162130` | 24 | UnwindData |  |
| 601 | `NtSetEventBoostPriority` | `0x162150` | 24 | UnwindData |  |
| 2248 | `ZwSetEventBoostPriority` | `0x162150` | 24 | UnwindData |  |
| 546 | `NtReadFileScatter` | `0x162170` | 24 | UnwindData |  |
| 2193 | `ZwReadFileScatter` | `0x162170` | 24 | UnwindData |  |
| 462 | `NtOpenThreadTokenEx` | `0x162190` | 24 | UnwindData |  |
| 2109 | `ZwOpenThreadTokenEx` | `0x162190` | 24 | UnwindData |  |
| 453 | `NtOpenProcessTokenEx` | `0x1621B0` | 24 | UnwindData |  |
| 2100 | `ZwOpenProcessTokenEx` | `0x1621B0` | 24 | UnwindData |  |
| 519 | `NtQueryPerformanceCounter` | `0x1621D0` | 24 | UnwindData |  |
| 2166 | `ZwQueryPerformanceCounter` | `0x1621D0` | 24 | UnwindData |  |
| 362 | `NtEnumerateKey` | `0x1621F0` | 24 | UnwindData |  |
| 2010 | `ZwEnumerateKey` | `0x1621F0` | 24 | UnwindData |  |
| 439 | `NtOpenFile` | `0x162210` | 24 | UnwindData |  |
| 2086 | `ZwOpenFile` | `0x162210` | 24 | UnwindData |  |
| 341 | `NtDelayExecution` | `0x162230` | 24 | UnwindData |  |
| 1989 | `ZwDelayExecution` | `0x162230` | 24 | UnwindData |  |
| 487 | `NtQueryDirectoryFile` | `0x162250` | 24 | UnwindData |  |
| 2134 | `ZwQueryDirectoryFile` | `0x162250` | 24 | UnwindData |  |
| 530 | `NtQuerySystemInformation` | `0x162270` | 24 | UnwindData |  |
| 1113 | `RtlGetNativeSystemInformation` | `0x162270` | 24 | UnwindData |  |
| 2177 | `ZwQuerySystemInformation` | `0x162270` | 24 | UnwindData |  |
| 456 | `NtOpenSection` | `0x162290` | 24 | UnwindData |  |
| 2103 | `ZwOpenSection` | `0x162290` | 24 | UnwindData |  |
| 533 | `NtQueryTimer` | `0x1622B0` | 24 | UnwindData |  |
| 2180 | `ZwQueryTimer` | `0x1622B0` | 24 | UnwindData |  |
| 383 | `NtFsControlFile` | `0x1622D0` | 24 | UnwindData |  |
| 2031 | `ZwFsControlFile` | `0x1622D0` | 24 | UnwindData |  |
| 691 | `NtWriteVirtualMemory` | `0x1622F0` | 24 | UnwindData |  |
| 2338 | `ZwWriteVirtualMemory` | `0x1622F0` | 24 | UnwindData |  |
| 271 | `NtCloseObjectAuditAlarm` | `0x162310` | 24 | UnwindData |  |
| 1919 | `ZwCloseObjectAuditAlarm` | `0x162310` | 24 | UnwindData |  |
| 357 | `NtDuplicateObject` | `0x162330` | 24 | UnwindData |  |
| 2005 | `ZwDuplicateObject` | `0x162330` | 24 | UnwindData |  |
| 480 | `NtQueryAttributesFile` | `0x162350` | 24 | UnwindData |  |
| 2127 | `ZwQueryAttributesFile` | `0x162350` | 24 | UnwindData |  |
| 269 | `NtClearEvent` | `0x162370` | 24 | UnwindData |  |
| 1917 | `ZwClearEvent` | `0x162370` | 24 | UnwindData |  |
| 549 | `NtReadVirtualMemory` | `0x162390` | 24 | UnwindData |  |
| 2196 | `ZwReadVirtualMemory` | `0x162390` | 24 | UnwindData |  |
| 437 | `NtOpenEvent` | `0x1623B0` | 24 | UnwindData |  |
| 2084 | `ZwOpenEvent` | `0x1623B0` | 24 | UnwindData |  |
| 218 | `NtAdjustPrivilegesToken` | `0x1623D0` | 24 | UnwindData |  |
| 1866 | `ZwAdjustPrivilegesToken` | `0x1623D0` | 24 | UnwindData |  |
| 358 | `NtDuplicateToken` | `0x1623F0` | 24 | UnwindData |  |
| 2006 | `ZwDuplicateToken` | `0x1623F0` | 24 | UnwindData |  |
| 283 | `NtContinue` | `0x162410` | 24 | UnwindData |  |
| 1931 | `ZwContinue` | `0x162410` | 24 | UnwindData |  |
| 486 | `NtQueryDefaultUILanguage` | `0x162430` | 24 | UnwindData |  |
| 2133 | `ZwQueryDefaultUILanguage` | `0x162430` | 24 | UnwindData |  |
| 540 | `NtQueueApcThread` | `0x162450` | 24 | UnwindData |  |
| 2187 | `ZwQueueApcThread` | `0x162450` | 24 | UnwindData |  |
| 692 | `NtYieldExecution` | `0x162470` | 24 | UnwindData |  |
| 2339 | `ZwYieldExecution` | `0x162470` | 24 | UnwindData |  |
| 213 | `NtAddAtom` | `0x162490` | 24 | UnwindData |  |
| 1861 | `ZwAddAtom` | `0x162490` | 24 | UnwindData |  |
| 295 | `NtCreateEvent` | `0x1624B0` | 24 | UnwindData |  |
| 1943 | `ZwCreateEvent` | `0x1624B0` | 24 | UnwindData |  |
| 537 | `NtQueryVolumeInformationFile` | `0x1624D0` | 24 | UnwindData |  |
| 2184 | `ZwQueryVolumeInformationFile` | `0x1624D0` | 24 | UnwindData |  |
| 321 | `NtCreateSection` | `0x1624F0` | 24 | UnwindData |  |
| 1969 | `ZwCreateSection` | `0x1624F0` | 24 | UnwindData |  |
| 371 | `NtFlushBuffersFile` | `0x162510` | 24 | UnwindData |  |
| 2019 | `ZwFlushBuffersFile` | `0x162510` | 24 | UnwindData |  |
| 255 | `NtApphelpCacheControl` | `0x162530` | 24 | UnwindData |  |
| 1903 | `ZwApphelpCacheControl` | `0x162530` | 24 | UnwindData |  |
| 315 | `NtCreateProcessEx` | `0x162550` | 24 | UnwindData |  |
| 1963 | `ZwCreateProcessEx` | `0x162550` | 24 | UnwindData |  |
| 325 | `NtCreateThread` | `0x162570` | 24 | UnwindData |  |
| 1973 | `ZwCreateThread` | `0x162570` | 24 | UnwindData |  |
| 404 | `NtIsProcessInJob` | `0x162590` | 24 | UnwindData |  |
| 2051 | `ZwIsProcessInJob` | `0x162590` | 24 | UnwindData |  |
| 477 | `NtProtectVirtualMemory` | `0x1625B0` | 24 | UnwindData |  |
| 2124 | `ZwProtectVirtualMemory` | `0x1625B0` | 24 | UnwindData |  |
| 522 | `NtQuerySection` | `0x1625D0` | 24 | UnwindData |  |
| 2169 | `ZwQuerySection` | `0x1625D0` | 24 | UnwindData |  |
| 577 | `NtResumeThread` | `0x1625F0` | 24 | UnwindData |  |
| 2224 | `ZwResumeThread` | `0x1625F0` | 24 | UnwindData |  |
| 659 | `NtTerminateThread` | `0x162610` | 24 | UnwindData |  |
| 2306 | `ZwTerminateThread` | `0x162610` | 24 | UnwindData |  |
| 548 | `NtReadRequestData` | `0x162630` | 24 | UnwindData |  |
| 2195 | `ZwReadRequestData` | `0x162630` | 24 | UnwindData |  |
| 297 | `NtCreateFile` | `0x162650` | 24 | UnwindData |  |
| 1945 | `ZwCreateFile` | `0x162650` | 24 | UnwindData |  |
| 492 | `NtQueryEvent` | `0x162670` | 24 | UnwindData |  |
| 2139 | `ZwQueryEvent` | `0x162670` | 24 | UnwindData |  |
| 690 | `NtWriteRequestData` | `0x162690` | 24 | UnwindData |  |
| 2337 | `ZwWriteRequestData` | `0x162690` | 24 | UnwindData |  |
| 435 | `NtOpenDirectoryObject` | `0x1626B0` | 24 | UnwindData |  |
| 2082 | `ZwOpenDirectoryObject` | `0x1626B0` | 24 | UnwindData |  |
| 207 | `NtAccessCheckByTypeAndAuditAlarm` | `0x1626D0` | 24 | UnwindData |  |
| 1855 | `ZwAccessCheckByTypeAndAuditAlarm` | `0x1626D0` | 24 | UnwindData |  |
| 532 | `NtQuerySystemTime` | `0x1626F0` | 5 | UnwindData |  |
| 2179 | `ZwQuerySystemTime` | `0x1626F0` | 5 | UnwindData |  |
| 681 | `NtWaitForMultipleObjects` | `0x162700` | 24 | UnwindData |  |
| 2328 | `ZwWaitForMultipleObjects` | `0x162700` | 24 | UnwindData |  |
| 613 | `NtSetInformationObject` | `0x162720` | 24 | UnwindData |  |
| 2260 | `ZwSetInformationObject` | `0x162720` | 24 | UnwindData |  |
| 261 | `NtCancelIoFile` | `0x162740` | 24 | UnwindData |  |
| 1909 | `ZwCancelIoFile` | `0x162740` | 24 | UnwindData |  |
| 664 | `NtTraceEvent` | `0x162760` | 24 | UnwindData |  |
| 2311 | `ZwTraceEvent` | `0x162760` | 24 | UnwindData |  |
| 467 | `NtPowerInformation` | `0x162780` | 24 | UnwindData |  |
| 2114 | `ZwPowerInformation` | `0x162780` | 24 | UnwindData |  |
| 642 | `NtSetValueKey` | `0x1627A0` | 24 | UnwindData |  |
| 2289 | `ZwSetValueKey` | `0x1627A0` | 24 | UnwindData |  |
| 264 | `NtCancelTimer` | `0x1627C0` | 24 | UnwindData |  |
| 1912 | `ZwCancelTimer` | `0x1627C0` | 24 | UnwindData |  |
| 637 | `NtSetTimer` | `0x1627E0` | 24 | UnwindData |  |
| 2284 | `ZwSetTimer` | `0x1627E0` | 24 | UnwindData |  |
| 206 | `NtAccessCheckByType` | `0x162800` | 24 | UnwindData |  |
| 1854 | `ZwAccessCheckByType` | `0x162800` | 24 | UnwindData |  |
| 208 | `NtAccessCheckByTypeResultList` | `0x162820` | 24 | UnwindData |  |
| 1856 | `ZwAccessCheckByTypeResultList` | `0x162820` | 24 | UnwindData |  |
| 209 | `NtAccessCheckByTypeResultListAndAuditAlarm` | `0x162840` | 24 | UnwindData |  |
| 1857 | `ZwAccessCheckByTypeResultListAndAuditAlarm` | `0x162840` | 24 | UnwindData |  |
| 210 | `NtAccessCheckByTypeResultListAndAuditAlarmByHandle` | `0x162860` | 24 | UnwindData |  |
| 1858 | `ZwAccessCheckByTypeResultListAndAuditAlarmByHandle` | `0x162860` | 24 | UnwindData |  |
| 211 | `NtAcquireCrossVmMutant` | `0x162880` | 24 | UnwindData |  |
| 1859 | `ZwAcquireCrossVmMutant` | `0x162880` | 24 | UnwindData |  |
| 212 | `NtAcquireProcessActivityReference` | `0x1628A0` | 24 | UnwindData |  |
| 1860 | `ZwAcquireProcessActivityReference` | `0x1628A0` | 24 | UnwindData |  |
| 214 | `NtAddAtomEx` | `0x1628C0` | 24 | UnwindData |  |
| 1862 | `ZwAddAtomEx` | `0x1628C0` | 24 | UnwindData |  |
| 215 | `NtAddBootEntry` | `0x1628E0` | 24 | UnwindData |  |
| 1863 | `ZwAddBootEntry` | `0x1628E0` | 24 | UnwindData |  |
| 216 | `NtAddDriverEntry` | `0x162900` | 24 | UnwindData |  |
| 1864 | `ZwAddDriverEntry` | `0x162900` | 24 | UnwindData |  |
| 217 | `NtAdjustGroupsToken` | `0x162920` | 24 | UnwindData |  |
| 1865 | `ZwAdjustGroupsToken` | `0x162920` | 24 | UnwindData |  |
| 219 | `NtAdjustTokenClaimsAndDeviceGroups` | `0x162940` | 24 | UnwindData |  |
| 1867 | `ZwAdjustTokenClaimsAndDeviceGroups` | `0x162940` | 24 | UnwindData |  |
| 220 | `NtAlertMultipleThreadByThreadId` | `0x162960` | 24 | UnwindData |  |
| 1868 | `ZwAlertMultipleThreadByThreadId` | `0x162960` | 24 | UnwindData |  |
| 221 | `NtAlertResumeThread` | `0x162980` | 24 | UnwindData |  |
| 1869 | `ZwAlertResumeThread` | `0x162980` | 24 | UnwindData |  |
| 222 | `NtAlertThread` | `0x1629A0` | 24 | UnwindData |  |
| 1870 | `ZwAlertThread` | `0x1629A0` | 24 | UnwindData |  |
| 223 | `NtAlertThreadByThreadId` | `0x1629C0` | 24 | UnwindData |  |
| 1871 | `ZwAlertThreadByThreadId` | `0x1629C0` | 24 | UnwindData |  |
| 224 | `NtAlertThreadByThreadIdEx` | `0x1629E0` | 24 | UnwindData |  |
| 1872 | `ZwAlertThreadByThreadIdEx` | `0x1629E0` | 24 | UnwindData |  |
| 225 | `NtAllocateLocallyUniqueId` | `0x162A00` | 24 | UnwindData |  |
| 1873 | `ZwAllocateLocallyUniqueId` | `0x162A00` | 24 | UnwindData |  |
| 226 | `NtAllocateReserveObject` | `0x162A20` | 24 | UnwindData |  |
| 1874 | `ZwAllocateReserveObject` | `0x162A20` | 24 | UnwindData |  |
| 227 | `NtAllocateUserPhysicalPages` | `0x162A40` | 24 | UnwindData |  |
| 1875 | `ZwAllocateUserPhysicalPages` | `0x162A40` | 24 | UnwindData |  |
| 228 | `NtAllocateUserPhysicalPagesEx` | `0x162A60` | 24 | UnwindData |  |
| 1876 | `ZwAllocateUserPhysicalPagesEx` | `0x162A60` | 24 | UnwindData |  |
| 229 | `NtAllocateUuids` | `0x162A80` | 24 | UnwindData |  |
| 1877 | `ZwAllocateUuids` | `0x162A80` | 24 | UnwindData |  |
| 231 | `NtAllocateVirtualMemoryEx` | `0x162AA0` | 24 | UnwindData |  |
| 1879 | `ZwAllocateVirtualMemoryEx` | `0x162AA0` | 24 | UnwindData |  |
| 232 | `NtAlpcAcceptConnectPort` | `0x162AC0` | 24 | UnwindData |  |
| 1880 | `ZwAlpcAcceptConnectPort` | `0x162AC0` | 24 | UnwindData |  |
| 233 | `NtAlpcCancelMessage` | `0x162AE0` | 24 | UnwindData |  |
| 1881 | `ZwAlpcCancelMessage` | `0x162AE0` | 24 | UnwindData |  |
| 234 | `NtAlpcConnectPort` | `0x162B00` | 24 | UnwindData |  |
| 1882 | `ZwAlpcConnectPort` | `0x162B00` | 24 | UnwindData |  |
| 235 | `NtAlpcConnectPortEx` | `0x162B20` | 24 | UnwindData |  |
| 1883 | `ZwAlpcConnectPortEx` | `0x162B20` | 24 | UnwindData |  |
| 236 | `NtAlpcCreatePort` | `0x162B40` | 24 | UnwindData |  |
| 1884 | `ZwAlpcCreatePort` | `0x162B40` | 24 | UnwindData |  |
| 237 | `NtAlpcCreatePortSection` | `0x162B60` | 24 | UnwindData |  |
| 1885 | `ZwAlpcCreatePortSection` | `0x162B60` | 24 | UnwindData |  |
| 238 | `NtAlpcCreateResourceReserve` | `0x162B80` | 24 | UnwindData |  |
| 1886 | `ZwAlpcCreateResourceReserve` | `0x162B80` | 24 | UnwindData |  |
| 239 | `NtAlpcCreateSectionView` | `0x162BA0` | 24 | UnwindData |  |
| 1887 | `ZwAlpcCreateSectionView` | `0x162BA0` | 24 | UnwindData |  |
| 240 | `NtAlpcCreateSecurityContext` | `0x162BC0` | 24 | UnwindData |  |
| 1888 | `ZwAlpcCreateSecurityContext` | `0x162BC0` | 24 | UnwindData |  |
| 241 | `NtAlpcDeletePortSection` | `0x162BE0` | 24 | UnwindData |  |
| 1889 | `ZwAlpcDeletePortSection` | `0x162BE0` | 24 | UnwindData |  |
| 242 | `NtAlpcDeleteResourceReserve` | `0x162C00` | 24 | UnwindData |  |
| 1890 | `ZwAlpcDeleteResourceReserve` | `0x162C00` | 24 | UnwindData |  |
| 243 | `NtAlpcDeleteSectionView` | `0x162C20` | 24 | UnwindData |  |
| 1891 | `ZwAlpcDeleteSectionView` | `0x162C20` | 24 | UnwindData |  |
| 244 | `NtAlpcDeleteSecurityContext` | `0x162C40` | 24 | UnwindData |  |
| 1892 | `ZwAlpcDeleteSecurityContext` | `0x162C40` | 24 | UnwindData |  |
| 245 | `NtAlpcDisconnectPort` | `0x162C60` | 24 | UnwindData |  |
| 1893 | `ZwAlpcDisconnectPort` | `0x162C60` | 24 | UnwindData |  |
| 246 | `NtAlpcImpersonateClientContainerOfPort` | `0x162C80` | 24 | UnwindData |  |
| 1894 | `ZwAlpcImpersonateClientContainerOfPort` | `0x162C80` | 24 | UnwindData |  |
| 247 | `NtAlpcImpersonateClientOfPort` | `0x162CA0` | 24 | UnwindData |  |
| 1895 | `ZwAlpcImpersonateClientOfPort` | `0x162CA0` | 24 | UnwindData |  |
| 248 | `NtAlpcOpenSenderProcess` | `0x162CC0` | 24 | UnwindData |  |
| 1896 | `ZwAlpcOpenSenderProcess` | `0x162CC0` | 24 | UnwindData |  |
| 249 | `NtAlpcOpenSenderThread` | `0x162CE0` | 24 | UnwindData |  |
| 1897 | `ZwAlpcOpenSenderThread` | `0x162CE0` | 24 | UnwindData |  |
| 250 | `NtAlpcQueryInformation` | `0x162D00` | 24 | UnwindData |  |
| 1898 | `ZwAlpcQueryInformation` | `0x162D00` | 24 | UnwindData |  |
| 251 | `NtAlpcQueryInformationMessage` | `0x162D20` | 24 | UnwindData |  |
| 1899 | `ZwAlpcQueryInformationMessage` | `0x162D20` | 24 | UnwindData |  |
| 252 | `NtAlpcRevokeSecurityContext` | `0x162D40` | 24 | UnwindData |  |
| 1900 | `ZwAlpcRevokeSecurityContext` | `0x162D40` | 24 | UnwindData |  |
| 253 | `NtAlpcSendWaitReceivePort` | `0x162D60` | 24 | UnwindData |  |
| 1901 | `ZwAlpcSendWaitReceivePort` | `0x162D60` | 24 | UnwindData |  |
| 254 | `NtAlpcSetInformation` | `0x162D80` | 24 | UnwindData |  |
| 1902 | `ZwAlpcSetInformation` | `0x162D80` | 24 | UnwindData |  |
| 256 | `NtAreMappedFilesTheSame` | `0x162DA0` | 24 | UnwindData |  |
| 1904 | `ZwAreMappedFilesTheSame` | `0x162DA0` | 24 | UnwindData |  |
| 257 | `NtAssignProcessToJobObject` | `0x162DC0` | 24 | UnwindData |  |
| 1905 | `ZwAssignProcessToJobObject` | `0x162DC0` | 24 | UnwindData |  |
| 258 | `NtAssociateWaitCompletionPacket` | `0x162DE0` | 24 | UnwindData |  |
| 1906 | `ZwAssociateWaitCompletionPacket` | `0x162DE0` | 24 | UnwindData |  |
| 259 | `NtCallEnclave` | `0x162E00` | 24 | UnwindData |  |
| 1907 | `ZwCallEnclave` | `0x162E00` | 24 | UnwindData |  |
| 262 | `NtCancelIoFileEx` | `0x162E20` | 24 | UnwindData |  |
| 1910 | `ZwCancelIoFileEx` | `0x162E20` | 24 | UnwindData |  |
| 263 | `NtCancelSynchronousIoFile` | `0x162E40` | 24 | UnwindData |  |
| 1911 | `ZwCancelSynchronousIoFile` | `0x162E40` | 24 | UnwindData |  |
| 265 | `NtCancelTimer2` | `0x162E60` | 24 | UnwindData |  |
| 1913 | `ZwCancelTimer2` | `0x162E60` | 24 | UnwindData |  |
| 266 | `NtCancelWaitCompletionPacket` | `0x162E80` | 24 | UnwindData |  |
| 1914 | `ZwCancelWaitCompletionPacket` | `0x162E80` | 24 | UnwindData |  |
| 267 | `NtChangeProcessState` | `0x162EA0` | 24 | UnwindData |  |
| 1915 | `ZwChangeProcessState` | `0x162EA0` | 24 | UnwindData |  |
| 268 | `NtChangeThreadState` | `0x162EC0` | 24 | UnwindData |  |
| 1916 | `ZwChangeThreadState` | `0x162EC0` | 24 | UnwindData |  |
| 272 | `NtCommitComplete` | `0x162EE0` | 24 | UnwindData |  |
| 1920 | `ZwCommitComplete` | `0x162EE0` | 24 | UnwindData |  |
| 273 | `NtCommitEnlistment` | `0x162F00` | 24 | UnwindData |  |
| 1921 | `ZwCommitEnlistment` | `0x162F00` | 24 | UnwindData |  |
| 274 | `NtCommitRegistryTransaction` | `0x162F20` | 24 | UnwindData |  |
| 1922 | `ZwCommitRegistryTransaction` | `0x162F20` | 24 | UnwindData |  |
| 275 | `NtCommitTransaction` | `0x162F40` | 24 | UnwindData |  |
| 1923 | `ZwCommitTransaction` | `0x162F40` | 24 | UnwindData |  |
| 276 | `NtCompactKeys` | `0x162F60` | 24 | UnwindData |  |
| 1924 | `ZwCompactKeys` | `0x162F60` | 24 | UnwindData |  |
| 277 | `NtCompareObjects` | `0x162F80` | 24 | UnwindData |  |
| 1925 | `ZwCompareObjects` | `0x162F80` | 24 | UnwindData |  |
| 278 | `NtCompareSigningLevels` | `0x162FA0` | 24 | UnwindData |  |
| 1926 | `ZwCompareSigningLevels` | `0x162FA0` | 24 | UnwindData |  |
| 279 | `NtCompareTokens` | `0x162FC0` | 24 | UnwindData |  |
| 1927 | `ZwCompareTokens` | `0x162FC0` | 24 | UnwindData |  |
| 280 | `NtCompleteConnectPort` | `0x162FE0` | 24 | UnwindData |  |
| 1928 | `ZwCompleteConnectPort` | `0x162FE0` | 24 | UnwindData |  |
| 281 | `NtCompressKey` | `0x163000` | 24 | UnwindData |  |
| 1929 | `ZwCompressKey` | `0x163000` | 24 | UnwindData |  |
| 282 | `NtConnectPort` | `0x163020` | 24 | UnwindData |  |
| 1930 | `ZwConnectPort` | `0x163020` | 24 | UnwindData |  |
| 284 | `NtContinueEx` | `0x163040` | 24 | UnwindData |  |
| 1932 | `ZwContinueEx` | `0x163040` | 24 | UnwindData |  |
| 285 | `NtConvertBetweenAuxiliaryCounterAndPerformanceCounter` | `0x163060` | 24 | UnwindData |  |
| 1933 | `ZwConvertBetweenAuxiliaryCounterAndPerformanceCounter` | `0x163060` | 24 | UnwindData |  |
| 286 | `NtCopyFileChunk` | `0x163080` | 24 | UnwindData |  |
| 1934 | `ZwCopyFileChunk` | `0x163080` | 24 | UnwindData |  |
| 287 | `NtCreateCpuPartition` | `0x1630A0` | 24 | UnwindData |  |
| 1935 | `ZwCreateCpuPartition` | `0x1630A0` | 24 | UnwindData |  |
| 288 | `NtCreateCrossVmEvent` | `0x1630C0` | 24 | UnwindData |  |
| 1936 | `ZwCreateCrossVmEvent` | `0x1630C0` | 24 | UnwindData |  |
| 289 | `NtCreateCrossVmMutant` | `0x1630E0` | 24 | UnwindData |  |
| 1937 | `ZwCreateCrossVmMutant` | `0x1630E0` | 24 | UnwindData |  |
| 290 | `NtCreateDebugObject` | `0x163100` | 24 | UnwindData |  |
| 1938 | `ZwCreateDebugObject` | `0x163100` | 24 | UnwindData |  |
| 291 | `NtCreateDirectoryObject` | `0x163120` | 24 | UnwindData |  |
| 1939 | `ZwCreateDirectoryObject` | `0x163120` | 24 | UnwindData |  |
| 292 | `NtCreateDirectoryObjectEx` | `0x163140` | 24 | UnwindData |  |
| 1940 | `ZwCreateDirectoryObjectEx` | `0x163140` | 24 | UnwindData |  |
| 293 | `NtCreateEnclave` | `0x163160` | 24 | UnwindData |  |
| 1941 | `ZwCreateEnclave` | `0x163160` | 24 | UnwindData |  |
| 294 | `NtCreateEnlistment` | `0x163180` | 24 | UnwindData |  |
| 1942 | `ZwCreateEnlistment` | `0x163180` | 24 | UnwindData |  |
| 296 | `NtCreateEventPair` | `0x1631A0` | 24 | UnwindData |  |
| 1944 | `ZwCreateEventPair` | `0x1631A0` | 24 | UnwindData |  |
| 298 | `NtCreateIRTimer` | `0x1631C0` | 24 | UnwindData |  |
| 1946 | `ZwCreateIRTimer` | `0x1631C0` | 24 | UnwindData |  |
| 299 | `NtCreateIoCompletion` | `0x1631E0` | 24 | UnwindData |  |
| 1947 | `ZwCreateIoCompletion` | `0x1631E0` | 24 | UnwindData |  |
| 300 | `NtCreateIoRing` | `0x163200` | 24 | UnwindData |  |
| 1948 | `ZwCreateIoRing` | `0x163200` | 24 | UnwindData |  |
| 301 | `NtCreateJobObject` | `0x163220` | 24 | UnwindData |  |
| 1949 | `ZwCreateJobObject` | `0x163220` | 24 | UnwindData |  |
| 302 | `NtCreateJobSet` | `0x163240` | 24 | UnwindData |  |
| 1950 | `ZwCreateJobSet` | `0x163240` | 24 | UnwindData |  |
| 304 | `NtCreateKeyTransacted` | `0x163260` | 24 | UnwindData |  |
| 1952 | `ZwCreateKeyTransacted` | `0x163260` | 24 | UnwindData |  |
| 305 | `NtCreateKeyedEvent` | `0x163280` | 24 | UnwindData |  |
| 1953 | `ZwCreateKeyedEvent` | `0x163280` | 24 | UnwindData |  |
| 306 | `NtCreateLowBoxToken` | `0x1632A0` | 24 | UnwindData |  |
| 1954 | `ZwCreateLowBoxToken` | `0x1632A0` | 24 | UnwindData |  |
| 307 | `NtCreateMailslotFile` | `0x1632C0` | 24 | UnwindData |  |
| 1955 | `ZwCreateMailslotFile` | `0x1632C0` | 24 | UnwindData |  |
| 308 | `NtCreateMutant` | `0x1632E0` | 24 | UnwindData |  |
| 1956 | `ZwCreateMutant` | `0x1632E0` | 24 | UnwindData |  |
| 309 | `NtCreateNamedPipeFile` | `0x163300` | 24 | UnwindData |  |
| 1957 | `ZwCreateNamedPipeFile` | `0x163300` | 24 | UnwindData |  |
| 310 | `NtCreatePagingFile` | `0x163320` | 24 | UnwindData |  |
| 1958 | `ZwCreatePagingFile` | `0x163320` | 24 | UnwindData |  |
| 311 | `NtCreatePartition` | `0x163340` | 24 | UnwindData |  |
| 1959 | `ZwCreatePartition` | `0x163340` | 24 | UnwindData |  |
| 312 | `NtCreatePort` | `0x163360` | 24 | UnwindData |  |
| 1960 | `ZwCreatePort` | `0x163360` | 24 | UnwindData |  |
| 313 | `NtCreatePrivateNamespace` | `0x163380` | 24 | UnwindData |  |
| 1961 | `ZwCreatePrivateNamespace` | `0x163380` | 24 | UnwindData |  |
| 314 | `NtCreateProcess` | `0x1633A0` | 24 | UnwindData |  |
| 1962 | `ZwCreateProcess` | `0x1633A0` | 24 | UnwindData |  |
| 316 | `NtCreateProcessStateChange` | `0x1633C0` | 24 | UnwindData |  |
| 1964 | `ZwCreateProcessStateChange` | `0x1633C0` | 24 | UnwindData |  |
| 317 | `NtCreateProfile` | `0x1633E0` | 24 | UnwindData |  |
| 1965 | `ZwCreateProfile` | `0x1633E0` | 24 | UnwindData |  |
| 318 | `NtCreateProfileEx` | `0x163400` | 24 | UnwindData |  |
| 1966 | `ZwCreateProfileEx` | `0x163400` | 24 | UnwindData |  |
| 319 | `NtCreateRegistryTransaction` | `0x163420` | 24 | UnwindData |  |
| 1967 | `ZwCreateRegistryTransaction` | `0x163420` | 24 | UnwindData |  |
| 320 | `NtCreateResourceManager` | `0x163440` | 24 | UnwindData |  |
| 1968 | `ZwCreateResourceManager` | `0x163440` | 24 | UnwindData |  |
| 322 | `NtCreateSectionEx` | `0x163460` | 24 | UnwindData |  |
| 1970 | `ZwCreateSectionEx` | `0x163460` | 24 | UnwindData |  |
| 323 | `NtCreateSemaphore` | `0x163480` | 24 | UnwindData |  |
| 1971 | `ZwCreateSemaphore` | `0x163480` | 24 | UnwindData |  |
| 324 | `NtCreateSymbolicLinkObject` | `0x1634A0` | 24 | UnwindData |  |
| 1972 | `ZwCreateSymbolicLinkObject` | `0x1634A0` | 24 | UnwindData |  |
| 326 | `NtCreateThreadEx` | `0x1634C0` | 24 | UnwindData |  |
| 1974 | `ZwCreateThreadEx` | `0x1634C0` | 24 | UnwindData |  |
| 327 | `NtCreateThreadStateChange` | `0x1634E0` | 24 | UnwindData |  |
| 1975 | `ZwCreateThreadStateChange` | `0x1634E0` | 24 | UnwindData |  |
| 328 | `NtCreateTimer` | `0x163500` | 24 | UnwindData |  |
| 1976 | `ZwCreateTimer` | `0x163500` | 24 | UnwindData |  |
| 329 | `NtCreateTimer2` | `0x163520` | 24 | UnwindData |  |
| 1977 | `ZwCreateTimer2` | `0x163520` | 24 | UnwindData |  |
| 330 | `NtCreateToken` | `0x163540` | 24 | UnwindData |  |
| 1978 | `ZwCreateToken` | `0x163540` | 24 | UnwindData |  |
| 331 | `NtCreateTokenEx` | `0x163560` | 24 | UnwindData |  |
| 1979 | `ZwCreateTokenEx` | `0x163560` | 24 | UnwindData |  |
| 332 | `NtCreateTransaction` | `0x163580` | 24 | UnwindData |  |
| 1980 | `ZwCreateTransaction` | `0x163580` | 24 | UnwindData |  |
| 333 | `NtCreateTransactionManager` | `0x1635A0` | 24 | UnwindData |  |
| 1981 | `ZwCreateTransactionManager` | `0x1635A0` | 24 | UnwindData |  |
| 334 | `NtCreateUserProcess` | `0x1635C0` | 24 | UnwindData |  |
| 1982 | `ZwCreateUserProcess` | `0x1635C0` | 24 | UnwindData |  |
| 335 | `NtCreateWaitCompletionPacket` | `0x1635E0` | 24 | UnwindData |  |
| 1983 | `ZwCreateWaitCompletionPacket` | `0x1635E0` | 24 | UnwindData |  |
| 336 | `NtCreateWaitablePort` | `0x163600` | 24 | UnwindData |  |
| 1984 | `ZwCreateWaitablePort` | `0x163600` | 24 | UnwindData |  |
| 337 | `NtCreateWnfStateName` | `0x163620` | 24 | UnwindData |  |
| 1985 | `ZwCreateWnfStateName` | `0x163620` | 24 | UnwindData |  |
| 338 | `NtCreateWorkerFactory` | `0x163640` | 24 | UnwindData |  |
| 1986 | `ZwCreateWorkerFactory` | `0x163640` | 24 | UnwindData |  |
| 339 | `NtDebugActiveProcess` | `0x163660` | 24 | UnwindData |  |
| 1987 | `ZwDebugActiveProcess` | `0x163660` | 24 | UnwindData |  |
| 340 | `NtDebugContinue` | `0x163680` | 24 | UnwindData |  |
| 1988 | `ZwDebugContinue` | `0x163680` | 24 | UnwindData |  |
| 342 | `NtDeleteAtom` | `0x1636A0` | 24 | UnwindData |  |
| 1990 | `ZwDeleteAtom` | `0x1636A0` | 24 | UnwindData |  |
| 343 | `NtDeleteBootEntry` | `0x1636C0` | 24 | UnwindData |  |
| 1991 | `ZwDeleteBootEntry` | `0x1636C0` | 24 | UnwindData |  |
| 344 | `NtDeleteDriverEntry` | `0x1636E0` | 24 | UnwindData |  |
| 1992 | `ZwDeleteDriverEntry` | `0x1636E0` | 24 | UnwindData |  |
| 345 | `NtDeleteFile` | `0x163700` | 24 | UnwindData |  |
| 1993 | `ZwDeleteFile` | `0x163700` | 24 | UnwindData |  |
| 346 | `NtDeleteKey` | `0x163720` | 24 | UnwindData |  |
| 1994 | `ZwDeleteKey` | `0x163720` | 24 | UnwindData |  |
| 347 | `NtDeleteObjectAuditAlarm` | `0x163740` | 24 | UnwindData |  |
| 1995 | `ZwDeleteObjectAuditAlarm` | `0x163740` | 24 | UnwindData |  |
| 348 | `NtDeletePrivateNamespace` | `0x163760` | 24 | UnwindData |  |
| 1996 | `ZwDeletePrivateNamespace` | `0x163760` | 24 | UnwindData |  |
| 349 | `NtDeleteValueKey` | `0x163780` | 24 | UnwindData |  |
| 1997 | `ZwDeleteValueKey` | `0x163780` | 24 | UnwindData |  |
| 350 | `NtDeleteWnfStateData` | `0x1637A0` | 24 | UnwindData |  |
| 1998 | `ZwDeleteWnfStateData` | `0x1637A0` | 24 | UnwindData |  |
| 351 | `NtDeleteWnfStateName` | `0x1637C0` | 24 | UnwindData |  |
| 1999 | `ZwDeleteWnfStateName` | `0x1637C0` | 24 | UnwindData |  |
| 353 | `NtDirectGraphicsCall` | `0x1637E0` | 24 | UnwindData |  |
| 2001 | `ZwDirectGraphicsCall` | `0x1637E0` | 24 | UnwindData |  |
| 354 | `NtDisableLastKnownGood` | `0x163800` | 24 | UnwindData |  |
| 2002 | `ZwDisableLastKnownGood` | `0x163800` | 24 | UnwindData |  |
| 355 | `NtDisplayString` | `0x163820` | 24 | UnwindData |  |
| 2003 | `ZwDisplayString` | `0x163820` | 24 | UnwindData |  |
| 356 | `NtDrawText` | `0x163840` | 24 | UnwindData |  |
| 2004 | `ZwDrawText` | `0x163840` | 24 | UnwindData |  |
| 359 | `NtEnableLastKnownGood` | `0x163860` | 24 | UnwindData |  |
| 2007 | `ZwEnableLastKnownGood` | `0x163860` | 24 | UnwindData |  |
| 360 | `NtEnumerateBootEntries` | `0x163880` | 24 | UnwindData |  |
| 2008 | `ZwEnumerateBootEntries` | `0x163880` | 24 | UnwindData |  |
| 361 | `NtEnumerateDriverEntries` | `0x1638A0` | 24 | UnwindData |  |
| 2009 | `ZwEnumerateDriverEntries` | `0x1638A0` | 24 | UnwindData |  |
| 363 | `NtEnumerateSystemEnvironmentValuesEx` | `0x1638C0` | 24 | UnwindData |  |
| 2011 | `ZwEnumerateSystemEnvironmentValuesEx` | `0x1638C0` | 24 | UnwindData |  |
| 364 | `NtEnumerateTransactionObject` | `0x1638E0` | 24 | UnwindData |  |
| 2012 | `ZwEnumerateTransactionObject` | `0x1638E0` | 24 | UnwindData |  |
| 366 | `NtExtendSection` | `0x163900` | 24 | UnwindData |  |
| 2014 | `ZwExtendSection` | `0x163900` | 24 | UnwindData |  |
| 367 | `NtFilterBootOption` | `0x163920` | 24 | UnwindData |  |
| 2015 | `ZwFilterBootOption` | `0x163920` | 24 | UnwindData |  |
| 368 | `NtFilterToken` | `0x163940` | 24 | UnwindData |  |
| 2016 | `ZwFilterToken` | `0x163940` | 24 | UnwindData |  |
| 369 | `NtFilterTokenEx` | `0x163960` | 24 | UnwindData |  |
| 2017 | `ZwFilterTokenEx` | `0x163960` | 24 | UnwindData |  |
| 372 | `NtFlushBuffersFileEx` | `0x163980` | 24 | UnwindData |  |
| 2020 | `ZwFlushBuffersFileEx` | `0x163980` | 24 | UnwindData |  |
| 373 | `NtFlushInstallUILanguage` | `0x1639A0` | 24 | UnwindData |  |
| 2021 | `ZwFlushInstallUILanguage` | `0x1639A0` | 24 | UnwindData |  |
| 374 | `NtFlushInstructionCache` | `0x1639C0` | 24 | UnwindData |  |
| 2022 | `ZwFlushInstructionCache` | `0x1639C0` | 24 | UnwindData |  |
| 375 | `NtFlushKey` | `0x1639E0` | 24 | UnwindData |  |
| 2023 | `ZwFlushKey` | `0x1639E0` | 24 | UnwindData |  |
| 376 | `NtFlushProcessWriteBuffers` | `0x163A00` | 24 | UnwindData |  |
| 2024 | `ZwFlushProcessWriteBuffers` | `0x163A00` | 24 | UnwindData |  |
| 377 | `NtFlushVirtualMemory` | `0x163A20` | 24 | UnwindData |  |
| 2025 | `ZwFlushVirtualMemory` | `0x163A20` | 24 | UnwindData |  |
| 378 | `NtFlushWriteBuffer` | `0x163A40` | 24 | UnwindData |  |
| 2026 | `ZwFlushWriteBuffer` | `0x163A40` | 24 | UnwindData |  |
| 379 | `NtFreeUserPhysicalPages` | `0x163A60` | 24 | UnwindData |  |
| 2027 | `ZwFreeUserPhysicalPages` | `0x163A60` | 24 | UnwindData |  |
| 381 | `NtFreezeRegistry` | `0x163A80` | 24 | UnwindData |  |
| 2029 | `ZwFreezeRegistry` | `0x163A80` | 24 | UnwindData |  |
| 382 | `NtFreezeTransactions` | `0x163AA0` | 24 | UnwindData |  |
| 2030 | `ZwFreezeTransactions` | `0x163AA0` | 24 | UnwindData |  |
| 384 | `NtGetCachedSigningLevel` | `0x163AC0` | 24 | UnwindData |  |
| 2032 | `ZwGetCachedSigningLevel` | `0x163AC0` | 24 | UnwindData |  |
| 385 | `NtGetCompleteWnfStateSubscription` | `0x163AE0` | 24 | UnwindData |  |
| 2033 | `ZwGetCompleteWnfStateSubscription` | `0x163AE0` | 24 | UnwindData |  |
| 386 | `NtGetContextThread` | `0x163B00` | 24 | UnwindData |  |
| 2034 | `ZwGetContextThread` | `0x163B00` | 24 | UnwindData |  |
| 387 | `NtGetCurrentProcessorNumber` | `0x163B20` | 24 | UnwindData |  |
| 2035 | `ZwGetCurrentProcessorNumber` | `0x163B20` | 24 | UnwindData |  |
| 388 | `NtGetCurrentProcessorNumberEx` | `0x163B40` | 24 | UnwindData |  |
| 2036 | `ZwGetCurrentProcessorNumberEx` | `0x163B40` | 24 | UnwindData |  |
| 389 | `NtGetDevicePowerState` | `0x163B60` | 24 | UnwindData |  |
| 2037 | `ZwGetDevicePowerState` | `0x163B60` | 24 | UnwindData |  |
| 390 | `NtGetMUIRegistryInfo` | `0x163B80` | 24 | UnwindData |  |
| 2038 | `ZwGetMUIRegistryInfo` | `0x163B80` | 24 | UnwindData |  |
| 391 | `NtGetNextProcess` | `0x163BA0` | 24 | UnwindData |  |
| 2039 | `ZwGetNextProcess` | `0x163BA0` | 24 | UnwindData |  |
| 392 | `NtGetNextThread` | `0x163BC0` | 24 | UnwindData |  |
| 2040 | `ZwGetNextThread` | `0x163BC0` | 24 | UnwindData |  |
| 393 | `NtGetNlsSectionPtr` | `0x163BE0` | 24 | UnwindData |  |
| 2041 | `ZwGetNlsSectionPtr` | `0x163BE0` | 24 | UnwindData |  |
| 394 | `NtGetNotificationResourceManager` | `0x163C00` | 24 | UnwindData |  |
| 2042 | `ZwGetNotificationResourceManager` | `0x163C00` | 24 | UnwindData |  |
| 396 | `NtGetWriteWatch` | `0x163C20` | 24 | UnwindData |  |
| 2043 | `ZwGetWriteWatch` | `0x163C20` | 24 | UnwindData |  |
| 397 | `NtImpersonateAnonymousToken` | `0x163C40` | 24 | UnwindData |  |
| 2044 | `ZwImpersonateAnonymousToken` | `0x163C40` | 24 | UnwindData |  |
| 399 | `NtImpersonateThread` | `0x163C60` | 24 | UnwindData |  |
| 2046 | `ZwImpersonateThread` | `0x163C60` | 24 | UnwindData |  |
| 400 | `NtInitializeEnclave` | `0x163C80` | 24 | UnwindData |  |
| 2047 | `ZwInitializeEnclave` | `0x163C80` | 24 | UnwindData |  |
| 401 | `NtInitializeNlsFiles` | `0x163CA0` | 24 | UnwindData |  |
| 2048 | `ZwInitializeNlsFiles` | `0x163CA0` | 24 | UnwindData |  |
| 402 | `NtInitializeRegistry` | `0x163CC0` | 24 | UnwindData |  |
| 2049 | `ZwInitializeRegistry` | `0x163CC0` | 24 | UnwindData |  |
| 403 | `NtInitiatePowerAction` | `0x163CE0` | 24 | UnwindData |  |
| 2050 | `ZwInitiatePowerAction` | `0x163CE0` | 24 | UnwindData |  |
| 405 | `NtIsSystemResumeAutomatic` | `0x163D00` | 24 | UnwindData |  |
| 2052 | `ZwIsSystemResumeAutomatic` | `0x163D00` | 24 | UnwindData |  |
| 406 | `NtIsUILanguageComitted` | `0x163D20` | 24 | UnwindData |  |
| 2053 | `ZwIsUILanguageComitted` | `0x163D20` | 24 | UnwindData |  |
| 407 | `NtListenPort` | `0x163D40` | 24 | UnwindData |  |
| 2054 | `ZwListenPort` | `0x163D40` | 24 | UnwindData |  |
| 408 | `NtLoadDriver` | `0x163D60` | 24 | UnwindData |  |
| 2055 | `ZwLoadDriver` | `0x163D60` | 24 | UnwindData |  |
| 409 | `NtLoadEnclaveData` | `0x163D80` | 24 | UnwindData |  |
| 2056 | `ZwLoadEnclaveData` | `0x163D80` | 24 | UnwindData |  |
| 410 | `NtLoadKey` | `0x163DA0` | 24 | UnwindData |  |
| 2057 | `ZwLoadKey` | `0x163DA0` | 24 | UnwindData |  |
| 411 | `NtLoadKey2` | `0x163DC0` | 24 | UnwindData |  |
| 2058 | `ZwLoadKey2` | `0x163DC0` | 24 | UnwindData |  |
| 412 | `NtLoadKey3` | `0x163DE0` | 24 | UnwindData |  |
| 2059 | `ZwLoadKey3` | `0x163DE0` | 24 | UnwindData |  |
| 413 | `NtLoadKeyEx` | `0x163E00` | 24 | UnwindData |  |
| 2060 | `ZwLoadKeyEx` | `0x163E00` | 24 | UnwindData |  |
| 414 | `NtLockFile` | `0x163E20` | 24 | UnwindData |  |
| 2061 | `ZwLockFile` | `0x163E20` | 24 | UnwindData |  |
| 415 | `NtLockProductActivationKeys` | `0x163E40` | 24 | UnwindData |  |
| 2062 | `ZwLockProductActivationKeys` | `0x163E40` | 24 | UnwindData |  |
| 416 | `NtLockRegistryKey` | `0x163E60` | 24 | UnwindData |  |
| 2063 | `ZwLockRegistryKey` | `0x163E60` | 24 | UnwindData |  |
| 417 | `NtLockVirtualMemory` | `0x163E80` | 24 | UnwindData |  |
| 2064 | `ZwLockVirtualMemory` | `0x163E80` | 24 | UnwindData |  |
| 418 | `NtMakePermanentObject` | `0x163EA0` | 24 | UnwindData |  |
| 2065 | `ZwMakePermanentObject` | `0x163EA0` | 24 | UnwindData |  |
| 419 | `NtMakeTemporaryObject` | `0x163EC0` | 24 | UnwindData |  |
| 2066 | `ZwMakeTemporaryObject` | `0x163EC0` | 24 | UnwindData |  |
| 420 | `NtManageHotPatch` | `0x163EE0` | 24 | UnwindData |  |
| 2067 | `ZwManageHotPatch` | `0x163EE0` | 24 | UnwindData |  |
| 421 | `NtManagePartition` | `0x163F00` | 24 | UnwindData |  |
| 2068 | `ZwManagePartition` | `0x163F00` | 24 | UnwindData |  |
| 422 | `NtMapCMFModule` | `0x163F20` | 24 | UnwindData |  |
| 2069 | `ZwMapCMFModule` | `0x163F20` | 24 | UnwindData |  |
| 423 | `NtMapUserPhysicalPages` | `0x163F40` | 24 | UnwindData |  |
| 2070 | `ZwMapUserPhysicalPages` | `0x163F40` | 24 | UnwindData |  |
| 426 | `NtMapViewOfSectionEx` | `0x163F60` | 24 | UnwindData |  |
| 2073 | `ZwMapViewOfSectionEx` | `0x163F60` | 24 | UnwindData |  |
| 427 | `NtModifyBootEntry` | `0x163F80` | 24 | UnwindData |  |
| 2074 | `ZwModifyBootEntry` | `0x163F80` | 24 | UnwindData |  |
| 428 | `NtModifyDriverEntry` | `0x163FA0` | 24 | UnwindData |  |
| 2075 | `ZwModifyDriverEntry` | `0x163FA0` | 24 | UnwindData |  |
| 429 | `NtNotifyChangeDirectoryFile` | `0x163FC0` | 24 | UnwindData |  |
| 2076 | `ZwNotifyChangeDirectoryFile` | `0x163FC0` | 24 | UnwindData |  |
| 430 | `NtNotifyChangeDirectoryFileEx` | `0x163FE0` | 24 | UnwindData |  |
| 2077 | `ZwNotifyChangeDirectoryFileEx` | `0x163FE0` | 24 | UnwindData |  |
| 431 | `NtNotifyChangeKey` | `0x164000` | 24 | UnwindData |  |
| 2078 | `ZwNotifyChangeKey` | `0x164000` | 24 | UnwindData |  |
| 432 | `NtNotifyChangeMultipleKeys` | `0x164020` | 24 | UnwindData |  |
| 2079 | `ZwNotifyChangeMultipleKeys` | `0x164020` | 24 | UnwindData |  |
| 433 | `NtNotifyChangeSession` | `0x164040` | 24 | UnwindData |  |
| 2080 | `ZwNotifyChangeSession` | `0x164040` | 24 | UnwindData |  |
| 434 | `NtOpenCpuPartition` | `0x164060` | 24 | UnwindData |  |
| 2081 | `ZwOpenCpuPartition` | `0x164060` | 24 | UnwindData |  |
| 436 | `NtOpenEnlistment` | `0x164080` | 24 | UnwindData |  |
| 2083 | `ZwOpenEnlistment` | `0x164080` | 24 | UnwindData |  |
| 438 | `NtOpenEventPair` | `0x1640A0` | 24 | UnwindData |  |
| 2085 | `ZwOpenEventPair` | `0x1640A0` | 24 | UnwindData |  |
| 440 | `NtOpenIoCompletion` | `0x1640C0` | 24 | UnwindData |  |
| 2087 | `ZwOpenIoCompletion` | `0x1640C0` | 24 | UnwindData |  |
| 441 | `NtOpenJobObject` | `0x1640E0` | 24 | UnwindData |  |
| 2088 | `ZwOpenJobObject` | `0x1640E0` | 24 | UnwindData |  |
| 443 | `NtOpenKeyEx` | `0x164100` | 24 | UnwindData |  |
| 2090 | `ZwOpenKeyEx` | `0x164100` | 24 | UnwindData |  |
| 444 | `NtOpenKeyTransacted` | `0x164120` | 24 | UnwindData |  |
| 2091 | `ZwOpenKeyTransacted` | `0x164120` | 24 | UnwindData |  |
| 445 | `NtOpenKeyTransactedEx` | `0x164140` | 24 | UnwindData |  |
| 2092 | `ZwOpenKeyTransactedEx` | `0x164140` | 24 | UnwindData |  |
| 446 | `NtOpenKeyedEvent` | `0x164160` | 24 | UnwindData |  |
| 2093 | `ZwOpenKeyedEvent` | `0x164160` | 24 | UnwindData |  |
| 447 | `NtOpenMutant` | `0x164180` | 24 | UnwindData |  |
| 2094 | `ZwOpenMutant` | `0x164180` | 24 | UnwindData |  |
| 448 | `NtOpenObjectAuditAlarm` | `0x1641A0` | 24 | UnwindData |  |
| 2095 | `ZwOpenObjectAuditAlarm` | `0x1641A0` | 24 | UnwindData |  |
| 449 | `NtOpenPartition` | `0x1641C0` | 24 | UnwindData |  |
| 2096 | `ZwOpenPartition` | `0x1641C0` | 24 | UnwindData |  |
| 450 | `NtOpenPrivateNamespace` | `0x1641E0` | 24 | UnwindData |  |
| 2097 | `ZwOpenPrivateNamespace` | `0x1641E0` | 24 | UnwindData |  |
| 452 | `NtOpenProcessToken` | `0x164200` | 24 | UnwindData |  |
| 2099 | `ZwOpenProcessToken` | `0x164200` | 24 | UnwindData |  |
| 454 | `NtOpenRegistryTransaction` | `0x164220` | 24 | UnwindData |  |
| 2101 | `ZwOpenRegistryTransaction` | `0x164220` | 24 | UnwindData |  |
| 455 | `NtOpenResourceManager` | `0x164240` | 24 | UnwindData |  |
| 2102 | `ZwOpenResourceManager` | `0x164240` | 24 | UnwindData |  |
| 457 | `NtOpenSemaphore` | `0x164260` | 24 | UnwindData |  |
| 2104 | `ZwOpenSemaphore` | `0x164260` | 24 | UnwindData |  |
| 458 | `NtOpenSession` | `0x164280` | 24 | UnwindData |  |
| 2105 | `ZwOpenSession` | `0x164280` | 24 | UnwindData |  |
| 459 | `NtOpenSymbolicLinkObject` | `0x1642A0` | 24 | UnwindData |  |
| 2106 | `ZwOpenSymbolicLinkObject` | `0x1642A0` | 24 | UnwindData |  |
| 460 | `NtOpenThread` | `0x1642C0` | 24 | UnwindData |  |
| 2107 | `ZwOpenThread` | `0x1642C0` | 24 | UnwindData |  |
| 463 | `NtOpenTimer` | `0x1642E0` | 24 | UnwindData |  |
| 2110 | `ZwOpenTimer` | `0x1642E0` | 24 | UnwindData |  |
| 464 | `NtOpenTransaction` | `0x164300` | 24 | UnwindData |  |
| 2111 | `ZwOpenTransaction` | `0x164300` | 24 | UnwindData |  |
| 465 | `NtOpenTransactionManager` | `0x164320` | 24 | UnwindData |  |
| 2112 | `ZwOpenTransactionManager` | `0x164320` | 24 | UnwindData |  |
| 466 | `NtPlugPlayControl` | `0x164340` | 24 | UnwindData |  |
| 2113 | `ZwPlugPlayControl` | `0x164340` | 24 | UnwindData |  |
| 468 | `NtPrePrepareComplete` | `0x164360` | 24 | UnwindData |  |
| 2115 | `ZwPrePrepareComplete` | `0x164360` | 24 | UnwindData |  |
| 469 | `NtPrePrepareEnlistment` | `0x164380` | 24 | UnwindData |  |
| 2116 | `ZwPrePrepareEnlistment` | `0x164380` | 24 | UnwindData |  |
| 470 | `NtPrepareComplete` | `0x1643A0` | 24 | UnwindData |  |
| 2117 | `ZwPrepareComplete` | `0x1643A0` | 24 | UnwindData |  |
| 471 | `NtPrepareEnlistment` | `0x1643C0` | 24 | UnwindData |  |
| 2118 | `ZwPrepareEnlistment` | `0x1643C0` | 24 | UnwindData |  |
| 472 | `NtPrivilegeCheck` | `0x1643E0` | 24 | UnwindData |  |
| 2119 | `ZwPrivilegeCheck` | `0x1643E0` | 24 | UnwindData |  |
| 473 | `NtPrivilegeObjectAuditAlarm` | `0x164400` | 24 | UnwindData |  |
| 2120 | `ZwPrivilegeObjectAuditAlarm` | `0x164400` | 24 | UnwindData |  |
| 474 | `NtPrivilegedServiceAuditAlarm` | `0x164420` | 24 | UnwindData |  |
| 2121 | `ZwPrivilegedServiceAuditAlarm` | `0x164420` | 24 | UnwindData |  |
| 475 | `NtPropagationComplete` | `0x164440` | 24 | UnwindData |  |
| 2122 | `ZwPropagationComplete` | `0x164440` | 24 | UnwindData |  |
| 476 | `NtPropagationFailed` | `0x164460` | 24 | UnwindData |  |
| 2123 | `ZwPropagationFailed` | `0x164460` | 24 | UnwindData |  |
| 478 | `NtPssCaptureVaSpaceBulk` | `0x164480` | 24 | UnwindData |  |
| 2125 | `ZwPssCaptureVaSpaceBulk` | `0x164480` | 24 | UnwindData |  |
| 479 | `NtPulseEvent` | `0x1644A0` | 24 | UnwindData |  |
| 2126 | `ZwPulseEvent` | `0x1644A0` | 24 | UnwindData |  |
| 481 | `NtQueryAuxiliaryCounterFrequency` | `0x1644C0` | 24 | UnwindData |  |
| 2128 | `ZwQueryAuxiliaryCounterFrequency` | `0x1644C0` | 24 | UnwindData |  |
| 482 | `NtQueryBootEntryOrder` | `0x1644E0` | 24 | UnwindData |  |
| 2129 | `ZwQueryBootEntryOrder` | `0x1644E0` | 24 | UnwindData |  |
| 483 | `NtQueryBootOptions` | `0x164500` | 24 | UnwindData |  |
| 2130 | `ZwQueryBootOptions` | `0x164500` | 24 | UnwindData |  |
| 484 | `NtQueryDebugFilterState` | `0x164520` | 24 | UnwindData |  |
| 2131 | `ZwQueryDebugFilterState` | `0x164520` | 24 | UnwindData |  |
| 488 | `NtQueryDirectoryFileEx` | `0x164540` | 24 | UnwindData |  |
| 2135 | `ZwQueryDirectoryFileEx` | `0x164540` | 24 | UnwindData |  |
| 489 | `NtQueryDirectoryObject` | `0x164560` | 24 | UnwindData |  |
| 2136 | `ZwQueryDirectoryObject` | `0x164560` | 24 | UnwindData |  |
| 490 | `NtQueryDriverEntryOrder` | `0x164580` | 24 | UnwindData |  |
| 2137 | `ZwQueryDriverEntryOrder` | `0x164580` | 24 | UnwindData |  |
| 491 | `NtQueryEaFile` | `0x1645A0` | 24 | UnwindData |  |
| 2138 | `ZwQueryEaFile` | `0x1645A0` | 24 | UnwindData |  |
| 493 | `NtQueryFullAttributesFile` | `0x1645C0` | 24 | UnwindData |  |
| 2140 | `ZwQueryFullAttributesFile` | `0x1645C0` | 24 | UnwindData |  |
| 494 | `NtQueryInformationAtom` | `0x1645E0` | 24 | UnwindData |  |
| 2141 | `ZwQueryInformationAtom` | `0x1645E0` | 24 | UnwindData |  |
| 495 | `NtQueryInformationByName` | `0x164600` | 24 | UnwindData |  |
| 2142 | `ZwQueryInformationByName` | `0x164600` | 24 | UnwindData |  |
| 496 | `NtQueryInformationCpuPartition` | `0x164620` | 24 | UnwindData |  |
| 2143 | `ZwQueryInformationCpuPartition` | `0x164620` | 24 | UnwindData |  |
| 497 | `NtQueryInformationEnlistment` | `0x164640` | 24 | UnwindData |  |
| 2144 | `ZwQueryInformationEnlistment` | `0x164640` | 24 | UnwindData |  |
| 499 | `NtQueryInformationJobObject` | `0x164660` | 24 | UnwindData |  |
| 2146 | `ZwQueryInformationJobObject` | `0x164660` | 24 | UnwindData |  |
| 500 | `NtQueryInformationPort` | `0x164680` | 24 | UnwindData |  |
| 2147 | `ZwQueryInformationPort` | `0x164680` | 24 | UnwindData |  |
| 502 | `NtQueryInformationResourceManager` | `0x1646A0` | 24 | UnwindData |  |
| 2149 | `ZwQueryInformationResourceManager` | `0x1646A0` | 24 | UnwindData |  |
| 505 | `NtQueryInformationTransaction` | `0x1646C0` | 24 | UnwindData |  |
| 2152 | `ZwQueryInformationTransaction` | `0x1646C0` | 24 | UnwindData |  |
| 506 | `NtQueryInformationTransactionManager` | `0x1646E0` | 24 | UnwindData |  |
| 2153 | `ZwQueryInformationTransactionManager` | `0x1646E0` | 24 | UnwindData |  |
| 507 | `NtQueryInformationWorkerFactory` | `0x164700` | 24 | UnwindData |  |
| 2154 | `ZwQueryInformationWorkerFactory` | `0x164700` | 24 | UnwindData |  |
| 508 | `NtQueryInstallUILanguage` | `0x164720` | 24 | UnwindData |  |
| 2155 | `ZwQueryInstallUILanguage` | `0x164720` | 24 | UnwindData |  |
| 509 | `NtQueryIntervalProfile` | `0x164740` | 24 | UnwindData |  |
| 2156 | `ZwQueryIntervalProfile` | `0x164740` | 24 | UnwindData |  |
| 510 | `NtQueryIoCompletion` | `0x164760` | 24 | UnwindData |  |
| 2157 | `ZwQueryIoCompletion` | `0x164760` | 24 | UnwindData |  |
| 511 | `NtQueryIoRingCapabilities` | `0x164780` | 24 | UnwindData |  |
| 2158 | `ZwQueryIoRingCapabilities` | `0x164780` | 24 | UnwindData |  |
| 513 | `NtQueryLicenseValue` | `0x1647A0` | 24 | UnwindData |  |
| 2160 | `ZwQueryLicenseValue` | `0x1647A0` | 24 | UnwindData |  |
| 514 | `NtQueryMultipleValueKey` | `0x1647C0` | 24 | UnwindData |  |
| 2161 | `ZwQueryMultipleValueKey` | `0x1647C0` | 24 | UnwindData |  |
| 515 | `NtQueryMutant` | `0x1647E0` | 24 | UnwindData |  |
| 2162 | `ZwQueryMutant` | `0x1647E0` | 24 | UnwindData |  |
| 517 | `NtQueryOpenSubKeys` | `0x164800` | 24 | UnwindData |  |
| 2164 | `ZwQueryOpenSubKeys` | `0x164800` | 24 | UnwindData |  |
| 518 | `NtQueryOpenSubKeysEx` | `0x164820` | 24 | UnwindData |  |
| 2165 | `ZwQueryOpenSubKeysEx` | `0x164820` | 24 | UnwindData |  |
| 520 | `NtQueryPortInformationProcess` | `0x164840` | 24 | UnwindData |  |
| 2167 | `ZwQueryPortInformationProcess` | `0x164840` | 24 | UnwindData |  |
| 521 | `NtQueryQuotaInformationFile` | `0x164860` | 24 | UnwindData |  |
| 2168 | `ZwQueryQuotaInformationFile` | `0x164860` | 24 | UnwindData |  |
| 523 | `NtQuerySecurityAttributesToken` | `0x164880` | 24 | UnwindData |  |
| 2170 | `ZwQuerySecurityAttributesToken` | `0x164880` | 24 | UnwindData |  |
| 524 | `NtQuerySecurityObject` | `0x1648A0` | 24 | UnwindData |  |
| 2171 | `ZwQuerySecurityObject` | `0x1648A0` | 24 | UnwindData |  |
| 525 | `NtQuerySecurityPolicy` | `0x1648C0` | 24 | UnwindData |  |
| 2172 | `ZwQuerySecurityPolicy` | `0x1648C0` | 24 | UnwindData |  |
| 526 | `NtQuerySemaphore` | `0x1648E0` | 24 | UnwindData |  |
| 2173 | `ZwQuerySemaphore` | `0x1648E0` | 24 | UnwindData |  |
| 527 | `NtQuerySymbolicLinkObject` | `0x164900` | 24 | UnwindData |  |
| 2174 | `ZwQuerySymbolicLinkObject` | `0x164900` | 24 | UnwindData |  |
| 528 | `NtQuerySystemEnvironmentValue` | `0x164920` | 24 | UnwindData |  |
| 2175 | `ZwQuerySystemEnvironmentValue` | `0x164920` | 24 | UnwindData |  |
| 529 | `NtQuerySystemEnvironmentValueEx` | `0x164940` | 24 | UnwindData |  |
| 2176 | `ZwQuerySystemEnvironmentValueEx` | `0x164940` | 24 | UnwindData |  |
| 531 | `NtQuerySystemInformationEx` | `0x164960` | 24 | UnwindData |  |
| 2178 | `ZwQuerySystemInformationEx` | `0x164960` | 24 | UnwindData |  |
| 534 | `NtQueryTimerResolution` | `0x164980` | 24 | UnwindData |  |
| 2181 | `ZwQueryTimerResolution` | `0x164980` | 24 | UnwindData |  |
| 538 | `NtQueryWnfStateData` | `0x1649A0` | 24 | UnwindData |  |
| 2185 | `ZwQueryWnfStateData` | `0x1649A0` | 24 | UnwindData |  |
| 539 | `NtQueryWnfStateNameInformation` | `0x1649C0` | 24 | UnwindData |  |
| 2186 | `ZwQueryWnfStateNameInformation` | `0x1649C0` | 24 | UnwindData |  |
| 541 | `NtQueueApcThreadEx` | `0x1649E0` | 24 | UnwindData |  |
| 2188 | `ZwQueueApcThreadEx` | `0x1649E0` | 24 | UnwindData |  |
| 542 | `NtQueueApcThreadEx2` | `0x164A00` | 24 | UnwindData |  |
| 2189 | `ZwQueueApcThreadEx2` | `0x164A00` | 24 | UnwindData |  |
| 543 | `NtRaiseException` | `0x164A20` | 24 | UnwindData |  |
| 2190 | `ZwRaiseException` | `0x164A20` | 24 | UnwindData |  |
| 544 | `NtRaiseHardError` | `0x164A40` | 24 | UnwindData |  |
| 2191 | `ZwRaiseHardError` | `0x164A40` | 24 | UnwindData |  |
| 547 | `NtReadOnlyEnlistment` | `0x164A60` | 24 | UnwindData |  |
| 2194 | `ZwReadOnlyEnlistment` | `0x164A60` | 24 | UnwindData |  |
| 550 | `NtReadVirtualMemoryEx` | `0x164A80` | 24 | UnwindData |  |
| 2197 | `ZwReadVirtualMemoryEx` | `0x164A80` | 24 | UnwindData |  |
| 551 | `NtRecoverEnlistment` | `0x164AA0` | 24 | UnwindData |  |
| 2198 | `ZwRecoverEnlistment` | `0x164AA0` | 24 | UnwindData |  |
| 552 | `NtRecoverResourceManager` | `0x164AC0` | 24 | UnwindData |  |
| 2199 | `ZwRecoverResourceManager` | `0x164AC0` | 24 | UnwindData |  |
| 553 | `NtRecoverTransactionManager` | `0x164AE0` | 24 | UnwindData |  |
| 2200 | `ZwRecoverTransactionManager` | `0x164AE0` | 24 | UnwindData |  |
| 554 | `NtRegisterProtocolAddressInformation` | `0x164B00` | 24 | UnwindData |  |
| 2201 | `ZwRegisterProtocolAddressInformation` | `0x164B00` | 24 | UnwindData |  |
| 555 | `NtRegisterThreadTerminatePort` | `0x164B20` | 24 | UnwindData |  |
| 2202 | `ZwRegisterThreadTerminatePort` | `0x164B20` | 24 | UnwindData |  |
| 556 | `NtReleaseKeyedEvent` | `0x164B40` | 24 | UnwindData |  |
| 2203 | `ZwReleaseKeyedEvent` | `0x164B40` | 24 | UnwindData |  |
| 559 | `NtReleaseWorkerFactoryWorker` | `0x164B60` | 24 | UnwindData |  |
| 2206 | `ZwReleaseWorkerFactoryWorker` | `0x164B60` | 24 | UnwindData |  |
| 561 | `NtRemoveIoCompletionEx` | `0x164B80` | 24 | UnwindData |  |
| 2208 | `ZwRemoveIoCompletionEx` | `0x164B80` | 24 | UnwindData |  |
| 562 | `NtRemoveProcessDebug` | `0x164BA0` | 24 | UnwindData |  |
| 2209 | `ZwRemoveProcessDebug` | `0x164BA0` | 24 | UnwindData |  |
| 563 | `NtRenameKey` | `0x164BC0` | 24 | UnwindData |  |
| 2210 | `ZwRenameKey` | `0x164BC0` | 24 | UnwindData |  |
| 564 | `NtRenameTransactionManager` | `0x164BE0` | 24 | UnwindData |  |
| 2211 | `ZwRenameTransactionManager` | `0x164BE0` | 24 | UnwindData |  |
| 565 | `NtReplaceKey` | `0x164C00` | 24 | UnwindData |  |
| 2212 | `ZwReplaceKey` | `0x164C00` | 24 | UnwindData |  |
| 566 | `NtReplacePartitionUnit` | `0x164C20` | 24 | UnwindData |  |
| 2213 | `ZwReplacePartitionUnit` | `0x164C20` | 24 | UnwindData |  |
| 570 | `NtReplyWaitReplyPort` | `0x164C40` | 24 | UnwindData |  |
| 2217 | `ZwReplyWaitReplyPort` | `0x164C40` | 24 | UnwindData |  |
| 571 | `NtRequestPort` | `0x164C60` | 24 | UnwindData |  |
| 2218 | `ZwRequestPort` | `0x164C60` | 24 | UnwindData |  |
| 573 | `NtResetEvent` | `0x164C80` | 24 | UnwindData |  |
| 2220 | `ZwResetEvent` | `0x164C80` | 24 | UnwindData |  |
| 574 | `NtResetWriteWatch` | `0x164CA0` | 24 | UnwindData |  |
| 2221 | `ZwResetWriteWatch` | `0x164CA0` | 24 | UnwindData |  |
| 575 | `NtRestoreKey` | `0x164CC0` | 24 | UnwindData |  |
| 2222 | `ZwRestoreKey` | `0x164CC0` | 24 | UnwindData |  |
| 576 | `NtResumeProcess` | `0x164CE0` | 24 | UnwindData |  |
| 2223 | `ZwResumeProcess` | `0x164CE0` | 24 | UnwindData |  |
| 578 | `NtRevertContainerImpersonation` | `0x164D00` | 24 | UnwindData |  |
| 2225 | `ZwRevertContainerImpersonation` | `0x164D00` | 24 | UnwindData |  |
| 579 | `NtRollbackComplete` | `0x164D20` | 24 | UnwindData |  |
| 2226 | `ZwRollbackComplete` | `0x164D20` | 24 | UnwindData |  |
| 580 | `NtRollbackEnlistment` | `0x164D40` | 24 | UnwindData |  |
| 2227 | `ZwRollbackEnlistment` | `0x164D40` | 24 | UnwindData |  |
| 581 | `NtRollbackRegistryTransaction` | `0x164D60` | 24 | UnwindData |  |
| 2228 | `ZwRollbackRegistryTransaction` | `0x164D60` | 24 | UnwindData |  |
| 582 | `NtRollbackTransaction` | `0x164D80` | 24 | UnwindData |  |
| 2229 | `ZwRollbackTransaction` | `0x164D80` | 24 | UnwindData |  |
| 583 | `NtRollforwardTransactionManager` | `0x164DA0` | 24 | UnwindData |  |
| 2230 | `ZwRollforwardTransactionManager` | `0x164DA0` | 24 | UnwindData |  |
| 584 | `NtSaveKey` | `0x164DC0` | 24 | UnwindData |  |
| 2231 | `ZwSaveKey` | `0x164DC0` | 24 | UnwindData |  |
| 585 | `NtSaveKeyEx` | `0x164DE0` | 24 | UnwindData |  |
| 2232 | `ZwSaveKeyEx` | `0x164DE0` | 24 | UnwindData |  |
| 586 | `NtSaveMergedKeys` | `0x164E00` | 24 | UnwindData |  |
| 2233 | `ZwSaveMergedKeys` | `0x164E00` | 24 | UnwindData |  |
| 587 | `NtSecureConnectPort` | `0x164E20` | 24 | UnwindData |  |
| 2234 | `ZwSecureConnectPort` | `0x164E20` | 24 | UnwindData |  |
| 588 | `NtSerializeBoot` | `0x164E40` | 24 | UnwindData |  |
| 2235 | `ZwSerializeBoot` | `0x164E40` | 24 | UnwindData |  |
| 589 | `NtSetBootEntryOrder` | `0x164E60` | 24 | UnwindData |  |
| 2236 | `ZwSetBootEntryOrder` | `0x164E60` | 24 | UnwindData |  |
| 590 | `NtSetBootOptions` | `0x164E80` | 24 | UnwindData |  |
| 2237 | `ZwSetBootOptions` | `0x164E80` | 24 | UnwindData |  |
| 591 | `NtSetCachedSigningLevel` | `0x164EA0` | 24 | UnwindData |  |
| 2238 | `ZwSetCachedSigningLevel` | `0x164EA0` | 24 | UnwindData |  |
| 592 | `NtSetCachedSigningLevel2` | `0x164EC0` | 24 | UnwindData |  |
| 2239 | `ZwSetCachedSigningLevel2` | `0x164EC0` | 24 | UnwindData |  |
| 593 | `NtSetContextThread` | `0x164EE0` | 24 | UnwindData |  |
| 2240 | `ZwSetContextThread` | `0x164EE0` | 24 | UnwindData |  |
| 594 | `NtSetDebugFilterState` | `0x164F00` | 24 | UnwindData |  |
| 2241 | `ZwSetDebugFilterState` | `0x164F00` | 24 | UnwindData |  |
| 595 | `NtSetDefaultHardErrorPort` | `0x164F20` | 24 | UnwindData |  |
| 2242 | `ZwSetDefaultHardErrorPort` | `0x164F20` | 24 | UnwindData |  |
| 596 | `NtSetDefaultLocale` | `0x164F40` | 24 | UnwindData |  |
| 2243 | `ZwSetDefaultLocale` | `0x164F40` | 24 | UnwindData |  |
| 597 | `NtSetDefaultUILanguage` | `0x164F60` | 24 | UnwindData |  |
| 2244 | `ZwSetDefaultUILanguage` | `0x164F60` | 24 | UnwindData |  |
| 598 | `NtSetDriverEntryOrder` | `0x164F80` | 24 | UnwindData |  |
| 2245 | `ZwSetDriverEntryOrder` | `0x164F80` | 24 | UnwindData |  |
| 599 | `NtSetEaFile` | `0x164FA0` | 24 | UnwindData |  |
| 2246 | `ZwSetEaFile` | `0x164FA0` | 24 | UnwindData |  |
| 602 | `NtSetEventEx` | `0x164FC0` | 24 | UnwindData |  |
| 2249 | `ZwSetEventEx` | `0x164FC0` | 24 | UnwindData |  |
| 603 | `NtSetHighEventPair` | `0x164FE0` | 24 | UnwindData |  |
| 2250 | `ZwSetHighEventPair` | `0x164FE0` | 24 | UnwindData |  |
| 604 | `NtSetHighWaitLowEventPair` | `0x165000` | 24 | UnwindData |  |
| 2251 | `ZwSetHighWaitLowEventPair` | `0x165000` | 24 | UnwindData |  |
| 605 | `NtSetIRTimer` | `0x165020` | 24 | UnwindData |  |
| 2252 | `ZwSetIRTimer` | `0x165020` | 24 | UnwindData |  |
| 606 | `NtSetInformationCpuPartition` | `0x165040` | 24 | UnwindData |  |
| 2253 | `ZwSetInformationCpuPartition` | `0x165040` | 24 | UnwindData |  |
| 607 | `NtSetInformationDebugObject` | `0x165060` | 24 | UnwindData |  |
| 2254 | `ZwSetInformationDebugObject` | `0x165060` | 24 | UnwindData |  |
| 608 | `NtSetInformationEnlistment` | `0x165080` | 24 | UnwindData |  |
| 2255 | `ZwSetInformationEnlistment` | `0x165080` | 24 | UnwindData |  |
| 610 | `NtSetInformationIoRing` | `0x1650A0` | 24 | UnwindData |  |
| 2257 | `ZwSetInformationIoRing` | `0x1650A0` | 24 | UnwindData |  |
| 611 | `NtSetInformationJobObject` | `0x1650C0` | 24 | UnwindData |  |
| 2258 | `ZwSetInformationJobObject` | `0x1650C0` | 24 | UnwindData |  |
| 612 | `NtSetInformationKey` | `0x1650E0` | 24 | UnwindData |  |
| 2259 | `ZwSetInformationKey` | `0x1650E0` | 24 | UnwindData |  |
| 615 | `NtSetInformationResourceManager` | `0x165100` | 24 | UnwindData |  |
| 2262 | `ZwSetInformationResourceManager` | `0x165100` | 24 | UnwindData |  |
| 616 | `NtSetInformationSymbolicLink` | `0x165120` | 24 | UnwindData |  |
| 2263 | `ZwSetInformationSymbolicLink` | `0x165120` | 24 | UnwindData |  |
| 618 | `NtSetInformationToken` | `0x165140` | 24 | UnwindData |  |
| 2265 | `ZwSetInformationToken` | `0x165140` | 24 | UnwindData |  |
| 619 | `NtSetInformationTransaction` | `0x165160` | 24 | UnwindData |  |
| 2266 | `ZwSetInformationTransaction` | `0x165160` | 24 | UnwindData |  |
| 620 | `NtSetInformationTransactionManager` | `0x165180` | 24 | UnwindData |  |
| 2267 | `ZwSetInformationTransactionManager` | `0x165180` | 24 | UnwindData |  |
| 621 | `NtSetInformationVirtualMemory` | `0x1651A0` | 24 | UnwindData |  |
| 2268 | `ZwSetInformationVirtualMemory` | `0x1651A0` | 24 | UnwindData |  |
| 622 | `NtSetInformationWorkerFactory` | `0x1651C0` | 24 | UnwindData |  |
| 2269 | `ZwSetInformationWorkerFactory` | `0x1651C0` | 24 | UnwindData |  |
| 623 | `NtSetIntervalProfile` | `0x1651E0` | 24 | UnwindData |  |
| 2270 | `ZwSetIntervalProfile` | `0x1651E0` | 24 | UnwindData |  |
| 624 | `NtSetIoCompletion` | `0x165200` | 24 | UnwindData |  |
| 2271 | `ZwSetIoCompletion` | `0x165200` | 24 | UnwindData |  |
| 625 | `NtSetIoCompletionEx` | `0x165220` | 24 | UnwindData |  |
| 2272 | `ZwSetIoCompletionEx` | `0x165220` | 24 | UnwindData |  |
| 626 | `NtSetLdtEntries` | `0x165240` | 24 | UnwindData |  |
| 2273 | `ZwSetLdtEntries` | `0x165240` | 24 | UnwindData |  |
| 627 | `NtSetLowEventPair` | `0x165260` | 24 | UnwindData |  |
| 2274 | `ZwSetLowEventPair` | `0x165260` | 24 | UnwindData |  |
| 628 | `NtSetLowWaitHighEventPair` | `0x165280` | 24 | UnwindData |  |
| 2275 | `ZwSetLowWaitHighEventPair` | `0x165280` | 24 | UnwindData |  |
| 629 | `NtSetQuotaInformationFile` | `0x1652A0` | 24 | UnwindData |  |
| 2276 | `ZwSetQuotaInformationFile` | `0x1652A0` | 24 | UnwindData |  |
| 630 | `NtSetSecurityObject` | `0x1652C0` | 24 | UnwindData |  |
| 2277 | `ZwSetSecurityObject` | `0x1652C0` | 24 | UnwindData |  |
| 631 | `NtSetSystemEnvironmentValue` | `0x1652E0` | 24 | UnwindData |  |
| 2278 | `ZwSetSystemEnvironmentValue` | `0x1652E0` | 24 | UnwindData |  |
| 632 | `NtSetSystemEnvironmentValueEx` | `0x165300` | 24 | UnwindData |  |
| 2279 | `ZwSetSystemEnvironmentValueEx` | `0x165300` | 24 | UnwindData |  |
| 633 | `NtSetSystemInformation` | `0x165320` | 24 | UnwindData |  |
| 2280 | `ZwSetSystemInformation` | `0x165320` | 24 | UnwindData |  |
| 634 | `NtSetSystemPowerState` | `0x165340` | 24 | UnwindData |  |
| 2281 | `ZwSetSystemPowerState` | `0x165340` | 24 | UnwindData |  |
| 635 | `NtSetSystemTime` | `0x165360` | 24 | UnwindData |  |
| 2282 | `ZwSetSystemTime` | `0x165360` | 24 | UnwindData |  |
| 636 | `NtSetThreadExecutionState` | `0x165380` | 24 | UnwindData |  |
| 2283 | `ZwSetThreadExecutionState` | `0x165380` | 24 | UnwindData |  |
| 638 | `NtSetTimer2` | `0x1653A0` | 24 | UnwindData |  |
| 2285 | `ZwSetTimer2` | `0x1653A0` | 24 | UnwindData |  |
| 639 | `NtSetTimerEx` | `0x1653C0` | 24 | UnwindData |  |
| 2286 | `ZwSetTimerEx` | `0x1653C0` | 24 | UnwindData |  |
| 640 | `NtSetTimerResolution` | `0x1653E0` | 24 | UnwindData |  |
| 2287 | `ZwSetTimerResolution` | `0x1653E0` | 24 | UnwindData |  |
| 641 | `NtSetUuidSeed` | `0x165400` | 24 | UnwindData |  |
| 2288 | `ZwSetUuidSeed` | `0x165400` | 24 | UnwindData |  |
| 643 | `NtSetVolumeInformationFile` | `0x165420` | 24 | UnwindData |  |
| 2290 | `ZwSetVolumeInformationFile` | `0x165420` | 24 | UnwindData |  |
| 644 | `NtSetWnfProcessNotificationEvent` | `0x165440` | 24 | UnwindData |  |
| 2291 | `ZwSetWnfProcessNotificationEvent` | `0x165440` | 24 | UnwindData |  |
| 645 | `NtShutdownSystem` | `0x165460` | 24 | UnwindData |  |
| 2292 | `ZwShutdownSystem` | `0x165460` | 24 | UnwindData |  |
| 646 | `NtShutdownWorkerFactory` | `0x165480` | 24 | UnwindData |  |
| 2293 | `ZwShutdownWorkerFactory` | `0x165480` | 24 | UnwindData |  |
| 647 | `NtSignalAndWaitForSingleObject` | `0x1654A0` | 24 | UnwindData |  |
| 2294 | `ZwSignalAndWaitForSingleObject` | `0x1654A0` | 24 | UnwindData |  |
| 648 | `NtSinglePhaseReject` | `0x1654C0` | 24 | UnwindData |  |
| 2295 | `ZwSinglePhaseReject` | `0x1654C0` | 24 | UnwindData |  |
| 649 | `NtStartProfile` | `0x1654E0` | 24 | UnwindData |  |
| 2296 | `ZwStartProfile` | `0x1654E0` | 24 | UnwindData |  |
| 650 | `NtStopProfile` | `0x165500` | 24 | UnwindData |  |
| 2297 | `ZwStopProfile` | `0x165500` | 24 | UnwindData |  |
| 651 | `NtSubmitIoRing` | `0x165520` | 24 | UnwindData |  |
| 2298 | `ZwSubmitIoRing` | `0x165520` | 24 | UnwindData |  |
| 652 | `NtSubscribeWnfStateChange` | `0x165540` | 24 | UnwindData |  |
| 2299 | `ZwSubscribeWnfStateChange` | `0x165540` | 24 | UnwindData |  |
| 653 | `NtSuspendProcess` | `0x165560` | 24 | UnwindData |  |
| 2300 | `ZwSuspendProcess` | `0x165560` | 24 | UnwindData |  |
| 654 | `NtSuspendThread` | `0x165580` | 24 | UnwindData |  |
| 2301 | `ZwSuspendThread` | `0x165580` | 24 | UnwindData |  |
| 655 | `NtSystemDebugControl` | `0x1655A0` | 24 | UnwindData |  |
| 2302 | `ZwSystemDebugControl` | `0x1655A0` | 24 | UnwindData |  |
| 656 | `NtTerminateEnclave` | `0x1655C0` | 24 | UnwindData |  |
| 2303 | `ZwTerminateEnclave` | `0x1655C0` | 24 | UnwindData |  |
| 657 | `NtTerminateJobObject` | `0x1655E0` | 24 | UnwindData |  |
| 2304 | `ZwTerminateJobObject` | `0x1655E0` | 24 | UnwindData |  |
| 660 | `NtTestAlert` | `0x165600` | 24 | UnwindData |  |
| 2307 | `ZwTestAlert` | `0x165600` | 24 | UnwindData |  |
| 661 | `NtThawRegistry` | `0x165620` | 24 | UnwindData |  |
| 2308 | `ZwThawRegistry` | `0x165620` | 24 | UnwindData |  |
| 662 | `NtThawTransactions` | `0x165640` | 24 | UnwindData |  |
| 2309 | `ZwThawTransactions` | `0x165640` | 24 | UnwindData |  |
| 663 | `NtTraceControl` | `0x165660` | 24 | UnwindData |  |
| 2310 | `ZwTraceControl` | `0x165660` | 24 | UnwindData |  |
| 665 | `NtTranslateFilePath` | `0x165680` | 24 | UnwindData |  |
| 2312 | `ZwTranslateFilePath` | `0x165680` | 24 | UnwindData |  |
| 666 | `NtUmsThreadYield` | `0x1656A0` | 24 | UnwindData |  |
| 2313 | `ZwUmsThreadYield` | `0x1656A0` | 24 | UnwindData |  |
| 667 | `NtUnloadDriver` | `0x1656C0` | 24 | UnwindData |  |
| 2314 | `ZwUnloadDriver` | `0x1656C0` | 24 | UnwindData |  |
| 668 | `NtUnloadKey` | `0x1656E0` | 24 | UnwindData |  |
| 2315 | `ZwUnloadKey` | `0x1656E0` | 24 | UnwindData |  |
| 669 | `NtUnloadKey2` | `0x165700` | 24 | UnwindData |  |
| 2316 | `ZwUnloadKey2` | `0x165700` | 24 | UnwindData |  |
| 670 | `NtUnloadKeyEx` | `0x165720` | 24 | UnwindData |  |
| 2317 | `ZwUnloadKeyEx` | `0x165720` | 24 | UnwindData |  |
| 671 | `NtUnlockFile` | `0x165740` | 24 | UnwindData |  |
| 2318 | `ZwUnlockFile` | `0x165740` | 24 | UnwindData |  |
| 672 | `NtUnlockVirtualMemory` | `0x165760` | 24 | UnwindData |  |
| 2319 | `ZwUnlockVirtualMemory` | `0x165760` | 24 | UnwindData |  |
| 674 | `NtUnmapViewOfSectionEx` | `0x165780` | 24 | UnwindData |  |
| 2321 | `ZwUnmapViewOfSectionEx` | `0x165780` | 24 | UnwindData |  |
| 675 | `NtUnsubscribeWnfStateChange` | `0x1657A0` | 24 | UnwindData |  |
| 2322 | `ZwUnsubscribeWnfStateChange` | `0x1657A0` | 24 | UnwindData |  |
| 676 | `NtUpdateWnfStateData` | `0x1657C0` | 24 | UnwindData |  |
| 2323 | `ZwUpdateWnfStateData` | `0x1657C0` | 24 | UnwindData |  |
| 677 | `NtVdmControl` | `0x1657E0` | 24 | UnwindData |  |
| 2324 | `ZwVdmControl` | `0x1657E0` | 24 | UnwindData |  |
| 678 | `NtWaitForAlertByThreadId` | `0x165800` | 24 | UnwindData |  |
| 2325 | `ZwWaitForAlertByThreadId` | `0x165800` | 24 | UnwindData |  |
| 679 | `NtWaitForDebugEvent` | `0x165820` | 24 | UnwindData |  |
| 2326 | `ZwWaitForDebugEvent` | `0x165820` | 24 | UnwindData |  |
| 680 | `NtWaitForKeyedEvent` | `0x165840` | 24 | UnwindData |  |
| 2327 | `ZwWaitForKeyedEvent` | `0x165840` | 24 | UnwindData |  |
| 684 | `NtWaitForWorkViaWorkerFactory` | `0x165860` | 24 | UnwindData |  |
| 2331 | `ZwWaitForWorkViaWorkerFactory` | `0x165860` | 24 | UnwindData |  |
| 685 | `NtWaitHighEventPair` | `0x165880` | 24 | UnwindData |  |
| 2332 | `ZwWaitHighEventPair` | `0x165880` | 24 | UnwindData |  |
| 686 | `NtWaitLowEventPair` | `0x1658A0` | 24 | UnwindData |  |
| 2333 | `ZwWaitLowEventPair` | `0x1658A0` | 24 | UnwindData |  |
| 395 | `NtGetTickCount` | `0x1658C0` | 5 | UnwindData |  |
| 1035 | `RtlFirstEntrySList` | `0x165910` | 7 | UnwindData |  |
| 1217 | `RtlInterlockedPopEntrySList` | `0x165920` | 52 | UnwindData |  |
| 105 | `ExpInterlockedPopEntrySListResume` | `0x165927` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `ExpInterlockedPopEntrySListFault` | `0x165937` | 9 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `ExpInterlockedPopEntrySListEnd` | `0x165940` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1219 | `RtlInterlockedPushListSList` | `0x1659D0` | 51 | UnwindData |  |
| 107 | `KiUserApcDispatcher` | `0x165AA0` | 131 | UnwindData |  |
| 108 | `KiUserCallbackDispatcher` | `0x165BC0` | 59 | UnwindData |  |
| 109 | `KiUserExceptionDispatcher` | `0x165C10` | 92 | UnwindData |  |
| 106 | `KiRaiseUserExceptionDispatcher` | `0x165C80` | 73 | UnwindData |  |
| 969 | `RtlEnclaveCallDispatch` | `0x165CE0` | 103 | UnwindData |  |
| 970 | `RtlEnclaveCallDispatchReturn` | `0x165D11` | 63 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `RtlCallEnclave` | `0x165D50` | 207 | UnwindData |  |
| 782 | `RtlCallEnclaveReturn` | `0x165DBB` | 117 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `RtlCompareMemory` | `0x165E30` | 122 | UnwindData |  |
| 819 | `RtlCompareMemoryUlong` | `0x165EB0` | 36 | UnwindData |  |
| 848 | `RtlCopyMemoryNonTemporal` | `0x165EE0` | 270 | UnwindData |  |
| 1010 | `RtlFillMemoryNonTemporal` | `0x166020` | 233 | UnwindData |  |
| 1079 | `RtlGetCurrentProcessorNumber` | `0x166120` | 97 | UnwindData |  |
| 1080 | `RtlGetCurrentProcessorNumberEx` | `0x166190` | 92 | UnwindData |  |
| 1418 | `RtlRaiseExceptionForReturnAddressHijack` | `0x166200` | 69 | UnwindData |  |
| 2341 | `__chkstk` | `0x166260` | 77 | UnwindData |  |
| 2367 | `_setjmp` | `0x166FF0` | 144 | UnwindData |  |
| 2368 | `_setjmpex` | `0x1670B0` | 144 | UnwindData |  |
| 847 | `RtlCopyMemory` | `0x167300` | 682 | UnwindData |  |
| 1316 | `RtlMoveMemory` | `0x167300` | 682 | UnwindData |  |
| 2455 | `memcpy` | `0x167300` | 682 | UnwindData |  |
| 2457 | `memmove` | `0x167300` | 682 | UnwindData |  |
| 2454 | `memcmp` | `0x1675D0` | 199 | UnwindData |  |
| 2469 | `strcat` | `0x167970` | 179 | UnwindData |  |
| 2473 | `strcpy` | `0x167A30` | 183 | UnwindData |  |
| 2472 | `strcmp` | `0x167B10` | 176 | UnwindData |  |
| 2476 | `strlen` | `0x167BE0` | 168 | UnwindData |  |
| 2477 | `strncat` | `0x167CB0` | 413 | UnwindData |  |
| 2479 | `strncmp` | `0x167E70` | 181 | UnwindData |  |
| 2480 | `strncpy` | `0x167F50` | 362 | UnwindData |  |
| 755 | `RtlAllocateMemoryBlockLookaside` | `0x170010` | 291 | UnwindData |  |
| 756 | `RtlAllocateMemoryZone` | `0x170140` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `RtlFreeMemoryBlockLookaside` | `0x1701A0` | 28 | UnwindData |  |
| 2459 | `memset` | `0x172030` | 9,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1731 | `RtlpScpCfgNtdllExports` | `0x174680` | 1,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1335 | `RtlNtdllName` | `0x174DB0` | 92,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2349 | `_fltused` | `0x18B888` | 268,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `NlsAnsiCodePage` | `0x1CD048` | 4,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `NlsMbOemCodePageTag` | `0x1CE3C0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `NlsMbCodePageTag` | `0x1CE5D0` | 232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1705 | `RtlpFreezeTimeBias` | `0x1CE6B8` | 97,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `KiUserInvertedFunctionTable` | `0x1E6420` | 12,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `LdrSystemDllInitBlock` | `0x1E9440` | 0 | Indeterminate |  |
