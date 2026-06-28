# Binary Specification: winhttp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\winhttp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0a6f2ba84dedf95cf3da755d0b4bc5f7485aaa73defa9099a80e906e5f20e0ba`
* **Total Exported Functions:** 91

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 27 | `WinHttpCreateProxyManager` | `0x2960` | 246 | UnwindData |  |
| 38 | `WinHttpGetDefaultProxyConfiguration` | `0x32A0` | 515 | UnwindData |  |
| 25 | `WinHttpCrackUrl` | `0xCF70` | 40 | UnwindData |  |
| 10 | `WinHttpConnect` | `0xDFB0` | 1,015 | UnwindData |  |
| 90 | `WinHttpWriteData` | `0xF010` | 3,627 | UnwindData |  |
| 59 | `WinHttpQueryDataAvailable` | `0x11290` | 3,584 | UnwindData |  |
| 63 | `WinHttpReadData` | `0x13910` | 255 | UnwindData |  |
| 64 | `WinHttpReadDataEx` | `0x13A20` | 31 | UnwindData |  |
| 9 | `WinHttpCloseHandle` | `0x17EA0` | 2,936 | UnwindData |  |
| 39 | `WinHttpGetIEProxyConfigForCurrentUser` | `0x1B180` | 869 | UnwindData |  |
| 35 | `WinHttpFreeProxySettings` | `0x1D690` | 122 | UnwindData |  |
| 65 | `WinHttpReadProxySettings` | `0x24320` | 1,366 | UnwindData |  |
| 28 | `WinHttpCreateProxyResolver` | `0x24C20` | 961 | UnwindData |  |
| 48 | `WinHttpGetProxySettingsVersion` | `0x25FD0` | 655 | UnwindData |  |
| 87 | `WinHttpWebSocketReceive` | `0x27D00` | 1,151 | UnwindData |  |
| 31 | `WinHttpCreateUrl` | `0x2B720` | 36 | UnwindData |  |
| 24 | `WinHttpConnectionUpdateIfIndexTable` | `0x2E5B0` | 799 | UnwindData |  |
| 41 | `WinHttpGetProxyForUrlEx` | `0x2E9D0` | 284 | UnwindData |  |
| 88 | `WinHttpWebSocketSend` | `0x2ED60` | 207 | UnwindData |  |
| 81 | `WinHttpTimeFromSystemTime` | `0x2F970` | 549 | UnwindData |  |
| 67 | `WinHttpReceiveResponse` | `0x344B0` | 33 | UnwindData |  |
| 32 | `WinHttpDetectAutoProxyConfigUrl` | `0x38550` | 694 | UnwindData |  |
| 76 | `WinHttpSetOption` | `0x43C80` | 821 | UnwindData |  |
| 79 | `WinHttpSetStatusCallback` | `0x43FC0` | 70 | UnwindData |  |
| 50 | `WinHttpOpen` | `0x45790` | 966 | UnwindData |  |
| 80 | `WinHttpSetTimeouts` | `0x48220` | 963 | UnwindData |  |
| 33 | `WinHttpFreeProxyResult` | `0x4D390` | 118 | UnwindData |  |
| 62 | `WinHttpQueryOption` | `0x4E2A0` | 392 | UnwindData |  |
| 34 | `WinHttpFreeProxyResultEx` | `0x4F050` | 96 | UnwindData |  |
| 51 | `WinHttpOpenRequest` | `0x50EB0` | 473 | UnwindData |  |
| 57 | `WinHttpQueryAuthSchemes` | `0x54530` | 700 | UnwindData |  |
| 73 | `WinHttpSendRequest` | `0x54C00` | 1,310 | UnwindData |  |
| 5 | `WinHttpAddRequestHeaders` | `0x56B30` | 889 | UnwindData |  |
| 74 | `WinHttpSetCredentials` | `0x5A240` | 551 | UnwindData |  |
| 71 | `WinHttpResolverGetProxyForUrl` | `0x5B1A0` | 622 | UnwindData |  |
| 40 | `WinHttpGetProxyForUrl` | `0x6F4C0` | 575 | UnwindData |  |
| 29 | `WinHttpCreateProxyResult` | `0x720A0` | 440 | UnwindData |  |
| 66 | `WinHttpReadProxySettingsHvsi` | `0x76620` | 242 | UnwindData |  |
| 42 | `WinHttpGetProxyForUrlEx2` | `0x7B450` | 345 | UnwindData |  |
| 52 | `WinHttpPacJsWorkerMain` | `0x7F9F0` | 262 | UnwindData |  |
| 60 | `WinHttpQueryHeaders` | `0x83CC0` | 1,640 | UnwindData |  |
| 70 | `WinHttpResetAutoProxy` | `0x86410` | 526 | UnwindData |  |
| 26 | `WinHttpCreateProxyList` | `0x86920` | 399 | UnwindData |  |
| 20 | `WinHttpConnectionOnlyReceive` | `0x8C9E0` | 263 | UnwindData |  |
| 21 | `WinHttpConnectionOnlySend` | `0x8F390` | 234 | UnwindData |  |
| 17 | `WinHttpConnectionGetProxyInfo` | `0x91710` | 80 | UnwindData |  |
| 22 | `WinHttpConnectionSetPolicyEntries` | `0x92830` | 755 | UnwindData |  |
| 44 | `WinHttpGetProxyResult` | `0x92C90` | 3,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `WinHttpGetProxyForUrlHvsi` | `0x93BA0` | 135 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x94F20` | 58,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `WinHttpCheckPlatform` | `0x94F20` | 58,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xA33C0` | 2,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `WinHttpFreeQueryConnectionGroupResult` | `0xA3D90` | 46 | UnwindData |  |
| 58 | `WinHttpQueryConnectionGroup` | `0xA3DD0` | 409 | UnwindData |  |
| 75 | `WinHttpSetDefaultProxyConfiguration` | `0xA3F70` | 424 | UnwindData |  |
| 78 | `WinHttpSetSecureLegacyServersAppCompat` | `0xA4120` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `WinHttpConnectionDeletePolicyEntries` | `0xA44B0` | 683 | UnwindData |  |
| 30 | `WinHttpCreateUiCompatibleProxyString` | `0xA4770` | 246 | UnwindData |  |
| 36 | `WinHttpFreeProxySettingsEx` | `0xA4870` | 173 | UnwindData |  |
| 45 | `WinHttpGetProxyResultEx` | `0xA4930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `WinHttpGetProxySettingsEx` | `0xA4950` | 615 | UnwindData |  |
| 47 | `WinHttpGetProxySettingsResultEx` | `0xA4BC0` | 397 | UnwindData |  |
| 68 | `WinHttpRefreshProxySettings` | `0xA4D60` | 270 | UnwindData |  |
| 69 | `WinHttpRegisterProxyChangeNotification` | `0xA4E80` | 264 | UnwindData |  |
| 77 | `WinHttpSetProxySettingsPerUser` | `0xA4F90` | 563 | UnwindData |  |
| 83 | `WinHttpUnregisterProxyChangeNotification` | `0xA51D0` | 180 | UnwindData |  |
| 91 | `WinHttpWriteProxySettings` | `0xA5290` | 759 | UnwindData |  |
| 12 | `WinHttpConnectionDeleteProxyInfo` | `0xA5C80` | 71 | UnwindData |  |
| 13 | `WinHttpConnectionFreeNameList` | `0xA5CD0` | 54 | UnwindData |  |
| 14 | `WinHttpConnectionFreeProxyInfo` | `0xA5D10` | 54 | UnwindData |  |
| 15 | `WinHttpConnectionFreeProxyList` | `0xA5D50` | 54 | UnwindData |  |
| 16 | `WinHttpConnectionGetNameList` | `0xA5D90` | 78 | UnwindData |  |
| 18 | `WinHttpConnectionGetProxyList` | `0xA5DF0` | 78 | UnwindData |  |
| 23 | `WinHttpConnectionSetProxyInfo` | `0xA5E50` | 71 | UnwindData |  |
| 49 | `WinHttpGetTunnelSocket` | `0xA6000` | 211 | UnwindData |  |
| 4 | `SvchostPushServiceGlobals` | `0xA7C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `WinHttpAutoProxySvcMain` | `0xA7C90` | 1,747 | UnwindData |  |
| 19 | `WinHttpConnectionOnlyConvert` | `0xABF20` | 76 | UnwindData |  |
| 3 | `Private1` | `0xB0370` | 663 | UnwindData |  |
| 6 | `WinHttpAddRequestHeadersEx` | `0xB0730` | 2,333 | UnwindData |  |
| 53 | `WinHttpProbeConnectivity` | `0xB1F10` | 97 | UnwindData |  |
| 72 | `WinHttpSaveProxyCredentials` | `0xB1F80` | 71 | UnwindData |  |
| 61 | `WinHttpQueryHeadersEx` | `0xB2C40` | 148 | UnwindData |  |
| 82 | `WinHttpTimeToSystemTime` | `0xB2CE0` | 676 | UnwindData |  |
| 84 | `WinHttpWebSocketClose` | `0xC82C0` | 208 | UnwindData |  |
| 86 | `WinHttpWebSocketQueryCloseStatus` | `0xC83A0` | 225 | UnwindData |  |
| 85 | `WinHttpWebSocketCompleteUpgrade` | `0xC86B0` | 36 | UnwindData |  |
| 89 | `WinHttpWebSocketShutdown` | `0xC8B80` | 208 | UnwindData |  |
| 54 | `WinHttpProtocolCompleteUpgrade` | `0xC8FA0` | 76 | UnwindData |  |
| 55 | `WinHttpProtocolReceive` | `0xC90E0` | 252 | UnwindData |  |
| 56 | `WinHttpProtocolSend` | `0xC92B0` | 238 | UnwindData |  |
