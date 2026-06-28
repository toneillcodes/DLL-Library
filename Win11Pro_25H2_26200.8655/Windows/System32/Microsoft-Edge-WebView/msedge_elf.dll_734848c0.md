# Binary Specification: msedge_elf.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Microsoft-Edge-WebView\msedge_elf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `734848c0e6cedb517d0f5bc224c6790b4768701ca35c66fc3d22a752dfb551ad`
* **Total Exported Functions:** 70

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 69 | `SignalInitializeCrashReporting` | `0x146FC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `EdgeGetElfCommandLine` | `0x147020` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `IsBrowserProcess` | `0x147170` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `GetInstallDetailsPayload` | `0x147320` | 19 | UnwindData |  |
| 47 | `GetHandleVerifier` | `0x1756B0` | 33 | UnwindData |  |
| 68 | `SignalChromeElf` | `0x280850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `GetUserDataDirectoryThunk` | `0x280860` | 250 | UnwindData |  |
| 38 | `EdgeGetElfLoadThreadId` | `0x280960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `EdgeGetInjectionMitigationStatus` | `0x280970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `EdgeModuleIsEnumerated` | `0x280980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `EdgeModuleIsLoaded` | `0x280990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `EdgeGetMitigationHistogramData` | `0x2809A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `EdgeElfBeaconDetect` | `0x2809C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `IsTemporaryUserDataDirectoryCreatedForHeadless` | `0x2809D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `DumpProcessWithoutCrash` | `0x280A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `SetMetricsClientId` | `0x280A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `IsExtensionPointDisableSet` | `0x280A80` | 4,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `DisableHook` | `0x281D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `GetApplyHookResult` | `0x281D70` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `DrainLog` | `0x282200` | 222 | UnwindData |  |
| 58 | `RegisterLogNotification` | `0x2828E0` | 190 | UnwindData |  |
| 44 | `GetBlockedModulesCount` | `0x2829A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `GetUniqueBlockedModulesCount` | `0x2829B0` | 1,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `IsThirdPartyInitialized` | `0x283110` | 1,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `RequestSingleCrashUpload_ExportThunk` | `0x2837B0` | 115 | UnwindData |  |
| 45 | `GetCrashReports_ExportThunk` | `0x283830` | 231 | UnwindData |  |
| 31 | `CrashForException_ExportThunk` | `0x283920` | 29 | UnwindData |  |
| 66 | `SetUploadConsent_ExportThunk` | `0x283940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `SetTelemetryLevel_ExportThunk` | `0x283950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `SetVariationsSeedEtag_ExportThunk` | `0x283960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `SetRuntimeVariationsSeedEtag_ExportThunk` | `0x283970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `SetUXConfigCorrelationId_ExportThunk` | `0x283980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `SetMetricsIds_ExportThunk` | `0x283990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `ClearMetricsClientId_ExportThunk` | `0x2839A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `SetIsCopilotModeEnabled_ExportThunk` | `0x2839B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `GetUploadConsent_ExportThunk` | `0x2839C0` | 33 | UnwindData |  |
| 49 | `GetProductInfo_ExportThunk` | `0x2839F0` | 41 | UnwindData |  |
| 53 | `InjectDumpForHungInput_ExportThunk` | `0x283A20` | 48 | UnwindData |  |
| 46 | `GetCrashpadDatabasePath_ExportThunk` | `0x283A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `ClearReportsBetween_ExportThunk` | `0x283A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `DumpHungProcessWithPtype_ExportThunk` | `0x283A70` | 112 | UnwindData |  |
| 70 | `StartAppWithParameter` | `0x28E870` | 262 | UnwindData |  |
| 1 | `??0PwaHelperImpl@edge_pwahelper@@QEAA@XZ` | `0x28E9F0` | 318 | UnwindData |  |
| 2 | `??1PwaHelperImpl@edge_pwahelper@@UEAA@XZ` | `0x28EB30` | 432 | UnwindData |  |
| 15 | `?InitMojo@PwaHelperImpl@edge_pwahelper@@AEAAXXZ` | `0x28ECE0` | 122 | UnwindData |  |
| 26 | `?StartProcessWithMojoIPC@PwaHelperImpl@edge_pwahelper@@QEAAKPEAXV?$unique_ptr@VCommandLine@base@@U?$default_delete@VCommandLine@base@@@__Cr@std@@@__Cr@std@@V?$unique_ptr@VScopedTempDir@base@@U?$default_delete@VScopedTempDir@base@@@__Cr@std@@@45@@Z` | `0x28ED60` | 866 | UnwindData |  |
| 25 | `?StartAppWithPlatformChannel@PwaHelperImpl@edge_pwahelper@@QEAAXV?$unique_ptr@VCommandLine@base@@U?$default_delete@VCommandLine@base@@@__Cr@std@@@__Cr@std@@@Z` | `0x28F160` | 1,600 | UnwindData |  |
| 24 | `?StartAppWithIncomingMojo@PwaHelperImpl@edge_pwahelper@@QEAAXVPlatformChannelEndpoint@mojo@@@Z` | `0x28F7A0` | 818 | UnwindData |  |
| 6 | `?BindWidgetManager@PwaHelperImpl@edge_pwahelper@@AEAAXV?$ScopedHandleBase@VMessagePipeHandle@mojo@@@mojo@@@Z` | `0x28FAE0` | 397 | UnwindData |  |
| 4 | `?AppendMojoServerBindingInfo@PwaHelperImpl@edge_pwahelper@@AEAAXPEAVCommandLine@base@@@Z` | `0x28FC70` | 139 | UnwindData |  |
| 28 | `?ValidateHandShake@PwaHelperImpl@edge_pwahelper@@AEAAXXZ` | `0x28FD00` | 26 | UnwindData |  |
| 27 | `?TryActivateInstance@PwaHelperImpl@edge_pwahelper@@AEAAXPEAVCommandLine@base@@@Z` | `0x28FD20` | 978 | UnwindData |  |
| 18 | `?OnClientConnected@PwaHelperImpl@edge_pwahelper@@AEAAXPEAVWaitableEvent@base@@@Z` | `0x290100` | 898 | UnwindData |  |
| 23 | `?Shutdown@PwaHelperImpl@edge_pwahelper@@AEAAXI@Z` | `0x290490` | 53 | UnwindData |  |
| 16 | `?InitializeAppUserModelIdForCurrentProcess@PwaHelperImpl@edge_pwahelper@@QEAA_NXZ` | `0x2904D0` | 84 | UnwindData |  |
| 5 | `?BadgeNotification@PwaHelperImpl@edge_pwahelper@@UEAAXW4BadgeNotificationType@mojom@2@AEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x290530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `?SetSingletonProcessId@PwaHelperImpl@edge_pwahelper@@UEAAXI@Z` | `0x290540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `?SetPwaHwnd@PwaHelperImpl@edge_pwahelper@@UEAAX_K@Z` | `0x290550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?PinTileToStart@PwaHelperImpl@edge_pwahelper@@UEAAXXZ` | `0x290560` | 299 | UnwindData |  |
| 20 | `?PinTileToTaskbar@PwaHelperImpl@edge_pwahelper@@UEAAXXZ` | `0x290690` | 299 | UnwindData |  |
| 17 | `?IsCurrentAppPinnedToTaskbar@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AX_N@Z@base@@@Z` | `0x2907C0` | 325 | UnwindData |  |
| 14 | `?GetAppLocalFolderPath@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@W4LocalFolderResponseCode@mojom@edge_pwahelper@@@Z@base@@@Z` | `0x290910` | 432 | UnwindData |  |
| 13 | `?GetAppAcquisitionDetail@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXW4AcquisitionInfoResponseCode@mojom@edge_acquisition_info@@V?$InlinedStructPtr@VAcquisitionDetails@mojom@edge_acquisition_info@@@mojo@@@Z@base@@@Z` | `0x290AC0` | 159 | UnwindData |  |
| 9 | `?DigitalGoodsGetDetails@PwaHelperImpl@edge_pwahelper@@UEAAXAEBV?$vector@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$allocator@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@@__Cr@std@@V?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@V?$vector@V?$StructPtr@VItemDetails@mojom@payments@@@mojo@@V?$allocator@V?$StructPtr@VItemDetails@mojom@payments@@@mojo@@@__Cr@std@@@__Cr@std@@@Z@base@@@Z` | `0x290B60` | 170 | UnwindData |  |
| 12 | `?DigitalGoodsListPurchases@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@V?$vector@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@V?$allocator@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@@__Cr@std@@@__Cr@std@@@Z@base@@@Z` | `0x290C10` | 159 | UnwindData |  |
| 11 | `?DigitalGoodsListPurchaseHistory@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@V?$vector@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@V?$allocator@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@@__Cr@std@@@__Cr@std@@@Z@base@@@Z` | `0x290CB0` | 159 | UnwindData |  |
| 8 | `?DigitalGoodsConsume@PwaHelperImpl@edge_pwahelper@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@@Z@base@@@Z` | `0x290D50` | 170 | UnwindData |  |
| 10 | `?DigitalGoodsInvokePaymentApp@PwaHelperImpl@edge_pwahelper@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$OnceCallback@$$A6AXW4PurchaseResponseCode@mojom@edge_pwahelper@@@Z@base@@@Z` | `0x290E00` | 299 | UnwindData |  |
| 7 | `?DigitalGoodsAbortPaymentApp@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AX_N@Z@base@@@Z` | `0x290F30` | 119 | UnwindData |  |
| 3 | `??_7PwaHelperImpl@edge_pwahelper@@6B@` | `0x3C5AA0` | 0 | Indeterminate |  |
