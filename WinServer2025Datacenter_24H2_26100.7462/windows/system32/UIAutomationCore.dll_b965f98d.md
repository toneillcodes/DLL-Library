# Binary Specification: UIAutomationCore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\UIAutomationCore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b965f98de0943c8b256a7a868f1f9b6e58ddb0f90f5982f2c3b7b00133b6414a`
* **Total Exported Functions:** 110

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 102 | `UiaReturnRawElementProvider` | `0x87340` | 2,823 | UnwindData |  |
| 82 | `UiaLookupId` | `0x88650` | 527 | UnwindData |  |
| 80 | `UiaHostProviderFromHwnd` | `0x88920` | 198 | UnwindData |  |
| 98 | `UiaRaiseStructureChangedEvent` | `0x89490` | 1,661 | UnwindData |  |
| 95 | `UiaRaiseAutomationPropertyChangedEvent` | `0x8A090` | 148 | UnwindData |  |
| 65 | `UiaEventAddWindow` | `0xA51A0` | 655 | UnwindData |  |
| 85 | `UiaNodeFromHandle` | `0xA55C0` | 339 | UnwindData |  |
| 97 | `UiaRaiseNotificationEvent` | `0xD86A0` | 350 | UnwindData |  |
| 62 | `UiaClientsAreListening` | `0xEECD0` | 55 | UnwindData |  |
| 86 | `UiaNodeFromPoint` | `0xF4170` | 646 | UnwindData |  |
| 67 | `UiaFind` | `0xF4400` | 3,253 | UnwindData |  |
| 70 | `UiaGetPropertyValue` | `0xF5240` | 415 | UnwindData |  |
| 75 | `UiaGetUpdatedCache` | `0xF53F0` | 707 | UnwindData |  |
| 94 | `UiaRaiseAutomationEvent` | `0x105F40` | 1,684 | UnwindData |  |
| 92 | `UiaRaiseActiveTextPositionChangedEvent` | `0x1079E0` | 228 | UnwindData |  |
| 64 | `UiaDisconnectProvider` | `0x11FCA0` | 911 | UnwindData |  |
| 29 | `StartIgnoringLeaks` | `0x12EBE0` | 57,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `StopIgnoringLeaks` | `0x12EBE0` | 57,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x13CB20` | 63 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x1412B0` | 27,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `UiaNodeRelease` | `0x147FA0` | 238 | UnwindData |  |
| 72 | `UiaGetReservedNotSupportedValue` | `0x14E310` | 71 | UnwindData |  |
| 66 | `UiaEventRemoveWindow` | `0x153210` | 358 | UnwindData |  |
| 78 | `UiaHUiaNodeFromVariant` | `0x153C70` | 163 | UnwindData |  |
| 79 | `UiaHasServerSideProvider` | `0x156850` | 50 | UnwindData |  |
| 83 | `UiaNavigate` | `0x157C30` | 815 | UnwindData |  |
| 71 | `UiaGetReservedMixedAttributeValue` | `0x15CFA0` | 71 | UnwindData |  |
| 73 | `UiaGetRootNode` | `0x15EAA0` | 189 | UnwindData |  |
| 81 | `UiaIAccessibleFromProvider` | `0x164060` | 618 | UnwindData |  |
| 69 | `UiaGetPatternProvider` | `0x165B90` | 411 | UnwindData |  |
| 11 | `InitializeChannelBasedConnectionForProviderProxy` | `0x166350` | 3,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `UiaNodeFromProvider` | `0x167110` | 225 | UnwindData |  |
| 1 | `DllGetActivationFactory` | `0x198950` | 12,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x19BA80` | 95 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x19BAF0` | 199 | UnwindData |  |
| 10 | `IgnoreLeaksInCurrentlyTrackedMemory` | `0x19BD10` | 18 | UnwindData |  |
| 13 | `IsIgnoringLeaks` | `0x19BD30` | 21 | UnwindData |  |
| 21 | `PostTestCheckForLeaks` | `0x19BD50` | 18 | UnwindData |  |
| 105 | `UpdateErrorLoggingCallback` | `0x19BD70` | 18 | UnwindData |  |
| 63 | `UiaDisconnectAllProviders` | `0x19BF10` | 162 | UnwindData |  |
| 76 | `UiaHPatternObjectFromVariant` | `0x19BFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `UiaHTextRangeFromVariant` | `0x19BFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `UiaProviderFromIAccessible` | `0x19BFD0` | 530 | UnwindData |  |
| 93 | `UiaRaiseAsyncContentLoadedEvent` | `0x19C1F0` | 205 | UnwindData |  |
| 96 | `UiaRaiseChangesEvent` | `0x19C2D0` | 229 | UnwindData |  |
| 99 | `UiaRaiseTextEditTextChangedEvent` | `0x19C3C0` | 228 | UnwindData |  |
| 6 | `DockPattern_SetDockPosition` | `0x19DBA0` | 161 | UnwindData |  |
| 7 | `ExpandCollapsePattern_Collapse` | `0x19DC50` | 112 | UnwindData |  |
| 8 | `ExpandCollapsePattern_Expand` | `0x19DCD0` | 112 | UnwindData |  |
| 9 | `GridPattern_GetItem` | `0x19DD50` | 423 | UnwindData |  |
| 12 | `InvokePattern_Invoke` | `0x19DF00` | 148 | UnwindData |  |
| 14 | `ItemContainerPattern_FindItemByProperty` | `0x19DFA0` | 656 | UnwindData |  |
| 15 | `LegacyIAccessiblePattern_DoDefaultAction` | `0x19E240` | 118 | UnwindData |  |
| 16 | `LegacyIAccessiblePattern_GetIAccessible` | `0x19E2C0` | 130 | UnwindData |  |
| 17 | `LegacyIAccessiblePattern_Select` | `0x19E350` | 131 | UnwindData |  |
| 18 | `LegacyIAccessiblePattern_SetValue` | `0x19E3E0` | 133 | UnwindData |  |
| 19 | `MultipleViewPattern_GetViewName` | `0x19E470` | 160 | UnwindData |  |
| 20 | `MultipleViewPattern_SetCurrentView` | `0x19E520` | 131 | UnwindData |  |
| 22 | `RangeValuePattern_SetValue` | `0x19E5B0` | 128 | UnwindData |  |
| 23 | `ScrollItemPattern_ScrollIntoView` | `0x19E640` | 145 | UnwindData |  |
| 24 | `ScrollPattern_Scroll` | `0x19E6E0` | 141 | UnwindData |  |
| 25 | `ScrollPattern_SetScrollPercent` | `0x19E780` | 153 | UnwindData |  |
| 26 | `SelectionItemPattern_AddToSelection` | `0x19E820` | 112 | UnwindData |  |
| 27 | `SelectionItemPattern_RemoveFromSelection` | `0x19E8A0` | 112 | UnwindData |  |
| 28 | `SelectionItemPattern_Select` | `0x19E920` | 112 | UnwindData |  |
| 31 | `SynchronizedInputPattern_Cancel` | `0x19E9A0` | 112 | UnwindData |  |
| 32 | `SynchronizedInputPattern_StartListening` | `0x19EA20` | 125 | UnwindData |  |
| 33 | `TextPattern_GetSelection` | `0x19EAB0` | 233 | UnwindData |  |
| 34 | `TextPattern_GetVisibleRanges` | `0x19EBA0` | 233 | UnwindData |  |
| 35 | `TextPattern_RangeFromChild` | `0x19EC90` | 389 | UnwindData |  |
| 36 | `TextPattern_RangeFromPoint` | `0x19EE20` | 282 | UnwindData |  |
| 37 | `TextPattern_get_DocumentRange` | `0x19EF40` | 159 | UnwindData |  |
| 38 | `TextPattern_get_SupportedTextSelection` | `0x19EFF0` | 142 | UnwindData |  |
| 39 | `TextRange_AddToSelection` | `0x19F090` | 197 | UnwindData |  |
| 40 | `TextRange_Clone` | `0x19F160` | 231 | UnwindData |  |
| 41 | `TextRange_Compare` | `0x19F250` | 329 | UnwindData |  |
| 42 | `TextRange_CompareEndpoints` | `0x19F3A0` | 369 | UnwindData |  |
| 43 | `TextRange_ExpandToEnclosingUnit` | `0x19F520` | 210 | UnwindData |  |
| 44 | `TextRange_FindAttribute` | `0x19F600` | 319 | UnwindData |  |
| 45 | `TextRange_FindText` | `0x19F750` | 292 | UnwindData |  |
| 46 | `TextRange_GetAttributeValue` | `0x19F880` | 301 | UnwindData |  |
| 47 | `TextRange_GetBoundingRectangles` | `0x19F9C0` | 355 | UnwindData |  |
| 48 | `TextRange_GetChildren` | `0x19FB30` | 407 | UnwindData |  |
| 49 | `TextRange_GetEnclosingElement` | `0x19FCD0` | 443 | UnwindData |  |
| 50 | `TextRange_GetText` | `0x19FEA0` | 245 | UnwindData |  |
| 51 | `TextRange_Move` | `0x19FFA0` | 259 | UnwindData |  |
| 52 | `TextRange_MoveEndpointByRange` | `0x1A00B0` | 331 | UnwindData |  |
| 53 | `TextRange_MoveEndpointByUnit` | `0x1A0210` | 297 | UnwindData |  |
| 54 | `TextRange_RemoveFromSelection` | `0x1A0340` | 197 | UnwindData |  |
| 55 | `TextRange_ScrollIntoView` | `0x1A0410` | 210 | UnwindData |  |
| 56 | `TextRange_Select` | `0x1A04F0` | 197 | UnwindData |  |
| 57 | `TogglePattern_Toggle` | `0x1A05C0` | 148 | UnwindData |  |
| 58 | `TransformPattern_Move` | `0x1A0660` | 153 | UnwindData |  |
| 59 | `TransformPattern_Resize` | `0x1A0700` | 153 | UnwindData |  |
| 60 | `TransformPattern_Rotate` | `0x1A07A0` | 128 | UnwindData |  |
| 61 | `UiaAddEvent` | `0x1A0830` | 398 | UnwindData |  |
| 68 | `UiaGetErrorDescription` | `0x1A09D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `UiaGetRuntimeId` | `0x1A09F0` | 178 | UnwindData |  |
| 84 | `UiaNodeFromFocus` | `0x1A0AB0` | 541 | UnwindData |  |
| 89 | `UiaPatternRelease` | `0x1A0CE0` | 151 | UnwindData |  |
| 90 | `UiaProviderForNonClient` | `0x1A0D80` | 242 | UnwindData |  |
| 100 | `UiaRegisterProviderCallback` | `0x1A0E80` | 53 | UnwindData |  |
| 101 | `UiaRemoveEvent` | `0x1A0EC0` | 232 | UnwindData |  |
| 103 | `UiaSetFocus` | `0x1A0FB0` | 144 | UnwindData |  |
| 104 | `UiaTextRangeRelease` | `0x1A1050` | 84 | UnwindData |  |
| 106 | `ValuePattern_SetValue` | `0x1A10B0` | 163 | UnwindData |  |
| 107 | `VirtualizedItemPattern_Realize` | `0x1A1160` | 145 | UnwindData |  |
| 108 | `WindowPattern_Close` | `0x1A1200` | 115 | UnwindData |  |
| 109 | `WindowPattern_SetWindowVisualState` | `0x1A1280` | 131 | UnwindData |  |
| 110 | `WindowPattern_WaitForInputIdle` | `0x1A1310` | 159 | UnwindData |  |
