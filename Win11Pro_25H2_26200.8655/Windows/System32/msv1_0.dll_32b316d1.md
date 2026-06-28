# Binary Specification: msv1_0.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msv1_0.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `32b316d19282b43198886677f20e1cbbb204184ee72a3252d77b6bb4451f0abe`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `LsaApLogonTerminated` | `0xA820` | 185 | UnwindData |  |
| 2 | `MsvIsLocalhostAliases` | `0xF4E0` | 10 | UnwindData |  |
| 16 | `MsvIsIpAddressLocal` | `0xF670` | 858 | UnwindData |  |
| 8 | `LsaApCallPackageUntrusted` | `0x139D0` | 571 | UnwindData |  |
| 18 | `MsvSamValidate` | `0x15D70` | 1,275 | UnwindData |  |
| 6 | `LsaApCallPackage` | `0x198A0` | 342 | UnwindData |  |
| 32 | `SpInstanceInit` | `0x19B90` | 510 | UnwindData |  |
| 4 | `SpUserModeInitialize` | `0x1BDE0` | 265 | UnwindData |  |
| 5 | `DllMain` | `0x1C9D0` | 304 | UnwindData |  |
| 11 | `LsaApLogonUserEx2` | `0x1D9E0` | 19,183 | UnwindData |  |
| 17 | `MsvSamLogoff` | `0x30B10` | 12,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `LsaApCallPackagePassthrough` | `0x33BD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `LsaApInitializePackage` | `0x33C20` | 466 | UnwindData |  |
| 15 | `MsvGetLogonAttemptCount` | `0x377F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `MsvValidateTarget` | `0x37800` | 695 | UnwindData |  |
| 12 | `Msv1_0ExportSubAuthenticationRoutine` | `0x380C0` | 239 | UnwindData |  |
| 13 | `Msv1_0ExportSubAuthenticationRoutineEx` | `0x381C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `Msv1_0SubAuthenticationPresent` | `0x381D0` | 31 | UnwindData |  |
| 3 | `SpLsaModeInitialize` | `0x4CBF0` | 723 | UnwindData |  |
| 1 | `SpInitialize` | `0x4EF90` | 2,332 | UnwindData |  |
