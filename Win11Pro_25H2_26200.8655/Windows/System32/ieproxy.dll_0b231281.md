# Binary Specification: ieproxy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ieproxy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0b2312811aabf9d0d22089ee7f4fd8d20211cdb1d703b94b90a90e2b3070daed`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllCanUnloadNow` | `0x3290` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllGetClassObject` | `0x32D0` | 53 | UnwindData |  |
| 6 | `DllRegisterServer` | `0x4A50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllUnregisterServer` | `0x4A80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetProxyDllInfo` | `0x4AB0` | 2,133 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
