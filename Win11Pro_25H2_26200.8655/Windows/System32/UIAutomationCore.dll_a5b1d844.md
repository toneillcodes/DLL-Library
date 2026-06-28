# Binary Specification: UIAutomationCore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\UIAutomationCore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a5b1d84414442d990d28f469173edb118a61c8518421a81198a85ec0f779af40`
* **Total Exported Functions:** 110

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 65 | `UiaEventAddWindow` | `0x64E70` | 655 | UnwindData |  |
| 85 | `UiaNodeFromHandle` | `0x65290` | 339 | UnwindData |  |
| 102 | `UiaReturnRawElementProvider` | `0xA7A50` | 2,823 | UnwindData |  |
| 82 | `UiaLookupId` | `0xA8D60` | 527 | UnwindData |  |
| 80 | `UiaHostProviderFromHwnd` | `0xA9030` | 198 | UnwindData |  |
| 98 | `UiaRaiseStructureChangedEvent` | `0xA9BA0` | 1,661 | UnwindData |  |
| 95 | `UiaRaiseAutomationPropertyChangedEvent` | `0xAA7A0` | 148 | UnwindData |  |
| 97 | `UiaRaiseNotificationEvent` | `0xD69B0` | 350 | UnwindData |  |
| 62 | `UiaClientsAreListening` | `0xECF90` | 55 | UnwindData |  |
| 86 | `UiaNodeFromPoint` | `0xF2430` | 646 | UnwindData |  |
| 67 | `UiaFind` | `0xF26C0` | 3,253 | UnwindData |  |
| 70 | `UiaGetPropertyValue` | `0xF3500` | 415 | UnwindData |  |
| 75 | `UiaGetUpdatedCache` | `0xF36B0` | 707 | UnwindData |  |
| 94 | `UiaRaiseAutomationEvent` | `0x104200` | 1,684 | UnwindData |  |
| 92 | `UiaRaiseActiveTextPositionChangedEvent` | `0x105FD0` | 228 | UnwindData |  |
| 64 | `UiaDisconnectProvider` | `0x11E170` | 911 | UnwindData |  |
| 29 | `StartIgnoringLeaks` | `0x12E550` | 57,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `StopIgnoringLeaks` | `0x12E550` | 57,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x13C5D0` | 63 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x140E60` | 27,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `UiaNodeRelease` | `0x147B50` | 238 | UnwindData |  |
| 72 | `UiaGetReservedNotSupportedValue` | `0x14DBA0` | 71 | UnwindData |  |
| 66 | `UiaEventRemoveWindow` | `0x152AA0` | 358 | UnwindData |  |
| 78 | `UiaHUiaNodeFromVariant` | `0x153740` | 163 | UnwindData |  |
| 79 | `UiaHasServerSideProvider` | `0x155EC0` | 50 | UnwindData |  |
| 83 | `UiaNavigate` | `0x1572A0` | 815 | UnwindData |  |
| 71 | `UiaGetReservedMixedAttributeValue` | `0x15C8D0` | 71 | UnwindData |  |
| 73 | `UiaGetRootNode` | `0x15E3D0` | 189 | UnwindData |  |
| 81 | `UiaIAccessibleFromProvider` | `0x1639B0` | 618 | UnwindData |  |
| 69 | `UiaGetPatternProvider` | `0x1654E0` | 411 | UnwindData |  |
| 11 | `InitializeChannelBasedConnectionForProviderProxy` | `0x165CA0` | 3,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `UiaNodeFromProvider` | `0x166A60` | 225 | UnwindData |  |
| 1 | `DllGetActivationFactory` | `0x1988C0` | 12,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x19BA50` | 95 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x19BAC0` | 199 | UnwindData |  |
| 10 | `IgnoreLeaksInCurrentlyTrackedMemory` | `0x19BCE0` | 18 | UnwindData |  |
| 13 | `IsIgnoringLeaks` | `0x19BD00` | 21 | UnwindData |  |
| 21 | `PostTestCheckForLeaks` | `0x19BD20` | 18 | UnwindData |  |
| 105 | `UpdateErrorLoggingCallback` | `0x19BD40` | 18 | UnwindData |  |
| 63 | `UiaDisconnectAllProviders` | `0x19BEE0` | 162 | UnwindData |  |
| 76 | `UiaHPatternObjectFromVariant` | `0x19BF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `UiaHTextRangeFromVariant` | `0x19BF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `UiaProviderFromIAccessible` | `0x19BFA0` | 530 | UnwindData |  |
| 93 | `UiaRaiseAsyncContentLoadedEvent` | `0x19C1C0` | 205 | UnwindData |  |
| 96 | `UiaRaiseChangesEvent` | `0x19C2A0` | 229 | UnwindData |  |
| 99 | `UiaRaiseTextEditTextChangedEvent` | `0x19C390` | 228 | UnwindData |  |
| 6 | `DockPattern_SetDockPosition` | `0x19DB70` | 161 | UnwindData |  |
| 7 | `ExpandCollapsePattern_Collapse` | `0x19DC20` | 112 | UnwindData |  |
| 8 | `ExpandCollapsePattern_Expand` | `0x19DCA0` | 112 | UnwindData |  |
| 9 | `GridPattern_GetItem` | `0x19DD20` | 423 | UnwindData |  |
| 12 | `InvokePattern_Invoke` | `0x19DED0` | 148 | UnwindData |  |
| 14 | `ItemContainerPattern_FindItemByProperty` | `0x19DF70` | 656 | UnwindData |  |
| 15 | `LegacyIAccessiblePattern_DoDefaultAction` | `0x19E210` | 118 | UnwindData |  |
| 16 | `LegacyIAccessiblePattern_GetIAccessible` | `0x19E290` | 130 | UnwindData |  |
| 17 | `LegacyIAccessiblePattern_Select` | `0x19E320` | 131 | UnwindData |  |
| 18 | `LegacyIAccessiblePattern_SetValue` | `0x19E3B0` | 133 | UnwindData |  |
| 19 | `MultipleViewPattern_GetViewName` | `0x19E440` | 160 | UnwindData |  |
| 20 | `MultipleViewPattern_SetCurrentView` | `0x19E4F0` | 131 | UnwindData |  |
| 22 | `RangeValuePattern_SetValue` | `0x19E580` | 128 | UnwindData |  |
| 23 | `ScrollItemPattern_ScrollIntoView` | `0x19E610` | 145 | UnwindData |  |
| 24 | `ScrollPattern_Scroll` | `0x19E6B0` | 141 | UnwindData |  |
| 25 | `ScrollPattern_SetScrollPercent` | `0x19E750` | 153 | UnwindData |  |
| 26 | `SelectionItemPattern_AddToSelection` | `0x19E7F0` | 112 | UnwindData |  |
| 27 | `SelectionItemPattern_RemoveFromSelection` | `0x19E870` | 112 | UnwindData |  |
| 28 | `SelectionItemPattern_Select` | `0x19E8F0` | 112 | UnwindData |  |
| 31 | `SynchronizedInputPattern_Cancel` | `0x19E970` | 112 | UnwindData |  |
| 32 | `SynchronizedInputPattern_StartListening` | `0x19E9F0` | 125 | UnwindData |  |
| 33 | `TextPattern_GetSelection` | `0x19EA80` | 233 | UnwindData |  |
| 34 | `TextPattern_GetVisibleRanges` | `0x19EB70` | 233 | UnwindData |  |
| 35 | `TextPattern_RangeFromChild` | `0x19EC60` | 389 | UnwindData |  |
| 36 | `TextPattern_RangeFromPoint` | `0x19EDF0` | 282 | UnwindData |  |
| 37 | `TextPattern_get_DocumentRange` | `0x19EF10` | 159 | UnwindData |  |
| 38 | `TextPattern_get_SupportedTextSelection` | `0x19EFC0` | 142 | UnwindData |  |
| 39 | `TextRange_AddToSelection` | `0x19F060` | 197 | UnwindData |  |
| 40 | `TextRange_Clone` | `0x19F130` | 231 | UnwindData |  |
| 41 | `TextRange_Compare` | `0x19F220` | 329 | UnwindData |  |
| 42 | `TextRange_CompareEndpoints` | `0x19F370` | 369 | UnwindData |  |
| 43 | `TextRange_ExpandToEnclosingUnit` | `0x19F4F0` | 210 | UnwindData |  |
| 44 | `TextRange_FindAttribute` | `0x19F5D0` | 319 | UnwindData |  |
| 45 | `TextRange_FindText` | `0x19F720` | 292 | UnwindData |  |
| 46 | `TextRange_GetAttributeValue` | `0x19F850` | 301 | UnwindData |  |
| 47 | `TextRange_GetBoundingRectangles` | `0x19F990` | 355 | UnwindData |  |
| 48 | `TextRange_GetChildren` | `0x19FB00` | 407 | UnwindData |  |
| 49 | `TextRange_GetEnclosingElement` | `0x19FCA0` | 443 | UnwindData |  |
| 50 | `TextRange_GetText` | `0x19FE70` | 245 | UnwindData |  |
| 51 | `TextRange_Move` | `0x19FF70` | 259 | UnwindData |  |
| 52 | `TextRange_MoveEndpointByRange` | `0x1A0080` | 331 | UnwindData |  |
| 53 | `TextRange_MoveEndpointByUnit` | `0x1A01E0` | 297 | UnwindData |  |
| 54 | `TextRange_RemoveFromSelection` | `0x1A0310` | 197 | UnwindData |  |
| 55 | `TextRange_ScrollIntoView` | `0x1A03E0` | 210 | UnwindData |  |
| 56 | `TextRange_Select` | `0x1A04C0` | 197 | UnwindData |  |
| 57 | `TogglePattern_Toggle` | `0x1A0590` | 148 | UnwindData |  |
| 58 | `TransformPattern_Move` | `0x1A0630` | 153 | UnwindData |  |
| 59 | `TransformPattern_Resize` | `0x1A06D0` | 153 | UnwindData |  |
| 60 | `TransformPattern_Rotate` | `0x1A0770` | 128 | UnwindData |  |
| 61 | `UiaAddEvent` | `0x1A0800` | 398 | UnwindData |  |
| 68 | `UiaGetErrorDescription` | `0x1A09A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `UiaGetRuntimeId` | `0x1A09C0` | 178 | UnwindData |  |
| 84 | `UiaNodeFromFocus` | `0x1A0A80` | 541 | UnwindData |  |
| 89 | `UiaPatternRelease` | `0x1A0CB0` | 151 | UnwindData |  |
| 90 | `UiaProviderForNonClient` | `0x1A0D50` | 242 | UnwindData |  |
| 100 | `UiaRegisterProviderCallback` | `0x1A0E50` | 53 | UnwindData |  |
| 101 | `UiaRemoveEvent` | `0x1A0E90` | 232 | UnwindData |  |
| 103 | `UiaSetFocus` | `0x1A0F80` | 144 | UnwindData |  |
| 104 | `UiaTextRangeRelease` | `0x1A1020` | 84 | UnwindData |  |
| 106 | `ValuePattern_SetValue` | `0x1A1080` | 163 | UnwindData |  |
| 107 | `VirtualizedItemPattern_Realize` | `0x1A1130` | 145 | UnwindData |  |
| 108 | `WindowPattern_Close` | `0x1A11D0` | 115 | UnwindData |  |
| 109 | `WindowPattern_SetWindowVisualState` | `0x1A1250` | 131 | UnwindData |  |
| 110 | `WindowPattern_WaitForInputIdle` | `0x1A12E0` | 159 | UnwindData |  |
