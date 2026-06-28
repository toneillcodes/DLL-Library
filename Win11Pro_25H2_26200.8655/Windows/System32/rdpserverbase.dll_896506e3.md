# Binary Specification: rdpserverbase.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rdpserverbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `896506e3868f4e7ea5ea22e2175f25b01b23c9dcbe2719293859cbdd180b8954`
* **Total Exported Functions:** 25

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `?GetTileFirst@Tiler@@QEAAJPEBURdpRect@@PEAU2@@Z` | `0xF510` | 605 | UnwindData |  |
| 1 | `?GetEncodingPixelMap@RdpSurface@@QEAAJPEAPEAVPixelMap@@@Z` | `0x23470` | 44 | UnwindData |  |
| 25 | `RDPSERVERBASE_CreateInstance` | `0x3E0F0` | 117 | UnwindData |  |
| 6 | `?GetTileNext@Tiler@@QEAAJPEAURdpRect@@@Z` | `0x4B560` | 114,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `?GetGraphicsSourceContext@RdpSurface@@QEAAJPEAPEAUIRdpGFXSourceUpdateContext@@@Z` | `0x675B0` | 39 | UnwindData |  |
| 8 | `?LogRDPGraphicsErrorStrings@RDPGraphicsTraceLogging@@YAXPEAD0IJ@Z` | `0x7B170` | 257 | UnwindData |  |
| 7 | `?Initialize@Tiler@@QEAAJPEBURdpRect@@0@Z` | `0x7FD80` | 197 | UnwindData |  |
| 2 | `?GetGfxPipeSettingBOOL@@YAJPEAGHPEAH@Z` | `0x8B9F0` | 162 | UnwindData |  |
| 3 | `?GetGfxPipeSettingUINT@@YAJPEAGIPEAI@Z` | `0x8BAA0` | 145 | UnwindData |  |
| 21 | `ImgClassifierTrainingDataProvider_Register` | `0xE2D40` | 205 | UnwindData |  |
| 22 | `ImgClassifierTrainingDataProvider_Unregister` | `0xE2E20` | 52 | UnwindData |  |
| 16 | `?RDPServerStackQOE_Register@@YAJXZ` | `0xE3670` | 43 | UnwindData |  |
| 17 | `?RDPServerStackQOE_Unregister@@YAXXZ` | `0xE36B0` | 52 | UnwindData |  |
| 18 | `CCompressedUpdateContext_CreateInstance` | `0xE6630` | 96 | UnwindData |  |
| 19 | `CUpdateContext_CreateInstance` | `0xE66A0` | 96 | UnwindData |  |
| 20 | `CUpdateDataAccumulator_CreateInstance` | `0xE6710` | 121 | UnwindData |  |
| 23 | `RDPEncryptionTraceLogging_Register` | `0x13C670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `RDPEncryptionTraceLogging_Unregister` | `0x13C690` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?LogRDPGraphicsFirstNonBlackFrame@RDPGraphicsTraceLogging@@YAX_K@Z` | `0x13CF60` | 212 | UnwindData |  |
| 10 | `?LogRDPGraphicsFirstNonBlackFramePostLogon@RDPGraphicsTraceLogging@@YAXI@Z` | `0x13D040` | 210 | UnwindData |  |
| 11 | `?LogRDPGraphicsSubsampleAdapter@RDPGraphicsTraceLogging@@YAXPEBGII@Z` | `0x13D910` | 205 | UnwindData |  |
| 12 | `?LogRDPGraphicsSubsampleFailure@RDPGraphicsTraceLogging@@YAXJI@Z` | `0x13D9F0` | 171 | UnwindData |  |
| 13 | `?LogRDPGraphicsVOBRHint@RDPGraphicsTraceLogging@@YAXI_KII@Z` | `0x13DC00` | 230 | UnwindData |  |
| 14 | `?RDPGraphicsTraceLogging_Register@RDPGraphicsTraceLogging@@YAJXZ` | `0x13DCF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?RDPGraphicsTraceLogging_Unregister@RDPGraphicsTraceLogging@@YAXXZ` | `0x13DD10` | 248,902 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
