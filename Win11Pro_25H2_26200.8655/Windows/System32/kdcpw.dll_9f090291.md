# Binary Specification: kdcpw.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\kdcpw.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9f09029160a984e8b8733fc9cee90c9be9d024f449b90c38722a986854fc2fe2`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CredentialUpdateFree` | `0x45E0` | 27 | UnwindData |  |
| 7 | `StrongNtowfFree` | `0x45E0` | 27 | UnwindData |  |
| 2 | `CredentialUpdateNotify2` | `0x4610` | 167 | UnwindData |  |
| 3 | `CredentialUpdateNotify` | `0x46C0` | 46 | UnwindData |  |
| 4 | `CredentialUpdateRegister2` | `0x4700` | 31 | UnwindData |  |
| 5 | `CredentialUpdateRegister` | `0x4730` | 31 | UnwindData |  |
| 6 | `RegisterMappedEntrypoints` | `0x7950` | 103 | UnwindData |  |
| 8 | `StrongNtowfNotify` | `0x8710` | 273 | UnwindData |  |
| 9 | `StrongNtowfRegister` | `0x8830` | 31 | UnwindData |  |
| 10 | `InitializeChangeNotify` | `0x9BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `PasswordChangeNotify` | `0x9BF0` | 11,790 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
