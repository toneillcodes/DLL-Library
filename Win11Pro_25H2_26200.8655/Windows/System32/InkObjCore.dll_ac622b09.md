# Binary Specification: InkObjCore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\InkObjCore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ac622b090160088b1d06607230ab8bacebf630a475de12463951256593d2a10d`
* **Total Exported Functions:** 35

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 25 | `LoadCachedAttributes` | `0x26A10` | 602 | UnwindData |  |
| 11 | `DllGetClassObject` | `0x2EB80` | 60,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `DllCanUnloadNow` | `0x3D800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllRegisterServer` | `0x3D820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DllUnregisterServer` | `0x3D830` | 132 | UnwindData |  |
| 23 | `InvokeIDispatch` | `0x3D8C0` | 75 | UnwindData |  |
| 1 | `AddStroke` | `0x422F0` | 197 | UnwindData |  |
| 2 | `AddStrokeWithId` | `0x423C0` | 227 | UnwindData |  |
| 3 | `AddWordsToWordList` | `0x424B0` | 165 | UnwindData |  |
| 4 | `AdviseInkChange` | `0x42560` | 163 | UnwindData |  |
| 5 | `CreateContext` | `0x42610` | 237 | UnwindData |  |
| 6 | `CreateRecognizer` | `0x42710` | 82 | UnwindData |  |
| 7 | `DestroyContext` | `0x42770` | 196 | UnwindData |  |
| 8 | `DestroyRecognizer` | `0x42840` | 192 | UnwindData |  |
| 9 | `DestroyWordList` | `0x42910` | 201 | UnwindData |  |
| 14 | `EndInkInput` | `0x429E0` | 149 | UnwindData |  |
| 15 | `GetAllRecognizers` | `0x42A80` | 953 | UnwindData |  |
| 16 | `GetBestResultString` | `0x42E40` | 167 | UnwindData |  |
| 17 | `GetLatticePtr` | `0x42EF0` | 165 | UnwindData |  |
| 18 | `GetLeftSeparator` | `0x42FA0` | 180 | UnwindData |  |
| 19 | `GetRecoAttributes` | `0x43060` | 161 | UnwindData |  |
| 20 | `GetResultPropertyList` | `0x43110` | 206 | UnwindData |  |
| 21 | `GetRightSeparator` | `0x431F0` | 180 | UnwindData |  |
| 22 | `GetUnicodeRanges` | `0x432B0` | 197 | UnwindData |  |
| 24 | `IsStringSupported` | `0x43380` | 178 | UnwindData |  |
| 26 | `MakeWordList` | `0x43440` | 271 | UnwindData |  |
| 27 | `Process` | `0x43560` | 152 | UnwindData |  |
| 28 | `SetConstraint` | `0x43600` | 178 | UnwindData |  |
| 29 | `SetEnabledUnicodeRanges` | `0x436C0` | 178 | UnwindData |  |
| 30 | `SetFactoid` | `0x43780` | 178 | UnwindData |  |
| 31 | `SetFlags` | `0x43840` | 163 | UnwindData |  |
| 32 | `SetGuide` | `0x438F0` | 180 | UnwindData |  |
| 33 | `SetStrokeGroupId` | `0x439B0` | 178 | UnwindData |  |
| 34 | `SetTextContext` | `0x43A70` | 210 | UnwindData |  |
| 35 | `SetWordList` | `0x43B50` | 203 | UnwindData |  |
