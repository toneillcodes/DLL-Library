# Binary Specification: syncutil.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\syncutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `acc51c0a476bf2a998ac93f1b5f774eb7d92be168d9fdfacb92c468d0472eaf1`
* **Total Exported Functions:** 283

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 167 | `LogSyncBiweeklySQM` | `0x54C0` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `SyncSqmUpdateStats` | `0x60F0` | 7,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `VerifyDataStoreLockOwner` | `0x60F0` | 7,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `DllCanUnloadNow` | `0x7D00` | 42 | UnwindData |  |
| 116 | `DllGetClassObject` | `0x7D30` | 3,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | *Ordinal Only* | `0x8900` | 619 | UnwindData |  |
| 746 | *Ordinal Only* | `0x8BD0` | 146 | UnwindData |  |
| 747 | *Ordinal Only* | `0x8C70` | 180 | UnwindData |  |
| 744 | *Ordinal Only* | `0x8D30` | 230 | UnwindData |  |
| 743 | *Ordinal Only* | `0x8FC0` | 330 | UnwindData |  |
| 742 | *Ordinal Only* | `0x9110` | 195 | UnwindData |  |
| 7 | `GetGalSearchResultsFolderAndPartnerGuidEx` | `0x91E0` | 419 | UnwindData |  |
| 748 | *Ordinal Only* | `0x9390` | 219 | UnwindData |  |
| 277 | *Ordinal Only* | `0xA7F0` | 93 | UnwindData |  |
| 281 | *Ordinal Only* | `0xA870` | 77 | UnwindData |  |
| 283 | *Ordinal Only* | `0xA8D0` | 77 | UnwindData |  |
| 285 | *Ordinal Only* | `0xA9F0` | 112 | UnwindData |  |
| 291 | *Ordinal Only* | `0xAB40` | 111 | UnwindData |  |
| 287 | *Ordinal Only* | `0xAFD0` | 94 | UnwindData |  |
| 275 | *Ordinal Only* | `0xB100` | 77 | UnwindData |  |
| 282 | *Ordinal Only* | `0xB270` | 77 | UnwindData |  |
| 286 | *Ordinal Only* | `0xB2D0` | 5,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | *Ordinal Only* | `0xC8D0` | 92 | UnwindData |  |
| 271 | *Ordinal Only* | `0xC940` | 114 | UnwindData |  |
| 510 | *Ordinal Only* | `0xC9C0` | 76 | UnwindData |  |
| 270 | *Ordinal Only* | `0xCA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | *Ordinal Only* | `0xCA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `DeleteHttpTransport` | `0xCA40` | 54 | UnwindData |  |
| 272 | *Ordinal Only* | `0xCA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | *Ordinal Only* | `0xCA90` | 54 | UnwindData |  |
| 147 | `GetMonitorDisplayState` | `0xCAD0` | 162 | UnwindData |  |
| 280 | *Ordinal Only* | `0xCB80` | 92 | UnwindData |  |
| 273 | *Ordinal Only* | `0xCBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `SetMonitorDisplayState` | `0xCC00` | 55 | UnwindData |  |
| 6 | `GetAuthority` | `0xD260` | 135 | UnwindData |  |
| 8 | `GetProviderUri` | `0xD550` | 280 | UnwindData |  |
| 62 | `OpenProviderKey` | `0xD770` | 210 | UnwindData |  |
| 11 | `GetWebAccountId` | `0x10460` | 303 | UnwindData |  |
| 12 | `GetWebAccountProvider` | `0x107F0` | 595 | UnwindData |  |
| 16 | `GetWebAccountProviderFromProviderId` | `0x10A50` | 351 | UnwindData |  |
| 43 | `InitializeServerReadyEvents` | `0x12B60` | 126 | UnwindData |  |
| 57 | `MarkServerReady` | `0x12C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `MarkServerShutdown` | `0x12C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `UninitializeServerReadyEvents` | `0x12C80` | 74 | UnwindData |  |
| 75 | `WaitForServerReady` | `0x12CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `WaitForSignalOrShutdown` | `0x12CF0` | 94 | UnwindData |  |
| 45 | `IsACOn` | `0x12D60` | 86 | UnwindData |  |
| 46 | `IsScreenOn` | `0x12DC0` | 47 | UnwindData |  |
| 138 | `GetBatterySaverWnfName` | `0x12E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `SetBatterySaverWnfName` | `0x12E10` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | *Ordinal Only* | `0x13080` | 369 | UnwindData |  |
| 472 | *Ordinal Only* | `0x13200` | 85 | UnwindData |  |
| 470 | *Ordinal Only* | `0x13260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 476 | *Ordinal Only* | `0x13280` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | *Ordinal Only* | `0x133E0` | 317 | UnwindData |  |
| 313 | *Ordinal Only* | `0x13530` | 58 | UnwindData |  |
| 156 | `HasNeverSyncedSuccessfully` | `0x13570` | 92 | UnwindData |  |
| 162 | `IsFirstSyncEver` | `0x135E0` | 83 | UnwindData |  |
| 475 | *Ordinal Only* | `0x13640` | 67 | UnwindData |  |
| 299 | *Ordinal Only* | `0x14600` | 938 | UnwindData |  |
| 362 | *Ordinal Only* | `0x150C0` | 530 | UnwindData |  |
| 117 | `DoesServerSupportAutoMoveSentItem` | `0x152E0` | 155 | UnwindData |  |
| 442 | *Ordinal Only* | `0x15390` | 759 | UnwindData |  |
| 739 | *Ordinal Only* | `0x15690` | 886 | UnwindData |  |
| 142 | `GetDefaultDeviceType` | `0x15A10` | 560 | UnwindData |  |
| 4 | *Ordinal Only* | `0x15C50` | 367 | UnwindData |  |
| 441 | *Ordinal Only* | `0x15DD0` | 97 | UnwindData |  |
| 440 | *Ordinal Only* | `0x15E40` | 104 | UnwindData |  |
| 1 | `GetSHA1HashOfString` | `0x15EB0` | 1,075 | UnwindData |  |
| 155 | `GetSyncWorkOnBehalfTicket` | `0x162F0` | 95 | UnwindData |  |
| 312 | *Ordinal Only* | `0x16360` | 59 | UnwindData |  |
| 301 | *Ordinal Only* | `0x163B0` | 115 | UnwindData |  |
| 308 | *Ordinal Only* | `0x16430` | 89 | UnwindData |  |
| 306 | *Ordinal Only* | `0x16490` | 49 | UnwindData |  |
| 363 | *Ordinal Only* | `0x164D0` | 100 | UnwindData |  |
| 307 | *Ordinal Only* | `0x16540` | 100 | UnwindData |  |
| 64 | *Ordinal Only* | `0x165B0` | 27 | UnwindData |  |
| 65 | *Ordinal Only* | `0x165E0` | 568 | UnwindData |  |
| 180 | `SetSyncWorkOnBehalfTicket` | `0x16820` | 179 | UnwindData |  |
| 66 | *Ordinal Only* | `0x168E0` | 27 | UnwindData |  |
| 67 | *Ordinal Only* | `0x16910` | 568 | UnwindData |  |
| 32 | *Ordinal Only* | `0x16B50` | 210 | UnwindData |  |
| 722 | *Ordinal Only* | `0x16D80` | 740 | UnwindData |  |
| 720 | *Ordinal Only* | `0x17070` | 372 | UnwindData |  |
| 721 | *Ordinal Only* | `0x171F0` | 414 | UnwindData |  |
| 70 | `UpdateYahooAccountType` | `0x173A0` | 2,704 | UnwindData |  |
| 77 | `AcquireDataStoreLock` | `0x18470` | 378 | UnwindData |  |
| 78 | `AcquireDataStoreLockEx` | `0x185F0` | 420 | UnwindData |  |
| 81 | `CloseDataStoreLock` | `0x187A0` | 111 | UnwindData |  |
| 91 | `CreateDataStoreLock` | `0x18820` | 350 | UnwindData |  |
| 174 | `ReleaseDataStoreLock` | `0x18990` | 50 | UnwindData |  |
| 79 | `AggregateAccountSyncStats` | `0x1A070` | 187 | UnwindData |  |
| 80 | `AggregateSessionSyncStats` | `0x1A140` | 113 | UnwindData |  |
| 127 | `GetAccountSyncStats` | `0x1A1C0` | 87 | UnwindData |  |
| 139 | `GetCurrentSyncStats` | `0x1A220` | 89 | UnwindData |  |
| 140 | `GetCurrentSyncStatsForMessage` | `0x1A280` | 101 | UnwindData |  |
| 141 | `GetCurrentSyncStatsForStore` | `0x1A2F0` | 136 | UnwindData |  |
| 153 | `GetSessionSyncStats` | `0x1A380` | 89 | UnwindData |  |
| 733 | *Ordinal Only* | `0x1C0B0` | 631 | UnwindData |  |
| 69 | *Ordinal Only* | `0x1C330` | 122 | UnwindData |  |
| 35 | *Ordinal Only* | `0x1C3B0` | 307 | UnwindData |  |
| 34 | *Ordinal Only* | `0x1C4F0` | 462 | UnwindData |  |
| 40 | *Ordinal Only* | `0x1C6D0` | 104 | UnwindData |  |
| 736 | *Ordinal Only* | `0x1C740` | 132 | UnwindData |  |
| 738 | *Ordinal Only* | `0x1C7D0` | 453 | UnwindData |  |
| 14 | *Ordinal Only* | `0x1C9A0` | 462 | UnwindData |  |
| 41 | *Ordinal Only* | `0x1CB80` | 231 | UnwindData |  |
| 737 | *Ordinal Only* | `0x1CC70` | 94 | UnwindData |  |
| 33 | *Ordinal Only* | `0x1CCE0` | 193 | UnwindData |  |
| 68 | *Ordinal Only* | `0x1CDB0` | 345 | UnwindData |  |
| 55 | *Ordinal Only* | `0x1D320` | 924 | UnwindData |  |
| 53 | *Ordinal Only* | `0x1D6D0` | 227 | UnwindData |  |
| 54 | *Ordinal Only* | `0x1D7C0` | 464 | UnwindData |  |
| 82 | `CoCreateInstanceElevated` | `0x1DBA0` | 313 | UnwindData |  |
| 290 | *Ordinal Only* | `0x1EB00` | 140 | UnwindData |  |
| 288 | *Ordinal Only* | `0x1FF60` | 170 | UnwindData |  |
| 90 | `CreateAuthHandler` | `0x20910` | 1,018 | UnwindData |  |
| 511 | *Ordinal Only* | `0x21CE0` | 160 | UnwindData |  |
| 92 | `CreateSyncBufferedStream` | `0x22760` | 122 | UnwindData |  |
| 170 | `OpenMimeBufferedStream` | `0x227E0` | 169 | UnwindData |  |
| 96 | `CredVaultDelete` | `0x230F0` | 355 | UnwindData |  |
| 97 | `CredVaultRead` | `0x23260` | 709 | UnwindData |  |
| 98 | `CredVaultWrite` | `0x23530` | 567 | UnwindData |  |
| 114 | `DeletePwd` | `0x23770` | 431 | UnwindData |  |
| 137 | `GetAuthCertTargetAndUser` | `0x23930` | 963 | UnwindData |  |
| 154 | `GetSyncTargetName` | `0x23D00` | 621 | UnwindData |  |
| 157 | `InitializeCredVault` | `0x23F80` | 99 | UnwindData |  |
| 164 | `IsPwdSaved` | `0x23FF0` | 307 | UnwindData |  |
| 103 | *Ordinal Only* | `0x24220` | 135 | UnwindData |  |
| 104 | *Ordinal Only* | `0x242B0` | 135 | UnwindData |  |
| 106 | *Ordinal Only* | `0x24340` | 123 | UnwindData |  |
| 107 | *Ordinal Only* | `0x243D0` | 123 | UnwindData |  |
| 105 | *Ordinal Only* | `0x24460` | 251 | UnwindData |  |
| 99 | `DeleteAuthCertHash` | `0x251C0` | 172 | UnwindData |  |
| 110 | `DeleteOAuthRefreshTokenForPartnership` | `0x25280` | 171 | UnwindData |  |
| 136 | `GetAuthCertHash` | `0x25340` | 211 | UnwindData |  |
| 171 | `ReadOAuthRefreshTokenForPartnership` | `0x25420` | 340 | UnwindData |  |
| 172 | `ReadPasswordForPartnership` | `0x25580` | 980 | UnwindData |  |
| 175 | `SetAuthCertHash` | `0x25960` | 221 | UnwindData |  |
| 184 | `WriteOAuthRefreshTokenForPartnership` | `0x25A50` | 156 | UnwindData |  |
| 185 | `WritePasswordForPartnership` | `0x25B00` | 487 | UnwindData |  |
| 101 | `DeleteDataSource` | `0x26050` | 457 | UnwindData |  |
| 111 | *Ordinal Only* | `0x26220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | *Ordinal Only* | `0x26230` | 1,078 | UnwindData |  |
| 47 | *Ordinal Only* | `0x26670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | *Ordinal Only* | `0x26690` | 139 | UnwindData |  |
| 48 | *Ordinal Only* | `0x26730` | 144 | UnwindData |  |
| 49 | *Ordinal Only* | `0x267D0` | 22 | UnwindData |  |
| 50 | *Ordinal Only* | `0x267F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | *Ordinal Only* | `0x26810` | 22 | UnwindData |  |
| 52 | *Ordinal Only* | `0x26830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | *Ordinal Only* | `0x26850` | 146 | UnwindData |  |
| 44 | *Ordinal Only* | `0x268F0` | 579 | UnwindData |  |
| 144 | `GetDefaultStoreDirty` | `0x26B40` | 86 | UnwindData |  |
| 146 | `GetGoldenPartnershipId` | `0x26BA0` | 81 | UnwindData |  |
| 109 | *Ordinal Only* | `0x26C00` | 112 | UnwindData |  |
| 242 | *Ordinal Only* | `0x26C80` | 139 | UnwindData |  |
| 87 | *Ordinal Only* | `0x26D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | *Ordinal Only* | `0x26D40` | 147 | UnwindData |  |
| 168 | `MarkUserDataAccountAsHidden` | `0x26DE0` | 530 | UnwindData |  |
| 734 | *Ordinal Only* | `0x27000` | 360 | UnwindData |  |
| 42 | *Ordinal Only* | `0x27170` | 71 | UnwindData |  |
| 36 | *Ordinal Only* | `0x271C0` | 770 | UnwindData |  |
| 255 | *Ordinal Only* | `0x274D0` | 203 | UnwindData |  |
| 177 | `SetDefaultStoreDirty` | `0x275B0` | 80 | UnwindData |  |
| 37 | *Ordinal Only* | `0x27610` | 216 | UnwindData |  |
| 113 | *Ordinal Only* | `0x276F0` | 136 | UnwindData |  |
| 735 | *Ordinal Only* | `0x27780` | 81 | UnwindData |  |
| 61 | *Ordinal Only* | `0x27A30` | 408 | UnwindData |  |
| 60 | *Ordinal Only* | `0x27EC0` | 2,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | *Ordinal Only* | `0x28830` | 75 | UnwindData |  |
| 503 | *Ordinal Only* | `0x28890` | 556 | UnwindData |  |
| 505 | *Ordinal Only* | `0x28AD0` | 294 | UnwindData |  |
| 504 | *Ordinal Only* | `0x28C00` | 506 | UnwindData |  |
| 506 | *Ordinal Only* | `0x28E00` | 622 | UnwindData |  |
| 500 | *Ordinal Only* | `0x29080` | 195 | UnwindData |  |
| 501 | *Ordinal Only* | `0x29150` | 521 | UnwindData |  |
| 464 | *Ordinal Only* | `0x29880` | 53 | UnwindData |  |
| 413 | *Ordinal Only* | `0x298C0` | 167 | UnwindData |  |
| 463 | *Ordinal Only* | `0x29970` | 68 | UnwindData |  |
| 412 | *Ordinal Only* | `0x299C0` | 87 | UnwindData |  |
| 461 | *Ordinal Only* | `0x29A20` | 67 | UnwindData |  |
| 462 | *Ordinal Only* | `0x29A70` | 140 | UnwindData |  |
| 126 | `GetAADToken` | `0x2AD80` | 116 | UnwindData |  |
| 165 | `IsValidAADAuthUri` | `0x2AE00` | 146 | UnwindData |  |
| 173 | `RegisterSsoAccountsCallback` | `0x2AEA0` | 117 | UnwindData |  |
| 182 | `TryGetDefaultSignInAccountInfo` | `0x2AF20` | 362 | UnwindData |  |
| 129 | `GetAccountUsernameFromToken` | `0x2CC90` | 90 | UnwindData |  |
| 150 | `GetOAuthHelperForAccount` | `0x2CCF0` | 214 | UnwindData |  |
| 151 | `GetOAuthHelperForProvider` | `0x2CDD0` | 1,474 | UnwindData |  |
| 169 | `OAuthHelper_CreateInstance` | `0x2D3A0` | 155 | UnwindData |  |
| 143 | `GetDefaultMsaWebAccountId` | `0x2D8F0` | 108 | UnwindData |  |
| 148 | `GetMsaCustomerId` | `0x2D970` | 942 | UnwindData |  |
| 158 | `InitializeMeContact` | `0x2DD30` | 346 | UnwindData |  |
| 159 | `InitializeMsaStore` | `0x2DE90` | 544 | UnwindData |  |
| 292 | *Ordinal Only* | `0x2E280` | 915 | UnwindData |  |
| 296 | *Ordinal Only* | `0x2E820` | 65 | UnwindData |  |
| 269 | *Ordinal Only* | `0x2ED10` | 475 | UnwindData |  |
| 268 | *Ordinal Only* | `0x2EF00` | 241 | UnwindData |  |
| 149 | `GetOAuthAccessTokenForPartnership` | `0x2F910` | 562 | UnwindData |  |
| 161 | `InvalidateOAuthAccessTokenForPartnership` | `0x2FB50` | 332 | UnwindData |  |
| 152 | `GetOutgoingMessageSizeLimit` | `0x2FD00` | 349 | UnwindData |  |
| 179 | `SetOutgoingMessageSizeLimit` | `0x2FE70` | 368 | UnwindData |  |
| 71 | *Ordinal Only* | `0x30320` | 469 | UnwindData |  |
| 73 | *Ordinal Only* | `0x30500` | 315 | UnwindData |  |
| 72 | *Ordinal Only* | `0x30650` | 146 | UnwindData |  |
| 118 | *Ordinal Only* | `0x306F0` | 218 | UnwindData |  |
| 74 | *Ordinal Only* | `0x307D0` | 744 | UnwindData |  |
| 119 | *Ordinal Only* | `0x30AC0` | 222 | UnwindData |  |
| 83 | *Ordinal Only* | `0x31030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | *Ordinal Only* | `0x31050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | *Ordinal Only* | `0x31070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | *Ordinal Only* | `0x31090` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | *Ordinal Only* | `0x310E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | *Ordinal Only* | `0x31130` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `LoadHeartbeatValues` | `0x31780` | 1,364 | UnwindData |  |
| 10 | *Ordinal Only* | `0x32450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | *Ordinal Only* | `0x32460` | 162 | UnwindData |  |
| 5 | `DeviceNeedsProvisioning` | `0x42910` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `FindErrorCode` | `0x42940` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | *Ordinal Only* | `0x42970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | *Ordinal Only* | `0x42990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | *Ordinal Only* | `0x429B0` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | *Ordinal Only* | `0x438B0` | 315 | UnwindData |  |
| 703 | *Ordinal Only* | `0x43A00` | 97 | UnwindData |  |
| 163 | `IsMatchingClientCertificateEx` | `0x43A70` | 331 | UnwindData |  |
| 705 | *Ordinal Only* | `0x43BD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 701 | *Ordinal Only* | `0x43C30` | 422 | UnwindData |  |
| 704 | *Ordinal Only* | `0x43DE0` | 233 | UnwindData |  |
| 17 | *Ordinal Only* | `0x444A0` | 72 | UnwindData |  |
| 20 | *Ordinal Only* | `0x444F0` | 153 | UnwindData |  |
| 15 | *Ordinal Only* | `0x44590` | 172 | UnwindData |  |
| 100 | *Ordinal Only* | `0x44870` | 210 | UnwindData |  |
| 18 | *Ordinal Only* | `0x44950` | 49 | UnwindData |  |
| 19 | *Ordinal Only* | `0x44990` | 53 | UnwindData |  |
| 93 | *Ordinal Only* | `0x449D0` | 147 | UnwindData |  |
| 28 | *Ordinal Only* | `0x44A70` | 284 | UnwindData |  |
| 95 | *Ordinal Only* | `0x44BA0` | 261 | UnwindData |  |
| 94 | *Ordinal Only* | `0x44CB0` | 139 | UnwindData |  |
| 256 | *Ordinal Only* | `0x44DF0` | 135 | UnwindData |  |
| 21 | *Ordinal Only* | `0x44E80` | 241 | UnwindData |  |
| 2 | *Ordinal Only* | `0x44F80` | 182 | UnwindData |  |
| 108 | *Ordinal Only* | `0x45040` | 169 | UnwindData |  |
| 26 | *Ordinal Only* | `0x450F0` | 152 | UnwindData |  |
| 23 | *Ordinal Only* | `0x45190` | 62 | UnwindData |  |
| 24 | *Ordinal Only* | `0x451E0` | 202 | UnwindData |  |
| 38 | *Ordinal Only* | `0x452B0` | 148 | UnwindData |  |
| 30 | *Ordinal Only* | `0x45350` | 165 | UnwindData |  |
| 22 | *Ordinal Only* | `0x45400` | 144 | UnwindData |  |
| 257 | *Ordinal Only* | `0x454A0` | 164 | UnwindData |  |
| 59 | *Ordinal Only* | `0x45550` | 194 | UnwindData |  |
| 29 | *Ordinal Only* | `0x45620` | 63 | UnwindData |  |
| 3 | *Ordinal Only* | `0x45670` | 163 | UnwindData |  |
| 27 | *Ordinal Only* | `0x45720` | 144 | UnwindData |  |
| 25 | *Ordinal Only* | `0x457C0` | 163 | UnwindData |  |
| 39 | *Ordinal Only* | `0x45870` | 172 | UnwindData |  |
| 31 | *Ordinal Only* | `0x45930` | 144 | UnwindData |  |
| 305 | *Ordinal Only* | `0x45BF0` | 262 | UnwindData |  |
| 243 | *Ordinal Only* | `0x45D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | *Ordinal Only* | `0x45D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | *Ordinal Only* | `0x45D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | *Ordinal Only* | `0x45D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | *Ordinal Only* | `0x45D80` | 67 | UnwindData |  |
| 249 | *Ordinal Only* | `0x45DD0` | 67 | UnwindData |  |
| 251 | *Ordinal Only* | `0x45E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | *Ordinal Only* | `0x45E40` | 121 | UnwindData |  |
| 253 | *Ordinal Only* | `0x45EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | *Ordinal Only* | `0x45EE0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `GetDomainFromEmail` | `0x46240` | 1,197 | UnwindData |  |
| 160 | `InitializeSyncStatus` | `0x46700` | 14,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | *Ordinal Only* | `0x49E80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | *Ordinal Only* | `0x49EC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | *Ordinal Only* | `0x49F00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | *Ordinal Only* | `0x49F40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | *Ordinal Only* | `0x49F80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | *Ordinal Only* | `0x49FC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | *Ordinal Only* | `0x4A000` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | *Ordinal Only* | `0x4A040` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | *Ordinal Only* | `0x4A080` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | *Ordinal Only* | `0x4A0C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | *Ordinal Only* | `0x4A100` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | *Ordinal Only* | `0x4A140` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | *Ordinal Only* | `0x4A180` | 0 | Indeterminate |  |
