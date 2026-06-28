# Binary Specification: WMADMOE.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WMADMOE.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `30fe10a87c49e3c5e84bf8c6ffd98ae17f745bffcb9ff03499d1811fbde47e27`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllRegisterServer` | `0x35AA0` | 242 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x35BA0` | 1,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateInstance` | `0x362E0` | 121 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x36360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x36390` | 231 | UnwindData |  |
