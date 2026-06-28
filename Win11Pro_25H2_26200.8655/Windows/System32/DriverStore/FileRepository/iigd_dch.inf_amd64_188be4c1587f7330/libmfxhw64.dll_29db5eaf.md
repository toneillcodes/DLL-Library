# Binary Specification: libmfxhw64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_188be4c1587f7330\libmfxhw64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `29db5eafbe9a69ce296c8b4f079f060b8e15bf22022531eb5ee474e9131f978d`
* **Total Exported Functions:** 63

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `MFXClose` | `0x439C00` | 480 | UnwindData |  |
| 4 | `MFXDoWork` | `0x439DE0` | 566 | UnwindData |  |
| 6 | `MFXInit` | `0x43A020` | 92 | UnwindData |  |
| 7 | `MFXInitEx` | `0x43A080` | 1,590 | UnwindData |  |
| 17 | `MFXVideoCORE_SyncOperation` | `0x43A890` | 1,057 | UnwindData |  |
| 18 | `MFXVideoDECODE_Close` | `0x43B8B0` | 810 | UnwindData |  |
| 19 | `MFXVideoDECODE_DecodeFrameAsync` | `0x43BBE0` | 2,250 | UnwindData |  |
| 20 | `MFXVideoDECODE_DecodeHeader` | `0x43C4B0` | 1,146 | UnwindData |  |
| 21 | `MFXVideoDECODE_GetDecodeStat` | `0x43C930` | 64 | UnwindData |  |
| 22 | `MFXVideoDECODE_GetPayload` | `0x43C970` | 64 | UnwindData |  |
| 23 | `MFXVideoDECODE_GetVideoParam` | `0x43C9B0` | 64 | UnwindData |  |
| 24 | `MFXVideoDECODE_Init` | `0x43C9F0` | 900 | UnwindData |  |
| 25 | `MFXVideoDECODE_Query` | `0x43CD80` | 1,217 | UnwindData |  |
| 26 | `MFXVideoDECODE_QueryIOSurf` | `0x43D250` | 1,166 | UnwindData |  |
| 27 | `MFXVideoDECODE_Reset` | `0x43D6E0` | 121 | UnwindData |  |
| 28 | `MFXVideoDECODE_SetSkipMode` | `0x43D760` | 64 | UnwindData |  |
| 29 | `MFXVideoENCODE_Close` | `0x441A50` | 1,070 | UnwindData |  |
| 30 | `MFXVideoENCODE_EncodeFrameAsync` | `0x441E80` | 3,090 | UnwindData |  |
| 31 | `MFXVideoENCODE_GetEncodeStat` | `0x442AA0` | 64 | UnwindData |  |
| 32 | `MFXVideoENCODE_GetVideoParam` | `0x442AE0` | 64 | UnwindData |  |
| 33 | `MFXVideoENCODE_Init` | `0x442B20` | 1,123 | UnwindData |  |
| 34 | `MFXVideoENCODE_Query` | `0x442F90` | 1,939 | UnwindData |  |
| 35 | `MFXVideoENCODE_QueryIOSurf` | `0x443730` | 1,473 | UnwindData |  |
| 36 | `MFXVideoENCODE_Reset` | `0x443D00` | 121 | UnwindData |  |
| 37 | `MFXVideoENC_Close` | `0x443E30` | 181 | UnwindData |  |
| 38 | `MFXVideoENC_GetVideoParam` | `0x443EF0` | 64 | UnwindData |  |
| 39 | `MFXVideoENC_Init` | `0x443F30` | 84 | UnwindData |  |
| 40 | `MFXVideoENC_ProcessFrameAsync` | `0x443F90` | 1,266 | UnwindData |  |
| 41 | `MFXVideoENC_Query` | `0x444490` | 263 | UnwindData |  |
| 42 | `MFXVideoENC_QueryIOSurf` | `0x4445A0` | 268 | UnwindData |  |
| 43 | `MFXVideoENC_Reset` | `0x4446B0` | 121 | UnwindData |  |
| 44 | `MFXVideoPAK_Close` | `0x444820` | 155 | UnwindData |  |
| 45 | `MFXVideoPAK_GetVideoParam` | `0x4448C0` | 64 | UnwindData |  |
| 46 | `MFXVideoPAK_Init` | `0x444900` | 156 | UnwindData |  |
| 47 | `MFXVideoPAK_ProcessFrameAsync` | `0x4449A0` | 1,110 | UnwindData |  |
| 48 | `MFXVideoPAK_Query` | `0x444E00` | 80 | UnwindData |  |
| 49 | `MFXVideoPAK_QueryIOSurf` | `0x444E50` | 87 | UnwindData |  |
| 50 | `MFXVideoPAK_Reset` | `0x444EB0` | 121 | UnwindData |  |
| 51 | `MFXVideoUSER_GetPlugin` | `0x445170` | 141 | UnwindData |  |
| 52 | `MFXVideoUSER_ProcessFrameAsync` | `0x445200` | 764 | UnwindData |  |
| 53 | `MFXVideoUSER_Register` | `0x445500` | 815 | UnwindData |  |
| 54 | `MFXVideoUSER_Unregister` | `0x445830` | 387 | UnwindData |  |
| 9 | `MFXQueryIMPL` | `0x446FD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MFXQueryVersion` | `0x447010` | 3,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `MFXCloneSession` | `0x447BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFXDisjoinSession` | `0x447BE0` | 570 | UnwindData |  |
| 5 | `MFXGetPriority` | `0x447E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MFXJoinSession` | `0x447E40` | 595 | UnwindData |  |
| 11 | `MFXSetPriority` | `0x4480A0` | 131 | UnwindData |  |
| 55 | `MFXVideoVPP_Close` | `0x448E30` | 809 | UnwindData |  |
| 56 | `MFXVideoVPP_GetVPPStat` | `0x449160` | 64 | UnwindData |  |
| 57 | `MFXVideoVPP_GetVideoParam` | `0x4491A0` | 64 | UnwindData |  |
| 58 | `MFXVideoVPP_Init` | `0x4491E0` | 942 | UnwindData |  |
| 59 | `MFXVideoVPP_Query` | `0x449590` | 1,163 | UnwindData |  |
| 60 | `MFXVideoVPP_QueryIOSurf` | `0x449A20` | 952 | UnwindData |  |
| 61 | `MFXVideoVPP_Reset` | `0x449DE0` | 121 | UnwindData |  |
| 62 | `MFXVideoVPP_RunFrameVPPAsync` | `0x449E60` | 3,269 | UnwindData |  |
| 63 | `MFXVideoVPP_RunFrameVPPAsyncEx` | `0x44AB30` | 1,735 | UnwindData |  |
| 12 | `MFXVideoCORE_GetHandle` | `0x45A020` | 64 | UnwindData |  |
| 13 | `MFXVideoCORE_QueryPlatform` | `0x45A060` | 126 | UnwindData |  |
| 14 | `MFXVideoCORE_SetBufferAllocator` | `0x45A0E0` | 64 | UnwindData |  |
| 15 | `MFXVideoCORE_SetFrameAllocator` | `0x45A120` | 64 | UnwindData |  |
| 16 | `MFXVideoCORE_SetHandle` | `0x45A160` | 64 | UnwindData |  |
