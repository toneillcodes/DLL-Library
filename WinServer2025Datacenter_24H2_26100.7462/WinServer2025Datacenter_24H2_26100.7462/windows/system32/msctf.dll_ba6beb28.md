# Binary Specification: msctf.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msctf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ba6beb28a670308676a2d6067e2fce0873c34770d89a7ba94dadc74b8e1ab9a1`
* **Total Exported Functions:** 78

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 30 | `CtfNotifyIME` | `0xC1F0` | 222 | UnwindData |  |
| 17 | `CtfImeInquireExW` | `0xC900` | 423 | UnwindData |  |
| 2 | `CtfImeAssociateFocus` | `0xD230` | 323 | UnwindData |  |
| 59 | `TF_GetInputScope` | `0xFEE0` | 190 | UnwindData |  |
| 62 | `TF_GetThreadMgr` | `0x10390` | 86 | UnwindData |  |
| 20 | `CtfImeProcessCicHotkey` | `0x107F0` | 551 | UnwindData |  |
| 58 | `TF_GetInitSystemFlags` | `0x10B10` | 79 | UnwindData |  |
| 37 | `HasDeferredInputForCoreDispatcher` | `0x10B70` | 99 | UnwindData |  |
| 25 | `CtfImeSetActiveContext` | `0x1B730` | 1,079 | UnwindData |  |
| 55 | `TF_GetAppCompatFlags` | `0x1BB70` | 65 | UnwindData |  |
| 45 | `TF_CanUninitialize` | `0x29800` | 156 | UnwindData |  |
| 48 | `TF_CreateCicLoadMutex` | `0x2ED00` | 164 | UnwindData |  |
| 78 | `TextInputClientWrapperCreate` | `0x2FBC0` | 410 | UnwindData |  |
| 6 | `CtfImeCreateThreadMgr` | `0x309B0` | 94 | UnwindData |  |
| 54 | `TF_CreateThreadMgr` | `0x32120` | 18 | UnwindData |  |
| 51 | `TF_CreateInputProcessorProfiles` | `0x32B30` | 191 | UnwindData |  |
| 8 | `CtfImeDestroyInputContext` | `0x338D0` | 76 | UnwindData |  |
| 9 | `CtfImeDestroyThreadMgr` | `0x33F60` | 66 | UnwindData |  |
| 10 | `CtfImeDispatchDefImeMessage` | `0x3AB60` | 162 | UnwindData |  |
| 21 | `CtfImeProcessKey` | `0x3BCA0` | 84 | UnwindData |  |
| 43 | `SetInputScopes2` | `0x50C30` | 59 | UnwindData |  |
| 40 | `SetInputScope` | `0x50C80` | 352 | UnwindData |  |
| 49 | `TF_CreateCicLoadWinStaMutex` | `0x51760` | 265 | UnwindData |  |
| 61 | `TF_GetThreadFlags` | `0x5FBD0` | 223 | UnwindData |  |
| 19 | `CtfImeIsIME` | `0x6AEA0` | 124 | UnwindData |  |
| 31 | `DllCanUnloadNow` | `0x6D2C0` | 19,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `TF_CreateCategoryMgr` | `0x71FA0` | 169 | UnwindData |  |
| 5 | `CtfImeCreateInputContext` | `0x78610` | 81 | UnwindData |  |
| 46 | `TF_CleanUpPrivateMessages` | `0x79FF0` | 16,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `TF_WaitForInitialized` | `0x79FF0` | 16,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `DllGetClassObject` | `0x7E120` | 15,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `CtfImeSelectEx` | `0x81CB0` | 5,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `CtfImeIsGuidMapEnable` | `0x83250` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `InputFocusMonitorCreate` | `0x83770` | 3,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `TF_CreateLangBarMgr` | `0x84580` | 1,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `TF_Notify` | `0x84C70` | 2,851 | UnwindData |  |
| 64 | `TF_InvalidAssemblyListCacheIfExist` | `0x869E0` | 15,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `TF_IsThreadWithFlags` | `0x869E0` | 15,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `TF_SetThreadFlags` | `0x869E0` | 15,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `SetInputScopes` | `0x8A7C0` | 63 | UnwindData |  |
| 76 | `TF_UninitSystem` | `0x8B120` | 211 | UnwindData |  |
| 14 | `CtfImeGetGuidAtom` | `0x8BEB0` | 106 | UnwindData |  |
| 52 | `TF_CreateLangBarItemMgr` | `0x8C1B0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `GetLogonUserSid` | `0x8C290` | 239 | UnwindData |  |
| 60 | `TF_GetShowFloatingStatus` | `0x8C700` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `CtfImeToAsciiEx` | `0x8CD80` | 30,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `DllRegisterServer` | `0x94360` | 879 | UnwindData |  |
| 34 | `DllUnregisterServer` | `0x946E0` | 474 | UnwindData |  |
| 1 | `TF_RunInputCPL` | `0x96230` | 220 | UnwindData |  |
| 3 | `CtfImeConfigure` | `0x963B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CtfImeConversionList` | `0x963C0` | 29 | UnwindData |  |
| 7 | `CtfImeDestroy` | `0x963F0` | 29 | UnwindData |  |
| 11 | `CtfImeEnumRegisterWord` | `0x96420` | 29 | UnwindData |  |
| 12 | `CtfImeEscape` | `0x96450` | 29 | UnwindData |  |
| 13 | `CtfImeEscapeEx` | `0x96480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `CtfImeGetRegisterWordStyle` | `0x96490` | 29 | UnwindData |  |
| 16 | `CtfImeInquire` | `0x964C0` | 29 | UnwindData |  |
| 22 | `CtfImeRegisterWord` | `0x964F0` | 29 | UnwindData |  |
| 23 | `CtfImeSelect` | `0x96520` | 29 | UnwindData |  |
| 26 | `CtfImeSetCompositionString` | `0x96550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `CtfImeSetFocus` | `0x96560` | 126 | UnwindData |  |
| 29 | `CtfImeUnregisterWord` | `0x965F0` | 29 | UnwindData |  |
| 35 | `GetHandwritingStrokeIdForPointer` | `0x96620` | 173 | UnwindData |  |
| 39 | `RegisterHandwritingInputRoutingCallback` | `0x966E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `TF_CUASAppFix` | `0x966F0` | 57 | UnwindData |  |
| 50 | `TF_CreateDisplayAttributeMgr` | `0x96730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `TF_GetCompatibleKeyboardLayout` | `0x96750` | 328 | UnwindData |  |
| 57 | `TF_GetGlobalCompartment` | `0x968A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `TF_IsLanguageBarEnabled` | `0x968B0` | 240 | UnwindData |  |
| 68 | `TF_MapCompatibleHKL` | `0x969B0` | 145 | UnwindData |  |
| 69 | `TF_MapCompatibleKeyboardTip` | `0x96A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `TF_PostAllThreadMsg` | `0x96A60` | 103 | UnwindData |  |
| 72 | `TF_SendLangBandMsg` | `0x96AD0` | 173 | UnwindData |  |
| 73 | `TF_SetDefaultRemoteKeyboardLayout` | `0x96B90` | 603 | UnwindData |  |
| 63 | `TF_InitSystem` | `0x9B240` | 600 | UnwindData |  |
| 65 | `TF_IsCtfmonRunning` | `0xA6890` | 49,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `SetInputScopeXML` | `0xB29C0` | 59 | UnwindData |  |
| 74 | `TF_SetShowFloatingStatus` | `0xB5480` | 391,920 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
