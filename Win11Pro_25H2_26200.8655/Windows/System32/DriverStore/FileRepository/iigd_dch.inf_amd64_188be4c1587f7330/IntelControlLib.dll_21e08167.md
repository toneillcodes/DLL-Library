# Binary Specification: IntelControlLib.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\IntelControlLib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `21e081675fd1c07e544414b5fcde14e3e6e1675d8282cba32945acaec3699287`
* **Total Exported Functions:** 92

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ctlAUXAccess` | `0x1370` | 140 | UnwindData |  |
| 2 | `ctlCheckDriverVersion` | `0x1400` | 65 | UnwindData |  |
| 3 | `ctlClose` | `0x1450` | 79 | UnwindData |  |
| 4 | `ctlEngineGetActivity` | `0x14A0` | 138 | UnwindData |  |
| 5 | `ctlEngineGetProperties` | `0x1530` | 138 | UnwindData |  |
| 6 | `ctlEnumEngineGroups` | `0x15C0` | 87 | UnwindData |  |
| 7 | `ctlEnumFans` | `0x1620` | 87 | UnwindData |  |
| 8 | `ctlEnumFrequencyDomains` | `0x1680` | 87 | UnwindData |  |
| 9 | `ctlEnumMemoryModules` | `0x16E0` | 87 | UnwindData |  |
| 10 | `ctlEnumPowerDomains` | `0x1740` | 87 | UnwindData |  |
| 11 | `ctlEnumTemperatureSensors` | `0x17A0` | 87 | UnwindData |  |
| 12 | `ctlEnumerateDevices` | `0x1800` | 97 | UnwindData |  |
| 13 | `ctlEnumerateDisplayOutputs` | `0x1870` | 87 | UnwindData |  |
| 14 | `ctlFanGetConfig` | `0x18D0` | 140 | UnwindData |  |
| 15 | `ctlFanGetProperties` | `0x1960` | 138 | UnwindData |  |
| 16 | `ctlFanGetState` | `0x19F0` | 111 | UnwindData |  |
| 17 | `ctlFanSetDefaultMode` | `0x1A60` | 46 | UnwindData |  |
| 18 | `ctlFanSetFixedSpeedMode` | `0x1A90` | 138 | UnwindData |  |
| 19 | `ctlFanSetSpeedTableMode` | `0x1B20` | 140 | UnwindData |  |
| 20 | `ctlFrequencyGetAvailableClocks` | `0x1BB0` | 87 | UnwindData |  |
| 21 | `ctlFrequencyGetProperties` | `0x1C10` | 138 | UnwindData |  |
| 22 | `ctlFrequencyGetRange` | `0x1CA0` | 138 | UnwindData |  |
| 23 | `ctlFrequencyGetState` | `0x1D30` | 138 | UnwindData |  |
| 24 | `ctlFrequencyGetThrottleTime` | `0x1DC0` | 138 | UnwindData |  |
| 25 | `ctlFrequencySetRange` | `0x1E50` | 138 | UnwindData |  |
| 26 | `ctlGetAdaperDisplayEncoderProperties` | `0x1EE0` | 138 | UnwindData |  |
| 27 | `ctlGetBrightnessSetting` | `0x1F70` | 138 | UnwindData |  |
| 28 | `ctlGetCurrentScaling` | `0x2000` | 138 | UnwindData |  |
| 29 | `ctlGetCurrentSharpness` | `0x2090` | 138 | UnwindData |  |
| 30 | `ctlGetDeviceProperties` | `0x2120` | 140 | UnwindData |  |
| 31 | `ctlGetDisplayProperties` | `0x21B0` | 140 | UnwindData |  |
| 32 | `ctlGetIntelArcSyncInfoForMonitor` | `0x2240` | 138 | UnwindData |  |
| 33 | `ctlGetIntelArcSyncProfile` | `0x22D0` | 138 | UnwindData |  |
| 34 | `ctlGetLACEConfig` | `0x2360` | 138 | UnwindData |  |
| 35 | `ctlGetMuxProperties` | `0x23F0` | 66 | UnwindData |  |
| 36 | `ctlGetPowerOptimizationCaps` | `0x2440` | 138 | UnwindData |  |
| 37 | `ctlGetPowerOptimizationSetting` | `0x24D0` | 138 | UnwindData |  |
| 38 | `ctlGetSet3DFeature` | `0x2560` | 138 | UnwindData |  |
| 39 | `ctlGetSetRetroScaling` | `0x25F0` | 138 | UnwindData |  |
| 40 | `ctlGetSetVideoProcessingFeature` | `0x2680` | 138 | UnwindData |  |
| 41 | `ctlGetSharpnessCaps` | `0x2710` | 138 | UnwindData |  |
| 42 | `ctlGetSupported3DCapabilities` | `0x27A0` | 138 | UnwindData |  |
| 43 | `ctlGetSupportedRetroScalingCapability` | `0x2830` | 138 | UnwindData |  |
| 44 | `ctlGetSupportedScalingCapability` | `0x28C0` | 138 | UnwindData |  |
| 45 | `ctlGetSupportedVideoProcessingCapabilities` | `0x2950` | 138 | UnwindData |  |
| 46 | `ctlGetZeDevice` | `0x29E0` | 87 | UnwindData |  |
| 47 | `ctlI2CAccess` | `0x2A40` | 140 | UnwindData |  |
| 48 | `ctlInit` | `0x2AD0` | 433 | UnwindData |  |
| 49 | `ctlMemoryGetBandwidth` | `0x2C90` | 138 | UnwindData |  |
| 50 | `ctlMemoryGetProperties` | `0x2D20` | 138 | UnwindData |  |
| 51 | `ctlMemoryGetState` | `0x2DB0` | 138 | UnwindData |  |
| 52 | `ctlOverclockGetProperties` | `0x2E40` | 140 | UnwindData |  |
| 53 | `ctlOverclockGpuFrequencyOffsetGet` | `0x2ED0` | 66 | UnwindData |  |
| 54 | `ctlOverclockGpuFrequencyOffsetSet` | `0x2F20` | 67 | UnwindData |  |
| 55 | `ctlOverclockGpuLockGet` | `0x2F70` | 66 | UnwindData |  |
| 56 | `ctlOverclockGpuLockSet` | `0x2FC0` | 88 | UnwindData |  |
| 57 | `ctlOverclockGpuVoltageOffsetGet` | `0x3020` | 66 | UnwindData |  |
| 58 | `ctlOverclockGpuVoltageOffsetSet` | `0x3070` | 67 | UnwindData |  |
| 59 | `ctlOverclockPowerLimitGet` | `0x30C0` | 66 | UnwindData |  |
| 60 | `ctlOverclockPowerLimitSet` | `0x3110` | 67 | UnwindData |  |
| 61 | `ctlOverclockTemperatureLimitGet` | `0x3160` | 66 | UnwindData |  |
| 62 | `ctlOverclockTemperatureLimitSet` | `0x31B0` | 67 | UnwindData |  |
| 63 | `ctlOverclockVramFrequencyOffsetGet` | `0x3200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `ctlOverclockVramFrequencyOffsetSet` | `0x3200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `ctlOverclockVramVoltageOffsetGet` | `0x3200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `ctlOverclockVramVoltageOffsetSet` | `0x3200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `ctlOverclockWaiverSet` | `0x3210` | 46 | UnwindData |  |
| 68 | `ctlPanelDescriptorAccess` | `0x3240` | 138 | UnwindData |  |
| 69 | `ctlPciGetProperties` | `0x32D0` | 138 | UnwindData |  |
| 70 | `ctlPciGetState` | `0x3360` | 138 | UnwindData |  |
| 71 | `ctlPixelTransformationGetConfig` | `0x33F0` | 140 | UnwindData |  |
| 72 | `ctlPixelTransformationSetConfig` | `0x3480` | 138 | UnwindData |  |
| 73 | `ctlPowerGetEnergyCounter` | `0x3510` | 138 | UnwindData |  |
| 74 | `ctlPowerGetLimits` | `0x35A0` | 138 | UnwindData |  |
| 75 | `ctlPowerGetProperties` | `0x3630` | 138 | UnwindData |  |
| 76 | `ctlPowerSetLimits` | `0x36C0` | 138 | UnwindData |  |
| 77 | `ctlPowerTelemetryGet` | `0x3750` | 66 | UnwindData |  |
| 78 | `ctlReservedCall` | `0x37A0` | 238 | UnwindData |  |
| 79 | `ctlSetBrightnessSetting` | `0x3890` | 138 | UnwindData |  |
| 80 | `ctlSetCurrentScaling` | `0x3920` | 138 | UnwindData |  |
| 81 | `ctlSetCurrentSharpness` | `0x39B0` | 138 | UnwindData |  |
| 82 | `ctlSetIntelArcSyncProfile` | `0x3A40` | 138 | UnwindData |  |
| 83 | `ctlSetLACEConfig` | `0x3AD0` | 138 | UnwindData |  |
| 84 | `ctlSetPowerOptimizationSetting` | `0x3B60` | 138 | UnwindData |  |
| 85 | `ctlSetRuntimePath` | `0x3BF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `ctlSoftwarePSR` | `0x3C30` | 138 | UnwindData |  |
| 87 | `ctlTemperatureGetProperties` | `0x3CC0` | 138 | UnwindData |  |
| 88 | `ctlTemperatureGetState` | `0x3D50` | 91 | UnwindData |  |
| 89 | `ctlWaitForPropertyChange` | `0x3DB0` | 151 | UnwindData |  |
| 90 | `ctlpvtDisplaySwitch` | `0x3E50` | 66 | UnwindData |  |
| 91 | `ctlpvtEnumerateMuxDevicesOnAdapter` | `0x3EA0` | 87 | UnwindData |  |
| 92 | `ctlpvtTestFunction` | `0x3F00` | 252,092 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
