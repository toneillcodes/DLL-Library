# Binary Specification: srpapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\srpapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `700e52b3a6b7edcb62d7243c913b4529f05e869a6c8d56d49d11d7b6e64c73d3`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `SrpCloseThreadNetworkContext` | `0x2560` | 127 | UnwindData |  |
| 7 | `SrpCreateThreadNetworkContext` | `0x25F0` | 129 | UnwindData |  |
| 8 | `SrpDisablePermissiveModeFileEncryption` | `0x2680` | 26 | UnwindData |  |
| 9 | `SrpDoesPolicyAllowAppExecution` | `0x26A0` | 205 | UnwindData |  |
| 10 | `SrpEnablePermissiveModeFileEncryption` | `0x2780` | 29 | UnwindData |  |
| 13 | `SrpGetEnterpriseIds` | `0x27B0` | 283 | UnwindData |  |
| 14 | `SrpGetEnterprisePolicy` | `0x28E0` | 135 | UnwindData |  |
| 15 | `SrpHostingInitialize` | `0x2970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SrpHostingTerminate` | `0x2980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SrpInheritEnterpriseContext` | `0x2990` | 58 | UnwindData |  |
| 22 | `SrpRestoreEnterpriseContext` | `0x29D0` | 75 | UnwindData |  |
| 23 | `SrpSetTokenEnterpriseId` | `0x2A30` | 201 | UnwindData |  |
| 1 | `AiEvaluatePlugin` | `0x7240` | 307 | UnwindData |  |
| 2 | `AppIDDecodeAttributeString` | `0x73A0` | 201 | UnwindData |  |
| 3 | `AppIDEncodeAttributeString` | `0x7470` | 205 | UnwindData |  |
| 4 | `AppIDFreeAttributeString` | `0x7550` | 20 | UnwindData |  |
| 6 | `SrpCloseTrackInstall` | `0x76A0` | 114 | UnwindData |  |
| 11 | `SrpGetAllowedEnterprises` | `0x7720` | 957 | UnwindData |  |
| 12 | `SrpGetAppxFqbnFromPackageFullName` | `0x7AF0` | 392 | UnwindData |  |
| 18 | `SrpInheritOriginClaim` | `0x7C80` | 338 | UnwindData |  |
| 19 | `SrpIsAllowed` | `0x7E60` | 2,594 | UnwindData |  |
| 21 | `SrpOpenTrackInstall` | `0x8890` | 117 | UnwindData |  |
| 20 | `SrpIsTokenService` | `0x8DC0` | 199 | UnwindData |  |
