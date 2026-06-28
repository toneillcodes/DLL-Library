# Binary Specification: Microsoft.Windows.Bcd.Utils.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WindowsPowerShell\v1.0\Modules\Microsoft.Windows.Bcd.Cmdlets\Microsoft.Windows.Bcd.Utils.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c4dc33f0fddbaada7a0726b3cbdecb1a89b034a0bd1a5f4a8780ec898eac564f`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `BcdUtilGetDebuggerStartPolicy` | `0x1740` | 152 | UnwindData |  |
| 2 | `BcdUtilGetDebuggerType` | `0x17E0` | 226 | UnwindData |  |
| 3 | `BcdUtilGetHypervisorDebuggerType` | `0x18D0` | 152 | UnwindData |  |
| 4 | `BcdUtilsGetElementAppliesTo` | `0x1970` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `BcdUtilsGetElementFriendlyName` | `0x19C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `BcdUtilsGetElementPolicyIndex` | `0x1A10` | 149 | UnwindData |  |
| 7 | `BcdUtilsGetElementPolicyString` | `0x1AB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `BcdUtilsGetElementTypeId` | `0x1B10` | 146 | UnwindData |  |
| 9 | `BcdUtilsGetNamedElements` | `0x1BB0` | 281 | UnwindData |  |
| 10 | `BcdUtilsGuidToString` | `0x1CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `BcdUtilsStringToGuid` | `0x1CE0` | 816 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
