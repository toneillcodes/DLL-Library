# Binary Specification: oneauth.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Microsoft-Edge-WebView\oneauth.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1d2ae4300c5e45c9602ac3770d8782582dd7c328d2f52c9a4a341c448aea6350`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 27 | `OneAuthUninitialize` | `0x4640` | 55 | UnwindData |  |
| 15 | `OneAuthInitialize` | `0x46D0` | 343 | UnwindData |  |
| 11 | `OneAuthGetDeviceInfo` | `0x4830` | 127 | UnwindData |  |
| 20 | `OneAuthSignInInteractively` | `0x48B0` | 382 | UnwindData |  |
| 21 | `OneAuthSignInSilently` | `0x4A30` | 419 | UnwindData |  |
| 22 | `OneAuthSignOutInteractively` | `0x5660` | 772 | UnwindData |  |
| 23 | `OneAuthSignOutSilently` | `0x5970` | 811 | UnwindData |  |
| 17 | `OneAuthIsBrokerEnabled` | `0x5CA0` | 236 | UnwindData |  |
| 4 | `OneAuthAcquireCredentialSilently` | `0x5D90` | 907 | UnwindData |  |
| 3 | `OneAuthAcquireAccessTokenSilently` | `0x6120` | 1,816 | UnwindData |  |
| 2 | `OneAuthAcquireAccessTokenInteractively` | `0x6F40` | 2,504 | UnwindData |  |
| 16 | `OneAuthIsAccountAssociated` | `0x7BB0` | 663 | UnwindData |  |
| 5 | `OneAuthAssociateAccount` | `0x7E50` | 457 | UnwindData |  |
| 6 | `OneAuthDisassociateAccount` | `0x8020` | 465 | UnwindData |  |
| 7 | `OneAuthDiscoverAccounts` | `0x8200` | 599 | UnwindData |  |
| 18 | `OneAuthReadAccountById` | `0x8460` | 571 | UnwindData |  |
| 19 | `OneAuthReadAllAccounts` | `0x8840` | 1,309 | UnwindData |  |
| 12 | `OneAuthGetProfileImage` | `0x8D60` | 578 | UnwindData |  |
| 13 | `OneAuthGetProofOfPossessionCookieInfo` | `0x8FB0` | 1,120 | UnwindData |  |
| 24 | `OneAuthTestDeleteAllAccounts` | `0x9410` | 161 | UnwindData |  |
| 9 | `OneAuthGetAccountProperty` | `0x94C0` | 725 | UnwindData |  |
| 14 | `OneAuthGetVersion` | `0x97A0` | 198 | UnwindData |  |
| 26 | `OneAuthTrackAccountChangeForEdgeClient` | `0x98E0` | 805 | UnwindData |  |
| 28 | `OneAuthUntrackAccountChangeForEdgeClient` | `0x9C10` | 702 | UnwindData |  |
| 29 | `OneAuthUntrackAllAccountChangeForEdgeClient` | `0x9ED0` | 289 | UnwindData |  |
| 1 | `LaunchAccountTransferFlow` | `0xA000` | 282 | UnwindData |  |
| 10 | `OneAuthGetBrowserSupportedNativeContracts` | `0xA120` | 387 | UnwindData |  |
| 8 | `OneAuthExecuteBrowserNativeRequest` | `0xA2B0` | 282 | UnwindData |  |
| 25 | `OneAuthTestSetLogPiiEnabled` | `0xFEE0` | 3,658,846 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
