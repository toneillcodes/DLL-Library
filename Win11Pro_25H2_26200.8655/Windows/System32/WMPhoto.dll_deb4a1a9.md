# Binary Specification: WMPhoto.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WMPhoto.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `deb4a1a9ff3c3a63bd9b242c99334232525c8c9e8ad8d9b9dd10c4f8692efd6e`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x2FE00` | 328 | UnwindData |  |
| 3 | `DllMain` | `0x30100` | 140 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x33010` | 45 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x37E20` | 3,417 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x38B80` | 52,652 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
