# Binary Specification: msutb.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msutb.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `161719f19d464efe9d7e6f980673cfe45bf6a4cb3f14494034eba7c79ac48faa`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x14F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x14FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x14FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x14FD0` | 70 | UnwindData |  |
| 8 | `SetRegisterLangBand` | `0x151B0` | 138 | UnwindData |  |
| 1 | `ClosePopupTipbar` | `0x1F200` | 306 | UnwindData |  |
| 6 | `GetChildTipbar` | `0x1F340` | 42 | UnwindData |  |
| 7 | `GetPopupTipbar` | `0x1F370` | 36 | UnwindData |  |
