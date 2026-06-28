# Binary Specification: shlwapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\shlwapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9629d3acea48bec8a568034a4d40c356ba58ef68d147abc39798ed4c0b31c685`
* **Total Exported Functions:** 931

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 270 | `GUIDFromStringW` | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#200` |
| 767 | `SHCreateStreamWrapper` | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#471` |
| 773 | `SHDeleteOrphanKeyA` | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#446` |
| 774 | `SHDeleteOrphanKeyW` | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#447` |
| 218 | `SHUnicodeToAnsiCP` | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#151` |
| 13 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#429` |
| 25 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `user32.IsCharAlphaW` |
| 26 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `user32.IsCharUpperW` |
| 27 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `user32.IsCharLowerW` |
| 28 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `user32.IsCharAlphaNumericW` |
| 36 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.AppendMenuW` |
| 37 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CallWindowProcW` |
| 38 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CharLowerW` |
| 39 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CharLowerBuffW` |
| 40 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CharNextW` |
| 41 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CharPrevW` |
| 42 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CharToOemW` |
| 43 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CharUpperW` |
| 44 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CharUpperBuffW` |
| 45 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.CompareStringW` |
| 46 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CopyAcceleratorTableW` |
| 47 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CreateAcceleratorTableW` |
| 48 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.CreateDCW` |
| 49 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CreateDialogParamW` |
| 50 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.CreateDirectoryW` |
| 51 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.CreateEventW` |
| 52 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.CreateFileW` |
| 53 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.CreateFontIndirectW` |
| 54 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.CreateICW` |
| 55 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CreateWindowExW` |
| 56 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.DefWindowProcW` |
| 57 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.DeleteFileW` |
| 58 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.DialogBoxIndirectParamW` |
| 59 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.DialogBoxParamW` |
| 60 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.DispatchMessageW` |
| 61 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.DrawTextW` |
| 62 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.EnumFontFamiliesW` |
| 63 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.EnumFontFamiliesExW` |
| 64 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.EnumResourceNamesW` |
| 65 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.FindFirstFileW` |
| 66 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.FindResourceW` |
| 67 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.FindWindowW` |
| 68 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.FormatMessageW` |
| 69 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetClassInfoW` |
| 70 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetClassLongW` |
| 71 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetClassNameW` |
| 72 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetClipboardFormatNameW` |
| 73 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetCurrentDirectoryW` |
| 74 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetDlgItemTextW` |
| 75 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetFileAttributesW` |
| 76 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetFullPathNameW` |
| 77 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetLocaleInfoW` |
| 78 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetMenuStringW` |
| 79 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetMessageW` |
| 80 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetModuleFileNameW` |
| 81 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetSystemDirectoryW` |
| 82 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.SearchPathW` |
| 83 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetModuleHandleW` |
| 84 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.GetObjectW` |
| 85 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetPrivateProfileIntW` |
| 86 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetProfileStringW` |
| 87 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetPropW` |
| 88 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetStringTypeExW` |
| 89 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetTempFileNameW` |
| 90 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetTempPathW` |
| 91 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.GetTextExtentPoint32W` |
| 92 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.GetTextFaceW` |
| 93 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.GetTextMetricsW` |
| 94 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetWindowLongW` |
| 95 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetWindowTextW` |
| 96 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetWindowTextLengthW` |
| 97 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetWindowsDirectoryW` |
| 98 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.InsertMenuW` |
| 99 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.IsDialogMessageW` |
| 100 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.LoadAcceleratorsW` |
| 101 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.LoadBitmapW` |
| 102 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.LoadCursorW` |
| 103 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.LoadIconW` |
| 104 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.LoadImageW` |
| 105 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.LoadLibraryExW` |
| 106 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.LoadMenuW` |
| 107 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.LoadStringW` |
| 108 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.MessageBoxIndirectW` |
| 109 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.ModifyMenuW` |
| 110 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.GetCharWidth32W` |
| 111 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.GetCharacterPlacementW` |
| 112 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.CopyFileW` |
| 113 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.MoveFileW` |
| 114 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.OemToCharW` |
| 115 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.OutputDebugStringW` |
| 116 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.PeekMessageW` |
| 117 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.PostMessageW` |
| 118 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.PostThreadMessageW` |
| 119 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#448` |
| 122 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#449` |
| 129 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#450` |
| 131 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.RegisterClassW` |
| 132 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.RegisterClipboardFormatW` |
| 133 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.RegisterWindowMessageW` |
| 134 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.RemovePropW` |
| 135 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.SendDlgItemMessageW` |
| 136 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.SendMessageW` |
| 137 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.SetCurrentDirectoryW` |
| 138 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.SetDlgItemTextW` |
| 139 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.SetMenuItemInfoW` |
| 140 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.SetPropW` |
| 141 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.SetWindowLongW` |
| 142 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.SetWindowsHookExW` |
| 143 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.SetWindowTextW` |
| 144 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.StartDocW` |
| 145 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.SystemParametersInfoW` |
| 146 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.TranslateAcceleratorW` |
| 147 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.UnregisterClassW` |
| 148 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.VkKeyScanW` |
| 149 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.WinHelpW` |
| 150 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.wvsprintfW` |
| 159 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.CompareStringW` |
| 161 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#472` |
| 166 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#102` |
| 171 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#246` |
| 175 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#142` |
| 188 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#451` |
| 189 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#452` |
| 194 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#160` |
| 196 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#243` |
| 205 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#124` |
| 206 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#125` |
| 207 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#453` |
| 216 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#150` |
| 222 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#139` |
| 223 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#140` |
| 224 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#141` |
| 226 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#244` |
| 227 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#245` |
| 241 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#142` |
| 242 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#143` |
| 243 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#144` |
| 244 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#145` |
| 245 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#146` |
| 246 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#147` |
| 247 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#148` |
| 248 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#149` |
| 249 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#150` |
| 250 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#152` |
| 251 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#153` |
| 252 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#154` |
| 253 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#155` |
| 254 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#156` |
| 255 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#157` |
| 258 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#158` |
| 259 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#159` |
| 260 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#162` |
| 261 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#160` |
| 262 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#161` |
| 264 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#162` |
| 272 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#163` |
| 273 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#164` |
| 274 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#316` |
| 275 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#317` |
| 277 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#240` |
| 289 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `WINMM.PlaySoundW` |
| 290 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#247` |
| 293 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#165` |
| 296 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#314` |
| 297 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#315` |
| 298 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.WritePrivateProfileStringW` |
| 299 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.ExtTextOutW` |
| 300 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.CreateFontW` |
| 301 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.DrawTextExW` |
| 302 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetMenuItemInfoW` |
| 303 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.InsertMenuItemW` |
| 304 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.CreateMetaFileW` |
| 305 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.CreateMutexW` |
| 306 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.ExpandEnvironmentStringsW` |
| 307 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.CreateSemaphoreW` |
| 308 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.IsBadStringPtrW` |
| 309 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.LoadLibraryW` |
| 310 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetTimeFormatW` |
| 311 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetDateFormatW` |
| 312 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetPrivateProfileStringW` |
| 313 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.SHGetFileInfoW` |
| 314 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.RegisterClassExW` |
| 315 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.GetClassInfoExW` |
| 318 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.DragQueryFileW` |
| 319 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.FindWindowExW` |
| 320 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#454` |
| 321 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#455` |
| 322 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#456` |
| 323 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#457` |
| 324 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#458` |
| 325 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#459` |
| 326 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#460` |
| 327 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#461` |
| 328 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#462` |
| 329 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#463` |
| 330 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#464` |
| 332 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CallMsgFilterW` |
| 333 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.SHBrowseForFolderW` |
| 334 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.SHGetPathFromIDListW` |
| 335 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.ShellExecuteExW` |
| 336 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.SHFileOperationW` |
| 337 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.ExtractIconExW` |
| 338 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.SetFileAttributesW` |
| 339 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetNumberFormatW` |
| 340 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.MessageBoxW` |
| 341 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.FindNextFileW` |
| 343 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#166` |
| 356 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#167` |
| 357 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.SHGetNewLinkInfoW` |
| 358 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.SHDefExtractIconW` |
| 359 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.OpenEventW` |
| 360 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.RemoveDirectoryW` |
| 361 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetShortPathNameW` |
| 362 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#465` |
| 367 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.WritePrivateProfileStructW` |
| 368 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetPrivateProfileStructW` |
| 369 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.CreateProcessW` |
| 370 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.ExtractIconW` |
| 371 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.DdeInitializeW` |
| 372 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.DdeCreateStringHandleW` |
| 373 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.DdeQueryStringW` |
| 374 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#344` |
| 375 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#345` |
| 376 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetThreadUILanguage` |
| 379 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.Shell_GetCachedImageIndexW` |
| 380 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.Shell_GetCachedImageIndexA` |
| 385 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#338` |
| 386 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#339` |
| 387 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#340` |
| 389 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `COMDLG32.GetSaveFileNameW` |
| 390 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#209` |
| 391 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `MPR.WNetGetLastErrorW` |
| 392 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.EndDialog` |
| 393 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.CreateDialogIndirectParamW` |
| 394 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.SHChangeNotify` |
| 395 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.WinHelpA` |
| 396 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#320` |
| 397 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.WinHelpW` |
| 398 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#321` |
| 401 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `COMDLG32.PageSetupDlgW` |
| 402 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `COMDLG32.PrintDlgW` |
| 403 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `COMDLG32.GetOpenFileNameW` |
| 404 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#313` |
| 405 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#466` |
| 406 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#467` |
| 411 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#238` |
| 412 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#239` |
| 414 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#323` |
| 415 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#322` |
| 416 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#325` |
| 417 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#324` |
| 418 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#468` |
| 419 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHELL32.SHFlushSFCache` |
| 420 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#241` |
| 421 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#242` |
| 422 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#168` |
| 423 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#169` |
| 424 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#170` |
| 425 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.DeleteMenu` |
| 426 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.DestroyMenu` |
| 427 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.TrackPopupMenu` |
| 428 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.TrackPopupMenuEx` |
| 429 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#331` |
| 430 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#332` |
| 431 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#333` |
| 434 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `USER32.SendMessageTimeoutW` |
| 439 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#126` |
| 440 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#469` |
| 441 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#470` |
| 442 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetEnvironmentVariableW` |
| 443 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetSystemWindowsDirectoryA` |
| 444 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetSystemWindowsDirectoryW` |
| 457 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetLongPathNameW` |
| 458 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GetLongPathNameA` |
| 461 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#428` |
| 470 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#346` |
| 473 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#171` |
| 474 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#172` |
| 475 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#211` |
| 476 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#193` |
| 480 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#341` |
| 482 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#369` |
| 483 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#370` |
| 485 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#103` |
| 486 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#104` |
| 488 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#347` |
| 489 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GlobalAddAtomW` |
| 490 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `KERNEL32.GlobalFindAtomW` |
| 492 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#357` |
| 498 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#348` |
| 500 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#210` |
| 501 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#211` |
| 502 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#212` |
| 503 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#213` |
| 514 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#140` |
| 543 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `GDI32.CreateColorSpaceW` |
| 547 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#173` |
| 550 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#174` |
| 551 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#175` |
| 552 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#176` |
| 554 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#177` |
| 555 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#178` |
| 556 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#179` |
| 557 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#180` |
| 558 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#181` |
| 559 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#443` |
| 560 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#191` |
| 563 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#167` |
| 564 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#182` |
| 565 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#183` |
| 566 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#180` |
| 573 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#349` |
| 574 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#350` |
| 576 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#127` |
| 598 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#210` |
| 599 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#152` |
| 600 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#153` |
| 601 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#352` |
| 602 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#351` |
| 603 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#353` |
| 604 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#354` |
| 605 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#355` |
| 606 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#356` |
| 611 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#141` |
| 618 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#190` |
| 619 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#192` |
| 627 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#110` |
| 628 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#109` |
| 632 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#130` |
| 633 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#131` |
| 634 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#132` |
| 642 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#442` |
| 644 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#107` |
| 645 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#108` |
| 646 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#101` |
| 647 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#100` |
| 648 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHCORE.#161` |
| 6 | *Ordinal Only* | `0x1DA0` | 878 | UnwindData |  |
| 511 | *Ordinal Only* | `0x2120` | 511 | UnwindData |  |
| 450 | *Ordinal Only* | `0x2330` | 232 | UnwindData |  |
| 663 | `PathCompactPathExW` | `0x26F0` | 721 | UnwindData |  |
| 236 | `SHPinDllOfCLSID` | `0x2D50` | 735 | UnwindData |  |
| 24 | *Ordinal Only* | `0x30B0` | 24 | UnwindData |  |
| 466 | *Ordinal Only* | `0x33C0` | 634 | UnwindData |  |
| 464 | *Ordinal Only* | `0x3640` | 32 | UnwindData |  |
| 4 | *Ordinal Only* | `0x3940` | 79 | UnwindData |  |
| 266 | *Ordinal Only* | `0x39A0` | 70 | UnwindData |  |
| 18 | *Ordinal Only* | `0x3BC0` | 1,136 | UnwindData |  |
| 268 | *Ordinal Only* | `0x4090` | 66 | UnwindData |  |
| 533 | *Ordinal Only* | `0x40E0` | 275 | UnwindData |  |
| 348 | *Ordinal Only* | `0x4200` | 1,541 | UnwindData |  |
| 516 | *Ordinal Only* | `0x4C30` | 143 | UnwindData |  |
| 519 | *Ordinal Only* | `0x4CD0` | 336 | UnwindData |  |
| 584 | `AssocGetPerceivedType` | `0x4F30` | 65 | UnwindData |  |
| 517 | *Ordinal Only* | `0x5690` | 142 | UnwindData |  |
| 635 | *Ordinal Only* | `0x5730` | 143 | UnwindData |  |
| 471 | *Ordinal Only* | `0x5FB0` | 379 | UnwindData |  |
| 365 | *Ordinal Only* | `0x6810` | 107 | UnwindData |  |
| 267 | *Ordinal Only* | `0x6890` | 111 | UnwindData |  |
| 20 | *Ordinal Only* | `0x6910` | 282 | UnwindData |  |
| 22 | *Ordinal Only* | `0x6DA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | *Ordinal Only* | `0x6DE0` | 212 | UnwindData |  |
| 478 | *Ordinal Only* | `0x6EC0` | 151 | UnwindData |  |
| 219 | `QISearch` | `0x6F60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 590 | `AssocQueryStringByKeyW` | `0x70A0` | 334 | UnwindData |  |
| 204 | `SHIsChildOrSelf` | `0x7200` | 54 | UnwindData |  |
| 172 | `IUnknown_GetWindow` | `0x7240` | 390 | UnwindData |  |
| 283 | *Ordinal Only* | `0x73D0` | 144 | UnwindData |  |
| 284 | *Ordinal Only* | `0x7470` | 99 | UnwindData |  |
| 288 | *Ordinal Only* | `0x76C0` | 68 | UnwindData |  |
| 544 | *Ordinal Only* | `0x79E0` | 40 | UnwindData |  |
| 187 | *Ordinal Only* | `0x7E40` | 124 | UnwindData |  |
| 239 | *Ordinal Only* | `0x7ED0` | 84 | UnwindData |  |
| 581 | *Ordinal Only* | `0x7F30` | 299 | UnwindData |  |
| 831 | `SHSkipJunction` | `0x8070` | 494 | UnwindData |  |
| 240 | *Ordinal Only* | `0x8270` | 106 | UnwindData |  |
| 156 | `StrCmpCW` | `0x8320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `PathFileExistsAndAttributesW` | `0x8340` | 82 | UnwindData |  |
| 19 | *Ordinal Only* | `0x8480` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | *Ordinal Only* | `0x8540` | 198 | UnwindData |  |
| 691 | `PathIsDirectoryW` | `0x8A40` | 267 | UnwindData |  |
| 164 | `IUnknown_Exec` | `0x8B60` | 181 | UnwindData |  |
| 591 | `AssocQueryStringW` | `0x8E00` | 334 | UnwindData |  |
| 579 | `AssocCreate` | `0x8F90` | 112 | UnwindData |  |
| 456 | *Ordinal Only* | `0x9860` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 849 | `StrChrW` | `0x9950` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | *Ordinal Only* | `0x9D30` | 146 | UnwindData |  |
| 854 | `StrCmpNIW` | `0x9DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | *Ordinal Only* | `0x9DF0` | 115 | UnwindData |  |
| 17 | *Ordinal Only* | `0x9E70` | 156 | UnwindData |  |
| 673 | `PathFindFileNameW` | `0x9F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `PathStripToRootW` | `0x9F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `StrCmpICW` | `0x9F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 856 | `StrCmpW` | `0x9F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `StrStrIW` | `0x9FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 672 | `PathFindFileNameA` | `0x9FC0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | *Ordinal Only* | `0xA030` | 130 | UnwindData |  |
| 899 | `StrToIntW` | `0xA5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 671 | `PathFindExtensionW` | `0xA5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | *Ordinal Only* | `0xA600` | 660 | UnwindData |  |
| 481 | *Ordinal Only* | `0xA8E0` | 126 | UnwindData |  |
| 925 | `UrlIsW` | `0xA970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `ConnectToConnectionPoint` | `0xA990` | 324 | UnwindData |  |
| 699 | `PathIsPrefixW` | `0xAAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | *Ordinal Only* | `0xAB00` | 141 | UnwindData |  |
| 885 | `StrRetToStrW` | `0xAED0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 572 | *Ordinal Only* | `0xAF40` | 289 | UnwindData |  |
| 512 | `IStream_ReadPidl` | `0xB0D0` | 247 | UnwindData |  |
| 271 | *Ordinal Only* | `0xB260` | 219 | UnwindData |  |
| 193 | *Ordinal Only* | `0xB350` | 116 | UnwindData |  |
| 163 | `IUnknown_QueryStatus` | `0xB3D0` | 167 | UnwindData |  |
| 165 | *Ordinal Only* | `0xB480` | 118 | UnwindData |  |
| 784 | `SHGetValueW` | `0xB520` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `PathStripPathW` | `0xB5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 717 | `PathMakePrettyW` | `0xB600` | 78 | UnwindData |  |
| 454 | *Ordinal Only* | `0xB660` | 34 | UnwindData |  |
| 225 | `SHStripMneumonicW` | `0xB7D0` | 239 | UnwindData |  |
| 479 | *Ordinal Only* | `0xB8D0` | 140 | UnwindData |  |
| 610 | `GetMenuPosFromID` | `0xB970` | 184 | UnwindData |  |
| 713 | `PathIsUNCW` | `0xBA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SHCreateMemStream` | `0xBAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 587 | `AssocQueryKeyW` | `0xBAD0` | 317 | UnwindData |  |
| 765 | `SHCreateStreamOnFileEx` | `0xBC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | *Ordinal Only* | `0xBC70` | 142 | UnwindData |  |
| 917 | `UrlGetPartW` | `0xBD10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | *Ordinal Only* | `0xBD30` | 67 | UnwindData |  |
| 233 | *Ordinal Only* | `0xBD80` | 413 | UnwindData |  |
| 669 | `PathFileExistsW` | `0xBF30` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `StrChrA` | `0xBF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 833 | `SHStrDupW` | `0xBFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `StrCmpNIA` | `0xBFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | *Ordinal Only* | `0xBFF0` | 264 | UnwindData |  |
| 179 | *Ordinal Only* | `0xC100` | 169 | UnwindData |  |
| 855 | `StrCmpNW` | `0xC1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 878 | `StrRChrW` | `0xC210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 883 | `StrRetToBufW` | `0xC230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 595 | `ColorHLSToRGB` | `0xC250` | 358 | UnwindData |  |
| 739 | `PathRemoveFileSpecW` | `0xC440` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `PathAddBackslashW` | `0xC6B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | *Ordinal Only* | `0xC6D0` | 147 | UnwindData |  |
| 208 | *Ordinal Only* | `0xC770` | 147 | UnwindData |  |
| 656 | `PathCanonicalizeW` | `0xC810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `PathSkipRootW` | `0xC830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `StrCmpNICW` | `0xC850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `PathAppendW` | `0xC870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 697 | `PathIsNetworkPathW` | `0xC890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | *Ordinal Only* | `0xC8B0` | 214 | UnwindData |  |
| 733 | `PathRemoveBackslashW` | `0xC990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | *Ordinal Only* | `0xC9B0` | 152 | UnwindData |  |
| 173 | *Ordinal Only* | `0xCA50` | 137 | UnwindData |  |
| 282 | *Ordinal Only* | `0xCC60` | 58 | UnwindData |  |
| 281 | `SHPackDispParamsV` | `0xCCA0` | 242 | UnwindData |  |
| 715 | `PathIsURLW` | `0xCDA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 860 | `StrDupW` | `0xCDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `IUnknown_QueryService` | `0xCDE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `PathIsRootW` | `0xCE00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 763 | `SHCreateShellPalette` | `0xCE20` | 316 | UnwindData |  |
| 295 | *Ordinal Only* | `0xD030` | 297 | UnwindData |  |
| 723 | `PathMatchSpecW` | `0xD520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 701 | `PathIsRelativeW` | `0xD540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 487 | `SHLoadIndirectString` | `0xD560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `GetAcceptLanguagesA` | `0xD580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `PathMakeSystemFolderW` | `0xD5A0` | 447 | UnwindData |  |
| 178 | *Ordinal Only* | `0xD890` | 183 | UnwindData |  |
| 901 | `StrTrimW` | `0xDBB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `PathRemoveBlanksW` | `0xDBD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | `UrlEscapeW` | `0xDBF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 693 | `PathIsFileSpecW` | `0xDC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `PathRemoveExtensionW` | `0xDC50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 685 | `PathGetDriveNumberW` | `0xDC70` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 905 | `UrlCanonicalizeW` | `0xDE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | `wnsprintfA` | `0xDE60` | 98 | UnwindData |  |
| 858 | `StrCpyW` | `0xE020` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 617 | *Ordinal Only* | `0xE050` | 136 | UnwindData |  |
| 210 | *Ordinal Only* | `0xE0E0` | 283 | UnwindData |  |
| 460 | *Ordinal Only* | `0xE210` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 667 | `PathCreateFromUrlW` | `0xE260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 811 | `SHRegGetUSValueW` | `0xE280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 889 | `StrStrIA` | `0xE2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | `PathCommonPrefixW` | `0xE2C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 690 | `PathIsDirectoryEmptyW` | `0xE2E0` | 257 | UnwindData |  |
| 668 | `PathFileExistsA` | `0xE460` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `ColorRGBToHLS` | `0xE5A0` | 424 | UnwindData |  |
| 157 | `StrCmpICA` | `0xE750` | 2,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | *Ordinal Only* | `0xF1D0` | 98 | UnwindData |  |
| 585 | `AssocIsDangerous` | `0xF240` | 27 | UnwindData |  |
| 561 | *Ordinal Only* | `0xF270` | 179 | UnwindData |  |
| 658 | `PathCombineW` | `0xF330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | *Ordinal Only* | `0xF350` | 65 | UnwindData |  |
| 731 | `PathRemoveArgsW` | `0xF3A0` | 68 | UnwindData |  |
| 813 | `SHRegGetValueW` | `0xF3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 898 | `StrToIntExW` | `0xF410` | 1,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | *Ordinal Only* | `0xF880` | 171 | UnwindData |  |
| 864 | `StrFormatByteSizeW` | `0xFA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 707 | `PathIsSystemFolderW` | `0xFA80` | 65 | UnwindData |  |
| 843 | `StrCatW` | `0xFAD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `PathGetArgsW` | `0xFB10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | *Ordinal Only* | `0xFB90` | 286 | UnwindData |  |
| 448 | *Ordinal Only* | `0xFCC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 772 | `SHDeleteKeyW` | `0xFCF0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 922 | `UrlIsNoHistoryW` | `0xFE20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `IUnknown_Set` | `0xFE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `UrlUnescapeW` | `0xFE60` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 437 | `IsOS` | `0xFEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 807 | `SHRegGetBoolUSValueW` | `0xFF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `StrRChrIW` | `0xFF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 881 | `StrRetToBSTR` | `0xFF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `SHRegOpenUSKeyW` | `0xFF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `PathIsUNCServerW` | `0xFF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | `StrCmpIW` | `0xFFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `StrPBrkW` | `0xFFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ParseURLW` | `0xFFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `SHAnsiToUnicode` | `0x10010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 778 | `SHEnumKeyExW` | `0x10030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 907 | `UrlCombineW` | `0x10050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 929 | `wnsprintfW` | `0x10070` | 103 | UnwindData |  |
| 679 | `PathFindSuffixArrayW` | `0x100E0` | 162 | UnwindData |  |
| 725 | `PathParseIconLocationW` | `0x10190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 852 | `StrCmpNA` | `0x101B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 830 | `SHSetValueW` | `0x101D0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 664 | `PathCompactPathW` | `0x102B0` | 1,036 | UnwindData |  |
| 388 | `ShellMessageBoxW` | `0x106D0` | 669 | UnwindData |  |
| 515 | `SHGetViewStatePropertyBag` | `0x10980` | 1,447 | UnwindData |  |
| 738 | `PathRemoveFileSpecA` | `0x11280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 743 | `PathSearchAndQualifyW` | `0x112A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 794 | `SHRegCloseUSKey` | `0x112C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `SHCreateWorkerWindowW` | `0x112E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `SHCreateStreamOnFileW` | `0x11300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `PathUnquoteSpacesW` | `0x11320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 711 | `PathIsUNCServerShareW` | `0x11340` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | `PathAppendA` | `0x11510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 708 | `PathIsUNCA` | `0x11530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `StrCmpLogicalW` | `0x11550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 825 | `SHRegWriteUSValueW` | `0x11570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 793 | `SHQueryValueExW` | `0x11590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `PathBuildRootW` | `0x115B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `PathUnExpandEnvStringsW` | `0x115D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 893 | `StrStrW` | `0x115F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 900 | `StrTrimA` | `0x11610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 783 | `SHGetValueA` | `0x11630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `IUnknown_GetSite` | `0x11650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `SHFormatDateTimeW` | `0x11670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 622 | `IntlStrEqWorkerW` | `0x11690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | `StrIsIntlEqualW` | `0x11690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 840 | `StrCatBuffA` | `0x116B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 670 | `PathFindExtensionA` | `0x116D0` | 7,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 629 | `SHRegGetValueFromHKCUHKLM` | `0x13290` | 2,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `SHRegGetBoolValueFromHKCUHKLM` | `0x13B90` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | *Ordinal Only* | `0x13C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 631 | *Ordinal Only* | `0x13C50` | 5,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 592 | `ChrCmpIA` | `0x14FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `ChrCmpIW` | `0x15000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `GetAcceptLanguagesW` | `0x15020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 612 | `HashData` | `0x15040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | *Ordinal Only* | `0x15060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | *Ordinal Only* | `0x15080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | *Ordinal Only* | `0x150A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | *Ordinal Only* | `0x150C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 623 | `IsCharSpaceA` | `0x150E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `IsCharSpaceW` | `0x15100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | *Ordinal Only* | `0x15120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `IsInternetESCEnabled` | `0x15140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 562 | *Ordinal Only* | `0x15140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `ParseURLA` | `0x15160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 624 | `PathAddBackslashA` | `0x15180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 649 | `PathAddExtensionA` | `0x151A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `PathAddExtensionW` | `0x151C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 655 | `PathCanonicalizeA` | `0x151E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 657 | `PathCombineA` | `0x15200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 659 | `PathCommonPrefixA` | `0x15220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 665 | `PathCreateFromUrlA` | `0x15240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 666 | `PathCreateFromUrlAlloc` | `0x15260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 674 | `PathFindNextComponentA` | `0x15280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 675 | `PathFindNextComponentW` | `0x152A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `PathGetArgsA` | `0x152C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 682 | `PathGetCharTypeA` | `0x152E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `PathGetCharTypeW` | `0x15300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `PathGetDriveNumberA` | `0x15320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 692 | `PathIsFileSpecA` | `0x15340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 694 | `PathIsLFNFileSpecA` | `0x15360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 695 | `PathIsLFNFileSpecW` | `0x15380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 698 | `PathIsPrefixA` | `0x153A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 700 | `PathIsRelativeA` | `0x153C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | `PathIsRootA` | `0x153E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `PathIsSameRootA` | `0x15400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `PathIsSameRootW` | `0x15420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `PathIsUNCServerA` | `0x15440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `PathIsUNCServerShareA` | `0x15460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `PathIsURLA` | `0x15480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | *Ordinal Only* | `0x154A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 720 | `PathMatchSpecA` | `0x154B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 721 | `PathMatchSpecExA` | `0x154D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 722 | `PathMatchSpecExW` | `0x154F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 724 | `PathParseIconLocationA` | `0x15510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 726 | `PathQuoteSpacesA` | `0x15530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 727 | `PathQuoteSpacesW` | `0x15550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `PathRelativePathToA` | `0x15570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 729 | `PathRelativePathToW` | `0x15590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `PathRemoveBackslashA` | `0x155B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `PathRemoveBlanksA` | `0x155D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 736 | `PathRemoveExtensionA` | `0x155F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `PathRenameExtensionA` | `0x15610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `PathRenameExtensionW` | `0x15630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `PathSearchAndQualifyA` | `0x15650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 746 | `PathSkipRootA` | `0x15670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 748 | `PathStripPathA` | `0x15690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `PathStripToRootA` | `0x156B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | `PathUnExpandEnvStringsA` | `0x156D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `PathUnquoteSpacesA` | `0x156F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | *Ordinal Only* | `0x15710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 795 | `SHRegCreateUSKeyA` | `0x15730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 796 | `SHRegCreateUSKeyW` | `0x15750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `SHRegDeleteEmptyUSKeyA` | `0x15770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 798 | `SHRegDeleteEmptyUSKeyW` | `0x15790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 799 | `SHRegDeleteUSValueA` | `0x157B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 800 | `SHRegDeleteUSValueW` | `0x157D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 802 | `SHRegEnumUSKeyA` | `0x157F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 803 | `SHRegEnumUSKeyW` | `0x15810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 804 | `SHRegEnumUSValueA` | `0x15830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 805 | `SHRegEnumUSValueW` | `0x15850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 806 | `SHRegGetBoolUSValueA` | `0x15870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `SHRegGetUSValueA` | `0x15890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `SHRegOpenUSKeyA` | `0x158B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 816 | `SHRegQueryInfoUSKeyA` | `0x158D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `SHRegQueryInfoUSKeyW` | `0x158F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | `SHRegQueryUSValueA` | `0x15910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 819 | `SHRegQueryUSValueW` | `0x15930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 822 | `SHRegSetUSValueA` | `0x15950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 823 | `SHRegSetUSValueW` | `0x15970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | `SHRegWriteUSValueA` | `0x15990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | *Ordinal Only* | `0x159B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 836 | `StrCSpnA` | `0x159D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 837 | `StrCSpnIA` | `0x159F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 838 | `StrCSpnIW` | `0x15A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 839 | `StrCSpnW` | `0x15A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 841 | `StrCatBuffW` | `0x15A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `StrCatChainW` | `0x15A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `StrChrIA` | `0x15A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `StrChrIW` | `0x15AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `StrChrNIW` | `0x15AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 848 | `StrChrNW` | `0x15AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `StrCmpCA` | `0x15B10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `StrCmpNCA` | `0x15B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `StrCmpNCW` | `0x15B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `StrCmpNICA` | `0x15B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 857 | `StrCpyNW` | `0x15B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | *Ordinal Only* | `0x15BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | *Ordinal Only* | `0x15BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 859 | `StrDupA` | `0x15BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 620 | `IntlStrEqWorkerA` | `0x15C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `StrIsIntlEqualA` | `0x15C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `StrPBrkA` | `0x15C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `StrRChrA` | `0x15C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 876 | `StrRChrIA` | `0x15C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `StrRStrIA` | `0x15C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `StrRStrIW` | `0x15CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | `StrSpnA` | `0x15CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | `StrSpnW` | `0x15CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 888 | `StrStrA` | `0x15D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 891 | `StrStrNIW` | `0x15D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `StrStrNW` | `0x15D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `StrToInt64ExA` | `0x15D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 895 | `StrToInt64ExW` | `0x15D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 896 | `StrToIntA` | `0x15DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | `StrToIntExA` | `0x15DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 902 | `UrlApplySchemeA` | `0x15DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `UrlApplySchemeW` | `0x15E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `UrlCanonicalizeA` | `0x15E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 906 | `UrlCombineA` | `0x15E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 908 | `UrlCompareA` | `0x15E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `UrlCompareW` | `0x15E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 910 | `UrlCreateFromPathA` | `0x15EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | `UrlCreateFromPathW` | `0x15ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 912 | `UrlEscapeA` | `0x15EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `UrlFixupW` | `0x15F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 914 | `UrlGetLocationA` | `0x15F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 915 | `UrlGetLocationW` | `0x15F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 916 | `UrlGetPartA` | `0x15F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 918 | `UrlHashA` | `0x15F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 919 | `UrlHashW` | `0x15FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 920 | `UrlIsA` | `0x15FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 921 | `UrlIsNoHistoryA` | `0x15FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 923 | `UrlIsOpaqueA` | `0x16010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 924 | `UrlIsOpaqueW` | `0x16030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `UrlUnescapeA` | `0x16050` | 10,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 568 | `IStream_Copy` | `0x18A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 596 | `IStream_ReadStr` | `0x18A40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `IStream_Read` | `0x18A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `IStream_Reset` | `0x18A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `IStream_Size` | `0x18AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `IStream_WriteStr` | `0x18AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `IStream_Write` | `0x18AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `IUnknown_AtomicRelease` | `0x18B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `IUnknown_SetSite` | `0x18B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `PathBuildRootA` | `0x18B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 696 | `PathIsNetworkPathA` | `0x18B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `SHAnsiToAnsi` | `0x18B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `SHCopyKeyA` | `0x18BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 762 | `SHCopyKeyW` | `0x18BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 764 | `SHCreateStreamOnFileA` | `0x18BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 768 | `SHCreateThreadRef` | `0x18C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SHCreateThread` | `0x18C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 615 | `SHCreateThreadWithHandle` | `0x18C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `SHDeleteEmptyKeyA` | `0x18C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 770 | `SHDeleteEmptyKeyW` | `0x18C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `SHDeleteKeyA` | `0x18CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 775 | `SHDeleteValueA` | `0x18CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `SHDeleteValueW` | `0x18CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 777 | `SHEnumKeyExA` | `0x18D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `SHEnumValueA` | `0x18D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 780 | `SHEnumValueW` | `0x18D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 782 | `SHGetThreadRef` | `0x18D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 786 | `SHOpenRegStream2A` | `0x18D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | `SHOpenRegStream2W` | `0x18DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 788 | `SHOpenRegStreamA` | `0x18DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `SHOpenRegStreamW` | `0x18DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 790 | `SHQueryInfoKeyA` | `0x18E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 791 | `SHQueryInfoKeyW` | `0x18E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 792 | `SHQueryValueExA` | `0x18E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 801 | `SHRegDuplicateHKey` | `0x18E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `SHRegGetIntW` | `0x18E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 808 | `SHRegGetPathA` | `0x18EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 809 | `SHRegGetPathW` | `0x18EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 812 | `SHRegGetValueA` | `0x18EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 820 | `SHRegSetPathA` | `0x18F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 821 | `SHRegSetPathW` | `0x18F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `SHReleaseThreadRef` | `0x18F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 828 | `SHSetThreadRef` | `0x18F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 829 | `SHSetValueA` | `0x18F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 832 | `SHStrDupA` | `0x18FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `SHUnicodeToAnsi` | `0x18FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `SHUnicodeToUnicode` | `0x18FE0` | 2,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | *Ordinal Only* | `0x19880` | 34 | UnwindData |  |
| 451 | *Ordinal Only* | `0x198B0` | 35 | UnwindData |  |
| 447 | *Ordinal Only* | `0x198E0` | 46 | UnwindData |  |
| 449 | *Ordinal Only* | `0x19920` | 226 | UnwindData |  |
| 661 | `PathCompactPathA` | `0x19A10` | 943 | UnwindData |  |
| 662 | `PathCompactPathExA` | `0x19DD0` | 550 | UnwindData |  |
| 445 | *Ordinal Only* | `0x1A000` | 287 | UnwindData |  |
| 3 | *Ordinal Only* | `0x1A130` | 76 | UnwindData |  |
| 676 | `PathFindOnPathA` | `0x1A230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | *Ordinal Only* | `0x1A240` | 671 | UnwindData |  |
| 678 | `PathFindSuffixArrayA` | `0x1A4F0` | 228 | UnwindData |  |
| 686 | `PathIsContentTypeA` | `0x1A5E0` | 171 | UnwindData |  |
| 688 | `PathIsDirectoryA` | `0x1A6A0` | 276 | UnwindData |  |
| 689 | `PathIsDirectoryEmptyA` | `0x1A7C0` | 240 | UnwindData |  |
| 706 | `PathIsSystemFolderA` | `0x1A8C0` | 64 | UnwindData |  |
| 716 | `PathMakePrettyA` | `0x1A9D0` | 114 | UnwindData |  |
| 718 | `PathMakeSystemFolderA` | `0x1AA50` | 440 | UnwindData |  |
| 730 | `PathRemoveArgsA` | `0x1AC10` | 56 | UnwindData |  |
| 744 | `PathSetDlgItemPathA` | `0x1AC50` | 351 | UnwindData |  |
| 465 | *Ordinal Only* | `0x1ADC0` | 29 | UnwindData |  |
| 754 | `PathUndecorateA` | `0x1ADF0` | 221 | UnwindData |  |
| 756 | `PathUnmakeSystemFolderA` | `0x1AEE0` | 74 | UnwindData |  |
| 364 | *Ordinal Only* | `0x1E8D0` | 32 | UnwindData |  |
| 463 | *Ordinal Only* | `0x1E900` | 131 | UnwindData |  |
| 349 | *Ordinal Only* | `0x1E990` | 1,157 | UnwindData |  |
| 170 | *Ordinal Only* | `0x1F340` | 4,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 834 | `ShellMessageBoxA` | `0x20690` | 811 | UnwindData |  |
| 381 | *Ordinal Only* | `0x21CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | *Ordinal Only* | `0x21CC0` | 181 | UnwindData |  |
| 409 | *Ordinal Only* | `0x21D80` | 680 | UnwindData |  |
| 407 | *Ordinal Only* | `0x22030` | 632 | UnwindData |  |
| 408 | *Ordinal Only* | `0x222B0` | 499 | UnwindData |  |
| 586 | `AssocQueryKeyA` | `0x224B0` | 242 | UnwindData |  |
| 588 | `AssocQueryStringA` | `0x225B0` | 421 | UnwindData |  |
| 589 | `AssocQueryStringByKeyA` | `0x22760` | 335 | UnwindData |  |
| 468 | *Ordinal Only* | `0x22940` | 130 | UnwindData |  |
| 469 | *Ordinal Only* | `0x229D0` | 308 | UnwindData |  |
| 467 | `SHRunIndirectRegClientCommand` | `0x22B10` | 538 | UnwindData |  |
| 452 | *Ordinal Only* | `0x22EC0` | 35 | UnwindData |  |
| 677 | `PathFindOnPathW` | `0x22EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 687 | `PathIsContentTypeW` | `0x22F00` | 172 | UnwindData |  |
| 745 | `PathSetDlgItemPathW` | `0x22FC0` | 366 | UnwindData |  |
| 643 | *Ordinal Only* | `0x23140` | 35 | UnwindData |  |
| 755 | `PathUndecorateW` | `0x23170` | 159 | UnwindData |  |
| 757 | `PathUnmakeSystemFolderW` | `0x23220` | 76 | UnwindData |  |
| 353 | `SHFormatDateTimeA` | `0x23390` | 120 | UnwindData |  |
| 413 | *Ordinal Only* | `0x237D0` | 101 | UnwindData |  |
| 438 | *Ordinal Only* | `0x23960` | 158 | UnwindData |  |
| 835 | `ShellMessageBoxInternal` | `0x23CE0` | 82 | UnwindData |  |
| 594 | `ColorAdjustLuma` | `0x23D40` | 195 | UnwindData |  |
| 569 | `DelayLoadFailureHook` | `0x23E10` | 82 | UnwindData |  |
| 871 | `StrNCatA` | `0x23EE0` | 60 | UnwindData |  |
| 872 | `StrNCatW` | `0x23F30` | 63 | UnwindData |  |
| 861 | `StrFormatByteSize64A` | `0x23F80` | 108 | UnwindData |  |
| 862 | `StrFormatByteSizeA` | `0x24000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 863 | `StrFormatByteSizeEx` | `0x24010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 865 | `StrFormatKBSizeA` | `0x24030` | 120 | UnwindData |  |
| 866 | `StrFormatKBSizeW` | `0x240B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 882 | `StrRetToBufA` | `0x240D0` | 173 | UnwindData |  |
| 884 | `StrRetToStrA` | `0x24190` | 127 | UnwindData |  |
| 269 | *Ordinal Only* | `0x24290` | 93 | UnwindData |  |
| 23 | *Ordinal Only* | `0x24300` | 129 | UnwindData |  |
| 35 | *Ordinal Only* | `0x24390` | 280 | UnwindData |  |
| 781 | `SHGetInverseCMAP` | `0x244B0` | 71 | UnwindData |  |
| 867 | `StrFromTimeIntervalA` | `0x24500` | 124 | UnwindData |  |
| 868 | `StrFromTimeIntervalW` | `0x24590` | 124 | UnwindData |  |
| 504 | *Ordinal Only* | `0x24C90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 930 | `wvnsprintfA` | `0x24CC0` | 58 | UnwindData |  |
| 931 | `wvnsprintfW` | `0x24D00` | 63 | UnwindData |  |
| 160 | *Ordinal Only* | `0x24EB0` | 146 | UnwindData |  |
| 435 | *Ordinal Only* | `0x26300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 436 | *Ordinal Only* | `0x26320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | *Ordinal Only* | `0x26340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 546 | *Ordinal Only* | `0x26350` | 146 | UnwindData |  |
| 355 | *Ordinal Only* | `0x263F0` | 398 | UnwindData |  |
| 190 | *Ordinal Only* | `0x26590` | 169 | UnwindData |  |
| 538 | *Ordinal Only* | `0x26640` | 149 | UnwindData |  |
| 539 | *Ordinal Only* | `0x266E0` | 280 | UnwindData |  |
| 575 | *Ordinal Only* | `0x26800` | 235 | UnwindData |  |
| 202 | *Ordinal Only* | `0x26900` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `MLLoadLibraryA` | `0x269D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `MLLoadLibraryW` | `0x269F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | *Ordinal Only* | `0x26A10` | 189 | UnwindData |  |
| 200 | *Ordinal Only* | `0x26AE0` | 138 | UnwindData |  |
| 760 | `SHAutoComplete` | `0x26B70` | 440 | UnwindData |  |
| 537 | *Ordinal Only* | `0x26D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | *Ordinal Only* | `0x26D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | *Ordinal Only* | `0x26D60` | 335 | UnwindData |  |
| 181 | *Ordinal Only* | `0x26EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | *Ordinal Only* | `0x26EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | *Ordinal Only* | `0x26F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | *Ordinal Only* | `0x26F10` | 39 | UnwindData |  |
| 540 | *Ordinal Only* | `0x26F40` | 45 | UnwindData |  |
| 639 | *Ordinal Only* | `0x26F80` | 52 | UnwindData |  |
| 571 | *Ordinal Only* | `0x26FC0` | 230 | UnwindData |  |
| 541 | *Ordinal Only* | `0x270B0` | 58 | UnwindData |  |
| 640 | *Ordinal Only* | `0x270F0` | 70 | UnwindData |  |
| 279 | *Ordinal Only* | `0x27140` | 39 | UnwindData |  |
| 195 | *Ordinal Only* | `0x27170` | 166 | UnwindData |  |
| 785 | `SHIsLowMemoryMachine` | `0x27220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | *Ordinal Only* | `0x27230` | 113 | UnwindData |  |
| 185 | `SHMessageBoxCheckA` | `0x272B0` | 362 | UnwindData |  |
| 291 | *Ordinal Only* | `0x27420` | 288 | UnwindData |  |
| 292 | *Ordinal Only* | `0x27550` | 333 | UnwindData |  |
| 191 | `SHMessageBoxCheckW` | `0x276B0` | 400 | UnwindData |  |
| 183 | *Ordinal Only* | `0x27850` | 120 | UnwindData |  |
| 237 | *Ordinal Only* | `0x278D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | *Ordinal Only* | `0x278F0` | 91 | UnwindData |  |
| 221 | *Ordinal Only* | `0x27960` | 77 | UnwindData |  |
| 384 | *Ordinal Only* | `0x279C0` | 101 | UnwindData |  |
| 198 | *Ordinal Only* | `0x27A30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `SHSendMessageBroadcastA` | `0x27A60` | 37 | UnwindData |  |
| 433 | `SHSendMessageBroadcastW` | `0x27A90` | 37 | UnwindData |  |
| 220 | *Ordinal Only* | `0x27AC0` | 347 | UnwindData |  |
| 186 | *Ordinal Only* | `0x27C30` | 192 | UnwindData |  |
| 203 | `SHStripMneumonicA` | `0x27D00` | 91 | UnwindData |  |
| 238 | *Ordinal Only* | `0x27D70` | 82 | UnwindData |  |
| 518 | *Ordinal Only* | `0x27DD0` | 105 | UnwindData |  |
| 276 | `WhichPlatform` | `0x27E40` | 3,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | *Ordinal Only* | `0x28B90` | 593 | UnwindData |  |
| 583 | *Ordinal Only* | `0x28DF0` | 782 | UnwindData |  |
| 582 | *Ordinal Only* | `0x29110` | 1,192 | UnwindData |  |
| 609 | `DllGetVersion` | `0x2A3A0` | 198 | UnwindData |  |
| 608 | `DllGetClassObject` | `0x2A470` | 65 | UnwindData |  |
| 350 | *Ordinal Only* | `0x2A560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | *Ordinal Only* | `0x2A580` | 41 | UnwindData |  |
| 352 | *Ordinal Only* | `0x2A5B0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | *Ordinal Only* | `0x2A680` | 40 | UnwindData |  |
| 513 | `IStream_WritePidl` | `0x2A6B0` | 128 | UnwindData |  |
| 331 | *Ordinal Only* | `0x2A810` | 142 | UnwindData |  |
| 120 | *Ordinal Only* | `0x2A8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | *Ordinal Only* | `0x2A8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | *Ordinal Only* | `0x2A8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | *Ordinal Only* | `0x2A910` | 67 | UnwindData |  |
| 366 | *Ordinal Only* | `0x2A960` | 67 | UnwindData |  |
| 125 | *Ordinal Only* | `0x2A9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | *Ordinal Only* | `0x2A9D0` | 36 | UnwindData |  |
| 126 | *Ordinal Only* | `0x2AA00` | 121 | UnwindData |  |
| 128 | *Ordinal Only* | `0x2AA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | *Ordinal Only* | `0x2AAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | *Ordinal Only* | `0x2AAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SHAllocShared` | `0x2AAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `SHFreeShared` | `0x2AB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 641 | *Ordinal Only* | `0x2AB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | *Ordinal Only* | `0x2AB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SHLockShared` | `0x2AB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | *Ordinal Only* | `0x2AB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SHUnlockShared` | `0x2ABA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | *Ordinal Only* | `0x2ABC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | *Ordinal Only* | `0x2ABE0` | 133 | UnwindData |  |
| 616 | *Ordinal Only* | `0x2ED80` | 616 | UnwindData |  |
| 549 | *Ordinal Only* | `0x2F160` | 143 | UnwindData |  |
| 626 | *Ordinal Only* | `0x2F670` | 199 | UnwindData |  |
| 472 | *Ordinal Only* | `0x2F740` | 196 | UnwindData |  |
| 477 | *Ordinal Only* | `0x2F960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | *Ordinal Only* | `0x2F980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | *Ordinal Only* | `0x2F9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | *Ordinal Only* | `0x2F9C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | *Ordinal Only* | `0x2F9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | *Ordinal Only* | `0x2FA00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 496 | *Ordinal Only* | `0x2FA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 529 | *Ordinal Only* | `0x2FA40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | *Ordinal Only* | `0x2FA60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 525 | *Ordinal Only* | `0x2FA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | *Ordinal Only* | `0x2FAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 523 | *Ordinal Only* | `0x2FAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | *Ordinal Only* | `0x2FAE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | *Ordinal Only* | `0x2FB00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 567 | `SHPropertyBag_ReadStrAlloc` | `0x2FB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 531 | *Ordinal Only* | `0x2FB40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | *Ordinal Only* | `0x2FB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 577 | *Ordinal Only* | `0x2FB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 636 | *Ordinal Only* | `0x2FBA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | *Ordinal Only* | `0x2FBC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `SHPropertyBag_WriteBSTR` | `0x2FBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | *Ordinal Only* | `0x2FC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 506 | *Ordinal Only* | `0x2FC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 497 | *Ordinal Only* | `0x2FC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | *Ordinal Only* | `0x2FC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | *Ordinal Only* | `0x2FC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | *Ordinal Only* | `0x2FCA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 613 | *Ordinal Only* | `0x2FCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | *Ordinal Only* | `0x2FCE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | *Ordinal Only* | `0x2FD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | *Ordinal Only* | `0x2FD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 532 | *Ordinal Only* | `0x2FD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | *Ordinal Only* | `0x2FD60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 637 | *Ordinal Only* | `0x2FD80` | 33,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 621 | *Ordinal Only* | `0x37EA0` | 355 | UnwindData |  |
| 294 | *Ordinal Only* | `0x382A0` | 160 | UnwindData |  |
| 826 | `SHRegisterValidateTemplate` | `0x388B0` | 282 | UnwindData |  |
| 234 | *Ordinal Only* | `0x389D0` | 37 | UnwindData |  |
| 235 | *Ordinal Only* | `0x38A00` | 172 | UnwindData |  |
| 228 | *Ordinal Only* | `0x38AC0` | 153 | UnwindData |  |
| 230 | *Ordinal Only* | `0x38B60` | 168 | UnwindData |  |
| 232 | *Ordinal Only* | `0x38C10` | 179 | UnwindData |  |
| 229 | *Ordinal Only* | `0x38CD0` | 46 | UnwindData |  |
| 382 | *Ordinal Only* | `0x38D10` | 491 | UnwindData |  |
| 383 | *Ordinal Only* | `0x38F10` | 400 | UnwindData |  |
