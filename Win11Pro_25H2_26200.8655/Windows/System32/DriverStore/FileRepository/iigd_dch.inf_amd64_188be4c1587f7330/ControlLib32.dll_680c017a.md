# Binary Specification: ControlLib32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\ControlLib32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `680c017ae4427c787a23bc8e31369b1657761ff3c5d3ab3bf811a76bdbd0f623`
* **Total Exported Functions:** 91

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ctlAUXAccess` | `0x1060` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ctlCheckDriverVersion` | `0x1180` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ctlClose` | `0x12A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ctlEngineGetActivity` | `0x12B0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ctlEngineGetProperties` | `0x13D0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ctlEnumEngineGroups` | `0x14F0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ctlEnumFans` | `0x1630` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `ctlEnumFrequencyDomains` | `0x1770` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `ctlEnumMemoryModules` | `0x18B0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `ctlEnumPowerDomains` | `0x19F0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ctlEnumTemperatureSensors` | `0x1B30` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `ctlEnumerateDevices` | `0x1C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `ctlEnumerateDisplayOutputs` | `0x1C80` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `ctlEnumerateMuxDevices` | `0x1DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ctlFanGetConfig` | `0x1DD0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ctlFanGetProperties` | `0x1EF0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `ctlFanGetState` | `0x2010` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ctlFanSetDefaultMode` | `0x2130` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ctlFanSetFixedSpeedMode` | `0x2240` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `ctlFanSetSpeedTableMode` | `0x2360` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `ctlFrequencyGetAvailableClocks` | `0x2480` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `ctlFrequencyGetProperties` | `0x25A0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `ctlFrequencyGetRange` | `0x26C0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `ctlFrequencyGetState` | `0x27E0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ctlFrequencyGetThrottleTime` | `0x2900` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `ctlFrequencySetRange` | `0x2A20` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `ctlGetAdaperDisplayEncoderProperties` | `0x2B40` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `ctlGetBrightnessSetting` | `0x2C60` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `ctlGetCurrentScaling` | `0x2D80` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `ctlGetCurrentSharpness` | `0x2EA0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `ctlGetDeviceProperties` | `0x2FC0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `ctlGetDisplayProperties` | `0x30E0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `ctlGetIntelArcSyncInfoForMonitor` | `0x3200` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `ctlGetIntelArcSyncProfile` | `0x3320` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `ctlGetLACEConfig` | `0x3440` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `ctlGetMuxProperties` | `0x3560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `ctlGetPowerOptimizationCaps` | `0x3570` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `ctlGetPowerOptimizationSetting` | `0x3690` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `ctlGetSet3DFeature` | `0x37B0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `ctlGetSetRetroScaling` | `0x38D0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `ctlGetSetVideoProcessingFeature` | `0x39F0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `ctlGetSharpnessCaps` | `0x3B10` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `ctlGetSupported3DCapabilities` | `0x3C30` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `ctlGetSupportedRetroScalingCapability` | `0x3D50` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `ctlGetSupportedScalingCapability` | `0x3E70` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `ctlGetSupportedVideoProcessingCapabilities` | `0x3F90` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `ctlGetZeDevice` | `0x40B0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `ctlI2CAccess` | `0x41D0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `ctlInit` | `0x42F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `ctlMemoryGetBandwidth` | `0x4300` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `ctlMemoryGetProperties` | `0x4420` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `ctlMemoryGetState` | `0x4540` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `ctlOverclockGetProperties` | `0x4660` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `ctlOverclockGpuFrequencyOffsetGet` | `0x4780` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `ctlOverclockGpuFrequencyOffsetSet` | `0x48A0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `ctlOverclockGpuLockGet` | `0x49C0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `ctlOverclockGpuLockSet` | `0x4AE0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `ctlOverclockGpuVoltageOffsetGet` | `0x4C10` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `ctlOverclockGpuVoltageOffsetSet` | `0x4D30` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `ctlOverclockPowerLimitGet` | `0x4E50` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `ctlOverclockPowerLimitSet` | `0x4F80` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `ctlOverclockTemperatureLimitGet` | `0x50A0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `ctlOverclockTemperatureLimitSet` | `0x51C0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `ctlOverclockVramFrequencyOffsetGet` | `0x52E0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `ctlOverclockVramFrequencyOffsetSet` | `0x5400` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `ctlOverclockVramVoltageOffsetGet` | `0x5520` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `ctlOverclockVramVoltageOffsetSet` | `0x5640` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `ctlOverclockWaiverSet` | `0x5760` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `ctlPanelDescriptorAccess` | `0x5870` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `ctlPciGetProperties` | `0x5990` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `ctlPciGetState` | `0x5AB0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `ctlPixelTransformationGetConfig` | `0x5BD0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `ctlPixelTransformationSetConfig` | `0x5CF0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `ctlPowerGetEnergyCounter` | `0x5E10` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `ctlPowerGetLimits` | `0x5F30` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `ctlPowerGetProperties` | `0x6050` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `ctlPowerSetLimits` | `0x6170` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `ctlPowerTelemetryGet` | `0x6290` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `ctlReservedCall` | `0x63B0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `ctlSetBrightnessSetting` | `0x64D0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `ctlSetCurrentScaling` | `0x65F0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `ctlSetCurrentSharpness` | `0x6710` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `ctlSetIntelArcSyncProfile` | `0x6830` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `ctlSetLACEConfig` | `0x6950` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `ctlSetPowerOptimizationSetting` | `0x6A70` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `ctlSetRuntimePath` | `0x6B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `ctlSoftwarePSR` | `0x6BA0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `ctlSwitchMux` | `0x6CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `ctlTemperatureGetProperties` | `0x6CD0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `ctlTemperatureGetState` | `0x6DF0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `ctlWaitForPropertyChange` | `0x6F10` | 89,045 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
