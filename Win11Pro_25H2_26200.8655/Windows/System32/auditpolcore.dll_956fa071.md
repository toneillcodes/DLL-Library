# Binary Specification: auditpolcore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\auditpolcore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `956fa071b0a8c3278930809ff1d21b31896e23cac7f7cd289b1172341ed2e1b0`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AdtBackupPolicy` | `0x3F90` | 398 | UnwindData |  |
| 2 | `AdtBackupPolicyGeneralized` | `0x4130` | 53 | UnwindData |  |
| 3 | `AdtClearPolicy` | `0x4550` | 389 | UnwindData |  |
| 9 | `AdtGetOption` | `0x4700` | 735 | UnwindData |  |
| 10 | `AdtGetPerUserPolicy` | `0x49F0` | 146 | UnwindData |  |
| 11 | `AdtGetSystemPolicy` | `0x4AB0` | 129 | UnwindData |  |
| 17 | `AdtRemoveAllUsers` | `0x4B40` | 122 | UnwindData |  |
| 18 | `AdtRemoveBasePolicy` | `0x4BC0` | 583 | UnwindData |  |
| 19 | `AdtRestorePolicy` | `0x4E10` | 1,024 | UnwindData |  |
| 20 | `AdtRestorePolicyGeneralized` | `0x5220` | 47 | UnwindData |  |
| 21 | `AdtSetOption` | `0x5260` | 179 | UnwindData |  |
| 22 | `AdtSetPerUserPolicy` | `0x5320` | 211 | UnwindData |  |
| 23 | `AdtSetSystemPolicy` | `0x5400` | 201 | UnwindData |  |
| 4 | `AdtConstructAllCategoryGuids` | `0x8050` | 169 | UnwindData |  |
| 5 | `AdtConvertGuidStringToGuid` | `0x8100` | 115 | UnwindData |  |
| 6 | `AdtConvertGuidToString` | `0x8180` | 198 | UnwindData |  |
| 7 | `AdtDisableSinglePrivilege` | `0x8250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `AdtEnableSinglePrivilege` | `0x8260` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `AdtListCategories` | `0x8340` | 371 | UnwindData |  |
| 13 | `AdtListSubCategories` | `0x84C0` | 520 | UnwindData |  |
| 14 | `AdtLoadStringEx` | `0x86D0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `AdtParseAuditOptionName` | `0x87F0` | 165 | UnwindData |  |
| 16 | `AdtParseGuidOrNameArray` | `0x88A0` | 844 | UnwindData |  |
| 24 | `AuditPolicyData_DeleteAuditDataInstance` | `0xAA70` | 56 | UnwindData |  |
| 25 | `DisplayMessage` | `0xAC20` | 73 | UnwindData |  |
| 26 | `DisplayMessageToSpecificConsoleHandle` | `0xAC70` | 34 | UnwindData |  |
| 27 | `GetDisplayPolicy` | `0xACA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `LoadFormatStringAndPrintToConsole` | `0xACB0` | 184 | UnwindData |  |
| 29 | `SetDisplayPolicy` | `0xAD70` | 7,874 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
