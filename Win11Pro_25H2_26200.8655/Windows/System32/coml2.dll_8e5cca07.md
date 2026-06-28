# Binary Specification: coml2.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\coml2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8e5cca07dc12055aad6ba0bd97fcdfecf6166f74d4c9e3e1608add719067b5a9`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 21 | `StgCreateDocfileOnILockBytes` | `0x23A0` | 706 | UnwindData |  |
| 30 | `StgOpenStorageOnILockBytes` | `0x16120` | 1,044 | UnwindData |  |
| 28 | `StgOpenStorage` | `0x17740` | 56 | UnwindData |  |
| 25 | `StgIsStorageFile` | `0x23CC0` | 179 | UnwindData |  |
| 29 | `StgOpenStorageEx` | `0x31870` | 330 | UnwindData |  |
| 20 | `StgCreateDocfile` | `0x32C10` | 43 | UnwindData |  |
| 22 | `StgCreatePropSetStg` | `0x352A0` | 257 | UnwindData |  |
| 23 | `StgCreatePropStg` | `0x353B0` | 441 | UnwindData |  |
| 32 | `WriteClassStg` | `0x35570` | 62 | UnwindData |  |
| 18 | `ReadClassStg` | `0x355C0` | 166 | UnwindData |  |
| 19 | `ReadClassStm` | `0x35670` | 81 | UnwindData |  |
| 33 | `WriteClassStm` | `0x356D0` | 69 | UnwindData |  |
| 9 | `Coml2DllGetClassObject` | `0x3A740` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DllGetClassObject` | `0x3A740` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `CreateILockBytesOnHGlobal` | `0x3A850` | 341 | UnwindData |  |
| 24 | `StgCreateStorageEx` | `0x3B4E0` | 553 | UnwindData |  |
| 15 | `GetConvertStg` | `0x3CC90` | 44 | UnwindData |  |
| 11 | *Ordinal Only* | `0x48C20` | 598 | UnwindData |  |
| 26 | `StgIsStorageILockBytes` | `0x48E80` | 164 | UnwindData |  |
| 31 | `StgSetTimes` | `0x48F30` | 231 | UnwindData |  |
| 14 | `FmtIdToPropStgName` | `0x4FDF0` | 70 | UnwindData |  |
| 17 | `PropStgNameToFmtId` | `0x4FE40` | 92 | UnwindData |  |
| 27 | `StgOpenPropStg` | `0x4FEB0` | 437 | UnwindData |  |
| 7 | *Ordinal Only* | `0x50070` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | *Ordinal Only* | `0x503B0` | 63 | UnwindData |  |
| 4 | *Ordinal Only* | `0x50530` | 66 | UnwindData |  |
| 6 | *Ordinal Only* | `0x507F0` | 83 | UnwindData |  |
| 8 | *Ordinal Only* | `0x52E30` | 266 | UnwindData |  |
| 3 | *Ordinal Only* | `0x5BAC0` | 406 | UnwindData |  |
| 2 | *Ordinal Only* | `0x5BC60` | 291 | UnwindData |  |
| 1 | *Ordinal Only* | `0x5BD90` | 772 | UnwindData |  |
| 16 | `GetHGlobalFromILockBytes` | `0x5E9C0` | 119 | UnwindData |  |
| 12 | *Ordinal Only* | `0x5EA40` | 40 | UnwindData |  |
