# Binary Specification: netman.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\netman.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `59bff8990abbc825dfa72efc05af7faeb0cdef75d67c62941e6b660e58c00391`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllRegisterServer` | `0x5730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllUnregisterServer` | `0x5730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `HrGetPnpDeviceStatus` | `0x5740` | 232 | UnwindData |  |
| 4 | `ServiceMain` | `0x59D0` | 82,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SvchostPushServiceGlobals` | `0x19D60` | 123,916 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
