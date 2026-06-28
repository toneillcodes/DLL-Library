# Binary Specification: ControlLib.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\lenovofnandfunctionkeys.inf_amd64_5e21bf389d23855a\ControlLib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b4b92aee9a1efe675e264deb688b04d8ee19f61d836e12636335c67600376408`
* **Total Exported Functions:** 121

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ctlAUXAccess` | `0x1A80` | 344 | UnwindData |  |
| 2 | `ctlCheckDriverVersion` | `0x1BE0` | 342 | UnwindData |  |
| 3 | `ctlClose` | `0x1D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `ctlEdidManagement` | `0x1D50` | 344 | UnwindData |  |
| 5 | `ctlEngineGetActivity` | `0x1EB0` | 344 | UnwindData |  |
| 6 | `ctlEngineGetProperties` | `0x2010` | 344 | UnwindData |  |
| 7 | `ctlEnumEngineGroups` | `0x2170` | 377 | UnwindData |  |
| 8 | `ctlEnumFans` | `0x22F0` | 377 | UnwindData |  |
| 9 | `ctlEnumFrequencyDomains` | `0x2470` | 377 | UnwindData |  |
| 10 | `ctlEnumLeds` | `0x25F0` | 377 | UnwindData |  |
| 11 | `ctlEnumMemoryModules` | `0x2770` | 377 | UnwindData |  |
| 12 | `ctlEnumPowerDomains` | `0x28F0` | 377 | UnwindData |  |
| 13 | `ctlEnumTemperatureSensors` | `0x2A70` | 377 | UnwindData |  |
| 14 | `ctlEnumerateDevices` | `0x2BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ctlEnumerateDisplayOutputs` | `0x2C00` | 377 | UnwindData |  |
| 16 | `ctlEnumerateI2CPinPairs` | `0x2D80` | 377 | UnwindData |  |
| 17 | `ctlEnumerateMuxDevices` | `0x2F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ctlFanGetConfig` | `0x2F10` | 344 | UnwindData |  |
| 19 | `ctlFanGetProperties` | `0x3070` | 344 | UnwindData |  |
| 20 | `ctlFanGetState` | `0x31D0` | 340 | UnwindData |  |
| 21 | `ctlFanSetDefaultMode` | `0x3330` | 326 | UnwindData |  |
| 22 | `ctlFanSetFixedSpeedMode` | `0x3480` | 344 | UnwindData |  |
| 23 | `ctlFanSetSpeedTableMode` | `0x35E0` | 344 | UnwindData |  |
| 24 | `ctlFrequencyGetAvailableClocks` | `0x3740` | 342 | UnwindData |  |
| 25 | `ctlFrequencyGetProperties` | `0x38A0` | 344 | UnwindData |  |
| 26 | `ctlFrequencyGetRange` | `0x3A00` | 344 | UnwindData |  |
| 27 | `ctlFrequencyGetState` | `0x3B60` | 344 | UnwindData |  |
| 28 | `ctlFrequencyGetThrottleTime` | `0x3CC0` | 344 | UnwindData |  |
| 29 | `ctlFrequencySetRange` | `0x3E20` | 344 | UnwindData |  |
| 30 | `ctlGetAdaperDisplayEncoderProperties` | `0x3F80` | 344 | UnwindData |  |
| 31 | `ctlGetBrightnessSetting` | `0x40E0` | 344 | UnwindData |  |
| 32 | `ctlGetCurrentScaling` | `0x4240` | 344 | UnwindData |  |
| 33 | `ctlGetCurrentSharpness` | `0x43A0` | 344 | UnwindData |  |
| 34 | `ctlGetDeviceProperties` | `0x4500` | 344 | UnwindData |  |
| 35 | `ctlGetDisplayProperties` | `0x4660` | 344 | UnwindData |  |
| 36 | `ctlGetIntelArcSyncInfoForMonitor` | `0x47C0` | 344 | UnwindData |  |
| 37 | `ctlGetIntelArcSyncProfile` | `0x4920` | 344 | UnwindData |  |
| 38 | `ctlGetLACEConfig` | `0x4A80` | 344 | UnwindData |  |
| 39 | `ctlGetLinkedDisplayAdapters` | `0x4BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `ctlGetMuxProperties` | `0x4BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `ctlGetPowerOptimizationCaps` | `0x4C00` | 344 | UnwindData |  |
| 42 | `ctlGetPowerOptimizationSetting` | `0x4D60` | 344 | UnwindData |  |
| 43 | `ctlGetSet3DFeature` | `0x4EC0` | 344 | UnwindData |  |
| 44 | `ctlGetSetCombinedDisplay` | `0x5020` | 344 | UnwindData |  |
| 45 | `ctlGetSetCustomMode` | `0x5180` | 344 | UnwindData |  |
| 46 | `ctlGetSetDisplayGenlock` | `0x52E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `ctlGetSetDisplaySettings` | `0x52F0` | 344 | UnwindData |  |
| 48 | `ctlGetSetDynamicContrastEnhancement` | `0x5450` | 344 | UnwindData |  |
| 49 | `ctlGetSetRetroScaling` | `0x55B0` | 344 | UnwindData |  |
| 50 | `ctlGetSetVideoProcessingFeature` | `0x5710` | 344 | UnwindData |  |
| 51 | `ctlGetSetWireFormat` | `0x5870` | 344 | UnwindData |  |
| 52 | `ctlGetSharpnessCaps` | `0x59D0` | 344 | UnwindData |  |
| 53 | `ctlGetSupported3DCapabilities` | `0x5B30` | 344 | UnwindData |  |
| 54 | `ctlGetSupportedRetroScalingCapability` | `0x5C90` | 344 | UnwindData |  |
| 55 | `ctlGetSupportedScalingCapability` | `0x5DF0` | 344 | UnwindData |  |
| 56 | `ctlGetSupportedVideoProcessingCapabilities` | `0x5F50` | 344 | UnwindData |  |
| 57 | `ctlGetVblankTimestamp` | `0x60B0` | 344 | UnwindData |  |
| 58 | `ctlGetZeDevice` | `0x6210` | 342 | UnwindData |  |
| 59 | `ctlI2CAccess` | `0x6370` | 344 | UnwindData |  |
| 60 | `ctlI2CAccessOnPinPair` | `0x64D0` | 344 | UnwindData |  |
| 61 | `ctlInit` | `0x6630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `ctlLedGetProperties` | `0x6640` | 344 | UnwindData |  |
| 63 | `ctlLedGetState` | `0x67A0` | 344 | UnwindData |  |
| 64 | `ctlLedSetState` | `0x6900` | 342 | UnwindData |  |
| 65 | `ctlLinkDisplayAdapters` | `0x6A60` | 344 | UnwindData |  |
| 66 | `ctlMemoryGetBandwidth` | `0x6BC0` | 344 | UnwindData |  |
| 67 | `ctlMemoryGetProperties` | `0x6D20` | 344 | UnwindData |  |
| 68 | `ctlMemoryGetState` | `0x6E80` | 344 | UnwindData |  |
| 69 | `ctlOverclockGetProperties` | `0x6FE0` | 344 | UnwindData |  |
| 70 | `ctlOverclockGpuFrequencyOffsetGet` | `0x7140` | 344 | UnwindData |  |
| 72 | `ctlOverclockGpuFrequencyOffsetSet` | `0x72A0` | 348 | UnwindData |  |
| 74 | `ctlOverclockGpuLockGet` | `0x7400` | 344 | UnwindData |  |
| 75 | `ctlOverclockGpuLockSet` | `0x7560` | 374 | UnwindData |  |
| 78 | `ctlOverclockGpuVoltageOffsetGet` | `0x76E0` | 344 | UnwindData |  |
| 79 | `ctlOverclockGpuVoltageOffsetSet` | `0x7840` | 348 | UnwindData |  |
| 80 | `ctlOverclockPowerLimitGet` | `0x79A0` | 344 | UnwindData |  |
| 82 | `ctlOverclockPowerLimitSet` | `0x7B00` | 348 | UnwindData |  |
| 85 | `ctlOverclockResetToDefault` | `0x7C60` | 326 | UnwindData |  |
| 86 | `ctlOverclockTemperatureLimitGet` | `0x7DB0` | 344 | UnwindData |  |
| 88 | `ctlOverclockTemperatureLimitSet` | `0x7F10` | 348 | UnwindData |  |
| 90 | `ctlOverclockVramFrequencyOffsetGet` | `0x8070` | 344 | UnwindData |  |
| 91 | `ctlOverclockVramFrequencyOffsetSet` | `0x81D0` | 348 | UnwindData |  |
| 94 | `ctlOverclockVramVoltageOffsetGet` | `0x8330` | 344 | UnwindData |  |
| 95 | `ctlOverclockVramVoltageOffsetSet` | `0x8490` | 348 | UnwindData |  |
| 96 | `ctlOverclockWaiverSet` | `0x85F0` | 326 | UnwindData |  |
| 98 | `ctlPanelDescriptorAccess` | `0x8740` | 344 | UnwindData |  |
| 99 | `ctlPciGetProperties` | `0x88A0` | 344 | UnwindData |  |
| 100 | `ctlPciGetState` | `0x8A00` | 344 | UnwindData |  |
| 101 | `ctlPixelTransformationGetConfig` | `0x8B60` | 344 | UnwindData |  |
| 102 | `ctlPixelTransformationSetConfig` | `0x8CC0` | 344 | UnwindData |  |
| 103 | `ctlPowerGetEnergyCounter` | `0x8E20` | 344 | UnwindData |  |
| 104 | `ctlPowerGetLimits` | `0x8F80` | 344 | UnwindData |  |
| 105 | `ctlPowerGetProperties` | `0x90E0` | 344 | UnwindData |  |
| 106 | `ctlPowerSetLimits` | `0x9240` | 344 | UnwindData |  |
| 107 | `ctlPowerTelemetryGet` | `0x93A0` | 344 | UnwindData |  |
| 108 | `ctlReservedCall` | `0x9500` | 344 | UnwindData |  |
| 109 | `ctlSetBrightnessSetting` | `0x9660` | 344 | UnwindData |  |
| 110 | `ctlSetCurrentScaling` | `0x97C0` | 344 | UnwindData |  |
| 111 | `ctlSetCurrentSharpness` | `0x9920` | 344 | UnwindData |  |
| 112 | `ctlSetIntelArcSyncProfile` | `0x9A80` | 344 | UnwindData |  |
| 113 | `ctlSetLACEConfig` | `0x9BE0` | 344 | UnwindData |  |
| 114 | `ctlSetPowerOptimizationSetting` | `0x9D40` | 344 | UnwindData |  |
| 115 | `ctlSetRuntimePath` | `0x9EA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `ctlSoftwarePSR` | `0x9EB0` | 344 | UnwindData |  |
| 117 | `ctlSwitchMux` | `0xA010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `ctlTemperatureGetProperties` | `0xA020` | 344 | UnwindData |  |
| 119 | `ctlTemperatureGetState` | `0xA180` | 344 | UnwindData |  |
| 120 | `ctlUnlinkDisplayAdapters` | `0xA2E0` | 326 | UnwindData |  |
| 121 | `ctlWaitForPropertyChange` | `0xA430` | 344 | UnwindData |  |
| 71 | `ctlOverclockGpuFrequencyOffsetGetV2` | `0xA590` | 344 | UnwindData |  |
| 73 | `ctlOverclockGpuFrequencyOffsetSetV2` | `0xA6F0` | 348 | UnwindData |  |
| 76 | `ctlOverclockGpuMaxVoltageOffsetGetV2` | `0xA850` | 344 | UnwindData |  |
| 77 | `ctlOverclockGpuMaxVoltageOffsetSetV2` | `0xA9B0` | 348 | UnwindData |  |
| 81 | `ctlOverclockPowerLimitGetV2` | `0xAB10` | 344 | UnwindData |  |
| 83 | `ctlOverclockPowerLimitSetV2` | `0xAC70` | 348 | UnwindData |  |
| 84 | `ctlOverclockReadVFCurve` | `0xADD0` | 365 | UnwindData |  |
| 87 | `ctlOverclockTemperatureLimitGetV2` | `0xAF40` | 344 | UnwindData |  |
| 89 | `ctlOverclockTemperatureLimitSetV2` | `0xB0A0` | 348 | UnwindData |  |
| 92 | `ctlOverclockVramMemSpeedLimitGetV2` | `0xB200` | 344 | UnwindData |  |
| 93 | `ctlOverclockVramMemSpeedLimitSetV2` | `0xB360` | 348 | UnwindData |  |
| 97 | `ctlOverclockWriteCustomVFCurve` | `0xB4C0` | 340 | UnwindData |  |
