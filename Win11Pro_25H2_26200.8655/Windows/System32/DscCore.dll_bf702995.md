# Binary Specification: DscCore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DscCore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bf7029956f3449c855cc23c7a578e4091dd70631fb41ec5ccf17871d0a881b17`
* **Total Exported Functions:** 16

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `MI_Main` | `0x1EE0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllCanUnloadNow` | `0x1F70` | 47 | UnwindData |  |
| 5 | `DllGetClassObject` | `0x1FB0` | 119 | UnwindData |  |
| 6 | `DllMain` | `0x2030` | 82 | UnwindData |  |
| 7 | `DllRegisterServer` | `0x2090` | 72 | UnwindData |  |
| 8 | `DllUnregisterServer` | `0x20E0` | 65 | UnwindData |  |
| 9 | `GetProviderClassID` | `0x2300` | 46,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `SysPrep_Cleanup` | `0xDA40` | 116 | UnwindData |  |
| 3 | `CreateAuthenticationCertificateWrapper` | `0xDAC0` | 198 | UnwindData |  |
| 15 | `ValidateCertificateExpirationWrapper` | `0xDB90` | 397 | UnwindData |  |
| 10 | `LCMTraps` | `0x51160` | 184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ValidatorTraps` | `0x51218` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CUTraps` | `0x51230` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CATraps` | `0x51290` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `NITS_STUB` | `0x51460` | 140,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `NITS_PRESENCE_STUB` | `0x73878` | 0 | Indeterminate |  |
