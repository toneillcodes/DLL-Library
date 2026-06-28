# Binary Specification: schannel.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\schannel.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6f80de9c3055dd724d56d33e7f189ca0216eae55fd19802bea23a2093db04c46`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AcceptSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.AcceptSecurityContext` |
| 2 | `AcquireCredentialsHandleA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.AcquireCredentialsHandleA` |
| 3 | `AcquireCredentialsHandleW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.AcquireCredentialsHandleW` |
| 4 | `ApplyControlToken` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.ApplyControlToken` |
| 5 | `CompleteAuthToken` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.CompleteAuthToken` |
| 6 | `DeleteSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.DeleteSecurityContext` |
| 7 | `EnumerateSecurityPackagesA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.EnumerateSecurityPackagesA` |
| 8 | `EnumerateSecurityPackagesW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.EnumerateSecurityPackagesW` |
| 9 | `FreeContextBuffer` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.FreeContextBuffer` |
| 10 | `FreeCredentialsHandle` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.FreeCredentialsHandle` |
| 11 | `ImpersonateSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.ImpersonateSecurityContext` |
| 12 | `InitSecurityInterfaceA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.InitSecurityInterfaceA` |
| 13 | `InitSecurityInterfaceW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.InitSecurityInterfaceW` |
| 14 | `InitializeSecurityContextA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.InitializeSecurityContextA` |
| 15 | `InitializeSecurityContextW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.InitializeSecurityContextW` |
| 16 | `MakeSignature` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.MakeSignature` |
| 17 | `QueryContextAttributesA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.QueryContextAttributesA` |
| 18 | `QueryContextAttributesW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.QueryContextAttributesW` |
| 19 | `QuerySecurityPackageInfoA` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.QuerySecurityPackageInfoA` |
| 20 | `QuerySecurityPackageInfoW` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.QuerySecurityPackageInfoW` |
| 21 | `RevertSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.RevertSecurityContext` |
| 22 | `SealMessage` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.SealMessage` |
| 36 | `UnsealMessage` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.UnsealMessage` |
| 37 | `VerifySignature` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.VerifySignature` |
| 24 | `SpUserModeInitialize` | `0x4A450` | 130 | UnwindData |  |
| 26 | `SslDeserializeCertificateStore` | `0x4B1A0` | 43 | UnwindData |  |
| 35 | `SslLoadCertificate` | `0x56210` | 96,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `SslFreeCustomBuffer` | `0x6DBD0` | 184 | UnwindData |  |
| 25 | `SslCrackCertificate` | `0x6F360` | 711 | UnwindData |  |
| 29 | `SslFreeCertificate` | `0x6F630` | 37 | UnwindData |  |
| 31 | `SslGenerateRandomBits` | `0x6F660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `SslGetMaximumKeySize` | `0x6F670` | 23,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `SpLsaModeInitialize` | `0x752F0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `SslEmptyCacheA` | `0x753A0` | 159 | UnwindData |  |
| 28 | `SslEmptyCacheW` | `0x75450` | 418 | UnwindData |  |
| 32 | `SslGetExtensions` | `0x78100` | 288 | UnwindData |  |
| 34 | `SslGetServerIdentity` | `0x785E0` | 325 | UnwindData |  |
