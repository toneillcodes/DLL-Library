# Binary Specification: mgmtprovider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\mgmtprovider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5da56046bc641952cb1a07ac374044138f557515808319bdf6df0aff57f6bc07`
* **Total Exported Functions:** 776

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 770 | `DllCanUnloadNow` | `0x26D0` | 47 | UnwindData |  |
| 771 | `DllGetClassObject` | `0x2710` | 119 | UnwindData |  |
| 772 | `DllMain` | `0x2790` | 82 | UnwindData |  |
| 773 | `DllRegisterServer` | `0x27F0` | 72 | UnwindData |  |
| 774 | `DllUnregisterServer` | `0x2840` | 65 | UnwindData |  |
| 775 | `GetProviderClassID` | `0x2A60` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 776 | `MI_Main` | `0x2AF0` | 2,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x3550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x3550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x3570` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x35F0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x3660` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@@Wmi@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x36E0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `??0CMsftGetCounterSamplesAtTime@PerformanceCounters@MgmtProvider@@QEAA@AEBV012@@Z` | `0x3860` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `??0CMsftGetCounterSamplesAtTime@PerformanceCounters@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x38E0` | 110 | UnwindData |  |
| 161 | `??1?$CWmiObject@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x39E0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `??1?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x39E0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `??1?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@@Wmi@MgmtProvider@@UEAA@XZ` | `0x39E0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `??1CMsftGetCounterSamplesAtTime@PerformanceCounters@MgmtProvider@@UEAA@XZ` | `0x3AB0` | 59 | UnwindData |  |
| 239 | `??4?$CWmiObject@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x3B00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `??4?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x3B00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `??4?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x3B00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `??4CMsftGetCounterSamplesAtTime@PerformanceCounters@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x3B00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `??4?$CEnumeratorAbstractBase@V?$shared_ptr@UCounterSampleList@PerformanceCounters@MgmtProvider@@@tr1@std@@@MgmtProvider@@QEAAAEAV01@AEBV01@@Z` | `0x3B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `??4CUtilities@MgmtProvider@@QEAAAEAV01@$$QEAV01@@Z` | `0x3B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `??4CUtilities@MgmtProvider@@QEAAAEAV01@AEBV01@@Z` | `0x3B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 585 | `?GetModelsRoot@CBpaConfiguration@Bpa@MgmtProvider@@QEBAAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0x3B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `??B?$CWmiObjectT@U_MSFT_ServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `??B?$CWmiObjectT@U_MSFT_ServerClusterInformation@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `??B?$CWmiObjectT@U_MSFT_ServerFeature@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 318 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 321 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerClusterName@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 327 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerInventory@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 336 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `??B?$CWmiObjectT@U_MSFT_ServerOperatingSystem@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `??B?$CWmiObjectT@U_MSFT_ServerPerformanceCounterSamples@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `??BCMsftGetServerFeature@Inventory@MgmtProvider@@QEBA?BT_MI_Value@@XZ` | `0x3B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `??B?$CWmiObjectT@U_MSFT_ServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `??B?$CWmiObjectT@U_MSFT_ServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerBpaResult@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `??B?$CWmiObjectT@U_MSFT_ServerClusterInformation@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `??B?$CWmiObjectT@U_MSFT_ServerClusterInformation@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerClusterInformation@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `??B?$CWmiObjectT@U_MSFT_ServerFeature@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 308 | `??B?$CWmiObjectT@U_MSFT_ServerFeature@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerFeature@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerManagerTasks_GetServerBpaResult@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerClusterName@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerClusterName@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerManagerTasks_GetServerClusterName@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 325 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 326 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerManagerTasks_GetServerEventDetail@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 328 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerManagerTasks_GetServerEventDetailEx@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerInventory@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerInventory@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerManagerTasks_GetServerInventory@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 335 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerManagerTasks_GetServerServiceDetail@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 338 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 340 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `??B?$CWmiObjectT@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `??B?$CWmiObjectT@U_MSFT_ServerOperatingSystem@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `??B?$CWmiObjectT@U_MSFT_ServerOperatingSystem@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerOperatingSystem@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `??B?$CWmiObjectT@U_MSFT_ServerPerformanceCounterSamples@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MI_Instance@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `??B?$CWmiObjectT@U_MSFT_ServerPerformanceCounterSamples@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEBAPEBU_MSFT_ServerPerformanceCounterSamples@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `??BCMsftGetServerFeature@Inventory@MgmtProvider@@QEBAPEBU_MSFT_ServerManagerTasks_GetServerFeature@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 575 | `?GetKey@CRegistry@MgmtProvider@@QEAAAEBV?$shared_ptr@UHKEY__@@@tr1@std@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 597 | `?GetReportsRoot@CBpaConfiguration@Bpa@MgmtProvider@@QEBAAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0x3BA0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `?BrandingFormatString@CWin32Services@Win32@MgmtProvider@@UEBAPEAGPEBG@Z` | `0x3D40` | 48 | UnwindData |  |
| 426 | `?BrandingLoadString@CWin32Services@Win32@MgmtProvider@@UEBAHPEBGIPEAGH@Z` | `0x3D80` | 69 | UnwindData |  |
| 440 | `?ClearId@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 443 | `?ClearMIReturn@CMsftGetCounterSamplesAtTime@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 444 | `?ClearMIReturn@CMsftGetCounterSamplesInTimeRange@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 445 | `?ClearMIReturn@CMsftGetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 446 | `?ClearMIReturn@CMsftGetServerBpaResult@Bpa@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 447 | `?ClearMIReturn@CMsftGetServerClusterName@Cluster@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 448 | `?ClearMIReturn@CMsftGetServerEventDetail@EventMonitoring@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 449 | `?ClearMIReturn@CMsftGetServerEventDetailEx@EventMonitoring@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 450 | `?ClearMIReturn@CMsftGetServerFeature@Inventory@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 451 | `?ClearMIReturn@CMsftGetServerInventory@Inventory@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 452 | `?ClearMIReturn@CMsftGetServerServiceDetail@ServiceMonitoring@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 453 | `?ClearMIReturn@CMsftRemoveServerPerformanceLog@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `?ClearMIReturn@CMsftSetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x3DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 478 | `?CloseCluster@CWin32Services@Win32@MgmtProvider@@UEBAHPEAU_HCLUSTER@@@Z` | `0x3DE0` | 48 | UnwindData |  |
| 479 | `?CloseClusterGroup@CWin32Services@Win32@MgmtProvider@@UEBAHPEAU_HGROUP@@@Z` | `0x3E20` | 48 | UnwindData |  |
| 480 | `?CloseClusterResource@CWin32Services@Win32@MgmtProvider@@UEBAHPEAU_HRESOURCE@@@Z` | `0x3E60` | 48 | UnwindData |  |
| 481 | `?CloseServiceHandle@CWin32Services@Win32@MgmtProvider@@UEBAHPEAUSC_HANDLE__@@@Z` | `0x3EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 482 | `?ClusterCloseEnum@CWin32Services@Win32@MgmtProvider@@UEBAKPEAU_HCLUSENUM@@@Z` | `0x3EC0` | 51 | UnwindData |  |
| 483 | `?ClusterEnum@CWin32Services@Win32@MgmtProvider@@UEBAKPEAU_HCLUSENUM@@KPEAKPEAG1@Z` | `0x3F00` | 81 | UnwindData |  |
| 484 | `?ClusterGroupControl@CWin32Services@Win32@MgmtProvider@@UEBAKPEAU_HGROUP@@PEAU_HNODE@@KPEAXK2KPEAK@Z` | `0x3F60` | 125 | UnwindData |  |
| 485 | `?ClusterOpenEnum@CWin32Services@Win32@MgmtProvider@@UEBAPEAU_HCLUSENUM@@PEAU_HCLUSTER@@K@Z` | `0x3FF0` | 54 | UnwindData |  |
| 486 | `?ClusterResourceControl@CWin32Services@Win32@MgmtProvider@@UEBAKPEAU_HRESOURCE@@PEAU_HNODE@@KPEAXK2KPEAK@Z` | `0x4030` | 125 | UnwindData |  |
| 487 | `?ClusterResourceTypeCloseEnum@CWin32Services@Win32@MgmtProvider@@UEBAKPEAU_HRESTYPEENUM@@@Z` | `0x40C0` | 51 | UnwindData |  |
| 488 | `?ClusterResourceTypeEnum@CWin32Services@Win32@MgmtProvider@@UEBAKPEAU_HRESTYPEENUM@@KPEAKPEAG1@Z` | `0x4100` | 81 | UnwindData |  |
| 489 | `?ClusterResourceTypeOpenEnum@CWin32Services@Win32@MgmtProvider@@UEBAPEAU_HRESTYPEENUM@@PEAU_HCLUSTER@@PEBGK@Z` | `0x4160` | 60 | UnwindData |  |
| 490 | `?CoCreateGuid@CWin32Services@Win32@MgmtProvider@@UEBAJPEAU_GUID@@@Z` | `0x41B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `?CoGetCallContext@CWin32Services@Win32@MgmtProvider@@UEBAJAEBU_GUID@@PEAPEAX@Z` | `0x41D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 492 | `?CoImpersonateClient@CWin32Services@Win32@MgmtProvider@@UEBAJXZ` | `0x41F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `?CoRevertToSelf@CWin32Services@Win32@MgmtProvider@@UEBAJXZ` | `0x4210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 497 | `?CreateStreamOnHGlobal@CWin32Services@Win32@MgmtProvider@@UEBAJPEAXHPEAPEAUIStream@@@Z` | `0x4230` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 501 | `?CreateXmlReader@CWin32Services@Win32@MgmtProvider@@UEBAJAEBU_GUID@@PEAPEAXPEAUIMalloc@@@Z` | `0x4250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 502 | `?CreateXmlReaderInputWithEncodingName@CWin32Services@Win32@MgmtProvider@@UEBAJPEAUIUnknown@@PEAUIMalloc@@PEBGH2PEAPEAU4@@Z` | `0x4270` | 65 | UnwindData |  |
| 503 | `?CreateXmlWriter@CWin32Services@Win32@MgmtProvider@@UEBAJAEBU_GUID@@PEAPEAXPEAUIMalloc@@@Z` | `0x42C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 504 | `?CreateXmlWriterOutputWithEncodingName@CWin32Services@Win32@MgmtProvider@@UEBAJPEAUIUnknown@@PEAUIMalloc@@PEBGPEAPEAU4@@Z` | `0x42E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `?CrtErrorCheck@CUtilities@MgmtProvider@@SAXH@Z` | `0x4310` | 176 | UnwindData |  |
| 506 | `?DeleteFileW@CWin32Services@Win32@MgmtProvider@@UEBAHPEBG@Z` | `0x43D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 508 | `?EvtClose@CWin32Services@Win32@MgmtProvider@@UEBAHPEAX@Z` | `0x43F0` | 51 | UnwindData |  |
| 509 | `?EvtCreateRenderContext@CWin32Services@Win32@MgmtProvider@@UEBAPEAXKPEAPEBGK@Z` | `0x4430` | 63 | UnwindData |  |
| 510 | `?EvtFormatMessage@CWin32Services@Win32@MgmtProvider@@UEBAHPEAX0KKPEAU_EVT_VARIANT@@KKPEAGPEAK@Z` | `0x4480` | 136 | UnwindData |  |
| 511 | `?EvtGetChannelConfigProperty@CWin32Services@Win32@MgmtProvider@@UEBAHPEAXW4_EVT_CHANNEL_CONFIG_PROPERTY_ID@@KKPEAU_EVT_VARIANT@@PEAK@Z` | `0x4510` | 95 | UnwindData |  |
| 512 | `?EvtGetObjectArrayProperty@CWin32Services@Win32@MgmtProvider@@UEBAHPEAXKKKKPEAU_EVT_VARIANT@@PEAK@Z` | `0x4580` | 106 | UnwindData |  |
| 513 | `?EvtGetObjectArraySize@CWin32Services@Win32@MgmtProvider@@UEBAHPEAXPEAK@Z` | `0x45F0` | 57 | UnwindData |  |
| 514 | `?EvtGetPublisherMetadataProperty@CWin32Services@Win32@MgmtProvider@@UEBAHPEAXW4_EVT_PUBLISHER_METADATA_PROPERTY_ID@@KKPEAU_EVT_VARIANT@@PEAK@Z` | `0x4630` | 95 | UnwindData |  |
| 515 | `?EvtIntGetClassicLogDisplayName@CWin32Services@Win32@MgmtProvider@@UEBAHPEAXPEBGKKKPEAGPEAK@Z` | `0x46A0` | 106 | UnwindData |  |
| 516 | `?EvtNext@CWin32Services@Win32@MgmtProvider@@UEBAHPEAXKPEAPEAXKKPEAK@Z` | `0x4710` | 93 | UnwindData |  |
| 517 | `?EvtNextChannelPath@CWin32Services@Win32@MgmtProvider@@UEBAHPEAXKPEAGPEAK@Z` | `0x4780` | 72 | UnwindData |  |
| 518 | `?EvtOpenChannelConfig@CWin32Services@Win32@MgmtProvider@@UEBAPEAXPEAXPEBGK@Z` | `0x47D0` | 63 | UnwindData |  |
| 519 | `?EvtOpenChannelEnum@CWin32Services@Win32@MgmtProvider@@UEBAPEAXPEAXK@Z` | `0x4820` | 57 | UnwindData |  |
| 520 | `?EvtOpenPublisherMetadata@CWin32Services@Win32@MgmtProvider@@UEBAPEAXPEAXPEBG1KK@Z` | `0x4860` | 80 | UnwindData |  |
| 521 | `?EvtQuery@CWin32Services@Win32@MgmtProvider@@UEBAPEAXPEAXPEBG1K@Z` | `0x48C0` | 72 | UnwindData |  |
| 522 | `?EvtRender@CWin32Services@Win32@MgmtProvider@@UEBAHPEAX0KK0PEAK1@Z` | `0x4910` | 108 | UnwindData |  |
| 541 | `?FindClose@CWin32Services@Win32@MgmtProvider@@QEBAHPEAX@Z` | `0x4990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 542 | `?FindFirstFileExW@CWin32Services@Win32@MgmtProvider@@QEBAPEAXPEBGW4_FINDEX_INFO_LEVELS@@PEAXW4_FINDEX_SEARCH_OPS@@2K@Z` | `0x49B0` | 63 | UnwindData |  |
| 543 | `?FindNextFileW@CWin32Services@Win32@MgmtProvider@@QEBAHPEAXPEAU_WIN32_FIND_DATAW@@@Z` | `0x4A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `?GetClusterInformation@CWin32Services@Win32@MgmtProvider@@UEBAKPEAU_HCLUSTER@@PEAGPEAKPEAUCLUSTERVERSIONINFO@@@Z` | `0x4A20` | 71 | UnwindData |  |
| 557 | `?GetClusterResourceState@CWin32Services@Win32@MgmtProvider@@UEBA?AW4CLUSTER_RESOURCE_STATE@@PEAU_HRESOURCE@@PEAGPEAK12@Z` | `0x4A70` | 83 | UnwindData |  |
| 560 | `?GetComputerNameExW@CWin32Services@Win32@MgmtProvider@@UEBAHW4_COMPUTER_NAME_FORMAT@@PEAGPEAK@Z` | `0x4AD0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 568 | `?GetFileAttributesExW@CWin32Services@Win32@MgmtProvider@@UEBAHPEBGW4_GET_FILEEX_INFO_LEVELS@@PEAX@Z` | `0x4B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 569 | `?GetFileAttributesW@CWin32Services@Win32@MgmtProvider@@UEBAKPEBG@Z` | `0x4B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 572 | `?GetHGlobalFromStream@CWin32Services@Win32@MgmtProvider@@UEBAJPEAUIStream@@PEAPEAX@Z` | `0x4B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 577 | `?GetLastError@CWin32Services@Win32@MgmtProvider@@UEBAKXZ` | `0x4BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 579 | `?GetLocaleInfoEx@CWin32Services@Win32@MgmtProvider@@UEBAHPEBGKPEAGH@Z` | `0x4BC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 595 | `?GetProductInfo@CWin32Services@Win32@MgmtProvider@@UEBAHKKKKPEAK@Z` | `0x4C00` | 44 | UnwindData |  |
| 580 | `?GetMajorVersion@COperatingSystem@Win32@MgmtProvider@@QEBA?BIXZ` | `0x4C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `?GetSystemDefaultLocaleName@CWin32Services@Win32@MgmtProvider@@UEBAHPEAGH@Z` | `0x4C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `?GetSystemDefaultUILanguage@CWin32Services@Win32@MgmtProvider@@UEBAGXZ` | `0x4C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `?GetVersionExW@CWin32Services@Win32@MgmtProvider@@UEBAHPEAU_OSVERSIONINFOW@@@Z` | `0x4C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 612 | `?GlobalAlloc@CWin32Services@Win32@MgmtProvider@@UEBAPEAXI_K@Z` | `0x4CB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 613 | `?GlobalFree@CWin32Services@Win32@MgmtProvider@@UEBAPEAXPEAX@Z` | `0x4CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | `?GlobalLock@CWin32Services@Win32@MgmtProvider@@UEBAPEAXPEAX@Z` | `0x4CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 615 | `?GlobalMemoryStatusEx@CWin32Services@Win32@MgmtProvider@@UEBAHPEAU_MEMORYSTATUSEX@@@Z` | `0x4D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 616 | `?GlobalSize@CWin32Services@Win32@MgmtProvider@@UEBA_KPEAX@Z` | `0x4D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 617 | `?GlobalUnlock@CWin32Services@Win32@MgmtProvider@@UEBAHPEAX@Z` | `0x4D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 626 | `?IsCoreSystem@CWin32Services@Win32@MgmtProvider@@UEBA_NXZ` | `0x4D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 629 | `?IsWow64Process@CWin32Services@Win32@MgmtProvider@@UEBAHPEAXPEAH@Z` | `0x4D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 638 | `?LocalFree@CWin32Services@Win32@MgmtProvider@@UEBAPEAXPEAX@Z` | `0x4DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 650 | `?OpenClusterEx@CWin32Services@Win32@MgmtProvider@@UEBAPEAU_HCLUSTER@@PEBGKPEAK@Z` | `0x4DC0` | 60 | UnwindData |  |
| 651 | `?OpenClusterGroupEx@CWin32Services@Win32@MgmtProvider@@UEBAPEAU_HGROUP@@PEAU_HCLUSTER@@PEBGKPEAK@Z` | `0x4E10` | 69 | UnwindData |  |
| 652 | `?OpenClusterResourceEx@CWin32Services@Win32@MgmtProvider@@UEBAPEAU_HRESOURCE@@PEAU_HCLUSTER@@PEBGKPEAK@Z` | `0x4E60` | 69 | UnwindData |  |
| 653 | `?OpenSCManagerW@CWin32Services@Win32@MgmtProvider@@UEBAPEAUSC_HANDLE__@@PEBG0K@Z` | `0x4EB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `?OpenServiceW@CWin32Services@Win32@MgmtProvider@@UEBAPEAUSC_HANDLE__@@PEAU4@PEBGK@Z` | `0x4ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 656 | `?PdhAddCounterW@CWin32Services@Win32@MgmtProvider@@UEBAJPEAXPEBG_KPEAPEAX@Z` | `0x4EF0` | 75 | UnwindData |  |
| 657 | `?PdhCloseLog@CWin32Services@Win32@MgmtProvider@@UEBAJPEAXK@Z` | `0x4F50` | 60 | UnwindData |  |
| 658 | `?PdhCloseQuery@CWin32Services@Win32@MgmtProvider@@UEBAJPEAX@Z` | `0x4FA0` | 54 | UnwindData |  |
| 659 | `?PdhCollectQueryDataWithTime@CWin32Services@Win32@MgmtProvider@@UEBAJPEAXPEA_J@Z` | `0x4FE0` | 60 | UnwindData |  |
| 660 | `?PdhExpandWildCardPathHW@CWin32Services@Win32@MgmtProvider@@UEBAJPEAXPEBGPEAGPEAKK@Z` | `0x5030` | 83 | UnwindData |  |
| 661 | `?PdhGetDataSourceTimeRangeW@CWin32Services@Win32@MgmtProvider@@UEBAJPEBGPEAKPEAU_PDH_TIME_INFO@@1@Z` | `0x5090` | 75 | UnwindData |  |
| 662 | `?PdhGetFormattedCounterValue@CWin32Services@Win32@MgmtProvider@@UEBAJPEAXKPEAKPEAU_PDH_FMT_COUNTERVALUE@@@Z` | `0x50F0` | 75 | UnwindData |  |
| 663 | `?PdhMakeCounterPathW@CWin32Services@Win32@MgmtProvider@@UEBAJPEAU_PDH_COUNTER_PATH_ELEMENTS_W@@PEAGPEAKK@Z` | `0x5150` | 75 | UnwindData |  |
| 664 | `?PdhOpenLogW@CWin32Services@Win32@MgmtProvider@@UEBAJPEBGKPEAKPEAXK0PEAPEAX@Z` | `0x51B0` | 109 | UnwindData |  |
| 665 | `?PdhOpenQueryH@CWin32Services@Win32@MgmtProvider@@UEBAJPEAX_KPEAPEAX@Z` | `0x5230` | 66 | UnwindData |  |
| 666 | `?PdhParseCounterPathW@CWin32Services@Win32@MgmtProvider@@UEBAJPEBGPEAU_PDH_COUNTER_PATH_ELEMENTS_W@@PEAKK@Z` | `0x5280` | 75 | UnwindData |  |
| 667 | `?PdhSetQueryTimeRange@CWin32Services@Win32@MgmtProvider@@UEBAJPEAXPEAU_PDH_TIME_INFO@@@Z` | `0x52E0` | 60 | UnwindData |  |
| 668 | `?PdhTranslate009Counter@CWin32Services@Win32@MgmtProvider@@UEBAJPEAG0PEAK@Z` | `0x5330` | 66 | UnwindData |  |
| 669 | `?PdhTranslateLocaleCounter@CWin32Services@Win32@MgmtProvider@@UEBAJPEAG0PEAK@Z` | `0x5380` | 66 | UnwindData |  |
| 670 | `?Post@CMsftGetCounterSamplesAtTime@PerformanceCounters@MgmtProvider@@UEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 671 | `?Post@CMsftGetCounterSamplesInTimeRange@PerformanceCounters@MgmtProvider@@UEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 672 | `?Post@CMsftGetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@UEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 673 | `?Post@CMsftGetServerBpaResult@Bpa@MgmtProvider@@UEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 674 | `?Post@CMsftGetServerClusterName@Cluster@MgmtProvider@@UEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 675 | `?Post@CMsftGetServerEventDetail@EventMonitoring@MgmtProvider@@UEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 676 | `?Post@CMsftGetServerEventDetailEx@EventMonitoring@MgmtProvider@@UEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 677 | `?Post@CMsftGetServerFeature@Inventory@MgmtProvider@@QEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 678 | `?Post@CMsftGetServerInventory@Inventory@MgmtProvider@@UEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 679 | `?Post@CMsftGetServerServiceDetail@ServiceMonitoring@MgmtProvider@@UEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 680 | `?Post@CMsftRemoveServerPerformanceLog@PerformanceCounters@MgmtProvider@@UEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 681 | `?Post@CMsftServerClusterInformation@Inventory@MgmtProvider@@UEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 682 | `?Post@CMsftServerOperatingSystem@Inventory@MgmtProvider@@QEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 683 | `?Post@CMsftSetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@UEAAXAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@3@@Z` | `0x53D0` | 83 | UnwindData |  |
| 686 | `?QueryServiceConfig2W@CWin32Services@Win32@MgmtProvider@@UEBAHPEAUSC_HANDLE__@@KPEAEKPEAK@Z` | `0x5430` | 45 | UnwindData |  |
| 687 | `?QueryServiceConfigW@CWin32Services@Win32@MgmtProvider@@UEBAHPEAUSC_HANDLE__@@PEAU_QUERY_SERVICE_CONFIGW@@KPEAK@Z` | `0x5470` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 694 | `?RegCloseKey@CWin32Services@Win32@MgmtProvider@@UEBAJPEAUHKEY__@@@Z` | `0x54A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 695 | `?RegEnumKeyExW@CWin32Services@Win32@MgmtProvider@@UEBAJPEAUHKEY__@@KPEAGPEAK212PEAU_FILETIME@@@Z` | `0x54C0` | 94 | UnwindData |  |
| 696 | `?RegGetValueW@CWin32Services@Win32@MgmtProvider@@UEBAJPEAUHKEY__@@PEBG1KPEAKPEAX2@Z` | `0x5530` | 81 | UnwindData |  |
| 697 | `?RegOpenKeyExW@CWin32Services@Win32@MgmtProvider@@UEBAJPEAUHKEY__@@PEBGKKPEAPEAU4@@Z` | `0x5590` | 45 | UnwindData |  |
| 698 | `?RegQueryValueExW@CWin32Services@Win32@MgmtProvider@@UEBAJPEAUHKEY__@@PEBGPEAK2PEAE2@Z` | `0x55D0` | 65 | UnwindData |  |
| 702 | `?SLGetWindowsInformationDWORD@CWin32Services@Win32@MgmtProvider@@UEBAJPEBGPEAK@Z` | `0x5620` | 60 | UnwindData |  |
| 713 | `?SetId@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXH@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `?SetMIReturn@CMsftGetCounterSamplesAtTime@PerformanceCounters@MgmtProvider@@UEAAXW4_MI_Result@@@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 717 | `?SetMIReturn@CMsftGetCounterSamplesInTimeRange@PerformanceCounters@MgmtProvider@@UEAAXW4_MI_Result@@@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 718 | `?SetMIReturn@CMsftGetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@UEAAXW4_MI_Result@@@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `?SetMIReturn@CMsftGetServerBpaResult@Bpa@MgmtProvider@@UEAAXI@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 720 | `?SetMIReturn@CMsftGetServerClusterName@Cluster@MgmtProvider@@UEAAXW4_MI_Result@@@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 721 | `?SetMIReturn@CMsftGetServerEventDetail@EventMonitoring@MgmtProvider@@UEAAXW4_MI_Result@@@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 722 | `?SetMIReturn@CMsftGetServerEventDetailEx@EventMonitoring@MgmtProvider@@UEAAXW4_MI_Result@@@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | `?SetMIReturn@CMsftGetServerFeature@Inventory@MgmtProvider@@UEAAXI@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 724 | `?SetMIReturn@CMsftGetServerInventory@Inventory@MgmtProvider@@UEAAXW4_MI_Result@@@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 725 | `?SetMIReturn@CMsftGetServerServiceDetail@ServiceMonitoring@MgmtProvider@@UEAAXW4_MI_Result@@@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 726 | `?SetMIReturn@CMsftRemoveServerPerformanceLog@PerformanceCounters@MgmtProvider@@UEAAXW4_MI_Result@@@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 727 | `?SetMIReturn@CMsftSetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@UEAAXW4_MI_Result@@@Z` | `0x5670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0?$CWmiObject@U_MSFT_ServerFeature@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `??0?$CWmiObjectT@U_MSFT_ServerFeature@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x5680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x5680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0?$CWmiObject@U_MSFT_ServerFeature@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x56A0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x56A0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `??0?$CWmiObjectT@U_MSFT_ServerFeature@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x5750` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x5750` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x57F0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@@Wmi@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x58A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `??0CMsftGetCounterSamplesInTimeRange@PerformanceCounters@MgmtProvider@@QEAA@AEBV012@@Z` | `0x58C0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `??0CMsftGetCounterSamplesInTimeRange@PerformanceCounters@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x5970` | 110 | UnwindData |  |
| 160 | `??1?$CWmiObject@U_MSFT_ServerFeature@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x59F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `??1?$CWmiObject@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x59F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `??1?$CWmiObjectT@U_MSFT_ServerFeature@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x59F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `??1?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x59F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `??1?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@@Wmi@MgmtProvider@@UEAA@XZ` | `0x59F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `??1CMsftGetCounterSamplesInTimeRange@PerformanceCounters@MgmtProvider@@UEAA@XZ` | `0x5A10` | 59 | UnwindData |  |
| 238 | `??4?$CWmiObject@U_MSFT_ServerFeature@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5A60` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `??4?$CWmiObject@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5A60` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `??4?$CWmiObjectT@U_MSFT_ServerFeature@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x5A60` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `??4?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x5A60` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `??4?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5A60` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `??4CMsftGetCounterSamplesInTimeRange@PerformanceCounters@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5A60` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `??4CMsftServerFeature@Inventory@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5A60` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0?$CWmiObject@U_MSFT_ServerClusterInformation@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerClusterName@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??0?$CWmiObjectT@U_MSFT_ServerClusterInformation@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x5BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x5BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerClusterName@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x5BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x5BF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0?$CWmiObject@U_MSFT_ServerClusterInformation@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x5C10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x5C10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerClusterName@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x5C10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x5C10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??0?$CWmiObjectT@U_MSFT_ServerClusterInformation@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x5C60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x5C60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerClusterName@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x5C60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x5C60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x5CB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerClusterName@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x5CB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x5CB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@@Wmi@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerClusterName@@@Wmi@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@@Wmi@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `??0CMsftGetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@QEAA@AEBV012@@Z` | `0x5D20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `??0CMsftGetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x5D70` | 110 | UnwindData |  |
| 159 | `??1?$CWmiObject@U_MSFT_ServerClusterInformation@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `??1?$CWmiObject@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `??1?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerClusterName@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `??1?$CWmiObject@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `??1?$CWmiObjectT@U_MSFT_ServerClusterInformation@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `??1?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `??1?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerClusterName@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `??1?$CWmiObjectT@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `??1?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@@Wmi@MgmtProvider@@UEAA@XZ` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `??1?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerClusterName@@@Wmi@MgmtProvider@@UEAA@XZ` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `??1?$CWmiOutObject@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@@Wmi@MgmtProvider@@UEAA@XZ` | `0x5DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `??1CMsftGetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@UEAA@XZ` | `0x5E10` | 59 | UnwindData |  |
| 237 | `??4?$CWmiObject@U_MSFT_ServerClusterInformation@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `??4?$CWmiObject@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `??4?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerClusterName@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `??4?$CWmiObject@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `??4?$CWmiObjectT@U_MSFT_ServerClusterInformation@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `??4?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `??4?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerClusterName@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `??4?$CWmiObjectT@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `??4?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `??4?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerClusterName@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `??4?$CWmiOutObject@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `??4CMsftGetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `??4CMsftGetServerClusterName@Cluster@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `??4CMsftGetServerFeature@Inventory@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `??4CMsftServerClusterInformation@Inventory@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `??4CMsftSetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x5E60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 462 | `?ClearRequiresReboot@CMsftGetServerFeature@Inventory@MgmtProvider@@UEAAXXZ` | `0x5FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 475 | `?ClearcmdletOutput@CMsftGetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x5FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `?SetRequiresReboot@CMsftGetServerFeature@Inventory@MgmtProvider@@UEAAXE@Z` | `0x5FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 748 | `?SetcmdletOutput@CMsftGetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@UEAAXE@Z` | `0x5FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0?$CWmiObject@U_MSFT_ServerBpaResult@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerBpaResult@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x5FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??0?$CWmiObjectT@U_MSFT_ServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x5FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x5FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x5FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x5FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0?$CWmiObject@U_MSFT_ServerBpaResult@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x5FF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerBpaResult@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x5FF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x5FF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x5FF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??0?$CWmiObjectT@U_MSFT_ServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x6050` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x6050` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x6050` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x6050` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerBpaResult@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x60A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x60A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x60A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerBpaResult@@@Wmi@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x6100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@@Wmi@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x6100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@@Wmi@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x6100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `??0CMsftGetServerBpaResult@Bpa@MgmtProvider@@QEAA@AEBV012@@Z` | `0x6120` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `??0CMsftGetServerServiceDetail@ServiceMonitoring@MgmtProvider@@QEAA@AEBV012@@Z` | `0x6120` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `??0CMsftRemoveServerPerformanceLog@PerformanceCounters@MgmtProvider@@QEAA@AEBV012@@Z` | `0x6120` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `??0CMsftGetServerBpaResult@Bpa@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x6180` | 110 | UnwindData |  |
| 158 | `??1?$CWmiObject@U_MSFT_ServerBpaResult@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x6200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `??1?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerBpaResult@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x6200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `??1?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x6200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `??1?$CWmiObject@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x6200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `??1?$CWmiObjectT@U_MSFT_ServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x6200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `??1?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x6200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `??1?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x6200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `??1?$CWmiObjectT@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x6200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `??1?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerBpaResult@@@Wmi@MgmtProvider@@UEAA@XZ` | `0x6200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `??1?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@@Wmi@MgmtProvider@@UEAA@XZ` | `0x6200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `??1?$CWmiOutObject@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@@Wmi@MgmtProvider@@UEAA@XZ` | `0x6200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `??1CMsftGetServerBpaResult@Bpa@MgmtProvider@@UEAA@XZ` | `0x6220` | 59 | UnwindData |  |
| 221 | `??1CMsftGetServerServiceDetail@ServiceMonitoring@MgmtProvider@@UEAA@XZ` | `0x6220` | 59 | UnwindData |  |
| 222 | `??1CMsftRemoveServerPerformanceLog@PerformanceCounters@MgmtProvider@@UEAA@XZ` | `0x6220` | 59 | UnwindData |  |
| 236 | `??4?$CWmiObject@U_MSFT_ServerBpaResult@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `??4?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerBpaResult@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `??4?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `??4?$CWmiObject@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `??4?$CWmiObjectT@U_MSFT_ServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `??4?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `??4?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `??4?$CWmiObjectT@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `??4?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerBpaResult@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `??4?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `??4?$CWmiOutObject@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `??4CMsftGetServerBpaResult@Bpa@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `??4CMsftGetServerServiceDetail@ServiceMonitoring@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `??4CMsftRemoveServerPerformanceLog@PerformanceCounters@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `??4CMsftServerBpaResult@Bpa@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6270` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `??0CMsftGetServerClusterName@Cluster@MgmtProvider@@QEAA@AEBV012@@Z` | `0x63C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `??0CMsftGetServerClusterName@Cluster@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x6410` | 110 | UnwindData |  |
| 216 | `??1CMsftGetServerClusterName@Cluster@MgmtProvider@@UEAA@XZ` | `0x6490` | 59 | UnwindData |  |
| 461 | `?ClearParentName@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXXZ` | `0x6560` | 65 | UnwindData |  |
| 470 | `?ClearTimestamps@CMsftServerPerformanceCounterSamples@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x6560` | 65 | UnwindData |  |
| 473 | `?ClearValues@CMsftServerBpaResult@Bpa@MgmtProvider@@UEAAXXZ` | `0x6560` | 65 | UnwindData |  |
| 476 | `?ClearcmdletOutput@CMsftGetServerClusterName@Cluster@MgmtProvider@@UEAAXXZ` | `0x6560` | 65 | UnwindData |  |
| 746 | `?SetValues@CMsftServerBpaResult@Bpa@MgmtProvider@@UEAAXPEAPEBGI@Z` | `0x65B0` | 95 | UnwindData |  |
| 749 | `?SetcmdletOutput@CMsftGetServerClusterName@Cluster@MgmtProvider@@UEAAXPEAPEBGI@Z` | `0x65B0` | 95 | UnwindData |  |
| 19 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerEventDetail@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x6620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x6620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerEventDetail@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x6640` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x66F0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerEventDetail@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x6790` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerEventDetail@@@Wmi@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x6840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `??0CMsftGetServerEventDetail@EventMonitoring@MgmtProvider@@QEAA@AEBV012@@Z` | `0x6860` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `??0CMsftGetServerEventDetail@EventMonitoring@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x6910` | 110 | UnwindData |  |
| 166 | `??1?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerEventDetail@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x6990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `??1?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x6990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `??1?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerEventDetail@@@Wmi@MgmtProvider@@UEAA@XZ` | `0x6990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `??1CMsftGetServerEventDetail@EventMonitoring@MgmtProvider@@UEAA@XZ` | `0x69B0` | 59 | UnwindData |  |
| 244 | `??4?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerEventDetail@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6A00` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `??4?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x6A00` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `??4?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerEventDetail@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6A00` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `??4CMsftGetServerEventDetail@EventMonitoring@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6A00` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 442 | `?ClearLatestEventTimestamp@CMsftGetServerEventDetail@EventMonitoring@MgmtProvider@@UEAAXXZ` | `0x6BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 715 | `?SetLatestEventTimestamp@CMsftGetServerEventDetail@EventMonitoring@MgmtProvider@@UEAAX_K@Z` | `0x6BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x6BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerInventory@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x6BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??0?$CWmiObject@U_MSFT_ServerPerformanceCounterSamples@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x6BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x6BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerInventory@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x6BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `??0?$CWmiObjectT@U_MSFT_ServerPerformanceCounterSamples@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x6BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x6C00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??0?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerInventory@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x6C00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??0?$CWmiObject@U_MSFT_ServerPerformanceCounterSamples@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x6C00` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x6C80` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??0?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerInventory@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x6C80` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `??0?$CWmiObjectT@U_MSFT_ServerPerformanceCounterSamples@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x6C80` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x6CF0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerInventory@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x6CF0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@@Wmi@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x6D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `??0?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerInventory@@@Wmi@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x6D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `??0CMsftGetServerEventDetailEx@EventMonitoring@MgmtProvider@@QEAA@AEBV012@@Z` | `0x6D90` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `??0CMsftGetServerEventDetailEx@EventMonitoring@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x6E10` | 110 | UnwindData |  |
| 167 | `??1?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x6E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `??1?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerInventory@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x6E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `??1?$CWmiObject@U_MSFT_ServerPerformanceCounterSamples@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x6E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `??1?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x6E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `??1?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerInventory@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x6E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `??1?$CWmiObjectT@U_MSFT_ServerPerformanceCounterSamples@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x6E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `??1?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@@Wmi@MgmtProvider@@UEAA@XZ` | `0x6E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `??1?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerInventory@@@Wmi@MgmtProvider@@UEAA@XZ` | `0x6E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `??1CMsftGetServerEventDetailEx@EventMonitoring@MgmtProvider@@UEAA@XZ` | `0x6EB0` | 59 | UnwindData |  |
| 245 | `??4?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6F00` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `??4?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerInventory@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6F00` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `??4?$CWmiObject@U_MSFT_ServerPerformanceCounterSamples@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6F00` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `??4?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x6F00` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `??4?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerInventory@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x6F00` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `??4?$CWmiObjectT@U_MSFT_ServerPerformanceCounterSamples@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x6F00` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `??4?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6F00` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `??4?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerInventory@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6F00` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 287 | `??4CMsftGetServerEventDetailEx@EventMonitoring@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6F00` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `??4CMsftGetServerInventory@Inventory@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6F00` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `??4CMsftServerPerformanceCounterSamples@PerformanceCounters@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x6F00` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `??0CMsftGetServerFeature@Inventory@MgmtProvider@@QEAA@AEBV012@@Z` | `0x7060` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `??0CMsftGetServerFeature@Inventory@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x70B0` | 106 | UnwindData |  |
| 219 | `??1CMsftGetServerFeature@Inventory@MgmtProvider@@UEAA@XZ` | `0x7120` | 44 | UnwindData |  |
| 31 | `??0?$CWmiObject@U_MSFT_ServerOperatingSystem@@@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@12@@Z` | `0x71E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `??0?$CWmiObjectT@U_MSFT_ServerOperatingSystem@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@IEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@123@@Z` | `0x71E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??0?$CWmiObject@U_MSFT_ServerOperatingSystem@@@Wmi@MgmtProvider@@QEAA@AEBV012@@Z` | `0x7200` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `??0?$CWmiObjectT@U_MSFT_ServerOperatingSystem@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAA@AEBV0123@@Z` | `0x7280` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `??0CMsftGetServerInventory@Inventory@MgmtProvider@@QEAA@AEBV012@@Z` | `0x7300` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `??0CMsftGetServerInventory@Inventory@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x7380` | 110 | UnwindData |  |
| 134 | `??0CMsftServerClusterInformation@Inventory@MgmtProvider@@QEAA@AEBV012@@Z` | `0x7400` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `??0CMsftServerOperatingSystem@Inventory@MgmtProvider@@QEAA@AEBV012@@Z` | `0x7450` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `??1?$CWmiObject@U_MSFT_ServerOperatingSystem@@@Wmi@MgmtProvider@@MEAA@XZ` | `0x74D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `??1?$CWmiObjectT@U_MSFT_ServerOperatingSystem@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@MEAA@XZ` | `0x74D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `??1CMsftGetServerInventory@Inventory@MgmtProvider@@UEAA@XZ` | `0x74F0` | 59 | UnwindData |  |
| 250 | `??4?$CWmiObject@U_MSFT_ServerOperatingSystem@@@Wmi@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x7540` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `??4?$CWmiObjectT@U_MSFT_ServerOperatingSystem@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@QEAAAEAV0123@AEBV0123@@Z` | `0x7540` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `??4CMsftServerOperatingSystem@Inventory@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0x7540` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 433 | `?ClearClusterInformation@CMsftGetServerInventory@Inventory@MgmtProvider@@UEAAXXZ` | `0x77B0` | 65 | UnwindData |  |
| 436 | `?ClearDisplayName@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXXZ` | `0x7800` | 65 | UnwindData |  |
| 460 | `?ClearOperatingSystem@CMsftGetServerInventory@Inventory@MgmtProvider@@UEAAXXZ` | `0x7800` | 65 | UnwindData |  |
| 467 | `?ClearServerInventory@CMsftGetServerInventory@Inventory@MgmtProvider@@UEAAXXZ` | `0x7850` | 65 | UnwindData |  |
| 472 | `?ClearUniqueName@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXXZ` | `0x7850` | 65 | UnwindData |  |
| 474 | `?ClearValues@CMsftServerPerformanceCounterSamples@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x7850` | 65 | UnwindData |  |
| 707 | `?SetClusterInformation@CMsftGetServerInventory@Inventory@MgmtProvider@@UEAAXPEBVCMsftServerClusterInformation@23@@Z` | `0x78A0` | 89 | UnwindData |  |
| 733 | `?SetOperatingSystem@CMsftGetServerInventory@Inventory@MgmtProvider@@UEAAXPEBVCMsftServerOperatingSystem@23@@Z` | `0x7900` | 89 | UnwindData |  |
| 740 | `?SetServerInventory@CMsftGetServerInventory@Inventory@MgmtProvider@@UEAAXPEBVCMsftServerInventory@23@@Z` | `0x7960` | 89 | UnwindData |  |
| 129 | `??0CMsftGetServerServiceDetail@ServiceMonitoring@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x79C0` | 110 | UnwindData |  |
| 131 | `??0CMsftRemoveServerPerformanceLog@PerformanceCounters@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x7A40` | 110 | UnwindData |  |
| 132 | `??0CMsftServerBpaResult@Bpa@MgmtProvider@@QEAA@AEBV012@@Z` | `0x7AC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `??0CMsftServerBpaResult@Bpa@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x7B20` | 110 | UnwindData |  |
| 231 | `??1CRemoveServerPerformanceLogTask@PerformanceCounters@MgmtProvider@@QEAA@XZ` | `0x7BA0` | 45 | UnwindData |  |
| 223 | `??1CMsftServerBpaResult@Bpa@MgmtProvider@@UEAA@XZ` | `0x7BE0` | 59 | UnwindData |  |
| 431 | `?ClearBpaXPath@CMsftServerBpaResult@Bpa@MgmtProvider@@UEAAXXZ` | `0x7CB0` | 62 | UnwindData |  |
| 435 | `?ClearCounterPaths@CMsftServerPerformanceCounterSamples@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x7CB0` | 62 | UnwindData |  |
| 457 | `?ClearName@CMsftServerClusterInformation@Inventory@MgmtProvider@@UEAAXXZ` | `0x7CB0` | 62 | UnwindData |  |
| 458 | `?ClearName@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXXZ` | `0x7CB0` | 62 | UnwindData |  |
| 705 | `?SetBpaXPath@CMsftServerBpaResult@Bpa@MgmtProvider@@UEAAXV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x7D00` | 131 | UnwindData |  |
| 730 | `?SetName@CMsftServerClusterInformation@Inventory@MgmtProvider@@UEAAXV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x7D00` | 131 | UnwindData |  |
| 731 | `?SetName@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x7D00` | 131 | UnwindData |  |
| 135 | `??0CMsftServerClusterInformation@Inventory@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x7D90` | 110 | UnwindData |  |
| 224 | `??1CMsftServerClusterInformation@Inventory@MgmtProvider@@UEAA@XZ` | `0x7E10` | 59 | UnwindData |  |
| 439 | `?ClearGroupType@CMsftServerClusterInformation@Inventory@MgmtProvider@@UEAAXXZ` | `0x7E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 459 | `?ClearObjectType@CMsftServerClusterInformation@Inventory@MgmtProvider@@UEAAXXZ` | `0x7E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `?SetGroupType@CMsftServerClusterInformation@Inventory@MgmtProvider@@UEAAXH@Z` | `0x7E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `?SetObjectType@CMsftServerClusterInformation@Inventory@MgmtProvider@@UEAAXE@Z` | `0x7EA0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 463 | `?ClearSKU@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXXZ` | `0x8000` | 65 | UnwindData |  |
| 432 | `?ClearBuildNumber@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXXZ` | `0x8080` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 736 | `?SetSKU@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x80B0` | 133 | UnwindData |  |
| 745 | `?SetUniqueName@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x8150` | 133 | UnwindData |  |
| 706 | `?SetBuildNumber@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXI@Z` | `0x8200` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `?SetParentName@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x8340` | 133 | UnwindData |  |
| 136 | `??0CMsftServerFeature@Inventory@MgmtProvider@@QEAA@AEBV012@@Z` | `0x83D0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `??0CMsftServerFeature@Inventory@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x8480` | 110 | UnwindData |  |
| 225 | `??1CMsftServerFeature@Inventory@MgmtProvider@@UEAA@XZ` | `0x8500` | 59 | UnwindData |  |
| 430 | `?ClearBpaModels@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXXZ` | `0x85D0` | 65 | UnwindData |  |
| 434 | `?ClearConfigurationStatus@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXXZ` | `0x8620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 438 | `?ClearEventQuery@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXXZ` | `0x8640` | 65 | UnwindData |  |
| 441 | `?ClearLanguage@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXXZ` | `0x8640` | 65 | UnwindData |  |
| 468 | `?ClearServices@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXXZ` | `0x8690` | 65 | UnwindData |  |
| 469 | `?ClearState@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXXZ` | `0x86E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `?ClearType@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXXZ` | `0x8700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `?SetBpaModels@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXPEAPEBGI@Z` | `0x8720` | 95 | UnwindData |  |
| 708 | `?SetConfigurationStatus@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXE@Z` | `0x8790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `?SetDisplayName@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x87B0` | 133 | UnwindData |  |
| 711 | `?SetEventQuery@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x8840` | 133 | UnwindData |  |
| 714 | `?SetLanguage@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x8840` | 133 | UnwindData |  |
| 741 | `?SetServices@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXPEAPEBGI@Z` | `0x88D0` | 95 | UnwindData |  |
| 742 | `?SetState@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXE@Z` | `0x8940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 744 | `?SetType@CMsftServerFeature@Inventory@MgmtProvider@@UEAAXE@Z` | `0x8960` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `??0CMsftServerOperatingSystem@Inventory@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x8F00` | 110 | UnwindData |  |
| 226 | `??1CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAA@XZ` | `0x8F80` | 59 | UnwindData |  |
| 429 | `?ClearArchitecture@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXXZ` | `0x8FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `?ClearMajorVersion@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXXZ` | `0x8FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 456 | `?ClearMinorVersion@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXXZ` | `0x9000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `?ClearSKUId@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXXZ` | `0x9010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 465 | `?ClearSPMajorVersion@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXXZ` | `0x9030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `?ClearSPMinorVersion@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXXZ` | `0x9040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `?SetArchitecture@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXE@Z` | `0x9050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `?SetMajorVersion@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXI@Z` | `0x9070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 729 | `?SetMinorVersion@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXI@Z` | `0x9080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `?SetSKUId@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXI@Z` | `0x9090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 738 | `?SetSPMajorVersion@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXG@Z` | `0x90B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 739 | `?SetSPMinorVersion@CMsftServerOperatingSystem@Inventory@MgmtProvider@@UEAAXG@Z` | `0x90C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `??0CMsftServerPerformanceCounterSamples@PerformanceCounters@MgmtProvider@@QEAA@AEBV012@@Z` | `0x90D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `??0CMsftServerPerformanceCounterSamples@PerformanceCounters@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x9150` | 110 | UnwindData |  |
| 227 | `??1CMsftServerPerformanceCounterSamples@PerformanceCounters@MgmtProvider@@UEAA@XZ` | `0x91D0` | 59 | UnwindData |  |
| 709 | `?SetCounterPaths@CMsftServerPerformanceCounterSamples@PerformanceCounters@MgmtProvider@@UEAAXPEAPEBGI@Z` | `0x92A0` | 93 | UnwindData |  |
| 743 | `?SetTimestamps@CMsftServerPerformanceCounterSamples@PerformanceCounters@MgmtProvider@@UEAAXPEBU_MI_Datetime@@I@Z` | `0x9310` | 95 | UnwindData |  |
| 747 | `?SetValues@CMsftServerPerformanceCounterSamples@PerformanceCounters@MgmtProvider@@UEAAXPEAPEBGI@Z` | `0x9380` | 95 | UnwindData |  |
| 142 | `??0CMsftSetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@QEAA@AEBV012@@Z` | `0x9550` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `??0CMsftSetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@@Z` | `0x95A0` | 110 | UnwindData |  |
| 228 | `??1CMsftSetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@UEAA@XZ` | `0x9620` | 59 | UnwindData |  |
| 89 | `??0CBpaConfiguration@Bpa@MgmtProvider@@QEAA@$$QEAV012@@Z` | `0x9ED0` | 76 | UnwindData |  |
| 90 | `??0CBpaConfiguration@Bpa@MgmtProvider@@QEAA@AEBV012@@Z` | `0x9ED0` | 76 | UnwindData |  |
| 91 | `??0CBpaConfiguration@Bpa@MgmtProvider@@QEAA@AEBVCWin32Services@Win32@2@@Z` | `0x9F30` | 314 | UnwindData |  |
| 92 | `??0CBpaXPath@Bpa@MgmtProvider@@QEAA@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@AEBVCBpaConfiguration@12@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0xA430` | 840 | UnwindData |  |
| 147 | `??0CRegistry@MgmtProvider@@QEAA@AEBV01@@Z` | `0xA8C0` | 170 | UnwindData |  |
| 208 | `??1CGetPerformanceCollectorStateTask@PerformanceCounters@MgmtProvider@@QEAA@XZ` | `0xAB30` | 31 | UnwindData |  |
| 201 | `??1CBpaConfiguration@Bpa@MgmtProvider@@QEAA@XZ` | `0xAD40` | 87 | UnwindData |  |
| 202 | `??1CBpaXPath@Bpa@MgmtProvider@@QEAA@XZ` | `0xADA0` | 253 | UnwindData |  |
| 279 | `??4CBpaConfiguration@Bpa@MgmtProvider@@QEAAAEAV012@$$QEAV012@@Z` | `0xAF50` | 49 | UnwindData |  |
| 280 | `??4CBpaConfiguration@Bpa@MgmtProvider@@QEAAAEAV012@AEBV012@@Z` | `0xAF50` | 49 | UnwindData |  |
| 570 | `?GetFilePath@CBpaXPath@Bpa@MgmtProvider@@QEBAAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0xBFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `?GetFilePathResolved@CBpaXPath@Bpa@MgmtProvider@@QEBAAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0xBFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 574 | `?GetIpAddresses@CCluster@Cluster@MgmtProvider@@QEBAAEBV?$CAtlArray@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@XZ` | `0xBFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 582 | `?GetModelId@CBpaXPath@Bpa@MgmtProvider@@QEBAAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0xBFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 583 | `?GetModelName@CBpaXPath@Bpa@MgmtProvider@@QEBAAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0xBFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 591 | `?GetNetworkNames@CCluster@Cluster@MgmtProvider@@QEBAAEBV?$CAtlArray@PEAUClusterNetworkName@Cluster@MgmtProvider@@V?$CElementTraits@PEAUClusterNetworkName@Cluster@MgmtProvider@@@ATL@@@ATL@@XZ` | `0xBFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 584 | `?GetModelNameFromId@CBpaXPath@Bpa@MgmtProvider@@IEAA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@AEBV45@@Z` | `0xBFE0` | 92 | UnwindData |  |
| 596 | `?GetPseudoVariableValue@CBpaXPath@Bpa@MgmtProvider@@IEAA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@AEBV45@@Z` | `0xC110` | 210 | UnwindData |  |
| 610 | `?GetXPath@CBpaXPath@Bpa@MgmtProvider@@QEBAAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0xC1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 611 | `?GetXPathResult@CBpaXPath@Bpa@MgmtProvider@@QEAAXAEAV?$CAtlList@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@@Z` | `0xC200` | 3,226 | UnwindData |  |
| 655 | `?Parse@CBpaXPath@Bpa@MgmtProvider@@IEAAXAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0xDAE0` | 703 | UnwindData |  |
| 700 | `?ResolvePseudoVariables@CBpaXPath@Bpa@MgmtProvider@@IEAA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@AEBV45@@Z` | `0xE0B0` | 667 | UnwindData |  |
| 643 | `?LogFailureHandler@CGetCounterSamplesTaskBase@PerformanceCounters@MgmtProvider@@MEAAXAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@AEBVCWin32Exception@3@@Z` | `0xED70` | 2,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 761 | `?Uninitialize@CWin32Services@Win32@MgmtProvider@@QEAAXXZ` | `0xED70` | 2,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??0CCluster@Cluster@MgmtProvider@@QEAA@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0xF8C0` | 102 | UnwindData |  |
| 203 | `??1CCluster@Cluster@MgmtProvider@@QEAA@XZ` | `0xFC60` | 253 | UnwindData |  |
| 419 | `?AddIpAddress@CCluster@Cluster@MgmtProvider@@IEAAXQEAU_HCLUSTER@@QEAU_HRESOURCE@@@Z` | `0x10040` | 539 | UnwindData |  |
| 422 | `?AddNetworkName@CCluster@Cluster@MgmtProvider@@IEAAXQEAU_HCLUSTER@@QEAU_HRESOURCE@@W4ClusterNetworkNameType@23@@Z` | `0x10270` | 1,543 | UnwindData |  |
| 552 | `?GetClusterGroupListProperty@CCluster@Cluster@MgmtProvider@@IEAAXQEAU_HGROUP@@W4CLUSCTL_GROUP_CODES@@AEAV?$CAtlMap@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEAVCClusterPropertyListPropertyValue@Cluster@MgmtProvider@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@V?$CElementTraits@PEAVCClusterPropertyListPropertyValue@Cluster@MgmtProvider@@@2@@ATL@@@Z` | `0x109A0` | 434 | UnwindData |  |
| 556 | `?GetClusterResourceListProperty@CCluster@Cluster@MgmtProvider@@IEAAXQEAU_HRESOURCE@@W4CLUSCTL_RESOURCE_CODES@@AEAV?$CAtlMap@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEAVCClusterPropertyListPropertyValue@Cluster@MgmtProvider@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@V?$CElementTraits@PEAVCClusterPropertyListPropertyValue@Cluster@MgmtProvider@@@2@@ATL@@@Z` | `0x10B60` | 434 | UnwindData |  |
| 587 | `?GetName@CCluster@Cluster@MgmtProvider@@QEBA?BV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0x10D20` | 39 | UnwindData |  |
| 601 | `?GetSkuName@COperatingSystem@Win32@MgmtProvider@@QEBA?BV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0x10D20` | 39 | UnwindData |  |
| 691 | `?RefreshProperties@CCluster@Cluster@MgmtProvider@@IEAAXXZ` | `0x11140` | 1,346 | UnwindData |  |
| 1 | `??0?$CEnumeratorAbstractBase@V?$shared_ptr@UCounterSampleList@PerformanceCounters@MgmtProvider@@@tr1@std@@@MgmtProvider@@QEAA@AEBV01@@Z` | `0x12580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0?$CEnumeratorAbstractBase@V?$shared_ptr@UCounterSampleList@PerformanceCounters@MgmtProvider@@@tr1@std@@@MgmtProvider@@QEAA@XZ` | `0x12580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `??0CCounterSampleEnumerator@PerformanceCounters@MgmtProvider@@QEAA@AEBV012@@Z` | `0x125A0` | 93 | UnwindData |  |
| 95 | `??0CCounterSampleEnumerator@PerformanceCounters@MgmtProvider@@QEAA@V?$shared_ptr@X@tr1@std@@KAEBV?$CAtlArray@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@_J2AEBVCWin32Services@Win32@2@@Z` | `0x12610` | 1,182 | UnwindData |  |
| 157 | `??1?$CEnumeratorAbstractBase@V?$shared_ptr@UCounterSampleList@PerformanceCounters@MgmtProvider@@@tr1@std@@@MgmtProvider@@UEAA@XZ` | `0x12B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `??1CCounterSampleEnumerator@PerformanceCounters@MgmtProvider@@UEAA@XZ` | `0x12B20` | 180 | UnwindData |  |
| 562 | `?GetCurrent@CCounterSampleEnumerator@PerformanceCounters@MgmtProvider@@UEBA?AV?$shared_ptr@UCounterSampleList@PerformanceCounters@MgmtProvider@@@tr1@std@@XZ` | `0x12DD0` | 31 | UnwindData |  |
| 625 | `?IsComplete@CCounterSampleEnumerator@PerformanceCounters@MgmtProvider@@UEBA_NXZ` | `0x12E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 647 | `?MoveNext@CCounterSampleEnumerator@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x12E20` | 85 | UnwindData |  |
| 648 | `?MoveNextInternal@CCounterSampleEnumerator@PerformanceCounters@MgmtProvider@@IEAAXXZ` | `0x12E80` | 332 | UnwindData |  |
| 96 | `??0CGetCounterSamplesAtTimeTask@PerformanceCounters@MgmtProvider@@QEAA@PEBGPEBQEBG_K_J3IAEBV?$CFilterAbstractBase@V?$shared_ptr@UCounterSampleList@PerformanceCounters@MgmtProvider@@@tr1@std@@@2@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x131B0` | 107 | UnwindData |  |
| 205 | `??1CGetCounterSamplesAtTimeTask@PerformanceCounters@MgmtProvider@@QEAA@XZ` | `0x13230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `??1CGetCounterSamplesInTimeRangeTask@PerformanceCounters@MgmtProvider@@QEAA@XZ` | `0x13230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `??1CGetCounterSamplesTaskBase@PerformanceCounters@MgmtProvider@@QEAA@XZ` | `0x13240` | 118 | UnwindData |  |
| 524 | `?Execute@CGetCounterSamplesAtTimeTask@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x132C0` | 111 | UnwindData |  |
| 641 | `?LogFailureHandler@CGetCounterSamplesAtTimeTask@PerformanceCounters@MgmtProvider@@MEAAXAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@AEBVCWin32Exception@3@@Z` | `0x13340` | 378 | UnwindData |  |
| 97 | `??0CGetCounterSamplesInTimeRangeTask@PerformanceCounters@MgmtProvider@@QEAA@PEBGPEBQEBG_K_J3IAEBV?$CFilterAbstractBase@V?$shared_ptr@UCounterSampleList@PerformanceCounters@MgmtProvider@@@tr1@std@@@2@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x134C0` | 107 | UnwindData |  |
| 525 | `?Execute@CGetCounterSamplesInTimeRangeTask@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x13540` | 111 | UnwindData |  |
| 642 | `?LogFailureHandler@CGetCounterSamplesInTimeRangeTask@PerformanceCounters@MgmtProvider@@MEAAXAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@AEBVCWin32Exception@3@@Z` | `0x135C0` | 378 | UnwindData |  |
| 98 | `??0CGetCounterSamplesTaskBase@PerformanceCounters@MgmtProvider@@QEAA@PEBGPEBQEBG_K_J3IAEBV?$CFilterAbstractBase@V?$shared_ptr@UCounterSampleList@PerformanceCounters@MgmtProvider@@@tr1@std@@@2@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x13850` | 984 | UnwindData |  |
| 495 | `?CountersResolved@CGetCounterSamplesTaskBase@PerformanceCounters@MgmtProvider@@MEAAXAEBV?$CAtlArray@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@@Z` | `0x13E00` | 286 | UnwindData |  |
| 526 | `?Execute@CGetCounterSamplesTaskBase@PerformanceCounters@MgmtProvider@@UEAAXXZ` | `0x13F30` | 1,006 | UnwindData |  |
| 602 | `?GetSortedLogFiles@CGetCounterSamplesTaskBase@PerformanceCounters@MgmtProvider@@IEAAXAEAV?$CAtlList@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@@Z` | `0x144A0` | 616 | UnwindData |  |
| 639 | `?LogEnumerationComplete@CGetCounterSamplesTaskBase@PerformanceCounters@MgmtProvider@@MEAAXAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x14850` | 74 | UnwindData |  |
| 627 | `?IsPdhQfeInstalled@CUtilities@MgmtProvider@@SA_NAEBVCWin32Services@Win32@2@@Z` | `0x148A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 640 | `?LogEnumerationStart@CGetCounterSamplesTaskBase@PerformanceCounters@MgmtProvider@@MEAA_NAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x148A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 685 | `?ProcessSamples@CGetCounterSamplesTaskBase@PerformanceCounters@MgmtProvider@@MEAAXAEBV?$shared_ptr@UCounterSampleList@PerformanceCounters@MgmtProvider@@@tr1@std@@@Z` | `0x14960` | 233 | UnwindData |  |
| 701 | `?ResolveWildCardPaths@CGetCounterSamplesTaskBase@PerformanceCounters@MgmtProvider@@IEAAXQEAXAEAV?$CAtlArray@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@@Z` | `0x14B10` | 735 | UnwindData |  |
| 750 | `?StreamBatch@CGetCounterSamplesTaskBase@PerformanceCounters@MgmtProvider@@MEAAXAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x14FE0` | 1,069 | UnwindData |  |
| 99 | `??0CGetPerformanceCollectorStateTask@PerformanceCounters@MgmtProvider@@QEAA@$$QEAV012@@Z` | `0x155F0` | 63 | UnwindData |  |
| 100 | `??0CGetPerformanceCollectorStateTask@PerformanceCounters@MgmtProvider@@QEAA@AEBV012@@Z` | `0x155F0` | 63 | UnwindData |  |
| 101 | `??0CGetPerformanceCollectorStateTask@PerformanceCounters@MgmtProvider@@QEAA@PEBGAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x15640` | 40 | UnwindData |  |
| 233 | `??1CSetPerformanceCollectorStateTask@PerformanceCounters@MgmtProvider@@QEAA@XZ` | `0x15670` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 527 | `?Execute@CGetPerformanceCollectorStateTask@PerformanceCounters@MgmtProvider@@QEAAXXZ` | `0x156A0` | 142 | UnwindData |  |
| 102 | `??0CGetServerBpaResultTask@Bpa@MgmtProvider@@QEAA@PEBU_MSFT_ServerManagerTasks_GetServerBpaResult@@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x15970` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `?Execute@CGetServerBpaResultTask@Bpa@MgmtProvider@@QEAAIXZ` | `0x15A90` | 1,688 | UnwindData |  |
| 103 | `??0CGetServerClusterNameTask@Cluster@MgmtProvider@@QEAA@PEBU_MSFT_ServerManagerTasks_GetServerClusterName@@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x16BA0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 529 | `?Execute@CGetServerClusterNameTask@Cluster@MgmtProvider@@QEAAIXZ` | `0x16D00` | 1,687 | UnwindData |  |
| 105 | `??0CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@QEAA@AEBV?$CAtlArray@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x17E00` | 136 | UnwindData |  |
| 106 | `??0CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@QEAA@PEBU_MSFT_ServerManagerTasks_GetServerEventDetail@@AEBV?$CAtlArray@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x17E90` | 1,189 | UnwindData |  |
| 210 | `??1CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@QEAA@XZ` | `0x18790` | 100 | UnwindData |  |
| 420 | `?AddLevelFilter@CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@IEBAXPEAV?$CEventQueryT@VCEmptyClass@MgmtProvider@@@UnitTestsInfrastructure@23@E@Z` | `0x189F0` | 738 | UnwindData |  |
| 423 | `?AddTimerangeFilter@CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@IEBAXPEAV?$CEventQueryT@VCEmptyClass@MgmtProvider@@@UnitTestsInfrastructure@23@PEB_K1@Z` | `0x19360` | 651 | UnwindData |  |
| 437 | `?ClearEventDetail@CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@IEBAXAEAVCMsftServerEventDetail@23@@Z` | `0x19600` | 137 | UnwindData |  |
| 507 | `?EVTHandleToEventDetails@CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@IEAA_KAEBQEAXAEAVCMsftServerEventDetail@23@H@Z` | `0x19690` | 1,672 | UnwindData |  |
| 531 | `?Execute@CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@UEAAIXZ` | `0x19D20` | 2,809 | UnwindData |  |
| 546 | `?GetAdamInstanceNames@CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@IEBAXAEAV?$CAtlArray@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@@Z` | `0x1A9D0` | 512 | UnwindData |  |
| 566 | `?GetEventQueryFromSearchPaths@CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@IEBA?AV?$shared_ptr@V?$CEventQueryT@VCEmptyClass@MgmtProvider@@@UnitTestsInfrastructure@EventMonitoring@MgmtProvider@@@tr1@std@@PEBG@Z` | `0x1AC00` | 797 | UnwindData |  |
| 646 | `?MorphAdamQuery@CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@IEBA?AV?$shared_ptr@V?$CEventQueryT@VCEmptyClass@MgmtProvider@@@UnitTestsInfrastructure@EventMonitoring@MgmtProvider@@@tr1@std@@AEAV456@AEAV?$CAtlArray@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@@Z` | `0x1B700` | 1,584 | UnwindData |  |
| 752 | `?StreamResults@CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@IEAA_KPEAPEAU_MI_Instance@@_K@Z` | `0x1C750` | 71 | UnwindData |  |
| 104 | `??0CGetServerEventDetailExTask@EventMonitoring@MgmtProvider@@QEAA@PEBU_MSFT_ServerManagerTasks_GetServerEventDetailEx@@AEBV?$CAtlArray@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x1CA10` | 485 | UnwindData |  |
| 209 | `??1CGetServerEventDetailExTask@EventMonitoring@MgmtProvider@@QEAA@XZ` | `0x1CC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 530 | `?Execute@CGetServerEventDetailExTask@EventMonitoring@MgmtProvider@@UEAAIXZ` | `0x1CC10` | 1,231 | UnwindData |  |
| 107 | `??0CGetServerFeatureTask@Inventory@MgmtProvider@@QEAA@PEBU_MSFT_ServerManagerTasks_GetServerFeature@@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x1D130` | 294 | UnwindData |  |
| 532 | `?Execute@CGetServerFeatureTask@Inventory@MgmtProvider@@QEAAIXZ` | `0x1D260` | 1,386 | UnwindData |  |
| 538 | `?FeatureInfoToUxxFeature@CGetServerFeatureTask@Inventory@MgmtProvider@@IEBA?AV?$shared_ptr@VCMsftServerFeature@Inventory@MgmtProvider@@@tr1@std@@PEBUFeatureInfo@23@@Z` | `0x1D7D0` | 680 | UnwindData |  |
| 108 | `??0CGetServerInventoryTask@Inventory@MgmtProvider@@QEAA@PEBU_MSFT_ServerManagerTasks_GetServerInventory@@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x1DDC0` | 221 | UnwindData |  |
| 144 | `??0COperatingSystem@Win32@MgmtProvider@@QEAA@$$QEAV012@@Z` | `0x1DEB0` | 151 | UnwindData |  |
| 145 | `??0COperatingSystem@Win32@MgmtProvider@@QEAA@AEBV012@@Z` | `0x1DEB0` | 151 | UnwindData |  |
| 229 | `??1COperatingSystem@Win32@MgmtProvider@@QEAA@XZ` | `0x1E4D0` | 124 | UnwindData |  |
| 533 | `?Execute@CGetServerInventoryTask@Inventory@MgmtProvider@@QEAAXXZ` | `0x1E600` | 1,112 | UnwindData |  |
| 550 | `?GetCbsTimestamp@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0x1EB50` | 279 | UnwindData |  |
| 551 | `?GetCeipStatus@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAA?AW4CeipStatus@23@XZ` | `0x1EC70` | 577 | UnwindData |  |
| 553 | `?GetClusterInformation@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAA_NPEAU_MI_Session@@AEAVCMsftServerInventory@23@AEAVCMsftServerClusterInformation@23@@Z` | `0x1EEC0` | 868 | UnwindData |  |
| 558 | `?GetComputerDescription@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0x1F230` | 279 | UnwindData |  |
| 559 | `?GetComputerInformation@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAAXPEAU_MI_Session@@AEAW4MachineType@23@AEAV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@Z` | `0x1F350` | 619 | UnwindData |  |
| 565 | `?GetEventLogs@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAAXAEAV?$CAtlList@V?$shared_ptr@VCMsftServerEventLog@EventMonitoring@MgmtProvider@@@tr1@std@@V?$CElementTraits@V?$shared_ptr@VCMsftServerEventLog@EventMonitoring@MgmtProvider@@@tr1@std@@@ATL@@@ATL@@@Z` | `0x1F5F0` | 6,652 | UnwindData |  |
| 573 | `?GetInventory@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAAXPEAU_MI_Session@@AEAVCMsftServerInventory@23@@Z` | `0x21000` | 938 | UnwindData |  |
| 578 | `?GetLicensingStatus@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAA?AW4SlLicensingStatus@23@XZ` | `0x213B0` | 256 | UnwindData |  |
| 590 | `?GetNetworkAdapters@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAAXPEAU_MI_Session@@AEAV?$CAtlList@V?$shared_ptr@VCMsftServerNetworkAdapter@Inventory@MgmtProvider@@@tr1@std@@V?$CElementTraits@V?$shared_ptr@VCMsftServerNetworkAdapter@Inventory@MgmtProvider@@@tr1@std@@@ATL@@@ATL@@PEBV?$CAtlArray@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@6@@Z` | `0x214C0` | 3,277 | UnwindData |  |
| 592 | `?GetOperatingSystem@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAAXPEAU_MI_Session@@AEAVCMsftServerOperatingSystem@23@@Z` | `0x22210` | 402 | UnwindData |  |
| 593 | `?GetProcessors@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAAXPEAU_MI_Session@@AEAV?$CAtlList@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@@Z` | `0x223B0` | 342 | UnwindData |  |
| 594 | `?GetProductId@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0x22510` | 278 | UnwindData |  |
| 609 | `?GetWerStatus@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAA_NAEAK@Z` | `0x22630` | 755 | UnwindData |  |
| 751 | `?StreamParameter@CGetServerInventoryTask@Inventory@MgmtProvider@@IEAAXPEBGPEAPEBU_MI_Instance@@IH@Z` | `0x230E0` | 210 | UnwindData |  |
| 109 | `??0CGetServerServiceDetailTask@ServiceMonitoring@MgmtProvider@@QEAA@PEBU_MSFT_ServerManagerTasks_GetServerServiceDetail@@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x239C0` | 546 | UnwindData |  |
| 211 | `??1CGetServerServiceDetailTask@ServiceMonitoring@MgmtProvider@@UEAA@XZ` | `0x23CC0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `?Execute@CGetServerServiceDetailTask@ServiceMonitoring@MgmtProvider@@QEAAIXZ` | `0x23DE0` | 3,003 | UnwindData |  |
| 149 | `??0CRemoveServerPerformanceLogTask@PerformanceCounters@MgmtProvider@@QEAA@$$QEAV012@@Z` | `0x25350` | 74 | UnwindData |  |
| 150 | `??0CRemoveServerPerformanceLogTask@PerformanceCounters@MgmtProvider@@QEAA@AEBV012@@Z` | `0x25350` | 74 | UnwindData |  |
| 153 | `??0CSetPerformanceCollectorStateTask@PerformanceCounters@MgmtProvider@@QEAA@$$QEAV012@@Z` | `0x253A0` | 111 | UnwindData |  |
| 154 | `??0CSetPerformanceCollectorStateTask@PerformanceCounters@MgmtProvider@@QEAA@AEBV012@@Z` | `0x253A0` | 111 | UnwindData |  |
| 146 | `??0COperatingSystem@Win32@MgmtProvider@@QEAA@AEBVCWin32Services@12@@Z` | `0x27EF0` | 144 | UnwindData |  |
| 547 | `?GetArchitecture@COperatingSystem@Win32@MgmtProvider@@QEBA?BW4OperatingSystemArchitecture@23@XZ` | `0x27F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `?GetBuildNumber@COperatingSystem@Win32@MgmtProvider@@QEBA?BIXZ` | `0x27FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 576 | `?GetLanguage@COperatingSystem@Win32@MgmtProvider@@QEBA?BV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0x27FB0` | 39 | UnwindData |  |
| 581 | `?GetMinorVersion@COperatingSystem@Win32@MgmtProvider@@QEBA?BIXZ` | `0x27FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 588 | `?GetName@COperatingSystem@Win32@MgmtProvider@@QEBA?BV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@XZ` | `0x27FF0` | 39 | UnwindData |  |
| 598 | `?GetSPMajorVersion@COperatingSystem@Win32@MgmtProvider@@QEBA?BGXZ` | `0x28020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 599 | `?GetSPMinorVersion@COperatingSystem@Win32@MgmtProvider@@QEBA?BGXZ` | `0x28030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 600 | `?GetSku@COperatingSystem@Win32@MgmtProvider@@QEBA?BIXZ` | `0x28040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 688 | `?RefreshArchitecture@COperatingSystem@Win32@MgmtProvider@@IEAAXXZ` | `0x28050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 689 | `?RefreshLanguage@COperatingSystem@Win32@MgmtProvider@@IEAAXXZ` | `0x28060` | 190 | UnwindData |  |
| 690 | `?RefreshName@COperatingSystem@Win32@MgmtProvider@@IEAAXXZ` | `0x28130` | 87 | UnwindData |  |
| 692 | `?RefreshProperties@COperatingSystem@Win32@MgmtProvider@@IEAAXXZ` | `0x28190` | 44 | UnwindData |  |
| 693 | `?RefreshVersion@COperatingSystem@Win32@MgmtProvider@@IEAAXXZ` | `0x281D0` | 355 | UnwindData |  |
| 148 | `??0CRegistry@MgmtProvider@@QEAA@AEBVCWin32Services@Win32@1@@Z` | `0x28450` | 40 | UnwindData |  |
| 230 | `??1CRegistry@MgmtProvider@@QEAA@XZ` | `0x284E0` | 89 | UnwindData |  |
| 424 | `?Attach@CRegistry@MgmtProvider@@QEAAXPEAUHKEY__@@@Z` | `0x28570` | 129 | UnwindData |  |
| 477 | `?Close@CRegistry@MgmtProvider@@QEAAXXZ` | `0x28600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `?GetBinary@CRegistry@MgmtProvider@@QEBA?AV?$shared_ptr@E@tr1@std@@PEBG@Z` | `0x28610` | 501 | UnwindData |  |
| 563 | `?GetDWORD@CRegistry@MgmtProvider@@QEBAKPEBG@Z` | `0x28810` | 491 | UnwindData |  |
| 586 | `?GetMultiString@CRegistry@MgmtProvider@@QEBAXPEBGAEAV?$CAtlArray@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@_N@Z` | `0x28A10` | 901 | UnwindData |  |
| 603 | `?GetString@CRegistry@MgmtProvider@@QEBA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEBG_N@Z` | `0x28DA0` | 704 | UnwindData |  |
| 604 | `?GetSubKeys@CRegistry@MgmtProvider@@QEAAXAEAV?$CAtlList@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@@ATL@@@Z` | `0x29070` | 674 | UnwindData |  |
| 649 | `?Open@CRegistry@MgmtProvider@@QEAAXPEAUHKEY__@@PEBGK@Z` | `0x29320` | 184 | UnwindData |  |
| 758 | `?TryGetDWORD@CRegistry@MgmtProvider@@QEBA_NPEBGAEAK@Z` | `0x29490` | 358 | UnwindData |  |
| 759 | `?TryGetString@CRegistry@MgmtProvider@@QEBA_NPEBGAEAV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@_N@Z` | `0x29600` | 675 | UnwindData |  |
| 760 | `?TryOpen@CRegistry@MgmtProvider@@QEAA_NPEAUHKEY__@@PEBGK@Z` | `0x298B0` | 133 | UnwindData |  |
| 151 | `??0CRemoveServerPerformanceLogTask@PerformanceCounters@MgmtProvider@@QEAA@AEBVCComBSTR@ATL@@_KAEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x29A50` | 339 | UnwindData |  |
| 535 | `?Execute@CRemoveServerPerformanceLogTask@PerformanceCounters@MgmtProvider@@QEAAIXZ` | `0x29C00` | 1,381 | UnwindData |  |
| 152 | `??0CServerFeatureStore@Inventory@MgmtProvider@@QEAA@V?$shared_ptr@VCXmlDocument@MgmtProvider@@@tr1@std@@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x2A640` | 214 | UnwindData |  |
| 232 | `??1CServerFeatureStore@Inventory@MgmtProvider@@QEAA@XZ` | `0x2A800` | 109 | UnwindData |  |
| 498 | `?CreateUxdGERSInputParameter@CServerFeatureStore@Inventory@MgmtProvider@@IEAA?AV?$shared_ptr@U_MI_Instance@@@tr1@std@@PEBU_MI_Instance@@PEAU_MI_Application@@@Z` | `0x2AA70` | 274 | UnwindData |  |
| 499 | `?CreateUxdGSCAInputParameter@CServerFeatureStore@Inventory@MgmtProvider@@IEAA?AV?$shared_ptr@U_MI_Instance@@@tr1@std@@PEBU_MI_Instance@@PEAU_MI_Application@@@Z` | `0x2AB90` | 274 | UnwindData |  |
| 500 | `?CreateUxdRequestGuid@CServerFeatureStore@Inventory@MgmtProvider@@IEAA?AV?$shared_ptr@U_MI_Instance@@@tr1@std@@PEBTUxdRequestGuid@23@PEAU_MI_Application@@@Z` | `0x2ACB0` | 367 | UnwindData |  |
| 567 | `?GetFeatureMap@CServerFeatureStore@Inventory@MgmtProvider@@QEBAAEBV?$CAtlMap@HV?$shared_ptr@UFeatureInfo@Inventory@MgmtProvider@@@tr1@std@@V?$CElementTraits@H@ATL@@V?$CElementTraits@V?$shared_ptr@UFeatureInfo@Inventory@MgmtProvider@@@tr1@std@@@5@@ATL@@XZ` | `0x2AE30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `?GetUxdAsyncOperationState@CServerFeatureStore@Inventory@MgmtProvider@@IEAAXPEBU_MI_Instance@@AEAW4UxdRequestEnumerationState@23@AEA_N@Z` | `0x2AE40` | 418 | UnwindData |  |
| 618 | `?Initialize@CServerFeatureStore@Inventory@MgmtProvider@@QEAAXXZ` | `0x2AFF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 628 | `?IsRestartRequired@CServerFeatureStore@Inventory@MgmtProvider@@QEBA_NXZ` | `0x2B000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 630 | `?LoadFeatureInfo@CServerFeatureStore@Inventory@MgmtProvider@@IEAAXXZ` | `0x2B010` | 631 | UnwindData |  |
| 631 | `?LoadFeatureInfoFromUxd@CServerFeatureStore@Inventory@MgmtProvider@@IEAAXPEAU_MI_Application@@PEAU_MI_Session@@@Z` | `0x2B290` | 2,603 | UnwindData |  |
| 632 | `?LoadFeatureInfoFromXml@CServerFeatureStore@Inventory@MgmtProvider@@IEAAXAEBV?$shared_ptr@VCXmlDocument@MgmtProvider@@@tr1@std@@@Z` | `0x2BCD0` | 2,234 | UnwindData |  |
| 633 | `?LoadFeatureStateFromCeip@CServerFeatureStore@Inventory@MgmtProvider@@IEAAXPEAU_MI_Application@@PEAU_MI_Session@@@Z` | `0x2C590` | 1,238 | UnwindData |  |
| 637 | `?LoadUxdServerComponentsToFeatureMap@CServerFeatureStore@Inventory@MgmtProvider@@IEAAXPEAPEBU_MI_Instance@@_KAEAV?$CAtlMap@HV?$shared_ptr@UFeatureInfo@Inventory@MgmtProvider@@@tr1@std@@V?$CElementTraits@H@ATL@@V?$CElementTraits@V?$shared_ptr@UFeatureInfo@Inventory@MgmtProvider@@@tr1@std@@@5@@ATL@@@Z` | `0x2CA70` | 186 | UnwindData |  |
| 684 | `?PostUxdAsyncOperationWarnings@CServerFeatureStore@Inventory@MgmtProvider@@IEBAXPEBU_MI_Instance@@@Z` | `0x2CB30` | 268 | UnwindData |  |
| 767 | `?UxdComponentToFeatureInfo@CServerFeatureStore@Inventory@MgmtProvider@@IEAA?AV?$shared_ptr@UFeatureInfo@Inventory@MgmtProvider@@@tr1@std@@PEBU_MI_Instance@@@Z` | `0x2CDC0` | 1,820 | UnwindData |  |
| 155 | `??0CSetPerformanceCollectorStateTask@PerformanceCounters@MgmtProvider@@QEAA@PEBGW4DataCollectorSetState@12@AEBV?$CWmiServicesT@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@2@AEBVCWin32Services@Win32@2@@Z` | `0x2DA00` | 93 | UnwindData |  |
| 536 | `?Execute@CSetPerformanceCollectorStateTask@PerformanceCounters@MgmtProvider@@QEAAXXZ` | `0x2DA70` | 1,003 | UnwindData |  |
| 421 | `?AddMachineToCounterPath@CUtilities@MgmtProvider@@SA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEBGAEBVCWin32Services@Win32@2@@Z` | `0x2E460` | 611 | UnwindData |  |
| 427 | `?CheckCoreSystem@CUtilities@MgmtProvider@@SA_NXZ` | `0x2E6D0` | 280 | UnwindData |  |
| 494 | `?CompareTimestampInFilename@CUtilities@MgmtProvider@@SAHAEBV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@0@Z` | `0x2E7F0` | 291 | UnwindData |  |
| 496 | `?CreateSafeString@CUtilities@MgmtProvider@@SA?AV?$shared_ptr@G@tr1@std@@PEBG@Z` | `0x2E920` | 316 | UnwindData |  |
| 523 | `?ExceptionToCimError@CUtilities@MgmtProvider@@SA?AW4_MI_Result@@IIPEBG0PEAU_MSFT_ServerError@@@Z` | `0x2EA70` | 5,453 | UnwindData |  |
| 537 | `?ExpandEnvironmentVariables@CUtilities@MgmtProvider@@SA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEBG@Z` | `0x2FFD0` | 364 | UnwindData |  |
| 539 | `?FileTimeToString@CUtilities@MgmtProvider@@SA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@U_FILETIME@@@Z` | `0x30150` | 502 | UnwindData |  |
| 540 | `?FiletimeToUtcMIDatetime@CUtilities@MgmtProvider@@SAXPEBU_FILETIME@@PEAU_MI_Datetime@@@Z` | `0x30350` | 201 | UnwindData |  |
| 544 | `?FormatOSBrandingString@CUtilities@MgmtProvider@@SA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEBGAEBVCWin32Services@Win32@2@@Z` | `0x30420` | 174 | UnwindData |  |
| 545 | `?FreeClusterResourceListProperty@CUtilities@MgmtProvider@@SAXAEAV?$CAtlMap@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEAVCClusterPropertyListPropertyValue@Cluster@MgmtProvider@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@V?$CElementTraits@PEAVCClusterPropertyListPropertyValue@Cluster@MgmtProvider@@@2@@ATL@@@Z` | `0x304E0` | 175 | UnwindData |  |
| 555 | `?GetClusterListProperty@CUtilities@MgmtProvider@@SAXQEBEIAEAV?$CAtlMap@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEAVCClusterPropertyListPropertyValue@Cluster@MgmtProvider@@V?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@V?$CElementTraits@PEAVCClusterPropertyListPropertyValue@Cluster@MgmtProvider@@@2@@ATL@@@Z` | `0x305C0` | 436 | UnwindData |  |
| 561 | `?GetComputerNameW@CUtilities@MgmtProvider@@SA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@W4_COMPUTER_NAME_FORMAT@@@Z` | `0x30780` | 267 | UnwindData |  |
| 564 | `?GetEventFormattedMessage@CUtilities@MgmtProvider@@SA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@QEAX0KW4_EVT_FORMAT_MESSAGE_FLAGS@@AEBVCWin32Services@Win32@2@@Z` | `0x308A0` | 695 | UnwindData |  |
| 589 | `?GetNetConnnectionStatus@CUtilities@MgmtProvider@@SAGII@Z` | `0x30B60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 634 | `?LoadFormattedError@CUtilities@MgmtProvider@@SA?AV?$shared_ptr@G@tr1@std@@K@Z` | `0x30BD0` | 152 | UnwindData |  |
| 635 | `?LoadFormattedString@CUtilities@MgmtProvider@@SA?AV?$shared_ptr@G@tr1@std@@KZZ` | `0x30C70` | 323 | UnwindData |  |
| 636 | `?LoadOSBrandingString@CUtilities@MgmtProvider@@SA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEBGIAEBVCWin32Services@Win32@2@@Z` | `0x30DC0` | 367 | UnwindData |  |
| 644 | `?MIDatetimeToUtcFileTime@CUtilities@MgmtProvider@@SAXPEBU_MI_Datetime@@PEAU_FILETIME@@@Z` | `0x30F40` | 187 | UnwindData |  |
| 645 | `?MIDatetimeToUtcSystemTime@CUtilities@MgmtProvider@@SAXPEBU_MI_Datetime@@PEAU_SYSTEMTIME@@@Z` | `0x31010` | 435 | UnwindData |  |
| 699 | `?ReportExceptionToClient@CUtilities@MgmtProvider@@SAXPEAU_MI_Context@@IIPEBG1_N@Z` | `0x311D0` | 366 | UnwindData |  |
| 753 | `?StringToFileTime@CUtilities@MgmtProvider@@SA?AU_FILETIME@@PEBG@Z` | `0x31400` | 330 | UnwindData |  |
| 754 | `?StripMachineFromCounterPath@CUtilities@MgmtProvider@@SA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEBGAEBVCWin32Services@Win32@2@@Z` | `0x31550` | 732 | UnwindData |  |
| 755 | `?TranslateCounterPath@CUtilities@MgmtProvider@@KA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEBGQ8CWin32Services@Win32@2@EBAJPEAG1PEAK@ZAEBV562@@Z` | `0x31840` | 2,104 | UnwindData |  |
| 756 | `?TranslateLocalizedToNeutralCounterPath@CUtilities@MgmtProvider@@SA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEBGAEBVCWin32Services@Win32@2@@Z` | `0x32080` | 34 | UnwindData |  |
| 757 | `?TranslateNeutralToLocalizedCounterPath@CUtilities@MgmtProvider@@SA?AV?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@PEBGAEBVCWin32Services@Win32@2@@Z` | `0x320B0` | 34 | UnwindData |  |
| 156 | `??0CWin32Services@Win32@MgmtProvider@@QEAA@XZ` | `0x323F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `??1CWin32Services@Win32@MgmtProvider@@UEAA@XZ` | `0x32430` | 64 | UnwindData |  |
| 428 | `?CheckCoreSystem@CWin32Services@Win32@MgmtProvider@@QEAA_NXZ` | `0x32530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `?Initialize@CWin32Services@Win32@MgmtProvider@@QEAAXXZ` | `0x32540` | 124 | UnwindData |  |
| 620 | `?InitializeBrdApi@CWin32Services@Win32@MgmtProvider@@IEAA_NXZ` | `0x325D0` | 110 | UnwindData |  |
| 621 | `?InitializeCluApi@CWin32Services@Win32@MgmtProvider@@IEAA_NXZ` | `0x32650` | 543 | UnwindData |  |
| 622 | `?InitializeEvtApi@CWin32Services@Win32@MgmtProvider@@IEAA_NXZ` | `0x32880` | 549 | UnwindData |  |
| 623 | `?InitializePdhApi@CWin32Services@Win32@MgmtProvider@@IEAA_NXZ` | `0x32AB0` | 516 | UnwindData |  |
| 624 | `?InitializeSlcApi@CWin32Services@Win32@MgmtProvider@@IEAA_NXZ` | `0x32CC0` | 83 | UnwindData |  |
| 762 | `?UninitializeBrdApi@CWin32Services@Win32@MgmtProvider@@IEAAXXZ` | `0x32D20` | 44 | UnwindData |  |
| 763 | `?UninitializeCluApi@CWin32Services@Win32@MgmtProvider@@IEAAXXZ` | `0x32D60` | 109 | UnwindData |  |
| 764 | `?UninitializeEvtApi@CWin32Services@Win32@MgmtProvider@@IEAAXXZ` | `0x32DE0` | 141 | UnwindData |  |
| 765 | `?UninitializePdhApi@CWin32Services@Win32@MgmtProvider@@IEAAXXZ` | `0x32E80` | 134 | UnwindData |  |
| 766 | `?UninitializeSlcApi@CWin32Services@Win32@MgmtProvider@@IEAAXXZ` | `0x32F10` | 42 | UnwindData |  |
| 354 | `??_7?$CWmiObject@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@@Wmi@MgmtProvider@@6B@` | `0x3D9A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `??_7?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3D9A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `??_7?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetCounterSamplesAtTime@@@Wmi@MgmtProvider@@6B@` | `0x3D9D0` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 401 | `??_7CMsftGetCounterSamplesAtTime@PerformanceCounters@MgmtProvider@@6B@` | `0x3DA08` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `??_7?$CWmiObject@U_MSFT_ServerFeature@@@Wmi@MgmtProvider@@6B@` | `0x3DA58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `??_7?$CWmiObject@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@@Wmi@MgmtProvider@@6B@` | `0x3DA58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 369 | `??_7?$CWmiObjectT@U_MSFT_ServerFeature@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DA58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 371 | `??_7?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DA58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `??_7?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetCounterSamplesInTimeRange@@@Wmi@MgmtProvider@@6B@` | `0x3DA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 402 | `??_7CMsftGetCounterSamplesInTimeRange@PerformanceCounters@MgmtProvider@@6B@` | `0x3DA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 403 | `??_7CMsftGetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@6B@` | `0x3DA90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 352 | `??_7?$CWmiObject@U_MSFT_ServerClusterInformation@@@Wmi@MgmtProvider@@6B@` | `0x3DAC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `??_7?$CWmiObject@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@@Wmi@MgmtProvider@@6B@` | `0x3DAC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `??_7?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerClusterName@@@Wmi@MgmtProvider@@6B@` | `0x3DAC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 364 | `??_7?$CWmiObject@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@@Wmi@MgmtProvider@@6B@` | `0x3DAC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `??_7?$CWmiObjectT@U_MSFT_ServerClusterInformation@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DAC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `??_7?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DAC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `??_7?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerClusterName@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DAC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `??_7?$CWmiObjectT@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DAC0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `??_7?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetPerformanceCollectorState@@@Wmi@MgmtProvider@@6B@` | `0x3DAC8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `??_7?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerClusterName@@@Wmi@MgmtProvider@@6B@` | `0x3DAC8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `??_7?$CWmiOutObject@U_MSFT_ServerManagerTasks_SetPerformanceCollectorState@@@Wmi@MgmtProvider@@6B@` | `0x3DAC8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 404 | `??_7CMsftGetServerBpaResult@Bpa@MgmtProvider@@6B@` | `0x3DAD8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `??_7CMsftGetServerServiceDetail@ServiceMonitoring@MgmtProvider@@6B@` | `0x3DAD8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `??_7CMsftRemoveServerPerformanceLog@PerformanceCounters@MgmtProvider@@6B@` | `0x3DAD8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `??_7?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerBpaResult@@@Wmi@MgmtProvider@@6B@` | `0x3DAF8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 391 | `??_7?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@@Wmi@MgmtProvider@@6B@` | `0x3DAF8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `??_7?$CWmiOutObject@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@@Wmi@MgmtProvider@@6B@` | `0x3DAF8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `??_7?$CWmiObject@U_MSFT_ServerBpaResult@@@Wmi@MgmtProvider@@6B@` | `0x3DB08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 357 | `??_7?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerBpaResult@@@Wmi@MgmtProvider@@6B@` | `0x3DB08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `??_7?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@@Wmi@MgmtProvider@@6B@` | `0x3DB08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 363 | `??_7?$CWmiObject@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@@Wmi@MgmtProvider@@6B@` | `0x3DB08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `??_7?$CWmiObjectT@U_MSFT_ServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DB08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `??_7?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerBpaResult@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DB08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 378 | `??_7?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerServiceDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DB08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `??_7?$CWmiObjectT@U_MSFT_ServerManagerTasks_RemoveServerPerformanceLog@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DB08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 405 | `??_7CMsftGetServerClusterName@Cluster@MgmtProvider@@6B@` | `0x3DB10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 359 | `??_7?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerEventDetail@@@Wmi@MgmtProvider@@6B@` | `0x3DB40` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `??_7?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetail@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DB40` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 388 | `??_7?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerEventDetail@@@Wmi@MgmtProvider@@6B@` | `0x3DB48` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 406 | `??_7CMsftGetServerEventDetail@EventMonitoring@MgmtProvider@@6B@` | `0x3DB58` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `??_7?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@@Wmi@MgmtProvider@@6B@` | `0x3DB88` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `??_7?$CWmiOutObject@U_MSFT_ServerManagerTasks_GetServerInventory@@@Wmi@MgmtProvider@@6B@` | `0x3DB88` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `??_7CMsftGetServerEventDetailEx@EventMonitoring@MgmtProvider@@6B@` | `0x3DB98` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `??_7?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@@Wmi@MgmtProvider@@6B@` | `0x3DBB8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `??_7?$CWmiObject@U_MSFT_ServerManagerTasks_GetServerInventory@@@Wmi@MgmtProvider@@6B@` | `0x3DBB8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 366 | `??_7?$CWmiObject@U_MSFT_ServerPerformanceCounterSamples@@@Wmi@MgmtProvider@@6B@` | `0x3DBB8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `??_7?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerEventDetailEx@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DBB8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `??_7?$CWmiObjectT@U_MSFT_ServerManagerTasks_GetServerInventory@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DBB8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `??_7?$CWmiObjectT@U_MSFT_ServerPerformanceCounterSamples@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DBB8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `??_7CMsftGetServerFeature@Inventory@MgmtProvider@@6B@` | `0x3DBC0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `??_7?$CWmiObject@U_MSFT_ServerOperatingSystem@@@Wmi@MgmtProvider@@6B@` | `0x3DBE8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `??_7?$CWmiObjectT@U_MSFT_ServerOperatingSystem@@VCEmptyClass@MgmtProvider@@@UnitTestInfrastructure@Wmi@MgmtProvider@@6B@` | `0x3DBE8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 409 | `??_7CMsftGetServerInventory@Inventory@MgmtProvider@@6B@` | `0x3DBF0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `??_7CMsftServerOperatingSystem@Inventory@MgmtProvider@@6B@` | `0x3DC40` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `??_7CMsftServerClusterInformation@Inventory@MgmtProvider@@6B@` | `0x3DCE8` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `??_7CMsftServerBpaResult@Bpa@MgmtProvider@@6B@` | `0x3DD28` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `??_7CMsftServerFeature@Inventory@MgmtProvider@@6B@` | `0x3DE08` | 488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `??_7CMsftServerPerformanceCounterSamples@PerformanceCounters@MgmtProvider@@6B@` | `0x3DFF0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `??_7CMsftSetPerformanceCollectorState@PerformanceCounters@MgmtProvider@@6B@` | `0x3E0D0` | 1,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `??_7?$CEnumeratorAbstractBase@V?$shared_ptr@UCounterSampleList@PerformanceCounters@MgmtProvider@@@tr1@std@@@MgmtProvider@@6B@` | `0x3E5C8` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `??_7CCounterSampleEnumerator@PerformanceCounters@MgmtProvider@@6B@` | `0x3E628` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `??_7CGetCounterSamplesAtTimeTask@PerformanceCounters@MgmtProvider@@6B@` | `0x3E668` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `??_7CGetCounterSamplesInTimeRangeTask@PerformanceCounters@MgmtProvider@@6B@` | `0x3E6A0` | 120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `??_7CGetCounterSamplesTaskBase@PerformanceCounters@MgmtProvider@@6B@` | `0x3E718` | 280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 399 | `??_7CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@6B@` | `0x3E830` | 264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 398 | `??_7CGetServerEventDetailExTask@EventMonitoring@MgmtProvider@@6B@` | `0x3E938` | 296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 400 | `??_7CGetServerServiceDetailTask@ServiceMonitoring@MgmtProvider@@6B@` | `0x3EA60` | 1,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 418 | `??_7CWin32Services@Win32@MgmtProvider@@6B@` | `0x3EE48` | 195,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `?sc_ppEventDetailPaths@CGetServerEventDetailTask@EventMonitoring@MgmtProvider@@1PAPEBGA` | `0x6E9A8` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 768 | `?c_oDefaultWin32Services@@3VCWin32Services@Win32@MgmtProvider@@A` | `0x6E9E0` | 0 | Indeterminate |  |
