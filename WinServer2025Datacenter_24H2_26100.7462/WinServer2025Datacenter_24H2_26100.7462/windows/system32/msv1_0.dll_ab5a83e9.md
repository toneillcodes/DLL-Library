# Binary Specification: msv1_0.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msv1_0.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ab5a83e9b15088a0a2d09dbc9f2ef1de623878b571672349526ec3c608404016`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `LsaApLogonTerminated` | `0xD0A0` | 185 | UnwindData |  |
| 2 | `MsvIsLocalhostAliases` | `0x10D00` | 10 | UnwindData |  |
| 16 | `MsvIsIpAddressLocal` | `0x10E90` | 858 | UnwindData |  |
| 18 | `MsvSamValidate` | `0x11450` | 1,275 | UnwindData |  |
| 8 | `LsaApCallPackageUntrusted` | `0x175A0` | 571 | UnwindData |  |
| 6 | `LsaApCallPackage` | `0x19F10` | 342 | UnwindData |  |
| 32 | `SpInstanceInit` | `0x1A200` | 510 | UnwindData |  |
| 4 | `SpUserModeInitialize` | `0x1C4D0` | 265 | UnwindData |  |
| 5 | `DllMain` | `0x1D0C0` | 304 | UnwindData |  |
| 11 | `LsaApLogonUserEx2` | `0x1DCE0` | 19,115 | UnwindData |  |
| 17 | `MsvSamLogoff` | `0x304A0` | 12,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `LsaApCallPackagePassthrough` | `0x334A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `LsaApInitializePackage` | `0x334F0` | 466 | UnwindData |  |
| 15 | `MsvGetLogonAttemptCount` | `0x370A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `MsvValidateTarget` | `0x370B0` | 695 | UnwindData |  |
| 12 | `Msv1_0ExportSubAuthenticationRoutine` | `0x38180` | 239 | UnwindData |  |
| 13 | `Msv1_0ExportSubAuthenticationRoutineEx` | `0x38280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `Msv1_0SubAuthenticationPresent` | `0x38290` | 31 | UnwindData |  |
| 3 | `SpLsaModeInitialize` | `0x4D2D0` | 723 | UnwindData |  |
| 1 | `SpInitialize` | `0x4F630` | 2,397 | UnwindData |  |
