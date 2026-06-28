# Binary Specification: ControlLib.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\lenovofnandfunctionkeys.inf_amd64_fa50a878363b0cec\ControlLib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ce2b22da7afa0f5a4681ed3ca0d2e4f77b180fc61a721048aa22ce6f837e548b`
* **Total Exported Functions:** 86

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ctlAUXAccess` | `0x1020` | 86 | UnwindData |  |
| 2 | `ctlCheckDriverVersion` | `0x1080` | 84 | UnwindData |  |
| 3 | `ctlClose` | `0x10E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ctlEngineGetActivity` | `0x10F0` | 86 | UnwindData |  |
| 5 | `ctlEngineGetProperties` | `0x1150` | 86 | UnwindData |  |
| 6 | `ctlEnumEngineGroups` | `0x11B0` | 128 | UnwindData |  |
| 7 | `ctlEnumFans` | `0x1230` | 128 | UnwindData |  |
| 8 | `ctlEnumFrequencyDomains` | `0x12B0` | 128 | UnwindData |  |
| 9 | `ctlEnumMemoryModules` | `0x1330` | 128 | UnwindData |  |
| 10 | `ctlEnumPowerDomains` | `0x13B0` | 128 | UnwindData |  |
| 11 | `ctlEnumTemperatureSensors` | `0x1430` | 128 | UnwindData |  |
| 12 | `ctlEnumerateDevices` | `0x14B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `ctlEnumerateDisplayOutputs` | `0x14C0` | 128 | UnwindData |  |
| 14 | `ctlFanGetConfig` | `0x1540` | 86 | UnwindData |  |
| 15 | `ctlFanGetProperties` | `0x15A0` | 86 | UnwindData |  |
| 16 | `ctlFanGetState` | `0x1600` | 105 | UnwindData |  |
| 17 | `ctlFanSetDefaultMode` | `0x1670` | 66 | UnwindData |  |
| 18 | `ctlFanSetFixedSpeedMode` | `0x16C0` | 86 | UnwindData |  |
| 19 | `ctlFanSetSpeedTableMode` | `0x1720` | 86 | UnwindData |  |
| 20 | `ctlFrequencyGetAvailableClocks` | `0x1780` | 107 | UnwindData |  |
| 21 | `ctlFrequencyGetProperties` | `0x17F0` | 86 | UnwindData |  |
| 22 | `ctlFrequencyGetRange` | `0x1850` | 86 | UnwindData |  |
| 23 | `ctlFrequencyGetState` | `0x18B0` | 86 | UnwindData |  |
| 24 | `ctlFrequencyGetThrottleTime` | `0x1910` | 86 | UnwindData |  |
| 25 | `ctlFrequencySetRange` | `0x1970` | 86 | UnwindData |  |
| 26 | `ctlGetAdaperDisplayEncoderProperties` | `0x19D0` | 86 | UnwindData |  |
| 27 | `ctlGetCurrentScaling` | `0x1A30` | 86 | UnwindData |  |
| 28 | `ctlGetCurrentSharpness` | `0x1A90` | 86 | UnwindData |  |
| 29 | `ctlGetDeviceProperties` | `0x1AF0` | 86 | UnwindData |  |
| 30 | `ctlGetDisplayProperties` | `0x1B50` | 86 | UnwindData |  |
| 31 | `ctlGetIntelArcSyncInfoForMonitor` | `0x1BB0` | 86 | UnwindData |  |
| 32 | `ctlGetIntelArcSyncProfile` | `0x1C10` | 86 | UnwindData |  |
| 33 | `ctlGetLACEConfig` | `0x1C70` | 86 | UnwindData |  |
| 34 | `ctlGetPowerOptimizationCaps` | `0x1CD0` | 86 | UnwindData |  |
| 35 | `ctlGetPowerOptimizationSetting` | `0x1D30` | 86 | UnwindData |  |
| 36 | `ctlGetSet3DFeature` | `0x1D90` | 86 | UnwindData |  |
| 37 | `ctlGetSetRetroScaling` | `0x1DF0` | 86 | UnwindData |  |
| 38 | `ctlGetSetVideoProcessingFeature` | `0x1E50` | 86 | UnwindData |  |
| 39 | `ctlGetSharpnessCaps` | `0x1EB0` | 86 | UnwindData |  |
| 40 | `ctlGetSupported3DCapabilities` | `0x1F10` | 86 | UnwindData |  |
| 41 | `ctlGetSupportedRetroScalingCapability` | `0x1F70` | 86 | UnwindData |  |
| 42 | `ctlGetSupportedScalingCapability` | `0x1FD0` | 86 | UnwindData |  |
| 43 | `ctlGetSupportedVideoProcessingCapabilities` | `0x2030` | 86 | UnwindData |  |
| 44 | `ctlGetZeDevice` | `0x2090` | 107 | UnwindData |  |
| 45 | `ctlI2CAccess` | `0x2100` | 86 | UnwindData |  |
| 46 | `ctlInit` | `0x2160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `ctlMemoryGetBandwidth` | `0x2170` | 86 | UnwindData |  |
| 48 | `ctlMemoryGetProperties` | `0x21D0` | 86 | UnwindData |  |
| 49 | `ctlMemoryGetState` | `0x2230` | 86 | UnwindData |  |
| 50 | `ctlOverclockGetProperties` | `0x2290` | 86 | UnwindData |  |
| 51 | `ctlOverclockGpuFrequencyOffsetGet` | `0x22F0` | 86 | UnwindData |  |
| 52 | `ctlOverclockGpuFrequencyOffsetSet` | `0x2350` | 87 | UnwindData |  |
| 53 | `ctlOverclockGpuLockGet` | `0x23B0` | 86 | UnwindData |  |
| 54 | `ctlOverclockGpuLockSet` | `0x2410` | 107 | UnwindData |  |
| 55 | `ctlOverclockGpuVoltageOffsetGet` | `0x2480` | 86 | UnwindData |  |
| 56 | `ctlOverclockGpuVoltageOffsetSet` | `0x24E0` | 87 | UnwindData |  |
| 57 | `ctlOverclockPowerLimitGet` | `0x2540` | 86 | UnwindData |  |
| 58 | `ctlOverclockPowerLimitSet` | `0x25A0` | 87 | UnwindData |  |
| 59 | `ctlOverclockTemperatureLimitGet` | `0x2600` | 86 | UnwindData |  |
| 60 | `ctlOverclockTemperatureLimitSet` | `0x2660` | 87 | UnwindData |  |
| 61 | `ctlOverclockVramFrequencyOffsetGet` | `0x26C0` | 86 | UnwindData |  |
| 62 | `ctlOverclockVramFrequencyOffsetSet` | `0x2720` | 87 | UnwindData |  |
| 63 | `ctlOverclockVramVoltageOffsetGet` | `0x2780` | 86 | UnwindData |  |
| 64 | `ctlOverclockVramVoltageOffsetSet` | `0x27E0` | 87 | UnwindData |  |
| 65 | `ctlOverclockWaiverSet` | `0x2840` | 66 | UnwindData |  |
| 66 | `ctlPanelDescriptorAccess` | `0x2890` | 86 | UnwindData |  |
| 67 | `ctlPciGetProperties` | `0x28F0` | 86 | UnwindData |  |
| 68 | `ctlPciGetState` | `0x2950` | 86 | UnwindData |  |
| 69 | `ctlPixelTransformationGetConfig` | `0x29B0` | 86 | UnwindData |  |
| 70 | `ctlPixelTransformationSetConfig` | `0x2A10` | 86 | UnwindData |  |
| 71 | `ctlPowerGetEnergyCounter` | `0x2A70` | 86 | UnwindData |  |
| 72 | `ctlPowerGetLimits` | `0x2AD0` | 86 | UnwindData |  |
| 73 | `ctlPowerGetProperties` | `0x2B30` | 86 | UnwindData |  |
| 74 | `ctlPowerSetLimits` | `0x2B90` | 86 | UnwindData |  |
| 75 | `ctlPowerTelemetryGet` | `0x2BF0` | 86 | UnwindData |  |
| 76 | `ctlReservedCall` | `0x2C50` | 86 | UnwindData |  |
| 77 | `ctlSetCurrentScaling` | `0x2CB0` | 86 | UnwindData |  |
| 78 | `ctlSetCurrentSharpness` | `0x2D10` | 86 | UnwindData |  |
| 79 | `ctlSetIntelArcSyncProfile` | `0x2D70` | 86 | UnwindData |  |
| 80 | `ctlSetLACEConfig` | `0x2DD0` | 86 | UnwindData |  |
| 81 | `ctlSetPowerOptimizationSetting` | `0x2E30` | 86 | UnwindData |  |
| 82 | `ctlSetRuntimePath` | `0x2E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `ctlSoftwarePSR` | `0x2EA0` | 86 | UnwindData |  |
| 84 | `ctlTemperatureGetProperties` | `0x2F00` | 86 | UnwindData |  |
| 85 | `ctlTemperatureGetState` | `0x2F60` | 86 | UnwindData |  |
| 86 | `ctlWaitForPropertyChange` | `0x2FC0` | 86 | UnwindData |  |
