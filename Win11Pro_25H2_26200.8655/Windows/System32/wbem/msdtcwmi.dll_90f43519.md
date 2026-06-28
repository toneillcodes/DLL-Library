# Binary Specification: msdtcwmi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\msdtcwmi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `90f43519567be561cbe7ee5fede05a20b436c879527adbf0b46db4ef4894aa9b`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0x1F30` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x1FC0` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2000` | 113 | UnwindData |  |
| 3 | `DllMain` | `0x2080` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x20E0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x2130` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x2350` | 63,917 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
