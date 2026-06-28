# Binary Specification: netprofmsvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\netprofmsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b19e16a6a31038bc0a6bc982f611aafe0afb58cc6c7fa7da7cba33afb256c343`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllMain` | `0xA2940` | 407 | UnwindData |  |
| 1 | `ServiceMain` | `0xA4400` | 422 | UnwindData |  |
| 2 | `SvchostPushServiceGlobalsEx` | `0xA4C00` | 711,867 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
