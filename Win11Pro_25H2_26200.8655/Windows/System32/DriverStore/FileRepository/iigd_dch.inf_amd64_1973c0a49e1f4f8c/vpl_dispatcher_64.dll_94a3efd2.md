# Binary Specification: vpl_dispatcher_64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\vpl_dispatcher_64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `94a3efd2be5e05bb36743e62090ff65f8a9f148919bd46c3e3f913fff8f16795`
* **Total Exported Functions:** 62

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 26 | `MFXVideoCORE_QueryPlatform` | `0x1250` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `MFXVideoENCODE_Query` | `0x12D0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `MFXQueryAdaptersNumber` | `0x16F0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `MFXVideoVPP_RunFrameVPPAsync` | `0x1940` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `MFXQueryIMPL` | `0x1A90` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `MFXVideoVPP_GetVideoParam` | `0x1CA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `MFXVideoDECODE_VPP_Close` | `0x1CE0` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `MFXVideoVPP_GetVPPStat` | `0x1FC0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `MFXVideoDECODE_DecodeHeader` | `0x2320` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MFXMemory_GetSurfaceForEncode` | `0x2370` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `MFXInit` | `0x23F0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `MFXVideoVPP_Reset` | `0x2500` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `MFXUnload` | `0x27D0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `MFXVideoCORE_GetHandle` | `0x2A00` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `MFXQueryAdapters` | `0x2C30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `MFXQueryVersion` | `0x2CA0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MFXVideoDECODE_VPP_GetChannelParam` | `0x2D00` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MFXInitEx` | `0x2DB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MFXMemory_GetSurfaceForDecode` | `0x2E30` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `MFXSetPriority` | `0x2EC0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `MFXVideoENCODE_Init` | `0x2F30` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `MFXVideoDECODE_Reset` | `0x2FA0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `MFXVideoDECODE_VPP_DecodeFrameAsync` | `0x33E0` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `MFXCloneSession` | `0x3820` | 2,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `MFXVideoVPP_ProcessFrameAsync` | `0x4290` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `MFXVideoDECODE_GetVideoParam` | `0x4740` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFXCreateConfig` | `0x4900` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `MFXVideoDECODE_Init` | `0x4BE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `MFXVideoDECODE_Query` | `0x4C40` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MFXVideoCORE_SetFrameAllocator` | `0x4D10` | 1,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MFXQueryAdaptersDecode` | `0x5370` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MFXMemory_GetSurfaceForVPPOut` | `0x5400` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `MFXVideoDECODE_VPP_Init` | `0x56E0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MFXVideoDECODE_Close` | `0x58D0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MFXCreateSession` | `0x5AF0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `MFXVideoVPP_Init` | `0x5BF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `MFXVideoDECODE_VPP_Reset` | `0x5C20` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MFXEnumImplementations` | `0x5C80` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `MFXVideoENCODE_GetVideoParam` | `0x5FF0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MFXDisjoinSession` | `0x6520` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `MFXMemory_GetSurfaceForVPP` | `0x6780` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MFXVideoENCODE_EncodeFrameAsync` | `0x6AD0` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `MFXVideoVPP_Query` | `0x6C20` | 1,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `MFXVideoDECODE_GetPayload` | `0x7110` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `MFXVideoDECODE_QueryIOSurf` | `0x7190` | 1,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `MFXJoinSession` | `0x7700` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `MFXSetConfigFilterProperty` | `0x78D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `MFXVideoCORE_SetHandle` | `0x7950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `MFXVideoCORE_SyncOperation` | `0x7970` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `MFXVideoDECODE_SetSkipMode` | `0x7A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `MFXVideoENCODE_Close` | `0x7A20` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MFXLoad` | `0x7C70` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `MFXVideoENCODE_QueryIOSurf` | `0x7D80` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MFXGetPriority` | `0x7E70` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `MFXVideoENCODE_GetEncodeStat` | `0x7EF0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `MFXVideoENCODE_Reset` | `0x8170` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `MFXVideoVPP_Close` | `0x8240` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MFXDispReleaseImplDescription` | `0x83C0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `MFXVideoVPP_QueryIOSurf` | `0x8480` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `MFXVideoDECODE_DecodeFrameAsync` | `0x86A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `MFXClose` | `0x86D0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `MFXVideoDECODE_GetDecodeStat` | `0x8A30` | 327,041 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
