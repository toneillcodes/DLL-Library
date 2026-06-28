# Binary Specification: rdpbase.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rdpbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bb4cead60ed789f12b20ed005117fed3575d5daad47a21b4f28ac002fee84c72`
* **Total Exported Functions:** 255

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 49 | `?ProcessAlignedData_AVX@SSECBCHash2@@AEAAXPEBIIII@Z` | `0x6A70` | 754 | UnwindData |  |
| 246 | `TsAddRectsToRegion` | `0xD860` | 84 | UnwindData |  |
| 111 | `PAL_System_AtomicDecrement` | `0x1D360` | 4,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `RdpX_DateTime_GetHighResolutionTimeSinceReboot` | `0x1E4C0` | 124 | UnwindData |  |
| 76 | `ApplyLuminanceFilter` | `0x217B0` | 89 | UnwindData |  |
| 16 | `?Compress@NSCodecCompressor@@QEAA_NAEBVPixelMap@@_NPEAEIAEAI@Z` | `0x22980` | 667 | UnwindData |  |
| 106 | `MemCopyAligned_SSE` | `0x27920` | 93 | UnwindData |  |
| 185 | `RDPENCHLPWS_GetIPFromAddr` | `0x27D10` | 270 | UnwindData |  |
| 129 | `PAL_System_CritSecTerminate` | `0x29750` | 68 | UnwindData |  |
| 144 | `PAL_System_HandleFree` | `0x297A0` | 33 | UnwindData |  |
| 119 | `PAL_System_CondSignal` | `0x2ACF0` | 33 | UnwindData |  |
| 120 | `PAL_System_CondWait` | `0x2C2B0` | 114 | UnwindData |  |
| 173 | `RDPCompressEx` | `0x30750` | 144 | UnwindData |  |
| 174 | `RDPCompress_GetContextSize` | `0x30940` | 55 | UnwindData |  |
| 125 | `PAL_System_CritSecEnter` | `0x32EC0` | 40 | UnwindData |  |
| 156 | `PAL_System_ThreadGetId` | `0x33740` | 55 | UnwindData |  |
| 117 | `PAL_System_CondAlloc` | `0x33E50` | 76 | UnwindData |  |
| 151 | `PAL_System_SemaphoreAlloc` | `0x34AC0` | 68 | UnwindData |  |
| 126 | `PAL_System_CritSecInit` | `0x34B50` | 241 | UnwindData |  |
| 168 | `RDPAPI_GetGenericCounter` | `0x35CF0` | 534 | UnwindData |  |
| 142 | `PAL_System_GetNumberOfProcessors` | `0x35F90` | 48 | UnwindData |  |
| 251 | `TsGetRegionRects` | `0x36A50` | 41 | UnwindData |  |
| 115 | `PAL_System_AtomicIncrement` | `0x36F80` | 12,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `?SearchCache@CRDPCache@@UEAAJIIPEAPEAUIUnknown@@PEAI@Z` | `0x39EC0` | 362 | UnwindData |  |
| 70 | `?UpdateKeys@SSECBCHash2@@AEBAXXZ` | `0x3A0B0` | 151 | UnwindData |  |
| 60 | `?SetCacheEntry@CRDPCache@@UEAAJIIPEAUIUnknown@@PEAI@Z` | `0x3A320` | 318 | UnwindData |  |
| 102 | `GetSupportedSSELevel_SSE` | `0x3C510` | 39 | UnwindData |  |
| 128 | `PAL_System_CritSecLeave` | `0x3C540` | 40 | UnwindData |  |
| 109 | `PAL_System_AtomicCompareAndExchange` | `0x3C880` | 8,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `?ProcessUnalignedData_REG@SSECBCHash2@@AEAAXPEBIIII@Z` | `0x3E7C0` | 46 | UnwindData |  |
| 250 | `TsGetRegionRectCount` | `0x3E970` | 2,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `?ProcessAlignedData_SSE41@SSECBCHash2@@AEAAXPEBIIII@Z` | `0x3F430` | 376 | UnwindData |  |
| 97 | `DrawIconToPixelMap` | `0x3FCE0` | 172 | UnwindData |  |
| 33 | `?GetMillisecondCount@PipelineClock@@QEAAIXZ` | `0x426D0` | 107 | UnwindData |  |
| 31 | `?GetInstance@PipelineClock@@SAAEAV1@XZ` | `0x42750` | 104 | UnwindData |  |
| 7 | `??0SSECBCHash2@@QEAA@XZ` | `0x427C0` | 132 | UnwindData |  |
| 53 | `?PromoteEntry@Evict@@QEAAXKK@Z` | `0x43560` | 359 | UnwindData |  |
| 252 | `TsSetRegionFromRects` | `0x43CB0` | 177 | UnwindData |  |
| 235 | `RgnlibBA_CreateInstance` | `0x4B8C0` | 423 | UnwindData |  |
| 247 | `TsCreateRegion` | `0x4BB80` | 611 | UnwindData |  |
| 37 | `?GetTickCount@PipelineClock@@QEAAIXZ` | `0x4BDF0` | 47 | UnwindData |  |
| 248 | `TsDestroyRegion` | `0x4BFC0` | 94 | UnwindData |  |
| 159 | `PAL_System_TimeGetTickCount` | `0x4EAF0` | 55 | UnwindData |  |
| 38 | `?GetTimeHNS@PipelineClock@@QEAA_JXZ` | `0x50480` | 115 | UnwindData |  |
| 28 | `?EvictEntry@Evict@@QEAAPEAU_SCORE_ENTRY@@XZ` | `0x508E0` | 314 | UnwindData |  |
| 101 | `ExpandRectForSSE` | `0x51710` | 4,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `?InsertEntry@Evict@@QEAAXPEAU_SCORE_ENTRY@@K@Z` | `0x52760` | 170 | UnwindData |  |
| 183 | `RDPENCHLPREG_ReadValueDWORD` | `0x52C40` | 289 | UnwindData |  |
| 249 | `TsGetRegionBoundingBox` | `0x56350` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `EncryptData` | `0x56830` | 96 | UnwindData |  |
| 93 | `DecryptData` | `0x568A0` | 175 | UnwindData |  |
| 210 | `RDP_RC4` | `0x56960` | 73 | UnwindData |  |
| 208 | `RDP_MD5Init` | `0x56C80` | 168 | UnwindData |  |
| 222 | `RDP_SHAInit` | `0x56D30` | 161 | UnwindData |  |
| 75 | `?XObjectId_RdpXSecFilterServer_CreateObject@@YA?AW4_XResult32@@PEAURdpXInterface@@IW4_XInterfaceId32@@PEAPEAX@Z` | `0x57060` | 153 | UnwindData |  |
| 237 | `SubtractRects` | `0x5A1B0` | 511 | UnwindData |  |
| 32 | `?GetMillisecondCount64@PipelineClock@@QEAA_KXZ` | `0x5A530` | 42 | UnwindData |  |
| 169 | `RDPAPI_GetGlobalObject` | `0x5AEB0` | 2,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `?Reset@CRDPCache@@UEAAJI@Z` | `0x5B9B0` | 566 | UnwindData |  |
| 206 | `RDP_HMACMD5Update` | `0x5C8D0` | 66 | UnwindData |  |
| 209 | `RDP_MD5Update` | `0x5C8D0` | 66 | UnwindData |  |
| 145 | `PAL_System_MemAlloc` | `0x5C9D0` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `RDP_SHAUpdate` | `0x5D1D0` | 68 | UnwindData |  |
| 62 | `?SetDecodeBuffer@RdpGfxProtocolBaseDecoder@@IEAAXPEBEI@Z` | `0x5D5B0` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `TSDbgAssertThread` | `0x5D850` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `CAPAPI_GetCapSet` | `0x5DD20` | 73 | UnwindData |  |
| 30 | `?GetFreeEntry@Evict@@QEAAPEAU_SCORE_ENTRY@@XZ` | `0x5DDE0` | 83 | UnwindData |  |
| 92 | `CRdpFIPSEncryption_CreateInstance` | `0x5DF40` | 495 | UnwindData |  |
| 24 | `?CreateInstance@RdpEncodeBuffer@@SAJPEAVRdpEncodeBufferPool@@KPEAPEAV1@@Z` | `0x5F620` | 262 | UnwindData |  |
| 207 | `RDP_MD5Final` | `0x60AA0` | 70 | UnwindData |  |
| 230 | `RdpX_AtomicIncrement32` | `0x60EE0` | 4,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `RdpUnionRect` | `0x620F0` | 86 | UnwindData |  |
| 229 | `RdpX_AtomicDecrement32` | `0x629D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `PAL_System_AtomicCompareAndExchangePointer` | `0x62A10` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `RDP_SHAFinal` | `0x62A80` | 66 | UnwindData |  |
| 178 | `RDPDecompress` | `0x63040` | 144 | UnwindData |  |
| 146 | `PAL_System_MemFree` | `0x63D90` | 8,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `TSFree` | `0x63D90` | 8,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `PAL_System_CritSecIsLockedByCurrentThread` | `0x65ED0` | 56 | UnwindData |  |
| 186 | `RDPENCHLPWS_GetPortFromAddr` | `0x663B0` | 71 | UnwindData |  |
| 171 | `RDPBASE_CreateInstance` | `0x688D0` | 8,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `RDPENCGDIHLP_FlipBitmapBits` | `0x6A940` | 197 | UnwindData |  |
| 81 | `CAPAPI_InitializeCombinedCaps` | `0x6B200` | 107 | UnwindData |  |
| 107 | `MemEqual` | `0x6C160` | 177 | UnwindData |  |
| 193 | `RDPServerStackDiagnostics_GetSymbolicNameFromCode` | `0x6C220` | 17,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?ClearCache@CRDPCache@@UEAAJXZ` | `0x70590` | 203 | UnwindData |  |
| 179 | `RDPENCDirectConnector_CreateInstance` | `0x70C90` | 643 | UnwindData |  |
| 1 | `??0CRDPCache@@QEAA@XZ` | `0x71500` | 169 | UnwindData |  |
| 239 | `TSAlloc` | `0x72390` | 4,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `CRDPCacCodec_CreateInstance` | `0x73480` | 276 | UnwindData |  |
| 89 | `CRDPENCGfxEncoder_CreateInstance` | `0x73E30` | 448 | UnwindData |  |
| 87 | `CRDPCacVideoCodec_CreateInstance` | `0x75F00` | 23 | UnwindData |  |
| 233 | `RdpX_GetActivityIdPrefix` | `0x76060` | 81 | UnwindData |  |
| 152 | `PAL_System_SemaphoreRelease` | `0x76B30` | 40 | UnwindData |  |
| 184 | `RDPENCHLPWSErr2Hr` | `0x76CD0` | 34 | UnwindData |  |
| 88 | `CRDPCaps_CreateInstance` | `0x76E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `?IsTestMode@PipelineClock@@QEAA_NXZ` | `0x76E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `RdpX_Threading_CreateCriticalSection` | `0x76E70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `PAL_System_SwitchToThread` | `0x76EA0` | 13,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `CRDPCacCodecEncoder_CreateInstance` | `0x7A450` | 209 | UnwindData |  |
| 86 | `CRDPCacVideoCodecForHardwareClient_CreateInstance` | `0x7A530` | 141 | UnwindData |  |
| 232 | `RdpX_DebugBreak` | `0x7F5B0` | 32,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0RdpEncodeBuffer@@QEAA@PEAVITSObjectPool@@@Z` | `0x87600` | 76 | UnwindData |  |
| 6 | `??0RdpGfxProtocolBaseDecoder@@IEAA@XZ` | `0x87910` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??1RdpGfxProtocolBaseDecoder@@IEAA@XZ` | `0x87940` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?CreateInstance@CRdpGfxCapsSet@@SAJPEAXKPEAPEAUIRdpGfxCapsSet@@@Z` | `0x87DD0` | 510 | UnwindData |  |
| 44 | `?IsSupportedVersion@CRdpGfxCaps@@SAHK@Z` | `0x889C0` | 34,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?XObjectId_RdpXHttpSession_CreateObject@@YA?AW4_XResult32@@PEAURdpXInterface@@IW4_XInterfaceId32@@PEAPEAX@Z` | `0x90F60` | 152 | UnwindData |  |
| 74 | `?XObjectId_RdpXInterfaceUriComponents_CreateObject@@YA?AW4_XResult32@@PEAURdpXInterface@@IW4_XInterfaceId32@@PEAPEAX@Z` | `0x91000` | 164 | UnwindData |  |
| 172 | `RDPCompress` | `0x927D0` | 84 | UnwindData |  |
| 175 | `RDPCompress_InitRecvContext` | `0x92830` | 141 | UnwindData |  |
| 176 | `RDPCompress_InitSendContext` | `0x928D0` | 153 | UnwindData |  |
| 177 | `RDPDeCompress_GetContextSize` | `0x92970` | 62 | UnwindData |  |
| 238 | `TRC_TraceBufferW` | `0x94830` | 317 | UnwindData |  |
| 14 | `?AlphaCompressor__CreateInstance@@YAJPEAPEAUIRdpImageCompressor@@@Z` | `0x949E0` | 2,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0NSCodecDecompressor@@QEAA@_N@Z` | `0x95220` | 157 | UnwindData |  |
| 22 | `?CreateInstance@NSCodecCompressor@@SA_N_N00EAEAV?$TCntPtr@VNSCodecCompressor@@@@@Z` | `0x959D0` | 113 | UnwindData |  |
| 25 | `?Decompress@NSCodecDecompressor@@QEAA_NPEBEIAEAVPixelMap@@@Z` | `0x95A50` | 1,244 | UnwindData |  |
| 46 | `?NSRunLengthDecode@@YAKPEBEKPEAEK@Z` | `0x96110` | 349 | UnwindData |  |
| 90 | `CRDPNsCodec_CreateInstance` | `0x96D30` | 619 | UnwindData |  |
| 23 | `?CreateInstance@PlanarCompressor@@SAJGGEHHHPEAPEAUIRdpImageCompressor@@@Z` | `0x97120` | 489 | UnwindData |  |
| 91 | `CRDPPlanarCompressor_CreateInstance` | `0x97CE0` | 531 | UnwindData |  |
| 78 | `BitmapCombinePlanes` | `0x98540` | 172 | UnwindData |  |
| 79 | `CAPAPI_AddCapSet` | `0xA63C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `CAPAPI_MergeCombinedCaps` | `0xA63E0` | 8,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `?CompressRdp8__CreateInstance@@YAJPEAPEAVIRdpPipeCompress@@I@Z` | `0xA8330` | 473 | UnwindData |  |
| 26 | `?DecompressRdp8__CreateInstance@@YAJPEAPEAVIRdpPipeDecompress@@@Z` | `0xA8A20` | 274 | UnwindData |  |
| 39 | `?HintCoconet__CreateInstance@@YAJPEAPEAVIRdpPipeCompressHintProvider@@@Z` | `0xA8CB0` | 243 | UnwindData |  |
| 240 | `TSCreateBaseServices` | `0xA9650` | 187 | UnwindData |  |
| 241 | `TSCreateCoreEvents` | `0xAC4C0` | 219 | UnwindData |  |
| 242 | `TSCreatePlatform` | `0xAD5C0` | 254 | UnwindData |  |
| 50 | `?ProcessAlignedData_SSE2@SSECBCHash2@@AEAAXPEBIIII@Z` | `0xAEFF0` | 765 | UnwindData |  |
| 77 | `ApplySobelFilterOnLum` | `0xAF300` | 491 | UnwindData |  |
| 95 | `DrawBox` | `0xAF720` | 127 | UnwindData |  |
| 96 | `DrawHLine` | `0xAF7B0` | 148 | UnwindData |  |
| 98 | `DrawVLine` | `0xAF850` | 175 | UnwindData |  |
| 236 | `SaveImageToFile` | `0xAF910` | 576 | UnwindData |  |
| 224 | `RdpIntersectRect` | `0xAFB60` | 84 | UnwindData |  |
| 108 | `MemMoveReverseAligned_SSE` | `0xAFBC0` | 339 | UnwindData |  |
| 103 | `GridBA_CreateInstance` | `0xB1D10` | 656 | UnwindData |  |
| 135 | `PAL_System_DebugBreak` | `0xB5B70` | 24 | UnwindData |  |
| 136 | `PAL_System_DebugOutput` | `0xB5B90` | 41 | UnwindData |  |
| 138 | `PAL_System_GetFIPSAlgorithmEnabled` | `0xB5BC0` | 366 | UnwindData |  |
| 140 | `PAL_System_GetModuleFilename` | `0xB5D40` | 316 | UnwindData |  |
| 154 | `PAL_System_Sleep` | `0xB5E90` | 5,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `PAL_System_AtomicExchange` | `0xB75F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `PAL_System_AtomicExchangeAdd` | `0xB7610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `PAL_System_AtomicExchangePointer` | `0xB7630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `PAL_System_CondReset` | `0xB7650` | 33 | UnwindData |  |
| 130 | `PAL_System_CritSecTryEnter` | `0xB7680` | 46 | UnwindData |  |
| 150 | `PAL_System_SemaphoreAcquire` | `0xB76C0` | 165 | UnwindData |  |
| 153 | `PAL_System_SingleCondWait` | `0xB7770` | 65 | UnwindData |  |
| 157 | `PAL_System_TimeGetCurrent` | `0xB77C0` | 111 | UnwindData |  |
| 160 | `PAL_System_TimeGetTickCount64` | `0xB7840` | 45 | UnwindData |  |
| 4 | `??0PipeETWEvents@@QEAA@XZ` | `0xB8180` | 414 | UnwindData |  |
| 27 | `?Enable@PipeETWEvents@@UEAAJKK@Z` | `0xB87A0` | 4,222 | UnwindData |  |
| 41 | `?Initialize@PipeETWEvents@@UEAAJPEAUIUnknown@@@Z` | `0xB9880` | 104 | UnwindData |  |
| 10 | `??1Evict@@QEAA@XZ` | `0xBA280` | 45 | UnwindData |  |
| 20 | `?CreateInstance@Evict@@SAJKKKKKPEAPEAV1@@Z` | `0xBA400` | 365 | UnwindData |  |
| 48 | `?ParkEntry@Evict@@QEAAXPEAU_SCORE_ENTRY@@@Z` | `0xBA990` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `?UnevictEntry@Evict@@QEAAXPEAU_SCORE_ENTRY@@@Z` | `0xBA9C0` | 66 | UnwindData |  |
| 21 | `?CreateInstance@HashTable@@SAJKKPEAPEAUIHashBucket@@@Z` | `0xBAAC0` | 540 | UnwindData |  |
| 29 | `?FakeSleep@PipelineClock@@QEAAX_K@Z` | `0xBB080` | 65 | UnwindData |  |
| 55 | `?RdpGfxProtocolServerEncoder_CreateInstance@@YAJPEAVIRdpEncoderIO@@PEAPEAVIRdpPipeProtocolEncoderEx@@@Z` | `0xBC450` | 500 | UnwindData |  |
| 8 | `??1CRDPCache@@UEAA@XZ` | `0xBCC70` | 87 | UnwindData |  |
| 83 | `CRDPBitmapRecorder_CreateInstance` | `0xBE1B0` | 17,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `RdpTiledSurface_CreateInstance` | `0xC2460` | 28,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `RDPAPI_GetLongCounter` | `0xC9550` | 1,079 | UnwindData |  |
| 181 | `RDPENCGDIHLP_FlipBitmapBitsInPlace` | `0xC9990` | 287 | UnwindData |  |
| 182 | `RDPENCGDIHLP_ValidatePointerParams` | `0xC9AC0` | 666 | UnwindData |  |
| 187 | `RDPENCHLP_GetInputDesktopName` | `0xC9EA0` | 340 | UnwindData |  |
| 188 | `RDPENCHLP_IsGreaterThanOrEqWin8` | `0xCA000` | 213 | UnwindData |  |
| 189 | `RDPENCHLP_IsSessionActive` | `0xCA0E0` | 350 | UnwindData |  |
| 190 | `RDPENCHLP_IsSessionRemote` | `0xCA250` | 264 | UnwindData |  |
| 191 | `RDPENCHLP_TraceWindowInfo` | `0xCA360` | 675 | UnwindData |  |
| 192 | `RDPENCORE_AddGlobalObject` | `0xCAEF0` | 13,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `RdpTaskScheduler_CreateInstance` | `0xCE210` | 544 | UnwindData |  |
| 226 | `RdpTaskTrigger_CreateInstance` | `0xCE440` | 620 | UnwindData |  |
| 245 | `ThreadPoolHandle_CreateInstance` | `0xCE6C0` | 462 | UnwindData |  |
| 2 | `??0CRDPENCONResolver@@QEAA@XZ` | `0xD63A0` | 257 | UnwindData |  |
| 9 | `??1CRDPENCONResolver@@QEAA@XZ` | `0xD64D0` | 249 | UnwindData |  |
| 12 | `?AddConnection@CRDPENCONResolver@@QEAAJPEAGKH@Z` | `0xD6650` | 411 | UnwindData |  |
| 35 | `?GetNext@CRDPENCONResolver@@QEAAHPEAPEAUsockaddr@@PEA_K@Z` | `0xD7310` | 426 | UnwindData |  |
| 64 | `?SortAddresses@CRDPENCONResolver@@QEAAJXZ` | `0xD7FC0` | 315 | UnwindData |  |
| 66 | `?StartEnum@CRDPENCONResolver@@QEAAIXZ` | `0xD8550` | 111 | UnwindData |  |
| 13 | `?AddPortMapping@CRDPENCConnectorStringSerializer@@UEAAJPEAGK@Z` | `0xD89A0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?GetPortMapping@CRDPENCConnectorStringDeserializer@@QEAAJKPEAPEAGPEAK@Z` | `0xD8BB0` | 443 | UnwindData |  |
| 42 | `?InitializeInstance@CRDPENCConnectorStringSerializer@@UEAAJXZ` | `0xD8D80` | 260 | UnwindData |  |
| 61 | `?SetConnectorId@CRDPENCConnectorStringSerializer@@UEAAJK@Z` | `0xD8F20` | 123 | UnwindData |  |
| 63 | `?SetSessionId@CRDPENCConnectorStringSerializer@@UEAAJI@Z` | `0xD8FB0` | 123 | UnwindData |  |
| 71 | `?XMLDeserialize@CRDPENCConnectorStringDeserializer@@QEAAJPEAG@Z` | `0xD9040` | 911 | UnwindData |  |
| 72 | `?XMLSerialize@CRDPENCConnectorStringSerializer@@UEAAJPEAPEAG@Z` | `0xD93E0` | 123 | UnwindData |  |
| 18 | `?CreateInstance@CRDPENCONPort@@SAJPEAUaddrinfo@@HPEAXPEAPEAV1@@Z` | `0xD9660` | 449 | UnwindData |  |
| 34 | `?GetNext@CRDPENCONIPHelper@@QEAAPEAU_SOCKET_ADDRESS@@XZ` | `0xDA5F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `?Initialize@CRDPENCONIPHelper@@QEAAJKHPEAG@Z` | `0xDA650` | 548 | UnwindData |  |
| 65 | `?StartEnum@CRDPENCONIPHelper@@QEAAHXZ` | `0xDA880` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `?Terminate@CRDPENCONIPHelper@@QEAAJXZ` | `0xDA8B0` | 63 | UnwindData |  |
| 203 | `RDPWSStreamConnector_CreateInstance` | `0x101860` | 559 | UnwindData |  |
| 56 | `?RdpPerfLoggerStaticInitialize@@YAXXZ` | `0x101AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?RdpPerfLoggerStaticTerminate@@YAXXZ` | `0x101AC0` | 56 | UnwindData |  |
| 54 | `RDPServerStackDiagnostics_LogConnectionQOEScore` | `0x102010` | 151 | UnwindData |  |
| 194 | `RDPServerStackDiagnostics_LogCheckpoint` | `0x1020B0` | 64 | UnwindData |  |
| 195 | `RDPServerStackDiagnostics_LogContext` | `0x102100` | 239 | UnwindData |  |
| 196 | `RDPServerStackDiagnostics_LogDisconnect` | `0x102200` | 190 | UnwindData |  |
| 197 | `RDPServerStackDiagnostics_LogFailure` | `0x1022D0` | 429 | UnwindData |  |
| 198 | `RDPServerStackDiagnostics_LogShortpathCheckpoint` | `0x102490` | 291 | UnwindData |  |
| 199 | `RDPServerStackDiagnostics_LogShortpathFallbackCheckpoint` | `0x1025C0` | 77 | UnwindData |  |
| 200 | `RDPServerStackDiagnostics_LogStringContext` | `0x102710` | 93 | UnwindData |  |
| 201 | `RDPServerStackDiagnostics_Register` | `0x102780` | 43 | UnwindData |  |
| 202 | `RDPServerStackDiagnostics_Unregister` | `0x1027C0` | 52 | UnwindData |  |
| 47 | `?PAL_System_Win32_IsRunningInAppContainer@@YAHXZ` | `0x103180` | 818 | UnwindData |  |
| 116 | `PAL_System_Beep` | `0x104A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `PAL_System_CredProtect` | `0x104AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `PAL_System_CredUnprotect` | `0x104AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `PAL_System_CryptDecryptLegacy` | `0x104AC0` | 15 | UnwindData |  |
| 132 | `PAL_System_CryptEncrypt` | `0x104AE0` | 15 | UnwindData |  |
| 133 | `PAL_System_CryptFree` | `0x104B00` | 120 | UnwindData |  |
| 137 | `PAL_System_GetComputerName` | `0x104B80` | 31 | UnwindData |  |
| 139 | `PAL_System_GetLocalSessionId` | `0x104BB0` | 174 | UnwindData |  |
| 141 | `PAL_System_GetNetworkStatus` | `0x104C70` | 179 | UnwindData |  |
| 143 | `PAL_System_GetWindowsProductId` | `0x104D30` | 160 | UnwindData |  |
| 147 | `PAL_System_NetworkMonitorInit` | `0x104DE0` | 367 | UnwindData |  |
| 148 | `PAL_System_NetworkMonitorTerminate` | `0x104F60` | 126 | UnwindData |  |
| 158 | `PAL_System_TimeGetDynamicTimeZoneInformation` | `0x104FF0` | 517 | UnwindData |  |
| 162 | `PAL_System_TimerCancel` | `0x105200` | 500 | UnwindData |  |
| 163 | `PAL_System_TimerDelete` | `0x105400` | 108 | UnwindData |  |
| 164 | `PAL_System_TimerInit` | `0x105480` | 350 | UnwindData |  |
| 165 | `PAL_System_TimerIsSet` | `0x1055F0` | 92 | UnwindData |  |
| 166 | `PAL_System_TimerSet` | `0x105660` | 581 | UnwindData |  |
| 121 | `PAL_System_ConvertToAndFromWideChar` | `0x105A10` | 101 | UnwindData |  |
| 122 | `PAL_System_CreateGuid` | `0x105A80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `PAL_System_CryptZeroMemory` | `0x105AA0` | 40 | UnwindData |  |
| 149 | `PAL_System_SecureZeroMemory` | `0x105AD0` | 21 | UnwindData |  |
| 161 | `PAL_System_TimeGetTimeZoneInformation` | `0x105AF0` | 348 | UnwindData |  |
| 167 | `PAL_System_WideCharToUnicode16` | `0x105C60` | 45,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `ICETransportContext_CreateInstance` | `0x110E50` | 3,492 | UnwindData |  |
| 94 | `DecryptDataEx` | `0x13C6E0` | 201 | UnwindData |  |
| 99 | `EncryptClientRandom` | `0x13C7B0` | 263 | UnwindData |  |
| 253 | `UnpackServerCert` | `0x13C8C0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `ValidateServerCert` | `0x13C980` | 343 | UnwindData |  |
| 105 | `MakeSessionKeys` | `0x13CDE0` | 461 | UnwindData |  |
| 254 | `UpdateSessionKey` | `0x13CFC0` | 132 | UnwindData |  |
| 244 | `TSRNG_GenerateRandomBits` | `0x13D050` | 25 | UnwindData |  |
| 204 | `RDP_HMACMD5Final` | `0x13D160` | 66 | UnwindData |  |
| 205 | `RDP_HMACMD5Init` | `0x13D1B0` | 181 | UnwindData |  |
| 211 | `RDP_RC4AllocKey` | `0x13D270` | 30 | UnwindData |  |
| 212 | `RDP_RC4FreeKey` | `0x13D2A0` | 52 | UnwindData |  |
| 213 | `RDP_RC4SetKey` | `0x13D2E0` | 198 | UnwindData |  |
| 214 | `RDP_RC4ZeroKey` | `0x13D3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `RDP_RsaBCryptDecryptPrivate` | `0x13D3D0` | 346 | UnwindData |  |
| 216 | `RDP_RsaBCryptGenerateRsaKeyPair` | `0x13D530` | 536 | UnwindData |  |
| 217 | `RDP_RsaBCryptPubKeyToBSafePubKey` | `0x13D750` | 272 | UnwindData |  |
| 218 | `RDP_RsaBSafeEncPublic` | `0x13D870` | 441 | UnwindData |  |
| 219 | `RDP_RsaGetPublicKeyDataLength` | `0x13DA30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `RDP_RsaGetPublicKeyLength` | `0x13DA50` | 118,850 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
