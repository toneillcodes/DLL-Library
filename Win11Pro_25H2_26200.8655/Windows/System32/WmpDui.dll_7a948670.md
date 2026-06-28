# Binary Specification: WmpDui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WmpDui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7a94867041054418f2b786ae369bf1e4ed647ffcb4e0623f30f5a782b77f69f7`
* **Total Exported Functions:** 146

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 49 | `DllMain` | `0x1760` | 63 | UnwindData |  |
| 12 | `AutoTrace` | `0x3350` | 55 | UnwindData |  |
| 65 | `GetDebug` | `0x3390` | 3,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `BuildAnimation` | `0x4020` | 133 | UnwindData |  |
| 14 | `BuildDropTarget` | `0x40B0` | 128 | UnwindData |  |
| 15 | `BuildInterpolation` | `0x4140` | 289 | UnwindData |  |
| 16 | `CacheDWriteRenderTarget` | `0x4270` | 132 | UnwindData |  |
| 17 | `ChangeCurrentAnimationScenario` | `0x4300` | 168 | UnwindData |  |
| 19 | `ClearTopmostVisual` | `0x43B0` | 45 | UnwindData |  |
| 22 | `CustomGadgetHitTestQuery` | `0x43F0` | 150 | UnwindData |  |
| 43 | `DUserStopPVLAnimation` | `0x4490` | 102 | UnwindData |  |
| 45 | `DestroyPendingDCVisuals` | `0x4500` | 29 | UnwindData |  |
| 46 | `DetachGadgetVisuals` | `0x4530` | 140 | UnwindData |  |
| 51 | `EnsureAnimationsEnabled` | `0x45D0` | 70 | UnwindData |  |
| 52 | `EnsureGadgetTransInitialized` | `0x4620` | 54 | UnwindData |  |
| 61 | `GadgetTransSettingChanged` | `0x4660` | 64 | UnwindData |  |
| 63 | `GetCachedDWriteRenderTarget` | `0x46B0` | 126 | UnwindData |  |
| 66 | `GetFinalAnimatingPosition` | `0x4740` | 116 | UnwindData |  |
| 68 | `GetGadgetAnimation` | `0x47C0` | 111 | UnwindData |  |
| 85 | `GetGadgetVisual` | `0x4840` | 117 | UnwindData |  |
| 107 | `ReleaseDetachedObjects` | `0x48C0` | 72 | UnwindData |  |
| 110 | `RemoveClippingImmunityFromVisual` | `0x4910` | 146 | UnwindData |  |
| 114 | `ScheduleGadgetTransitions` | `0x49B0` | 121 | UnwindData |  |
| 135 | `SetMinimumDCompVersion` | `0x4A30` | 97 | UnwindData |  |
| 137 | `SetTransitionVisualProperties` | `0x4AA0` | 105 | UnwindData |  |
| 29 | `DUserGetAlphaPRID` | `0x5860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `DUserGetRectPRID` | `0x5870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `DUserGetRotatePRID` | `0x5880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `DUserGetScalePRID` | `0x5890` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `DUserStopAnimation` | `0x5FB0` | 143 | UnwindData |  |
| 1 | `DUserCastHandle` | `0x1A430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DUserDeleteGadget` | `0x1A450` | 205 | UnwindData |  |
| 3 | `GetStdColorBrushF` | `0x1A830` | 163 | UnwindData |  |
| 4 | `GetStdColorF` | `0x1A8E0` | 100 | UnwindData |  |
| 5 | `GetStdColorPenF` | `0x1A950` | 163 | UnwindData |  |
| 6 | `UtilDrawOutlineRect` | `0x1ABF0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `AddGadgetMessageHandler` | `0x1ACA0` | 311 | UnwindData |  |
| 8 | `AddLayeredRef` | `0x1ADE0` | 203 | UnwindData |  |
| 9 | `AdjustClipInsideRef` | `0x1AEC0` | 213 | UnwindData |  |
| 10 | `AttachWndProcA` | `0x1AFA0` | 48 | UnwindData |  |
| 11 | `AttachWndProcW` | `0x1AFE0` | 45 | UnwindData |  |
| 18 | `ClearPushedOpacitiesFromGadgetTree` | `0x1B020` | 261 | UnwindData |  |
| 20 | `CreateAction` | `0x1B130` | 171 | UnwindData |  |
| 21 | `CreateGadget` | `0x1B1F0` | 767 | UnwindData |  |
| 23 | `DUserBuildGadget` | `0x1B500` | 65 | UnwindData |  |
| 24 | `DUserCastClass` | `0x1B550` | 89 | UnwindData |  |
| 25 | `DUserCastDirect` | `0x1B5B0` | 28 | UnwindData |  |
| 26 | `DUserFindClass` | `0x1B5E0` | 84 | UnwindData |  |
| 27 | `DUserFlushDeferredMessages` | `0x1B640` | 114 | UnwindData |  |
| 28 | `DUserFlushMessages` | `0x1B6C0` | 110 | UnwindData |  |
| 30 | `DUserGetGutsData` | `0x1B740` | 94 | UnwindData |  |
| 34 | `DUserInstanceOf` | `0x1B7B0` | 76 | UnwindData |  |
| 35 | `DUserPostEvent` | `0x1B810` | 153 | UnwindData |  |
| 36 | `DUserPostMethod` | `0x1B8B0` | 151 | UnwindData |  |
| 37 | `DUserRegisterGuts` | `0x1B950` | 171 | UnwindData |  |
| 38 | `DUserRegisterStub` | `0x1BA10` | 171 | UnwindData |  |
| 39 | `DUserRegisterSuper` | `0x1BAD0` | 171 | UnwindData |  |
| 40 | `DUserSendEvent` | `0x1BB90` | 205 | UnwindData |  |
| 41 | `DUserSendMethod` | `0x1BC70` | 166 | UnwindData |  |
| 44 | `DeleteHandle` | `0x1BD20` | 429 | UnwindData |  |
| 47 | `DetachWndProc` | `0x1BEE0` | 148 | UnwindData |  |
| 48 | `DisableContainerHwnd` | `0x1BF80` | 58 | UnwindData |  |
| 50 | `DrawGadgetTree` | `0x1BFC0` | 279 | UnwindData |  |
| 53 | `EnumGadgets` | `0x1C0E0` | 323 | UnwindData |  |
| 54 | `FindGadgetFromPoint` | `0x1C230` | 245 | UnwindData |  |
| 55 | `FindGadgetMessages` | `0x1C330` | 258 | UnwindData |  |
| 56 | `FindStdColor` | `0x1C440` | 130 | UnwindData |  |
| 57 | `FireGadgetMessages` | `0x1C4D0` | 242 | UnwindData |  |
| 58 | `ForwardGadgetMessage` | `0x1C5D0` | 344 | UnwindData |  |
| 59 | `FreeGdiDxInteropStagingBuffer` | `0x1C730` | 172 | UnwindData |  |
| 60 | `GadgetTransCompositionChanged` | `0x1C7F0` | 232 | UnwindData |  |
| 62 | `GetActionTimeslice` | `0x1C8E0` | 160 | UnwindData |  |
| 64 | `GetDUserModule` | `0x1C990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `GetGadget` | `0x1C9A0` | 206 | UnwindData |  |
| 69 | `GetGadgetBitmap` | `0x1CA80` | 259 | UnwindData |  |
| 70 | `GetGadgetBufferInfo` | `0x1CB90` | 249 | UnwindData |  |
| 71 | `GetGadgetCenterPoint` | `0x1CC90` | 219 | UnwindData |  |
| 72 | `GetGadgetFlags` | `0x1CD80` | 185 | UnwindData |  |
| 73 | `GetGadgetFocus` | `0x1CE40` | 133 | UnwindData |  |
| 74 | `GetGadgetLayerInfo` | `0x1CED0` | 224 | UnwindData |  |
| 124 | `SetGadgetLayerInfo` | `0x1CED0` | 224 | UnwindData |  |
| 75 | `GetGadgetMessageFilter` | `0x1CFC0` | 197 | UnwindData |  |
| 76 | `GetGadgetProperty` | `0x1D090` | 233 | UnwindData |  |
| 77 | `GetGadgetRect` | `0x1D180` | 231 | UnwindData |  |
| 78 | `GetGadgetRgn` | `0x1D270` | 237 | UnwindData |  |
| 79 | `GetGadgetRootInfo` | `0x1D370` | 239 | UnwindData |  |
| 80 | `GetGadgetRotation` | `0x1D470` | 213 | UnwindData |  |
| 81 | `GetGadgetScale` | `0x1D550` | 219 | UnwindData |  |
| 82 | `GetGadgetSize` | `0x1D640` | 233 | UnwindData |  |
| 83 | `GetGadgetStyle` | `0x1D730` | 184 | UnwindData |  |
| 84 | `GetGadgetTicket` | `0x1D7F0` | 356 | UnwindData |  |
| 86 | `GetMessageExA` | `0x1D960` | 153 | UnwindData |  |
| 87 | `GetMessageExW` | `0x1DA00` | 153 | UnwindData |  |
| 88 | `GetStdColorBrushI` | `0x1DAA0` | 204 | UnwindData |  |
| 89 | `GetStdColorI` | `0x1DB80` | 59 | UnwindData |  |
| 90 | `GetStdColorName` | `0x1DBD0` | 61 | UnwindData |  |
| 91 | `GetStdColorPenI` | `0x1DC20` | 218 | UnwindData |  |
| 92 | `GetStdPalette` | `0x1DD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `InitGadgetComponent` | `0x1DD10` | 188 | UnwindData |  |
| 94 | `InitGadgets` | `0x1DDE0` | 102 | UnwindData |  |
| 95 | `InvalidateGadget` | `0x1DE50` | 259 | UnwindData |  |
| 96 | `InvalidateLayeredDescendants` | `0x1DF60` | 259 | UnwindData |  |
| 97 | `IsGadgetParentChainStyle` | `0x1E070` | 254 | UnwindData |  |
| 98 | `IsInsideContext` | `0x1E180` | 78 | UnwindData |  |
| 99 | `IsStartDelete` | `0x1E1E0` | 181 | UnwindData |  |
| 100 | `LookupGadgetTicket` | `0x1E2A0` | 175 | UnwindData |  |
| 101 | `MapGadgetPoints` | `0x1E360` | 281 | UnwindData |  |
| 102 | `PeekMessageExA` | `0x1E480` | 183 | UnwindData |  |
| 103 | `PeekMessageExW` | `0x1E540` | 179 | UnwindData |  |
| 104 | `RegisterGadgetMessage` | `0x1E600` | 107 | UnwindData |  |
| 105 | `RegisterGadgetMessageString` | `0x1E680` | 39 | UnwindData |  |
| 140 | `UnregisterGadgetMessageString` | `0x1E680` | 39 | UnwindData |  |
| 106 | `RegisterGadgetProperty` | `0x1E6B0` | 107 | UnwindData |  |
| 108 | `ReleaseLayeredRef` | `0x1E730` | 201 | UnwindData |  |
| 109 | `ReleaseMouseCapture` | `0x1E800` | 206 | UnwindData |  |
| 111 | `RemoveGadgetMessageHandler` | `0x1E8E0` | 311 | UnwindData |  |
| 112 | `RemoveGadgetProperty` | `0x1EA20` | 265 | UnwindData |  |
| 113 | `ResetDUserDevice` | `0x1EB30` | 226 | UnwindData |  |
| 115 | `SetActionTimeslice` | `0x1EC20` | 152 | UnwindData |  |
| 116 | `SetAtlasingHints` | `0x1ECC0` | 136 | UnwindData |  |
| 117 | `SetGadgetBufferInfo` | `0x1ED50` | 299 | UnwindData |  |
| 118 | `SetGadgetCenterPoint` | `0x1EE90` | 307 | UnwindData |  |
| 119 | `SetGadgetFillF` | `0x1EFD0` | 269 | UnwindData |  |
| 120 | `SetGadgetFillI` | `0x1F0F0` | 315 | UnwindData |  |
| 121 | `SetGadgetFlags` | `0x1F240` | 315 | UnwindData |  |
| 122 | `SetGadgetFocus` | `0x1F390` | 278 | UnwindData |  |
| 123 | `SetGadgetFocusEx` | `0x1F4B0` | 274 | UnwindData |  |
| 125 | `SetGadgetMessageFilter` | `0x1F5D0` | 314 | UnwindData |  |
| 126 | `SetGadgetOrder` | `0x1F710` | 354 | UnwindData |  |
| 127 | `SetGadgetParent` | `0x1F880` | 365 | UnwindData |  |
| 128 | `SetGadgetProperty` | `0x1FA00` | 288 | UnwindData |  |
| 129 | `SetGadgetRect` | `0x1FB30` | 392 | UnwindData |  |
| 130 | `SetGadgetRootInfo` | `0x1FCC0` | 310 | UnwindData |  |
| 131 | `SetGadgetRotation` | `0x1FE00` | 282 | UnwindData |  |
| 132 | `SetGadgetScale` | `0x1FF20` | 307 | UnwindData |  |
| 133 | `SetGadgetStyle` | `0x20060` | 318 | UnwindData |  |
| 134 | `SetHardwareDeviceUsage` | `0x201B0` | 162 | UnwindData |  |
| 136 | `SetRestoreCachedLayeredRefFlag` | `0x20260` | 173 | UnwindData |  |
| 138 | `SetWindowResizeFlag` | `0x20320` | 192 | UnwindData |  |
| 139 | `UnregisterGadgetMessage` | `0x203F0` | 95 | UnwindData |  |
| 141 | `UnregisterGadgetProperty` | `0x20460` | 95 | UnwindData |  |
| 142 | `UtilBuildFont` | `0x204D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `UtilDrawBlendRect` | `0x204E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `UtilGetColor` | `0x204F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `UtilSetBackground` | `0x20500` | 85 | UnwindData |  |
| 146 | `WaitMessageEx` | `0x20560` | 78 | UnwindData |  |
