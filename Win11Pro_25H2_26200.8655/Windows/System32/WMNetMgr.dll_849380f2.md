# Binary Specification: WMNetMgr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WMNetMgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `849380f2875c5852499ea7a3163ad7bd478d4a1279621f32c6e245254d3807de`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1FBF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1FC10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x1FC30` | 29 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1FC60` | 132 | UnwindData |  |
