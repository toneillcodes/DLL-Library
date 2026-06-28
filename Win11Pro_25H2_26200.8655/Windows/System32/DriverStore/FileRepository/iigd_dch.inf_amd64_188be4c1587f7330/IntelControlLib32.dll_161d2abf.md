# Binary Specification: IntelControlLib32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\IntelControlLib32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `161d2abfb73b22c22a07cc11406ebf212375b738173a71cf093b2cfff7207c82`
* **Total Exported Functions:** 92

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ctlAUXAccess` | `0x1430` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ctlCheckDriverVersion` | `0x1490` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ctlClose` | `0x14C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ctlEngineGetActivity` | `0x1500` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ctlEngineGetProperties` | `0x1560` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ctlEnumEngineGroups` | `0x15C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ctlEnumFans` | `0x15F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `ctlEnumFrequencyDomains` | `0x1620` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `ctlEnumMemoryModules` | `0x1650` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ctlEnumPowerDomains` | `0x1680` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ctlEnumTemperatureSensors` | `0x16B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `ctlEnumerateDevices` | `0x16E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `ctlEnumerateDisplayOutputs` | `0x1720` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `ctlFanGetConfig` | `0x1750` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ctlFanGetProperties` | `0x17B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ctlFanGetState` | `0x1810` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `ctlFanSetDefaultMode` | `0x1850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ctlFanSetFixedSpeedMode` | `0x1870` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ctlFanSetSpeedTableMode` | `0x18D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `ctlFrequencyGetAvailableClocks` | `0x1930` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `ctlFrequencyGetProperties` | `0x1960` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `ctlFrequencyGetRange` | `0x19C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `ctlFrequencyGetState` | `0x1A20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `ctlFrequencyGetThrottleTime` | `0x1A80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ctlFrequencySetRange` | `0x1AE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `ctlGetAdaperDisplayEncoderProperties` | `0x1B40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `ctlGetBrightnessSetting` | `0x1BA0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `ctlGetCurrentScaling` | `0x1C00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `ctlGetCurrentSharpness` | `0x1C60` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `ctlGetDeviceProperties` | `0x1CC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `ctlGetDisplayProperties` | `0x1D20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `ctlGetIntelArcSyncInfoForMonitor` | `0x1D80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `ctlGetIntelArcSyncProfile` | `0x1DE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `ctlGetLACEConfig` | `0x1E40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `ctlGetMuxProperties` | `0x1EA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `ctlGetPowerOptimizationCaps` | `0x1ED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `ctlGetPowerOptimizationSetting` | `0x1F30` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `ctlGetSet3DFeature` | `0x1F90` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `ctlGetSetRetroScaling` | `0x1FF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `ctlGetSetVideoProcessingFeature` | `0x2050` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `ctlGetSharpnessCaps` | `0x20B0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `ctlGetSupported3DCapabilities` | `0x2110` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `ctlGetSupportedRetroScalingCapability` | `0x2170` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `ctlGetSupportedScalingCapability` | `0x21D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `ctlGetSupportedVideoProcessingCapabilities` | `0x2230` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `ctlGetZeDevice` | `0x2290` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `ctlI2CAccess` | `0x22C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `ctlInit` | `0x2320` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `ctlMemoryGetBandwidth` | `0x2470` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `ctlMemoryGetProperties` | `0x24D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `ctlMemoryGetState` | `0x2530` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `ctlOverclockGetProperties` | `0x2590` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `ctlOverclockGpuFrequencyOffsetGet` | `0x25F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `ctlOverclockGpuFrequencyOffsetSet` | `0x2620` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `ctlOverclockGpuLockGet` | `0x2650` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `ctlOverclockGpuLockSet` | `0x2680` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `ctlOverclockGpuVoltageOffsetGet` | `0x26C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `ctlOverclockGpuVoltageOffsetSet` | `0x26F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `ctlOverclockPowerLimitGet` | `0x2720` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `ctlOverclockPowerLimitSet` | `0x2750` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `ctlOverclockTemperatureLimitGet` | `0x2780` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `ctlOverclockTemperatureLimitSet` | `0x27B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `ctlOverclockVramFrequencyOffsetGet` | `0x27E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `ctlOverclockVramFrequencyOffsetSet` | `0x27E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `ctlOverclockVramVoltageOffsetGet` | `0x27E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `ctlOverclockVramVoltageOffsetSet` | `0x27E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `ctlOverclockWaiverSet` | `0x27F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `ctlPanelDescriptorAccess` | `0x2810` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `ctlPciGetProperties` | `0x2870` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `ctlPciGetState` | `0x28D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `ctlPixelTransformationGetConfig` | `0x2930` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `ctlPixelTransformationSetConfig` | `0x2990` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `ctlPowerGetEnergyCounter` | `0x29F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `ctlPowerGetLimits` | `0x2A50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `ctlPowerGetProperties` | `0x2AB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `ctlPowerSetLimits` | `0x2B10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `ctlPowerTelemetryGet` | `0x2B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `ctlReservedCall` | `0x2BA0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `ctlSetBrightnessSetting` | `0x2C90` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `ctlSetCurrentScaling` | `0x2CF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `ctlSetCurrentSharpness` | `0x2D50` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `ctlSetIntelArcSyncProfile` | `0x2DB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `ctlSetLACEConfig` | `0x2E10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `ctlSetPowerOptimizationSetting` | `0x2E70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `ctlSetRuntimePath` | `0x2ED0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `ctlSoftwarePSR` | `0x2F20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `ctlTemperatureGetProperties` | `0x2F80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `ctlTemperatureGetState` | `0x2FE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `ctlWaitForPropertyChange` | `0x3020` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `ctlpvtDisplaySwitch` | `0x3080` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `ctlpvtEnumerateMuxDevicesOnAdapter` | `0x30B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `ctlpvtTestFunction` | `0x30E0` | 222,964 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
