# Binary Specification: kdcpw.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\kdcpw.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `52cc7d315e17dd55778a6284eedda6587928fee5455884e2de07e7643b27106e`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CredentialUpdateFree` | `0x45D0` | 27 | UnwindData |  |
| 7 | `StrongNtowfFree` | `0x45D0` | 27 | UnwindData |  |
| 2 | `CredentialUpdateNotify2` | `0x4600` | 167 | UnwindData |  |
| 3 | `CredentialUpdateNotify` | `0x46B0` | 46 | UnwindData |  |
| 4 | `CredentialUpdateRegister2` | `0x46F0` | 31 | UnwindData |  |
| 5 | `CredentialUpdateRegister` | `0x4720` | 31 | UnwindData |  |
| 6 | `RegisterMappedEntrypoints` | `0x7840` | 103 | UnwindData |  |
| 8 | `StrongNtowfNotify` | `0x85F0` | 273 | UnwindData |  |
| 9 | `StrongNtowfRegister` | `0x8710` | 31 | UnwindData |  |
| 10 | `InitializeChangeNotify` | `0x9AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `PasswordChangeNotify` | `0x9AD0` | 11,790 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
