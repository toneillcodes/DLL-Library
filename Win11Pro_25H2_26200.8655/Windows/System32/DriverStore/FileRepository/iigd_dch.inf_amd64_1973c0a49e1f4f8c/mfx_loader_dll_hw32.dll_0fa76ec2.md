# Binary Specification: mfx_loader_dll_hw32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\mfx_loader_dll_hw32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `0fa76ec26010accda552c686a8b5e081806d7797edc684018d8d1a26dd615779`
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
| 7 | `MFXInitEx` | `0x114B0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MFXJoinSession` | `0x118B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `MFXQueryIMPL` | `0x11900` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MFXQueryVersion` | `0x11940` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `MFXSetPriority` | `0x11980` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MFXVideoCORE_GetHandle` | `0x119C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MFXVideoCORE_QueryPlatform` | `0x11A00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MFXVideoCORE_SetBufferAllocator` | `0x11A40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `MFXVideoCORE_SetFrameAllocator` | `0x11A80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MFXVideoCORE_SetHandle` | `0x11AC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `MFXVideoCORE_SyncOperation` | `0x11B00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MFXVideoDECODE_Close` | `0x11B40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `MFXVideoDECODE_DecodeFrameAsync` | `0x11B80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `MFXVideoDECODE_DecodeHeader` | `0x11BD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `MFXVideoDECODE_GetDecodeStat` | `0x11C10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `MFXVideoDECODE_GetPayload` | `0x11C50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `MFXVideoDECODE_GetVideoParam` | `0x11C90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `MFXVideoDECODE_Init` | `0x11CD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `MFXVideoDECODE_Query` | `0x11D10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `MFXVideoDECODE_QueryIOSurf` | `0x11D50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MFXVideoDECODE_Reset` | `0x11D90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `MFXVideoDECODE_SetSkipMode` | `0x11DD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `MFXVideoENCODE_Close` | `0x11E10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MFXVideoENCODE_EncodeFrameAsync` | `0x11E50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `MFXVideoENCODE_GetEncodeStat` | `0x11E90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `MFXVideoENCODE_GetVideoParam` | `0x11ED0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `MFXVideoENCODE_Init` | `0x11F10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `MFXVideoENCODE_Query` | `0x11F50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `MFXVideoENCODE_QueryIOSurf` | `0x11F90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `MFXVideoENCODE_Reset` | `0x11FD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `MFXVideoENC_Close` | `0x12010` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `MFXVideoENC_GetVideoParam` | `0x12050` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `MFXVideoENC_Init` | `0x12090` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `MFXVideoENC_ProcessFrameAsync` | `0x120D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `MFXVideoENC_Query` | `0x12110` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `MFXVideoENC_QueryIOSurf` | `0x12150` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MFXVideoENC_Reset` | `0x12190` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `MFXVideoPAK_Close` | `0x121D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `MFXVideoPAK_GetVideoParam` | `0x12210` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `MFXVideoPAK_Init` | `0x12250` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MFXVideoPAK_ProcessFrameAsync` | `0x12290` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `MFXVideoPAK_Query` | `0x122D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `MFXVideoPAK_QueryIOSurf` | `0x12310` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `MFXVideoPAK_Reset` | `0x12350` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `MFXVideoUSER_GetPlugin` | `0x12390` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `MFXVideoUSER_ProcessFrameAsync` | `0x123D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `MFXVideoUSER_Register` | `0x12420` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `MFXVideoUSER_Unregister` | `0x12460` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `MFXVideoVPP_Close` | `0x124A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `MFXVideoVPP_GetVPPStat` | `0x124E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `MFXVideoVPP_GetVideoParam` | `0x12520` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `MFXVideoVPP_Init` | `0x12560` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `MFXVideoVPP_Query` | `0x125A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `MFXVideoVPP_QueryIOSurf` | `0x125E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `MFXVideoVPP_Reset` | `0x12620` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `MFXVideoVPP_RunFrameVPPAsync` | `0x12660` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `MFXVideoVPP_RunFrameVPPAsyncEx` | `0x126B0` | 448,954 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
