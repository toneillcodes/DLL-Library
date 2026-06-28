# Binary Specification: EventDataLogging.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Service\EventDataLogging.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `68a433b9112bb908e7ee663823635f745c80c34c507201621129c854d342584a`
* **Total Exported Functions:** 44

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `exports_LogItemContext` | `0x100A` | 25 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `?ToDbFile@EventDataLogging@UDC@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV34@0@Z` | `0x1023` | 10 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `?GetDeviceContext@EventDataLogging@UDC@@QEAAHAEAV?$list@VDeviceContext@@V?$allocator@VDeviceContext@@@std@@@std@@@Z` | `0x102D` | 25 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `?GetDatabase@EventDataLogging@UDC@@QEAA?AV?$shared_ptr@VDatabase@UDC@@@std@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@4@_N1@Z` | `0x1046` | 10 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `?LogItemEvent@EventDataLogging@UDC@@UEAAHAEBVItemEvent@@@Z` | `0x1050` | 35 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `?GetLastItemContext@EventDataLogging@UDC@@QEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVItemContext@@@Z` | `0x1073` | 100 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `exports_GetLastItemEvent` | `0x10D7` | 85 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `?LogDeviceContext@EventDataLogging@UDC@@QEAAHAEBVDeviceContext@@@Z` | `0x112C` | 5 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `exports_GetItemEvents` | `0x1131` | 30 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `?GetItemContext@EventDataLogging@UDC@@QEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV?$list@VItemContext@@V?$allocator@VItemContext@@@std@@@4@@Z` | `0x114F` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `exports_GetDeviceContext` | `0x1163` | 10 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `?GetInstance@EventDataLogging@UDC@@SAPEAV12@XZ` | `0x116D` | 60 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??1EventDataLogging@UDC@@UEAA@XZ` | `0x11A9` | 45 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?GetLastDeviceContext@EventDataLogging@UDC@@UEAAHAEAVDeviceContext@@W4EGetDBPathMethod@utility@2@@Z` | `0x11D6` | 45 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?GetItemEvents@EventDataLogging@UDC@@QEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV?$list@VItemEvent@@V?$allocator@VItemEvent@@@std@@@4@@Z` | `0x1203` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?GetDatasetContext@EventDataLogging@UDC@@QEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV?$list@VDatasetContext@@V?$allocator@VDatasetContext@@@std@@@4@@Z` | `0x1217` | 15 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `?GetLastItemEventWithItemId@EventDataLogging@UDC@@QEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0AEAVItemEvent@@W4EGetDBPathMethod@utility@2@@Z` | `0x1226` | 15 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `?GetLastDatasetContextN@EventDataLogging@UDC@@QEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV?$list@VDatasetContext@@V?$allocator@VDatasetContext@@@std@@@4@W4EGetDBPathMethod@utility@2@H@Z` | `0x1235` | 25 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `exports_GetLastDeviceContext` | `0x124E` | 25 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `exports_GetDatasetContext` | `0x1267` | 25 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `exports_LogDeviceContext` | `0x1280` | 50 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `?GetFirstID@EventDataLogging@UDC@@QEAAHV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0W4EGetDBPathMethod@utility@2@@Z` | `0x12B2` | 10 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?GetLastDatasetContext@EventDataLogging@UDC@@UEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVDatasetContext@@W4EGetDBPathMethod@utility@2@@Z` | `0x12BC` | 90 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `exports_GetLastItemContext` | `0x1316` | 15 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `?GetLastID@EventDataLogging@UDC@@QEAAHV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0W4EGetDBPathMethod@utility@2@@Z` | `0x1325` | 45 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `?LogDatasetContext@EventDataLogging@UDC@@UEAAHAEBVDatasetContext@@@Z` | `0x1352` | 5 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `?GetLastItemEvent@EventDataLogging@UDC@@UEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVItemEvent@@@Z` | `0x1357` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0EventDataLogging@UDC@@IEAA@XZ` | `0x137F` | 10 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `exports_GetLastDatasetContext` | `0x1389` | 65 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `?GetLastItemEventWithItemIdN@EventDataLogging@UDC@@QEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0AEAV?$list@VItemEvent@@V?$allocator@VItemEvent@@@std@@@4@HW4EGetDBPathMethod@utility@2@@Z` | `0x13CA` | 25 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??4EventDataLogging@UDC@@QEAAAEAV01@AEBV01@@Z` | `0x13E3` | 5 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `?UpdateItemDataEncryted@EventDataLogging@UDC@@QEAA_NHHW4EGetDBPathMethod@utility@2@@Z` | `0x13E8` | 25 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `exports_LogDatasetContext` | `0x1401` | 25 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `?mark_integrity_check_all@EventDataLogging@UDC@@QEAAXXZ` | `0x141A` | 55 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `?GetLastLogtime@EventDataLogging@UDC@@QEAA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@4@0W4EGetDBPathMethod@utility@2@@Z` | `0x1451` | 25 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0EventDataLogging@UDC@@QEAA@AEBV01@@Z` | `0x146A` | 90 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `?GetDatasetId@EventDataLogging@UDC@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV34@@Z` | `0x14C4` | 25 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `?LogItemContext@EventDataLogging@UDC@@QEAAHAEBVItemContext@@@Z` | `0x14DD` | 35 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `?GetLastItemEventN@EventDataLogging@UDC@@QEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV?$list@VItemEvent@@V?$allocator@VItemEvent@@@std@@@4@W4EGetDBPathMethod@utility@2@H@Z` | `0x1500` | 15 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?Init@EventDataLogging@UDC@@AEAA_NXZ` | `0x150F` | 20 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `exports_GetItemContext` | `0x1523` | 55 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `?integrity_check_all@EventDataLogging@UDC@@QEAAXXZ` | `0x155A` | 25 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `exports_LogItemEvent` | `0x1573` | 128,605 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??_7EventDataLogging@UDC@@6B@` | `0x20BD0` | 0 | Indeterminate |  |
