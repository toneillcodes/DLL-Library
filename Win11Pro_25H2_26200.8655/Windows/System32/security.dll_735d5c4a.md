# Binary Specification: security.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\security.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `735d5c4a10b02553a3ebd09e3d03507c522b20e72d94e505c43805c7ef2ffaf9`
* **Total Exported Functions:** 36

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AcceptSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.AcceptSecurityContext` |
| 2 | `AcquireCredentialsHandleA` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.AcquireCredentialsHandleA` |
| 3 | `AcquireCredentialsHandleW` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.AcquireCredentialsHandleW` |
| 4 | `AddSecurityPackageA` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.AddSecurityPackageA` |
| 5 | `AddSecurityPackageW` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.AddSecurityPackageW` |
| 6 | `ApplyControlToken` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.ApplyControlToken` |
| 7 | `CompleteAuthToken` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.CompleteAuthToken` |
| 8 | `DecryptMessage` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.DecryptMessage` |
| 9 | `DeleteSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.DeleteSecurityContext` |
| 10 | `DeleteSecurityPackageA` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.DeleteSecurityPackageA` |
| 11 | `DeleteSecurityPackageW` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.DeleteSecurityPackageW` |
| 12 | `EncryptMessage` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.EncryptMessage` |
| 13 | `EnumerateSecurityPackagesA` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.EnumerateSecurityPackagesA` |
| 14 | `EnumerateSecurityPackagesW` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.EnumerateSecurityPackagesW` |
| 15 | `ExportSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.ExportSecurityContext` |
| 16 | `FreeContextBuffer` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.FreeContextBuffer` |
| 17 | `FreeCredentialsHandle` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.FreeCredentialsHandle` |
| 18 | `ImpersonateSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.ImpersonateSecurityContext` |
| 19 | `ImportSecurityContextA` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.ImportSecurityContextA` |
| 20 | `ImportSecurityContextW` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.ImportSecurityContextW` |
| 21 | `InitSecurityInterfaceA` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.InitSecurityInterfaceA` |
| 22 | `InitSecurityInterfaceW` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.InitSecurityInterfaceW` |
| 23 | `InitializeSecurityContextA` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.InitializeSecurityContextA` |
| 24 | `InitializeSecurityContextW` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.InitializeSecurityContextW` |
| 25 | `MakeSignature` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.MakeSignature` |
| 26 | `QueryContextAttributesA` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.QueryContextAttributesA` |
| 27 | `QueryContextAttributesW` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.QueryContextAttributesW` |
| 28 | `QueryCredentialsAttributesA` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.QueryCredentialsAttributesA` |
| 29 | `QueryCredentialsAttributesW` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.QueryCredentialsAttributesW` |
| 30 | `QuerySecurityContextToken` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.QuerySecurityContextToken` |
| 31 | `QuerySecurityPackageInfoA` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.QuerySecurityPackageInfoA` |
| 32 | `QuerySecurityPackageInfoW` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.QuerySecurityPackageInfoW` |
| 33 | `RevertSecurityContext` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.RevertSecurityContext` |
| 34 | `SealMessage` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.EncryptMessage` |
| 35 | `UnsealMessage` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.DecryptMessage` |
| 36 | `VerifySignature` | `0x0` | - | Forwarded | Forwarded to: `SECUR32.VerifySignature` |
