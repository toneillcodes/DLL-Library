# Binary Specification: cmlua.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cmlua.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `42fc635ccde06cd2ea618be236d8113b5bfe1ef865d64a30c2e972c6179a5786`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllAddRef` | `0x1A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x1A80` | 53 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x1AC0` | 124 | UnwindData |  |
| 4 | `DllMain` | `0x1B50` | 32 | UnwindData |  |
| 5 | `DllRelease` | `0x1B80` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `_GetCoCreateInstanceAsAdminHandle` | `0x1C10` | 279 | UnwindData |  |
| 7 | `_RemoveShieldIcon` | `0x1D30` | 55 | UnwindData |  |
| 8 | `_SetShieldButton` | `0x1D70` | 35 | UnwindData |  |
| 9 | `_SetShieldIcon` | `0x1DA0` | 157 | UnwindData |  |
| 10 | `_ThrowErrorBox` | `0x1E50` | 130 | UnwindData |  |
