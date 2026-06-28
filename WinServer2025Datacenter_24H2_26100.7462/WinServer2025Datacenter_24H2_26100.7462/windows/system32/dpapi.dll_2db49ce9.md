# Binary Specification: dpapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dpapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2db49ce97e44f116c31b06136e79e887141c3e74abe823cb243c2073509b7eea`
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
