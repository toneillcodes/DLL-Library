# Binary Specification: igd12um64xel.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\igd12um64xel.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d7404c480a3e2c9e81898db3350574c9e621d7318cded49504a53eb38cb643e3`
* **Total Exported Functions:** 92

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `OpenAdapter_Gen12LP` | `0xA0B70` | 15,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `ctlTemperatureGetState` | `0xA4860` | 88 | UnwindData |  |
| 90 | `ctlTemperatureGetProperties` | `0xA48C0` | 88 | UnwindData |  |
| 12 | `ctlEnumTemperatureSensors` | `0xA4920` | 104 | UnwindData |  |
| 78 | `ctlPowerSetLimits` | `0xA4990` | 88 | UnwindData |  |
| 76 | `ctlPowerGetLimits` | `0xA49F0` | 88 | UnwindData |  |
| 75 | `ctlPowerGetEnergyCounter` | `0xA4A50` | 88 | UnwindData |  |
| 77 | `ctlPowerGetProperties` | `0xA4AB0` | 88 | UnwindData |  |
| 11 | `ctlEnumPowerDomains` | `0xA4B10` | 104 | UnwindData |  |
| 72 | `ctlPciGetState` | `0xA4B80` | 88 | UnwindData |  |
| 71 | `ctlPciGetProperties` | `0xA4BE0` | 88 | UnwindData |  |
| 79 | `ctlPowerTelemetryGet` | `0xA4C40` | 88 | UnwindData |  |
| 64 | `ctlOverclockTemperatureLimitSet` | `0xA4CA0` | 88 | UnwindData |  |
| 63 | `ctlOverclockTemperatureLimitGet` | `0xA4D00` | 88 | UnwindData |  |
| 62 | `ctlOverclockPowerLimitSet` | `0xA4D60` | 88 | UnwindData |  |
| 61 | `ctlOverclockPowerLimitGet` | `0xA4DC0` | 88 | UnwindData |  |
| 68 | `ctlOverclockVramVoltageOffsetSet` | `0xA4E20` | 88 | UnwindData |  |
| 67 | `ctlOverclockVramVoltageOffsetGet` | `0xA4E80` | 88 | UnwindData |  |
| 66 | `ctlOverclockVramFrequencyOffsetSet` | `0xA4EE0` | 88 | UnwindData |  |
| 65 | `ctlOverclockVramFrequencyOffsetGet` | `0xA4F40` | 88 | UnwindData |  |
| 58 | `ctlOverclockGpuLockSet` | `0xA4FA0` | 109 | UnwindData |  |
| 57 | `ctlOverclockGpuLockGet` | `0xA5020` | 88 | UnwindData |  |
| 60 | `ctlOverclockGpuVoltageOffsetSet` | `0xA5080` | 88 | UnwindData |  |
| 59 | `ctlOverclockGpuVoltageOffsetGet` | `0xA50E0` | 88 | UnwindData |  |
| 56 | `ctlOverclockGpuFrequencyOffsetSet` | `0xA5140` | 88 | UnwindData |  |
| 55 | `ctlOverclockGpuFrequencyOffsetGet` | `0xA51A0` | 88 | UnwindData |  |
| 69 | `ctlOverclockWaiverSet` | `0xA5200` | 72 | UnwindData |  |
| 54 | `ctlOverclockGetProperties` | `0xA5250` | 88 | UnwindData |  |
| 51 | `ctlMemoryGetBandwidth` | `0xA52B0` | 88 | UnwindData |  |
| 53 | `ctlMemoryGetState` | `0xA5310` | 88 | UnwindData |  |
| 52 | `ctlMemoryGetProperties` | `0xA5370` | 88 | UnwindData |  |
| 10 | `ctlEnumMemoryModules` | `0xA53D0` | 104 | UnwindData |  |
| 42 | `ctlGetSetVideoProcessingFeature` | `0xA5440` | 88 | UnwindData |  |
| 47 | `ctlGetSupportedVideoProcessingCapabilities` | `0xA54A0` | 88 | UnwindData |  |
| 26 | `ctlFrequencyGetThrottleTime` | `0xA5500` | 88 | UnwindData |  |
| 25 | `ctlFrequencyGetState` | `0xA5560` | 88 | UnwindData |  |
| 27 | `ctlFrequencySetRange` | `0xA55C0` | 88 | UnwindData |  |
| 24 | `ctlFrequencyGetRange` | `0xA5620` | 88 | UnwindData |  |
| 22 | `ctlFrequencyGetAvailableClocks` | `0xA5680` | 104 | UnwindData |  |
| 23 | `ctlFrequencyGetProperties` | `0xA56F0` | 88 | UnwindData |  |
| 9 | `ctlEnumFrequencyDomains` | `0xA5750` | 104 | UnwindData |  |
| 18 | `ctlFanGetState` | `0xA57C0` | 102 | UnwindData |  |
| 21 | `ctlFanSetSpeedTableMode` | `0xA5830` | 88 | UnwindData |  |
| 20 | `ctlFanSetFixedSpeedMode` | `0xA5890` | 88 | UnwindData |  |
| 19 | `ctlFanSetDefaultMode` | `0xA58F0` | 72 | UnwindData |  |
| 16 | `ctlFanGetConfig` | `0xA5940` | 88 | UnwindData |  |
| 17 | `ctlFanGetProperties` | `0xA59A0` | 88 | UnwindData |  |
| 8 | `ctlEnumFans` | `0xA5A00` | 104 | UnwindData |  |
| 5 | `ctlEngineGetActivity` | `0xA5A70` | 88 | UnwindData |  |
| 6 | `ctlEngineGetProperties` | `0xA5AD0` | 88 | UnwindData |  |
| 7 | `ctlEnumEngineGroups` | `0xA5B30` | 104 | UnwindData |  |
| 84 | `ctlSetIntelArcSyncProfile` | `0xA5BA0` | 88 | UnwindData |  |
| 35 | `ctlGetIntelArcSyncProfile` | `0xA5C00` | 88 | UnwindData |  |
| 89 | `ctlSwitchMux` | `0xA5C60` | 88 | UnwindData |  |
| 37 | `ctlGetMuxProperties` | `0xA5CC0` | 88 | UnwindData |  |
| 15 | `ctlEnumerateMuxDevices` | `0xA5D20` | 104 | UnwindData |  |
| 34 | `ctlGetIntelArcSyncInfoForMonitor` | `0xA5D90` | 88 | UnwindData |  |
| 88 | `ctlSoftwarePSR` | `0xA5DF0` | 88 | UnwindData |  |
| 85 | `ctlSetLACEConfig` | `0xA5E50` | 88 | UnwindData |  |
| 36 | `ctlGetLACEConfig` | `0xA5EB0` | 88 | UnwindData |  |
| 82 | `ctlSetCurrentScaling` | `0xA5F10` | 88 | UnwindData |  |
| 30 | `ctlGetCurrentScaling` | `0xA5F70` | 88 | UnwindData |  |
| 46 | `ctlGetSupportedScalingCapability` | `0xA5FD0` | 88 | UnwindData |  |
| 41 | `ctlGetSetRetroScaling` | `0xA6030` | 88 | UnwindData |  |
| 45 | `ctlGetSupportedRetroScalingCapability` | `0xA6090` | 88 | UnwindData |  |
| 70 | `ctlPanelDescriptorAccess` | `0xA60F0` | 88 | UnwindData |  |
| 74 | `ctlPixelTransformationSetConfig` | `0xA6150` | 88 | UnwindData |  |
| 73 | `ctlPixelTransformationGetConfig` | `0xA61B0` | 88 | UnwindData |  |
| 29 | `ctlGetBrightnessSetting` | `0xA6210` | 88 | UnwindData |  |
| 81 | `ctlSetBrightnessSetting` | `0xA6270` | 88 | UnwindData |  |
| 86 | `ctlSetPowerOptimizationSetting` | `0xA62D0` | 88 | UnwindData |  |
| 39 | `ctlGetPowerOptimizationSetting` | `0xA6330` | 88 | UnwindData |  |
| 38 | `ctlGetPowerOptimizationCaps` | `0xA6390` | 88 | UnwindData |  |
| 2 | `ctlAUXAccess` | `0xA63F0` | 88 | UnwindData |  |
| 49 | `ctlI2CAccess` | `0xA6450` | 88 | UnwindData |  |
| 83 | `ctlSetCurrentSharpness` | `0xA64B0` | 88 | UnwindData |  |
| 31 | `ctlGetCurrentSharpness` | `0xA6510` | 88 | UnwindData |  |
| 43 | `ctlGetSharpnessCaps` | `0xA6570` | 88 | UnwindData |  |
| 48 | `ctlGetZeDevice` | `0xA65D0` | 104 | UnwindData |  |
| 28 | `ctlGetAdaperDisplayEncoderProperties` | `0xA6640` | 88 | UnwindData |  |
| 33 | `ctlGetDisplayProperties` | `0xA66A0` | 88 | UnwindData |  |
| 14 | `ctlEnumerateDisplayOutputs` | `0xA6700` | 104 | UnwindData |  |
| 3 | `ctlCheckDriverVersion` | `0xA6770` | 86 | UnwindData |  |
| 92 | `ctlWaitForPropertyChange` | `0xA67D0` | 88 | UnwindData |  |
| 87 | `ctlSetRuntimePath` | `0xA6830` | 90 | UnwindData |  |
| 80 | `ctlReservedCall` | `0xA68E0` | 88 | UnwindData |  |
| 4 | `ctlClose` | `0xA6940` | 55 | UnwindData |  |
| 50 | `ctlInit` | `0xA6980` | 162 | UnwindData |  |
| 13 | `ctlEnumerateDevices` | `0xA6A30` | 104 | UnwindData |  |
| 32 | `ctlGetDeviceProperties` | `0xA6AA0` | 88 | UnwindData |  |
| 44 | `ctlGetSupported3DCapabilities` | `0xA6B00` | 88 | UnwindData |  |
| 40 | `ctlGetSet3DFeature` | `0xA6B60` | 88 | UnwindData |  |
