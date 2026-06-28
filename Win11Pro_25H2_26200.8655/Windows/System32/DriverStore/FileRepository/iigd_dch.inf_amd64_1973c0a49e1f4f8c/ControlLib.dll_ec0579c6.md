# Binary Specification: ControlLib.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\ControlLib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ec0579c62f84f62ea7d6a80b8b4b077eba24ba80be574f814cdceaa46c53d9bd`
* **Total Exported Functions:** 62

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ctlAUXAccess` | `0x1150` | 140 | UnwindData |  |
| 2 | `ctlCheckDriverVersion` | `0x11E0` | 65 | UnwindData |  |
| 3 | `ctlClose` | `0x1230` | 70 | UnwindData |  |
| 4 | `ctlEngineGetActivity` | `0x1280` | 138 | UnwindData |  |
| 5 | `ctlEngineGetProperties` | `0x1310` | 138 | UnwindData |  |
| 6 | `ctlEnumEngineGroups` | `0x13A0` | 87 | UnwindData |  |
| 7 | `ctlEnumFans` | `0x1400` | 87 | UnwindData |  |
| 8 | `ctlEnumFrequencyDomains` | `0x1460` | 87 | UnwindData |  |
| 9 | `ctlEnumMemoryModules` | `0x14C0` | 87 | UnwindData |  |
| 10 | `ctlEnumPowerDomains` | `0x1520` | 87 | UnwindData |  |
| 11 | `ctlEnumTemperatureSensors` | `0x1580` | 87 | UnwindData |  |
| 12 | `ctlEnumerateDevices` | `0x15E0` | 97 | UnwindData |  |
| 13 | `ctlEnumerateDisplayOutputs` | `0x1650` | 87 | UnwindData |  |
| 14 | `ctlFanGetConfig` | `0x16B0` | 140 | UnwindData |  |
| 15 | `ctlFanGetProperties` | `0x1740` | 138 | UnwindData |  |
| 16 | `ctlFanGetState` | `0x17D0` | 111 | UnwindData |  |
| 17 | `ctlFanSetDefaultMode` | `0x1840` | 46 | UnwindData |  |
| 18 | `ctlFanSetFixedSpeedMode` | `0x1870` | 138 | UnwindData |  |
| 19 | `ctlFanSetSpeedTableMode` | `0x1900` | 140 | UnwindData |  |
| 20 | `ctlFrequencyGetAvailableClocks` | `0x1990` | 87 | UnwindData |  |
| 21 | `ctlFrequencyGetProperties` | `0x19F0` | 138 | UnwindData |  |
| 22 | `ctlFrequencyGetRange` | `0x1A80` | 138 | UnwindData |  |
| 23 | `ctlFrequencyGetState` | `0x1B10` | 138 | UnwindData |  |
| 24 | `ctlFrequencyGetThrottleTime` | `0x1BA0` | 138 | UnwindData |  |
| 25 | `ctlFrequencySetRange` | `0x1C30` | 138 | UnwindData |  |
| 26 | `ctlGetAdaperDisplayEncoderProperties` | `0x1CC0` | 138 | UnwindData |  |
| 27 | `ctlGetCurrentScaling` | `0x1D50` | 138 | UnwindData |  |
| 28 | `ctlGetCurrentSharpness` | `0x1DE0` | 138 | UnwindData |  |
| 29 | `ctlGetDeviceProperties` | `0x1E70` | 140 | UnwindData |  |
| 30 | `ctlGetDisplayProperties` | `0x1F00` | 140 | UnwindData |  |
| 31 | `ctlGetPowerOptimizationCaps` | `0x1F90` | 138 | UnwindData |  |
| 32 | `ctlGetPowerOptimizationSetting` | `0x2020` | 138 | UnwindData |  |
| 33 | `ctlGetSet3DFeature` | `0x20B0` | 138 | UnwindData |  |
| 34 | `ctlGetSetRetroScaling` | `0x2140` | 138 | UnwindData |  |
| 35 | `ctlGetSetVideoProcessingFeature` | `0x21D0` | 138 | UnwindData |  |
| 36 | `ctlGetSharpnessCaps` | `0x2260` | 138 | UnwindData |  |
| 37 | `ctlGetSupported3DCapabilities` | `0x22F0` | 138 | UnwindData |  |
| 38 | `ctlGetSupportedRetroScalingCapability` | `0x2380` | 138 | UnwindData |  |
| 39 | `ctlGetSupportedScalingCapability` | `0x2410` | 138 | UnwindData |  |
| 40 | `ctlGetSupportedVideoProcessingCapabilities` | `0x24A0` | 138 | UnwindData |  |
| 41 | `ctlGetZeDevice` | `0x2530` | 87 | UnwindData |  |
| 42 | `ctlI2CAccess` | `0x2590` | 140 | UnwindData |  |
| 43 | `ctlInit` | `0x2620` | 270 | UnwindData |  |
| 44 | `ctlMemoryGetBandwidth` | `0x2730` | 138 | UnwindData |  |
| 45 | `ctlMemoryGetProperties` | `0x27C0` | 138 | UnwindData |  |
| 46 | `ctlMemoryGetState` | `0x2850` | 138 | UnwindData |  |
| 47 | `ctlPanelDescriptorAccess` | `0x28E0` | 138 | UnwindData |  |
| 48 | `ctlPciGetProperties` | `0x2970` | 138 | UnwindData |  |
| 49 | `ctlPciGetState` | `0x2A00` | 138 | UnwindData |  |
| 50 | `ctlPixelTransformationGetConfig` | `0x2A90` | 140 | UnwindData |  |
| 51 | `ctlPixelTransformationSetConfig` | `0x2B20` | 138 | UnwindData |  |
| 52 | `ctlPowerGetEnergyCounter` | `0x2BB0` | 138 | UnwindData |  |
| 53 | `ctlPowerGetLimits` | `0x2C40` | 138 | UnwindData |  |
| 54 | `ctlPowerGetProperties` | `0x2CD0` | 138 | UnwindData |  |
| 55 | `ctlPowerSetLimits` | `0x2D60` | 138 | UnwindData |  |
| 56 | `ctlReservedCall` | `0x2DF0` | 122 | UnwindData |  |
| 57 | `ctlSetCurrentScaling` | `0x2E70` | 138 | UnwindData |  |
| 58 | `ctlSetCurrentSharpness` | `0x2F00` | 138 | UnwindData |  |
| 59 | `ctlSetPowerOptimizationSetting` | `0x2F90` | 138 | UnwindData |  |
| 60 | `ctlTemperatureGetProperties` | `0x3020` | 138 | UnwindData |  |
| 61 | `ctlTemperatureGetState` | `0x30B0` | 91 | UnwindData |  |
| 62 | `ctlWaitForPropertyChange` | `0x3110` | 151 | UnwindData |  |
