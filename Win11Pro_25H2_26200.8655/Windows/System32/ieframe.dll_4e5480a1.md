# Binary Specification: ieframe.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ieframe.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4e5480a122f5ca55c0b849553c42428cf8cfc78052f19acc411829565b09a09f`
* **Total Exported Functions:** 145

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 153 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `iertutil.#900` |
| 256 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `iertutil.#900` |
| 118 | `DllGetClassObject` | `0x9D70` | 705 | UnwindData |  |
| 114 | `SetQueryNetSessionCount` | `0x187E0` | 367 | UnwindData |  |
| 159 | *Ordinal Only* | `0x18D10` | 43 | UnwindData |  |
| 172 | *Ordinal Only* | `0x1EDD0` | 45 | UnwindData |  |
| 218 | *Ordinal Only* | `0x33770` | 1,434 | UnwindData |  |
| 222 | *Ordinal Only* | `0x33D10` | 108 | UnwindData |  |
| 137 | *Ordinal Only* | `0x34910` | 103 | UnwindData |  |
| 117 | `DllCanUnloadNow` | `0x47480` | 131 | UnwindData |  |
| 139 | `IEGetProtectedModeCookie` | `0x4C9D0` | 1,270 | UnwindData |  |
| 319 | *Ordinal Only* | `0x74130` | 167 | UnwindData |  |
| 224 | *Ordinal Only* | `0x7A5D0` | 48,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `IEIsProtectedModeProcess` | `0x86320` | 78 | UnwindData |  |
| 141 | *Ordinal Only* | `0x88010` | 6,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `DllRegisterServer` | `0x89900` | 53,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `DllUnregisterServer` | `0x89900` | 53,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | *Ordinal Only* | `0x96840` | 433 | UnwindData |  |
| 120 | `DllInstall` | `0xA1E60` | 240 | UnwindData |  |
| 316 | *Ordinal Only* | `0xA2340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | *Ordinal Only* | `0xA2350` | 50 | UnwindData |  |
| 303 | *Ordinal Only* | `0xA26E0` | 432 | UnwindData |  |
| 315 | *Ordinal Only* | `0xA3D00` | 74 | UnwindData |  |
| 212 | *Ordinal Only* | `0xA8440` | 312 | UnwindData |  |
| 98 | `IECreateDirectory` | `0xA8630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `IECreateFile` | `0xA8650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `IEDeleteFile` | `0xA8670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `IEFindFirstFile` | `0xA8690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `IEGetFileAttributesEx` | `0xA86B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `IEMoveFileEx` | `0xA86D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `IERemoveDirectory` | `0xA86F0` | 3,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `IECancelSaveFile` | `0xA9410` | 147 | UnwindData |  |
| 140 | `IEGetWriteableFolderPath` | `0xA94B0` | 401 | UnwindData |  |
| 144 | `IEGetWriteableHKCU` | `0xA9650` | 153 | UnwindData |  |
| 146 | `IEIsProtectedModeURL` | `0xA96F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `IELaunchURL` | `0xA9710` | 390 | UnwindData |  |
| 148 | `IERefreshElevationPolicy` | `0xA98A0` | 51 | UnwindData |  |
| 149 | `IERegCreateKeyEx` | `0xA98E0` | 202 | UnwindData |  |
| 154 | `IERegSetValueEx` | `0xA99B0` | 240 | UnwindData |  |
| 155 | `IERegisterWritableRegistryKey` | `0xA9AB0` | 80 | UnwindData |  |
| 156 | `IERegisterWritableRegistryValue` | `0xA9B10` | 121 | UnwindData |  |
| 157 | `IESaveFile` | `0xA9B90` | 327 | UnwindData |  |
| 161 | `IESetProtectedModeCookie` | `0xA9CE0` | 21 | UnwindData |  |
| 164 | `IESetProtectedModeCookieEx` | `0xA9D00` | 848 | UnwindData |  |
| 169 | `IEShowOpenFileDialog` | `0xAA060` | 1,069 | UnwindData |  |
| 171 | `IEShowSaveFileDialog` | `0xAA4A0` | 704 | UnwindData |  |
| 173 | `IEUnregisterWritableRegistry` | `0xAA770` | 141 | UnwindData |  |
| 107 | `IEInPrivateFilteringEnabled` | `0xAB800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `IETrackingProtectionEnabled` | `0xAB800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `IEIsInPrivateBrowsing` | `0xAB810` | 25 | UnwindData |  |
| 162 | *Ordinal Only* | `0xAC010` | 789 | UnwindData |  |
| 166 | *Ordinal Only* | `0xAC330` | 181 | UnwindData |  |
| 142 | *Ordinal Only* | `0xAD090` | 139 | UnwindData |  |
| 135 | *Ordinal Only* | `0xAD150` | 89 | UnwindData |  |
| 160 | *Ordinal Only* | `0xAD710` | 113 | UnwindData |  |
| 176 | `SoftwareUpdateMessageBox` | `0xAD900` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | *Ordinal Only* | `0xADAD0` | 57 | UnwindData |  |
| 223 | *Ordinal Only* | `0xAEAF0` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | *Ordinal Only* | `0xAEE90` | 105 | UnwindData |  |
| 167 | *Ordinal Only* | `0xAEF80` | 59 | UnwindData |  |
| 318 | *Ordinal Only* | `0xAFDF0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | *Ordinal Only* | `0xB0140` | 85 | UnwindData |  |
| 325 | *Ordinal Only* | `0xB01A0` | 23,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | *Ordinal Only* | `0xB5F10` | 317 | UnwindData |  |
| 175 | `OpenURL` | `0xB8480` | 311 | UnwindData |  |
| 257 | *Ordinal Only* | `0xBC830` | 218 | UnwindData |  |
| 115 | `AddUrlToFavorites` | `0xBD600` | 32 | UnwindData |  |
| 123 | `DoAddToFavDlg` | `0xBD630` | 240 | UnwindData |  |
| 124 | `DoAddToFavDlgW` | `0xBD880` | 175 | UnwindData |  |
| 128 | `DoOrganizeFavDlg` | `0xBD940` | 98 | UnwindData |  |
| 129 | `DoOrganizeFavDlgW` | `0xBD9B0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | *Ordinal Only* | `0xBDA60` | 991 | UnwindData |  |
| 163 | `SHAddSubscribeFavorite` | `0xBDEA0` | 23 | UnwindData |  |
| 152 | *Ordinal Only* | `0xC3A20` | 228 | UnwindData |  |
| 211 | *Ordinal Only* | `0xCAED0` | 210 | UnwindData |  |
| 259 | *Ordinal Only* | `0xD2820` | 74 | UnwindData |  |
| 125 | `DoBlobDownload` | `0xD2870` | 403 | UnwindData |  |
| 126 | `DoFileDownload` | `0xD2A10` | 171 | UnwindData |  |
| 127 | `DoFileDownloadEx` | `0xD2AD0` | 388 | UnwindData |  |
| 177 | `TriggerFileDownload` | `0xD2C60` | 182 | UnwindData |  |
| 234 | *Ordinal Only* | `0xD33D0` | 122 | UnwindData |  |
| 233 | *Ordinal Only* | `0xD3450` | 29 | UnwindData |  |
| 232 | *Ordinal Only* | `0xD3480` | 37 | UnwindData |  |
| 231 | *Ordinal Only* | `0xD34B0` | 295 | UnwindData |  |
| 265 | *Ordinal Only* | `0xDBFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | *Ordinal Only* | `0xDBFD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | *Ordinal Only* | `0xDC000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | *Ordinal Only* | `0xDC010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | *Ordinal Only* | `0xDC020` | 6,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | *Ordinal Only* | `0xDD860` | 469 | UnwindData |  |
| 103 | *Ordinal Only* | `0xDDA40` | 267 | UnwindData |  |
| 199 | *Ordinal Only* | `0xE4170` | 97 | UnwindData |  |
| 130 | `DoPrivacyDlg` | `0xE68A0` | 221 | UnwindData |  |
| 333 | *Ordinal Only* | `0xE8880` | 149 | UnwindData |  |
| 332 | *Ordinal Only* | `0xE8920` | 175 | UnwindData |  |
| 131 | `HlinkFindFrame` | `0xEA340` | 94 | UnwindData |  |
| 132 | `HlinkFrameNavigate` | `0xFB810` | 404 | UnwindData |  |
| 133 | `HlinkFrameNavigateNHL` | `0xFB9B0` | 728 | UnwindData |  |
| 236 | *Ordinal Only* | `0xFE7D0` | 137 | UnwindData |  |
| 240 | *Ordinal Only* | `0xFE860` | 205 | UnwindData |  |
| 329 | *Ordinal Only* | `0x105B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | *Ordinal Only* | `0x105B20` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | *Ordinal Only* | `0x105ED0` | 1,030 | UnwindData |  |
| 174 | `ImportPrivacySettings` | `0x107F30` | 194 | UnwindData |  |
| 331 | *Ordinal Only* | `0x11DD30` | 241 | UnwindData |  |
| 243 | *Ordinal Only* | `0x11E5C0` | 351 | UnwindData |  |
| 150 | *Ordinal Only* | `0x133FF0` | 25 | UnwindData |  |
| 93 | *Ordinal Only* | `0x17FFE0` | 188,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | *Ordinal Only* | `0x1ADFD0` | 46 | UnwindData |  |
| 168 | *Ordinal Only* | `0x1B3BE0` | 447 | UnwindData |  |
| 258 | *Ordinal Only* | `0x1B8820` | 60 | UnwindData |  |
| 255 | *Ordinal Only* | `0x1B8870` | 53 | UnwindData |  |
| 251 | *Ordinal Only* | `0x1B88B0` | 283 | UnwindData |  |
| 253 | *Ordinal Only* | `0x1B9130` | 181 | UnwindData |  |
| 254 | *Ordinal Only* | `0x1B9350` | 447 | UnwindData |  |
| 252 | *Ordinal Only* | `0x1B9F00` | 197 | UnwindData |  |
| 241 | *Ordinal Only* | `0x1BB210` | 16,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | *Ordinal Only* | `0x1BF400` | 34 | UnwindData |  |
| 134 | `IEAssociateThreadWithTab` | `0x1C4980` | 166 | UnwindData |  |
| 138 | `IEDisassociateThreadWithTab` | `0x1C4A30` | 151 | UnwindData |  |
| 244 | *Ordinal Only* | `0x1C5230` | 348 | UnwindData |  |
| 245 | *Ordinal Only* | `0x1C53A0` | 174 | UnwindData |  |
| 246 | *Ordinal Only* | `0x1C5460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | *Ordinal Only* | `0x1C5470` | 11,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | *Ordinal Only* | `0x1C8260` | 228 | UnwindData |  |
| 242 | *Ordinal Only* | `0x1C8D80` | 6,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | *Ordinal Only* | `0x1CA610` | 183 | UnwindData |  |
| 92 | *Ordinal Only* | `0x1CE340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | *Ordinal Only* | `0x1CE350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | *Ordinal Only* | `0x1CE360` | 40 | UnwindData |  |
| 95 | *Ordinal Only* | `0x1CE390` | 50 | UnwindData |  |
| 96 | `CreateExtensionGuidEnumerator` | `0x3EF5B0` | 65 | UnwindData |  |
| 109 | `IELaunchManageAddOnsUI` | `0x3F0FF0` | 2,975 | UnwindData |  |
| 116 | `CORLockDownProvider` | `0x41DDC0` | 250 | UnwindData |  |
| 119 | `DllGetVersion` | `0x41E920` | 211 | UnwindData |  |
| 170 | *Ordinal Only* | `0x423080` | 200 | UnwindData |  |
| 178 | `URLQualifyA` | `0x4233C0` | 223 | UnwindData |  |
| 179 | `URLQualifyW` | `0x4234B0` | 147 | UnwindData |  |
| 165 | *Ordinal Only* | `0x423550` | 588 | UnwindData |  |
| 328 | *Ordinal Only* | `0x424BD0` | 42 | UnwindData |  |
| 97 | `ExportCookieFileByProcessW` | `0x42F0B0` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `ImportCookieFileByProcessW` | `0x42FCF0` | 1,235,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | *Ordinal Only* | `0x55D5D0` | 125 | UnwindData |  |
| 151 | *Ordinal Only* | `0x55D660` | 207 | UnwindData |  |
| 238 | *Ordinal Only* | `0x55D740` | 215 | UnwindData |  |
