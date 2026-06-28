# Binary Specification: wshext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wshext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `762e48b4bedb91a07389da0f055b36f65198c60f8f55f3efed4043be6a29157c`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `VerifyIndirectData` | `0x1010` | 85 | UnwindData |  |
| 2 | `GetSignedDataMsg` | `0x1540` | 360 | UnwindData |  |
| 3 | `IsFileSupportedName` | `0x2A30` | 114 | UnwindData |  |
| 7 | `DllCanUnloadNow` | `0x3170` | 17,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllGetClassObject` | `0x7590` | 67 | UnwindData |  |
| 9 | `DllRegisterServer` | `0x75E0` | 1,088 | UnwindData |  |
| 10 | `DllUnregisterServer` | `0x7A30` | 155 | UnwindData |  |
| 1 | `CreateIndirectData` | `0xA080` | 894 | UnwindData |  |
| 4 | `PutSignedDataMsg` | `0xA800` | 385 | UnwindData |  |
| 5 | `RemoveSignedDataMsg` | `0xA990` | 230 | UnwindData |  |
