# Binary Specification: libmfxhw32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\libmfxhw32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `3dbf072ada9556e189da62656b399dbaaaca327a4a44f18b9745880ed26722a5`
* **Total Exported Functions:** 63

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `MFXClose` | `0x3EF530` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MFXDoWork` | `0x3EF720` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MFXInit` | `0x3EF920` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MFXInitEx` | `0x3EF990` | 1,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `MFXVideoCORE_SyncOperation` | `0x3EFFF0` | 4,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MFXVideoDECODE_Close` | `0x3F1270` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `MFXVideoDECODE_DecodeFrameAsync` | `0x3F14E0` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `MFXVideoDECODE_DecodeHeader` | `0x3F1AD0` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `MFXVideoDECODE_GetDecodeStat` | `0x3F1E70` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `MFXVideoDECODE_GetPayload` | `0x3F1F30` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `MFXVideoDECODE_GetVideoParam` | `0x3F1FF0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `MFXVideoDECODE_Init` | `0x3F20B0` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `MFXVideoDECODE_Query` | `0x3F2350` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `MFXVideoDECODE_QueryIOSurf` | `0x3F27B0` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MFXVideoDECODE_Reset` | `0x3F2BC0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `MFXVideoDECODE_SetSkipMode` | `0x3F2CA0` | 22,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `MFXVideoENCODE_Close` | `0x3F84B0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MFXVideoENCODE_EncodeFrameAsync` | `0x3F8740` | 2,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `MFXVideoENCODE_GetEncodeStat` | `0x3F9020` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `MFXVideoENCODE_GetVideoParam` | `0x3F90E0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `MFXVideoENCODE_Init` | `0x3F91A0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `MFXVideoENCODE_Query` | `0x3F94D0` | 1,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `MFXVideoENCODE_QueryIOSurf` | `0x3F9AD0` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `MFXVideoENCODE_Reset` | `0x3F9F20` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `MFXVideoENC_Close` | `0x3FA1A0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `MFXVideoENC_GetVideoParam` | `0x3FA2A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `MFXVideoENC_Init` | `0x3FA360` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `MFXVideoENC_ProcessFrameAsync` | `0x3FA460` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `MFXVideoENC_Query` | `0x3FA910` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `MFXVideoENC_QueryIOSurf` | `0x3FAA80` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MFXVideoENC_Reset` | `0x3FAC00` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `MFXVideoPAK_Close` | `0x3FAEA0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `MFXVideoPAK_GetVideoParam` | `0x3FAF90` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `MFXVideoPAK_Init` | `0x3FB050` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MFXVideoPAK_ProcessFrameAsync` | `0x3FB150` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `MFXVideoPAK_Query` | `0x3FB550` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `MFXVideoPAK_QueryIOSurf` | `0x3FB640` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `MFXVideoPAK_Reset` | `0x3FB740` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `MFXVideoUSER_GetPlugin` | `0x3FBBF0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `MFXVideoUSER_ProcessFrameAsync` | `0x3FBD10` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `MFXVideoUSER_Register` | `0x3FBF40` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `MFXVideoUSER_Unregister` | `0x3FC210` | 6,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `MFXQueryIMPL` | `0x3FDA40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MFXQueryVersion` | `0x3FDA90` | 3,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `MFXCloneSession` | `0x3FE700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFXDisjoinSession` | `0x3FE710` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MFXGetPriority` | `0x3FE910` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MFXJoinSession` | `0x3FE940` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `MFXSetPriority` | `0x3FEAF0` | 4,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `MFXVideoVPP_Close` | `0x3FFB60` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `MFXVideoVPP_GetVPPStat` | `0x3FFDD0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `MFXVideoVPP_GetVideoParam` | `0x3FFE90` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `MFXVideoVPP_Init` | `0x3FFF50` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `MFXVideoVPP_Query` | `0x400220` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `MFXVideoVPP_QueryIOSurf` | `0x400580` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `MFXVideoVPP_Reset` | `0x400870` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `MFXVideoVPP_RunFrameVPPAsync` | `0x400950` | 2,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `MFXVideoVPP_RunFrameVPPAsyncEx` | `0x4012C0` | 62,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MFXVideoCORE_GetHandle` | `0x4105F0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MFXVideoCORE_QueryPlatform` | `0x4106B0` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MFXVideoCORE_SetBufferAllocator` | `0x4107A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `MFXVideoCORE_SetFrameAllocator` | `0x410860` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MFXVideoCORE_SetHandle` | `0x410920` | 6,142,179 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
