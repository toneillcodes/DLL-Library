# Binary Specification: usbdr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\UMDF\usbdr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b848e42102274dd52d41a7962ac0e037b9768e60a2b03cbf1d68a370b6e047cc`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2580` | 297 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x26B0` | 129,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x26B0` | 129,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `Microsoft_WDF_UMDF_Version` | `0x220D0` | 0 | Indeterminate |  |
