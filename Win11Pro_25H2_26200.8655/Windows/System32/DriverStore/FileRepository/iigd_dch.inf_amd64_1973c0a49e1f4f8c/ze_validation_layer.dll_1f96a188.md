# Binary Specification: ze_validation_layer.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\ze_validation_layer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1f96a188be0bd44447ebf93bd88ccd01da5b160631ae69b0770b69e7764ea395`
* **Total Exported Functions:** 51

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 21 | `zelLoaderGetVersion` | `0x10F0` | 73 | UnwindData |  |
| 1 | `zeGetCommandListProcAddrTable` | `0x3CB0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `zeGetCommandQueueProcAddrTable` | `0x3F60` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `zeGetContextProcAddrTable` | `0x3FF0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `zeGetDeviceProcAddrTable` | `0x40F0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `zeGetDriverProcAddrTable` | `0x42B0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `zeGetEventExpProcAddrTable` | `0x4370` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `zeGetEventPoolProcAddrTable` | `0x43C0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `zeGetEventProcAddrTable` | `0x4460` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `zeGetFenceProcAddrTable` | `0x4530` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `zeGetGlobalProcAddrTable` | `0x45D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `zeGetImageExpProcAddrTable` | `0x4620` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `zeGetImageProcAddrTable` | `0x4680` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `zeGetKernelExpProcAddrTable` | `0x46F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `zeGetKernelProcAddrTable` | `0x4750` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `zeGetMemProcAddrTable` | `0x4890` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `zeGetModuleBuildLogProcAddrTable` | `0x4990` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `zeGetModuleProcAddrTable` | `0x49F0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `zeGetPhysicalMemProcAddrTable` | `0x4AE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `zeGetSamplerProcAddrTable` | `0x4B40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `zeGetVirtualMemProcAddrTable` | `0x4BA0` | 3,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `zetGetCommandListProcAddrTable` | `0x5860` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `zetGetContextProcAddrTable` | `0x58F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `zetGetDebugProcAddrTable` | `0x5940` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `zetGetDeviceProcAddrTable` | `0x5A70` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `zetGetKernelProcAddrTable` | `0x5AC0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `zetGetMetricGroupExpProcAddrTable` | `0x5B10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `zetGetMetricGroupProcAddrTable` | `0x5B60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `zetGetMetricProcAddrTable` | `0x5BD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `zetGetMetricQueryPoolProcAddrTable` | `0x5C30` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `zetGetMetricQueryProcAddrTable` | `0x5C90` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `zetGetMetricStreamerProcAddrTable` | `0x5D20` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `zetGetModuleProcAddrTable` | `0x5D90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `zetGetTracerExpProcAddrTable` | `0x5DE0` | 6,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `zesGetDeviceProcAddrTable` | `0x7750` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `zesGetDiagnosticsProcAddrTable` | `0x79D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `zesGetDriverProcAddrTable` | `0x7A40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `zesGetEngineProcAddrTable` | `0x7AA0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `zesGetFabricPortProcAddrTable` | `0x7B00` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `zesGetFanProcAddrTable` | `0x7BC0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `zesGetFirmwareProcAddrTable` | `0x7C80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `zesGetFrequencyProcAddrTable` | `0x7CE0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `zesGetLedProcAddrTable` | `0x7EA0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `zesGetMemoryProcAddrTable` | `0x7F30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `zesGetPerformanceFactorProcAddrTable` | `0x7FA0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `zesGetPowerProcAddrTable` | `0x8010` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `zesGetPsuProcAddrTable` | `0x80D0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `zesGetRasProcAddrTable` | `0x8130` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `zesGetSchedulerProcAddrTable` | `0x81C0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `zesGetStandbyProcAddrTable` | `0x82B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `zesGetTemperatureProcAddrTable` | `0x8320` | 42,355 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
