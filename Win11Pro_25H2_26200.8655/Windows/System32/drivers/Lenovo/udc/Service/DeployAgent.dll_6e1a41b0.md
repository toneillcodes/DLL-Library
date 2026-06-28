# Binary Specification: DeployAgent.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Service\DeployAgent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6e1a41b0ba61fb529a5038a5a648a214692a095dcac26382df6f6c7df9f28698`
* **Total Exported Functions:** 516

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 191 | `?GetInstallAgent@InstallAgentFactory@@QEAAPEAUIInstallAgent@@XZ` | `0x1A60` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `?GetPluginInstaller@PluginInstallerFactory@@QEAAPEAUIPluginInstaller@@XZ` | `0x1A60` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??0UpdateUtility@@AEAA@XZ` | `0x28E0` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??4NotificationAlertUtility@@QEAAAEAV0@$$QEAV0@@Z` | `0x28E0` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `??4NotificationAlertUtility@@QEAAAEAV0@AEBV0@@Z` | `0x28E0` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??4UpdateUtility@@QEAAAEAV0@AEBV0@@Z` | `0x28E0` | 1,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `??4InstallAgentFactory@@QEAAAEAV0@AEBV0@@Z` | `0x2D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??4PluginInstallerFactory@@QEAAAEAV0@AEBV0@@Z` | `0x2D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0DeployAgent@@IEAA@XZ` | `0x2D20` | 472 | UnwindData |  |
| 3 | `??0ForceUpdate@@QEAA@AEBV0@@Z` | `0x30F0` | 92 | UnwindData |  |
| 5 | `??0ForceUpdate@@QEAA@XZ` | `0x3150` | 33 | UnwindData |  |
| 8 | `??0NormalUpdate@@QEAA@AEBV0@@Z` | `0x3180` | 92 | UnwindData |  |
| 10 | `??0NormalUpdate@@QEAA@XZ` | `0x31E0` | 33 | UnwindData |  |
| 11 | `??0PackageEx@@QEAA@AEBV0@@Z` | `0x3740` | 821 | UnwindData |  |
| 14 | `??0PackageManifestManager@@QEAA@$$QEAV0@@Z` | `0x4330` | 124 | UnwindData |  |
| 15 | `??0PackageManifestManager@@QEAA@AEBV0@@Z` | `0x43B0` | 73 | UnwindData |  |
| 16 | `??0PackageManifestManager@@QEAA@XZ` | `0x4400` | 64 | UnwindData |  |
| 17 | `??0PluginInstaller@@IEAA@XZ` | `0x4440` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0PluginInstaller@@QEAA@AEBV0@@Z` | `0x4440` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??0UpdateTypeBase@@QEAA@AEBV0@@Z` | `0x4680` | 82 | UnwindData |  |
| 30 | `??1DeployAgent@@UEAA@XZ` | `0x57E0` | 355 | UnwindData |  |
| 31 | `??1ForceUpdate@@UEAA@XZ` | `0x5A80` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??1NormalUpdate@@UEAA@XZ` | `0x5A80` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??1UpdateTypeBase@@UEAA@XZ` | `0x5A80` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??1PackageManifestManager@@QEAA@XZ` | `0x5CD0` | 34 | UnwindData |  |
| 33 | `??1InstallAgentFactory@@AEAA@XZ` | `0x5DD0` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??1PluginInstallerFactory@@AEAA@XZ` | `0x5DD0` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `??1UpdateUtility@@QEAA@XZ` | `0x5DD0` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??4ForceUpdate@@QEAAAEAV0@AEBV0@@Z` | `0x6830` | 91 | UnwindData |  |
| 48 | `??4NormalUpdate@@QEAAAEAV0@AEBV0@@Z` | `0x6830` | 91 | UnwindData |  |
| 56 | `??4UpdateTypeBase@@QEAAAEAV0@AEBV0@@Z` | `0x6830` | 91 | UnwindData |  |
| 46 | `??4InstallAgent@@QEAAAEAV0@AEAV0@@Z` | `0x6890` | 28 | UnwindData |  |
| 53 | `??4PluginInstaller@@QEAAAEAV0@AEAV0@@Z` | `0x6890` | 28 | UnwindData |  |
| 51 | `??4PackageManifestManager@@QEAAAEAV0@$$QEAV0@@Z` | `0x6ED0` | 127 | UnwindData |  |
| 52 | `??4PackageManifestManager@@QEAAAEAV0@AEBV0@@Z` | `0x6F50` | 86 | UnwindData |  |
| 68 | `??_FS3LinkRetryStrategy@retry_strategies@UDC@@QEAAXXZ` | `0x8840` | 1,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `?FullInit@DeployAgent@@UEAAXXZ` | `0x8EB0` | 1,655 | UnwindData |  |
| 194 | `?GetInstance@DeployAgent@@SAPEAV1@XZ` | `0x9530` | 158 | UnwindData |  |
| 200 | `?GetManifest@PackageManifestManager@@QEAA?AVPackageManifest@@XZ` | `0x95D0` | 79 | UnwindData |  |
| 238 | `?GetRetryInfo@S3LinkRetryStrategy@retry_strategies@UDC@@QEBAAEBURetryInfo@123@XZ` | `0x9620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `?GetUpdateStatus@DeployAgent@@UEAAXAEAVUDCNotificationData@@@Z` | `0x9630` | 105 | UnwindData |  |
| 265 | `?HandleRunTimeZDUTrigger@DeployAgent@@QEAAXXZ` | `0x96A0` | 180 | UnwindData |  |
| 273 | `?Init@DeployAgent@@UEAAXAEAPEAX@Z` | `0x9760` | 1,144 | UnwindData |  |
| 357 | `?OnUDCNotification@DeployAgent@@QEAAXAEAVUDCNotificationData@@@Z` | `0x9BE0` | 6,712 | UnwindData |  |
| 358 | `?OnZDUCompleted@DeployAgent@@QEAAXXZ` | `0xB620` | 361 | UnwindData |  |
| 364 | `?RegisterDevice@DeployAgent@@AEAAXXZ` | `0xB790` | 628 | UnwindData |  |
| 378 | `?RenamePackageRepoToPackageIdIfAny@DeployAgent@@AEAAXXZ` | `0xBA10` | 1,100 | UnwindData |  |
| 437 | `?SpawnVoluntaryUpdateThread@DeployAgent@@AEAAXV?$shared_ptr@VUpdateManager@@@std@@W4UpdateScope@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@3@22@Z` | `0xBE60` | 773 | UnwindData |  |
| 438 | `?StartCommonUpdateThread@DeployAgent@@UEAA_NJJ@Z` | `0xC170` | 449 | UnwindData |  |
| 439 | `?StartDeployThread@DeployAgent@@EEAAXXZ` | `0xC340` | 227 | UnwindData |  |
| 441 | `?StartScheduleUpdateThread@DeployAgent@@UEAA_NJJ@Z` | `0xC430` | 461 | UnwindData |  |
| 444 | `?StopCommonUpdateThread@DeployAgent@@UEAAXXZ` | `0xC660` | 91 | UnwindData |  |
| 445 | `?StopDeployThreads@DeployAgent@@EEAAXXZ` | `0xC6C0` | 246 | UnwindData |  |
| 446 | `?StopDeployTimerThreads@DeployAgent@@EEAAXXZ` | `0xC7C0` | 141 | UnwindData |  |
| 450 | `?StopScheduleUpdateThread@DeployAgent@@UEAAXXZ` | `0xC850` | 100 | UnwindData |  |
| 460 | `?TriggerZDU@DeployAgent@@QEAAXXZ` | `0xC8C0` | 575 | UnwindData |  |
| 467 | `?UnInit@DeployAgent@@UEAAXXZ` | `0xCB00` | 141 | UnwindData |  |
| 476 | `?UninstalllAllPackages@DeployAgent@@UEAA_NXZ` | `0xCD90` | 160 | UnwindData |  |
| 393 | `?Run@UpdateTypeBase@@UEAA_NXZ` | `0xF170` | 5,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 500 | `?__autoclassinit2@DeployAgent@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `?__autoclassinit2@DeviceInfoProvider@UDC@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `?__autoclassinit2@ForceUpdate@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `?__autoclassinit2@InstallAgentFactory@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `?__autoclassinit2@NormalUpdate@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `?__autoclassinit2@PackageEx@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 506 | `?__autoclassinit2@PackageManifestManager@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 507 | `?__autoclassinit2@PluginInstallerFactory@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `?__autoclassinit2@S3LinkRetryStrategy@retry_strategies@UDC@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `?__autoclassinit2@UDCHelperFactory@udc@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 510 | `?__autoclassinit2@UdcStatusManager@UDC@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `?__autoclassinit2@UpdateManager@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `?__autoclassinit2@UpdateTypeBase@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | `?__autoclassinit2@ZDUUpdateManager@UDC@@QEAAX_K@Z` | `0x10580` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0S3LinkRetryStrategy@retry_strategies@UDC@@QEAA@AEBV012@@Z` | `0x134E0` | 176 | UnwindData |  |
| 21 | `??0S3LinkRetryStrategy@retry_strategies@UDC@@QEAA@PEAVLog@2@@Z` | `0x13590` | 167 | UnwindData |  |
| 39 | `??1S3LinkRetryStrategy@retry_strategies@UDC@@QEAA@XZ` | `0x13640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?BackOffDelayForRetryStrategyLow@S3LinkRetryStrategy@retry_strategies@UDC@@IEAAX_K@Z` | `0x13650` | 86 | UnwindData |  |
| 270 | `?IncrementRetriesExpired@S3LinkRetryStrategy@retry_strategies@UDC@@QEAAXXZ` | `0x136B0` | 56 | UnwindData |  |
| 328 | `?IsRetriesExceeded@S3LinkRetryStrategy@retry_strategies@UDC@@QEAA_NXZ` | `0x136F0` | 70 | UnwindData |  |
| 385 | `?ResetStrategy@S3LinkRetryStrategy@retry_strategies@UDC@@QEAAXXZ` | `0x13740` | 126 | UnwindData |  |
| 390 | `?RetryNow@S3LinkRetryStrategy@retry_strategies@UDC@@QEAA_NAEAURetryState@123@@Z` | `0x137C0` | 107 | UnwindData |  |
| 480 | `?UpdateCurrentBackoffDelay@S3LinkRetryStrategy@retry_strategies@UDC@@AEAA_NXZ` | `0x13830` | 460 | UnwindData |  |
| 7 | `??0InstallAgentFactory@@AEAA@XZ` | `0x13A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??0PluginInstallerFactory@@AEAA@XZ` | `0x13A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `?GetInstance@InstallAgentFactory@@SAPEAV1@XZ` | `0x13A10` | 108 | UnwindData |  |
| 406 | `?SetInstallAgent@InstallAgentFactory@@QEAAXPEAUIInstallAgent@@@Z` | `0x13A80` | 2,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `?SetPluginInstaller@PluginInstallerFactory@@QEAAXPEAUIPluginInstaller@@@Z` | `0x13A80` | 2,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0InstallAgent@@IEAA@XZ` | `0x14490` | 58 | UnwindData |  |
| 32 | `??1InstallAgent@@MEAA@XZ` | `0x14650` | 42 | UnwindData |  |
| 145 | `?DoesFileExists@InstallAgent@@MEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x14890` | 21 | UnwindData |  |
| 180 | `?GetCatalogInstallName@InstallAgent@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV23@0@Z` | `0x148B0` | 515 | UnwindData |  |
| 187 | `?GetFilePathIfExists@InstallAgent@@MEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV23@0@Z` | `0x14AC0` | 1,687 | UnwindData |  |
| 195 | `?GetInstance@InstallAgent@@SAPEAV1@XZ` | `0x15160` | 144 | UnwindData |  |
| 261 | `?HandleInstallationResult@InstallAgent@@MEAAHPEAVPackageEx@@W4InstallResult@UDC@@HHHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x151F0` | 1,851 | UnwindData |  |
| 282 | `?InstallPackage@InstallAgent@@UEAA_NPEAVPackageEx@@W4UpdateScope@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAX@Z` | `0x15B20` | 611 | UnwindData |  |
| 288 | `?InstallSecurityCatalog@InstallAgent@@UEAA_NPEAVPackageEx@@@Z` | `0x15D90` | 5,082 | UnwindData |  |
| 289 | `?InstallZipfile@InstallAgent@@IEAA_NPEAVPackageEx@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4UpdateScope@@1PEAX@Z` | `0x17170` | 2,824 | UnwindData |  |
| 290 | `?Installfile@InstallAgent@@IEAA_NPEAVPackageEx@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4UpdateScope@@1PEAX@Z` | `0x17C80` | 5,893 | UnwindData |  |
| 298 | `?IsCatalogInstalled@InstallAgent@@AEAA_NPEAXAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x19390` | 139 | UnwindData |  |
| 344 | `?LaunchInstallation@InstallAgent@@MEAAHV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@00_NPEAXPEAVPackageEx@@0@Z` | `0x19420` | 2,325 | UnwindData |  |
| 345 | `?LaunchInstallationInSystemSession@InstallAgent@@MEAAHV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0_NPEAXPEAVPackageEx@@0@Z` | `0x19D40` | 1,329 | UnwindData |  |
| 346 | `?LaunchInstallationInUserSession@InstallAgent@@MEAAHV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0PEAXPEAVPackageEx@@0@Z` | `0x1A280` | 957 | UnwindData |  |
| 350 | `?NotifyInstallSlotWaiters@InstallAgent@@QEAAXXZ` | `0x1A640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `?UnInstallPackage@InstallAgent@@UEAA_NPEAVPackageEx@@W4UpdateScope@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAX@Z` | `0x1A650` | 611 | UnwindData |  |
| 472 | `?UnInstallfile@InstallAgent@@IEAA_NPEAVPackageEx@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4UpdateScope@@1PEAX@Z` | `0x1A8C0` | 5,562 | UnwindData |  |
| 475 | `?UninstallSecurityCatalog@InstallAgent@@UEAA_NPEAVPackageEx@@@Z` | `0x1BE80` | 1,116 | UnwindData |  |
| 477 | `?UnzipPackageCabFile@InstallAgent@@MEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x1C2E0` | 23 | UnwindData |  |
| 489 | `?ValidateInstallScript@InstallAgent@@MEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@_N@Z` | `0x1C300` | 10,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0DeviceInfoProvider@UDC@@QEAA@XZ` | `0x1EC80` | 502 | UnwindData |  |
| 12 | `??0PackageEx@@QEAA@AEBVPackage@@PEAX@Z` | `0x1F160` | 382 | UnwindData |  |
| 13 | `??0PackageEx@@QEAA@PEAX@Z` | `0x1F2E0` | 349 | UnwindData |  |
| 22 | `??0UDCHelperFactory@udc@@QEAA@AEBV01@@Z` | `0x1F440` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??1PackageEx@@QEAA@XZ` | `0x1FD10` | 114 | UnwindData |  |
| 40 | `??1UdcStatusManager@UDC@@QEAA@XZ` | `0x1FE30` | 392 | UnwindData |  |
| 55 | `??4UDCHelperFactory@udc@@QEAAAEAV01@AEBV01@@Z` | `0x20040` | 369 | UnwindData |  |
| 71 | `?AddToRepository@PackageEx@@UEAA_N_N@Z` | `0x215E0` | 2,012 | UnwindData |  |
| 72 | `?AreUpdatesAllowedByPolicy@PackageEx@@UEAA?AW4DownloadPolicy@1@XZ` | `0x21DC0` | 1,065 | UnwindData |  |
| 75 | `?ChecKAndDeletePackage@PackageEx@@QEAA_NXZ` | `0x221F0` | 503 | UnwindData |  |
| 79 | `?CheckAndRecoverPartialExtraction@PackageEx@@QEAA_NXZ` | `0x223F0` | 815 | UnwindData |  |
| 80 | `?CheckAndUpdatePackageStatus@PackageEx@@QEAAXXZ` | `0x22720` | 1,392 | UnwindData |  |
| 85 | `?CheckForHashOrSetupValidation@PackageEx@@QEAA_NXZ` | `0x22C90` | 1,108 | UnwindData |  |
| 86 | `?CheckForLimitedPackageRetention@PackageEx@@QEAA_NXZ` | `0x230F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `?CheckProcessingCancelled@PackageEx@@QEAA_NPEAX_K@Z` | `0x23100` | 328 | UnwindData |  |
| 97 | `?CheckProcessingCancelled@PackageEx@@UEAA_NPEAX@Z` | `0x23250` | 1,219 | UnwindData |  |
| 112 | `?ClearCleanedUpDueToDiskFullOrCancellationFlag@PackageEx@@QEAAXXZ` | `0x23720` | 600 | UnwindData |  |
| 114 | `?ClearPendingInstallationDetails@PackageEx@@UEAA_NXZ` | `0x23980` | 730 | UnwindData |  |
| 117 | `?CloseEventHandles@PackageEx@@QEAAXXZ` | `0x23C60` | 44 | UnwindData |  |
| 122 | `?CreateTempDownloadFolder@PackageEx@@UEAAXXZ` | `0x267D0` | 429 | UnwindData |  |
| 123 | `?CreateTempDownloadZDUFolder@PackageEx@@QEAAXXZ` | `0x26980` | 426 | UnwindData |  |
| 125 | `?DelayDownloadProcess@PackageEx@@QEAA?AW4DownloadDelayResult@1@XZ` | `0x26B30` | 1,744 | UnwindData |  |
| 126 | `?DeleteDownloadProgressKey@PackageEx@@QEAAXXZ` | `0x27200` | 584 | UnwindData |  |
| 127 | `?DeleteExcessPackageFilesIfLimitedRetentionForNotApplicable@PackageEx@@AEAAXXZ` | `0x27450` | 1,624 | UnwindData |  |
| 129 | `?DeletePackageRegStatusKey@PackageEx@@QEAAXXZ` | `0x27AB0` | 1,083 | UnwindData |  |
| 130 | `?DeletePackageRepositoryFolder@PackageEx@@QEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x27EF0` | 2,310 | UnwindData |  |
| 132 | `?DeletePartialDownloadedZduFile@PackageEx@@QEAA_NXZ` | `0x28800` | 352 | UnwindData |  |
| 133 | `?DeleteRegistryKeyFromPackagesPath@PackageEx@@QEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@_N@Z` | `0x28960` | 2,622 | UnwindData |  |
| 135 | `?DeleteTempDownloadFolder@PackageEx@@UEAAXXZ` | `0x293A0` | 1,603 | UnwindData |  |
| 140 | `?DeserializeForCmd@PackageEx@@SA_NV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAVPackage@@@Z` | `0x299F0` | 1,000 | UnwindData |  |
| 141 | `?DeserializeForUpdateCmd@PackageEx@@SA_NV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAV?$list@VPackage@@V?$allocator@VPackage@@@std@@@3@@Z` | `0x29DE0` | 1,322 | UnwindData |  |
| 142 | `?DeserializePackageEx@PackageEx@@CAXVValue@Json@@AEAVPackage@@@Z` | `0x2A310` | 4,682 | UnwindData |  |
| 144 | `?DoPropertiesMatch@PackageEx@@QEAA_NPEAV1@@Z` | `0x2B560` | 2,978 | UnwindData |  |
| 146 | `?DoesInstallScriptOrManifestExist@PackageEx@@QEAA_NXZ` | `0x2C110` | 599 | UnwindData |  |
| 150 | `?DoesPackageContainBundledManifestFile@PackageEx@@UEAA_NXZ` | `0x2C370` | 107 | UnwindData |  |
| 151 | `?DoesPackageContainsInstallScript@PackageEx@@UEAA_NXZ` | `0x2C3E0` | 729 | UnwindData |  |
| 162 | `?ExtractPackage@PackageEx@@UEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@_N0@Z` | `0x2C6C0` | 6,107 | UnwindData |  |
| 168 | `?GetAdditionalInstallStatus@PackageEx@@AEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x2DEA0` | 6,162 | UnwindData |  |
| 169 | `?GetAdditionalOnDemandTags@PackageEx@@QEAA?AV?$list@V?$KeyValuePair@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@@V?$allocator@V?$KeyValuePair@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@@@std@@@std@@XZ` | `0x2F6C0` | 33 | UnwindData |  |
| 175 | `?GetAppFliterHash@PackageEx@@AEAA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@XZ` | `0x2F6F0` | 689 | UnwindData |  |
| 177 | `?GetAttemptedInstallStringVersion@PackageEx@@QEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x2F9B0` | 215 | UnwindData |  |
| 178 | `?GetAttemptedInstallVersion@PackageEx@@QEAA_NAEAVVersion@@@Z` | `0x2FA90` | 215 | UnwindData |  |
| 179 | `?GetBundledManifestPath@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x2FB70` | 1,510 | UnwindData |  |
| 189 | `?GetFiletypeExtension@PackageEx@@UEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x30160` | 715 | UnwindData |  |
| 192 | `?GetInstallContext@PackageEx@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x30430` | 33 | UnwindData |  |
| 201 | `?GetManifestType@PackageEx@@QEAA?AW4ManifestFileType@1@_N@Z` | `0x30460` | 2,658 | UnwindData |  |
| 202 | `?GetMaxInstallationTime@PackageEx@@QEAAHXZ` | `0x30ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `?GetPackageDeleteCount@PackageEx@@QEAAKXZ` | `0x30EE0` | 1,162 | UnwindData |  |
| 206 | `?GetPackageDownloadProgressKeyPath@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x31370` | 551 | UnwindData |  |
| 207 | `?GetPackageExecutionState@PackageEx@@QEAA?AW4PackageExecutionState@1@XZ` | `0x315A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `?GetPackageFilePath@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x315B0` | 733 | UnwindData |  |
| 214 | `?GetPackageManifestFilePath@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@_N@Z` | `0x31890` | 1,041 | UnwindData |  |
| 215 | `?GetPackageManifestMgr@PackageEx@@QEAAPEAVPackageManifestManager@@XZ` | `0x31CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `?GetPackageRegPath@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V23@@Z` | `0x31CC0` | 490 | UnwindData |  |
| 220 | `?GetPackageRepositoryFolderInOldFormat@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@_N@Z` | `0x31EB0` | 1,127 | UnwindData |  |
| 222 | `?GetPackageS3Link@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x32320` | 33 | UnwindData |  |
| 223 | `?GetPackageStateValueFromReg@PackageEx@@QEAA?AW4PackageState@@XZ` | `0x32350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `?GetPackageUpdateScope@PackageEx@@UEAA?AW4UpdateScope@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@_N@Z` | `0x32360` | 2,988 | UnwindData |  |
| 231 | `?GetRepositoryFolderPath@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@_N@Z` | `0x32F10` | 1,093 | UnwindData |  |
| 232 | `?GetRepositoryManifestFilePath@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x33360` | 785 | UnwindData |  |
| 233 | `?GetRepositoryPackageFilePath@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x33680` | 1,365 | UnwindData |  |
| 234 | `?GetRetryCountForFailedInstallation@PackageEx@@QEAAHXZ` | `0x33BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `?GetRetryCountForFailedInstallationFromReg@PackageEx@@QEAAHXZ` | `0x33BF0` | 431 | UnwindData |  |
| 236 | `?GetRetryCountForS3Link@PackageEx@@QEAAHXZ` | `0x33DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `?GetS3LinkRetryStrategyState@PackageEx@@QEAA_NAEAURetryState@S3LinkRetryStrategy@retry_strategies@UDC@@@Z` | `0x33DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `?GetState@PackageEx@@QEAA?AW4EventState@@XZ` | `0x33DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `?GetStringVersionFromRegistry@PackageEx@@QEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V23@@Z` | `0x33DD0` | 584 | UnwindData |  |
| 243 | `?GetTempDownloadFolder@PackageEx@@UEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x34020` | 282 | UnwindData |  |
| 244 | `?GetTempDownloadedFilePath@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x34140` | 1,401 | UnwindData |  |
| 245 | `?GetTempDownloadedManifestFilePath@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x346C0` | 799 | UnwindData |  |
| 246 | `?GetTempDownloadedZDUFilePath@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x349E0` | 722 | UnwindData |  |
| 247 | `?GetTempExtractedFolder@PackageEx@@UEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x34CC0` | 282 | UnwindData |  |
| 248 | `?GetTimeoutRetryCountFromReg@PackageEx@@QEAAHXZ` | `0x34DE0` | 431 | UnwindData |  |
| 253 | `?GetVersionFromRegistry@PackageEx@@QEAA_NAEAVVersion@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x34F90` | 548 | UnwindData |  |
| 254 | `?GetVersionFromRegistryStatusPath@PackageEx@@QEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V23@@Z` | `0x351C0` | 559 | UnwindData |  |
| 256 | `?GetZDUPackageFilePath@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x353F0` | 560 | UnwindData |  |
| 258 | `?GetZDUTempExtractedFolder@PackageEx@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x35620` | 279 | UnwindData |  |
| 263 | `?HandleNotificationForNotApplicablePackage@PackageEx@@QEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x35740` | 2,602 | UnwindData |  |
| 267 | `?HasPlugins@PackageEx@@UEAA_NXZ` | `0x36170` | 453 | UnwindData |  |
| 268 | `?HasSecurityCatalogs@PackageEx@@QEAA_NXZ` | `0x36340` | 553 | UnwindData |  |
| 271 | `?IncrementRetryCountForS3Link@PackageEx@@QEAAXXZ` | `0x36570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `?IncrementS3LinkRetryStrategyState@PackageEx@@QEAAXXZ` | `0x36580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `?InitEventHandles@PackageEx@@QEAAXXZ` | `0x36590` | 40 | UnwindData |  |
| 297 | `?IsCancelOperationReceived@PackageEx@@QEBA_NXZ` | `0x365C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `?IsCleanedUpDueToDiskFullOrCancellation@PackageEx@@QEAA_NPEAK@Z` | `0x365D0` | 1,439 | UnwindData |  |
| 303 | `?IsCriticalOrSecurityUpdate@PackageEx@@QEAA_NXZ` | `0x36B70` | 32 | UnwindData |  |
| 307 | `?IsFileCached@PackageEx@@UEAA_NXZ` | `0x36D60` | 162 | UnwindData |  |
| 308 | `?IsInstallCompleted@PackageEx@@QEAA_NXZ` | `0x36E10` | 637 | UnwindData |  |
| 309 | `?IsInstalledPackageToBeForcedInstall@PackageEx@@QEAA_NW4UpdateScope@@@Z` | `0x37090` | 38 | UnwindData |  |
| 310 | `?IsInstalledWithRelaxedVersion@PackageEx@@UEAA_NAEA_N@Z` | `0x370C0` | 2,316 | UnwindData |  |
| 313 | `?IsManifestSigned@PackageEx@@UEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@_N@Z` | `0x379D0` | 2,989 | UnwindData |  |
| 314 | `?IsMqttForceInstallCmd@PackageEx@@QEAA_NXZ` | `0x38580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `?IsOnDemandInstall@PackageEx@@QEBA_NXZ` | `0x38590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `?IsPackageDownloaded@PackageEx@@QEAA_NXZ` | `0x385A0` | 568 | UnwindData |  |
| 318 | `?IsPackageGreaterThanInstalled@PackageEx@@UEAA_NXZ` | `0x387E0` | 695 | UnwindData |  |
| 319 | `?IsPackageIdVersionAndFilterAreSame@PackageEx@@AEAA_NXZ` | `0x38AA0` | 3,876 | UnwindData |  |
| 320 | `?IsPackageInstallToBeResumed@PackageEx@@QEAA_NXZ` | `0x399D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `?IsPackageInstalled@PackageEx@@UEAA_NXZ` | `0x399E0` | 114 | UnwindData |  |
| 322 | `?IsPendingInstallation@PackageEx@@QEAA_NXZ` | `0x39A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `?IsPreviousExtractionConsistent@PackageEx@@QEAA_NAEAJ0@Z` | `0x39A70` | 799 | UnwindData |  |
| 324 | `?IsPreviousInstallationFailOrInvalid@PackageEx@@QEAA_N_N@Z` | `0x39D90` | 412 | UnwindData |  |
| 325 | `?IsReadyForProcessing@PackageEx@@QEAA_NXZ` | `0x39F30` | 355 | UnwindData |  |
| 326 | `?IsRegistrationStatusKeySet@PackageEx@@AEAA_NXZ` | `0x3A0A0` | 1,322 | UnwindData |  |
| 327 | `?IsRetentionOrFailedValidationSet@PackageEx@@QEAA_NXZ` | `0x3A5D0` | 34 | UnwindData |  |
| 332 | `?IsS3LinkRetriesExceeded@PackageEx@@QEAA_NXZ` | `0x3A600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `?IsSameVersionInstalled@PackageEx@@UEAA_N_N@Z` | `0x3A610` | 694 | UnwindData |  |
| 335 | `?IsTempFolderEmpty@PackageEx@@QEAA_NXZ` | `0x3A8D0` | 704 | UnwindData |  |
| 336 | `?IsThereAnErrorInPackageProcessing@PackageEx@@QEAA_NXZ` | `0x3AB90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `?IsUDCPackage@PackageEx@@UEAA_N_N@Z` | `0x3ABC0` | 278 | UnwindData |  |
| 338 | `?IsUDCPkgInstallPendingForSameVersion@PackageEx@@UEAA_NXZ` | `0x3ACE0` | 1,235 | UnwindData |  |
| 339 | `?IsUDCStandalonePackage@PackageEx@@QEAA_N_N@Z` | `0x3B1C0` | 732 | UnwindData |  |
| 340 | `?IsUDCVersionInstalled@PackageEx@@UEAA_NXZ` | `0x3B4A0` | 1,672 | UnwindData |  |
| 341 | `?IsUninstallAction@PackageEx@@QEAA_NXZ` | `0x3BB30` | 569 | UnwindData |  |
| 342 | `?IsWaiting@PackageEx@@QEAA_NXZ` | `0x3BD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `?IsWindowsCompliant@PackageEx@@UEAA_NXZ` | `0x3BD80` | 22 | UnwindData |  |
| 351 | `?NotifyLCP1@PackageEx@@UEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@IH0@Z` | `0x3BF40` | 1,546 | UnwindData |  |
| 352 | `?NotifyLCP@PackageEx@@UEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@E0@Z` | `0x3C550` | 438 | UnwindData |  |
| 356 | `?OnPackageEvent@PackageEx@@QEAAXW4PackageState@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x3C710` | 4,176 | UnwindData |  |
| 359 | `?PersisteAndNotifyPkgStatus@PackageEx@@QEAAXW4PackageState@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x3D950` | 2,500 | UnwindData |  |
| 362 | `?ReadRegistryForPolicy@PackageEx@@UEAAKAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x3E320` | 229 | UnwindData |  |
| 366 | `?RegisterPackageInstallation@PackageEx@@UEAAXXZ` | `0x3E410` | 4,494 | UnwindData |  |
| 367 | `?RegisterPackageInstallationFailed@PackageEx@@UEAAXXZ` | `0x3F5A0` | 3,822 | UnwindData |  |
| 368 | `?RegisterPendingInstallation@PackageEx@@UEAAXW4UpdateScope@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x40490` | 4,285 | UnwindData |  |
| 373 | `?RegisterUpdateDetails@PackageEx@@UEAAXW4UpdateScope@@@Z` | `0x41550` | 25 | UnwindData |  |
| 376 | `?RemoveNonStatusPackageDetails@PackageEx@@QEAAX_N@Z` | `0x41570` | 210 | UnwindData |  |
| 377 | `?RemovePackageDetailsFromRegistry@PackageEx@@QEAAX_N@Z` | `0x41650` | 260 | UnwindData |  |
| 380 | `?ReportAdditionalStatus@PackageEx@@QEAA_NXZ` | `0x41760` | 2,520 | UnwindData |  |
| 383 | `?ResetRetryCountForS3Link@PackageEx@@QEAAXXZ` | `0x42140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `?ResetS3LinkRetryStrategyState@PackageEx@@QEAAXXZ` | `0x42150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `?ResetTimeoutRetryCountInReg@PackageEx@@QEAAXXZ` | `0x42160` | 385 | UnwindData |  |
| 397 | `?Set@PackageEx@@QEAAXAEBVPackage@@@Z` | `0x422F0` | 3,802 | UnwindData |  |
| 398 | `?SetAdditionalTags@PackageEx@@QEAAXAEBV?$list@V?$KeyValuePair@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@@V?$allocator@V?$KeyValuePair@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@@@std@@@std@@@Z` | `0x431D0` | 315 | UnwindData |  |
| 399 | `?SetAppFilterInRegistry@PackageEx@@AEAAXXZ` | `0x43310` | 1,160 | UnwindData |  |
| 401 | `?SetCancelOperation@PackageEx@@QEAAX_N@Z` | `0x437A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `?SetCleanedUpDueToDiskFullOrCancellationFlag@PackageEx@@QEAAXW4CleanupFlagValue@1@@Z` | `0x437B0` | 566 | UnwindData |  |
| 405 | `?SetDownloadProgressKey@PackageEx@@QEAAXH@Z` | `0x439F0` | 490 | UnwindData |  |
| 407 | `?SetInstallContext@PackageEx@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x43BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `?SetLCPNotification@PackageEx@@QEAAX_N@Z` | `0x43C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `?SetMaxInstallationTime@PackageEx@@QEAAXAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x43C10` | 35 | UnwindData |  |
| 411 | `?SetMqttForceInstallCmd@PackageEx@@QEAAX_N@Z` | `0x43C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `?SetOnDemandInstall@PackageEx@@QEAAX_N@Z` | `0x43C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `?SetPackageExecutionState@PackageEx@@QEAAXW4PackageExecutionState@1@@Z` | `0x43C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `?SetPackageInstallToBeResumed@PackageEx@@QEAAX_N@Z` | `0x43C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `?SetPackageS3Link@PackageEx@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x43C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `?SetPackageStateRegValue@PackageEx@@QEAAXW4PackageState@@@Z` | `0x43CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `?SetPendingInstallation@PackageEx@@QEAAX_N@Z` | `0x43CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 423 | `?SetRetryCountForFailedInstallation@PackageEx@@QEAAXH@Z` | `0x43CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 427 | `?SetState@PackageEx@@UEAAXW4EventState@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x43CD0` | 163 | UnwindData |  |
| 428 | `?SetTimeoutRetryCountInReg@PackageEx@@QEAAXH@Z` | `0x43D80` | 288 | UnwindData |  |
| 429 | `?SetUpdateCancel@PackageEx@@QEAAXXZ` | `0x43EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `?SetWaiting@PackageEx@@QEAAX_N@Z` | `0x43EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `?ShouldDeletePackage@PackageEx@@QEAA_NXZ` | `0x43ED0` | 488 | UnwindData |  |
| 434 | `?ShouldIgnoreManifestValidation@PackageEx@@QEAA_NXZ` | `0x440C0` | 768 | UnwindData |  |
| 435 | `?ShouldRetryOnHashFailure@PackageEx@@QEAA_NXZ` | `0x443C0` | 1,101 | UnwindData |  |
| 436 | `?ShouldSkipInstallOfPackage@PackageEx@@QEAA_NAEAW4UpdateScope@@@Z` | `0x44810` | 862 | UnwindData |  |
| 452 | `?StorePreviousRetentionValue@PackageEx@@QEAA_NXZ` | `0x44B70` | 1,145 | UnwindData |  |
| 481 | `?UpdatePackageDetails@PackageEx@@UEAAXXZ` | `0x45810` | 1,627 | UnwindData |  |
| 482 | `?UpdatePackageDetailsFromModernManifest@PackageEx@@QEAAXXZ` | `0x45E70` | 2,046 | UnwindData |  |
| 483 | `?UpdatePackageStateInRegistry@PackageEx@@QEAAXW4PackageState@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@111@Z` | `0x46670` | 4,436 | UnwindData |  |
| 484 | `?UpdateRegParamsForInvalidPackage@PackageEx@@QEAAXXZ` | `0x477D0` | 4,089 | UnwindData |  |
| 490 | `?ValidatePackage@PackageEx@@UEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x487D0` | 1,094 | UnwindData |  |
| 491 | `?ValidatePackageHash@PackageEx@@QEAA_NXZ` | `0x48C20` | 2,741 | UnwindData |  |
| 495 | `?VerifyManifest@PackageEx@@UEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAH_N@Z` | `0x496E0` | 2,434 | UnwindData |  |
| 496 | `?VerifyManifestAndValidateWithPackage@PackageEx@@UEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAH@Z` | `0x4A070` | 1,675 | UnwindData |  |
| 499 | `?WasInstallAtemptedForSameVersion@PackageEx@@UEAA_NXZ` | `0x4A700` | 838 | UnwindData |  |
| 515 | `?findUdcDriverInPackage@PackageEx@@AEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0_N@Z` | `0x4E1C0` | 1,356 | UnwindData |  |
| 138 | `?Deserialize@PackageManifestManager@@QEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x4FA20` | 6,034 | UnwindData |  |
| 347 | `?Load@PackageManifestManager@@QEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV23@@Z` | `0x511C0` | 895 | UnwindData |  |
| 486 | `?Validate@PackageManifestManager@@QEAA_NAEBVPackage@@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x51BC0` | 346 | UnwindData |  |
| 494 | `?Verify@PackageManifestManager@@QEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x51D20` | 571 | UnwindData |  |
| 37 | `??1PluginInstaller@@UEAA@XZ` | `0x52790` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `?CleanupLockFiles@PluginInstaller@@AEAAXXZ` | `0x528C0` | 1,399 | UnwindData |  |
| 109 | `?CleanupPluginDataDirectory@PluginInstaller@@SAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAX@Z` | `0x52E40` | 819 | UnwindData |  |
| 120 | `?CreateLockerForPluginInstallation@PluginInstaller@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV23@@Z` | `0x53180` | 2,125 | UnwindData |  |
| 134 | `?DeleteRegistryKeyFromPluginPath@PluginInstaller@@AEAAXAEBVPluginDetails@UDC@@@Z` | `0x539D0` | 3,473 | UnwindData |  |
| 172 | `?GetAllInstalledPluginManifests@PluginInstaller@@MEAAHAEAV?$list@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@std@@PEAX@Z` | `0x54770` | 466 | UnwindData |  |
| 197 | `?GetInstance@PluginInstaller@@SAPEAV1@XZ` | `0x54950` | 108 | UnwindData |  |
| 198 | `?GetInstance@PluginInstallerFactory@@SAPEAV1@XZ` | `0x549C0` | 108 | UnwindData |  |
| 284 | `?InstallPendingPlugins@PluginInstaller@@UEAA_NPEAX@Z` | `0x54A30` | 3,082 | UnwindData |  |
| 286 | `?InstallPlugin@PluginInstaller@@AEAA_NAEBVPluginDetails@UDC@@PEAVPackageEx@@PEAX_N@Z` | `0x55640` | 4,473 | UnwindData |  |
| 287 | `?InstallPlugins@PluginInstaller@@UEAA_NPEAVPackageEx@@PEAX@Z` | `0x567C0` | 4,828 | UnwindData |  |
| 361 | `?PromotePendingPluginToActive@PluginInstaller@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x57AA0` | 2,255 | UnwindData |  |
| 379 | `?ReplaceAndLaunchImmediately@PluginInstaller@@IEAA_NPEAVPackageEx@@PEAXAEBVPluginDetails@UDC@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x58370` | 3,770 | UnwindData |  |
| 382 | `?ResetLock@PluginInstaller@@AEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x59230` | 63 | UnwindData |  |
| 448 | `?StopPlugins@PluginInstaller@@UEAAXXZ` | `0x592F0` | 35 | UnwindData |  |
| 449 | `?StopPluginsAndSetEvent@PluginInstaller@@AEAAXPEAVPluginManager@UDC@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAX@Z` | `0x59320` | 80 | UnwindData |  |
| 464 | `?TryDeletingPlugin@PluginInstaller@@UEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0PEAX@Z` | `0x59370` | 185 | UnwindData |  |
| 470 | `?UnInstallPlugin@PluginInstaller@@AEAA_NAEBVPluginDetails@UDC@@PEAVPackageEx@@PEAX@Z` | `0x59430` | 1,173 | UnwindData |  |
| 471 | `?UnInstallPlugins@PluginInstaller@@UEAA_NPEAVPackageEx@@PEAX@Z` | `0x598D0` | 3,054 | UnwindData |  |
| 23 | `??0UpdateManager@@QEAA@AEAVUpdatePolicy@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x5E400` | 79 | UnwindData |  |
| 24 | `??0UpdateManager@@QEAA@XZ` | `0x5E450` | 928 | UnwindData |  |
| 41 | `??1UpdateManager@@QEAA@XZ` | `0x5F0A0` | 944 | UnwindData |  |
| 69 | `?AddPackageToProcessingThread@UpdateManager@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAVPackageEx@@@Z` | `0x60A30` | 888 | UnwindData |  |
| 70 | `?AddPairToIdUrlMap@UpdateManager@@AEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x60DB0` | 384 | UnwindData |  |
| 74 | `?CancelPackages@UpdateManager@@QEAAXAEBV?$list@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@std@@@Z` | `0x60F30` | 2,445 | UnwindData |  |
| 77 | `?CheckAndCancelIfThePackageNotFoundInConfig@UpdateManager@@IEAAXAEBV?$list@VPackage@@V?$allocator@VPackage@@@std@@@std@@@Z` | `0x618C0` | 1,092 | UnwindData |  |
| 78 | `?CheckAndDeleteCorruptedPackages@UpdateManager@@AEAAXAEAV?$list@VPackage@@V?$allocator@VPackage@@@std@@@std@@@Z` | `0x61D10` | 2,953 | UnwindData |  |
| 84 | `?CheckForCancellation@UpdateManager@@IEAA_NPEAVPackageEx@@@Z` | `0x628A0` | 59 | UnwindData |  |
| 87 | `?CheckForPackagesToDeleteOrUninstall@UpdateManager@@IEAAXAEBV?$list@VPackage@@V?$allocator@VPackage@@@std@@@std@@@Z` | `0x628E0` | 9,091 | UnwindData |  |
| 91 | `?CheckPackageCanBeDownloaded@UpdateManager@@IEAA_NPEAVPackageEx@@@Z` | `0x64C70` | 698 | UnwindData |  |
| 92 | `?CheckPackageCanbeEnqueued@UpdateManager@@IEAA_NPEAVPackageEx@@W4UpdateScope@@@Z` | `0x64F30` | 5,664 | UnwindData |  |
| 93 | `?CheckPackageInQ@UpdateManager@@MEAAPEAVPackageEx@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x66550` | 40 | UnwindData |  |
| 98 | `?CheckProcessingStatus@UpdateManager@@QEAAXXZ` | `0x665F0` | 1,873 | UnwindData |  |
| 105 | `?CleanUpPackagesMarkedForDeletion@UpdateManager@@IEAAXXZ` | `0x66D50` | 497 | UnwindData |  |
| 106 | `?CleanUpPluginDetailsInRegistry@UpdateManager@@IEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@_N@Z` | `0x66F50` | 1,176 | UnwindData |  |
| 107 | `?Cleanup@UpdateManager@@QEAAXXZ` | `0x673F0` | 95 | UnwindData |  |
| 110 | `?CleanupRemnantFilesWorker@UpdateManager@@QEAAXXZ` | `0x67450` | 3,335 | UnwindData |  |
| 113 | `?ClearIdUrlMap@UpdateManager@@AEAAXXZ` | `0x68160` | 29 | UnwindData |  |
| 115 | `?ClearQueue@UpdateManager@@IEAAXXZ` | `0x681E0` | 1,213 | UnwindData |  |
| 119 | `?CreateBitsJobDescription@UpdateManager@@IEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAVPackageEx@@@Z` | `0x686A0` | 1,546 | UnwindData |  |
| 121 | `?CreateRegistrationStatusKeyForInstalledPackagesInRegistry@UpdateManager@@AEAAXXZ` | `0x68CB0` | 1,389 | UnwindData |  |
| 137 | `?DequeuePackage@UpdateManager@@UEAA_NPEAVPackageEx@@_N@Z` | `0x69220` | 2,967 | UnwindData |  |
| 139 | `?DeserializeAndHandleOnDemandOperation@UpdateManager@@IEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x69DC0` | 3,820 | UnwindData |  |
| 143 | `?DoProcessing@UpdateManager@@QEAAXXZ` | `0x6AD20` | 3,178 | UnwindData |  |
| 147 | `?DoesListContain@UpdateManager@@IEAA_NAEBV?$list@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@std@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@3@@Z` | `0x6B990` | 20 | UnwindData |  |
| 148 | `?DoesListContain@UpdateManager@@IEAA_NAEBV?$list@VPackageEx@@V?$allocator@VPackageEx@@@std@@@std@@AEAVPackageEx@@@Z` | `0x6BA40` | 50 | UnwindData |  |
| 152 | `?DoesPackageRepositoryExists@UpdateManager@@IEAA_NPEAVPackageEx@@@Z` | `0x6BA80` | 665 | UnwindData |  |
| 154 | `?DownloadPackage@UpdateManager@@IEAA_NPEAVPackageEx@@@Z` | `0x6BD20` | 5,233 | UnwindData |  |
| 155 | `?DownloadPackageManifest@UpdateManager@@IEAA_NPEAVPackageEx@@@Z` | `0x6D1A0` | 3,156 | UnwindData |  |
| 156 | `?DownloadPackageS3Link@UpdateManager@@MEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV23@AEAUInvokeHttpResponse@UDCCore@@PEAVPackageEx@@@Z` | `0x6DE00` | 4,080 | UnwindData |  |
| 158 | `?EnqueuePackage@UpdateManager@@UEAA_NPEAVPackage@@_N1AEBV?$list@V?$KeyValuePair@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@@V?$allocator@V?$KeyValuePair@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@@@std@@@std@@@Z` | `0x6EDF0` | 992 | UnwindData |  |
| 159 | `?EnqueuePackage@UpdateManager@@UEAA_NPEAVPackageEx@@@Z` | `0x6F1D0` | 6,383 | UnwindData |  |
| 160 | `?EraseFromIdUrlMap@UpdateManager@@AEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x70AC0` | 130 | UnwindData |  |
| 164 | `?FinishPendingUpdateForPackage@UpdateManager@@QEAA_NAEAVPackageEx@@AEAW4UpdateScope@@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x70B50` | 4,584 | UnwindData |  |
| 165 | `?FinishPendingUpdates@UpdateManager@@QEAA_NXZ` | `0x71D40` | 332 | UnwindData |  |
| 170 | `?GetAllInstalledPackageIdsFromRegistry@UpdateManager@@MEAA_NAEAV?$vector@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@std@@@Z` | `0x71E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `?GetAnyPendingInstallationDetails@UpdateManager@@MEAA_NAEAVPackageEx@@AEAW4UpdateScope@@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x71EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `?GetDiskFreeSpaceInGb@UpdateManager@@MEAAKXZ` | `0x71EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `?GetFullyDownloadedLazyInstallPackages@UpdateManager@@QEAAXAEAV?$list@VPackage@@V?$allocator@VPackage@@@std@@@std@@@Z` | `0x71ED0` | 1,195 | UnwindData |  |
| 204 | `?GetPackageDetailsFromRegistry@UpdateManager@@MEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVPackage@@AEAV23@@Z` | `0x72380` | 96 | UnwindData |  |
| 209 | `?GetPackageFromQueueUsingUrl@UpdateManager@@MEAAPEAVPackageEx@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x723E0` | 342 | UnwindData |  |
| 210 | `?GetPackageIdFromIdUrlMap@UpdateManager@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV23@@Z` | `0x72540` | 214 | UnwindData |  |
| 228 | `?GetPluginsFromPackagesInConfig@UpdateManager@@AEAAXAEBV?$list@VPackage@@V?$allocator@VPackage@@@std@@@std@@AEAV?$set@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@U?$less@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@3@@Z` | `0x72680` | 2,257 | UnwindData |  |
| 252 | `?GetUpdateTypeFromConfig@UpdateManager@@MEAA?AW4UpdateScope@@XZ` | `0x72F60` | 33 | UnwindData |  |
| 264 | `?HandlePendingDownload@UpdateManager@@AEAAXXZ` | `0x72F90` | 2,093 | UnwindData |  |
| 266 | `?HandleStartOperationCommand@UpdateManager@@QEAAXAEAV?$list@VPackage@@V?$allocator@VPackage@@@std@@@std@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@3@V?$list@V?$KeyValuePair@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@@V?$allocator@V?$KeyValuePair@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@@@std@@@3@@Z` | `0x737C0` | 3,747 | UnwindData |  |
| 274 | `?Init@UpdateManager@@QEAAXAEAVUpdatePolicy@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x74670` | 697 | UnwindData |  |
| 275 | `?InitConfig@UpdateManager@@QEAAXAEAVUpdatePolicy@@_N@Z` | `0x74930` | 3,204 | UnwindData |  |
| 285 | `?InstallPendingPlugins@UpdateManager@@QEAA_NXZ` | `0x755C0` | 47 | UnwindData |  |
| 291 | `?InvokeInstall@UpdateManager@@MEAA_NPEAVPackageEx@@W4UpdateScope@@@Z` | `0x755F0` | 5,748 | UnwindData |  |
| 294 | `?InvokeRollback@UpdateManager@@IEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x76C70` | 6,626 | UnwindData |  |
| 295 | `?InvokeUninstall@UpdateManager@@MEAA_NPEAVPackageEx@@W4UpdateScope@@@Z` | `0x78660` | 1,464 | UnwindData |  |
| 296 | `?InvokeUpdate@UpdateManager@@IEAA_NPEAVPackageEx@@W4UpdateScope@@@Z` | `0x78C20` | 7,588 | UnwindData |  |
| 299 | `?IsCheckProcessingStatusThreadExited@UpdateManager@@IEAA_NXZ` | `0x7A9D0` | 107 | UnwindData |  |
| 302 | `?IsConfigUpdated@UpdateManager@@AEAA_NXZ` | `0x7AA40` | 184 | UnwindData |  |
| 304 | `?IsDNSErrorOccurred@UpdateManager@@QEAA_NXZ` | `0x7AB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `?IsDownloadProgressFlagSet@UpdateManager@@IEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV23@@Z` | `0x7AB10` | 1,516 | UnwindData |  |
| 311 | `?IsLastUpdateRollback@UpdateManager@@IEAA_NXZ` | `0x7B100` | 430 | UnwindData |  |
| 348 | `?LogAndHandleInstallBlockedByApplicabilityOrPolicy@UpdateManager@@IEAAXPEAVPackageEx@@_NW4DownloadPolicy@2@@Z` | `0x7B2B0` | 640 | UnwindData |  |
| 349 | `?NetworkCertificateErrorOccurred@UpdateManager@@QEAA_NXZ` | `0x7B530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `?OnFileDownloadComplete@UpdateManager@@IEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@U_GUID@@_NAEAV?$map@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@U?$less@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@std@@@2@@3@@Z` | `0x7B540` | 2,046 | UnwindData |  |
| 354 | `?OnFileDownloadError@UpdateManager@@IEAAXAEAV?$map@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@U?$less@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V12@@std@@@2@@std@@AEAUErrorDetails@@AEA_N@Z` | `0x7BD40` | 5,397 | UnwindData |  |
| 355 | `?OnFileDownloadProgress@UpdateManager@@IEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAUDownloadProgressDetail@@AEAV?$vector@UDownloadProgressDetail@@V?$allocator@UDownloadProgressDetail@@@std@@@3@@Z` | `0x7D260` | 2,118 | UnwindData |  |
| 360 | `?ProcessPackage@UpdateManager@@IEAAXPEAVPackageEx@@@Z` | `0x7DAB0` | 4,996 | UnwindData |  |
| 363 | `?ReapPackageProcessingStateAndRunPendingReEnqueue@UpdateManager@@AEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x7EE40` | 650 | UnwindData |  |
| 370 | `?RegisterPendingReEnqueueAfterStopIncomplete@UpdateManager@@AEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x7F0D0` | 345 | UnwindData |  |
| 375 | `?RemoveDuplicatePackagesFromList@UpdateManager@@AEAAXAEAV?$list@VPackage@@V?$allocator@VPackage@@@std@@@std@@@Z` | `0x7F230` | 1,305 | UnwindData |  |
| 388 | `?RetainOnlyRequiredFiles@UpdateManager@@IEAA_NPEAVPackageEx@@@Z` | `0x7F750` | 1,597 | UnwindData |  |
| 394 | `?SchedulePackageProcessingCompletionFollowUp@UpdateManager@@AEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x7FD90` | 270 | UnwindData |  |
| 403 | `?SetDNSErrorStatus@UpdateManager@@QEAAX_N@Z` | `0x7FEA0` | 79 | UnwindData |  |
| 404 | `?SetDownloadProgress@UpdateManager@@QEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@E@Z` | `0x7FEF0` | 174 | UnwindData |  |
| 413 | `?SetNetworkCertificateErrorStatus@UpdateManager@@QEAAX_N@Z` | `0x7FFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `?SetUpdatePolicy@UpdateManager@@UEAAXAEAVUpdatePolicy@@@Z` | `0x7FFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `?StopAllPlugins@UpdateManager@@IEAAX_N@Z` | `0x7FFC0` | 60 | UnwindData |  |
| 443 | `?StopAndCleanUpPlugins@UpdateManager@@IEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV?$set@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@U?$less@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@3@@Z` | `0x80000` | 5,849 | UnwindData |  |
| 447 | `?StopIfPackageProcessingThreadCompleted@UpdateManager@@IEAA?AW4PackageProcessingStopResult@1@PEAVPackageEx@@_NJ1@Z` | `0x816E0` | 2,853 | UnwindData |  |
| 451 | `?StopUpdateWorker@UpdateManager@@QEAAXXZ` | `0x82210` | 267 | UnwindData |  |
| 453 | `?Subscribe@UpdateManager@@QEAAXV?$function@$$A6A_NJJ@Z@std@@0V?$function@$$A6AXXZ@3@1@Z` | `0x82320` | 214 | UnwindData |  |
| 454 | `?SuspendPackageProcessing@UpdateManager@@IEAAXPEAVPackageEx@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x82400` | 1,811 | UnwindData |  |
| 455 | `?TriggerCommonUpdatePolicyChange@UpdateManager@@QEAAXXZ` | `0x82B20` | 83 | UnwindData |  |
| 457 | `?TriggerPowerStateChange@UpdateManager@@QEAAXXZ` | `0x82B80` | 75 | UnwindData |  |
| 458 | `?TriggerScheduleUpdatePolicyChange@UpdateManager@@QEAAXXZ` | `0x82BD0` | 85 | UnwindData |  |
| 459 | `?TriggerVoluntaryUpdate@UpdateManager@@QEAAXW4UpdateScope@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@11@Z` | `0x82C30` | 6,784 | UnwindData |  |
| 465 | `?TryDownloadPackageS3Link@UpdateManager@@IEAA?AW4S3LinkRetryResult@1@PEAVPackageEx@@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x846B0` | 3,391 | UnwindData |  |
| 466 | `?TryReEnqueuePackageFromCurrentPolicy@UpdateManager@@AEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x853F0` | 989 | UnwindData |  |
| 473 | `?UninstallAllPackages@UpdateManager@@IEAA_N_N@Z` | `0x857D0` | 1,611 | UnwindData |  |
| 474 | `?UninstallAllPackagesAndPlugins@UpdateManager@@QEAA_N_N@Z` | `0x85E20` | 89 | UnwindData |  |
| 479 | `?UpdateCleanupFlagsPostFullInit@UpdateManager@@IEAAXXZ` | `0x85E80` | 1,334 | UnwindData |  |
| 497 | `?WaitForCheckProcessingStatus@UpdateManager@@AEAAXXZ` | `0x863C0` | 206 | UnwindData |  |
| 4 | `??0ForceUpdate@@QEAA@PEAVPackageEx@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4UpdateScope@@@Z` | `0x886D0` | 33 | UnwindData |  |
| 9 | `??0NormalUpdate@@QEAA@PEAVPackageEx@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4UpdateScope@@@Z` | `0x88700` | 33 | UnwindData |  |
| 25 | `??0UpdateTypeBase@@IEAA@PEAVPackageEx@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4UpdateScope@@@Z` | `0x88960` | 124 | UnwindData |  |
| 26 | `??0UpdateTypeBase@@IEAA@XZ` | `0x889E0` | 96 | UnwindData |  |
| 100 | `?CheckUpdatePolicy@ForceUpdate@@UEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAVUpdatePolicy@@@Z` | `0x88B50` | 23 | UnwindData |  |
| 101 | `?CheckUpdatePolicy@NormalUpdate@@UEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAVUpdatePolicy@@@Z` | `0x88B50` | 23 | UnwindData |  |
| 102 | `?CheckUpdatePolicy@UpdateTypeBase@@UEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAVUpdatePolicy@@@Z` | `0x88B70` | 244 | UnwindData |  |
| 124 | `?CreateUpdateType@UpdateTypeBase@@SAPEAV1@PEAVPackageEx@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4UpdateScope@@PEAX@Z` | `0x88C70` | 784 | UnwindData |  |
| 277 | `?Initialize@ForceUpdate@@UEAAXPEAVPackageEx@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4UpdateScope@@PEAX@Z` | `0x88F80` | 83 | UnwindData |  |
| 278 | `?Initialize@NormalUpdate@@UEAAXPEAVPackageEx@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4UpdateScope@@PEAX@Z` | `0x88FE0` | 83 | UnwindData |  |
| 279 | `?Initialize@UpdateTypeBase@@UEAAXPEAVPackageEx@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4UpdateScope@@PEAX@Z` | `0x89040` | 77 | UnwindData |  |
| 280 | `?Install@UpdateTypeBase@@IEAA_NAEA_N@Z` | `0x89090` | 7,011 | UnwindData |  |
| 374 | `?Release@UpdateTypeBase@@SAXPEAV1@@Z` | `0x8AC00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `?Run@ForceUpdate@@UEAA_NXZ` | `0x8AC20` | 6,199 | UnwindData |  |
| 392 | `?Run@NormalUpdate@@UEAA_NXZ` | `0x8C460` | 6,918 | UnwindData |  |
| 396 | `?SendTelemetryInformation@UpdateTypeBase@@IEAAXAEAVPackage@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x90F80` | 1,112 | UnwindData |  |
| 408 | `?SetIsRetryInstallationNeeded@UpdateTypeBase@@QEAAX_N@Z` | `0x91DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 468 | `?UnInstall@UpdateTypeBase@@IEAA_NAEA_N@Z` | `0x91DC0` | 6,320 | UnwindData |  |
| 516 | `?getUpdateScope@UpdateTypeBase@@QEAA?AW4UpdateScope@@XZ` | `0x93670` | 1,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `?CheckActiveHoursConfig@UpdateUtility@@SA_NPEAVUpdatePolicy@@_N@Z` | `0x93BF0` | 1,209 | UnwindData |  |
| 81 | `?CheckAndValidateInstallScript@UpdateUtility@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@_N@Z` | `0x940B0` | 140 | UnwindData |  |
| 82 | `?CheckBatteryPercentConfiguration@UpdateUtility@@SA_NPEAVUpdatePolicy@@_N@Z` | `0x94140` | 576 | UnwindData |  |
| 83 | `?CheckCommonUpdatePolicy@UpdateUtility@@SA_NPEAVUpdatePolicy@@@Z` | `0x94380` | 68 | UnwindData |  |
| 89 | `?CheckIfCurrentTimeIsWithTimeRanges@UpdateUtility@@SA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0AEAJ1@Z` | `0x943D0` | 982 | UnwindData |  |
| 90 | `?CheckOnACPowerConfiguration@UpdateUtility@@SA_NPEAVUpdatePolicy@@_N@Z` | `0x947B0` | 550 | UnwindData |  |
| 94 | `?CheckPowerConfiguration@UpdateUtility@@SA_NPEAVUpdatePolicy@@_N@Z` | `0x949E0` | 994 | UnwindData |  |
| 95 | `?CheckPreferredDaysConfig@UpdateUtility@@SA_NPEAVUpdatePolicy@@_N@Z` | `0x94DD0` | 1,090 | UnwindData |  |
| 99 | `?CheckScheduleUpdateConfig@UpdateUtility@@SA_NPEAVUpdatePolicy@@_N@Z` | `0x95220` | 1,404 | UnwindData |  |
| 111 | `?ClearAbandonedPackagesFromRegistry@UpdateUtility@@SA_NAEBV?$list@VPackage@@V?$allocator@VPackage@@@std@@@std@@@Z` | `0x957A0` | 1,606 | UnwindData |  |
| 116 | `?ClearRegisteredLastUpdateTypeDetails@UpdateUtility@@SAXXZ` | `0x95DF0` | 279 | UnwindData |  |
| 118 | `?ConstructPayloadAndNotifyLCP@UpdateUtility@@SAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@E000@Z` | `0x95F10` | 2,751 | UnwindData |  |
| 149 | `?DoesListContain@UpdateUtility@@SA_NAEBV?$list@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@std@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@3@@Z` | `0x969D0` | 20 | UnwindData |  |
| 161 | `?ExtractCabFile@UpdateUtility@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x96A80` | 1,845 | UnwindData |  |
| 163 | `?ExtractZipFile@UpdateUtility@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0PEAX1@Z` | `0x971C0` | 1,624 | UnwindData |  |
| 167 | `?GetActiveHoursTimeOffset@UpdateUtility@@SAJPEAVUpdatePolicy@@@Z` | `0x98810` | 799 | UnwindData |  |
| 171 | `?GetAllInstalledPackageIdsFromRegistry@UpdateUtility@@SA_NAEAV?$vector@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@std@@@Z` | `0x98B30` | 292 | UnwindData |  |
| 174 | `?GetAnyPendingInstallationDetails@UpdateUtility@@SA_NAEAVPackage@@AEAW4UpdateScope@@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x98C60` | 4,881 | UnwindData |  |
| 176 | `?GetArchiveExtractedSuccessfullyFlag@UpdateUtility@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x99F80` | 535 | UnwindData |  |
| 184 | `?GetDeployRoutineIntrvlMSeconds@UpdateUtility@@SAJXZ` | `0x9A1A0` | 450 | UnwindData |  |
| 186 | `?GetExtractedFileCount@UpdateUtility@@SAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x9A370` | 923 | UnwindData |  |
| 188 | `?GetFileVersion@UpdateUtility@@SA?AVVersion@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x9A710` | 273 | UnwindData |  |
| 199 | `?GetIntialScheduleTimeOffset@UpdateUtility@@SAJXZ` | `0x9A830` | 224 | UnwindData |  |
| 205 | `?GetPackageDetailsFromRegistry@UpdateUtility@@SA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVPackage@@AEAV23@@Z` | `0x9A910` | 3,283 | UnwindData |  |
| 211 | `?GetPackageIdFromJson@UpdateUtility@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@@Z` | `0x9B5F0` | 997 | UnwindData |  |
| 212 | `?GetPackageIdsFromJson@UpdateUtility@@SA_NAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEAV?$list@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@3@@Z` | `0x9B9E0` | 1,393 | UnwindData |  |
| 213 | `?GetPackageIdsFromRegistry@UpdateUtility@@SA_NAEAV?$vector@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@V?$allocator@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@@std@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@3@@Z` | `0x9BF60` | 157 | UnwindData |  |
| 218 | `?GetPackageRepositoryFolder@UpdateUtility@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVPackage@@_N@Z` | `0x9C000` | 1,093 | UnwindData |  |
| 219 | `?GetPackageRepositoryFolderForVersion@UpdateUtility@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVPackage@@V23@@Z` | `0x9C450` | 1,716 | UnwindData |  |
| 221 | `?GetPackageRepositoryFolderInOldFormat@UpdateUtility@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVPackage@@_N@Z` | `0x9CB10` | 1,127 | UnwindData |  |
| 229 | `?GetProgressIntervalFromJson@UpdateUtility@@SAEAEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@Z` | `0x9CF80` | 941 | UnwindData |  |
| 230 | `?GetRegisteredLastUpdateTypeDetails@UpdateUtility@@SAXAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x9D330` | 299 | UnwindData |  |
| 240 | `?GetScheduleTimeOffset@UpdateUtility@@SAJPEAVUpdatePolicy@@AEAJ@Z` | `0x9D460` | 1,328 | UnwindData |  |
| 249 | `?GetUpdateCheckDateTime@UpdateUtility@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x9D990` | 204 | UnwindData |  |
| 250 | `?GetUpdateDateTime@UpdateUtility@@SA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x9DA60` | 218 | UnwindData |  |
| 259 | `?GetZipFileCount@UpdateUtility@@SAJAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x9DB40` | 1,358 | UnwindData |  |
| 292 | `?InvokeInternalNotificationEvent@UpdateUtility@@SAXW4TopicId@@W4EventState@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@2@Z` | `0x9E090` | 287 | UnwindData |  |
| 293 | `?InvokeLCPNotificationEvent@UpdateUtility@@SAXAEAVPackage@@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@IH1@Z` | `0x9E1B0` | 4,079 | UnwindData |  |
| 312 | `?IsLimitedPackageRetentionDefined@UpdateUtility@@SA_NXZ` | `0x9F1A0` | 713 | UnwindData |  |
| 329 | `?IsRetryAllowedFailedInstall@UpdateUtility@@SA_NXZ` | `0x9F470` | 713 | UnwindData |  |
| 331 | `?IsRetryStrategyLowDefined@UpdateUtility@@SA_NXZ` | `0x9F740` | 655 | UnwindData |  |
| 334 | `?IsSetupValidationDefined@UpdateUtility@@SA_NXZ` | `0x9F9D0` | 713 | UnwindData |  |
| 365 | `?RegisterLastUpdateTypeDetails@UpdateUtility@@SAXW4UpdateScope@@@Z` | `0x9FCA0` | 420 | UnwindData |  |
| 371 | `?RegisterUpdateCheckDateTime@UpdateUtility@@SAXXZ` | `0x9FE50` | 238 | UnwindData |  |
| 372 | `?RegisterUpdateDateTime@UpdateUtility@@SAXXZ` | `0x9FF40` | 238 | UnwindData |  |
| 395 | `?SendPackageStatusAlert@UpdateUtility@@SAXAEAVPackage@@IV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@1@Z` | `0xA0030` | 4,985 | UnwindData |  |
| 400 | `?SetArchiveExtractedSuccessfullyFlag@UpdateUtility@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xA13B0` | 819 | UnwindData |  |
| 412 | `?SetMqttInstallPackageFlag@UpdateUtility@@SAXXZ` | `0xA16F0` | 109 | UnwindData |  |
| 462 | `?TryDeleteFile@UpdateUtility@@SA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAX@Z` | `0xA1760` | 774 | UnwindData |  |
| 463 | `?TryDeleteFolder@UpdateUtility@@SA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAX@Z` | `0xA1A70` | 774 | UnwindData |  |
| 478 | `?UnzipPackageZipFile@UpdateUtility@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0xA1D80` | 1,495 | UnwindData |  |
| 487 | `?ValidateFilePath@UpdateUtility@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xA2360` | 264 | UnwindData |  |
| 488 | `?ValidateFolderPath@UpdateUtility@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xA2470` | 264 | UnwindData |  |
| 493 | `?ValidateStatusJson@UpdateUtility@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xA2580` | 867 | UnwindData |  |
| 498 | `?WaitForExtractedFiles@UpdateUtility@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAX@Z` | `0xA28F0` | 990 | UnwindData |  |
| 29 | `??0ZDUUpdateManager@UDC@@QEAA@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@PEAX@Z` | `0xA72C0` | 437 | UnwindData |  |
| 44 | `??1ZDUUpdateManager@UDC@@QEAA@XZ` | `0xA75A0` | 393 | UnwindData |  |
| 88 | `?CheckForPendingUpdateOfPackage@ZDUUpdateManager@UDC@@QEAAXXZ` | `0xA7940` | 3,340 | UnwindData |  |
| 103 | `?CheckZDUProcessingCancelled@ZDUUpdateManager@UDC@@AEAA_NPEAX@Z` | `0xA8650` | 64 | UnwindData |  |
| 104 | `?CleanUp@ZDUUpdateManager@UDC@@QEAAXXZ` | `0xA8690` | 170 | UnwindData |  |
| 128 | `?DeleteKeyInRegistry@ZDUUpdateManager@UDC@@AEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xA87F0` | 132 | UnwindData |  |
| 131 | `?DeletePackageStatusInReg@ZDUUpdateManager@UDC@@AEAAXXZ` | `0xA8880` | 1,823 | UnwindData |  |
| 136 | `?DeleteZDUPackages@ZDUUpdateManager@UDC@@AEAAXXZ` | `0xA8FA0` | 673 | UnwindData |  |
| 153 | `?DownloadAndInstallPackage@ZDUUpdateManager@UDC@@QEAA?AW4ZDUErrorCode@@AEAVPackageEx@@@Z` | `0xA9250` | 2,309 | UnwindData |  |
| 157 | `?DownloadZDUConfig@ZDUUpdateManager@UDC@@AEAAXXZ` | `0xA9B60` | 1,442 | UnwindData |  |
| 181 | `?GetConfigPolicyFilePath@ZDUUpdateManager@UDC@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0xAA110` | 644 | UnwindData |  |
| 182 | `?GetCurrentExecutingPackage@ZDUUpdateManager@UDC@@AEAA?AVPackage@@XZ` | `0xAA3A0` | 33 | UnwindData |  |
| 183 | `?GetCurrentTimeStamp@ZDUUpdateManager@UDC@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0xAA3D0` | 90 | UnwindData |  |
| 193 | `?GetInstallPendingRetryCountFromRegistry@ZDUUpdateManager@UDC@@QEAAKAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xAA430` | 978 | UnwindData |  |
| 216 | `?GetPackageNameFromUrl@ZDUUpdateManager@UDC@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV34@@Z` | `0xAA810` | 264 | UnwindData |  |
| 224 | `?GetPackageType@ZDUUpdateManager@UDC@@QEAA?AW4PackageType@@AEAVPackageEx@@@Z` | `0xAA920` | 138 | UnwindData |  |
| 226 | `?GetPackagesFromZDUConfig@ZDUUpdateManager@UDC@@QEAA_NXZ` | `0xAA9B0` | 549 | UnwindData |  |
| 237 | `?GetRetryCountFromRegistry@ZDUUpdateManager@UDC@@AEAAKXZ` | `0xAABE0` | 495 | UnwindData |  |
| 255 | `?GetZDUErrorCode@ZDUUpdateManager@UDC@@QEAA?AW4ZDUErrorCode@@XZ` | `0xAADD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `?GetZDUStartTimeFromRegistry@ZDUUpdateManager@UDC@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0xAADE0` | 238 | UnwindData |  |
| 260 | `?HandleDownloadError@ZDUUpdateManager@UDC@@QEAA_NXZ` | `0xAAED0` | 134 | UnwindData |  |
| 262 | `?HandleNetwokError@ZDUUpdateManager@UDC@@AEAAXXZ` | `0xAAF60` | 40 | UnwindData |  |
| 269 | `?HasTimeElapsed@ZDUUpdateManager@UDC@@QEAA_NXZ` | `0xAB120` | 1,748 | UnwindData |  |
| 281 | `?InstallAndHandleTimeout@ZDUUpdateManager@UDC@@AEAA?AW4ZDUErrorCode@@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0_N@Z` | `0xAB800` | 638 | UnwindData |  |
| 283 | `?InstallPackage@ZDUUpdateManager@UDC@@AEAA?AW4ZDUErrorCode@@PEAVPackageEx@@@Z` | `0xABA80` | 3,813 | UnwindData |  |
| 301 | `?IsConfigDownloadInProgress@ZDUUpdateManager@UDC@@AEAA_NXZ` | `0xAC970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `?IsExceeded24Hours@ZDUUpdateManager@UDC@@QEAA_N_J0@Z` | `0xAC980` | 140 | UnwindData |  |
| 316 | `?IsPackageAlreadyProcessed@ZDUUpdateManager@UDC@@QEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xACA10` | 993 | UnwindData |  |
| 330 | `?IsRetryInProgress@ZDUUpdateManager@UDC@@QEAA_NXZ` | `0xACE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `?RegisterPendingInstallation@ZDUUpdateManager@UDC@@AEAAXXZ` | `0xACE10` | 77 | UnwindData |  |
| 381 | `?ResetErrorValues@ZDUUpdateManager@UDC@@AEAAXXZ` | `0xACE60` | 48 | UnwindData |  |
| 387 | `?ResetZDURequired@ZDUUpdateManager@UDC@@QEAAX_N@Z` | `0xACE90` | 168 | UnwindData |  |
| 389 | `?RetryAfterDelay@ZDUUpdateManager@UDC@@AEAA_NAEAW4ZDUErrorCode@@@Z` | `0xACF40` | 476 | UnwindData |  |
| 416 | `?SetPackageInstallPendingRetryCount@ZDUUpdateManager@UDC@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@H@Z` | `0xAD120` | 952 | UnwindData |  |
| 420 | `?SetPackageStatusInReg@ZDUUpdateManager@UDC@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xAD4E0` | 1,005 | UnwindData |  |
| 424 | `?SetRetryCountInRegistry@ZDUUpdateManager@UDC@@AEAAXK@Z` | `0xAD8D0` | 237 | UnwindData |  |
| 425 | `?SetRetryFunction@ZDUUpdateManager@UDC@@AEAAXV?$function@$$A6AXXZ@std@@@Z` | `0xAD9C0` | 156 | UnwindData |  |
| 426 | `?SetStartTimeInRegistry@ZDUUpdateManager@UDC@@QEAAXXZ` | `0xADA60` | 537 | UnwindData |  |
| 432 | `?SetZDUErrorCode@ZDUUpdateManager@UDC@@AEAAXW4ZDUErrorCode@@@Z` | `0xADC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `?StartMonitorRegSync@ZDUUpdateManager@UDC@@AEAAXXZ` | `0xADC90` | 673 | UnwindData |  |
| 456 | `?TriggerDownload@ZDUUpdateManager@UDC@@QEAA?AW4ZDUErrorCode@@AEAVPackageEx@@@Z` | `0xADF40` | 950 | UnwindData |  |
| 461 | `?TriggerZDU@ZDUUpdateManager@UDC@@QEAA_NXZ` | `0xAE300` | 2,717 | UnwindData |  |
| 485 | `?UpdateZDUStatus@ZDUUpdateManager@UDC@@QEAAXW4ZDUStatusCode@ZDUStatus@@@Z` | `0xAEDA0` | 840 | UnwindData |  |
| 492 | `?ValidatePackageHash@ZDUUpdateManager@UDC@@AEAA_NAEAVPackageEx@@@Z` | `0xAF0F0` | 841 | UnwindData |  |
| 64 | `??_7PackageEx@@6B@` | `0xC4540` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `??_7UpdateTypeBase@@6B@` | `0xC4670` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `??_7NormalUpdate@@6B@` | `0xC4698` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `??_7ForceUpdate@@6B@` | `0xC46C0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??_7DeployAgent@@6BIDeployAgent@@@` | `0xC46E8` | 88 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `??_7DeployAgent@@6BIUDCAgent@@@` | `0xC4740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `??_7PluginInstaller@@6B@` | `0xC4760` | 15,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `??_7InstallAgent@@6B@` | `0xC8398` | 10,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `??_7DeviceInfoProvider@UDC@@6B@` | `0xCACC8` | 36,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `??_7UpdateManager@@6B@` | `0xD3988` | 260,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 514 | `?_extractionFlagFileName@UpdateUtility@@0V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@B` | `0x113268` | 0 | Indeterminate |  |
