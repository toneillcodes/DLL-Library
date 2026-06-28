# Binary Specification: msdmo.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msdmo.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `32e85193f2c39c0ac0bc51bd9be213fe85c892be41f4cdd4af2d25ff8f60a997`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DMOGetName` | `0x1010` | 294 | UnwindData |  |
| 3 | `DMOGetTypes` | `0x1190` | 1,005 | UnwindData |  |
| 5 | `DMOGuidToStrW` | `0x1590` | 164 | UnwindData |  |
| 1 | `DMOEnum` | `0x1640` | 89 | UnwindData |  |
| 15 | `MoInitMediaType` | `0x2980` | 109 | UnwindData |  |
| 14 | `MoFreeMediaType` | `0x2B00` | 14 | UnwindData |  |
| 10 | `MoCopyMediaType` | `0x2B60` | 34 | UnwindData |  |
| 8 | `DMOStrToGuidW` | `0x2C60` | 346 | UnwindData |  |
| 7 | `DMOStrToGuidA` | `0x2DC0` | 260 | UnwindData |  |
| 11 | `MoCreateMediaType` | `0x40C0` | 108 | UnwindData |  |
| 12 | `MoDeleteMediaType` | `0x4140` | 61 | UnwindData |  |
| 13 | `MoDuplicateMediaType` | `0x4190` | 81 | UnwindData |  |
| 6 | `DMORegister` | `0x4680` | 1,328 | UnwindData |  |
| 9 | `DMOUnregister` | `0x4BC0` | 611 | UnwindData |  |
| 4 | `DMOGuidToStrA` | `0x4F60` | 163 | UnwindData |  |
