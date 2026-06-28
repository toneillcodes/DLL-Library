# Binary Specification: usermgrcli.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\usermgrcli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `be229b1169a3ab14391c79c7fab120ef29c65c2eb989ca1961b93e44366749cc`
* **Total Exported Functions:** 39

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 31 | `UMgrQueryUserContext` | `0x1180` | 30 | UnwindData |  |
| 34 | `UMgrQueryUserToken` | `0x18B0` | 30 | UnwindData |  |
| 14 | `UMgrGetConstrainedUserToken` | `0x1F20` | 104 | UnwindData |  |
| 25 | `UMgrLogonUser` | `0x2260` | 260 | UnwindData |  |
| 33 | `UMgrQueryUserContextFromSid` | `0x2710` | 30 | UnwindData |  |
| 17 | `UMgrGetSessionActiveShellUserToken` | `0x27E0` | 40 | UnwindData |  |
| 16 | `UMgrGetImpersonationTokenForContext` | `0x2870` | 35 | UnwindData |  |
| 36 | `UMgrQueryUserTokenFromSid` | `0x2900` | 30 | UnwindData |  |
| 22 | `UMgrIsAllowedToActivateAsUser` | `0x2990` | 35 | UnwindData |  |
| 10 | `UMgrEnumerateSessionUsers` | `0x2A90` | 30 | UnwindData |  |
| 11 | `UMgrFreeSessionUsers` | `0x42A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `UMgrOpenProcessHandleForAccess` | `0x42C0` | 146 | UnwindData |  |
| 27 | `UMgrOpenProcessTokenForQuery` | `0x43F0` | 236 | UnwindData |  |
| 19 | `UMgrInformFlags` | `0x5050` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `UMgrSetShellInformation` | `0x50C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `UMgrQueryDefaultAccountToken` | `0x50D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `UMgrInformUserLogoff` | `0x5120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `UMgrInformUserLogon` | `0x5130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `UMgrLaunchShellInfrastructureHost` | `0x5140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `UMgrLaunchShell` | `0x5150` | 14,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `UMgrChangeSessionActiveShellUser` | `0x89B0` | 40 | UnwindData |  |
| 6 | `UMgrChangeSessionUserToken` | `0x89E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `UMgrClearDefaultSignInAccount` | `0x89F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `UMgrConnectLocalUser` | `0x8A00` | 74 | UnwindData |  |
| 9 | `UMgrDisconnectLocalUser` | `0x8A50` | 80 | UnwindData |  |
| 12 | `UMgrFreeUserCredentials` | `0x8AB0` | 84 | UnwindData |  |
| 13 | `UMgrGetCachedCredentials` | `0x8B10` | 30 | UnwindData |  |
| 15 | `UMgrGetDefaultSignInAccount` | `0x8B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `UMgrGetStandardAccessImpersonationTokenForContext` | `0x8B50` | 34 | UnwindData |  |
| 29 | `UMgrQuerySessionUserToken` | `0x8B80` | 40 | UnwindData |  |
| 30 | `UMgrQuerySessionVirtualAccountToken` | `0x8BB0` | 40 | UnwindData |  |
| 32 | `UMgrQueryUserContextFromName` | `0x8BE0` | 30 | UnwindData |  |
| 35 | `UMgrQueryUserTokenFromName` | `0x8C10` | 30 | UnwindData |  |
| 37 | `UMgrSetCachedCredentials` | `0x8C40` | 51 | UnwindData |  |
| 39 | `UMgrpGetRegistryLocation` | `0x8C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `IsInteractiveUserSession` | `0x8C90` | 93 | UnwindData |  |
| 2 | `QueryActiveSession` | `0x8D00` | 111 | UnwindData |  |
| 3 | `QueryUserToken` | `0x8D80` | 164 | UnwindData |  |
| 4 | `RegisterUsertokenForNoWinlogon` | `0x8E30` | 29 | UnwindData |  |
