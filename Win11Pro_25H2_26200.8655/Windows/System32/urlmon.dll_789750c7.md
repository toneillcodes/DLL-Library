# Binary Specification: urlmon.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\urlmon.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `789750c7ed748155c0ad2ccdeb33ba231f5e3183901e88e042b39fe1e9c5e958`
* **Total Exported Functions:** 318

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 156 | `CopyBindInfo` | `0x4C30` | 778 | UnwindData |  |
| 217 | `ReleaseBindInfo` | `0x5B40` | 127 | UnwindData |  |
| 142 | `CoInternetGetSecurityUrlEx` | `0xD350` | 214 | UnwindData |  |
| 509 | *Ordinal Only* | `0xE2E0` | 44 | UnwindData |  |
| 149 | `CoInternetParseUrl` | `0xF100` | 1,336 | UnwindData |  |
| 207 | `MkParseDisplayNameEx` | `0x10540` | 461 | UnwindData |  |
| 163 | `CreateURLMonikerEx` | `0x10720` | 15 | UnwindData |  |
| 219 | `RevokeBindStatusCallback` | `0x11C30` | 531 | UnwindData |  |
| 212 | `RegisterBindStatusCallback` | `0x11F50` | 806 | UnwindData |  |
| 162 | `CreateURLMoniker` | `0x126C0` | 18 | UnwindData |  |
| 164 | `CreateURLMonikerEx2` | `0x126E0` | 20 | UnwindData |  |
| 159 | `CreateAsyncBindCtxEx` | `0x129C0` | 238 | UnwindData |  |
| 445 | *Ordinal Only* | `0x22380` | 1,308 | UnwindData |  |
| 184 | `GetIDNFlagsForUri` | `0x30090` | 145 | UnwindData |  |
| 154 | `CompareSecurityIds` | `0x32E90` | 99 | UnwindData |  |
| 240 | `UrlMkGetSessionOption` | `0x35DE0` | 394 | UnwindData |  |
| 208 | `ObtainUserAgentString` | `0x36CA0` | 429 | UnwindData |  |
| 565 | *Ordinal Only* | `0x37A90` | 139 | UnwindData |  |
| 443 | *Ordinal Only* | `0x37E10` | 375 | UnwindData |  |
| 177 | `FindMediaType` | `0x3AD80` | 310 | UnwindData |  |
| 179 | `FindMimeFromData` | `0x3B950` | 1,508 | UnwindData |  |
| 144 | `CoInternetIsFeatureEnabled` | `0x3DC50` | 33 | UnwindData |  |
| 492 | *Ordinal Only* | `0x43430` | 1,329 | UnwindData |  |
| 499 | *Ordinal Only* | `0x492E0` | 273 | UnwindData |  |
| 206 | `IsValidURL` | `0x58DD0` | 3,117 | UnwindData |  |
| 150 | `CoInternetQueryInfo` | `0x5B230` | 1,210 | UnwindData |  |
| 520 | *Ordinal Only* | `0x5DD80` | 380 | UnwindData |  |
| 135 | `CoInternetCreateSecurityManager` | `0x5E2A0` | 954 | UnwindData |  |
| 108 | *Ordinal Only* | `0x5EE90` | 297 | UnwindData |  |
| 504 | *Ordinal Only* | `0x64AD0` | 987 | UnwindData |  |
| 503 | *Ordinal Only* | `0x66740` | 459 | UnwindData |  |
| 441 | *Ordinal Only* | `0x67880` | 140 | UnwindData |  |
| 132 | `CoInternetCombineUrl` | `0x69CA0` | 2,255 | UnwindData |  |
| 518 | *Ordinal Only* | `0x6DEF0` | 850 | UnwindData |  |
| 131 | `CoInternetCombineIUri` | `0x72740` | 422 | UnwindData |  |
| 403 | *Ordinal Only* | `0x73240` | 3,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | *Ordinal Only* | `0x73240` | 3,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | *Ordinal Only* | `0x73240` | 3,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | *Ordinal Only* | `0x73240` | 3,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `GetZoneFromAlternateDataStreamEx` | `0x740B0` | 237 | UnwindData |  |
| 603 | *Ordinal Only* | `0x752D0` | 398 | UnwindData |  |
| 133 | `CoInternetCombineUrlEx` | `0x76940` | 25 | UnwindData |  |
| 521 | *Ordinal Only* | `0x76E90` | 377 | UnwindData |  |
| 519 | *Ordinal Only* | `0x776B0` | 384 | UnwindData |  |
| 536 | *Ordinal Only* | `0x78C80` | 247 | UnwindData |  |
| 148 | `CoInternetParseIUri` | `0x7A1A0` | 228 | UnwindData |  |
| 449 | *Ordinal Only* | `0x7C5C0` | 208 | UnwindData |  |
| 446 | *Ordinal Only* | `0x7DAB0` | 166 | UnwindData |  |
| 170 | `DllGetClassObject` | `0x7E1E0` | 156 | UnwindData |  |
| 143 | `CoInternetGetSession` | `0x7FB50` | 181 | UnwindData |  |
| 165 | `CreateUri` | `0x81260` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `CoInternetIsFeatureEnabledForIUri` | `0x81310` | 258 | UnwindData |  |
| 109 | `FileBearsMarkOfTheWeb` | `0x816E0` | 1,398 | UnwindData |  |
| 157 | `CopyStgMedium` | `0x82190` | 452 | UnwindData |  |
| 121 | `AsyncGetClassBits` | `0x85840` | 127 | UnwindData |  |
| 169 | `DllCanUnloadNow` | `0x87090` | 6,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | *Ordinal Only* | `0x88A10` | 170 | UnwindData |  |
| 176 | `FaultInIEFeature` | `0x8AC30` | 619 | UnwindData |  |
| 511 | *Ordinal Only* | `0x8B700` | 455 | UnwindData |  |
| 471 | *Ordinal Only* | `0x8CC80` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `CreateIUriBuilder` | `0x8CE20` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | *Ordinal Only* | `0x8D330` | 235 | UnwindData |  |
| 442 | *Ordinal Only* | `0x8D610` | 1,567 | UnwindData |  |
| 160 | `CreateFormatEnumerator` | `0x8DD00` | 48 | UnwindData |  |
| 105 | *Ordinal Only* | `0x911E0` | 834 | UnwindData |  |
| 241 | `UrlMkSetSessionOption` | `0x917D0` | 625 | UnwindData |  |
| 151 | `CoInternetSetFeatureEnabled` | `0x91C30` | 353 | UnwindData |  |
| 553 | *Ordinal Only* | `0x92E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `CoInternetCreateZoneManager` | `0x92EA0` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | *Ordinal Only* | `0x93320` | 81 | UnwindData |  |
| 555 | *Ordinal Only* | `0x95450` | 61 | UnwindData |  |
| 577 | *Ordinal Only* | `0x954A0` | 100 | UnwindData |  |
| 571 | *Ordinal Only* | `0x97300` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | *Ordinal Only* | `0x97500` | 153 | UnwindData |  |
| 570 | *Ordinal Only* | `0x97F20` | 75 | UnwindData |  |
| 488 | *Ordinal Only* | `0x98470` | 140 | UnwindData |  |
| 486 | *Ordinal Only* | `0x98640` | 135 | UnwindData |  |
| 201 | `IsAsyncMoniker` | `0x98C20` | 86 | UnwindData |  |
| 146 | `CoInternetIsFeatureEnabledForUrl` | `0x98C80` | 91 | UnwindData |  |
| 484 | *Ordinal Only* | `0x98DF0` | 312 | UnwindData |  |
| 233 | `URLOpenBlockingStreamW` | `0x99E50` | 251 | UnwindData |  |
| 485 | *Ordinal Only* | `0x9A100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | *Ordinal Only* | `0x9A110` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `GetIUriPriv` | `0x9A450` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 489 | *Ordinal Only* | `0x9AEB0` | 249 | UnwindData |  |
| 155 | `CompatFlagsFromClsid` | `0x9B010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `ShouldShowIntranetWarningSecband` | `0x9B030` | 277 | UnwindData |  |
| 533 | *Ordinal Only* | `0x9BB00` | 94 | UnwindData |  |
| 213 | `RegisterFormatEnumerator` | `0x9C5C0` | 42 | UnwindData |  |
| 507 | *Ordinal Only* | `0x9C7D0` | 170 | UnwindData |  |
| 506 | *Ordinal Only* | `0x9C900` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | *Ordinal Only* | `0x9CDE0` | 41 | UnwindData |  |
| 498 | *Ordinal Only* | `0x9CEE0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `RestrictHTTP2` | `0x9CF60` | 13,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | *Ordinal Only* | `0xA0450` | 46 | UnwindData |  |
| 493 | *Ordinal Only* | `0xA3960` | 138 | UnwindData |  |
| 242 | `UrlmonCleanupCurrentThread` | `0xA3DF0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `RegisterMediaTypes` | `0xA3EA0` | 126 | UnwindData |  |
| 461 | *Ordinal Only* | `0xA43A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | *Ordinal Only* | `0xA43B0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | *Ordinal Only* | `0xA45D0` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | *Ordinal Only* | `0xA45D0` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | *Ordinal Only* | `0xA45D0` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | *Ordinal Only* | `0xA4EA0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `IsJITInProgress` | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | *Ordinal Only* | `0xA4FF0` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `GetPortFromUrlScheme` | `0xA8D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `GetPropertyFromName` | `0xA8D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `GetPropertyName` | `0xA8D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `IsDWORDProperty` | `0xA8DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `IsStringProperty` | `0xA8DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `CreateUriFromMultiByteString` | `0xA8DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `CreateUriPriv` | `0xA8E00` | 67 | UnwindData |  |
| 168 | `CreateUriWithFragment` | `0xA8E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `GetIUriPriv2` | `0xA8E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `IntlPercentEncodeNormalize` | `0xA8E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `BindAsyncMoniker` | `0xA8EB0` | 157 | UnwindData |  |
| 158 | `CreateAsyncBindCtx` | `0xA8F60` | 239 | UnwindData |  |
| 178 | `FindMediaTypeClass` | `0xA9060` | 177 | UnwindData |  |
| 140 | `CoInternetGetProtocolFlags` | `0xA9120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `DllRegisterServerEx` | `0xA9120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `GetClassURL` | `0xA9120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `GetSoftwareUpdateInfo` | `0xA9120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `SetSoftwareUpdateAdvertisementState` | `0xA9120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `RegisterMediaTypeClass` | `0xA9130` | 259 | UnwindData |  |
| 220 | `RevokeFormatEnumerator` | `0xA9240` | 39 | UnwindData |  |
| 457 | *Ordinal Only* | `0xA9270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `DllInstall` | `0xA9290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `DllRegisterServer` | `0xA92A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `DllUnregisterServer` | `0xA92B0` | 61 | UnwindData |  |
| 239 | `UrlMkBuildVersion` | `0xA9300` | 8,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `CoInternetGetMobileBrowserAppCompatMode` | `0xAB5F0` | 92 | UnwindData |  |
| 139 | `CoInternetGetMobileBrowserForceDesktopMode` | `0xAB660` | 33 | UnwindData |  |
| 447 | *Ordinal Only* | `0xAB690` | 111 | UnwindData |  |
| 152 | `CoInternetSetMobileBrowserAppCompatMode` | `0xAB710` | 61 | UnwindData |  |
| 153 | `CoInternetSetMobileBrowserForceDesktopMode` | `0xAB760` | 26 | UnwindData |  |
| 564 | *Ordinal Only* | `0xABA40` | 136 | UnwindData |  |
| 451 | *Ordinal Only* | `0xABAD0` | 118 | UnwindData |  |
| 450 | *Ordinal Only* | `0xABB50` | 301 | UnwindData |  |
| 545 | *Ordinal Only* | `0xABC90` | 223 | UnwindData |  |
| 524 | *Ordinal Only* | `0xABD80` | 127 | UnwindData |  |
| 576 | *Ordinal Only* | `0xABE10` | 117 | UnwindData |  |
| 510 | *Ordinal Only* | `0xABE90` | 170 | UnwindData |  |
| 547 | *Ordinal Only* | `0xABF40` | 53 | UnwindData |  |
| 548 | *Ordinal Only* | `0xABF80` | 155 | UnwindData |  |
| 543 | *Ordinal Only* | `0xAC030` | 166 | UnwindData |  |
| 566 | *Ordinal Only* | `0xAC0E0` | 587 | UnwindData |  |
| 546 | *Ordinal Only* | `0xAC3F0` | 54 | UnwindData |  |
| 527 | *Ordinal Only* | `0xAC430` | 114 | UnwindData |  |
| 574 | *Ordinal Only* | `0xAC4B0` | 117 | UnwindData |  |
| 512 | *Ordinal Only* | `0xAC530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | *Ordinal Only* | `0xAC550` | 114 | UnwindData |  |
| 452 | *Ordinal Only* | `0xACA80` | 230 | UnwindData |  |
| 448 | *Ordinal Only* | `0xACB70` | 259 | UnwindData |  |
| 567 | *Ordinal Only* | `0xB1F90` | 724 | UnwindData |  |
| 122 | `AsyncInstallDistributionUnit` | `0xB96A0` | 127 | UnwindData |  |
| 128 | `CoGetClassObjectFromURL` | `0xB9730` | 94 | UnwindData |  |
| 490 | *Ordinal Only* | `0xB97A0` | 1,269 | UnwindData |  |
| 129 | `CoInstall` | `0xB9CA0` | 151 | UnwindData |  |
| 199 | `IEInstallScope` | `0xB9D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `PrivateCoInstall` | `0xB9D50` | 300 | UnwindData |  |
| 125 | `CDLGetLongPathNameA` | `0xBA020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `CDLGetLongPathNameW` | `0xBA040` | 7,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `Extract` | `0xBBC10` | 370 | UnwindData |  |
| 183 | `GetComponentIDFromCLSSPEC` | `0xBCE00` | 97 | UnwindData |  |
| 470 | *Ordinal Only* | `0xDCB70` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `CAuthenticateHostUI_CreateInstance` | `0xDD040` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | *Ordinal Only* | `0xDD100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `ShouldDisplayPunycodeForUri` | `0xDD110` | 108 | UnwindData |  |
| 568 | *Ordinal Only* | `0xE4E40` | 239 | UnwindData |  |
| 569 | *Ordinal Only* | `0xE4F40` | 58 | UnwindData |  |
| 210 | `QueryAssociations` | `0xF0970` | 241 | UnwindData |  |
| 211 | `QueryClsidAssociation` | `0xF0A70` | 200 | UnwindData |  |
| 462 | *Ordinal Only* | `0xF15D0` | 111 | UnwindData |  |
| 463 | *Ordinal Only* | `0xF1650` | 109 | UnwindData |  |
| 460 | *Ordinal Only* | `0xF16D0` | 25 | UnwindData |  |
| 130 | `CoInternetCanonicalizeIUri` | `0xF2590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | *Ordinal Only* | `0xF25A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `CoInternetCompareUrl` | `0xF25B0` | 178 | UnwindData |  |
| 141 | `CoInternetGetSecurityUrl` | `0xF2670` | 1,050 | UnwindData |  |
| 147 | `CoInternetIsFeatureZoneElevationEnabled` | `0xF2A90` | 640 | UnwindData |  |
| 604 | *Ordinal Only* | `0xF2D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `GetClassFileOrMime` | `0xF2D30` | 54 | UnwindData |  |
| 602 | *Ordinal Only* | `0xF2D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `URLDownloadA` | `0xF2D80` | 91 | UnwindData |  |
| 231 | `URLDownloadW` | `0xF2DF0` | 633 | UnwindData |  |
| 190 | `GetUrlmonThreadNotificationHwnd` | `0xF3600` | 82 | UnwindData |  |
| 324 | *Ordinal Only* | `0xF46A0` | 121 | UnwindData |  |
| 192 | `HlinkGoBack` | `0xFC3B0` | 189 | UnwindData |  |
| 193 | `HlinkGoForward` | `0xFC480` | 189 | UnwindData |  |
| 194 | `HlinkNavigateMoniker` | `0xFC550` | 123 | UnwindData |  |
| 195 | `HlinkNavigateString` | `0xFC5E0` | 123 | UnwindData |  |
| 196 | `HlinkSimpleNavigateToMoniker` | `0xFC670` | 1,668 | UnwindData |  |
| 197 | `HlinkSimpleNavigateToString` | `0xFCD00` | 253 | UnwindData |  |
| 227 | `URLDownloadToCacheFileA` | `0xFE0F0` | 381 | UnwindData |  |
| 228 | `URLDownloadToCacheFileW` | `0xFE280` | 351 | UnwindData |  |
| 229 | `URLDownloadToFileA` | `0xFE3F0` | 343 | UnwindData |  |
| 230 | `URLDownloadToFileW` | `0xFE550` | 247 | UnwindData |  |
| 232 | `URLOpenBlockingStreamA` | `0xFE650` | 222 | UnwindData |  |
| 234 | `URLOpenPullStreamA` | `0xFE740` | 195 | UnwindData |  |
| 235 | `URLOpenPullStreamW` | `0xFE810` | 190 | UnwindData |  |
| 236 | `URLOpenStreamA` | `0xFE8E0` | 195 | UnwindData |  |
| 237 | `URLOpenStreamW` | `0xFE9B0` | 190 | UnwindData |  |
| 204 | `IsLoggingEnabledA` | `0xFEA80` | 120 | UnwindData |  |
| 243 | `WriteHitLogging` | `0xFEB00` | 200 | UnwindData |  |
| 205 | `IsLoggingEnabledW` | `0xFEBD0` | 216 | UnwindData |  |
| 316 | *Ordinal Only* | `0xFF730` | 165 | UnwindData |  |
| 311 | *Ordinal Only* | `0xFF7E0` | 112 | UnwindData |  |
| 322 | `IECompatLogCSSFix` | `0xFF8F0` | 211 | UnwindData |  |
| 321 | *Ordinal Only* | `0xFF9D0` | 75 | UnwindData |  |
| 312 | *Ordinal Only* | `0xFFA30` | 315 | UnwindData |  |
| 307 | *Ordinal Only* | `0xFFB80` | 186 | UnwindData |  |
| 437 | *Ordinal Only* | `0xFFC40` | 97 | UnwindData |  |
| 436 | *Ordinal Only* | `0xFFCB0` | 82 | UnwindData |  |
| 306 | *Ordinal Only* | `0xFFD10` | 49 | UnwindData |  |
| 435 | *Ordinal Only* | `0xFFD50` | 124 | UnwindData |  |
| 439 | *Ordinal Only* | `0xFFDE0` | 56 | UnwindData |  |
| 309 | *Ordinal Only* | `0xFFE20` | 49 | UnwindData |  |
| 438 | *Ordinal Only* | `0xFFE60` | 487 | UnwindData |  |
| 314 | *Ordinal Only* | `0x100050` | 49 | UnwindData |  |
| 313 | *Ordinal Only* | `0x100090` | 182 | UnwindData |  |
| 315 | *Ordinal Only* | `0x100150` | 75 | UnwindData |  |
| 320 | *Ordinal Only* | `0x1001B0` | 117 | UnwindData |  |
| 323 | *Ordinal Only* | `0x100230` | 393 | UnwindData |  |
| 318 | *Ordinal Only* | `0x1003C0` | 189 | UnwindData |  |
| 319 | *Ordinal Only* | `0x100490` | 120 | UnwindData |  |
| 434 | *Ordinal Only* | `0x100510` | 167 | UnwindData |  |
| 305 | *Ordinal Only* | `0x1005C0` | 197 | UnwindData |  |
| 310 | *Ordinal Only* | `0x100690` | 231 | UnwindData |  |
| 107 | *Ordinal Only* | `0x100DF0` | 108 | UnwindData |  |
| 104 | *Ordinal Only* | `0x100E70` | 433 | UnwindData |  |
| 116 | *Ordinal Only* | `0x101030` | 179 | UnwindData |  |
| 103 | *Ordinal Only* | `0x1010F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | *Ordinal Only* | `0x101110` | 204 | UnwindData |  |
| 102 | *Ordinal Only* | `0x1011F0` | 38 | UnwindData |  |
| 500 | *Ordinal Only* | `0x101220` | 75 | UnwindData |  |
| 562 | *Ordinal Only* | `0x101280` | 45 | UnwindData |  |
| 579 | *Ordinal Only* | `0x1012C0` | 162 | UnwindData |  |
| 115 | *Ordinal Only* | `0x101370` | 196 | UnwindData |  |
| 112 | *Ordinal Only* | `0x1014F0` | 151 | UnwindData |  |
| 111 | *Ordinal Only* | `0x101590` | 200 | UnwindData |  |
| 114 | *Ordinal Only* | `0x101660` | 234 | UnwindData |  |
| 304 | *Ordinal Only* | `0x101750` | 222 | UnwindData |  |
| 198 | `IEGetUserPrivateNamespaceName` | `0x101840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `SetAccessForIEAppContainer` | `0x101860` | 555 | UnwindData |  |
| 395 | *Ordinal Only* | `0x101AA0` | 3,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | *Ordinal Only* | `0x1027A0` | 310 | UnwindData |  |
| 558 | *Ordinal Only* | `0x1028E0` | 98 | UnwindData |  |
| 559 | *Ordinal Only* | `0x102950` | 138 | UnwindData |  |
| 188 | `GetMarkOfTheWeb` | `0x10B3C0` | 213 | UnwindData |  |
| 113 | *Ordinal Only* | `0x10B4A0` | 117 | UnwindData |  |
| 244 | `ZonesReInit` | `0x10B8C0` | 108 | UnwindData |  |
| 563 | *Ordinal Only* | `0x10D480` | 151 | UnwindData |  |
| 502 | *Ordinal Only* | `0x111500` | 60 | UnwindData |  |
| 137 | `CoInternetFeatureSettingsChanged` | `0x111550` | 29 | UnwindData |  |
| 180 | `GetAddSitesFileUrl` | `0x111580` | 243 | UnwindData |  |
| 523 | *Ordinal Only* | `0x111680` | 345 | UnwindData |  |
| 453 | *Ordinal Only* | `0x1117E0` | 77 | UnwindData |  |
| 544 | *Ordinal Only* | `0x111840` | 225 | UnwindData |  |
| 501 | *Ordinal Only* | `0x111930` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | *Ordinal Only* | `0x111970` | 185 | UnwindData |  |
| 491 | *Ordinal Only* | `0x111A30` | 455 | UnwindData |  |
| 202 | `IsIntranetAvailable` | `0x111C00` | 137 | UnwindData |  |
| 496 | *Ordinal Only* | `0x111C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | *Ordinal Only* | `0x111CA0` | 372 | UnwindData |  |
| 225 | `ShowTrustAlertDialog` | `0x111E20` | 345 | UnwindData |  |
| 497 | *Ordinal Only* | `0x111F80` | 28 | UnwindData |  |
| 100 | *Ordinal Only* | `0x111FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | *Ordinal Only* | `0x111FC0` | 112 | UnwindData |  |
| 482 | *Ordinal Only* | `0x112040` | 37 | UnwindData |  |
| 483 | *Ordinal Only* | `0x112070` | 156 | UnwindData |  |
| 474 | *Ordinal Only* | `0x112120` | 156 | UnwindData |  |
| 475 | *Ordinal Only* | `0x1121D0` | 50 | UnwindData |  |
| 476 | *Ordinal Only* | `0x112210` | 153 | UnwindData |  |
| 478 | *Ordinal Only* | `0x1122B0` | 168 | UnwindData |  |
| 480 | *Ordinal Only* | `0x112360` | 179 | UnwindData |  |
| 481 | *Ordinal Only* | `0x112420` | 363 | UnwindData |  |
| 479 | *Ordinal Only* | `0x1125A0` | 67 | UnwindData |  |
| 477 | *Ordinal Only* | `0x1125F0` | 46 | UnwindData |  |
| 455 | *Ordinal Only* | `0x112CF0` | 41 | UnwindData |  |
| 525 | *Ordinal Only* | `0x1164C0` | 492 | UnwindData |  |
| 514 | *Ordinal Only* | `0x1166C0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | *Ordinal Only* | `0x1168B0` | 156 | UnwindData |  |
| 127 | `CORPolicyProvider` | `0x119420` | 784 | UnwindData |  |
| 575 | *Ordinal Only* | `0x11EBC0` | 149 | UnwindData |  |
| 560 | *Ordinal Only* | `0x11EC60` | 110 | UnwindData |  |
| 561 | *Ordinal Only* | `0x11ECE0` | 28 | UnwindData |  |
| 308 | *Ordinal Only* | `0x120160` | 554 | UnwindData |  |
| 187 | `GetLabelsFromNamedHost` | `0x120D60` | 272 | UnwindData |  |
| 606 | *Ordinal Only* | `0x122A60` | 48 | UnwindData |  |
| 607 | *Ordinal Only* | `0x122AA0` | 48 | UnwindData |  |
| 573 | *Ordinal Only* | `0x124310` | 259 | UnwindData |  |
| 572 | *Ordinal Only* | `0x124420` | 412 | UnwindData |  |
| 530 | *Ordinal Only* | `0x124F30` | 318 | UnwindData |  |
| 539 | *Ordinal Only* | `0x125080` | 50 | UnwindData |  |
| 528 | *Ordinal Only* | `0x1250C0` | 103 | UnwindData |  |
| 540 | *Ordinal Only* | `0x125130` | 50 | UnwindData |  |
| 529 | *Ordinal Only* | `0x125170` | 599 | UnwindData |  |
| 532 | *Ordinal Only* | `0x1253D0` | 393 | UnwindData |  |
| 580 | *Ordinal Only* | `0x125560` | 31 | UnwindData |  |
| 535 | *Ordinal Only* | `0x125590` | 66 | UnwindData |  |
| 531 | *Ordinal Only* | `0x1255E0` | 142 | UnwindData |  |
| 487 | *Ordinal Only* | `0x125B20` | 124 | UnwindData |  |
| 515 | *Ordinal Only* | `0x125BB0` | 74 | UnwindData |  |
| 216 | `RegisterWebPlatformPermanentSecurityManager` | `0x12AAC0` | 209 | UnwindData |  |
| 238 | `UnregisterWebPlatformPermanentSecurityManager` | `0x12ABA0` | 140 | UnwindData |  |
