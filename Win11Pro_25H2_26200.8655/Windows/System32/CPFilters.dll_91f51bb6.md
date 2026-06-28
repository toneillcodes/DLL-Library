# Binary Specification: CPFilters.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\CPFilters.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `91f51bb60ebedda89710c3bb6b3593ffd9b86c5ad0adf2f7601e216f02b57a33`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0xB790` | 629 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xBA10` | 243 | UnwindData |  |
| 5 | `UpdatePlayready` | `0xC2C0` | 297 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x13800` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x13860` | 224 | UnwindData |  |
