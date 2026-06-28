# Binary Specification: sbe.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sbe.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f316f3f78b5a80bb9b96f285a25b450cf97eb09c6720d5ee6b2652b475c95656`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x3110` | 75 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x3170` | 72 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x31C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x3200` | 120 | UnwindData |  |
