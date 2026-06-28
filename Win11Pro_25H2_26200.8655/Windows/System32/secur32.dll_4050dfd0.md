# Binary Specification: secur32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\secur32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4050dfd0d4e04e8d013cb16c09d90c2177e2b7e4f102f5931187b2bd0c9d14fc`
* **Total Exported Functions:** 98

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AcceptSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.AcceptSecurityContext` |
| 2 | `AcquireCredentialsHandleA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.AcquireCredentialsHandleA` |
| 3 | `AcquireCredentialsHandleW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.AcquireCredentialsHandleW` |
| 4 | `AddCredentialsA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.AddCredentialsA` |
| 5 | `AddCredentialsW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.AddCredentialsW` |
| 6 | `AddSecurityPackageA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.AddSecurityPackageA` |
| 7 | `AddSecurityPackageW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.AddSecurityPackageW` |
| 8 | `ApplyControlToken` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.ApplyControlToken` |
| 9 | `ChangeAccountPasswordA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.ChangeAccountPasswordA` |
| 10 | `ChangeAccountPasswordW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.ChangeAccountPasswordW` |
| 11 | `CompleteAuthToken` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.CompleteAuthToken` |
| 12 | `CredMarshalTargetInfo` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.CredMarshalTargetInfo` |
| 13 | `CredUnmarshalTargetInfo` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.CredUnmarshalTargetInfo` |
| 14 | `DecryptMessage` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.DecryptMessage` |
| 15 | `DeleteSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.DeleteSecurityContext` |
| 16 | `DeleteSecurityPackageA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.DeleteSecurityPackageA` |
| 17 | `DeleteSecurityPackageW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.DeleteSecurityPackageW` |
| 18 | `EncryptMessage` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.EncryptMessage` |
| 19 | `EnumerateSecurityPackagesA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.EnumerateSecurityPackagesA` |
| 20 | `EnumerateSecurityPackagesW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.EnumerateSecurityPackagesW` |
| 21 | `ExportSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.ExportSecurityContext` |
| 22 | `FreeContextBuffer` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.FreeContextBuffer` |
| 23 | `FreeCredentialsHandle` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.FreeCredentialsHandle` |
| 26 | `GetSecurityUserInfo` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.GetSecurityUserInfo` |
| 27 | `GetUserNameExA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.GetUserNameExA` |
| 28 | `GetUserNameExW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.GetUserNameExW` |
| 29 | `ImpersonateSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.ImpersonateSecurityContext` |
| 30 | `ImportSecurityContextA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.ImportSecurityContextA` |
| 31 | `ImportSecurityContextW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.ImportSecurityContextW` |
| 32 | `InitSecurityInterfaceA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.InitSecurityInterfaceA` |
| 33 | `InitSecurityInterfaceW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.InitSecurityInterfaceW` |
| 34 | `InitializeSecurityContextA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.InitializeSecurityContextA` |
| 35 | `InitializeSecurityContextW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.InitializeSecurityContextW` |
| 36 | `LsaCallAuthenticationPackage` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.LsaCallAuthenticationPackage` |
| 37 | `LsaConnectUntrusted` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.LsaConnectUntrusted` |
| 38 | `LsaDeregisterLogonProcess` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.LsaDeregisterLogonProcess` |
| 39 | `LsaEnumerateLogonSessions` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.LsaEnumerateLogonSessions` |
| 40 | `LsaFreeReturnBuffer` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.LsaFreeReturnBuffer` |
| 41 | `LsaGetLogonSessionData` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.LsaGetLogonSessionData` |
| 42 | `LsaLogonUser` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.LsaLogonUser` |
| 43 | `LsaLookupAuthenticationPackage` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.LsaLookupAuthenticationPackage` |
| 44 | `LsaRegisterLogonProcess` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.LsaRegisterLogonProcess` |
| 45 | `LsaRegisterPolicyChangeNotification` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.LsaRegisterPolicyChangeNotification` |
| 46 | `LsaUnregisterPolicyChangeNotification` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.LsaUnregisterPolicyChangeNotification` |
| 47 | `MakeSignature` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.MakeSignature` |
| 48 | `QueryContextAttributesA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.QueryContextAttributesA` |
| 49 | `QueryContextAttributesW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.QueryContextAttributesW` |
| 50 | `QueryCredentialsAttributesA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.QueryCredentialsAttributesA` |
| 51 | `QueryCredentialsAttributesW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.QueryCredentialsAttributesW` |
| 52 | `QuerySecurityContextToken` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.QuerySecurityContextToken` |
| 53 | `QuerySecurityPackageInfoA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.QuerySecurityPackageInfoA` |
| 54 | `QuerySecurityPackageInfoW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.QuerySecurityPackageInfoW` |
| 55 | `RevertSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.RevertSecurityContext` |
| 56 | `SaslAcceptSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SaslAcceptSecurityContext` |
| 57 | `SaslEnumerateProfilesA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SaslEnumerateProfilesA` |
| 58 | `SaslEnumerateProfilesW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SaslEnumerateProfilesW` |
| 59 | `SaslGetContextOption` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SaslGetContextOption` |
| 60 | `SaslGetProfilePackageA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SaslGetProfilePackageA` |
| 61 | `SaslGetProfilePackageW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SaslGetProfilePackageW` |
| 62 | `SaslIdentifyPackageA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SaslIdentifyPackageA` |
| 63 | `SaslIdentifyPackageW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SaslIdentifyPackageW` |
| 64 | `SaslInitializeSecurityContextA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SaslInitializeSecurityContextA` |
| 65 | `SaslInitializeSecurityContextW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SaslInitializeSecurityContextW` |
| 66 | `SaslSetContextOption` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SaslSetContextOption` |
| 67 | `SealMessage` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SealMessage` |
| 68 | `SeciAllocateAndSetCallFlags` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SeciAllocateAndSetCallFlags` |
| 69 | `SeciAllocateAndSetIPAddress` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SeciAllocateAndSetIPAddress` |
| 70 | `SeciFreeCallContext` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SeciFreeCallContext` |
| 74 | `SetContextAttributesA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SetContextAttributesA` |
| 75 | `SetContextAttributesW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SetContextAttributesW` |
| 76 | `SetCredentialsAttributesA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SetCredentialsAttributesA` |
| 77 | `SetCredentialsAttributesW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SetCredentialsAttributesW` |
| 78 | `SspiCompareAuthIdentities` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiCompareAuthIdentities` |
| 79 | `SspiCopyAuthIdentity` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiCopyAuthIdentity` |
| 80 | `SspiDecryptAuthIdentity` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiDecryptAuthIdentity` |
| 81 | `SspiEncodeAuthIdentityAsStrings` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiEncodeAuthIdentityAsStrings` |
| 82 | `SspiEncodeStringsAsAuthIdentity` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiEncodeStringsAsAuthIdentity` |
| 83 | `SspiEncryptAuthIdentity` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiEncryptAuthIdentity` |
| 84 | `SspiExcludePackage` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiExcludePackage` |
| 85 | `SspiFreeAuthIdentity` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiFreeAuthIdentity` |
| 86 | `SspiGetTargetHostName` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiGetTargetHostName` |
| 87 | `SspiIsAuthIdentityEncrypted` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiIsAuthIdentityEncrypted` |
| 88 | `SspiLocalFree` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiLocalFree` |
| 89 | `SspiMarshalAuthIdentity` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiMarshalAuthIdentity` |
| 90 | `SspiPrepareForCredRead` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiPrepareForCredRead` |
| 91 | `SspiPrepareForCredWrite` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiPrepareForCredWrite` |
| 92 | `SspiUnmarshalAuthIdentity` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiUnmarshalAuthIdentity` |
| 93 | `SspiValidateAuthIdentity` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiValidateAuthIdentity` |
| 94 | `SspiZeroAuthIdentity` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SspiZeroAuthIdentity` |
| 97 | `UnsealMessage` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.UnsealMessage` |
| 98 | `VerifySignature` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.VerifySignature` |
| 25 | `GetComputerObjectNameW` | `0x1040` | 296 | UnwindData |  |
| 73 | `SecpTranslateNameEx` | `0x1490` | 173 | UnwindData |  |
| 96 | `TranslateNameW` | `0x1C20` | 72 | UnwindData |  |
| 72 | `SecpTranslateName` | `0x1C70` | 262 | UnwindData |  |
| 95 | `TranslateNameA` | `0x2950` | 146 | UnwindData |  |
| 71 | `SecpFreeMemory` | `0x2B30` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `GetComputerObjectNameA` | `0x3120` | 349 | UnwindData |  |
