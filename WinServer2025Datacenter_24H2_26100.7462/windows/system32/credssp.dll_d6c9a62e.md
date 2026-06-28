# Binary Specification: credssp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\credssp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d6c9a62ed07db26ebc12ec818e5dc5875720b115e33434a8055d89dc413b57b1`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `InitSecurityInterfaceW` | `0x19F0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SpAcceptSecurityContext` | `0x1B90` | 1,378 | UnwindData |  |
| 3 | `SpAcquireCredentialsHandleW` | `0x2100` | 636 | UnwindData |  |
| 4 | `SpAddCredentialsW` | `0x2390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SpChangeAccountPasswordW` | `0x2390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SpCompleteAuthToken` | `0x2390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SpExportSecurityContext` | `0x2390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SpImportSecurityContextW` | `0x2390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `SpQueryCredentialsAttributesW` | `0x2390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `SpSetContextAttributesW` | `0x2390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SpApplyControlToken` | `0x23A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SpDecryptMessage` | `0x23D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SpDeleteSecurityContext` | `0x2400` | 261 | UnwindData |  |
| 10 | `SpEncryptMessage` | `0x2510` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `SpEnumerateSecurityPackagesW` | `0x2540` | 60 | UnwindData |  |
| 13 | `SpFreeContextBuffer` | `0x2590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `SpFreeCredentialsHandle` | `0x25B0` | 119 | UnwindData |  |
| 15 | `SpImpersonateSecurityContext` | `0x2630` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SpInitializeSecurityContextW` | `0x2660` | 2,464 | UnwindData |  |
| 18 | `SpMakeSignature` | `0x3010` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `SpQueryContextAttributesW` | `0x3040` | 156 | UnwindData |  |
| 21 | `SpQuerySecurityContextToken` | `0x30F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `SpQuerySecurityPackageInfoW` | `0x3120` | 68 | UnwindData |  |
| 23 | `SpRevertSecurityContext` | `0x3170` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `SpSetCredentialsAttributesW` | `0x31A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `SpVerifySignature` | `0x31D0` | 832 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
