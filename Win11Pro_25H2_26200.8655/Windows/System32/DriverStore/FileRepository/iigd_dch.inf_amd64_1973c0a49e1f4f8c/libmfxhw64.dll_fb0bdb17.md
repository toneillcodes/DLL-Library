# Binary Specification: libmfxhw64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\libmfxhw64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fb0bdb1733af66ed0f312edf6c8dbc22482f7de9fae8ca0c285eaf5d49a8e910`
* **Total Exported Functions:** 63

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `MFXClose` | `0x439810` | 480 | UnwindData |  |
| 4 | `MFXDoWork` | `0x4399F0` | 566 | UnwindData |  |
| 6 | `MFXInit` | `0x439C30` | 92 | UnwindData |  |
| 7 | `MFXInitEx` | `0x439C90` | 1,590 | UnwindData |  |
| 17 | `MFXVideoCORE_SyncOperation` | `0x43A4A0` | 1,057 | UnwindData |  |
| 18 | `MFXVideoDECODE_Close` | `0x43B4C0` | 810 | UnwindData |  |
| 19 | `MFXVideoDECODE_DecodeFrameAsync` | `0x43B7F0` | 2,250 | UnwindData |  |
| 20 | `MFXVideoDECODE_DecodeHeader` | `0x43C0C0` | 1,146 | UnwindData |  |
| 21 | `MFXVideoDECODE_GetDecodeStat` | `0x43C540` | 64 | UnwindData |  |
| 22 | `MFXVideoDECODE_GetPayload` | `0x43C580` | 64 | UnwindData |  |
| 23 | `MFXVideoDECODE_GetVideoParam` | `0x43C5C0` | 64 | UnwindData |  |
| 24 | `MFXVideoDECODE_Init` | `0x43C600` | 900 | UnwindData |  |
| 25 | `MFXVideoDECODE_Query` | `0x43C990` | 1,217 | UnwindData |  |
| 26 | `MFXVideoDECODE_QueryIOSurf` | `0x43CE60` | 1,166 | UnwindData |  |
| 27 | `MFXVideoDECODE_Reset` | `0x43D2F0` | 121 | UnwindData |  |
| 28 | `MFXVideoDECODE_SetSkipMode` | `0x43D370` | 64 | UnwindData |  |
| 29 | `MFXVideoENCODE_Close` | `0x441660` | 1,070 | UnwindData |  |
| 30 | `MFXVideoENCODE_EncodeFrameAsync` | `0x441A90` | 3,090 | UnwindData |  |
| 31 | `MFXVideoENCODE_GetEncodeStat` | `0x4426B0` | 64 | UnwindData |  |
| 32 | `MFXVideoENCODE_GetVideoParam` | `0x4426F0` | 64 | UnwindData |  |
| 33 | `MFXVideoENCODE_Init` | `0x442730` | 1,123 | UnwindData |  |
| 34 | `MFXVideoENCODE_Query` | `0x442BA0` | 1,939 | UnwindData |  |
| 35 | `MFXVideoENCODE_QueryIOSurf` | `0x443340` | 1,473 | UnwindData |  |
| 36 | `MFXVideoENCODE_Reset` | `0x443910` | 121 | UnwindData |  |
| 37 | `MFXVideoENC_Close` | `0x443A40` | 181 | UnwindData |  |
| 38 | `MFXVideoENC_GetVideoParam` | `0x443B00` | 64 | UnwindData |  |
| 39 | `MFXVideoENC_Init` | `0x443B40` | 84 | UnwindData |  |
| 40 | `MFXVideoENC_ProcessFrameAsync` | `0x443BA0` | 1,266 | UnwindData |  |
| 41 | `MFXVideoENC_Query` | `0x4440A0` | 263 | UnwindData |  |
| 42 | `MFXVideoENC_QueryIOSurf` | `0x4441B0` | 268 | UnwindData |  |
| 43 | `MFXVideoENC_Reset` | `0x4442C0` | 121 | UnwindData |  |
| 44 | `MFXVideoPAK_Close` | `0x444430` | 155 | UnwindData |  |
| 45 | `MFXVideoPAK_GetVideoParam` | `0x4444D0` | 64 | UnwindData |  |
| 46 | `MFXVideoPAK_Init` | `0x444510` | 156 | UnwindData |  |
| 47 | `MFXVideoPAK_ProcessFrameAsync` | `0x4445B0` | 1,110 | UnwindData |  |
| 48 | `MFXVideoPAK_Query` | `0x444A10` | 80 | UnwindData |  |
| 49 | `MFXVideoPAK_QueryIOSurf` | `0x444A60` | 87 | UnwindData |  |
| 50 | `MFXVideoPAK_Reset` | `0x444AC0` | 121 | UnwindData |  |
| 51 | `MFXVideoUSER_GetPlugin` | `0x444D80` | 141 | UnwindData |  |
| 52 | `MFXVideoUSER_ProcessFrameAsync` | `0x444E10` | 764 | UnwindData |  |
| 53 | `MFXVideoUSER_Register` | `0x445110` | 815 | UnwindData |  |
| 54 | `MFXVideoUSER_Unregister` | `0x445440` | 387 | UnwindData |  |
| 9 | `MFXQueryIMPL` | `0x446BE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MFXQueryVersion` | `0x446C20` | 3,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `MFXCloneSession` | `0x4477E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFXDisjoinSession` | `0x4477F0` | 570 | UnwindData |  |
| 5 | `MFXGetPriority` | `0x447A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MFXJoinSession` | `0x447A50` | 595 | UnwindData |  |
| 11 | `MFXSetPriority` | `0x447CB0` | 131 | UnwindData |  |
| 55 | `MFXVideoVPP_Close` | `0x448A40` | 809 | UnwindData |  |
| 56 | `MFXVideoVPP_GetVPPStat` | `0x448D70` | 64 | UnwindData |  |
| 57 | `MFXVideoVPP_GetVideoParam` | `0x448DB0` | 64 | UnwindData |  |
| 58 | `MFXVideoVPP_Init` | `0x448DF0` | 942 | UnwindData |  |
| 59 | `MFXVideoVPP_Query` | `0x4491A0` | 1,163 | UnwindData |  |
| 60 | `MFXVideoVPP_QueryIOSurf` | `0x449630` | 952 | UnwindData |  |
| 61 | `MFXVideoVPP_Reset` | `0x4499F0` | 121 | UnwindData |  |
| 62 | `MFXVideoVPP_RunFrameVPPAsync` | `0x449A70` | 3,269 | UnwindData |  |
| 63 | `MFXVideoVPP_RunFrameVPPAsyncEx` | `0x44A740` | 1,735 | UnwindData |  |
| 12 | `MFXVideoCORE_GetHandle` | `0x459C30` | 64 | UnwindData |  |
| 13 | `MFXVideoCORE_QueryPlatform` | `0x459C70` | 126 | UnwindData |  |
| 14 | `MFXVideoCORE_SetBufferAllocator` | `0x459CF0` | 64 | UnwindData |  |
| 15 | `MFXVideoCORE_SetFrameAllocator` | `0x459D30` | 64 | UnwindData |  |
| 16 | `MFXVideoCORE_SetHandle` | `0x459D70` | 64 | UnwindData |  |
