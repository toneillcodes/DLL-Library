# Binary Specification: user32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\user32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e159acbaa3e7a44213ad8faebdf45427d7008b03d5dfdc21c0cb0c9c63b712a1`
* **Total Exported Functions:** 1204

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1668 | `DefDlgProcA` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.NtdllDialogWndProc_A` |
| 1669 | `DefDlgProcW` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.NtdllDialogWndProc_W` |
| 1675 | `DefWindowProcA` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.NtdllDefWindowProc_A` |
| 1676 | `DefWindowProcW` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.NtdllDefWindowProc_W` |
| 1738 | `EditWndProc` | `0x51A0` | 828 | UnwindData |  |
| 2168 | `NotifyWinEvent` | `0x8960` | 65 | UnwindData |  |
| 2090 | `IsWinEventHookInstalled` | `0x89B0` | 95 | UnwindData |  |
| 1726 | `DrawStateW` | `0x9150` | 2,039 | UnwindData |  |
| 1721 | `DrawIcon` | `0x9950` | 42 | UnwindData |  |
| 1722 | `DrawIconEx` | `0x9980` | 892 | UnwindData |  |
| 1720 | `DrawFrameControl` | `0xAF80` | 171 | UnwindData |  |
| 2103 | `LoadBitmapA` | `0xB300` | 276 | UnwindData |  |
| 2104 | `LoadBitmapW` | `0xB420` | 26 | UnwindData |  |
| 1833 | `GetDesktopWindow` | `0xBB80` | 155 | UnwindData |  |
| 1779 | `FillRect` | `0xBC30` | 112 | UnwindData |  |
| 1800 | `GetCapture` | `0xBCB0` | 2,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2473 | `UpdateWindow` | `0xC630` | 81 | UnwindData |  |
| 2523 | *Ordinal Only* | `0xCE70` | 93 | UnwindData |  |
| 1971 | `GetTopWindow` | `0xCEE0` | 466 | UnwindData |  |
| 1981 | `GetWindow` | `0xD0C0` | 442 | UnwindData |  |
| 1794 | `GetAppCompatFlags` | `0xD610` | 65 | UnwindData |  |
| 2068 | `IsDialogMessage` | `0xD710` | 165 | UnwindData |  |
| 2069 | `IsDialogMessageA` | `0xD710` | 165 | UnwindData |  |
| 2188 | `PeekMessageA` | `0xDD40` | 458 | UnwindData |  |
| 2189 | `PeekMessageW` | `0xDF10` | 406 | UnwindData |  |
| 2070 | `IsDialogMessageW` | `0xE780` | 889 | UnwindData |  |
| 2448 | `TranslateMessage` | `0xEB00` | 143 | UnwindData |  |
| 1534 | `CallMsgFilterW` | `0xECD0` | 196 | UnwindData |  |
| 1897 | `GetMessageA` | `0xEDA0` | 429 | UnwindData |  |
| 2091 | `IsWindow` | `0xEFD0` | 367 | UnwindData |  |
| 1814 | `GetClientRect` | `0xF150` | 868 | UnwindData |  |
| 2004 | `GetWindowRect` | `0xF4C0` | 765 | UnwindData |  |
| 2162 | `MonitorFromRect` | `0xF7D0` | 61 | UnwindData |  |
| 2163 | `MonitorFromWindow` | `0xF9A0` | 736 | UnwindData |  |
| 1902 | `GetMonitorInfoA` | `0x10790` | 518 | UnwindData |  |
| 2161 | `MonitorFromPoint` | `0x10C00` | 61 | UnwindData |  |
| 2085 | `IsThreadDesktopComposited` | `0x114A0` | 88 | UnwindData |  |
| 2356 | `SetProcessDpiAwarenessContext` | `0x11DF0` | 162 | UnwindData |  |
| 2707 | *Ordinal Only* | `0x11EA0` | 151 | UnwindData |  |
| 2366 | `SetScrollInfo` | `0x11F40` | 175 | UnwindData |  |
| 2089 | `IsValidDpiAwarenessContext` | `0x12000` | 146 | UnwindData |  |
| 2558 | *Ordinal Only* | `0x12100` | 140 | UnwindData |  |
| 1517 | `AreDpiAwarenessContextsEqual` | `0x121A0` | 350 | UnwindData |  |
| 1798 | `GetAwarenessFromDpiAwarenessContext` | `0x12310` | 142 | UnwindData |  |
| 2378 | `SetThreadDpiAwarenessContext` | `0x12400` | 29 | UnwindData |  |
| 2432 | `SystemParametersInfoW` | `0x12DB0` | 173 | UnwindData |  |
| 1509 | `AdjustWindowRectExForDpi` | `0x12EE0` | 147 | UnwindData |  |
| 1795 | `GetAppCompatFlags2` | `0x13210` | 90 | UnwindData |  |
| 1962 | `GetSystemMetricsForDpi` | `0x13530` | 211 | UnwindData |  |
| 2013 | `GetWindowTextW` | `0x13610` | 160 | UnwindData |  |
| 1961 | `GetSystemMetrics` | `0x13730` | 218 | UnwindData |  |
| 2572 | *Ordinal Only* | `0x14EF0` | 39 | UnwindData |  |
| 1840 | `GetDlgItem` | `0x14F20` | 170 | UnwindData |  |
| 2096 | `IsWindowUnicode` | `0x14FD0` | 33 | UnwindData |  |
| 1811 | `GetClassNameA` | `0x15770` | 165 | UnwindData |  |
| 1847 | `GetDpiForSystem` | `0x15820` | 231 | UnwindData |  |
| 2146 | `MapWindowPoints` | `0x15910` | 76 | UnwindData |  |
| 1991 | `GetWindowInfo` | `0x15AE0` | 1,041 | UnwindData |  |
| 2282 | `ScreenToClient` | `0x16150` | 509 | UnwindData |  |
| 2712 | *Ordinal Only* | `0x16360` | 18 | UnwindData |  |
| 2292 | `SendMessageA` | `0x16540` | 181 | UnwindData |  |
| 2297 | `SendMessageW` | `0x16600` | 35 | UnwindData |  |
| 1537 | `CallWindowProcW` | `0x171A0` | 39 | UnwindData |  |
| 2012 | `GetWindowTextLengthW` | `0x18320` | 82 | UnwindData |  |
| 1848 | `GetDpiForWindow` | `0x18380` | 90 | UnwindData |  |
| 1536 | `CallWindowProcA` | `0x183E0` | 269 | UnwindData |  |
| 2574 | *Ordinal Only* | `0x18500` | 54 | UnwindData |  |
| 2093 | `IsWindowEnabled` | `0x18540` | 62 | UnwindData |  |
| 1993 | `GetWindowLongPtrA` | `0x18590` | 64 | UnwindData |  |
| 1995 | `GetWindowLongW` | `0x187D0` | 408 | UnwindData |  |
| 1994 | `GetWindowLongPtrW` | `0x18B20` | 408 | UnwindData |  |
| 1992 | `GetWindowLongA` | `0x19630` | 64 | UnwindData |  |
| 2536 | *Ordinal Only* | `0x1A5C0` | 264 | UnwindData |  |
| 2394 | `SetWindowLongPtrW` | `0x1AB90` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2051 | `InsertMenuW` | `0x1AE30` | 146 | UnwindData |  |
| 2347 | `SetMenuItemInfoW` | `0x1AED0` | 133 | UnwindData |  |
| 1887 | `GetMenuDefaultItem` | `0x1AF60` | 57 | UnwindData |  |
| 1896 | `GetMenuStringW` | `0x1AFA0` | 133 | UnwindData |  |
| 1894 | `GetMenuState` | `0x1B030` | 114 | UnwindData |  |
| 2077 | `IsMenu` | `0x1B100` | 27 | UnwindData |  |
| 1576 | `CheckMenuItem` | `0x1B130` | 122 | UnwindData |  |
| 1577 | `CheckMenuRadioItem` | `0x1B1B0` | 450 | UnwindData |  |
| 1890 | `GetMenuItemID` | `0x1B380` | 133 | UnwindData |  |
| 1740 | `EnableMenuItem` | `0x1B410` | 151 | UnwindData |  |
| 1956 | `GetSubMenu` | `0x1B4B0` | 142 | UnwindData |  |
| 1889 | `GetMenuItemCount` | `0x1B550` | 60 | UnwindData |  |
| 2050 | `InsertMenuItemW` | `0x1B750` | 429 | UnwindData |  |
| 1892 | `GetMenuItemInfoW` | `0x1B910` | 259 | UnwindData |  |
| 1516 | `AppendMenuW` | `0x1C1C0` | 139 | UnwindData |  |
| 1891 | `GetMenuItemInfoA` | `0x1C6A0` | 259 | UnwindData |  |
| 1888 | `GetMenuInfo` | `0x1C950` | 154 | UnwindData |  |
| 1895 | `GetMenuStringA` | `0x1CC90` | 131 | UnwindData |  |
| 2160 | `ModifyMenuW` | `0x1CD20` | 143 | UnwindData |  |
| 2345 | `SetMenuItemBitmaps` | `0x1CDC0` | 127 | UnwindData |  |
| 1515 | `AppendMenuA` | `0x1CE50` | 139 | UnwindData |  |
| 2346 | `SetMenuItemInfoA` | `0x1CEF0` | 136 | UnwindData |  |
| 2049 | `InsertMenuItemA` | `0x1CF80` | 136 | UnwindData |  |
| 1883 | `GetMenu` | `0x1D1E0` | 109 | UnwindData |  |
| 2048 | `InsertMenuA` | `0x1D510` | 146 | UnwindData |  |
| 1672 | `DefMDIChildProcA` | `0x1E210` | 23 | UnwindData |  |
| 1673 | `DefMDIChildProcW` | `0x1E230` | 20 | UnwindData |  |
| 1670 | `DefFrameProcA` | `0x1E5F0` | 33 | UnwindData |  |
| 1671 | `DefFrameProcW` | `0x1E620` | 30 | UnwindData |  |
| 1616 | `CreateIcon` | `0x1F5F0` | 201 | UnwindData |  |
| 1605 | `CreateCursor` | `0x1F700` | 233 | UnwindData |  |
| 2130 | `LookupIconIdFromDirectory` | `0x1FDA0` | 26 | UnwindData |  |
| 2131 | `LookupIconIdFromDirectoryEx` | `0x21720` | 123 | UnwindData |  |
| 1618 | `CreateIconFromResourceEx` | `0x21810` | 327 | UnwindData |  |
| 1598 | `CopyIcon` | `0x21A50` | 150 | UnwindData |  |
| 1619 | `CreateIconIndirect` | `0x23010` | 1,173 | UnwindData |  |
| 2108 | `LoadCursorW` | `0x24930` | 35 | UnwindData |  |
| 2270 | `ReleaseDC` | `0x25450` | 88 | UnwindData |  |
| 1806 | `GetClassInfoW` | `0x275B0` | 121 | UnwindData |  |
| 1805 | `GetClassInfoExW` | `0x27630` | 609 | UnwindData |  |
| 2241 | `RegisterClassW` | `0x278A0` | 121 | UnwindData |  |
| 2240 | `RegisterClassExW` | `0x27920` | 58 | UnwindData |  |
| 1627 | `CreateWindowExW` | `0x27960` | 139 | UnwindData |  |
| 2458 | `UnregisterClassW` | `0x28780` | 417 | UnwindData |  |
| 1626 | `CreateWindowExA` | `0x28F70` | 139 | UnwindData |  |
| 1628 | `CreateWindowInBand` | `0x29270` | 146 | UnwindData |  |
| 1629 | `CreateWindowInBandEx` | `0x29310` | 153 | UnwindData |  |
| 2457 | `UnregisterClassA` | `0x29640` | 483 | UnwindData |  |
| 2238 | `RegisterClassA` | `0x29DD0` | 121 | UnwindData |  |
| 1611 | `CreateDialogIndirectParamA` | `0x29E50` | 33 | UnwindData |  |
| 1612 | `CreateDialogIndirectParamAorW` | `0x29E80` | 113 | UnwindData |  |
| 1613 | `CreateDialogIndirectParamW` | `0x2B440` | 30 | UnwindData |  |
| 1803 | `GetClassInfoA` | `0x2BA00` | 121 | UnwindData |  |
| 1804 | `GetClassInfoExA` | `0x2BA80` | 703 | UnwindData |  |
| 2635 | *Ordinal Only* | `0x2BDF0` | 222 | UnwindData |  |
| 1749 | `EndDialog` | `0x2C410` | 406 | UnwindData |  |
| 1789 | `GetActiveWindow` | `0x2C5B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1851 | `GetFocus` | `0x2C650` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2066 | `IsChild` | `0x2C680` | 859 | UnwindData |  |
| 1906 | `GetNextDlgTabItem` | `0x2CC40` | 114 | UnwindData |  |
| 2423 | `SoftModalMessageBox` | `0x2D3A0` | 1,973 | UnwindData |  |
| 1727 | `DrawTextA` | `0x2ECF0` | 126 | UnwindData |  |
| 1728 | `DrawTextExA` | `0x2ED80` | 656 | UnwindData |  |
| 1729 | `DrawTextExW` | `0x2F020` | 38 | UnwindData |  |
| 1730 | `DrawTextW` | `0x2F050` | 222 | UnwindData |  |
| 1964 | `GetTabbedTextExtentW` | `0x31CC0` | 61 | UnwindData |  |
| 1834 | `GetDialogBaseUnits` | `0x31D10` | 28 | UnwindData |  |
| 2434 | `TabbedTextOutW` | `0x31D40` | 74 | UnwindData |  |
| 2433 | `TabbedTextOutA` | `0x31D90` | 575 | UnwindData |  |
| 1908 | `GetParent` | `0x31FE0` | 564 | UnwindData |  |
| 1513 | `AnimateWindow` | `0x32970` | 4,309 | UnwindData |  |
| 2097 | `IsWindowVisible` | `0x33AA0` | 443 | UnwindData |  |
| 2475 | `User32InitializeImmEntryTable` | `0x34740` | 250 | UnwindData |  |
| 2193 | `PostMessageW` | `0x36B70` | 173 | UnwindData |  |
| 1590 | `CloseGestureInfoHandle` | `0x37650` | 205 | UnwindData |  |
| 1591 | `CloseTouchInputHandle` | `0x37730` | 213 | UnwindData |  |
| 2192 | `PostMessageA` | `0x37AC0` | 465 | UnwindData |  |
| 2444 | `TranslateAccelerator` | `0x37CA0` | 138 | UnwindData |  |
| 2445 | `TranslateAcceleratorA` | `0x37CA0` | 138 | UnwindData |  |
| 1979 | `GetUserObjectSecurity` | `0x37EB0` | 54 | UnwindData |  |
| 2195 | `PostThreadMessageA` | `0x37EF0` | 216 | UnwindData |  |
| 2384 | `SetUserObjectSecurity` | `0x37FD0` | 44 | UnwindData |  |
| 2506 | *Ordinal Only* | `0x38010` | 514 | UnwindData |  |
| 1502 | *Ordinal Only* | `0x38340` | 388 | UnwindData |  |
| 1856 | `GetGestureInfo` | `0x385D0` | 273 | UnwindData |  |
| 2182 | `OpenWindowStationW` | `0x39230` | 70 | UnwindData |  |
| 2115 | `LoadKeyboardLayoutW` | `0x39C20` | 31 | UnwindData |  |
| 2309 | `SetClipboardData` | `0x39F30` | 642 | UnwindData |  |
| 1817 | `GetClipboardData` | `0x3B3C0` | 1,585 | UnwindData |  |
| 1565 | `CharToOemA` | `0x3C0D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2170 | `OemToCharA` | `0x3C120` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2235 | `RecordShutdownReason` | `0x3C530` | 1,311 | UnwindData |  |
| 1645 | `DdeDisconnect` | `0x3D070` | 163 | UnwindData |  |
| 1667 | `DdeUninitialize` | `0x3D120` | 480 | UnwindData |  |
| 1660 | `DdeQueryNextServer` | `0x3D780` | 328 | UnwindData |  |
| 1650 | `DdeGetData` | `0x3D8D0` | 341 | UnwindData |  |
| 1638 | `DdeClientTransaction` | `0x3DAB0` | 1,718 | UnwindData |  |
| 1658 | `DdePostAdvise` | `0x3E170` | 727 | UnwindData |  |
| 1647 | `DdeEnableCallback` | `0x3E550` | 456 | UnwindData |  |
| 1657 | `DdeNameService` | `0x3E720` | 654 | UnwindData |  |
| 1649 | `DdeFreeStringHandle` | `0x3EAB0` | 222 | UnwindData |  |
| 2527 | *Ordinal Only* | `0x3EEE0` | 37 | UnwindData |  |
| 2525 | *Ordinal Only* | `0x3EF10` | 44 | UnwindData |  |
| 1756 | `EnumDesktopWindows` | `0x3EF50` | 41 | UnwindData |  |
| 1770 | `EnumThreadWindows` | `0x3EF80` | 42 | UnwindData |  |
| 1901 | `GetMessageW` | `0x3F3E0` | 22 | UnwindData |  |
| 2362 | `SetPropA` | `0x403C0` | 431 | UnwindData |  |
| 2363 | `SetPropW` | `0x40580` | 442 | UnwindData |  |
| 1938 | `GetPropA` | `0x40740` | 317 | UnwindData |  |
| 1939 | `GetPropW` | `0x40890` | 61 | UnwindData |  |
| 2074 | `IsIconic` | `0x40C40` | 399 | UnwindData |  |
| 1903 | `GetMonitorInfoW` | `0x40DE0` | 214 | UnwindData |  |
| 1773 | `EnumWindows` | `0x41270` | 176 | UnwindData |  |
| 2319 | `SetDialogDpiChangeBehavior` | `0x41620` | 170 | UnwindData |  |
| 2534 | *Ordinal Only* | `0x416D0` | 207 | UnwindData |  |
| 2014 | `GetWindowThreadProcessId` | `0x417B0` | 273 | UnwindData |  |
| 1809 | `GetClassLongPtrW` | `0x41A00` | 1,108 | UnwindData |  |
| 2166 | `MsgWaitForMultipleObjectsEx` | `0x41E60` | 175 | UnwindData |  |
| 1807 | `GetClassLongA` | `0x41F70` | 64 | UnwindData |  |
| 1808 | `GetClassLongPtrA` | `0x41FC0` | 64 | UnwindData |  |
| 1813 | `GetClassWord` | `0x42580` | 161 | UnwindData |  |
| 1810 | `GetClassLongW` | `0x42630` | 150 | UnwindData |  |
| 1868 | `GetKeyState` | `0x429A0` | 172 | UnwindData |  |
| 2205 | `QueryDisplayConfig` | `0x42A60` | 619 | UnwindData |  |
| 1717 | `DrawEdge` | `0x451E0` | 887 | UnwindData |  |
| 2555 | *Ordinal Only* | `0x45980` | 237 | UnwindData |  |
| 1719 | `DrawFrame` | `0x45A80` | 309 | UnwindData |  |
| 1776 | `EvaluateProximityToRect` | `0x45EE0` | 304 | UnwindData |  |
| 2203 | `PtInRect` | `0x46090` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2054 | `IntersectRect` | `0x46380` | 2,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1943 | `GetRawInputDeviceInfoA` | `0x46C10` | 315 | UnwindData |  |
| 2230 | `RealGetWindowClass` | `0x46D60` | 212 | UnwindData |  |
| 2231 | `RealGetWindowClassA` | `0x46D60` | 212 | UnwindData |  |
| 1818 | `GetClipboardFormatNameA` | `0x46E40` | 172 | UnwindData |  |
| 1866 | `GetKeyNameTextA` | `0x46F00` | 184 | UnwindData |  |
| 2122 | `LoadStringA` | `0x46FC0` | 144 | UnwindData |  |
| 2490 | `WCSToMBEx` | `0x47060` | 448 | UnwindData |  |
| 2075 | `IsImmersiveProcess` | `0x47230` | 88 | UnwindData |  |
| 1940 | `GetQueueStatus` | `0x47290` | 136 | UnwindData |  |
| 1586 | `ClientToScreen` | `0x47320` | 842 | UnwindData |  |
| 1535 | `CallNextHookEx` | `0x47690` | 451 | UnwindData |  |
| 1754 | `EnumChildWindows` | `0x478C0` | 915 | UnwindData |  |
| 1988 | `GetWindowDpiAwarenessContext` | `0x47CA0` | 34 | UnwindData |  |
| 2449 | `TranslateMessageEx` | `0x47EC0` | 83 | UnwindData |  |
| 1983 | `GetWindowCompositionAttribute` | `0x47F20` | 129 | UnwindData |  |
| 2099 | `IsZoomed` | `0x48280` | 396 | UnwindData |  |
| 1839 | `GetDlgCtrlID` | `0x48420` | 358 | UnwindData |  |
| 1600 | `CopyRect` | `0x48840` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2165 | `MsgWaitForMultipleObjects` | `0x48870` | 150 | UnwindData |  |
| 1759 | `EnumDisplayDevicesA` | `0x48970` | 628 | UnwindData |  |
| 1774 | `EqualRect` | `0x48BF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2583 | `wsprintfW` | `0x48C20` | 34 | UnwindData |  |
| 2601 | `wvsprintfW` | `0x48C50` | 2,541 | UnwindData |  |
| 2174 | `OffsetRect` | `0x49A40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1507 | `AdjustWindowRect` | `0x49A70` | 101 | UnwindData |  |
| 1508 | `AdjustWindowRectEx` | `0x49AE0` | 114 | UnwindData |  |
| 2082 | `IsRectEmpty` | `0x4A1C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2580 | `wsprintfA` | `0x4A1F0` | 34 | UnwindData |  |
| 2596 | `wvsprintfA` | `0x4A220` | 2,389 | UnwindData |  |
| 2242 | `RegisterClipboardFormatA` | `0x4AC30` | 321 | UnwindData |  |
| 2267 | `RegisterWindowMessageA` | `0x4AC30` | 321 | UnwindData |  |
| 2364 | `SetRect` | `0x4B1F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2453 | `UnionRect` | `0x4B220` | 189 | UnwindData |  |
| 1812 | `GetClassNameW` | `0x4B2F0` | 51 | UnwindData |  |
| 2381 | `SetTimer` | `0x4B330` | 27 | UnwindData |  |
| 2446 | `TranslateAcceleratorW` | `0x4B360` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1838 | `GetDisplayConfigBufferSizes` | `0x4B430` | 102 | UnwindData |  |
| 1782 | `FindWindowExW` | `0x4B4A0` | 207 | UnwindData |  |
| 2296 | `SendMessageTimeoutW` | `0x4B580` | 429 | UnwindData |  |
| 2395 | `SetWindowLongW` | `0x4B880` | 267 | UnwindData |  |
| 1863 | `GetInputState` | `0x4BA00` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1697 | `DispatchMessageW` | `0x4BAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2006 | `GetWindowRgn` | `0x4BAC0` | 542 | UnwindData |  |
| 2030 | `InSendMessageEx` | `0x4BF00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2294 | `SendMessageCallbackW` | `0x4BF40` | 134 | UnwindData |  |
| 1967 | `GetThreadDpiAwarenessContext` | `0x4C000` | 146 | UnwindData |  |
| 1731 | `DwmGetDxSharedSurface` | `0x4C0A0` | 186 | UnwindData |  |
| 1574 | `CheckDBCSEnabledExt` | `0x4C1D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2199 | `PrivateExtractIconExW` | `0x4C250` | 401 | UnwindData |  |
| 2201 | `PrivateExtractIconsW` | `0x4C3F0` | 980 | UnwindData |  |
| 1764 | `EnumDisplaySettingsExW` | `0x4CAE0` | 362 | UnwindData |  |
| 2133 | `MBToWCSExt` | `0x4CC50` | 248 | UnwindData |  |
| 1925 | `GetPointerInfo` | `0x4CD50` | 76 | UnwindData |  |
| 1982 | `GetWindowBand` | `0x4CDB0` | 72 | UnwindData |  |
| 1869 | `GetKeyboardLayout` | `0x4CE00` | 93 | UnwindData |  |
| 1765 | `EnumDisplaySettingsW` | `0x4CE70` | 311 | UnwindData |  |
| 2132 | `MBToWCSEx` | `0x4CFB0` | 416 | UnwindData |  |
| 2276 | `RemovePropW` | `0x4D160` | 153 | UnwindData |  |
| 2081 | `IsProcessDPIAware` | `0x4D200` | 118 | UnwindData |  |
| 1957 | `GetSysColor` | `0x4DAF0` | 53 | UnwindData |  |
| 1783 | `FindWindowW` | `0x4DB30` | 178 | UnwindData |  |
| 1763 | `EnumDisplaySettingsExA` | `0x4DD50` | 654 | UnwindData |  |
| 2053 | `InternalGetWindowText` | `0x4E070` | 37 | UnwindData |  |
| 2560 | *Ordinal Only* | `0x4E0A0` | 307 | UnwindData |  |
| 1829 | `GetDC` | `0x4E240` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2031 | `InflateRect` | `0x4E300` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2518 | *Ordinal Only* | `0x4E330` | 63 | UnwindData |  |
| 1941 | `GetRawInputBuffer` | `0x4E7F0` | 101 | UnwindData |  |
| 2118 | `LoadMenuIndirectA` | `0x4E8A0` | 81 | UnwindData |  |
| 2119 | `LoadMenuIndirectW` | `0x4E8A0` | 81 | UnwindData |  |
| 2295 | `SendMessageTimeoutA` | `0x4EF00` | 52 | UnwindData |  |
| 2365 | `SetRectEmpty` | `0x4F1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1698 | `DisplayConfigGetDeviceInfo` | `0x4F1F0` | 34 | UnwindData |  |
| 1858 | `GetIconInfo` | `0x4F880` | 90 | UnwindData |  |
| 1542 | `ChangeDisplaySettingsA` | `0x4F8E0` | 42 | UnwindData |  |
| 1543 | `ChangeDisplaySettingsExA` | `0x4F910` | 296 | UnwindData |  |
| 1544 | `ChangeDisplaySettingsExW` | `0x4FD40` | 144 | UnwindData |  |
| 1760 | `EnumDisplayDevicesW` | `0x500E0` | 233 | UnwindData |  |
| 2009 | `GetWindowTextA` | `0x504E0` | 167 | UnwindData |  |
| 2425 | `SubtractRect` | `0x50590` | 309 | UnwindData |  |
| 1876 | `GetLastInputInfo` | `0x506D0` | 60 | UnwindData |  |
| 2029 | `InSendMessage` | `0x50720` | 70 | UnwindData |  |
| 1828 | `GetCursorPos` | `0x50C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1909 | `GetPhysicalCursorPos` | `0x50C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2243 | `RegisterClipboardFormatW` | `0x50C90` | 71 | UnwindData |  |
| 2268 | `RegisterWindowMessageW` | `0x50C90` | 71 | UnwindData |  |
| 1846 | `GetDpiForMonitorInternal` | `0x50CE0` | 74 | UnwindData |  |
| 2094 | `IsWindowInDestroy` | `0x50DA0` | 31 | UnwindData |  |
| 2092 | `IsWindowArranged` | `0x50DD0` | 54 | UnwindData |  |
| 2405 | `SetWindowsHookExA` | `0x50E10` | 23 | UnwindData |  |
| 2407 | `SetWindowsHookExW` | `0x50E30` | 20 | UnwindData |  |
| 2406 | `SetWindowsHookExAW` | `0x50E50` | 302 | UnwindData |  |
| 1875 | `GetLastActivePopup` | `0x51180` | 83 | UnwindData |  |
| 2007 | `GetWindowRgnBox` | `0x511E0` | 557 | UnwindData |  |
| 1898 | `GetMessageExtraInfo` | `0x51640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2299 | `SendNotifyMessageW` | `0x51660` | 94 | UnwindData |  |
| 2440 | `ToUnicodeEx` | `0x516D0` | 66 | UnwindData |  |
| 2123 | `LoadStringW` | `0x51780` | 29 | UnwindData |  |
| 2196 | `PostThreadMessageW` | `0x517B0` | 61 | UnwindData |  |
| 1974 | `GetUpdateRect` | `0x51800` | 109 | UnwindData |  |
| 2402 | `SetWindowTextW` | `0x51880` | 102 | UnwindData |  |
| 1900 | `GetMessageTime` | `0x518F0` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2599 | *Ordinal Only* | `0x51B90` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2084 | `IsServerSideWindow` | `0x51DA0` | 29 | UnwindData |  |
| 1955 | `GetShellWindow` | `0x51DD0` | 88 | UnwindData |  |
| 2470 | `UpdateLayeredWindow` | `0x51F60` | 102 | UnwindData |  |
| 1585 | `ClientThreadSetup` | `0x52070` | 1,098 | UnwindData |  |
| 1918 | `GetPointerFrameInfo` | `0x52510` | 68 | UnwindData |  |
| 2036 | `InitializeLpkHooks` | `0x52560` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2528 | `IsThreadMessageQueueAttached` | `0x527E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1935 | `GetProcessDpiAwarenessInternal` | `0x52800` | 106 | UnwindData |  |
| 2312 | `SetCursor` | `0x528D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2582 | *Ordinal Only* | `0x52930` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2095 | `IsWindowRedirectedForPrint` | `0x529B0` | 37 | UnwindData |  |
| 1696 | `DispatchMessageA` | `0x52C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1520 | `BeginDeferWindowPos` | `0x52C90` | 49 | UnwindData |  |
| 2232 | `RealGetWindowClassW` | `0x52CD0` | 68 | UnwindData |  |
| 2073 | `IsHungAppWindow` | `0x52D20` | 37 | UnwindData |  |
| 2452 | `UnhookWindowsHookEx` | `0x53060` | 43 | UnwindData |  |
| 2288 | `SendDlgItemMessageW` | `0x53490` | 72 | UnwindData |  |
| 2636 | *Ordinal Only* | `0x53590` | 86 | UnwindData |  |
| 2573 | *Ordinal Only* | `0x535F0` | 51 | UnwindData |  |
| 2476 | `UserClientDllInitialize` | `0x53630` | 49 | UnwindData |  |
| 1677 | `DeferWindowPos` | `0x53670` | 76 | UnwindData |  |
| 1780 | `FindWindowA` | `0x536D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2385 | `SetWinEventHook` | `0x536F0` | 233 | UnwindData |  |
| 1634 | `CtxInitUser32` | `0x537E0` | 74 | UnwindData |  |
| 2175 | `OpenClipboard` | `0x53A10` | 51 | UnwindData |  |
| 1683 | `DestroyCursor` | `0x53BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1685 | `DestroyIcon` | `0x53BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1786 | `FrameRect` | `0x53BC0` | 34 | UnwindData |  |
| 1718 | `DrawFocusRect` | `0x53BF0` | 78 | UnwindData |  |
| 1599 | `CopyImage` | `0x53E90` | 49 | UnwindData |  |
| 1594 | `ConsoleControl` | `0x53ED0` | 183 | UnwindData |  |
| 2142 | `MapVirtualKeyExA` | `0x53FD0` | 157 | UnwindData |  |
| 1977 | `GetUserObjectInformationA` | `0x54080` | 275 | UnwindData |  |
| 1919 | `GetPointerFrameInfoHistory` | `0x541A0` | 55 | UnwindData |  |
| 2471 | `UpdateLayeredWindowIndirect` | `0x54270` | 114 | UnwindData |  |
| 2072 | `IsGUIThread` | `0x542F0` | 81 | UnwindData |  |
| 1958 | `GetSysColorBrush` | `0x54350` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1975 | `GetUpdateRgn` | `0x54380` | 155 | UnwindData |  |
| 1871 | `GetKeyboardLayoutNameA` | `0x54430` | 138 | UnwindData |  |
| 1566 | `CharToOemBuffA` | `0x546F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1681 | `DestroyAcceleratorTable` | `0x54740` | 147 | UnwindData |  |
| 1572 | `CharUpperW` | `0x54A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2176 | `OpenDesktopA` | `0x54A30` | 116 | UnwindData |  |
| 2177 | `OpenDesktopW` | `0x54AB0` | 85 | UnwindData |  |
| 1559 | `CharNextA` | `0x54C40` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2510 | *Ordinal Only* | `0x55040` | 32 | UnwindData |  |
| 2171 | `OemToCharBuffA` | `0x55070` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1860 | `GetIconInfoExW` | `0x550C0` | 287 | UnwindData |  |
| 2447 | `TranslateMDISysAccel` | `0x555D0` | 204 | UnwindData |  |
| 1826 | `GetCursorFrameInfo` | `0x55890` | 72 | UnwindData |  |
| 1571 | `CharUpperBuffW` | `0x55960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2557 | *Ordinal Only* | `0x55980` | 140 | UnwindData |  |
| 2387 | `SetWindowCompositionAttribute` | `0x55A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1950 | `GetScrollInfo` | `0x55A40` | 156 | UnwindData |  |
| 2120 | `LoadMenuW` | `0x55CF0` | 59 | UnwindData |  |
| 2112 | `LoadImageW` | `0x55DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1928 | `GetPointerPenInfo` | `0x55DC0` | 76 | UnwindData |  |
| 1561 | `CharNextW` | `0x55E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1674 | `DefRawInputProc` | `0x55E40` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2143 | `MapVirtualKeyExW` | `0x56180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1899 | `GetMessagePos` | `0x561A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2110 | `LoadIconW` | `0x561C0` | 35 | UnwindData |  |
| 1558 | `CharLowerW` | `0x561F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2430 | `SystemParametersInfoA` | `0x56210` | 173 | UnwindData |  |
| 2105 | `LoadCursorA` | `0x562D0` | 97 | UnwindData |  |
| 2067 | `IsClipboardFormatAvailable` | `0x56340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2246 | `RegisterDeviceNotificationW` | `0x56360` | 68 | UnwindData |  |
| 2597 | *Ordinal Only* | `0x56480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2587 | *Ordinal Only* | `0x564A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2033 | `InitDManipHook` | `0x564C0` | 713 | UnwindData |  |
| 2344 | `SetMenuInfo` | `0x56790` | 67 | UnwindData |  |
| 2076 | `IsInDesktopWindowBand` | `0x56850` | 69 | UnwindData |  |
| 2256 | `RegisterPowerSettingNotification` | `0x56900` | 118 | UnwindData |  |
| 1930 | `GetPointerTouchInfo` | `0x56980` | 76 | UnwindData |  |
| 2569 | *Ordinal Only* | `0x56BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1747 | `EndDeferWindowPos` | `0x56C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1762 | `EnumDisplaySettingsA` | `0x56C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1582 | `ChildWindowFromPoint` | `0x56C40` | 78 | UnwindData |  |
| 2144 | `MapVirtualKeyW` | `0x56CA0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2306 | `SetClassLongPtrW` | `0x56EC0` | 263 | UnwindData |  |
| 2286 | `ScrollWindowEx` | `0x56FD0` | 100 | UnwindData |  |
| 1819 | `GetClipboardFormatNameW` | `0x57040` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2011 | `GetWindowTextLengthA` | `0x57100` | 33 | UnwindData |  |
| 1557 | `CharLowerBuffW` | `0x57270` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2245 | `RegisterDeviceNotificationA` | `0x57320` | 70 | UnwindData |  |
| 2354 | `SetProcessDPIAware` | `0x57370` | 5,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2357 | `SetProcessDpiAwarenessInternal` | `0x58760` | 87 | UnwindData |  |
| 1527 | `BroadcastSystemMessageExW` | `0x587C0` | 40 | UnwindData |  |
| 1633 | `CsrBroadcastSystemMessageExW` | `0x587F0` | 220 | UnwindData |  |
| 1528 | `BroadcastSystemMessageW` | `0x588E0` | 36 | UnwindData |  |
| 2437 | `ToAscii` | `0x58B60` | 157 | UnwindData |  |
| 2439 | `ToUnicode` | `0x58C80` | 67 | UnwindData |  |
| 2275 | `RemovePropA` | `0x58CD0` | 153 | UnwindData |  |
| 2019 | `HideCaret` | `0x58D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2398 | `SetWindowRgn` | `0x58D90` | 158 | UnwindData |  |
| 1604 | `CreateCaret` | `0x58E40` | 28 | UnwindData |  |
| 2321 | `SetDisplayConfig` | `0x58E70` | 480 | UnwindData |  |
| 1781 | `FindWindowExA` | `0x59C50` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2464 | `UnregisterPowerSettingNotification` | `0x59D20` | 65 | UnwindData |  |
| 1944 | `GetRawInputDeviceInfoW` | `0x59D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2619 | *Ordinal Only* | `0x59D90` | 44 | UnwindData |  |
| 1947 | `GetReasonTitleFromReasonCode` | `0x59DD0` | 295 | UnwindData |  |
| 1529 | `BuildReasonArray` | `0x59F00` | 418 | UnwindData |  |
| 1687 | `DestroyReasons` | `0x5A2C0` | 132 | UnwindData |  |
| 1931 | `GetPointerTouchInfoHistory` | `0x5A7A0` | 69 | UnwindData |  |
| 1792 | `GetAltTabInfoW` | `0x5A7F0` | 35 | UnwindData |  |
| 2279 | `ReplyMessage` | `0x5A940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1926 | `GetPointerInfoHistory` | `0x5A960` | 68 | UnwindData |  |
| 1874 | `GetKeyboardType` | `0x5A9B0` | 177 | UnwindData |  |
| 2418 | `ShutdownBlockReasonCreate` | `0x5AAC0` | 101 | UnwindData |  |
| 1821 | `GetClipboardSequenceNumber` | `0x5AB30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2577 | `mouse_event` | `0x5AB50` | 77 | UnwindData |  |
| 2431 | `SystemParametersInfoForDpi` | `0x5ABB0` | 183 | UnwindData |  |
| 2410 | `ShowCaret` | `0x5ADD0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2111 | `LoadImageA` | `0x5AEF0` | 328 | UnwindData |  |
| 1555 | `CharLowerA` | `0x5B040` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2269 | `ReleaseCapture` | `0x5B0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2324 | `SetDlgItemTextW` | `0x5B0D0` | 42 | UnwindData |  |
| 2374 | `SetSystemCursor` | `0x5B100` | 89 | UnwindData |  |
| 2351 | `SetParent` | `0x5B2D0` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1553 | `DwmGetDxRgn` | `0x5B5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2313 | `SetCursorContents` | `0x5B5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2482 | `VRipOutput` | `0x5B5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2483 | `VTagOutput` | `0x5B5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2493 | `WINNLSGetIMEHotkey` | `0x5B5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1554 | *Ordinal Only* | `0x5B5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2459 | `UnregisterDeviceNotification` | `0x5B5C0` | 59 | UnwindData |  |
| 1746 | `EnableWindow` | `0x5B610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2551 | `ReportInertia` | `0x5B630` | 40 | UnwindData |  |
| 2438 | `ToAsciiEx` | `0x5B660` | 278 | UnwindData |  |
| 1610 | `CreateDesktopW` | `0x5B780` | 44 | UnwindData |  |
| 1609 | `CreateDesktopExW` | `0x5B7C0` | 160 | UnwindData |  |
| 2287 | `SendDlgItemMessageA` | `0x5B940` | 72 | UnwindData |  |
| 2494 | `WaitForInputIdle` | `0x5B990` | 134 | UnwindData |  |
| 2302 | `SetCaretBlinkTime` | `0x5C070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2393 | `SetWindowLongPtrA` | `0x5C090` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2565 | *Ordinal Only* | `0x5C110` | 72 | UnwindData |  |
| 2303 | `SetCaretPos` | `0x5C160` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `CloseClipboard` | `0x5C530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2401 | `SetWindowTextA` | `0x5C550` | 40 | UnwindData |  |
| 2285 | `ScrollWindow` | `0x5D150` | 83 | UnwindData |  |
| 1744 | `EnableScrollBar` | `0x5D1B0` | 158 | UnwindData |  |
| 2015 | `GetWindowWord` | `0x5D2D0` | 76 | UnwindData |  |
| 2713 | *Ordinal Only* | `0x5D330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1820 | `GetClipboardOwner` | `0x5D350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2472 | `UpdatePerUserSystemParameters` | `0x5D370` | 359 | UnwindData |  |
| 2173 | `OemToCharW` | `0x5D810` | 84 | UnwindData |  |
| 1755 | `EnumClipboardFormats` | `0x5D870` | 41 | UnwindData |  |
| 2102 | `LoadAcceleratorsW` | `0x5D950` | 47 | UnwindData |  |
| 1929 | `GetPointerPenInfoHistory` | `0x5E070` | 69 | UnwindData |  |
| 2141 | `MapVirtualKeyA` | `0x5E0C0` | 111 | UnwindData |  |
| 2172 | `OemToCharBuffW` | `0x5E280` | 74 | UnwindData |  |
| 2139 | `MapDialogRect` | `0x5E2D0` | 186 | UnwindData |  |
| 2252 | `RegisterMessagePumpHook` | `0x5E390` | 286 | UnwindData |  |
| 2298 | `SendNotifyMessageA` | `0x5ECD0` | 97 | UnwindData |  |
| 1758 | `EnumDesktopsW` | `0x5EE80` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2057 | `InvertRect` | `0x5F040` | 53 | UnwindData |  |
| 2377 | `SetThreadDesktop` | `0x5F080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1872 | `GetKeyboardLayoutNameW` | `0x5F0A0` | 50 | UnwindData |  |
| 2488 | `VkKeyScanExW` | `0x5F0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1523 | `BringWindowToTop` | `0x5F100` | 48 | UnwindData |  |
| 1623 | `CreatePopupMenu` | `0x5F2A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2382 | `SetUserObjectInformationA` | `0x5F320` | 114 | UnwindData |  |
| 2002 | *Ordinal Only* | `0x5F3A0` | 163 | UnwindData |  |
| 1954 | `GetShellChangeNotifyWindow` | `0x5F450` | 70 | UnwindData |  |
| 1843 | `GetDlgItemTextW` | `0x5F510` | 65 | UnwindData |  |
| 2379 | `SetThreadDpiHostingBehavior` | `0x5F560` | 129 | UnwindData |  |
| 1548 | `ChangeWindowMessageFilter` | `0x5F5F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2486 | `VkKeyScanA` | `0x5F610` | 102 | UnwindData |  |
| 1632 | `CreateWindowStationW` | `0x5F680` | 85 | UnwindData |  |
| 2329 | `SetForegroundWindow` | `0x5FAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2485 | `ValidateRgn` | `0x5FAC0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `AllowSetForegroundWindow` | `0x5FCC0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2337 | `SetMagnificationDesktopMagnification` | `0x5FDA0` | 110 | UnwindData |  |
| 1601 | `CountClipboardFormats` | `0x5FE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2158 | `MessageBoxW` | `0x5FE40` | 75 | UnwindData |  |
| 2157 | `MessageBoxTimeoutW` | `0x5FEA0` | 447 | UnwindData |  |
| 2154 | `MessageBoxIndirectA` | `0x60070` | 523 | UnwindData |  |
| 2266 | `RegisterUserApiHook` | `0x60750` | 259 | UnwindData |  |
| 2284 | `ScrollDC` | `0x60860` | 87 | UnwindData |  |
| 2261 | `RegisterSuspendResumeNotification` | `0x60D40` | 110 | UnwindData |  |
| 1615 | `CreateDialogParamW` | `0x60E30` | 141 | UnwindData |  |
| 2581 | *Ordinal Only* | `0x60ED0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2194 | `PostQuitMessage` | `0x61030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1682 | `DestroyCaret` | `0x61050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2461 | `UnregisterMessagePumpHook` | `0x61070` | 201 | UnwindData |  |
| 1867 | `GetKeyNameTextW` | `0x61140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1556 | `CharLowerBuffA` | `0x61160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2109 | `LoadIconA` | `0x61180` | 97 | UnwindData |  |
| 1569 | `CharUpperA` | `0x61310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2083 | `IsSETEnabled` | `0x61330` | 209 | UnwindData |  |
| 1639 | `DdeCmpStringHandles` | `0x61660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1989 | `GetWindowDpiHostingBehavior` | `0x61680` | 97 | UnwindData |  |
| 2101 | `LoadAcceleratorsA` | `0x61B40` | 47 | UnwindData |  |
| 2251 | `RegisterLogonProcess` | `0x61B80` | 28 | UnwindData |  |
| 2305 | `SetClassLongPtrA` | `0x61BB0` | 263 | UnwindData |  |
| 2060 | `IsCharAlphaNumericW` | `0x61FA0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1768 | `EnumPropsExW` | `0x620F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1560 | `CharNextExA` | `0x62110` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `CreateWindowIndirect` | `0x62310` | 155 | UnwindData |  |
| 1504 | `ActivateKeyboardLayout` | `0x62900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `DdeCreateStringHandleW` | `0x62920` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2620 | *Ordinal Only* | `0x629F0` | 54 | UnwindData |  |
| 1622 | `CreateMenu` | `0x63230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1692 | `DialogBoxIndirectParamW` | `0x63250` | 30 | UnwindData |  |
| 1691 | `DialogBoxIndirectParamAorW` | `0x63280` | 110 | UnwindData |  |
| 2001 | *Ordinal Only* | `0x63300` | 146 | UnwindData |  |
| 2427 | `SwitchDesktop` | `0x633F0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2202 | `PrivateRegisterICSProc` | `0x635A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2466 | `UnregisterSuspendResumeNotification` | `0x635D0` | 65 | UnwindData |  |
| 1784 | `FlashWindow` | `0x63650` | 67 | UnwindData |  |
| 1596 | `CopyAcceleratorTableA` | `0x63810` | 138 | UnwindData |  |
| 2400 | `SetWindowStationUser` | `0x639F0` | 72 | UnwindData |  |
| 2239 | `RegisterClassExA` | `0x64720` | 58 | UnwindData |  |
| 1564 | `CharPrevW` | `0x647C0` | 1,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2339 | `SetMagnificationDesktopSamplingMode` | `0x64F40` | 62 | UnwindData |  |
| 1562 | `CharPrevA` | `0x64F90` | 2,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2071 | `IsDlgButtonChecked` | `0x659C0` | 43 | UnwindData |  |
| 2323 | `SetDlgItemTextA` | `0x65A80` | 42 | UnwindData |  |
| 1570 | `CharUpperBuffA` | `0x65AB0` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `EmptyClipboard` | `0x65D90` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2184 | `PackTouchHitTestingProximityEvaluation` | `0x65E40` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1575 | `CheckDlgButton` | `0x65FF0` | 52 | UnwindData |  |
| 2489 | `VkKeyScanW` | `0x66030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1972 | `GetTouchInputInfo` | `0x66050` | 47 | UnwindData |  |
| 1921 | `GetPointerFramePenInfoHistory` | `0x66090` | 57 | UnwindData |  |
| 2480 | `UserRealizePalette` | `0x660D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2121 | `LoadRemoteFonts` | `0x660F0` | 42 | UnwindData |  |
| 2700 | *Ordinal Only* | `0x66120` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2063 | `IsCharLowerW` | `0x66150` | 3,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1923 | `GetPointerFrameTouchInfo` | `0x66FA0` | 66 | UnwindData |  |
| 2061 | `IsCharAlphaW` | `0x67190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2535 | *Ordinal Only* | `0x671B0` | 89 | UnwindData |  |
| 1772 | `EnumWindowStationsW` | `0x672C0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `AddClipboardFormatListener` | `0x673B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1620 | `CreateMDIWindowA` | `0x673D0` | 110 | UnwindData |  |
| 2515 | *Ordinal Only* | `0x67770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2260 | `RegisterShellHookWindow` | `0x67790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2429 | `SwitchToThisWindow` | `0x677B0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2183 | `PackDDElParam` | `0x67950` | 107 | UnwindData |  |
| 2052 | `InternalGetWindowIcon` | `0x67A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2562 | `keybd_event` | `0x67A70` | 85 | UnwindData |  |
| 2059 | `IsCharAlphaNumericA` | `0x67C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1965 | `GetTaskmanWindow` | `0x67C70` | 88 | UnwindData |  |
| 2372 | `SetSysColors` | `0x67CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2124 | `LockSetForegroundWindow` | `0x67CF0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2265 | `RegisterTouchWindow` | `0x67FA0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2281 | `ReuseDDElParam` | `0x68080` | 161 | UnwindData |  |
| 2428 | `SwitchDesktopWithFade` | `0x68130` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2341 | `SetMenu` | `0x681F0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1999 | `GetWindowModuleFileNameW` | `0x68270` | 62 | UnwindData |  |
| 2150 | `MessageBeep` | `0x682C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1694 | `DialogBoxParamW` | `0x682E0` | 142 | UnwindData |  |
| 1655 | `DdeInitializeW` | `0x68380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2561 | *Ordinal Only* | `0x683A0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1787 | `FreeDDElParam` | `0x686F0` | 102 | UnwindData |  |
| 2272 | `RemoveClipboardFormatListener` | `0x687C0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1614 | `CreateDialogParamA` | `0x68A40` | 143 | UnwindData |  |
| 1580 | `CheckRadioButton` | `0x68F30` | 137 | UnwindData |  |
| 2058 | `IsCharAlphaA` | `0x68FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2568 | *Ordinal Only* | `0x68FE0` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2383 | `SetUserObjectInformationW` | `0x69410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2442 | `TrackPopupMenu` | `0x69420` | 38 | UnwindData |  |
| 2600 | *Ordinal Only* | `0x69450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2567 | *Ordinal Only* | `0x69470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1563 | `CharPrevExA` | `0x69490` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1680 | `DeregisterShellHookWindow` | `0x696D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `CreateMDIWindowW` | `0x696F0` | 110 | UnwindData |  |
| 1725 | `DrawStateA` | `0x697E0` | 430 | UnwindData |  |
| 1841 | `GetDlgItemInt` | `0x699A0` | 375 | UnwindData |  |
| 1924 | `GetPointerFrameTouchInfoHistory` | `0x69EE0` | 57 | UnwindData |  |
| 2412 | `ShowOwnedPopups` | `0x69F20` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1933 | `GetPriorityClipboardFormat` | `0x6A060` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1699 | `DisplayConfigSetDeviceInfo` | `0x6A230` | 34 | UnwindData |  |
| 1920 | `GetPointerFramePenInfo` | `0x6A260` | 66 | UnwindData |  |
| 2498 | `WinHelpW` | `0x6A2B0` | 834 | UnwindData |  |
| 1700 | `DisplayExitWindowsWarnings` | `0x6A600` | 725 | UnwindData |  |
| 1723 | `DrawMenuBar` | `0x6A8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2107 | `LoadCursorFromFileW` | `0x6A900` | 79 | UnwindData |  |
| 2310 | `SetClipboardViewer` | `0x6AB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2116 | `LoadLocalFonts` | `0x6AB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1541 | `ChangeClipboardChain` | `0x6ABB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2065 | `IsCharUpperW` | `0x6ABD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2355 | `SetProcessDefaultLayout` | `0x6ABF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1907 | `GetOpenClipboardWindow` | `0x6AC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2467 | `UnregisterTouchWindow` | `0x6AC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2392 | `SetWindowLongA` | `0x6AC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2376 | `SetTaskmanWindow` | `0x6AC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2135 | `MITGetCursorUpdateHandle` | `0x6AC90` | 1,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `DdeCreateDataHandle` | `0x6B410` | 342 | UnwindData |  |
| 2564 | *Ordinal Only* | `0x6B6F0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2370 | `SetShellWindow` | `0x6B7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1822 | `GetClipboardViewer` | `0x6B810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1976 | `GetUpdatedClipboardFormats` | `0x6B830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2369 | `SetShellChangeNotifyWindow` | `0x6B850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2249 | `RegisterGhostWindow` | `0x6B870` | 1,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2136 | `MITSetLastInputRecipient` | `0x6BDE0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2456 | `UnpackDDElParam` | `0x6C1B0` | 178 | UnwindData |  |
| 1736 | `DwmLockScreenUpdates` | `0x6C2E0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1693 | `DialogBoxParamA` | `0x6C470` | 145 | UnwindData |  |
| 1953 | `GetSendMessageReceiver` | `0x6C510` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2037 | `InitializePointerDeviceInjection` | `0x6C910` | 63 | UnwindData |  |
| 2618 | *Ordinal Only* | `0x6C960` | 44 | UnwindData |  |
| 1778 | `ExitWindowsEx` | `0x6D2A0` | 285 | UnwindData |  |
| 1796 | `GetAsyncKeyState` | `0x6E3C0` | 316 | UnwindData |  |
| 1949 | `GetScrollBarInfo` | `0x6ECC0` | 601 | UnwindData |  |
| 1661 | `DdeQueryStringA` | `0x70160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1745 | `EnableSessionForMMCSS` | `0x70180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1695 | `DisableProcessWindowsGhosting` | `0x701A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2307 | `SetClassLongW` | `0x701C0` | 2,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1766 | `EnumPropsA` | `0x70A80` | 1,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1757 | `EnumDesktopsA` | `0x710E0` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1934 | `GetProcessDefaultLayout` | `0x71B90` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2426 | `SwapMouseButton` | `0x72440` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2153 | `MessageBoxExW` | `0x724B0` | 30 | UnwindData |  |
| 1567 | `CharToOemBuffW` | `0x72580` | 88 | UnwindData |  |
| 2064 | `IsCharUpperA` | `0x725E0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2348 | `SetMessageExtraInfo` | `0x72700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2062 | `IsCharLowerA` | `0x72720` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2509 | *Ordinal Only* | `0x72AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2588 | *Ordinal Only* | `0x72AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1506 | `AddVisualIdentifier` | `0x72AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2681 | `ApplyWindowAction` | `0x72AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `AttachThreadInput` | `0x72B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2616 | *Ordinal Only* | `0x72B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1521 | `BeginPaint` | `0x72B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `BlockInput` | `0x72B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2708 | *Ordinal Only* | `0x72B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1530 | `CalcMenuBar` | `0x72B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `CalculatePopupWindowPosition` | `0x72B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2533 | *Ordinal Only* | `0x72B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1549 | `ChangeWindowMessageFilterEx` | `0x72B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `CheckProcessForClipboardAccess` | `0x72B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1579 | `CheckProcessSession` | `0x72BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `CheckWindowThreadDesktop` | `0x72BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1583 | `ChildWindowFromPointEx` | `0x72BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2563 | *Ordinal Only* | `0x72BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1587 | `ClipCursor` | `0x72BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1589 | `CloseDesktop` | `0x72BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `CloseWindowStation` | `0x72C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2550 | *Ordinal Only* | `0x72C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2610 | *Ordinal Only* | `0x72C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2647 | *Ordinal Only* | `0x72C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2638 | *Ordinal Only* | `0x72C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2621 | *Ordinal Only* | `0x72C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `ControlMagnification` | `0x72C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2675 | `ConvertToInterceptWindow` | `0x72C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1597 | `CopyAcceleratorTableW` | `0x72C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1603 | `CreateAcceleratorTableW` | `0x72C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2633 | *Ordinal Only* | `0x72CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1606 | `CreateDCompositionHwndTarget` | `0x72CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2644 | *Ordinal Only* | `0x72CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2516 | *Ordinal Only* | `0x72CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2503 | `DelegateInput` | `0x72CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1679 | `DeleteMenu` | `0x72CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2648 | *Ordinal Only* | `0x72D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1684 | `DestroyDCompositionHwndTarget` | `0x72D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `DestroyMenu` | `0x72D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1688 | `DestroySyntheticPointerDevice` | `0x72D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2273 | `RemoveInjectionDevice` | `0x72D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1689 | `DestroyWindow` | `0x72D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2529 | *Ordinal Only* | `0x72D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1709 | `DoSoundConnect` | `0x72D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1710 | `DoSoundDisconnect` | `0x72D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2651 | *Ordinal Only* | `0x72D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1711 | `DragDetect` | `0x72D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1712 | `DragObject` | `0x72DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2613 | *Ordinal Only* | `0x72DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2670 | *Ordinal Only* | `0x72DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1713 | `DrawAnimatedRects` | `0x72DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1732 | `DwmGetRemoteSessionOcclusionEvent` | `0x72DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1733 | `DwmGetRemoteSessionOcclusionState` | `0x72DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1734 | `DwmKernelShutdown` | `0x72E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1735 | `DwmKernelStartup` | `0x72E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `DwmValidateWindow` | `0x72E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2680 | `DwmWindowNotificationsEnabled` | `0x72E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2704 | *Ordinal Only* | `0x72E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1741 | `EnableMouseInPointer` | `0x72E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2656 | *Ordinal Only* | `0x72E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2519 | *Ordinal Only* | `0x72E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1742 | `EnableNonClientDpiScaling` | `0x72E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1743 | `EnableOneCoreTransformMode` | `0x72E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2615 | *Ordinal Only* | `0x72EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2606 | *Ordinal Only* | `0x72EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2544 | *Ordinal Only* | `0x72EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2709 | *Ordinal Only* | `0x72ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2611 | *Ordinal Only* | `0x72EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2804 | `EnableWindowShellWindowManagementBehavior` | `0x72EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1748 | `EndDeferWindowPosEx` | `0x72F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1750 | `EndMenu` | `0x72F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1751 | `EndPaint` | `0x72F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2686 | `EnterMoveSizeLoop` | `0x72F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1761 | `EnumDisplayMonitors` | `0x72F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1777 | `ExcludeUpdateRgn` | `0x72F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1785 | `FlashWindowEx` | `0x72F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2642 | *Ordinal Only* | `0x72F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1788 | `FrostCrashedWindow` | `0x72F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2711 | *Ordinal Only* | `0x72F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1793 | `GetAncestor` | `0x72FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1797 | `GetAutoRotationState` | `0x72FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1799 | `GetCIMSSM` | `0x72FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1801 | `GetCaretBlinkTime` | `0x72FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1802 | `GetCaretPos` | `0x72FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1815 | `GetClipCursor` | `0x72FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1816 | `GetClipboardAccessToken` | `0x73000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2668 | `GetClipboardMetadata` | `0x73010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1823 | `GetComboBoxInfo` | `0x73020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1824 | `GetCurrentInputMessageSource` | `0x73030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1825 | `GetCursor` | `0x73040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1827 | `GetCursorInfo` | `0x73050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1830 | `GetDCEx` | `0x73060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1831 | `GetDCompositionHwndBitmap` | `0x73070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1832 | `GetDesktopID` | `0x73080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1837 | `GetDisplayAutoRotationPreferences` | `0x73090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2512 | *Ordinal Only* | `0x730A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1844 | `GetDoubleClickTime` | `0x730B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1850 | `GetExtendedPointerDeviceProperty` | `0x730C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1853 | `GetGUIThreadInfo` | `0x730D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1854 | `GetGestureConfig` | `0x730E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1857 | `GetGuiResources` | `0x730F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2650 | *Ordinal Only* | `0x73100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1862 | `GetInputLocaleInfo` | `0x73110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2590 | *Ordinal Only* | `0x73120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2589 | *Ordinal Only* | `0x73130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2609 | *Ordinal Only* | `0x73140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1870 | `GetKeyboardLayoutList` | `0x73150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1873 | `GetKeyboardState` | `0x73160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1877 | `GetLayeredWindowAttributes` | `0x73170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1878 | `GetListBoxInfo` | `0x73180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1882 | `GetMagnificationLensCtxInformation` | `0x73190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1884 | `GetMenuBarInfo` | `0x731A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1893 | `GetMenuItemRect` | `0x731B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1904 | `GetMouseMovePointsEx` | `0x731C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2559 | *Ordinal Only* | `0x731D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2545 | *Ordinal Only* | `0x731E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1910 | `GetPointerCursorId` | `0x731F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1911 | `GetPointerDevice` | `0x73200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1912 | `GetPointerDeviceCursors` | `0x73210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1913 | `GetPointerDeviceInputSpace` | `0x73220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1914 | `GetPointerDeviceOrientation` | `0x73230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1915 | `GetPointerDeviceProperties` | `0x73240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1916 | `GetPointerDeviceRects` | `0x73250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1917 | `GetPointerDevices` | `0x73260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1922 | `GetPointerFrameTimes` | `0x73270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1927 | `GetPointerInputTransform` | `0x73280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2653 | *Ordinal Only* | `0x73290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1932 | `GetPointerType` | `0x732A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2521 | `GetProcessUIContextInformation` | `0x732B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1936 | `GetProcessWindowStation` | `0x732C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2541 | *Ordinal Only* | `0x732D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1942 | `GetRawInputData` | `0x732E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1945 | `GetRawInputDeviceList` | `0x732F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1946 | `GetRawPointerDeviceData` | `0x73300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1948 | `GetRegisteredRawInputDevices` | `0x73310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2614 | *Ordinal Only* | `0x73320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1959 | `GetSystemDpiForProcess` | `0x73330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1960 | `GetSystemMenu` | `0x73340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1966 | `GetThreadDesktop` | `0x73350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1969 | `GetTitleBarInfo` | `0x73360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1970 | `GetTopLevelWindow` | `0x73370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2517 | *Ordinal Only* | `0x73380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2652 | *Ordinal Only* | `0x73390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1978 | `GetUserObjectInformationW` | `0x733A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1984 | `GetWindowCompositionInfo` | `0x733B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1986 | `GetWindowDC` | `0x733C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1987 | `GetWindowDisplayAffinity` | `0x733D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1990 | `GetWindowFeedbackSetting` | `0x733E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1996 | `GetWindowMinimizeRect` | `0x733F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2000 | `GetWindowPlacement` | `0x73400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2008 | `GetWindowRgnEx` | `0x73410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2016 | `GhostWindowFromHungWindow` | `0x73420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2505 | `HandleDelegatedInput` | `0x73430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2539 | *Ordinal Only* | `0x73440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2020 | `HiliteMenuItem` | `0x73450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2021 | `HungWindowFromGhostWindow` | `0x73460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2028 | `ImpersonateDdeClientWindow` | `0x73470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2032 | `InheritWindowMonitor` | `0x73480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2612 | *Ordinal Only* | `0x73490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2669 | *Ordinal Only* | `0x734A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2034 | `InitializeGenericHidInjection` | `0x734B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2035 | `InitializeInputDeviceInjection` | `0x734C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2039 | `InitializeTouchInjection` | `0x734D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2040 | `InjectDeviceInput` | `0x734E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2041 | `InjectGenericHidInput` | `0x734F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2042 | `InjectKeyboardInput` | `0x73500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2043 | `InjectMouseInput` | `0x73510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2044 | `InjectPointerInput` | `0x73520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2045 | `InjectSyntheticPointerInput` | `0x73520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2046 | `InjectTouchInput` | `0x73530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2803 | *Ordinal Only* | `0x73540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2047 | `InputSpaceRegionFromPoint` | `0x73550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2593 | *Ordinal Only* | `0x73560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2055 | `InvalidateRect` | `0x73570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2056 | `InvalidateRgn` | `0x73580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2705 | *Ordinal Only* | `0x73590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2676 | `IsInterceptWindow` | `0x735A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2078 | `IsMouseInPointerEnabled` | `0x735B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2520 | *Ordinal Only* | `0x735C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2703 | *Ordinal Only* | `0x735D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2080 | `IsOneCoreTransformMode` | `0x735E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2617 | *Ordinal Only* | `0x735F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2087 | `IsTopLevelWindow` | `0x73600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2088 | `IsTouchWindow` | `0x73610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2706 | *Ordinal Only* | `0x73620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2685 | `IsWindowDisplayChangeSuppressed` | `0x73630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2710 | *Ordinal Only* | `0x73640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2100 | `KillTimer` | `0x73650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2538 | *Ordinal Only* | `0x73660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2125 | `LockWindowStation` | `0x73670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2126 | `LockWindowUpdate` | `0x73680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2127 | `LockWorkStation` | `0x73690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2715 | *Ordinal Only* | `0x736A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2128 | `LogicalToPhysicalPoint` | `0x736B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2129 | `LogicalToPhysicalPointForPerMonitorDPI` | `0x736C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2140 | `MapPointsByVisualIdentifier` | `0x736D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2145 | `MapVisualRelativePoints` | `0x736E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2147 | `MenuItemFromPoint` | `0x736F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2164 | `MoveWindow` | `0x73700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2578 | *Ordinal Only* | `0x73710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2179 | `OpenInputDesktop` | `0x73720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2180 | `OpenThreadDesktop` | `0x73730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2186 | `PaintMenuBar` | `0x73740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2187 | `PaintMonitor` | `0x73750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2716 | *Ordinal Only* | `0x73760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2190 | `PhysicalToLogicalPoint` | `0x73770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2191 | `PhysicalToLogicalPointForPerMonitorDPI` | `0x73780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2197 | `PrintWindow` | `0x73790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2608 | *Ordinal Only* | `0x737A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2508 | *Ordinal Only* | `0x737B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2204 | `QueryBSDRWindow` | `0x737C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2206 | `QuerySendMessage` | `0x737D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2207 | `RIMAddInputObserver` | `0x737E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2208 | `RIMAreSiblingDevices` | `0x737F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2209 | `RIMDeviceIoControl` | `0x73800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2210 | `RIMEnableMonitorMappingForDevice` | `0x73810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2211 | `RIMFreeInputBuffer` | `0x73820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2212 | `RIMGetDevicePreparsedData` | `0x73830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2213 | `RIMGetDevicePreparsedDataLockfree` | `0x73840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2214 | `RIMGetDeviceProperties` | `0x73850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2215 | `RIMGetDevicePropertiesLockfree` | `0x73860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2216 | `RIMGetPhysicalDeviceRect` | `0x73870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2217 | `RIMGetSourceProcessId` | `0x73880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2218 | `RIMObserveNextInput` | `0x73890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2663 | `RIMOnAsyncPnpWorkNotification` | `0x738A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2219 | `RIMOnPnpNotification` | `0x738B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2220 | `RIMOnTimerNotification` | `0x738C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2221 | `RIMQueryDevicePath` | `0x738D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2222 | `RIMReadInput` | `0x738E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2662 | `RIMRegisterForInputEx` | `0x738F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2224 | `RIMRemoveInputObserver` | `0x73900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2225 | `RIMSetExtendedDeviceProperty` | `0x73910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2226 | `RIMSetTestModeStatus` | `0x73920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2227 | `RIMUnregisterForInput` | `0x73930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2228 | `RIMUpdateInputObserverRegistration` | `0x73940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2687 | `RaiseLowerShellWindow` | `0x73950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2229 | `RealChildWindowFromPoint` | `0x73960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2236 | `RedrawWindow` | `0x73970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2237 | `RegisterBSDRWindow` | `0x73980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2682 | `RegisterCloakedNotification` | `0x73990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2244 | `RegisterDManipHook` | `0x739A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2247 | `RegisterErrorReportingDialog` | `0x739B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2667 | `RegisterForCustomDockTargets` | `0x739C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2666 | `RegisterForTooltipDismissNotification` | `0x739D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2250 | `RegisterHotKey` | `0x739E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2253 | `RegisterPointerDeviceNotifications` | `0x739F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2257 | `RegisterRawInputDevices` | `0x73A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2258 | `RegisterServicesProcess` | `0x73A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2259 | `RegisterSessionPort` | `0x73A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2263 | `RegisterTasklist` | `0x73A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2264 | `RegisterTouchHitTestingWindow` | `0x73A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2546 | *Ordinal Only* | `0x73A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2689 | `RegisterTouchpadCapableWindow` | `0x73A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2271 | `ReleaseDwmHitTestWaiters` | `0x73A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2274 | `RemoveMenu` | `0x73A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2278 | `RemoveVisualIdentifier` | `0x73A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2280 | `ResolveDesktopForWOW` | `0x73AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2643 | *Ordinal Only* | `0x73AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2537 | *Ordinal Only* | `0x73AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2291 | `SendInput` | `0x73AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2591 | *Ordinal Only* | `0x73AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2556 | *Ordinal Only* | `0x73AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2513 | *Ordinal Only* | `0x73B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2300 | `SetActiveWindow` | `0x73B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2665 | `SetAdditionalForegroundBoostProcesses` | `0x73B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2805 | *Ordinal Only* | `0x73B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2507 | *Ordinal Only* | `0x73B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2627 | *Ordinal Only* | `0x73B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2522 | *Ordinal Only* | `0x73B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2531 | *Ordinal Only* | `0x73B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2301 | `SetCapture` | `0x73B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2005 | *Ordinal Only* | `0x73B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2308 | `SetClassWord` | `0x73BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2311 | `SetCoalescableTimer` | `0x73BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2571 | `SetCoreWindow` | `0x73BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2576 | *Ordinal Only* | `0x73BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2542 | `SetCoveredWindowStates` | `0x73BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2639 | *Ordinal Only* | `0x73BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2314 | `SetCursorPos` | `0x73C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2352 | `SetPhysicalCursorPos` | `0x73C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2317 | `SetDesktopColorTransform` | `0x73C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2658 | *Ordinal Only* | `0x73C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2318 | `SetDialogControlDpiChangeBehavior` | `0x73C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2320 | `SetDisplayAutoRotationPreferences` | `0x73C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2532 | *Ordinal Only* | `0x73C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2661 | *Ordinal Only* | `0x73C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2326 | `SetFeatureReportResponse` | `0x73C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2327 | `SetFocus` | `0x73C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2328 | `SetForegroundRedirectionForActivationObject` | `0x73C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2649 | *Ordinal Only* | `0x73CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2330 | `SetFullscreenMagnifierOffsetsDWMUpdated` | `0x73CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2331 | `SetGestureConfig` | `0x73CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2586 | *Ordinal Only* | `0x73CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2592 | *Ordinal Only* | `0x73CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2594 | *Ordinal Only* | `0x73CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2332 | `SetInternalWindowPos` | `0x73D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2333 | `SetKeyboardState` | `0x73D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2335 | `SetLayeredWindowAttributes` | `0x73D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2338 | `SetMagnificationDesktopMagnifierOffsetsDWMUpdated` | `0x73D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2340 | `SetMagnificationLensCtxInformation` | `0x73D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2342 | `SetMenuContextHelpId` | `0x73D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2343 | `SetMenuDefaultItem` | `0x73D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2350 | `SetMirrorRendering` | `0x73D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2353 | `SetPointerDeviceInputSpace` | `0x73D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2595 | *Ordinal Only* | `0x73D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2358 | `SetProcessLaunchForegroundPolicy` | `0x73DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2657 | *Ordinal Only* | `0x73DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2359 | `SetProcessRestrictionExemption` | `0x73DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2360 | `SetProcessWindowStation` | `0x73DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2637 | *Ordinal Only* | `0x73DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2371 | `SetShellWindowEx` | `0x73DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2375 | `SetSystemMenu` | `0x73E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2622 | *Ordinal Only* | `0x73E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2380 | `SetThreadInputBlocked` | `0x73E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2672 | `SetUserObjectCapability` | `0x73E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2386 | `SetWindowBand` | `0x73E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2388 | `SetWindowCompositionTransition` | `0x73E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2390 | `SetWindowDisplayAffinity` | `0x73E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2391 | `SetWindowFeedbackSetting` | `0x73E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2673 | `SetWindowMessageCapability` | `0x73E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2396 | `SetWindowPlacement` | `0x73E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2397 | `SetWindowPos` | `0x73EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2579 | *Ordinal Only* | `0x73EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2403 | `SetWindowWord` | `0x73EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2674 | `ShellForegroundBoostProcess` | `0x73ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2800 | `ShellHandwritingDelegateInput` | `0x73EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2802 | `ShellHandwritingHandleDelegatedInput` | `0x73EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2801 | `ShellHandwritingUndelegateInput` | `0x73F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2664 | `ShellMigrateWindow` | `0x73F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2671 | `ShellRegisterHotKey` | `0x73F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2409 | `ShellSetWindowPos` | `0x73F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2411 | `ShowCursor` | `0x73F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2415 | `ShowSystemCursor` | `0x73F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2416 | `ShowWindow` | `0x73F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2417 | `ShowWindowAsync` | `0x73F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2419 | `ShutdownBlockReasonDestroy` | `0x73F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2420 | `ShutdownBlockReasonQuery` | `0x73F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2421 | `SignalRedirectionStartComplete` | `0x73FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2422 | `SkipPointerFrameMessages` | `0x73FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2010 | *Ordinal Only* | `0x73FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2424 | `SoundSentry` | `0x73FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2684 | `SuppressWindowDisplayChange` | `0x73FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2441 | `TrackMouseEvent` | `0x73FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2443 | `TrackPopupMenuEx` | `0x74000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2504 | `UndelegateInput` | `0x74010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2450 | `UnhookWinEvent` | `0x74020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2455 | `UnlockWindowStation` | `0x74030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2460 | `UnregisterHotKey` | `0x74040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2465 | `UnregisterSessionPort` | `0x74050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2468 | `UnregisterUserApiHook` | `0x74060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2469 | `UpdateDefaultDesktopThumbnail` | `0x74070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2474 | `UpdateWindowInputSinkHints` | `0x74080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2585 | *Ordinal Only* | `0x74090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2477 | `UserHandleGrantAccess` | `0x740A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2484 | `ValidateRect` | `0x740B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2530 | *Ordinal Only* | `0x740C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2495 | `WaitForRedirectionStartComplete` | `0x740D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2496 | `WaitMessage` | `0x740E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2499 | `WindowFromDC` | `0x740F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2500 | `WindowFromPhysicalPoint` | `0x74100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2501 | `WindowFromPoint` | `0x74110` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1584 | `CliImmSetHotKey` | `0x74C70` | 152 | UnwindData |  |
| 2106 | `LoadCursorFromFileA` | `0x75330` | 126 | UnwindData |  |
| 2714 | *Ordinal Only* | `0x75490` | 43 | UnwindData |  |
| 1767 | `EnumPropsExA` | `0x76040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1769 | `EnumPropsW` | `0x76060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1771 | `EnumWindowStationsA` | `0x76080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2526 | *Ordinal Only* | `0x760A0` | 39 | UnwindData |  |
| 2524 | *Ordinal Only* | `0x760D0` | 39 | UnwindData |  |
| 1855 | `GetGestureExtraArgs` | `0x76100` | 29 | UnwindData |  |
| 2404 | `SetWindowsHookA` | `0x76130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2408 | `SetWindowsHookW` | `0x76150` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2117 | `LoadMenuA` | `0x76590` | 59 | UnwindData |  |
| 1573 | `CheckBannedOneCoreTransformApi` | `0x765E0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2315 | `SetDebugErrorLevel` | `0x765E0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2659 | *Ordinal Only* | `0x765E0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2815 | *Ordinal Only* | `0x76960` | 114 | UnwindData |  |
| 2098 | `IsWow64Message` | `0x769E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2148 | `MenuWindowProcA` | `0x76A00` | 118 | UnwindData |  |
| 2149 | `MenuWindowProcW` | `0x76A80` | 115 | UnwindData |  |
| 1503 | `GetPointerFrameArrivalTimes` | `0x76C40` | 29 | UnwindData |  |
| 2255 | `RegisterPointerInputTargetEx` | `0x76C40` | 29 | UnwindData |  |
| 2463 | `UnregisterPointerInputTargetEx` | `0x76C40` | 29 | UnwindData |  |
| 2548 | *Ordinal Only* | `0x76C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2549 | *Ordinal Only* | `0x76C90` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2693 | `GetPointerFrameTouchpadInfo` | `0x76CF0` | 128 | UnwindData |  |
| 2694 | `GetPointerFrameTouchpadInfoHistory` | `0x76D80` | 131 | UnwindData |  |
| 2691 | `GetPointerTouchpadInfo` | `0x76E10` | 125 | UnwindData |  |
| 2692 | `GetPointerTouchpadInfoHistory` | `0x76EA0` | 128 | UnwindData |  |
| 2514 | *Ordinal Only* | `0x76F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2254 | `RegisterPointerInputTarget` | `0x76F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2695 | *Ordinal Only* | `0x76F70` | 148 | UnwindData |  |
| 2462 | `UnregisterPointerInputTarget` | `0x77010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1864 | `GetInternalWindowPos` | `0x77030` | 160 | UnwindData |  |
| 2079 | `SetThreadCursorCreationScaling` | `0x77160` | 74 | UnwindData |  |
| 1602 | `CreateAcceleratorTableA` | `0x771B0` | 130 | UnwindData |  |
| 1617 | `CreateIconFromResource` | `0x77240` | 33 | UnwindData |  |
| 1690 | `DialogBoxIndirectParamA` | `0x77270` | 33 | UnwindData |  |
| 2598 | *Ordinal Only* | `0x772A0` | 30 | UnwindData |  |
| 1859 | `GetIconInfoExA` | `0x772D0` | 352 | UnwindData |  |
| 1702 | `DlgDirListComboBoxA` | `0x787A0` | 233 | UnwindData |  |
| 1703 | `DlgDirListComboBoxW` | `0x78890` | 85 | UnwindData |  |
| 1705 | `DlgDirSelectComboBoxExA` | `0x788F0` | 165 | UnwindData |  |
| 1706 | `DlgDirSelectComboBoxExW` | `0x789A0` | 128 | UnwindData |  |
| 1640 | `DdeConnect` | `0x795B0` | 270 | UnwindData |  |
| 1641 | `DdeConnectList` | `0x796D0` | 745 | UnwindData |  |
| 1646 | `DdeDisconnectList` | `0x799C0` | 281 | UnwindData |  |
| 1652 | `DdeGetQualityOfService` | `0x79AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1664 | `DdeSetQualityOfService` | `0x79AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2349 | `SetMessageQueue` | `0x79AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1663 | `DdeReconnect` | `0x79AF0` | 448 | UnwindData |  |
| 1538 | `CancelShutdown` | `0x79D00` | 105 | UnwindData |  |
| 1752 | `EndTask` | `0x79D70` | 199 | UnwindData |  |
| 1963 | `GetTabbedTextExtentA` | `0x79E40` | 255 | UnwindData |  |
| 2478 | `UserLpkPSMTextOut` | `0x79F50` | 602 | UnwindData |  |
| 2479 | `UserLpkTabbedTextOut` | `0x7A1B0` | 648 | UnwindData |  |
| 1651 | `DdeGetLastError` | `0x7A440` | 83 | UnwindData |  |
| 1653 | `DdeImpersonateClient` | `0x7A4A0` | 142 | UnwindData |  |
| 1654 | `DdeInitializeA` | `0x7A540` | 3,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1835 | `GetDialogControlDpiChangeBehavior` | `0x7B1A0` | 32 | UnwindData |  |
| 1836 | `GetDialogDpiChangeBehavior` | `0x7B1D0` | 66 | UnwindData |  |
| 2322 | `SetDlgItemInt` | `0x7B220` | 187 | UnwindData |  |
| 1905 | `GetNextDlgGroupItem` | `0x7B2F0` | 122 | UnwindData |  |
| 1845 | `GetDpiAwarenessContextForProcess` | `0x7B370` | 24 | UnwindData |  |
| 1849 | `GetDpiFromDpiAwarenessContext` | `0x7B390` | 29 | UnwindData |  |
| 1968 | `GetThreadDpiHostingBehavior` | `0x7B3C0` | 63 | UnwindData |  |
| 2813 | *Ordinal Only* | `0x7B810` | 127 | UnwindData |  |
| 2809 | *Ordinal Only* | `0x7B8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2810 | *Ordinal Only* | `0x7B8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2812 | *Ordinal Only* | `0x7B8C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2811 | *Ordinal Only* | `0x7B8D0` | 127 | UnwindData |  |
| 2808 | *Ordinal Only* | `0x7B960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2814 | *Ordinal Only* | `0x7B970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2806 | `SetMaxTouchpadSensitivity` | `0x7B980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2807 | *Ordinal Only* | `0x7B990` | 23,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2198 | `PrivateExtractIconExA` | `0x81380` | 135 | UnwindData |  |
| 2200 | `PrivateExtractIconsA` | `0x81410` | 175 | UnwindData |  |
| 1636 | `DdeAccessData` | `0x81A70` | 180 | UnwindData |  |
| 1637 | `DdeAddData` | `0x81B30` | 428 | UnwindData |  |
| 1648 | `DdeFreeDataHandle` | `0x81CF0` | 118 | UnwindData |  |
| 1666 | `DdeUnaccessData` | `0x81D70` | 107 | UnwindData |  |
| 2497 | `WinHelpA` | `0x82260` | 1,162 | UnwindData |  |
| 1643 | `DdeCreateStringHandleA` | `0x827C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1656 | `DdeKeepStringHandle` | `0x827E0` | 189 | UnwindData |  |
| 1662 | `DdeQueryStringW` | `0x828B0` | 32,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1701 | `DlgDirListA` | `0x8A690` | 236 | UnwindData |  |
| 1704 | `DlgDirListW` | `0x8A790` | 88 | UnwindData |  |
| 1707 | `DlgDirSelectExA` | `0x8A7F0` | 171 | UnwindData |  |
| 1708 | `DlgDirSelectExW` | `0x8A8B0` | 47 | UnwindData |  |
| 1879 | `GetMagnificationDesktopColorEffect` | `0x8AC30` | 220 | UnwindData |  |
| 1880 | `GetMagnificationDesktopMagnification` | `0x8AD20` | 139 | UnwindData |  |
| 1881 | `GetMagnificationDesktopSamplingMode` | `0x8ADC0` | 76 | UnwindData |  |
| 2336 | `SetMagnificationDesktopColorEffect` | `0x8AE20` | 206 | UnwindData |  |
| 1540 | `CascadeWindows` | `0x8BEE0` | 37 | UnwindData |  |
| 2283 | `ScrollChildren` | `0x8BF10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2436 | `TileWindows` | `0x8BF40` | 37 | UnwindData |  |
| 1546 | `ChangeMenuA` | `0x8BF70` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1547 | `ChangeMenuW` | `0x8C020` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1724 | `DrawMenuBarTemp` | `0x8C0D0` | 130 | UnwindData |  |
| 1885 | `GetMenuCheckMarkDimensions` | `0x8C160` | 58 | UnwindData |  |
| 1886 | `GetMenuContextHelpId` | `0x8C1A0` | 25 | UnwindData |  |
| 2134 | `MB_GetString` | `0x8D7A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2151 | `MessageBoxA` | `0x8D7D0` | 75 | UnwindData |  |
| 2152 | `MessageBoxExA` | `0x8D830` | 30 | UnwindData |  |
| 2155 | `MessageBoxIndirectW` | `0x8D860` | 174 | UnwindData |  |
| 2156 | `MessageBoxTimeoutA` | `0x8D920` | 333 | UnwindData |  |
| 1714 | `DrawCaption` | `0x8DC60` | 171 | UnwindData |  |
| 2185 | `PaintDesktop` | `0x8DD60` | 622 | UnwindData |  |
| 2688 | `RegisterTouchpadCapableThread` | `0x8DFE0` | 60 | UnwindData |  |
| 2399 | `SetWindowRgnEx` | `0x8E030` | 60 | UnwindData |  |
| 1568 | `CharToOemW` | `0x8E080` | 99 | UnwindData |  |
| 2169 | `OemKeyScan` | `0x8E0F0` | 132 | UnwindData |  |
| 2334 | `SetLastErrorEx` | `0x8E180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2373 | `SetSysColorsTemp` | `0x8E1A0` | 385 | UnwindData |  |
| 1753 | `EnterReaderModeHelper` | `0x8E610` | 119 | UnwindData |  |
| 2233 | `ReasonCodeNeedsBugID` | `0x8E980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2234 | `ReasonCodeNeedsComment` | `0x8E990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1552 | *Ordinal Only* | `0x8E9A0` | 69 | UnwindData |  |
| 1550 | *Ordinal Only* | `0x8E9F0` | 129 | UnwindData |  |
| 1551 | *Ordinal Only* | `0x8EA80` | 41 | UnwindData |  |
| 1624 | `CreateSyntheticPointerDevice` | `0x8EAB0` | 78 | UnwindData |  |
| 2690 | `CreateSyntheticPointerDevice2` | `0x8EB10` | 92 | UnwindData |  |
| 2038 | `InitializePointerDeviceInjectionEx` | `0x8EB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2223 | `RIMRegisterForInput` | `0x8EBA0` | 34 | UnwindData |  |
| 2137 | `MITSynthesizeTouchInput` | `0x8EBD0` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1951 | `GetScrollPos` | `0x8EE70` | 840 | UnwindData |  |
| 1952 | `GetScrollRange` | `0x8F1C0` | 925 | UnwindData |  |
| 2367 | `SetScrollPos` | `0x8F5B0` | 177 | UnwindData |  |
| 2368 | `SetScrollRange` | `0x8F670` | 346 | UnwindData |  |
| 2413 | `ShowScrollBar` | `0x8F7D0` | 512 | UnwindData |  |
| 2511 | *Ordinal Only* | `0x94F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2566 | *Ordinal Only* | `0x94F20` | 74 | UnwindData |  |
| 1775 | `EvaluateProximityToPolygon` | `0x96C30` | 1,393 | UnwindData |  |
| 2502 | `_UserTestTokenForInteractive` | `0x97240` | 223 | UnwindData |  |
| 2086 | `IsThreadTSFEventAware` | `0x973C0` | 114 | UnwindData |  |
| 2138 | `MakeThreadTSFEventAware` | `0x97440` | 90 | UnwindData |  |
| 2277 | `RemoveThreadTSFEventAwareness` | `0x974A0` | 75 | UnwindData |  |
| 1514 | `AnyPopup` | `0x97500` | 64 | UnwindData |  |
| 1852 | `GetForegroundWindow` | `0x97590` | 133 | UnwindData |  |
| 2003 | `GetWindowProcessHandle` | `0x97620` | 101 | UnwindData |  |
| 2540 | *Ordinal Only* | `0x97690` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1635 | `DdeAbandonTransaction` | `0x978C0` | 235 | UnwindData |  |
| 1659 | `DdeQueryConvInfo` | `0x979C0` | 548 | UnwindData |  |
| 1665 | `DdeSetUserHandle` | `0x97BF0` | 150 | UnwindData |  |
| 1532 | `CallMsgFilter` | `0x97C90` | 273 | UnwindData |  |
| 1533 | `CallMsgFilterA` | `0x97C90` | 273 | UnwindData |  |
| 1715 | `DrawCaptionTempA` | `0x97DB0` | 277 | UnwindData |  |
| 1790 | `GetAltTabInfo` | `0x97ED0` | 38 | UnwindData |  |
| 1791 | `GetAltTabInfoA` | `0x97ED0` | 38 | UnwindData |  |
| 2293 | `SendMessageCallbackA` | `0x97F00` | 136 | UnwindData |  |
| 2304 | `SetClassLongA` | `0x97F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2487 | `VkKeyScanExA` | `0x97FB0` | 211 | UnwindData |  |
| 2022 | `IMPGetIMEA` | `0x989D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2023 | `IMPGetIMEW` | `0x989F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2024 | `IMPQueryIMEA` | `0x98A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2025 | `IMPQueryIMEW` | `0x98A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2026 | `IMPSetIMEA` | `0x98A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2027 | `IMPSetIMEW` | `0x98A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2289 | `SendIMEMessageExA` | `0x98A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2290 | `SendIMEMessageExW` | `0x98AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2491 | `WINNLSEnableIME` | `0x98AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2492 | `WINNLSGetEnableStatus` | `0x98AF0` | 7,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2683 | `GetCurrentMonitorTopologyId` | `0x9A740` | 2,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1511 | `AllowForegroundActivation` | `0x9AFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1518 | `ArrangeIconicWindows` | `0x9AFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `CascadeChildWindows` | `0x9B000` | 42 | UnwindData |  |
| 1592 | `CloseWindow` | `0x9B030` | 57 | UnwindData |  |
| 1607 | `CreateDesktopA` | `0x9B070` | 44 | UnwindData |  |
| 1608 | `CreateDesktopExA` | `0x9B0B0` | 394 | UnwindData |  |
| 2640 | *Ordinal Only* | `0x9B240` | 218 | UnwindData |  |
| 2641 | *Ordinal Only* | `0x9B320` | 351 | UnwindData |  |
| 1631 | `CreateWindowStationA` | `0x9B490` | 116 | UnwindData |  |
| 1678 | `DeferWindowPosAndBand` | `0x9B510` | 85 | UnwindData |  |
| 2645 | *Ordinal Only* | `0x9B570` | 33 | UnwindData |  |
| 2584 | *Ordinal Only* | `0x9B5A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2575 | *Ordinal Only* | `0x9B600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1861 | `GetInputDesktop` | `0x9B620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1865 | `GetKBCodePage` | `0x9B640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1937 | `GetProgmanWindow` | `0x9B660` | 88 | UnwindData |  |
| 1973 | `GetUnpredictedMessagePos` | `0x9B6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1980 | `GetWinStationInfo` | `0x9B6E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1985 | `GetWindowContextHelpId` | `0x9B700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2017 | `GrayStringA` | `0x9B720` | 78 | UnwindData |  |
| 2018 | `GrayStringW` | `0x9B780` | 75 | UnwindData |  |
| 2113 | `LoadKeyboardLayoutA` | `0x9B7E0` | 127 | UnwindData |  |
| 2114 | `LoadKeyboardLayoutEx` | `0x9B870` | 35 | UnwindData |  |
| 2167 | `NotifyOverlayWindow` | `0x9B8A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2178 | `OpenIcon` | `0x9B8C0` | 57 | UnwindData |  |
| 2181 | `OpenWindowStationA` | `0x9B900` | 101 | UnwindData |  |
| 2554 | *Ordinal Only* | `0x9B970` | 50 | UnwindData |  |
| 2248 | `RegisterFrostWindow` | `0x9B9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2552 | *Ordinal Only* | `0x9B9D0` | 20 | UnwindData |  |
| 2262 | `RegisterSystemThread` | `0x9B9F0` | 26 | UnwindData |  |
| 2316 | `SetDeskWallpaper` | `0x9BA10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2325 | `SetDoubleClickTime` | `0x9BA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2361 | `SetProgmanWindow` | `0x9BA50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2634 | *Ordinal Only* | `0x9BA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2570 | *Ordinal Only* | `0x9BA90` | 80 | UnwindData |  |
| 2389 | `SetWindowContextHelpId` | `0x9BAF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2414 | `ShowStartGlass` | `0x9BB10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2435 | `TileChildWindows` | `0x9BB30` | 42 | UnwindData |  |
| 2553 | *Ordinal Only* | `0x9BB60` | 121 | UnwindData |  |
| 2451 | `UnhookWindowsHook` | `0x9BBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2454 | `UnloadKeyboardLayout` | `0x9BC00` | 45 | UnwindData |  |
| 2481 | `UserRegisterWowHandlers` | `0x9BC40` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1625 | `CreateSystemThreads` | `0x9BD10` | 24 | UnwindData |  |
| 1545 | `ChangeDisplaySettingsW` | `0x9C9F0` | 42 | UnwindData |  |
| 1716 | `DrawCaptionTempW` | `0x9CA20` | 225 | UnwindData |  |
| 1524 | `BroadcastSystemMessage` | `0x9CB90` | 39 | UnwindData |  |
| 1525 | `BroadcastSystemMessageA` | `0x9CB90` | 39 | UnwindData |  |
| 1526 | `BroadcastSystemMessageExA` | `0x9CBC0` | 43 | UnwindData |  |
| 1842 | `GetDlgItemTextA` | `0x9CC00` | 63 | UnwindData |  |
| 1997 | `GetWindowModuleFileName` | `0x9CC50` | 60 | UnwindData |  |
| 1998 | `GetWindowModuleFileNameA` | `0x9CC50` | 60 | UnwindData |  |
| 2159 | `ModifyMenuA` | `0x9CCA0` | 146 | UnwindData |  |
| 1510 | `AlignRects` | `0x9D680` | 352 | UnwindData |  |
| 2547 | `gapfnScSendMessage` | `0xAA440` | 155,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2543 | `gSharedInfo` | `0xD02C0` | 0 | Indeterminate |  |
