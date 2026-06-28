# Binary Specification: coml2.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\coml2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bcbc16aa26725208d0e23b76b377a0e4a0d6ec0411209db1856e9231825932bb`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 21 | `StgCreateDocfileOnILockBytes` | `0x2390` | 706 | UnwindData |  |
| 30 | `StgOpenStorageOnILockBytes` | `0x16110` | 1,044 | UnwindData |  |
| 28 | `StgOpenStorage` | `0x17730` | 56 | UnwindData |  |
| 25 | `StgIsStorageFile` | `0x23D30` | 170 | UnwindData |  |
| 29 | `StgOpenStorageEx` | `0x329E0` | 354 | UnwindData |  |
| 22 | `StgCreatePropSetStg` | `0x35000` | 257 | UnwindData |  |
| 23 | `StgCreatePropStg` | `0x35110` | 441 | UnwindData |  |
| 32 | `WriteClassStg` | `0x352D0` | 62 | UnwindData |  |
| 18 | `ReadClassStg` | `0x35320` | 166 | UnwindData |  |
| 19 | `ReadClassStm` | `0x353D0` | 81 | UnwindData |  |
| 33 | `WriteClassStm` | `0x35430` | 69 | UnwindData |  |
| 9 | `Coml2DllGetClassObject` | `0x3A4A0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DllGetClassObject` | `0x3A4A0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `CreateILockBytesOnHGlobal` | `0x3A5B0` | 341 | UnwindData |  |
| 20 | `StgCreateDocfile` | `0x3B160` | 43 | UnwindData |  |
| 24 | `StgCreateStorageEx` | `0x3B530` | 553 | UnwindData |  |
| 15 | `GetConvertStg` | `0x3CE20` | 44 | UnwindData |  |
| 11 | *Ordinal Only* | `0x48BB0` | 598 | UnwindData |  |
| 26 | `StgIsStorageILockBytes` | `0x48E10` | 164 | UnwindData |  |
| 31 | `StgSetTimes` | `0x48EC0` | 231 | UnwindData |  |
| 14 | `FmtIdToPropStgName` | `0x4FD80` | 70 | UnwindData |  |
| 17 | `PropStgNameToFmtId` | `0x4FDD0` | 110 | UnwindData |  |
| 27 | `StgOpenPropStg` | `0x4FE50` | 437 | UnwindData |  |
| 7 | *Ordinal Only* | `0x50010` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | *Ordinal Only* | `0x50350` | 63 | UnwindData |  |
| 4 | *Ordinal Only* | `0x504D0` | 66 | UnwindData |  |
| 6 | *Ordinal Only* | `0x50790` | 83 | UnwindData |  |
| 8 | *Ordinal Only* | `0x52DD0` | 266 | UnwindData |  |
| 3 | *Ordinal Only* | `0x5BA60` | 406 | UnwindData |  |
| 2 | *Ordinal Only* | `0x5BC00` | 291 | UnwindData |  |
| 1 | *Ordinal Only* | `0x5BD30` | 772 | UnwindData |  |
| 16 | `GetHGlobalFromILockBytes` | `0x5E960` | 119 | UnwindData |  |
| 12 | *Ordinal Only* | `0x5E9E0` | 40 | UnwindData |  |
