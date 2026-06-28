# Binary Specification: imm32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\imm32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a9c460d2e4b17e3b59a3c9e4462d0733264a4e817988a7f41768caf7a662f90e`
* **Total Exported Functions:** 137

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 126 | `ImmSetHotKey` | `0x0` | - | Forwarded | Forwarded to: `USER32.CliImmSetHotKey` |
| 70 | `ImmGetCompositionFontA` | `0x1010` | 251 | UnwindData |  |
| 63 | `ImmGenerateMessage` | `0x11B0` | 451 | UnwindData |  |
| 124 | `ImmSetCompositionWindow` | `0x1D30` | 295 | UnwindData |  |
| 119 | `ImmSetCandidateWindow` | `0x1F50` | 197 | UnwindData |  |
| 131 | `ImmTranslateMessage` | `0x2020` | 826 | UnwindData |  |
| 121 | `ImmSetCompositionFontW` | `0x2360` | 474 | UnwindData |  |
| 125 | `ImmSetConversionStatus` | `0x2540` | 350 | UnwindData |  |
| 127 | `ImmSetOpenStatus` | `0x26B0` | 340 | UnwindData |  |
| 74 | `ImmGetCompositionWindow` | `0x2D60` | 322 | UnwindData |  |
| 71 | `ImmGetCompositionFontW` | `0x2F80` | 444 | UnwindData |  |
| 64 | `ImmGetAppCompatFlags` | `0x3420` | 131 | UnwindData |  |
| 111 | `ImmProcessKey` | `0x34B0` | 1,891 | UnwindData |  |
| 78 | `ImmGetConversionStatus` | `0x3C20` | 290 | UnwindData |  |
| 69 | `ImmGetCandidateWindow` | `0x3E20` | 276 | UnwindData |  |
| 93 | `ImmGetOpenStatus` | `0x4030` | 179 | UnwindData |  |
| 75 | `ImmGetContext` | `0x4450` | 25 | UnwindData |  |
| 106 | `ImmLockClientImc` | `0x46D0` | 746 | UnwindData |  |
| 132 | `ImmUnlockClientImc` | `0x49C0` | 99 | UnwindData |  |
| 107 | `ImmLockIMC` | `0x4A30` | 1,121 | UnwindData |  |
| 133 | `ImmUnlockIMC` | `0x4FE0` | 634 | UnwindData |  |
| 73 | `ImmGetCompositionStringW` | `0x5260` | 220 | UnwindData |  |
| 108 | `ImmLockIMCC` | `0x5440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `ImmSetActiveContext` | `0x5460` | 473 | UnwindData |  |
| 109 | `ImmLockImeDpi` | `0x5700` | 29 | UnwindData |  |
| 135 | `ImmUnlockImeDpi` | `0x57D0` | 182 | UnwindData |  |
| 40 | `CtfImmTIMActivate` | `0x5AF0` | 282 | UnwindData |  |
| 26 | `CtfImmGetTMAEFlags` | `0x5D80` | 110 | UnwindData |  |
| 110 | `ImmNotifyIME` | `0x5FE0` | 173 | UnwindData |  |
| 134 | `ImmUnlockIMCC` | `0x67B0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `ImmGetProperty` | `0x6AB0` | 435 | UnwindData |  |
| 21 | `CtfImmGenerateMessage` | `0x6C70` | 425 | UnwindData |  |
| 31 | `CtfImmIsGuidMapEnable` | `0x6E20` | 132 | UnwindData |  |
| 42 | `ImmActivateLayout` | `0x6EB0` | 536 | UnwindData |  |
| 104 | `ImmLoadIME` | `0x70D0` | 417 | UnwindData |  |
| 57 | `ImmEnumInputContext` | `0x7C20` | 184 | UnwindData |  |
| 48 | `ImmCreateIMCC` | `0x8810` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `ImmSystemHandler` | `0x8840` | 107 | UnwindData |  |
| 51 | `ImmDestroyIMCC` | `0x89B0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `ImmCreateContext` | `0x8A70` | 154 | UnwindData |  |
| 19 | `CtfImmDispatchDefImeMessage` | `0x8BE0` | 131 | UnwindData |  |
| 9 | `ImmRegisterClient` | `0x8CB0` | 387 | UnwindData |  |
| 34 | `CtfImmLeaveCoInitCountSkipMode` | `0x8F00` | 42 | UnwindData |  |
| 20 | `CtfImmEnterCoInitCountSkipMode` | `0x8F30` | 30 | UnwindData |  |
| 18 | `CtfImmCoUninitialize` | `0x8F60` | 139 | UnwindData |  |
| 35 | `CtfImmNotify` | `0x9070` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `ImmGetIMEFileNameW` | `0x9230` | 84 | UnwindData |  |
| 29 | `CtfImmIsCiceroStartedInThread` | `0x9420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `ImmGetIMCCSize` | `0x9440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `ImmReleaseContext` | `0x9460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `ImmIsIME` | `0x9480` | 258 | UnwindData |  |
| 103 | `ImmIsUIMessageW` | `0x9590` | 84 | UnwindData |  |
| 38 | `CtfImmSetCiceroStartInThread` | `0x96A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `ImmAssociateContext` | `0x96D0` | 403 | UnwindData |  |
| 102 | `ImmIsUIMessageA` | `0x98D0` | 84 | UnwindData |  |
| 79 | `ImmGetDefaultIMEWnd` | `0x9930` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `ImmGetDescriptionW` | `0x9980` | 206 | UnwindData |  |
| 90 | `ImmGetImeInfoEx` | `0x9A60` | 217 | UnwindData |  |
| 55 | `ImmDisableLegacyIME` | `0x9B40` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `CtfImmLastEnabledWndDestroy` | `0x9BB0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `CtfImmGetGuidAtom` | `0x9C60` | 174 | UnwindData |  |
| 37 | `CtfImmSetAppCompatFlags` | `0x9D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `ImmDisableIME` | `0x9D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `ImmDisableIme` | `0x9D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `ImmRequestMessageW` | `0x9D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `ImmGetIMCCLockCount` | `0x9D70` | 34 | UnwindData |  |
| 84 | `ImmGetHotKey` | `0x9DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `ImmReSizeIMCC` | `0x9DC0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `ImmAssociateContextEx` | `0x9E30` | 351 | UnwindData |  |
| 27 | `CtfImmHideToolbarWnd` | `0x9FA0` | 162 | UnwindData |  |
| 36 | `CtfImmRestoreToolbarWnd` | `0xA080` | 82 | UnwindData |  |
| 98 | `ImmGetVirtualKey` | `0xA380` | 87 | UnwindData |  |
| 120 | `ImmSetCompositionFontA` | `0xA3E0` | 428 | UnwindData |  |
| 72 | `ImmGetCompositionStringA` | `0xAE00` | 208 | UnwindData |  |
| 87 | `ImmGetIMCLockCount` | `0xB280` | 70 | UnwindData |  |
| 39 | `CtfImmSetDefaultRemoteKeyboardLayout` | `0xB490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `CtfImmIsTextFrameServiceDisabled` | `0xB4B0` | 4,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `ImmDisableTextFrameService` | `0xB4B0` | 4,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ImmWINNLSGetIMEHotkey` | `0xB4B0` | 4,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `CtfImmAppCompatEnableIMEonProtectedCode` | `0xC4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `CtfImmGetCompatibleKeyboardLayout` | `0xC4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `CtfImmGetGlobalIMEStatus` | `0xC500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `CtfImmGetIMEFileName` | `0xC520` | 255 | UnwindData |  |
| 28 | `CtfImmIsCiceroEnabled` | `0xC630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `CtfImmIsComStartedInThread` | `0xC650` | 3,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `ImmDestroyContext` | `0xD2A0` | 110 | UnwindData |  |
| 65 | `ImmGetCandidateListA` | `0xDC60` | 23 | UnwindData |  |
| 66 | `ImmGetCandidateListCountA` | `0xDC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `ImmGetCandidateListCountW` | `0xDCA0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `ImmGetCandidateListW` | `0xDE00` | 20 | UnwindData |  |
| 76 | `ImmGetConversionListA` | `0xDE20` | 510 | UnwindData |  |
| 77 | `ImmGetConversionListW` | `0xE030` | 522 | UnwindData |  |
| 82 | `ImmGetGuideLineA` | `0xE240` | 23 | UnwindData |  |
| 83 | `ImmGetGuideLineW` | `0xE260` | 20 | UnwindData |  |
| 97 | `ImmGetStatusWindowPos` | `0xE550` | 84 | UnwindData |  |
| 116 | `ImmRequestMessageA` | `0xE5B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `ImmSetCompositionStringA` | `0xE5D0` | 41 | UnwindData |  |
| 123 | `ImmSetCompositionStringW` | `0xE600` | 38 | UnwindData |  |
| 128 | `ImmSetStatusWindowPos` | `0xEC10` | 163 | UnwindData |  |
| 130 | `ImmSimulateHotKey` | `0xF3F0` | 91 | UnwindData |  |
| 45 | `ImmConfigureIMEA` | `0xF460` | 658 | UnwindData |  |
| 46 | `ImmConfigureIMEW` | `0xF700` | 671 | UnwindData |  |
| 60 | `ImmEscapeA` | `0xF9B0` | 752 | UnwindData |  |
| 61 | `ImmEscapeW` | `0xFCB0` | 647 | UnwindData |  |
| 62 | `ImmFreeLayout` | `0xFF40` | 543 | UnwindData |  |
| 105 | `ImmLoadLayout` | `0x104E0` | 540 | UnwindData |  |
| 80 | `ImmGetDescriptionA` | `0x11070` | 248 | UnwindData |  |
| 88 | `ImmGetIMEFileNameA` | `0x11170` | 427 | UnwindData |  |
| 99 | `ImmInstallIMEA` | `0x11330` | 311 | UnwindData |  |
| 100 | `ImmInstallIMEW` | `0x11470` | 781 | UnwindData |  |
| 41 | `GetKeyboardLayoutCP` | `0x11790` | 129 | UnwindData |  |
| 58 | `ImmEnumRegisterWordA` | `0x11BA0` | 543 | UnwindData |  |
| 59 | `ImmEnumRegisterWordW` | `0x11DD0` | 575 | UnwindData |  |
| 95 | `ImmGetRegisterWordStyleA` | `0x12020` | 333 | UnwindData |  |
| 96 | `ImmGetRegisterWordStyleW` | `0x12180` | 327 | UnwindData |  |
| 113 | `ImmRegisterWordA` | `0x122D0` | 446 | UnwindData |  |
| 114 | `ImmRegisterWordW` | `0x124A0` | 489 | UnwindData |  |
| 136 | `ImmUnregisterWordA` | `0x12690` | 446 | UnwindData |  |
| 137 | `ImmUnregisterWordW` | `0x12860` | 489 | UnwindData |  |
| 49 | `ImmCreateSoftKeyboard` | `0x16C50` | 632 | UnwindData |  |
| 52 | `ImmDestroySoftKeyboard` | `0x16ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `ImmShowSoftKeyboard` | `0x16EF0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ImmIMPGetIMEA` | `0x172C0` | 151 | UnwindData |  |
| 3 | `ImmIMPGetIMEW` | `0x17360` | 72 | UnwindData |  |
| 4 | `ImmIMPQueryIMEA` | `0x173B0` | 191 | UnwindData |  |
| 5 | `ImmIMPQueryIMEW` | `0x17480` | 330 | UnwindData |  |
| 6 | `ImmIMPSetIMEA` | `0x175D0` | 187 | UnwindData |  |
| 7 | `ImmIMPSetIMEW` | `0x176A0` | 396 | UnwindData |  |
| 10 | `ImmSendIMEMessageExA` | `0x17840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ImmSendIMEMessageExW` | `0x17860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `ImmWINNLSEnableIME` | `0x17870` | 65 | UnwindData |  |
| 15 | `ImmWINNLSGetEnableStatus` | `0x178C0` | 76 | UnwindData |  |
| 1 | `ImmCallImeConsoleIME` | `0x1CBE0` | 362 | UnwindData |  |
| 12 | `ImmSetActiveContextConsoleIME` | `0x1CD50` | 51 | UnwindData |  |
| 8 | `ImmPutImeMenuItemsIntoMappedFile` | `0x1D7E0` | 873 | UnwindData |  |
| 91 | `ImmGetImeMenuItemsA` | `0x1DDD0` | 41 | UnwindData |  |
| 92 | `ImmGetImeMenuItemsW` | `0x1DE00` | 38 | UnwindData |  |
