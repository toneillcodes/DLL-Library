# Binary Specification: AppProvisioningagent.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Service\AppProvisioningagent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `15b26945200404a454714e2a6442986814a4c671b043358fd0053f3cc60680c1`
* **Total Exported Functions:** 60

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0AppProvisioningAgent@@IEAA@XZ` | `0x23E0` | 446 | UnwindData |  |
| 2 | `??0ComponentVersion@@QEAA@XZ` | `0x25A0` | 257 | UnwindData |  |
| 3 | `??1AppProvisioningAgent@@UEAA@XZ` | `0x2E20` | 165 | UnwindData |  |
| 6 | `?DoesItNeedToReportProgressNow@AppProvisioningAgent@@AEAA_NXZ` | `0x3380` | 136 | UnwindData |  |
| 7 | `?DownloadNInstallSoftwarePackage@AppProvisioningAgent@@AEAAKAEAVSoftwarePackage@@PEAX@Z` | `0x3410` | 5,259 | UnwindData |  |
| 8 | `?FullInit@AppProvisioningAgent@@UEAAXXZ` | `0x48A0` | 1,302 | UnwindData |  |
| 9 | `?GetAppInstallStatus@AppProvisioningAgent@@AEAAXAEAVSoftwareModule@@PEAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x4DC0` | 1,051 | UnwindData |  |
| 10 | `?GetAppsRedemptionCodes@AppProvisioningAgent@@UEAAKAEAVValue@Json@@@Z` | `0x51E0` | 2,290 | UnwindData |  |
| 11 | `?GetCurrentInstallingModule@AppProvisioningAgent@@AEAA?AVSoftwareModule@@XZ` | `0x5AE0` | 113 | UnwindData |  |
| 12 | `?GetCurrentInstallingSoftware@AppProvisioningAgent@@AEAA?AVSoftwarePackage@@XZ` | `0x5B60` | 113 | UnwindData |  |
| 13 | `?GetDownloadFiles@AppProvisioningAgent@@QEAAKAEAVValue@Json@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@1@Z` | `0x5BE0` | 984 | UnwindData |  |
| 14 | `?GetEntitledSoftware@AppProvisioningAgent@@UEAAKAEAVValue@Json@@AEAVComponentVersion@@@Z` | `0x5FC0` | 1,623 | UnwindData |  |
| 15 | `?GetEntitledSoftwareStatus@AppProvisioningAgent@@UEAAKAEAVValue@Json@@PEAX_N@Z` | `0x6620` | 1,019 | UnwindData |  |
| 16 | `?GetEntitledSoftwareStatusThreadRtn@AppProvisioningAgent@@QEAAXPEAVValue@Json@@PEAXH_N@Z` | `0x6A20` | 3,393 | UnwindData |  |
| 17 | `?GetHttpRequestHeaders@AppProvisioningAgent@@AEAA_NAEAV?$map@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V12@U?$less@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V12@@std@@@2@@std@@@Z` | `0x7770` | 480 | UnwindData |  |
| 18 | `?GetInstallEntitledSoftwareStatus@AppProvisioningAgent@@UEAAKAEAVValue@Json@@@Z` | `0x7950` | 1,491 | UnwindData |  |
| 19 | `?GetInstance@AppProvisioningAgent@@SAPEAV1@XZ` | `0x7F30` | 68 | UnwindData |  |
| 20 | `?GetModuleFileListNInstallationStatus@AppProvisioningAgent@@AEAAKAEAVSoftwareModule@@_NPEAX@Z` | `0x7F80` | 3,278 | UnwindData |  |
| 21 | `?GetPlainTextLicenses@AppProvisioningAgent@@AEAAXAEAVValue@Json@@AEBVEccEncryption@@@Z` | `0x8C50` | 3,778 | UnwindData |  |
| 22 | `?GetStrHttpRequestHeaders@AppProvisioningAgent@@AEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x9B20` | 760 | UnwindData |  |
| 23 | `?HasEntitledSoftware@AppProvisioningAgent@@UEAAKAEAEAEAVValue@Json@@AEAVComponentVersion@@@Z` | `0x9E20` | 716 | UnwindData |  |
| 24 | `?Init@AppProvisioningAgent@@UEAAXAEAPEAX@Z` | `0xA0F0` | 1,127 | UnwindData |  |
| 25 | `?InstallEntitledSoftware@AppProvisioningAgent@@UEAAKAEAVValue@Json@@PEAX_N@Z` | `0xA560` | 2,958 | UnwindData |  |
| 26 | `?InstallModule@AppProvisioningAgent@@AEAA?AW4ErrorCode@UDC@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0_NPEAX@Z` | `0xB0F0` | 3,983 | UnwindData |  |
| 27 | `?InstallPreinstallSoftware@AppProvisioningAgent@@EEAAXXZ` | `0xC080` | 223 | UnwindData |  |
| 28 | `?IsAPSCapable@AppProvisioningAgent@@AEAA_NXZ` | `0xC160` | 262 | UnwindData |  |
| 29 | `?JsonDeSerialize@ComponentVersion@@SA?AV1@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xC270` | 1,409 | UnwindData |  |
| 30 | `?JsonSerialize@ComponentVersion@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV1@@Z` | `0xC800` | 1,065 | UnwindData |  |
| 31 | `?OnDownloadComplete@AppProvisioningAgent@@AEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@U_GUID@@_N@Z` | `0xCC30` | 565 | UnwindData |  |
| 32 | `?OnFileDownloadError@AppProvisioningAgent@@AEAAXAEAV?$map@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@U?$less@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@std@@@2@@std@@AEAUErrorDetails@@AEA_N@Z` | `0xCE70` | 3,170 | UnwindData |  |
| 33 | `?OnFileDownloadProgress@AppProvisioningAgent@@AEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAUDownloadProgressDetail@@AEAV?$vector@UDownloadProgressDetail@@V?$allocator@UDownloadProgressDetail@@@std@@@3@@Z` | `0xDAE0` | 755 | UnwindData |  |
| 34 | `?OnUDCNotification@AppProvisioningAgent@@QEAAXAEAVUDCNotificationData@@@Z` | `0xDDE0` | 1,712 | UnwindData |  |
| 35 | `?ParseDownloadFilesResponseForRetry@AppProvisioningAgent@@AEAA_NAEAVValue@Json@@AEAKVLCPResponse@@@Z` | `0xE490` | 983 | UnwindData |  |
| 36 | `?ParseEntitledSoftwareResponseForRetry@AppProvisioningAgent@@AEAA_NAEAVValue@Json@@AEAKAEBVEccEncryption@@VLCPResponse@@@Z` | `0xE870` | 1,003 | UnwindData |  |
| 37 | `?ParseHasEntitlementResponseForRetry@AppProvisioningAgent@@AEAA_NAEAEAEAVValue@Json@@AEAKVLCPResponse@@@Z` | `0xEC60` | 1,263 | UnwindData |  |
| 38 | `?ParseRedemptionCodeResponse@AppProvisioningAgent@@AEAA_NAEAVValue@Json@@AEAKVLCPResponse@@@Z` | `0xF150` | 1,514 | UnwindData |  |
| 39 | `?PreinstallSoftwareThrdRtn@AppProvisioningAgent@@AEAAXXZ` | `0xF740` | 657 | UnwindData |  |
| 40 | `?ReportDownloadProgress@AppProvisioningAgent@@QEAAKV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0H000H0@Z` | `0xF9E0` | 2,339 | UnwindData |  |
| 41 | `?ReportDownloadProgressInternal@AppProvisioningAgent@@AEAAXAEAVSoftwareModule@@W4DownloadStatus@@HV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x10310` | 994 | UnwindData |  |
| 42 | `?ReportInstallProgress@AppProvisioningAgent@@QEAAKV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0H00@Z` | `0x10700` | 2,007 | UnwindData |  |
| 43 | `?ReportInstallProgressInternal@AppProvisioningAgent@@AEAAXAEAVSoftwareModule@@W4InstallStatus@@HV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x10EE0` | 595 | UnwindData |  |
| 44 | `?RequestDownload@AppProvisioningAgent@@AEAA?AVLCPResponse@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x11140` | 4,278 | UnwindData |  |
| 45 | `?RequestDownloadProgress@AppProvisioningAgent@@AEAA?AVLCPResponse@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0H000H0@Z` | `0x12200` | 6,315 | UnwindData |  |
| 46 | `?RequestEntitlement@AppProvisioningAgent@@AEAA?AVLCPResponse@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVComponentVersion@@@Z` | `0x13AB0` | 3,265 | UnwindData |  |
| 47 | `?RequestHasEntitlement@AppProvisioningAgent@@AEAA?AVLCPResponse@@AEAVComponentVersion@@@Z` | `0x14780` | 2,488 | UnwindData |  |
| 48 | `?RequestInstallProgress@AppProvisioningAgent@@AEAA?AVLCPResponse@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0H00@Z` | `0x15140` | 5,243 | UnwindData |  |
| 49 | `?RequestRedemptionCode@AppProvisioningAgent@@AEAA?AVLCPResponse@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@00@Z` | `0x165C0` | 4,303 | UnwindData |  |
| 50 | `?SetBaseUri@AppProvisioningAgent@@SAXAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x17690` | 45 | UnwindData |  |
| 51 | `?SetCurrentInstallingModule@AppProvisioningAgent@@AEAAXAEAVSoftwareModule@@@Z` | `0x177B0` | 79 | UnwindData |  |
| 52 | `?SetCurrentInstallingSoftware@AppProvisioningAgent@@AEAAXAEAVSoftwarePackage@@@Z` | `0x17800` | 79 | UnwindData |  |
| 53 | `?SetCurrentInstallingSoftwareStatus@AppProvisioningAgent@@AEAAXPEAG@Z` | `0x17850` | 103 | UnwindData |  |
| 54 | `?SetRealm@AppProvisioningAgent@@SAXAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x178C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `?SetRegistryEntitlementFlag@AppProvisioningAgent@@EEAAXE@Z` | `0x178F0` | 158 | UnwindData |  |
| 56 | `?UnInit@AppProvisioningAgent@@UEAAXXZ` | `0x17990` | 83 | UnwindData |  |
| 57 | `?__autoclassinit2@AppProvisioningAgent@@QEAAX_K@Z` | `0x18160` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?shouldRetry@AppProvisioningAgent@@AEAA_NAEBK@Z` | `0x18BC0` | 273 | UnwindData |  |
| 4 | `??_7AppProvisioningAgent@@6BIAppProvisioningAgent@@@` | `0x1D800` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??_7AppProvisioningAgent@@6BIUDCAgent@@@` | `0x1D850` | 51,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `?_serverUrl@AppProvisioningAgent@@0V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@A` | `0x2A000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `?_realm@AppProvisioningAgent@@0V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@A` | `0x2A020` | 0 | Indeterminate |  |
