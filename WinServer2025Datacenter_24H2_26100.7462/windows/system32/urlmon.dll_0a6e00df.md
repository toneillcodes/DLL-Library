# Binary Specification: urlmon.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\urlmon.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0a6e00dfb6704f2d63bf745825c5799dc0fcee60d7ed84c67684ce99c156d943`
* **Total Exported Functions:** 318

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 156 | `CopyBindInfo` | `0x4C10` | 778 | UnwindData |  |
| 217 | `ReleaseBindInfo` | `0x5B20` | 127 | UnwindData |  |
| 142 | `CoInternetGetSecurityUrlEx` | `0xD330` | 214 | UnwindData |  |
| 509 | *Ordinal Only* | `0xE2C0` | 44 | UnwindData |  |
| 149 | `CoInternetParseUrl` | `0xF0E0` | 1,336 | UnwindData |  |
| 207 | `MkParseDisplayNameEx` | `0x10520` | 461 | UnwindData |  |
| 163 | `CreateURLMonikerEx` | `0x10700` | 15 | UnwindData |  |
| 219 | `RevokeBindStatusCallback` | `0x11C10` | 531 | UnwindData |  |
| 212 | `RegisterBindStatusCallback` | `0x11F30` | 806 | UnwindData |  |
| 162 | `CreateURLMoniker` | `0x126A0` | 18 | UnwindData |  |
| 164 | `CreateURLMonikerEx2` | `0x126C0` | 20 | UnwindData |  |
| 159 | `CreateAsyncBindCtxEx` | `0x129A0` | 238 | UnwindData |  |
| 445 | *Ordinal Only* | `0x22360` | 1,308 | UnwindData |  |
| 184 | `GetIDNFlagsForUri` | `0x30070` | 145 | UnwindData |  |
| 154 | `CompareSecurityIds` | `0x32E70` | 99 | UnwindData |  |
| 240 | `UrlMkGetSessionOption` | `0x35DC0` | 394 | UnwindData |  |
| 208 | `ObtainUserAgentString` | `0x36C80` | 429 | UnwindData |  |
| 565 | *Ordinal Only* | `0x37A70` | 139 | UnwindData |  |
| 443 | *Ordinal Only* | `0x37DF0` | 375 | UnwindData |  |
| 177 | `FindMediaType` | `0x3AD60` | 310 | UnwindData |  |
| 179 | `FindMimeFromData` | `0x3B930` | 1,508 | UnwindData |  |
| 144 | `CoInternetIsFeatureEnabled` | `0x3DC30` | 33 | UnwindData |  |
| 492 | *Ordinal Only* | `0x43970` | 1,329 | UnwindData |  |
| 499 | *Ordinal Only* | `0x49410` | 273 | UnwindData |  |
| 206 | `IsValidURL` | `0x58F00` | 3,117 | UnwindData |  |
| 150 | `CoInternetQueryInfo` | `0x5B360` | 1,210 | UnwindData |  |
| 520 | *Ordinal Only* | `0x5DEB0` | 380 | UnwindData |  |
| 135 | `CoInternetCreateSecurityManager` | `0x5E3D0` | 954 | UnwindData |  |
| 108 | *Ordinal Only* | `0x5EFC0` | 297 | UnwindData |  |
| 504 | *Ordinal Only* | `0x64C00` | 987 | UnwindData |  |
| 503 | *Ordinal Only* | `0x66870` | 459 | UnwindData |  |
| 441 | *Ordinal Only* | `0x679B0` | 140 | UnwindData |  |
| 132 | `CoInternetCombineUrl` | `0x69DD0` | 2,255 | UnwindData |  |
| 518 | *Ordinal Only* | `0x70E80` | 850 | UnwindData |  |
| 131 | `CoInternetCombineIUri` | `0x725D0` | 422 | UnwindData |  |
| 403 | *Ordinal Only* | `0x73E80` | 4,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | *Ordinal Only* | `0x73E80` | 4,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | *Ordinal Only* | `0x73E80` | 4,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | *Ordinal Only* | `0x73E80` | 4,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 603 | *Ordinal Only* | `0x75060` | 398 | UnwindData |  |
| 133 | `CoInternetCombineUrlEx` | `0x76360` | 25 | UnwindData |  |
| 521 | *Ordinal Only* | `0x768B0` | 377 | UnwindData |  |
| 519 | *Ordinal Only* | `0x770D0` | 384 | UnwindData |  |
| 536 | *Ordinal Only* | `0x786A0` | 247 | UnwindData |  |
| 148 | `CoInternetParseIUri` | `0x79BC0` | 228 | UnwindData |  |
| 191 | `GetZoneFromAlternateDataStreamEx` | `0x7A100` | 237 | UnwindData |  |
| 449 | *Ordinal Only* | `0x7CDB0` | 208 | UnwindData |  |
| 446 | *Ordinal Only* | `0x7E2A0` | 166 | UnwindData |  |
| 170 | `DllGetClassObject` | `0x7E9D0` | 156 | UnwindData |  |
| 143 | `CoInternetGetSession` | `0x801F0` | 181 | UnwindData |  |
| 165 | `CreateUri` | `0x81910` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `CoInternetIsFeatureEnabledForIUri` | `0x819C0` | 258 | UnwindData |  |
| 109 | `FileBearsMarkOfTheWeb` | `0x81D90` | 1,398 | UnwindData |  |
| 157 | `CopyStgMedium` | `0x82840` | 452 | UnwindData |  |
| 121 | `AsyncGetClassBits` | `0x85FD0` | 127 | UnwindData |  |
| 169 | `DllCanUnloadNow` | `0x87820` | 6,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 517 | *Ordinal Only* | `0x89100` | 170 | UnwindData |  |
| 176 | `FaultInIEFeature` | `0x8AAA0` | 619 | UnwindData |  |
| 511 | *Ordinal Only* | `0x8B570` | 455 | UnwindData |  |
| 471 | *Ordinal Only* | `0x8CAF0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `CreateIUriBuilder` | `0x8CC90` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | *Ordinal Only* | `0x8D1A0` | 235 | UnwindData |  |
| 442 | *Ordinal Only* | `0x8D480` | 1,567 | UnwindData |  |
| 160 | `CreateFormatEnumerator` | `0x8DB70` | 48 | UnwindData |  |
| 105 | *Ordinal Only* | `0x91050` | 834 | UnwindData |  |
| 241 | `UrlMkSetSessionOption` | `0x916D0` | 625 | UnwindData |  |
| 151 | `CoInternetSetFeatureEnabled` | `0x91B30` | 353 | UnwindData |  |
| 553 | *Ordinal Only* | `0x92D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `CoInternetCreateZoneManager` | `0x92DA0` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | *Ordinal Only* | `0x93220` | 81 | UnwindData |  |
| 555 | *Ordinal Only* | `0x953B0` | 61 | UnwindData |  |
| 577 | *Ordinal Only* | `0x95400` | 100 | UnwindData |  |
| 571 | *Ordinal Only* | `0x97210` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | *Ordinal Only* | `0x97410` | 153 | UnwindData |  |
| 570 | *Ordinal Only* | `0x97E30` | 75 | UnwindData |  |
| 488 | *Ordinal Only* | `0x98380` | 140 | UnwindData |  |
| 486 | *Ordinal Only* | `0x98550` | 135 | UnwindData |  |
| 201 | `IsAsyncMoniker` | `0x98B30` | 86 | UnwindData |  |
| 146 | `CoInternetIsFeatureEnabledForUrl` | `0x98B90` | 91 | UnwindData |  |
| 484 | *Ordinal Only* | `0x98D00` | 312 | UnwindData |  |
| 233 | `URLOpenBlockingStreamW` | `0x99D60` | 251 | UnwindData |  |
| 485 | *Ordinal Only* | `0x9A010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | *Ordinal Only* | `0x9A020` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `GetIUriPriv` | `0x9A360` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 489 | *Ordinal Only* | `0x9ADC0` | 249 | UnwindData |  |
| 155 | `CompatFlagsFromClsid` | `0x9AF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `ShouldShowIntranetWarningSecband` | `0x9AF40` | 277 | UnwindData |  |
| 533 | *Ordinal Only* | `0x9BA10` | 94 | UnwindData |  |
| 213 | `RegisterFormatEnumerator` | `0x9C4D0` | 42 | UnwindData |  |
| 507 | *Ordinal Only* | `0x9C6E0` | 170 | UnwindData |  |
| 506 | *Ordinal Only* | `0x9C810` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | *Ordinal Only* | `0x9CCF0` | 41 | UnwindData |  |
| 498 | *Ordinal Only* | `0x9CDF0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `RestrictHTTP2` | `0x9CE70` | 13,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | *Ordinal Only* | `0xA0180` | 46 | UnwindData |  |
| 493 | *Ordinal Only* | `0xA36E0` | 138 | UnwindData |  |
| 242 | `UrlmonCleanupCurrentThread` | `0xA3B70` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `RegisterMediaTypes` | `0xA3C20` | 126 | UnwindData |  |
| 461 | *Ordinal Only* | `0xA4120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | *Ordinal Only* | `0xA4130` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | *Ordinal Only* | `0xA4350` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | *Ordinal Only* | `0xA4350` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 538 | *Ordinal Only* | `0xA4350` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | *Ordinal Only* | `0xA4C20` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `IsJITInProgress` | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | *Ordinal Only* | `0xA4D70` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `GetPortFromUrlScheme` | `0xA8AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `GetPropertyFromName` | `0xA8AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `GetPropertyName` | `0xA8B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `IsDWORDProperty` | `0xA8B20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `IsStringProperty` | `0xA8B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `CreateUriFromMultiByteString` | `0xA8B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `CreateUriPriv` | `0xA8B80` | 67 | UnwindData |  |
| 168 | `CreateUriWithFragment` | `0xA8BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `GetIUriPriv2` | `0xA8BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `IntlPercentEncodeNormalize` | `0xA8C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `BindAsyncMoniker` | `0xA8C30` | 157 | UnwindData |  |
| 158 | `CreateAsyncBindCtx` | `0xA8CE0` | 239 | UnwindData |  |
| 178 | `FindMediaTypeClass` | `0xA8DE0` | 177 | UnwindData |  |
| 140 | `CoInternetGetProtocolFlags` | `0xA8EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `DllRegisterServerEx` | `0xA8EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `GetClassURL` | `0xA8EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `GetSoftwareUpdateInfo` | `0xA8EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `SetSoftwareUpdateAdvertisementState` | `0xA8EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `RegisterMediaTypeClass` | `0xA8EB0` | 259 | UnwindData |  |
| 220 | `RevokeFormatEnumerator` | `0xA8FC0` | 39 | UnwindData |  |
| 457 | *Ordinal Only* | `0xA8FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `DllInstall` | `0xA9010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `DllRegisterServer` | `0xA9020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `DllUnregisterServer` | `0xA9030` | 61 | UnwindData |  |
| 239 | `UrlMkBuildVersion` | `0xA9080` | 8,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `CoInternetGetMobileBrowserAppCompatMode` | `0xAB370` | 92 | UnwindData |  |
| 139 | `CoInternetGetMobileBrowserForceDesktopMode` | `0xAB3E0` | 33 | UnwindData |  |
| 447 | *Ordinal Only* | `0xAB410` | 111 | UnwindData |  |
| 152 | `CoInternetSetMobileBrowserAppCompatMode` | `0xAB490` | 61 | UnwindData |  |
| 153 | `CoInternetSetMobileBrowserForceDesktopMode` | `0xAB4E0` | 26 | UnwindData |  |
| 564 | *Ordinal Only* | `0xAB7C0` | 136 | UnwindData |  |
| 451 | *Ordinal Only* | `0xAB850` | 118 | UnwindData |  |
| 450 | *Ordinal Only* | `0xAB8D0` | 301 | UnwindData |  |
| 545 | *Ordinal Only* | `0xABA10` | 223 | UnwindData |  |
| 524 | *Ordinal Only* | `0xABB00` | 127 | UnwindData |  |
| 576 | *Ordinal Only* | `0xABB90` | 117 | UnwindData |  |
| 510 | *Ordinal Only* | `0xABC10` | 170 | UnwindData |  |
| 547 | *Ordinal Only* | `0xABCC0` | 53 | UnwindData |  |
| 548 | *Ordinal Only* | `0xABD00` | 155 | UnwindData |  |
| 543 | *Ordinal Only* | `0xABDB0` | 166 | UnwindData |  |
| 566 | *Ordinal Only* | `0xABE60` | 587 | UnwindData |  |
| 546 | *Ordinal Only* | `0xAC170` | 54 | UnwindData |  |
| 527 | *Ordinal Only* | `0xAC1B0` | 114 | UnwindData |  |
| 574 | *Ordinal Only* | `0xAC230` | 117 | UnwindData |  |
| 512 | *Ordinal Only* | `0xAC2B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | *Ordinal Only* | `0xAC2D0` | 114 | UnwindData |  |
| 452 | *Ordinal Only* | `0xAC800` | 230 | UnwindData |  |
| 448 | *Ordinal Only* | `0xAC8F0` | 259 | UnwindData |  |
| 567 | *Ordinal Only* | `0xB1D10` | 724 | UnwindData |  |
| 122 | `AsyncInstallDistributionUnit` | `0xB9420` | 127 | UnwindData |  |
| 128 | `CoGetClassObjectFromURL` | `0xB94B0` | 94 | UnwindData |  |
| 490 | *Ordinal Only* | `0xB9520` | 1,269 | UnwindData |  |
| 129 | `CoInstall` | `0xB9A20` | 151 | UnwindData |  |
| 199 | `IEInstallScope` | `0xB9AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `PrivateCoInstall` | `0xB9AD0` | 300 | UnwindData |  |
| 125 | `CDLGetLongPathNameA` | `0xB9DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `CDLGetLongPathNameW` | `0xB9DC0` | 6,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `Extract` | `0xBB8C0` | 370 | UnwindData |  |
| 183 | `GetComponentIDFromCLSSPEC` | `0xBCAB0` | 97 | UnwindData |  |
| 470 | *Ordinal Only* | `0xDC820` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `CAuthenticateHostUI_CreateInstance` | `0xDCCF0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | *Ordinal Only* | `0xDCDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `ShouldDisplayPunycodeForUri` | `0xDCDC0` | 108 | UnwindData |  |
| 568 | *Ordinal Only* | `0xE5C90` | 239 | UnwindData |  |
| 569 | *Ordinal Only* | `0xE5D90` | 58 | UnwindData |  |
| 210 | `QueryAssociations` | `0xF17C0` | 241 | UnwindData |  |
| 211 | `QueryClsidAssociation` | `0xF18C0` | 200 | UnwindData |  |
| 462 | *Ordinal Only* | `0xF2420` | 111 | UnwindData |  |
| 463 | *Ordinal Only* | `0xF24A0` | 109 | UnwindData |  |
| 460 | *Ordinal Only* | `0xF2520` | 25 | UnwindData |  |
| 130 | `CoInternetCanonicalizeIUri` | `0xF33E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | *Ordinal Only* | `0xF33F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `CoInternetCompareUrl` | `0xF3400` | 178 | UnwindData |  |
| 141 | `CoInternetGetSecurityUrl` | `0xF34C0` | 1,050 | UnwindData |  |
| 147 | `CoInternetIsFeatureZoneElevationEnabled` | `0xF38E0` | 640 | UnwindData |  |
| 604 | *Ordinal Only* | `0xF3B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `GetClassFileOrMime` | `0xF3B80` | 54 | UnwindData |  |
| 602 | *Ordinal Only* | `0xF3BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `URLDownloadA` | `0xF3BD0` | 91 | UnwindData |  |
| 231 | `URLDownloadW` | `0xF3C40` | 633 | UnwindData |  |
| 190 | `GetUrlmonThreadNotificationHwnd` | `0xF4450` | 82 | UnwindData |  |
| 324 | *Ordinal Only* | `0xF54F0` | 121 | UnwindData |  |
| 192 | `HlinkGoBack` | `0xFD200` | 189 | UnwindData |  |
| 193 | `HlinkGoForward` | `0xFD2D0` | 189 | UnwindData |  |
| 194 | `HlinkNavigateMoniker` | `0xFD3A0` | 123 | UnwindData |  |
| 195 | `HlinkNavigateString` | `0xFD430` | 123 | UnwindData |  |
| 196 | `HlinkSimpleNavigateToMoniker` | `0xFD4C0` | 1,668 | UnwindData |  |
| 197 | `HlinkSimpleNavigateToString` | `0xFDB50` | 253 | UnwindData |  |
| 227 | `URLDownloadToCacheFileA` | `0xFEF40` | 381 | UnwindData |  |
| 228 | `URLDownloadToCacheFileW` | `0xFF0D0` | 351 | UnwindData |  |
| 229 | `URLDownloadToFileA` | `0xFF240` | 343 | UnwindData |  |
| 230 | `URLDownloadToFileW` | `0xFF3A0` | 247 | UnwindData |  |
| 232 | `URLOpenBlockingStreamA` | `0xFF4A0` | 222 | UnwindData |  |
| 234 | `URLOpenPullStreamA` | `0xFF590` | 195 | UnwindData |  |
| 235 | `URLOpenPullStreamW` | `0xFF660` | 190 | UnwindData |  |
| 236 | `URLOpenStreamA` | `0xFF730` | 195 | UnwindData |  |
| 237 | `URLOpenStreamW` | `0xFF800` | 190 | UnwindData |  |
| 204 | `IsLoggingEnabledA` | `0xFF8D0` | 120 | UnwindData |  |
| 243 | `WriteHitLogging` | `0xFF950` | 200 | UnwindData |  |
| 205 | `IsLoggingEnabledW` | `0xFFA20` | 216 | UnwindData |  |
| 316 | *Ordinal Only* | `0x100820` | 165 | UnwindData |  |
| 311 | *Ordinal Only* | `0x1008D0` | 112 | UnwindData |  |
| 322 | `IECompatLogCSSFix` | `0x1009E0` | 211 | UnwindData |  |
| 321 | *Ordinal Only* | `0x100AC0` | 75 | UnwindData |  |
| 312 | *Ordinal Only* | `0x100B20` | 315 | UnwindData |  |
| 307 | *Ordinal Only* | `0x100C70` | 186 | UnwindData |  |
| 437 | *Ordinal Only* | `0x100D30` | 97 | UnwindData |  |
| 436 | *Ordinal Only* | `0x100DA0` | 82 | UnwindData |  |
| 306 | *Ordinal Only* | `0x100E00` | 49 | UnwindData |  |
| 435 | *Ordinal Only* | `0x100E40` | 124 | UnwindData |  |
| 439 | *Ordinal Only* | `0x100ED0` | 56 | UnwindData |  |
| 309 | *Ordinal Only* | `0x100F10` | 49 | UnwindData |  |
| 438 | *Ordinal Only* | `0x100F50` | 487 | UnwindData |  |
| 314 | *Ordinal Only* | `0x101140` | 49 | UnwindData |  |
| 313 | *Ordinal Only* | `0x101180` | 182 | UnwindData |  |
| 315 | *Ordinal Only* | `0x101240` | 75 | UnwindData |  |
| 320 | *Ordinal Only* | `0x1012A0` | 117 | UnwindData |  |
| 323 | *Ordinal Only* | `0x101320` | 393 | UnwindData |  |
| 318 | *Ordinal Only* | `0x1014B0` | 189 | UnwindData |  |
| 319 | *Ordinal Only* | `0x101580` | 120 | UnwindData |  |
| 434 | *Ordinal Only* | `0x101600` | 167 | UnwindData |  |
| 305 | *Ordinal Only* | `0x1016B0` | 197 | UnwindData |  |
| 310 | *Ordinal Only* | `0x101780` | 231 | UnwindData |  |
| 107 | *Ordinal Only* | `0x101EE0` | 108 | UnwindData |  |
| 104 | *Ordinal Only* | `0x101F60` | 433 | UnwindData |  |
| 116 | *Ordinal Only* | `0x102120` | 179 | UnwindData |  |
| 103 | *Ordinal Only* | `0x1021E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | *Ordinal Only* | `0x102200` | 204 | UnwindData |  |
| 102 | *Ordinal Only* | `0x1022E0` | 38 | UnwindData |  |
| 500 | *Ordinal Only* | `0x102310` | 75 | UnwindData |  |
| 562 | *Ordinal Only* | `0x102370` | 45 | UnwindData |  |
| 579 | *Ordinal Only* | `0x1023B0` | 162 | UnwindData |  |
| 115 | *Ordinal Only* | `0x102460` | 196 | UnwindData |  |
| 112 | *Ordinal Only* | `0x1025E0` | 151 | UnwindData |  |
| 111 | *Ordinal Only* | `0x102680` | 200 | UnwindData |  |
| 114 | *Ordinal Only* | `0x102750` | 234 | UnwindData |  |
| 304 | *Ordinal Only* | `0x102840` | 222 | UnwindData |  |
| 198 | `IEGetUserPrivateNamespaceName` | `0x102930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `SetAccessForIEAppContainer` | `0x102950` | 555 | UnwindData |  |
| 395 | *Ordinal Only* | `0x102B90` | 3,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | *Ordinal Only* | `0x103890` | 310 | UnwindData |  |
| 558 | *Ordinal Only* | `0x1039D0` | 98 | UnwindData |  |
| 559 | *Ordinal Only* | `0x103A40` | 138 | UnwindData |  |
| 188 | `GetMarkOfTheWeb` | `0x10C9A0` | 213 | UnwindData |  |
| 113 | *Ordinal Only* | `0x10CA80` | 117 | UnwindData |  |
| 244 | `ZonesReInit` | `0x10CEA0` | 108 | UnwindData |  |
| 563 | *Ordinal Only* | `0x10F860` | 151 | UnwindData |  |
| 502 | *Ordinal Only* | `0x113D90` | 60 | UnwindData |  |
| 137 | `CoInternetFeatureSettingsChanged` | `0x113DE0` | 29 | UnwindData |  |
| 180 | `GetAddSitesFileUrl` | `0x113E10` | 243 | UnwindData |  |
| 523 | *Ordinal Only* | `0x113F10` | 345 | UnwindData |  |
| 453 | *Ordinal Only* | `0x114070` | 77 | UnwindData |  |
| 544 | *Ordinal Only* | `0x1140D0` | 225 | UnwindData |  |
| 501 | *Ordinal Only* | `0x1141C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | *Ordinal Only* | `0x114200` | 185 | UnwindData |  |
| 491 | *Ordinal Only* | `0x1142C0` | 455 | UnwindData |  |
| 202 | `IsIntranetAvailable` | `0x114490` | 407 | UnwindData |  |
| 496 | *Ordinal Only* | `0x114630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | *Ordinal Only* | `0x114640` | 372 | UnwindData |  |
| 225 | `ShowTrustAlertDialog` | `0x1147C0` | 345 | UnwindData |  |
| 497 | *Ordinal Only* | `0x114920` | 28 | UnwindData |  |
| 100 | *Ordinal Only* | `0x114950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | *Ordinal Only* | `0x114960` | 112 | UnwindData |  |
| 482 | *Ordinal Only* | `0x1149E0` | 37 | UnwindData |  |
| 483 | *Ordinal Only* | `0x114A10` | 156 | UnwindData |  |
| 474 | *Ordinal Only* | `0x114AC0` | 156 | UnwindData |  |
| 475 | *Ordinal Only* | `0x114B70` | 50 | UnwindData |  |
| 476 | *Ordinal Only* | `0x114BB0` | 153 | UnwindData |  |
| 478 | *Ordinal Only* | `0x114C50` | 168 | UnwindData |  |
| 480 | *Ordinal Only* | `0x114D00` | 179 | UnwindData |  |
| 481 | *Ordinal Only* | `0x114DC0` | 363 | UnwindData |  |
| 479 | *Ordinal Only* | `0x114F40` | 67 | UnwindData |  |
| 477 | *Ordinal Only* | `0x114F90` | 46 | UnwindData |  |
| 455 | *Ordinal Only* | `0x115690` | 41 | UnwindData |  |
| 525 | *Ordinal Only* | `0x118200` | 492 | UnwindData |  |
| 514 | *Ordinal Only* | `0x118400` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 526 | *Ordinal Only* | `0x1185F0` | 156 | UnwindData |  |
| 127 | `CORPolicyProvider` | `0x11B160` | 784 | UnwindData |  |
| 575 | *Ordinal Only* | `0x120940` | 149 | UnwindData |  |
| 560 | *Ordinal Only* | `0x1209E0` | 110 | UnwindData |  |
| 561 | *Ordinal Only* | `0x120A60` | 28 | UnwindData |  |
| 308 | *Ordinal Only* | `0x121EE0` | 554 | UnwindData |  |
| 187 | `GetLabelsFromNamedHost` | `0x122B20` | 272 | UnwindData |  |
| 606 | *Ordinal Only* | `0x1247F0` | 48 | UnwindData |  |
| 607 | *Ordinal Only* | `0x124830` | 48 | UnwindData |  |
| 573 | *Ordinal Only* | `0x1260A0` | 259 | UnwindData |  |
| 572 | *Ordinal Only* | `0x1261B0` | 412 | UnwindData |  |
| 530 | *Ordinal Only* | `0x126CC0` | 318 | UnwindData |  |
| 539 | *Ordinal Only* | `0x126E10` | 50 | UnwindData |  |
| 528 | *Ordinal Only* | `0x126E50` | 103 | UnwindData |  |
| 540 | *Ordinal Only* | `0x126EC0` | 50 | UnwindData |  |
| 529 | *Ordinal Only* | `0x126F00` | 599 | UnwindData |  |
| 532 | *Ordinal Only* | `0x127160` | 393 | UnwindData |  |
| 580 | *Ordinal Only* | `0x1272F0` | 31 | UnwindData |  |
| 535 | *Ordinal Only* | `0x127320` | 66 | UnwindData |  |
| 531 | *Ordinal Only* | `0x127370` | 142 | UnwindData |  |
| 487 | *Ordinal Only* | `0x1278B0` | 124 | UnwindData |  |
| 515 | *Ordinal Only* | `0x127940` | 74 | UnwindData |  |
| 216 | `RegisterWebPlatformPermanentSecurityManager` | `0x12CB50` | 209 | UnwindData |  |
| 238 | `UnregisterWebPlatformPermanentSecurityManager` | `0x12CC30` | 140 | UnwindData |  |
