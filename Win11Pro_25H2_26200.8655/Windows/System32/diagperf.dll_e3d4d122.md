# Binary Specification: diagperf.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\diagperf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e3d4d122bf62bc01833891868701a9725819d5e5a00a0c9a99f2cde012faee9d`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `WdiHandleInstance` | `0x1AF00` | 35 | UnwindData |  |
| 5 | `WdiDiagnosticModuleMain` | `0x1B0C0` | 35 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x35F00` | 16,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `WdiGetDiagnosticModuleInterfaceVersion` | `0x39EE0` | 17,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x3E3C0` | 28,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x3E3C0` | 28,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x45440` | 42 | UnwindData |  |
