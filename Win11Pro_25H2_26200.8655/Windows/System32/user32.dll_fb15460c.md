# Binary Specification: user32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\user32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fb15460c5a7068a9cb118cfdec0b60f2c715018c4af8f501b62825a6435421d1`
* **Total Exported Functions:** 1208

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1668 | `DefDlgProcA` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.NtdllDialogWndProc_A` |
| 1669 | `DefDlgProcW` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.NtdllDialogWndProc_W` |
| 1675 | `DefWindowProcA` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.NtdllDefWindowProc_A` |
| 1676 | `DefWindowProcW` | `0x0` | - | Forwarded | Forwarded to: `NTDLL.NtdllDefWindowProc_W` |
| 2131 | `LookupIconIdFromDirectoryEx` | `0x36B0` | 123 | UnwindData |  |
| 1618 | `CreateIconFromResourceEx` | `0x3FC0` | 377 | UnwindData |  |
| 1598 | `CopyIcon` | `0x4A80` | 150 | UnwindData |  |
| 2270 | `ReleaseDC` | `0x5AA0` | 88 | UnwindData |  |
| 1509 | `AdjustWindowRectExForDpi` | `0x5B60` | 147 | UnwindData |  |
| 1619 | `CreateIconIndirect` | `0x62D0` | 1,173 | UnwindData |  |
| 1795 | `GetAppCompatFlags2` | `0x7AF0` | 90 | UnwindData |  |
| 2108 | `LoadCursorW` | `0x7B50` | 35 | UnwindData |  |
| 1847 | `GetDpiForSystem` | `0x87F0` | 155 | UnwindData |  |
| 1962 | `GetSystemMetricsForDpi` | `0x8980` | 211 | UnwindData |  |
| 1961 | `GetSystemMetrics` | `0x8AD0` | 218 | UnwindData |  |
| 2093 | `IsWindowEnabled` | `0xA0D0` | 62 | UnwindData |  |
| 2574 | *Ordinal Only* | `0xA120` | 54 | UnwindData |  |
| 1536 | `CallWindowProcA` | `0xA160` | 269 | UnwindData |  |
| 1848 | `GetDpiForWindow` | `0xA280` | 90 | UnwindData |  |
| 2012 | `GetWindowTextLengthW` | `0xA2E0` | 82 | UnwindData |  |
| 2572 | *Ordinal Only* | `0xA340` | 39 | UnwindData |  |
| 1840 | `GetDlgItem` | `0xA370` | 170 | UnwindData |  |
| 2096 | `IsWindowUnicode` | `0xA420` | 33 | UnwindData |  |
| 1811 | `GetClassNameA` | `0xABC0` | 165 | UnwindData |  |
| 2146 | `MapWindowPoints` | `0xAC70` | 76 | UnwindData |  |
| 2712 | *Ordinal Only* | `0xAEB0` | 18 | UnwindData |  |
| 2292 | `SendMessageA` | `0xB090` | 181 | UnwindData |  |
| 2297 | `SendMessageW` | `0xB150` | 35 | UnwindData |  |
| 1537 | `CallWindowProcW` | `0xBCF0` | 39 | UnwindData |  |
| 1993 | `GetWindowLongPtrA` | `0xD050` | 64 | UnwindData |  |
| 1995 | `GetWindowLongW` | `0xD290` | 408 | UnwindData |  |
| 1994 | `GetWindowLongPtrW` | `0xD5E0` | 408 | UnwindData |  |
| 1992 | `GetWindowLongA` | `0xE0F0` | 64 | UnwindData |  |
| 2013 | `GetWindowTextW` | `0xE140` | 160 | UnwindData |  |
| 2009 | `GetWindowTextA` | `0xE2E0` | 167 | UnwindData |  |
| 2402 | `SetWindowTextW` | `0xE390` | 102 | UnwindData |  |
| 2536 | *Ordinal Only* | `0xF140` | 264 | UnwindData |  |
| 2394 | `SetWindowLongPtrW` | `0xF710` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2051 | `InsertMenuW` | `0xF9B0` | 146 | UnwindData |  |
| 2347 | `SetMenuItemInfoW` | `0xFA50` | 133 | UnwindData |  |
| 1887 | `GetMenuDefaultItem` | `0xFAE0` | 57 | UnwindData |  |
| 1896 | `GetMenuStringW` | `0xFB20` | 133 | UnwindData |  |
| 1894 | `GetMenuState` | `0xFBB0` | 114 | UnwindData |  |
| 2077 | `IsMenu` | `0xFC80` | 27 | UnwindData |  |
| 1576 | `CheckMenuItem` | `0xFCB0` | 122 | UnwindData |  |
| 1577 | `CheckMenuRadioItem` | `0xFD30` | 450 | UnwindData |  |
| 1890 | `GetMenuItemID` | `0xFF00` | 133 | UnwindData |  |
| 1740 | `EnableMenuItem` | `0xFF90` | 151 | UnwindData |  |
| 1956 | `GetSubMenu` | `0x10030` | 142 | UnwindData |  |
| 1889 | `GetMenuItemCount` | `0x100D0` | 60 | UnwindData |  |
| 2050 | `InsertMenuItemW` | `0x102D0` | 429 | UnwindData |  |
| 1892 | `GetMenuItemInfoW` | `0x10490` | 259 | UnwindData |  |
| 1516 | `AppendMenuW` | `0x10D40` | 139 | UnwindData |  |
| 1891 | `GetMenuItemInfoA` | `0x11220` | 259 | UnwindData |  |
| 1888 | `GetMenuInfo` | `0x114D0` | 154 | UnwindData |  |
| 1895 | `GetMenuStringA` | `0x11810` | 131 | UnwindData |  |
| 2160 | `ModifyMenuW` | `0x118A0` | 143 | UnwindData |  |
| 2473 | `UpdateWindow` | `0x11E70` | 81 | UnwindData |  |
| 2523 | *Ordinal Only* | `0x126B0` | 93 | UnwindData |  |
| 1971 | `GetTopWindow` | `0x12720` | 466 | UnwindData |  |
| 1981 | `GetWindow` | `0x12900` | 442 | UnwindData |  |
| 1794 | `GetAppCompatFlags` | `0x12E10` | 65 | UnwindData |  |
| 2068 | `IsDialogMessage` | `0x12F10` | 165 | UnwindData |  |
| 2069 | `IsDialogMessageA` | `0x12F10` | 165 | UnwindData |  |
| 2188 | `PeekMessageA` | `0x13540` | 458 | UnwindData |  |
| 2189 | `PeekMessageW` | `0x13710` | 406 | UnwindData |  |
| 2070 | `IsDialogMessageW` | `0x13F80` | 889 | UnwindData |  |
| 2448 | `TranslateMessage` | `0x14300` | 143 | UnwindData |  |
| 1534 | `CallMsgFilterW` | `0x144D0` | 196 | UnwindData |  |
| 1897 | `GetMessageA` | `0x145A0` | 429 | UnwindData |  |
| 2091 | `IsWindow` | `0x147D0` | 367 | UnwindData |  |
| 2162 | `MonitorFromRect` | `0x14990` | 61 | UnwindData |  |
| 2163 | `MonitorFromWindow` | `0x14B60` | 736 | UnwindData |  |
| 1902 | `GetMonitorInfoA` | `0x15950` | 518 | UnwindData |  |
| 2161 | `MonitorFromPoint` | `0x15DC0` | 61 | UnwindData |  |
| 2085 | `IsThreadDesktopComposited` | `0x16660` | 88 | UnwindData |  |
| 2168 | `NotifyWinEvent` | `0x17A40` | 65 | UnwindData |  |
| 2090 | `IsWinEventHookInstalled` | `0x17A90` | 95 | UnwindData |  |
| 2398 | `SetWindowRgn` | `0x18480` | 158 | UnwindData |  |
| 1508 | `AdjustWindowRectEx` | `0x18530` | 114 | UnwindData |  |
| 2430 | `SystemParametersInfoA` | `0x18660` | 173 | UnwindData |  |
| 1950 | `GetScrollInfo` | `0x18720` | 156 | UnwindData |  |
| 2366 | `SetScrollInfo` | `0x187D0` | 175 | UnwindData |  |
| 2432 | `SystemParametersInfoW` | `0x189D0` | 173 | UnwindData |  |
| 2431 | `SystemParametersInfoForDpi` | `0x18C10` | 183 | UnwindData |  |
| 1507 | `AdjustWindowRect` | `0x18CD0` | 101 | UnwindData |  |
| 1744 | `EnableScrollBar` | `0x18D40` | 158 | UnwindData |  |
| 1726 | `DrawStateW` | `0x18FB0` | 2,039 | UnwindData |  |
| 1721 | `DrawIcon` | `0x19960` | 42 | UnwindData |  |
| 1722 | `DrawIconEx` | `0x19990` | 892 | UnwindData |  |
| 1833 | `GetDesktopWindow` | `0x1A910` | 155 | UnwindData |  |
| 1779 | `FillRect` | `0x1A9C0` | 112 | UnwindData |  |
| 1717 | `DrawEdge` | `0x1B390` | 887 | UnwindData |  |
| 2555 | *Ordinal Only* | `0x1BDD0` | 237 | UnwindData |  |
| 1738 | `EditWndProc` | `0x201E0` | 828 | UnwindData |  |
| 2004 | `GetWindowRect` | `0x20CE0` | 365 | UnwindData |  |
| 2475 | `User32InitializeImmEntryTable` | `0x22E60` | 250 | UnwindData |  |
| 2193 | `PostMessageW` | `0x25290` | 173 | UnwindData |  |
| 1590 | `CloseGestureInfoHandle` | `0x25D70` | 205 | UnwindData |  |
| 1591 | `CloseTouchInputHandle` | `0x25E50` | 213 | UnwindData |  |
| 2192 | `PostMessageA` | `0x261E0` | 465 | UnwindData |  |
| 2444 | `TranslateAccelerator` | `0x263C0` | 138 | UnwindData |  |
| 2445 | `TranslateAcceleratorA` | `0x263C0` | 138 | UnwindData |  |
| 1979 | `GetUserObjectSecurity` | `0x265D0` | 54 | UnwindData |  |
| 2195 | `PostThreadMessageA` | `0x26610` | 216 | UnwindData |  |
| 2384 | `SetUserObjectSecurity` | `0x266F0` | 44 | UnwindData |  |
| 2506 | *Ordinal Only* | `0x26730` | 514 | UnwindData |  |
| 1502 | *Ordinal Only* | `0x26A60` | 388 | UnwindData |  |
| 1856 | `GetGestureInfo` | `0x26CF0` | 273 | UnwindData |  |
| 2182 | `OpenWindowStationW` | `0x27BC0` | 70 | UnwindData |  |
| 2309 | `SetClipboardData` | `0x280E0` | 642 | UnwindData |  |
| 1817 | `GetClipboardData` | `0x286B0` | 1,585 | UnwindData |  |
| 2115 | `LoadKeyboardLayoutW` | `0x29930` | 31 | UnwindData |  |
| 1565 | `CharToOemA` | `0x29B40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2170 | `OemToCharA` | `0x29B90` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2472 | `UpdatePerUserSystemParameters` | `0x29C80` | 359 | UnwindData |  |
| 1908 | `GetParent` | `0x2AB70` | 564 | UnwindData |  |
| 2199 | `PrivateExtractIconExW` | `0x2B500` | 401 | UnwindData |  |
| 2305 | `SetClassLongPtrA` | `0x2B6A0` | 263 | UnwindData |  |
| 1620 | `CreateMDIWindowA` | `0x2B820` | 110 | UnwindData |  |
| 2239 | `RegisterClassExA` | `0x2B8A0` | 58 | UnwindData |  |
| 2111 | `LoadImageA` | `0x2B8E0` | 328 | UnwindData |  |
| 1803 | `GetClassInfoA` | `0x2BA30` | 121 | UnwindData |  |
| 1804 | `GetClassInfoExA` | `0x2BAB0` | 703 | UnwindData |  |
| 2201 | `PrivateExtractIconsW` | `0x2BD80` | 980 | UnwindData |  |
| 2238 | `RegisterClassA` | `0x2C540` | 121 | UnwindData |  |
| 2457 | `UnregisterClassA` | `0x2CB60` | 483 | UnwindData |  |
| 1629 | `CreateWindowInBandEx` | `0x2CFD0` | 153 | UnwindData |  |
| 1628 | `CreateWindowInBand` | `0x2D1E0` | 146 | UnwindData |  |
| 1626 | `CreateWindowExA` | `0x2D280` | 139 | UnwindData |  |
| 1806 | `GetClassInfoW` | `0x2D4E0` | 121 | UnwindData |  |
| 1805 | `GetClassInfoExW` | `0x2D560` | 609 | UnwindData |  |
| 2241 | `RegisterClassW` | `0x2D7D0` | 121 | UnwindData |  |
| 2240 | `RegisterClassExW` | `0x2D850` | 58 | UnwindData |  |
| 1627 | `CreateWindowExW` | `0x2D890` | 139 | UnwindData |  |
| 2458 | `UnregisterClassW` | `0x2E6B0` | 417 | UnwindData |  |
| 2104 | `LoadBitmapW` | `0x2F720` | 26 | UnwindData |  |
| 1611 | `CreateDialogIndirectParamA` | `0x2F740` | 33 | UnwindData |  |
| 1612 | `CreateDialogIndirectParamAorW` | `0x2F770` | 113 | UnwindData |  |
| 1613 | `CreateDialogIndirectParamW` | `0x30D30` | 30 | UnwindData |  |
| 2103 | `LoadBitmapA` | `0x30D80` | 276 | UnwindData |  |
| 2635 | *Ordinal Only* | `0x31370` | 222 | UnwindData |  |
| 1749 | `EndDialog` | `0x31990` | 406 | UnwindData |  |
| 1789 | `GetActiveWindow` | `0x31B30` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1851 | `GetFocus` | `0x31BD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2066 | `IsChild` | `0x31C00` | 859 | UnwindData |  |
| 1906 | `GetNextDlgTabItem` | `0x321C0` | 114 | UnwindData |  |
| 2423 | `SoftModalMessageBox` | `0x32920` | 1,973 | UnwindData |  |
| 1727 | `DrawTextA` | `0x34270` | 126 | UnwindData |  |
| 1728 | `DrawTextExA` | `0x34300` | 656 | UnwindData |  |
| 1729 | `DrawTextExW` | `0x345A0` | 38 | UnwindData |  |
| 1730 | `DrawTextW` | `0x345D0` | 222 | UnwindData |  |
| 1964 | `GetTabbedTextExtentW` | `0x37190` | 61 | UnwindData |  |
| 2434 | `TabbedTextOutW` | `0x371E0` | 74 | UnwindData |  |
| 2433 | `TabbedTextOutA` | `0x37230` | 575 | UnwindData |  |
| 1513 | `AnimateWindow` | `0x37480` | 4,309 | UnwindData |  |
| 2097 | `IsWindowVisible` | `0x385B0` | 443 | UnwindData |  |
| 1645 | `DdeDisconnect` | `0x38FC0` | 163 | UnwindData |  |
| 1667 | `DdeUninitialize` | `0x39070` | 480 | UnwindData |  |
| 1660 | `DdeQueryNextServer` | `0x396D0` | 328 | UnwindData |  |
| 1650 | `DdeGetData` | `0x39820` | 341 | UnwindData |  |
| 1638 | `DdeClientTransaction` | `0x39A00` | 1,718 | UnwindData |  |
| 1658 | `DdePostAdvise` | `0x3A0C0` | 727 | UnwindData |  |
| 1647 | `DdeEnableCallback` | `0x3A4A0` | 456 | UnwindData |  |
| 1657 | `DdeNameService` | `0x3A670` | 654 | UnwindData |  |
| 1649 | `DdeFreeStringHandle` | `0x3AA00` | 222 | UnwindData |  |
| 2527 | *Ordinal Only* | `0x3AE30` | 37 | UnwindData |  |
| 2525 | *Ordinal Only* | `0x3AE60` | 44 | UnwindData |  |
| 1756 | `EnumDesktopWindows` | `0x3AEA0` | 41 | UnwindData |  |
| 1770 | `EnumThreadWindows` | `0x3AED0` | 42 | UnwindData |  |
| 1901 | `GetMessageW` | `0x3B330` | 22 | UnwindData |  |
| 2362 | `SetPropA` | `0x3C310` | 431 | UnwindData |  |
| 2363 | `SetPropW` | `0x3C4D0` | 442 | UnwindData |  |
| 1938 | `GetPropA` | `0x3C690` | 317 | UnwindData |  |
| 1939 | `GetPropW` | `0x3C7E0` | 61 | UnwindData |  |
| 2074 | `IsIconic` | `0x3CB90` | 399 | UnwindData |  |
| 1903 | `GetMonitorInfoW` | `0x3CD30` | 214 | UnwindData |  |
| 1773 | `EnumWindows` | `0x3D1C0` | 176 | UnwindData |  |
| 2319 | `SetDialogDpiChangeBehavior` | `0x3D570` | 170 | UnwindData |  |
| 2534 | *Ordinal Only* | `0x3D620` | 207 | UnwindData |  |
| 2014 | `GetWindowThreadProcessId` | `0x3D700` | 273 | UnwindData |  |
| 1809 | `GetClassLongPtrW` | `0x3D950` | 1,108 | UnwindData |  |
| 2166 | `MsgWaitForMultipleObjectsEx` | `0x3DDB0` | 175 | UnwindData |  |
| 2378 | `SetThreadDpiAwarenessContext` | `0x3DEC0` | 29 | UnwindData |  |
| 1807 | `GetClassLongA` | `0x3E0F0` | 64 | UnwindData |  |
| 1808 | `GetClassLongPtrA` | `0x3E140` | 64 | UnwindData |  |
| 1813 | `GetClassWord` | `0x3E700` | 161 | UnwindData |  |
| 1810 | `GetClassLongW` | `0x3E7B0` | 150 | UnwindData |  |
| 1868 | `GetKeyState` | `0x3EB20` | 172 | UnwindData |  |
| 2205 | `QueryDisplayConfig` | `0x3EBE0` | 619 | UnwindData |  |
| 1776 | `EvaluateProximityToRect` | `0x3FB00` | 304 | UnwindData |  |
| 2203 | `PtInRect` | `0x3FCB0` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2054 | `IntersectRect` | `0x3FFA0` | 2,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1943 | `GetRawInputDeviceInfoA` | `0x40830` | 315 | UnwindData |  |
| 2230 | `RealGetWindowClass` | `0x40980` | 212 | UnwindData |  |
| 2231 | `RealGetWindowClassA` | `0x40980` | 212 | UnwindData |  |
| 1818 | `GetClipboardFormatNameA` | `0x40A60` | 172 | UnwindData |  |
| 1866 | `GetKeyNameTextA` | `0x40B20` | 184 | UnwindData |  |
| 2122 | `LoadStringA` | `0x40BE0` | 144 | UnwindData |  |
| 2490 | `WCSToMBEx` | `0x40C80` | 448 | UnwindData |  |
| 2075 | `IsImmersiveProcess` | `0x40E50` | 88 | UnwindData |  |
| 1940 | `GetQueueStatus` | `0x40EB0` | 136 | UnwindData |  |
| 1535 | `CallNextHookEx` | `0x40F40` | 451 | UnwindData |  |
| 1754 | `EnumChildWindows` | `0x41170` | 915 | UnwindData |  |
| 2557 | *Ordinal Only* | `0x41550` | 140 | UnwindData |  |
| 2356 | `SetProcessDpiAwarenessContext` | `0x41B60` | 162 | UnwindData |  |
| 2558 | *Ordinal Only* | `0x41C10` | 140 | UnwindData |  |
| 1988 | `GetWindowDpiAwarenessContext` | `0x41DD0` | 34 | UnwindData |  |
| 2449 | `TranslateMessageEx` | `0x422D0` | 83 | UnwindData |  |
| 1983 | `GetWindowCompositionAttribute` | `0x42330` | 129 | UnwindData |  |
| 2099 | `IsZoomed` | `0x42690` | 396 | UnwindData |  |
| 1839 | `GetDlgCtrlID` | `0x42830` | 358 | UnwindData |  |
| 1600 | `CopyRect` | `0x429A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2165 | `MsgWaitForMultipleObjects` | `0x429D0` | 150 | UnwindData |  |
| 1759 | `EnumDisplayDevicesA` | `0x42AD0` | 628 | UnwindData |  |
| 1774 | `EqualRect` | `0x42D50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2583 | `wsprintfW` | `0x42D80` | 34 | UnwindData |  |
| 2601 | `wvsprintfW` | `0x42DB0` | 2,541 | UnwindData |  |
| 2174 | `OffsetRect` | `0x43BA0` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2082 | `IsRectEmpty` | `0x44180` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2580 | `wsprintfA` | `0x441B0` | 34 | UnwindData |  |
| 2596 | `wvsprintfA` | `0x441E0` | 2,389 | UnwindData |  |
| 2089 | `IsValidDpiAwarenessContext` | `0x44B40` | 146 | UnwindData |  |
| 1517 | `AreDpiAwarenessContextsEqual` | `0x44BE0` | 350 | UnwindData |  |
| 1798 | `GetAwarenessFromDpiAwarenessContext` | `0x44D50` | 142 | UnwindData |  |
| 2242 | `RegisterClipboardFormatA` | `0x44E40` | 321 | UnwindData |  |
| 2267 | `RegisterWindowMessageA` | `0x44E40` | 321 | UnwindData |  |
| 2364 | `SetRect` | `0x45400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2453 | `UnionRect` | `0x45430` | 189 | UnwindData |  |
| 1812 | `GetClassNameW` | `0x45500` | 51 | UnwindData |  |
| 1672 | `DefMDIChildProcA` | `0x45BF0` | 23 | UnwindData |  |
| 1673 | `DefMDIChildProcW` | `0x45C10` | 20 | UnwindData |  |
| 1670 | `DefFrameProcA` | `0x45FD0` | 33 | UnwindData |  |
| 1671 | `DefFrameProcW` | `0x46000` | 30 | UnwindData |  |
| 2381 | `SetTimer` | `0x473A0` | 27 | UnwindData |  |
| 2446 | `TranslateAcceleratorW` | `0x473D0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1838 | `GetDisplayConfigBufferSizes` | `0x474A0` | 102 | UnwindData |  |
| 1782 | `FindWindowExW` | `0x47510` | 207 | UnwindData |  |
| 2296 | `SendMessageTimeoutW` | `0x475F0` | 429 | UnwindData |  |
| 1947 | `GetReasonTitleFromReasonCode` | `0x478F0` | 295 | UnwindData |  |
| 2518 | *Ordinal Only* | `0x47A20` | 63 | UnwindData |  |
| 2235 | `RecordShutdownReason` | `0x47EE0` | 1,311 | UnwindData |  |
| 1529 | `BuildReasonArray` | `0x487C0` | 418 | UnwindData |  |
| 1687 | `DestroyReasons` | `0x48B80` | 132 | UnwindData |  |
| 2395 | `SetWindowLongW` | `0x49040` | 267 | UnwindData |  |
| 1863 | `GetInputState` | `0x491C0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1697 | `DispatchMessageW` | `0x49270` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2030 | `InSendMessageEx` | `0x49360` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2294 | `SendMessageCallbackW` | `0x493A0` | 134 | UnwindData |  |
| 1967 | `GetThreadDpiAwarenessContext` | `0x49460` | 146 | UnwindData |  |
| 1731 | `DwmGetDxSharedSurface` | `0x49500` | 186 | UnwindData |  |
| 1574 | `CheckDBCSEnabledExt` | `0x49630` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1764 | `EnumDisplaySettingsExW` | `0x49720` | 362 | UnwindData |  |
| 2133 | `MBToWCSExt` | `0x49890` | 248 | UnwindData |  |
| 1925 | `GetPointerInfo` | `0x49990` | 76 | UnwindData |  |
| 1982 | `GetWindowBand` | `0x499F0` | 72 | UnwindData |  |
| 1869 | `GetKeyboardLayout` | `0x49A40` | 93 | UnwindData |  |
| 1765 | `EnumDisplaySettingsW` | `0x49F00` | 311 | UnwindData |  |
| 2132 | `MBToWCSEx` | `0x4A040` | 416 | UnwindData |  |
| 1800 | `GetCapture` | `0x4A1F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2276 | `RemovePropW` | `0x4A220` | 153 | UnwindData |  |
| 2081 | `IsProcessDPIAware` | `0x4A2C0` | 118 | UnwindData |  |
| 1957 | `GetSysColor` | `0x4ABB0` | 53 | UnwindData |  |
| 1783 | `FindWindowW` | `0x4ABF0` | 178 | UnwindData |  |
| 2707 | *Ordinal Only* | `0x4ADB0` | 151 | UnwindData |  |
| 1763 | `EnumDisplaySettingsExA` | `0x4D610` | 654 | UnwindData |  |
| 2053 | `InternalGetWindowText` | `0x4D930` | 37 | UnwindData |  |
| 2560 | *Ordinal Only* | `0x4D960` | 307 | UnwindData |  |
| 1829 | `GetDC` | `0x4DB00` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2031 | `InflateRect` | `0x4DBC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1941 | `GetRawInputBuffer` | `0x4DBF0` | 101 | UnwindData |  |
| 2118 | `LoadMenuIndirectA` | `0x4DCA0` | 81 | UnwindData |  |
| 2119 | `LoadMenuIndirectW` | `0x4DCA0` | 81 | UnwindData |  |
| 2295 | `SendMessageTimeoutA` | `0x4E300` | 52 | UnwindData |  |
| 2365 | `SetRectEmpty` | `0x4E5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1698 | `DisplayConfigGetDeviceInfo` | `0x4E5F0` | 34 | UnwindData |  |
| 1858 | `GetIconInfo` | `0x4EC80` | 90 | UnwindData |  |
| 1542 | `ChangeDisplaySettingsA` | `0x4ECE0` | 42 | UnwindData |  |
| 1543 | `ChangeDisplaySettingsExA` | `0x4ED10` | 296 | UnwindData |  |
| 1544 | `ChangeDisplaySettingsExW` | `0x4F140` | 144 | UnwindData |  |
| 1760 | `EnumDisplayDevicesW` | `0x4F4E0` | 233 | UnwindData |  |
| 2425 | `SubtractRect` | `0x4F8E0` | 309 | UnwindData |  |
| 1876 | `GetLastInputInfo` | `0x4FA20` | 60 | UnwindData |  |
| 2029 | `InSendMessage` | `0x4FA70` | 70 | UnwindData |  |
| 1828 | `GetCursorPos` | `0x50370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1909 | `GetPhysicalCursorPos` | `0x50370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2243 | `RegisterClipboardFormatW` | `0x50390` | 71 | UnwindData |  |
| 2268 | `RegisterWindowMessageW` | `0x50390` | 71 | UnwindData |  |
| 1846 | `GetDpiForMonitorInternal` | `0x503E0` | 74 | UnwindData |  |
| 2094 | `IsWindowInDestroy` | `0x504A0` | 31 | UnwindData |  |
| 2092 | `IsWindowArranged` | `0x504D0` | 54 | UnwindData |  |
| 2405 | `SetWindowsHookExA` | `0x50510` | 23 | UnwindData |  |
| 2407 | `SetWindowsHookExW` | `0x50530` | 20 | UnwindData |  |
| 2406 | `SetWindowsHookExAW` | `0x50550` | 302 | UnwindData |  |
| 1875 | `GetLastActivePopup` | `0x50840` | 83 | UnwindData |  |
| 1898 | `GetMessageExtraInfo` | `0x50AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2299 | `SendNotifyMessageW` | `0x50AE0` | 94 | UnwindData |  |
| 2440 | `ToUnicodeEx` | `0x50B50` | 66 | UnwindData |  |
| 2123 | `LoadStringW` | `0x50C00` | 29 | UnwindData |  |
| 2196 | `PostThreadMessageW` | `0x50C30` | 61 | UnwindData |  |
| 1974 | `GetUpdateRect` | `0x50C80` | 109 | UnwindData |  |
| 1900 | `GetMessageTime` | `0x50D00` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2599 | *Ordinal Only* | `0x50FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2084 | `IsServerSideWindow` | `0x50FC0` | 29 | UnwindData |  |
| 1955 | `GetShellWindow` | `0x50FF0` | 88 | UnwindData |  |
| 2470 | `UpdateLayeredWindow` | `0x51180` | 102 | UnwindData |  |
| 1585 | `ClientThreadSetup` | `0x51290` | 1,216 | UnwindData |  |
| 1918 | `GetPointerFrameInfo` | `0x517B0` | 68 | UnwindData |  |
| 2036 | `InitializeLpkHooks` | `0x51800` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2528 | `IsThreadMessageQueueAttached` | `0x51A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1935 | `GetProcessDpiAwarenessInternal` | `0x51AA0` | 106 | UnwindData |  |
| 2312 | `SetCursor` | `0x51B70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2582 | *Ordinal Only* | `0x51BD0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2095 | `IsWindowRedirectedForPrint` | `0x51C50` | 37 | UnwindData |  |
| 1696 | `DispatchMessageA` | `0x51F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1520 | `BeginDeferWindowPos` | `0x51F30` | 49 | UnwindData |  |
| 2232 | `RealGetWindowClassW` | `0x51F70` | 68 | UnwindData |  |
| 2073 | `IsHungAppWindow` | `0x51FC0` | 37 | UnwindData |  |
| 2452 | `UnhookWindowsHookEx` | `0x51FF0` | 43 | UnwindData |  |
| 2288 | `SendDlgItemMessageW` | `0x52420` | 72 | UnwindData |  |
| 2636 | *Ordinal Only* | `0x52650` | 86 | UnwindData |  |
| 2573 | *Ordinal Only* | `0x526B0` | 51 | UnwindData |  |
| 2476 | `UserClientDllInitialize` | `0x526F0` | 49 | UnwindData |  |
| 1677 | `DeferWindowPos` | `0x52730` | 76 | UnwindData |  |
| 1780 | `FindWindowA` | `0x52790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2385 | `SetWinEventHook` | `0x527B0` | 233 | UnwindData |  |
| 1634 | `CtxInitUser32` | `0x528A0` | 74 | UnwindData |  |
| 2175 | `OpenClipboard` | `0x52AD0` | 51 | UnwindData |  |
| 1683 | `DestroyCursor` | `0x52C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1685 | `DestroyIcon` | `0x52C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1786 | `FrameRect` | `0x52C80` | 34 | UnwindData |  |
| 1718 | `DrawFocusRect` | `0x52CB0` | 78 | UnwindData |  |
| 1599 | `CopyImage` | `0x52F50` | 49 | UnwindData |  |
| 1594 | `ConsoleControl` | `0x52F90` | 183 | UnwindData |  |
| 2142 | `MapVirtualKeyExA` | `0x53090` | 157 | UnwindData |  |
| 1977 | `GetUserObjectInformationA` | `0x53140` | 275 | UnwindData |  |
| 1919 | `GetPointerFrameInfoHistory` | `0x53260` | 55 | UnwindData |  |
| 2471 | `UpdateLayeredWindowIndirect` | `0x53330` | 114 | UnwindData |  |
| 2072 | `IsGUIThread` | `0x533B0` | 81 | UnwindData |  |
| 1958 | `GetSysColorBrush` | `0x53410` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1975 | `GetUpdateRgn` | `0x53440` | 155 | UnwindData |  |
| 1871 | `GetKeyboardLayoutNameA` | `0x534F0` | 138 | UnwindData |  |
| 1566 | `CharToOemBuffA` | `0x537B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1681 | `DestroyAcceleratorTable` | `0x53800` | 147 | UnwindData |  |
| 1572 | `CharUpperW` | `0x53AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2176 | `OpenDesktopA` | `0x53AF0` | 116 | UnwindData |  |
| 2177 | `OpenDesktopW` | `0x53B70` | 85 | UnwindData |  |
| 1559 | `CharNextA` | `0x53D00` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1883 | `GetMenu` | `0x53EF0` | 109 | UnwindData |  |
| 2510 | *Ordinal Only* | `0x54060` | 32 | UnwindData |  |
| 2171 | `OemToCharBuffA` | `0x54090` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1860 | `GetIconInfoExW` | `0x540E0` | 287 | UnwindData |  |
| 2447 | `TranslateMDISysAccel` | `0x545F0` | 204 | UnwindData |  |
| 1826 | `GetCursorFrameInfo` | `0x548B0` | 72 | UnwindData |  |
| 1571 | `CharUpperBuffW` | `0x55720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2387 | `SetWindowCompositionAttribute` | `0x55740` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2120 | `LoadMenuW` | `0x55970` | 59 | UnwindData |  |
| 2112 | `LoadImageW` | `0x55A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1928 | `GetPointerPenInfo` | `0x55A40` | 76 | UnwindData |  |
| 1561 | `CharNextW` | `0x55AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1674 | `DefRawInputProc` | `0x55AC0` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2143 | `MapVirtualKeyExW` | `0x55E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1899 | `GetMessagePos` | `0x55E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2110 | `LoadIconW` | `0x55E40` | 35 | UnwindData |  |
| 1558 | `CharLowerW` | `0x55E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2105 | `LoadCursorA` | `0x55E90` | 97 | UnwindData |  |
| 2067 | `IsClipboardFormatAvailable` | `0x55F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2246 | `RegisterDeviceNotificationW` | `0x55F20` | 68 | UnwindData |  |
| 2597 | *Ordinal Only* | `0x56040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2587 | *Ordinal Only* | `0x56060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2033 | `InitDManipHook` | `0x56080` | 713 | UnwindData |  |
| 2344 | `SetMenuInfo` | `0x56350` | 67 | UnwindData |  |
| 2076 | `IsInDesktopWindowBand` | `0x56410` | 69 | UnwindData |  |
| 2256 | `RegisterPowerSettingNotification` | `0x564C0` | 118 | UnwindData |  |
| 1930 | `GetPointerTouchInfo` | `0x56540` | 76 | UnwindData |  |
| 2569 | *Ordinal Only* | `0x567A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1747 | `EndDeferWindowPos` | `0x567C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1762 | `EnumDisplaySettingsA` | `0x567E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1582 | `ChildWindowFromPoint` | `0x56800` | 78 | UnwindData |  |
| 2144 | `MapVirtualKeyW` | `0x56860` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2306 | `SetClassLongPtrW` | `0x56A80` | 263 | UnwindData |  |
| 2286 | `ScrollWindowEx` | `0x56B90` | 100 | UnwindData |  |
| 1819 | `GetClipboardFormatNameW` | `0x56C00` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2011 | `GetWindowTextLengthA` | `0x56CC0` | 33 | UnwindData |  |
| 1557 | `CharLowerBuffW` | `0x56E30` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2245 | `RegisterDeviceNotificationA` | `0x56EE0` | 70 | UnwindData |  |
| 2354 | `SetProcessDPIAware` | `0x56F30` | 5,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2357 | `SetProcessDpiAwarenessInternal` | `0x58320` | 87 | UnwindData |  |
| 1527 | `BroadcastSystemMessageExW` | `0x58380` | 40 | UnwindData |  |
| 1633 | `CsrBroadcastSystemMessageExW` | `0x583B0` | 220 | UnwindData |  |
| 1528 | `BroadcastSystemMessageW` | `0x584A0` | 36 | UnwindData |  |
| 2437 | `ToAscii` | `0x58720` | 157 | UnwindData |  |
| 2439 | `ToUnicode` | `0x587D0` | 67 | UnwindData |  |
| 2275 | `RemovePropA` | `0x58820` | 153 | UnwindData |  |
| 2019 | `HideCaret` | `0x588C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1604 | `CreateCaret` | `0x588E0` | 28 | UnwindData |  |
| 2321 | `SetDisplayConfig` | `0x58910` | 480 | UnwindData |  |
| 1781 | `FindWindowExA` | `0x596F0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2464 | `UnregisterPowerSettingNotification` | `0x597C0` | 65 | UnwindData |  |
| 1944 | `GetRawInputDeviceInfoW` | `0x59810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2619 | *Ordinal Only* | `0x59830` | 44 | UnwindData |  |
| 1931 | `GetPointerTouchInfoHistory` | `0x59890` | 69 | UnwindData |  |
| 2279 | `ReplyMessage` | `0x599A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1926 | `GetPointerInfoHistory` | `0x599C0` | 68 | UnwindData |  |
| 1874 | `GetKeyboardType` | `0x59A10` | 177 | UnwindData |  |
| 2418 | `ShutdownBlockReasonCreate` | `0x59B20` | 101 | UnwindData |  |
| 1821 | `GetClipboardSequenceNumber` | `0x59B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2577 | `mouse_event` | `0x59BB0` | 77 | UnwindData |  |
| 2410 | `ShowCaret` | `0x59D70` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1555 | `CharLowerA` | `0x59E90` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2269 | `ReleaseCapture` | `0x59F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2324 | `SetDlgItemTextW` | `0x59F20` | 42 | UnwindData |  |
| 2374 | `SetSystemCursor` | `0x59F50` | 89 | UnwindData |  |
| 2351 | `SetParent` | `0x5A120` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1553 | `DwmGetDxRgn` | `0x5A400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2313 | `SetCursorContents` | `0x5A400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2482 | `VRipOutput` | `0x5A400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2483 | `VTagOutput` | `0x5A400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2493 | `WINNLSGetIMEHotkey` | `0x5A400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1554 | *Ordinal Only* | `0x5A400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2459 | `UnregisterDeviceNotification` | `0x5A410` | 59 | UnwindData |  |
| 1746 | `EnableWindow` | `0x5A460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2551 | `ReportInertia` | `0x5A480` | 40 | UnwindData |  |
| 2438 | `ToAsciiEx` | `0x5A4B0` | 278 | UnwindData |  |
| 1616 | `CreateIcon` | `0x5A5D0` | 201 | UnwindData |  |
| 1605 | `CreateCursor` | `0x5A6A0` | 233 | UnwindData |  |
| 1610 | `CreateDesktopW` | `0x5AA60` | 44 | UnwindData |  |
| 1609 | `CreateDesktopExW` | `0x5AAA0` | 160 | UnwindData |  |
| 2287 | `SendDlgItemMessageA` | `0x5AC20` | 72 | UnwindData |  |
| 2494 | `WaitForInputIdle` | `0x5AC70` | 134 | UnwindData |  |
| 1814 | `GetClientRect` | `0x5B2B0` | 458 | UnwindData |  |
| 2302 | `SetCaretBlinkTime` | `0x5B480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2393 | `SetWindowLongPtrA` | `0x5B4A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2565 | *Ordinal Only* | `0x5B520` | 72 | UnwindData |  |
| 2303 | `SetCaretPos` | `0x5B570` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `CloseClipboard` | `0x5B940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2401 | `SetWindowTextA` | `0x5B960` | 40 | UnwindData |  |
| 2285 | `ScrollWindow` | `0x5C160` | 83 | UnwindData |  |
| 1515 | `AppendMenuA` | `0x5C1C0` | 139 | UnwindData |  |
| 2015 | `GetWindowWord` | `0x5C2D0` | 76 | UnwindData |  |
| 2345 | `SetMenuItemBitmaps` | `0x5C330` | 127 | UnwindData |  |
| 2713 | *Ordinal Only* | `0x5C3C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1820 | `GetClipboardOwner` | `0x5C3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2173 | `OemToCharW` | `0x5C400` | 84 | UnwindData |  |
| 1755 | `EnumClipboardFormats` | `0x5C460` | 41 | UnwindData |  |
| 2346 | `SetMenuItemInfoA` | `0x5C4F0` | 136 | UnwindData |  |
| 2102 | `LoadAcceleratorsW` | `0x5C580` | 47 | UnwindData |  |
| 1929 | `GetPointerPenInfoHistory` | `0x5CCA0` | 69 | UnwindData |  |
| 2141 | `MapVirtualKeyA` | `0x5CCF0` | 111 | UnwindData |  |
| 2172 | `OemToCharBuffW` | `0x5CEB0` | 74 | UnwindData |  |
| 2139 | `MapDialogRect` | `0x5CF00` | 186 | UnwindData |  |
| 2252 | `RegisterMessagePumpHook` | `0x5CFC0` | 286 | UnwindData |  |
| 1719 | `DrawFrame` | `0x5D380` | 309 | UnwindData |  |
| 2298 | `SendNotifyMessageA` | `0x5DA50` | 97 | UnwindData |  |
| 1758 | `EnumDesktopsW` | `0x5DC00` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2057 | `InvertRect` | `0x5DDC0` | 53 | UnwindData |  |
| 2377 | `SetThreadDesktop` | `0x5DE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1872 | `GetKeyboardLayoutNameW` | `0x5DE20` | 50 | UnwindData |  |
| 2488 | `VkKeyScanExW` | `0x5DE60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1523 | `BringWindowToTop` | `0x5DE80` | 48 | UnwindData |  |
| 1623 | `CreatePopupMenu` | `0x5E020` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2382 | `SetUserObjectInformationA` | `0x5E0A0` | 114 | UnwindData |  |
| 2002 | *Ordinal Only* | `0x5E120` | 163 | UnwindData |  |
| 1954 | `GetShellChangeNotifyWindow` | `0x5E1D0` | 70 | UnwindData |  |
| 1843 | `GetDlgItemTextW` | `0x5E290` | 65 | UnwindData |  |
| 2379 | `SetThreadDpiHostingBehavior` | `0x5E2E0` | 129 | UnwindData |  |
| 1548 | `ChangeWindowMessageFilter` | `0x5E370` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2486 | `VkKeyScanA` | `0x5E390` | 102 | UnwindData |  |
| 1632 | `CreateWindowStationW` | `0x5E400` | 85 | UnwindData |  |
| 2329 | `SetForegroundWindow` | `0x5E820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2485 | `ValidateRgn` | `0x5E840` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `AllowSetForegroundWindow` | `0x5EA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2049 | `InsertMenuItemA` | `0x5EA60` | 136 | UnwindData |  |
| 2337 | `SetMagnificationDesktopMagnification` | `0x5EBB0` | 110 | UnwindData |  |
| 1601 | `CountClipboardFormats` | `0x5EC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2158 | `MessageBoxW` | `0x5EC50` | 75 | UnwindData |  |
| 2157 | `MessageBoxTimeoutW` | `0x5ECB0` | 447 | UnwindData |  |
| 2154 | `MessageBoxIndirectA` | `0x5EE80` | 523 | UnwindData |  |
| 2266 | `RegisterUserApiHook` | `0x5F560` | 259 | UnwindData |  |
| 2284 | `ScrollDC` | `0x5F670` | 87 | UnwindData |  |
| 2261 | `RegisterSuspendResumeNotification` | `0x5FA10` | 110 | UnwindData |  |
| 1615 | `CreateDialogParamW` | `0x5FB00` | 141 | UnwindData |  |
| 2581 | *Ordinal Only* | `0x5FBA0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2194 | `PostQuitMessage` | `0x5FD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1682 | `DestroyCaret` | `0x5FD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2461 | `UnregisterMessagePumpHook` | `0x5FD40` | 201 | UnwindData |  |
| 1867 | `GetKeyNameTextW` | `0x5FE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1556 | `CharLowerBuffA` | `0x5FE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2109 | `LoadIconA` | `0x5FE50` | 97 | UnwindData |  |
| 1569 | `CharUpperA` | `0x5FFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2083 | `IsSETEnabled` | `0x60000` | 209 | UnwindData |  |
| 1639 | `DdeCmpStringHandles` | `0x603A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1989 | `GetWindowDpiHostingBehavior` | `0x603C0` | 97 | UnwindData |  |
| 2101 | `LoadAcceleratorsA` | `0x60880` | 47 | UnwindData |  |
| 2251 | `RegisterLogonProcess` | `0x608C0` | 28 | UnwindData |  |
| 2060 | `IsCharAlphaNumericW` | `0x60BC0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1768 | `EnumPropsExW` | `0x60D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1560 | `CharNextExA` | `0x60D30` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1630 | `CreateWindowIndirect` | `0x60F30` | 155 | UnwindData |  |
| 1504 | `ActivateKeyboardLayout` | `0x61580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1644 | `DdeCreateStringHandleW` | `0x615A0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2620 | *Ordinal Only* | `0x61670` | 54 | UnwindData |  |
| 2130 | `LookupIconIdFromDirectory` | `0x618B0` | 26 | UnwindData |  |
| 1622 | `CreateMenu` | `0x61ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1692 | `DialogBoxIndirectParamW` | `0x61EF0` | 30 | UnwindData |  |
| 1691 | `DialogBoxIndirectParamAorW` | `0x61F20` | 110 | UnwindData |  |
| 2001 | *Ordinal Only* | `0x61FA0` | 146 | UnwindData |  |
| 2427 | `SwitchDesktop` | `0x62090` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2202 | `PrivateRegisterICSProc` | `0x62240` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2466 | `UnregisterSuspendResumeNotification` | `0x62270` | 65 | UnwindData |  |
| 1784 | `FlashWindow` | `0x622F0` | 67 | UnwindData |  |
| 1596 | `CopyAcceleratorTableA` | `0x624B0` | 138 | UnwindData |  |
| 2048 | `InsertMenuA` | `0x62690` | 146 | UnwindData |  |
| 2400 | `SetWindowStationUser` | `0x62730` | 72 | UnwindData |  |
| 1564 | `CharPrevW` | `0x62850` | 1,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2339 | `SetMagnificationDesktopSamplingMode` | `0x62FD0` | 62 | UnwindData |  |
| 1834 | `GetDialogBaseUnits` | `0x63020` | 28 | UnwindData |  |
| 1562 | `CharPrevA` | `0x63050` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2071 | `IsDlgButtonChecked` | `0x63900` | 43 | UnwindData |  |
| 2323 | `SetDlgItemTextA` | `0x639C0` | 42 | UnwindData |  |
| 1570 | `CharUpperBuffA` | `0x639F0` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `EmptyClipboard` | `0x63CD0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2184 | `PackTouchHitTestingProximityEvaluation` | `0x63D80` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1575 | `CheckDlgButton` | `0x63DF0` | 52 | UnwindData |  |
| 2489 | `VkKeyScanW` | `0x63E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1972 | `GetTouchInputInfo` | `0x63E50` | 47 | UnwindData |  |
| 1921 | `GetPointerFramePenInfoHistory` | `0x63E90` | 57 | UnwindData |  |
| 2480 | `UserRealizePalette` | `0x63ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2121 | `LoadRemoteFonts` | `0x63EF0` | 42 | UnwindData |  |
| 2700 | *Ordinal Only* | `0x63F20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2063 | `IsCharLowerW` | `0x63F50` | 6,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1923 | `GetPointerFrameTouchInfo` | `0x65890` | 66 | UnwindData |  |
| 2061 | `IsCharAlphaW` | `0x65A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2535 | *Ordinal Only* | `0x65AA0` | 89 | UnwindData |  |
| 1772 | `EnumWindowStationsW` | `0x65B00` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `AddClipboardFormatListener` | `0x65BF0` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2515 | *Ordinal Only* | `0x65F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2260 | `RegisterShellHookWindow` | `0x65F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2429 | `SwitchToThisWindow` | `0x65F70` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2183 | `PackDDElParam` | `0x661A0` | 107 | UnwindData |  |
| 2052 | `InternalGetWindowIcon` | `0x662E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2562 | `keybd_event` | `0x66300` | 85 | UnwindData |  |
| 2059 | `IsCharAlphaNumericA` | `0x664E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1965 | `GetTaskmanWindow` | `0x66500` | 88 | UnwindData |  |
| 2372 | `SetSysColors` | `0x66560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2124 | `LockSetForegroundWindow` | `0x66580` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2265 | `RegisterTouchWindow` | `0x66830` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2281 | `ReuseDDElParam` | `0x66910` | 161 | UnwindData |  |
| 2428 | `SwitchDesktopWithFade` | `0x669C0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2341 | `SetMenu` | `0x66A80` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1999 | `GetWindowModuleFileNameW` | `0x66B00` | 62 | UnwindData |  |
| 2150 | `MessageBeep` | `0x66B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1694 | `DialogBoxParamW` | `0x66B70` | 142 | UnwindData |  |
| 1655 | `DdeInitializeW` | `0x66C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2561 | *Ordinal Only* | `0x66C30` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1787 | `FreeDDElParam` | `0x66F80` | 102 | UnwindData |  |
| 2272 | `RemoveClipboardFormatListener` | `0x67050` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1614 | `CreateDialogParamA` | `0x670F0` | 143 | UnwindData |  |
| 1580 | `CheckRadioButton` | `0x675E0` | 137 | UnwindData |  |
| 2058 | `IsCharAlphaA` | `0x67670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2568 | *Ordinal Only* | `0x67690` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2383 | `SetUserObjectInformationW` | `0x67AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2442 | `TrackPopupMenu` | `0x67AD0` | 38 | UnwindData |  |
| 2600 | *Ordinal Only* | `0x67B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2567 | *Ordinal Only* | `0x67B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1563 | `CharPrevExA` | `0x67B40` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1680 | `DeregisterShellHookWindow` | `0x67D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `CreateMDIWindowW` | `0x67DA0` | 110 | UnwindData |  |
| 1725 | `DrawStateA` | `0x67E90` | 430 | UnwindData |  |
| 1841 | `GetDlgItemInt` | `0x68050` | 375 | UnwindData |  |
| 1720 | `DrawFrameControl` | `0x684A0` | 171 | UnwindData |  |
| 1924 | `GetPointerFrameTouchInfoHistory` | `0x68820` | 57 | UnwindData |  |
| 2412 | `ShowOwnedPopups` | `0x68860` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1933 | `GetPriorityClipboardFormat` | `0x689A0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1699 | `DisplayConfigSetDeviceInfo` | `0x68B70` | 34 | UnwindData |  |
| 1920 | `GetPointerFramePenInfo` | `0x68BA0` | 66 | UnwindData |  |
| 2498 | `WinHelpW` | `0x68BF0` | 834 | UnwindData |  |
| 1700 | `DisplayExitWindowsWarnings` | `0x68F40` | 725 | UnwindData |  |
| 1723 | `DrawMenuBar` | `0x69220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2107 | `LoadCursorFromFileW` | `0x69240` | 79 | UnwindData |  |
| 2310 | `SetClipboardViewer` | `0x694B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2116 | `LoadLocalFonts` | `0x694D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1541 | `ChangeClipboardChain` | `0x694F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2065 | `IsCharUpperW` | `0x69510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2355 | `SetProcessDefaultLayout` | `0x69530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1907 | `GetOpenClipboardWindow` | `0x69550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2467 | `UnregisterTouchWindow` | `0x69570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2392 | `SetWindowLongA` | `0x69590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2376 | `SetTaskmanWindow` | `0x695B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2135 | `MITGetCursorUpdateHandle` | `0x695D0` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1642 | `DdeCreateDataHandle` | `0x69DD0` | 342 | UnwindData |  |
| 2564 | *Ordinal Only* | `0x6A0B0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2370 | `SetShellWindow` | `0x6A1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1822 | `GetClipboardViewer` | `0x6A1D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1976 | `GetUpdatedClipboardFormats` | `0x6A1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2369 | `SetShellChangeNotifyWindow` | `0x6A210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2249 | `RegisterGhostWindow` | `0x6A230` | 1,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2136 | `MITSetLastInputRecipient` | `0x6A7A0` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2456 | `UnpackDDElParam` | `0x6AD00` | 178 | UnwindData |  |
| 1736 | `DwmLockScreenUpdates` | `0x6ADC0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1693 | `DialogBoxParamA` | `0x6AF50` | 145 | UnwindData |  |
| 1953 | `GetSendMessageReceiver` | `0x6AFF0` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2037 | `InitializePointerDeviceInjection` | `0x6B580` | 63 | UnwindData |  |
| 2618 | *Ordinal Only* | `0x6B5D0` | 44 | UnwindData |  |
| 1778 | `ExitWindowsEx` | `0x6BF10` | 285 | UnwindData |  |
| 1796 | `GetAsyncKeyState` | `0x6D0D0` | 316 | UnwindData |  |
| 1949 | `GetScrollBarInfo` | `0x6D9B0` | 592 | UnwindData |  |
| 1991 | `GetWindowInfo` | `0x6E2C0` | 507 | UnwindData |  |
| 2006 | `GetWindowRgn` | `0x6E4D0` | 455 | UnwindData |  |
| 2007 | `GetWindowRgnBox` | `0x6E6A0` | 450 | UnwindData |  |
| 1790 | `GetAltTabInfo` | `0x6E870` | 29 | UnwindData |  |
| 1791 | `GetAltTabInfoA` | `0x6E870` | 29 | UnwindData |  |
| 1792 | `GetAltTabInfoW` | `0x6E870` | 29 | UnwindData |  |
| 1586 | `ClientToScreen` | `0x6E8A0` | 400 | UnwindData |  |
| 2282 | `ScreenToClient` | `0x6EA40` | 400 | UnwindData |  |
| 1661 | `DdeQueryStringA` | `0x6F900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1745 | `EnableSessionForMMCSS` | `0x6F920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1695 | `DisableProcessWindowsGhosting` | `0x6F940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2307 | `SetClassLongW` | `0x6F960` | 2,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1766 | `EnumPropsA` | `0x70220` | 1,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1757 | `EnumDesktopsA` | `0x70880` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1934 | `GetProcessDefaultLayout` | `0x71330` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2426 | `SwapMouseButton` | `0x71BE0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2153 | `MessageBoxExW` | `0x71C50` | 30 | UnwindData |  |
| 1567 | `CharToOemBuffW` | `0x71D20` | 88 | UnwindData |  |
| 2064 | `IsCharUpperA` | `0x71D80` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2348 | `SetMessageExtraInfo` | `0x71EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2062 | `IsCharLowerA` | `0x71EC0` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2509 | *Ordinal Only* | `0x72260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2588 | *Ordinal Only* | `0x72270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1506 | `AddVisualIdentifier` | `0x72280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2681 | `ApplyWindowAction` | `0x72290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `AttachThreadInput` | `0x722A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2616 | *Ordinal Only* | `0x722B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1521 | `BeginPaint` | `0x722C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `BlockInput` | `0x722D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2708 | *Ordinal Only* | `0x722E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1530 | `CalcMenuBar` | `0x722F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `CalculatePopupWindowPosition` | `0x72300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2533 | *Ordinal Only* | `0x72310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1549 | `ChangeWindowMessageFilterEx` | `0x72320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `CheckProcessForClipboardAccess` | `0x72330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1579 | `CheckProcessSession` | `0x72340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `CheckWindowThreadDesktop` | `0x72350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1583 | `ChildWindowFromPointEx` | `0x72360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2563 | *Ordinal Only* | `0x72370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1587 | `ClipCursor` | `0x72380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1589 | `CloseDesktop` | `0x72390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1593 | `CloseWindowStation` | `0x723A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2550 | *Ordinal Only* | `0x723B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2610 | *Ordinal Only* | `0x723C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2647 | *Ordinal Only* | `0x723D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2638 | *Ordinal Only* | `0x723E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2621 | *Ordinal Only* | `0x723F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `ControlMagnification` | `0x72400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2675 | `ConvertToInterceptWindow` | `0x72410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1597 | `CopyAcceleratorTableW` | `0x72420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1603 | `CreateAcceleratorTableW` | `0x72430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2633 | *Ordinal Only* | `0x72440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1606 | `CreateDCompositionHwndTarget` | `0x72450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2817 | `CreateLayoutSyncForHwnd` | `0x72460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2644 | *Ordinal Only* | `0x72470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2516 | *Ordinal Only* | `0x72480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2503 | `DelegateInput` | `0x72490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1679 | `DeleteMenu` | `0x724A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2648 | *Ordinal Only* | `0x724B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1684 | `DestroyDCompositionHwndTarget` | `0x724C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1686 | `DestroyMenu` | `0x724D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1688 | `DestroySyntheticPointerDevice` | `0x724E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2273 | `RemoveInjectionDevice` | `0x724E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1689 | `DestroyWindow` | `0x724F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2529 | *Ordinal Only* | `0x72500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1709 | `DoSoundConnect` | `0x72510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1710 | `DoSoundDisconnect` | `0x72520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2651 | *Ordinal Only* | `0x72530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1711 | `DragDetect` | `0x72540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1712 | `DragObject` | `0x72550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2613 | *Ordinal Only* | `0x72560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2670 | *Ordinal Only* | `0x72570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1713 | `DrawAnimatedRects` | `0x72580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1732 | `DwmGetRemoteSessionOcclusionEvent` | `0x72590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1733 | `DwmGetRemoteSessionOcclusionState` | `0x725A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1734 | `DwmKernelShutdown` | `0x725B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1735 | `DwmKernelStartup` | `0x725C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `DwmValidateWindow` | `0x725D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2680 | `DwmWindowNotificationsEnabled` | `0x725E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2704 | *Ordinal Only* | `0x725F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1741 | `EnableMouseInPointer` | `0x72600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2656 | *Ordinal Only* | `0x72610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2519 | *Ordinal Only* | `0x72620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1742 | `EnableNonClientDpiScaling` | `0x72630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1743 | `EnableOneCoreTransformMode` | `0x72640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2615 | *Ordinal Only* | `0x72650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2606 | *Ordinal Only* | `0x72660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2818 | `EnableSynchronizedLayout` | `0x72670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2544 | *Ordinal Only* | `0x72680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2709 | *Ordinal Only* | `0x72690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2611 | *Ordinal Only* | `0x726A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2804 | `EnableWindowShellWindowManagementBehavior` | `0x726B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1748 | `EndDeferWindowPosEx` | `0x726C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1750 | `EndMenu` | `0x726D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1751 | `EndPaint` | `0x726E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2686 | `EnterMoveSizeLoop` | `0x726F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1761 | `EnumDisplayMonitors` | `0x72700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1777 | `ExcludeUpdateRgn` | `0x72710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1785 | `FlashWindowEx` | `0x72720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2642 | *Ordinal Only* | `0x72730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1788 | `FrostCrashedWindow` | `0x72740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2711 | *Ordinal Only* | `0x72750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1793 | `GetAncestor` | `0x72760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1797 | `GetAutoRotationState` | `0x72770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1799 | `GetCIMSSM` | `0x72780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1801 | `GetCaretBlinkTime` | `0x72790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1802 | `GetCaretPos` | `0x727A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1815 | `GetClipCursor` | `0x727B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1816 | `GetClipboardAccessToken` | `0x727C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2668 | `GetClipboardMetadata` | `0x727D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1823 | `GetComboBoxInfo` | `0x727E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1824 | `GetCurrentInputMessageSource` | `0x727F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1825 | `GetCursor` | `0x72800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1827 | `GetCursorInfo` | `0x72810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1830 | `GetDCEx` | `0x72820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1831 | `GetDCompositionHwndBitmap` | `0x72830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1832 | `GetDesktopID` | `0x72840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1837 | `GetDisplayAutoRotationPreferences` | `0x72850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2512 | *Ordinal Only* | `0x72860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1844 | `GetDoubleClickTime` | `0x72870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1850 | `GetExtendedPointerDeviceProperty` | `0x72880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1853 | `GetGUIThreadInfo` | `0x72890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1854 | `GetGestureConfig` | `0x728A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1857 | `GetGuiResources` | `0x728B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2650 | *Ordinal Only* | `0x728C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1862 | `GetInputLocaleInfo` | `0x728D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2590 | *Ordinal Only* | `0x728E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2589 | *Ordinal Only* | `0x728F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2609 | *Ordinal Only* | `0x72900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1870 | `GetKeyboardLayoutList` | `0x72910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1873 | `GetKeyboardState` | `0x72920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1877 | `GetLayeredWindowAttributes` | `0x72930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1878 | `GetListBoxInfo` | `0x72940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1882 | `GetMagnificationLensCtxInformation` | `0x72950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1884 | `GetMenuBarInfo` | `0x72960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1893 | `GetMenuItemRect` | `0x72970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1904 | `GetMouseMovePointsEx` | `0x72980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2559 | *Ordinal Only* | `0x72990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2545 | *Ordinal Only* | `0x729A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1910 | `GetPointerCursorId` | `0x729B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1911 | `GetPointerDevice` | `0x729C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1912 | `GetPointerDeviceCursors` | `0x729D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1913 | `GetPointerDeviceInputSpace` | `0x729E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1914 | `GetPointerDeviceOrientation` | `0x729F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1915 | `GetPointerDeviceProperties` | `0x72A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1916 | `GetPointerDeviceRects` | `0x72A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1917 | `GetPointerDevices` | `0x72A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1922 | `GetPointerFrameTimes` | `0x72A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1927 | `GetPointerInputTransform` | `0x72A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2653 | *Ordinal Only* | `0x72A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1932 | `GetPointerType` | `0x72A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2521 | `GetProcessUIContextInformation` | `0x72A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1936 | `GetProcessWindowStation` | `0x72A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2541 | *Ordinal Only* | `0x72A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1942 | `GetRawInputData` | `0x72AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1945 | `GetRawInputDeviceList` | `0x72AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1946 | `GetRawPointerDeviceData` | `0x72AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1948 | `GetRegisteredRawInputDevices` | `0x72AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2614 | *Ordinal Only* | `0x72AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1959 | `GetSystemDpiForProcess` | `0x72AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1960 | `GetSystemMenu` | `0x72B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1966 | `GetThreadDesktop` | `0x72B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1969 | `GetTitleBarInfo` | `0x72B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1970 | `GetTopLevelWindow` | `0x72B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2517 | *Ordinal Only* | `0x72B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2652 | *Ordinal Only* | `0x72B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1978 | `GetUserObjectInformationW` | `0x72B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1984 | `GetWindowCompositionInfo` | `0x72B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1986 | `GetWindowDC` | `0x72B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1987 | `GetWindowDisplayAffinity` | `0x72B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1990 | `GetWindowFeedbackSetting` | `0x72BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1996 | `GetWindowMinimizeRect` | `0x72BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2000 | `GetWindowPlacement` | `0x72BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2008 | `GetWindowRgnEx` | `0x72BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2016 | `GhostWindowFromHungWindow` | `0x72BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2505 | `HandleDelegatedInput` | `0x72BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2539 | *Ordinal Only* | `0x72C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2020 | `HiliteMenuItem` | `0x72C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2021 | `HungWindowFromGhostWindow` | `0x72C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2028 | `ImpersonateDdeClientWindow` | `0x72C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2032 | `InheritWindowMonitor` | `0x72C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2612 | *Ordinal Only* | `0x72C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2669 | *Ordinal Only* | `0x72C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2034 | `InitializeGenericHidInjection` | `0x72C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2035 | `InitializeInputDeviceInjection` | `0x72C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2039 | `InitializeTouchInjection` | `0x72C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2040 | `InjectDeviceInput` | `0x72CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2041 | `InjectGenericHidInput` | `0x72CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2042 | `InjectKeyboardInput` | `0x72CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2043 | `InjectMouseInput` | `0x72CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2044 | `InjectPointerInput` | `0x72CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2045 | `InjectSyntheticPointerInput` | `0x72CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2046 | `InjectTouchInput` | `0x72CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2803 | `InjectTouchpadAction` | `0x72D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2047 | `InputSpaceRegionFromPoint` | `0x72D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2593 | *Ordinal Only* | `0x72D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2055 | `InvalidateRect` | `0x72D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2056 | `InvalidateRgn` | `0x72D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2705 | *Ordinal Only* | `0x72D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2676 | `IsInterceptWindow` | `0x72D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2078 | `IsMouseInPointerEnabled` | `0x72D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2520 | *Ordinal Only* | `0x72D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2703 | *Ordinal Only* | `0x72D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2080 | `IsOneCoreTransformMode` | `0x72DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2617 | *Ordinal Only* | `0x72DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2087 | `IsTopLevelWindow` | `0x72DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2088 | `IsTouchWindow` | `0x72DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2706 | *Ordinal Only* | `0x72DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2685 | `IsWindowDisplayChangeSuppressed` | `0x72DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2710 | *Ordinal Only* | `0x72E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2100 | `KillTimer` | `0x72E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2538 | *Ordinal Only* | `0x72E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2125 | `LockWindowStation` | `0x72E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2126 | `LockWindowUpdate` | `0x72E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2127 | `LockWorkStation` | `0x72E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2715 | *Ordinal Only* | `0x72E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2128 | `LogicalToPhysicalPoint` | `0x72E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2129 | `LogicalToPhysicalPointForPerMonitorDPI` | `0x72E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2140 | `MapPointsByVisualIdentifier` | `0x72E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2145 | `MapVisualRelativePoints` | `0x72EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2147 | `MenuItemFromPoint` | `0x72EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2164 | `MoveWindow` | `0x72EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2578 | *Ordinal Only* | `0x72ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2179 | `OpenInputDesktop` | `0x72EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2180 | `OpenThreadDesktop` | `0x72EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2186 | `PaintMenuBar` | `0x72F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2187 | `PaintMonitor` | `0x72F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2716 | *Ordinal Only* | `0x72F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2190 | `PhysicalToLogicalPoint` | `0x72F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2191 | `PhysicalToLogicalPointForPerMonitorDPI` | `0x72F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2197 | `PrintWindow` | `0x72F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2608 | *Ordinal Only* | `0x72F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2508 | *Ordinal Only* | `0x72F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2204 | `QueryBSDRWindow` | `0x72F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2206 | `QuerySendMessage` | `0x72F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2207 | `RIMAddInputObserver` | `0x72FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2208 | `RIMAreSiblingDevices` | `0x72FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2209 | `RIMDeviceIoControl` | `0x72FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2210 | `RIMEnableMonitorMappingForDevice` | `0x72FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2211 | `RIMFreeInputBuffer` | `0x72FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2212 | `RIMGetDevicePreparsedData` | `0x72FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2213 | `RIMGetDevicePreparsedDataLockfree` | `0x73000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2214 | `RIMGetDeviceProperties` | `0x73010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2215 | `RIMGetDevicePropertiesLockfree` | `0x73020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2216 | `RIMGetPhysicalDeviceRect` | `0x73030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2217 | `RIMGetSourceProcessId` | `0x73040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2218 | `RIMObserveNextInput` | `0x73050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2663 | `RIMOnAsyncPnpWorkNotification` | `0x73060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2219 | `RIMOnPnpNotification` | `0x73070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2220 | `RIMOnTimerNotification` | `0x73080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2221 | `RIMQueryDevicePath` | `0x73090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2222 | `RIMReadInput` | `0x730A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2662 | `RIMRegisterForInputEx` | `0x730B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2224 | `RIMRemoveInputObserver` | `0x730C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2225 | `RIMSetExtendedDeviceProperty` | `0x730D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2226 | `RIMSetTestModeStatus` | `0x730E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2227 | `RIMUnregisterForInput` | `0x730F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2228 | `RIMUpdateInputObserverRegistration` | `0x73100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2687 | `RaiseLowerShellWindow` | `0x73110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2229 | `RealChildWindowFromPoint` | `0x73120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2236 | `RedrawWindow` | `0x73130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2237 | `RegisterBSDRWindow` | `0x73140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2682 | `RegisterCloakedNotification` | `0x73150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2244 | `RegisterDManipHook` | `0x73160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2247 | `RegisterErrorReportingDialog` | `0x73170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2667 | `RegisterForCustomDockTargets` | `0x73180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2666 | `RegisterForTooltipDismissNotification` | `0x73190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2250 | `RegisterHotKey` | `0x731A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2253 | `RegisterPointerDeviceNotifications` | `0x731B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2257 | `RegisterRawInputDevices` | `0x731C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2258 | `RegisterServicesProcess` | `0x731D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2259 | `RegisterSessionPort` | `0x731E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2263 | `RegisterTasklist` | `0x731F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2264 | `RegisterTouchHitTestingWindow` | `0x73200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2688 | `RegisterTouchpadCapableThread` | `0x73210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2546 | *Ordinal Only* | `0x73210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2689 | `RegisterTouchpadCapableWindow` | `0x73220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2271 | `ReleaseDwmHitTestWaiters` | `0x73230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2274 | `RemoveMenu` | `0x73240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2278 | `RemoveVisualIdentifier` | `0x73250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2280 | `ResolveDesktopForWOW` | `0x73260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2643 | *Ordinal Only* | `0x73270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2537 | *Ordinal Only* | `0x73280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2291 | `SendInput` | `0x73290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2591 | *Ordinal Only* | `0x732A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2556 | *Ordinal Only* | `0x732B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2513 | *Ordinal Only* | `0x732C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2300 | `SetActiveWindow` | `0x732D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2665 | `SetAdditionalForegroundBoostProcesses` | `0x732E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2805 | *Ordinal Only* | `0x732F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2507 | *Ordinal Only* | `0x73300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2627 | *Ordinal Only* | `0x73310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2522 | *Ordinal Only* | `0x73320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2531 | *Ordinal Only* | `0x73330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2301 | `SetCapture` | `0x73340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2005 | *Ordinal Only* | `0x73350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2308 | `SetClassWord` | `0x73360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2311 | `SetCoalescableTimer` | `0x73370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2571 | `SetCoreWindow` | `0x73380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2576 | *Ordinal Only* | `0x73390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2542 | `SetCoveredWindowStates` | `0x733A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2639 | *Ordinal Only* | `0x733B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2314 | `SetCursorPos` | `0x733C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2352 | `SetPhysicalCursorPos` | `0x733C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2317 | `SetDesktopColorTransform` | `0x733D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2658 | *Ordinal Only* | `0x733E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2318 | `SetDialogControlDpiChangeBehavior` | `0x733F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2320 | `SetDisplayAutoRotationPreferences` | `0x73400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2532 | *Ordinal Only* | `0x73410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2661 | *Ordinal Only* | `0x73420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2326 | `SetFeatureReportResponse` | `0x73430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2327 | `SetFocus` | `0x73440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2328 | `SetForegroundRedirectionForActivationObject` | `0x73450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2649 | *Ordinal Only* | `0x73460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2330 | `SetFullscreenMagnifierOffsetsDWMUpdated` | `0x73470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2331 | `SetGestureConfig` | `0x73480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2586 | *Ordinal Only* | `0x73490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2592 | *Ordinal Only* | `0x734A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2594 | *Ordinal Only* | `0x734B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2332 | `SetInternalWindowPos` | `0x734C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2333 | `SetKeyboardState` | `0x734D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2335 | `SetLayeredWindowAttributes` | `0x734E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2338 | `SetMagnificationDesktopMagnifierOffsetsDWMUpdated` | `0x734F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2340 | `SetMagnificationLensCtxInformation` | `0x73500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2342 | `SetMenuContextHelpId` | `0x73510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2343 | `SetMenuDefaultItem` | `0x73520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2350 | `SetMirrorRendering` | `0x73530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2353 | `SetPointerDeviceInputSpace` | `0x73540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2595 | *Ordinal Only* | `0x73550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2358 | `SetProcessLaunchForegroundPolicy` | `0x73560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2657 | *Ordinal Only* | `0x73570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2359 | `SetProcessRestrictionExemption` | `0x73580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2360 | `SetProcessWindowStation` | `0x73590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2637 | *Ordinal Only* | `0x735A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2371 | `SetShellWindowEx` | `0x735B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2375 | `SetSystemMenu` | `0x735C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2622 | *Ordinal Only* | `0x735D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2380 | `SetThreadInputBlocked` | `0x735E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2672 | `SetUserObjectCapability` | `0x735F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2386 | `SetWindowBand` | `0x73600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2388 | `SetWindowCompositionTransition` | `0x73610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2390 | `SetWindowDisplayAffinity` | `0x73620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2391 | `SetWindowFeedbackSetting` | `0x73630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2673 | `SetWindowMessageCapability` | `0x73640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2396 | `SetWindowPlacement` | `0x73650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2397 | `SetWindowPos` | `0x73660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2579 | *Ordinal Only* | `0x73670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2403 | `SetWindowWord` | `0x73680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2674 | `ShellForegroundBoostProcess` | `0x73690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2800 | `ShellHandwritingDelegateInput` | `0x736A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2802 | `ShellHandwritingHandleDelegatedInput` | `0x736B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2801 | `ShellHandwritingUndelegateInput` | `0x736C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2664 | `ShellMigrateWindow` | `0x736D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2671 | `ShellRegisterHotKey` | `0x736E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2409 | `ShellSetWindowPos` | `0x736F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2411 | `ShowCursor` | `0x73700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2415 | `ShowSystemCursor` | `0x73710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2416 | `ShowWindow` | `0x73720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2417 | `ShowWindowAsync` | `0x73730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2419 | `ShutdownBlockReasonDestroy` | `0x73740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2420 | `ShutdownBlockReasonQuery` | `0x73750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2421 | `SignalRedirectionStartComplete` | `0x73760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2422 | `SkipPointerFrameMessages` | `0x73770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2010 | *Ordinal Only* | `0x73780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2424 | `SoundSentry` | `0x73790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2684 | `SuppressWindowDisplayChange` | `0x737A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2441 | `TrackMouseEvent` | `0x737B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2443 | `TrackPopupMenuEx` | `0x737C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2504 | `UndelegateInput` | `0x737D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2450 | `UnhookWinEvent` | `0x737E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2455 | `UnlockWindowStation` | `0x737F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2460 | `UnregisterHotKey` | `0x73800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2465 | `UnregisterSessionPort` | `0x73810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2468 | `UnregisterUserApiHook` | `0x73820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2469 | `UpdateDefaultDesktopThumbnail` | `0x73830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2474 | `UpdateWindowInputSinkHints` | `0x73840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2585 | *Ordinal Only* | `0x73850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2477 | `UserHandleGrantAccess` | `0x73860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2484 | `ValidateRect` | `0x73870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2530 | *Ordinal Only* | `0x73880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2495 | `WaitForRedirectionStartComplete` | `0x73890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2496 | `WaitMessage` | `0x738A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2499 | `WindowFromDC` | `0x738B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2500 | `WindowFromPhysicalPoint` | `0x738C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2501 | `WindowFromPoint` | `0x738D0` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1584 | `CliImmSetHotKey` | `0x74430` | 152 | UnwindData |  |
| 2106 | `LoadCursorFromFileA` | `0x74B50` | 126 | UnwindData |  |
| 2714 | *Ordinal Only* | `0x74CB0` | 43 | UnwindData |  |
| 1767 | `EnumPropsExA` | `0x75860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1769 | `EnumPropsW` | `0x75880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1771 | `EnumWindowStationsA` | `0x758A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2526 | *Ordinal Only* | `0x758C0` | 39 | UnwindData |  |
| 2524 | *Ordinal Only* | `0x758F0` | 39 | UnwindData |  |
| 1855 | `GetGestureExtraArgs` | `0x75920` | 29 | UnwindData |  |
| 2404 | `SetWindowsHookA` | `0x75950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2408 | `SetWindowsHookW` | `0x75970` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2117 | `LoadMenuA` | `0x75DB0` | 59 | UnwindData |  |
| 1573 | `CheckBannedOneCoreTransformApi` | `0x75E00` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2315 | `SetDebugErrorLevel` | `0x75E00` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2659 | *Ordinal Only* | `0x75E00` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2815 | *Ordinal Only* | `0x76180` | 114 | UnwindData |  |
| 2098 | `IsWow64Message` | `0x76200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2148 | `MenuWindowProcA` | `0x76220` | 118 | UnwindData |  |
| 2149 | `MenuWindowProcW` | `0x762A0` | 115 | UnwindData |  |
| 1503 | `GetPointerFrameArrivalTimes` | `0x76460` | 29 | UnwindData |  |
| 2255 | `RegisterPointerInputTargetEx` | `0x76460` | 29 | UnwindData |  |
| 2463 | `UnregisterPointerInputTargetEx` | `0x76460` | 29 | UnwindData |  |
| 2548 | *Ordinal Only* | `0x76490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2549 | *Ordinal Only* | `0x764B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2693 | `GetPointerFrameTouchpadInfo` | `0x764D0` | 66 | UnwindData |  |
| 2694 | `GetPointerFrameTouchpadInfoHistory` | `0x76520` | 57 | UnwindData |  |
| 2691 | `GetPointerTouchpadInfo` | `0x76560` | 76 | UnwindData |  |
| 2692 | `GetPointerTouchpadInfoHistory` | `0x765C0` | 69 | UnwindData |  |
| 2514 | *Ordinal Only* | `0x76610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2254 | `RegisterPointerInputTarget` | `0x76630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2695 | `ReportWindowContentInertia` | `0x76650` | 100 | UnwindData |  |
| 2462 | `UnregisterPointerInputTarget` | `0x766C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1864 | `GetInternalWindowPos` | `0x766E0` | 160 | UnwindData |  |
| 2079 | `SetThreadCursorCreationScaling` | `0x76810` | 74 | UnwindData |  |
| 1602 | `CreateAcceleratorTableA` | `0x76860` | 130 | UnwindData |  |
| 1617 | `CreateIconFromResource` | `0x768F0` | 33 | UnwindData |  |
| 1690 | `DialogBoxIndirectParamA` | `0x76920` | 33 | UnwindData |  |
| 2598 | *Ordinal Only* | `0x76950` | 30 | UnwindData |  |
| 1859 | `GetIconInfoExA` | `0x76980` | 352 | UnwindData |  |
| 1702 | `DlgDirListComboBoxA` | `0x77E50` | 233 | UnwindData |  |
| 1703 | `DlgDirListComboBoxW` | `0x77F40` | 85 | UnwindData |  |
| 1705 | `DlgDirSelectComboBoxExA` | `0x77FA0` | 165 | UnwindData |  |
| 1706 | `DlgDirSelectComboBoxExW` | `0x78050` | 128 | UnwindData |  |
| 1640 | `DdeConnect` | `0x78C60` | 270 | UnwindData |  |
| 1641 | `DdeConnectList` | `0x78D80` | 745 | UnwindData |  |
| 1646 | `DdeDisconnectList` | `0x79070` | 281 | UnwindData |  |
| 1652 | `DdeGetQualityOfService` | `0x79190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1664 | `DdeSetQualityOfService` | `0x79190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2349 | `SetMessageQueue` | `0x79190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1663 | `DdeReconnect` | `0x791A0` | 448 | UnwindData |  |
| 1538 | `CancelShutdown` | `0x793B0` | 105 | UnwindData |  |
| 1752 | `EndTask` | `0x79420` | 199 | UnwindData |  |
| 1963 | `GetTabbedTextExtentA` | `0x794F0` | 255 | UnwindData |  |
| 2478 | `UserLpkPSMTextOut` | `0x79600` | 602 | UnwindData |  |
| 2479 | `UserLpkTabbedTextOut` | `0x79860` | 648 | UnwindData |  |
| 1651 | `DdeGetLastError` | `0x79AF0` | 83 | UnwindData |  |
| 1653 | `DdeImpersonateClient` | `0x79B50` | 142 | UnwindData |  |
| 1654 | `DdeInitializeA` | `0x79BF0` | 3,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1835 | `GetDialogControlDpiChangeBehavior` | `0x7A850` | 32 | UnwindData |  |
| 1836 | `GetDialogDpiChangeBehavior` | `0x7A880` | 66 | UnwindData |  |
| 2322 | `SetDlgItemInt` | `0x7A8D0` | 187 | UnwindData |  |
| 1905 | `GetNextDlgGroupItem` | `0x7A9A0` | 122 | UnwindData |  |
| 1845 | `GetDpiAwarenessContextForProcess` | `0x7AA20` | 24 | UnwindData |  |
| 1849 | `GetDpiFromDpiAwarenessContext` | `0x7AA40` | 29 | UnwindData |  |
| 1968 | `GetThreadDpiHostingBehavior` | `0x7AA70` | 63 | UnwindData |  |
| 2811 | `ConvertPrimaryPointerToMouseDrag` | `0x7B080` | 127 | UnwindData |  |
| 2813 | *Ordinal Only* | `0x7B110` | 127 | UnwindData |  |
| 2809 | *Ordinal Only* | `0x7B1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2810 | *Ordinal Only* | `0x7B1B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2812 | *Ordinal Only* | `0x7B1C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2808 | *Ordinal Only* | `0x7B1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2816 | *Ordinal Only* | `0x7B1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2819 | *Ordinal Only* | `0x7B1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2814 | *Ordinal Only* | `0x7B200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2806 | `SetMaxTouchpadSensitivity` | `0x7B210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2807 | *Ordinal Only* | `0x7B220` | 19,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2198 | `PrivateExtractIconExA` | `0x80020` | 135 | UnwindData |  |
| 2200 | `PrivateExtractIconsA` | `0x800B0` | 175 | UnwindData |  |
| 1636 | `DdeAccessData` | `0x80710` | 180 | UnwindData |  |
| 1637 | `DdeAddData` | `0x807D0` | 428 | UnwindData |  |
| 1648 | `DdeFreeDataHandle` | `0x80990` | 118 | UnwindData |  |
| 1666 | `DdeUnaccessData` | `0x80A10` | 107 | UnwindData |  |
| 2497 | `WinHelpA` | `0x80F00` | 1,162 | UnwindData |  |
| 1643 | `DdeCreateStringHandleA` | `0x81460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1656 | `DdeKeepStringHandle` | `0x81480` | 189 | UnwindData |  |
| 1662 | `DdeQueryStringW` | `0x81550` | 42,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1701 | `DlgDirListA` | `0x8BA80` | 236 | UnwindData |  |
| 1704 | `DlgDirListW` | `0x8BB80` | 88 | UnwindData |  |
| 1707 | `DlgDirSelectExA` | `0x8BBE0` | 171 | UnwindData |  |
| 1708 | `DlgDirSelectExW` | `0x8BCA0` | 47 | UnwindData |  |
| 1879 | `GetMagnificationDesktopColorEffect` | `0x8C020` | 220 | UnwindData |  |
| 1880 | `GetMagnificationDesktopMagnification` | `0x8C110` | 139 | UnwindData |  |
| 1881 | `GetMagnificationDesktopSamplingMode` | `0x8C1B0` | 76 | UnwindData |  |
| 2336 | `SetMagnificationDesktopColorEffect` | `0x8C210` | 206 | UnwindData |  |
| 1540 | `CascadeWindows` | `0x8D2D0` | 37 | UnwindData |  |
| 2283 | `ScrollChildren` | `0x8D300` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2436 | `TileWindows` | `0x8D330` | 37 | UnwindData |  |
| 1546 | `ChangeMenuA` | `0x8D360` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1547 | `ChangeMenuW` | `0x8D410` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1724 | `DrawMenuBarTemp` | `0x8D4C0` | 130 | UnwindData |  |
| 1885 | `GetMenuCheckMarkDimensions` | `0x8D550` | 58 | UnwindData |  |
| 1886 | `GetMenuContextHelpId` | `0x8D590` | 25 | UnwindData |  |
| 2134 | `MB_GetString` | `0x8EB90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2151 | `MessageBoxA` | `0x8EBC0` | 75 | UnwindData |  |
| 2152 | `MessageBoxExA` | `0x8EC20` | 30 | UnwindData |  |
| 2155 | `MessageBoxIndirectW` | `0x8EC50` | 174 | UnwindData |  |
| 2156 | `MessageBoxTimeoutA` | `0x8ED10` | 333 | UnwindData |  |
| 1714 | `DrawCaption` | `0x8F050` | 171 | UnwindData |  |
| 2185 | `PaintDesktop` | `0x8F150` | 622 | UnwindData |  |
| 2399 | `SetWindowRgnEx` | `0x8F3D0` | 60 | UnwindData |  |
| 1568 | `CharToOemW` | `0x8F420` | 99 | UnwindData |  |
| 2169 | `OemKeyScan` | `0x8F490` | 132 | UnwindData |  |
| 2334 | `SetLastErrorEx` | `0x8F520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2373 | `SetSysColorsTemp` | `0x8F540` | 385 | UnwindData |  |
| 1753 | `EnterReaderModeHelper` | `0x8F9B0` | 119 | UnwindData |  |
| 2233 | `ReasonCodeNeedsBugID` | `0x8FD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2234 | `ReasonCodeNeedsComment` | `0x8FD30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1552 | *Ordinal Only* | `0x8FD40` | 69 | UnwindData |  |
| 1550 | *Ordinal Only* | `0x8FD90` | 129 | UnwindData |  |
| 1551 | *Ordinal Only* | `0x8FE20` | 41 | UnwindData |  |
| 1624 | `CreateSyntheticPointerDevice` | `0x8FE50` | 78 | UnwindData |  |
| 2690 | `CreateSyntheticPointerDevice2` | `0x8FEB0` | 49 | UnwindData |  |
| 2038 | `InitializePointerDeviceInjectionEx` | `0x8FEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2223 | `RIMRegisterForInput` | `0x8FF10` | 34 | UnwindData |  |
| 2137 | `MITSynthesizeTouchInput` | `0x8FF40` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1951 | `GetScrollPos` | `0x90180` | 831 | UnwindData |  |
| 1952 | `GetScrollRange` | `0x904D0` | 916 | UnwindData |  |
| 2367 | `SetScrollPos` | `0x908C0` | 177 | UnwindData |  |
| 2368 | `SetScrollRange` | `0x90980` | 346 | UnwindData |  |
| 2413 | `ShowScrollBar` | `0x90AE0` | 487 | UnwindData |  |
| 2511 | *Ordinal Only* | `0x96200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2566 | *Ordinal Only* | `0x96220` | 74 | UnwindData |  |
| 1775 | `EvaluateProximityToPolygon` | `0x97F30` | 1,393 | UnwindData |  |
| 2502 | `_UserTestTokenForInteractive` | `0x98540` | 223 | UnwindData |  |
| 2086 | `IsThreadTSFEventAware` | `0x986C0` | 114 | UnwindData |  |
| 2138 | `MakeThreadTSFEventAware` | `0x98740` | 90 | UnwindData |  |
| 2277 | `RemoveThreadTSFEventAwareness` | `0x987A0` | 75 | UnwindData |  |
| 1514 | `AnyPopup` | `0x98800` | 64 | UnwindData |  |
| 1852 | `GetForegroundWindow` | `0x98850` | 133 | UnwindData |  |
| 2003 | `GetWindowProcessHandle` | `0x988E0` | 89 | UnwindData |  |
| 2540 | *Ordinal Only* | `0x98940` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1635 | `DdeAbandonTransaction` | `0x98B70` | 235 | UnwindData |  |
| 1659 | `DdeQueryConvInfo` | `0x98C70` | 548 | UnwindData |  |
| 1665 | `DdeSetUserHandle` | `0x98EA0` | 150 | UnwindData |  |
| 1532 | `CallMsgFilter` | `0x98F40` | 273 | UnwindData |  |
| 1533 | `CallMsgFilterA` | `0x98F40` | 273 | UnwindData |  |
| 1715 | `DrawCaptionTempA` | `0x99060` | 277 | UnwindData |  |
| 2293 | `SendMessageCallbackA` | `0x99180` | 136 | UnwindData |  |
| 2304 | `SetClassLongA` | `0x99210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2487 | `VkKeyScanExA` | `0x99230` | 211 | UnwindData |  |
| 2022 | `IMPGetIMEA` | `0x99B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2023 | `IMPGetIMEW` | `0x99B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2024 | `IMPQueryIMEA` | `0x99B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2025 | `IMPQueryIMEW` | `0x99BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2026 | `IMPSetIMEA` | `0x99BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2027 | `IMPSetIMEW` | `0x99BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2289 | `SendIMEMessageExA` | `0x99C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2290 | `SendIMEMessageExW` | `0x99C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2491 | `WINNLSEnableIME` | `0x99C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2492 | `WINNLSGetEnableStatus` | `0x99C70` | 7,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2683 | `GetCurrentMonitorTopologyId` | `0x9B8C0` | 2,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1511 | `AllowForegroundActivation` | `0x9C450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1518 | `ArrangeIconicWindows` | `0x9C460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `CascadeChildWindows` | `0x9C480` | 42 | UnwindData |  |
| 1592 | `CloseWindow` | `0x9C4B0` | 57 | UnwindData |  |
| 1607 | `CreateDesktopA` | `0x9C4F0` | 44 | UnwindData |  |
| 1608 | `CreateDesktopExA` | `0x9C530` | 394 | UnwindData |  |
| 2640 | *Ordinal Only* | `0x9C6C0` | 218 | UnwindData |  |
| 2641 | *Ordinal Only* | `0x9C7A0` | 351 | UnwindData |  |
| 1631 | `CreateWindowStationA` | `0x9C910` | 116 | UnwindData |  |
| 1678 | `DeferWindowPosAndBand` | `0x9C990` | 85 | UnwindData |  |
| 2645 | *Ordinal Only* | `0x9C9F0` | 33 | UnwindData |  |
| 2584 | *Ordinal Only* | `0x9CA20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2575 | *Ordinal Only* | `0x9CA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1861 | `GetInputDesktop` | `0x9CAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1865 | `GetKBCodePage` | `0x9CAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1937 | `GetProgmanWindow` | `0x9CAE0` | 88 | UnwindData |  |
| 1973 | `GetUnpredictedMessagePos` | `0x9CB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1980 | `GetWinStationInfo` | `0x9CB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1985 | `GetWindowContextHelpId` | `0x9CB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2017 | `GrayStringA` | `0x9CBA0` | 78 | UnwindData |  |
| 2018 | `GrayStringW` | `0x9CC00` | 75 | UnwindData |  |
| 2113 | `LoadKeyboardLayoutA` | `0x9CC60` | 127 | UnwindData |  |
| 2114 | `LoadKeyboardLayoutEx` | `0x9CCF0` | 35 | UnwindData |  |
| 2167 | `NotifyOverlayWindow` | `0x9CD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2178 | `OpenIcon` | `0x9CD40` | 57 | UnwindData |  |
| 2181 | `OpenWindowStationA` | `0x9CD80` | 101 | UnwindData |  |
| 2554 | *Ordinal Only* | `0x9CDF0` | 50 | UnwindData |  |
| 2248 | `RegisterFrostWindow` | `0x9CE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2552 | *Ordinal Only* | `0x9CE50` | 20 | UnwindData |  |
| 2262 | `RegisterSystemThread` | `0x9CE70` | 26 | UnwindData |  |
| 2316 | `SetDeskWallpaper` | `0x9CE90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2325 | `SetDoubleClickTime` | `0x9CEB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2361 | `SetProgmanWindow` | `0x9CED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2634 | *Ordinal Only* | `0x9CEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2570 | *Ordinal Only* | `0x9CF10` | 80 | UnwindData |  |
| 2389 | `SetWindowContextHelpId` | `0x9CF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2414 | `ShowStartGlass` | `0x9CF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2435 | `TileChildWindows` | `0x9CFB0` | 42 | UnwindData |  |
| 2553 | *Ordinal Only* | `0x9CFE0` | 121 | UnwindData |  |
| 2451 | `UnhookWindowsHook` | `0x9D060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2454 | `UnloadKeyboardLayout` | `0x9D080` | 45 | UnwindData |  |
| 2481 | `UserRegisterWowHandlers` | `0x9D0C0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1625 | `CreateSystemThreads` | `0x9D190` | 24 | UnwindData |  |
| 1545 | `ChangeDisplaySettingsW` | `0x9DE70` | 42 | UnwindData |  |
| 1716 | `DrawCaptionTempW` | `0x9DEA0` | 225 | UnwindData |  |
| 1524 | `BroadcastSystemMessage` | `0x9E010` | 39 | UnwindData |  |
| 1525 | `BroadcastSystemMessageA` | `0x9E010` | 39 | UnwindData |  |
| 1526 | `BroadcastSystemMessageExA` | `0x9E040` | 43 | UnwindData |  |
| 1842 | `GetDlgItemTextA` | `0x9E080` | 63 | UnwindData |  |
| 1997 | `GetWindowModuleFileName` | `0x9E0D0` | 60 | UnwindData |  |
| 1998 | `GetWindowModuleFileNameA` | `0x9E0D0` | 60 | UnwindData |  |
| 2159 | `ModifyMenuA` | `0x9E120` | 146 | UnwindData |  |
| 1510 | `AlignRects` | `0x9EB00` | 352 | UnwindData |  |
| 2547 | `gapfnScSendMessage` | `0xAC440` | 155,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2543 | `gSharedInfo` | `0xD2300` | 0 | Indeterminate |  |
