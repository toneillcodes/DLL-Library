# Binary Specification: Windows.Storage.Compression.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.Storage.Compression.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0ef0b90927c89b5b6e01cb8a9f8a0d218510ed383f89d5f887bdc546786b2336`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x3C90` | 58 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x3CD0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3D10` | 134 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3DD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x3E00` | 40,252 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
