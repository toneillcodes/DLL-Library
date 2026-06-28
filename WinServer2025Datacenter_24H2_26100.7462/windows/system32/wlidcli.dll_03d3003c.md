# Binary Specification: wlidcli.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wlidcli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `03d3003c5ce7b5d48e5fc7ae59158c2409077b4f0664cf6bced7031e2ca41e46`
* **Total Exported Functions:** 96

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `DllInstall` | `0x11DF0` | 4,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllRegisterServer` | `0x11DF0` | 4,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `DllUnregisterServer` | `0x11DF0` | 4,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `SetDeviceConsent` | `0x11DF0` | 4,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `IDCRL_GetLatestProtectionKey` | `0x12E50` | 74,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `IDCRL_GetSpecifiedProtectionKey` | `0x12E50` | 74,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `RemoveChangeNotificationCallback` | `0x12E50` | 74,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `SendOneTimeCode` | `0x12E50` | 74,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `SetChangeNotificationCallback` | `0x12E50` | 74,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `GetDeviceShortLivedToken` | `0x25060` | 222 | UnwindData |  |
| 95 | `IsMappedError` | `0x25690` | 119 | UnwindData |  |
| 13 | `AuthIdentityToService` | `0x28A20` | 220 | UnwindData |  |
| 33 | `AuthIdentityToServiceEx` | `0x28B10` | 26 | UnwindData |  |
| 38 | `CancelPendingRequest` | `0x28B30` | 300 | UnwindData |  |
| 19 | `CloseEnumIdentitiesHandle` | `0x28C70` | 178 | UnwindData |  |
| 8 | `CloseIdentityHandle` | `0x28D30` | 175 | UnwindData |  |
| 4 | `CreateIdentityHandle` | `0x28DF0` | 400 | UnwindData |  |
| 68 | `CreateLinkedIdentityHandle` | `0x28F90` | 1,425 | UnwindData |  |
| 101 | `DeProvisionDeviceId` | `0x29530` | 241 | UnwindData |  |
| 54 | `DecryptWithSessionKey` | `0x29630` | 965 | UnwindData |  |
| 53 | `EncryptWithSessionKey` | `0x29A00` | 965 | UnwindData |  |
| 17 | `EnumIdentitiesWithCachedCredentials` | `0x29DD0` | 499 | UnwindData |  |
| 62 | `EnumerateCertificates` | `0x29FD0` | 590 | UnwindData |  |
| 70 | `EnumerateDeviceID` | `0x2A230` | 1,551 | UnwindData |  |
| 86 | `EnumerateUserAssociatedDevices` | `0x2A850` | 981 | UnwindData |  |
| 94 | `FlushIDCRLTraceBuffer` | `0x2AC30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `GenerateCertToken` | `0x2AC40` | 1,716 | UnwindData |  |
| 67 | `GenerateDeviceToken` | `0x2B300` | 551 | UnwindData |  |
| 72 | `GetAssertion` | `0x2B530` | 60 | UnwindData |  |
| 20 | `GetAuthState` | `0x2B580` | 774 | UnwindData |  |
| 34 | `GetAuthStateEx` | `0x2B890` | 1,085 | UnwindData |  |
| 96 | `GetAuthenticationStatus` | `0x2BCE0` | 1,246 | UnwindData |  |
| 35 | `GetCertificate` | `0x2C1D0` | 1,324 | UnwindData |  |
| 97 | `GetConfigDWORDValue` | `0x2C710` | 215 | UnwindData |  |
| 104 | `GetDefaultNoUISSOUser` | `0x2C7F0` | 422 | UnwindData |  |
| 82 | `GetDefaultUserForTarget` | `0x2C9A0` | 340 | UnwindData |  |
| 64 | `GetDeviceId` | `0x2CB00` | 897 | UnwindData |  |
| 99 | `GetDeviceIdEx` | `0x2CE90` | 835 | UnwindData |  |
| 60 | `GetExtendedError` | `0x2D1E0` | 4,694 | UnwindData |  |
| 48 | `GetExtendedProperty` | `0x2E440` | 283 | UnwindData |  |
| 78 | `GetHIPChallenge` | `0x2E570` | 529 | UnwindData |  |
| 6 | `GetIdentityProperty` | `0x2E790` | 1,113 | UnwindData |  |
| 41 | `GetIdentityPropertyByName` | `0x2EBF0` | 873 | UnwindData |  |
| 112 | `GetRealmInfo` | `0x2EF60` | 187 | UnwindData |  |
| 76 | `GetResponseForHttpChallenge` | `0x2F030` | 1,432 | UnwindData |  |
| 49 | `GetServiceConfig` | `0x2F5D0` | 371 | UnwindData |  |
| 56 | `GetUserExtendedProperty` | `0x2F750` | 515 | UnwindData |  |
| 30 | `GetWebAuthUrl` | `0x2F960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `GetWebAuthUrlEx` | `0x2F980` | 3,000 | UnwindData |  |
| 23 | `HasPersistedCredential` | `0x30540` | 729 | UnwindData |  |
| 1 | `Initialize` | `0x30820` | 23 | UnwindData |  |
| 61 | `InitializeApp` | `0x30840` | 1,356 | UnwindData |  |
| 29 | `InitializeEx` | `0x30DA0` | 158 | UnwindData |  |
| 93 | `InitializeIDCRLTraceBuffer` | `0x30E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `IsDeviceIDAdmin` | `0x30E70` | 176 | UnwindData |  |
| 21 | `LogonIdentity` | `0x30F30` | 23 | UnwindData |  |
| 31 | `LogonIdentityEx` | `0x30F50` | 715 | UnwindData |  |
| 108 | `LogonIdentityExSSO` | `0x31230` | 338 | UnwindData |  |
| 75 | `LogonIdentityExWithUI` | `0x31390` | 226 | UnwindData |  |
| 18 | `NextIdentity` | `0x31590` | 339 | UnwindData |  |
| 74 | `OpenAuthenticatedBrowser` | `0x316F0` | 390 | UnwindData |  |
| 3 | `PassportFreeMemory` | `0x31880` | 178 | UnwindData |  |
| 15 | `PersistCredential` | `0x31940` | 929 | UnwindData |  |
| 98 | `ProvisionDeviceId` | `0x31CF0` | 241 | UnwindData |  |
| 16 | `RemovePersistedCredential` | `0x31DF0` | 870 | UnwindData |  |
| 100 | `RenewDeviceId` | `0x32160` | 241 | UnwindData |  |
| 5 | `SetCredential` | `0x32260` | 2,078 | UnwindData |  |
| 81 | `SetDefaultUserForTarget` | `0x32A90` | 475 | UnwindData |  |
| 47 | `SetExtendedProperty` | `0x32C80` | 266 | UnwindData |  |
| 79 | `SetHIPSolution` | `0x32D90` | 614 | UnwindData |  |
| 51 | `SetIdcrlOptions` | `0x33000` | 1,062 | UnwindData |  |
| 24 | `SetIdentityCallback` | `0x33430` | 520 | UnwindData |  |
| 7 | `SetIdentityProperty` | `0x33640` | 545 | UnwindData |  |
| 55 | `SetUserExtendedProperty` | `0x33870` | 591 | UnwindData |  |
| 2 | `Uninitialize` | `0x33AD0` | 490 | UnwindData |  |
| 87 | `UpdateUserAssociatedDeviceProperties` | `0x33CC0` | 1,328 | UnwindData |  |
| 73 | `VerifyAssertion` | `0x34200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `VerifyCertificate` | `0x34210` | 594 | UnwindData |  |
| 114 | `AddUserToSsoGroup` | `0x34470` | 621 | UnwindData |  |
| 84 | `AssociateDeviceToUser` | `0x346F0` | 787 | UnwindData |  |
| 113 | `CreateIdentityHandleEx` | `0x34A10` | 959 | UnwindData |  |
| 119 | `DecryptWithSessionKeyEx` | `0x34DE0` | 800 | UnwindData |  |
| 85 | `DisassociateDeviceFromUser` | `0x35110` | 579 | UnwindData |  |
| 118 | `EncryptWithSessionKeyEx` | `0x35360` | 781 | UnwindData |  |
| 120 | `GetErrorMessage` | `0x35680` | 460 | UnwindData |  |
| 115 | `GetUsersFromSsoGroup` | `0x35860` | 1,036 | UnwindData |  |
| 116 | `RemoveUserFromSsoGroup` | `0x35C80` | 617 | UnwindData |  |
| 121 | `SendWatsonReport` | `0x35EF0` | 504 | UnwindData |  |
| 110 | `StartTracing` | `0x360F0` | 45 | UnwindData |  |
| 111 | `StopTracing` | `0x36130` | 133 | UnwindData |  |
| 9 | `DllCanUnloadNow` | `0x378F0` | 68 | UnwindData |  |
| 10 | `DllGetClassObject` | `0x37940` | 120 | UnwindData |  |
| 83 | `UICollectCredential` | `0x3FC20` | 301 | UnwindData |  |
| 92 | `UIEndWaitDialog` | `0x40620` | 110 | UnwindData |  |
| 91 | `UIShowWaitDialog` | `0x406A0` | 222 | UnwindData |  |
| 102 | `UnPackErrorBlob` | `0x40790` | 50 | UnwindData |  |
