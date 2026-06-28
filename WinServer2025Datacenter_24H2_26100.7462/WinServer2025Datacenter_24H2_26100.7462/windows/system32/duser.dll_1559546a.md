# Binary Specification: duser.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\duser.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1559546a2e137a61473430e9860abbf43c11dacbd9ffe27fc1987337c02584bb`
* **Total Exported Functions:** 150

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 65 | `GadgetTransSettingChanged` | `0x4720` | 65 | UnwindData |  |
| 67 | `GetCachedDWriteRenderTarget` | `0x47C0` | 126 | UnwindData |  |
| 104 | `LookupGadgetTicket` | `0x6560` | 182 | UnwindData |  |
| 72 | `GetGadgetAnimation` | `0x6860` | 113 | UnwindData |  |
| 127 | `SetGadgetFocusEx` | `0x6980` | 287 | UnwindData |  |
| 100 | `InvalidateLayeredDescendants` | `0x6B10` | 272 | UnwindData |  |
| 105 | `MapGadgetPoints` | `0x6C30` | 286 | UnwindData |  |
| 80 | `GetGadgetProperty` | `0x6D60` | 234 | UnwindData |  |
| 87 | `GetGadgetStyle` | `0x6FA0` | 188 | UnwindData |  |
| 103 | `IsStartDelete` | `0x7070` | 185 | UnwindData |  |
| 71 | `GetGadget` | `0x7130` | 210 | UnwindData |  |
| 62 | `ForwardGadgetMessage` | `0x7210` | 362 | UnwindData |  |
| 134 | `SetGadgetRootInfo` | `0x7380` | 315 | UnwindData |  |
| 126 | `SetGadgetFocus` | `0x7540` | 302 | UnwindData |  |
| 130 | `SetGadgetOrder` | `0x7700` | 381 | UnwindData |  |
| 23 | `CreateGadget` | `0xBCD0` | 91 | UnwindData |  |
| 77 | `GetGadgetFocus` | `0xD1D0` | 140 | UnwindData |  |
| 46 | `DeleteHandle` | `0xD580` | 61 | UnwindData |  |
| 22 | `CreateAction` | `0xD880` | 182 | UnwindData |  |
| 11 | `AttachWndProcW` | `0xDA90` | 216 | UnwindData |  |
| 81 | `GetGadgetRect` | `0xECF0` | 374 | UnwindData |  |
| 82 | `GetGadgetRgn` | `0x116C0` | 934 | UnwindData |  |
| 42 | `DUserSendEvent` | `0x12B40` | 252 | UnwindData |  |
| 99 | `InvalidateGadget` | `0x14790` | 73 | UnwindData |  |
| 76 | `GetGadgetFlags` | `0x14C90` | 62 | UnwindData |  |
| 137 | `SetGadgetStyle` | `0x14FF0` | 69 | UnwindData |  |
| 57 | `FindGadgetFromPoint` | `0x162E0` | 89 | UnwindData |  |
| 129 | `SetGadgetMessageFilter` | `0x16540` | 73 | UnwindData |  |
| 133 | `SetGadgetRect` | `0x168D0` | 72 | UnwindData |  |
| 131 | `SetGadgetParent` | `0x16D00` | 74 | UnwindData |  |
| 88 | `GetGadgetTicket` | `0x17030` | 770 | UnwindData |  |
| 37 | `DUserPostEvent` | `0x17C70` | 721 | UnwindData |  |
| 29 | `DUserFlushDeferredMessages` | `0x18550` | 114 | UnwindData |  |
| 39 | `DUserRegisterGuts` | `0x18CD0` | 171 | UnwindData |  |
| 40 | `DUserRegisterStub` | `0x18D90` | 199 | UnwindData |  |
| 30 | `DUserFlushMessages` | `0x19700` | 110 | UnwindData |  |
| 41 | `DUserRegisterSuper` | `0x19A70` | 85 | UnwindData |  |
| 8 | `AddLayeredRef` | `0x1C800` | 202 | UnwindData |  |
| 89 | `GetGadgetVisual` | `0x1D400` | 118 | UnwindData |  |
| 55 | `EnsureGadgetTransInitialized` | `0x1EEC0` | 55 | UnwindData |  |
| 18 | `CacheDWriteRenderTarget` | `0x1FB40` | 80 | UnwindData |  |
| 98 | `InitGadgets` | `0x228C0` | 102 | UnwindData |  |
| 90 | `GetMessageExA` | `0x233D0` | 153 | UnwindData |  |
| 50 | `DisableContainerHwnd` | `0x24470` | 58 | UnwindData |  |
| 121 | `SetGadgetBufferInfo` | `0x28600` | 309 | UnwindData |  |
| 60 | `FindStdColor` | `0x28AB0` | 51 | UnwindData |  |
| 147 | `UtilDrawBlendRect` | `0x28EC0` | 425 | UnwindData |  |
| 7 | `AddGadgetMessageHandler` | `0x29580` | 325 | UnwindData |  |
| 132 | `SetGadgetProperty` | `0x299B0` | 288 | UnwindData |  |
| 108 | `RegisterGadgetMessage` | `0x2CAA0` | 55 | UnwindData |  |
| 110 | `RegisterGadgetProperty` | `0x2CB70` | 55 | UnwindData |  |
| 49 | `DetachWndProc` | `0x2D200` | 42 | UnwindData |  |
| 125 | `SetGadgetFlags` | `0x2EB80` | 325 | UnwindData |  |
| 116 | `RemoveGadgetProperty` | `0x30430` | 265 | UnwindData |  |
| 142 | `SetWindowResizeFlag` | `0x306A0` | 194 | UnwindData |  |
| 83 | `GetGadgetRootInfo` | `0x30800` | 239 | UnwindData |  |
| 78 | `GetGadgetLayerInfo` | `0x30C10` | 263 | UnwindData |  |
| 74 | `GetGadgetBufferInfo` | `0x312E0` | 249 | UnwindData |  |
| 45 | `DUserStopPVLAnimation` | `0x31480` | 104 | UnwindData |  |
| 138 | `SetHardwareDeviceUsage` | `0x315D0` | 158 | UnwindData |  |
| 141 | `SetTransitionVisualProperties` | `0x31A90` | 104 | UnwindData |  |
| 118 | `ScheduleGadgetTransitions` | `0x31B00` | 122 | UnwindData |  |
| 19 | `ChangeCurrentAnimationScenario` | `0x32520` | 60 | UnwindData |  |
| 112 | `ReleaseLayeredRef` | `0x325F0` | 201 | UnwindData |  |
| 15 | `BuildAnimation` | `0x32780` | 133 | UnwindData |  |
| 68 | `GetDUserModule` | `0x32A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `BuildInterpolation` | `0x32A50` | 127 | UnwindData |  |
| 51 | `DllMain` | `0x338D0` | 655 | UnwindData |  |
| 139 | `SetMinimumDCompVersion` | `0x33FD0` | 96 | UnwindData |  |
| 93 | `GetStdColorI` | `0x34AE0` | 59 | UnwindData |  |
| 92 | `GetStdColorBrushI` | `0x35020` | 204 | UnwindData |  |
| 64 | `GadgetTransCompositionChanged` | `0x36060` | 232 | UnwindData |  |
| 47 | `DestroyPendingDCVisuals` | `0x381C0` | 28 | UnwindData |  |
| 12 | `AutoTrace` | `0x3E2F0` | 55 | UnwindData |  |
| 69 | `GetDebug` | `0x3E330` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `BeginHideInputPaneAnimation` | `0x3EB00` | 102 | UnwindData |  |
| 14 | `BeginShowInputPaneAnimation` | `0x3EB70` | 102 | UnwindData |  |
| 16 | `BuildDropTarget` | `0x3EBE0` | 128 | UnwindData |  |
| 21 | `ClearTopmostVisual` | `0x3EC70` | 45 | UnwindData |  |
| 24 | `CustomGadgetHitTestQuery` | `0x3ECB0` | 150 | UnwindData |  |
| 48 | `DetachGadgetVisuals` | `0x3ED50` | 139 | UnwindData |  |
| 53 | `EndInputPaneAnimation` | `0x3EDF0` | 49 | UnwindData |  |
| 54 | `EnsureAnimationsEnabled` | `0x3EE30` | 69 | UnwindData |  |
| 70 | `GetFinalAnimatingPosition` | `0x3EE80` | 114 | UnwindData |  |
| 111 | `ReleaseDetachedObjects` | `0x3EF00` | 71 | UnwindData |  |
| 114 | `RemoveClippingImmunityFromVisual` | `0x3EF50` | 144 | UnwindData |  |
| 31 | `DUserGetAlphaPRID` | `0x3FD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `DUserGetRectPRID` | `0x3FD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `DUserGetRotatePRID` | `0x3FD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `DUserGetScalePRID` | `0x3FD70` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `DUserStopAnimation` | `0x40490` | 143 | UnwindData |  |
| 1 | `DUserCastHandle` | `0x48A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DUserDeleteGadget` | `0x48AA0` | 205 | UnwindData |  |
| 3 | `GetStdColorBrushF` | `0x48C60` | 163 | UnwindData |  |
| 4 | `GetStdColorF` | `0x48D10` | 100 | UnwindData |  |
| 5 | `GetStdColorPenF` | `0x48D80` | 163 | UnwindData |  |
| 6 | `UtilDrawOutlineRect` | `0x48E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `AdjustClipInsideRef` | `0x48E40` | 213 | UnwindData |  |
| 10 | `AttachWndProcA` | `0x48F20` | 48 | UnwindData |  |
| 20 | `ClearPushedOpacitiesFromGadgetTree` | `0x48F60` | 261 | UnwindData |  |
| 25 | `DUserBuildGadget` | `0x49070` | 65 | UnwindData |  |
| 26 | `DUserCastClass` | `0x490C0` | 89 | UnwindData |  |
| 27 | `DUserCastDirect` | `0x49120` | 28 | UnwindData |  |
| 28 | `DUserFindClass` | `0x49150` | 84 | UnwindData |  |
| 32 | `DUserGetGutsData` | `0x491B0` | 94 | UnwindData |  |
| 36 | `DUserInstanceOf` | `0x49220` | 76 | UnwindData |  |
| 38 | `DUserPostMethod` | `0x49280` | 151 | UnwindData |  |
| 43 | `DUserSendMethod` | `0x49320` | 166 | UnwindData |  |
| 52 | `DrawGadgetTree` | `0x493D0` | 279 | UnwindData |  |
| 56 | `EnumGadgets` | `0x494F0` | 323 | UnwindData |  |
| 58 | `FindGadgetMessages` | `0x49640` | 258 | UnwindData |  |
| 59 | `FindGadgetTargetingInfo` | `0x49750` | 250 | UnwindData |  |
| 61 | `FireGadgetMessages` | `0x49850` | 241 | UnwindData |  |
| 63 | `FreeGdiDxInteropStagingBuffer` | `0x49950` | 168 | UnwindData |  |
| 66 | `GetActionTimeslice` | `0x49A00` | 160 | UnwindData |  |
| 73 | `GetGadgetBitmap` | `0x49AB0` | 259 | UnwindData |  |
| 75 | `GetGadgetCenterPoint` | `0x49BC0` | 219 | UnwindData |  |
| 79 | `GetGadgetMessageFilter` | `0x49CB0` | 197 | UnwindData |  |
| 84 | `GetGadgetRotation` | `0x49D80` | 213 | UnwindData |  |
| 85 | `GetGadgetScale` | `0x49E60` | 219 | UnwindData |  |
| 86 | `GetGadgetSize` | `0x49F50` | 233 | UnwindData |  |
| 91 | `GetMessageExW` | `0x4A040` | 153 | UnwindData |  |
| 94 | `GetStdColorName` | `0x4A0E0` | 61 | UnwindData |  |
| 95 | `GetStdColorPenI` | `0x4A130` | 218 | UnwindData |  |
| 96 | `GetStdPalette` | `0x4A210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `InitGadgetComponent` | `0x4A220` | 188 | UnwindData |  |
| 101 | `IsGadgetParentChainStyle` | `0x4A2F0` | 254 | UnwindData |  |
| 102 | `IsInsideContext` | `0x4A400` | 78 | UnwindData |  |
| 106 | `PeekMessageExA` | `0x4A460` | 183 | UnwindData |  |
| 107 | `PeekMessageExW` | `0x4A520` | 179 | UnwindData |  |
| 109 | `RegisterGadgetMessageString` | `0x4A5E0` | 39 | UnwindData |  |
| 144 | `UnregisterGadgetMessageString` | `0x4A5E0` | 39 | UnwindData |  |
| 113 | `ReleaseMouseCapture` | `0x4A610` | 206 | UnwindData |  |
| 115 | `RemoveGadgetMessageHandler` | `0x4A6F0` | 311 | UnwindData |  |
| 117 | `ResetDUserDevice` | `0x4A830` | 226 | UnwindData |  |
| 119 | `SetActionTimeslice` | `0x4A920` | 152 | UnwindData |  |
| 120 | `SetAtlasingHints` | `0x4A9C0` | 250 | UnwindData |  |
| 122 | `SetGadgetCenterPoint` | `0x4AAC0` | 307 | UnwindData |  |
| 123 | `SetGadgetFillF` | `0x4AC00` | 269 | UnwindData |  |
| 124 | `SetGadgetFillI` | `0x4AD20` | 315 | UnwindData |  |
| 128 | `SetGadgetLayerInfo` | `0x4AE70` | 250 | UnwindData |  |
| 135 | `SetGadgetRotation` | `0x4AF70` | 282 | UnwindData |  |
| 136 | `SetGadgetScale` | `0x4B090` | 307 | UnwindData |  |
| 140 | `SetRestoreCachedLayeredRefFlag` | `0x4B1D0` | 173 | UnwindData |  |
| 143 | `UnregisterGadgetMessage` | `0x4B290` | 95 | UnwindData |  |
| 145 | `UnregisterGadgetProperty` | `0x4B300` | 95 | UnwindData |  |
| 146 | `UtilBuildFont` | `0x4B370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `UtilGetColor` | `0x4B380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `UtilSetBackground` | `0x4B390` | 85 | UnwindData |  |
| 150 | `WaitMessageEx` | `0x4B3F0` | 87 | UnwindData |  |
