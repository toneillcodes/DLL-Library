# Binary Specification: igdext64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\igdext64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b69a247fffa4aed63e4bc1eb6b3b90c2e3928ae1aa0d753cdcf51a0ea1b4bd43`
* **Total Exported Functions:** 81

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
| 11 | `D3D11GetSupportedVersions2` | `0x13450` | 602 | UnwindData |  |
| 3 | `D3D11CreateDeviceExtensionContext2` | `0x136B0` | 353 | UnwindData |  |
| 18 | `D3D12GetSupportedVersions2` | `0x13820` | 602 | UnwindData |  |
| 13 | `D3D12CreateDeviceExtensionContext2` | `0x13A80` | 358 | UnwindData |  |
| 5 | `D3D11D3D12CreateDeviceExtensionContext2` | `0x13BF0` | 612 | UnwindData |  |
| 7 | `D3D11D3D12DestroyDeviceExtensionContext2` | `0x13E60` | 198 | UnwindData |  |
| 9 | `D3D11EnumInternalExtensions` | `0x13F30` | 57 | UnwindData |  |
| 4 | `D3D11CreateDeviceExtensionContextInternal` | `0x14030` | 349 | UnwindData |  |
| 16 | `D3D12EnumInternalExtensions` | `0x141A0` | 49 | UnwindData |  |
| 14 | `D3D12CreateDeviceExtensionContextInternal` | `0x142A0` | 354 | UnwindData |  |
| 6 | `D3D11D3D12CreateDeviceExtensionContextInternal` | `0x14410` | 612 | UnwindData |  |
| 21 | `_INTC_D3D11_CreateDeviceExtensionContext` | `0x14B40` | 55 | UnwindData |  |
| 37 | `_INTC_D3D12_CreateDeviceExtensionContext` | `0x14B80` | 55 | UnwindData |  |
| 19 | `_INTC_CreateDeviceExtensionContext` | `0x14BC0` | 140 | UnwindData |  |
| 20 | `_INTC_D3D11_BeginUAVOverlap` | `0x14C60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `_INTC_D3D11_EndUAVOverlap` | `0x14C90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `_INTC_D3D11_MultiDrawInstancedIndirect` | `0x14CC0` | 50 | UnwindData |  |
| 25 | `_INTC_D3D11_MultiDrawIndexedInstancedIndirect` | `0x14D00` | 50 | UnwindData |  |
| 28 | `_INTC_D3D11_MultiDrawInstancedIndirectCountIndirect` | `0x14D40` | 95 | UnwindData |  |
| 26 | `_INTC_D3D11_MultiDrawIndexedInstancedIndirectCountIndirect` | `0x14DB0` | 95 | UnwindData |  |
| 29 | `_INTC_D3D11_SetDepthBounds` | `0x14E20` | 30 | UnwindData |  |
| 22 | `_INTC_D3D11_CreateTexture2D` | `0x14E50` | 40 | UnwindData |  |
| 33 | `_INTC_D3D12_CreateCommandQueue` | `0x14E80` | 41 | UnwindData |  |
| 36 | `_INTC_D3D12_CreateComputePipelineState` | `0x14EB0` | 41 | UnwindData |  |
| 41 | `_INTC_D3D12_CreateReservedResource` | `0x14EE0` | 67 | UnwindData |  |
| 34 | `_INTC_D3D12_CreateCommittedResource` | `0x14F30` | 97 | UnwindData |  |
| 35 | `_INTC_D3D12_CreateCommittedResource1` | `0x14FA0` | 97 | UnwindData |  |
| 38 | `_INTC_D3D12_CreateHeap` | `0x15010` | 41 | UnwindData |  |
| 40 | `_INTC_D3D12_CreatePlacedResource` | `0x15040` | 97 | UnwindData |  |
| 39 | `_INTC_D3D12_CreateHostRTASResource` | `0x150B0` | 57 | UnwindData |  |
| 31 | `_INTC_D3D12_BuildRaytracingAccelerationStructure_Host` | `0x150F0` | 31 | UnwindData |  |
| 32 | `_INTC_D3D12_CopyRaytracingAccelerationStructure_Host` | `0x15120` | 31 | UnwindData |  |
| 43 | `_INTC_D3D12_EmitRaytracingAccelerationStructurePostbuildInfo_Host` | `0x15150` | 31 | UnwindData |  |
| 45 | `_INTC_D3D12_GetRaytracingAccelerationStructurePrebuildInfo_Host` | `0x15180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `_INTC_D3D12_TransferHostRTAS` | `0x151A0` | 41 | UnwindData |  |
| 79 | `_INTC_D3D12_SetDriverEventMetadata` | `0x151D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `_INTC_D3D12_QueryCpuVisibleVidmem` | `0x151F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `_INTC_D3D12_CreateStateObject` | `0x15210` | 41 | UnwindData |  |
| 30 | `_INTC_D3D12_BuildRaytracingAccelerationStructure` | `0x15240` | 51 | UnwindData |  |
| 44 | `_INTC_D3D12_GetRaytracingAccelerationStructurePrebuildInfo` | `0x15280` | 31 | UnwindData |  |
| 24 | `_INTC_D3D11_INT_CreateDeviceExtensionContext` | `0x152A0` | 55 | UnwindData |  |
| 54 | `_INTC_D3D12_INT_CreateDeviceExtensionContext` | `0x152E0` | 55 | UnwindData |  |
| 81 | `_INTC_INT_CreateDeviceExtensionContext` | `0x15320` | 140 | UnwindData |  |
| 55 | `_INTC_D3D12_INT_CreateGraphicsPipelineState` | `0x153C0` | 41 | UnwindData |  |
| 56 | `_INTC_D3D12_INT_CreateGraphicsPipelineState1` | `0x153F0` | 41 | UnwindData |  |
| 57 | `_INTC_D3D12_INT_CreateGraphicsPipelineState2` | `0x15420` | 41 | UnwindData |  |
| 53 | `_INTC_D3D12_INT_CreateComputePipelineState` | `0x15450` | 41 | UnwindData |  |
| 75 | `_INTC_D3D12_INT_SetCoarsePixelSizeState` | `0x15480` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `_INTC_D3D12_INT_RSSetViewports` | `0x154B0` | 31 | UnwindData |  |
| 58 | `_INTC_D3D12_INT_CreateHeap` | `0x154E0` | 41 | UnwindData |  |
| 50 | `_INTC_D3D12_INT_CreateCommittedResource` | `0x15510` | 97 | UnwindData |  |
| 51 | `_INTC_D3D12_INT_CreateCommittedResource1` | `0x15580` | 97 | UnwindData |  |
| 52 | `_INTC_D3D12_INT_CreateCommittedResource2` | `0x155F0` | 97 | UnwindData |  |
| 72 | `_INTC_D3D12_INT_ReserveGpuVirtualAddress` | `0x15660` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `_INTC_D3D12_INT_CreatePlacedResource` | `0x15690` | 97 | UnwindData |  |
| 60 | `_INTC_D3D12_INT_CreatePlacedResource1` | `0x15700` | 97 | UnwindData |  |
| 63 | `_INTC_D3D12_INT_CreateReservedResource` | `0x15770` | 67 | UnwindData |  |
| 64 | `_INTC_D3D12_INT_CreateReservedResource1` | `0x157C0` | 67 | UnwindData |  |
| 65 | `_INTC_D3D12_INT_CreateReservedResource2` | `0x15810` | 67 | UnwindData |  |
| 66 | `_INTC_D3D12_INT_CreateSampler` | `0x15860` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `_INTC_D3D12_INT_ResourceBarrier` | `0x15890` | 31 | UnwindData |  |
| 67 | `_INTC_D3D12_INT_CreateShaderResourceView` | `0x158C0` | 31 | UnwindData |  |
| 62 | `_INTC_D3D12_INT_CreateRenderTargetView` | `0x158F0` | 31 | UnwindData |  |
| 69 | `_INTC_D3D12_INT_CreateUnorderedAccessView` | `0x15920` | 41 | UnwindData |  |
| 61 | `_INTC_D3D12_INT_CreateProceduralTextureResourceView` | `0x15950` | 31 | UnwindData |  |
| 49 | `_INTC_D3D12_INT_CopyTextureRegion` | `0x15980` | 96 | UnwindData |  |
| 46 | `_INTC_D3D12_INT_ClearProceduralTextureView` | `0x159F0` | 51 | UnwindData |  |
| 48 | `_INTC_D3D12_INT_CopyProceduralTextureStatus` | `0x15A30` | 98 | UnwindData |  |
| 76 | `_INTC_D3D12_INT_SetProceduralTextures` | `0x15AA0` | 31 | UnwindData |  |
| 68 | `_INTC_D3D12_INT_CreateTexelMaskView` | `0x15AD0` | 31 | UnwindData |  |
| 70 | `_INTC_D3D12_INT_GetDefaultTexelMaskGranularity` | `0x15B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `_INTC_D3D12_INT_ClearTexelMaskView` | `0x15B20` | 89 | UnwindData |  |
| 73 | `_INTC_D3D12_INT_ResolveTexelMask` | `0x15B80` | 70 | UnwindData |  |
| 77 | `_INTC_D3D12_INT_SetRootTMVs` | `0x15BD0` | 31 | UnwindData |  |
