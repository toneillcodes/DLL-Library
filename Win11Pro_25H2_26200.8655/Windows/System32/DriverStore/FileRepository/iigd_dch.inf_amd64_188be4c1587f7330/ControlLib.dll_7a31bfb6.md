# Binary Specification: ControlLib.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\ControlLib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7a31bfb6a5689f234ea80353e9a382224fa68bf174e7c48ddab8b4ffcda43e69`
* **Total Exported Functions:** 91

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ctlAUXAccess` | `0x1070` | 327 | UnwindData |  |
| 2 | `ctlCheckDriverVersion` | `0x11C0` | 325 | UnwindData |  |
| 3 | `ctlClose` | `0x1310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ctlEngineGetActivity` | `0x1320` | 327 | UnwindData |  |
| 5 | `ctlEngineGetProperties` | `0x1470` | 327 | UnwindData |  |
| 6 | `ctlEnumEngineGroups` | `0x15C0` | 360 | UnwindData |  |
| 7 | `ctlEnumFans` | `0x1730` | 360 | UnwindData |  |
| 8 | `ctlEnumFrequencyDomains` | `0x18A0` | 360 | UnwindData |  |
| 9 | `ctlEnumMemoryModules` | `0x1A10` | 360 | UnwindData |  |
| 10 | `ctlEnumPowerDomains` | `0x1B80` | 360 | UnwindData |  |
| 11 | `ctlEnumTemperatureSensors` | `0x1CF0` | 360 | UnwindData |  |
| 12 | `ctlEnumerateDevices` | `0x1E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `ctlEnumerateDisplayOutputs` | `0x1E70` | 360 | UnwindData |  |
| 14 | `ctlEnumerateMuxDevices` | `0x1FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ctlFanGetConfig` | `0x1FF0` | 327 | UnwindData |  |
| 16 | `ctlFanGetProperties` | `0x2140` | 327 | UnwindData |  |
| 17 | `ctlFanGetState` | `0x2290` | 323 | UnwindData |  |
| 18 | `ctlFanSetDefaultMode` | `0x23E0` | 309 | UnwindData |  |
| 19 | `ctlFanSetFixedSpeedMode` | `0x2520` | 327 | UnwindData |  |
| 20 | `ctlFanSetSpeedTableMode` | `0x2670` | 327 | UnwindData |  |
| 21 | `ctlFrequencyGetAvailableClocks` | `0x27C0` | 325 | UnwindData |  |
| 22 | `ctlFrequencyGetProperties` | `0x2910` | 327 | UnwindData |  |
| 23 | `ctlFrequencyGetRange` | `0x2A60` | 327 | UnwindData |  |
| 24 | `ctlFrequencyGetState` | `0x2BB0` | 327 | UnwindData |  |
| 25 | `ctlFrequencyGetThrottleTime` | `0x2D00` | 327 | UnwindData |  |
| 26 | `ctlFrequencySetRange` | `0x2E50` | 327 | UnwindData |  |
| 27 | `ctlGetAdaperDisplayEncoderProperties` | `0x2FA0` | 327 | UnwindData |  |
| 28 | `ctlGetBrightnessSetting` | `0x30F0` | 327 | UnwindData |  |
| 29 | `ctlGetCurrentScaling` | `0x3240` | 327 | UnwindData |  |
| 30 | `ctlGetCurrentSharpness` | `0x3390` | 327 | UnwindData |  |
| 31 | `ctlGetDeviceProperties` | `0x34E0` | 327 | UnwindData |  |
| 32 | `ctlGetDisplayProperties` | `0x3630` | 327 | UnwindData |  |
| 33 | `ctlGetIntelArcSyncInfoForMonitor` | `0x3780` | 327 | UnwindData |  |
| 34 | `ctlGetIntelArcSyncProfile` | `0x38D0` | 327 | UnwindData |  |
| 35 | `ctlGetLACEConfig` | `0x3A20` | 327 | UnwindData |  |
| 36 | `ctlGetMuxProperties` | `0x3B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `ctlGetPowerOptimizationCaps` | `0x3B80` | 327 | UnwindData |  |
| 38 | `ctlGetPowerOptimizationSetting` | `0x3CD0` | 327 | UnwindData |  |
| 39 | `ctlGetSet3DFeature` | `0x3E20` | 327 | UnwindData |  |
| 40 | `ctlGetSetRetroScaling` | `0x3F70` | 327 | UnwindData |  |
| 41 | `ctlGetSetVideoProcessingFeature` | `0x40C0` | 327 | UnwindData |  |
| 42 | `ctlGetSharpnessCaps` | `0x4210` | 327 | UnwindData |  |
| 43 | `ctlGetSupported3DCapabilities` | `0x4360` | 327 | UnwindData |  |
| 44 | `ctlGetSupportedRetroScalingCapability` | `0x44B0` | 327 | UnwindData |  |
| 45 | `ctlGetSupportedScalingCapability` | `0x4600` | 327 | UnwindData |  |
| 46 | `ctlGetSupportedVideoProcessingCapabilities` | `0x4750` | 327 | UnwindData |  |
| 47 | `ctlGetZeDevice` | `0x48A0` | 325 | UnwindData |  |
| 48 | `ctlI2CAccess` | `0x49F0` | 327 | UnwindData |  |
| 49 | `ctlInit` | `0x4B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `ctlMemoryGetBandwidth` | `0x4B50` | 327 | UnwindData |  |
| 51 | `ctlMemoryGetProperties` | `0x4CA0` | 327 | UnwindData |  |
| 52 | `ctlMemoryGetState` | `0x4DF0` | 327 | UnwindData |  |
| 53 | `ctlOverclockGetProperties` | `0x4F40` | 327 | UnwindData |  |
| 54 | `ctlOverclockGpuFrequencyOffsetGet` | `0x5090` | 327 | UnwindData |  |
| 55 | `ctlOverclockGpuFrequencyOffsetSet` | `0x51E0` | 331 | UnwindData |  |
| 56 | `ctlOverclockGpuLockGet` | `0x5330` | 327 | UnwindData |  |
| 57 | `ctlOverclockGpuLockSet` | `0x5480` | 357 | UnwindData |  |
| 58 | `ctlOverclockGpuVoltageOffsetGet` | `0x55F0` | 327 | UnwindData |  |
| 59 | `ctlOverclockGpuVoltageOffsetSet` | `0x5740` | 331 | UnwindData |  |
| 60 | `ctlOverclockPowerLimitGet` | `0x5890` | 327 | UnwindData |  |
| 61 | `ctlOverclockPowerLimitSet` | `0x59E0` | 331 | UnwindData |  |
| 62 | `ctlOverclockTemperatureLimitGet` | `0x5B30` | 327 | UnwindData |  |
| 63 | `ctlOverclockTemperatureLimitSet` | `0x5C80` | 331 | UnwindData |  |
| 64 | `ctlOverclockVramFrequencyOffsetGet` | `0x5DD0` | 327 | UnwindData |  |
| 65 | `ctlOverclockVramFrequencyOffsetSet` | `0x5F20` | 331 | UnwindData |  |
| 66 | `ctlOverclockVramVoltageOffsetGet` | `0x6070` | 327 | UnwindData |  |
| 67 | `ctlOverclockVramVoltageOffsetSet` | `0x61C0` | 331 | UnwindData |  |
| 68 | `ctlOverclockWaiverSet` | `0x6310` | 309 | UnwindData |  |
| 69 | `ctlPanelDescriptorAccess` | `0x6450` | 327 | UnwindData |  |
| 70 | `ctlPciGetProperties` | `0x65A0` | 327 | UnwindData |  |
| 71 | `ctlPciGetState` | `0x66F0` | 327 | UnwindData |  |
| 72 | `ctlPixelTransformationGetConfig` | `0x6840` | 327 | UnwindData |  |
| 73 | `ctlPixelTransformationSetConfig` | `0x6990` | 327 | UnwindData |  |
| 74 | `ctlPowerGetEnergyCounter` | `0x6AE0` | 327 | UnwindData |  |
| 75 | `ctlPowerGetLimits` | `0x6C30` | 327 | UnwindData |  |
| 76 | `ctlPowerGetProperties` | `0x6D80` | 327 | UnwindData |  |
| 77 | `ctlPowerSetLimits` | `0x6ED0` | 327 | UnwindData |  |
| 78 | `ctlPowerTelemetryGet` | `0x7020` | 327 | UnwindData |  |
| 79 | `ctlReservedCall` | `0x7170` | 327 | UnwindData |  |
| 80 | `ctlSetBrightnessSetting` | `0x72C0` | 327 | UnwindData |  |
| 81 | `ctlSetCurrentScaling` | `0x7410` | 327 | UnwindData |  |
| 82 | `ctlSetCurrentSharpness` | `0x7560` | 327 | UnwindData |  |
| 83 | `ctlSetIntelArcSyncProfile` | `0x76B0` | 327 | UnwindData |  |
| 84 | `ctlSetLACEConfig` | `0x7800` | 327 | UnwindData |  |
| 85 | `ctlSetPowerOptimizationSetting` | `0x7950` | 327 | UnwindData |  |
| 86 | `ctlSetRuntimePath` | `0x7AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `ctlSoftwarePSR` | `0x7AB0` | 327 | UnwindData |  |
| 88 | `ctlSwitchMux` | `0x7C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `ctlTemperatureGetProperties` | `0x7C10` | 327 | UnwindData |  |
| 90 | `ctlTemperatureGetState` | `0x7D60` | 327 | UnwindData |  |
| 91 | `ctlWaitForPropertyChange` | `0x7EB0` | 327 | UnwindData |  |
