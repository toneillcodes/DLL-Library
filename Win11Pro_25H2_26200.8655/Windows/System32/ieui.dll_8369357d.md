# Binary Specification: ieui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ieui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8369357d7918c3667cfaef8c87c42aba35a44224888668adfc129590adaf87af`
* **Total Exported Functions:** 150

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 133 | `SetGadgetRect` | `0x26F0` | 72 | UnwindData |  |
| 23 | `CreateGadget` | `0x2CD0` | 87 | UnwindData |  |
| 131 | `SetGadgetParent` | `0x3580` | 74 | UnwindData |  |
| 99 | `InvalidateGadget` | `0x38A0` | 73 | UnwindData |  |
| 129 | `SetGadgetMessageFilter` | `0x3EB0` | 73 | UnwindData |  |
| 137 | `SetGadgetStyle` | `0x4240` | 69 | UnwindData |  |
| 88 | `GetGadgetTicket` | `0xA5D0` | 60 | UnwindData |  |
| 107 | `PeekMessageExW` | `0xABF0` | 88 | UnwindData |  |
| 150 | `WaitMessageEx` | `0xB760` | 47 | UnwindData |  |
| 132 | `SetGadgetProperty` | `0xB9E0` | 299 | UnwindData |  |
| 57 | `FindGadgetFromPoint` | `0xBD90` | 252 | UnwindData |  |
| 46 | `DeleteHandle` | `0xD760` | 429 | UnwindData |  |
| 91 | `GetMessageExW` | `0xE570` | 75 | UnwindData |  |
| 76 | `GetGadgetFlags` | `0xF250` | 418 | UnwindData |  |
| 40 | `DUserRegisterStub` | `0xFF30` | 471 | UnwindData |  |
| 42 | `DUserSendEvent` | `0x10630` | 254 | UnwindData |  |
| 30 | `DUserFlushMessages` | `0x11740` | 110 | UnwindData |  |
| 98 | `InitGadgets` | `0x11B80` | 102 | UnwindData |  |
| 121 | `SetGadgetBufferInfo` | `0x12390` | 299 | UnwindData |  |
| 39 | `DUserRegisterGuts` | `0x13110` | 171 | UnwindData |  |
| 51 | `DllMain` | `0x14B40` | 686 | UnwindData |  |
| 12 | `AutoTrace` | `0x150B0` | 55 | UnwindData |  |
| 69 | `GetDebug` | `0x150F0` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `BeginHideInputPaneAnimation` | `0x15C50` | 103 | UnwindData |  |
| 14 | `BeginShowInputPaneAnimation` | `0x15CC0` | 103 | UnwindData |  |
| 15 | `BuildAnimation` | `0x15D30` | 133 | UnwindData |  |
| 16 | `BuildDropTarget` | `0x15DC0` | 128 | UnwindData |  |
| 17 | `BuildInterpolation` | `0x15E50` | 289 | UnwindData |  |
| 18 | `CacheDWriteRenderTarget` | `0x15F80` | 132 | UnwindData |  |
| 19 | `ChangeCurrentAnimationScenario` | `0x16010` | 168 | UnwindData |  |
| 21 | `ClearTopmostVisual` | `0x160C0` | 45 | UnwindData |  |
| 24 | `CustomGadgetHitTestQuery` | `0x16100` | 150 | UnwindData |  |
| 45 | `DUserStopPVLAnimation` | `0x161A0` | 102 | UnwindData |  |
| 47 | `DestroyPendingDCVisuals` | `0x16210` | 29 | UnwindData |  |
| 48 | `DetachGadgetVisuals` | `0x16240` | 140 | UnwindData |  |
| 53 | `EndInputPaneAnimation` | `0x162E0` | 53 | UnwindData |  |
| 54 | `EnsureAnimationsEnabled` | `0x16320` | 70 | UnwindData |  |
| 55 | `EnsureGadgetTransInitialized` | `0x16370` | 54 | UnwindData |  |
| 65 | `GadgetTransSettingChanged` | `0x163B0` | 64 | UnwindData |  |
| 67 | `GetCachedDWriteRenderTarget` | `0x16400` | 126 | UnwindData |  |
| 70 | `GetFinalAnimatingPosition` | `0x16490` | 116 | UnwindData |  |
| 72 | `GetGadgetAnimation` | `0x16510` | 111 | UnwindData |  |
| 89 | `GetGadgetVisual` | `0x16590` | 117 | UnwindData |  |
| 111 | `ReleaseDetachedObjects` | `0x16610` | 72 | UnwindData |  |
| 114 | `RemoveClippingImmunityFromVisual` | `0x16660` | 146 | UnwindData |  |
| 118 | `ScheduleGadgetTransitions` | `0x16700` | 121 | UnwindData |  |
| 139 | `SetMinimumDCompVersion` | `0x16780` | 97 | UnwindData |  |
| 141 | `SetTransitionVisualProperties` | `0x167F0` | 105 | UnwindData |  |
| 31 | `DUserGetAlphaPRID` | `0x175B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `DUserGetRectPRID` | `0x175C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `DUserGetRotatePRID` | `0x175D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `DUserGetScalePRID` | `0x175E0` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `DUserStopAnimation` | `0x17D00` | 143 | UnwindData |  |
| 1 | `DUserCastHandle` | `0x2C780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DUserDeleteGadget` | `0x2C7A0` | 205 | UnwindData |  |
| 3 | `GetStdColorBrushF` | `0x2CB20` | 163 | UnwindData |  |
| 4 | `GetStdColorF` | `0x2CBD0` | 100 | UnwindData |  |
| 5 | `GetStdColorPenF` | `0x2CC40` | 163 | UnwindData |  |
| 6 | `UtilDrawOutlineRect` | `0x2CDD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `AddGadgetMessageHandler` | `0x2CE10` | 311 | UnwindData |  |
| 8 | `AddLayeredRef` | `0x2CF50` | 203 | UnwindData |  |
| 9 | `AdjustClipInsideRef` | `0x2D030` | 213 | UnwindData |  |
| 10 | `AttachWndProcA` | `0x2D110` | 48 | UnwindData |  |
| 11 | `AttachWndProcW` | `0x2D150` | 45 | UnwindData |  |
| 20 | `ClearPushedOpacitiesFromGadgetTree` | `0x2D190` | 261 | UnwindData |  |
| 22 | `CreateAction` | `0x2D2A0` | 171 | UnwindData |  |
| 25 | `DUserBuildGadget` | `0x2D360` | 65 | UnwindData |  |
| 26 | `DUserCastClass` | `0x2D3B0` | 89 | UnwindData |  |
| 27 | `DUserCastDirect` | `0x2D410` | 28 | UnwindData |  |
| 28 | `DUserFindClass` | `0x2D440` | 84 | UnwindData |  |
| 29 | `DUserFlushDeferredMessages` | `0x2D4A0` | 114 | UnwindData |  |
| 32 | `DUserGetGutsData` | `0x2D520` | 94 | UnwindData |  |
| 36 | `DUserInstanceOf` | `0x2D590` | 76 | UnwindData |  |
| 37 | `DUserPostEvent` | `0x2D5F0` | 153 | UnwindData |  |
| 38 | `DUserPostMethod` | `0x2D690` | 151 | UnwindData |  |
| 41 | `DUserRegisterSuper` | `0x2D730` | 171 | UnwindData |  |
| 43 | `DUserSendMethod` | `0x2D7F0` | 166 | UnwindData |  |
| 49 | `DetachWndProc` | `0x2D8A0` | 148 | UnwindData |  |
| 50 | `DisableContainerHwnd` | `0x2D940` | 58 | UnwindData |  |
| 52 | `DrawGadgetTree` | `0x2D980` | 279 | UnwindData |  |
| 56 | `EnumGadgets` | `0x2DAA0` | 323 | UnwindData |  |
| 58 | `FindGadgetMessages` | `0x2DBF0` | 258 | UnwindData |  |
| 59 | `FindGadgetTargetingInfo` | `0x2DD00` | 250 | UnwindData |  |
| 60 | `FindStdColor` | `0x2DE00` | 130 | UnwindData |  |
| 61 | `FireGadgetMessages` | `0x2DE90` | 241 | UnwindData |  |
| 62 | `ForwardGadgetMessage` | `0x2DF90` | 344 | UnwindData |  |
| 63 | `FreeGdiDxInteropStagingBuffer` | `0x2E0F0` | 172 | UnwindData |  |
| 64 | `GadgetTransCompositionChanged` | `0x2E1B0` | 232 | UnwindData |  |
| 66 | `GetActionTimeslice` | `0x2E2A0` | 160 | UnwindData |  |
| 68 | `GetDUserModule` | `0x2E350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `GetGadget` | `0x2E360` | 206 | UnwindData |  |
| 73 | `GetGadgetBitmap` | `0x2E440` | 259 | UnwindData |  |
| 74 | `GetGadgetBufferInfo` | `0x2E550` | 249 | UnwindData |  |
| 75 | `GetGadgetCenterPoint` | `0x2E650` | 219 | UnwindData |  |
| 77 | `GetGadgetFocus` | `0x2E740` | 133 | UnwindData |  |
| 78 | `GetGadgetLayerInfo` | `0x2E7D0` | 250 | UnwindData |  |
| 79 | `GetGadgetMessageFilter` | `0x2E8D0` | 197 | UnwindData |  |
| 80 | `GetGadgetProperty` | `0x2E9A0` | 233 | UnwindData |  |
| 81 | `GetGadgetRect` | `0x2EA90` | 231 | UnwindData |  |
| 82 | `GetGadgetRgn` | `0x2EB80` | 237 | UnwindData |  |
| 83 | `GetGadgetRootInfo` | `0x2EC80` | 239 | UnwindData |  |
| 84 | `GetGadgetRotation` | `0x2ED80` | 213 | UnwindData |  |
| 85 | `GetGadgetScale` | `0x2EE60` | 219 | UnwindData |  |
| 86 | `GetGadgetSize` | `0x2EF50` | 233 | UnwindData |  |
| 87 | `GetGadgetStyle` | `0x2F040` | 184 | UnwindData |  |
| 90 | `GetMessageExA` | `0x2F100` | 153 | UnwindData |  |
| 92 | `GetStdColorBrushI` | `0x2F1A0` | 204 | UnwindData |  |
| 93 | `GetStdColorI` | `0x2F280` | 59 | UnwindData |  |
| 94 | `GetStdColorName` | `0x2F2D0` | 61 | UnwindData |  |
| 95 | `GetStdColorPenI` | `0x2F320` | 218 | UnwindData |  |
| 96 | `GetStdPalette` | `0x2F400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `InitGadgetComponent` | `0x2F410` | 188 | UnwindData |  |
| 100 | `InvalidateLayeredDescendants` | `0x2F4E0` | 259 | UnwindData |  |
| 101 | `IsGadgetParentChainStyle` | `0x2F5F0` | 254 | UnwindData |  |
| 102 | `IsInsideContext` | `0x2F700` | 78 | UnwindData |  |
| 103 | `IsStartDelete` | `0x2F760` | 181 | UnwindData |  |
| 104 | `LookupGadgetTicket` | `0x2F820` | 175 | UnwindData |  |
| 105 | `MapGadgetPoints` | `0x2F8E0` | 281 | UnwindData |  |
| 106 | `PeekMessageExA` | `0x2FA00` | 183 | UnwindData |  |
| 108 | `RegisterGadgetMessage` | `0x2FAC0` | 107 | UnwindData |  |
| 109 | `RegisterGadgetMessageString` | `0x2FB40` | 39 | UnwindData |  |
| 144 | `UnregisterGadgetMessageString` | `0x2FB40` | 39 | UnwindData |  |
| 110 | `RegisterGadgetProperty` | `0x2FB70` | 107 | UnwindData |  |
| 112 | `ReleaseLayeredRef` | `0x2FBF0` | 201 | UnwindData |  |
| 113 | `ReleaseMouseCapture` | `0x2FCC0` | 206 | UnwindData |  |
| 115 | `RemoveGadgetMessageHandler` | `0x2FDA0` | 311 | UnwindData |  |
| 116 | `RemoveGadgetProperty` | `0x2FEE0` | 265 | UnwindData |  |
| 117 | `ResetDUserDevice` | `0x2FFF0` | 226 | UnwindData |  |
| 119 | `SetActionTimeslice` | `0x300E0` | 152 | UnwindData |  |
| 120 | `SetAtlasingHints` | `0x30180` | 136 | UnwindData |  |
| 122 | `SetGadgetCenterPoint` | `0x30210` | 307 | UnwindData |  |
| 123 | `SetGadgetFillF` | `0x30350` | 269 | UnwindData |  |
| 124 | `SetGadgetFillI` | `0x30470` | 315 | UnwindData |  |
| 125 | `SetGadgetFlags` | `0x305C0` | 315 | UnwindData |  |
| 126 | `SetGadgetFocus` | `0x30710` | 278 | UnwindData |  |
| 127 | `SetGadgetFocusEx` | `0x30830` | 274 | UnwindData |  |
| 128 | `SetGadgetLayerInfo` | `0x30950` | 250 | UnwindData |  |
| 130 | `SetGadgetOrder` | `0x30A50` | 354 | UnwindData |  |
| 134 | `SetGadgetRootInfo` | `0x30BC0` | 310 | UnwindData |  |
| 135 | `SetGadgetRotation` | `0x30D00` | 282 | UnwindData |  |
| 136 | `SetGadgetScale` | `0x30E20` | 307 | UnwindData |  |
| 138 | `SetHardwareDeviceUsage` | `0x30F60` | 162 | UnwindData |  |
| 140 | `SetRestoreCachedLayeredRefFlag` | `0x31010` | 173 | UnwindData |  |
| 142 | `SetWindowResizeFlag` | `0x310D0` | 192 | UnwindData |  |
| 143 | `UnregisterGadgetMessage` | `0x311A0` | 95 | UnwindData |  |
| 145 | `UnregisterGadgetProperty` | `0x31210` | 95 | UnwindData |  |
| 146 | `UtilBuildFont` | `0x31280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `UtilDrawBlendRect` | `0x31290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `UtilGetColor` | `0x312A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `UtilSetBackground` | `0x312B0` | 85 | UnwindData |  |
