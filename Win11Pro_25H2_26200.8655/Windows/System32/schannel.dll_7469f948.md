# Binary Specification: schannel.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\schannel.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7469f9480e9345c278054a819ea1a56a4f9a710b81c6de5f890649a51b53807f`
* **Total Exported Functions:** 38

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
| 37 | `UnsealMessage` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.UnsealMessage` |
| 38 | `VerifySignature` | `0x0` | - | Forwarded | Forwarded to: `SSPICLI.VerifySignature` |
| 24 | `SpUserModeInitialize` | `0x45E80` | 130 | UnwindData |  |
| 27 | `SslDeserializeCertificateStore` | `0x46940` | 43 | UnwindData |  |
| 36 | `SslLoadCertificate` | `0x51FE0` | 80,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `SslFreeCustomBuffer` | `0x65C20` | 184 | UnwindData |  |
| 26 | `SslCrackCertificate` | `0x66C30` | 711 | UnwindData |  |
| 30 | `SslFreeCertificate` | `0x66F00` | 37 | UnwindData |  |
| 32 | `SslGenerateRandomBits` | `0x66F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `SslGetMaximumKeySize` | `0x66F40` | 43,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `SpLsaModeInitialize` | `0x71AB0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `SslEmptyCacheA` | `0x71B60` | 159 | UnwindData |  |
| 29 | `SslEmptyCacheW` | `0x71C10` | 418 | UnwindData |  |
| 25 | `SslCopyTlsExtensions` | `0x75820` | 565 | UnwindData |  |
| 33 | `SslGetExtensions` | `0x75E60` | 288 | UnwindData |  |
| 35 | `SslGetServerIdentity` | `0x76340` | 325 | UnwindData |  |
