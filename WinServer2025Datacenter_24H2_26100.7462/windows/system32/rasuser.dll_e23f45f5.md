# Binary Specification: rasuser.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rasuser.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e23f45f59b1067a26605712a066b1472e0fa1cbc76051917d545ee5e5102523c`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `GetEapProviders` | `0xCBD0` | 257 | UnwindData |  |
| 6 | `IASCreateProfileAdvancedPage` | `0x1A2F0` | 263 | UnwindData |  |
| 7 | `IASDeleteProfileAdvancedPage` | `0x1A400` | 48 | UnwindData |  |
| 9 | `OpenRAS_IASProfileDlg2` | `0x1A470` | 362 | UnwindData |  |
| 5 | `OpenRAS_IASProfileDlg` | `0x1A5E0` | 332 | UnwindData |  |
| 10 | `DllCanUnloadNow` | `0x1BB00` | 94 | UnwindData |  |
| 11 | `DllGetClassObject` | `0x1BB70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `DllRegisterServer` | `0x1BBA0` | 586 | UnwindData |  |
| 13 | `DllUnregisterServer` | `0x1BDF0` | 33 | UnwindData |  |
