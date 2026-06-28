# Binary Specification: libmfxhw32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\iigd_dch.inf_amd64_1973c0a49e1f4f8c\libmfxhw32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `b6e9675c0bf53ec264bd620af3c3ea1717844098185de5fb5451b5605fe87124`
* **Total Exported Functions:** 63

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `MFXClose` | `0x3EF0D0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MFXDoWork` | `0x3EF2C0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MFXInit` | `0x3EF4C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MFXInitEx` | `0x3EF530` | 1,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `MFXVideoCORE_SyncOperation` | `0x3EFB90` | 4,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MFXVideoDECODE_Close` | `0x3F0E10` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `MFXVideoDECODE_DecodeFrameAsync` | `0x3F1080` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `MFXVideoDECODE_DecodeHeader` | `0x3F1670` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `MFXVideoDECODE_GetDecodeStat` | `0x3F1A10` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `MFXVideoDECODE_GetPayload` | `0x3F1AD0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `MFXVideoDECODE_GetVideoParam` | `0x3F1B90` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `MFXVideoDECODE_Init` | `0x3F1C50` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `MFXVideoDECODE_Query` | `0x3F1EF0` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `MFXVideoDECODE_QueryIOSurf` | `0x3F2350` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `MFXVideoDECODE_Reset` | `0x3F2760` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `MFXVideoDECODE_SetSkipMode` | `0x3F2840` | 22,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `MFXVideoENCODE_Close` | `0x3F8050` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MFXVideoENCODE_EncodeFrameAsync` | `0x3F82E0` | 2,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `MFXVideoENCODE_GetEncodeStat` | `0x3F8BC0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `MFXVideoENCODE_GetVideoParam` | `0x3F8C80` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `MFXVideoENCODE_Init` | `0x3F8D50` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `MFXVideoENCODE_Query` | `0x3F9080` | 1,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `MFXVideoENCODE_QueryIOSurf` | `0x3F9680` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `MFXVideoENCODE_Reset` | `0x3F9AD0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `MFXVideoENC_Close` | `0x3F9D50` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `MFXVideoENC_GetVideoParam` | `0x3F9E50` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `MFXVideoENC_Init` | `0x3F9F10` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `MFXVideoENC_ProcessFrameAsync` | `0x3FA010` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `MFXVideoENC_Query` | `0x3FA4C0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `MFXVideoENC_QueryIOSurf` | `0x3FA630` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MFXVideoENC_Reset` | `0x3FA7B0` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `MFXVideoPAK_Close` | `0x3FAA50` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `MFXVideoPAK_GetVideoParam` | `0x3FAB40` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `MFXVideoPAK_Init` | `0x3FAC00` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MFXVideoPAK_ProcessFrameAsync` | `0x3FAD00` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `MFXVideoPAK_Query` | `0x3FB100` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `MFXVideoPAK_QueryIOSurf` | `0x3FB1F0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `MFXVideoPAK_Reset` | `0x3FB2F0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `MFXVideoUSER_GetPlugin` | `0x3FB7A0` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `MFXVideoUSER_ProcessFrameAsync` | `0x3FB8C0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `MFXVideoUSER_Register` | `0x3FBAF0` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `MFXVideoUSER_Unregister` | `0x3FBDC0` | 6,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `MFXQueryIMPL` | `0x3FD5F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MFXQueryVersion` | `0x3FD640` | 3,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `MFXCloneSession` | `0x3FE2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFXDisjoinSession` | `0x3FE2C0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MFXGetPriority` | `0x3FE4C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MFXJoinSession` | `0x3FE4F0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `MFXSetPriority` | `0x3FE6A0` | 4,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `MFXVideoVPP_Close` | `0x3FF710` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `MFXVideoVPP_GetVPPStat` | `0x3FF980` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `MFXVideoVPP_GetVideoParam` | `0x3FFA40` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `MFXVideoVPP_Init` | `0x3FFB00` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `MFXVideoVPP_Query` | `0x3FFDD0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `MFXVideoVPP_QueryIOSurf` | `0x400130` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `MFXVideoVPP_Reset` | `0x400420` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `MFXVideoVPP_RunFrameVPPAsync` | `0x400500` | 2,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `MFXVideoVPP_RunFrameVPPAsyncEx` | `0x400E70` | 62,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MFXVideoCORE_GetHandle` | `0x4101A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MFXVideoCORE_QueryPlatform` | `0x410260` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MFXVideoCORE_SetBufferAllocator` | `0x410350` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `MFXVideoCORE_SetFrameAllocator` | `0x410410` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MFXVideoCORE_SetHandle` | `0x4104D0` | 6,109,043 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
