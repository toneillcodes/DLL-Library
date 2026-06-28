# Binary Specification: msedge_elf.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Microsoft-Edge-WebView\msedge_elf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0ee5375d08459588c49ac4d48ba5a82698ef0dc874a824635682b804908e8130`
* **Total Exported Functions:** 64

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 63 | `SignalInitializeCrashReporting` | `0x133980` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `EdgeGetElfCommandLine` | `0x1339E0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `IsBrowserProcess` | `0x133B40` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `GetInstallDetailsPayload` | `0x133D30` | 19 | UnwindData |  |
| 45 | `GetCrashpadDatabasePath_ExportThunk` | `0x133D50` | 170,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `GetHandleVerifier` | `0x15D770` | 33 | UnwindData |  |
| 62 | `SignalChromeElf` | `0x202950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `GetUserDataDirectoryThunk` | `0x202960` | 234 | UnwindData |  |
| 37 | `EdgeGetElfLoadThreadId` | `0x202A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `EdgeGetInjectionMitigationStatus` | `0x202A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `EdgeModuleIsEnumerated` | `0x202A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `EdgeModuleIsLoaded` | `0x202A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `EdgeGetMitigationHistogramData` | `0x202A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `EdgeElfBeaconDetect` | `0x202AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `IsTemporaryUserDataDirectoryCreatedForHeadless` | `0x202AC0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `DumpProcessWithoutCrash` | `0x202B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `SetMetricsClientId` | `0x202B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `IsExtensionPointDisableSet` | `0x202B70` | 4,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `DisableHook` | `0x203E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `GetApplyHookResult` | `0x203E20` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `DrainLog` | `0x2042A0` | 222 | UnwindData |  |
| 57 | `RegisterLogNotification` | `0x2049D0` | 190 | UnwindData |  |
| 43 | `GetBlockedModulesCount` | `0x204A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `GetUniqueBlockedModulesCount` | `0x204AA0` | 1,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `IsThirdPartyInitialized` | `0x205200` | 1,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `RequestSingleCrashUpload_ExportThunk` | `0x2058A0` | 100 | UnwindData |  |
| 44 | `GetCrashReports_ExportThunk` | `0x205910` | 223 | UnwindData |  |
| 30 | `CrashForException_ExportThunk` | `0x2059F0` | 29 | UnwindData |  |
| 61 | `SetUploadConsent_ExportThunk` | `0x205A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `SetTelemetryLevel_ExportThunk` | `0x205A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `GetUploadConsent_ExportThunk` | `0x205A30` | 36 | UnwindData |  |
| 48 | `GetProductInfo_ExportThunk` | `0x205A60` | 44 | UnwindData |  |
| 52 | `InjectDumpForHungInput_ExportThunk` | `0x205A90` | 48 | UnwindData |  |
| 29 | `ClearReportsBetween_ExportThunk` | `0x205AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `DumpHungProcessWithPtype_ExportThunk` | `0x205AD0` | 116 | UnwindData |  |
| 64 | `StartAppWithParameter` | `0x210AF0` | 272 | UnwindData |  |
| 1 | `??0PwaHelperImpl@edge_pwahelper@@QEAA@XZ` | `0x210C60` | 320 | UnwindData |  |
| 2 | `??1PwaHelperImpl@edge_pwahelper@@UEAA@XZ` | `0x210DA0` | 432 | UnwindData |  |
| 15 | `?InitMojo@PwaHelperImpl@edge_pwahelper@@AEAAXXZ` | `0x210F50` | 138 | UnwindData |  |
| 26 | `?StartProcessWithMojoIPC@PwaHelperImpl@edge_pwahelper@@QEAAKPEAXV?$unique_ptr@VCommandLine@base@@U?$default_delete@VCommandLine@base@@@__Cr@std@@@__Cr@std@@V?$unique_ptr@VScopedTempDir@base@@U?$default_delete@VScopedTempDir@base@@@__Cr@std@@@45@@Z` | `0x210FE0` | 867 | UnwindData |  |
| 25 | `?StartAppWithPlatformChannel@PwaHelperImpl@edge_pwahelper@@QEAAXV?$unique_ptr@VCommandLine@base@@U?$default_delete@VCommandLine@base@@@__Cr@std@@@__Cr@std@@@Z` | `0x2113D0` | 1,577 | UnwindData |  |
| 24 | `?StartAppWithIncomingMojo@PwaHelperImpl@edge_pwahelper@@QEAAXVPlatformChannelEndpoint@mojo@@@Z` | `0x211A00` | 834 | UnwindData |  |
| 6 | `?BindWidgetManager@PwaHelperImpl@edge_pwahelper@@AEAAXV?$ScopedHandleBase@VMessagePipeHandle@mojo@@@mojo@@@Z` | `0x211D50` | 411 | UnwindData |  |
| 4 | `?AppendMojoServerBindingInfo@PwaHelperImpl@edge_pwahelper@@AEAAXPEAVCommandLine@base@@@Z` | `0x211EF0` | 139 | UnwindData |  |
| 28 | `?ValidateHandShake@PwaHelperImpl@edge_pwahelper@@AEAAXXZ` | `0x211F80` | 26 | UnwindData |  |
| 27 | `?TryActivateInstance@PwaHelperImpl@edge_pwahelper@@AEAAXPEAVCommandLine@base@@@Z` | `0x211FA0` | 920 | UnwindData |  |
| 18 | `?OnClientConnected@PwaHelperImpl@edge_pwahelper@@AEAAXPEAVWaitableEvent@base@@@Z` | `0x212340` | 908 | UnwindData |  |
| 23 | `?Shutdown@PwaHelperImpl@edge_pwahelper@@AEAAXI@Z` | `0x2126D0` | 53 | UnwindData |  |
| 16 | `?InitializeAppUserModelIdForCurrentProcess@PwaHelperImpl@edge_pwahelper@@QEAA_NXZ` | `0x212710` | 84 | UnwindData |  |
| 5 | `?BadgeNotification@PwaHelperImpl@edge_pwahelper@@UEAAXW4BadgeNotificationType@mojom@2@AEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x212770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `?SetSingletonProcessId@PwaHelperImpl@edge_pwahelper@@UEAAXI@Z` | `0x212780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `?SetPwaHwnd@PwaHelperImpl@edge_pwahelper@@UEAAX_K@Z` | `0x212790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?PinTileToStart@PwaHelperImpl@edge_pwahelper@@UEAAXXZ` | `0x2127A0` | 299 | UnwindData |  |
| 20 | `?PinTileToTaskbar@PwaHelperImpl@edge_pwahelper@@UEAAXXZ` | `0x2128D0` | 299 | UnwindData |  |
| 17 | `?IsCurrentAppPinnedToTaskbar@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AX_N@Z@base@@@Z` | `0x212A00` | 325 | UnwindData |  |
| 14 | `?GetAppLocalFolderPath@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@W4LocalFolderResponseCode@mojom@edge_pwahelper@@@Z@base@@@Z` | `0x212B50` | 408 | UnwindData |  |
| 13 | `?GetAppAcquisitionDetail@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXW4AcquisitionInfoResponseCode@mojom@edge_acquisition_info@@V?$InlinedStructPtr@VAcquisitionDetails@mojom@edge_acquisition_info@@@mojo@@@Z@base@@@Z` | `0x212CF0` | 159 | UnwindData |  |
| 9 | `?DigitalGoodsGetDetails@PwaHelperImpl@edge_pwahelper@@UEAAXAEBV?$vector@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$allocator@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@@__Cr@std@@V?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@V?$vector@V?$StructPtr@VItemDetails@mojom@payments@@@mojo@@V?$allocator@V?$StructPtr@VItemDetails@mojom@payments@@@mojo@@@__Cr@std@@@__Cr@std@@@Z@base@@@Z` | `0x212D90` | 170 | UnwindData |  |
| 12 | `?DigitalGoodsListPurchases@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@V?$vector@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@V?$allocator@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@@__Cr@std@@@__Cr@std@@@Z@base@@@Z` | `0x212E40` | 159 | UnwindData |  |
| 11 | `?DigitalGoodsListPurchaseHistory@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@V?$vector@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@V?$allocator@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@@__Cr@std@@@__Cr@std@@@Z@base@@@Z` | `0x212EE0` | 159 | UnwindData |  |
| 8 | `?DigitalGoodsConsume@PwaHelperImpl@edge_pwahelper@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@@Z@base@@@Z` | `0x212F80` | 170 | UnwindData |  |
| 10 | `?DigitalGoodsInvokePaymentApp@PwaHelperImpl@edge_pwahelper@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$OnceCallback@$$A6AXW4PurchaseResponseCode@mojom@edge_pwahelper@@@Z@base@@@Z` | `0x213030` | 299 | UnwindData |  |
| 7 | `?DigitalGoodsAbortPaymentApp@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AX_N@Z@base@@@Z` | `0x213160` | 119 | UnwindData |  |
| 3 | `??_7PwaHelperImpl@edge_pwahelper@@6B@` | `0x32C640` | 0 | Indeterminate |  |
