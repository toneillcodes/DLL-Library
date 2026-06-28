# Binary Specification: SxsMigPlugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\migration\SxsMigPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3981e510d3efbc9f96607e6ee2732ae50b472f658d1f37faeceab16a32308a49`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x9840` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x9870` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x99B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x99D0` | 321 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x9B20` | 179 | UnwindData |  |
