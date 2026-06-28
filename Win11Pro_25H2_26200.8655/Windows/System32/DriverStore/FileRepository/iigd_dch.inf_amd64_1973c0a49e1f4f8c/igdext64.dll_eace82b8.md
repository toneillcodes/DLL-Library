# Binary Specification: igdext64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\igdext64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eace82b8246c9b2cb3b8d72f991fdc9e8077bb417fc97b1f6ba8f360b752dc1f`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `D3D11GetSupportedVersions` | `0x1820` | 507 | UnwindData |  |
| 2 | `D3D11CreateDeviceExtensionContext1` | `0x1A30` | 259 | UnwindData |  |
| 1 | `D3D11CreateDeviceExtensionContext` | `0x1B40` | 249 | UnwindData |  |
| 8 | `D3D11DestroyDeviceExtensionContext` | `0x1C40` | 102 | UnwindData |  |
| 17 | `D3D12GetSupportedVersions` | `0x1CB0` | 507 | UnwindData |  |
| 12 | `D3D12CreateDeviceExtensionContext` | `0x1EC0` | 259 | UnwindData |  |
| 15 | `D3D12DestroyDeviceExtensionContext` | `0x1FD0` | 102 | UnwindData |  |
| 11 | `D3D11GetSupportedVersions2` | `0x12030` | 602 | UnwindData |  |
| 3 | `D3D11CreateDeviceExtensionContext2` | `0x12290` | 346 | UnwindData |  |
| 18 | `D3D12GetSupportedVersions2` | `0x123F0` | 602 | UnwindData |  |
| 13 | `D3D12CreateDeviceExtensionContext2` | `0x12650` | 350 | UnwindData |  |
| 5 | `D3D11D3D12CreateDeviceExtensionContext2` | `0x127C0` | 585 | UnwindData |  |
| 7 | `D3D11D3D12DestroyDeviceExtensionContext2` | `0x12A10` | 175 | UnwindData |  |
| 9 | `D3D11EnumInternalExtensions` | `0x12AD0` | 57 | UnwindData |  |
| 4 | `D3D11CreateDeviceExtensionContextInternal` | `0x12BD0` | 346 | UnwindData |  |
| 16 | `D3D12EnumInternalExtensions` | `0x12D30` | 49 | UnwindData |  |
| 14 | `D3D12CreateDeviceExtensionContextInternal` | `0x12E30` | 350 | UnwindData |  |
| 6 | `D3D11D3D12CreateDeviceExtensionContextInternal` | `0x12FA0` | 585 | UnwindData |  |
| 21 | `_INTC_D3D11_CreateDeviceExtensionContext` | `0x13690` | 55 | UnwindData |  |
| 35 | `_INTC_D3D12_CreateDeviceExtensionContext` | `0x136D0` | 73 | UnwindData |  |
| 19 | `_INTC_CreateDeviceExtensionContext` | `0x13720` | 140 | UnwindData |  |
| 20 | `_INTC_D3D11_BeginUAVOverlap` | `0x137C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `_INTC_D3D11_EndUAVOverlap` | `0x137F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `_INTC_D3D11_MultiDrawInstancedIndirect` | `0x13820` | 50 | UnwindData |  |
| 25 | `_INTC_D3D11_MultiDrawIndexedInstancedIndirect` | `0x13860` | 50 | UnwindData |  |
| 28 | `_INTC_D3D11_MultiDrawInstancedIndirectCountIndirect` | `0x138A0` | 95 | UnwindData |  |
| 26 | `_INTC_D3D11_MultiDrawIndexedInstancedIndirectCountIndirect` | `0x13910` | 95 | UnwindData |  |
| 29 | `_INTC_D3D11_SetDepthBounds` | `0x13980` | 30 | UnwindData |  |
| 22 | `_INTC_D3D11_CreateTexture2D` | `0x139B0` | 40 | UnwindData |  |
| 32 | `_INTC_D3D12_CreateCommandQueue` | `0x139E0` | 41 | UnwindData |  |
| 34 | `_INTC_D3D12_CreateComputePipelineState` | `0x13A10` | 41 | UnwindData |  |
| 38 | `_INTC_D3D12_CreateReservedResource` | `0x13A40` | 67 | UnwindData |  |
| 33 | `_INTC_D3D12_CreateCommittedResource` | `0x13A90` | 97 | UnwindData |  |
| 37 | `_INTC_D3D12_CreatePlacedResource` | `0x13B00` | 97 | UnwindData |  |
| 36 | `_INTC_D3D12_CreateHostRTASResource` | `0x13B70` | 57 | UnwindData |  |
| 30 | `_INTC_D3D12_BuildRaytracingAccelerationStructure_Host` | `0x13BB0` | 31 | UnwindData |  |
| 31 | `_INTC_D3D12_CopyRaytracingAccelerationStructure_Host` | `0x13BE0` | 31 | UnwindData |  |
| 39 | `_INTC_D3D12_EmitRaytracingAccelerationStructurePostbuildInfo_Host` | `0x13C10` | 31 | UnwindData |  |
| 40 | `_INTC_D3D12_GetRaytracingAccelerationStructurePrebuildInfo_Host` | `0x13C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `_INTC_D3D12_TransferHostRTAS` | `0x13C60` | 41 | UnwindData |  |
| 69 | `_INTC_D3D12_SetDriverEventMetadata` | `0x13C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `_INTC_D3D11_INT_CreateDeviceExtensionContext` | `0x13CB0` | 55 | UnwindData |  |
| 48 | `_INTC_D3D12_INT_CreateDeviceExtensionContext` | `0x13CF0` | 55 | UnwindData |  |
| 71 | `_INTC_INT_CreateDeviceExtensionContext` | `0x13D30` | 140 | UnwindData |  |
| 49 | `_INTC_D3D12_INT_CreateGraphicsPipelineState` | `0x13DD0` | 41 | UnwindData |  |
| 50 | `_INTC_D3D12_INT_CreateGraphicsPipelineState1` | `0x13E00` | 41 | UnwindData |  |
| 51 | `_INTC_D3D12_INT_CreateGraphicsPipelineState2` | `0x13E30` | 41 | UnwindData |  |
| 47 | `_INTC_D3D12_INT_CreateComputePipelineState` | `0x13E60` | 41 | UnwindData |  |
| 66 | `_INTC_D3D12_INT_SetCoarsePixelSizeState` | `0x13E90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `_INTC_D3D12_INT_RSSetViewports` | `0x13EC0` | 31 | UnwindData |  |
| 45 | `_INTC_D3D12_INT_CreateCommittedResource` | `0x13EF0` | 97 | UnwindData |  |
| 46 | `_INTC_D3D12_INT_CreateCommittedResource1` | `0x13F60` | 97 | UnwindData |  |
| 52 | `_INTC_D3D12_INT_CreatePlacedResource` | `0x13FD0` | 97 | UnwindData |  |
| 53 | `_INTC_D3D12_INT_CreatePlacedResource1` | `0x14040` | 97 | UnwindData |  |
| 56 | `_INTC_D3D12_INT_CreateReservedResource` | `0x140B0` | 67 | UnwindData |  |
| 57 | `_INTC_D3D12_INT_CreateReservedResource1` | `0x14100` | 67 | UnwindData |  |
| 58 | `_INTC_D3D12_INT_CreateSampler` | `0x14150` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `_INTC_D3D12_INT_ResourceBarrier` | `0x14180` | 31 | UnwindData |  |
| 59 | `_INTC_D3D12_INT_CreateShaderResourceView` | `0x141B0` | 31 | UnwindData |  |
| 55 | `_INTC_D3D12_INT_CreateRenderTargetView` | `0x141E0` | 31 | UnwindData |  |
| 61 | `_INTC_D3D12_INT_CreateUnorderedAccessView` | `0x14210` | 41 | UnwindData |  |
| 54 | `_INTC_D3D12_INT_CreateProceduralTextureResourceView` | `0x14240` | 31 | UnwindData |  |
| 44 | `_INTC_D3D12_INT_CopyTextureRegion` | `0x14270` | 96 | UnwindData |  |
| 41 | `_INTC_D3D12_INT_ClearProceduralTextureView` | `0x142E0` | 51 | UnwindData |  |
| 43 | `_INTC_D3D12_INT_CopyProceduralTextureStatus` | `0x14320` | 98 | UnwindData |  |
| 67 | `_INTC_D3D12_INT_SetProceduralTextures` | `0x14390` | 31 | UnwindData |  |
| 60 | `_INTC_D3D12_INT_CreateTexelMaskView` | `0x143C0` | 31 | UnwindData |  |
| 62 | `_INTC_D3D12_INT_GetDefaultTexelMaskGranularity` | `0x143F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `_INTC_D3D12_INT_ClearTexelMaskView` | `0x14410` | 89 | UnwindData |  |
| 64 | `_INTC_D3D12_INT_ResolveTexelMask` | `0x14470` | 70 | UnwindData |  |
| 68 | `_INTC_D3D12_INT_SetRootTMVs` | `0x144C0` | 31 | UnwindData |  |
