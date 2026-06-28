# Binary Specification: wininet.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wininet.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cf280341b2118571a7021861bab524b3fcc20f83db3d45baf27cec386ee819a1`
* **Total Exported Functions:** 327

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 227 | `HttpAddRequestHeadersW` | `0xDAB0` | 671 | UnwindData |  |
| 226 | `HttpAddRequestHeadersA` | `0xF430` | 844 | UnwindData |  |
| 300 | `InternetGetCookieExW` | `0x13510` | 1,005 | UnwindData |  |
| 289 | `InternetFreeCookies` | `0x13910` | 380 | UnwindData |  |
| 298 | `InternetGetCookieEx2` | `0x13AA0` | 86 | UnwindData |  |
| 332 | `InternetSetCookieExW` | `0x13C20` | 1,223 | UnwindData |  |
| 296 | `InternetGetConnectedStateExW` | `0x16020` | 909 | UnwindData |  |
| 323 | `InternetQueryOptionW` | `0x26680` | 2,996 | UnwindData |  |
| 322 | `InternetQueryOptionA` | `0x276A0` | 9,416 | UnwindData |  |
| 338 | `InternetSetOptionA` | `0x2A3C0` | 12,933 | UnwindData |  |
| 243 | `HttpQueryInfoA` | `0x2EDB0` | 46 | UnwindData |  |
| 239 | `HttpOpenRequestW` | `0x41FA0` | 2,507 | UnwindData |  |
| 279 | `InternetCreateUrlW` | `0x44990` | 3,766 | UnwindData |  |
| 278 | `InternetCreateUrlA` | `0x46B90` | 159 | UnwindData |  |
| 276 | `InternetCrackUrlA` | `0x46C40` | 160 | UnwindData |  |
| 367 | `PrivacyGetZonePreferenceW` | `0x48390` | 965 | UnwindData |  |
| 116 | *Ordinal Only* | `0x496D0` | 263 | UnwindData |  |
| 229 | `HttpCloseDependencyHandle` | `0x4C170` | 47 | UnwindData |  |
| 277 | `InternetCrackUrlW` | `0x62320` | 3,272 | UnwindData |  |
| 314 | `InternetInitializeAutoProxyDll` | `0x7ED40` | 548 | UnwindData |  |
| 362 | `IsHostInProxyBypassList` | `0x85240` | 1,850 | UnwindData |  |
| 208 | `GetUrlCacheEntryBinaryBlob` | `0x8E560` | 111 | UnwindData |  |
| 212 | `GetUrlCacheEntryInfoW` | `0x90A20` | 964 | UnwindData |  |
| 174 | `FindNextUrlCacheEntryW` | `0x925A0` | 613 | UnwindData |  |
| 172 | `FindNextUrlCacheEntryExA` | `0x92810` | 652 | UnwindData |  |
| 171 | `FindNextUrlCacheEntryA` | `0x94B60` | 623 | UnwindData |  |
| 169 | `FindNextUrlCacheContainerA` | `0x94DE0` | 477 | UnwindData |  |
| 138 | `CommitUrlCacheEntryW` | `0x953F0` | 939 | UnwindData |  |
| 137 | `CommitUrlCacheEntryBinaryBlob` | `0x96640` | 97 | UnwindData |  |
| 374 | `RetrieveUrlCacheEntryFileW` | `0x96A10` | 659 | UnwindData |  |
| 162 | `FindFirstUrlCacheContainerA` | `0x96CB0` | 567 | UnwindData |  |
| 165 | `FindFirstUrlCacheEntryExA` | `0x97140` | 525 | UnwindData |  |
| 148 | `DeleteUrlCacheContainerW` | `0x98830` | 285 | UnwindData |  |
| 404 | `UrlCacheFindFirstEntry` | `0x98C20` | 97 | UnwindData |  |
| 161 | `FindCloseUrlCache` | `0x98EA0` | 275 | UnwindData |  |
| 395 | `UnlockUrlCacheEntryStream` | `0x98FC0` | 254 | UnwindData |  |
| 140 | `CreateUrlCacheContainerA` | `0x99830` | 684 | UnwindData |  |
| 149 | `DeleteUrlCacheEntry` | `0x99B80` | 370 | UnwindData |  |
| 150 | `DeleteUrlCacheEntryA` | `0x99B80` | 370 | UnwindData |  |
| 151 | `DeleteUrlCacheEntryW` | `0x99E30` | 389 | UnwindData |  |
| 383 | `SetUrlCacheEntryInfoA` | `0x9AB30` | 716 | UnwindData |  |
| 236 | `HttpIsHostHstsEnabled` | `0xA8030` | 73 | UnwindData |  |
| 215 | `GetUrlCacheHeaderData` | `0xABCE0` | 403 | UnwindData |  |
| 250 | `HttpWebSocketCompleteUpgrade` | `0xC58C0` | 211 | UnwindData |  |
| 252 | `HttpWebSocketReceive` | `0xC6520` | 340 | UnwindData |  |
| 253 | `HttpWebSocketSend` | `0xC6820` | 321 | UnwindData |  |
| 249 | `HttpWebSocketClose` | `0xC8BB0` | 310 | UnwindData |  |
| 251 | `HttpWebSocketQueryCloseStatus` | `0xC8EA0` | 324 | UnwindData |  |
| 265 | `InternetCheckConnectionW` | `0xC91E0` | 298 | UnwindData |  |
| 264 | `InternetCheckConnectionA` | `0xC9310` | 1,370 | UnwindData |  |
| 273 | `InternetConnectA` | `0xC9A20` | 516 | UnwindData |  |
| 316 | `InternetOpenA` | `0xCAE10` | 195 | UnwindData |  |
| 319 | `InternetOpenW` | `0xCB0F0` | 988 | UnwindData |  |
| 359 | `InternetWriteFile` | `0xCC690` | 117 | UnwindData |  |
| 325 | `InternetReadFileExA` | `0xCD210` | 1,586 | UnwindData |  |
| 324 | `InternetReadFile` | `0xCDAB0` | 117 | UnwindData |  |
| 269 | `InternetCombineUrlW` | `0xD6390` | 296 | UnwindData |  |
| 274 | `InternetConnectW` | `0xDD920` | 1,656 | UnwindData |  |
| 155 | `DispatchAPICall` | `0xF2240` | 3,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `InternetSetOptionW` | `0xF30B0` | 3,696 | UnwindData |  |
| 370 | `ReadUrlCacheEntryStreamEx` | `0x106CF0` | 902 | UnwindData |  |
| 315 | `InternetLockRequestFile` | `0x107080` | 1,090 | UnwindData |  |
| 348 | `InternetSetStatusCallbackW` | `0x108550` | 415 | UnwindData |  |
| 345 | `InternetSetStatusCallback` | `0x10A660` | 170 | UnwindData |  |
| 347 | `InternetSetStatusCallbackA` | `0x10A660` | 170 | UnwindData |  |
| 248 | `HttpSendRequestW` | `0x10DE50` | 747 | UnwindData |  |
| 358 | `InternetUnlockRequestFile` | `0x10F3C0` | 1,157 | UnwindData |  |
| 211 | `GetUrlCacheEntryInfoExW` | `0x10F850` | 720 | UnwindData |  |
| 263 | `InternetCanonicalizeUrlW` | `0x1158A0` | 303 | UnwindData |  |
| 267 | `InternetCloseHandle` | `0x117CC0` | 70 | UnwindData |  |
| 238 | `HttpOpenRequestA` | `0x117D60` | 181 | UnwindData |  |
| 245 | `HttpSendRequestA` | `0x117E20` | 329 | UnwindData |  |
| 330 | `InternetSetCookieEx2` | `0x119050` | 86 | UnwindData |  |
| 247 | `HttpSendRequestExW` | `0x11A5A0` | 692 | UnwindData |  |
| 293 | `InternetGetConnectedState` | `0x11D510` | 163 | UnwindData |  |
| 268 | `InternetCombineUrlA` | `0x11DD00` | 307 | UnwindData |  |
| 405 | `UrlCacheFindNextEntry` | `0x11F360` | 73 | UnwindData |  |
| 157 | `DllGetClassObject` | `0x11FA30` | 107 | UnwindData |  |
| 309 | `InternetGetSecurityInfoByURLW` | `0x120370` | 303 | UnwindData |  |
| 307 | `InternetGetSecurityInfoByURL` | `0x1204B0` | 364 | UnwindData |  |
| 308 | `InternetGetSecurityInfoByURLA` | `0x1204B0` | 364 | UnwindData |  |
| 156 | `DllCanUnloadNow` | `0x122BD0` | 42 | UnwindData |  |
| 230 | `HttpDuplicateDependencyHandle` | `0x123DC0` | 73 | UnwindData |  |
| 326 | `InternetReadFileExW` | `0x127940` | 289 | UnwindData |  |
| 231 | `HttpEndRequestA` | `0x127A70` | 278 | UnwindData |  |
| 233 | `HttpGetServerCredentials` | `0x12AC00` | 71 | UnwindData |  |
| 246 | `HttpSendRequestExA` | `0x12D290` | 373 | UnwindData |  |
| 420 | *Ordinal Only* | `0x12EC70` | 73 | UnwindData |  |
| 318 | `InternetOpenUrlW` | `0x12FB00` | 761 | UnwindData |  |
| 317 | `InternetOpenUrlA` | `0x12FE00` | 143 | UnwindData |  |
| 232 | `HttpEndRequestW` | `0x1316A0` | 300 | UnwindData |  |
| 421 | *Ordinal Only* | `0x132F20` | 75 | UnwindData |  |
| 425 | `UrlCacheUpdateEntryExtraData` | `0x133C00` | 71 | UnwindData |  |
| 406 | `UrlCacheFreeEntryInfo` | `0x136B10` | 105 | UnwindData |  |
| 158 | `DllInstall` | `0x1378B0` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `InternetGetCertByURL` | `0x1378B0` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `InternetGetCertByURLA` | `0x1378B0` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `RunOnceUrlCache` | `0x1378B0` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | *Ordinal Only* | `0x1378B0` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `UnlockUrlCacheEntryFileW` | `0x137D90` | 346 | UnwindData |  |
| 141 | `CreateUrlCacheContainerW` | `0x1380B0` | 495 | UnwindData |  |
| 371 | `RegisterUrlCacheNotification` | `0x139290` | 3,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `UrlCacheServer` | `0x139290` | 3,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | *Ordinal Only* | `0x139290` | 3,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `InternetErrorDlg` | `0x139F60` | 1,682 | UnwindData |  |
| 144 | `CreateUrlCacheEntryW` | `0x13A740` | 28 | UnwindData |  |
| 143 | `CreateUrlCacheEntryExW` | `0x13A770` | 537 | UnwindData |  |
| 290 | `InternetFreeProxyInfoList` | `0x13B8E0` | 53 | UnwindData |  |
| 154 | `DetectAutoProxyUrl` | `0x13C960` | 379 | UnwindData |  |
| 167 | `FindFirstUrlCacheEntryW` | `0x13EBB0` | 385 | UnwindData |  |
| 107 | `AppCacheCloseHandle` | `0x140280` | 47 | UnwindData |  |
| 207 | `GetUrlCacheConfigInfoW` | `0x1407F0` | 286 | UnwindData |  |
| 255 | `IncrementUrlCacheHeaderData` | `0x140A80` | 271 | UnwindData |  |
| 147 | `DeleteUrlCacheContainerA` | `0x141660` | 324 | UnwindData |  |
| 136 | `CommitUrlCacheEntryA` | `0x143050` | 677 | UnwindData |  |
| 164 | `FindFirstUrlCacheEntryA` | `0x143520` | 382 | UnwindData |  |
| 339 | `InternetSetOptionExA` | `0x143BC0` | 258 | UnwindData |  |
| 131 | `AppCacheGetGroupList` | `0x1452E0` | 71 | UnwindData |  |
| 320 | `InternetQueryDataAvailable` | `0x146B30` | 30 | UnwindData |  |
| 244 | `HttpQueryInfoW` | `0x1477E0` | 28 | UnwindData |  |
| 352 | `InternetTimeFromSystemTime` | `0x157620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `InternetTimeFromSystemTimeA` | `0x157620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 354 | `InternetTimeFromSystemTimeW` | `0x157630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `InternetTimeToSystemTime` | `0x157640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `InternetTimeToSystemTimeA` | `0x157640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `InternetTimeToSystemTimeW` | `0x157650` | 6,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `GetProxyDllInfo` | `0x158F20` | 3,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | *Ordinal Only* | `0x159BD0` | 29 | UnwindData |  |
| 159 | `DllRegisterServer` | `0x160B20` | 52 | UnwindData |  |
| 160 | `DllUnregisterServer` | `0x160B60` | 52 | UnwindData |  |
| 139 | `CreateMD5SSOHash` | `0x1626A0` | 715 | UnwindData |  |
| 176 | `ForceNexusLookup` | `0x162980` | 66 | UnwindData |  |
| 177 | `ForceNexusLookupExW` | `0x1629D0` | 127 | UnwindData |  |
| 426 | `UrlZonesDetach` | `0x1648F0` | 158 | UnwindData |  |
| 275 | `InternetConvertUrlFromWireToWideChar` | `0x169580` | 149 | UnwindData |  |
| 427 | `_GetFileExtensionFromUrl` | `0x169F70` | 124 | UnwindData |  |
| 235 | `HttpIndicatePageLoadComplete` | `0x16C220` | 44 | UnwindData |  |
| 237 | `HttpOpenDependencyHandle` | `0x16C260` | 71 | UnwindData |  |
| 234 | `HttpGetTunnelSocket` | `0x16C510` | 246 | UnwindData |  |
| 240 | `HttpPushClose` | `0x16D3E0` | 47 | UnwindData |  |
| 241 | `HttpPushEnable` | `0x16D420` | 71 | UnwindData |  |
| 242 | `HttpPushWait` | `0x16D470` | 71 | UnwindData |  |
| 288 | `InternetFortezzaCommand` | `0x16D590` | 110 | UnwindData |  |
| 321 | `InternetQueryFortezzaStatus` | `0x16D610` | 105 | UnwindData |  |
| 101 | *Ordinal Only* | `0x173460` | 289 | UnwindData |  |
| 109 | *Ordinal Only* | `0x173700` | 154 | UnwindData |  |
| 111 | *Ordinal Only* | `0x1737A0` | 1,226 | UnwindData |  |
| 120 | *Ordinal Only* | `0x173C70` | 32 | UnwindData |  |
| 121 | *Ordinal Only* | `0x173C70` | 32 | UnwindData |  |
| 122 | *Ordinal Only* | `0x173C70` | 32 | UnwindData |  |
| 123 | *Ordinal Only* | `0x173C70` | 32 | UnwindData |  |
| 108 | *Ordinal Only* | `0x173EA0` | 138 | UnwindData |  |
| 110 | *Ordinal Only* | `0x173F30` | 1,212 | UnwindData |  |
| 258 | `InternetAttemptConnect` | `0x175050` | 94 | UnwindData |  |
| 262 | `InternetCanonicalizeUrlA` | `0x1750C0` | 283 | UnwindData |  |
| 302 | `InternetGetLastResponseInfoA` | `0x1751F0` | 463 | UnwindData |  |
| 337 | `InternetSetFilePointer` | `0x1753D0` | 470 | UnwindData |  |
| 349 | `InternetShowSecurityInfoByURL` | `0x1755B0` | 238 | UnwindData |  |
| 350 | `InternetShowSecurityInfoByURLA` | `0x1755B0` | 238 | UnwindData |  |
| 216 | `GopherCreateLocatorA` | `0x1756B0` | 29 | UnwindData |  |
| 217 | `GopherCreateLocatorW` | `0x1756B0` | 29 | UnwindData |  |
| 218 | `GopherFindFirstFileA` | `0x1756B0` | 29 | UnwindData |  |
| 219 | `GopherFindFirstFileW` | `0x1756B0` | 29 | UnwindData |  |
| 220 | `GopherGetAttributeA` | `0x1756B0` | 29 | UnwindData |  |
| 221 | `GopherGetAttributeW` | `0x1756B0` | 29 | UnwindData |  |
| 222 | `GopherGetLocatorTypeA` | `0x1756B0` | 29 | UnwindData |  |
| 223 | `GopherGetLocatorTypeW` | `0x1756B0` | 29 | UnwindData |  |
| 224 | `GopherOpenFileA` | `0x1756B0` | 29 | UnwindData |  |
| 225 | `GopherOpenFileW` | `0x1756B0` | 29 | UnwindData |  |
| 360 | `InternetWriteFileExA` | `0x1756B0` | 29 | UnwindData |  |
| 361 | `InternetWriteFileExW` | `0x1756B0` | 29 | UnwindData |  |
| 365 | `LoadUrlCacheContent` | `0x1756B0` | 29 | UnwindData |  |
| 259 | `InternetAutodial` | `0x1756E0` | 184 | UnwindData |  |
| 261 | `InternetAutodialHangup` | `0x1757A0` | 172 | UnwindData |  |
| 280 | `InternetDial` | `0x175860` | 200 | UnwindData |  |
| 281 | `InternetDialA` | `0x175860` | 200 | UnwindData |  |
| 282 | `InternetDialW` | `0x175930` | 200 | UnwindData |  |
| 310 | `InternetGoOnline` | `0x175A00` | 176 | UnwindData |  |
| 311 | `InternetGoOnlineA` | `0x175A00` | 176 | UnwindData |  |
| 312 | `InternetGoOnlineW` | `0x175AC0` | 195 | UnwindData |  |
| 313 | `InternetHangUp` | `0x175B90` | 153 | UnwindData |  |
| 334 | `InternetSetDialState` | `0x175C30` | 94 | UnwindData |  |
| 335 | `InternetSetDialStateA` | `0x175C30` | 94 | UnwindData |  |
| 336 | `InternetSetDialStateW` | `0x175CA0` | 94 | UnwindData |  |
| 260 | `InternetAutodialCallback` | `0x175D10` | 88 | UnwindData |  |
| 294 | `InternetGetConnectedStateEx` | `0x175D70` | 266 | UnwindData |  |
| 295 | `InternetGetConnectedStateExA` | `0x175D70` | 266 | UnwindData |  |
| 303 | `InternetGetLastResponseInfoW` | `0x175EC0` | 478 | UnwindData |  |
| 344 | `InternetSetSecureLegacyServersAppCompat` | `0x1760B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `InternetShowSecurityInfoByURLW` | `0x1760D0` | 288 | UnwindData |  |
| 340 | `InternetSetOptionExW` | `0x1766A0` | 258 | UnwindData |  |
| 422 | *Ordinal Only* | `0x1767B0` | 71 | UnwindData |  |
| 423 | *Ordinal Only* | `0x176800` | 47 | UnwindData |  |
| 372 | `ResumeSuspendedDownload` | `0x177120` | 245 | UnwindData |  |
| 180 | `FtpCommandA` | `0x17B1A0` | 230 | UnwindData |  |
| 182 | `FtpCreateDirectoryA` | `0x17B4F0` | 164 | UnwindData |  |
| 184 | `FtpDeleteFileA` | `0x17B5A0` | 164 | UnwindData |  |
| 186 | `FtpFindFirstFileA` | `0x17B650` | 230 | UnwindData |  |
| 188 | `FtpGetCurrentDirectoryA` | `0x17B910` | 198 | UnwindData |  |
| 190 | `FtpGetFileA` | `0x17B9E0` | 608 | UnwindData |  |
| 192 | `FtpGetFileSize` | `0x17BC50` | 655 | UnwindData |  |
| 194 | `FtpOpenFileA` | `0x17BEF0` | 224 | UnwindData |  |
| 196 | `FtpPutFileA` | `0x17BFE0` | 564 | UnwindData |  |
| 199 | `FtpRemoveDirectoryA` | `0x17C3E0` | 164 | UnwindData |  |
| 201 | `FtpRenameFileA` | `0x17C490` | 183 | UnwindData |  |
| 203 | `FtpSetCurrentDirectoryA` | `0x17C550` | 164 | UnwindData |  |
| 286 | `InternetFindNextFileA` | `0x17EB10` | 88 | UnwindData |  |
| 181 | `FtpCommandW` | `0x17F2C0` | 440 | UnwindData |  |
| 183 | `FtpCreateDirectoryW` | `0x17F480` | 405 | UnwindData |  |
| 185 | `FtpDeleteFileW` | `0x17F620` | 405 | UnwindData |  |
| 187 | `FtpFindFirstFileW` | `0x17F7C0` | 508 | UnwindData |  |
| 189 | `FtpGetCurrentDirectoryW` | `0x17F9D0` | 440 | UnwindData |  |
| 191 | `FtpGetFileEx` | `0x17FB90` | 437 | UnwindData |  |
| 193 | `FtpGetFileW` | `0x17FD50` | 259 | UnwindData |  |
| 195 | `FtpOpenFileW` | `0x17FE60` | 137 | UnwindData |  |
| 197 | `FtpPutFileEx` | `0x17FEF0` | 393 | UnwindData |  |
| 198 | `FtpPutFileW` | `0x180080` | 213 | UnwindData |  |
| 200 | `FtpRemoveDirectoryW` | `0x180160` | 393 | UnwindData |  |
| 202 | `FtpRenameFileW` | `0x1802F0` | 589 | UnwindData |  |
| 204 | `FtpSetCurrentDirectoryW` | `0x180550` | 393 | UnwindData |  |
| 287 | `InternetFindNextFileW` | `0x180BC0` | 399 | UnwindData |  |
| 118 | *Ordinal Only* | `0x18AAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `PrivacySetZonePreferenceW` | `0x18AAF0` | 683 | UnwindData |  |
| 228 | `HttpCheckDavCompliance` | `0x18ADB0` | 192 | UnwindData |  |
| 104 | *Ordinal Only* | `0x18ADB0` | 192 | UnwindData |  |
| 105 | *Ordinal Only* | `0x18AE80` | 192 | UnwindData |  |
| 266 | `InternetClearAllPerSiteCookieDecisions` | `0x18BFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `InternetEnumPerSiteCookieDecisionA` | `0x18BFF0` | 105 | UnwindData |  |
| 284 | `InternetEnumPerSiteCookieDecisionW` | `0x18C060` | 232 | UnwindData |  |
| 304 | `InternetGetPerSiteCookieDecisionA` | `0x18C150` | 73 | UnwindData |  |
| 305 | `InternetGetPerSiteCookieDecisionW` | `0x18C1A0` | 164 | UnwindData |  |
| 342 | `InternetSetPerSiteCookieDecisionA` | `0x18C250` | 187 | UnwindData |  |
| 343 | `InternetSetPerSiteCookieDecisionW` | `0x18C320` | 157 | UnwindData |  |
| 297 | `InternetGetCookieA` | `0x18D700` | 28 | UnwindData |  |
| 299 | `InternetGetCookieExA` | `0x18D730` | 859 | UnwindData |  |
| 301 | `InternetGetCookieW` | `0x18DAA0` | 26 | UnwindData |  |
| 329 | `InternetSetCookieA` | `0x18DAC0` | 34 | UnwindData |  |
| 331 | `InternetSetCookieExA` | `0x18DAF0` | 162 | UnwindData |  |
| 333 | `InternetSetCookieW` | `0x18DBA0` | 510 | UnwindData |  |
| 117 | *Ordinal Only* | `0x18DDB0` | 290 | UnwindData |  |
| 256 | `InternetAlgIdToStringA` | `0x197780` | 504 | UnwindData |  |
| 257 | `InternetAlgIdToStringW` | `0x197980` | 504 | UnwindData |  |
| 327 | `InternetSecurityProtocolToStringA` | `0x197B80` | 375 | UnwindData |  |
| 328 | `InternetSecurityProtocolToStringW` | `0x197D00` | 375 | UnwindData |  |
| 366 | `ParseX509EncodedCertificateForListBoxEntry` | `0x197E80` | 32 | UnwindData |  |
| 388 | `ShowCertificate` | `0x197E80` | 32 | UnwindData |  |
| 389 | `ShowClientAuthCerts` | `0x197E80` | 32 | UnwindData |  |
| 390 | `ShowSecurityInfo` | `0x197EB0` | 370 | UnwindData |  |
| 391 | `ShowX509EncodedCertificate` | `0x198030` | 132 | UnwindData |  |
| 270 | `InternetConfirmZoneCrossing` | `0x1986B0` | 193 | UnwindData |  |
| 271 | `InternetConfirmZoneCrossingA` | `0x1986B0` | 193 | UnwindData |  |
| 272 | `InternetConfirmZoneCrossingW` | `0x198780` | 193 | UnwindData |  |
| 153 | `DeleteWpadCacheForNetworks` | `0x19F370` | 407 | UnwindData |  |
| 401 | *Ordinal Only* | `0x19F510` | 79 | UnwindData |  |
| 306 | `InternetGetProxyForUrl` | `0x19F800` | 71 | UnwindData |  |
| 106 | `AppCacheCheckManifest` | `0x1A4270` | 120 | UnwindData |  |
| 113 | `AppCacheCreateAndCommitFile` | `0x1A42F0` | 82 | UnwindData |  |
| 114 | `AppCacheDeleteGroup` | `0x1A4350` | 71 | UnwindData |  |
| 115 | `AppCacheDeleteIEGroup` | `0x1A43A0` | 71 | UnwindData |  |
| 119 | `AppCacheDuplicateHandle` | `0x1A43F0` | 71 | UnwindData |  |
| 124 | `AppCacheFinalize` | `0x1A4440` | 71 | UnwindData |  |
| 125 | `AppCacheFreeDownloadList` | `0x1A4490` | 223 | UnwindData |  |
| 126 | `AppCacheFreeGroupList` | `0x1A4580` | 122 | UnwindData |  |
| 127 | `AppCacheFreeIESpace` | `0x1A4600` | 71 | UnwindData |  |
| 128 | `AppCacheFreeSpace` | `0x1A4650` | 71 | UnwindData |  |
| 129 | `AppCacheGetDownloadList` | `0x1A46A0` | 71 | UnwindData |  |
| 130 | `AppCacheGetFallbackUrl` | `0x1A46F0` | 71 | UnwindData |  |
| 132 | `AppCacheGetIEGroupList` | `0x1A4740` | 71 | UnwindData |  |
| 133 | `AppCacheGetInfo` | `0x1A4790` | 71 | UnwindData |  |
| 134 | `AppCacheGetManifestUrl` | `0x1A47E0` | 71 | UnwindData |  |
| 135 | `AppCacheLookup` | `0x1A4830` | 71 | UnwindData |  |
| 142 | `CreateUrlCacheEntryA` | `0x1A5900` | 616 | UnwindData |  |
| 145 | `CreateUrlCacheGroup` | `0x1A5B70` | 330 | UnwindData |  |
| 152 | `DeleteUrlCacheGroup` | `0x1A5CC0` | 259 | UnwindData |  |
| 163 | `FindFirstUrlCacheContainerW` | `0x1A5DD0` | 488 | UnwindData |  |
| 166 | `FindFirstUrlCacheEntryExW` | `0x1A5FC0` | 475 | UnwindData |  |
| 168 | `FindFirstUrlCacheGroup` | `0x1A61B0` | 337 | UnwindData |  |
| 170 | `FindNextUrlCacheContainerW` | `0x1A6310` | 429 | UnwindData |  |
| 173 | `FindNextUrlCacheEntryExW` | `0x1A64D0` | 595 | UnwindData |  |
| 175 | `FindNextUrlCacheGroup` | `0x1A6730` | 300 | UnwindData |  |
| 178 | `FreeUrlCacheSpaceA` | `0x1A6870` | 577 | UnwindData |  |
| 179 | `FreeUrlCacheSpaceW` | `0x1A6AC0` | 260 | UnwindData |  |
| 206 | `GetUrlCacheConfigInfoA` | `0x1A6BD0` | 686 | UnwindData |  |
| 209 | `GetUrlCacheEntryInfoA` | `0x1A6E90` | 506 | UnwindData |  |
| 210 | `GetUrlCacheEntryInfoExA` | `0x1A7090` | 625 | UnwindData |  |
| 213 | `GetUrlCacheGroupAttributeA` | `0x1A7310` | 598 | UnwindData |  |
| 214 | `GetUrlCacheGroupAttributeW` | `0x1A7570` | 562 | UnwindData |  |
| 363 | `IsUrlCacheEntryExpiredA` | `0x1A77B0` | 353 | UnwindData |  |
| 364 | `IsUrlCacheEntryExpiredW` | `0x1A7920` | 381 | UnwindData |  |
| 369 | `ReadUrlCacheEntryStream` | `0x1A7AB0` | 294 | UnwindData |  |
| 373 | `RetrieveUrlCacheEntryFileA` | `0x1A7BE0` | 562 | UnwindData |  |
| 375 | `RetrieveUrlCacheEntryStreamA` | `0x1A7E20` | 607 | UnwindData |  |
| 376 | `RetrieveUrlCacheEntryStreamW` | `0x1A8090` | 616 | UnwindData |  |
| 378 | `SetUrlCacheConfigInfoA` | `0x1A8300` | 349 | UnwindData |  |
| 379 | `SetUrlCacheConfigInfoW` | `0x1A8470` | 292 | UnwindData |  |
| 380 | `SetUrlCacheEntryGroup` | `0x1A85A0` | 510 | UnwindData |  |
| 381 | `SetUrlCacheEntryGroupA` | `0x1A85A0` | 510 | UnwindData |  |
| 382 | `SetUrlCacheEntryGroupW` | `0x1A87B0` | 528 | UnwindData |  |
| 384 | `SetUrlCacheEntryInfoW` | `0x1A89D0` | 531 | UnwindData |  |
| 385 | `SetUrlCacheGroupAttributeA` | `0x1A8BF0` | 543 | UnwindData |  |
| 386 | `SetUrlCacheGroupAttributeW` | `0x1A8E20` | 483 | UnwindData |  |
| 387 | `SetUrlCacheHeaderData` | `0x1A9010` | 338 | UnwindData |  |
| 392 | `UnlockUrlCacheEntryFile` | `0x1A9170` | 331 | UnwindData |  |
| 393 | `UnlockUrlCacheEntryFileA` | `0x1A9170` | 331 | UnwindData |  |
| 396 | `UpdateUrlCacheContentPath` | `0x1A92D0` | 328 | UnwindData |  |
| 397 | `UrlCacheCheckEntriesExist` | `0x1A9420` | 71 | UnwindData |  |
| 398 | `UrlCacheCloseEntryHandle` | `0x1A9470` | 52 | UnwindData |  |
| 399 | `UrlCacheContainerSetEntryMaximumAge` | `0x1A94B0` | 71 | UnwindData |  |
| 400 | `UrlCacheCreateContainer` | `0x1A9500` | 82 | UnwindData |  |
| 407 | `UrlCacheFreeGlobalSpace` | `0x1A9560` | 239 | UnwindData |  |
| 408 | `UrlCacheGetContentPaths` | `0x1A9660` | 71 | UnwindData |  |
| 409 | `UrlCacheGetEntryInfo` | `0x1A96B0` | 71 | UnwindData |  |
| 412 | `UrlCacheGetGlobalCacheSize` | `0x1A9700` | 275 | UnwindData |  |
| 414 | `UrlCacheGetGlobalLimit` | `0x1A9820` | 71 | UnwindData |  |
| 415 | `UrlCacheReadEntryStream` | `0x1A9870` | 84 | UnwindData |  |
| 416 | `UrlCacheReloadSettings` | `0x1A98D0` | 71 | UnwindData |  |
| 417 | `UrlCacheRetrieveEntryFile` | `0x1A9920` | 71 | UnwindData |  |
| 418 | `UrlCacheRetrieveEntryStream` | `0x1A9970` | 84 | UnwindData |  |
| 424 | `UrlCacheSetGlobalLimit` | `0x1A99D0` | 71 | UnwindData |  |
| 411 | *Ordinal Only* | `0x1AC780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | *Ordinal Only* | `0x1AC7A0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | *Ordinal Only* | `0x1AC990` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `DeleteIE3Cache` | `0x1ACA40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | *Ordinal Only* | `0x1ACA50` | 224 | UnwindData |  |
| 346 | *Ordinal Only* | `0x1ACB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | *Ordinal Only* | `0x1ACB50` | 564 | UnwindData |  |
| 254 | `HttpWebSocketShutdown` | `0x1B1F80` | 310 | UnwindData |  |
