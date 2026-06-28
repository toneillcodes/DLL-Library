# Binary Specification: RpcRtRemote.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\RpcRtRemote.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `26c0090323ef0869b0aed894406e0e2e31e5ba3a52d200cdf1e115446a4be9bb`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `IndicatePortInUse` | `0x1CE0` | 47 | UnwindData |  |
| 9 | `ResetIndicatedPortsInUse` | `0x2950` | 38 | UnwindData |  |
| 1 | `DuplicateCertificate` | `0x2980` | 59 | UnwindData |  |
| 2 | `FreeCertificate` | `0x29D0` | 24 | UnwindData |  |
| 3 | `GeneratePrincipalName` | `0x29F0` | 29 | UnwindData |  |
| 6 | `IsMarshaledCredential` | `0x2A20` | 32 | UnwindData |  |
| 7 | `MatchPrincipalName` | `0x2A50` | 29 | UnwindData |  |
| 8 | `ProcessAndProvisionCertificate` | `0x2A80` | 62 | UnwindData |  |
| 10 | `ValidatePrincipalName` | `0x2AD0` | 29 | UnwindData |  |
| 4 | `I_RpcExtInitializeExtensionPoint` | `0x2C80` | 22,330 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
