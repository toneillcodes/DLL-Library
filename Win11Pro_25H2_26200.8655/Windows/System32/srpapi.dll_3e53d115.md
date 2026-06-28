# Binary Specification: srpapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\srpapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3e53d115e872020ecf0a0d41e2fa4aba005d6d26a720d7888578cbfbf52758cd`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `SrpCloseThreadNetworkContext` | `0x26A0` | 127 | UnwindData |  |
| 7 | `SrpCreateThreadNetworkContext` | `0x2730` | 129 | UnwindData |  |
| 8 | `SrpDisablePermissiveModeFileEncryption` | `0x27C0` | 26 | UnwindData |  |
| 9 | `SrpDoesPolicyAllowAppExecution` | `0x27E0` | 205 | UnwindData |  |
| 10 | `SrpEnablePermissiveModeFileEncryption` | `0x28C0` | 29 | UnwindData |  |
| 13 | `SrpGetEnterpriseIds` | `0x28F0` | 283 | UnwindData |  |
| 14 | `SrpGetEnterprisePolicy` | `0x2A20` | 135 | UnwindData |  |
| 15 | `SrpHostingInitialize` | `0x2AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SrpHostingTerminate` | `0x2AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SrpInheritEnterpriseContext` | `0x2AD0` | 58 | UnwindData |  |
| 22 | `SrpRestoreEnterpriseContext` | `0x2B10` | 75 | UnwindData |  |
| 23 | `SrpSetTokenEnterpriseId` | `0x2B70` | 201 | UnwindData |  |
| 1 | `AiEvaluatePlugin` | `0xC1E0` | 307 | UnwindData |  |
| 2 | `AppIDDecodeAttributeString` | `0xC340` | 201 | UnwindData |  |
| 3 | `AppIDEncodeAttributeString` | `0xC410` | 205 | UnwindData |  |
| 4 | `AppIDFreeAttributeString` | `0xC4F0` | 20 | UnwindData |  |
| 6 | `SrpCloseTrackInstall` | `0xC640` | 114 | UnwindData |  |
| 11 | `SrpGetAllowedEnterprises` | `0xC6C0` | 957 | UnwindData |  |
| 12 | `SrpGetAppxFqbnFromPackageFullName` | `0xCA90` | 392 | UnwindData |  |
| 18 | `SrpInheritOriginClaim` | `0xCC20` | 338 | UnwindData |  |
| 19 | `SrpIsAllowed` | `0xCE00` | 3,689 | UnwindData |  |
| 21 | `SrpOpenTrackInstall` | `0xDC70` | 117 | UnwindData |  |
| 20 | `SrpIsTokenService` | `0xEAA0` | 199 | UnwindData |  |
