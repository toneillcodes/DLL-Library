# Binary Specification: msidcrl40.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msidcrl40.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6f74bcf0e40fa16e017ef575e7be71d2803eabbacbe621da2d697963b107270b`
* **Total Exported Functions:** 85

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 114 | `AddUserToSsoGroup` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.AddUserToSsoGroup` |
| 84 | `AssociateDeviceToUser` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.AssociateDeviceToUser` |
| 13 | `AuthIdentityToService` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.AuthIdentityToService` |
| 33 | `AuthIdentityToServiceEx` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.AuthIdentityToServiceEx` |
| 38 | `CancelPendingRequest` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.CancelPendingRequest` |
| 19 | `CloseEnumIdentitiesHandle` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.CloseEnumIdentitiesHandle` |
| 8 | `CloseIdentityHandle` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.CloseIdentityHandle` |
| 4 | `CreateIdentityHandle` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.CreateIdentityHandle` |
| 113 | `CreateIdentityHandleEx` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.CreateIdentityHandleEx` |
| 68 | `CreateLinkedIdentityHandle` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.CreateLinkedIdentityHandle` |
| 101 | `DeProvisionDeviceId` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.DeProvisionDeviceId` |
| 54 | `DecryptWithSessionKey` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.DecryptWithSessionKey` |
| 85 | `DisassociateDeviceFromUser` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.DisassociateDeviceFromUser` |
| 53 | `EncryptWithSessionKey` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.EncryptWithSessionKey` |
| 17 | `EnumIdentitiesWithCachedCredentials` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.EnumIdentitiesWithCachedCredentials` |
| 62 | `EnumerateCertificates` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.EnumerateCertificates` |
| 70 | `EnumerateDeviceID` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.EnumerateDeviceID` |
| 86 | `EnumerateUserAssociatedDevices` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.EnumerateUserAssociatedDevices` |
| 94 | `FlushIDCRLTraceBuffer` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.FlushIDCRLTraceBuffer` |
| 63 | `GenerateCertToken` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GenerateCertToken` |
| 67 | `GenerateDeviceToken` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GenerateDeviceToken` |
| 72 | `GetAssertion` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetAssertion` |
| 20 | `GetAuthState` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetAuthState` |
| 34 | `GetAuthStateEx` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetAuthStateEx` |
| 96 | `GetAuthenticationStatus` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetAuthenticationStatus` |
| 35 | `GetCertificate` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetCertificate` |
| 97 | `GetConfigDWORDValue` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetConfigDWORDValue` |
| 104 | `GetDefaultNoUISSOUser` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetDefaultNoUISSOUser` |
| 82 | `GetDefaultUserForTarget` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetDefaultUserForTarget` |
| 64 | `GetDeviceId` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetDeviceId` |
| 99 | `GetDeviceIdEx` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetDeviceIdEx` |
| 77 | `GetDeviceShortLivedToken` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetDeviceShortLivedToken` |
| 60 | `GetExtendedError` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetExtendedError` |
| 48 | `GetExtendedProperty` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetExtendedProperty` |
| 78 | `GetHIPChallenge` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetHIPChallenge` |
| 6 | `GetIdentityProperty` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetIdentityProperty` |
| 41 | `GetIdentityPropertyByName` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetIdentityPropertyByName` |
| 112 | `GetRealmInfo` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetRealmInfo` |
| 76 | `GetResponseForHttpChallenge` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetResponseForHttpChallenge` |
| 49 | `GetServiceConfig` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetServiceConfig` |
| 56 | `GetUserExtendedProperty` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetUserExtendedProperty` |
| 115 | `GetUsersFromSsoGroup` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetUsersFromSsoGroup` |
| 30 | `GetWebAuthUrl` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetWebAuthUrl` |
| 52 | `GetWebAuthUrlEx` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.GetWebAuthUrlEx` |
| 23 | `HasPersistedCredential` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.HasPersistedCredential` |
| 1 | `Initialize` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.Initialize` |
| 61 | `InitializeApp` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.InitializeApp` |
| 29 | `InitializeEx` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.InitializeEx` |
| 93 | `InitializeIDCRLTraceBuffer` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.InitializeIDCRLTraceBuffer` |
| 69 | `IsDeviceIDAdmin` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.IsDeviceIDAdmin` |
| 95 | `IsMappedError` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.IsMappedError` |
| 21 | `LogonIdentity` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.LogonIdentity` |
| 31 | `LogonIdentityEx` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.LogonIdentityEx` |
| 108 | `LogonIdentityExSSO` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.LogonIdentityExSSO` |
| 75 | `LogonIdentityExWithUI` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.LogonIdentityExWithUI` |
| 18 | `NextIdentity` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.NextIdentity` |
| 74 | `OpenAuthenticatedBrowser` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.OpenAuthenticatedBrowser` |
| 3 | `PassportFreeMemory` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.PassportFreeMemory` |
| 15 | `PersistCredential` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.PersistCredential` |
| 98 | `ProvisionDeviceId` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.ProvisionDeviceId` |
| 58 | `RemoveChangeNotificationCallback` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.RemoveChangeNotificationCallback` |
| 16 | `RemovePersistedCredential` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.RemovePersistedCredential` |
| 116 | `RemoveUserFromSsoGroup` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.RemoveUserFromSsoGroup` |
| 100 | `RenewDeviceId` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.RenewDeviceId` |
| 117 | `SendOneTimeCode` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.SendOneTimeCode` |
| 57 | `SetChangeNotificationCallback` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.SetChangeNotificationCallback` |
| 5 | `SetCredential` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.SetCredential` |
| 81 | `SetDefaultUserForTarget` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.SetDefaultUserForTarget` |
| 65 | `SetDeviceConsent` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.SetDeviceConsent` |
| 47 | `SetExtendedProperty` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.SetExtendedProperty` |
| 79 | `SetHIPSolution` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.SetHIPSolution` |
| 51 | `SetIdcrlOptions` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.SetIdcrlOptions` |
| 24 | `SetIdentityCallback` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.SetIdentityCallback` |
| 7 | `SetIdentityProperty` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.SetIdentityProperty` |
| 55 | `SetUserExtendedProperty` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.SetUserExtendedProperty` |
| 110 | `StartTracing` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.StartTracing` |
| 111 | `StopTracing` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.StopTracing` |
| 83 | `UICollectCredential` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.UICollectCredential` |
| 92 | `UIEndWaitDialog` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.UIEndWaitDialog` |
| 91 | `UIShowWaitDialog` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.UIShowWaitDialog` |
| 102 | `UnPackErrorBlob` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.UnPackErrorBlob` |
| 2 | `Uninitialize` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.Uninitialize` |
| 87 | `UpdateUserAssociatedDeviceProperties` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.UpdateUserAssociatedDeviceProperties` |
| 73 | `VerifyAssertion` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.VerifyAssertion` |
| 40 | `VerifyCertificate` | `0x0` | - | Forwarded | Forwarded to: `wlidcli.VerifyCertificate` |
