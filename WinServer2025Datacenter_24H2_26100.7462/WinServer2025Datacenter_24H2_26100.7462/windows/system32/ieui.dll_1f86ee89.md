# Binary Specification: ieui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ieui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1f86ee89c8889a3c2b12fefa71104e5bebf5f24bea825bd3a16022ef89253db7`
* **Total Exported Functions:** 150

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 133 | `SetGadgetRect` | `0x26E0` | 72 | UnwindData |  |
| 23 | `CreateGadget` | `0x2CC0` | 87 | UnwindData |  |
| 131 | `SetGadgetParent` | `0x3570` | 74 | UnwindData |  |
| 99 | `InvalidateGadget` | `0x3890` | 73 | UnwindData |  |
| 129 | `SetGadgetMessageFilter` | `0x3EA0` | 73 | UnwindData |  |
| 137 | `SetGadgetStyle` | `0x4230` | 69 | UnwindData |  |
| 88 | `GetGadgetTicket` | `0xA5C0` | 60 | UnwindData |  |
| 107 | `PeekMessageExW` | `0xABE0` | 88 | UnwindData |  |
| 150 | `WaitMessageEx` | `0xB750` | 47 | UnwindData |  |
| 132 | `SetGadgetProperty` | `0xB9D0` | 299 | UnwindData |  |
| 57 | `FindGadgetFromPoint` | `0xBD80` | 252 | UnwindData |  |
| 46 | `DeleteHandle` | `0xD750` | 429 | UnwindData |  |
| 91 | `GetMessageExW` | `0xE560` | 75 | UnwindData |  |
| 76 | `GetGadgetFlags` | `0xF240` | 418 | UnwindData |  |
| 40 | `DUserRegisterStub` | `0xFF20` | 471 | UnwindData |  |
| 42 | `DUserSendEvent` | `0x10620` | 254 | UnwindData |  |
| 30 | `DUserFlushMessages` | `0x11730` | 110 | UnwindData |  |
| 98 | `InitGadgets` | `0x11B70` | 102 | UnwindData |  |
| 121 | `SetGadgetBufferInfo` | `0x12380` | 299 | UnwindData |  |
| 39 | `DUserRegisterGuts` | `0x13100` | 171 | UnwindData |  |
| 51 | `DllMain` | `0x14B30` | 686 | UnwindData |  |
| 12 | `AutoTrace` | `0x150A0` | 55 | UnwindData |  |
| 69 | `GetDebug` | `0x150E0` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `BeginHideInputPaneAnimation` | `0x15C40` | 103 | UnwindData |  |
| 14 | `BeginShowInputPaneAnimation` | `0x15CB0` | 103 | UnwindData |  |
| 15 | `BuildAnimation` | `0x15D20` | 133 | UnwindData |  |
| 16 | `BuildDropTarget` | `0x15DB0` | 128 | UnwindData |  |
| 17 | `BuildInterpolation` | `0x15E40` | 289 | UnwindData |  |
| 18 | `CacheDWriteRenderTarget` | `0x15F70` | 132 | UnwindData |  |
| 19 | `ChangeCurrentAnimationScenario` | `0x16000` | 168 | UnwindData |  |
| 21 | `ClearTopmostVisual` | `0x160B0` | 45 | UnwindData |  |
| 24 | `CustomGadgetHitTestQuery` | `0x160F0` | 150 | UnwindData |  |
| 45 | `DUserStopPVLAnimation` | `0x16190` | 102 | UnwindData |  |
| 47 | `DestroyPendingDCVisuals` | `0x16200` | 29 | UnwindData |  |
| 48 | `DetachGadgetVisuals` | `0x16230` | 140 | UnwindData |  |
| 53 | `EndInputPaneAnimation` | `0x162D0` | 53 | UnwindData |  |
| 54 | `EnsureAnimationsEnabled` | `0x16310` | 70 | UnwindData |  |
| 55 | `EnsureGadgetTransInitialized` | `0x16360` | 54 | UnwindData |  |
| 65 | `GadgetTransSettingChanged` | `0x163A0` | 64 | UnwindData |  |
| 67 | `GetCachedDWriteRenderTarget` | `0x163F0` | 126 | UnwindData |  |
| 70 | `GetFinalAnimatingPosition` | `0x16480` | 116 | UnwindData |  |
| 72 | `GetGadgetAnimation` | `0x16500` | 111 | UnwindData |  |
| 89 | `GetGadgetVisual` | `0x16580` | 117 | UnwindData |  |
| 111 | `ReleaseDetachedObjects` | `0x16600` | 72 | UnwindData |  |
| 114 | `RemoveClippingImmunityFromVisual` | `0x16650` | 146 | UnwindData |  |
| 118 | `ScheduleGadgetTransitions` | `0x166F0` | 121 | UnwindData |  |
| 139 | `SetMinimumDCompVersion` | `0x16770` | 97 | UnwindData |  |
| 141 | `SetTransitionVisualProperties` | `0x167E0` | 105 | UnwindData |  |
| 31 | `DUserGetAlphaPRID` | `0x175A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `DUserGetRectPRID` | `0x175B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `DUserGetRotatePRID` | `0x175C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `DUserGetScalePRID` | `0x175D0` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `DUserStopAnimation` | `0x17CF0` | 143 | UnwindData |  |
| 1 | `DUserCastHandle` | `0x2C770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DUserDeleteGadget` | `0x2C790` | 205 | UnwindData |  |
| 3 | `GetStdColorBrushF` | `0x2CB10` | 163 | UnwindData |  |
| 4 | `GetStdColorF` | `0x2CBC0` | 100 | UnwindData |  |
| 5 | `GetStdColorPenF` | `0x2CC30` | 163 | UnwindData |  |
| 6 | `UtilDrawOutlineRect` | `0x2CDC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `AddGadgetMessageHandler` | `0x2CE00` | 311 | UnwindData |  |
| 8 | `AddLayeredRef` | `0x2CF40` | 203 | UnwindData |  |
| 9 | `AdjustClipInsideRef` | `0x2D020` | 213 | UnwindData |  |
| 10 | `AttachWndProcA` | `0x2D100` | 48 | UnwindData |  |
| 11 | `AttachWndProcW` | `0x2D140` | 45 | UnwindData |  |
| 20 | `ClearPushedOpacitiesFromGadgetTree` | `0x2D180` | 261 | UnwindData |  |
| 22 | `CreateAction` | `0x2D290` | 171 | UnwindData |  |
| 25 | `DUserBuildGadget` | `0x2D350` | 65 | UnwindData |  |
| 26 | `DUserCastClass` | `0x2D3A0` | 89 | UnwindData |  |
| 27 | `DUserCastDirect` | `0x2D400` | 28 | UnwindData |  |
| 28 | `DUserFindClass` | `0x2D430` | 84 | UnwindData |  |
| 29 | `DUserFlushDeferredMessages` | `0x2D490` | 114 | UnwindData |  |
| 32 | `DUserGetGutsData` | `0x2D510` | 94 | UnwindData |  |
| 36 | `DUserInstanceOf` | `0x2D580` | 76 | UnwindData |  |
| 37 | `DUserPostEvent` | `0x2D5E0` | 153 | UnwindData |  |
| 38 | `DUserPostMethod` | `0x2D680` | 151 | UnwindData |  |
| 41 | `DUserRegisterSuper` | `0x2D720` | 171 | UnwindData |  |
| 43 | `DUserSendMethod` | `0x2D7E0` | 166 | UnwindData |  |
| 49 | `DetachWndProc` | `0x2D890` | 148 | UnwindData |  |
| 50 | `DisableContainerHwnd` | `0x2D930` | 58 | UnwindData |  |
| 52 | `DrawGadgetTree` | `0x2D970` | 279 | UnwindData |  |
| 56 | `EnumGadgets` | `0x2DA90` | 323 | UnwindData |  |
| 58 | `FindGadgetMessages` | `0x2DBE0` | 258 | UnwindData |  |
| 59 | `FindGadgetTargetingInfo` | `0x2DCF0` | 250 | UnwindData |  |
| 60 | `FindStdColor` | `0x2DDF0` | 130 | UnwindData |  |
| 61 | `FireGadgetMessages` | `0x2DE80` | 241 | UnwindData |  |
| 62 | `ForwardGadgetMessage` | `0x2DF80` | 344 | UnwindData |  |
| 63 | `FreeGdiDxInteropStagingBuffer` | `0x2E0E0` | 172 | UnwindData |  |
| 64 | `GadgetTransCompositionChanged` | `0x2E1A0` | 232 | UnwindData |  |
| 66 | `GetActionTimeslice` | `0x2E290` | 160 | UnwindData |  |
| 68 | `GetDUserModule` | `0x2E340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `GetGadget` | `0x2E350` | 206 | UnwindData |  |
| 73 | `GetGadgetBitmap` | `0x2E430` | 259 | UnwindData |  |
| 74 | `GetGadgetBufferInfo` | `0x2E540` | 249 | UnwindData |  |
| 75 | `GetGadgetCenterPoint` | `0x2E640` | 219 | UnwindData |  |
| 77 | `GetGadgetFocus` | `0x2E730` | 133 | UnwindData |  |
| 78 | `GetGadgetLayerInfo` | `0x2E7C0` | 250 | UnwindData |  |
| 79 | `GetGadgetMessageFilter` | `0x2E8C0` | 197 | UnwindData |  |
| 80 | `GetGadgetProperty` | `0x2E990` | 233 | UnwindData |  |
| 81 | `GetGadgetRect` | `0x2EA80` | 231 | UnwindData |  |
| 82 | `GetGadgetRgn` | `0x2EB70` | 237 | UnwindData |  |
| 83 | `GetGadgetRootInfo` | `0x2EC70` | 239 | UnwindData |  |
| 84 | `GetGadgetRotation` | `0x2ED70` | 213 | UnwindData |  |
| 85 | `GetGadgetScale` | `0x2EE50` | 219 | UnwindData |  |
| 86 | `GetGadgetSize` | `0x2EF40` | 233 | UnwindData |  |
| 87 | `GetGadgetStyle` | `0x2F030` | 184 | UnwindData |  |
| 90 | `GetMessageExA` | `0x2F0F0` | 153 | UnwindData |  |
| 92 | `GetStdColorBrushI` | `0x2F190` | 204 | UnwindData |  |
| 93 | `GetStdColorI` | `0x2F270` | 59 | UnwindData |  |
| 94 | `GetStdColorName` | `0x2F2C0` | 61 | UnwindData |  |
| 95 | `GetStdColorPenI` | `0x2F310` | 218 | UnwindData |  |
| 96 | `GetStdPalette` | `0x2F3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `InitGadgetComponent` | `0x2F400` | 188 | UnwindData |  |
| 100 | `InvalidateLayeredDescendants` | `0x2F4D0` | 259 | UnwindData |  |
| 101 | `IsGadgetParentChainStyle` | `0x2F5E0` | 254 | UnwindData |  |
| 102 | `IsInsideContext` | `0x2F6F0` | 78 | UnwindData |  |
| 103 | `IsStartDelete` | `0x2F750` | 181 | UnwindData |  |
| 104 | `LookupGadgetTicket` | `0x2F810` | 175 | UnwindData |  |
| 105 | `MapGadgetPoints` | `0x2F8D0` | 281 | UnwindData |  |
| 106 | `PeekMessageExA` | `0x2F9F0` | 183 | UnwindData |  |
| 108 | `RegisterGadgetMessage` | `0x2FAB0` | 107 | UnwindData |  |
| 109 | `RegisterGadgetMessageString` | `0x2FB30` | 39 | UnwindData |  |
| 144 | `UnregisterGadgetMessageString` | `0x2FB30` | 39 | UnwindData |  |
| 110 | `RegisterGadgetProperty` | `0x2FB60` | 107 | UnwindData |  |
| 112 | `ReleaseLayeredRef` | `0x2FBE0` | 201 | UnwindData |  |
| 113 | `ReleaseMouseCapture` | `0x2FCB0` | 206 | UnwindData |  |
| 115 | `RemoveGadgetMessageHandler` | `0x2FD90` | 311 | UnwindData |  |
| 116 | `RemoveGadgetProperty` | `0x2FED0` | 265 | UnwindData |  |
| 117 | `ResetDUserDevice` | `0x2FFE0` | 226 | UnwindData |  |
| 119 | `SetActionTimeslice` | `0x300D0` | 152 | UnwindData |  |
| 120 | `SetAtlasingHints` | `0x30170` | 136 | UnwindData |  |
| 122 | `SetGadgetCenterPoint` | `0x30200` | 307 | UnwindData |  |
| 123 | `SetGadgetFillF` | `0x30340` | 269 | UnwindData |  |
| 124 | `SetGadgetFillI` | `0x30460` | 315 | UnwindData |  |
| 125 | `SetGadgetFlags` | `0x305B0` | 315 | UnwindData |  |
| 126 | `SetGadgetFocus` | `0x30700` | 278 | UnwindData |  |
| 127 | `SetGadgetFocusEx` | `0x30820` | 274 | UnwindData |  |
| 128 | `SetGadgetLayerInfo` | `0x30940` | 250 | UnwindData |  |
| 130 | `SetGadgetOrder` | `0x30A40` | 354 | UnwindData |  |
| 134 | `SetGadgetRootInfo` | `0x30BB0` | 310 | UnwindData |  |
| 135 | `SetGadgetRotation` | `0x30CF0` | 282 | UnwindData |  |
| 136 | `SetGadgetScale` | `0x30E10` | 307 | UnwindData |  |
| 138 | `SetHardwareDeviceUsage` | `0x30F50` | 162 | UnwindData |  |
| 140 | `SetRestoreCachedLayeredRefFlag` | `0x31000` | 173 | UnwindData |  |
| 142 | `SetWindowResizeFlag` | `0x310C0` | 192 | UnwindData |  |
| 143 | `UnregisterGadgetMessage` | `0x31190` | 95 | UnwindData |  |
| 145 | `UnregisterGadgetProperty` | `0x31200` | 95 | UnwindData |  |
| 146 | `UtilBuildFont` | `0x31270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `UtilDrawBlendRect` | `0x31280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `UtilGetColor` | `0x31290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `UtilSetBackground` | `0x312A0` | 85 | UnwindData |  |
