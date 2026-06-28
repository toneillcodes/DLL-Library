# Binary Specification: igvk64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\igvk64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b236563fdca31669d0143d749cca1358bce7c5a1bd49d633067c015673c7413f`
* **Total Exported Functions:** 98

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 96 | `vk_icdGetInstanceProcAddr` | `0x53B3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `vk_icdNegotiateLoaderICDInterfaceVersion` | `0x53B3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `vk_icdEnumerateAdapterPhysicalDevices` | `0x53B3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `vk_icdGetPhysicalDeviceProcAddr` | `0x53B3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `vkGetDeviceProcAddrINTEL` | `0x53B3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DumpRegistryKeyDefinitions` | `0x53B400` | 2,633,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SetDriverStoreDir` | `0x53B400` | 2,633,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `ctlInit` | `0x7BE310` | 296 | UnwindData |  |
| 5 | `ctlClose` | `0x7BE440` | 116 | UnwindData |  |
| 88 | `ctlSetRuntimePath` | `0x7BE4C0` | 87 | UnwindData |  |
| 93 | `ctlWaitForPropertyChange` | `0x7BE520` | 85 | UnwindData |  |
| 81 | `ctlReservedCall` | `0x7BE580` | 85 | UnwindData |  |
| 45 | `ctlGetSupported3DCapabilities` | `0x7BE5E0` | 85 | UnwindData |  |
| 41 | `ctlGetSet3DFeature` | `0x7BE640` | 85 | UnwindData |  |
| 4 | `ctlCheckDriverVersion` | `0x7BE6A0` | 83 | UnwindData |  |
| 14 | `ctlEnumerateDevices` | `0x7BE700` | 106 | UnwindData |  |
| 15 | `ctlEnumerateDisplayOutputs` | `0x7BE770` | 106 | UnwindData |  |
| 33 | `ctlGetDeviceProperties` | `0x7BE7E0` | 85 | UnwindData |  |
| 34 | `ctlGetDisplayProperties` | `0x7BE840` | 85 | UnwindData |  |
| 29 | `ctlGetAdaperDisplayEncoderProperties` | `0x7BE8A0` | 85 | UnwindData |  |
| 49 | `ctlGetZeDevice` | `0x7BE900` | 106 | UnwindData |  |
| 44 | `ctlGetSharpnessCaps` | `0x7BE970` | 85 | UnwindData |  |
| 32 | `ctlGetCurrentSharpness` | `0x7BE9D0` | 85 | UnwindData |  |
| 84 | `ctlSetCurrentSharpness` | `0x7BEA30` | 85 | UnwindData |  |
| 50 | `ctlI2CAccess` | `0x7BEA90` | 85 | UnwindData |  |
| 3 | `ctlAUXAccess` | `0x7BEAF0` | 85 | UnwindData |  |
| 39 | `ctlGetPowerOptimizationCaps` | `0x7BEB50` | 85 | UnwindData |  |
| 40 | `ctlGetPowerOptimizationSetting` | `0x7BEBB0` | 85 | UnwindData |  |
| 87 | `ctlSetPowerOptimizationSetting` | `0x7BEC10` | 85 | UnwindData |  |
| 82 | `ctlSetBrightnessSetting` | `0x7BEC70` | 85 | UnwindData |  |
| 30 | `ctlGetBrightnessSetting` | `0x7BECD0` | 85 | UnwindData |  |
| 74 | `ctlPixelTransformationGetConfig` | `0x7BED30` | 85 | UnwindData |  |
| 75 | `ctlPixelTransformationSetConfig` | `0x7BED90` | 85 | UnwindData |  |
| 71 | `ctlPanelDescriptorAccess` | `0x7BEDF0` | 85 | UnwindData |  |
| 46 | `ctlGetSupportedRetroScalingCapability` | `0x7BEE50` | 85 | UnwindData |  |
| 42 | `ctlGetSetRetroScaling` | `0x7BEEB0` | 85 | UnwindData |  |
| 47 | `ctlGetSupportedScalingCapability` | `0x7BEF10` | 85 | UnwindData |  |
| 31 | `ctlGetCurrentScaling` | `0x7BEF70` | 85 | UnwindData |  |
| 83 | `ctlSetCurrentScaling` | `0x7BEFD0` | 85 | UnwindData |  |
| 37 | `ctlGetLACEConfig` | `0x7BF030` | 85 | UnwindData |  |
| 86 | `ctlSetLACEConfig` | `0x7BF090` | 85 | UnwindData |  |
| 89 | `ctlSoftwarePSR` | `0x7BF0F0` | 85 | UnwindData |  |
| 35 | `ctlGetIntelArcSyncInfoForMonitor` | `0x7BF150` | 85 | UnwindData |  |
| 16 | `ctlEnumerateMuxDevices` | `0x7BF1B0` | 106 | UnwindData |  |
| 38 | `ctlGetMuxProperties` | `0x7BF220` | 85 | UnwindData |  |
| 90 | `ctlSwitchMux` | `0x7BF280` | 85 | UnwindData |  |
| 36 | `ctlGetIntelArcSyncProfile` | `0x7BF2E0` | 85 | UnwindData |  |
| 85 | `ctlSetIntelArcSyncProfile` | `0x7BF340` | 85 | UnwindData |  |
| 8 | `ctlEnumEngineGroups` | `0x7BF3A0` | 106 | UnwindData |  |
| 7 | `ctlEngineGetProperties` | `0x7BF410` | 85 | UnwindData |  |
| 6 | `ctlEngineGetActivity` | `0x7BF470` | 85 | UnwindData |  |
| 9 | `ctlEnumFans` | `0x7BF4D0` | 106 | UnwindData |  |
| 18 | `ctlFanGetProperties` | `0x7BF540` | 85 | UnwindData |  |
| 17 | `ctlFanGetConfig` | `0x7BF5A0` | 85 | UnwindData |  |
| 20 | `ctlFanSetDefaultMode` | `0x7BF600` | 65 | UnwindData |  |
| 21 | `ctlFanSetFixedSpeedMode` | `0x7BF650` | 85 | UnwindData |  |
| 22 | `ctlFanSetSpeedTableMode` | `0x7BF6B0` | 85 | UnwindData |  |
| 19 | `ctlFanGetState` | `0x7BF710` | 104 | UnwindData |  |
| 10 | `ctlEnumFrequencyDomains` | `0x7BF780` | 106 | UnwindData |  |
| 24 | `ctlFrequencyGetProperties` | `0x7BF7F0` | 85 | UnwindData |  |
| 23 | `ctlFrequencyGetAvailableClocks` | `0x7BF850` | 106 | UnwindData |  |
| 25 | `ctlFrequencyGetRange` | `0x7BF8C0` | 85 | UnwindData |  |
| 28 | `ctlFrequencySetRange` | `0x7BF920` | 85 | UnwindData |  |
| 26 | `ctlFrequencyGetState` | `0x7BF980` | 85 | UnwindData |  |
| 27 | `ctlFrequencyGetThrottleTime` | `0x7BF9E0` | 85 | UnwindData |  |
| 48 | `ctlGetSupportedVideoProcessingCapabilities` | `0x7BFA40` | 85 | UnwindData |  |
| 43 | `ctlGetSetVideoProcessingFeature` | `0x7BFAA0` | 85 | UnwindData |  |
| 11 | `ctlEnumMemoryModules` | `0x7BFB00` | 106 | UnwindData |  |
| 53 | `ctlMemoryGetProperties` | `0x7BFB70` | 85 | UnwindData |  |
| 54 | `ctlMemoryGetState` | `0x7BFBD0` | 85 | UnwindData |  |
| 52 | `ctlMemoryGetBandwidth` | `0x7BFC30` | 85 | UnwindData |  |
| 55 | `ctlOverclockGetProperties` | `0x7BFC90` | 85 | UnwindData |  |
| 70 | `ctlOverclockWaiverSet` | `0x7BFCF0` | 65 | UnwindData |  |
| 56 | `ctlOverclockGpuFrequencyOffsetGet` | `0x7BFD40` | 85 | UnwindData |  |
| 57 | `ctlOverclockGpuFrequencyOffsetSet` | `0x7BFDA0` | 86 | UnwindData |  |
| 60 | `ctlOverclockGpuVoltageOffsetGet` | `0x7BFE00` | 85 | UnwindData |  |
| 61 | `ctlOverclockGpuVoltageOffsetSet` | `0x7BFE60` | 86 | UnwindData |  |
| 58 | `ctlOverclockGpuLockGet` | `0x7BFEC0` | 85 | UnwindData |  |
| 59 | `ctlOverclockGpuLockSet` | `0x7BFF20` | 106 | UnwindData |  |
| 66 | `ctlOverclockVramFrequencyOffsetGet` | `0x7BFF90` | 85 | UnwindData |  |
| 67 | `ctlOverclockVramFrequencyOffsetSet` | `0x7BFFF0` | 86 | UnwindData |  |
| 68 | `ctlOverclockVramVoltageOffsetGet` | `0x7C0050` | 85 | UnwindData |  |
| 69 | `ctlOverclockVramVoltageOffsetSet` | `0x7C00B0` | 86 | UnwindData |  |
| 62 | `ctlOverclockPowerLimitGet` | `0x7C0110` | 85 | UnwindData |  |
| 63 | `ctlOverclockPowerLimitSet` | `0x7C0170` | 86 | UnwindData |  |
| 64 | `ctlOverclockTemperatureLimitGet` | `0x7C01D0` | 85 | UnwindData |  |
| 65 | `ctlOverclockTemperatureLimitSet` | `0x7C0230` | 86 | UnwindData |  |
| 80 | `ctlPowerTelemetryGet` | `0x7C0290` | 85 | UnwindData |  |
| 72 | `ctlPciGetProperties` | `0x7C02F0` | 85 | UnwindData |  |
| 73 | `ctlPciGetState` | `0x7C0350` | 85 | UnwindData |  |
| 12 | `ctlEnumPowerDomains` | `0x7C03B0` | 106 | UnwindData |  |
| 78 | `ctlPowerGetProperties` | `0x7C0420` | 85 | UnwindData |  |
| 76 | `ctlPowerGetEnergyCounter` | `0x7C0480` | 85 | UnwindData |  |
| 77 | `ctlPowerGetLimits` | `0x7C04E0` | 85 | UnwindData |  |
| 79 | `ctlPowerSetLimits` | `0x7C0540` | 85 | UnwindData |  |
| 13 | `ctlEnumTemperatureSensors` | `0x7C05A0` | 106 | UnwindData |  |
| 91 | `ctlTemperatureGetProperties` | `0x7C0610` | 85 | UnwindData |  |
| 92 | `ctlTemperatureGetState` | `0x7C0670` | 85 | UnwindData |  |
