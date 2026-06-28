# Binary Specification: IntelControlLib.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\lenovofnandfunctionkeys.inf_amd64_fa50a878363b0cec\IntelControlLib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `916c4cf8edd1c88f81004a3d417d8c2f12ee9ea764e2ff33ad803f9129286873`
* **Total Exported Functions:** 87

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ctlAUXAccess` | `0x1020` | 140 | UnwindData |  |
| 2 | `ctlCheckDriverVersion` | `0x10B0` | 65 | UnwindData |  |
| 3 | `ctlClose` | `0x1100` | 79 | UnwindData |  |
| 4 | `ctlEngineGetActivity` | `0x1150` | 138 | UnwindData |  |
| 5 | `ctlEngineGetProperties` | `0x11E0` | 138 | UnwindData |  |
| 6 | `ctlEnumEngineGroups` | `0x1270` | 87 | UnwindData |  |
| 7 | `ctlEnumFans` | `0x12D0` | 87 | UnwindData |  |
| 8 | `ctlEnumFrequencyDomains` | `0x1330` | 87 | UnwindData |  |
| 9 | `ctlEnumMemoryModules` | `0x1390` | 87 | UnwindData |  |
| 10 | `ctlEnumPowerDomains` | `0x13F0` | 87 | UnwindData |  |
| 11 | `ctlEnumTemperatureSensors` | `0x1450` | 87 | UnwindData |  |
| 12 | `ctlEnumerateDevices` | `0x14B0` | 97 | UnwindData |  |
| 13 | `ctlEnumerateDisplayOutputs` | `0x1520` | 87 | UnwindData |  |
| 14 | `ctlFanGetConfig` | `0x1580` | 140 | UnwindData |  |
| 15 | `ctlFanGetProperties` | `0x1610` | 138 | UnwindData |  |
| 16 | `ctlFanGetState` | `0x16A0` | 111 | UnwindData |  |
| 17 | `ctlFanSetDefaultMode` | `0x1710` | 46 | UnwindData |  |
| 18 | `ctlFanSetFixedSpeedMode` | `0x1740` | 138 | UnwindData |  |
| 19 | `ctlFanSetSpeedTableMode` | `0x17D0` | 140 | UnwindData |  |
| 20 | `ctlFrequencyGetAvailableClocks` | `0x1860` | 87 | UnwindData |  |
| 21 | `ctlFrequencyGetProperties` | `0x18C0` | 138 | UnwindData |  |
| 22 | `ctlFrequencyGetRange` | `0x1950` | 138 | UnwindData |  |
| 23 | `ctlFrequencyGetState` | `0x19E0` | 138 | UnwindData |  |
| 24 | `ctlFrequencyGetThrottleTime` | `0x1A70` | 138 | UnwindData |  |
| 25 | `ctlFrequencySetRange` | `0x1B00` | 138 | UnwindData |  |
| 26 | `ctlGetAdaperDisplayEncoderProperties` | `0x1B90` | 138 | UnwindData |  |
| 27 | `ctlGetCurrentScaling` | `0x1C20` | 138 | UnwindData |  |
| 28 | `ctlGetCurrentSharpness` | `0x1CB0` | 138 | UnwindData |  |
| 29 | `ctlGetDeviceProperties` | `0x1D40` | 140 | UnwindData |  |
| 30 | `ctlGetDisplayProperties` | `0x1DD0` | 140 | UnwindData |  |
| 31 | `ctlGetIntelArcSyncInfoForMonitor` | `0x1E60` | 138 | UnwindData |  |
| 32 | `ctlGetIntelArcSyncProfile` | `0x1EF0` | 138 | UnwindData |  |
| 33 | `ctlGetLACEConfig` | `0x1F80` | 138 | UnwindData |  |
| 34 | `ctlGetPowerOptimizationCaps` | `0x2010` | 138 | UnwindData |  |
| 35 | `ctlGetPowerOptimizationSetting` | `0x20A0` | 138 | UnwindData |  |
| 36 | `ctlGetSet3DFeature` | `0x2130` | 138 | UnwindData |  |
| 37 | `ctlGetSetRetroScaling` | `0x21C0` | 138 | UnwindData |  |
| 38 | `ctlGetSetVideoProcessingFeature` | `0x2250` | 138 | UnwindData |  |
| 39 | `ctlGetSharpnessCaps` | `0x22E0` | 138 | UnwindData |  |
| 40 | `ctlGetSupported3DCapabilities` | `0x2370` | 138 | UnwindData |  |
| 41 | `ctlGetSupportedRetroScalingCapability` | `0x2400` | 138 | UnwindData |  |
| 42 | `ctlGetSupportedScalingCapability` | `0x2490` | 138 | UnwindData |  |
| 43 | `ctlGetSupportedVideoProcessingCapabilities` | `0x2520` | 138 | UnwindData |  |
| 44 | `ctlGetZeDevice` | `0x25B0` | 87 | UnwindData |  |
| 45 | `ctlI2CAccess` | `0x2610` | 140 | UnwindData |  |
| 46 | `ctlInit` | `0x26A0` | 433 | UnwindData |  |
| 47 | `ctlMemoryGetBandwidth` | `0x2860` | 138 | UnwindData |  |
| 48 | `ctlMemoryGetProperties` | `0x28F0` | 138 | UnwindData |  |
| 49 | `ctlMemoryGetState` | `0x2980` | 138 | UnwindData |  |
| 50 | `ctlOverclockGetProperties` | `0x2A10` | 140 | UnwindData |  |
| 51 | `ctlOverclockGpuFrequencyOffsetGet` | `0x2AA0` | 66 | UnwindData |  |
| 52 | `ctlOverclockGpuFrequencyOffsetSet` | `0x2AF0` | 67 | UnwindData |  |
| 53 | `ctlOverclockGpuLockGet` | `0x2B40` | 66 | UnwindData |  |
| 54 | `ctlOverclockGpuLockSet` | `0x2B90` | 88 | UnwindData |  |
| 55 | `ctlOverclockGpuVoltageOffsetGet` | `0x2BF0` | 66 | UnwindData |  |
| 56 | `ctlOverclockGpuVoltageOffsetSet` | `0x2C40` | 67 | UnwindData |  |
| 57 | `ctlOverclockPowerLimitGet` | `0x2C90` | 66 | UnwindData |  |
| 58 | `ctlOverclockPowerLimitSet` | `0x2CE0` | 67 | UnwindData |  |
| 59 | `ctlOverclockTemperatureLimitGet` | `0x2D30` | 66 | UnwindData |  |
| 60 | `ctlOverclockTemperatureLimitSet` | `0x2D80` | 67 | UnwindData |  |
| 61 | `ctlOverclockVramFrequencyOffsetGet` | `0x2DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `ctlOverclockVramFrequencyOffsetSet` | `0x2DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `ctlOverclockVramVoltageOffsetGet` | `0x2DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `ctlOverclockVramVoltageOffsetSet` | `0x2DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `ctlOverclockWaiverSet` | `0x2DE0` | 46 | UnwindData |  |
| 66 | `ctlPanelDescriptorAccess` | `0x2E10` | 138 | UnwindData |  |
| 67 | `ctlPciGetProperties` | `0x2EA0` | 138 | UnwindData |  |
| 68 | `ctlPciGetState` | `0x2F30` | 138 | UnwindData |  |
| 69 | `ctlPixelTransformationGetConfig` | `0x2FC0` | 140 | UnwindData |  |
| 70 | `ctlPixelTransformationSetConfig` | `0x3050` | 138 | UnwindData |  |
| 71 | `ctlPowerGetEnergyCounter` | `0x30E0` | 138 | UnwindData |  |
| 72 | `ctlPowerGetLimits` | `0x3170` | 138 | UnwindData |  |
| 73 | `ctlPowerGetProperties` | `0x3200` | 138 | UnwindData |  |
| 74 | `ctlPowerSetLimits` | `0x3290` | 138 | UnwindData |  |
| 75 | `ctlPowerTelemetryGet` | `0x3320` | 66 | UnwindData |  |
| 76 | `ctlReservedCall` | `0x3370` | 238 | UnwindData |  |
| 77 | `ctlSetCurrentScaling` | `0x3460` | 138 | UnwindData |  |
| 78 | `ctlSetCurrentSharpness` | `0x34F0` | 138 | UnwindData |  |
| 79 | `ctlSetIntelArcSyncProfile` | `0x3580` | 138 | UnwindData |  |
| 80 | `ctlSetLACEConfig` | `0x3610` | 138 | UnwindData |  |
| 81 | `ctlSetPowerOptimizationSetting` | `0x36A0` | 138 | UnwindData |  |
| 82 | `ctlSetRuntimePath` | `0x3730` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `ctlSoftwarePSR` | `0x3770` | 138 | UnwindData |  |
| 84 | `ctlTemperatureGetProperties` | `0x3800` | 138 | UnwindData |  |
| 85 | `ctlTemperatureGetState` | `0x3890` | 91 | UnwindData |  |
| 86 | `ctlWaitForPropertyChange` | `0x38F0` | 151 | UnwindData |  |
| 87 | `ctlpvtTestFunction` | `0x3990` | 230,048 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
