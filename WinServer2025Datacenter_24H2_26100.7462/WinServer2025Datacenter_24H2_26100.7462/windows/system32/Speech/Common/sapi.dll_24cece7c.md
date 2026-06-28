# Binary Specification: sapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Speech\Common\sapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `24cece7ce9d94f423573da31f09554a1055a81e1cdddcefe04ee017d984f73b3`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1FD0` | 171,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2BCF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x2BD10` | 90 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x2BD70` | 84 | UnwindData |  |
