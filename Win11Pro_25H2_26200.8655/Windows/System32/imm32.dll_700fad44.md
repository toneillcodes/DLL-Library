# Binary Specification: imm32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\imm32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `700fad44c3c8bd4ccd68b47464234197b378d1aeb95a249e036adfbe8e45eef0`
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
| 133 | `ImmUnlockIMC` | `0x5310` | 634 | UnwindData |  |
| 73 | `ImmGetCompositionStringW` | `0x5590` | 220 | UnwindData |  |
| 108 | `ImmLockIMCC` | `0x5770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `ImmSetActiveContext` | `0x5790` | 473 | UnwindData |  |
| 109 | `ImmLockImeDpi` | `0x5A30` | 29 | UnwindData |  |
| 135 | `ImmUnlockImeDpi` | `0x5B00` | 182 | UnwindData |  |
| 40 | `CtfImmTIMActivate` | `0x5E20` | 282 | UnwindData |  |
| 26 | `CtfImmGetTMAEFlags` | `0x60B0` | 143 | UnwindData |  |
| 110 | `ImmNotifyIME` | `0x6150` | 173 | UnwindData |  |
| 134 | `ImmUnlockIMCC` | `0x6920` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `ImmGetProperty` | `0x6C50` | 435 | UnwindData |  |
| 21 | `CtfImmGenerateMessage` | `0x6E10` | 425 | UnwindData |  |
| 31 | `CtfImmIsGuidMapEnable` | `0x6FC0` | 132 | UnwindData |  |
| 42 | `ImmActivateLayout` | `0x7050` | 536 | UnwindData |  |
| 104 | `ImmLoadIME` | `0x7270` | 417 | UnwindData |  |
| 57 | `ImmEnumInputContext` | `0x7DC0` | 184 | UnwindData |  |
| 48 | `ImmCreateIMCC` | `0x8980` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `ImmSystemHandler` | `0x89B0` | 107 | UnwindData |  |
| 51 | `ImmDestroyIMCC` | `0x8B20` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `ImmCreateContext` | `0x8BE0` | 154 | UnwindData |  |
| 19 | `CtfImmDispatchDefImeMessage` | `0x8E30` | 131 | UnwindData |  |
| 9 | `ImmRegisterClient` | `0x8F00` | 387 | UnwindData |  |
| 34 | `CtfImmLeaveCoInitCountSkipMode` | `0x9150` | 42 | UnwindData |  |
| 20 | `CtfImmEnterCoInitCountSkipMode` | `0x9180` | 30 | UnwindData |  |
| 18 | `CtfImmCoUninitialize` | `0x91B0` | 139 | UnwindData |  |
| 35 | `CtfImmNotify` | `0x93E0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `ImmGetIMEFileNameW` | `0x95A0` | 84 | UnwindData |  |
| 29 | `CtfImmIsCiceroStartedInThread` | `0x9790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `ImmGetIMCCSize` | `0x97B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `ImmReleaseContext` | `0x97D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `ImmIsIME` | `0x97F0` | 258 | UnwindData |  |
| 103 | `ImmIsUIMessageW` | `0x9900` | 84 | UnwindData |  |
| 38 | `CtfImmSetCiceroStartInThread` | `0x9A10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `ImmAssociateContext` | `0x9A40` | 403 | UnwindData |  |
| 102 | `ImmIsUIMessageA` | `0x9C40` | 84 | UnwindData |  |
| 79 | `ImmGetDefaultIMEWnd` | `0x9CA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `ImmGetDescriptionW` | `0x9CF0` | 206 | UnwindData |  |
| 90 | `ImmGetImeInfoEx` | `0x9DD0` | 217 | UnwindData |  |
| 55 | `ImmDisableLegacyIME` | `0x9EB0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `CtfImmLastEnabledWndDestroy` | `0x9F20` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `CtfImmGetGuidAtom` | `0x9FD0` | 174 | UnwindData |  |
| 37 | `CtfImmSetAppCompatFlags` | `0xA090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `ImmDisableIME` | `0xA0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `ImmDisableIme` | `0xA0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `ImmRequestMessageW` | `0xA0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `ImmGetIMCCLockCount` | `0xA0E0` | 34 | UnwindData |  |
| 84 | `ImmGetHotKey` | `0xA110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `ImmReSizeIMCC` | `0xA130` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `ImmAssociateContextEx` | `0xA1A0` | 351 | UnwindData |  |
| 27 | `CtfImmHideToolbarWnd` | `0xA310` | 162 | UnwindData |  |
| 36 | `CtfImmRestoreToolbarWnd` | `0xA3F0` | 82 | UnwindData |  |
| 98 | `ImmGetVirtualKey` | `0xA6F0` | 87 | UnwindData |  |
| 120 | `ImmSetCompositionFontA` | `0xA750` | 428 | UnwindData |  |
| 72 | `ImmGetCompositionStringA` | `0xB170` | 208 | UnwindData |  |
| 87 | `ImmGetIMCLockCount` | `0xB5F0` | 70 | UnwindData |  |
| 39 | `CtfImmSetDefaultRemoteKeyboardLayout` | `0xB800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `CtfImmIsTextFrameServiceDisabled` | `0xB820` | 4,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `ImmDisableTextFrameService` | `0xB820` | 4,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ImmWINNLSGetIMEHotkey` | `0xB820` | 4,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `CtfImmAppCompatEnableIMEonProtectedCode` | `0xC840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `CtfImmGetCompatibleKeyboardLayout` | `0xC860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `CtfImmGetGlobalIMEStatus` | `0xC880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `CtfImmGetIMEFileName` | `0xC8A0` | 255 | UnwindData |  |
| 28 | `CtfImmIsCiceroEnabled` | `0xC9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `CtfImmIsComStartedInThread` | `0xC9D0` | 3,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `ImmDestroyContext` | `0xD6D0` | 110 | UnwindData |  |
| 65 | `ImmGetCandidateListA` | `0xE090` | 23 | UnwindData |  |
| 66 | `ImmGetCandidateListCountA` | `0xE0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `ImmGetCandidateListCountW` | `0xE0D0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `ImmGetCandidateListW` | `0xE230` | 20 | UnwindData |  |
| 76 | `ImmGetConversionListA` | `0xE250` | 510 | UnwindData |  |
| 77 | `ImmGetConversionListW` | `0xE460` | 522 | UnwindData |  |
| 82 | `ImmGetGuideLineA` | `0xE670` | 23 | UnwindData |  |
| 83 | `ImmGetGuideLineW` | `0xE690` | 20 | UnwindData |  |
| 97 | `ImmGetStatusWindowPos` | `0xE980` | 84 | UnwindData |  |
| 116 | `ImmRequestMessageA` | `0xE9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `ImmSetCompositionStringA` | `0xEA00` | 41 | UnwindData |  |
| 123 | `ImmSetCompositionStringW` | `0xEA30` | 38 | UnwindData |  |
| 128 | `ImmSetStatusWindowPos` | `0xF040` | 163 | UnwindData |  |
| 130 | `ImmSimulateHotKey` | `0xF820` | 91 | UnwindData |  |
| 45 | `ImmConfigureIMEA` | `0xF890` | 658 | UnwindData |  |
| 46 | `ImmConfigureIMEW` | `0xFB30` | 671 | UnwindData |  |
| 60 | `ImmEscapeA` | `0xFDE0` | 752 | UnwindData |  |
| 61 | `ImmEscapeW` | `0x100E0` | 647 | UnwindData |  |
| 62 | `ImmFreeLayout` | `0x10370` | 695 | UnwindData |  |
| 105 | `ImmLoadLayout` | `0x109B0` | 540 | UnwindData |  |
| 80 | `ImmGetDescriptionA` | `0x11540` | 248 | UnwindData |  |
| 88 | `ImmGetIMEFileNameA` | `0x11640` | 427 | UnwindData |  |
| 99 | `ImmInstallIMEA` | `0x11800` | 311 | UnwindData |  |
| 100 | `ImmInstallIMEW` | `0x11940` | 781 | UnwindData |  |
| 41 | `GetKeyboardLayoutCP` | `0x11C60` | 129 | UnwindData |  |
| 58 | `ImmEnumRegisterWordA` | `0x12070` | 543 | UnwindData |  |
| 59 | `ImmEnumRegisterWordW` | `0x122A0` | 575 | UnwindData |  |
| 95 | `ImmGetRegisterWordStyleA` | `0x124F0` | 333 | UnwindData |  |
| 96 | `ImmGetRegisterWordStyleW` | `0x12650` | 327 | UnwindData |  |
| 113 | `ImmRegisterWordA` | `0x127A0` | 446 | UnwindData |  |
| 114 | `ImmRegisterWordW` | `0x12970` | 489 | UnwindData |  |
| 136 | `ImmUnregisterWordA` | `0x12B60` | 446 | UnwindData |  |
| 137 | `ImmUnregisterWordW` | `0x12D30` | 489 | UnwindData |  |
| 49 | `ImmCreateSoftKeyboard` | `0x17120` | 632 | UnwindData |  |
| 52 | `ImmDestroySoftKeyboard` | `0x173A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `ImmShowSoftKeyboard` | `0x173C0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ImmIMPGetIMEA` | `0x17790` | 151 | UnwindData |  |
| 3 | `ImmIMPGetIMEW` | `0x17830` | 72 | UnwindData |  |
| 4 | `ImmIMPQueryIMEA` | `0x17880` | 191 | UnwindData |  |
| 5 | `ImmIMPQueryIMEW` | `0x17950` | 330 | UnwindData |  |
| 6 | `ImmIMPSetIMEA` | `0x17AA0` | 187 | UnwindData |  |
| 7 | `ImmIMPSetIMEW` | `0x17B70` | 396 | UnwindData |  |
| 10 | `ImmSendIMEMessageExA` | `0x17D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ImmSendIMEMessageExW` | `0x17D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `ImmWINNLSEnableIME` | `0x17D40` | 65 | UnwindData |  |
| 15 | `ImmWINNLSGetEnableStatus` | `0x17D90` | 76 | UnwindData |  |
| 1 | `ImmCallImeConsoleIME` | `0x1D0B0` | 362 | UnwindData |  |
| 12 | `ImmSetActiveContextConsoleIME` | `0x1D220` | 51 | UnwindData |  |
| 8 | `ImmPutImeMenuItemsIntoMappedFile` | `0x1DCB0` | 873 | UnwindData |  |
| 91 | `ImmGetImeMenuItemsA` | `0x1E2A0` | 41 | UnwindData |  |
| 92 | `ImmGetImeMenuItemsW` | `0x1E2D0` | 38 | UnwindData |  |
