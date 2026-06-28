# Binary Specification: dmcfgutils.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dmcfgutils.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7c36c073073730010d5b729ddeac18e78c8caa7669a4b658f0d323680667d940`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `CfgUtilCheckCharacteristicNode` | `0x4AA0` | 114 | UnwindData |  |
| 5 | `CfgUtilCheckParmNode` | `0x4B20` | 113 | UnwindData |  |
| 17 | `CfgUtilParseNameByLen` | `0x4BA0` | 195 | UnwindData |  |
| 16 | `CfgUtilParseName` | `0x4C70` | 67 | UnwindData |  |
| 11 | `CfgUtilGetName` | `0x4CC0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `CfgUtilParseElementName` | `0x4D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `CfgUtilGetElementName` | `0x4D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `CfgUtilParseParmAttributeName` | `0x4DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `CfgUtilGetParmAttributeName` | `0x4DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CfgUtilParseConfigDataTypeName` | `0x4DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CfgUtilGetConfigDataTypeName` | `0x4E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `CfgUtilParseConfigSemanticTypeName` | `0x4E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CfgUtilGetConfigSemanticTypeName` | `0x4E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CfgUtilCreateCharacteristic` | `0x4E70` | 161 | UnwindData |  |
| 7 | `CfgUtilCreateParm` | `0x4F20` | 205 | UnwindData |  |
| 2 | `EnsurePolicyComplianceForSource` | `0x5490` | 1,422 | UnwindData |  |
| 1 | `CleanupPolicyComplianceEnsuranceForSource` | `0x5A30` | 544 | UnwindData |  |
| 3 | `VerifyFullAdminPrivileges` | `0x105F0` | 372 | UnwindData |  |
| 19 | `SyncGetDeviceUniqueID` | `0x12230` | 587 | UnwindData |  |
