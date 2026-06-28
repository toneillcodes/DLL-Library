# Binary Specification: winhttp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\winhttp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a57e76dc79b93b0f5ae81dd0c2827081ac8b1978ed991532b73b8d7661b32387`
* **Total Exported Functions:** 91

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 63 | `WinHttpReadData` | `0x1900` | 243 | UnwindData |  |
| 64 | `WinHttpReadDataEx` | `0x1A00` | 31 | UnwindData |  |
| 67 | `WinHttpReceiveResponse` | `0x6C20` | 33 | UnwindData |  |
| 80 | `WinHttpSetTimeouts` | `0x8820` | 907 | UnwindData |  |
| 5 | `WinHttpAddRequestHeaders` | `0xFC60` | 737 | UnwindData |  |
| 60 | `WinHttpQueryHeaders` | `0x10750` | 1,590 | UnwindData |  |
| 73 | `WinHttpSendRequest` | `0x12C80` | 1,206 | UnwindData |  |
| 50 | `WinHttpOpen` | `0x15AC0` | 951 | UnwindData |  |
| 9 | `WinHttpCloseHandle` | `0x190A0` | 2,745 | UnwindData |  |
| 39 | `WinHttpGetIEProxyConfigForCurrentUser` | `0x1C100` | 844 | UnwindData |  |
| 35 | `WinHttpFreeProxySettings` | `0x1E530` | 112 | UnwindData |  |
| 65 | `WinHttpReadProxySettings` | `0x25430` | 1,344 | UnwindData |  |
| 28 | `WinHttpCreateProxyResolver` | `0x25C00` | 921 | UnwindData |  |
| 81 | `WinHttpTimeFromSystemTime` | `0x2A8D0` | 532 | UnwindData |  |
| 88 | `WinHttpWebSocketSend` | `0x2B310` | 200 | UnwindData |  |
| 25 | `WinHttpCrackUrl` | `0x378A0` | 37 | UnwindData |  |
| 10 | `WinHttpConnect` | `0x38880` | 1,001 | UnwindData |  |
| 59 | `WinHttpQueryDataAvailable` | `0x38EB0` | 3,406 | UnwindData |  |
| 90 | `WinHttpWriteData` | `0x39C10` | 3,454 | UnwindData |  |
| 76 | `WinHttpSetOption` | `0x41ED0` | 786 | UnwindData |  |
| 79 | `WinHttpSetStatusCallback` | `0x421F0` | 70 | UnwindData |  |
| 62 | `WinHttpQueryOption` | `0x436B0` | 404 | UnwindData |  |
| 34 | `WinHttpFreeProxyResultEx` | `0x46990` | 86 | UnwindData |  |
| 33 | `WinHttpFreeProxyResult` | `0x46E50` | 108 | UnwindData |  |
| 43 | `WinHttpGetProxyForUrlHvsi` | `0x47CF0` | 135 | UnwindData |  |
| 31 | `WinHttpCreateUrl` | `0x4BDA0` | 36 | UnwindData |  |
| 51 | `WinHttpOpenRequest` | `0x4DDC0` | 461 | UnwindData |  |
| 52 | `WinHttpPacJsWorkerMain` | `0x56680` | 246 | UnwindData |  |
| 74 | `WinHttpSetCredentials` | `0x675F0` | 540 | UnwindData |  |
| 71 | `WinHttpResolverGetProxyForUrl` | `0x68630` | 596 | UnwindData |  |
| 38 | `WinHttpGetDefaultProxyConfiguration` | `0x6A7D0` | 495 | UnwindData |  |
| 87 | `WinHttpWebSocketReceive` | `0x6FCB0` | 1,113 | UnwindData |  |
| 40 | `WinHttpGetProxyForUrl` | `0x732D0` | 557 | UnwindData |  |
| 29 | `WinHttpCreateProxyResult` | `0x78930` | 429 | UnwindData |  |
| 66 | `WinHttpReadProxySettingsHvsi` | `0x7D0C0` | 242 | UnwindData |  |
| 48 | `WinHttpGetProxySettingsVersion` | `0x80D30` | 645 | UnwindData |  |
| 42 | `WinHttpGetProxyForUrlEx2` | `0x82210` | 338 | UnwindData |  |
| 70 | `WinHttpResetAutoProxy` | `0x8BFD0` | 514 | UnwindData |  |
| 26 | `WinHttpCreateProxyList` | `0x8C510` | 392 | UnwindData |  |
| 32 | `WinHttpDetectAutoProxyConfigUrl` | `0x8C9B0` | 677 | UnwindData |  |
| 27 | `WinHttpCreateProxyManager` | `0x8E850` | 239 | UnwindData |  |
| 24 | `WinHttpConnectionUpdateIfIndexTable` | `0x8E9F0` | 781 | UnwindData |  |
| 57 | `WinHttpQueryAuthSchemes` | `0x91370` | 670 | UnwindData |  |
| 41 | `WinHttpGetProxyForUrlEx` | `0x91BB0` | 269 | UnwindData |  |
| 20 | `WinHttpConnectionOnlyReceive` | `0x92BD0` | 257 | UnwindData |  |
| 21 | `WinHttpConnectionOnlySend` | `0x95230` | 228 | UnwindData |  |
| 17 | `WinHttpConnectionGetProxyInfo` | `0x96060` | 80 | UnwindData |  |
| 22 | `WinHttpConnectionSetPolicyEntries` | `0x97F30` | 747 | UnwindData |  |
| 44 | `WinHttpGetProxyResult` | `0x98380` | 7,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x9A1B0` | 42,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `WinHttpCheckPlatform` | `0x9A1B0` | 42,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xA4990` | 2,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `WinHttpFreeQueryConnectionGroupResult` | `0xA5340` | 46 | UnwindData |  |
| 58 | `WinHttpQueryConnectionGroup` | `0xA5380` | 402 | UnwindData |  |
| 75 | `WinHttpSetDefaultProxyConfiguration` | `0xA5520` | 424 | UnwindData |  |
| 78 | `WinHttpSetSecureLegacyServersAppCompat` | `0xA56D0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `WinHttpConnectionDeletePolicyEntries` | `0xA5A50` | 670 | UnwindData |  |
| 30 | `WinHttpCreateUiCompatibleProxyString` | `0xA5D00` | 236 | UnwindData |  |
| 36 | `WinHttpFreeProxySettingsEx` | `0xA5E00` | 161 | UnwindData |  |
| 45 | `WinHttpGetProxyResultEx` | `0xA5EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `WinHttpGetProxySettingsEx` | `0xA5ED0` | 609 | UnwindData |  |
| 47 | `WinHttpGetProxySettingsResultEx` | `0xA6140` | 385 | UnwindData |  |
| 68 | `WinHttpRefreshProxySettings` | `0xA62D0` | 260 | UnwindData |  |
| 69 | `WinHttpRegisterProxyChangeNotification` | `0xA63E0` | 253 | UnwindData |  |
| 77 | `WinHttpSetProxySettingsPerUser` | `0xA64F0` | 545 | UnwindData |  |
| 83 | `WinHttpUnregisterProxyChangeNotification` | `0xA6720` | 170 | UnwindData |  |
| 91 | `WinHttpWriteProxySettings` | `0xA67D0` | 746 | UnwindData |  |
| 12 | `WinHttpConnectionDeleteProxyInfo` | `0xA7170` | 71 | UnwindData |  |
| 13 | `WinHttpConnectionFreeNameList` | `0xA71C0` | 54 | UnwindData |  |
| 14 | `WinHttpConnectionFreeProxyInfo` | `0xA7200` | 54 | UnwindData |  |
| 15 | `WinHttpConnectionFreeProxyList` | `0xA7240` | 54 | UnwindData |  |
| 16 | `WinHttpConnectionGetNameList` | `0xA7280` | 78 | UnwindData |  |
| 18 | `WinHttpConnectionGetProxyList` | `0xA72E0` | 78 | UnwindData |  |
| 23 | `WinHttpConnectionSetProxyInfo` | `0xA7340` | 71 | UnwindData |  |
| 49 | `WinHttpGetTunnelSocket` | `0xA74E0` | 201 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0xA8EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `WinHttpAutoProxySvcMain` | `0xA8EF0` | 1,701 | UnwindData |  |
| 19 | `WinHttpConnectionOnlyConvert` | `0xACF10` | 76 | UnwindData |  |
| 3 | `Private1` | `0xB1050` | 663 | UnwindData |  |
| 6 | `WinHttpAddRequestHeadersEx` | `0xB1410` | 2,325 | UnwindData |  |
| 53 | `WinHttpProbeConnectivity` | `0xB2B20` | 97 | UnwindData |  |
| 72 | `WinHttpSaveProxyCredentials` | `0xB2B90` | 71 | UnwindData |  |
| 61 | `WinHttpQueryHeadersEx` | `0xB3850` | 148 | UnwindData |  |
| 82 | `WinHttpTimeToSystemTime` | `0xB38F0` | 659 | UnwindData |  |
| 84 | `WinHttpWebSocketClose` | `0xC8170` | 198 | UnwindData |  |
| 86 | `WinHttpWebSocketQueryCloseStatus` | `0xC8240` | 215 | UnwindData |  |
| 85 | `WinHttpWebSocketCompleteUpgrade` | `0xC8530` | 36 | UnwindData |  |
| 89 | `WinHttpWebSocketShutdown` | `0xC8A00` | 198 | UnwindData |  |
| 54 | `WinHttpProtocolCompleteUpgrade` | `0xC8E00` | 76 | UnwindData |  |
| 55 | `WinHttpProtocolReceive` | `0xC8F40` | 245 | UnwindData |  |
| 56 | `WinHttpProtocolSend` | `0xC9100` | 226 | UnwindData |  |
