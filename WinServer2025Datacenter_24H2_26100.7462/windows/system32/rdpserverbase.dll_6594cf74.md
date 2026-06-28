# Binary Specification: rdpserverbase.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rdpserverbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6594cf7427c8fee010975a235d1ef5cc0431e8ffdc07fc796cc8e0b682857572`
* **Total Exported Functions:** 25

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `?GetTileFirst@Tiler@@QEAAJPEBURdpRect@@PEAU2@@Z` | `0xF3B0` | 605 | UnwindData |  |
| 1 | `?GetEncodingPixelMap@RdpSurface@@QEAAJPEAPEAVPixelMap@@@Z` | `0x23340` | 44 | UnwindData |  |
| 25 | `RDPSERVERBASE_CreateInstance` | `0x3DFD0` | 117 | UnwindData |  |
| 6 | `?GetTileNext@Tiler@@QEAAJPEAURdpRect@@@Z` | `0x4B440` | 114,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `?GetGraphicsSourceContext@RdpSurface@@QEAAJPEAPEAUIRdpGFXSourceUpdateContext@@@Z` | `0x674D0` | 39 | UnwindData |  |
| 8 | `?LogRDPGraphicsErrorStrings@RDPGraphicsTraceLogging@@YAXPEAD0IJ@Z` | `0x7AEF0` | 257 | UnwindData |  |
| 7 | `?Initialize@Tiler@@QEAAJPEBURdpRect@@0@Z` | `0x7FA00` | 197 | UnwindData |  |
| 2 | `?GetGfxPipeSettingBOOL@@YAJPEAGHPEAH@Z` | `0x8AAD0` | 162 | UnwindData |  |
| 3 | `?GetGfxPipeSettingUINT@@YAJPEAGIPEAI@Z` | `0x8AB80` | 145 | UnwindData |  |
| 21 | `ImgClassifierTrainingDataProvider_Register` | `0xDF980` | 205 | UnwindData |  |
| 22 | `ImgClassifierTrainingDataProvider_Unregister` | `0xDFA60` | 52 | UnwindData |  |
| 16 | `?RDPServerStackQOE_Register@@YAJXZ` | `0xE02B0` | 43 | UnwindData |  |
| 17 | `?RDPServerStackQOE_Unregister@@YAXXZ` | `0xE02F0` | 52 | UnwindData |  |
| 18 | `CCompressedUpdateContext_CreateInstance` | `0xE3270` | 96 | UnwindData |  |
| 19 | `CUpdateContext_CreateInstance` | `0xE32E0` | 96 | UnwindData |  |
| 20 | `CUpdateDataAccumulator_CreateInstance` | `0xE3350` | 121 | UnwindData |  |
| 23 | `RDPEncryptionTraceLogging_Register` | `0x13C450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `RDPEncryptionTraceLogging_Unregister` | `0x13C470` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?LogRDPGraphicsFirstNonBlackFrame@RDPGraphicsTraceLogging@@YAX_K@Z` | `0x13CD40` | 212 | UnwindData |  |
| 10 | `?LogRDPGraphicsFirstNonBlackFramePostLogon@RDPGraphicsTraceLogging@@YAXI@Z` | `0x13CE20` | 210 | UnwindData |  |
| 11 | `?LogRDPGraphicsSubsampleAdapter@RDPGraphicsTraceLogging@@YAXPEBGII@Z` | `0x13D6F0` | 205 | UnwindData |  |
| 12 | `?LogRDPGraphicsSubsampleFailure@RDPGraphicsTraceLogging@@YAXJI@Z` | `0x13D7D0` | 171 | UnwindData |  |
| 13 | `?LogRDPGraphicsVOBRHint@RDPGraphicsTraceLogging@@YAXI_KII@Z` | `0x13D9E0` | 230 | UnwindData |  |
| 14 | `?RDPGraphicsTraceLogging_Register@RDPGraphicsTraceLogging@@YAJXZ` | `0x13DAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?RDPGraphicsTraceLogging_Unregister@RDPGraphicsTraceLogging@@YAXXZ` | `0x13DAF0` | 236,220 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
