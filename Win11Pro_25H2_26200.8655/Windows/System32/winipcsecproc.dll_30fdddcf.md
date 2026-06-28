# Binary Specification: winipcsecproc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\winipcsecproc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `30fdddcf4fac49ab8fa437883a2c15b9e63c061ba8a36edee34613108d93d271`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `IpcSPAttest` | `0x5BD0` | 415 | UnwindData |  |
| 2 | `IpcSPBindLicense` | `0x5D80` | 459 | UnwindData |  |
| 3 | `IpcSPCheckEnvironmentSecurity` | `0x5F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `IpcSPCloseHandle` | `0x5F70` | 140 | UnwindData |  |
| 5 | `IpcSPCommit` | `0x6010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `IpcSPCreatePCE` | `0x6010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `IpcSPDecryptFinal` | `0x6010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `IpcSPDecryptUpdate` | `0x6010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `IpcSPEncryptFinal` | `0x6010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `IpcSPEncryptUpdate` | `0x6010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `IpcSPCreateDecryptor` | `0x6020` | 437 | UnwindData |  |
| 7 | `IpcSPCreateEnablingPrincipal` | `0x61E0` | 513 | UnwindData |  |
| 8 | `IpcSPCreateEncryptor` | `0x63F0` | 437 | UnwindData |  |
| 9 | `IpcSPCreateMachineCerts` | `0x65B0` | 175 | UnwindData |  |
| 11 | `IpcSPCreateSecurityProcessor` | `0x6670` | 552 | UnwindData |  |
| 12 | `IpcSPDecrypt` | `0x68A0` | 383 | UnwindData |  |
| 15 | `IpcSPDecryptWithRac` | `0x6A30` | 388 | UnwindData |  |
| 16 | `IpcSPEnableAndEncrypt` | `0x6BC0` | 1,751 | UnwindData |  |
| 17 | `IpcSPEnablePublishingLicense` | `0x72A0` | 178 | UnwindData |  |
| 18 | `IpcSPEncrypt` | `0x7360` | 383 | UnwindData |  |
| 21 | `IpcSPGetBoundRightKey` | `0x74F0` | 473 | UnwindData |  |
| 22 | `IpcSPGetCurrentTime` | `0x76D0` | 347 | UnwindData |  |
| 23 | `IpcSPGetInfo` | `0x7840` | 545 | UnwindData |  |
| 24 | `IpcSPGetProcAddress` | `0x7A70` | 571 | UnwindData |  |
| 25 | `IpcSPInitialize` | `0x7CC0` | 170 | UnwindData |  |
| 26 | `IpcSPIsActivated` | `0x7D70` | 162 | UnwindData |  |
| 27 | `IpcSPLoadLibrary` | `0x7E20` | 447 | UnwindData |  |
| 28 | `IpcSPSign` | `0x7FF0` | 421 | UnwindData |  |
