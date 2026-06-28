# Binary Specification: oneauth.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Microsoft-Edge-WebView\oneauth.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `71559c26098850ee818ab600872ef3cb246ec0186b87bf0582dc975515a9c1bc`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `OneAuthReadAllAccounts` | `0x865C0` | 1,268 | UnwindData |  |
| 15 | `OneAuthInitialize` | `0x949B0` | 379 | UnwindData |  |
| 7 | `OneAuthDiscoverAccounts` | `0xCC5C0` | 621 | UnwindData |  |
| 13 | `OneAuthGetProofOfPossessionCookieInfo` | `0xD2A40` | 1,197 | UnwindData |  |
| 21 | `OneAuthSignInSilently` | `0xD60E0` | 2,522 | UnwindData |  |
| 29 | `OneAuthUntrackAllAccountChangeForEdgeClient` | `0xE68B0` | 333 | UnwindData |  |
| 27 | `OneAuthUninitialize` | `0xF0800` | 58 | UnwindData |  |
| 17 | `OneAuthIsBrokerEnabled` | `0xF5BD0` | 253 | UnwindData |  |
| 14 | `OneAuthGetVersion` | `0xF5CD0` | 180 | UnwindData |  |
| 11 | `OneAuthGetDeviceInfo` | `0x135270` | 121 | UnwindData |  |
| 20 | `OneAuthSignInInteractively` | `0x1352F0` | 407 | UnwindData |  |
| 22 | `OneAuthSignOutInteractively` | `0x135600` | 815 | UnwindData |  |
| 23 | `OneAuthSignOutSilently` | `0x135930` | 870 | UnwindData |  |
| 4 | `OneAuthAcquireCredentialSilently` | `0x135CA0` | 1,009 | UnwindData |  |
| 3 | `OneAuthAcquireAccessTokenSilently` | `0x1360A0` | 2,013 | UnwindData |  |
| 2 | `OneAuthAcquireAccessTokenInteractively` | `0x136F50` | 2,707 | UnwindData |  |
| 16 | `OneAuthIsAccountAssociated` | `0x137CA0` | 756 | UnwindData |  |
| 5 | `OneAuthAssociateAccount` | `0x137FA0` | 527 | UnwindData |  |
| 6 | `OneAuthDisassociateAccount` | `0x1381B0` | 541 | UnwindData |  |
| 18 | `OneAuthReadAccountById` | `0x1383D0` | 610 | UnwindData |  |
| 12 | `OneAuthGetProfileImage` | `0x138640` | 635 | UnwindData |  |
| 24 | `OneAuthTestDeleteAllAccounts` | `0x1388C0` | 157 | UnwindData |  |
| 9 | `OneAuthGetAccountProperty` | `0x138960` | 803 | UnwindData |  |
| 26 | `OneAuthTrackAccountChangeForEdgeClient` | `0x138C90` | 863 | UnwindData |  |
| 28 | `OneAuthUntrackAccountChangeForEdgeClient` | `0x138FF0` | 738 | UnwindData |  |
| 1 | `LaunchAccountTransferFlow` | `0x1392E0` | 297 | UnwindData |  |
| 10 | `OneAuthGetBrowserSupportedNativeContracts` | `0x139410` | 435 | UnwindData |  |
| 8 | `OneAuthExecuteBrowserNativeRequest` | `0x1395D0` | 297 | UnwindData |  |
| 25 | `OneAuthTestSetLogPiiEnabled` | `0x13EA00` | 2,548,667 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
