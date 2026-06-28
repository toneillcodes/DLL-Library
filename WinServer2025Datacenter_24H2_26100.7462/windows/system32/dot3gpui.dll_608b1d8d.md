# Binary Specification: dot3gpui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dot3gpui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `608b1d8d4094c3c91247f14ffc13f3a5ab90bfc88af3eb156fed2ca6ec3cd0cc`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x11970` | 94 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x119E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x11A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x11A30` | 66,195 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
