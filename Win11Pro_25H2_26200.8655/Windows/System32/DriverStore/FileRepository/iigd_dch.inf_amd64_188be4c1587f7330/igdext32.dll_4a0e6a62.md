# Binary Specification: igdext32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\igdext32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `4a0e6a6283b1a23ac85b9d4b5e03577d534d1670e54fdc248f3972ac51cc1046`
* **Total Exported Functions:** 81

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `D3D11GetSupportedVersions` | `0x16E0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `D3D11CreateDeviceExtensionContext1` | `0x1900` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `D3D11CreateDeviceExtensionContext` | `0x1A10` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `D3D11DestroyDeviceExtensionContext` | `0x1B20` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `D3D12GetSupportedVersions` | `0x1BB0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `D3D12CreateDeviceExtensionContext` | `0x1DD0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `D3D12DestroyDeviceExtensionContext` | `0x1EE0` | 59,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `D3D11GetSupportedVersions2` | `0x108D0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `D3D11CreateDeviceExtensionContext2` | `0x10B10` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `D3D12GetSupportedVersions2` | `0x10CA0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `D3D12CreateDeviceExtensionContext2` | `0x10EE0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `D3D11D3D12CreateDeviceExtensionContext2` | `0x11080` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `D3D11D3D12DestroyDeviceExtensionContext2` | `0x112E0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `D3D11EnumInternalExtensions` | `0x113E0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `D3D11CreateDeviceExtensionContextInternal` | `0x11480` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `D3D12EnumInternalExtensions` | `0x11600` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `D3D12CreateDeviceExtensionContextInternal` | `0x116A0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `D3D11D3D12CreateDeviceExtensionContextInternal` | `0x11830` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `_INTC_D3D11_CreateDeviceExtensionContext` | `0x11EB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `_INTC_D3D12_CreateDeviceExtensionContext` | `0x11EF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `_INTC_CreateDeviceExtensionContext` | `0x11F30` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `_INTC_D3D11_BeginUAVOverlap` | `0x11F90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `_INTC_D3D11_EndUAVOverlap` | `0x11FC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `_INTC_D3D11_MultiDrawInstancedIndirect` | `0x11FF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `_INTC_D3D11_MultiDrawIndexedInstancedIndirect` | `0x12020` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `_INTC_D3D11_MultiDrawInstancedIndirectCountIndirect` | `0x12050` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `_INTC_D3D11_MultiDrawIndexedInstancedIndirectCountIndirect` | `0x12090` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `_INTC_D3D11_SetDepthBounds` | `0x120D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `_INTC_D3D11_CreateTexture2D` | `0x12110` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `_INTC_D3D12_CreateCommandQueue` | `0x12150` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `_INTC_D3D12_CreateComputePipelineState` | `0x12190` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `_INTC_D3D12_CreateReservedResource` | `0x121D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `_INTC_D3D12_CreateCommittedResource` | `0x12210` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `_INTC_D3D12_CreateCommittedResource1` | `0x12250` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `_INTC_D3D12_CreateHeap` | `0x12290` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `_INTC_D3D12_CreatePlacedResource` | `0x122D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `_INTC_D3D12_CreateHostRTASResource` | `0x12320` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `_INTC_D3D12_BuildRaytracingAccelerationStructure_Host` | `0x12360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `_INTC_D3D12_CopyRaytracingAccelerationStructure_Host` | `0x12390` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `_INTC_D3D12_EmitRaytracingAccelerationStructurePostbuildInfo_Host` | `0x123C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `_INTC_D3D12_GetRaytracingAccelerationStructurePrebuildInfo_Host` | `0x123F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `_INTC_D3D12_TransferHostRTAS` | `0x12420` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `_INTC_D3D12_SetDriverEventMetadata` | `0x12460` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `_INTC_D3D12_QueryCpuVisibleVidmem` | `0x12490` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `_INTC_D3D12_CreateStateObject` | `0x124C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `_INTC_D3D12_BuildRaytracingAccelerationStructure` | `0x12500` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `_INTC_D3D12_GetRaytracingAccelerationStructurePrebuildInfo` | `0x12540` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `_INTC_D3D11_INT_CreateDeviceExtensionContext` | `0x12570` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `_INTC_D3D12_INT_CreateDeviceExtensionContext` | `0x125B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `_INTC_INT_CreateDeviceExtensionContext` | `0x125F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `_INTC_D3D12_INT_CreateGraphicsPipelineState` | `0x12650` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `_INTC_D3D12_INT_CreateGraphicsPipelineState1` | `0x12690` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `_INTC_D3D12_INT_CreateGraphicsPipelineState2` | `0x126D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `_INTC_D3D12_INT_CreateComputePipelineState` | `0x12710` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `_INTC_D3D12_INT_SetCoarsePixelSizeState` | `0x12750` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `_INTC_D3D12_INT_RSSetViewports` | `0x12790` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `_INTC_D3D12_INT_CreateHeap` | `0x127C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `_INTC_D3D12_INT_CreateCommittedResource` | `0x12800` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `_INTC_D3D12_INT_CreateCommittedResource1` | `0x12850` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `_INTC_D3D12_INT_CreateCommittedResource2` | `0x128A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `_INTC_D3D12_INT_ReserveGpuVirtualAddress` | `0x128F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `_INTC_D3D12_INT_CreatePlacedResource` | `0x12930` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `_INTC_D3D12_INT_CreatePlacedResource1` | `0x12980` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `_INTC_D3D12_INT_CreateReservedResource` | `0x129D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `_INTC_D3D12_INT_CreateReservedResource1` | `0x12A10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `_INTC_D3D12_INT_CreateReservedResource2` | `0x12A50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `_INTC_D3D12_INT_CreateSampler` | `0x12A90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `_INTC_D3D12_INT_ResourceBarrier` | `0x12AD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `_INTC_D3D12_INT_CreateShaderResourceView` | `0x12B00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `_INTC_D3D12_INT_CreateRenderTargetView` | `0x12B30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `_INTC_D3D12_INT_CreateUnorderedAccessView` | `0x12B60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `_INTC_D3D12_INT_CreateProceduralTextureResourceView` | `0x12BA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `_INTC_D3D12_INT_CopyTextureRegion` | `0x12BD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `_INTC_D3D12_INT_ClearProceduralTextureView` | `0x12C10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `_INTC_D3D12_INT_CopyProceduralTextureStatus` | `0x12C50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `_INTC_D3D12_INT_SetProceduralTextures` | `0x12C90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `_INTC_D3D12_INT_CreateTexelMaskView` | `0x12CC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `_INTC_D3D12_INT_GetDefaultTexelMaskGranularity` | `0x12CF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `_INTC_D3D12_INT_ClearTexelMaskView` | `0x12D20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `_INTC_D3D12_INT_ResolveTexelMask` | `0x12D60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `_INTC_D3D12_INT_SetRootTMVs` | `0x12DA0` | 81,914 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
