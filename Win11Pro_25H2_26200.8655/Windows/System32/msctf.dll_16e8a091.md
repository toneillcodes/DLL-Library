# Binary Specification: msctf.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msctf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `16e8a0918dae628ecefa7d82b6b4dedd1535ab0a31de521e58ee8ca970868bc1`
* **Total Exported Functions:** 78

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `CtfImeCreateThreadMgr` | `0xD8C0` | 94 | UnwindData |  |
| 45 | `TF_CanUninitialize` | `0xDE70` | 156 | UnwindData |  |
| 48 | `TF_CreateCicLoadMutex` | `0x13760` | 164 | UnwindData |  |
| 78 | `TextInputClientWrapperCreate` | `0x145C0` | 410 | UnwindData |  |
| 8 | `CtfImeDestroyInputContext` | `0x15E30` | 76 | UnwindData |  |
| 9 | `CtfImeDestroyThreadMgr` | `0x16A20` | 66 | UnwindData |  |
| 21 | `CtfImeProcessKey` | `0x177B0` | 84 | UnwindData |  |
| 25 | `CtfImeSetActiveContext` | `0x196F0` | 1,079 | UnwindData |  |
| 55 | `TF_GetAppCompatFlags` | `0x19B30` | 65 | UnwindData |  |
| 30 | `CtfNotifyIME` | `0x22420` | 222 | UnwindData |  |
| 17 | `CtfImeInquireExW` | `0x22B30` | 423 | UnwindData |  |
| 2 | `CtfImeAssociateFocus` | `0x23460` | 323 | UnwindData |  |
| 59 | `TF_GetInputScope` | `0x26110` | 190 | UnwindData |  |
| 62 | `TF_GetThreadMgr` | `0x265C0` | 86 | UnwindData |  |
| 20 | `CtfImeProcessCicHotkey` | `0x26A20` | 551 | UnwindData |  |
| 58 | `TF_GetInitSystemFlags` | `0x26D40` | 79 | UnwindData |  |
| 37 | `HasDeferredInputForCoreDispatcher` | `0x26DA0` | 99 | UnwindData |  |
| 10 | `CtfImeDispatchDefImeMessage` | `0x39870` | 162 | UnwindData |  |
| 54 | `TF_CreateThreadMgr` | `0x421F0` | 18 | UnwindData |  |
| 51 | `TF_CreateInputProcessorProfiles` | `0x42C00` | 191 | UnwindData |  |
| 43 | `SetInputScopes2` | `0x4E5B0` | 59 | UnwindData |  |
| 40 | `SetInputScope` | `0x4E600` | 352 | UnwindData |  |
| 49 | `TF_CreateCicLoadWinStaMutex` | `0x4F0E0` | 265 | UnwindData |  |
| 61 | `TF_GetThreadFlags` | `0x5E130` | 223 | UnwindData |  |
| 31 | `DllCanUnloadNow` | `0x6C6C0` | 18,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `TF_CreateCategoryMgr` | `0x71030` | 169 | UnwindData |  |
| 19 | `CtfImeIsIME` | `0x722C0` | 80 | UnwindData |  |
| 5 | `CtfImeCreateInputContext` | `0x76F10` | 81 | UnwindData |  |
| 46 | `TF_CleanUpPrivateMessages` | `0x78C80` | 14,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `TF_WaitForInitialized` | `0x78C80` | 14,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `DllGetClassObject` | `0x7C500` | 16,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `CtfImeSelectEx` | `0x804E0` | 5,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `CtfImeIsGuidMapEnable` | `0x81A80` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `InputFocusMonitorCreate` | `0x81FA0` | 3,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `TF_CreateLangBarMgr` | `0x82DB0` | 4,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `TF_Notify` | `0x84060` | 2,397 | UnwindData |  |
| 64 | `TF_InvalidAssemblyListCacheIfExist` | `0x85D60` | 16,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `TF_IsThreadWithFlags` | `0x85D60` | 16,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `TF_SetThreadFlags` | `0x85D60` | 16,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `SetInputScopes` | `0x89C10` | 63 | UnwindData |  |
| 76 | `TF_UninitSystem` | `0x8A570` | 211 | UnwindData |  |
| 14 | `CtfImeGetGuidAtom` | `0x8B300` | 106 | UnwindData |  |
| 52 | `TF_CreateLangBarItemMgr` | `0x8B600` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `GetLogonUserSid` | `0x8B6E0` | 239 | UnwindData |  |
| 60 | `TF_GetShowFloatingStatus` | `0x8BB50` | 1,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `CtfImeToAsciiEx` | `0x8C160` | 30,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `DllRegisterServer` | `0x938B0` | 879 | UnwindData |  |
| 34 | `DllUnregisterServer` | `0x93C30` | 474 | UnwindData |  |
| 1 | `TF_RunInputCPL` | `0x97950` | 220 | UnwindData |  |
| 3 | `CtfImeConfigure` | `0x97AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CtfImeConversionList` | `0x97AE0` | 29 | UnwindData |  |
| 7 | `CtfImeDestroy` | `0x97B10` | 29 | UnwindData |  |
| 11 | `CtfImeEnumRegisterWord` | `0x97B40` | 29 | UnwindData |  |
| 12 | `CtfImeEscape` | `0x97B70` | 29 | UnwindData |  |
| 13 | `CtfImeEscapeEx` | `0x97BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `CtfImeGetRegisterWordStyle` | `0x97BB0` | 29 | UnwindData |  |
| 16 | `CtfImeInquire` | `0x97BE0` | 29 | UnwindData |  |
| 22 | `CtfImeRegisterWord` | `0x97C10` | 29 | UnwindData |  |
| 23 | `CtfImeSelect` | `0x97C40` | 29 | UnwindData |  |
| 26 | `CtfImeSetCompositionString` | `0x97C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `CtfImeSetFocus` | `0x97C80` | 126 | UnwindData |  |
| 29 | `CtfImeUnregisterWord` | `0x97D10` | 29 | UnwindData |  |
| 35 | `GetHandwritingStrokeIdForPointer` | `0x97D40` | 173 | UnwindData |  |
| 39 | `RegisterHandwritingInputRoutingCallback` | `0x97E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `TF_CUASAppFix` | `0x97E10` | 57 | UnwindData |  |
| 50 | `TF_CreateDisplayAttributeMgr` | `0x97E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `TF_GetCompatibleKeyboardLayout` | `0x97E70` | 328 | UnwindData |  |
| 57 | `TF_GetGlobalCompartment` | `0x97FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `TF_IsLanguageBarEnabled` | `0x97FD0` | 240 | UnwindData |  |
| 68 | `TF_MapCompatibleHKL` | `0x980D0` | 145 | UnwindData |  |
| 69 | `TF_MapCompatibleKeyboardTip` | `0x98170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `TF_PostAllThreadMsg` | `0x98180` | 103 | UnwindData |  |
| 72 | `TF_SendLangBandMsg` | `0x981F0` | 173 | UnwindData |  |
| 73 | `TF_SetDefaultRemoteKeyboardLayout` | `0x982B0` | 603 | UnwindData |  |
| 63 | `TF_InitSystem` | `0x9A830` | 600 | UnwindData |  |
| 65 | `TF_IsCtfmonRunning` | `0xA42E0` | 51,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `SetInputScopeXML` | `0xB0B20` | 59 | UnwindData |  |
| 74 | `TF_SetShowFloatingStatus` | `0xB35E0` | 390,636 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
