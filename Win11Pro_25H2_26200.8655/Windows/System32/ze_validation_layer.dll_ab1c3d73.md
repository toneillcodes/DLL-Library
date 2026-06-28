# Binary Specification: ze_validation_layer.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ze_validation_layer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ab1c3d73193762fe6a3d1a24f8a8d6b6afff45543448f6680cca0eb70542cf38`
* **Total Exported Functions:** 51

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 21 | `zelLoaderGetVersion` | `0x10F0` | 82 | UnwindData |  |
| 1 | `zeGetCommandListProcAddrTable` | `0x3F50` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `zeGetCommandQueueProcAddrTable` | `0x4240` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `zeGetContextProcAddrTable` | `0x42D0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `zeGetDeviceProcAddrTable` | `0x43D0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `zeGetDriverProcAddrTable` | `0x45A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `zeGetEventExpProcAddrTable` | `0x4660` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `zeGetEventPoolProcAddrTable` | `0x46B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `zeGetEventProcAddrTable` | `0x4750` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `zeGetFenceProcAddrTable` | `0x4820` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `zeGetGlobalProcAddrTable` | `0x48C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `zeGetImageExpProcAddrTable` | `0x4910` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `zeGetImageProcAddrTable` | `0x4970` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `zeGetKernelExpProcAddrTable` | `0x4A00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `zeGetKernelProcAddrTable` | `0x4A60` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `zeGetMemProcAddrTable` | `0x4BA0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `zeGetModuleBuildLogProcAddrTable` | `0x4CC0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `zeGetModuleProcAddrTable` | `0x4D20` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `zeGetPhysicalMemProcAddrTable` | `0x4E20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `zeGetSamplerProcAddrTable` | `0x4E80` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `zeGetVirtualMemProcAddrTable` | `0x4EE0` | 3,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `zetGetCommandListProcAddrTable` | `0x5BA0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `zetGetContextProcAddrTable` | `0x5C30` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `zetGetDebugProcAddrTable` | `0x5C80` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `zetGetDeviceProcAddrTable` | `0x5DB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `zetGetKernelProcAddrTable` | `0x5E00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `zetGetMetricGroupExpProcAddrTable` | `0x5E50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `zetGetMetricGroupProcAddrTable` | `0x5EA0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `zetGetMetricProcAddrTable` | `0x5F10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `zetGetMetricQueryPoolProcAddrTable` | `0x5F70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `zetGetMetricQueryProcAddrTable` | `0x5FD0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `zetGetMetricStreamerProcAddrTable` | `0x6060` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `zetGetModuleProcAddrTable` | `0x60D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `zetGetTracerExpProcAddrTable` | `0x6120` | 6,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `zesGetDeviceProcAddrTable` | `0x7AD0` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `zesGetDiagnosticsProcAddrTable` | `0x7D70` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `zesGetDriverProcAddrTable` | `0x7DE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `zesGetEngineProcAddrTable` | `0x7E40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `zesGetFabricPortProcAddrTable` | `0x7EA0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `zesGetFanProcAddrTable` | `0x7F60` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `zesGetFirmwareProcAddrTable` | `0x8020` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `zesGetFrequencyProcAddrTable` | `0x8080` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `zesGetLedProcAddrTable` | `0x8240` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `zesGetMemoryProcAddrTable` | `0x82D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `zesGetPerformanceFactorProcAddrTable` | `0x8340` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `zesGetPowerProcAddrTable` | `0x83B0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `zesGetPsuProcAddrTable` | `0x8470` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `zesGetRasProcAddrTable` | `0x84D0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `zesGetSchedulerProcAddrTable` | `0x8560` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `zesGetStandbyProcAddrTable` | `0x8650` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `zesGetTemperatureProcAddrTable` | `0x86C0` | 41,923 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
