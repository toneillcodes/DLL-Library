# Binary Specification: recovery.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\recovery.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `834860a784e54825bc55999f584d878107bd948c84c4b943b023e93fd3bf0b96`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2A90` | 58 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x2AD0` | 374 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x2DB0` | 40,700 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x2DB0` | 40,700 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
