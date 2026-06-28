# Binary Specification: vpl_dispatcher_64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\vpl_dispatcher_64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8da252b7621ee1c57818208f187aeb2ce527a956d301a95a240025d786c9dbfb`
* **Total Exported Functions:** 62

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 26 | `MFXVideoCORE_QueryPlatform` | `0x12A0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `MFXVideoENCODE_Query` | `0x1330` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `MFXQueryAdaptersNumber` | `0x17C0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `MFXVideoVPP_RunFrameVPPAsync` | `0x1A40` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `MFXQueryIMPL` | `0x1B70` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `MFXVideoVPP_GetVideoParam` | `0x1DD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `MFXVideoDECODE_VPP_Close` | `0x1E10` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `MFXVideoVPP_GetVPPStat` | `0x2110` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `MFXVideoDECODE_DecodeHeader` | `0x2480` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MFXMemory_GetSurfaceForEncode` | `0x24E0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `MFXInit` | `0x2580` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `MFXVideoVPP_Reset` | `0x2690` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `MFXUnload` | `0x29A0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `MFXVideoCORE_GetHandle` | `0x2BE0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `MFXQueryAdapters` | `0x2E00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `MFXQueryVersion` | `0x2E60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MFXVideoDECODE_VPP_GetChannelParam` | `0x2ED0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MFXInitEx` | `0x2F90` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MFXMemory_GetSurfaceForDecode` | `0x3000` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `MFXSetPriority` | `0x30A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `MFXVideoENCODE_Init` | `0x3110` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `MFXVideoDECODE_Reset` | `0x3180` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `MFXVideoDECODE_VPP_DecodeFrameAsync` | `0x35C0` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `MFXCloneSession` | `0x3A20` | 2,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `MFXVideoVPP_ProcessFrameAsync` | `0x44E0` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `MFXVideoDECODE_GetVideoParam` | `0x49B0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFXCreateConfig` | `0x4B60` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `MFXVideoDECODE_Init` | `0x4E80` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `MFXVideoDECODE_Query` | `0x4F20` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MFXVideoCORE_SetFrameAllocator` | `0x5000` | 1,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MFXQueryAdaptersDecode` | `0x5640` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MFXMemory_GetSurfaceForVPPOut` | `0x56F0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `MFXVideoDECODE_VPP_Init` | `0x5A70` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MFXVideoDECODE_Close` | `0x5C70` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MFXCreateSession` | `0x5EF0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `MFXVideoVPP_Init` | `0x6010` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `MFXVideoDECODE_VPP_Reset` | `0x6040` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MFXEnumImplementations` | `0x60A0` | 960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `MFXVideoENCODE_GetVideoParam` | `0x6460` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MFXDisjoinSession` | `0x69F0` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `MFXMemory_GetSurfaceForVPP` | `0x6CA0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MFXVideoENCODE_EncodeFrameAsync` | `0x6FF0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `MFXVideoVPP_Query` | `0x7130` | 1,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `MFXVideoDECODE_GetPayload` | `0x76B0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `MFXVideoDECODE_QueryIOSurf` | `0x7770` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `MFXJoinSession` | `0x7D10` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `MFXSetConfigFilterProperty` | `0x7EE0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `MFXVideoCORE_SetHandle` | `0x7F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `MFXVideoCORE_SyncOperation` | `0x7FA0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `MFXVideoDECODE_SetSkipMode` | `0x8040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `MFXVideoENCODE_Close` | `0x8060` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MFXLoad` | `0x82C0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `MFXVideoENCODE_QueryIOSurf` | `0x83C0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MFXGetPriority` | `0x84E0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `MFXVideoENCODE_GetEncodeStat` | `0x8570` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `MFXVideoENCODE_Reset` | `0x87C0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `MFXVideoVPP_Close` | `0x8880` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MFXDispReleaseImplDescription` | `0x89F0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `MFXVideoVPP_QueryIOSurf` | `0x8AD0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `MFXVideoDECODE_DecodeFrameAsync` | `0x8D00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `MFXClose` | `0x8D30` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `MFXVideoDECODE_GetDecodeStat` | `0x90E0` | 332,881 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
