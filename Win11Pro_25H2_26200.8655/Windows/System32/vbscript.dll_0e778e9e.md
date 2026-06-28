# Binary Specification: vbscript.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vbscript.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0e778e9ea0a3d8a8b17623b12a2d985966075917a3ac1faa438001f4d749bb53`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x3AF70` | 302 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x3EAB0` | 101,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x57700` | 1,472 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x57CD0` | 315 | UnwindData |  |
