# Binary Specification: qasf.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\qasf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `126c20bd89c17684d83598a323d50cb473f178344cc015ef8ba85275405f33d1`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2080` | 225 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x2170` | 513 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x2380` | 116,916 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
