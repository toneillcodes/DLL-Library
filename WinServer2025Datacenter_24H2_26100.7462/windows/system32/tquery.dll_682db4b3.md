# Binary Specification: tquery.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\tquery.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `682db4b3958c3b4a6c643433a5b93a254d1acb2f87ec8c6c76477ad9de0fdaf3`
* **Total Exported Functions:** 69

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 298 | `?SetProperty@CFullPropSpec@@QEAAXK@Z` | `0x780B0` | 59 | UnwindData |  |
| 256 | `??0CFullPropSpec@@QEAA@AEBV0@@Z` | `0x79280` | 74 | UnwindData |  |
| 259 | `??1CAllocStorageVariant@@IEAA@XZ` | `0x7CF90` | 3,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `?ResetType@CAllocStorageVariant@@IEAAXAEAVPMemoryAllocator@@@Z` | `0x7DC20` | 722 | UnwindData |  |
| 314 | `ExternPropagateEventToOpenQueries` | `0x9A4A0` | 17 | UnwindData |  |
| 311 | `DllGetClassObject` | `0x9FB30` | 239 | UnwindData |  |
| 288 | `?PutFloat@CMemSerStream@@UEAAXM@Z` | `0xB65D0` | 78 | UnwindData |  |
| 271 | `?GetFloat@CMemDeSerStream@@UEAAMXZ` | `0xB68F0` | 65 | UnwindData |  |
| 278 | `?GetWChar@CMemDeSerStream@@UEAAXPEAGK@Z` | `0xB7540` | 106 | UnwindData |  |
| 294 | `?PutWChar@CMemSerStream@@UEAAXPEBGK@Z` | `0xB75B0` | 101 | UnwindData |  |
| 284 | `?PutBlob@CMemSerStream@@UEAAXPEBEK@Z` | `0xB7620` | 90 | UnwindData |  |
| 286 | `?PutChar@CMemSerStream@@UEAAXPEBDK@Z` | `0xB7680` | 88 | UnwindData |  |
| 265 | `?GetBlob@CMemDeSerStream@@UEAAXPEAEK@Z` | `0xB76E0` | 95 | UnwindData |  |
| 267 | `?GetChar@CMemDeSerStream@@UEAAXPEADK@Z` | `0xB7750` | 95 | UnwindData |  |
| 290 | `?PutLong@CMemSerStream@@UEAAXJ@Z` | `0xB77C0` | 74 | UnwindData |  |
| 273 | `?GetLong@CMemDeSerStream@@UEAAJXZ` | `0xB7810` | 63 | UnwindData |  |
| 276 | `?GetULong@CMemDeSerStream@@UEAAKXZ` | `0xB7860` | 61 | UnwindData |  |
| 293 | `?PutUShort@CMemSerStream@@UEAAXG@Z` | `0xB78B0` | 75 | UnwindData |  |
| 289 | `?PutGUID@CMemSerStream@@UEAAXAEBU_GUID@@@Z` | `0xB7910` | 80 | UnwindData |  |
| 266 | `?GetByte@CMemDeSerStream@@UEAAEXZ` | `0xB7970` | 82 | UnwindData |  |
| 277 | `?GetUShort@CMemDeSerStream@@UEAAGXZ` | `0xB79D0` | 63 | UnwindData |  |
| 272 | `?GetGUID@CMemDeSerStream@@UEAAXAEAU_GUID@@@Z` | `0xB7A20` | 80 | UnwindData |  |
| 292 | `?PutULong@CMemSerStream@@UEAAXK@Z` | `0xB7A80` | 63 | UnwindData |  |
| 285 | `?PutByte@CMemSerStream@@UEAAXE@Z` | `0xE19D0` | 78 | UnwindData |  |
| 260 | `??1CMemSerStream@@UEAA@XZ` | `0xF9BE0` | 53 | UnwindData |  |
| 257 | `??0CMemSerStream@@QEAA@PEAEK@Z` | `0xFE760` | 14,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `?SetProperty@CFullPropSpec@@QEAAHPEBG@Z` | `0x101F00` | 141 | UnwindData |  |
| 310 | `DllCanUnloadNow` | `0x107480` | 57 | UnwindData |  |
| 258 | `??0CUnNormalizer@@QEAA@XZ` | `0x10D750` | 6,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `PerfmonIDXCollect` | `0x10F1C0` | 588 | UnwindData |  |
| 320 | `PerfmonIDXOpen` | `0x110B00` | 114 | UnwindData |  |
| 263 | `CreatePropMapperStorage` | `0x129610` | 89 | UnwindData |  |
| 264 | `CreateSecurityStoreStorage` | `0x159050` | 223 | UnwindData |  |
| 312 | `DllRegisterServer` | `0x16A2A0` | 91 | UnwindData |  |
| 313 | `DllUnregisterServer` | `0x16A310` | 3,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `PerfmonClose` | `0x16B270` | 89 | UnwindData |  |
| 317 | `PerfmonCollect` | `0x16B2D0` | 426 | UnwindData |  |
| 318 | `PerfmonIDXClose` | `0x16B480` | 89 | UnwindData |  |
| 321 | `PerfmonOpen` | `0x16B4E0` | 90 | UnwindData |  |
| 254 | `??0CDriveInfo@@QEAA@PEBGK@Z` | `0x16BDC0` | 262 | UnwindData |  |
| 262 | `?ContainsDrive@CDriveInfo@@SAHPEBG@Z` | `0x16BED0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `?GetDiskSpace@CDriveInfo@@QEAAXAEA_J0@Z` | `0x16BF10` | 194 | UnwindData |  |
| 270 | `?GetDrive@CDriveInfo@@SAXPEBGPEAG@Z` | `0x16BFE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `?GetSectorSize@CDriveInfo@@QEAAKXZ` | `0x16C040` | 224 | UnwindData |  |
| 280 | `?IsSameDrive@CDriveInfo@@QEAAHPEBG@Z` | `0x16C130` | 46 | UnwindData |  |
| 281 | `?IsWriteProtected@CDriveInfo@@QEAAHXZ` | `0x16C170` | 500 | UnwindData |  |
| 255 | `??0CFullPath@@QEAA@PEBG@Z` | `0x16C3D0` | 98 | UnwindData |  |
| 282 | `?MakePath@CFullPath@@QEAAXPEBG@Z` | `0x16C6E0` | 67 | UnwindData |  |
| 261 | `CIState` | `0x183240` | 176 | UnwindData |  |
| 315 | `ForceMasterMerge` | `0x184290` | 161 | UnwindData |  |
| 309 | `?UnNormalizeKey@CUnNormalizer@@QEAAXAEBVCKeyBuf@@AEAUtagPROPVARIANT@@PEAGK@Z` | `0x187530` | 87 | UnwindData |  |
| 287 | `?PutDouble@CMemSerStream@@UEAAXN@Z` | `0x18AEA0` | 76 | UnwindData |  |
| 291 | `?PutString@CMemSerStream@@UEAAXPEBD@Z` | `0x18AF00` | 135 | UnwindData |  |
| 295 | `?PutWString@CMemSerStream@@UEAAXPEBG@Z` | `0x18AF90` | 139 | UnwindData |  |
| 269 | `?GetDouble@CMemDeSerStream@@UEAANXZ` | `0x18B7E0` | 63 | UnwindData |  |
| 275 | `?GetString@CMemDeSerStream@@UEAAPEADXZ` | `0x18B830` | 203 | UnwindData |  |
| 279 | `?GetWString@CMemDeSerStream@@UEAAPEAGXZ` | `0x18B910` | 270 | UnwindData |  |
| 283 | `?PeekULong@CMemDeSerStream@@UEAAKXZ` | `0x18BA30` | 48 | UnwindData |  |
| 299 | `?SkipBlob@CMemDeSerStream@@UEAAXK@Z` | `0x18BA70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `?SkipChar@CMemDeSerStream@@UEAAXK@Z` | `0x18BA70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `?SkipByte@CMemDeSerStream@@UEAAXXZ` | `0x18BAB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `?SkipDouble@CMemDeSerStream@@UEAAXXZ` | `0x18BAE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `?SkipFloat@CMemDeSerStream@@UEAAXXZ` | `0x18BB20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `?SkipLong@CMemDeSerStream@@UEAAXXZ` | `0x18BB20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `?SkipULong@CMemDeSerStream@@UEAAXXZ` | `0x18BB20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `?SkipGUID@CMemDeSerStream@@UEAAXXZ` | `0x18BB60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `?SkipUShort@CMemDeSerStream@@UEAAXXZ` | `0x18BBA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `?SkipWChar@CMemDeSerStream@@UEAAXK@Z` | `0x18BBD0` | 1,857,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `?CoTaskAllocator@@3VCCoTaskAllocator@@A` | `0x351418` | 0 | Indeterminate |  |
