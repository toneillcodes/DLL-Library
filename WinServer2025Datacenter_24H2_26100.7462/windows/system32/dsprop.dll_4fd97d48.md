# Binary Specification: dsprop.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dsprop.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4fd97d48dd65713590ba8aa3682ac7a0980bf3f99fe8a9cd21d0b45828965140`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CheckADsError` | `0x2970` | 222 | UnwindData |  |
| 4 | `ErrMsg` | `0x2A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ErrMsgParam` | `0x2A80` | 264 | UnwindData |  |
| 7 | `MsgBox` | `0x3260` | 52 | UnwindData |  |
| 8 | `ReportError` | `0x33F0` | 171 | UnwindData |  |
| 18 | `DllCanUnloadNow` | `0x3540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `DllGetClassObject` | `0x3560` | 223 | UnwindData |  |
| 20 | `DllRegisterServer` | `0x3700` | 873 | UnwindData |  |
| 21 | `DllUnregisterServer` | `0x3A70` | 406 | UnwindData |  |
| 9 | `Smart_PADS_ATTR_INFO__Empty` | `0x3C80` | 40 | UnwindData |  |
| 6 | `FindSheet` | `0x5F70` | 51 | UnwindData |  |
| 10 | `ADsPropCheckIfWritable` | `0x7AE0` | 111 | UnwindData |  |
| 11 | `ADsPropCreateNotifyObj` | `0x7B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `ADsPropGetInitInfo` | `0x7B70` | 108 | UnwindData |  |
| 13 | `ADsPropSendErrorMessage` | `0x7BF0` | 43 | UnwindData |  |
| 14 | `ADsPropSetHwnd` | `0x7C30` | 82 | UnwindData |  |
| 15 | `ADsPropSetHwndWithTitle` | `0x7C90` | 95 | UnwindData |  |
| 16 | `ADsPropShowErrorDialog` | `0x7D00` | 308 | UnwindData |  |
| 17 | `BringSheetToForeground` | `0x7E40` | 57 | UnwindData |  |
| 22 | `IsSheetAlreadyUp` | `0x7E80` | 264 | UnwindData |  |
| 2 | `CrackName` | `0x87B0` | 1,737 | UnwindData |  |
| 3 | `DSPROP_GetGCSearchOnDomain` | `0x9080` | 218 | UnwindData |  |
| 23 | `PostADsPropSheet` | `0xADE0` | 31 | UnwindData |  |
