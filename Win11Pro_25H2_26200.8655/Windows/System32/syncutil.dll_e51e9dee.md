# Binary Specification: syncutil.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\syncutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e51e9dee41ce92f4490505ec0f116da5f7237dc5b1f1d8f286c7165206d382c9`
* **Total Exported Functions:** 283

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 167 | `LogSyncBiweeklySQM` | `0x54C0` | 3,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `SyncSqmUpdateStats` | `0x6110` | 7,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `VerifyDataStoreLockOwner` | `0x6110` | 7,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `DllCanUnloadNow` | `0x7D20` | 42 | UnwindData |  |
| 116 | `DllGetClassObject` | `0x7D50` | 3,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | *Ordinal Only* | `0x8920` | 619 | UnwindData |  |
| 746 | *Ordinal Only* | `0x8BF0` | 146 | UnwindData |  |
| 747 | *Ordinal Only* | `0x8C90` | 180 | UnwindData |  |
| 744 | *Ordinal Only* | `0x8D50` | 230 | UnwindData |  |
| 743 | *Ordinal Only* | `0x8FE0` | 330 | UnwindData |  |
| 742 | *Ordinal Only* | `0x9130` | 195 | UnwindData |  |
| 7 | `GetGalSearchResultsFolderAndPartnerGuidEx` | `0x9200` | 419 | UnwindData |  |
| 748 | *Ordinal Only* | `0x93B0` | 219 | UnwindData |  |
| 277 | *Ordinal Only* | `0xA810` | 93 | UnwindData |  |
| 281 | *Ordinal Only* | `0xA890` | 77 | UnwindData |  |
| 283 | *Ordinal Only* | `0xA8F0` | 77 | UnwindData |  |
| 285 | *Ordinal Only* | `0xAA10` | 112 | UnwindData |  |
| 291 | *Ordinal Only* | `0xAB60` | 111 | UnwindData |  |
| 287 | *Ordinal Only* | `0xAFF0` | 94 | UnwindData |  |
| 275 | *Ordinal Only* | `0xB120` | 77 | UnwindData |  |
| 282 | *Ordinal Only* | `0xB290` | 77 | UnwindData |  |
| 286 | *Ordinal Only* | `0xB2F0` | 5,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | *Ordinal Only* | `0xC8F0` | 92 | UnwindData |  |
| 271 | *Ordinal Only* | `0xC960` | 114 | UnwindData |  |
| 510 | *Ordinal Only* | `0xC9E0` | 76 | UnwindData |  |
| 270 | *Ordinal Only* | `0xCA40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | *Ordinal Only* | `0xCA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `DeleteHttpTransport` | `0xCA60` | 54 | UnwindData |  |
| 272 | *Ordinal Only* | `0xCAA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | *Ordinal Only* | `0xCAB0` | 54 | UnwindData |  |
| 147 | `GetMonitorDisplayState` | `0xCAF0` | 162 | UnwindData |  |
| 280 | *Ordinal Only* | `0xCBA0` | 92 | UnwindData |  |
| 273 | *Ordinal Only* | `0xCC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `SetMonitorDisplayState` | `0xCC20` | 55 | UnwindData |  |
| 6 | `GetAuthority` | `0xD280` | 135 | UnwindData |  |
| 8 | `GetProviderUri` | `0xD570` | 280 | UnwindData |  |
| 62 | `OpenProviderKey` | `0xD790` | 210 | UnwindData |  |
| 11 | `GetWebAccountId` | `0x10480` | 303 | UnwindData |  |
| 12 | `GetWebAccountProvider` | `0x10810` | 595 | UnwindData |  |
| 16 | `GetWebAccountProviderFromProviderId` | `0x10A70` | 351 | UnwindData |  |
| 43 | `InitializeServerReadyEvents` | `0x12B80` | 126 | UnwindData |  |
| 57 | `MarkServerReady` | `0x12C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `MarkServerShutdown` | `0x12C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `UninitializeServerReadyEvents` | `0x12CA0` | 74 | UnwindData |  |
| 75 | `WaitForServerReady` | `0x12CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `WaitForSignalOrShutdown` | `0x12D10` | 94 | UnwindData |  |
| 45 | `IsACOn` | `0x12D80` | 86 | UnwindData |  |
| 46 | `IsScreenOn` | `0x12DE0` | 47 | UnwindData |  |
| 138 | `GetBatterySaverWnfName` | `0x12E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `SetBatterySaverWnfName` | `0x12E30` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | *Ordinal Only* | `0x130A0` | 369 | UnwindData |  |
| 472 | *Ordinal Only* | `0x13220` | 85 | UnwindData |  |
| 470 | *Ordinal Only* | `0x13280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 476 | *Ordinal Only* | `0x132A0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | *Ordinal Only* | `0x13400` | 317 | UnwindData |  |
| 313 | *Ordinal Only* | `0x13550` | 58 | UnwindData |  |
| 156 | `HasNeverSyncedSuccessfully` | `0x13590` | 92 | UnwindData |  |
| 162 | `IsFirstSyncEver` | `0x13600` | 83 | UnwindData |  |
| 475 | *Ordinal Only* | `0x13660` | 67 | UnwindData |  |
| 299 | *Ordinal Only* | `0x14620` | 938 | UnwindData |  |
| 362 | *Ordinal Only* | `0x150E0` | 530 | UnwindData |  |
| 117 | `DoesServerSupportAutoMoveSentItem` | `0x15300` | 155 | UnwindData |  |
| 442 | *Ordinal Only* | `0x153B0` | 759 | UnwindData |  |
| 739 | *Ordinal Only* | `0x156B0` | 886 | UnwindData |  |
| 142 | `GetDefaultDeviceType` | `0x15A30` | 560 | UnwindData |  |
| 4 | *Ordinal Only* | `0x15C70` | 367 | UnwindData |  |
| 441 | *Ordinal Only* | `0x15DF0` | 97 | UnwindData |  |
| 440 | *Ordinal Only* | `0x15E60` | 104 | UnwindData |  |
| 1 | `GetSHA1HashOfString` | `0x15ED0` | 1,075 | UnwindData |  |
| 155 | `GetSyncWorkOnBehalfTicket` | `0x16310` | 95 | UnwindData |  |
| 312 | *Ordinal Only* | `0x16380` | 59 | UnwindData |  |
| 301 | *Ordinal Only* | `0x163D0` | 115 | UnwindData |  |
| 308 | *Ordinal Only* | `0x16450` | 89 | UnwindData |  |
| 306 | *Ordinal Only* | `0x164B0` | 49 | UnwindData |  |
| 363 | *Ordinal Only* | `0x164F0` | 100 | UnwindData |  |
| 307 | *Ordinal Only* | `0x16560` | 100 | UnwindData |  |
| 64 | *Ordinal Only* | `0x165D0` | 27 | UnwindData |  |
| 65 | *Ordinal Only* | `0x16600` | 568 | UnwindData |  |
| 180 | `SetSyncWorkOnBehalfTicket` | `0x16840` | 179 | UnwindData |  |
| 66 | *Ordinal Only* | `0x16900` | 27 | UnwindData |  |
| 67 | *Ordinal Only* | `0x16930` | 568 | UnwindData |  |
| 32 | *Ordinal Only* | `0x16B70` | 210 | UnwindData |  |
| 722 | *Ordinal Only* | `0x16DA0` | 740 | UnwindData |  |
| 720 | *Ordinal Only* | `0x17090` | 372 | UnwindData |  |
| 721 | *Ordinal Only* | `0x17210` | 414 | UnwindData |  |
| 70 | `UpdateYahooAccountType` | `0x173C0` | 2,704 | UnwindData |  |
| 77 | `AcquireDataStoreLock` | `0x18490` | 378 | UnwindData |  |
| 78 | `AcquireDataStoreLockEx` | `0x18610` | 420 | UnwindData |  |
| 81 | `CloseDataStoreLock` | `0x187C0` | 111 | UnwindData |  |
| 91 | `CreateDataStoreLock` | `0x18840` | 350 | UnwindData |  |
| 174 | `ReleaseDataStoreLock` | `0x189B0` | 50 | UnwindData |  |
| 79 | `AggregateAccountSyncStats` | `0x1A090` | 187 | UnwindData |  |
| 80 | `AggregateSessionSyncStats` | `0x1A160` | 113 | UnwindData |  |
| 127 | `GetAccountSyncStats` | `0x1A1E0` | 87 | UnwindData |  |
| 139 | `GetCurrentSyncStats` | `0x1A240` | 89 | UnwindData |  |
| 140 | `GetCurrentSyncStatsForMessage` | `0x1A2A0` | 101 | UnwindData |  |
| 141 | `GetCurrentSyncStatsForStore` | `0x1A310` | 136 | UnwindData |  |
| 153 | `GetSessionSyncStats` | `0x1A3A0` | 89 | UnwindData |  |
| 733 | *Ordinal Only* | `0x1C0D0` | 631 | UnwindData |  |
| 69 | *Ordinal Only* | `0x1C350` | 122 | UnwindData |  |
| 35 | *Ordinal Only* | `0x1C3D0` | 307 | UnwindData |  |
| 34 | *Ordinal Only* | `0x1C510` | 462 | UnwindData |  |
| 40 | *Ordinal Only* | `0x1C6F0` | 104 | UnwindData |  |
| 736 | *Ordinal Only* | `0x1C760` | 132 | UnwindData |  |
| 738 | *Ordinal Only* | `0x1C7F0` | 453 | UnwindData |  |
| 14 | *Ordinal Only* | `0x1C9C0` | 462 | UnwindData |  |
| 41 | *Ordinal Only* | `0x1CBA0` | 231 | UnwindData |  |
| 737 | *Ordinal Only* | `0x1CC90` | 94 | UnwindData |  |
| 33 | *Ordinal Only* | `0x1CD00` | 193 | UnwindData |  |
| 68 | *Ordinal Only* | `0x1CDD0` | 345 | UnwindData |  |
| 55 | *Ordinal Only* | `0x1D340` | 924 | UnwindData |  |
| 53 | *Ordinal Only* | `0x1D6F0` | 227 | UnwindData |  |
| 54 | *Ordinal Only* | `0x1D7E0` | 464 | UnwindData |  |
| 82 | `CoCreateInstanceElevated` | `0x1DBC0` | 313 | UnwindData |  |
| 290 | *Ordinal Only* | `0x1EB20` | 140 | UnwindData |  |
| 288 | *Ordinal Only* | `0x1FF80` | 170 | UnwindData |  |
| 90 | `CreateAuthHandler` | `0x20930` | 1,018 | UnwindData |  |
| 511 | *Ordinal Only* | `0x21D00` | 160 | UnwindData |  |
| 92 | `CreateSyncBufferedStream` | `0x22780` | 122 | UnwindData |  |
| 170 | `OpenMimeBufferedStream` | `0x22800` | 169 | UnwindData |  |
| 96 | `CredVaultDelete` | `0x23110` | 355 | UnwindData |  |
| 97 | `CredVaultRead` | `0x23280` | 709 | UnwindData |  |
| 98 | `CredVaultWrite` | `0x23550` | 567 | UnwindData |  |
| 114 | `DeletePwd` | `0x23790` | 431 | UnwindData |  |
| 137 | `GetAuthCertTargetAndUser` | `0x23950` | 963 | UnwindData |  |
| 154 | `GetSyncTargetName` | `0x23D20` | 621 | UnwindData |  |
| 157 | `InitializeCredVault` | `0x23FA0` | 99 | UnwindData |  |
| 164 | `IsPwdSaved` | `0x24010` | 307 | UnwindData |  |
| 103 | *Ordinal Only* | `0x24240` | 135 | UnwindData |  |
| 104 | *Ordinal Only* | `0x242D0` | 135 | UnwindData |  |
| 106 | *Ordinal Only* | `0x24360` | 123 | UnwindData |  |
| 107 | *Ordinal Only* | `0x243F0` | 123 | UnwindData |  |
| 105 | *Ordinal Only* | `0x24480` | 251 | UnwindData |  |
| 99 | `DeleteAuthCertHash` | `0x251E0` | 172 | UnwindData |  |
| 110 | `DeleteOAuthRefreshTokenForPartnership` | `0x252A0` | 171 | UnwindData |  |
| 136 | `GetAuthCertHash` | `0x25360` | 211 | UnwindData |  |
| 171 | `ReadOAuthRefreshTokenForPartnership` | `0x25440` | 340 | UnwindData |  |
| 172 | `ReadPasswordForPartnership` | `0x255A0` | 980 | UnwindData |  |
| 175 | `SetAuthCertHash` | `0x25980` | 221 | UnwindData |  |
| 184 | `WriteOAuthRefreshTokenForPartnership` | `0x25A70` | 156 | UnwindData |  |
| 185 | `WritePasswordForPartnership` | `0x25B20` | 487 | UnwindData |  |
| 101 | `DeleteDataSource` | `0x26070` | 457 | UnwindData |  |
| 111 | *Ordinal Only* | `0x26240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | *Ordinal Only* | `0x26250` | 1,078 | UnwindData |  |
| 47 | *Ordinal Only* | `0x26690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | *Ordinal Only* | `0x266B0` | 139 | UnwindData |  |
| 48 | *Ordinal Only* | `0x26750` | 144 | UnwindData |  |
| 49 | *Ordinal Only* | `0x267F0` | 22 | UnwindData |  |
| 50 | *Ordinal Only* | `0x26810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | *Ordinal Only* | `0x26830` | 22 | UnwindData |  |
| 52 | *Ordinal Only* | `0x26850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | *Ordinal Only* | `0x26870` | 146 | UnwindData |  |
| 44 | *Ordinal Only* | `0x26910` | 579 | UnwindData |  |
| 144 | `GetDefaultStoreDirty` | `0x26B60` | 86 | UnwindData |  |
| 146 | `GetGoldenPartnershipId` | `0x26BC0` | 81 | UnwindData |  |
| 109 | *Ordinal Only* | `0x26C20` | 112 | UnwindData |  |
| 242 | *Ordinal Only* | `0x26CA0` | 139 | UnwindData |  |
| 87 | *Ordinal Only* | `0x26D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | *Ordinal Only* | `0x26D60` | 147 | UnwindData |  |
| 168 | `MarkUserDataAccountAsHidden` | `0x26E00` | 530 | UnwindData |  |
| 734 | *Ordinal Only* | `0x27020` | 360 | UnwindData |  |
| 42 | *Ordinal Only* | `0x27190` | 71 | UnwindData |  |
| 36 | *Ordinal Only* | `0x271E0` | 770 | UnwindData |  |
| 255 | *Ordinal Only* | `0x274F0` | 203 | UnwindData |  |
| 177 | `SetDefaultStoreDirty` | `0x275D0` | 80 | UnwindData |  |
| 37 | *Ordinal Only* | `0x27630` | 216 | UnwindData |  |
| 113 | *Ordinal Only* | `0x27710` | 136 | UnwindData |  |
| 735 | *Ordinal Only* | `0x277A0` | 81 | UnwindData |  |
| 61 | *Ordinal Only* | `0x27A50` | 408 | UnwindData |  |
| 60 | *Ordinal Only* | `0x27EE0` | 2,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | *Ordinal Only* | `0x28850` | 75 | UnwindData |  |
| 503 | *Ordinal Only* | `0x288B0` | 556 | UnwindData |  |
| 505 | *Ordinal Only* | `0x28AF0` | 294 | UnwindData |  |
| 504 | *Ordinal Only* | `0x28C20` | 506 | UnwindData |  |
| 506 | *Ordinal Only* | `0x28E20` | 622 | UnwindData |  |
| 500 | *Ordinal Only* | `0x290A0` | 195 | UnwindData |  |
| 501 | *Ordinal Only* | `0x29170` | 521 | UnwindData |  |
| 464 | *Ordinal Only* | `0x298A0` | 53 | UnwindData |  |
| 413 | *Ordinal Only* | `0x298E0` | 167 | UnwindData |  |
| 463 | *Ordinal Only* | `0x29990` | 68 | UnwindData |  |
| 412 | *Ordinal Only* | `0x299E0` | 87 | UnwindData |  |
| 461 | *Ordinal Only* | `0x29A40` | 67 | UnwindData |  |
| 462 | *Ordinal Only* | `0x29A90` | 140 | UnwindData |  |
| 126 | `GetAADToken` | `0x2ADA0` | 116 | UnwindData |  |
| 165 | `IsValidAADAuthUri` | `0x2AE20` | 146 | UnwindData |  |
| 173 | `RegisterSsoAccountsCallback` | `0x2AEC0` | 117 | UnwindData |  |
| 182 | `TryGetDefaultSignInAccountInfo` | `0x2AF40` | 362 | UnwindData |  |
| 129 | `GetAccountUsernameFromToken` | `0x2CCB0` | 90 | UnwindData |  |
| 150 | `GetOAuthHelperForAccount` | `0x2CD10` | 214 | UnwindData |  |
| 151 | `GetOAuthHelperForProvider` | `0x2CDF0` | 1,474 | UnwindData |  |
| 169 | `OAuthHelper_CreateInstance` | `0x2D3C0` | 155 | UnwindData |  |
| 143 | `GetDefaultMsaWebAccountId` | `0x2D910` | 108 | UnwindData |  |
| 148 | `GetMsaCustomerId` | `0x2D990` | 942 | UnwindData |  |
| 158 | `InitializeMeContact` | `0x2DD50` | 346 | UnwindData |  |
| 159 | `InitializeMsaStore` | `0x2DEB0` | 544 | UnwindData |  |
| 292 | *Ordinal Only* | `0x2E2A0` | 915 | UnwindData |  |
| 296 | *Ordinal Only* | `0x2E840` | 65 | UnwindData |  |
| 269 | *Ordinal Only* | `0x2ED30` | 475 | UnwindData |  |
| 268 | *Ordinal Only* | `0x2EF20` | 241 | UnwindData |  |
| 149 | `GetOAuthAccessTokenForPartnership` | `0x2F930` | 562 | UnwindData |  |
| 161 | `InvalidateOAuthAccessTokenForPartnership` | `0x2FB70` | 332 | UnwindData |  |
| 152 | `GetOutgoingMessageSizeLimit` | `0x2FD20` | 349 | UnwindData |  |
| 179 | `SetOutgoingMessageSizeLimit` | `0x2FE90` | 368 | UnwindData |  |
| 71 | *Ordinal Only* | `0x30340` | 469 | UnwindData |  |
| 73 | *Ordinal Only* | `0x30520` | 315 | UnwindData |  |
| 72 | *Ordinal Only* | `0x30670` | 146 | UnwindData |  |
| 118 | *Ordinal Only* | `0x30710` | 218 | UnwindData |  |
| 74 | *Ordinal Only* | `0x307F0` | 744 | UnwindData |  |
| 119 | *Ordinal Only* | `0x30AE0` | 222 | UnwindData |  |
| 83 | *Ordinal Only* | `0x31050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | *Ordinal Only* | `0x31070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | *Ordinal Only* | `0x31090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | *Ordinal Only* | `0x310B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | *Ordinal Only* | `0x31100` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | *Ordinal Only* | `0x31150` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `LoadHeartbeatValues` | `0x317A0` | 1,364 | UnwindData |  |
| 10 | *Ordinal Only* | `0x32470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | *Ordinal Only* | `0x32480` | 162 | UnwindData |  |
| 5 | `DeviceNeedsProvisioning` | `0x42930` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `FindErrorCode` | `0x42960` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | *Ordinal Only* | `0x42990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | *Ordinal Only* | `0x429B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | *Ordinal Only* | `0x429D0` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | *Ordinal Only* | `0x438D0` | 315 | UnwindData |  |
| 703 | *Ordinal Only* | `0x43A20` | 97 | UnwindData |  |
| 163 | `IsMatchingClientCertificateEx` | `0x43A90` | 331 | UnwindData |  |
| 705 | *Ordinal Only* | `0x43BF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 701 | *Ordinal Only* | `0x43C50` | 422 | UnwindData |  |
| 704 | *Ordinal Only* | `0x43E00` | 233 | UnwindData |  |
| 17 | *Ordinal Only* | `0x444C0` | 72 | UnwindData |  |
| 20 | *Ordinal Only* | `0x44510` | 153 | UnwindData |  |
| 15 | *Ordinal Only* | `0x445B0` | 172 | UnwindData |  |
| 100 | *Ordinal Only* | `0x44890` | 210 | UnwindData |  |
| 18 | *Ordinal Only* | `0x44970` | 49 | UnwindData |  |
| 19 | *Ordinal Only* | `0x449B0` | 53 | UnwindData |  |
| 93 | *Ordinal Only* | `0x449F0` | 147 | UnwindData |  |
| 28 | *Ordinal Only* | `0x44A90` | 284 | UnwindData |  |
| 95 | *Ordinal Only* | `0x44BC0` | 261 | UnwindData |  |
| 94 | *Ordinal Only* | `0x44CD0` | 139 | UnwindData |  |
| 256 | *Ordinal Only* | `0x44E10` | 135 | UnwindData |  |
| 21 | *Ordinal Only* | `0x44EA0` | 241 | UnwindData |  |
| 2 | *Ordinal Only* | `0x44FA0` | 182 | UnwindData |  |
| 108 | *Ordinal Only* | `0x45060` | 169 | UnwindData |  |
| 26 | *Ordinal Only* | `0x45110` | 152 | UnwindData |  |
| 23 | *Ordinal Only* | `0x451B0` | 62 | UnwindData |  |
| 24 | *Ordinal Only* | `0x45200` | 202 | UnwindData |  |
| 38 | *Ordinal Only* | `0x452D0` | 148 | UnwindData |  |
| 30 | *Ordinal Only* | `0x45370` | 165 | UnwindData |  |
| 22 | *Ordinal Only* | `0x45420` | 144 | UnwindData |  |
| 257 | *Ordinal Only* | `0x454C0` | 164 | UnwindData |  |
| 59 | *Ordinal Only* | `0x45570` | 194 | UnwindData |  |
| 29 | *Ordinal Only* | `0x45640` | 63 | UnwindData |  |
| 3 | *Ordinal Only* | `0x45690` | 163 | UnwindData |  |
| 27 | *Ordinal Only* | `0x45740` | 144 | UnwindData |  |
| 25 | *Ordinal Only* | `0x457E0` | 163 | UnwindData |  |
| 39 | *Ordinal Only* | `0x45890` | 172 | UnwindData |  |
| 31 | *Ordinal Only* | `0x45950` | 144 | UnwindData |  |
| 305 | *Ordinal Only* | `0x45C10` | 262 | UnwindData |  |
| 243 | *Ordinal Only* | `0x45D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | *Ordinal Only* | `0x45D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | *Ordinal Only* | `0x45D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | *Ordinal Only* | `0x45D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | *Ordinal Only* | `0x45DA0` | 67 | UnwindData |  |
| 249 | *Ordinal Only* | `0x45DF0` | 67 | UnwindData |  |
| 251 | *Ordinal Only* | `0x45E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | *Ordinal Only* | `0x45E60` | 121 | UnwindData |  |
| 253 | *Ordinal Only* | `0x45EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | *Ordinal Only* | `0x45F00` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `GetDomainFromEmail` | `0x46260` | 1,197 | UnwindData |  |
| 160 | `InitializeSyncStatus` | `0x46720` | 14,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
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
