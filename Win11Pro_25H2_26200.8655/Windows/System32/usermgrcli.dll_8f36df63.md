# Binary Specification: usermgrcli.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\usermgrcli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8f36df633756eecef02a2c606a7c5ab7ba032bbb164709c4977a8b26b0232b89`
* **Total Exported Functions:** 41

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 33 | `UMgrQueryUserContext` | `0x1180` | 30 | UnwindData |  |
| 36 | `UMgrQueryUserToken` | `0x18B0` | 30 | UnwindData |  |
| 14 | `UMgrGetConstrainedUserToken` | `0x1F20` | 104 | UnwindData |  |
| 35 | `UMgrQueryUserContextFromSid` | `0x2380` | 30 | UnwindData |  |
| 17 | `UMgrGetSessionActiveShellUserToken` | `0x2450` | 40 | UnwindData |  |
| 16 | `UMgrGetImpersonationTokenForContext` | `0x24E0` | 35 | UnwindData |  |
| 38 | `UMgrQueryUserTokenFromSid` | `0x2570` | 30 | UnwindData |  |
| 24 | `UMgrIsAllowedToActivateAsUser` | `0x2600` | 35 | UnwindData |  |
| 10 | `UMgrEnumerateSessionUsers` | `0x2700` | 30 | UnwindData |  |
| 11 | `UMgrFreeSessionUsers` | `0x3D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `UMgrOpenProcessHandleForAccess` | `0x3D70` | 146 | UnwindData |  |
| 29 | `UMgrOpenProcessTokenForQuery` | `0x3EA0` | 236 | UnwindData |  |
| 27 | `UMgrLogonUser` | `0x47F0` | 333 | UnwindData |  |
| 19 | `UMgrInformFlags` | `0x4E10` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `UMgrSetShellInformation` | `0x4E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `UMgrQueryDefaultAccountToken` | `0x4E90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `UMgrInformUserLogoff` | `0x4EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `UMgrInformUserLogon` | `0x4EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `UMgrLaunchShellInfrastructureHost` | `0x4F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `UMgrLaunchShell` | `0x4F10` | 15,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `UMgrChangeSessionActiveShellUser` | `0x8BE0` | 40 | UnwindData |  |
| 6 | `UMgrChangeSessionUserToken` | `0x8C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `UMgrClearDefaultSignInAccount` | `0x8C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `UMgrConnectLocalUser` | `0x8C30` | 74 | UnwindData |  |
| 9 | `UMgrDisconnectLocalUser` | `0x8C80` | 80 | UnwindData |  |
| 12 | `UMgrFreeUserCredentials` | `0x8CE0` | 84 | UnwindData |  |
| 13 | `UMgrGetCachedCredentials` | `0x8D40` | 30 | UnwindData |  |
| 15 | `UMgrGetDefaultSignInAccount` | `0x8D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `UMgrGetStandardAccessImpersonationTokenForContext` | `0x8D80` | 34 | UnwindData |  |
| 20 | `UMgrInformSecondaryUserLogoff` | `0x8DB0` | 40 | UnwindData |  |
| 21 | `UMgrInformSecondaryUserLogon` | `0x8DE0` | 40 | UnwindData |  |
| 31 | `UMgrQuerySessionUserToken` | `0x8E10` | 40 | UnwindData |  |
| 32 | `UMgrQuerySessionVirtualAccountToken` | `0x8E40` | 40 | UnwindData |  |
| 34 | `UMgrQueryUserContextFromName` | `0x8E70` | 30 | UnwindData |  |
| 37 | `UMgrQueryUserTokenFromName` | `0x8EA0` | 30 | UnwindData |  |
| 39 | `UMgrSetCachedCredentials` | `0x8ED0` | 51 | UnwindData |  |
| 41 | `UMgrpGetRegistryLocation` | `0x8F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `IsInteractiveUserSession` | `0x8F20` | 93 | UnwindData |  |
| 2 | `QueryActiveSession` | `0x8F90` | 111 | UnwindData |  |
| 3 | `QueryUserToken` | `0x9010` | 164 | UnwindData |  |
| 4 | `RegisterUsertokenForNoWinlogon` | `0x90C0` | 29 | UnwindData |  |
