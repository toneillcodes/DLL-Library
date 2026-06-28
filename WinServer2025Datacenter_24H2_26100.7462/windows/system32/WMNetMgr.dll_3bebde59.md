# Binary Specification: WMNetMgr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WMNetMgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3bebde594e1233a7aa3220c313f874903bd8cc2cdb552898aa96e77b525c13b9`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1F110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1F130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x1F150` | 29 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1F180` | 132 | UnwindData |  |
