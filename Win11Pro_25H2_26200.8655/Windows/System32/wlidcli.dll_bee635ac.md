# Binary Specification: wlidcli.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wlidcli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bee635ac2563b5925b663f237594c6bdd6d52bab4d9b02e6e0e8757c42678659`
* **Total Exported Functions:** 96

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `DllInstall` | `0x11F30` | 4,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllRegisterServer` | `0x11F30` | 4,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DllUnregisterServer` | `0x11F30` | 4,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `SetDeviceConsent` | `0x11F30` | 4,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `IDCRL_GetLatestProtectionKey` | `0x12F90` | 74,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `IDCRL_GetSpecifiedProtectionKey` | `0x12F90` | 74,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `RemoveChangeNotificationCallback` | `0x12F90` | 74,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `SendOneTimeCode` | `0x12F90` | 74,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `SetChangeNotificationCallback` | `0x12F90` | 74,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `GetDeviceShortLivedToken` | `0x251A0` | 222 | UnwindData |  |
| 95 | `IsMappedError` | `0x257D0` | 119 | UnwindData |  |
| 13 | `AuthIdentityToService` | `0x28B60` | 220 | UnwindData |  |
| 33 | `AuthIdentityToServiceEx` | `0x28C50` | 26 | UnwindData |  |
| 38 | `CancelPendingRequest` | `0x28C70` | 300 | UnwindData |  |
| 19 | `CloseEnumIdentitiesHandle` | `0x28DB0` | 178 | UnwindData |  |
| 8 | `CloseIdentityHandle` | `0x28E70` | 175 | UnwindData |  |
| 4 | `CreateIdentityHandle` | `0x28F30` | 400 | UnwindData |  |
| 68 | `CreateLinkedIdentityHandle` | `0x290D0` | 1,425 | UnwindData |  |
| 101 | `DeProvisionDeviceId` | `0x29670` | 241 | UnwindData |  |
| 54 | `DecryptWithSessionKey` | `0x29770` | 965 | UnwindData |  |
| 53 | `EncryptWithSessionKey` | `0x29B40` | 965 | UnwindData |  |
| 17 | `EnumIdentitiesWithCachedCredentials` | `0x29F10` | 499 | UnwindData |  |
| 62 | `EnumerateCertificates` | `0x2A110` | 590 | UnwindData |  |
| 70 | `EnumerateDeviceID` | `0x2A370` | 1,551 | UnwindData |  |
| 86 | `EnumerateUserAssociatedDevices` | `0x2A990` | 981 | UnwindData |  |
| 94 | `FlushIDCRLTraceBuffer` | `0x2AD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `GenerateCertToken` | `0x2AD80` | 1,716 | UnwindData |  |
| 67 | `GenerateDeviceToken` | `0x2B440` | 551 | UnwindData |  |
| 72 | `GetAssertion` | `0x2B670` | 60 | UnwindData |  |
| 20 | `GetAuthState` | `0x2B6C0` | 774 | UnwindData |  |
| 34 | `GetAuthStateEx` | `0x2B9D0` | 1,085 | UnwindData |  |
| 96 | `GetAuthenticationStatus` | `0x2BE20` | 1,246 | UnwindData |  |
| 35 | `GetCertificate` | `0x2C310` | 1,324 | UnwindData |  |
| 97 | `GetConfigDWORDValue` | `0x2C850` | 215 | UnwindData |  |
| 104 | `GetDefaultNoUISSOUser` | `0x2C930` | 422 | UnwindData |  |
| 82 | `GetDefaultUserForTarget` | `0x2CAE0` | 340 | UnwindData |  |
| 64 | `GetDeviceId` | `0x2CC40` | 897 | UnwindData |  |
| 99 | `GetDeviceIdEx` | `0x2CFD0` | 835 | UnwindData |  |
| 60 | `GetExtendedError` | `0x2D320` | 4,694 | UnwindData |  |
| 48 | `GetExtendedProperty` | `0x2E580` | 283 | UnwindData |  |
| 78 | `GetHIPChallenge` | `0x2E6B0` | 529 | UnwindData |  |
| 6 | `GetIdentityProperty` | `0x2E8D0` | 1,113 | UnwindData |  |
| 41 | `GetIdentityPropertyByName` | `0x2ED30` | 873 | UnwindData |  |
| 112 | `GetRealmInfo` | `0x2F0A0` | 187 | UnwindData |  |
| 76 | `GetResponseForHttpChallenge` | `0x2F170` | 1,432 | UnwindData |  |
| 49 | `GetServiceConfig` | `0x2F710` | 371 | UnwindData |  |
| 56 | `GetUserExtendedProperty` | `0x2F890` | 515 | UnwindData |  |
| 30 | `GetWebAuthUrl` | `0x2FAA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `GetWebAuthUrlEx` | `0x2FAC0` | 3,000 | UnwindData |  |
| 23 | `HasPersistedCredential` | `0x30680` | 729 | UnwindData |  |
| 1 | `Initialize` | `0x30960` | 23 | UnwindData |  |
| 61 | `InitializeApp` | `0x30980` | 1,356 | UnwindData |  |
| 29 | `InitializeEx` | `0x30EE0` | 158 | UnwindData |  |
| 93 | `InitializeIDCRLTraceBuffer` | `0x30F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `IsDeviceIDAdmin` | `0x30FB0` | 176 | UnwindData |  |
| 21 | `LogonIdentity` | `0x31070` | 23 | UnwindData |  |
| 31 | `LogonIdentityEx` | `0x31090` | 715 | UnwindData |  |
| 108 | `LogonIdentityExSSO` | `0x31370` | 338 | UnwindData |  |
| 75 | `LogonIdentityExWithUI` | `0x314D0` | 226 | UnwindData |  |
| 18 | `NextIdentity` | `0x316D0` | 339 | UnwindData |  |
| 74 | `OpenAuthenticatedBrowser` | `0x31830` | 390 | UnwindData |  |
| 3 | `PassportFreeMemory` | `0x319C0` | 178 | UnwindData |  |
| 15 | `PersistCredential` | `0x31A80` | 929 | UnwindData |  |
| 98 | `ProvisionDeviceId` | `0x31E30` | 241 | UnwindData |  |
| 16 | `RemovePersistedCredential` | `0x31F30` | 870 | UnwindData |  |
| 100 | `RenewDeviceId` | `0x322A0` | 241 | UnwindData |  |
| 5 | `SetCredential` | `0x323A0` | 2,078 | UnwindData |  |
| 81 | `SetDefaultUserForTarget` | `0x32BD0` | 475 | UnwindData |  |
| 47 | `SetExtendedProperty` | `0x32DC0` | 266 | UnwindData |  |
| 79 | `SetHIPSolution` | `0x32ED0` | 614 | UnwindData |  |
| 51 | `SetIdcrlOptions` | `0x33140` | 1,062 | UnwindData |  |
| 24 | `SetIdentityCallback` | `0x33570` | 520 | UnwindData |  |
| 7 | `SetIdentityProperty` | `0x33780` | 545 | UnwindData |  |
| 55 | `SetUserExtendedProperty` | `0x339B0` | 591 | UnwindData |  |
| 2 | `Uninitialize` | `0x33C10` | 490 | UnwindData |  |
| 87 | `UpdateUserAssociatedDeviceProperties` | `0x33E00` | 1,328 | UnwindData |  |
| 73 | `VerifyAssertion` | `0x34340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `VerifyCertificate` | `0x34350` | 594 | UnwindData |  |
| 114 | `AddUserToSsoGroup` | `0x345B0` | 621 | UnwindData |  |
| 84 | `AssociateDeviceToUser` | `0x34830` | 787 | UnwindData |  |
| 113 | `CreateIdentityHandleEx` | `0x34B50` | 959 | UnwindData |  |
| 119 | `DecryptWithSessionKeyEx` | `0x34F20` | 800 | UnwindData |  |
| 85 | `DisassociateDeviceFromUser` | `0x35250` | 579 | UnwindData |  |
| 118 | `EncryptWithSessionKeyEx` | `0x354A0` | 781 | UnwindData |  |
| 120 | `GetErrorMessage` | `0x357C0` | 460 | UnwindData |  |
| 115 | `GetUsersFromSsoGroup` | `0x359A0` | 1,036 | UnwindData |  |
| 116 | `RemoveUserFromSsoGroup` | `0x35DC0` | 617 | UnwindData |  |
| 121 | `SendWatsonReport` | `0x36030` | 504 | UnwindData |  |
| 110 | `StartTracing` | `0x36230` | 45 | UnwindData |  |
| 111 | `StopTracing` | `0x36270` | 133 | UnwindData |  |
| 9 | `DllCanUnloadNow` | `0x37A30` | 68 | UnwindData |  |
| 10 | `DllGetClassObject` | `0x37A80` | 120 | UnwindData |  |
| 83 | `UICollectCredential` | `0x3FD60` | 301 | UnwindData |  |
| 92 | `UIEndWaitDialog` | `0x40760` | 110 | UnwindData |  |
| 91 | `UIShowWaitDialog` | `0x407E0` | 222 | UnwindData |  |
| 102 | `UnPackErrorBlob` | `0x408D0` | 50 | UnwindData |  |
