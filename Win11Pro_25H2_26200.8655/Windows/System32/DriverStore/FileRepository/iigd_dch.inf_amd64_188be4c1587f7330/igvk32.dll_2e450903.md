# Binary Specification: igvk32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\igvk32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `2e450903cd13ac085e1ceaab752d9f8f5a4b6a2dfc25853279869cc24d153028`
* **Total Exported Functions:** 98

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 96 | `vk_icdGetInstanceProcAddr` | `0x415910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `vk_icdNegotiateLoaderICDInterfaceVersion` | `0x415930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `vk_icdEnumerateAdapterPhysicalDevices` | `0x415940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `vk_icdGetPhysicalDeviceProcAddr` | `0x415960` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `vkGetDeviceProcAddrINTEL` | `0x415980` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DumpRegistryKeyDefinitions` | `0x4159B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SetDriverStoreDir` | `0x4159C0` | 2,565,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `ctlInit` | `0x687FB0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ctlClose` | `0x688100` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `ctlSetRuntimePath` | `0x688170` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `ctlWaitForPropertyChange` | `0x6881D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `ctlReservedCall` | `0x688220` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `ctlGetSupported3DCapabilities` | `0x688270` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `ctlGetSet3DFeature` | `0x6882C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ctlCheckDriverVersion` | `0x688310` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `ctlEnumerateDevices` | `0x688360` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ctlEnumerateDisplayOutputs` | `0x6883B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `ctlGetDeviceProperties` | `0x688400` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `ctlGetDisplayProperties` | `0x688450` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `ctlGetAdaperDisplayEncoderProperties` | `0x6884A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `ctlGetZeDevice` | `0x6884F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `ctlGetSharpnessCaps` | `0x688540` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `ctlGetCurrentSharpness` | `0x688590` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `ctlSetCurrentSharpness` | `0x6885E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `ctlI2CAccess` | `0x688630` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ctlAUXAccess` | `0x688680` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `ctlGetPowerOptimizationCaps` | `0x6886D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `ctlGetPowerOptimizationSetting` | `0x688720` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `ctlSetPowerOptimizationSetting` | `0x688770` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `ctlSetBrightnessSetting` | `0x6887C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `ctlGetBrightnessSetting` | `0x688810` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `ctlPixelTransformationGetConfig` | `0x688860` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `ctlPixelTransformationSetConfig` | `0x6888B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `ctlPanelDescriptorAccess` | `0x688900` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `ctlGetSupportedRetroScalingCapability` | `0x688950` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `ctlGetSetRetroScaling` | `0x6889A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `ctlGetSupportedScalingCapability` | `0x6889F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `ctlGetCurrentScaling` | `0x688A40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `ctlSetCurrentScaling` | `0x688A90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `ctlGetLACEConfig` | `0x688AE0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `ctlSetLACEConfig` | `0x688B30` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `ctlSoftwarePSR` | `0x688B80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `ctlGetIntelArcSyncInfoForMonitor` | `0x688BD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ctlEnumerateMuxDevices` | `0x688C20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `ctlGetMuxProperties` | `0x688C70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `ctlSwitchMux` | `0x688CC0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `ctlGetIntelArcSyncProfile` | `0x688D10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `ctlSetIntelArcSyncProfile` | `0x688D60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `ctlEnumEngineGroups` | `0x688DB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ctlEngineGetProperties` | `0x688E00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ctlEngineGetActivity` | `0x688E50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `ctlEnumFans` | `0x688EA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ctlFanGetProperties` | `0x688EF0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `ctlFanGetConfig` | `0x688F40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `ctlFanSetDefaultMode` | `0x688F90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `ctlFanSetFixedSpeedMode` | `0x688FE0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `ctlFanSetSpeedTableMode` | `0x689030` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ctlFanGetState` | `0x689080` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ctlEnumFrequencyDomains` | `0x6890D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `ctlFrequencyGetProperties` | `0x689120` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `ctlFrequencyGetAvailableClocks` | `0x689170` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ctlFrequencyGetRange` | `0x6891C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `ctlFrequencySetRange` | `0x689210` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `ctlFrequencyGetState` | `0x689260` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `ctlFrequencyGetThrottleTime` | `0x6892B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `ctlGetSupportedVideoProcessingCapabilities` | `0x689300` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `ctlGetSetVideoProcessingFeature` | `0x689350` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ctlEnumMemoryModules` | `0x6893A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `ctlMemoryGetProperties` | `0x6893F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `ctlMemoryGetState` | `0x689440` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `ctlMemoryGetBandwidth` | `0x689490` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `ctlOverclockGetProperties` | `0x6894E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `ctlOverclockWaiverSet` | `0x689530` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `ctlOverclockGpuFrequencyOffsetGet` | `0x689580` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `ctlOverclockGpuFrequencyOffsetSet` | `0x6895D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `ctlOverclockGpuVoltageOffsetGet` | `0x689620` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `ctlOverclockGpuVoltageOffsetSet` | `0x689670` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `ctlOverclockGpuLockGet` | `0x6896C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `ctlOverclockGpuLockSet` | `0x689710` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `ctlOverclockVramFrequencyOffsetGet` | `0x689760` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `ctlOverclockVramFrequencyOffsetSet` | `0x6897B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `ctlOverclockVramVoltageOffsetGet` | `0x689800` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `ctlOverclockVramVoltageOffsetSet` | `0x689850` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `ctlOverclockPowerLimitGet` | `0x6898A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `ctlOverclockPowerLimitSet` | `0x6898F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `ctlOverclockTemperatureLimitGet` | `0x689940` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `ctlOverclockTemperatureLimitSet` | `0x689990` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `ctlPowerTelemetryGet` | `0x6899E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `ctlPciGetProperties` | `0x689A30` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `ctlPciGetState` | `0x689A80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `ctlEnumPowerDomains` | `0x689AD0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `ctlPowerGetProperties` | `0x689B20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `ctlPowerGetEnergyCounter` | `0x689B70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `ctlPowerGetLimits` | `0x689BC0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `ctlPowerSetLimits` | `0x689C10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `ctlEnumTemperatureSensors` | `0x689C60` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `ctlTemperatureGetProperties` | `0x689CB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `ctlTemperatureGetState` | `0x689D00` | 6,495,155 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
