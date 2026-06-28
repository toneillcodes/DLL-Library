# Binary Specification: igd10um64xe.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\igd10um64xe.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d36e3ef5bfa8b16957443a490b2c059dbc18d64b197ebe2832fcc1cd5f3fd301`
* **Total Exported Functions:** 94

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `ctlClose` | `0x28F80` | 55 | UnwindData |  |
| 52 | `ctlInit` | `0x28FC0` | 200 | UnwindData |  |
| 2 | `OpenAdapter10_2` | `0xCBDB0` | 224 | UnwindData |  |
| 1 | `OpenAdapter10` | `0x282930` | 252 | UnwindData |  |
| 3 | `GTPin_Init` | `0x6AA7A0` | 89,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ctlAUXAccess` | `0x6C0480` | 88 | UnwindData |  |
| 5 | `ctlCheckDriverVersion` | `0x6C04E0` | 86 | UnwindData |  |
| 7 | `ctlEngineGetActivity` | `0x6C0540` | 88 | UnwindData |  |
| 8 | `ctlEngineGetProperties` | `0x6C05A0` | 88 | UnwindData |  |
| 9 | `ctlEnumEngineGroups` | `0x6C0600` | 104 | UnwindData |  |
| 10 | `ctlEnumFans` | `0x6C0670` | 104 | UnwindData |  |
| 11 | `ctlEnumFrequencyDomains` | `0x6C06E0` | 104 | UnwindData |  |
| 12 | `ctlEnumMemoryModules` | `0x6C0750` | 104 | UnwindData |  |
| 13 | `ctlEnumPowerDomains` | `0x6C07C0` | 104 | UnwindData |  |
| 14 | `ctlEnumTemperatureSensors` | `0x6C0830` | 104 | UnwindData |  |
| 15 | `ctlEnumerateDevices` | `0x6C08A0` | 104 | UnwindData |  |
| 16 | `ctlEnumerateDisplayOutputs` | `0x6C0910` | 104 | UnwindData |  |
| 17 | `ctlEnumerateMuxDevices` | `0x6C0980` | 104 | UnwindData |  |
| 18 | `ctlFanGetConfig` | `0x6C09F0` | 88 | UnwindData |  |
| 19 | `ctlFanGetProperties` | `0x6C0A50` | 88 | UnwindData |  |
| 20 | `ctlFanGetState` | `0x6C0AB0` | 102 | UnwindData |  |
| 21 | `ctlFanSetDefaultMode` | `0x6C0B20` | 72 | UnwindData |  |
| 22 | `ctlFanSetFixedSpeedMode` | `0x6C0B70` | 88 | UnwindData |  |
| 23 | `ctlFanSetSpeedTableMode` | `0x6C0BD0` | 88 | UnwindData |  |
| 24 | `ctlFrequencyGetAvailableClocks` | `0x6C0C30` | 104 | UnwindData |  |
| 25 | `ctlFrequencyGetProperties` | `0x6C0CA0` | 88 | UnwindData |  |
| 26 | `ctlFrequencyGetRange` | `0x6C0D00` | 88 | UnwindData |  |
| 27 | `ctlFrequencyGetState` | `0x6C0D60` | 88 | UnwindData |  |
| 28 | `ctlFrequencyGetThrottleTime` | `0x6C0DC0` | 88 | UnwindData |  |
| 29 | `ctlFrequencySetRange` | `0x6C0E20` | 88 | UnwindData |  |
| 30 | `ctlGetAdaperDisplayEncoderProperties` | `0x6C0E80` | 88 | UnwindData |  |
| 31 | `ctlGetBrightnessSetting` | `0x6C0EE0` | 88 | UnwindData |  |
| 32 | `ctlGetCurrentScaling` | `0x6C0F40` | 88 | UnwindData |  |
| 33 | `ctlGetCurrentSharpness` | `0x6C0FA0` | 88 | UnwindData |  |
| 34 | `ctlGetDeviceProperties` | `0x6C1000` | 88 | UnwindData |  |
| 35 | `ctlGetDisplayProperties` | `0x6C1060` | 88 | UnwindData |  |
| 36 | `ctlGetIntelArcSyncInfoForMonitor` | `0x6C10C0` | 88 | UnwindData |  |
| 37 | `ctlGetIntelArcSyncProfile` | `0x6C1120` | 88 | UnwindData |  |
| 38 | `ctlGetLACEConfig` | `0x6C1180` | 88 | UnwindData |  |
| 39 | `ctlGetMuxProperties` | `0x6C11E0` | 88 | UnwindData |  |
| 40 | `ctlGetPowerOptimizationCaps` | `0x6C1240` | 88 | UnwindData |  |
| 41 | `ctlGetPowerOptimizationSetting` | `0x6C12A0` | 88 | UnwindData |  |
| 42 | `ctlGetSet3DFeature` | `0x6C1300` | 88 | UnwindData |  |
| 43 | `ctlGetSetRetroScaling` | `0x6C1360` | 88 | UnwindData |  |
| 44 | `ctlGetSetVideoProcessingFeature` | `0x6C13C0` | 88 | UnwindData |  |
| 45 | `ctlGetSharpnessCaps` | `0x6C1420` | 88 | UnwindData |  |
| 46 | `ctlGetSupported3DCapabilities` | `0x6C1480` | 88 | UnwindData |  |
| 47 | `ctlGetSupportedRetroScalingCapability` | `0x6C14E0` | 88 | UnwindData |  |
| 48 | `ctlGetSupportedScalingCapability` | `0x6C1540` | 88 | UnwindData |  |
| 49 | `ctlGetSupportedVideoProcessingCapabilities` | `0x6C15A0` | 88 | UnwindData |  |
| 50 | `ctlGetZeDevice` | `0x6C1600` | 104 | UnwindData |  |
| 51 | `ctlI2CAccess` | `0x6C1670` | 88 | UnwindData |  |
| 53 | `ctlMemoryGetBandwidth` | `0x6C16D0` | 88 | UnwindData |  |
| 54 | `ctlMemoryGetProperties` | `0x6C1730` | 88 | UnwindData |  |
| 55 | `ctlMemoryGetState` | `0x6C1790` | 88 | UnwindData |  |
| 56 | `ctlOverclockGetProperties` | `0x6C17F0` | 88 | UnwindData |  |
| 57 | `ctlOverclockGpuFrequencyOffsetGet` | `0x6C1850` | 88 | UnwindData |  |
| 58 | `ctlOverclockGpuFrequencyOffsetSet` | `0x6C18B0` | 88 | UnwindData |  |
| 59 | `ctlOverclockGpuLockGet` | `0x6C1910` | 88 | UnwindData |  |
| 60 | `ctlOverclockGpuLockSet` | `0x6C1970` | 109 | UnwindData |  |
| 61 | `ctlOverclockGpuVoltageOffsetGet` | `0x6C19E0` | 88 | UnwindData |  |
| 62 | `ctlOverclockGpuVoltageOffsetSet` | `0x6C1A40` | 88 | UnwindData |  |
| 63 | `ctlOverclockPowerLimitGet` | `0x6C1AA0` | 88 | UnwindData |  |
| 64 | `ctlOverclockPowerLimitSet` | `0x6C1B00` | 88 | UnwindData |  |
| 65 | `ctlOverclockTemperatureLimitGet` | `0x6C1B60` | 88 | UnwindData |  |
| 66 | `ctlOverclockTemperatureLimitSet` | `0x6C1BC0` | 88 | UnwindData |  |
| 67 | `ctlOverclockVramFrequencyOffsetGet` | `0x6C1C20` | 88 | UnwindData |  |
| 68 | `ctlOverclockVramFrequencyOffsetSet` | `0x6C1C80` | 88 | UnwindData |  |
| 69 | `ctlOverclockVramVoltageOffsetGet` | `0x6C1CE0` | 88 | UnwindData |  |
| 70 | `ctlOverclockVramVoltageOffsetSet` | `0x6C1D40` | 88 | UnwindData |  |
| 71 | `ctlOverclockWaiverSet` | `0x6C1DA0` | 72 | UnwindData |  |
| 72 | `ctlPanelDescriptorAccess` | `0x6C1DF0` | 88 | UnwindData |  |
| 73 | `ctlPciGetProperties` | `0x6C1E50` | 88 | UnwindData |  |
| 74 | `ctlPciGetState` | `0x6C1EB0` | 88 | UnwindData |  |
| 75 | `ctlPixelTransformationGetConfig` | `0x6C1F10` | 88 | UnwindData |  |
| 76 | `ctlPixelTransformationSetConfig` | `0x6C1F70` | 88 | UnwindData |  |
| 77 | `ctlPowerGetEnergyCounter` | `0x6C1FD0` | 88 | UnwindData |  |
| 78 | `ctlPowerGetLimits` | `0x6C2030` | 88 | UnwindData |  |
| 79 | `ctlPowerGetProperties` | `0x6C2090` | 88 | UnwindData |  |
| 80 | `ctlPowerSetLimits` | `0x6C20F0` | 88 | UnwindData |  |
| 81 | `ctlPowerTelemetryGet` | `0x6C2150` | 88 | UnwindData |  |
| 82 | `ctlReservedCall` | `0x6C21B0` | 88 | UnwindData |  |
| 83 | `ctlSetBrightnessSetting` | `0x6C2210` | 88 | UnwindData |  |
| 84 | `ctlSetCurrentScaling` | `0x6C2270` | 88 | UnwindData |  |
| 85 | `ctlSetCurrentSharpness` | `0x6C22D0` | 88 | UnwindData |  |
| 86 | `ctlSetIntelArcSyncProfile` | `0x6C2330` | 88 | UnwindData |  |
| 87 | `ctlSetLACEConfig` | `0x6C2390` | 88 | UnwindData |  |
| 88 | `ctlSetPowerOptimizationSetting` | `0x6C23F0` | 88 | UnwindData |  |
| 89 | `ctlSetRuntimePath` | `0x6C2450` | 90 | UnwindData |  |
| 90 | `ctlSoftwarePSR` | `0x6C24B0` | 88 | UnwindData |  |
| 91 | `ctlSwitchMux` | `0x6C2510` | 88 | UnwindData |  |
| 92 | `ctlTemperatureGetProperties` | `0x6C2570` | 88 | UnwindData |  |
| 93 | `ctlTemperatureGetState` | `0x6C25D0` | 88 | UnwindData |  |
| 94 | `ctlWaitForPropertyChange` | `0x6C2630` | 88 | UnwindData |  |
