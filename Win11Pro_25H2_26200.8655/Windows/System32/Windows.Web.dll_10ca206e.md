# Binary Specification: Windows.Web.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.Web.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `10ca206e6e5ccf5c7983fd71d8d1732e3b7be1e24832ee88e81c800dbd5230ba`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetActivationFactory` | `0x13180` | 83 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x13710` | 58 | UnwindData |  |
| 4 | `DllMain` | `0x15C40` | 81 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x4EFD0` | 134 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x4F060` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x4F090` | 71,228 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
