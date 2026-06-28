# Binary Specification: wininet.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wininet.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `091e5656e9bcb7256bd68eca823f96a4bb7eddc5de2e0b7d63217937e73e72c0`
* **Total Exported Functions:** 327

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 341 | `InternetSetOptionW` | `0x2050` | 3,684 | UnwindData |  |
| 149 | `DeleteUrlCacheEntry` | `0x74D0` | 355 | UnwindData |  |
| 150 | `DeleteUrlCacheEntryA` | `0x74D0` | 355 | UnwindData |  |
| 362 | `IsHostInProxyBypassList` | `0x191A0` | 1,831 | UnwindData |  |
| 314 | `InternetInitializeAutoProxyDll` | `0x1AB50` | 538 | UnwindData |  |
| 226 | `HttpAddRequestHeadersA` | `0x1BB90` | 751 | UnwindData |  |
| 319 | `InternetOpenW` | `0x30BC0` | 976 | UnwindData |  |
| 316 | `InternetOpenA` | `0x316A0` | 185 | UnwindData |  |
| 265 | `InternetCheckConnectionW` | `0x31760` | 281 | UnwindData |  |
| 264 | `InternetCheckConnectionA` | `0x31880` | 1,336 | UnwindData |  |
| 273 | `InternetConnectA` | `0x31DC0` | 509 | UnwindData |  |
| 300 | `InternetGetCookieExW` | `0x31FD0` | 998 | UnwindData |  |
| 289 | `InternetFreeCookies` | `0x323C0` | 366 | UnwindData |  |
| 298 | `InternetGetCookieEx2` | `0x32540` | 86 | UnwindData |  |
| 332 | `InternetSetCookieExW` | `0x325A0` | 1,206 | UnwindData |  |
| 367 | `PrivacyGetZonePreferenceW` | `0x356E0` | 963 | UnwindData |  |
| 323 | `InternetQueryOptionW` | `0x36A30` | 2,992 | UnwindData |  |
| 322 | `InternetQueryOptionA` | `0x37A40` | 9,344 | UnwindData |  |
| 338 | `InternetSetOptionA` | `0x3A6B0` | 12,841 | UnwindData |  |
| 243 | `HttpQueryInfoA` | `0x3EFE0` | 46 | UnwindData |  |
| 239 | `HttpOpenRequestW` | `0x49E90` | 2,488 | UnwindData |  |
| 279 | `InternetCreateUrlW` | `0x4C830` | 3,755 | UnwindData |  |
| 278 | `InternetCreateUrlA` | `0x4EA80` | 153 | UnwindData |  |
| 276 | `InternetCrackUrlA` | `0x4EB20` | 154 | UnwindData |  |
| 320 | `InternetQueryDataAvailable` | `0x53D60` | 34 | UnwindData |  |
| 277 | `InternetCrackUrlW` | `0x643B0` | 3,264 | UnwindData |  |
| 293 | `InternetGetConnectedState` | `0x6D4C0` | 147 | UnwindData |  |
| 296 | `InternetGetConnectedStateExW` | `0x6D560` | 879 | UnwindData |  |
| 212 | `GetUrlCacheEntryInfoW` | `0x71660` | 947 | UnwindData |  |
| 208 | `GetUrlCacheEntryBinaryBlob` | `0x721E0` | 111 | UnwindData |  |
| 169 | `FindNextUrlCacheContainerA` | `0x75180` | 460 | UnwindData |  |
| 171 | `FindNextUrlCacheEntryA` | `0x75730` | 601 | UnwindData |  |
| 174 | `FindNextUrlCacheEntryW` | `0x75990` | 591 | UnwindData |  |
| 172 | `FindNextUrlCacheEntryExA` | `0x75BF0` | 624 | UnwindData |  |
| 138 | `CommitUrlCacheEntryW` | `0x77F30` | 927 | UnwindData |  |
| 383 | `SetUrlCacheEntryInfoA` | `0x78320` | 699 | UnwindData |  |
| 274 | `InternetConnectW` | `0xA5300` | 1,642 | UnwindData |  |
| 116 | *Ordinal Only* | `0xA7150` | 263 | UnwindData |  |
| 269 | `InternetCombineUrlW` | `0xA79C0` | 284 | UnwindData |  |
| 326 | `InternetReadFileExW` | `0xA9670` | 270 | UnwindData |  |
| 359 | `InternetWriteFile` | `0xA9990` | 117 | UnwindData |  |
| 325 | `InternetReadFileExA` | `0xAA3C0` | 1,533 | UnwindData |  |
| 324 | `InternetReadFile` | `0xAAC30` | 117 | UnwindData |  |
| 236 | `HttpIsHostHstsEnabled` | `0xB0070` | 73 | UnwindData |  |
| 215 | `GetUrlCacheHeaderData` | `0xB4140` | 386 | UnwindData |  |
| 229 | `HttpCloseDependencyHandle` | `0xBA620` | 47 | UnwindData |  |
| 251 | `HttpWebSocketQueryCloseStatus` | `0xDBEC0` | 308 | UnwindData |  |
| 249 | `HttpWebSocketClose` | `0xDC1F0` | 297 | UnwindData |  |
| 250 | `HttpWebSocketCompleteUpgrade` | `0xDC720` | 199 | UnwindData |  |
| 252 | `HttpWebSocketReceive` | `0xDD920` | 329 | UnwindData |  |
| 253 | `HttpWebSocketSend` | `0xDDC70` | 310 | UnwindData |  |
| 155 | `DispatchAPICall` | `0xE4A80` | 12,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `UrlCacheFindFirstEntry` | `0xE7BA0` | 97 | UnwindData |  |
| 161 | `FindCloseUrlCache` | `0xE7E20` | 256 | UnwindData |  |
| 395 | `UnlockUrlCacheEntryStream` | `0xE7F30` | 236 | UnwindData |  |
| 140 | `CreateUrlCacheContainerA` | `0xE8D30` | 671 | UnwindData |  |
| 148 | `DeleteUrlCacheContainerW` | `0xE92A0` | 267 | UnwindData |  |
| 162 | `FindFirstUrlCacheContainerA` | `0xE9730` | 555 | UnwindData |  |
| 165 | `FindFirstUrlCacheEntryExA` | `0xE9B90` | 513 | UnwindData |  |
| 227 | `HttpAddRequestHeadersW` | `0x103370` | 570 | UnwindData |  |
| 370 | `ReadUrlCacheEntryStreamEx` | `0x1076B0` | 882 | UnwindData |  |
| 315 | `InternetLockRequestFile` | `0x107A30` | 1,058 | UnwindData |  |
| 348 | `InternetSetStatusCallbackW` | `0x108840` | 398 | UnwindData |  |
| 345 | `InternetSetStatusCallback` | `0x109C40` | 158 | UnwindData |  |
| 347 | `InternetSetStatusCallbackA` | `0x109C40` | 158 | UnwindData |  |
| 248 | `HttpSendRequestW` | `0x10F0C0` | 627 | UnwindData |  |
| 358 | `InternetUnlockRequestFile` | `0x10F530` | 1,123 | UnwindData |  |
| 211 | `GetUrlCacheEntryInfoExW` | `0x10F9A0` | 708 | UnwindData |  |
| 137 | `CommitUrlCacheEntryBinaryBlob` | `0x112620` | 97 | UnwindData |  |
| 263 | `InternetCanonicalizeUrlW` | `0x114200` | 291 | UnwindData |  |
| 267 | `InternetCloseHandle` | `0x1150B0` | 70 | UnwindData |  |
| 238 | `HttpOpenRequestA` | `0x115380` | 181 | UnwindData |  |
| 247 | `HttpSendRequestExW` | `0x117280` | 686 | UnwindData |  |
| 245 | `HttpSendRequestA` | `0x1189D0` | 249 | UnwindData |  |
| 268 | `InternetCombineUrlA` | `0x119E30` | 295 | UnwindData |  |
| 405 | `UrlCacheFindNextEntry` | `0x11ACC0` | 73 | UnwindData |  |
| 157 | `DllGetClassObject` | `0x11B040` | 107 | UnwindData |  |
| 309 | `InternetGetSecurityInfoByURLW` | `0x11B910` | 285 | UnwindData |  |
| 307 | `InternetGetSecurityInfoByURL` | `0x11BA40` | 345 | UnwindData |  |
| 308 | `InternetGetSecurityInfoByURLA` | `0x11BA40` | 345 | UnwindData |  |
| 151 | `DeleteUrlCacheEntryW` | `0x11CEA0` | 374 | UnwindData |  |
| 156 | `DllCanUnloadNow` | `0x11E740` | 42 | UnwindData |  |
| 230 | `HttpDuplicateDependencyHandle` | `0x120210` | 73 | UnwindData |  |
| 374 | `RetrieveUrlCacheEntryFileW` | `0x122BB0` | 647 | UnwindData |  |
| 231 | `HttpEndRequestA` | `0x122E40` | 257 | UnwindData |  |
| 233 | `HttpGetServerCredentials` | `0x126330` | 71 | UnwindData |  |
| 246 | `HttpSendRequestExA` | `0x1289F0` | 361 | UnwindData |  |
| 420 | *Ordinal Only* | `0x12A670` | 73 | UnwindData |  |
| 318 | `InternetOpenUrlW` | `0x12B2A0` | 676 | UnwindData |  |
| 317 | `InternetOpenUrlA` | `0x12B550` | 143 | UnwindData |  |
| 232 | `HttpEndRequestW` | `0x12D3F0` | 275 | UnwindData |  |
| 421 | *Ordinal Only* | `0x12E000` | 75 | UnwindData |  |
| 425 | `UrlCacheUpdateEntryExtraData` | `0x12EA20` | 71 | UnwindData |  |
| 330 | `InternetSetCookieEx2` | `0x1317B0` | 86 | UnwindData |  |
| 406 | `UrlCacheFreeEntryInfo` | `0x132190` | 105 | UnwindData |  |
| 158 | `DllInstall` | `0x1337D0` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `InternetGetCertByURL` | `0x1337D0` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `InternetGetCertByURLA` | `0x1337D0` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `RunOnceUrlCache` | `0x1337D0` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | *Ordinal Only* | `0x1337D0` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `UnlockUrlCacheEntryFileW` | `0x133CE0` | 331 | UnwindData |  |
| 141 | `CreateUrlCacheContainerW` | `0x133FF0` | 484 | UnwindData |  |
| 371 | `RegisterUrlCacheNotification` | `0x134BD0` | 3,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `UrlCacheServer` | `0x134BD0` | 3,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | *Ordinal Only* | `0x134BD0` | 3,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `InternetErrorDlg` | `0x1358C0` | 1,669 | UnwindData |  |
| 144 | `CreateUrlCacheEntryW` | `0x136090` | 28 | UnwindData |  |
| 143 | `CreateUrlCacheEntryExW` | `0x1360C0` | 517 | UnwindData |  |
| 290 | `InternetFreeProxyInfoList` | `0x137200` | 53 | UnwindData |  |
| 154 | `DetectAutoProxyUrl` | `0x1383A0` | 351 | UnwindData |  |
| 167 | `FindFirstUrlCacheEntryW` | `0x13A3B0` | 369 | UnwindData |  |
| 255 | `IncrementUrlCacheHeaderData` | `0x13BCA0` | 255 | UnwindData |  |
| 107 | `AppCacheCloseHandle` | `0x13BE90` | 47 | UnwindData |  |
| 207 | `GetUrlCacheConfigInfoW` | `0x13C360` | 266 | UnwindData |  |
| 147 | `DeleteUrlCacheContainerA` | `0x13D020` | 306 | UnwindData |  |
| 136 | `CommitUrlCacheEntryA` | `0x13E0E0` | 665 | UnwindData |  |
| 164 | `FindFirstUrlCacheEntryA` | `0x13E750` | 362 | UnwindData |  |
| 339 | `InternetSetOptionExA` | `0x13EC40` | 244 | UnwindData |  |
| 131 | `AppCacheGetGroupList` | `0x1404C0` | 71 | UnwindData |  |
| 244 | `HttpQueryInfoW` | `0x1420F0` | 28 | UnwindData |  |
| 352 | `InternetTimeFromSystemTime` | `0x151EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `InternetTimeFromSystemTimeA` | `0x151EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `InternetTimeFromSystemTimeW` | `0x151EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `InternetTimeToSystemTime` | `0x151EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `InternetTimeToSystemTimeA` | `0x151EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `InternetTimeToSystemTimeW` | `0x151ED0` | 6,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `GetProxyDllInfo` | `0x1537A0` | 3,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | *Ordinal Only* | `0x154430` | 29 | UnwindData |  |
| 159 | `DllRegisterServer` | `0x154460` | 52 | UnwindData |  |
| 160 | `DllUnregisterServer` | `0x1544A0` | 52 | UnwindData |  |
| 139 | `CreateMD5SSOHash` | `0x156040` | 692 | UnwindData |  |
| 176 | `ForceNexusLookup` | `0x156300` | 66 | UnwindData |  |
| 177 | `ForceNexusLookupExW` | `0x156350` | 127 | UnwindData |  |
| 426 | `UrlZonesDetach` | `0x158240` | 158 | UnwindData |  |
| 275 | `InternetConvertUrlFromWireToWideChar` | `0x15CD00` | 149 | UnwindData |  |
| 427 | `_GetFileExtensionFromUrl` | `0x15D6F0` | 124 | UnwindData |  |
| 235 | `HttpIndicatePageLoadComplete` | `0x15F860` | 44 | UnwindData |  |
| 237 | `HttpOpenDependencyHandle` | `0x15F8A0` | 71 | UnwindData |  |
| 234 | `HttpGetTunnelSocket` | `0x15FB40` | 234 | UnwindData |  |
| 240 | `HttpPushClose` | `0x160960` | 151 | UnwindData |  |
| 241 | `HttpPushEnable` | `0x160A00` | 71 | UnwindData |  |
| 242 | `HttpPushWait` | `0x160A50` | 71 | UnwindData |  |
| 288 | `InternetFortezzaCommand` | `0x160B70` | 97 | UnwindData |  |
| 321 | `InternetQueryFortezzaStatus` | `0x160BE0` | 90 | UnwindData |  |
| 101 | *Ordinal Only* | `0x166850` | 269 | UnwindData |  |
| 109 | *Ordinal Only* | `0x166AE0` | 154 | UnwindData |  |
| 111 | *Ordinal Only* | `0x166B80` | 1,226 | UnwindData |  |
| 120 | *Ordinal Only* | `0x167050` | 32 | UnwindData |  |
| 121 | *Ordinal Only* | `0x167050` | 32 | UnwindData |  |
| 122 | *Ordinal Only* | `0x167050` | 32 | UnwindData |  |
| 123 | *Ordinal Only* | `0x167050` | 32 | UnwindData |  |
| 108 | *Ordinal Only* | `0x167280` | 138 | UnwindData |  |
| 110 | *Ordinal Only* | `0x167310` | 1,200 | UnwindData |  |
| 258 | `InternetAttemptConnect` | `0x1684B0` | 84 | UnwindData |  |
| 262 | `InternetCanonicalizeUrlA` | `0x168510` | 271 | UnwindData |  |
| 302 | `InternetGetLastResponseInfoA` | `0x168630` | 428 | UnwindData |  |
| 337 | `InternetSetFilePointer` | `0x1687F0` | 463 | UnwindData |  |
| 349 | `InternetShowSecurityInfoByURL` | `0x1689D0` | 226 | UnwindData |  |
| 350 | `InternetShowSecurityInfoByURLA` | `0x1689D0` | 226 | UnwindData |  |
| 216 | `GopherCreateLocatorA` | `0x168AC0` | 29 | UnwindData |  |
| 217 | `GopherCreateLocatorW` | `0x168AC0` | 29 | UnwindData |  |
| 218 | `GopherFindFirstFileA` | `0x168AC0` | 29 | UnwindData |  |
| 219 | `GopherFindFirstFileW` | `0x168AC0` | 29 | UnwindData |  |
| 220 | `GopherGetAttributeA` | `0x168AC0` | 29 | UnwindData |  |
| 221 | `GopherGetAttributeW` | `0x168AC0` | 29 | UnwindData |  |
| 222 | `GopherGetLocatorTypeA` | `0x168AC0` | 29 | UnwindData |  |
| 223 | `GopherGetLocatorTypeW` | `0x168AC0` | 29 | UnwindData |  |
| 224 | `GopherOpenFileA` | `0x168AC0` | 29 | UnwindData |  |
| 225 | `GopherOpenFileW` | `0x168AC0` | 29 | UnwindData |  |
| 360 | `InternetWriteFileExA` | `0x168AC0` | 29 | UnwindData |  |
| 361 | `InternetWriteFileExW` | `0x168AC0` | 29 | UnwindData |  |
| 365 | `LoadUrlCacheContent` | `0x168AC0` | 29 | UnwindData |  |
| 259 | `InternetAutodial` | `0x168AF0` | 169 | UnwindData |  |
| 261 | `InternetAutodialHangup` | `0x168BA0` | 162 | UnwindData |  |
| 280 | `InternetDial` | `0x168C50` | 191 | UnwindData |  |
| 281 | `InternetDialA` | `0x168C50` | 191 | UnwindData |  |
| 282 | `InternetDialW` | `0x168D20` | 191 | UnwindData |  |
| 310 | `InternetGoOnline` | `0x168DF0` | 170 | UnwindData |  |
| 311 | `InternetGoOnlineA` | `0x168DF0` | 170 | UnwindData |  |
| 312 | `InternetGoOnlineW` | `0x168EA0` | 179 | UnwindData |  |
| 313 | `InternetHangUp` | `0x168F60` | 142 | UnwindData |  |
| 334 | `InternetSetDialState` | `0x169000` | 87 | UnwindData |  |
| 335 | `InternetSetDialStateA` | `0x169000` | 87 | UnwindData |  |
| 336 | `InternetSetDialStateW` | `0x169060` | 87 | UnwindData |  |
| 260 | `InternetAutodialCallback` | `0x1690C0` | 70 | UnwindData |  |
| 294 | `InternetGetConnectedStateEx` | `0x169110` | 259 | UnwindData |  |
| 295 | `InternetGetConnectedStateExA` | `0x169110` | 259 | UnwindData |  |
| 303 | `InternetGetLastResponseInfoW` | `0x169260` | 461 | UnwindData |  |
| 344 | `InternetSetSecureLegacyServersAppCompat` | `0x169440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `InternetShowSecurityInfoByURLW` | `0x169460` | 271 | UnwindData |  |
| 340 | `InternetSetOptionExW` | `0x169A20` | 244 | UnwindData |  |
| 422 | *Ordinal Only* | `0x169B20` | 71 | UnwindData |  |
| 423 | *Ordinal Only* | `0x169B70` | 47 | UnwindData |  |
| 372 | `ResumeSuspendedDownload` | `0x16A3F0` | 245 | UnwindData |  |
| 180 | `FtpCommandA` | `0x174F10` | 223 | UnwindData |  |
| 182 | `FtpCreateDirectoryA` | `0x175250` | 152 | UnwindData |  |
| 184 | `FtpDeleteFileA` | `0x1752F0` | 152 | UnwindData |  |
| 186 | `FtpFindFirstFileA` | `0x175390` | 223 | UnwindData |  |
| 188 | `FtpGetCurrentDirectoryA` | `0x175640` | 186 | UnwindData |  |
| 190 | `FtpGetFileA` | `0x175700` | 597 | UnwindData |  |
| 192 | `FtpGetFileSize` | `0x175960` | 643 | UnwindData |  |
| 194 | `FtpOpenFileA` | `0x175BF0` | 218 | UnwindData |  |
| 196 | `FtpPutFileA` | `0x175CD0` | 553 | UnwindData |  |
| 199 | `FtpRemoveDirectoryA` | `0x1760A0` | 152 | UnwindData |  |
| 201 | `FtpRenameFileA` | `0x176140` | 172 | UnwindData |  |
| 203 | `FtpSetCurrentDirectoryA` | `0x176200` | 152 | UnwindData |  |
| 286 | `InternetFindNextFileA` | `0x1786C0` | 88 | UnwindData |  |
| 181 | `FtpCommandW` | `0x178E70` | 429 | UnwindData |  |
| 183 | `FtpCreateDirectoryW` | `0x179030` | 388 | UnwindData |  |
| 185 | `FtpDeleteFileW` | `0x1791C0` | 388 | UnwindData |  |
| 187 | `FtpFindFirstFileW` | `0x179350` | 496 | UnwindData |  |
| 189 | `FtpGetCurrentDirectoryW` | `0x179550` | 423 | UnwindData |  |
| 191 | `FtpGetFileEx` | `0x179700` | 426 | UnwindData |  |
| 193 | `FtpGetFileW` | `0x1798B0` | 253 | UnwindData |  |
| 195 | `FtpOpenFileW` | `0x1799C0` | 137 | UnwindData |  |
| 197 | `FtpPutFileEx` | `0x179A50` | 382 | UnwindData |  |
| 198 | `FtpPutFileW` | `0x179BE0` | 207 | UnwindData |  |
| 200 | `FtpRemoveDirectoryW` | `0x179CC0` | 376 | UnwindData |  |
| 202 | `FtpRenameFileW` | `0x179E40` | 572 | UnwindData |  |
| 204 | `FtpSetCurrentDirectoryW` | `0x17A090` | 376 | UnwindData |  |
| 287 | `InternetFindNextFileW` | `0x17A6E0` | 378 | UnwindData |  |
| 118 | *Ordinal Only* | `0x1841D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `PrivacySetZonePreferenceW` | `0x1841F0` | 677 | UnwindData |  |
| 228 | `HttpCheckDavCompliance` | `0x1844A0` | 185 | UnwindData |  |
| 104 | *Ordinal Only* | `0x1844A0` | 185 | UnwindData |  |
| 105 | *Ordinal Only* | `0x184560` | 185 | UnwindData |  |
| 266 | `InternetClearAllPerSiteCookieDecisions` | `0x185620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `InternetEnumPerSiteCookieDecisionA` | `0x185630` | 105 | UnwindData |  |
| 284 | `InternetEnumPerSiteCookieDecisionW` | `0x1856A0` | 232 | UnwindData |  |
| 304 | `InternetGetPerSiteCookieDecisionA` | `0x185790` | 73 | UnwindData |  |
| 305 | `InternetGetPerSiteCookieDecisionW` | `0x1857E0` | 164 | UnwindData |  |
| 342 | `InternetSetPerSiteCookieDecisionA` | `0x185890` | 187 | UnwindData |  |
| 343 | `InternetSetPerSiteCookieDecisionW` | `0x185960` | 157 | UnwindData |  |
| 297 | `InternetGetCookieA` | `0x186CA0` | 28 | UnwindData |  |
| 299 | `InternetGetCookieExA` | `0x186CD0` | 852 | UnwindData |  |
| 301 | `InternetGetCookieW` | `0x187030` | 26 | UnwindData |  |
| 329 | `InternetSetCookieA` | `0x187050` | 34 | UnwindData |  |
| 331 | `InternetSetCookieExA` | `0x187080` | 156 | UnwindData |  |
| 333 | `InternetSetCookieW` | `0x187130` | 493 | UnwindData |  |
| 117 | *Ordinal Only* | `0x187330` | 290 | UnwindData |  |
| 256 | `InternetAlgIdToStringA` | `0x190A70` | 492 | UnwindData |  |
| 257 | `InternetAlgIdToStringW` | `0x190C70` | 496 | UnwindData |  |
| 327 | `InternetSecurityProtocolToStringA` | `0x190E70` | 363 | UnwindData |  |
| 328 | `InternetSecurityProtocolToStringW` | `0x190FF0` | 367 | UnwindData |  |
| 366 | `ParseX509EncodedCertificateForListBoxEntry` | `0x191170` | 32 | UnwindData |  |
| 388 | `ShowCertificate` | `0x191170` | 32 | UnwindData |  |
| 389 | `ShowClientAuthCerts` | `0x191170` | 32 | UnwindData |  |
| 390 | `ShowSecurityInfo` | `0x1911A0` | 370 | UnwindData |  |
| 391 | `ShowX509EncodedCertificate` | `0x191320` | 132 | UnwindData |  |
| 270 | `InternetConfirmZoneCrossing` | `0x191990` | 185 | UnwindData |  |
| 271 | `InternetConfirmZoneCrossingA` | `0x191990` | 185 | UnwindData |  |
| 272 | `InternetConfirmZoneCrossingW` | `0x191A50` | 185 | UnwindData |  |
| 153 | `DeleteWpadCacheForNetworks` | `0x1983A0` | 389 | UnwindData |  |
| 401 | *Ordinal Only* | `0x198530` | 69 | UnwindData |  |
| 306 | `InternetGetProxyForUrl` | `0x198800` | 71 | UnwindData |  |
| 106 | `AppCacheCheckManifest` | `0x19CD80` | 120 | UnwindData |  |
| 113 | `AppCacheCreateAndCommitFile` | `0x19CE00` | 82 | UnwindData |  |
| 114 | `AppCacheDeleteGroup` | `0x19CE60` | 71 | UnwindData |  |
| 115 | `AppCacheDeleteIEGroup` | `0x19CEB0` | 71 | UnwindData |  |
| 119 | `AppCacheDuplicateHandle` | `0x19CF00` | 71 | UnwindData |  |
| 124 | `AppCacheFinalize` | `0x19CF50` | 71 | UnwindData |  |
| 125 | `AppCacheFreeDownloadList` | `0x19CFA0` | 213 | UnwindData |  |
| 126 | `AppCacheFreeGroupList` | `0x19D080` | 112 | UnwindData |  |
| 127 | `AppCacheFreeIESpace` | `0x19D100` | 71 | UnwindData |  |
| 128 | `AppCacheFreeSpace` | `0x19D150` | 71 | UnwindData |  |
| 129 | `AppCacheGetDownloadList` | `0x19D1A0` | 71 | UnwindData |  |
| 130 | `AppCacheGetFallbackUrl` | `0x19D1F0` | 71 | UnwindData |  |
| 132 | `AppCacheGetIEGroupList` | `0x19D240` | 71 | UnwindData |  |
| 133 | `AppCacheGetInfo` | `0x19D290` | 71 | UnwindData |  |
| 134 | `AppCacheGetManifestUrl` | `0x19D2E0` | 71 | UnwindData |  |
| 135 | `AppCacheLookup` | `0x19D330` | 71 | UnwindData |  |
| 142 | `CreateUrlCacheEntryA` | `0x19E3A0` | 604 | UnwindData |  |
| 145 | `CreateUrlCacheGroup` | `0x19E610` | 313 | UnwindData |  |
| 152 | `DeleteUrlCacheGroup` | `0x19E750` | 249 | UnwindData |  |
| 163 | `FindFirstUrlCacheContainerW` | `0x19E850` | 478 | UnwindData |  |
| 166 | `FindFirstUrlCacheEntryExW` | `0x19EA40` | 465 | UnwindData |  |
| 168 | `FindFirstUrlCacheGroup` | `0x19EC20` | 326 | UnwindData |  |
| 170 | `FindNextUrlCacheContainerW` | `0x19ED70` | 412 | UnwindData |  |
| 173 | `FindNextUrlCacheEntryExW` | `0x19EF20` | 567 | UnwindData |  |
| 175 | `FindNextUrlCacheGroup` | `0x19F160` | 284 | UnwindData |  |
| 178 | `FreeUrlCacheSpaceA` | `0x19F290` | 560 | UnwindData |  |
| 179 | `FreeUrlCacheSpaceW` | `0x19F4D0` | 250 | UnwindData |  |
| 206 | `GetUrlCacheConfigInfoA` | `0x19F5D0` | 669 | UnwindData |  |
| 209 | `GetUrlCacheEntryInfoA` | `0x19F880` | 486 | UnwindData |  |
| 210 | `GetUrlCacheEntryInfoExA` | `0x19FA70` | 613 | UnwindData |  |
| 213 | `GetUrlCacheGroupAttributeA` | `0x19FCE0` | 585 | UnwindData |  |
| 214 | `GetUrlCacheGroupAttributeW` | `0x19FF30` | 533 | UnwindData |  |
| 363 | `IsUrlCacheEntryExpiredA` | `0x1A0150` | 342 | UnwindData |  |
| 364 | `IsUrlCacheEntryExpiredW` | `0x1A02B0` | 364 | UnwindData |  |
| 369 | `ReadUrlCacheEntryStream` | `0x1A0430` | 283 | UnwindData |  |
| 373 | `RetrieveUrlCacheEntryFileA` | `0x1A0560` | 550 | UnwindData |  |
| 375 | `RetrieveUrlCacheEntryStreamA` | `0x1A0790` | 592 | UnwindData |  |
| 376 | `RetrieveUrlCacheEntryStreamW` | `0x1A09F0` | 601 | UnwindData |  |
| 378 | `SetUrlCacheConfigInfoA` | `0x1A0C50` | 333 | UnwindData |  |
| 379 | `SetUrlCacheConfigInfoW` | `0x1A0DB0` | 277 | UnwindData |  |
| 380 | `SetUrlCacheEntryGroup` | `0x1A0ED0` | 500 | UnwindData |  |
| 381 | `SetUrlCacheEntryGroupA` | `0x1A0ED0` | 500 | UnwindData |  |
| 382 | `SetUrlCacheEntryGroupW` | `0x1A10D0` | 518 | UnwindData |  |
| 384 | `SetUrlCacheEntryInfoW` | `0x1A12E0` | 521 | UnwindData |  |
| 385 | `SetUrlCacheGroupAttributeA` | `0x1A14F0` | 530 | UnwindData |  |
| 386 | `SetUrlCacheGroupAttributeW` | `0x1A1710` | 470 | UnwindData |  |
| 387 | `SetUrlCacheHeaderData` | `0x1A18F0` | 322 | UnwindData |  |
| 392 | `UnlockUrlCacheEntryFile` | `0x1A1A40` | 316 | UnwindData |  |
| 393 | `UnlockUrlCacheEntryFileA` | `0x1A1A40` | 316 | UnwindData |  |
| 396 | `UpdateUrlCacheContentPath` | `0x1A1B90` | 313 | UnwindData |  |
| 397 | `UrlCacheCheckEntriesExist` | `0x1A1CD0` | 71 | UnwindData |  |
| 398 | `UrlCacheCloseEntryHandle` | `0x1A1D20` | 52 | UnwindData |  |
| 399 | `UrlCacheContainerSetEntryMaximumAge` | `0x1A1D60` | 71 | UnwindData |  |
| 400 | `UrlCacheCreateContainer` | `0x1A1DB0` | 82 | UnwindData |  |
| 407 | `UrlCacheFreeGlobalSpace` | `0x1A1E10` | 223 | UnwindData |  |
| 408 | `UrlCacheGetContentPaths` | `0x1A1F00` | 71 | UnwindData |  |
| 409 | `UrlCacheGetEntryInfo` | `0x1A1F50` | 71 | UnwindData |  |
| 412 | `UrlCacheGetGlobalCacheSize` | `0x1A1FA0` | 260 | UnwindData |  |
| 414 | `UrlCacheGetGlobalLimit` | `0x1A20B0` | 71 | UnwindData |  |
| 415 | `UrlCacheReadEntryStream` | `0x1A2100` | 84 | UnwindData |  |
| 416 | `UrlCacheReloadSettings` | `0x1A2160` | 71 | UnwindData |  |
| 417 | `UrlCacheRetrieveEntryFile` | `0x1A21B0` | 71 | UnwindData |  |
| 418 | `UrlCacheRetrieveEntryStream` | `0x1A2200` | 84 | UnwindData |  |
| 424 | `UrlCacheSetGlobalLimit` | `0x1A2260` | 71 | UnwindData |  |
| 411 | *Ordinal Only* | `0x1A4650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | *Ordinal Only* | `0x1A4670` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | *Ordinal Only* | `0x1A4860` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `DeleteIE3Cache` | `0x1A4910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | *Ordinal Only* | `0x1A4920` | 224 | UnwindData |  |
| 346 | *Ordinal Only* | `0x1A4A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | *Ordinal Only* | `0x1A4A20` | 564 | UnwindData |  |
| 254 | `HttpWebSocketShutdown` | `0x1A9CF0` | 297 | UnwindData |  |
