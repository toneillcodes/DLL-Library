# Binary Specification: dpapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dpapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f1c4c0719336b952e838119be42df427d67621a265323593449a7a832f90cb20`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `CryptUnprotectDataNoUI` | `0x1010` | 790 | UnwindData |  |
| 1 | `CryptProtectDataNoUI` | `0x1330` | 885 | UnwindData |  |
| 7 | `iCryptIdentifyProtection` | `0x1780` | 135 | UnwindData |  |
| 5 | `CryptUnprotectMemory` | `0x1900` | 63 | UnwindData |  |
| 2 | `CryptProtectMemory` | `0x1950` | 63 | UnwindData |  |
| 6 | `CryptUpdateProtectedState` | `0x2090` | 577 | UnwindData |  |
| 3 | `CryptResetMachineCredentials` | `0x22E0` | 210 | UnwindData |  |
