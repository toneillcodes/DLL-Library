# Binary Specification: IMEPADSM.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\IME\SHARED\IMEPADSM.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `98b77dc1b62412e10846f21cc66db6277d8e3ae3c754472896083ce298e3319d`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DllCanUnloadNow` | `0x7FE0` | 30,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllRegisterServer` | `0x7FE0` | 30,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllUnregisterServer` | `0x7FE0` | 30,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateObject2` | `0xF710` | 160 | UnwindData |  |
| 2 | `CreateObject` | `0xF7C0` | 200 | UnwindData |  |
| 3 | `RegClass` | `0xF940` | 215 | UnwindData |  |
| 4 | `UnregClass` | `0xFA20` | 73 | UnwindData |  |
| 6 | `DllGetClassObject` | `0xFAA0` | 32,556 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
