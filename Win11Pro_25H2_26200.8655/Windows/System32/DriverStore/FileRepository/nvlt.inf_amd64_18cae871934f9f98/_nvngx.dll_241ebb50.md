# Binary Specification: _nvngx.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\_nvngx.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `241ebb5011fb9e2ff529835b6f93a47ee31298b80f28fe1aa5eacfc66ac5ea08`
* **Total Exported Functions:** 67

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `NVSDK_NGX_CUDA_Init_Ext` | `0x3210` | 565 | UnwindData |  |
| 8 | `NVSDK_NGX_CUDA_Init` | `0x3450` | 549 | UnwindData |  |
| 10 | `NVSDK_NGX_CUDA_Init_ProjectID` | `0x3680` | 598 | UnwindData |  |
| 1 | `NVSDK_NGX_CUDA_AllocateParameters` | `0x38E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `NVSDK_NGX_CUDA_DestroyParameters` | `0x38F0` | 104 | UnwindData |  |
| 5 | `NVSDK_NGX_CUDA_GetCapabilityParameters` | `0x3960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `NVSDK_NGX_CUDA_Shutdown` | `0x3970` | 56 | UnwindData |  |
| 6 | `NVSDK_NGX_CUDA_GetParameters` | `0x39B0` | 92 | UnwindData |  |
| 7 | `NVSDK_NGX_CUDA_GetScratchBufferSize` | `0x3A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `NVSDK_NGX_CUDA_CreateFeature` | `0x3A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `NVSDK_NGX_CUDA_ReleaseFeature` | `0x3A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `NVSDK_NGX_CUDA_EvaluateFeature` | `0x3A50` | 21,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `NVSDK_NGX_VULKAN_RequiredExtensions` | `0x8E60` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `NVSDK_NGX_VULKAN_AllocateParameters` | `0x9400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `NVSDK_NGX_VULKAN_DestroyParameters` | `0x9410` | 104 | UnwindData |  |
| 53 | `NVSDK_NGX_VULKAN_GetCapabilityParameters` | `0x9480` | 3,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `NVSDK_NGX_VULKAN_Init` | `0xA0B0` | 342 | UnwindData |  |
| 60 | `NVSDK_NGX_VULKAN_Init_Ext` | `0xA210` | 360 | UnwindData |  |
| 61 | `NVSDK_NGX_VULKAN_Init_Ext2` | `0xA380` | 405 | UnwindData |  |
| 62 | `NVSDK_NGX_VULKAN_Init_ProjectID` | `0xA520` | 456 | UnwindData |  |
| 63 | `NVSDK_NGX_VULKAN_Init_ProjectID_Ext` | `0xA6F0` | 495 | UnwindData |  |
| 66 | `NVSDK_NGX_VULKAN_Shutdown` | `0xA8E0` | 56 | UnwindData |  |
| 67 | `NVSDK_NGX_VULKAN_Shutdown1` | `0xA920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `NVSDK_NGX_VULKAN_GetParameters` | `0xA950` | 92 | UnwindData |  |
| 58 | `NVSDK_NGX_VULKAN_GetScratchBufferSize` | `0xA9B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `NVSDK_NGX_VULKAN_CreateFeature` | `0xA9D0` | 19 | UnwindData |  |
| 50 | `NVSDK_NGX_VULKAN_CreateFeature1` | `0xA9F0` | 41 | UnwindData |  |
| 64 | `NVSDK_NGX_VULKAN_ReleaseFeature` | `0xAA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `NVSDK_NGX_VULKAN_EvaluateFeature` | `0xAA30` | 19 | UnwindData |  |
| 56 | `NVSDK_NGX_VULKAN_GetFeatureRequirements` | `0xAA50` | 67 | UnwindData |  |
| 55 | `NVSDK_NGX_VULKAN_GetFeatureInstanceExtensionRequirements` | `0xADD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `NVSDK_NGX_VULKAN_GetFeatureDeviceExtensionRequirements` | `0xADE0` | 72 | UnwindData |  |
| 44 | `NVSDK_NGX_OTA_UPDATES_Register` | `0x121D0` | 1,626 | UnwindData |  |
| 45 | `NVSDK_NGX_OTA_UPDATES_Unregister` | `0x12850` | 626 | UnwindData |  |
| 41 | `NVSDK_NGX_OTA_UPDATES_CheckForUpdate` | `0x133F0` | 247 | UnwindData |  |
| 43 | `NVSDK_NGX_OTA_UPDATES_Install` | `0x14880` | 1,127 | UnwindData |  |
| 46 | `NVSDK_NGX_OTA_UPDATES_Update` | `0x14CF0` | 1,185 | UnwindData |  |
| 42 | `NVSDK_NGX_OTA_UPDATES_GetPath` | `0x151A0` | 695 | UnwindData |  |
| 47 | `NVSDK_NGX_UpdateFeature` | `0x36040` | 522 | UnwindData |  |
| 22 | `NVSDK_NGX_D3D11_Init_Ext` | `0x52CF0` | 314 | UnwindData |  |
| 21 | `NVSDK_NGX_D3D11_Init` | `0x52E30` | 306 | UnwindData |  |
| 23 | `NVSDK_NGX_D3D11_Init_ProjectID` | `0x52F70` | 369 | UnwindData |  |
| 13 | `NVSDK_NGX_D3D11_AllocateParameters` | `0x530F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `NVSDK_NGX_D3D11_DestroyParameters` | `0x53100` | 104 | UnwindData |  |
| 17 | `NVSDK_NGX_D3D11_GetCapabilityParameters` | `0x53170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `NVSDK_NGX_D3D11_Shutdown` | `0x53180` | 56 | UnwindData |  |
| 26 | `NVSDK_NGX_D3D11_Shutdown1` | `0x531C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `NVSDK_NGX_D3D11_GetParameters` | `0x531F0` | 92 | UnwindData |  |
| 20 | `NVSDK_NGX_D3D11_GetScratchBufferSize` | `0x53250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `NVSDK_NGX_D3D11_CreateFeature` | `0x53270` | 19 | UnwindData |  |
| 24 | `NVSDK_NGX_D3D11_ReleaseFeature` | `0x53290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `NVSDK_NGX_D3D11_EvaluateFeature` | `0x532A0` | 19 | UnwindData |  |
| 18 | `NVSDK_NGX_D3D11_GetFeatureRequirements` | `0x532C0` | 116 | UnwindData |  |
| 36 | `NVSDK_NGX_D3D12_Init_Ext` | `0x54740` | 314 | UnwindData |  |
| 35 | `NVSDK_NGX_D3D12_Init` | `0x54880` | 306 | UnwindData |  |
| 37 | `NVSDK_NGX_D3D12_Init_ProjectID` | `0x549C0` | 369 | UnwindData |  |
| 27 | `NVSDK_NGX_D3D12_AllocateParameters` | `0x54B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `NVSDK_NGX_D3D12_DestroyParameters` | `0x54B50` | 104 | UnwindData |  |
| 31 | `NVSDK_NGX_D3D12_GetCapabilityParameters` | `0x54BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `NVSDK_NGX_D3D12_Shutdown` | `0x54BD0` | 56 | UnwindData |  |
| 40 | `NVSDK_NGX_D3D12_Shutdown1` | `0x54C10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `NVSDK_NGX_D3D12_GetParameters` | `0x54C40` | 92 | UnwindData |  |
| 34 | `NVSDK_NGX_D3D12_GetScratchBufferSize` | `0x54CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `NVSDK_NGX_D3D12_CreateFeature` | `0x54CC0` | 19 | UnwindData |  |
| 38 | `NVSDK_NGX_D3D12_ReleaseFeature` | `0x54CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `NVSDK_NGX_D3D12_EvaluateFeature` | `0x54CF0` | 19 | UnwindData |  |
| 32 | `NVSDK_NGX_D3D12_GetFeatureRequirements` | `0x54D10` | 116 | UnwindData |  |
