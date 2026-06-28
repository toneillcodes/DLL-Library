# Binary Specification: usbdr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\drivers\UMDF\usbdr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `061ed33ae26b53190ec8c8f760787a8b48325b11b08764ed3601e43231233824`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2350` | 297 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x2480` | 113,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2480` | 113,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `Microsoft_WDF_UMDF_Version` | `0x1E0D0` | 0 | Indeterminate |  |
