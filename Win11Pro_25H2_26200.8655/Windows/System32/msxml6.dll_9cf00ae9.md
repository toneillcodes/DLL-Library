# Binary Specification: msxml6.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msxml6.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9cf00ae96d681fc94104070d61534b3a82ae944085f7ee7c648ac4f9c9111e1b`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetActivationFactory` | `0x6EFD0` | 134 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x6F3F0` | 346 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x8B710` | 124 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x9B8F0` | 137,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x9B8F0` | 137,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllSetProperty` | `0xBD3D0` | 802,012 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
