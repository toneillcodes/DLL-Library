# Binary Specification: wisp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wisp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `882f80ce8dd90ee258d73e90eb719338f51b1bee3913c4a1b895fc02d179c3c5`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x19240` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1CB40` | 73,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x2EB80` | 6,588 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2EB80` | 6,588 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
