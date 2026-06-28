# Binary Specification: dmcfgutils.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dmcfgutils.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `15eaa7ed61dffdbfe37be03811fa71c673a6c61790e00bb16fbc491dda057023`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `CfgUtilCheckCharacteristicNode` | `0x4A90` | 114 | UnwindData |  |
| 5 | `CfgUtilCheckParmNode` | `0x4B10` | 113 | UnwindData |  |
| 17 | `CfgUtilParseNameByLen` | `0x4B90` | 195 | UnwindData |  |
| 16 | `CfgUtilParseName` | `0x4C60` | 67 | UnwindData |  |
| 11 | `CfgUtilGetName` | `0x4CB0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `CfgUtilParseElementName` | `0x4D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `CfgUtilGetElementName` | `0x4D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `CfgUtilParseParmAttributeName` | `0x4DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `CfgUtilGetParmAttributeName` | `0x4DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `CfgUtilParseConfigDataTypeName` | `0x4DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CfgUtilGetConfigDataTypeName` | `0x4E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `CfgUtilParseConfigSemanticTypeName` | `0x4E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CfgUtilGetConfigSemanticTypeName` | `0x4E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CfgUtilCreateCharacteristic` | `0x4E60` | 161 | UnwindData |  |
| 7 | `CfgUtilCreateParm` | `0x4F10` | 205 | UnwindData |  |
| 2 | `EnsurePolicyComplianceForSource` | `0x5480` | 1,422 | UnwindData |  |
| 1 | `CleanupPolicyComplianceEnsuranceForSource` | `0x5A20` | 544 | UnwindData |  |
| 3 | `VerifyFullAdminPrivileges` | `0x105E0` | 372 | UnwindData |  |
| 19 | `SyncGetDeviceUniqueID` | `0x12220` | 587 | UnwindData |  |
