# Binary Specification: libmfxhw64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\libmfxhw64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `889949165ad40bb22d07f3122622aaa7081a661511ab740ec226770a836171f7`
* **Total Exported Functions:** 63

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `MFXCloneSession` | `0x11950` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `MFXClose` | `0x11980` | 133 | UnwindData |  |
| 3 | `MFXDisjoinSession` | `0x11A10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MFXDoWork` | `0x11A40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MFXGetPriority` | `0x11A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MFXInit` | `0x11AA0` | 92 | UnwindData |  |
| 7 | `MFXInitEx` | `0x11B00` | 950 | UnwindData |  |
| 8 | `MFXJoinSession` | `0x11EC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `MFXQueryIMPL` | `0x11F00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MFXQueryVersion` | `0x11F30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `MFXSetPriority` | `0x11F60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MFXVideoCORE_GetHandle` | `0x11F90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MFXVideoCORE_QueryPlatform` | `0x11FC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MFXVideoCORE_SetBufferAllocator` | `0x11FF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `MFXVideoCORE_SetFrameAllocator` | `0x12020` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MFXVideoCORE_SetHandle` | `0x12050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `MFXVideoCORE_SyncOperation` | `0x12080` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MFXVideoDECODE_Close` | `0x120B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `MFXVideoDECODE_DecodeFrameAsync` | `0x120E0` | 69 | UnwindData |  |
| 20 | `MFXVideoDECODE_DecodeHeader` | `0x12130` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `MFXVideoDECODE_GetDecodeStat` | `0x12160` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `MFXVideoDECODE_GetPayload` | `0x12190` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `MFXVideoDECODE_GetVideoParam` | `0x121C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `MFXVideoDECODE_Init` | `0x121F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `MFXVideoDECODE_Query` | `0x12220` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `MFXVideoDECODE_QueryIOSurf` | `0x12250` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MFXVideoDECODE_Reset` | `0x12280` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `MFXVideoDECODE_SetSkipMode` | `0x122B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `MFXVideoENCODE_Close` | `0x122E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MFXVideoENCODE_EncodeFrameAsync` | `0x12310` | 69 | UnwindData |  |
| 31 | `MFXVideoENCODE_GetEncodeStat` | `0x12360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `MFXVideoENCODE_GetVideoParam` | `0x12390` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `MFXVideoENCODE_Init` | `0x123C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `MFXVideoENCODE_Query` | `0x123F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `MFXVideoENCODE_QueryIOSurf` | `0x12420` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `MFXVideoENCODE_Reset` | `0x12450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `MFXVideoENC_Close` | `0x12480` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `MFXVideoENC_GetVideoParam` | `0x124B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `MFXVideoENC_Init` | `0x124E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `MFXVideoENC_ProcessFrameAsync` | `0x12510` | 53 | UnwindData |  |
| 41 | `MFXVideoENC_Query` | `0x12550` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `MFXVideoENC_QueryIOSurf` | `0x12580` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MFXVideoENC_Reset` | `0x125B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `MFXVideoPAK_Close` | `0x125E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `MFXVideoPAK_GetVideoParam` | `0x12610` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `MFXVideoPAK_Init` | `0x12640` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MFXVideoPAK_ProcessFrameAsync` | `0x12670` | 53 | UnwindData |  |
| 48 | `MFXVideoPAK_Query` | `0x126B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `MFXVideoPAK_QueryIOSurf` | `0x126E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `MFXVideoPAK_Reset` | `0x12710` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `MFXVideoUSER_GetPlugin` | `0x12740` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `MFXVideoUSER_ProcessFrameAsync` | `0x12770` | 77 | UnwindData |  |
| 53 | `MFXVideoUSER_Register` | `0x127C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `MFXVideoUSER_Unregister` | `0x127F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `MFXVideoVPP_Close` | `0x12820` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `MFXVideoVPP_GetVPPStat` | `0x12850` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `MFXVideoVPP_GetVideoParam` | `0x12880` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `MFXVideoVPP_Init` | `0x128B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `MFXVideoVPP_Query` | `0x128E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `MFXVideoVPP_QueryIOSurf` | `0x12910` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `MFXVideoVPP_Reset` | `0x12940` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `MFXVideoVPP_RunFrameVPPAsync` | `0x12970` | 69 | UnwindData |  |
| 63 | `MFXVideoVPP_RunFrameVPPAsyncEx` | `0x129C0` | 69 | UnwindData |  |
