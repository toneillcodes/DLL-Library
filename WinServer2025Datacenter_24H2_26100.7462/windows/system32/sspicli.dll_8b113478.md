# Binary Specification: sspicli.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sspicli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8b1134784d8babc6ef24569abba93e20917679c51cd777de972bdc6fee2fca22`
* **Total Exported Functions:** 111

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `AcceptSecurityContext` | `0x14C0` | 1,051 | UnwindData |  |
| 51 | `MakeSignature` | `0x18F0` | 146 | UnwindData |  |
| 111 | `VerifySignature` | `0x1990` | 148 | UnwindData |  |
| 60 | `QuerySecurityContextToken` | `0x1A30` | 165 | UnwindData |  |
| 63 | `RevertSecurityContext` | `0x1AE0` | 124 | UnwindData |  |
| 30 | `ImpersonateSecurityContext` | `0x1B70` | 124 | UnwindData |  |
| 11 | `ApplyControlToken` | `0x1C00` | 139 | UnwindData |  |
| 52 | `QueryContextAttributesA` | `0x1CA0` | 138 | UnwindData |  |
| 59 | `QueryCredentialsAttributesW` | `0x1D30` | 156 | UnwindData |  |
| 58 | `QueryCredentialsAttributesExW` | `0x1DE0` | 175 | UnwindData |  |
| 86 | `SetContextAttributesW` | `0x1EA0` | 178 | UnwindData |  |
| 35 | `InitializeSecurityContextA` | `0x1F60` | 118 | UnwindData |  |
| 36 | `InitializeSecurityContextW` | `0x1FE0` | 118 | UnwindData |  |
| 26 | `FreeCredentialsHandle` | `0x2950` | 121 | UnwindData |  |
| 55 | `QueryContextAttributesW` | `0x29D0` | 138 | UnwindData |  |
| 18 | `DeleteSecurityContext` | `0x2A60` | 223 | UnwindData |  |
| 54 | `QueryContextAttributesExW` | `0x2B50` | 178 | UnwindData |  |
| 53 | `QueryContextAttributesExA` | `0x2C10` | 185 | UnwindData |  |
| 17 | `DecryptMessage` | `0x2CD0` | 151 | UnwindData |  |
| 110 | `UnsealMessage` | `0x2CD0` | 151 | UnwindData |  |
| 21 | `EncryptMessage` | `0x2D70` | 149 | UnwindData |  |
| 75 | `SealMessage` | `0x2D70` | 149 | UnwindData |  |
| 62 | `QuerySecurityPackageInfoW` | `0x3650` | 59 | UnwindData |  |
| 5 | `AcquireCredentialsHandleA` | `0x36A0` | 83 | UnwindData |  |
| 6 | `AcquireCredentialsHandleW` | `0x3700` | 83 | UnwindData |  |
| 23 | `EnumerateSecurityPackagesW` | `0x4D00` | 158 | UnwindData |  |
| 43 | `LsaFreeReturnBuffer` | `0x5DE0` | 164 | UnwindData |  |
| 29 | `GetUserNameExW` | `0x9770` | 312 | UnwindData |  |
| 44 | `LsaGetLogonSessionData` | `0xAD10` | 64 | UnwindData |  |
| 42 | `LsaEnumerateLogonSessions` | `0xAD60` | 52 | UnwindData |  |
| 46 | `LsaLookupAuthenticationPackage` | `0xB380` | 217 | UnwindData |  |
| 40 | `LsaConnectUntrusted` | `0xB640` | 435 | UnwindData |  |
| 37 | `LogonUserExExW` | `0xBA80` | 1,144 | UnwindData |  |
| 45 | `LsaLogonUser` | `0xC480` | 137 | UnwindData |  |
| 25 | `FreeContextBuffer` | `0xC960` | 93 | UnwindData |  |
| 16 | `CredUnmarshalTargetInfo` | `0xE030` | 1,530 | UnwindData |  |
| 96 | `SspiEncryptAuthIdentityEx` | `0xED00` | 634 | UnwindData |  |
| 3 | `SspiUnmarshalAuthIdentityInternal` | `0xEF80` | 1,112 | UnwindData |  |
| 92 | `SspiDecryptAuthIdentityEx` | `0xF3E0` | 475 | UnwindData |  |
| 90 | `SspiCopyAuthIdentity` | `0xF5D0` | 1,445 | UnwindData |  |
| 108 | `SspiValidateAuthIdentity` | `0xFB80` | 1,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `SeciIsProtectedUser` | `0x10040` | 631 | UnwindData |  |
| 79 | `SecFreeCallContext` | `0x10360` | 124 | UnwindData |  |
| 83 | `SeciFreeCallContext` | `0x10360` | 124 | UnwindData |  |
| 104 | `SspiPrepareForCredRead` | `0x10520` | 113 | UnwindData |  |
| 105 | `SspiPrepareForCredWrite` | `0x105A0` | 1,248 | UnwindData |  |
| 100 | `SspiGetTargetHostName` | `0x10A90` | 277 | UnwindData |  |
| 47 | `LsaRegisterLogonProcess` | `0x10F70` | 363 | UnwindData |  |
| 89 | `SspiCompareAuthIdentities` | `0x11110` | 655 | UnwindData |  |
| 93 | `SspiEncodeAuthIdentityAsStrings` | `0x113B0` | 3,164 | UnwindData |  |
| 34 | `InitSecurityInterfaceW` | `0x12100` | 52 | UnwindData |  |
| 109 | `SspiZeroAuthIdentity` | `0x123A0` | 93 | UnwindData |  |
| 41 | `LsaDeregisterLogonProcess` | `0x125E0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `SspiIsAuthIdentityEncrypted` | `0x127D0` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `LsaCallAuthenticationPackage` | `0x12C30` | 356 | UnwindData |  |
| 77 | `SecAllocateAndSetIPAddress` | `0x12DA0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `SeciAllocateAndSetIPAddress` | `0x12DA0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `SeciAllocateAndSetCallFlags` | `0x12F80` | 67 | UnwindData |  |
| 28 | `GetUserNameExA` | `0x12FD0` | 365 | UnwindData |  |
| 98 | `SspiFreeAuthIdentity` | `0x131F0` | 156 | UnwindData |  |
| 107 | `SspiUnmarshalAuthIdentity` | `0x13790` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `LsaRegisterPolicyChangeNotification` | `0x13D80` | 51 | UnwindData |  |
| 33 | `InitSecurityInterfaceA` | `0x13DC0` | 50 | UnwindData |  |
| 76 | `SecAllocateAndSetCallTarget` | `0x14180` | 280 | UnwindData |  |
| 81 | `SeciAllocateAndSetCallTarget` | `0x14180` | 280 | UnwindData |  |
| 50 | `LsaUnregisterPolicyChangeNotification` | `0x14320` | 51 | UnwindData |  |
| 91 | `SspiDecryptAuthIdentity` | `0x14560` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `SspiLocalFree` | `0x14A90` | 27 | UnwindData |  |
| 15 | `CredMarshalTargetInfo` | `0x15850` | 865 | UnwindData |  |
| 94 | `SspiEncodeStringsAsAuthIdentity` | `0x1C690` | 1,622 | UnwindData |  |
| 97 | `SspiExcludePackage` | `0x1CCF0` | 855 | UnwindData |  |
| 103 | `SspiMarshalAuthIdentity` | `0x1D050` | 756 | UnwindData |  |
| 106 | `SspiSetChannelBindingFlags` | `0x1D350` | 335 | UnwindData |  |
| 27 | `GetSecurityUserInfo` | `0x1D4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `AddSecurityPackageA` | `0x1D4C0` | 127 | UnwindData |  |
| 10 | `AddSecurityPackageW` | `0x1D550` | 95 | UnwindData |  |
| 19 | `DeleteSecurityPackageA` | `0x1D5C0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `DeleteSecurityPackageW` | `0x1D5C0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `SspiEncryptAuthIdentity` | `0x1D6C0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `SspiGetComputerNameForSPN` | `0x1D840` | 299 | UnwindData |  |
| 78 | `SecCacheSspiPackages` | `0x1E330` | 1,648 | UnwindData |  |
| 1 | `SecDeleteUserModeContext` | `0x200C0` | 113 | UnwindData |  |
| 2 | `SecInitUserModeContext` | `0x20140` | 169 | UnwindData |  |
| 7 | `AddCredentialsA` | `0x203B0` | 314 | UnwindData |  |
| 8 | `AddCredentialsW` | `0x204F0` | 314 | UnwindData |  |
| 12 | `ChangeAccountPasswordA` | `0x20630` | 68 | UnwindData |  |
| 13 | `ChangeAccountPasswordW` | `0x20680` | 68 | UnwindData |  |
| 14 | `CompleteAuthToken` | `0x206D0` | 139 | UnwindData |  |
| 22 | `EnumerateSecurityPackagesA` | `0x20770` | 158 | UnwindData |  |
| 24 | `ExportSecurityContext` | `0x20820` | 173 | UnwindData |  |
| 31 | `ImportSecurityContextA` | `0x208E0` | 220 | UnwindData |  |
| 32 | `ImportSecurityContextW` | `0x209D0` | 220 | UnwindData |  |
| 56 | `QueryCredentialsAttributesA` | `0x20AC0` | 156 | UnwindData |  |
| 57 | `QueryCredentialsAttributesExA` | `0x20B70` | 175 | UnwindData |  |
| 61 | `QuerySecurityPackageInfoA` | `0x20C30` | 54 | UnwindData |  |
| 85 | `SetContextAttributesA` | `0x20C70` | 178 | UnwindData |  |
| 87 | `SetCredentialsAttributesA` | `0x20D30` | 175 | UnwindData |  |
| 88 | `SetCredentialsAttributesW` | `0x20DF0` | 175 | UnwindData |  |
| 64 | `SaslAcceptSecurityContext` | `0x21870` | 600 | UnwindData |  |
| 65 | `SaslEnumerateProfilesA` | `0x21AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `SaslEnumerateProfilesW` | `0x21AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `SaslGetContextOption` | `0x21AF0` | 318 | UnwindData |  |
| 68 | `SaslGetProfilePackageA` | `0x21C40` | 111 | UnwindData |  |
| 69 | `SaslGetProfilePackageW` | `0x21CC0` | 81 | UnwindData |  |
| 70 | `SaslIdentifyPackageA` | `0x21D20` | 48 | UnwindData |  |
| 71 | `SaslIdentifyPackageW` | `0x21D60` | 48 | UnwindData |  |
| 72 | `SaslInitializeSecurityContextA` | `0x21DA0` | 442 | UnwindData |  |
| 73 | `SaslInitializeSecurityContextW` | `0x21F60` | 444 | UnwindData |  |
| 74 | `SaslSetContextOption` | `0x22130` | 264 | UnwindData |  |
| 39 | `LsaConnectLocalUser` | `0x22A60` | 357 | UnwindData |  |
| 49 | `LsaSetMachineCertificate` | `0x22BD0` | 354 | UnwindData |  |
