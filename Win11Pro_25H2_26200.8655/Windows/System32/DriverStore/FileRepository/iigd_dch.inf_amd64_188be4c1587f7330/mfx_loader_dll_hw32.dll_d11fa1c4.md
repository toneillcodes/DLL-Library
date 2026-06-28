# Binary Specification: mfx_loader_dll_hw32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\mfx_loader_dll_hw32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `d11fa1c4f41a31ee66d07c34400d23cbbd92913563c53f498fa63a30ed9a79fe`
* **Total Exported Functions:** 63

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `MFXCloneSession` | `0x112F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `MFXClose` | `0x11330` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFXDisjoinSession` | `0x11380` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MFXDoWork` | `0x113C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MFXGetPriority` | `0x11400` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MFXInit` | `0x11440` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MFXInitEx` | `0x114B0` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MFXJoinSession` | `0x118C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `MFXQueryIMPL` | `0x11910` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MFXQueryVersion` | `0x11950` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `MFXSetPriority` | `0x11990` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MFXVideoCORE_GetHandle` | `0x119D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MFXVideoCORE_QueryPlatform` | `0x11A10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MFXVideoCORE_SetBufferAllocator` | `0x11A50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `MFXVideoCORE_SetFrameAllocator` | `0x11A90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MFXVideoCORE_SetHandle` | `0x11AD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `MFXVideoCORE_SyncOperation` | `0x11B10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MFXVideoDECODE_Close` | `0x11B50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `MFXVideoDECODE_DecodeFrameAsync` | `0x11B90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `MFXVideoDECODE_DecodeHeader` | `0x11BE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `MFXVideoDECODE_GetDecodeStat` | `0x11C20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `MFXVideoDECODE_GetPayload` | `0x11C60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `MFXVideoDECODE_GetVideoParam` | `0x11CA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `MFXVideoDECODE_Init` | `0x11CE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `MFXVideoDECODE_Query` | `0x11D20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `MFXVideoDECODE_QueryIOSurf` | `0x11D60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MFXVideoDECODE_Reset` | `0x11DA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `MFXVideoDECODE_SetSkipMode` | `0x11DE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `MFXVideoENCODE_Close` | `0x11E20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MFXVideoENCODE_EncodeFrameAsync` | `0x11E60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `MFXVideoENCODE_GetEncodeStat` | `0x11EA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `MFXVideoENCODE_GetVideoParam` | `0x11EE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `MFXVideoENCODE_Init` | `0x11F20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `MFXVideoENCODE_Query` | `0x11F60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `MFXVideoENCODE_QueryIOSurf` | `0x11FA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `MFXVideoENCODE_Reset` | `0x11FE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `MFXVideoENC_Close` | `0x12020` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `MFXVideoENC_GetVideoParam` | `0x12060` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `MFXVideoENC_Init` | `0x120A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `MFXVideoENC_ProcessFrameAsync` | `0x120E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `MFXVideoENC_Query` | `0x12120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `MFXVideoENC_QueryIOSurf` | `0x12160` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MFXVideoENC_Reset` | `0x121A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `MFXVideoPAK_Close` | `0x121E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `MFXVideoPAK_GetVideoParam` | `0x12220` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `MFXVideoPAK_Init` | `0x12260` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MFXVideoPAK_ProcessFrameAsync` | `0x122A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `MFXVideoPAK_Query` | `0x122E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `MFXVideoPAK_QueryIOSurf` | `0x12320` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `MFXVideoPAK_Reset` | `0x12360` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `MFXVideoUSER_GetPlugin` | `0x123A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `MFXVideoUSER_ProcessFrameAsync` | `0x123E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `MFXVideoUSER_Register` | `0x12430` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `MFXVideoUSER_Unregister` | `0x12470` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `MFXVideoVPP_Close` | `0x124B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `MFXVideoVPP_GetVPPStat` | `0x124F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `MFXVideoVPP_GetVideoParam` | `0x12530` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `MFXVideoVPP_Init` | `0x12570` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `MFXVideoVPP_Query` | `0x125B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `MFXVideoVPP_QueryIOSurf` | `0x125F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `MFXVideoVPP_Reset` | `0x12630` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `MFXVideoVPP_RunFrameVPPAsync` | `0x12670` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `MFXVideoVPP_RunFrameVPPAsyncEx` | `0x126C0` | 448,970 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
