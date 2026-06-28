# Binary Specification: cscui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cscui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cef4567d4fe5dd9604860c46670bf7827e97b21b8f9b665ca6c054505b88c073`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `DllGetClassObject` | `0x4860` | 899 | UnwindData |  |
| 9 | `DllCanUnloadNow` | `0x51B0` | 42 | UnwindData |  |
| 1 | `CPlApplet` | `0xA890` | 365 | UnwindData |  |
| 2 | `CSCUIOptionsPropertySheet` | `0xAA10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CSCOptions_RunDLL` | `0xAA20` | 145 | UnwindData |  |
| 4 | `CSCOptions_RunDLLA` | `0xAA20` | 145 | UnwindData |  |
| 5 | `CSCOptions_RunDLLW` | `0xAAC0` | 62 | UnwindData |  |
| 6 | `CSCUIInitialize` | `0xAB10` | 2,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CSCUISetState` | `0xAB10` | 2,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CSCUIRemoveFolderFromCache` | `0xB3B0` | 176 | UnwindData |  |
| 11 | `DllRegisterServer` | `0xB660` | 63 | UnwindData |  |
| 12 | `DllUnregisterServer` | `0xB6B0` | 63 | UnwindData |  |
