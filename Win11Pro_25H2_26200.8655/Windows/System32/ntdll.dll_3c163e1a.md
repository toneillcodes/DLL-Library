# Binary Specification: ntdll.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ntdll.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3c163e1a808c566871bdfcdac5f5afdfa799b7fef359f8695e99db808211f0c4`
* **Total Exported Functions:** 2517

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1540 | `RtlSetUserFlagsHeap` | `0x1D70` | 847 | UnwindData |  |
| 1149 | `RtlGetUserInfoHeap` | `0x2600` | 774 | UnwindData |  |
| 1541 | `RtlSetUserValueHeap` | `0x3050` | 744 | UnwindData |  |
| 1644 | `RtlValidateHeap` | `0x3610` | 535 | UnwindData |  |
| 1611 | `RtlUnlockHeap` | `0x3D30` | 335 | UnwindData |  |
| 1297 | `RtlLockHeap` | `0x3F20` | 430 | UnwindData |  |
| 1548 | `RtlSizeHeap` | `0x4510` | 64 | UnwindData |  |
| 943 | `RtlDestroyQueryDebugBuffer` | `0x5680` | 51 | UnwindData |  |
| 1392 | `RtlQueryProcessDebugInformation` | `0x5810` | 2,455 | UnwindData |  |
| 1368 | `RtlQueryCriticalSectionOwner` | `0x6CA0` | 270 | UnwindData |  |
| 1393 | `RtlQueryProcessHeapInformation` | `0x6EF0` | 1,528 | UnwindData |  |
| 1377 | `RtlQueryHeapInformation` | `0x7680` | 512 | UnwindData |  |
| 1391 | `RtlQueryProcessBackTraceInformation` | `0x7890` | 631 | UnwindData |  |
| 1394 | `RtlQueryProcessLockInformation` | `0x7B10` | 659 | UnwindData |  |
| 145 | `LdrInitializeThunk` | `0x8540` | 32 | UnwindData |  |
| 1268 | `RtlIsProcessorFeaturePresent` | `0x8730` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `RtlLoadString` | `0x8860` | 641 | UnwindData |  |
| 1436 | `RtlRegisterFeatureConfigurationChangeNotification` | `0x8CA0` | 147 | UnwindData |  |
| 1421 | `RtlRandom` | `0x8F30` | 358 | UnwindData |  |
| 1422 | `RtlRandomEx` | `0x8F30` | 358 | UnwindData |  |
| 1478 | `RtlRunOnceExecuteOnce` | `0x9380` | 269 | UnwindData |  |
| 166 | `LdrResFindResourceDirectory` | `0x94A0` | 134 | UnwindData |  |
| 169 | `LdrResSearchResource` | `0x9530` | 1,929 | UnwindData |  |
| 1477 | `RtlRunOnceComplete` | `0x9DA0` | 147 | UnwindData |  |
| 1412 | `RtlQueryWnfStateData` | `0x9EC0` | 36 | UnwindData |  |
| 1413 | `RtlQueryWnfStateDataWithExplicitScope` | `0x9EF0` | 210 | UnwindData |  |
| 1653 | `RtlWakeAddressAll` | `0x9FD0` | 23 | UnwindData |  |
| 1191 | `RtlInitializeCriticalSectionAndSpinCount` | `0x9FF0` | 379 | UnwindData |  |
| 1190 | `RtlInitializeCriticalSection` | `0xA180` | 336 | UnwindData |  |
| 1560 | `RtlSubscribeWnfStateChangeNotification` | `0xA2E0` | 68 | UnwindData |  |
| 1618 | `RtlUnsubscribeWnfNotificationWaitForCompletion` | `0xAFA0` | 122 | UnwindData |  |
| 1620 | `RtlUnsubscribeWnfStateChangeNotification` | `0xB020` | 76 | UnwindData |  |
| 1200 | `RtlInitializeResource` | `0xB4F0` | 94 | UnwindData |  |
| 1652 | `RtlWaitOnAddress` | `0xC660` | 101 | UnwindData |  |
| 1192 | `RtlInitializeCriticalSectionEx` | `0xCEF0` | 59 | UnwindData |  |
| 971 | `RtlEncodePointer` | `0xD7F0` | 96 | UnwindData |  |
| 139 | `LdrGetProcedureAddress` | `0xD8B0` | 30 | UnwindData |  |
| 140 | `LdrGetProcedureAddressEx` | `0xDCF0` | 33 | UnwindData |  |
| 141 | `LdrGetProcedureAddressForCaller` | `0xDD20` | 130 | UnwindData |  |
| 1491 | `RtlSetBits` | `0xEF90` | 10 | UnwindData |  |
| 777 | `RtlAvlInsertNodeEx` | `0xF6F0` | 34 | UnwindData |  |
| 737 | `RtlAddGrowableFunctionTable` | `0xF8D0` | 73 | UnwindData |  |
| 1160 | `RtlImageDirectoryEntryToData` | `0x11730` | 410 | UnwindData |  |
| 1468 | `RtlRestoreContext` | `0x11BD0` | 911 | UnwindData |  |
| 1153 | `RtlGuardCheckLongJumpTarget` | `0x11FE0` | 462 | UnwindData |  |
| 117 | `LdrControlFlowGuardEnforced` | `0x12A20` | 2,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `LdrGetDllHandle` | `0x134B0` | 471 | UnwindData |  |
| 134 | `LdrGetDllHandleEx` | `0x13690` | 587 | UnwindData |  |
| 1318 | `RtlMultiByteToUnicodeN` | `0x14E00` | 15 | UnwindData |  |
| 895 | `RtlCustomCPToUnicodeN` | `0x14FB0` | 192 | UnwindData |  |
| 1591 | `RtlUTF8ToUnicodeN` | `0x15120` | 57 | UnwindData |  |
| 760 | `RtlAnsiStringToUnicodeString` | `0x15C90` | 856 | UnwindData |  |
| 900 | `RtlDeactivateActivationContextUnsafeFast` | `0x182A0` | 251 | UnwindData |  |
| 717 | `RtlAcquireSRWLockShared` | `0x18F50` | 85 | UnwindData |  |
| 1449 | `RtlReleaseSRWLockShared` | `0x18FB0` | 300 | UnwindData |  |
| 1770 | `TpCallbackSendAlpcMessageOnCompletion` | `0x19E90` | 98 | UnwindData |  |
| 754 | `RtlAllocateHeap` | `0x19F90` | 2,790 | UnwindData |  |
| 1549 | `RtlSleepConditionVariableCS` | `0x1C060` | 575 | UnwindData |  |
| 977 | `RtlEnterCriticalSection` | `0x1D620` | 244 | UnwindData |  |
| 1282 | `RtlLeaveCriticalSection` | `0x1D720` | 777 | UnwindData |  |
| 1720 | `RtlpNotOwnerCriticalSection` | `0x1DA30` | 211 | UnwindData |  |
| 1420 | `RtlRaiseStatus` | `0x1DB10` | 107 | UnwindData |  |
| 1312 | `RtlLookupFunctionTable` | `0x1DDB0` | 131 | UnwindData |  |
| 1311 | `RtlLookupFunctionEntry` | `0x1DE40` | 160 | UnwindData |  |
| 1622 | `RtlUnwindEx` | `0x1E1B0` | 2,711 | UnwindData |  |
| 1650 | `RtlVirtualUnwind2` | `0x1EC50` | 50 | UnwindData |  |
| 1649 | `RtlVirtualUnwind` | `0x21950` | 422 | UnwindData |  |
| 1292 | `RtlLocateExtendedFeature` | `0x21C30` | 345 | UnwindData |  |
| 902 | `RtlDecodePointer` | `0x23170` | 108 | UnwindData |  |
| 130 | `LdrGetDllFullName` | `0x231F0` | 252 | UnwindData |  |
| 1380 | `RtlQueryInformationActivationContext` | `0x23900` | 1,904 | UnwindData |  |
| 185 | `LdrUnloadDll` | `0x243E0` | 22 | UnwindData |  |
| 1586 | `RtlTryAcquireSRWLockExclusive` | `0x24680` | 112 | UnwindData |  |
| 1761 | `TpAllocWork` | `0x24B80` | 378 | UnwindData |  |
| 67 | `EtwEventActivityIdControl` | `0x251D0` | 293 | UnwindData |  |
| 1469 | `RtlRestoreLastWin32Error` | `0x25300` | 72 | UnwindData |  |
| 1510 | `RtlSetLastWin32Error` | `0x25300` | 72 | UnwindData |  |
| 1333 | `RtlNtStatusToDosError` | `0x25350` | 400 | UnwindData |  |
| 170 | `LdrResolveDelayLoadedAPI` | `0x25BD0` | 666 | UnwindData |  |
| 86 | `EtwNotificationUnregister` | `0x25E70` | 269 | UnwindData |  |
| 70 | `EtwEventRegister` | `0x26130` | 20 | UnwindData |  |
| 85 | `EtwNotificationRegister` | `0x26180` | 528 | UnwindData |  |
| 65 | `EtwDeliverDataBlock` | `0x26E80` | 33 | UnwindData |  |
| 1587 | `RtlTryAcquireSRWLockShared` | `0x27540` | 373 | UnwindData |  |
| 1805 | `TpSetWaitEx` | `0x28E10` | 104 | UnwindData |  |
| 1767 | `TpCallbackMayRunLong` | `0x2AD70` | 73 | UnwindData |  |
| 1534 | `RtlSetThreadSubProcessTag` | `0x2AE90` | 243 | UnwindData |  |
| 175 | `LdrSetDllDirectory` | `0x2EE30` | 104 | UnwindData |  |
| 1123 | `RtlGetPersistedStateLocation` | `0x2F350` | 97 | UnwindData |  |
| 1053 | `RtlFreeHeap` | `0x2F720` | 2,748 | UnwindData |  |
| 885 | `RtlCreateUnicodeString` | `0x30D80` | 129 | UnwindData |  |
| 944 | `RtlDetectHeapLeaks` | `0x3AFF0` | 465 | UnwindData |  |
| 880 | `RtlCreateTagHeap` | `0x3B340` | 670 | UnwindData |  |
| 33 | `CsrCaptureMessageBuffer` | `0x3BC60` | 85 | UnwindData |  |
| 38 | `CsrClientConnectToServer` | `0x3BFF0` | 490 | UnwindData |  |
| 34 | `CsrCaptureMessageMultiUnicodeStringsInPlace` | `0x3C2B0` | 285 | UnwindData |  |
| 35 | `CsrCaptureMessageString` | `0x3C3E0` | 17 | UnwindData |  |
| 31 | `CsrAllocateCaptureBuffer` | `0x3C520` | 200 | UnwindData |  |
| 39 | `CsrFreeCaptureBuffer` | `0x3C5F0` | 36 | UnwindData |  |
| 37 | `CsrClientCallServer` | `0x3C620` | 450 | UnwindData |  |
| 32 | `CsrAllocateMessagePointer` | `0x3C7F0` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 868 | `RtlCreateHeap` | `0x3CCE0` | 40 | UnwindData |  |
| 1575 | `RtlTlsFree` | `0x3EE30` | 192 | UnwindData |  |
| 805 | `RtlClearBits` | `0x3EF00` | 10 | UnwindData |  |
| 919 | `RtlDeleteFunctionTable` | `0x3FA40` | 508 | UnwindData |  |
| 920 | `RtlDeleteGrowableFunctionTable` | `0x3FC50` | 408 | UnwindData |  |
| 778 | `RtlAvlRemoveNode` | `0x3FDF0` | 1,000 | UnwindData |  |
| 939 | `RtlDestroyHeap` | `0x401E0` | 996 | UnwindData |  |
| 1360 | `RtlProtectHeap` | `0x40780` | 196 | UnwindData |  |
| 924 | `RtlDeleteResource` | `0x40F20` | 128 | UnwindData |  |
| 915 | `RtlDeleteCriticalSection` | `0x40FB0` | 392 | UnwindData |  |
| 1550 | `RtlSleepConditionVariableSRW` | `0x42500` | 49 | UnwindData |  |
| 1658 | `RtlWakeConditionVariable` | `0x43100` | 40 | UnwindData |  |
| 1424 | `RtlRbRemoveNode` | `0x4A3F0` | 40 | UnwindData |  |
| 1423 | `RtlRbInsertNodeEx` | `0x4D500` | 134 | UnwindData |  |
| 1081 | `RtlGetCurrentServiceSessionId` | `0x4E070` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `RtlAcquireSRWLockExclusive` | `0x4E130` | 79 | UnwindData |  |
| 1448 | `RtlReleaseSRWLockExclusive` | `0x4EE00` | 167 | UnwindData |  |
| 1162 | `RtlImageNtHeaderEx` | `0x51740` | 263 | UnwindData |  |
| 149 | `LdrLoadDll` | `0x51850` | 313 | UnwindData |  |
| 1103 | `RtlGetImageFileMachines` | `0x51B30` | 1,871 | UnwindData |  |
| 914 | `RtlDeleteBoundaryDescriptor` | `0x52290` | 5,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 952 | `RtlDosApplyFileIsolationRedirection_Ustr` | `0x53830` | 47 | UnwindData |  |
| 1015 | `RtlFindActivationContextSectionString` | `0x56320` | 61 | UnwindData |  |
| 1441 | `RtlReleaseActivationContext` | `0x56B40` | 40 | UnwindData |  |
| 46 | `DbgPrintEx` | `0x57100` | 54 | UnwindData |  |
| 1014 | `RtlFindActivationContextSectionGuid` | `0x57140` | 82 | UnwindData |  |
| 172 | `LdrRscIsTypeExist` | `0x57570` | 531 | UnwindData |  |
| 148 | `LdrLoadAlternateResourceModuleEx` | `0x58590` | 5,455 | UnwindData |  |
| 184 | `LdrUnloadAlternateResourceModuleEx` | `0x59E70` | 512 | UnwindData |  |
| 1027 | `RtlFindMessage` | `0x5A2C0` | 276 | UnwindData |  |
| 113 | `LdrAddLoadAsDataTable` | `0x5C800` | 566 | UnwindData |  |
| 164 | `LdrRemoveLoadAsDataTable` | `0x5CA40` | 836 | UnwindData |  |
| 790 | `RtlCharToInteger` | `0x5CE60` | 454 | UnwindData |  |
| 748 | `RtlAddressInSectionTable` | `0x5D030` | 89 | UnwindData |  |
| 1430 | `RtlReAllocateHeap` | `0x5D260` | 204 | UnwindData |  |
| 124 | `LdrFindEntryForAddress` | `0x5D4A0` | 78 | UnwindData |  |
| 1367 | `RtlQueryAtomInAtomTable` | `0x5D500` | 529 | UnwindData |  |
| 912 | `RtlDeleteAtomFromAtomTable` | `0x5D720` | 155 | UnwindData |  |
| 753 | `RtlAllocateHandle` | `0x5DDE0` | 522 | UnwindData |  |
| 1273 | `RtlIsValidHandle` | `0x5E1A0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `RtlIsNameInExpression` | `0x5E290` | 111 | UnwindData |  |
| 1034 | `RtlFindUnicodeSubstring` | `0x5E860` | 220 | UnwindData |  |
| 1601 | `RtlUnicodeStringToOemString` | `0x5ECE0` | 273 | UnwindData |  |
| 1458 | `RtlReplaceSystemDirectoryInPath` | `0x5EF70` | 180 | UnwindData |  |
| 1674 | `RtlWow64GetProcessMachines` | `0x5F030` | 469 | UnwindData |  |
| 1596 | `RtlUnicodeStringToAnsiSize` | `0x5F990` | 172 | UnwindData |  |
| 1600 | `RtlUnicodeStringToOemSize` | `0x5F990` | 172 | UnwindData |  |
| 1745 | `RtlxUnicodeStringToAnsiSize` | `0x5F990` | 172 | UnwindData |  |
| 1746 | `RtlxUnicodeStringToOemSize` | `0x5F990` | 172 | UnwindData |  |
| 1597 | `RtlUnicodeStringToAnsiString` | `0x608A0` | 811 | UnwindData |  |
| 1605 | `RtlUnicodeToMultiByteSize` | `0x60BE0` | 171 | UnwindData |  |
| 1629 | `RtlUpcaseUnicodeToMultiByteN` | `0x60CA0` | 941 | UnwindData |  |
| 1603 | `RtlUnicodeToCustomCPN` | `0x61060` | 90 | UnwindData |  |
| 1607 | `RtlUnicodeToUTF8N` | `0x611C0` | 54 | UnwindData |  |
| 1604 | `RtlUnicodeToMultiByteN` | `0x61760` | 363 | UnwindData |  |
| 765 | `RtlAppendUnicodeToString` | `0x61EE0` | 74 | UnwindData |  |
| 1119 | `RtlGetNtSystemRoot` | `0x61FA0` | 7,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1051 | `RtlFreeAnsiString` | `0x63EC0` | 36 | UnwindData |  |
| 1059 | `RtlFreeUTF8String` | `0x63EC0` | 36 | UnwindData |  |
| 1060 | `RtlFreeUnicodeString` | `0x63EC0` | 36 | UnwindData |  |
| 1071 | `RtlGetAppContainerSidType` | `0x64960` | 118 | UnwindData |  |
| 1070 | `RtlGetAppContainerParent` | `0x64A50` | 215 | UnwindData |  |
| 1264 | `RtlIsParentOfChildAppContainer` | `0x64B30` | 110 | UnwindData |  |
| 793 | `RtlCheckPortableOperatingSystem` | `0x64F20` | 204 | UnwindData |  |
| 1697 | `RtlpCheckDynamicTimeZoneInformation` | `0x65000` | 416 | UnwindData |  |
| 1400 | `RtlQueryRegistryValuesEx` | `0x651B0` | 30 | UnwindData |  |
| 794 | `RtlCheckRegistryKey` | `0x65430` | 58 | UnwindData |  |
| 1690 | `RtlWriteRegistryValue` | `0x66520` | 196 | UnwindData |  |
| 1399 | `RtlQueryRegistryValues` | `0x666A0` | 30 | UnwindData |  |
| 923 | `RtlDeleteRegistryValue` | `0x666D0` | 141 | UnwindData |  |
| 711 | `RtlAcquirePebLock` | `0x66860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1444 | `RtlReleasePebLock` | `0x66880` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1712 | `RtlpIsQualifiedLanguage` | `0x66C90` | 366 | UnwindData |  |
| 1096 | `RtlGetFileMUIPath` | `0x66E10` | 222 | UnwindData |  |
| 1098 | `RtlGetFullPathName_U` | `0x67960` | 132 | UnwindData |  |
| 859 | `RtlCreateActivationContext` | `0x68190` | 398 | UnwindData |  |
| 1182 | `RtlInitUnicodeStringEx` | `0x69C20` | 76 | UnwindData |  |
| 959 | `RtlDosSearchPath_U` | `0x69E70` | 566 | UnwindData |  |
| 1090 | `RtlGetExePath` | `0x6A0B0` | 77 | UnwindData |  |
| 865 | `RtlCreateEnvironmentEx` | `0x6A330` | 579 | UnwindData |  |
| 1129 | `RtlGetSearchPath` | `0x6A580` | 66 | UnwindData |  |
| 937 | `RtlDestroyEnvironment` | `0x6A5D0` | 17 | UnwindData |  |
| 1502 | `RtlSetEnvironmentVariable` | `0x6A5F0` | 55 | UnwindData |  |
| 1501 | `RtlSetEnvironmentVar` | `0x6A630` | 2,369 | UnwindData |  |
| 945 | `RtlDetermineDosPathNameType_U` | `0x6B2D0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `LdrGetDllPath` | `0x6B4A0` | 35 | UnwindData |  |
| 1373 | `RtlQueryEnvironmentVariable_U` | `0x6C4E0` | 102 | UnwindData |  |
| 1003 | `RtlExpandEnvironmentStrings_U` | `0x6C550` | 139 | UnwindData |  |
| 1002 | `RtlExpandEnvironmentStrings` | `0x6C5F0` | 14 | UnwindData |  |
| 1372 | `RtlQueryEnvironmentVariable` | `0x6C7B0` | 2,500 | UnwindData |  |
| 1386 | `RtlQueryPackageIdentity` | `0x6E630` | 84 | UnwindData |  |
| 1387 | `RtlQueryPackageIdentityEx` | `0x6E690` | 98 | UnwindData |  |
| 1385 | `RtlQueryPackageClaims` | `0x6E700` | 778 | UnwindData |  |
| 1171 | `RtlInitCodePageTable` | `0x6EEE0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1363 | `RtlQueryActivationContextApplicationSettings` | `0x6F0D0` | 567 | UnwindData |  |
| 1648 | `RtlVerifyVersionInfo` | `0x6F830` | 952 | UnwindData |  |
| 833 | `RtlConvertDeviceFamilyInfoToString` | `0x6FC20` | 229 | UnwindData |  |
| 1706 | `RtlpGetDeviceFamilyInfoEnum` | `0x6FD10` | 40 | UnwindData |  |
| 1563 | `RtlSwitchedVVI` | `0x700B0` | 1,138 | UnwindData |  |
| 1748 | `SbSelectProcedure` | `0x707B0` | 1,822 | UnwindData |  |
| 1151 | `RtlGetVersion` | `0x70EE0` | 868 | UnwindData |  |
| 1118 | `RtlGetNtProductType` | `0x71250` | 113 | UnwindData |  |
| 1133 | `RtlGetSuiteMask` | `0x712D0` | 15,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `DbgPrint` | `0x74EC0` | 66 | UnwindData |  |
| 1518 | `RtlSetProcessPreferredUILanguages` | `0x75000` | 52 | UnwindData |  |
| 1703 | `RtlpCreateProcessRegistryInfo` | `0x76C80` | 126 | UnwindData |  |
| 1532 | `RtlSetThreadPreferredUILanguages` | `0x77150` | 1,349 | UnwindData |  |
| 1122 | `RtlGetParentLocaleName` | `0x77F80` | 536 | UnwindData |  |
| 1104 | `RtlGetIntegerAtom` | `0x781A0` | 199 | UnwindData |  |
| 1304 | `RtlLookupAtomInAtomTable` | `0x791B0` | 913 | UnwindData |  |
| 1599 | `RtlUnicodeStringToInteger` | `0x79550` | 537 | UnwindData |  |
| 1291 | `RtlLocaleNameToLcid` | `0x79770` | 337 | UnwindData |  |
| 894 | `RtlCultureNameToLCID` | `0x798D0` | 199 | UnwindData |  |
| 1727 | `RtlpQueryDefaultUILanguage` | `0x7B670` | 7 | UnwindData |  |
| 1279 | `RtlLCIDToCultureName` | `0x7BA70` | 683 | UnwindData |  |
| 1349 | `RtlOpenCurrentUser` | `0x7C9A0` | 285 | UnwindData |  |
| 1142 | `RtlGetThreadPreferredUILanguages` | `0x7CAD0` | 3,422 | UnwindData |  |
| 722 | `RtlAddAccessAllowedAceEx` | `0x7D840` | 118 | UnwindData |  |
| 728 | `RtlAddAce` | `0x7DF60` | 397 | UnwindData |  |
| 1288 | `RtlLengthSidAsUnicodeString` | `0x7E100` | 91 | UnwindData |  |
| 1047 | `RtlFormatCurrentUserKeyPath` | `0x7E370` | 85 | UnwindData |  |
| 721 | `RtlAddAccessAllowedAce` | `0x7E550` | 104 | UnwindData |  |
| 839 | `RtlConvertSidToUnicodeString` | `0x7E7F0` | 71 | UnwindData |  |
| 1642 | `RtlValidSid` | `0x7EBD0` | 44 | UnwindData |  |
| 1638 | `RtlValidAcl` | `0x7EC10` | 453 | UnwindData |  |
| 1641 | `RtlValidSecurityDescriptor` | `0x7F040` | 251 | UnwindData |  |
| 1204 | `RtlInitializeSidEx` | `0x7F150` | 107 | UnwindData |  |
| 76 | `EtwEventWriteFull` | `0x7F1D0` | 68 | UnwindData |  |
| 1112 | `RtlGetMultiTimePrecise` | `0x7F220` | 80 | UnwindData |  |
| 799 | `RtlCheckTokenMembershipEx` | `0x7F420` | 177 | UnwindData |  |
| 785 | `RtlCapabilityCheck` | `0x7F9A0` | 42 | UnwindData |  |
| 1388 | `RtlQueryPerformanceCounter` | `0x7FFD0` | 243 | UnwindData |  |
| 1476 | `RtlRunOnceBeginInitialize` | `0x800D0` | 62 | UnwindData |  |
| 935 | `RtlDeriveCapabilitySidsFromName` | `0x801D0` | 128 | UnwindData |  |
| 1256 | `RtlIsMultiSessionSku` | `0x803F0` | 52 | UnwindData |  |
| 73 | `EtwEventWrite` | `0x80430` | 160 | UnwindData |  |
| 80 | `EtwEventWriteTransfer` | `0x80730` | 175 | UnwindData |  |
| 797 | `RtlCheckTokenCapability` | `0x81840` | 1,124 | UnwindData |  |
| 1242 | `RtlIsCapabilitySid` | `0x81CB0` | 66 | UnwindData |  |
| 789 | `RtlCaptureStackBackTrace` | `0x820B0` | 147 | UnwindData |  |
| 1659 | `RtlWalkFrameChain` | `0x82150` | 61 | UnwindData |  |
| 1139 | `RtlGetSystemTimePrecise` | `0x832B0` | 385 | UnwindData |  |
| 1067 | `RtlGetActiveActivationContext` | `0x834A0` | 89 | UnwindData |  |
| 718 | `RtlActivateActivationContext` | `0x835D0` | 39 | UnwindData |  |
| 719 | `RtlActivateActivationContextEx` | `0x83740` | 84 | UnwindData |  |
| 741 | `RtlAddRefActivationContext` | `0x83E30` | 4,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `EtwProcessPrivateLoggerRequest` | `0x84FE0` | 44 | UnwindData |  |
| 1657 | `RtlWakeAllConditionVariable` | `0x86DF0` | 54 | UnwindData |  |
| 1298 | `RtlLockMemoryBlockLookaside` | `0x875E0` | 117 | UnwindData |  |
| 1300 | `RtlLockMemoryZone` | `0x87660` | 274 | UnwindData |  |
| 1615 | `RtlUnlockModuleSection` | `0x878E0` | 162 | UnwindData |  |
| 1301 | `RtlLockModuleSection` | `0x87990` | 298 | UnwindData |  |
| 122 | `LdrEnumerateLoadedModules` | `0x87B00` | 185 | UnwindData |  |
| 1636 | `RtlUserFiberStart` | `0x87BC0` | 36 | UnwindData |  |
| 1637 | `RtlUserThreadStart` | `0x87BF0` | 92 | UnwindData |  |
| 1001 | `RtlExitUserThread` | `0x87C60` | 88 | UnwindData |  |
| 1000 | `RtlExitUserProcess` | `0x87CC0` | 224 | UnwindData |  |
| 1776 | `TpCheckTerminateWorker` | `0x87DB0` | 138 | UnwindData |  |
| 180 | `LdrShutdownThread` | `0x87F80` | 841 | UnwindData |  |
| 1058 | `RtlFreeThreadActivationContextStack` | `0x88410` | 48 | UnwindData |  |
| 1050 | `RtlFreeActivationContextStack` | `0x88450` | 206 | UnwindData |  |
| 1461 | `RtlReportSilentProcessExit` | `0x88860` | 495 | UnwindData |  |
| 179 | `LdrShutdownProcess` | `0x88A60` | 931 | UnwindData |  |
| 143 | `LdrInitShimEngineDynamic` | `0x89980` | 245 | UnwindData |  |
| 1140 | `RtlGetThreadErrorMode` | `0x8B280` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `EtwEventWriteNoRegistration` | `0x8B2F0` | 209 | UnwindData |  |
| 1763 | `TpAlpcUnregisterCompletionList` | `0x8E8A0` | 50 | UnwindData |  |
| 1773 | `TpCallbackUnloadDllOnCompletion` | `0x8F0D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1810 | `TpWaitForAlpcCompletion` | `0x8F110` | 97 | UnwindData |  |
| 1786 | `TpReleaseCleanupGroupMembers` | `0x8F180` | 786 | UnwindData |  |
| 1788 | `TpReleaseJobNotification` | `0x8F5F0` | 158 | UnwindData |  |
| 1800 | `TpSetPoolThreadCpuSets` | `0x8FFD0` | 177 | UnwindData |  |
| 1795 | `TpSetPoolMaxThreads` | `0x90110` | 136 | UnwindData |  |
| 1801 | `TpSetPoolWorkerThreadIdleTimeout` | `0x901A0` | 80 | UnwindData |  |
| 1812 | `TpWaitForJobNotification` | `0x90200` | 53 | UnwindData |  |
| 1785 | `TpReleaseCleanupGroup` | `0x902B0` | 94 | UnwindData |  |
| 1755 | `TpAllocCleanupGroup` | `0x90320` | 235 | UnwindData |  |
| 1784 | `TpReleaseAlpcCompletion` | `0x90420` | 164 | UnwindData |  |
| 1787 | `TpReleaseIoCompletion` | `0x90590` | 160 | UnwindData |  |
| 1774 | `TpCancelAsyncIoOperation` | `0x90730` | 267 | UnwindData |  |
| 1633 | `RtlUpdateTimer` | `0x90890` | 252 | UnwindData |  |
| 1771 | `TpCallbackSendPendingAlpcMessage` | `0x909A0` | 54 | UnwindData |  |
| 1796 | `TpSetPoolMaxThreadsSoftLimit` | `0x90A90` | 73 | UnwindData |  |
| 1758 | `TpAllocPool` | `0x90BA0` | 60 | UnwindData |  |
| 1806 | `TpSimpleTryPost` | `0x90CC0` | 368 | UnwindData |  |
| 1409 | `RtlQueryUnbiasedInterruptTime` | `0x910B0` | 12 | UnwindData |  |
| 1334 | `RtlNtStatusToDosErrorNoTeb` | `0x91160` | 54 | UnwindData |  |
| 926 | `RtlDeleteTimer` | `0x912D0` | 460 | UnwindData |  |
| 1808 | `TpTimerOutstandingCallbackCount` | `0x914B0` | 146 | UnwindData |  |
| 1762 | `TpAlpcRegisterCompletionList` | `0x91660` | 138 | UnwindData |  |
| 1803 | `TpSetTimerEx` | `0x916F0` | 129 | UnwindData |  |
| 1781 | `TpIsTimerSet` | `0x91E20` | 95 | UnwindData |  |
| 1790 | `TpReleaseTimer` | `0x91FF0` | 356 | UnwindData |  |
| 1813 | `TpWaitForTimer` | `0x92880` | 103 | UnwindData |  |
| 1792 | `TpReleaseWork` | `0x93410` | 353 | UnwindData |  |
| 1759 | `TpAllocTimer` | `0x93580` | 102 | UnwindData |  |
| 881 | `RtlCreateTimer` | `0x937B0` | 672 | UnwindData |  |
| 1815 | `TpWaitForWork` | `0x94000` | 104 | UnwindData |  |
| 1415 | `RtlQueueWorkItem` | `0x94150` | 1,306 | UnwindData |  |
| 1440 | `RtlRegisterWait` | `0x94670` | 928 | UnwindData |  |
| 934 | `RtlDeregisterWaitEx` | `0x94A20` | 448 | UnwindData |  |
| 1791 | `TpReleaseWait` | `0x94C30` | 137 | UnwindData |  |
| 1760 | `TpAllocWait` | `0x94F50` | 110 | UnwindData |  |
| 1814 | `TpWaitForWait` | `0x952A0` | 91 | UnwindData |  |
| 1353 | `RtlPcToFileHeader` | `0x956B0` | 102 | UnwindData |  |
| 114 | `LdrAddRefDll` | `0x95940` | 27 | UnwindData |  |
| 8 | *Ordinal Only* | `0x965D0` | 167 | UnwindData |  |
| 899 | `RtlDeactivateActivationContext` | `0x96680` | 67 | UnwindData |  |
| 720 | `RtlActivateActivationContextUnsafeFast` | `0x96B10` | 351 | UnwindData |  |
| 1417 | `RtlRaiseException` | `0x96C80` | 639 | UnwindData |  |
| 1634 | `RtlUpperChar` | `0x97060` | 30 | UnwindData |  |
| 1208 | `RtlInsertElementGenericTableFullAvl` | `0x97C50` | 340 | UnwindData |  |
| 917 | `RtlDeleteElementGenericTableAvl` | `0x982B0` | 220 | UnwindData |  |
| 1206 | `RtlInsertElementGenericTableAvl` | `0x983A0` | 534 | UnwindData |  |
| 1308 | `RtlLookupElementGenericTableFullAvl` | `0x986B0` | 242 | UnwindData |  |
| 1306 | `RtlLookupElementGenericTableAvl` | `0x987B0` | 43 | UnwindData |  |
| 822 | `RtlCompareUnicodeStrings` | `0x98CC0` | 338 | UnwindData |  |
| 918 | `RtlDeleteElementGenericTableAvlEx` | `0x98E20` | 85 | UnwindData |  |
| 764 | `RtlAppendUnicodeStringToString` | `0x9C220` | 54 | UnwindData |  |
| 960 | `RtlDosSearchPath_Ustr` | `0x9D630` | 2,336 | UnwindData |  |
| 1446 | `RtlReleaseRelativeName` | `0x9DFA0` | 90 | UnwindData |  |
| 1100 | `RtlGetFullPathName_UstrEx` | `0x9E000` | 839 | UnwindData |  |
| 1077 | `RtlGetCurrentDirectory_U` | `0x9E8B0` | 54 | UnwindData |  |
| 191 | `LdrpResGetMappingSize` | `0x9F390` | 805 | UnwindData |  |
| 167 | `LdrResGetRCConfig` | `0x9F880` | 1,548 | UnwindData |  |
| 192 | `LdrpResGetResourceDirectory` | `0xA1DD0` | 1,306 | UnwindData |  |
| 1281 | `RtlLcidToLocaleName` | `0xA2EF0` | 629 | UnwindData |  |
| 1709 | `RtlpGetSystemDefaultUILanguage` | `0xA3950` | 172 | UnwindData |  |
| 1710 | `RtlpGetUserOrMachineUILanguage4NLS` | `0xA3CB0` | 480 | UnwindData |  |
| 1155 | `RtlHeapTrkInitialize` | `0xAA490` | 1,094 | UnwindData |  |
| 1506 | `RtlSetHeapInformation` | `0xAA990` | 574 | UnwindData |  |
| 151 | `LdrLockLoaderLock` | `0xAAD30` | 447 | UnwindData |  |
| 1589 | `RtlTryEnterCriticalSection` | `0xAB100` | 216 | UnwindData |  |
| 896 | `RtlCutoverTimeToSystemTime` | `0xAC920` | 559 | UnwindData |  |
| 1736 | `RtlpTimeToTimeFields` | `0xACB60` | 55 | UnwindData |  |
| 1735 | `RtlpTimeFieldsToTime` | `0xAD190` | 54 | UnwindData |  |
| 1038 | `RtlFlsAllocEx` | `0xAD7B0` | 50 | UnwindData |  |
| 1037 | `RtlFlsAlloc` | `0xAD8A0` | 33 | UnwindData |  |
| 1042 | `RtlFlsSetValue` | `0xADB00` | 61 | UnwindData |  |
| 1574 | `RtlTlsAlloc` | `0xADE50` | 545 | UnwindData |  |
| 1576 | `RtlTlsSetValue` | `0xAE080` | 154 | UnwindData |  |
| 1234 | `RtlIpv6AddressToStringExW` | `0xAE140` | 308 | UnwindData |  |
| 1159 | `RtlIdnToUnicode` | `0xAE280` | 134 | UnwindData |  |
| 1226 | `RtlIpv4AddressToStringExW` | `0xAE330` | 64 | UnwindData |  |
| 987 | `RtlEqualDomainName` | `0xAE410` | 158 | UnwindData |  |
| 1227 | `RtlIpv4AddressToStringW` | `0xAE5B0` | 75 | UnwindData |  |
| 1235 | `RtlIpv6AddressToStringW` | `0xAE610` | 38 | UnwindData |  |
| 1157 | `RtlIdnToAscii` | `0xAE910` | 219 | UnwindData |  |
| 1230 | `RtlIpv4StringToAddressExW` | `0xAEA00` | 448 | UnwindData |  |
| 784 | `RtlCanonicalizeDomainName` | `0xAEBD0` | 1,493 | UnwindData |  |
| 1238 | `RtlIpv6StringToAddressExW` | `0xAF1B0` | 712 | UnwindData |  |
| 1239 | `RtlIpv6StringToAddressW` | `0xAF480` | 1,021 | UnwindData |  |
| 1231 | `RtlIpv4StringToAddressW` | `0xB0750` | 748 | UnwindData |  |
| 1329 | `RtlNormalizeString` | `0xB1420` | 130 | UnwindData |  |
| 1262 | `RtlIsNormalizedString` | `0xB18B0` | 134 | UnwindData |  |
| 1378 | `RtlQueryImageMitigationPolicy` | `0xB38C0` | 3,136 | UnwindData |  |
| 156 | `LdrQueryImageFileExecutionOptions` | `0xB57D0` | 54 | UnwindData |  |
| 157 | `LdrQueryImageFileExecutionOptionsEx` | `0xB5810` | 151 | UnwindData |  |
| 158 | `LdrQueryImageFileKeyOption` | `0xB58B0` | 890 | UnwindData |  |
| 1332 | `RtlNtPathNameToDosPathName` | `0xB64E0` | 627 | UnwindData |  |
| 1357 | `RtlPrefixUnicodeString` | `0xB6760` | 317 | UnwindData |  |
| 1317 | `RtlMultiAppendUnicodeStringBuffer` | `0xB68B0` | 97 | UnwindData |  |
| 1016 | `RtlFindCharInUnicodeString` | `0xB69D0` | 201 | UnwindData |  |
| 1704 | `RtlpEnsureBufferSize` | `0xB6E20` | 68 | UnwindData |  |
| 992 | `RtlEqualUnicodeString` | `0xB77A0` | 301 | UnwindData |  |
| 762 | `RtlAppendPathElement` | `0xB7940` | 669 | UnwindData |  |
| 150 | `LdrLoadEnclaveModule` | `0xB7FB0` | 587 | UnwindData |  |
| 144 | `LdrInitializeEnclave` | `0xB8360` | 262 | UnwindData |  |
| 1555 | `RtlStringFromGUIDEx` | `0xB8D90` | 131 | UnwindData |  |
| 1509 | `RtlSetIoCompletionCallback` | `0xB9150` | 325 | UnwindData |  |
| 1757 | `TpAllocJobNotification` | `0xB93F0` | 572 | UnwindData |  |
| 1753 | `TpAllocAlpcCompletion` | `0xB9640` | 30 | UnwindData |  |
| 1754 | `TpAllocAlpcCompletionEx` | `0xB96D0` | 30 | UnwindData |  |
| 1756 | `TpAllocIoCompletion` | `0xB9A20` | 553 | UnwindData |  |
| 981 | `RtlEnumerateGenericTable` | `0xB9E50` | 104 | UnwindData |  |
| 922 | `RtlDeleteNoSplay` | `0xB9EC0` | 197 | UnwindData |  |
| 916 | `RtlDeleteElementGenericTable` | `0xB9F90` | 193 | UnwindData |  |
| 910 | `RtlDelete` | `0xBA060` | 157 | UnwindData |  |
| 1561 | `RtlSubtreePredecessor` | `0xBA110` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `RtlInsertElementGenericTable` | `0xBA2C0` | 374 | UnwindData |  |
| 1207 | `RtlInsertElementGenericTableFull` | `0xBA440` | 278 | UnwindData |  |
| 1307 | `RtlLookupElementGenericTableFull` | `0xBA560` | 194 | UnwindData |  |
| 1305 | `RtlLookupElementGenericTable` | `0xBA630` | 111 | UnwindData |  |
| 1551 | `RtlSplay` | `0xBA6B0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1435 | `RtlRealSuccessor` | `0xBA8F0` | 11,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1193 | `RtlInitializeExtendedContext` | `0xBD670` | 261 | UnwindData |  |
| 1091 | `RtlGetExtendedContextLength` | `0xBD780` | 238 | UnwindData |  |
| 701 | `PssNtCaptureSnapshot` | `0xBD910` | 1,557 | UnwindData |  |
| 702 | `PssNtDuplicateSnapshot` | `0xBE6F0` | 120 | UnwindData |  |
| 704 | `PssNtFreeSnapshot` | `0xBE770` | 441 | UnwindData |  |
| 706 | `PssNtQuerySnapshot` | `0xBE930` | 652 | UnwindData |  |
| 708 | `PssNtWalkSnapshot` | `0xBEBD0` | 632 | UnwindData |  |
| 707 | `PssNtValidateDescriptor` | `0xBEE50` | 265 | UnwindData |  |
| 758 | `RtlAnsiCharToUnicodeChar` | `0xBFE60` | 12 | UnwindData |  |
| 1017 | `RtlFindClearBits` | `0xC0080` | 55 | UnwindData |  |
| 1018 | `RtlFindClearBitsAndSet` | `0xC0450` | 22 | UnwindData |  |
| 1525 | `RtlSetSecurityObjectEx` | `0xC08A0` | 55 | UnwindData |  |
| 1524 | `RtlSetSecurityObject` | `0xC1070` | 50 | UnwindData |  |
| 1543 | `RtlSidDominatesForTrust` | `0xC2930` | 134 | UnwindData |  |
| 1276 | `RtlIsValidProcessTrustLabelSid` | `0xC29C0` | 107 | UnwindData |  |
| 1542 | `RtlSidDominates` | `0xC2A40` | 131 | UnwindData |  |
| 739 | `RtlAddMandatoryAce` | `0xC2B60` | 425 | UnwindData |  |
| 852 | `RtlCopySid` | `0xC2D10` | 55 | UnwindData |  |
| 1325 | `RtlNewSecurityObjectEx` | `0xC2D50` | 100 | UnwindData |  |
| 989 | `RtlEqualPrefixSid` | `0xC76E0` | 237 | UnwindData |  |
| 908 | `RtlDefaultNpAcl` | `0xC7B00` | 1,014 | UnwindData |  |
| 858 | `RtlCreateAcl` | `0xC7F00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1069 | `RtlGetAppContainerNamedObjectPath` | `0xC7F40` | 118 | UnwindData |  |
| 990 | `RtlEqualSid` | `0xC8390` | 51 | UnwindData |  |
| 860 | `RtlCreateAndSetSD` | `0xC83D0` | 937 | UnwindData |  |
| 1513 | `RtlSetOwnerSecurityDescriptor` | `0xC8780` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `RtlSetGroupSecurityDescriptor` | `0xC87D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1521 | `RtlSetSaclSecurityDescriptor` | `0xC8820` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1493 | `RtlSetControlSecurityDescriptor` | `0xC8A10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `RtlCreateSystemVolumeInformationFolder` | `0xC8A60` | 726 | UnwindData |  |
| 1065 | `RtlGetAce` | `0xC90C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `RtlAbsoluteToSelfRelativeSD` | `0xC9110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1313 | `RtlMakeSelfRelativeSD` | `0xC9130` | 80 | UnwindData |  |
| 1484 | `RtlSelfRelativeToAbsoluteSD2` | `0xC9390` | 513 | UnwindData |  |
| 1181 | `RtlInitUnicodeString` | `0xCA4A0` | 69 | UnwindData |  |
| 1150 | `RtlGetUserPreferredUILanguages` | `0xCA4F0` | 1,575 | UnwindData |  |
| 1471 | `RtlRestoreThreadPreferredUILanguages` | `0xCACC0` | 218 | UnwindData |  |
| 1533 | `RtlSetThreadPreferredUILanguages2` | `0xCBFB0` | 414 | UnwindData |  |
| 1714 | `RtlpLoadUserUIByPolicy` | `0xCC160` | 548 | UnwindData |  |
| 1137 | `RtlGetSystemPreferredUILanguages` | `0xCC420` | 1,343 | UnwindData |  |
| 800 | `RtlCleanUpTEBLangLists` | `0xCCAC0` | 196 | UnwindData |  |
| 1145 | `RtlGetUILanguageInfo` | `0xCCBE0` | 156 | UnwindData |  |
| 1716 | `RtlpMuiFreeLangRegistryInfo` | `0xCDD90` | 74 | UnwindData |  |
| 1275 | `RtlIsValidLocaleName` | `0xCE4C0` | 165 | UnwindData |  |
| 1719 | `RtlpMuiRegLoadRegistryInfo` | `0xCE570` | 345 | UnwindData |  |
| 1718 | `RtlpMuiRegFreeRegistryInfo` | `0xCE6D0` | 32 | UnwindData |  |
| 74 | `EtwEventWriteEndScenario` | `0xCEF50` | 300 | UnwindData |  |
| 78 | `EtwEventWriteStartScenario` | `0xCF090` | 501 | UnwindData |  |
| 68 | `EtwEventEnabled` | `0xCF290` | 18 | UnwindData |  |
| 878 | `RtlCreateServiceSid` | `0xCFF60` | 318 | UnwindData |  |
| 893 | `RtlCreateVirtualAccountSid` | `0xD00B0` | 340 | UnwindData |  |
| 1624 | `RtlUpcaseUnicodeString` | `0xD0210` | 283 | UnwindData |  |
| 1623 | `RtlUpcaseUnicodeChar` | `0xD0B20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1049 | `RtlFormatMessageEx` | `0xD0B80` | 2,542 | UnwindData |  |
| 821 | `RtlCompareUnicodeString` | `0xD1650` | 361 | UnwindData |  |
| 949 | `RtlDnsHostNameToComputerName` | `0xD17C0` | 576 | UnwindData |  |
| 1346 | `RtlOemStringToUnicodeString` | `0xD1A10` | 231 | UnwindData |  |
| 1319 | `RtlMultiByteToUnicodeSize` | `0xD1B00` | 173 | UnwindData |  |
| 1347 | `RtlOemToUnicodeN` | `0xD1BC0` | 93 | UnwindData |  |
| 1627 | `RtlUpcaseUnicodeStringToOemString` | `0xD1C30` | 257 | UnwindData |  |
| 1630 | `RtlUpcaseUnicodeToOemN` | `0xD1D40` | 109 | UnwindData |  |
| 909 | `RtlDelayExecution` | `0xD1FD0` | 280 | UnwindData |  |
| 1270 | `RtlIsTextUnicode` | `0xD20F0` | 2,179 | UnwindData |  |
| 1590 | `RtlUTF8StringToUnicodeString` | `0xD2980` | 56 | UnwindData |  |
| 1154 | `RtlHashUnicodeString` | `0xD2D40` | 79 | UnwindData |  |
| 1376 | `RtlQueryFeatureUsageNotificationSubscriptions` | `0xD36A0` | 114 | UnwindData |  |
| 1364 | `RtlQueryAllFeatureConfigurations` | `0xD3720` | 165 | UnwindData |  |
| 1331 | `RtlNotifyFeatureUsage` | `0xD3810` | 125 | UnwindData |  |
| 1374 | `RtlQueryFeatureConfiguration` | `0xD3960` | 309 | UnwindData |  |
| 1782 | `TpPostWork` | `0xD44D0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `EtwTraceMessage` | `0xD4730` | 231 | UnwindData |  |
| 96 | `EtwTraceMessageVa` | `0xD4820` | 228 | UnwindData |  |
| 1672 | `RtlWow64GetCurrentMachine` | `0xD4C70` | 58 | UnwindData |  |
| 1621 | `RtlUnwind` | `0xD4CB0` | 253 | UnwindData |  |
| 1194 | `RtlInitializeExtendedContext2` | `0xD4DC0` | 429 | UnwindData |  |
| 1670 | `RtlWow64GetCpuAreaInfo` | `0xD5090` | 360 | UnwindData |  |
| 1671 | `RtlWow64GetCurrentCpuArea` | `0xD5200` | 306 | UnwindData |  |
| 1092 | `RtlGetExtendedContextLength2` | `0xD5340` | 204 | UnwindData |  |
| 1041 | `RtlFlsGetValue2` | `0xD5CD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `RtlAnsiStringToUnicodeSize` | `0xD5D20` | 152 | UnwindData |  |
| 1345 | `RtlOemStringToUnicodeSize` | `0xD5D20` | 152 | UnwindData |  |
| 1743 | `RtlxAnsiStringToUnicodeSize` | `0xD5D20` | 152 | UnwindData |  |
| 1744 | `RtlxOemStringToUnicodeSize` | `0xD5D20` | 152 | UnwindData |  |
| 1293 | `RtlLocateExtendedFeature2` | `0xD5DC0` | 317 | UnwindData |  |
| 1817 | `TpWorkOnBehalfSetTicket` | `0xD5FF0` | 127 | UnwindData |  |
| 1765 | `TpCallbackIndependent` | `0xD6460` | 405 | UnwindData |  |
| 1105 | `RtlGetInterruptTimePrecise` | `0xD6930` | 401 | UnwindData |  |
| 1040 | `RtlFlsGetValue` | `0xD6AD0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 958 | `RtlDosPathNameToRelativeNtPathName_U_WithStatus` | `0xD6B40` | 140 | UnwindData |  |
| 1136 | `RtlGetSystemGlobalData` | `0xD6C50` | 740 | UnwindData |  |
| 1572 | `RtlTimeToSecondsSince1980` | `0xD6F40` | 58 | UnwindData |  |
| 1535 | `RtlSetThreadWorkOnBehalfTicket` | `0xD7100` | 106 | UnwindData |  |
| 18 | `AlpcGetMessageFromCompletionList` | `0xD7240` | 380 | UnwindData |  |
| 953 | `RtlDosLongPathNameToNtPathName_U_WithStatus` | `0xD73D0` | 34 | UnwindData |  |
| 129 | `LdrGetDllDirectory` | `0xD75C0` | 130 | UnwindData |  |
| 855 | `RtlCopyUnicodeString` | `0xD7650` | 33 | UnwindData |  |
| 1186 | `RtlInitializeBitMapEx` | `0xD79A0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `AlpcFreeCompletionListMessage` | `0xD7BB0` | 60 | UnwindData |  |
| 962 | `RtlDowncaseUnicodeString` | `0xD7CD0` | 284 | UnwindData |  |
| 715 | `RtlAcquireResourceShared` | `0xD7E00` | 22 | UnwindData |  |
| 1646 | `RtlValidateUnicodeString` | `0xD7F80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1063 | `RtlGUIDFromString` | `0xD7FE0` | 269 | UnwindData |  |
| 1740 | `RtlpWow64CtxFromAmd64` | `0xD8AB0` | 758 | UnwindData |  |
| 842 | `RtlCopyContext` | `0xD9230` | 53 | UnwindData |  |
| 1660 | `RtlWalkHeap` | `0xD99E0` | 72 | UnwindData |  |
| 1036 | `RtlFirstFreeAce` | `0xDA060` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1029 | `RtlFindNextForwardRunClear` | `0xDA120` | 33 | UnwindData |  |
| 1356 | `RtlPrefixString` | `0xDA230` | 164 | UnwindData |  |
| 1789 | `TpReleasePool` | `0xDA2E0` | 566 | UnwindData |  |
| 1497 | `RtlSetCurrentTransaction` | `0xDA7C0` | 3,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 956 | `RtlDosPathNameToNtPathName_U_WithStatus` | `0xDB3B0` | 138 | UnwindData |  |
| 984 | `RtlEnumerateGenericTableWithoutSplaying` | `0xDB610` | 1,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1169 | `RtlInitAnsiStringEx` | `0xDBA80` | 72 | UnwindData |  |
| 1093 | `RtlGetExtendedFeaturesMask` | `0xDBAD0` | 22 | UnwindData |  |
| 1494 | `RtlSetCriticalSectionSpinCount` | `0xDBB80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `RtlAcquireResourceExclusive` | `0xDBBD0` | 22 | UnwindData |  |
| 1447 | `RtlReleaseResource` | `0xDC380` | 211 | UnwindData |  |
| 1161 | `RtlImageNtHeader` | `0xDC460` | 44 | UnwindData |  |
| 1209 | `RtlInsertEntryHashTable` | `0xDC4C0` | 311 | UnwindData |  |
| 1172 | `RtlInitEnumerationHashTable` | `0xDC600` | 109 | UnwindData |  |
| 1089 | `RtlGetEnabledExtendedFeatures` | `0xDC840` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `RtlInstallFunctionTableCallback` | `0xDC870` | 793 | UnwindData |  |
| 1708 | `RtlpGetNameFromLangInfoNode` | `0xDCB90` | 252 | UnwindData |  |
| 1379 | `RtlQueryInformationAcl` | `0xDCD80` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1669 | `RtlWow64GetCpuAreaEnabledFeatures` | `0xDCE30` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1344 | `RtlNumberOfSetBitsUlongPtr` | `0xDCFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1138 | `RtlGetSystemTimeAndBias` | `0xDCFE0` | 332 | UnwindData |  |
| 1143 | `RtlGetThreadWorkOnBehalfTicket` | `0xDD140` | 188 | UnwindData |  |
| 948 | `RtlDllShutdownInProgress` | `0xDD290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1213 | `RtlIntegerToUnicodeString` | `0xDD2B0` | 140 | UnwindData |  |
| 1212 | `RtlIntegerToChar` | `0xDD350` | 323 | UnwindData |  |
| 1099 | `RtlGetFullPathName_UEx` | `0xDDD50` | 175 | UnwindData |  |
| 991 | `RtlEqualString` | `0xDDE10` | 25 | UnwindData |  |
| 23 | `AlpcRegisterCompletionListWorkerThread` | `0xDDFE0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `RtlEnumerateEntryHashTable` | `0xDE140` | 276 | UnwindData |  |
| 26 | `AlpcUnregisterCompletionListWorkerThread` | `0xDE260` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `RtlDosPathNameToRelativeNtPathName_U` | `0xDE2C0` | 142 | UnwindData |  |
| 973 | `RtlEncodeSystemPointer` | `0xDE360` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1309 | `RtlLookupEntryHashTable` | `0xDE3F0` | 214 | UnwindData |  |
| 1820 | `WerReportSQMEvent` | `0xDE5B0` | 73 | UnwindData |  |
| 1749 | `ShipAssert` | `0xDE600` | 494 | UnwindData |  |
| 807 | `RtlClearThreadWorkOnBehalfTicket` | `0xDF760` | 98 | UnwindData |  |
| 1168 | `RtlInitAnsiString` | `0xDF840` | 65 | UnwindData |  |
| 1176 | `RtlInitString` | `0xDF840` | 65 | UnwindData |  |
| 1245 | `RtlIsCriticalSectionLockedByThread` | `0xDF890` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `RtlLengthRequiredSid` | `0xDFAF0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `RtlInitializeSid` | `0xDFC30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1314 | `RtlMapGenericMask` | `0xDFC60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1369 | `RtlQueryDepthSList` | `0xDFCA0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1389 | `RtlQueryPerformanceFrequency` | `0xDFE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 820 | `RtlCompareString` | `0xDFE70` | 203 | UnwindData |  |
| 751 | `RtlAllocateAndInitializeSid` | `0xDFFA0` | 65 | UnwindData |  |
| 1164 | `RtlImageRvaToVa` | `0xE00D0` | 124 | UnwindData |  |
| 1163 | `RtlImageRvaToSection` | `0xE0160` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `RtlIsDosDeviceName_U` | `0xE01B0` | 73 | UnwindData |  |
| 1362 | `RtlPushFrame` | `0xE0200` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `RtlFindLongestRunClear` | `0xE0230` | 57 | UnwindData |  |
| 1021 | `RtlFindClearRuns` | `0xE0270` | 733 | UnwindData |  |
| 20 | `AlpcInitializeMessageAttribute` | `0xE0560` | 88 | UnwindData |  |
| 17 | `AlpcGetMessageAttribute` | `0xE05C0` | 51 | UnwindData |  |
| 16 | `AlpcGetHeaderSize` | `0xE0600` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1254 | `RtlIsGenericTableEmpty` | `0xE0660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1498 | `RtlSetDaclSecurityDescriptor` | `0xE0670` | 3,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `EtwLogTraceEvent` | `0xE1390` | 93 | UnwindData |  |
| 869 | `RtlCreateMemoryBlockLookaside` | `0xE1760` | 516 | UnwindData |  |
| 1201 | `RtlInitializeSListHead` | `0xE1970` | 32 | UnwindData |  |
| 870 | `RtlCreateMemoryZone` | `0xE19A0` | 154 | UnwindData |  |
| 1348 | `RtlOpenCrossProcessEmulatorWorkConnection` | `0xE1A40` | 361 | UnwindData |  |
| 1246 | `RtlIsCurrentProcess` | `0xE1BB0` | 44 | UnwindData |  |
| 1556 | `RtlStronglyEnumerateEntryHashTable` | `0xE1BF0` | 90 | UnwindData |  |
| 832 | `RtlContractHashTable` | `0xE1C50` | 334 | UnwindData |  |
| 1004 | `RtlExpandHashTable` | `0xE1DB0` | 492 | UnwindData |  |
| 921 | `RtlDeleteHashTable` | `0xE2190` | 165 | UnwindData |  |
| 1807 | `TpStartAsyncIoOperation` | `0xE2260` | 79 | UnwindData |  |
| 1355 | `RtlPopFrame` | `0xE2330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `RtlCreateProcessParametersEx` | `0xE2350` | 106 | UnwindData |  |
| 873 | `RtlCreateProcessParametersWithTemplate` | `0xE23C0` | 295 | UnwindData |  |
| 1287 | `RtlLengthSid` | `0xE2BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1083 | `RtlGetCurrentTransaction` | `0xE2BC0` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `EtwpCreateEtwThread` | `0xE2EB0` | 118 | UnwindData |  |
| 892 | `RtlCreateUserThread` | `0xE2F30` | 104 | UnwindData |  |
| 1085 | `RtlGetDaclSecurityDescriptor` | `0xE3150` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `RtlDosPathNameToNtPathName_U` | `0xE3400` | 140 | UnwindData |  |
| 127 | `LdrFindResource_U` | `0xE3510` | 333 | UnwindData |  |
| 1715 | `RtlpMergeSecurityAttributeInformation` | `0xE3670` | 1,061 | UnwindData |  |
| 886 | `RtlCreateUnicodeStringFromAsciiz` | `0xE3E30` | 94 | UnwindData |  |
| 1274 | `RtlIsValidIndexHandle` | `0xE3EA0` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `EtwEventProviderEnabled` | `0xE4650` | 204 | UnwindData |  |
| 1294 | `RtlLocateLegacyContext` | `0xE4730` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `RtlCreateSecurityDescriptor` | `0xE48B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1117 | `RtlGetNtGlobalFlags` | `0xE48E0` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1571 | `RtlTimeToSecondsSince1970` | `0xE4F60` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `RtlAcquirePrivilege` | `0xE52C0` | 827 | UnwindData |  |
| 1166 | `RtlImpersonateSelfEx` | `0xE5610` | 113 | UnwindData |  |
| 79 | `EtwEventWriteString` | `0xE57B0` | 145 | UnwindData |  |
| 1229 | `RtlIpv4StringToAddressExA` | `0xE5AB0` | 455 | UnwindData |  |
| 1228 | `RtlIpv4StringToAddressA` | `0xE5C80` | 702 | UnwindData |  |
| 1818 | `VerSetConditionMask` | `0xE5F50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `RtlEnumerateGenericTableWithoutSplayingAvl` | `0xE5F90` | 105 | UnwindData |  |
| 1286 | `RtlLengthSecurityDescriptor` | `0xE6220` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `RtlInitializeConditionVariable` | `0xE6350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1202 | `RtlInitializeSRWLock` | `0xE6350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1479 | `RtlRunOnceInitialize` | `0xE6350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `EtwRegisterTraceGuidsA` | `0xE6360` | 49 | UnwindData |  |
| 90 | `EtwRegisterTraceGuidsW` | `0xE63A0` | 103 | UnwindData |  |
| 1214 | `RtlInterlockedClearBitRun` | `0xE6850` | 177 | UnwindData |  |
| 1057 | `RtlFreeSid` | `0xE6910` | 50 | UnwindData |  |
| 775 | `RtlAreLongPathsEnabled` | `0xE6980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1269 | `RtlIsStateSeparationEnabled` | `0xE69A0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1126 | `RtlGetProductInfo` | `0xE6A80` | 442 | UnwindData |  |
| 1608 | `RtlUniform` | `0xE6DA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1816 | `TpWorkOnBehalfClearTicket` | `0xE6DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1128 | `RtlGetSaclSecurityDescriptor` | `0xE6E10` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1691 | `RtlXRestore` | `0xE6E80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `RtlCopyLuid` | `0xE6ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `RtlDecodeSystemPointer` | `0xE6EE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `RtlTimeToElapsedTimeFields` | `0xE6F10` | 247 | UnwindData |  |
| 1558 | `RtlSubAuthoritySid` | `0xE7020` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1451 | `RtlRemoveEntryHashTable` | `0xE7130` | 93 | UnwindData |  |
| 1640 | `RtlValidRelativeSecurityDescriptor` | `0xE8980` | 347 | UnwindData |  |
| 1483 | `RtlSelfRelativeToAbsoluteSD` | `0xE8BC0` | 595 | UnwindData |  |
| 1107 | `RtlGetLastWin32Error` | `0xE8F80` | 1,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 965 | `RtlDuplicateUnicodeString` | `0xE9660` | 428 | UnwindData |  |
| 1121 | `RtlGetOwnerSecurityDescriptor` | `0xE9820` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1528 | `RtlSetThreadErrorMode` | `0xE9920` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `RtlFindExportedRoutineByName` | `0xE9990` | 232 | UnwindData |  |
| 1434 | `RtlRealPredecessor` | `0xE9A80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1530 | `RtlSetThreadPlaceholderCompatibilityMode` | `0xE9AD0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1775 | `TpCaptureCaller` | `0xE9B70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1443 | `RtlReleasePath` | `0xE9BD0` | 105 | UnwindData |  |
| 1013 | `RtlFindAceByType` | `0xE9CB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `LdrGetDllHandleByName` | `0xE9D00` | 162 | UnwindData |  |
| 1793 | `TpSetDefaultPoolMaxThreads` | `0xE9DB0` | 323 | UnwindData |  |
| 1794 | `TpSetDefaultPoolStackInformation` | `0xE9F00` | 273 | UnwindData |  |
| 1798 | `TpSetPoolStackInformation` | `0xEA070` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1218 | `RtlInterlockedPushEntrySList` | `0xEA0C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `LdrUpdatePackageSearchPath` | `0xEA0D0` | 245 | UnwindData |  |
| 120 | `LdrDisableThreadCalloutsForDll` | `0xEA240` | 82 | UnwindData |  |
| 1216 | `RtlInterlockedFlushSList` | `0xEA2A0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1557 | `RtlSubAuthorityCountSid` | `0xEA330` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `EtwSendNotification` | `0xEA6B0` | 655 | UnwindData |  |
| 1573 | `RtlTimeToTimeFields` | `0xEAE10` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `RtlAreBitsClearEx` | `0xEB080` | 205 | UnwindData |  |
| 1075 | `RtlGetControlSecurityDescriptor` | `0xEB160` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `LdrGetDllHandleByMapping` | `0xEB190` | 247 | UnwindData |  |
| 1102 | `RtlGetGroupSecurityDescriptor` | `0xEB290` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1052 | `RtlFreeHandle` | `0xEB2D0` | 55 | UnwindData |  |
| 28 | `ApiSetQueryApiSetPresence` | `0xEB440` | 193 | UnwindData |  |
| 770 | `RtlAreAllAccessesGranted` | `0xEB510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1237 | `RtlIpv6StringToAddressExA` | `0xEB520` | 637 | UnwindData |  |
| 1236 | `RtlIpv6StringToAddressA` | `0xEB7B0` | 1,273 | UnwindData |  |
| 1655 | `RtlWakeAddressSingle` | `0xEC090` | 23 | UnwindData |  |
| 1224 | `RtlIpv4AddressToStringA` | `0xEC0B0` | 73 | UnwindData |  |
| 75 | `EtwEventWriteEx` | `0xEC100` | 73 | UnwindData |  |
| 1114 | `RtlGetNextEntryHashTable` | `0xEC2B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `RtlCheckTokenMembership` | `0xEC300` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1248 | `RtlIsCurrentThreadAttachExempt` | `0xEC4F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1404 | `RtlQueryThreadPlaceholderCompatibilityMode` | `0xEC530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1439 | `RtlRegisterThreadWithCsrss` | `0xEC550` | 179 | UnwindData |  |
| 1233 | `RtlIpv6AddressToStringExA` | `0xEC610` | 275 | UnwindData |  |
| 1232 | `RtlIpv6AddressToStringA` | `0xEC730` | 688 | UnwindData |  |
| 801 | `RtlClearAllBits` | `0xECB10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `RtlCreateBoundaryDescriptor` | `0xECB40` | 203 | UnwindData |  |
| 1565 | `RtlTestAndPublishWnfStateData` | `0xECC20` | 171 | UnwindData |  |
| 1361 | `RtlPublishWnfStateData` | `0xECCE0` | 162 | UnwindData |  |
| 29 | `ApiSetQueryApiSetPresenceEx` | `0xECE30` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `LdrLoadAlternateResourceModule` | `0xED010` | 1,044 | UnwindData |  |
| 1257 | `RtlIsMultiUsersInSessionSku` | `0xED4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `EtwGetTraceLoggerHandle` | `0xED4C0` | 91 | UnwindData |  |
| 82 | `EtwGetTraceEnableLevel` | `0xED530` | 65 | UnwindData |  |
| 81 | `EtwGetTraceEnableFlags` | `0xED580` | 65 | UnwindData |  |
| 749 | `RtlAdjustPrivilege` | `0xED630` | 269 | UnwindData |  |
| 925 | `RtlDeleteSecurityObject` | `0xED750` | 35 | UnwindData |  |
| 736 | `RtlAddFunctionTable` | `0xED8A0` | 768 | UnwindData |  |
| 1359 | `RtlProcessFlsData` | `0xEDBB0` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `RtlAssert` | `0xEDE80` | 287 | UnwindData |  |
| 1033 | `RtlFindSetBitsEx` | `0xEDFD0` | 917 | UnwindData |  |
| 1804 | `TpSetWait` | `0xEE370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `RtlSetSearchPathMode` | `0xEE380` | 254 | UnwindData |  |
| 1156 | `RtlIdentifierAuthoritySid` | `0xEE490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `AlpcGetOutstandingCompletionListMessageCount` | `0xEE4A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `RtlNumberOfClearBits` | `0xEE4C0` | 27 | UnwindData |  |
| 1341 | `RtlNumberOfSetBits` | `0xEE4F0` | 348 | UnwindData |  |
| 97 | `EtwUnregisterTraceGuids` | `0xEE660` | 71 | UnwindData |  |
| 792 | `RtlCheckForOrphanedCriticalSections` | `0xEE710` | 29 | UnwindData |  |
| 1725 | `RtlpNtQueryValueKey` | `0xEEBA0` | 269 | UnwindData |  |
| 1265 | `RtlIsPartialPlaceholder` | `0xEF0D0` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `EvtIntReportEventAndSourceAsync` | `0xEF3A0` | 103 | UnwindData |  |
| 98 | `EtwWriteUMSecurityEvent` | `0xEF860` | 209 | UnwindData |  |
| 1486 | `RtlSetAllBits` | `0xEF940` | 95 | UnwindData |  |
| 1569 | `RtlTimeFieldsToTime` | `0xEF9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `RtlIpv4AddressToStringExA` | `0xEF9C0` | 254 | UnwindData |  |
| 1087 | `RtlGetElementGenericTable` | `0xEFAD0` | 154 | UnwindData |  |
| 713 | `RtlAcquireReleaseSRWLockExclusive` | `0xEFCD0` | 46 | UnwindData |  |
| 1185 | `RtlInitializeBitMap` | `0xF01C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1397 | `RtlQueryProtectedPolicy` | `0xF01D0` | 137 | UnwindData |  |
| 851 | `RtlCopySecurityDescriptor` | `0xF07B0` | 376 | UnwindData |  |
| 891 | `RtlCreateUserStack` | `0xF0990` | 720 | UnwindData |  |
| 1243 | `RtlIsCloudFilesPlaceholder` | `0xF0C70` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1722 | `RtlpNtEnumerateSubKey` | `0xF0DE0` | 262 | UnwindData |  |
| 1381 | `RtlQueryInformationActiveActivationContext` | `0xF0EF0` | 41 | UnwindData |  |
| 982 | `RtlEnumerateGenericTableAvl` | `0xF0F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1068 | `RtlGetActiveConsoleId` | `0xF0F70` | 47 | UnwindData |  |
| 1809 | `TpTrimPools` | `0xF0FB0` | 1,017 | UnwindData |  |
| 1310 | `RtlLookupFirstMatchingElementGenericTableAvl` | `0xF13B0` | 146 | UnwindData |  |
| 774 | `RtlAreBitsSet` | `0xF1450` | 211 | UnwindData |  |
| 1678 | `RtlWow64IsWowGuestMachineSupported` | `0xF1580` | 282 | UnwindData |  |
| 1195 | `RtlInitializeGenericTable` | `0xF1740` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1696 | `RtlpApplyLengthFunction` | `0xF1780` | 144 | UnwindData |  |
| 1005 | `RtlExtendCorrelationVector` | `0xF1820` | 62 | UnwindData |  |
| 1167 | `RtlIncrementCorrelationVector` | `0xF1870` | 223 | UnwindData |  |
| 1643 | `RtlValidateCorrelationVector` | `0xF1960` | 230 | UnwindData |  |
| 1024 | `RtlFindLastBackwardRunClear` | `0xF1B80` | 224 | UnwindData |  |
| 1165 | `RtlImpersonateSelf` | `0xF1C70` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1066 | `RtlGetAcesBufferSize` | `0xF1E00` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1802 | `TpSetTimer` | `0xF1EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1651 | `RtlWaitForWnfMetaNotification` | `0xF1ED0` | 540 | UnwindData |  |
| 875 | `RtlCreateQueryDebugBuffer` | `0xF2100` | 671 | UnwindData |  |
| 911 | `RtlDeleteAce` | `0xF26B0` | 144 | UnwindData |  |
| 1675 | `RtlWow64GetSharedInfoProcess` | `0xF2960` | 122 | UnwindData |  |
| 1302 | `RtlLogStackBackTrace` | `0xF2BD0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1780 | `TpDisassociateCallback` | `0xF2CF0` | 133 | UnwindData |  |
| 100 | `EtwpGetCpuSpeed` | `0xF2E50` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `LdrUnlockLoaderLock` | `0xF2F70` | 173 | UnwindData |  |
| 1215 | `RtlInterlockedClearBitRunEx` | `0xF3160` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1585 | `RtlTryAcquirePebLock` | `0xF3220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1445 | `RtlReleasePrivilege` | `0xF3240` | 184 | UnwindData |  |
| 1616 | `RtlUnregisterFeatureConfigurationChangeNotification` | `0xF3300` | 41 | UnwindData |  |
| 961 | `RtlDowncaseUnicodeChar` | `0xF33D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `EtwEventUnregister` | `0xF3460` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `RtlExtendMemoryZone` | `0xF3720` | 253 | UnwindData |  |
| 947 | `RtlDisownModuleHeapAllocation` | `0xF3830` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 974 | `RtlEndEnumerationHashTable` | `0xF3AB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1546 | `RtlSidHashLookup` | `0xF3B00` | 294 | UnwindData |  |
| 1196 | `RtlInitializeGenericTableAvl` | `0xF3D50` | 89 | UnwindData |  |
| 1106 | `RtlGetLastNtStatus` | `0xF4110` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `LdrFindResourceEx_U` | `0xF4180` | 295 | UnwindData |  |
| 1148 | `RtlGetUnloadEventTraceEx` | `0xF42B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 856 | `RtlCrc32` | `0xF42E0` | 81 | UnwindData |  |
| 750 | `RtlAllocateActivationContextStack` | `0xF4BD0` | 118 | UnwindData |  |
| 1271 | `RtlIsThreadWithinLoaderCallout` | `0xF4C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1724 | `RtlpNtOpenKey` | `0xF4C70` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1554 | `RtlStringFromGUID` | `0xF4CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1811 | `TpWaitForIoCompletion` | `0xF4D00` | 252 | UnwindData |  |
| 1152 | `RtlGrowFunctionTable` | `0xF4E10` | 236 | UnwindData |  |
| 1647 | `RtlValidateUserCallTarget` | `0xF4F10` | 149 | UnwindData |  |
| 824 | `RtlCompressBuffer` | `0xF4FF0` | 131 | UnwindData |  |
| 772 | `RtlAreBitsClear` | `0xF5080` | 203 | UnwindData |  |
| 1711 | `RtlpInitializeLangRegistryInfo` | `0xF5160` | 38 | UnwindData |  |
| 1545 | `RtlSidHashInitialize` | `0xF5300` | 177 | UnwindData |  |
| 1375 | `RtlQueryFeatureConfigurationChangeStamp` | `0xF53C0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1086 | `RtlGetDeviceFamilyInfoEnum` | `0xF5670` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `RtlGetCurrentPeb` | `0xF5740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `RtlCopyMappedMemory` | `0xF5760` | 24 | UnwindData |  |
| 906 | `RtlDecompressBufferEx` | `0xF57D0` | 126 | UnwindData |  |
| 1337 | `RtlNumberGenericTableElementsAvl` | `0xF5860` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `LdrAccessResource` | `0xF58E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `RtlSetProtectedPolicy` | `0xF58F0` | 741 | UnwindData |  |
| 1296 | `RtlLockCurrentThread` | `0xF5BE0` | 264 | UnwindData |  |
| 1263 | `RtlIsPackageSid` | `0xF5D70` | 66 | UnwindData |  |
| 1110 | `RtlGetLocaleFileMappingAddress` | `0xF5DC0` | 139 | UnwindData |  |
| 1280 | `RtlLargeIntegerToChar` | `0xF6250` | 351 | UnwindData |  |
| 1489 | `RtlSetBit` | `0xF6560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1673 | `RtlWow64GetEquivalentMachineCHPE` | `0xF6580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1336 | `RtlNumberGenericTableElements` | `0xF65A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `LdrStandardizeSystemPath` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 901 | `RtlDebugPrintTimes` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `RtlEndStrongEnumerationHashTable` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1012 | `RtlFinalReleaseOutOfProcessMemoryStream` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `RtlInitMemoryStream` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `RtlInitNlsTables` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `RtlInitOutOfProcessMemoryStream` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1466 | `RtlResetRtlTranslations` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `RtlpWaitForCriticalSection` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1778 | `TpDbgSetLogRoutine` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1821 | `WinSqmAddToAverageDWORD` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1822 | `WinSqmAddToStream` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1823 | `WinSqmAddToStreamEx` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1833 | `WinSqmEndSession` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1838 | `WinSqmIncrementDWORD` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1842 | `WinSqmSetDWORD` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1843 | `WinSqmSetDWORD64` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1845 | `WinSqmSetIfMaxDWORD` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1846 | `WinSqmSetIfMinDWORD` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1847 | `WinSqmSetString` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2345 | `__misaligned_access` | `0xF65B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1495 | `RtlSetCurrentDirectory_U` | `0xF65C0` | 552 | UnwindData |  |
| 928 | `RtlDeleteTimerQueueEx` | `0xF69A0` | 385 | UnwindData |  |
| 183 | `LdrUnloadAlternateResourceModule` | `0xF6F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1371 | `RtlQueryElevationFlags` | `0xF6F50` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1567 | `RtlTestBitEx` | `0xF72C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `RtlDestroyProcessParameters` | `0xF72E0` | 35 | UnwindData |  |
| 1511 | `RtlSetLastWin32ErrorAndNtStatusFromNtStatus` | `0xF7310` | 20 | UnwindData |  |
| 889 | `RtlCreateUserProcessEx` | `0xF7330` | 176 | UnwindData |  |
| 1327 | `RtlNormalizeProcessParams` | `0xF73F0` | 44,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `RtlInitializeRXact` | `0x101FD0` | 1,090 | UnwindData |  |
| 767 | `RtlApplyRXact` | `0x102420` | 204 | UnwindData |  |
| 768 | `RtlApplyRXactNoFlush` | `0x102500` | 33 | UnwindData |  |
| 709 | `RtlAbortRXact` | `0x1026F0` | 63 | UnwindData |  |
| 1111 | `RtlGetLongestNtPathLength` | `0x102740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1564 | `RtlSystemTimeToLocalTime` | `0x102750` | 112 | UnwindData |  |
| 803 | `RtlClearBit` | `0x1027D0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1713 | `RtlpLoadMachineUIByPolicy` | `0x102930` | 385 | UnwindData |  |
| 882 | `RtlCreateTimerQueue` | `0x102AC0` | 180 | UnwindData |  |
| 838 | `RtlConvertSharedToExclusive` | `0x102B80` | 77 | UnwindData |  |
| 1411 | `RtlQueryWnfMetaNotification` | `0x102BE0` | 70 | UnwindData |  |
| 1707 | `RtlpGetLCIDFromLangInfoNode` | `0x102CA0` | 147 | UnwindData |  |
| 1797 | `TpSetPoolMinThreads` | `0x102D40` | 157 | UnwindData |  |
| 1197 | `RtlInitializeHandleTable` | `0x102DF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | `RtlCreateUserFiberShadowStack` | `0x102E30` | 223 | UnwindData |  |
| 1073 | `RtlGetCompressionWorkSpaceSize` | `0x103050` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1606 | `RtlUnicodeToOemN` | `0x1030A0` | 70 | UnwindData |  |
| 1062 | `RtlFreeUserStack` | `0x1048F0` | 45 | UnwindData |  |
| 152 | `LdrOpenImageFileOptionsKey` | `0x105680` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `RtlCreateEnvironment` | `0x105870` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1694 | `RtlZeroMemory` | `0x1059C0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `RtlQueryTokenHostIdAsUlong64` | `0x105A50` | 173 | UnwindData |  |
| 1566 | `RtlTestBit` | `0x105C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `LdrGetKnownDllSectionHandle` | `0x105CB0` | 381 | UnwindData |  |
| 950 | `RtlDoesFileExists_U` | `0x105E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 757 | `RtlAllocateWnfSerializationGroup` | `0x105E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1433 | `RtlReadThreadProfilingData` | `0x105E70` | 359 | UnwindData |  |
| 1251 | `RtlIsElevatedRid` | `0x1061F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `AlpcMaxAllowedMessageLength` | `0x106270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1552 | `RtlStartRXact` | `0x106280` | 91 | UnwindData |  |
| 1612 | `RtlUnlockMemoryBlockLookaside` | `0x106680` | 87 | UnwindData |  |
| 1614 | `RtlUnlockMemoryZone` | `0x1066E0` | 148 | UnwindData |  |
| 162 | `LdrRegisterDllNotification` | `0x1067C0` | 195 | UnwindData |  |
| 1108 | `RtlGetLengthWithoutLastFullDosOrNtPathElement` | `0x106A50` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `RtlNewSecurityObjectWithMultipleInheritance` | `0x106AF0` | 80 | UnwindData |  |
| 729 | `RtlAddActionToRXact` | `0x106B50` | 67 | UnwindData |  |
| 731 | `RtlAddAttributeActionToRXact` | `0x106BA0` | 491 | UnwindData |  |
| 1539 | `RtlSetUnhandledExceptionFilter` | `0x106E00` | 22 | UnwindData |  |
| 951 | `RtlDoesNameContainWildCards` | `0x106ED0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `RtlFlsFree` | `0x106F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1247 | `RtlIsCurrentThread` | `0x106F40` | 40 | UnwindData |  |
| 747 | `RtlAddVectoredExceptionHandler` | `0x106F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1568 | `RtlTestProtectedAccess` | `0x106F80` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 744 | `RtlAddSIDToBoundaryDescriptor` | `0x107150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `LdrResRelease` | `0x107160` | 630 | UnwindData |  |
| 827 | `RtlComputePrivatizedDllName_U` | `0x107550` | 956 | UnwindData |  |
| 41 | `CsrIdentifyAlertableThread` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `LdrSetAppCompatDllRedirectionCallback` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `RtlAddRefMemoryStream` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1184 | `RtlInitializeAtomPackage` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1442 | `RtlReleaseMemoryStream` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1462 | `RtlReportSqmEscalation` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `RtlSetThreadPoolStartFunc` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1824 | `WinSqmCheckEscalationAddToStreamEx` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1825 | `WinSqmCheckEscalationSetDWORD` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1826 | `WinSqmCheckEscalationSetDWORD64` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1827 | `WinSqmCheckEscalationSetString` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1834 | `WinSqmEventEnabled` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1835 | `WinSqmEventWrite` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1836 | `WinSqmGetEscalationRuleStatus` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1839 | `WinSqmIsOptedIn` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1840 | `WinSqmIsOptedInEx` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1850 | `WinSqmStartSqmOptinListener` | `0x107A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `RtlCompactHeap` | `0x107A80` | 311 | UnwindData |  |
| 1261 | `RtlIsNonEmptyDirectoryReparsePointAllowed` | `0x107DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `AlpcRegisterCompletionList` | `0x107E10` | 76 | UnwindData |  |
| 740 | `RtlAddProcessTrustLabelAce` | `0x108170` | 366 | UnwindData |  |
| 1631 | `RtlUpdateClonedCriticalSection` | `0x1082F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1144 | `RtlGetTokenNamedObjectPath` | `0x108320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1130 | `RtlGetSecurityDescriptorRMControl` | `0x108340` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `LdrAddDllDirectory` | `0x108370` | 612 | UnwindData |  |
| 1456 | `RtlRemoveVectoredExceptionHandler` | `0x1085E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `LdrSetDllManifestProber` | `0x1085F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1772 | `TpCallbackSetEventOnCompletion` | `0x108610` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1799 | `TpSetPoolThreadBasePriority` | `0x108650` | 78 | UnwindData |  |
| 1255 | `RtlIsGenericTableEmptyAvl` | `0x1087C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `RtlFindLeastSignificantBit` | `0x108800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1179 | `RtlInitUTF8String` | `0x108820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `LdrSetDefaultDllDirectories` | `0x108830` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 854 | `RtlCopyString` | `0x108870` | 52 | UnwindData |  |
| 1082 | `RtlGetCurrentThreadPrimaryGroup` | `0x1088B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `RtlFreeUserFiberShadowStack` | `0x1088D0` | 39 | UnwindData |  |
| 725 | `RtlAddAccessDeniedAceEx` | `0x108900` | 30 | UnwindData |  |
| 1220 | `RtlInterlockedPushListSListEx` | `0x108930` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1437 | `RtlRegisterForWnfMetaNotification` | `0x108C00` | 77 | UnwindData |  |
| 1278 | `RtlKnownExceptionFilter` | `0x108C60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `LdrProcessInitializationComplete` | `0x108CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `RtlCreateHashTable` | `0x108CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1125 | `RtlGetProcessPreferredUILanguages` | `0x108D10` | 242 | UnwindData |  |
| 730 | `RtlAddAtomToAtomTable` | `0x108EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `RtlComputeCrc32` | `0x108F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1342 | `RtlNumberOfSetBitsEx` | `0x108F10` | 353 | UnwindData |  |
| 2348 | `_errno` | `0x109080` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1520 | `RtlSetProxiedProcessId` | `0x1091A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1523 | `RtlSetSecurityDescriptorRMControl` | `0x1091D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 795 | `RtlCheckSandboxedToken` | `0x109250` | 89 | UnwindData |  |
| 940 | `RtlDestroyMemoryBlockLookaside` | `0x1092B0` | 84 | UnwindData |  |
| 941 | `RtlDestroyMemoryZone` | `0x109310` | 93 | UnwindData |  |
| 199 | `MicrosoftTelemetryAssertTriggeredUM` | `0x109380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1402 | `RtlQuerySecurityObject` | `0x1093A0` | 813 | UnwindData |  |
| 933 | `RtlDeregisterWait` | `0x109960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `LdrFlushAlternateResourceModules` | `0x109970` | 255 | UnwindData |  |
| 1028 | `RtlFindMostSignificantBit` | `0x109A80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1324 | `RtlNewSecurityObject` | `0x109AB0` | 64 | UnwindData |  |
| 1610 | `RtlUnlockCurrentThread` | `0x109B00` | 168 | UnwindData |  |
| 733 | `RtlAddAuditAccessAceEx` | `0x109C90` | 62 | UnwindData |  |
| 1779 | `TpDisablePoolCallbackChecks` | `0x10A0A0` | 64 | UnwindData |  |
| 1453 | `RtlRemovePrivileges` | `0x10A0F0` | 254 | UnwindData |  |
| 123 | `LdrFastFailInLoaderCallout` | `0x10A200` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `DbgUiWaitStateChange` | `0x10A2C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 835 | `RtlConvertHostPerfCounterToPerfCounter` | `0x10A330` | 157 | UnwindData |  |
| 1406 | `RtlQueryTimeZoneInformation` | `0x10A3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1664 | `RtlWow64CallFunction64` | `0x10A3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1667 | `RtlWow64EnableFsRedirection` | `0x10A3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `RtlWow64EnableFsRedirectionEx` | `0x10A3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1741 | `RtlpWow64GetContextOnAmd64` | `0x10A3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1742 | `RtlpWow64SetContextOnAmd64` | `0x10A3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1490 | `RtlSetBitEx` | `0x10A400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1120 | `RtlGetNtVersionNumbers` | `0x10A410` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `EtwReplyNotification` | `0x10A460` | 68 | UnwindData |  |
| 834 | `RtlConvertExclusiveToShared` | `0x10B510` | 71 | UnwindData |  |
| 1485 | `RtlSendMsgToSm` | `0x10B560` | 172 | UnwindData |  |
| 116 | `LdrCallEnclave` | `0x10B620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1109 | `RtlGetLengthWithoutTrailingPathSeperators` | `0x10B630` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `AlpcAdjustCompletionListConcurrencyCount` | `0x10B690` | 34 | UnwindData |  |
| 1401 | `RtlQueryResourcePolicy` | `0x10B770` | 179 | UnwindData |  |
| 1189 | `RtlInitializeCorrelationVector` | `0x10B830` | 122 | UnwindData |  |
| 1097 | `RtlGetFrame` | `0x10B990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1687 | `RtlWow64SuspendThread` | `0x10B9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `RtlSetThreadIsCritical` | `0x10B9C0` | 159 | UnwindData |  |
| 1046 | `RtlFlushSecureMemoryCache` | `0x10BA70` | 121 | UnwindData |  |
| 1475 | `RtlRunEncodeUnicodeString` | `0x10BAF0` | 169 | UnwindData |  |
| 137 | `LdrGetFileNameFromLoadAsDataTable` | `0x10BC00` | 83 | UnwindData |  |
| 1459 | `RtlReportException` | `0x10BC60` | 155 | UnwindData |  |
| 1480 | `RtlSecondsSince1970ToTime` | `0x10BDA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 996 | `RtlEthernetAddressToStringW` | `0x10BDD0` | 102 | UnwindData |  |
| 52 | `DbgUiContinue` | `0x10BF40` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `EtwCheckCoverage` | `0x10C040` | 69 | UnwindData |  |
| 1828 | `WinSqmCommonDatapointDelete` | `0x10C100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1829 | `WinSqmCommonDatapointSetDWORD` | `0x10C100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1830 | `WinSqmCommonDatapointSetDWORD64` | `0x10C100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1831 | `WinSqmCommonDatapointSetStreamEx` | `0x10C100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1832 | `WinSqmCommonDatapointSetString` | `0x10C100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1841 | `WinSqmIsSessionDisabled` | `0x10C100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1844 | `WinSqmSetEscalationInfo` | `0x10C100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 993 | `RtlEqualWnfChangeStamps` | `0x10C110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1766 | `TpCallbackLeaveCriticalSectionOnCompletion` | `0x10C120` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `LdrVerifyImageMatchesChecksumEx` | `0x10C150` | 968 | UnwindData |  |
| 163 | `LdrRemoveDllDirectory` | `0x10C520` | 239 | UnwindData |  |
| 938 | `RtlDestroyHandleTable` | `0x10C620` | 104 | UnwindData |  |
| 1030 | `RtlFindSetBits` | `0x10C690` | 934 | UnwindData |  |
| 861 | `RtlCreateAtomTable` | `0x10CA40` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1008 | `RtlExtractBitMap` | `0x10CB20` | 412 | UnwindData |  |
| 187 | `LdrUnregisterDllNotification` | `0x10CEC0` | 155 | UnwindData |  |
| 1504 | `RtlSetFeatureConfigurations` | `0x10D110` | 248 | UnwindData |  |
| 1043 | `RtlFlushHeaps` | `0x10D210` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `LdrCreateEnclave` | `0x10D500` | 254 | UnwindData |  |
| 1619 | `RtlUnsubscribeWnfNotificationWithCompletionCallback` | `0x10D7A0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1141 | `RtlGetThreadLangIdByIndex` | `0x10D8A0` | 230 | UnwindData |  |
| 1474 | `RtlRunDecodeUnicodeString` | `0x10DED0` | 87 | UnwindData |  |
| 161 | `LdrQueryProcessModuleInformation` | `0x10DFC0` | 33 | UnwindData |  |
| 1666 | `RtlWow64ChangeThreadState` | `0x10DFF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `PssNtFreeRemoteSnapshot` | `0x10E020` | 548 | UnwindData |  |
| 828 | `RtlConnectToSm` | `0x10E250` | 465 | UnwindData |  |
| 1496 | `RtlSetCurrentEnvironment` | `0x10E440` | 162 | UnwindData |  |
| 53 | `DbgUiConvertStateChangeStructure` | `0x10E4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1124 | `RtlGetProcessHeaps` | `0x10E500` | 121 | UnwindData |  |
| 1632 | `RtlUpdateClonedSRWLock` | `0x10E710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `AlpcRundownCompletionList` | `0x10E730` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1500 | `RtlSetEnvironmentStrings` | `0x10E7B0` | 296 | UnwindData |  |
| 786 | `RtlCapabilityCheckForSingleSessionSku` | `0x10EA70` | 96 | UnwindData |  |
| 1009 | `RtlFillMemory` | `0x10EB40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1266 | `RtlIsPartialPlaceholderFileHandle` | `0x10EB80` | 87 | UnwindData |  |
| 1663 | `RtlWnfDllUnloadCallback` | `0x10EC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 966 | `RtlEmptyAtomTable` | `0x10EC70` | 163 | UnwindData |  |
| 25 | `AlpcUnregisterCompletionList` | `0x10ED40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `PssNtFreeWalkMarker` | `0x10ED60` | 42 | UnwindData |  |
| 1526 | `RtlSetSystemBootStatus` | `0x10ED90` | 90 | UnwindData |  |
| 746 | `RtlAddVectoredContinueHandler` | `0x10EDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 724 | `RtlAddAccessDeniedAce` | `0x10EE10` | 31 | UnwindData |  |
| 1072 | `RtlGetCallersAddress` | `0x10F1C0` | 103 | UnwindData |  |
| 1517 | `RtlSetProcessPlaceholderCompatibilityMode` | `0x10F250` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1134 | `RtlGetSystemBootStatus` | `0x10F2C0` | 90 | UnwindData |  |
| 1006 | `RtlExtendMemoryBlockLookaside` | `0x10F320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `LdrFindResourceDirectory_U` | `0x10F330` | 26 | UnwindData |  |
| 812 | `RtlCommitDebugInfo` | `0x10F350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `RtlDeCommitDebugInfo` | `0x10F360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `RtlCheckSystemBootStatusIntegrity` | `0x10F370` | 92 | UnwindData |  |
| 998 | `RtlEthernetStringToAddressW` | `0x10F3E0` | 305 | UnwindData |  |
| 40 | `CsrGetProcessId` | `0x10F870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 936 | `RtlDestroyAtomTable` | `0x10F890` | 170 | UnwindData |  |
| 1259 | `RtlIsNameInUnUpcasedExpression` | `0x10FA00` | 173 | UnwindData |  |
| 994 | `RtlEraseUnicodeString` | `0x10FE20` | 57 | UnwindData |  |
| 1352 | `RtlOwnerAcesPresent` | `0x10FE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1848 | `WinSqmStartSession` | `0x10FE70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1849 | `WinSqmStartSessionForPartner` | `0x10FE70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 857 | `RtlCrc64` | `0x10FE80` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `RtlGetCriticalSectionRecursionCount` | `0x1100B0` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1699 | `RtlpConvertAbsoluteToRelativeSecurityAttribute` | `0x1103C0` | 928 | UnwindData |  |
| 771 | `RtlAreAnyAccessesGranted` | `0x110AC0` | 2,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `LdrAppxHandleIntegrityFailure` | `0x1112B0` | 532 | UnwindData |  |
| 1717 | `RtlpMuiRegCreateRegistryInfo` | `0x1120B0` | 50 | UnwindData |  |
| 738 | `RtlAddIntegrityLabelToBoundaryDescriptor` | `0x112800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `DbgUiConvertStateChangeStructureEx` | `0x112810` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `LdrQueryOptionalDelayLoadedAPI` | `0x112D20` | 188 | UnwindData |  |
| 51 | `DbgUiConnectToDbg` | `0x112DF0` | 110 | UnwindData |  |
| 1244 | `RtlIsCriticalSectionLocked` | `0x1134E0` | 9,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1503 | `RtlSetExtendedFeaturesMask` | `0x1158B0` | 44 | UnwindData |  |
| 1252 | `RtlIsEnclaveFeaturePresent` | `0x1178C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1241 | `RtlIsApiSetImplemented` | `0x1178E0` | 58 | UnwindData |  |
| 9 | `A_SHAFinal` | `0x117CF0` | 246 | UnwindData |  |
| 10 | `A_SHAInit` | `0x117DF0` | 221 | UnwindData |  |
| 11 | `A_SHAUpdate` | `0x117EE0` | 249 | UnwindData |  |
| 196 | `MD5Final` | `0x117FE0` | 301 | UnwindData |  |
| 197 | `MD5Init` | `0x118120` | 138 | UnwindData |  |
| 198 | `MD5Update` | `0x1181B0` | 247 | UnwindData |  |
| 71 | `EtwEventSetInformation` | `0x1182B0` | 131 | UnwindData |  |
| 1383 | `RtlQueryInternalFeatureConfiguration` | `0x11A9F0` | 179 | UnwindData |  |
| 1284 | `RtlLengthCurrentClearRunForwardEx` | `0x11B720` | 219 | UnwindData |  |
| 1127 | `RtlGetReturnAddressHijackTarget` | `0x11D0A0` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `RtlUnhandledExceptionFilter2` | `0x11D850` | 975 | UnwindData |  |
| 898 | `RtlDeNormalizeProcessParams` | `0x11DFC0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1135 | `RtlGetSystemBootStatusEx` | `0x11E0A0` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1527 | `RtlSetSystemBootStatusEx` | `0x11E5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1398 | `RtlQueryRegistryValueWithFallback` | `0x11E5D0` | 355 | UnwindData |  |
| 1700 | `RtlpConvertCultureNamesToLCIDs` | `0x11E740` | 497 | UnwindData |  |
| 1101 | `RtlGetFunctionTableListHead` | `0x11E960` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `DbgBreakPoint` | `0x11ECE0` | 2 | UnwindData |  |
| 62 | `DbgUserBreakPoint` | `0x11ECF0` | 2 | UnwindData |  |
| 787 | `RtlCaptureContext` | `0x11EE00` | 175 | UnwindData |  |
| 788 | `RtlCaptureContext2` | `0x11EF40` | 256 | UnwindData |  |
| 1419 | `RtlRaiseNoncontinuableException` | `0x11F5D0` | 112 | UnwindData |  |
| 2340 | `__C_specific_handler` | `0x11F8A0` | 455 | UnwindData |  |
| 2342 | `__isascii` | `0x11FA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2343 | `__iscsym` | `0x11FA90` | 45 | UnwindData |  |
| 2344 | `__iscsymf` | `0x11FAD0` | 58 | UnwindData |  |
| 2346 | `__toascii` | `0x11FB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2428 | `isalnum` | `0x11FB20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2429 | `isalpha` | `0x11FB50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2430 | `iscntrl` | `0x11FB80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2431 | `isdigit` | `0x11FBB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2432 | `isgraph` | `0x11FBE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2433 | `islower` | `0x11FC10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2434 | `isprint` | `0x11FC40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2435 | `ispunct` | `0x11FC70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2436 | `isspace` | `0x11FCA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2437 | `isupper` | `0x11FCD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2448 | `isxdigit` | `0x11FD00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2347 | `_atoi64` | `0x11FD30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2420 | `atoi` | `0x11FD50` | 31 | UnwindData |  |
| 2421 | `atol` | `0x11FD80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2350 | `_i64toa` | `0x11FDA0` | 41 | UnwindData |  |
| 2354 | `_itoa` | `0x11FDD0` | 40 | UnwindData |  |
| 2360 | `_ltoa` | `0x11FDD0` | 40 | UnwindData |  |
| 2387 | `_ui64toa` | `0x11FE00` | 26 | UnwindData |  |
| 2391 | `_ultoa` | `0x11FE20` | 26 | UnwindData |  |
| 2352 | `_i64tow` | `0x11FF30` | 41 | UnwindData |  |
| 2356 | `_itow` | `0x11FF60` | 40 | UnwindData |  |
| 2362 | `_ltow` | `0x11FF60` | 40 | UnwindData |  |
| 2389 | `_ui64tow` | `0x11FF90` | 26 | UnwindData |  |
| 2393 | `_ultow` | `0x11FFB0` | 26 | UnwindData |  |
| 2358 | `_lfind` | `0x120100` | 164 | UnwindData |  |
| 2359 | `_local_unwind` | `0x1201B0` | 40 | UnwindData |  |
| 2365 | `_memccpy` | `0x1201E0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2366 | `_memicmp` | `0x120280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2369 | `_snprintf` | `0x1202A0` | 174 | UnwindData |  |
| 2372 | `_snwprintf` | `0x120360` | 229 | UnwindData |  |
| 2375 | `_splitpath` | `0x120450` | 136 | UnwindData |  |
| 2377 | `_strcmpi` | `0x1207B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2378 | `_stricmp` | `0x1207B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2379 | `_strlwr` | `0x1207C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2380 | `_strlwr_s` | `0x1207F0` | 98 | UnwindData |  |
| 2381 | `_strnicmp` | `0x1208C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2384 | `_strupr` | `0x1208D0` | 70 | UnwindData |  |
| 2385 | `_strupr_s` | `0x120920` | 98 | UnwindData |  |
| 2386 | `_swprintf` | `0x120990` | 188 | UnwindData |  |
| 2490 | `swprintf` | `0x120990` | 188 | UnwindData |  |
| 2395 | `_vscprintf` | `0x120A60` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2500 | `vsprintf` | `0x120B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2396 | `_vscwprintf` | `0x120B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2401 | `_vswprintf` | `0x120BB0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2397 | `_vsnprintf` | `0x120C80` | 22 | UnwindData |  |
| 2399 | `_vsnwprintf` | `0x120D60` | 22 | UnwindData |  |
| 2402 | `_wcsicmp` | `0x120E70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2403 | `_wcslwr` | `0x120ED0` | 78 | UnwindData |  |
| 2404 | `_wcslwr_s` | `0x120F30` | 116 | UnwindData |  |
| 2405 | `_wcsnicmp` | `0x120FB0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2406 | `_wcsnset_s` | `0x121020` | 137 | UnwindData |  |
| 2407 | `_wcsset_s` | `0x1210B0` | 86 | UnwindData |  |
| 2408 | `_wcstoi64` | `0x121110` | 41 | UnwindData |  |
| 2409 | `_wcstoui64` | `0x121140` | 44 | UnwindData |  |
| 2410 | `_wcsupr` | `0x1213E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2411 | `_wcsupr_s` | `0x121410` | 116 | UnwindData |  |
| 2414 | `_wtoi` | `0x121490` | 31 | UnwindData |  |
| 2415 | `_wtoi64` | `0x1214C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2416 | `_wtol` | `0x1214E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2417 | `abs` | `0x121500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2449 | `labs` | `0x121500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2418 | `atan` | `0x121510` | 608 | UnwindData |  |
| 2419 | `atan2` | `0x121780` | 307 | UnwindData |  |
| 2422 | `bsearch` | `0x121F40` | 244 | UnwindData |  |
| 2423 | `bsearch_s` | `0x122040` | 262 | UnwindData |  |
| 2424 | `ceil` | `0x122150` | 273 | UnwindData |  |
| 2425 | `cos` | `0x122270` | 729 | UnwindData |  |
| 2463 | `sin` | `0x122600` | 359 | UnwindData |  |
| 2426 | `fabs` | `0x122A20` | 248 | UnwindData |  |
| 2427 | `floor` | `0x122B20` | 255 | UnwindData |  |
| 2438 | `iswalnum` | `0x122C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2439 | `iswalpha` | `0x122C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2440 | `iswascii` | `0x122C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2442 | `iswdigit` | `0x122C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2443 | `iswgraph` | `0x122CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2444 | `iswlower` | `0x122CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2445 | `iswprint` | `0x122CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2446 | `iswspace` | `0x122CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2447 | `iswxdigit` | `0x122CE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2441 | `iswctype` | `0x122D20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2450 | `log` | `0x122D50` | 764 | UnwindData |  |
| 2451 | `longjmp` | `0x123060` | 40 | UnwindData |  |
| 2452 | `mbstowcs` | `0x123090` | 197 | UnwindData |  |
| 2453 | `memchr` | `0x123180` | 144 | UnwindData |  |
| 2460 | `pow` | `0x123220` | 2,993 | UnwindData |  |
| 2461 | `qsort` | `0x123DE0` | 126 | UnwindData |  |
| 2462 | `qsort_s` | `0x1241A0` | 141 | UnwindData |  |
| 2464 | `sprintf` | `0x124590` | 151 | UnwindData |  |
| 2466 | `sqrt` | `0x124630` | 273 | UnwindData |  |
| 2467 | `sscanf` | `0x124760` | 55 | UnwindData |  |
| 2471 | `strchr` | `0x124850` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2475 | `strcspn` | `0x1248E0` | 134 | UnwindData |  |
| 2482 | `strnlen` | `0x124980` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2483 | `strpbrk` | `0x124AD0` | 112 | UnwindData |  |
| 2484 | `strrchr` | `0x124B50` | 317 | UnwindData |  |
| 2485 | `strspn` | `0x124CA0` | 138 | UnwindData |  |
| 2486 | `strstr` | `0x124D30` | 492 | UnwindData |  |
| 2488 | `strtol` | `0x125160` | 40 | UnwindData |  |
| 2489 | `strtoul` | `0x1251C0` | 43 | UnwindData |  |
| 2493 | `tan` | `0x125200` | 796 | UnwindData |  |
| 2494 | `tolower` | `0x125730` | 45 | UnwindData |  |
| 2495 | `toupper` | `0x125770` | 97 | UnwindData |  |
| 2496 | `towlower` | `0x1257E0` | 37 | UnwindData |  |
| 2497 | `towupper` | `0x125810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2503 | `wcscat` | `0x125820` | 47 | UnwindData |  |
| 2507 | `wcscpy` | `0x125860` | 57 | UnwindData |  |
| 2505 | `wcschr` | `0x1258A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2506 | `wcscmp` | `0x125920` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2509 | `wcscspn` | `0x125960` | 94 | UnwindData |  |
| 2510 | `wcslen` | `0x1259D0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2511 | `wcsncat` | `0x125AF0` | 99 | UnwindData |  |
| 2513 | `wcsncmp` | `0x125B60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2514 | `wcsncpy` | `0x125BA0` | 119 | UnwindData |  |
| 2516 | `wcsnlen` | `0x125C20` | 453 | UnwindData |  |
| 2517 | `wcspbrk` | `0x125DF0` | 77 | UnwindData |  |
| 2518 | `wcsrchr` | `0x125E50` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2519 | `wcsspn` | `0x125F10` | 94 | UnwindData |  |
| 2520 | `wcsstr` | `0x125F80` | 534 | UnwindData |  |
| 2522 | `wcstol` | `0x1263D0` | 40 | UnwindData |  |
| 2524 | `wcstoul` | `0x126430` | 43 | UnwindData |  |
| 2523 | `wcstombs` | `0x126470` | 118 | UnwindData |  |
| 2351 | `_i64toa_s` | `0x12A7D0` | 36 | UnwindData |  |
| 2355 | `_itoa_s` | `0x12A800` | 35 | UnwindData |  |
| 2361 | `_ltoa_s` | `0x12A800` | 35 | UnwindData |  |
| 2388 | `_ui64toa_s` | `0x12A830` | 20 | UnwindData |  |
| 2392 | `_ultoa_s` | `0x12A850` | 20 | UnwindData |  |
| 2353 | `_i64tow_s` | `0x12AAD0` | 36 | UnwindData |  |
| 2357 | `_itow_s` | `0x12AB00` | 35 | UnwindData |  |
| 2363 | `_ltow_s` | `0x12AB00` | 35 | UnwindData |  |
| 2390 | `_ui64tow_s` | `0x12AB30` | 20 | UnwindData |  |
| 2394 | `_ultow_s` | `0x12AB50` | 20 | UnwindData |  |
| 2364 | `_makepath_s` | `0x12ADF0` | 334 | UnwindData |  |
| 2370 | `_snprintf_s` | `0x12AF50` | 30 | UnwindData |  |
| 2398 | `_vsnprintf_s` | `0x12AF80` | 152 | UnwindData |  |
| 2371 | `_snscanf_s` | `0x12B020` | 57 | UnwindData |  |
| 2373 | `_snwprintf_s` | `0x12B060` | 30 | UnwindData |  |
| 2400 | `_vsnwprintf_s` | `0x12B090` | 163 | UnwindData |  |
| 2374 | `_snwscanf_s` | `0x12B140` | 57 | UnwindData |  |
| 2376 | `_splitpath_s` | `0x12B180` | 654 | UnwindData |  |
| 2382 | `_strnset_s` | `0x12B420` | 131 | UnwindData |  |
| 2383 | `_strset_s` | `0x12B4B0` | 82 | UnwindData |  |
| 2412 | `_wmakepath_s` | `0x12B510` | 381 | UnwindData |  |
| 2413 | `_wsplitpath_s` | `0x12B6A0` | 687 | UnwindData |  |
| 2456 | `memcpy_s` | `0x12B960` | 140 | UnwindData |  |
| 2458 | `memmove_s` | `0x12BA00` | 88 | UnwindData |  |
| 2465 | `sprintf_s` | `0x12BA60` | 30 | UnwindData |  |
| 2501 | `vsprintf_s` | `0x12BA90` | 72 | UnwindData |  |
| 2468 | `sscanf_s` | `0x12BAE0` | 77 | UnwindData |  |
| 2470 | `strcat_s` | `0x12BB40` | 137 | UnwindData |  |
| 2474 | `strcpy_s` | `0x12BBD0` | 127 | UnwindData |  |
| 2478 | `strncat_s` | `0x12BC60` | 245 | UnwindData |  |
| 2481 | `strncpy_s` | `0x12BD60` | 235 | UnwindData |  |
| 2487 | `strtok_s` | `0x12BE60` | 348 | UnwindData |  |
| 2491 | `swprintf_s` | `0x12BFD0` | 30 | UnwindData |  |
| 2502 | `vswprintf_s` | `0x12C000` | 82 | UnwindData |  |
| 2492 | `swscanf_s` | `0x12C060` | 78 | UnwindData |  |
| 2504 | `wcscat_s` | `0x12C0C0` | 144 | UnwindData |  |
| 2508 | `wcscpy_s` | `0x12C160` | 132 | UnwindData |  |
| 2512 | `wcsncat_s` | `0x12C1F0` | 264 | UnwindData |  |
| 2515 | `wcsncpy_s` | `0x12C300` | 254 | UnwindData |  |
| 2521 | `wcstok_s` | `0x12C410` | 249 | UnwindData |  |
| 769 | `RtlAppxIsFileOwnedByTrustedInstaller` | `0x12FD50` | 367 | UnwindData |  |
| 36 | `CsrCaptureTimeout` | `0x12FED0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `CsrVerifyRegion` | `0x12FF00` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1250 | `RtlIsEcCode` | `0x12FF00` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `RtlApplicationVerifierStop` | `0x1301F0` | 155 | UnwindData |  |
| 1665 | `RtlWow64ChangeProcessState` | `0x130380` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1676 | `RtlWow64GetThreadContext` | `0x1303B0` | 35 | UnwindData |  |
| 1677 | `RtlWow64GetThreadSelectorEntry` | `0x1303E0` | 426 | UnwindData |  |
| 1685 | `RtlWow64SetThreadContext` | `0x130590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `RtlWow64SuspendProcess` | `0x1305B0` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 946 | `RtlDisableThreadProfiling` | `0x130A50` | 101 | UnwindData |  |
| 968 | `RtlEnableThreadProfiling` | `0x130AC0` | 244 | UnwindData |  |
| 1405 | `RtlQueryThreadProfiling` | `0x130BC0` | 34 | UnwindData |  |
| 55 | `DbgUiDebugActiveProcess` | `0x130BF0` | 76 | UnwindData |  |
| 56 | `DbgUiGetThreadDebugObject` | `0x130C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `DbgUiIssueRemoteBreakin` | `0x130C70` | 318 | UnwindData |  |
| 58 | `DbgUiRemoteBreakin` | `0x130DC0` | 88 | UnwindData |  |
| 59 | `DbgUiSetThreadDebugObject` | `0x130E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `DbgUiStopDebugging` | `0x130E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `LdrDeleteEnclave` | `0x130E60` | 238 | UnwindData |  |
| 808 | `RtlCloneMemoryStream` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `RtlCommitMemoryStream` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `RtlCopyMemoryStreamTo` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | `RtlCopyOutOfProcessMemoryStreamTo` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `RtlLockMemoryStreamRegion` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1382 | `RtlQueryInterfaceMemoryStream` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1431 | `RtlReadMemoryStream` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1432 | `RtlReadOutOfProcessMemoryStream` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1473 | `RtlRevertMemoryStream` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1482 | `RtlSeekMemoryStream` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `RtlSetMemoryStreamSize` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1553 | `RtlStatMemoryStream` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1613 | `RtlUnlockMemoryStreamRegion` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1688 | `RtlWriteMemoryStream` | `0x131100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `RtlCreateProcessReflection` | `0x131110` | 1,432 | UnwindData |  |
| 840 | `RtlConvertToAutoInheritSecurityObject` | `0x131A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `RtlCreateUserSecurityObject` | `0x131A50` | 148 | UnwindData |  |
| 1322 | `RtlNewInstanceSecurityObject` | `0x131AF0` | 319 | UnwindData |  |
| 1323 | `RtlNewSecurityGrantedAccess` | `0x131C40` | 349 | UnwindData |  |
| 1515 | `RtlSetProcessDebugInformation` | `0x131DB0` | 488 | UnwindData |  |
| 1728 | `RtlpQueryProcessDebugInformationFromWow64` | `0x132060` | 152 | UnwindData |  |
| 1729 | `RtlpQueryProcessDebugInformationRemote` | `0x132100` | 233 | UnwindData |  |
| 1198 | `RtlInitializeNtUserPfn` | `0x132270` | 283 | UnwindData |  |
| 1465 | `RtlResetNtUserPfn` | `0x1323A0` | 115 | UnwindData |  |
| 1472 | `RtlRetrieveNtUserPfn` | `0x132420` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1455 | `RtlRemoveVectoredContinueHandler` | `0x1324A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1414 | `RtlQueueApcWow64Thread` | `0x1324B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1460 | `RtlReportExceptionEx` | `0x1324D0` | 1,150 | UnwindData |  |
| 1662 | `RtlWerpReportException` | `0x132960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1819 | `WerReportExceptionWorker` | `0x132970` | 163 | UnwindData |  |
| 1750 | `ShipAssertGetBufferInfo` | `0x132A20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1751 | `ShipAssertMsgA` | `0x132A50` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1752 | `ShipAssertMsgW` | `0x132A50` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1837 | `WinSqmGetInstrumentationProperty` | `0x132C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1695 | `RtlZombifyActivationContext` | `0x132C90` | 112 | UnwindData |  |
| 1240 | `RtlIsActivationContextActive` | `0x132D10` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 826 | `RtlComputeImportTableHash` | `0x1330A0` | 664 | UnwindData |  |
| 14 | `AlpcGetCompletionListLastMessageInformation` | `0x134A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `AlpcGetCompletionListMessageAttributes` | `0x134A80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `DbgPrintReturnControlC` | `0x134AC0` | 64 | UnwindData |  |
| 48 | `DbgPrompt` | `0x134B10` | 74 | UnwindData |  |
| 49 | `DbgQueryDebugFilterState` | `0x134B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `DbgSetDebugFilterState` | `0x134B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2498 | `vDbgPrintEx` | `0x134B80` | 40 | UnwindData |  |
| 2499 | `vDbgPrintExWithPrefix` | `0x134BB0` | 30 | UnwindData |  |
| 121 | `LdrEnumResources` | `0x134BE0` | 698 | UnwindData |  |
| 178 | `LdrSetMUICacheType` | `0x134EA0` | 98 | UnwindData |  |
| 888 | `RtlCreateUserProcess` | `0x134FF0` | 128 | UnwindData |  |
| 1507 | `RtlSetImageMitigationPolicy` | `0x135080` | 4,357 | UnwindData |  |
| 1639 | `RtlValidProcessProtection` | `0x136190` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `LdrProcessRelocationBlock` | `0x1364C0` | 37 | UnwindData |  |
| 155 | `LdrProcessRelocationBlockEx` | `0x1364F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1384 | `RtlQueryModuleInformation` | `0x136500` | 659 | UnwindData |  |
| 165 | `LdrResFindResource` | `0x1367A0` | 160 | UnwindData |  |
| 829 | `RtlConsoleMultiByteToUnicodeN` | `0x136850` | 357 | UnwindData |  |
| 1628 | `RtlUpcaseUnicodeToCustomCPN` | `0x1369C0` | 359 | UnwindData |  |
| 697 | `PfxFindPrefix` | `0x136D80` | 203 | UnwindData |  |
| 698 | `PfxInitialize` | `0x136E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 699 | `PfxInsertPrefix` | `0x136E80` | 270 | UnwindData |  |
| 700 | `PfxRemovePrefix` | `0x136FA0` | 183 | UnwindData |  |
| 752 | `RtlAllocateAndInitializeSidEx` | `0x137060` | 190 | UnwindData |  |
| 845 | `RtlCopyLuidAndAttributesArray` | `0x137130` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `RtlCopySidAndAttributesArray` | `0x137160` | 173 | UnwindData |  |
| 988 | `RtlEqualLuid` | `0x137220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1131 | `RtlGetSessionProperties` | `0x137240` | 188 | UnwindData |  |
| 1272 | `RtlIsUntrustedObject` | `0x137310` | 389 | UnwindData |  |
| 1315 | `RtlMapSecurityErrorToNtStatus` | `0x1374A0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `RtlNormalizeSecurityDescriptor` | `0x1375B0` | 728 | UnwindData |  |
| 1457 | `RtlReplaceSidInSd` | `0x137890` | 748 | UnwindData |  |
| 1488 | `RtlSetAttributesSecurityDescriptor` | `0x137B90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1544 | `RtlSidEqualLevel` | `0x137BC0` | 127 | UnwindData |  |
| 1547 | `RtlSidIsHigherLevel` | `0x137C50` | 127 | UnwindData |  |
| 837 | `RtlConvertSRWLockExclusiveToShared` | `0x138C60` | 69 | UnwindData |  |
| 1588 | `RtlTryConvertSRWLockSharedToExclusiveOrRelease` | `0x138CB0` | 116 | UnwindData |  |
| 964 | `RtlDumpResource` | `0x138D30` | 74 | UnwindData |  |
| 967 | `RtlEnableEarlyCriticalSectionEventCreation` | `0x138D80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `RtlpUnWaitCriticalSection` | `0x138DB0` | 82 | UnwindData |  |
| 723 | `RtlAddAccessAllowedObjectAce` | `0x138E10` | 90 | UnwindData |  |
| 726 | `RtlAddAccessDeniedObjectAce` | `0x138E70` | 90 | UnwindData |  |
| 727 | `RtlAddAccessFilterAce` | `0x138ED0` | 506 | UnwindData |  |
| 732 | `RtlAddAuditAccessAce` | `0x1390D0` | 57 | UnwindData |  |
| 734 | `RtlAddAuditAccessObjectAce` | `0x139110` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `RtlAddCompoundAce` | `0x139180` | 365 | UnwindData |  |
| 743 | `RtlAddResourceAttributeAce` | `0x139300` | 903 | UnwindData |  |
| 745 | `RtlAddScopedPolicyIDAce` | `0x139690` | 380 | UnwindData |  |
| 1508 | `RtlSetInformationAcl` | `0x139820` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1702 | `RtlpConvertRelativeToAbsoluteSecurityAttribute` | `0x139A10` | 1,258 | UnwindData |  |
| 1354 | `RtlPinAtomInAtomTable` | `0x13A280` | 173 | UnwindData |  |
| 1463 | `RtlResetMemoryBlockLookaside` | `0x13A360` | 83 | UnwindData |  |
| 1464 | `RtlResetMemoryZone` | `0x13A3C0` | 75 | UnwindData |  |
| 986 | `RtlEqualComputerName` | `0x13A420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1056 | `RtlFreeOemString` | `0x13A430` | 24 | UnwindData |  |
| 1598 | `RtlUnicodeStringToCountedOemString` | `0x13A450` | 257 | UnwindData |  |
| 1625 | `RtlUpcaseUnicodeStringToAnsiString` | `0x13A560` | 225 | UnwindData |  |
| 1626 | `RtlUpcaseUnicodeStringToCountedOemString` | `0x13A650` | 257 | UnwindData |  |
| 761 | `RtlAppendAsciizToString` | `0x13A760` | 109 | UnwindData |  |
| 763 | `RtlAppendStringToString` | `0x13A7E0` | 77 | UnwindData |  |
| 1177 | `RtlInitStringEx` | `0x13A840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1180 | `RtlInitUTF8StringEx` | `0x13A840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1635 | `RtlUpperString` | `0x13A850` | 80 | UnwindData |  |
| 802 | `RtlClearAllBitsEx` | `0x13A8B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 804 | `RtlClearBitEx` | `0x13A8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 806 | `RtlClearBitsEx` | `0x13A8F0` | 177 | UnwindData |  |
| 841 | `RtlCopyBitMap` | `0x13A9B0` | 519 | UnwindData |  |
| 1019 | `RtlFindClearBitsAndSetEx` | `0x13ABC0` | 878 | UnwindData |  |
| 1020 | `RtlFindClearBitsEx` | `0x13AF40` | 821 | UnwindData |  |
| 1031 | `RtlFindSetBitsAndClear` | `0x13B280` | 955 | UnwindData |  |
| 1032 | `RtlFindSetBitsAndClearEx` | `0x13B650` | 944 | UnwindData |  |
| 1221 | `RtlInterlockedSetBitRun` | `0x13BA10` | 177 | UnwindData |  |
| 1283 | `RtlLengthCurrentClearRunBackwardEx` | `0x13BAD0` | 157 | UnwindData |  |
| 1339 | `RtlNumberOfClearBitsEx` | `0x13BB80` | 30 | UnwindData |  |
| 1340 | `RtlNumberOfClearBitsInRange` | `0x13BBB0` | 33 | UnwindData |  |
| 1343 | `RtlNumberOfSetBitsInRange` | `0x13BBE0` | 422 | UnwindData |  |
| 1487 | `RtlSetAllBitsEx` | `0x13BD90` | 102 | UnwindData |  |
| 1492 | `RtlSetBitsEx` | `0x13BE00` | 174 | UnwindData |  |
| 779 | `RtlBarrier` | `0x13C070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 780 | `RtlBarrierForDelete` | `0x13C080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | `RtlDeleteBarrier` | `0x13C090` | 41 | UnwindData |  |
| 1170 | `RtlInitBarrier` | `0x13C0C0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1211 | `RtlInt64ToUnicodeString` | `0x13C1D0` | 158 | UnwindData |  |
| 791 | `RtlCheckBootStatusIntegrity` | `0x13C2B0` | 355 | UnwindData |  |
| 862 | `RtlCreateBootStatusDataFile` | `0x13C420` | 461 | UnwindData |  |
| 1132 | `RtlGetSetBootStatusData` | `0x13C600` | 379 | UnwindData |  |
| 1295 | `RtlLockBootStatusData` | `0x13C790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1467 | `RtlRestoreBootStatusDefaults` | `0x13C7B0` | 241 | UnwindData |  |
| 1470 | `RtlRestoreSystemBootStatusDefaults` | `0x13C8B0` | 54 | UnwindData |  |
| 1609 | `RtlUnlockBootStatusData` | `0x13C8F0` | 59 | UnwindData |  |
| 1514 | `RtlSetPortableOperatingSystem` | `0x13CC60` | 59 | UnwindData |  |
| 876 | `RtlCreateRegistryKey` | `0x13CCB0` | 56 | UnwindData |  |
| 1370 | `RtlQueryDynamicTimeZoneInformation` | `0x13CCF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1499 | `RtlSetDynamicTimeZoneInformation` | `0x13CD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1536 | `RtlSetTimeZoneInformation` | `0x13CD10` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 836 | `RtlConvertLCIDToString` | `0x13D120` | 260 | UnwindData |  |
| 1698 | `RtlpCleanupRegistryKeys` | `0x13D730` | 1,100 | UnwindData |  |
| 1701 | `RtlpConvertLCIDsToCultureNames` | `0x13DB90` | 539 | UnwindData |  |
| 1732 | `RtlpSetInstallLanguage` | `0x13E300` | 1,176 | UnwindData |  |
| 1733 | `RtlpSetPreferredUILanguages` | `0x13E910` | 3,030 | UnwindData |  |
| 1734 | `RtlpSetUserPreferredUILanguages` | `0x13E910` | 3,030 | UnwindData |  |
| 1738 | `RtlpVerifyAndCommitUILanguageSettings` | `0x13F4F0` | 368 | UnwindData |  |
| 810 | `RtlCmDecodeMemIoResource` | `0x13F6B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 811 | `RtlCmEncodeMemIoResource` | `0x13F720` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `RtlFindClosestEncodableLength` | `0x13F800` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1222 | `RtlIoDecodeMemIoResource` | `0x13F8B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `RtlIoEncodeMemIoResource` | `0x13F950` | 394 | UnwindData |  |
| 979 | `RtlEnumProcessHeaps` | `0x13FB00` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1320 | `RtlMultipleAllocateHeap` | `0x13FBC0` | 104 | UnwindData |  |
| 1321 | `RtlMultipleFreeHeap` | `0x13FC30` | 98 | UnwindData |  |
| 1403 | `RtlQueryTagHeap` | `0x13FCA0` | 439 | UnwindData |  |
| 1645 | `RtlValidateProcessHeaps` | `0x13FF40` | 32 | UnwindData |  |
| 815 | `RtlCompareAltitudes` | `0x1410A0` | 490 | UnwindData |  |
| 816 | `RtlCompareExchangePointerMapping` | `0x141290` | 318 | UnwindData |  |
| 817 | `RtlCompareExchangePropertyStore` | `0x1413E0` | 546 | UnwindData |  |
| 1390 | `RtlQueryPointerMapping` | `0x141610` | 172 | UnwindData |  |
| 1396 | `RtlQueryPropertyStore` | `0x1416D0` | 128 | UnwindData |  |
| 1452 | `RtlRemovePointerMapping` | `0x141760` | 208 | UnwindData |  |
| 1454 | `RtlRemovePropertyStore` | `0x141840` | 202 | UnwindData |  |
| 905 | `RtlDecompressBuffer` | `0x141910` | 119 | UnwindData |  |
| 907 | `RtlDecompressFragment` | `0x141990` | 143 | UnwindData |  |
| 830 | `RtlConstructCrossVmEventPath` | `0x141B10` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `RtlConstructCrossVmMutexPath` | `0x141B10` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 867 | `RtlCreateHashTableEx` | `0x141C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `RtlEndWeakEnumerationHashTable` | `0x141C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1178 | `RtlInitStrongEnumerationHashTable` | `0x141CA0` | 65 | UnwindData |  |
| 1183 | `RtlInitWeakEnumerationHashTable` | `0x141CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1661 | `RtlWeaklyEnumerateEntryHashTable` | `0x141D00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `RtlLocalTimeToSystemTime` | `0x141D30` | 112 | UnwindData |  |
| 1481 | `RtlSecondsSince1980ToTime` | `0x141DB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `RtlCopyExtendedContext` | `0x141DE0` | 26 | UnwindData |  |
| 1693 | `RtlZeroHeap` | `0x142330` | 1,272 | UnwindData |  |
| 883 | `RtlCreateUmsCompletionList` | `0x1429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 884 | `RtlCreateUmsThreadContext` | `0x1429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `RtlDeleteUmsCompletionList` | `0x1429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | `RtlDeleteUmsThreadContext` | `0x1429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 931 | `RtlDequeueUmsCompletionListItems` | `0x1429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 978 | `RtlEnterUmsSchedulingMode` | `0x1429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `RtlExecuteUmsThread` | `0x1429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1115 | `RtlGetNextUmsListItem` | `0x1429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1146 | `RtlGetUmsCompletionListEvent` | `0x1429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `RtlQueryUmsThreadInformation` | `0x1429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `RtlSetUmsThreadInformation` | `0x1429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `RtlUmsThreadYield` | `0x1429D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1084 | `RtlGetCurrentUmsThread` | `0x1429E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1562 | `RtlSubtreeSuccessor` | `0x142A00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 983 | `RtlEnumerateGenericTableLikeADirectory` | `0x142A30` | 252 | UnwindData |  |
| 1088 | `RtlGetElementGenericTableAvl` | `0x142B40` | 285 | UnwindData |  |
| 932 | `RtlDeregisterSecureMemoryCacheCallback` | `0x142C70` | 172 | UnwindData |  |
| 1438 | `RtlRegisterSecureMemoryCacheCallback` | `0x142D30` | 171 | UnwindData |  |
| 963 | `RtlDrainNonVolatileFlush` | `0x1430B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1044 | `RtlFlushNonVolatileMemory` | `0x1430E0` | 126 | UnwindData |  |
| 995 | `RtlEthernetAddressToStringA` | `0x143170` | 100 | UnwindData |  |
| 997 | `RtlEthernetStringToAddressA` | `0x1431E0` | 298 | UnwindData |  |
| 1011 | `RtlFillNonVolatileMemory` | `0x143310` | 165 | UnwindData |  |
| 1045 | `RtlFlushNonVolatileMemoryRanges` | `0x1433C0` | 136 | UnwindData |  |
| 1055 | `RtlFreeNonVolatileToken` | `0x143450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1116 | `RtlGetNonVolatileToken` | `0x143470` | 130 | UnwindData |  |
| 1689 | `RtlWriteNonVolatileMemory` | `0x143500` | 172 | UnwindData |  |
| 1048 | `RtlFormatMessage` | `0x1435C0` | 81 | UnwindData |  |
| 1064 | `RtlGenerate8dot3Name` | `0x143790` | 1,227 | UnwindData |  |
| 1260 | `RtlIsNameLegalDOS8Dot3` | `0x143C70` | 463 | UnwindData |  |
| 1074 | `RtlGetConsoleSessionForegroundProcessId` | `0x143F40` | 49 | UnwindData |  |
| 1516 | `RtlSetProcessIsCritical` | `0x143F80` | 151 | UnwindData |  |
| 1692 | `RtlXSave` | `0x144020` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `RtlGetFeatureToggleConfiguration` | `0x144070` | 334 | UnwindData |  |
| 1095 | `RtlGetFeatureTogglesChangeToken` | `0x1441D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `RtlNotifyFeatureToggleUsage` | `0x1441E0` | 202 | UnwindData |  |
| 1158 | `RtlIdnToNameprepUnicode` | `0x144C00` | 30 | UnwindData |  |
| 1188 | `RtlInitializeContext` | `0x144C40` | 285 | UnwindData |  |
| 1450 | `RtlRemoteCall` | `0x144D70` | 380 | UnwindData |  |
| 1267 | `RtlIsPartialPlaceholderFileInfo` | `0x144F00` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1395 | `RtlQueryProcessPlaceholderCompatibilityMode` | `0x144F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1277 | `RtlIsZeroMemory` | `0x144FB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `RtlIsFeatureEnabledForEnterprise` | `0x145000` | 119 | UnwindData |  |
| 1594 | `RtlUnhandledExceptionFilter` | `0x145530` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `RtlLogUnexpectedCodepath` | `0x1455A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1351 | `RtlOverwriteFeatureConfigurationBuffer` | `0x1455B0` | 168 | UnwindData |  |
| 1365 | `RtlQueryAllInternalFeatureConfigurations` | `0x145660` | 163 | UnwindData |  |
| 1366 | `RtlQueryAllInternalRuntimeFeatureConfigurations` | `0x145710` | 237 | UnwindData |  |
| 1559 | `RtlSubscribeForFeatureUsageNotification` | `0x145810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `RtlUnsubscribeFromFeatureUsageNotifications` | `0x145820` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1350 | `RtlOsDeploymentState` | `0x1458E0` | 322 | UnwindData |  |
| 1410 | `RtlQueryValidationRunlevel` | `0x145A30` | 204 | UnwindData |  |
| 1416 | `RtlRaiseCustomSystemEventTrigger` | `0x145B10` | 575 | UnwindData |  |
| 1425 | `RtlRcuAllocate` | `0x145EF0` | 196 | UnwindData |  |
| 1426 | `RtlRcuFree` | `0x145FC0` | 166 | UnwindData |  |
| 1427 | `RtlRcuReadLock` | `0x146070` | 99 | UnwindData |  |
| 1428 | `RtlRcuReadUnlock` | `0x1460E0` | 76 | UnwindData |  |
| 1429 | `RtlRcuSynchronize` | `0x146140` | 193 | UnwindData |  |
| 1577 | `RtlTraceDatabaseAdd` | `0x146480` | 112 | UnwindData |  |
| 1578 | `RtlTraceDatabaseCreate` | `0x146500` | 302 | UnwindData |  |
| 1579 | `RtlTraceDatabaseDestroy` | `0x146640` | 120 | UnwindData |  |
| 1580 | `RtlTraceDatabaseEnumerate` | `0x1466C0` | 203 | UnwindData |  |
| 1581 | `RtlTraceDatabaseFind` | `0x1467A0` | 120 | UnwindData |  |
| 1582 | `RtlTraceDatabaseLock` | `0x146820` | 30 | UnwindData |  |
| 1583 | `RtlTraceDatabaseUnlock` | `0x146850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1584 | `RtlTraceDatabaseValidate` | `0x146870` | 50 | UnwindData |  |
| 1602 | `RtlUnicodeStringToUTF8String` | `0x146B90` | 277 | UnwindData |  |
| 1592 | `RtlUdiv128` | `0x146CB0` | 111 | UnwindData |  |
| 1654 | `RtlWakeAddressAllNoFence` | `0x146D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1656 | `RtlWakeAddressSingleNoFence` | `0x146D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1680 | `RtlWow64PopAllCrossProcessWorkFromWorkList` | `0x146D50` | 207 | UnwindData |  |
| 1681 | `RtlWow64PopCrossProcessWorkFromFreeList` | `0x146E30` | 184 | UnwindData |  |
| 1682 | `RtlWow64PushCrossProcessWorkOntoFreeList` | `0x146EF0` | 201 | UnwindData |  |
| 1683 | `RtlWow64PushCrossProcessWorkOntoWorkList` | `0x146FC0` | 648 | UnwindData |  |
| 1684 | `RtlWow64RequestCrossProcessHeavyFlush` | `0x147250` | 88 | UnwindData |  |
| 1730 | `RtlpRefreshCachedUILanguage` | `0x147F90` | 233 | UnwindData |  |
| 1721 | `RtlpNtCreateKey` | `0x1498D0` | 49 | UnwindData |  |
| 1723 | `RtlpNtMakeTemporaryKey` | `0x149910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1726 | `RtlpNtSetValueKey` | `0x149920` | 43 | UnwindData |  |
| 193 | `MD4Final` | `0x159DD0` | 301 | UnwindData |  |
| 194 | `MD4Init` | `0x159F10` | 138 | UnwindData |  |
| 195 | `MD4Update` | `0x159FA0` | 201 | UnwindData |  |
| 66 | `EtwEnumerateProcessRegGuids` | `0x15A120` | 203 | UnwindData |  |
| 88 | `EtwRegisterSecurityProvider` | `0x15A200` | 79 | UnwindData |  |
| 64 | `EtwCreateTraceInstanceId` | `0x15A3A0` | 73 | UnwindData |  |
| 93 | `EtwSetMark` | `0x15A3F0` | 36 | UnwindData |  |
| 94 | `EtwTraceEventInstance` | `0x15A420` | 448 | UnwindData |  |
| 101 | `EvtIntReportAuthzEventAndSourceAsync` | `0x15A7C0` | 106 | UnwindData |  |
| 1783 | `TpQueryPoolStackInformation` | `0x15A8D0` | 127 | UnwindData |  |
| 1764 | `TpCallbackDetectedUnrecoverableError` | `0x15A9E0` | 40 | UnwindData |  |
| 1768 | `TpCallbackReleaseMutexOnCompletion` | `0x15AA10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1769 | `TpCallbackReleaseSemaphoreOnCompletion` | `0x15AA50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1777 | `TpDbgDumpHeapUsage` | `0x15AA90` | 181 | UnwindData |  |
| 783 | `RtlCancelTimer` | `0x15ADE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `RtlDeleteTimerQueue` | `0x15ADF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1537 | `RtlSetTimer` | `0x15AE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1747 | `SbExecuteProcedure` | `0x15AE10` | 34 | UnwindData |  |
| 27 | `ApiSetGetImplementationHost` | `0x15C6F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `ApiSetQuerySchema` | `0x15C720` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `CsrSetPriorityClass` | `0x15C750` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `LdrGetFailureData` | `0x15CA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `LdrHotPatchNotify` | `0x15CA60` | 464 | UnwindData |  |
| 146 | `LdrIsModuleSxsRedirected` | `0x15CC40` | 58 | UnwindData |  |
| 159 | `LdrQueryModuleServiceTags` | `0x15CC80` | 161 | UnwindData |  |
| 177 | `LdrSetImplicitPathOptions` | `0x15CD30` | 100 | UnwindData |  |
| 189 | `LdrVerifyImageMatchesChecksum` | `0x15CDA0` | 147 | UnwindData |  |
| 1147 | `RtlGetUnloadEventTrace` | `0x15D1D0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `LdrResolveDelayLoadsFromDll` | `0x15D400` | 64 | UnwindData |  |
| 954 | `RtlDosLongPathNameToRelativeNtPathName_U_WithStatus` | `0x15D610` | 34 | UnwindData |  |
| 809 | `RtlCloneUserProcess` | `0x15D640` | 763 | UnwindData |  |
| 823 | `RtlCompleteProcessCloning` | `0x15D950` | 301 | UnwindData |  |
| 871 | `RtlCreateProcessParameters` | `0x15DA90` | 100 | UnwindData |  |
| 1358 | `RtlPrepareForProcessCloning` | `0x15DB00` | 284 | UnwindData |  |
| 1679 | `RtlWow64LogMessageInEventLogger` | `0x15DC30` | 30 | UnwindData |  |
| 903 | `RtlDecodeRemotePointer` | `0x15DC60` | 103 | UnwindData |  |
| 972 | `RtlEncodeRemotePointer` | `0x15DCD0` | 98 | UnwindData |  |
| 693 | `NtdllDefWindowProc_A` | `0x15FD20` | 6 | UnwindData |  |
| 694 | `NtdllDefWindowProc_W` | `0x15FD30` | 6 | UnwindData |  |
| 695 | `NtdllDialogWndProc_A` | `0x15FDE0` | 6 | UnwindData |  |
| 696 | `NtdllDialogWndProc_W` | `0x15FDF0` | 6 | UnwindData |  |
| 204 | `NtAccessCheck` | `0x160060` | 24 | UnwindData |  |
| 1852 | `ZwAccessCheck` | `0x160060` | 24 | UnwindData |  |
| 687 | `NtWorkerFactoryWorkerReady` | `0x160080` | 24 | UnwindData |  |
| 2334 | `ZwWorkerFactoryWorkerReady` | `0x160080` | 24 | UnwindData |  |
| 203 | `NtAcceptConnectPort` | `0x1600A0` | 24 | UnwindData |  |
| 1851 | `ZwAcceptConnectPort` | `0x1600A0` | 24 | UnwindData |  |
| 424 | `NtMapUserPhysicalPagesScatter` | `0x1600C0` | 24 | UnwindData |  |
| 2071 | `ZwMapUserPhysicalPagesScatter` | `0x1600C0` | 24 | UnwindData |  |
| 683 | `NtWaitForSingleObject` | `0x1600E0` | 24 | UnwindData |  |
| 2330 | `ZwWaitForSingleObject` | `0x1600E0` | 24 | UnwindData |  |
| 260 | `NtCallbackReturn` | `0x160100` | 24 | UnwindData |  |
| 1908 | `ZwCallbackReturn` | `0x160100` | 24 | UnwindData |  |
| 545 | `NtReadFile` | `0x160120` | 24 | UnwindData |  |
| 2192 | `ZwReadFile` | `0x160120` | 24 | UnwindData |  |
| 352 | `NtDeviceIoControlFile` | `0x160140` | 24 | UnwindData |  |
| 2000 | `ZwDeviceIoControlFile` | `0x160140` | 24 | UnwindData |  |
| 688 | `NtWriteFile` | `0x160160` | 24 | UnwindData |  |
| 2335 | `ZwWriteFile` | `0x160160` | 24 | UnwindData |  |
| 560 | `NtRemoveIoCompletion` | `0x160180` | 24 | UnwindData |  |
| 2207 | `ZwRemoveIoCompletion` | `0x160180` | 24 | UnwindData |  |
| 558 | `NtReleaseSemaphore` | `0x1601A0` | 24 | UnwindData |  |
| 2205 | `ZwReleaseSemaphore` | `0x1601A0` | 24 | UnwindData |  |
| 568 | `NtReplyWaitReceivePort` | `0x1601C0` | 24 | UnwindData |  |
| 2215 | `ZwReplyWaitReceivePort` | `0x1601C0` | 24 | UnwindData |  |
| 567 | `NtReplyPort` | `0x1601E0` | 24 | UnwindData |  |
| 2214 | `ZwReplyPort` | `0x1601E0` | 24 | UnwindData |  |
| 617 | `NtSetInformationThread` | `0x160200` | 24 | UnwindData |  |
| 2264 | `ZwSetInformationThread` | `0x160200` | 24 | UnwindData |  |
| 600 | `NtSetEvent` | `0x160220` | 24 | UnwindData |  |
| 2247 | `ZwSetEvent` | `0x160220` | 24 | UnwindData |  |
| 270 | `NtClose` | `0x160240` | 24 | UnwindData |  |
| 1918 | `ZwClose` | `0x160240` | 24 | UnwindData |  |
| 516 | `NtQueryObject` | `0x160260` | 24 | UnwindData |  |
| 2163 | `ZwQueryObject` | `0x160260` | 24 | UnwindData |  |
| 498 | `NtQueryInformationFile` | `0x160280` | 24 | UnwindData |  |
| 2145 | `ZwQueryInformationFile` | `0x160280` | 24 | UnwindData |  |
| 442 | `NtOpenKey` | `0x1602A0` | 24 | UnwindData |  |
| 2089 | `ZwOpenKey` | `0x1602A0` | 24 | UnwindData |  |
| 365 | `NtEnumerateValueKey` | `0x1602C0` | 24 | UnwindData |  |
| 2013 | `ZwEnumerateValueKey` | `0x1602C0` | 24 | UnwindData |  |
| 370 | `NtFindAtom` | `0x1602E0` | 24 | UnwindData |  |
| 2018 | `ZwFindAtom` | `0x1602E0` | 24 | UnwindData |  |
| 485 | `NtQueryDefaultLocale` | `0x160300` | 24 | UnwindData |  |
| 2132 | `ZwQueryDefaultLocale` | `0x160300` | 24 | UnwindData |  |
| 512 | `NtQueryKey` | `0x160320` | 24 | UnwindData |  |
| 2159 | `ZwQueryKey` | `0x160320` | 24 | UnwindData |  |
| 535 | `NtQueryValueKey` | `0x160340` | 24 | UnwindData |  |
| 2182 | `ZwQueryValueKey` | `0x160340` | 24 | UnwindData |  |
| 230 | `NtAllocateVirtualMemory` | `0x160360` | 24 | UnwindData |  |
| 1878 | `ZwAllocateVirtualMemory` | `0x160360` | 24 | UnwindData |  |
| 501 | `NtQueryInformationProcess` | `0x160380` | 24 | UnwindData |  |
| 2148 | `ZwQueryInformationProcess` | `0x160380` | 24 | UnwindData |  |
| 682 | `NtWaitForMultipleObjects32` | `0x1603A0` | 24 | UnwindData |  |
| 2329 | `ZwWaitForMultipleObjects32` | `0x1603A0` | 24 | UnwindData |  |
| 689 | `NtWriteFileGather` | `0x1603C0` | 24 | UnwindData |  |
| 2336 | `ZwWriteFileGather` | `0x1603C0` | 24 | UnwindData |  |
| 614 | `NtSetInformationProcess` | `0x1603E0` | 24 | UnwindData |  |
| 2261 | `ZwSetInformationProcess` | `0x1603E0` | 24 | UnwindData |  |
| 303 | `NtCreateKey` | `0x160400` | 24 | UnwindData |  |
| 1951 | `ZwCreateKey` | `0x160400` | 24 | UnwindData |  |
| 380 | `NtFreeVirtualMemory` | `0x160420` | 24 | UnwindData |  |
| 2028 | `ZwFreeVirtualMemory` | `0x160420` | 24 | UnwindData |  |
| 398 | `NtImpersonateClientOfPort` | `0x160440` | 24 | UnwindData |  |
| 2045 | `ZwImpersonateClientOfPort` | `0x160440` | 24 | UnwindData |  |
| 557 | `NtReleaseMutant` | `0x160460` | 24 | UnwindData |  |
| 2204 | `ZwReleaseMutant` | `0x160460` | 24 | UnwindData |  |
| 504 | `NtQueryInformationToken` | `0x160480` | 24 | UnwindData |  |
| 2151 | `ZwQueryInformationToken` | `0x160480` | 24 | UnwindData |  |
| 572 | `NtRequestWaitReplyPort` | `0x1604A0` | 24 | UnwindData |  |
| 2219 | `ZwRequestWaitReplyPort` | `0x1604A0` | 24 | UnwindData |  |
| 536 | `NtQueryVirtualMemory` | `0x1604C0` | 24 | UnwindData |  |
| 2183 | `ZwQueryVirtualMemory` | `0x1604C0` | 24 | UnwindData |  |
| 461 | `NtOpenThreadToken` | `0x1604E0` | 24 | UnwindData |  |
| 2108 | `ZwOpenThreadToken` | `0x1604E0` | 24 | UnwindData |  |
| 503 | `NtQueryInformationThread` | `0x160500` | 24 | UnwindData |  |
| 2150 | `ZwQueryInformationThread` | `0x160500` | 24 | UnwindData |  |
| 451 | `NtOpenProcess` | `0x160520` | 24 | UnwindData |  |
| 2098 | `ZwOpenProcess` | `0x160520` | 24 | UnwindData |  |
| 609 | `NtSetInformationFile` | `0x160540` | 24 | UnwindData |  |
| 2256 | `ZwSetInformationFile` | `0x160540` | 24 | UnwindData |  |
| 425 | `NtMapViewOfSection` | `0x160560` | 24 | UnwindData |  |
| 2072 | `ZwMapViewOfSection` | `0x160560` | 24 | UnwindData |  |
| 205 | `NtAccessCheckAndAuditAlarm` | `0x160580` | 24 | UnwindData |  |
| 1853 | `ZwAccessCheckAndAuditAlarm` | `0x160580` | 24 | UnwindData |  |
| 673 | `NtUnmapViewOfSection` | `0x1605A0` | 24 | UnwindData |  |
| 2320 | `ZwUnmapViewOfSection` | `0x1605A0` | 24 | UnwindData |  |
| 569 | `NtReplyWaitReceivePortEx` | `0x1605C0` | 24 | UnwindData |  |
| 2216 | `ZwReplyWaitReceivePortEx` | `0x1605C0` | 24 | UnwindData |  |
| 658 | `NtTerminateProcess` | `0x1605E0` | 24 | UnwindData |  |
| 2305 | `ZwTerminateProcess` | `0x1605E0` | 24 | UnwindData |  |
| 601 | `NtSetEventBoostPriority` | `0x160600` | 24 | UnwindData |  |
| 2248 | `ZwSetEventBoostPriority` | `0x160600` | 24 | UnwindData |  |
| 546 | `NtReadFileScatter` | `0x160620` | 24 | UnwindData |  |
| 2193 | `ZwReadFileScatter` | `0x160620` | 24 | UnwindData |  |
| 462 | `NtOpenThreadTokenEx` | `0x160640` | 24 | UnwindData |  |
| 2109 | `ZwOpenThreadTokenEx` | `0x160640` | 24 | UnwindData |  |
| 453 | `NtOpenProcessTokenEx` | `0x160660` | 24 | UnwindData |  |
| 2100 | `ZwOpenProcessTokenEx` | `0x160660` | 24 | UnwindData |  |
| 519 | `NtQueryPerformanceCounter` | `0x160680` | 24 | UnwindData |  |
| 2166 | `ZwQueryPerformanceCounter` | `0x160680` | 24 | UnwindData |  |
| 362 | `NtEnumerateKey` | `0x1606A0` | 24 | UnwindData |  |
| 2010 | `ZwEnumerateKey` | `0x1606A0` | 24 | UnwindData |  |
| 439 | `NtOpenFile` | `0x1606C0` | 24 | UnwindData |  |
| 2086 | `ZwOpenFile` | `0x1606C0` | 24 | UnwindData |  |
| 341 | `NtDelayExecution` | `0x1606E0` | 24 | UnwindData |  |
| 1989 | `ZwDelayExecution` | `0x1606E0` | 24 | UnwindData |  |
| 487 | `NtQueryDirectoryFile` | `0x160700` | 24 | UnwindData |  |
| 2134 | `ZwQueryDirectoryFile` | `0x160700` | 24 | UnwindData |  |
| 530 | `NtQuerySystemInformation` | `0x160720` | 24 | UnwindData |  |
| 1113 | `RtlGetNativeSystemInformation` | `0x160720` | 24 | UnwindData |  |
| 2177 | `ZwQuerySystemInformation` | `0x160720` | 24 | UnwindData |  |
| 456 | `NtOpenSection` | `0x160740` | 24 | UnwindData |  |
| 2103 | `ZwOpenSection` | `0x160740` | 24 | UnwindData |  |
| 533 | `NtQueryTimer` | `0x160760` | 24 | UnwindData |  |
| 2180 | `ZwQueryTimer` | `0x160760` | 24 | UnwindData |  |
| 383 | `NtFsControlFile` | `0x160780` | 24 | UnwindData |  |
| 2031 | `ZwFsControlFile` | `0x160780` | 24 | UnwindData |  |
| 691 | `NtWriteVirtualMemory` | `0x1607A0` | 24 | UnwindData |  |
| 2338 | `ZwWriteVirtualMemory` | `0x1607A0` | 24 | UnwindData |  |
| 271 | `NtCloseObjectAuditAlarm` | `0x1607C0` | 24 | UnwindData |  |
| 1919 | `ZwCloseObjectAuditAlarm` | `0x1607C0` | 24 | UnwindData |  |
| 357 | `NtDuplicateObject` | `0x1607E0` | 24 | UnwindData |  |
| 2005 | `ZwDuplicateObject` | `0x1607E0` | 24 | UnwindData |  |
| 480 | `NtQueryAttributesFile` | `0x160800` | 24 | UnwindData |  |
| 2127 | `ZwQueryAttributesFile` | `0x160800` | 24 | UnwindData |  |
| 269 | `NtClearEvent` | `0x160820` | 24 | UnwindData |  |
| 1917 | `ZwClearEvent` | `0x160820` | 24 | UnwindData |  |
| 549 | `NtReadVirtualMemory` | `0x160840` | 24 | UnwindData |  |
| 2196 | `ZwReadVirtualMemory` | `0x160840` | 24 | UnwindData |  |
| 437 | `NtOpenEvent` | `0x160860` | 24 | UnwindData |  |
| 2084 | `ZwOpenEvent` | `0x160860` | 24 | UnwindData |  |
| 218 | `NtAdjustPrivilegesToken` | `0x160880` | 24 | UnwindData |  |
| 1866 | `ZwAdjustPrivilegesToken` | `0x160880` | 24 | UnwindData |  |
| 358 | `NtDuplicateToken` | `0x1608A0` | 24 | UnwindData |  |
| 2006 | `ZwDuplicateToken` | `0x1608A0` | 24 | UnwindData |  |
| 283 | `NtContinue` | `0x1608C0` | 24 | UnwindData |  |
| 1931 | `ZwContinue` | `0x1608C0` | 24 | UnwindData |  |
| 486 | `NtQueryDefaultUILanguage` | `0x1608E0` | 24 | UnwindData |  |
| 2133 | `ZwQueryDefaultUILanguage` | `0x1608E0` | 24 | UnwindData |  |
| 540 | `NtQueueApcThread` | `0x160900` | 24 | UnwindData |  |
| 2187 | `ZwQueueApcThread` | `0x160900` | 24 | UnwindData |  |
| 692 | `NtYieldExecution` | `0x160920` | 24 | UnwindData |  |
| 2339 | `ZwYieldExecution` | `0x160920` | 24 | UnwindData |  |
| 213 | `NtAddAtom` | `0x160940` | 24 | UnwindData |  |
| 1861 | `ZwAddAtom` | `0x160940` | 24 | UnwindData |  |
| 295 | `NtCreateEvent` | `0x160960` | 24 | UnwindData |  |
| 1943 | `ZwCreateEvent` | `0x160960` | 24 | UnwindData |  |
| 537 | `NtQueryVolumeInformationFile` | `0x160980` | 24 | UnwindData |  |
| 2184 | `ZwQueryVolumeInformationFile` | `0x160980` | 24 | UnwindData |  |
| 321 | `NtCreateSection` | `0x1609A0` | 24 | UnwindData |  |
| 1969 | `ZwCreateSection` | `0x1609A0` | 24 | UnwindData |  |
| 371 | `NtFlushBuffersFile` | `0x1609C0` | 24 | UnwindData |  |
| 2019 | `ZwFlushBuffersFile` | `0x1609C0` | 24 | UnwindData |  |
| 255 | `NtApphelpCacheControl` | `0x1609E0` | 24 | UnwindData |  |
| 1903 | `ZwApphelpCacheControl` | `0x1609E0` | 24 | UnwindData |  |
| 315 | `NtCreateProcessEx` | `0x160A00` | 24 | UnwindData |  |
| 1963 | `ZwCreateProcessEx` | `0x160A00` | 24 | UnwindData |  |
| 325 | `NtCreateThread` | `0x160A20` | 24 | UnwindData |  |
| 1973 | `ZwCreateThread` | `0x160A20` | 24 | UnwindData |  |
| 404 | `NtIsProcessInJob` | `0x160A40` | 24 | UnwindData |  |
| 2051 | `ZwIsProcessInJob` | `0x160A40` | 24 | UnwindData |  |
| 477 | `NtProtectVirtualMemory` | `0x160A60` | 24 | UnwindData |  |
| 2124 | `ZwProtectVirtualMemory` | `0x160A60` | 24 | UnwindData |  |
| 522 | `NtQuerySection` | `0x160A80` | 24 | UnwindData |  |
| 2169 | `ZwQuerySection` | `0x160A80` | 24 | UnwindData |  |
| 577 | `NtResumeThread` | `0x160AA0` | 24 | UnwindData |  |
| 2224 | `ZwResumeThread` | `0x160AA0` | 24 | UnwindData |  |
| 659 | `NtTerminateThread` | `0x160AC0` | 24 | UnwindData |  |
| 2306 | `ZwTerminateThread` | `0x160AC0` | 24 | UnwindData |  |
| 548 | `NtReadRequestData` | `0x160AE0` | 24 | UnwindData |  |
| 2195 | `ZwReadRequestData` | `0x160AE0` | 24 | UnwindData |  |
| 297 | `NtCreateFile` | `0x160B00` | 24 | UnwindData |  |
| 1945 | `ZwCreateFile` | `0x160B00` | 24 | UnwindData |  |
| 492 | `NtQueryEvent` | `0x160B20` | 24 | UnwindData |  |
| 2139 | `ZwQueryEvent` | `0x160B20` | 24 | UnwindData |  |
| 690 | `NtWriteRequestData` | `0x160B40` | 24 | UnwindData |  |
| 2337 | `ZwWriteRequestData` | `0x160B40` | 24 | UnwindData |  |
| 435 | `NtOpenDirectoryObject` | `0x160B60` | 24 | UnwindData |  |
| 2082 | `ZwOpenDirectoryObject` | `0x160B60` | 24 | UnwindData |  |
| 207 | `NtAccessCheckByTypeAndAuditAlarm` | `0x160B80` | 24 | UnwindData |  |
| 1855 | `ZwAccessCheckByTypeAndAuditAlarm` | `0x160B80` | 24 | UnwindData |  |
| 532 | `NtQuerySystemTime` | `0x160BA0` | 5 | UnwindData |  |
| 2179 | `ZwQuerySystemTime` | `0x160BA0` | 5 | UnwindData |  |
| 681 | `NtWaitForMultipleObjects` | `0x160BB0` | 24 | UnwindData |  |
| 2328 | `ZwWaitForMultipleObjects` | `0x160BB0` | 24 | UnwindData |  |
| 613 | `NtSetInformationObject` | `0x160BD0` | 24 | UnwindData |  |
| 2260 | `ZwSetInformationObject` | `0x160BD0` | 24 | UnwindData |  |
| 261 | `NtCancelIoFile` | `0x160BF0` | 24 | UnwindData |  |
| 1909 | `ZwCancelIoFile` | `0x160BF0` | 24 | UnwindData |  |
| 664 | `NtTraceEvent` | `0x160C10` | 24 | UnwindData |  |
| 2311 | `ZwTraceEvent` | `0x160C10` | 24 | UnwindData |  |
| 467 | `NtPowerInformation` | `0x160C30` | 24 | UnwindData |  |
| 2114 | `ZwPowerInformation` | `0x160C30` | 24 | UnwindData |  |
| 642 | `NtSetValueKey` | `0x160C50` | 24 | UnwindData |  |
| 2289 | `ZwSetValueKey` | `0x160C50` | 24 | UnwindData |  |
| 264 | `NtCancelTimer` | `0x160C70` | 24 | UnwindData |  |
| 1912 | `ZwCancelTimer` | `0x160C70` | 24 | UnwindData |  |
| 637 | `NtSetTimer` | `0x160C90` | 24 | UnwindData |  |
| 2284 | `ZwSetTimer` | `0x160C90` | 24 | UnwindData |  |
| 206 | `NtAccessCheckByType` | `0x160CB0` | 24 | UnwindData |  |
| 1854 | `ZwAccessCheckByType` | `0x160CB0` | 24 | UnwindData |  |
| 208 | `NtAccessCheckByTypeResultList` | `0x160CD0` | 24 | UnwindData |  |
| 1856 | `ZwAccessCheckByTypeResultList` | `0x160CD0` | 24 | UnwindData |  |
| 209 | `NtAccessCheckByTypeResultListAndAuditAlarm` | `0x160CF0` | 24 | UnwindData |  |
| 1857 | `ZwAccessCheckByTypeResultListAndAuditAlarm` | `0x160CF0` | 24 | UnwindData |  |
| 210 | `NtAccessCheckByTypeResultListAndAuditAlarmByHandle` | `0x160D10` | 24 | UnwindData |  |
| 1858 | `ZwAccessCheckByTypeResultListAndAuditAlarmByHandle` | `0x160D10` | 24 | UnwindData |  |
| 211 | `NtAcquireCrossVmMutant` | `0x160D30` | 24 | UnwindData |  |
| 1859 | `ZwAcquireCrossVmMutant` | `0x160D30` | 24 | UnwindData |  |
| 212 | `NtAcquireProcessActivityReference` | `0x160D50` | 24 | UnwindData |  |
| 1860 | `ZwAcquireProcessActivityReference` | `0x160D50` | 24 | UnwindData |  |
| 214 | `NtAddAtomEx` | `0x160D70` | 24 | UnwindData |  |
| 1862 | `ZwAddAtomEx` | `0x160D70` | 24 | UnwindData |  |
| 215 | `NtAddBootEntry` | `0x160D90` | 24 | UnwindData |  |
| 1863 | `ZwAddBootEntry` | `0x160D90` | 24 | UnwindData |  |
| 216 | `NtAddDriverEntry` | `0x160DB0` | 24 | UnwindData |  |
| 1864 | `ZwAddDriverEntry` | `0x160DB0` | 24 | UnwindData |  |
| 217 | `NtAdjustGroupsToken` | `0x160DD0` | 24 | UnwindData |  |
| 1865 | `ZwAdjustGroupsToken` | `0x160DD0` | 24 | UnwindData |  |
| 219 | `NtAdjustTokenClaimsAndDeviceGroups` | `0x160DF0` | 24 | UnwindData |  |
| 1867 | `ZwAdjustTokenClaimsAndDeviceGroups` | `0x160DF0` | 24 | UnwindData |  |
| 220 | `NtAlertMultipleThreadByThreadId` | `0x160E10` | 24 | UnwindData |  |
| 1868 | `ZwAlertMultipleThreadByThreadId` | `0x160E10` | 24 | UnwindData |  |
| 221 | `NtAlertResumeThread` | `0x160E30` | 24 | UnwindData |  |
| 1869 | `ZwAlertResumeThread` | `0x160E30` | 24 | UnwindData |  |
| 222 | `NtAlertThread` | `0x160E50` | 24 | UnwindData |  |
| 1870 | `ZwAlertThread` | `0x160E50` | 24 | UnwindData |  |
| 223 | `NtAlertThreadByThreadId` | `0x160E70` | 24 | UnwindData |  |
| 1871 | `ZwAlertThreadByThreadId` | `0x160E70` | 24 | UnwindData |  |
| 224 | `NtAlertThreadByThreadIdEx` | `0x160E90` | 24 | UnwindData |  |
| 1872 | `ZwAlertThreadByThreadIdEx` | `0x160E90` | 24 | UnwindData |  |
| 225 | `NtAllocateLocallyUniqueId` | `0x160EB0` | 24 | UnwindData |  |
| 1873 | `ZwAllocateLocallyUniqueId` | `0x160EB0` | 24 | UnwindData |  |
| 226 | `NtAllocateReserveObject` | `0x160ED0` | 24 | UnwindData |  |
| 1874 | `ZwAllocateReserveObject` | `0x160ED0` | 24 | UnwindData |  |
| 227 | `NtAllocateUserPhysicalPages` | `0x160EF0` | 24 | UnwindData |  |
| 1875 | `ZwAllocateUserPhysicalPages` | `0x160EF0` | 24 | UnwindData |  |
| 228 | `NtAllocateUserPhysicalPagesEx` | `0x160F10` | 24 | UnwindData |  |
| 1876 | `ZwAllocateUserPhysicalPagesEx` | `0x160F10` | 24 | UnwindData |  |
| 229 | `NtAllocateUuids` | `0x160F30` | 24 | UnwindData |  |
| 1877 | `ZwAllocateUuids` | `0x160F30` | 24 | UnwindData |  |
| 231 | `NtAllocateVirtualMemoryEx` | `0x160F50` | 24 | UnwindData |  |
| 1879 | `ZwAllocateVirtualMemoryEx` | `0x160F50` | 24 | UnwindData |  |
| 232 | `NtAlpcAcceptConnectPort` | `0x160F70` | 24 | UnwindData |  |
| 1880 | `ZwAlpcAcceptConnectPort` | `0x160F70` | 24 | UnwindData |  |
| 233 | `NtAlpcCancelMessage` | `0x160F90` | 24 | UnwindData |  |
| 1881 | `ZwAlpcCancelMessage` | `0x160F90` | 24 | UnwindData |  |
| 234 | `NtAlpcConnectPort` | `0x160FB0` | 24 | UnwindData |  |
| 1882 | `ZwAlpcConnectPort` | `0x160FB0` | 24 | UnwindData |  |
| 235 | `NtAlpcConnectPortEx` | `0x160FD0` | 24 | UnwindData |  |
| 1883 | `ZwAlpcConnectPortEx` | `0x160FD0` | 24 | UnwindData |  |
| 236 | `NtAlpcCreatePort` | `0x160FF0` | 24 | UnwindData |  |
| 1884 | `ZwAlpcCreatePort` | `0x160FF0` | 24 | UnwindData |  |
| 237 | `NtAlpcCreatePortSection` | `0x161010` | 24 | UnwindData |  |
| 1885 | `ZwAlpcCreatePortSection` | `0x161010` | 24 | UnwindData |  |
| 238 | `NtAlpcCreateResourceReserve` | `0x161030` | 24 | UnwindData |  |
| 1886 | `ZwAlpcCreateResourceReserve` | `0x161030` | 24 | UnwindData |  |
| 239 | `NtAlpcCreateSectionView` | `0x161050` | 24 | UnwindData |  |
| 1887 | `ZwAlpcCreateSectionView` | `0x161050` | 24 | UnwindData |  |
| 240 | `NtAlpcCreateSecurityContext` | `0x161070` | 24 | UnwindData |  |
| 1888 | `ZwAlpcCreateSecurityContext` | `0x161070` | 24 | UnwindData |  |
| 241 | `NtAlpcDeletePortSection` | `0x161090` | 24 | UnwindData |  |
| 1889 | `ZwAlpcDeletePortSection` | `0x161090` | 24 | UnwindData |  |
| 242 | `NtAlpcDeleteResourceReserve` | `0x1610B0` | 24 | UnwindData |  |
| 1890 | `ZwAlpcDeleteResourceReserve` | `0x1610B0` | 24 | UnwindData |  |
| 243 | `NtAlpcDeleteSectionView` | `0x1610D0` | 24 | UnwindData |  |
| 1891 | `ZwAlpcDeleteSectionView` | `0x1610D0` | 24 | UnwindData |  |
| 244 | `NtAlpcDeleteSecurityContext` | `0x1610F0` | 24 | UnwindData |  |
| 1892 | `ZwAlpcDeleteSecurityContext` | `0x1610F0` | 24 | UnwindData |  |
| 245 | `NtAlpcDisconnectPort` | `0x161110` | 24 | UnwindData |  |
| 1893 | `ZwAlpcDisconnectPort` | `0x161110` | 24 | UnwindData |  |
| 246 | `NtAlpcImpersonateClientContainerOfPort` | `0x161130` | 24 | UnwindData |  |
| 1894 | `ZwAlpcImpersonateClientContainerOfPort` | `0x161130` | 24 | UnwindData |  |
| 247 | `NtAlpcImpersonateClientOfPort` | `0x161150` | 24 | UnwindData |  |
| 1895 | `ZwAlpcImpersonateClientOfPort` | `0x161150` | 24 | UnwindData |  |
| 248 | `NtAlpcOpenSenderProcess` | `0x161170` | 24 | UnwindData |  |
| 1896 | `ZwAlpcOpenSenderProcess` | `0x161170` | 24 | UnwindData |  |
| 249 | `NtAlpcOpenSenderThread` | `0x161190` | 24 | UnwindData |  |
| 1897 | `ZwAlpcOpenSenderThread` | `0x161190` | 24 | UnwindData |  |
| 250 | `NtAlpcQueryInformation` | `0x1611B0` | 24 | UnwindData |  |
| 1898 | `ZwAlpcQueryInformation` | `0x1611B0` | 24 | UnwindData |  |
| 251 | `NtAlpcQueryInformationMessage` | `0x1611D0` | 24 | UnwindData |  |
| 1899 | `ZwAlpcQueryInformationMessage` | `0x1611D0` | 24 | UnwindData |  |
| 252 | `NtAlpcRevokeSecurityContext` | `0x1611F0` | 24 | UnwindData |  |
| 1900 | `ZwAlpcRevokeSecurityContext` | `0x1611F0` | 24 | UnwindData |  |
| 253 | `NtAlpcSendWaitReceivePort` | `0x161210` | 24 | UnwindData |  |
| 1901 | `ZwAlpcSendWaitReceivePort` | `0x161210` | 24 | UnwindData |  |
| 254 | `NtAlpcSetInformation` | `0x161230` | 24 | UnwindData |  |
| 1902 | `ZwAlpcSetInformation` | `0x161230` | 24 | UnwindData |  |
| 256 | `NtAreMappedFilesTheSame` | `0x161250` | 24 | UnwindData |  |
| 1904 | `ZwAreMappedFilesTheSame` | `0x161250` | 24 | UnwindData |  |
| 257 | `NtAssignProcessToJobObject` | `0x161270` | 24 | UnwindData |  |
| 1905 | `ZwAssignProcessToJobObject` | `0x161270` | 24 | UnwindData |  |
| 258 | `NtAssociateWaitCompletionPacket` | `0x161290` | 24 | UnwindData |  |
| 1906 | `ZwAssociateWaitCompletionPacket` | `0x161290` | 24 | UnwindData |  |
| 259 | `NtCallEnclave` | `0x1612B0` | 24 | UnwindData |  |
| 1907 | `ZwCallEnclave` | `0x1612B0` | 24 | UnwindData |  |
| 262 | `NtCancelIoFileEx` | `0x1612D0` | 24 | UnwindData |  |
| 1910 | `ZwCancelIoFileEx` | `0x1612D0` | 24 | UnwindData |  |
| 263 | `NtCancelSynchronousIoFile` | `0x1612F0` | 24 | UnwindData |  |
| 1911 | `ZwCancelSynchronousIoFile` | `0x1612F0` | 24 | UnwindData |  |
| 265 | `NtCancelTimer2` | `0x161310` | 24 | UnwindData |  |
| 1913 | `ZwCancelTimer2` | `0x161310` | 24 | UnwindData |  |
| 266 | `NtCancelWaitCompletionPacket` | `0x161330` | 24 | UnwindData |  |
| 1914 | `ZwCancelWaitCompletionPacket` | `0x161330` | 24 | UnwindData |  |
| 267 | `NtChangeProcessState` | `0x161350` | 24 | UnwindData |  |
| 1915 | `ZwChangeProcessState` | `0x161350` | 24 | UnwindData |  |
| 268 | `NtChangeThreadState` | `0x161370` | 24 | UnwindData |  |
| 1916 | `ZwChangeThreadState` | `0x161370` | 24 | UnwindData |  |
| 272 | `NtCommitComplete` | `0x161390` | 24 | UnwindData |  |
| 1920 | `ZwCommitComplete` | `0x161390` | 24 | UnwindData |  |
| 273 | `NtCommitEnlistment` | `0x1613B0` | 24 | UnwindData |  |
| 1921 | `ZwCommitEnlistment` | `0x1613B0` | 24 | UnwindData |  |
| 274 | `NtCommitRegistryTransaction` | `0x1613D0` | 24 | UnwindData |  |
| 1922 | `ZwCommitRegistryTransaction` | `0x1613D0` | 24 | UnwindData |  |
| 275 | `NtCommitTransaction` | `0x1613F0` | 24 | UnwindData |  |
| 1923 | `ZwCommitTransaction` | `0x1613F0` | 24 | UnwindData |  |
| 276 | `NtCompactKeys` | `0x161410` | 24 | UnwindData |  |
| 1924 | `ZwCompactKeys` | `0x161410` | 24 | UnwindData |  |
| 277 | `NtCompareObjects` | `0x161430` | 24 | UnwindData |  |
| 1925 | `ZwCompareObjects` | `0x161430` | 24 | UnwindData |  |
| 278 | `NtCompareSigningLevels` | `0x161450` | 24 | UnwindData |  |
| 1926 | `ZwCompareSigningLevels` | `0x161450` | 24 | UnwindData |  |
| 279 | `NtCompareTokens` | `0x161470` | 24 | UnwindData |  |
| 1927 | `ZwCompareTokens` | `0x161470` | 24 | UnwindData |  |
| 280 | `NtCompleteConnectPort` | `0x161490` | 24 | UnwindData |  |
| 1928 | `ZwCompleteConnectPort` | `0x161490` | 24 | UnwindData |  |
| 281 | `NtCompressKey` | `0x1614B0` | 24 | UnwindData |  |
| 1929 | `ZwCompressKey` | `0x1614B0` | 24 | UnwindData |  |
| 282 | `NtConnectPort` | `0x1614D0` | 24 | UnwindData |  |
| 1930 | `ZwConnectPort` | `0x1614D0` | 24 | UnwindData |  |
| 284 | `NtContinueEx` | `0x1614F0` | 24 | UnwindData |  |
| 1932 | `ZwContinueEx` | `0x1614F0` | 24 | UnwindData |  |
| 285 | `NtConvertBetweenAuxiliaryCounterAndPerformanceCounter` | `0x161510` | 24 | UnwindData |  |
| 1933 | `ZwConvertBetweenAuxiliaryCounterAndPerformanceCounter` | `0x161510` | 24 | UnwindData |  |
| 286 | `NtCopyFileChunk` | `0x161530` | 24 | UnwindData |  |
| 1934 | `ZwCopyFileChunk` | `0x161530` | 24 | UnwindData |  |
| 287 | `NtCreateCpuPartition` | `0x161550` | 24 | UnwindData |  |
| 1935 | `ZwCreateCpuPartition` | `0x161550` | 24 | UnwindData |  |
| 288 | `NtCreateCrossVmEvent` | `0x161570` | 24 | UnwindData |  |
| 1936 | `ZwCreateCrossVmEvent` | `0x161570` | 24 | UnwindData |  |
| 289 | `NtCreateCrossVmMutant` | `0x161590` | 24 | UnwindData |  |
| 1937 | `ZwCreateCrossVmMutant` | `0x161590` | 24 | UnwindData |  |
| 290 | `NtCreateDebugObject` | `0x1615B0` | 24 | UnwindData |  |
| 1938 | `ZwCreateDebugObject` | `0x1615B0` | 24 | UnwindData |  |
| 291 | `NtCreateDirectoryObject` | `0x1615D0` | 24 | UnwindData |  |
| 1939 | `ZwCreateDirectoryObject` | `0x1615D0` | 24 | UnwindData |  |
| 292 | `NtCreateDirectoryObjectEx` | `0x1615F0` | 24 | UnwindData |  |
| 1940 | `ZwCreateDirectoryObjectEx` | `0x1615F0` | 24 | UnwindData |  |
| 293 | `NtCreateEnclave` | `0x161610` | 24 | UnwindData |  |
| 1941 | `ZwCreateEnclave` | `0x161610` | 24 | UnwindData |  |
| 294 | `NtCreateEnlistment` | `0x161630` | 24 | UnwindData |  |
| 1942 | `ZwCreateEnlistment` | `0x161630` | 24 | UnwindData |  |
| 296 | `NtCreateEventPair` | `0x161650` | 24 | UnwindData |  |
| 1944 | `ZwCreateEventPair` | `0x161650` | 24 | UnwindData |  |
| 298 | `NtCreateIRTimer` | `0x161670` | 24 | UnwindData |  |
| 1946 | `ZwCreateIRTimer` | `0x161670` | 24 | UnwindData |  |
| 299 | `NtCreateIoCompletion` | `0x161690` | 24 | UnwindData |  |
| 1947 | `ZwCreateIoCompletion` | `0x161690` | 24 | UnwindData |  |
| 300 | `NtCreateIoRing` | `0x1616B0` | 24 | UnwindData |  |
| 1948 | `ZwCreateIoRing` | `0x1616B0` | 24 | UnwindData |  |
| 301 | `NtCreateJobObject` | `0x1616D0` | 24 | UnwindData |  |
| 1949 | `ZwCreateJobObject` | `0x1616D0` | 24 | UnwindData |  |
| 302 | `NtCreateJobSet` | `0x1616F0` | 24 | UnwindData |  |
| 1950 | `ZwCreateJobSet` | `0x1616F0` | 24 | UnwindData |  |
| 304 | `NtCreateKeyTransacted` | `0x161710` | 24 | UnwindData |  |
| 1952 | `ZwCreateKeyTransacted` | `0x161710` | 24 | UnwindData |  |
| 305 | `NtCreateKeyedEvent` | `0x161730` | 24 | UnwindData |  |
| 1953 | `ZwCreateKeyedEvent` | `0x161730` | 24 | UnwindData |  |
| 306 | `NtCreateLowBoxToken` | `0x161750` | 24 | UnwindData |  |
| 1954 | `ZwCreateLowBoxToken` | `0x161750` | 24 | UnwindData |  |
| 307 | `NtCreateMailslotFile` | `0x161770` | 24 | UnwindData |  |
| 1955 | `ZwCreateMailslotFile` | `0x161770` | 24 | UnwindData |  |
| 308 | `NtCreateMutant` | `0x161790` | 24 | UnwindData |  |
| 1956 | `ZwCreateMutant` | `0x161790` | 24 | UnwindData |  |
| 309 | `NtCreateNamedPipeFile` | `0x1617B0` | 24 | UnwindData |  |
| 1957 | `ZwCreateNamedPipeFile` | `0x1617B0` | 24 | UnwindData |  |
| 310 | `NtCreatePagingFile` | `0x1617D0` | 24 | UnwindData |  |
| 1958 | `ZwCreatePagingFile` | `0x1617D0` | 24 | UnwindData |  |
| 311 | `NtCreatePartition` | `0x1617F0` | 24 | UnwindData |  |
| 1959 | `ZwCreatePartition` | `0x1617F0` | 24 | UnwindData |  |
| 312 | `NtCreatePort` | `0x161810` | 24 | UnwindData |  |
| 1960 | `ZwCreatePort` | `0x161810` | 24 | UnwindData |  |
| 313 | `NtCreatePrivateNamespace` | `0x161830` | 24 | UnwindData |  |
| 1961 | `ZwCreatePrivateNamespace` | `0x161830` | 24 | UnwindData |  |
| 314 | `NtCreateProcess` | `0x161850` | 24 | UnwindData |  |
| 1962 | `ZwCreateProcess` | `0x161850` | 24 | UnwindData |  |
| 316 | `NtCreateProcessStateChange` | `0x161870` | 24 | UnwindData |  |
| 1964 | `ZwCreateProcessStateChange` | `0x161870` | 24 | UnwindData |  |
| 317 | `NtCreateProfile` | `0x161890` | 24 | UnwindData |  |
| 1965 | `ZwCreateProfile` | `0x161890` | 24 | UnwindData |  |
| 318 | `NtCreateProfileEx` | `0x1618B0` | 24 | UnwindData |  |
| 1966 | `ZwCreateProfileEx` | `0x1618B0` | 24 | UnwindData |  |
| 319 | `NtCreateRegistryTransaction` | `0x1618D0` | 24 | UnwindData |  |
| 1967 | `ZwCreateRegistryTransaction` | `0x1618D0` | 24 | UnwindData |  |
| 320 | `NtCreateResourceManager` | `0x1618F0` | 24 | UnwindData |  |
| 1968 | `ZwCreateResourceManager` | `0x1618F0` | 24 | UnwindData |  |
| 322 | `NtCreateSectionEx` | `0x161910` | 24 | UnwindData |  |
| 1970 | `ZwCreateSectionEx` | `0x161910` | 24 | UnwindData |  |
| 323 | `NtCreateSemaphore` | `0x161930` | 24 | UnwindData |  |
| 1971 | `ZwCreateSemaphore` | `0x161930` | 24 | UnwindData |  |
| 324 | `NtCreateSymbolicLinkObject` | `0x161950` | 24 | UnwindData |  |
| 1972 | `ZwCreateSymbolicLinkObject` | `0x161950` | 24 | UnwindData |  |
| 326 | `NtCreateThreadEx` | `0x161970` | 24 | UnwindData |  |
| 1974 | `ZwCreateThreadEx` | `0x161970` | 24 | UnwindData |  |
| 327 | `NtCreateThreadStateChange` | `0x161990` | 24 | UnwindData |  |
| 1975 | `ZwCreateThreadStateChange` | `0x161990` | 24 | UnwindData |  |
| 328 | `NtCreateTimer` | `0x1619B0` | 24 | UnwindData |  |
| 1976 | `ZwCreateTimer` | `0x1619B0` | 24 | UnwindData |  |
| 329 | `NtCreateTimer2` | `0x1619D0` | 24 | UnwindData |  |
| 1977 | `ZwCreateTimer2` | `0x1619D0` | 24 | UnwindData |  |
| 330 | `NtCreateToken` | `0x1619F0` | 24 | UnwindData |  |
| 1978 | `ZwCreateToken` | `0x1619F0` | 24 | UnwindData |  |
| 331 | `NtCreateTokenEx` | `0x161A10` | 24 | UnwindData |  |
| 1979 | `ZwCreateTokenEx` | `0x161A10` | 24 | UnwindData |  |
| 332 | `NtCreateTransaction` | `0x161A30` | 24 | UnwindData |  |
| 1980 | `ZwCreateTransaction` | `0x161A30` | 24 | UnwindData |  |
| 333 | `NtCreateTransactionManager` | `0x161A50` | 24 | UnwindData |  |
| 1981 | `ZwCreateTransactionManager` | `0x161A50` | 24 | UnwindData |  |
| 334 | `NtCreateUserProcess` | `0x161A70` | 24 | UnwindData |  |
| 1982 | `ZwCreateUserProcess` | `0x161A70` | 24 | UnwindData |  |
| 335 | `NtCreateWaitCompletionPacket` | `0x161A90` | 24 | UnwindData |  |
| 1983 | `ZwCreateWaitCompletionPacket` | `0x161A90` | 24 | UnwindData |  |
| 336 | `NtCreateWaitablePort` | `0x161AB0` | 24 | UnwindData |  |
| 1984 | `ZwCreateWaitablePort` | `0x161AB0` | 24 | UnwindData |  |
| 337 | `NtCreateWnfStateName` | `0x161AD0` | 24 | UnwindData |  |
| 1985 | `ZwCreateWnfStateName` | `0x161AD0` | 24 | UnwindData |  |
| 338 | `NtCreateWorkerFactory` | `0x161AF0` | 24 | UnwindData |  |
| 1986 | `ZwCreateWorkerFactory` | `0x161AF0` | 24 | UnwindData |  |
| 339 | `NtDebugActiveProcess` | `0x161B10` | 24 | UnwindData |  |
| 1987 | `ZwDebugActiveProcess` | `0x161B10` | 24 | UnwindData |  |
| 340 | `NtDebugContinue` | `0x161B30` | 24 | UnwindData |  |
| 1988 | `ZwDebugContinue` | `0x161B30` | 24 | UnwindData |  |
| 342 | `NtDeleteAtom` | `0x161B50` | 24 | UnwindData |  |
| 1990 | `ZwDeleteAtom` | `0x161B50` | 24 | UnwindData |  |
| 343 | `NtDeleteBootEntry` | `0x161B70` | 24 | UnwindData |  |
| 1991 | `ZwDeleteBootEntry` | `0x161B70` | 24 | UnwindData |  |
| 344 | `NtDeleteDriverEntry` | `0x161B90` | 24 | UnwindData |  |
| 1992 | `ZwDeleteDriverEntry` | `0x161B90` | 24 | UnwindData |  |
| 345 | `NtDeleteFile` | `0x161BB0` | 24 | UnwindData |  |
| 1993 | `ZwDeleteFile` | `0x161BB0` | 24 | UnwindData |  |
| 346 | `NtDeleteKey` | `0x161BD0` | 24 | UnwindData |  |
| 1994 | `ZwDeleteKey` | `0x161BD0` | 24 | UnwindData |  |
| 347 | `NtDeleteObjectAuditAlarm` | `0x161BF0` | 24 | UnwindData |  |
| 1995 | `ZwDeleteObjectAuditAlarm` | `0x161BF0` | 24 | UnwindData |  |
| 348 | `NtDeletePrivateNamespace` | `0x161C10` | 24 | UnwindData |  |
| 1996 | `ZwDeletePrivateNamespace` | `0x161C10` | 24 | UnwindData |  |
| 349 | `NtDeleteValueKey` | `0x161C30` | 24 | UnwindData |  |
| 1997 | `ZwDeleteValueKey` | `0x161C30` | 24 | UnwindData |  |
| 350 | `NtDeleteWnfStateData` | `0x161C50` | 24 | UnwindData |  |
| 1998 | `ZwDeleteWnfStateData` | `0x161C50` | 24 | UnwindData |  |
| 351 | `NtDeleteWnfStateName` | `0x161C70` | 24 | UnwindData |  |
| 1999 | `ZwDeleteWnfStateName` | `0x161C70` | 24 | UnwindData |  |
| 353 | `NtDirectGraphicsCall` | `0x161C90` | 24 | UnwindData |  |
| 2001 | `ZwDirectGraphicsCall` | `0x161C90` | 24 | UnwindData |  |
| 354 | `NtDisableLastKnownGood` | `0x161CB0` | 24 | UnwindData |  |
| 2002 | `ZwDisableLastKnownGood` | `0x161CB0` | 24 | UnwindData |  |
| 355 | `NtDisplayString` | `0x161CD0` | 24 | UnwindData |  |
| 2003 | `ZwDisplayString` | `0x161CD0` | 24 | UnwindData |  |
| 356 | `NtDrawText` | `0x161CF0` | 24 | UnwindData |  |
| 2004 | `ZwDrawText` | `0x161CF0` | 24 | UnwindData |  |
| 359 | `NtEnableLastKnownGood` | `0x161D10` | 24 | UnwindData |  |
| 2007 | `ZwEnableLastKnownGood` | `0x161D10` | 24 | UnwindData |  |
| 360 | `NtEnumerateBootEntries` | `0x161D30` | 24 | UnwindData |  |
| 2008 | `ZwEnumerateBootEntries` | `0x161D30` | 24 | UnwindData |  |
| 361 | `NtEnumerateDriverEntries` | `0x161D50` | 24 | UnwindData |  |
| 2009 | `ZwEnumerateDriverEntries` | `0x161D50` | 24 | UnwindData |  |
| 363 | `NtEnumerateSystemEnvironmentValuesEx` | `0x161D70` | 24 | UnwindData |  |
| 2011 | `ZwEnumerateSystemEnvironmentValuesEx` | `0x161D70` | 24 | UnwindData |  |
| 364 | `NtEnumerateTransactionObject` | `0x161D90` | 24 | UnwindData |  |
| 2012 | `ZwEnumerateTransactionObject` | `0x161D90` | 24 | UnwindData |  |
| 366 | `NtExtendSection` | `0x161DB0` | 24 | UnwindData |  |
| 2014 | `ZwExtendSection` | `0x161DB0` | 24 | UnwindData |  |
| 367 | `NtFilterBootOption` | `0x161DD0` | 24 | UnwindData |  |
| 2015 | `ZwFilterBootOption` | `0x161DD0` | 24 | UnwindData |  |
| 368 | `NtFilterToken` | `0x161DF0` | 24 | UnwindData |  |
| 2016 | `ZwFilterToken` | `0x161DF0` | 24 | UnwindData |  |
| 369 | `NtFilterTokenEx` | `0x161E10` | 24 | UnwindData |  |
| 2017 | `ZwFilterTokenEx` | `0x161E10` | 24 | UnwindData |  |
| 372 | `NtFlushBuffersFileEx` | `0x161E30` | 24 | UnwindData |  |
| 2020 | `ZwFlushBuffersFileEx` | `0x161E30` | 24 | UnwindData |  |
| 373 | `NtFlushInstallUILanguage` | `0x161E50` | 24 | UnwindData |  |
| 2021 | `ZwFlushInstallUILanguage` | `0x161E50` | 24 | UnwindData |  |
| 374 | `NtFlushInstructionCache` | `0x161E70` | 24 | UnwindData |  |
| 2022 | `ZwFlushInstructionCache` | `0x161E70` | 24 | UnwindData |  |
| 375 | `NtFlushKey` | `0x161E90` | 24 | UnwindData |  |
| 2023 | `ZwFlushKey` | `0x161E90` | 24 | UnwindData |  |
| 376 | `NtFlushProcessWriteBuffers` | `0x161EB0` | 24 | UnwindData |  |
| 2024 | `ZwFlushProcessWriteBuffers` | `0x161EB0` | 24 | UnwindData |  |
| 377 | `NtFlushVirtualMemory` | `0x161ED0` | 24 | UnwindData |  |
| 2025 | `ZwFlushVirtualMemory` | `0x161ED0` | 24 | UnwindData |  |
| 378 | `NtFlushWriteBuffer` | `0x161EF0` | 24 | UnwindData |  |
| 2026 | `ZwFlushWriteBuffer` | `0x161EF0` | 24 | UnwindData |  |
| 379 | `NtFreeUserPhysicalPages` | `0x161F10` | 24 | UnwindData |  |
| 2027 | `ZwFreeUserPhysicalPages` | `0x161F10` | 24 | UnwindData |  |
| 381 | `NtFreezeRegistry` | `0x161F30` | 24 | UnwindData |  |
| 2029 | `ZwFreezeRegistry` | `0x161F30` | 24 | UnwindData |  |
| 382 | `NtFreezeTransactions` | `0x161F50` | 24 | UnwindData |  |
| 2030 | `ZwFreezeTransactions` | `0x161F50` | 24 | UnwindData |  |
| 384 | `NtGetCachedSigningLevel` | `0x161F70` | 24 | UnwindData |  |
| 2032 | `ZwGetCachedSigningLevel` | `0x161F70` | 24 | UnwindData |  |
| 385 | `NtGetCompleteWnfStateSubscription` | `0x161F90` | 24 | UnwindData |  |
| 2033 | `ZwGetCompleteWnfStateSubscription` | `0x161F90` | 24 | UnwindData |  |
| 386 | `NtGetContextThread` | `0x161FB0` | 24 | UnwindData |  |
| 2034 | `ZwGetContextThread` | `0x161FB0` | 24 | UnwindData |  |
| 387 | `NtGetCurrentProcessorNumber` | `0x161FD0` | 24 | UnwindData |  |
| 2035 | `ZwGetCurrentProcessorNumber` | `0x161FD0` | 24 | UnwindData |  |
| 388 | `NtGetCurrentProcessorNumberEx` | `0x161FF0` | 24 | UnwindData |  |
| 2036 | `ZwGetCurrentProcessorNumberEx` | `0x161FF0` | 24 | UnwindData |  |
| 389 | `NtGetDevicePowerState` | `0x162010` | 24 | UnwindData |  |
| 2037 | `ZwGetDevicePowerState` | `0x162010` | 24 | UnwindData |  |
| 390 | `NtGetMUIRegistryInfo` | `0x162030` | 24 | UnwindData |  |
| 2038 | `ZwGetMUIRegistryInfo` | `0x162030` | 24 | UnwindData |  |
| 391 | `NtGetNextProcess` | `0x162050` | 24 | UnwindData |  |
| 2039 | `ZwGetNextProcess` | `0x162050` | 24 | UnwindData |  |
| 392 | `NtGetNextThread` | `0x162070` | 24 | UnwindData |  |
| 2040 | `ZwGetNextThread` | `0x162070` | 24 | UnwindData |  |
| 393 | `NtGetNlsSectionPtr` | `0x162090` | 24 | UnwindData |  |
| 2041 | `ZwGetNlsSectionPtr` | `0x162090` | 24 | UnwindData |  |
| 394 | `NtGetNotificationResourceManager` | `0x1620B0` | 24 | UnwindData |  |
| 2042 | `ZwGetNotificationResourceManager` | `0x1620B0` | 24 | UnwindData |  |
| 396 | `NtGetWriteWatch` | `0x1620D0` | 24 | UnwindData |  |
| 2043 | `ZwGetWriteWatch` | `0x1620D0` | 24 | UnwindData |  |
| 397 | `NtImpersonateAnonymousToken` | `0x1620F0` | 24 | UnwindData |  |
| 2044 | `ZwImpersonateAnonymousToken` | `0x1620F0` | 24 | UnwindData |  |
| 399 | `NtImpersonateThread` | `0x162110` | 24 | UnwindData |  |
| 2046 | `ZwImpersonateThread` | `0x162110` | 24 | UnwindData |  |
| 400 | `NtInitializeEnclave` | `0x162130` | 24 | UnwindData |  |
| 2047 | `ZwInitializeEnclave` | `0x162130` | 24 | UnwindData |  |
| 401 | `NtInitializeNlsFiles` | `0x162150` | 24 | UnwindData |  |
| 2048 | `ZwInitializeNlsFiles` | `0x162150` | 24 | UnwindData |  |
| 402 | `NtInitializeRegistry` | `0x162170` | 24 | UnwindData |  |
| 2049 | `ZwInitializeRegistry` | `0x162170` | 24 | UnwindData |  |
| 403 | `NtInitiatePowerAction` | `0x162190` | 24 | UnwindData |  |
| 2050 | `ZwInitiatePowerAction` | `0x162190` | 24 | UnwindData |  |
| 405 | `NtIsSystemResumeAutomatic` | `0x1621B0` | 24 | UnwindData |  |
| 2052 | `ZwIsSystemResumeAutomatic` | `0x1621B0` | 24 | UnwindData |  |
| 406 | `NtIsUILanguageComitted` | `0x1621D0` | 24 | UnwindData |  |
| 2053 | `ZwIsUILanguageComitted` | `0x1621D0` | 24 | UnwindData |  |
| 407 | `NtListenPort` | `0x1621F0` | 24 | UnwindData |  |
| 2054 | `ZwListenPort` | `0x1621F0` | 24 | UnwindData |  |
| 408 | `NtLoadDriver` | `0x162210` | 24 | UnwindData |  |
| 2055 | `ZwLoadDriver` | `0x162210` | 24 | UnwindData |  |
| 409 | `NtLoadEnclaveData` | `0x162230` | 24 | UnwindData |  |
| 2056 | `ZwLoadEnclaveData` | `0x162230` | 24 | UnwindData |  |
| 410 | `NtLoadKey` | `0x162250` | 24 | UnwindData |  |
| 2057 | `ZwLoadKey` | `0x162250` | 24 | UnwindData |  |
| 411 | `NtLoadKey2` | `0x162270` | 24 | UnwindData |  |
| 2058 | `ZwLoadKey2` | `0x162270` | 24 | UnwindData |  |
| 412 | `NtLoadKey3` | `0x162290` | 24 | UnwindData |  |
| 2059 | `ZwLoadKey3` | `0x162290` | 24 | UnwindData |  |
| 413 | `NtLoadKeyEx` | `0x1622B0` | 24 | UnwindData |  |
| 2060 | `ZwLoadKeyEx` | `0x1622B0` | 24 | UnwindData |  |
| 414 | `NtLockFile` | `0x1622D0` | 24 | UnwindData |  |
| 2061 | `ZwLockFile` | `0x1622D0` | 24 | UnwindData |  |
| 415 | `NtLockProductActivationKeys` | `0x1622F0` | 24 | UnwindData |  |
| 2062 | `ZwLockProductActivationKeys` | `0x1622F0` | 24 | UnwindData |  |
| 416 | `NtLockRegistryKey` | `0x162310` | 24 | UnwindData |  |
| 2063 | `ZwLockRegistryKey` | `0x162310` | 24 | UnwindData |  |
| 417 | `NtLockVirtualMemory` | `0x162330` | 24 | UnwindData |  |
| 2064 | `ZwLockVirtualMemory` | `0x162330` | 24 | UnwindData |  |
| 418 | `NtMakePermanentObject` | `0x162350` | 24 | UnwindData |  |
| 2065 | `ZwMakePermanentObject` | `0x162350` | 24 | UnwindData |  |
| 419 | `NtMakeTemporaryObject` | `0x162370` | 24 | UnwindData |  |
| 2066 | `ZwMakeTemporaryObject` | `0x162370` | 24 | UnwindData |  |
| 420 | `NtManageHotPatch` | `0x162390` | 24 | UnwindData |  |
| 2067 | `ZwManageHotPatch` | `0x162390` | 24 | UnwindData |  |
| 421 | `NtManagePartition` | `0x1623B0` | 24 | UnwindData |  |
| 2068 | `ZwManagePartition` | `0x1623B0` | 24 | UnwindData |  |
| 422 | `NtMapCMFModule` | `0x1623D0` | 24 | UnwindData |  |
| 2069 | `ZwMapCMFModule` | `0x1623D0` | 24 | UnwindData |  |
| 423 | `NtMapUserPhysicalPages` | `0x1623F0` | 24 | UnwindData |  |
| 2070 | `ZwMapUserPhysicalPages` | `0x1623F0` | 24 | UnwindData |  |
| 426 | `NtMapViewOfSectionEx` | `0x162410` | 24 | UnwindData |  |
| 2073 | `ZwMapViewOfSectionEx` | `0x162410` | 24 | UnwindData |  |
| 427 | `NtModifyBootEntry` | `0x162430` | 24 | UnwindData |  |
| 2074 | `ZwModifyBootEntry` | `0x162430` | 24 | UnwindData |  |
| 428 | `NtModifyDriverEntry` | `0x162450` | 24 | UnwindData |  |
| 2075 | `ZwModifyDriverEntry` | `0x162450` | 24 | UnwindData |  |
| 429 | `NtNotifyChangeDirectoryFile` | `0x162470` | 24 | UnwindData |  |
| 2076 | `ZwNotifyChangeDirectoryFile` | `0x162470` | 24 | UnwindData |  |
| 430 | `NtNotifyChangeDirectoryFileEx` | `0x162490` | 24 | UnwindData |  |
| 2077 | `ZwNotifyChangeDirectoryFileEx` | `0x162490` | 24 | UnwindData |  |
| 431 | `NtNotifyChangeKey` | `0x1624B0` | 24 | UnwindData |  |
| 2078 | `ZwNotifyChangeKey` | `0x1624B0` | 24 | UnwindData |  |
| 432 | `NtNotifyChangeMultipleKeys` | `0x1624D0` | 24 | UnwindData |  |
| 2079 | `ZwNotifyChangeMultipleKeys` | `0x1624D0` | 24 | UnwindData |  |
| 433 | `NtNotifyChangeSession` | `0x1624F0` | 24 | UnwindData |  |
| 2080 | `ZwNotifyChangeSession` | `0x1624F0` | 24 | UnwindData |  |
| 434 | `NtOpenCpuPartition` | `0x162510` | 24 | UnwindData |  |
| 2081 | `ZwOpenCpuPartition` | `0x162510` | 24 | UnwindData |  |
| 436 | `NtOpenEnlistment` | `0x162530` | 24 | UnwindData |  |
| 2083 | `ZwOpenEnlistment` | `0x162530` | 24 | UnwindData |  |
| 438 | `NtOpenEventPair` | `0x162550` | 24 | UnwindData |  |
| 2085 | `ZwOpenEventPair` | `0x162550` | 24 | UnwindData |  |
| 440 | `NtOpenIoCompletion` | `0x162570` | 24 | UnwindData |  |
| 2087 | `ZwOpenIoCompletion` | `0x162570` | 24 | UnwindData |  |
| 441 | `NtOpenJobObject` | `0x162590` | 24 | UnwindData |  |
| 2088 | `ZwOpenJobObject` | `0x162590` | 24 | UnwindData |  |
| 443 | `NtOpenKeyEx` | `0x1625B0` | 24 | UnwindData |  |
| 2090 | `ZwOpenKeyEx` | `0x1625B0` | 24 | UnwindData |  |
| 444 | `NtOpenKeyTransacted` | `0x1625D0` | 24 | UnwindData |  |
| 2091 | `ZwOpenKeyTransacted` | `0x1625D0` | 24 | UnwindData |  |
| 445 | `NtOpenKeyTransactedEx` | `0x1625F0` | 24 | UnwindData |  |
| 2092 | `ZwOpenKeyTransactedEx` | `0x1625F0` | 24 | UnwindData |  |
| 446 | `NtOpenKeyedEvent` | `0x162610` | 24 | UnwindData |  |
| 2093 | `ZwOpenKeyedEvent` | `0x162610` | 24 | UnwindData |  |
| 447 | `NtOpenMutant` | `0x162630` | 24 | UnwindData |  |
| 2094 | `ZwOpenMutant` | `0x162630` | 24 | UnwindData |  |
| 448 | `NtOpenObjectAuditAlarm` | `0x162650` | 24 | UnwindData |  |
| 2095 | `ZwOpenObjectAuditAlarm` | `0x162650` | 24 | UnwindData |  |
| 449 | `NtOpenPartition` | `0x162670` | 24 | UnwindData |  |
| 2096 | `ZwOpenPartition` | `0x162670` | 24 | UnwindData |  |
| 450 | `NtOpenPrivateNamespace` | `0x162690` | 24 | UnwindData |  |
| 2097 | `ZwOpenPrivateNamespace` | `0x162690` | 24 | UnwindData |  |
| 452 | `NtOpenProcessToken` | `0x1626B0` | 24 | UnwindData |  |
| 2099 | `ZwOpenProcessToken` | `0x1626B0` | 24 | UnwindData |  |
| 454 | `NtOpenRegistryTransaction` | `0x1626D0` | 24 | UnwindData |  |
| 2101 | `ZwOpenRegistryTransaction` | `0x1626D0` | 24 | UnwindData |  |
| 455 | `NtOpenResourceManager` | `0x1626F0` | 24 | UnwindData |  |
| 2102 | `ZwOpenResourceManager` | `0x1626F0` | 24 | UnwindData |  |
| 457 | `NtOpenSemaphore` | `0x162710` | 24 | UnwindData |  |
| 2104 | `ZwOpenSemaphore` | `0x162710` | 24 | UnwindData |  |
| 458 | `NtOpenSession` | `0x162730` | 24 | UnwindData |  |
| 2105 | `ZwOpenSession` | `0x162730` | 24 | UnwindData |  |
| 459 | `NtOpenSymbolicLinkObject` | `0x162750` | 24 | UnwindData |  |
| 2106 | `ZwOpenSymbolicLinkObject` | `0x162750` | 24 | UnwindData |  |
| 460 | `NtOpenThread` | `0x162770` | 24 | UnwindData |  |
| 2107 | `ZwOpenThread` | `0x162770` | 24 | UnwindData |  |
| 463 | `NtOpenTimer` | `0x162790` | 24 | UnwindData |  |
| 2110 | `ZwOpenTimer` | `0x162790` | 24 | UnwindData |  |
| 464 | `NtOpenTransaction` | `0x1627B0` | 24 | UnwindData |  |
| 2111 | `ZwOpenTransaction` | `0x1627B0` | 24 | UnwindData |  |
| 465 | `NtOpenTransactionManager` | `0x1627D0` | 24 | UnwindData |  |
| 2112 | `ZwOpenTransactionManager` | `0x1627D0` | 24 | UnwindData |  |
| 466 | `NtPlugPlayControl` | `0x1627F0` | 24 | UnwindData |  |
| 2113 | `ZwPlugPlayControl` | `0x1627F0` | 24 | UnwindData |  |
| 468 | `NtPrePrepareComplete` | `0x162810` | 24 | UnwindData |  |
| 2115 | `ZwPrePrepareComplete` | `0x162810` | 24 | UnwindData |  |
| 469 | `NtPrePrepareEnlistment` | `0x162830` | 24 | UnwindData |  |
| 2116 | `ZwPrePrepareEnlistment` | `0x162830` | 24 | UnwindData |  |
| 470 | `NtPrepareComplete` | `0x162850` | 24 | UnwindData |  |
| 2117 | `ZwPrepareComplete` | `0x162850` | 24 | UnwindData |  |
| 471 | `NtPrepareEnlistment` | `0x162870` | 24 | UnwindData |  |
| 2118 | `ZwPrepareEnlistment` | `0x162870` | 24 | UnwindData |  |
| 472 | `NtPrivilegeCheck` | `0x162890` | 24 | UnwindData |  |
| 2119 | `ZwPrivilegeCheck` | `0x162890` | 24 | UnwindData |  |
| 473 | `NtPrivilegeObjectAuditAlarm` | `0x1628B0` | 24 | UnwindData |  |
| 2120 | `ZwPrivilegeObjectAuditAlarm` | `0x1628B0` | 24 | UnwindData |  |
| 474 | `NtPrivilegedServiceAuditAlarm` | `0x1628D0` | 24 | UnwindData |  |
| 2121 | `ZwPrivilegedServiceAuditAlarm` | `0x1628D0` | 24 | UnwindData |  |
| 475 | `NtPropagationComplete` | `0x1628F0` | 24 | UnwindData |  |
| 2122 | `ZwPropagationComplete` | `0x1628F0` | 24 | UnwindData |  |
| 476 | `NtPropagationFailed` | `0x162910` | 24 | UnwindData |  |
| 2123 | `ZwPropagationFailed` | `0x162910` | 24 | UnwindData |  |
| 478 | `NtPssCaptureVaSpaceBulk` | `0x162930` | 24 | UnwindData |  |
| 2125 | `ZwPssCaptureVaSpaceBulk` | `0x162930` | 24 | UnwindData |  |
| 479 | `NtPulseEvent` | `0x162950` | 24 | UnwindData |  |
| 2126 | `ZwPulseEvent` | `0x162950` | 24 | UnwindData |  |
| 481 | `NtQueryAuxiliaryCounterFrequency` | `0x162970` | 24 | UnwindData |  |
| 2128 | `ZwQueryAuxiliaryCounterFrequency` | `0x162970` | 24 | UnwindData |  |
| 482 | `NtQueryBootEntryOrder` | `0x162990` | 24 | UnwindData |  |
| 2129 | `ZwQueryBootEntryOrder` | `0x162990` | 24 | UnwindData |  |
| 483 | `NtQueryBootOptions` | `0x1629B0` | 24 | UnwindData |  |
| 2130 | `ZwQueryBootOptions` | `0x1629B0` | 24 | UnwindData |  |
| 484 | `NtQueryDebugFilterState` | `0x1629D0` | 24 | UnwindData |  |
| 2131 | `ZwQueryDebugFilterState` | `0x1629D0` | 24 | UnwindData |  |
| 488 | `NtQueryDirectoryFileEx` | `0x1629F0` | 24 | UnwindData |  |
| 2135 | `ZwQueryDirectoryFileEx` | `0x1629F0` | 24 | UnwindData |  |
| 489 | `NtQueryDirectoryObject` | `0x162A10` | 24 | UnwindData |  |
| 2136 | `ZwQueryDirectoryObject` | `0x162A10` | 24 | UnwindData |  |
| 490 | `NtQueryDriverEntryOrder` | `0x162A30` | 24 | UnwindData |  |
| 2137 | `ZwQueryDriverEntryOrder` | `0x162A30` | 24 | UnwindData |  |
| 491 | `NtQueryEaFile` | `0x162A50` | 24 | UnwindData |  |
| 2138 | `ZwQueryEaFile` | `0x162A50` | 24 | UnwindData |  |
| 493 | `NtQueryFullAttributesFile` | `0x162A70` | 24 | UnwindData |  |
| 2140 | `ZwQueryFullAttributesFile` | `0x162A70` | 24 | UnwindData |  |
| 494 | `NtQueryInformationAtom` | `0x162A90` | 24 | UnwindData |  |
| 2141 | `ZwQueryInformationAtom` | `0x162A90` | 24 | UnwindData |  |
| 495 | `NtQueryInformationByName` | `0x162AB0` | 24 | UnwindData |  |
| 2142 | `ZwQueryInformationByName` | `0x162AB0` | 24 | UnwindData |  |
| 496 | `NtQueryInformationCpuPartition` | `0x162AD0` | 24 | UnwindData |  |
| 2143 | `ZwQueryInformationCpuPartition` | `0x162AD0` | 24 | UnwindData |  |
| 497 | `NtQueryInformationEnlistment` | `0x162AF0` | 24 | UnwindData |  |
| 2144 | `ZwQueryInformationEnlistment` | `0x162AF0` | 24 | UnwindData |  |
| 499 | `NtQueryInformationJobObject` | `0x162B10` | 24 | UnwindData |  |
| 2146 | `ZwQueryInformationJobObject` | `0x162B10` | 24 | UnwindData |  |
| 500 | `NtQueryInformationPort` | `0x162B30` | 24 | UnwindData |  |
| 2147 | `ZwQueryInformationPort` | `0x162B30` | 24 | UnwindData |  |
| 502 | `NtQueryInformationResourceManager` | `0x162B50` | 24 | UnwindData |  |
| 2149 | `ZwQueryInformationResourceManager` | `0x162B50` | 24 | UnwindData |  |
| 505 | `NtQueryInformationTransaction` | `0x162B70` | 24 | UnwindData |  |
| 2152 | `ZwQueryInformationTransaction` | `0x162B70` | 24 | UnwindData |  |
| 506 | `NtQueryInformationTransactionManager` | `0x162B90` | 24 | UnwindData |  |
| 2153 | `ZwQueryInformationTransactionManager` | `0x162B90` | 24 | UnwindData |  |
| 507 | `NtQueryInformationWorkerFactory` | `0x162BB0` | 24 | UnwindData |  |
| 2154 | `ZwQueryInformationWorkerFactory` | `0x162BB0` | 24 | UnwindData |  |
| 508 | `NtQueryInstallUILanguage` | `0x162BD0` | 24 | UnwindData |  |
| 2155 | `ZwQueryInstallUILanguage` | `0x162BD0` | 24 | UnwindData |  |
| 509 | `NtQueryIntervalProfile` | `0x162BF0` | 24 | UnwindData |  |
| 2156 | `ZwQueryIntervalProfile` | `0x162BF0` | 24 | UnwindData |  |
| 510 | `NtQueryIoCompletion` | `0x162C10` | 24 | UnwindData |  |
| 2157 | `ZwQueryIoCompletion` | `0x162C10` | 24 | UnwindData |  |
| 511 | `NtQueryIoRingCapabilities` | `0x162C30` | 24 | UnwindData |  |
| 2158 | `ZwQueryIoRingCapabilities` | `0x162C30` | 24 | UnwindData |  |
| 513 | `NtQueryLicenseValue` | `0x162C50` | 24 | UnwindData |  |
| 2160 | `ZwQueryLicenseValue` | `0x162C50` | 24 | UnwindData |  |
| 514 | `NtQueryMultipleValueKey` | `0x162C70` | 24 | UnwindData |  |
| 2161 | `ZwQueryMultipleValueKey` | `0x162C70` | 24 | UnwindData |  |
| 515 | `NtQueryMutant` | `0x162C90` | 24 | UnwindData |  |
| 2162 | `ZwQueryMutant` | `0x162C90` | 24 | UnwindData |  |
| 517 | `NtQueryOpenSubKeys` | `0x162CB0` | 24 | UnwindData |  |
| 2164 | `ZwQueryOpenSubKeys` | `0x162CB0` | 24 | UnwindData |  |
| 518 | `NtQueryOpenSubKeysEx` | `0x162CD0` | 24 | UnwindData |  |
| 2165 | `ZwQueryOpenSubKeysEx` | `0x162CD0` | 24 | UnwindData |  |
| 520 | `NtQueryPortInformationProcess` | `0x162CF0` | 24 | UnwindData |  |
| 2167 | `ZwQueryPortInformationProcess` | `0x162CF0` | 24 | UnwindData |  |
| 521 | `NtQueryQuotaInformationFile` | `0x162D10` | 24 | UnwindData |  |
| 2168 | `ZwQueryQuotaInformationFile` | `0x162D10` | 24 | UnwindData |  |
| 523 | `NtQuerySecurityAttributesToken` | `0x162D30` | 24 | UnwindData |  |
| 2170 | `ZwQuerySecurityAttributesToken` | `0x162D30` | 24 | UnwindData |  |
| 524 | `NtQuerySecurityObject` | `0x162D50` | 24 | UnwindData |  |
| 2171 | `ZwQuerySecurityObject` | `0x162D50` | 24 | UnwindData |  |
| 525 | `NtQuerySecurityPolicy` | `0x162D70` | 24 | UnwindData |  |
| 2172 | `ZwQuerySecurityPolicy` | `0x162D70` | 24 | UnwindData |  |
| 526 | `NtQuerySemaphore` | `0x162D90` | 24 | UnwindData |  |
| 2173 | `ZwQuerySemaphore` | `0x162D90` | 24 | UnwindData |  |
| 527 | `NtQuerySymbolicLinkObject` | `0x162DB0` | 24 | UnwindData |  |
| 2174 | `ZwQuerySymbolicLinkObject` | `0x162DB0` | 24 | UnwindData |  |
| 528 | `NtQuerySystemEnvironmentValue` | `0x162DD0` | 24 | UnwindData |  |
| 2175 | `ZwQuerySystemEnvironmentValue` | `0x162DD0` | 24 | UnwindData |  |
| 529 | `NtQuerySystemEnvironmentValueEx` | `0x162DF0` | 24 | UnwindData |  |
| 2176 | `ZwQuerySystemEnvironmentValueEx` | `0x162DF0` | 24 | UnwindData |  |
| 531 | `NtQuerySystemInformationEx` | `0x162E10` | 24 | UnwindData |  |
| 2178 | `ZwQuerySystemInformationEx` | `0x162E10` | 24 | UnwindData |  |
| 534 | `NtQueryTimerResolution` | `0x162E30` | 24 | UnwindData |  |
| 2181 | `ZwQueryTimerResolution` | `0x162E30` | 24 | UnwindData |  |
| 538 | `NtQueryWnfStateData` | `0x162E50` | 24 | UnwindData |  |
| 2185 | `ZwQueryWnfStateData` | `0x162E50` | 24 | UnwindData |  |
| 539 | `NtQueryWnfStateNameInformation` | `0x162E70` | 24 | UnwindData |  |
| 2186 | `ZwQueryWnfStateNameInformation` | `0x162E70` | 24 | UnwindData |  |
| 541 | `NtQueueApcThreadEx` | `0x162E90` | 24 | UnwindData |  |
| 2188 | `ZwQueueApcThreadEx` | `0x162E90` | 24 | UnwindData |  |
| 542 | `NtQueueApcThreadEx2` | `0x162EB0` | 24 | UnwindData |  |
| 2189 | `ZwQueueApcThreadEx2` | `0x162EB0` | 24 | UnwindData |  |
| 543 | `NtRaiseException` | `0x162ED0` | 24 | UnwindData |  |
| 2190 | `ZwRaiseException` | `0x162ED0` | 24 | UnwindData |  |
| 544 | `NtRaiseHardError` | `0x162EF0` | 24 | UnwindData |  |
| 2191 | `ZwRaiseHardError` | `0x162EF0` | 24 | UnwindData |  |
| 547 | `NtReadOnlyEnlistment` | `0x162F10` | 24 | UnwindData |  |
| 2194 | `ZwReadOnlyEnlistment` | `0x162F10` | 24 | UnwindData |  |
| 550 | `NtReadVirtualMemoryEx` | `0x162F30` | 24 | UnwindData |  |
| 2197 | `ZwReadVirtualMemoryEx` | `0x162F30` | 24 | UnwindData |  |
| 551 | `NtRecoverEnlistment` | `0x162F50` | 24 | UnwindData |  |
| 2198 | `ZwRecoverEnlistment` | `0x162F50` | 24 | UnwindData |  |
| 552 | `NtRecoverResourceManager` | `0x162F70` | 24 | UnwindData |  |
| 2199 | `ZwRecoverResourceManager` | `0x162F70` | 24 | UnwindData |  |
| 553 | `NtRecoverTransactionManager` | `0x162F90` | 24 | UnwindData |  |
| 2200 | `ZwRecoverTransactionManager` | `0x162F90` | 24 | UnwindData |  |
| 554 | `NtRegisterProtocolAddressInformation` | `0x162FB0` | 24 | UnwindData |  |
| 2201 | `ZwRegisterProtocolAddressInformation` | `0x162FB0` | 24 | UnwindData |  |
| 555 | `NtRegisterThreadTerminatePort` | `0x162FD0` | 24 | UnwindData |  |
| 2202 | `ZwRegisterThreadTerminatePort` | `0x162FD0` | 24 | UnwindData |  |
| 556 | `NtReleaseKeyedEvent` | `0x162FF0` | 24 | UnwindData |  |
| 2203 | `ZwReleaseKeyedEvent` | `0x162FF0` | 24 | UnwindData |  |
| 559 | `NtReleaseWorkerFactoryWorker` | `0x163010` | 24 | UnwindData |  |
| 2206 | `ZwReleaseWorkerFactoryWorker` | `0x163010` | 24 | UnwindData |  |
| 561 | `NtRemoveIoCompletionEx` | `0x163030` | 24 | UnwindData |  |
| 2208 | `ZwRemoveIoCompletionEx` | `0x163030` | 24 | UnwindData |  |
| 562 | `NtRemoveProcessDebug` | `0x163050` | 24 | UnwindData |  |
| 2209 | `ZwRemoveProcessDebug` | `0x163050` | 24 | UnwindData |  |
| 563 | `NtRenameKey` | `0x163070` | 24 | UnwindData |  |
| 2210 | `ZwRenameKey` | `0x163070` | 24 | UnwindData |  |
| 564 | `NtRenameTransactionManager` | `0x163090` | 24 | UnwindData |  |
| 2211 | `ZwRenameTransactionManager` | `0x163090` | 24 | UnwindData |  |
| 565 | `NtReplaceKey` | `0x1630B0` | 24 | UnwindData |  |
| 2212 | `ZwReplaceKey` | `0x1630B0` | 24 | UnwindData |  |
| 566 | `NtReplacePartitionUnit` | `0x1630D0` | 24 | UnwindData |  |
| 2213 | `ZwReplacePartitionUnit` | `0x1630D0` | 24 | UnwindData |  |
| 570 | `NtReplyWaitReplyPort` | `0x1630F0` | 24 | UnwindData |  |
| 2217 | `ZwReplyWaitReplyPort` | `0x1630F0` | 24 | UnwindData |  |
| 571 | `NtRequestPort` | `0x163110` | 24 | UnwindData |  |
| 2218 | `ZwRequestPort` | `0x163110` | 24 | UnwindData |  |
| 573 | `NtResetEvent` | `0x163130` | 24 | UnwindData |  |
| 2220 | `ZwResetEvent` | `0x163130` | 24 | UnwindData |  |
| 574 | `NtResetWriteWatch` | `0x163150` | 24 | UnwindData |  |
| 2221 | `ZwResetWriteWatch` | `0x163150` | 24 | UnwindData |  |
| 575 | `NtRestoreKey` | `0x163170` | 24 | UnwindData |  |
| 2222 | `ZwRestoreKey` | `0x163170` | 24 | UnwindData |  |
| 576 | `NtResumeProcess` | `0x163190` | 24 | UnwindData |  |
| 2223 | `ZwResumeProcess` | `0x163190` | 24 | UnwindData |  |
| 578 | `NtRevertContainerImpersonation` | `0x1631B0` | 24 | UnwindData |  |
| 2225 | `ZwRevertContainerImpersonation` | `0x1631B0` | 24 | UnwindData |  |
| 579 | `NtRollbackComplete` | `0x1631D0` | 24 | UnwindData |  |
| 2226 | `ZwRollbackComplete` | `0x1631D0` | 24 | UnwindData |  |
| 580 | `NtRollbackEnlistment` | `0x1631F0` | 24 | UnwindData |  |
| 2227 | `ZwRollbackEnlistment` | `0x1631F0` | 24 | UnwindData |  |
| 581 | `NtRollbackRegistryTransaction` | `0x163210` | 24 | UnwindData |  |
| 2228 | `ZwRollbackRegistryTransaction` | `0x163210` | 24 | UnwindData |  |
| 582 | `NtRollbackTransaction` | `0x163230` | 24 | UnwindData |  |
| 2229 | `ZwRollbackTransaction` | `0x163230` | 24 | UnwindData |  |
| 583 | `NtRollforwardTransactionManager` | `0x163250` | 24 | UnwindData |  |
| 2230 | `ZwRollforwardTransactionManager` | `0x163250` | 24 | UnwindData |  |
| 584 | `NtSaveKey` | `0x163270` | 24 | UnwindData |  |
| 2231 | `ZwSaveKey` | `0x163270` | 24 | UnwindData |  |
| 585 | `NtSaveKeyEx` | `0x163290` | 24 | UnwindData |  |
| 2232 | `ZwSaveKeyEx` | `0x163290` | 24 | UnwindData |  |
| 586 | `NtSaveMergedKeys` | `0x1632B0` | 24 | UnwindData |  |
| 2233 | `ZwSaveMergedKeys` | `0x1632B0` | 24 | UnwindData |  |
| 587 | `NtSecureConnectPort` | `0x1632D0` | 24 | UnwindData |  |
| 2234 | `ZwSecureConnectPort` | `0x1632D0` | 24 | UnwindData |  |
| 588 | `NtSerializeBoot` | `0x1632F0` | 24 | UnwindData |  |
| 2235 | `ZwSerializeBoot` | `0x1632F0` | 24 | UnwindData |  |
| 589 | `NtSetBootEntryOrder` | `0x163310` | 24 | UnwindData |  |
| 2236 | `ZwSetBootEntryOrder` | `0x163310` | 24 | UnwindData |  |
| 590 | `NtSetBootOptions` | `0x163330` | 24 | UnwindData |  |
| 2237 | `ZwSetBootOptions` | `0x163330` | 24 | UnwindData |  |
| 591 | `NtSetCachedSigningLevel` | `0x163350` | 24 | UnwindData |  |
| 2238 | `ZwSetCachedSigningLevel` | `0x163350` | 24 | UnwindData |  |
| 592 | `NtSetCachedSigningLevel2` | `0x163370` | 24 | UnwindData |  |
| 2239 | `ZwSetCachedSigningLevel2` | `0x163370` | 24 | UnwindData |  |
| 593 | `NtSetContextThread` | `0x163390` | 24 | UnwindData |  |
| 2240 | `ZwSetContextThread` | `0x163390` | 24 | UnwindData |  |
| 594 | `NtSetDebugFilterState` | `0x1633B0` | 24 | UnwindData |  |
| 2241 | `ZwSetDebugFilterState` | `0x1633B0` | 24 | UnwindData |  |
| 595 | `NtSetDefaultHardErrorPort` | `0x1633D0` | 24 | UnwindData |  |
| 2242 | `ZwSetDefaultHardErrorPort` | `0x1633D0` | 24 | UnwindData |  |
| 596 | `NtSetDefaultLocale` | `0x1633F0` | 24 | UnwindData |  |
| 2243 | `ZwSetDefaultLocale` | `0x1633F0` | 24 | UnwindData |  |
| 597 | `NtSetDefaultUILanguage` | `0x163410` | 24 | UnwindData |  |
| 2244 | `ZwSetDefaultUILanguage` | `0x163410` | 24 | UnwindData |  |
| 598 | `NtSetDriverEntryOrder` | `0x163430` | 24 | UnwindData |  |
| 2245 | `ZwSetDriverEntryOrder` | `0x163430` | 24 | UnwindData |  |
| 599 | `NtSetEaFile` | `0x163450` | 24 | UnwindData |  |
| 2246 | `ZwSetEaFile` | `0x163450` | 24 | UnwindData |  |
| 602 | `NtSetEventEx` | `0x163470` | 24 | UnwindData |  |
| 2249 | `ZwSetEventEx` | `0x163470` | 24 | UnwindData |  |
| 603 | `NtSetHighEventPair` | `0x163490` | 24 | UnwindData |  |
| 2250 | `ZwSetHighEventPair` | `0x163490` | 24 | UnwindData |  |
| 604 | `NtSetHighWaitLowEventPair` | `0x1634B0` | 24 | UnwindData |  |
| 2251 | `ZwSetHighWaitLowEventPair` | `0x1634B0` | 24 | UnwindData |  |
| 605 | `NtSetIRTimer` | `0x1634D0` | 24 | UnwindData |  |
| 2252 | `ZwSetIRTimer` | `0x1634D0` | 24 | UnwindData |  |
| 606 | `NtSetInformationCpuPartition` | `0x1634F0` | 24 | UnwindData |  |
| 2253 | `ZwSetInformationCpuPartition` | `0x1634F0` | 24 | UnwindData |  |
| 607 | `NtSetInformationDebugObject` | `0x163510` | 24 | UnwindData |  |
| 2254 | `ZwSetInformationDebugObject` | `0x163510` | 24 | UnwindData |  |
| 608 | `NtSetInformationEnlistment` | `0x163530` | 24 | UnwindData |  |
| 2255 | `ZwSetInformationEnlistment` | `0x163530` | 24 | UnwindData |  |
| 610 | `NtSetInformationIoRing` | `0x163550` | 24 | UnwindData |  |
| 2257 | `ZwSetInformationIoRing` | `0x163550` | 24 | UnwindData |  |
| 611 | `NtSetInformationJobObject` | `0x163570` | 24 | UnwindData |  |
| 2258 | `ZwSetInformationJobObject` | `0x163570` | 24 | UnwindData |  |
| 612 | `NtSetInformationKey` | `0x163590` | 24 | UnwindData |  |
| 2259 | `ZwSetInformationKey` | `0x163590` | 24 | UnwindData |  |
| 615 | `NtSetInformationResourceManager` | `0x1635B0` | 24 | UnwindData |  |
| 2262 | `ZwSetInformationResourceManager` | `0x1635B0` | 24 | UnwindData |  |
| 616 | `NtSetInformationSymbolicLink` | `0x1635D0` | 24 | UnwindData |  |
| 2263 | `ZwSetInformationSymbolicLink` | `0x1635D0` | 24 | UnwindData |  |
| 618 | `NtSetInformationToken` | `0x1635F0` | 24 | UnwindData |  |
| 2265 | `ZwSetInformationToken` | `0x1635F0` | 24 | UnwindData |  |
| 619 | `NtSetInformationTransaction` | `0x163610` | 24 | UnwindData |  |
| 2266 | `ZwSetInformationTransaction` | `0x163610` | 24 | UnwindData |  |
| 620 | `NtSetInformationTransactionManager` | `0x163630` | 24 | UnwindData |  |
| 2267 | `ZwSetInformationTransactionManager` | `0x163630` | 24 | UnwindData |  |
| 621 | `NtSetInformationVirtualMemory` | `0x163650` | 24 | UnwindData |  |
| 2268 | `ZwSetInformationVirtualMemory` | `0x163650` | 24 | UnwindData |  |
| 622 | `NtSetInformationWorkerFactory` | `0x163670` | 24 | UnwindData |  |
| 2269 | `ZwSetInformationWorkerFactory` | `0x163670` | 24 | UnwindData |  |
| 623 | `NtSetIntervalProfile` | `0x163690` | 24 | UnwindData |  |
| 2270 | `ZwSetIntervalProfile` | `0x163690` | 24 | UnwindData |  |
| 624 | `NtSetIoCompletion` | `0x1636B0` | 24 | UnwindData |  |
| 2271 | `ZwSetIoCompletion` | `0x1636B0` | 24 | UnwindData |  |
| 625 | `NtSetIoCompletionEx` | `0x1636D0` | 24 | UnwindData |  |
| 2272 | `ZwSetIoCompletionEx` | `0x1636D0` | 24 | UnwindData |  |
| 626 | `NtSetLdtEntries` | `0x1636F0` | 24 | UnwindData |  |
| 2273 | `ZwSetLdtEntries` | `0x1636F0` | 24 | UnwindData |  |
| 627 | `NtSetLowEventPair` | `0x163710` | 24 | UnwindData |  |
| 2274 | `ZwSetLowEventPair` | `0x163710` | 24 | UnwindData |  |
| 628 | `NtSetLowWaitHighEventPair` | `0x163730` | 24 | UnwindData |  |
| 2275 | `ZwSetLowWaitHighEventPair` | `0x163730` | 24 | UnwindData |  |
| 629 | `NtSetQuotaInformationFile` | `0x163750` | 24 | UnwindData |  |
| 2276 | `ZwSetQuotaInformationFile` | `0x163750` | 24 | UnwindData |  |
| 630 | `NtSetSecurityObject` | `0x163770` | 24 | UnwindData |  |
| 2277 | `ZwSetSecurityObject` | `0x163770` | 24 | UnwindData |  |
| 631 | `NtSetSystemEnvironmentValue` | `0x163790` | 24 | UnwindData |  |
| 2278 | `ZwSetSystemEnvironmentValue` | `0x163790` | 24 | UnwindData |  |
| 632 | `NtSetSystemEnvironmentValueEx` | `0x1637B0` | 24 | UnwindData |  |
| 2279 | `ZwSetSystemEnvironmentValueEx` | `0x1637B0` | 24 | UnwindData |  |
| 633 | `NtSetSystemInformation` | `0x1637D0` | 24 | UnwindData |  |
| 2280 | `ZwSetSystemInformation` | `0x1637D0` | 24 | UnwindData |  |
| 634 | `NtSetSystemPowerState` | `0x1637F0` | 24 | UnwindData |  |
| 2281 | `ZwSetSystemPowerState` | `0x1637F0` | 24 | UnwindData |  |
| 635 | `NtSetSystemTime` | `0x163810` | 24 | UnwindData |  |
| 2282 | `ZwSetSystemTime` | `0x163810` | 24 | UnwindData |  |
| 636 | `NtSetThreadExecutionState` | `0x163830` | 24 | UnwindData |  |
| 2283 | `ZwSetThreadExecutionState` | `0x163830` | 24 | UnwindData |  |
| 638 | `NtSetTimer2` | `0x163850` | 24 | UnwindData |  |
| 2285 | `ZwSetTimer2` | `0x163850` | 24 | UnwindData |  |
| 639 | `NtSetTimerEx` | `0x163870` | 24 | UnwindData |  |
| 2286 | `ZwSetTimerEx` | `0x163870` | 24 | UnwindData |  |
| 640 | `NtSetTimerResolution` | `0x163890` | 24 | UnwindData |  |
| 2287 | `ZwSetTimerResolution` | `0x163890` | 24 | UnwindData |  |
| 641 | `NtSetUuidSeed` | `0x1638B0` | 24 | UnwindData |  |
| 2288 | `ZwSetUuidSeed` | `0x1638B0` | 24 | UnwindData |  |
| 643 | `NtSetVolumeInformationFile` | `0x1638D0` | 24 | UnwindData |  |
| 2290 | `ZwSetVolumeInformationFile` | `0x1638D0` | 24 | UnwindData |  |
| 644 | `NtSetWnfProcessNotificationEvent` | `0x1638F0` | 24 | UnwindData |  |
| 2291 | `ZwSetWnfProcessNotificationEvent` | `0x1638F0` | 24 | UnwindData |  |
| 645 | `NtShutdownSystem` | `0x163910` | 24 | UnwindData |  |
| 2292 | `ZwShutdownSystem` | `0x163910` | 24 | UnwindData |  |
| 646 | `NtShutdownWorkerFactory` | `0x163930` | 24 | UnwindData |  |
| 2293 | `ZwShutdownWorkerFactory` | `0x163930` | 24 | UnwindData |  |
| 647 | `NtSignalAndWaitForSingleObject` | `0x163950` | 24 | UnwindData |  |
| 2294 | `ZwSignalAndWaitForSingleObject` | `0x163950` | 24 | UnwindData |  |
| 648 | `NtSinglePhaseReject` | `0x163970` | 24 | UnwindData |  |
| 2295 | `ZwSinglePhaseReject` | `0x163970` | 24 | UnwindData |  |
| 649 | `NtStartProfile` | `0x163990` | 24 | UnwindData |  |
| 2296 | `ZwStartProfile` | `0x163990` | 24 | UnwindData |  |
| 650 | `NtStopProfile` | `0x1639B0` | 24 | UnwindData |  |
| 2297 | `ZwStopProfile` | `0x1639B0` | 24 | UnwindData |  |
| 651 | `NtSubmitIoRing` | `0x1639D0` | 24 | UnwindData |  |
| 2298 | `ZwSubmitIoRing` | `0x1639D0` | 24 | UnwindData |  |
| 652 | `NtSubscribeWnfStateChange` | `0x1639F0` | 24 | UnwindData |  |
| 2299 | `ZwSubscribeWnfStateChange` | `0x1639F0` | 24 | UnwindData |  |
| 653 | `NtSuspendProcess` | `0x163A10` | 24 | UnwindData |  |
| 2300 | `ZwSuspendProcess` | `0x163A10` | 24 | UnwindData |  |
| 654 | `NtSuspendThread` | `0x163A30` | 24 | UnwindData |  |
| 2301 | `ZwSuspendThread` | `0x163A30` | 24 | UnwindData |  |
| 655 | `NtSystemDebugControl` | `0x163A50` | 24 | UnwindData |  |
| 2302 | `ZwSystemDebugControl` | `0x163A50` | 24 | UnwindData |  |
| 656 | `NtTerminateEnclave` | `0x163A70` | 24 | UnwindData |  |
| 2303 | `ZwTerminateEnclave` | `0x163A70` | 24 | UnwindData |  |
| 657 | `NtTerminateJobObject` | `0x163A90` | 24 | UnwindData |  |
| 2304 | `ZwTerminateJobObject` | `0x163A90` | 24 | UnwindData |  |
| 660 | `NtTestAlert` | `0x163AB0` | 24 | UnwindData |  |
| 2307 | `ZwTestAlert` | `0x163AB0` | 24 | UnwindData |  |
| 661 | `NtThawRegistry` | `0x163AD0` | 24 | UnwindData |  |
| 2308 | `ZwThawRegistry` | `0x163AD0` | 24 | UnwindData |  |
| 662 | `NtThawTransactions` | `0x163AF0` | 24 | UnwindData |  |
| 2309 | `ZwThawTransactions` | `0x163AF0` | 24 | UnwindData |  |
| 663 | `NtTraceControl` | `0x163B10` | 24 | UnwindData |  |
| 2310 | `ZwTraceControl` | `0x163B10` | 24 | UnwindData |  |
| 665 | `NtTranslateFilePath` | `0x163B30` | 24 | UnwindData |  |
| 2312 | `ZwTranslateFilePath` | `0x163B30` | 24 | UnwindData |  |
| 666 | `NtUmsThreadYield` | `0x163B50` | 24 | UnwindData |  |
| 2313 | `ZwUmsThreadYield` | `0x163B50` | 24 | UnwindData |  |
| 667 | `NtUnloadDriver` | `0x163B70` | 24 | UnwindData |  |
| 2314 | `ZwUnloadDriver` | `0x163B70` | 24 | UnwindData |  |
| 668 | `NtUnloadKey` | `0x163B90` | 24 | UnwindData |  |
| 2315 | `ZwUnloadKey` | `0x163B90` | 24 | UnwindData |  |
| 669 | `NtUnloadKey2` | `0x163BB0` | 24 | UnwindData |  |
| 2316 | `ZwUnloadKey2` | `0x163BB0` | 24 | UnwindData |  |
| 670 | `NtUnloadKeyEx` | `0x163BD0` | 24 | UnwindData |  |
| 2317 | `ZwUnloadKeyEx` | `0x163BD0` | 24 | UnwindData |  |
| 671 | `NtUnlockFile` | `0x163BF0` | 24 | UnwindData |  |
| 2318 | `ZwUnlockFile` | `0x163BF0` | 24 | UnwindData |  |
| 672 | `NtUnlockVirtualMemory` | `0x163C10` | 24 | UnwindData |  |
| 2319 | `ZwUnlockVirtualMemory` | `0x163C10` | 24 | UnwindData |  |
| 674 | `NtUnmapViewOfSectionEx` | `0x163C30` | 24 | UnwindData |  |
| 2321 | `ZwUnmapViewOfSectionEx` | `0x163C30` | 24 | UnwindData |  |
| 675 | `NtUnsubscribeWnfStateChange` | `0x163C50` | 24 | UnwindData |  |
| 2322 | `ZwUnsubscribeWnfStateChange` | `0x163C50` | 24 | UnwindData |  |
| 676 | `NtUpdateWnfStateData` | `0x163C70` | 24 | UnwindData |  |
| 2323 | `ZwUpdateWnfStateData` | `0x163C70` | 24 | UnwindData |  |
| 677 | `NtVdmControl` | `0x163C90` | 24 | UnwindData |  |
| 2324 | `ZwVdmControl` | `0x163C90` | 24 | UnwindData |  |
| 678 | `NtWaitForAlertByThreadId` | `0x163CB0` | 24 | UnwindData |  |
| 2325 | `ZwWaitForAlertByThreadId` | `0x163CB0` | 24 | UnwindData |  |
| 679 | `NtWaitForDebugEvent` | `0x163CD0` | 24 | UnwindData |  |
| 2326 | `ZwWaitForDebugEvent` | `0x163CD0` | 24 | UnwindData |  |
| 680 | `NtWaitForKeyedEvent` | `0x163CF0` | 24 | UnwindData |  |
| 2327 | `ZwWaitForKeyedEvent` | `0x163CF0` | 24 | UnwindData |  |
| 684 | `NtWaitForWorkViaWorkerFactory` | `0x163D10` | 24 | UnwindData |  |
| 2331 | `ZwWaitForWorkViaWorkerFactory` | `0x163D10` | 24 | UnwindData |  |
| 685 | `NtWaitHighEventPair` | `0x163D30` | 24 | UnwindData |  |
| 2332 | `ZwWaitHighEventPair` | `0x163D30` | 24 | UnwindData |  |
| 686 | `NtWaitLowEventPair` | `0x163D50` | 24 | UnwindData |  |
| 2333 | `ZwWaitLowEventPair` | `0x163D50` | 24 | UnwindData |  |
| 395 | `NtGetTickCount` | `0x163D70` | 5 | UnwindData |  |
| 1035 | `RtlFirstEntrySList` | `0x163DC0` | 7 | UnwindData |  |
| 1217 | `RtlInterlockedPopEntrySList` | `0x163DD0` | 52 | UnwindData |  |
| 105 | `ExpInterlockedPopEntrySListResume` | `0x163DD7` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `ExpInterlockedPopEntrySListFault` | `0x163DE7` | 9 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `ExpInterlockedPopEntrySListEnd` | `0x163DF0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1219 | `RtlInterlockedPushListSList` | `0x163E80` | 51 | UnwindData |  |
| 107 | `KiUserApcDispatcher` | `0x163F50` | 131 | UnwindData |  |
| 108 | `KiUserCallbackDispatcher` | `0x164070` | 59 | UnwindData |  |
| 109 | `KiUserExceptionDispatcher` | `0x1640C0` | 92 | UnwindData |  |
| 106 | `KiRaiseUserExceptionDispatcher` | `0x164130` | 73 | UnwindData |  |
| 969 | `RtlEnclaveCallDispatch` | `0x164190` | 103 | UnwindData |  |
| 970 | `RtlEnclaveCallDispatchReturn` | `0x1641C1` | 63 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `RtlCallEnclave` | `0x164200` | 207 | UnwindData |  |
| 782 | `RtlCallEnclaveReturn` | `0x16426B` | 117 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `RtlCompareMemory` | `0x1642E0` | 122 | UnwindData |  |
| 819 | `RtlCompareMemoryUlong` | `0x164360` | 36 | UnwindData |  |
| 848 | `RtlCopyMemoryNonTemporal` | `0x164390` | 270 | UnwindData |  |
| 1010 | `RtlFillMemoryNonTemporal` | `0x1644D0` | 233 | UnwindData |  |
| 1079 | `RtlGetCurrentProcessorNumber` | `0x1645D0` | 97 | UnwindData |  |
| 1080 | `RtlGetCurrentProcessorNumberEx` | `0x164640` | 92 | UnwindData |  |
| 1418 | `RtlRaiseExceptionForReturnAddressHijack` | `0x1646B0` | 69 | UnwindData |  |
| 2341 | `__chkstk` | `0x164710` | 77 | UnwindData |  |
| 2367 | `_setjmp` | `0x1654A0` | 144 | UnwindData |  |
| 2368 | `_setjmpex` | `0x165560` | 144 | UnwindData |  |
| 847 | `RtlCopyMemory` | `0x1657C0` | 682 | UnwindData |  |
| 1316 | `RtlMoveMemory` | `0x1657C0` | 682 | UnwindData |  |
| 2455 | `memcpy` | `0x1657C0` | 682 | UnwindData |  |
| 2457 | `memmove` | `0x1657C0` | 682 | UnwindData |  |
| 2454 | `memcmp` | `0x165A90` | 199 | UnwindData |  |
| 2469 | `strcat` | `0x165E30` | 179 | UnwindData |  |
| 2473 | `strcpy` | `0x165EF0` | 183 | UnwindData |  |
| 2472 | `strcmp` | `0x165FD0` | 176 | UnwindData |  |
| 2476 | `strlen` | `0x1660A0` | 168 | UnwindData |  |
| 2477 | `strncat` | `0x166170` | 413 | UnwindData |  |
| 2479 | `strncmp` | `0x166330` | 181 | UnwindData |  |
| 2480 | `strncpy` | `0x166410` | 362 | UnwindData |  |
| 755 | `RtlAllocateMemoryBlockLookaside` | `0x16F010` | 291 | UnwindData |  |
| 756 | `RtlAllocateMemoryZone` | `0x16F140` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1054 | `RtlFreeMemoryBlockLookaside` | `0x16F1A0` | 28 | UnwindData |  |
| 2459 | `memset` | `0x171030` | 9,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1731 | `RtlpScpCfgNtdllExports` | `0x173670` | 1,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1335 | `RtlNtdllName` | `0x173DB0` | 92,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2349 | `_fltused` | `0x18A788` | 268,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `NlsAnsiCodePage` | `0x1CC048` | 5,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `NlsMbOemCodePageTag` | `0x1CD440` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `NlsMbCodePageTag` | `0x1CD650` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1705 | `RtlpFreezeTimeBias` | `0x1CD6D0` | 101,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `KiUserInvertedFunctionTable` | `0x1E6430` | 12,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `LdrSystemDllInitBlock` | `0x1E9450` | 0 | Indeterminate |  |
