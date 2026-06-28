# Binary Specification: IMETIP.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\IME\SHARED\IMETIP.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `359d3b25ef18032ba90c2d48967099a2c325eb5c3b3e148c6436f9646b2763a6`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x24CA0` | 73 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x56820` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x56870` | 138 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x56900` | 24 | UnwindData |  |
