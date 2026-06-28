# Binary Specification: Windows.Storage.Compression.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.Storage.Compression.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1548d6c4076a0e624c387fa7fa4026dbacc2e118ed219b70a22aee07981cf9f0`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x3C90` | 58 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x3CD0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3D10` | 134 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3DD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x3E00` | 40,428 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
