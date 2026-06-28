# Binary Specification: tquery.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\tquery.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eca506dcc0bc7fb281d059460a918cc4d64323c3133c865ca4911eaf80db098a`
* **Total Exported Functions:** 69

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 298 | `?SetProperty@CFullPropSpec@@QEAAXK@Z` | `0x85B20` | 59 | UnwindData |  |
| 256 | `??0CFullPropSpec@@QEAA@AEBV0@@Z` | `0x86C30` | 74 | UnwindData |  |
| 259 | `??1CAllocStorageVariant@@IEAA@XZ` | `0x89DD0` | 3,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `?ResetType@CAllocStorageVariant@@IEAAXAEAVPMemoryAllocator@@@Z` | `0x8AA60` | 722 | UnwindData |  |
| 311 | `DllGetClassObject` | `0xA1EF0` | 239 | UnwindData |  |
| 314 | `ExternPropagateEventToOpenQueries` | `0xAA110` | 17 | UnwindData |  |
| 288 | `?PutFloat@CMemSerStream@@UEAAXM@Z` | `0xC8BD0` | 78 | UnwindData |  |
| 271 | `?GetFloat@CMemDeSerStream@@UEAAMXZ` | `0xC8C30` | 65 | UnwindData |  |
| 278 | `?GetWChar@CMemDeSerStream@@UEAAXPEAGK@Z` | `0xC8C80` | 106 | UnwindData |  |
| 294 | `?PutWChar@CMemSerStream@@UEAAXPEBGK@Z` | `0xC8CF0` | 101 | UnwindData |  |
| 284 | `?PutBlob@CMemSerStream@@UEAAXPEBEK@Z` | `0xC8D60` | 90 | UnwindData |  |
| 286 | `?PutChar@CMemSerStream@@UEAAXPEBDK@Z` | `0xC8DC0` | 88 | UnwindData |  |
| 265 | `?GetBlob@CMemDeSerStream@@UEAAXPEAEK@Z` | `0xC8E20` | 95 | UnwindData |  |
| 267 | `?GetChar@CMemDeSerStream@@UEAAXPEADK@Z` | `0xC8E90` | 95 | UnwindData |  |
| 290 | `?PutLong@CMemSerStream@@UEAAXJ@Z` | `0xC8F00` | 74 | UnwindData |  |
| 273 | `?GetLong@CMemDeSerStream@@UEAAJXZ` | `0xC8F50` | 63 | UnwindData |  |
| 276 | `?GetULong@CMemDeSerStream@@UEAAKXZ` | `0xC8FA0` | 61 | UnwindData |  |
| 293 | `?PutUShort@CMemSerStream@@UEAAXG@Z` | `0xC8FF0` | 75 | UnwindData |  |
| 289 | `?PutGUID@CMemSerStream@@UEAAXAEBU_GUID@@@Z` | `0xC9050` | 80 | UnwindData |  |
| 266 | `?GetByte@CMemDeSerStream@@UEAAEXZ` | `0xC90B0` | 82 | UnwindData |  |
| 277 | `?GetUShort@CMemDeSerStream@@UEAAGXZ` | `0xC9110` | 63 | UnwindData |  |
| 272 | `?GetGUID@CMemDeSerStream@@UEAAXAEAU_GUID@@@Z` | `0xC9160` | 80 | UnwindData |  |
| 292 | `?PutULong@CMemSerStream@@UEAAXK@Z` | `0xC91C0` | 63 | UnwindData |  |
| 285 | `?PutByte@CMemSerStream@@UEAAXE@Z` | `0xE0330` | 78 | UnwindData |  |
| 260 | `??1CMemSerStream@@UEAA@XZ` | `0xF4BA0` | 53 | UnwindData |  |
| 257 | `??0CMemSerStream@@QEAA@PEAEK@Z` | `0xFB300` | 19,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `?SetProperty@CFullPropSpec@@QEAAHPEBG@Z` | `0xFFE60` | 141 | UnwindData |  |
| 310 | `DllCanUnloadNow` | `0x1050A0` | 57 | UnwindData |  |
| 258 | `??0CUnNormalizer@@QEAA@XZ` | `0x10B860` | 7,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `PerfmonIDXCollect` | `0x10D5A0` | 588 | UnwindData |  |
| 320 | `PerfmonIDXOpen` | `0x10EF10` | 114 | UnwindData |  |
| 263 | `CreatePropMapperStorage` | `0x1284E0` | 89 | UnwindData |  |
| 312 | `DllRegisterServer` | `0x16DBB0` | 91 | UnwindData |  |
| 313 | `DllUnregisterServer` | `0x16DC20` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `PerfmonClose` | `0x16EB70` | 89 | UnwindData |  |
| 317 | `PerfmonCollect` | `0x16EBD0` | 426 | UnwindData |  |
| 318 | `PerfmonIDXClose` | `0x16ED80` | 89 | UnwindData |  |
| 321 | `PerfmonOpen` | `0x16EDE0` | 90 | UnwindData |  |
| 254 | `??0CDriveInfo@@QEAA@PEBGK@Z` | `0x16F6C0` | 262 | UnwindData |  |
| 262 | `?ContainsDrive@CDriveInfo@@SAHPEBG@Z` | `0x16F7D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `?GetDiskSpace@CDriveInfo@@QEAAXAEA_J0@Z` | `0x16F810` | 194 | UnwindData |  |
| 270 | `?GetDrive@CDriveInfo@@SAXPEBGPEAG@Z` | `0x16F8E0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `?GetSectorSize@CDriveInfo@@QEAAKXZ` | `0x16F940` | 224 | UnwindData |  |
| 280 | `?IsSameDrive@CDriveInfo@@QEAAHPEBG@Z` | `0x16FA30` | 46 | UnwindData |  |
| 281 | `?IsWriteProtected@CDriveInfo@@QEAAHXZ` | `0x16FA70` | 500 | UnwindData |  |
| 255 | `??0CFullPath@@QEAA@PEBG@Z` | `0x16FCD0` | 98 | UnwindData |  |
| 282 | `?MakePath@CFullPath@@QEAAXPEBG@Z` | `0x16FFE0` | 67 | UnwindData |  |
| 264 | `CreateSecurityStoreStorage` | `0x1712B0` | 273 | UnwindData |  |
| 261 | `CIState` | `0x1871B0` | 176 | UnwindData |  |
| 315 | `ForceMasterMerge` | `0x188200` | 161 | UnwindData |  |
| 309 | `?UnNormalizeKey@CUnNormalizer@@QEAAXAEBVCKeyBuf@@AEAUtagPROPVARIANT@@PEAGK@Z` | `0x18CBA0` | 87 | UnwindData |  |
| 287 | `?PutDouble@CMemSerStream@@UEAAXN@Z` | `0x190AF0` | 76 | UnwindData |  |
| 291 | `?PutString@CMemSerStream@@UEAAXPEBD@Z` | `0x190B50` | 135 | UnwindData |  |
| 295 | `?PutWString@CMemSerStream@@UEAAXPEBG@Z` | `0x190BE0` | 139 | UnwindData |  |
| 269 | `?GetDouble@CMemDeSerStream@@UEAANXZ` | `0x191430` | 63 | UnwindData |  |
| 275 | `?GetString@CMemDeSerStream@@UEAAPEADXZ` | `0x191480` | 203 | UnwindData |  |
| 279 | `?GetWString@CMemDeSerStream@@UEAAPEAGXZ` | `0x191560` | 270 | UnwindData |  |
| 283 | `?PeekULong@CMemDeSerStream@@UEAAKXZ` | `0x191680` | 48 | UnwindData |  |
| 299 | `?SkipBlob@CMemDeSerStream@@UEAAXK@Z` | `0x1916C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `?SkipChar@CMemDeSerStream@@UEAAXK@Z` | `0x1916C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `?SkipByte@CMemDeSerStream@@UEAAXXZ` | `0x191700` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `?SkipDouble@CMemDeSerStream@@UEAAXXZ` | `0x191730` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `?SkipFloat@CMemDeSerStream@@UEAAXXZ` | `0x191770` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `?SkipLong@CMemDeSerStream@@UEAAXXZ` | `0x191770` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `?SkipULong@CMemDeSerStream@@UEAAXXZ` | `0x191770` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `?SkipGUID@CMemDeSerStream@@UEAAXXZ` | `0x1917B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `?SkipUShort@CMemDeSerStream@@UEAAXXZ` | `0x1917F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `?SkipWChar@CMemDeSerStream@@UEAAXK@Z` | `0x191820` | 2,018,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `?CoTaskAllocator@@3VCCoTaskAllocator@@A` | `0x37E418` | 0 | Indeterminate |  |
