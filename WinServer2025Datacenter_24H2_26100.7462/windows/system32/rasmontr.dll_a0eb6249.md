# Binary Specification: rasmontr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rasmontr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a0eb62496d95a87bef027f8aa2506a31fb5802688ed7bc152334ba20230aa910`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetDiagnosticFunctions` | `0x19600` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `InitHelperDll` | `0x196D0` | 221 | UnwindData |  |
| 3 | `RutlAlloc` | `0x1AC50` | 61 | UnwindData |  |
| 4 | `RutlAssignmentFromTokenAndDword` | `0x1AD30` | 147 | UnwindData |  |
| 5 | `RutlAssignmentFromTokens` | `0x1ADD0` | 148 | UnwindData |  |
| 6 | `RutlCloseDumpFile` | `0x1AE70` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `RutlCreateDumpFile` | `0x1AF30` | 128 | UnwindData |  |
| 8 | `RutlDwordDup` | `0x1AFC0` | 32 | UnwindData |  |
| 9 | `RutlFree` | `0x1B350` | 52 | UnwindData |  |
| 10 | `RutlGetOsVersion` | `0x1B390` | 298 | UnwindData |  |
| 11 | `RutlGetTagToken` | `0x1B4C0` | 721 | UnwindData |  |
| 12 | `RutlIsHelpToken` | `0x1B820` | 86 | UnwindData |  |
| 13 | `RutlParse` | `0x1B880` | 668 | UnwindData |  |
| 14 | `RutlStrDup` | `0x1BFB0` | 124 | UnwindData |  |
