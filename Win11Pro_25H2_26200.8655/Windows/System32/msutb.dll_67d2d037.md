# Binary Specification: msutb.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msutb.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `67d2d0374cf27f659fdbf4937410f067ceb6130e61abfab60973b97859e91e61`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x12830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x12850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x12860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x12870` | 70 | UnwindData |  |
| 8 | `SetRegisterLangBand` | `0x12A50` | 138 | UnwindData |  |
| 1 | `ClosePopupTipbar` | `0x1D9C0` | 306 | UnwindData |  |
| 6 | `GetChildTipbar` | `0x1DB00` | 42 | UnwindData |  |
| 7 | `GetPopupTipbar` | `0x1DB30` | 36 | UnwindData |  |
