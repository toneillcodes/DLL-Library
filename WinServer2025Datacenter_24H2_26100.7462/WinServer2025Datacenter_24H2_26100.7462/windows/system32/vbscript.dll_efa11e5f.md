# Binary Specification: vbscript.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vbscript.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `efa11e5fcdd2423df4bd16d84fd5f7bf44cd4e55e05593ebfea83609c7883655`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x3B070` | 302 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x3ECF0` | 108,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x594E0` | 1,472 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x59AB0` | 315 | UnwindData |  |
