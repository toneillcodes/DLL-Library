# Binary Specification: Chakradiag.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Chakradiag.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `255f5f83ca2c688bd133bc38dd2529658f4d3842b9c7f5adb599023d955bf790`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0xA5B0` | 41 | UnwindData |  |
| 4 | `DllGetClassObject` | `0xA5E0` | 319 | UnwindData |  |
| 5 | `DllRegisterServer` | `0xA730` | 227 | UnwindData |  |
| 6 | `DllUnregisterServer` | `0xA820` | 49,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `GetDumpStreams` | `0x16950` | 115 | UnwindData |  |
| 1 | `FreeDumpStreams` | `0x169D0` | 74 | UnwindData |  |
