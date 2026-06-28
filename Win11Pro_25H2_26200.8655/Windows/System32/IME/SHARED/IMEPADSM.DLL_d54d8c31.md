# Binary Specification: IMEPADSM.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\IME\SHARED\IMEPADSM.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d54d8c319706fdaeb98e4293daf46cf0ea4a30518d0008c4c7b36554d9f207e0`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DllCanUnloadNow` | `0x7C90` | 28,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllRegisterServer` | `0x7C90` | 28,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllUnregisterServer` | `0x7C90` | 28,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateObject2` | `0xEDA0` | 160 | UnwindData |  |
| 2 | `CreateObject` | `0xEE50` | 200 | UnwindData |  |
| 3 | `RegClass` | `0xEFD0` | 215 | UnwindData |  |
| 4 | `UnregClass` | `0xF0B0` | 73 | UnwindData |  |
| 6 | `DllGetClassObject` | `0xF130` | 32,476 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
