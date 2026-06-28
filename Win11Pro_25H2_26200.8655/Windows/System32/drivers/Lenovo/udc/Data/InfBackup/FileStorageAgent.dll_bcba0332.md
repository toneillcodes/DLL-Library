# Binary Specification: FileStorageAgent.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Data\InfBackup\FileStorageAgent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bcba0332f2e5bc02bfc9e499550b752f4182b54485dfb563a95fe16dc1ad1b0d`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `?AbordPendingStorage@FileStorageAgent@@SAXXZ` | `0x1BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0FileStorageAgent@@QEAA@AEBV0@@Z` | `0x1BD0` | 77 | UnwindData |  |
| 14 | `?__autoclassinit2@FileStorageAgent@@QEAAX_K@Z` | `0x1C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0FileStorageAgent@@AEAA@XZ` | `0x1C30` | 712 | UnwindData |  |
| 3 | `??1FileStorageAgent@@AEAA@XZ` | `0x1F40` | 268 | UnwindData |  |
| 6 | `?CreateHash@FileStorageAgent@@AEAA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEBV23@@Z` | `0x2050` | 243 | UnwindData |  |
| 12 | `?UploadFile@FileStorageAgent@@QEAA?AW4StoragError@1@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@0AEAV34@0@Z` | `0x2150` | 6,064 | UnwindData |  |
| 9 | `?ReadUploadFile@FileStorageAgent@@AEAAXV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAV23@@Z` | `0x3A20` | 667 | UnwindData |  |
| 7 | `?GetFileSize@FileStorageAgent@@AEAAHV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x3D90` | 319 | UnwindData |  |
| 13 | `?UploadFile@FileStorageAgent@@QEAA?AW4StoragError@1@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV34@AEBV34@@Z` | `0x3ED0` | 984 | UnwindData |  |
| 8 | `?GetInstance@FileStorageAgent@@SAPEAV1@XZ` | `0x42B0` | 178 | UnwindData |  |
| 10 | `?UploadContent@FileStorageAgent@@AEAA?AW4StoragError@1@AEBV?$map@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V12@U?$less@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V12@@std@@@2@@std@@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@4@AEAV54@@Z` | `0x4370` | 1,724 | UnwindData |  |
| 11 | `?UploadDiagResult@FileStorageAgent@@QEAA?AW4StoragError@1@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@_N00@Z` | `0x4E90` | 3,008 | UnwindData |  |
| 4 | `?AbordFlag@FileStorageAgent@@0U?$atomic@_N@std@@A` | `0x10B40` | 0 | Indeterminate |  |
