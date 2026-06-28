# Binary Specification: wuapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wuapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e864a3efd619a4f9dae42ae7a4045535a96ba57fd82374e7a179a2e04a5df030`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x7E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x7E50` | 187 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x7F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x7F40` | 63,042 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
