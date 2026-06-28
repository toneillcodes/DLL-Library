# Binary Specification: igdext32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\igdext32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `604ea6bba734114bb0bc17eadd016bfea784e6f85fd771878cfe4cb722c9f531`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `D3D11GetSupportedVersions` | `0x16E0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `D3D11CreateDeviceExtensionContext1` | `0x1900` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `D3D11CreateDeviceExtensionContext` | `0x1A10` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `D3D11DestroyDeviceExtensionContext` | `0x1B20` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `D3D12GetSupportedVersions` | `0x1BB0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `D3D12CreateDeviceExtensionContext` | `0x1DD0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `D3D12DestroyDeviceExtensionContext` | `0x1EE0` | 55,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `D3D11GetSupportedVersions2` | `0xF700` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `D3D11CreateDeviceExtensionContext2` | `0xF940` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `D3D12GetSupportedVersions2` | `0xFAC0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `D3D12CreateDeviceExtensionContext2` | `0xFD00` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `D3D11D3D12CreateDeviceExtensionContext2` | `0xFE90` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `D3D11D3D12DestroyDeviceExtensionContext2` | `0x100F0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `D3D11EnumInternalExtensions` | `0x101D0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `D3D11CreateDeviceExtensionContextInternal` | `0x10270` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `D3D12EnumInternalExtensions` | `0x103E0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `D3D12CreateDeviceExtensionContextInternal` | `0x10480` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `D3D11D3D12CreateDeviceExtensionContextInternal` | `0x10600` | 1,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `_INTC_D3D11_CreateDeviceExtensionContext` | `0x10C60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `_INTC_D3D12_CreateDeviceExtensionContext` | `0x10CA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `_INTC_CreateDeviceExtensionContext` | `0x10CF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `_INTC_D3D11_BeginUAVOverlap` | `0x10D50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `_INTC_D3D11_EndUAVOverlap` | `0x10D80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `_INTC_D3D11_MultiDrawInstancedIndirect` | `0x10DB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `_INTC_D3D11_MultiDrawIndexedInstancedIndirect` | `0x10DE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `_INTC_D3D11_MultiDrawInstancedIndirectCountIndirect` | `0x10E10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `_INTC_D3D11_MultiDrawIndexedInstancedIndirectCountIndirect` | `0x10E50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `_INTC_D3D11_SetDepthBounds` | `0x10E90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `_INTC_D3D11_CreateTexture2D` | `0x10ED0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `_INTC_D3D12_CreateCommandQueue` | `0x10F10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `_INTC_D3D12_CreateComputePipelineState` | `0x10F50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `_INTC_D3D12_CreateReservedResource` | `0x10F90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `_INTC_D3D12_CreateCommittedResource` | `0x10FD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `_INTC_D3D12_CreatePlacedResource` | `0x11010` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `_INTC_D3D12_CreateHostRTASResource` | `0x11060` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `_INTC_D3D12_BuildRaytracingAccelerationStructure_Host` | `0x110A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `_INTC_D3D12_CopyRaytracingAccelerationStructure_Host` | `0x110D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `_INTC_D3D12_EmitRaytracingAccelerationStructurePostbuildInfo_Host` | `0x11100` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `_INTC_D3D12_GetRaytracingAccelerationStructurePrebuildInfo_Host` | `0x11130` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `_INTC_D3D12_TransferHostRTAS` | `0x11160` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `_INTC_D3D12_SetDriverEventMetadata` | `0x111A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `_INTC_D3D11_INT_CreateDeviceExtensionContext` | `0x111D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `_INTC_D3D12_INT_CreateDeviceExtensionContext` | `0x11210` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `_INTC_INT_CreateDeviceExtensionContext` | `0x11250` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `_INTC_D3D12_INT_CreateGraphicsPipelineState` | `0x112B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `_INTC_D3D12_INT_CreateGraphicsPipelineState1` | `0x112F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `_INTC_D3D12_INT_CreateGraphicsPipelineState2` | `0x11330` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `_INTC_D3D12_INT_CreateComputePipelineState` | `0x11370` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `_INTC_D3D12_INT_SetCoarsePixelSizeState` | `0x113B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `_INTC_D3D12_INT_RSSetViewports` | `0x113F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `_INTC_D3D12_INT_CreateCommittedResource` | `0x11420` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `_INTC_D3D12_INT_CreateCommittedResource1` | `0x11470` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `_INTC_D3D12_INT_CreatePlacedResource` | `0x114C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `_INTC_D3D12_INT_CreatePlacedResource1` | `0x11510` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `_INTC_D3D12_INT_CreateReservedResource` | `0x11560` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `_INTC_D3D12_INT_CreateReservedResource1` | `0x115A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `_INTC_D3D12_INT_CreateSampler` | `0x115E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `_INTC_D3D12_INT_ResourceBarrier` | `0x11620` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `_INTC_D3D12_INT_CreateShaderResourceView` | `0x11650` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `_INTC_D3D12_INT_CreateRenderTargetView` | `0x11680` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `_INTC_D3D12_INT_CreateUnorderedAccessView` | `0x116B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `_INTC_D3D12_INT_CreateProceduralTextureResourceView` | `0x116F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `_INTC_D3D12_INT_CopyTextureRegion` | `0x11720` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `_INTC_D3D12_INT_ClearProceduralTextureView` | `0x11760` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `_INTC_D3D12_INT_CopyProceduralTextureStatus` | `0x117A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `_INTC_D3D12_INT_SetProceduralTextures` | `0x117E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `_INTC_D3D12_INT_CreateTexelMaskView` | `0x11810` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `_INTC_D3D12_INT_GetDefaultTexelMaskGranularity` | `0x11840` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `_INTC_D3D12_INT_ClearTexelMaskView` | `0x11870` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `_INTC_D3D12_INT_ResolveTexelMask` | `0x118B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `_INTC_D3D12_INT_SetRootTMVs` | `0x118F0` | 81,114 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
