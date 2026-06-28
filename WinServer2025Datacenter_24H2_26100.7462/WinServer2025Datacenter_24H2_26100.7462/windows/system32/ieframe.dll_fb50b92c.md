# Binary Specification: ieframe.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ieframe.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fb50b92c6989eb67499d46a84597d3b2b3b279ebcc172c710cab5fc0671e884e`
* **Total Exported Functions:** 145

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 153 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `iertutil.#900` |
| 256 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `iertutil.#900` |
| 118 | `DllGetClassObject` | `0x9D60` | 705 | UnwindData |  |
| 114 | `SetQueryNetSessionCount` | `0x187D0` | 367 | UnwindData |  |
| 159 | *Ordinal Only* | `0x18D00` | 43 | UnwindData |  |
| 172 | *Ordinal Only* | `0x1EDC0` | 45 | UnwindData |  |
| 218 | *Ordinal Only* | `0x33760` | 1,434 | UnwindData |  |
| 222 | *Ordinal Only* | `0x33D00` | 108 | UnwindData |  |
| 137 | *Ordinal Only* | `0x34900` | 103 | UnwindData |  |
| 117 | `DllCanUnloadNow` | `0x47470` | 131 | UnwindData |  |
| 139 | `IEGetProtectedModeCookie` | `0x4C9C0` | 1,270 | UnwindData |  |
| 319 | *Ordinal Only* | `0x74230` | 167 | UnwindData |  |
| 224 | *Ordinal Only* | `0x7A750` | 48,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `IEIsProtectedModeProcess` | `0x86510` | 78 | UnwindData |  |
| 141 | *Ordinal Only* | `0x882A0` | 6,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `DllRegisterServer` | `0x89B90` | 53,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `DllUnregisterServer` | `0x89B90` | 53,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | *Ordinal Only* | `0x96AD0` | 433 | UnwindData |  |
| 120 | `DllInstall` | `0xA2020` | 240 | UnwindData |  |
| 316 | *Ordinal Only* | `0xA2500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | *Ordinal Only* | `0xA2510` | 50 | UnwindData |  |
| 303 | *Ordinal Only* | `0xA28A0` | 432 | UnwindData |  |
| 315 | *Ordinal Only* | `0xA3EC0` | 74 | UnwindData |  |
| 212 | *Ordinal Only* | `0xA8600` | 312 | UnwindData |  |
| 98 | `IECreateDirectory` | `0xA87F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `IECreateFile` | `0xA8810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `IEDeleteFile` | `0xA8830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `IEFindFirstFile` | `0xA8850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `IEGetFileAttributesEx` | `0xA8870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `IEMoveFileEx` | `0xA8890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `IERemoveDirectory` | `0xA88B0` | 3,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `IECancelSaveFile` | `0xA95D0` | 147 | UnwindData |  |
| 140 | `IEGetWriteableFolderPath` | `0xA9670` | 401 | UnwindData |  |
| 144 | `IEGetWriteableHKCU` | `0xA9810` | 153 | UnwindData |  |
| 146 | `IEIsProtectedModeURL` | `0xA98B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `IELaunchURL` | `0xA98D0` | 390 | UnwindData |  |
| 148 | `IERefreshElevationPolicy` | `0xA9A60` | 51 | UnwindData |  |
| 149 | `IERegCreateKeyEx` | `0xA9AA0` | 202 | UnwindData |  |
| 154 | `IERegSetValueEx` | `0xA9B70` | 240 | UnwindData |  |
| 155 | `IERegisterWritableRegistryKey` | `0xA9C70` | 80 | UnwindData |  |
| 156 | `IERegisterWritableRegistryValue` | `0xA9CD0` | 121 | UnwindData |  |
| 157 | `IESaveFile` | `0xA9D50` | 327 | UnwindData |  |
| 161 | `IESetProtectedModeCookie` | `0xA9EA0` | 21 | UnwindData |  |
| 164 | `IESetProtectedModeCookieEx` | `0xA9EC0` | 848 | UnwindData |  |
| 169 | `IEShowOpenFileDialog` | `0xAA220` | 1,069 | UnwindData |  |
| 171 | `IEShowSaveFileDialog` | `0xAA660` | 704 | UnwindData |  |
| 173 | `IEUnregisterWritableRegistry` | `0xAA930` | 141 | UnwindData |  |
| 107 | `IEInPrivateFilteringEnabled` | `0xAB9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `IETrackingProtectionEnabled` | `0xAB9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `IEIsInPrivateBrowsing` | `0xAB9D0` | 25 | UnwindData |  |
| 162 | *Ordinal Only* | `0xAC1D0` | 789 | UnwindData |  |
| 166 | *Ordinal Only* | `0xAC4F0` | 181 | UnwindData |  |
| 142 | *Ordinal Only* | `0xAD250` | 139 | UnwindData |  |
| 135 | *Ordinal Only* | `0xAD310` | 89 | UnwindData |  |
| 160 | *Ordinal Only* | `0xAD8D0` | 113 | UnwindData |  |
| 176 | `SoftwareUpdateMessageBox` | `0xADAC0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | *Ordinal Only* | `0xADC90` | 57 | UnwindData |  |
| 223 | *Ordinal Only* | `0xAECB0` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | *Ordinal Only* | `0xAF050` | 105 | UnwindData |  |
| 167 | *Ordinal Only* | `0xAF140` | 59 | UnwindData |  |
| 318 | *Ordinal Only* | `0xAFFB0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | *Ordinal Only* | `0xB0300` | 85 | UnwindData |  |
| 325 | *Ordinal Only* | `0xB0360` | 23,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | *Ordinal Only* | `0xB5F50` | 317 | UnwindData |  |
| 175 | `OpenURL` | `0xB84B0` | 311 | UnwindData |  |
| 257 | *Ordinal Only* | `0xBC860` | 218 | UnwindData |  |
| 115 | `AddUrlToFavorites` | `0xBD630` | 32 | UnwindData |  |
| 123 | `DoAddToFavDlg` | `0xBD660` | 240 | UnwindData |  |
| 124 | `DoAddToFavDlgW` | `0xBD8B0` | 175 | UnwindData |  |
| 128 | `DoOrganizeFavDlg` | `0xBD970` | 98 | UnwindData |  |
| 129 | `DoOrganizeFavDlgW` | `0xBD9E0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | *Ordinal Only* | `0xBDA90` | 991 | UnwindData |  |
| 163 | `SHAddSubscribeFavorite` | `0xBDED0` | 23 | UnwindData |  |
| 152 | *Ordinal Only* | `0xC3A50` | 228 | UnwindData |  |
| 211 | *Ordinal Only* | `0xCAF00` | 210 | UnwindData |  |
| 259 | *Ordinal Only* | `0xD2850` | 74 | UnwindData |  |
| 125 | `DoBlobDownload` | `0xD28A0` | 403 | UnwindData |  |
| 126 | `DoFileDownload` | `0xD2A40` | 171 | UnwindData |  |
| 127 | `DoFileDownloadEx` | `0xD2B00` | 388 | UnwindData |  |
| 177 | `TriggerFileDownload` | `0xD2C90` | 182 | UnwindData |  |
| 234 | *Ordinal Only* | `0xD3400` | 122 | UnwindData |  |
| 233 | *Ordinal Only* | `0xD3480` | 29 | UnwindData |  |
| 232 | *Ordinal Only* | `0xD34B0` | 37 | UnwindData |  |
| 231 | *Ordinal Only* | `0xD34E0` | 295 | UnwindData |  |
| 265 | *Ordinal Only* | `0xDBFF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | *Ordinal Only* | `0xDC000` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | *Ordinal Only* | `0xDC030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | *Ordinal Only* | `0xDC040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | *Ordinal Only* | `0xDC050` | 6,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | *Ordinal Only* | `0xDD890` | 469 | UnwindData |  |
| 103 | *Ordinal Only* | `0xDDA70` | 267 | UnwindData |  |
| 199 | *Ordinal Only* | `0xE41A0` | 97 | UnwindData |  |
| 130 | `DoPrivacyDlg` | `0xE68D0` | 221 | UnwindData |  |
| 333 | *Ordinal Only* | `0xE88B0` | 149 | UnwindData |  |
| 332 | *Ordinal Only* | `0xE8950` | 175 | UnwindData |  |
| 131 | `HlinkFindFrame` | `0xEA370` | 94 | UnwindData |  |
| 132 | `HlinkFrameNavigate` | `0xFB5B0` | 404 | UnwindData |  |
| 133 | `HlinkFrameNavigateNHL` | `0xFB750` | 728 | UnwindData |  |
| 236 | *Ordinal Only* | `0xFFEF0` | 137 | UnwindData |  |
| 240 | *Ordinal Only* | `0xFFF80` | 205 | UnwindData |  |
| 329 | *Ordinal Only* | `0x107620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | *Ordinal Only* | `0x107630` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | *Ordinal Only* | `0x1079E0` | 1,030 | UnwindData |  |
| 174 | `ImportPrivacySettings` | `0x109A40` | 194 | UnwindData |  |
| 331 | *Ordinal Only* | `0x11FB80` | 241 | UnwindData |  |
| 243 | *Ordinal Only* | `0x120410` | 351 | UnwindData |  |
| 150 | *Ordinal Only* | `0x135F50` | 25 | UnwindData |  |
| 93 | *Ordinal Only* | `0x181BB0` | 188,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | *Ordinal Only* | `0x1AFD50` | 46 | UnwindData |  |
| 168 | *Ordinal Only* | `0x1B59A0` | 447 | UnwindData |  |
| 258 | *Ordinal Only* | `0x1BA5D0` | 60 | UnwindData |  |
| 255 | *Ordinal Only* | `0x1BA620` | 53 | UnwindData |  |
| 251 | *Ordinal Only* | `0x1BA660` | 283 | UnwindData |  |
| 253 | *Ordinal Only* | `0x1BAEE0` | 181 | UnwindData |  |
| 254 | *Ordinal Only* | `0x1BB100` | 447 | UnwindData |  |
| 252 | *Ordinal Only* | `0x1BBCB0` | 197 | UnwindData |  |
| 241 | *Ordinal Only* | `0x1BCFC0` | 16,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | *Ordinal Only* | `0x1C11B0` | 34 | UnwindData |  |
| 134 | `IEAssociateThreadWithTab` | `0x1C6730` | 166 | UnwindData |  |
| 138 | `IEDisassociateThreadWithTab` | `0x1C67E0` | 151 | UnwindData |  |
| 244 | *Ordinal Only* | `0x1C6FE0` | 348 | UnwindData |  |
| 245 | *Ordinal Only* | `0x1C7150` | 174 | UnwindData |  |
| 246 | *Ordinal Only* | `0x1C7210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | *Ordinal Only* | `0x1C7220` | 11,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | *Ordinal Only* | `0x1CA010` | 228 | UnwindData |  |
| 242 | *Ordinal Only* | `0x1CAB30` | 6,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | *Ordinal Only* | `0x1CC3C0` | 183 | UnwindData |  |
| 92 | *Ordinal Only* | `0x1D00F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | *Ordinal Only* | `0x1D0100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | *Ordinal Only* | `0x1D0110` | 40 | UnwindData |  |
| 95 | *Ordinal Only* | `0x1D0140` | 50 | UnwindData |  |
| 96 | `CreateExtensionGuidEnumerator` | `0x3F23A0` | 65 | UnwindData |  |
| 109 | `IELaunchManageAddOnsUI` | `0x3F3DE0` | 2,975 | UnwindData |  |
| 116 | `CORLockDownProvider` | `0x420BB0` | 250 | UnwindData |  |
| 119 | `DllGetVersion` | `0x421710` | 211 | UnwindData |  |
| 170 | *Ordinal Only* | `0x425E70` | 200 | UnwindData |  |
| 178 | `URLQualifyA` | `0x4261B0` | 223 | UnwindData |  |
| 179 | `URLQualifyW` | `0x4262A0` | 147 | UnwindData |  |
| 165 | *Ordinal Only* | `0x426340` | 588 | UnwindData |  |
| 328 | *Ordinal Only* | `0x4279C0` | 42 | UnwindData |  |
| 97 | `ExportCookieFileByProcessW` | `0x431EA0` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `ImportCookieFileByProcessW` | `0x432AE0` | 1,240,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | *Ordinal Only* | `0x561A60` | 125 | UnwindData |  |
| 151 | *Ordinal Only* | `0x561AF0` | 207 | UnwindData |  |
| 238 | *Ordinal Only* | `0x561BD0` | 215 | UnwindData |  |
