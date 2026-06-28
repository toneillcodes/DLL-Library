# Binary Specification: cscui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cscui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3265ee0c3be784c50dd040eda7be173a574dea4f4eb5b320cdac93003dcf45ea`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `DllGetClassObject` | `0x4830` | 899 | UnwindData |  |
| 9 | `DllCanUnloadNow` | `0x5180` | 42 | UnwindData |  |
| 1 | `CPlApplet` | `0xA720` | 365 | UnwindData |  |
| 2 | `CSCUIOptionsPropertySheet` | `0xA8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CSCOptions_RunDLL` | `0xA8B0` | 145 | UnwindData |  |
| 4 | `CSCOptions_RunDLLA` | `0xA8B0` | 145 | UnwindData |  |
| 5 | `CSCOptions_RunDLLW` | `0xA950` | 62 | UnwindData |  |
| 6 | `CSCUIInitialize` | `0xA9A0` | 2,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CSCUISetState` | `0xA9A0` | 2,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CSCUIRemoveFolderFromCache` | `0xB240` | 176 | UnwindData |  |
| 11 | `DllRegisterServer` | `0xB4F0` | 63 | UnwindData |  |
| 12 | `DllUnregisterServer` | `0xB540` | 63 | UnwindData |  |
