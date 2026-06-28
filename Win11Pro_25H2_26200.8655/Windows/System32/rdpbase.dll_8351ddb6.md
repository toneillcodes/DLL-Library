# Binary Specification: rdpbase.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rdpbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8351ddb6d1d86faf4ce17aac11e9b7fa232b5432bf693d183296ec1b0e8fe88a`
* **Total Exported Functions:** 255

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 49 | `?ProcessAlignedData_AVX@SSECBCHash2@@AEAAXPEBIIII@Z` | `0x6D30` | 754 | UnwindData |  |
| 246 | `TsAddRectsToRegion` | `0xDB20` | 84 | UnwindData |  |
| 111 | `PAL_System_AtomicDecrement` | `0x1D620` | 4,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `RdpX_DateTime_GetHighResolutionTimeSinceReboot` | `0x1E780` | 124 | UnwindData |  |
| 76 | `ApplyLuminanceFilter` | `0x21A70` | 89 | UnwindData |  |
| 16 | `?Compress@NSCodecCompressor@@QEAA_NAEBVPixelMap@@_NPEAEIAEAI@Z` | `0x22C40` | 667 | UnwindData |  |
| 106 | `MemCopyAligned_SSE` | `0x27BB0` | 93 | UnwindData |  |
| 185 | `RDPENCHLPWS_GetIPFromAddr` | `0x27FA0` | 270 | UnwindData |  |
| 129 | `PAL_System_CritSecTerminate` | `0x299E0` | 68 | UnwindData |  |
| 144 | `PAL_System_HandleFree` | `0x29A30` | 33 | UnwindData |  |
| 119 | `PAL_System_CondSignal` | `0x2AF80` | 33 | UnwindData |  |
| 120 | `PAL_System_CondWait` | `0x2C540` | 114 | UnwindData |  |
| 173 | `RDPCompressEx` | `0x30700` | 144 | UnwindData |  |
| 174 | `RDPCompress_GetContextSize` | `0x308F0` | 55 | UnwindData |  |
| 125 | `PAL_System_CritSecEnter` | `0x32E70` | 40 | UnwindData |  |
| 156 | `PAL_System_ThreadGetId` | `0x336F0` | 55 | UnwindData |  |
| 117 | `PAL_System_CondAlloc` | `0x33E00` | 76 | UnwindData |  |
| 151 | `PAL_System_SemaphoreAlloc` | `0x34A70` | 68 | UnwindData |  |
| 126 | `PAL_System_CritSecInit` | `0x34B00` | 241 | UnwindData |  |
| 168 | `RDPAPI_GetGenericCounter` | `0x35CA0` | 534 | UnwindData |  |
| 142 | `PAL_System_GetNumberOfProcessors` | `0x35F40` | 48 | UnwindData |  |
| 251 | `TsGetRegionRects` | `0x36A00` | 41 | UnwindData |  |
| 115 | `PAL_System_AtomicIncrement` | `0x36F30` | 12,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `?SearchCache@CRDPCache@@UEAAJIIPEAPEAUIUnknown@@PEAI@Z` | `0x39E70` | 362 | UnwindData |  |
| 70 | `?UpdateKeys@SSECBCHash2@@AEBAXXZ` | `0x3A060` | 151 | UnwindData |  |
| 60 | `?SetCacheEntry@CRDPCache@@UEAAJIIPEAUIUnknown@@PEAI@Z` | `0x3A2D0` | 318 | UnwindData |  |
| 102 | `GetSupportedSSELevel_SSE` | `0x3C4C0` | 39 | UnwindData |  |
| 128 | `PAL_System_CritSecLeave` | `0x3C4F0` | 40 | UnwindData |  |
| 109 | `PAL_System_AtomicCompareAndExchange` | `0x3C830` | 8,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `?ProcessUnalignedData_REG@SSECBCHash2@@AEAAXPEBIIII@Z` | `0x3E770` | 46 | UnwindData |  |
| 250 | `TsGetRegionRectCount` | `0x3E920` | 2,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `?ProcessAlignedData_SSE41@SSECBCHash2@@AEAAXPEBIIII@Z` | `0x3F3E0` | 376 | UnwindData |  |
| 97 | `DrawIconToPixelMap` | `0x3FC90` | 172 | UnwindData |  |
| 33 | `?GetMillisecondCount@PipelineClock@@QEAAIXZ` | `0x40E80` | 107 | UnwindData |  |
| 31 | `?GetInstance@PipelineClock@@SAAEAV1@XZ` | `0x40F00` | 104 | UnwindData |  |
| 7 | `??0SSECBCHash2@@QEAA@XZ` | `0x40F70` | 132 | UnwindData |  |
| 53 | `?PromoteEntry@Evict@@QEAAXKK@Z` | `0x42500` | 359 | UnwindData |  |
| 252 | `TsSetRegionFromRects` | `0x42C30` | 177 | UnwindData |  |
| 235 | `RgnlibBA_CreateInstance` | `0x4A840` | 423 | UnwindData |  |
| 247 | `TsCreateRegion` | `0x4AB00` | 611 | UnwindData |  |
| 37 | `?GetTickCount@PipelineClock@@QEAAIXZ` | `0x4BC80` | 47 | UnwindData |  |
| 248 | `TsDestroyRegion` | `0x4BE50` | 94 | UnwindData |  |
| 159 | `PAL_System_TimeGetTickCount` | `0x4E980` | 55 | UnwindData |  |
| 38 | `?GetTimeHNS@PipelineClock@@QEAA_JXZ` | `0x50310` | 115 | UnwindData |  |
| 28 | `?EvictEntry@Evict@@QEAAPEAU_SCORE_ENTRY@@XZ` | `0x50770` | 314 | UnwindData |  |
| 101 | `ExpandRectForSSE` | `0x515A0` | 4,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `?InsertEntry@Evict@@QEAAXPEAU_SCORE_ENTRY@@K@Z` | `0x525F0` | 170 | UnwindData |  |
| 183 | `RDPENCHLPREG_ReadValueDWORD` | `0x52AD0` | 289 | UnwindData |  |
| 249 | `TsGetRegionBoundingBox` | `0x561E0` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `EncryptData` | `0x566C0` | 96 | UnwindData |  |
| 93 | `DecryptData` | `0x56730` | 175 | UnwindData |  |
| 210 | `RDP_RC4` | `0x567F0` | 73 | UnwindData |  |
| 208 | `RDP_MD5Init` | `0x56B10` | 168 | UnwindData |  |
| 222 | `RDP_SHAInit` | `0x56BC0` | 161 | UnwindData |  |
| 75 | `?XObjectId_RdpXSecFilterServer_CreateObject@@YA?AW4_XResult32@@PEAURdpXInterface@@IW4_XInterfaceId32@@PEAPEAX@Z` | `0x56EF0` | 153 | UnwindData |  |
| 237 | `SubtractRects` | `0x5A040` | 511 | UnwindData |  |
| 32 | `?GetMillisecondCount64@PipelineClock@@QEAA_KXZ` | `0x5A3C0` | 42 | UnwindData |  |
| 169 | `RDPAPI_GetGlobalObject` | `0x5AD30` | 2,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `?Reset@CRDPCache@@UEAAJI@Z` | `0x5B830` | 566 | UnwindData |  |
| 206 | `RDP_HMACMD5Update` | `0x5C750` | 66 | UnwindData |  |
| 209 | `RDP_MD5Update` | `0x5C750` | 66 | UnwindData |  |
| 145 | `PAL_System_MemAlloc` | `0x5C850` | 2,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `RDP_SHAUpdate` | `0x5D040` | 68 | UnwindData |  |
| 62 | `?SetDecodeBuffer@RdpGfxProtocolBaseDecoder@@IEAAXPEBEI@Z` | `0x5D420` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `TSDbgAssertThread` | `0x5D6C0` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `CAPAPI_GetCapSet` | `0x5DB90` | 73 | UnwindData |  |
| 30 | `?GetFreeEntry@Evict@@QEAAPEAU_SCORE_ENTRY@@XZ` | `0x5DC50` | 83 | UnwindData |  |
| 92 | `CRdpFIPSEncryption_CreateInstance` | `0x5DDB0` | 495 | UnwindData |  |
| 24 | `?CreateInstance@RdpEncodeBuffer@@SAJPEAVRdpEncodeBufferPool@@KPEAPEAV1@@Z` | `0x5F490` | 262 | UnwindData |  |
| 207 | `RDP_MD5Final` | `0x60900` | 70 | UnwindData |  |
| 230 | `RdpX_AtomicIncrement32` | `0x60D40` | 4,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `RdpUnionRect` | `0x61F50` | 86 | UnwindData |  |
| 229 | `RdpX_AtomicDecrement32` | `0x62830` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `PAL_System_AtomicCompareAndExchangePointer` | `0x62870` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `RDP_SHAFinal` | `0x628E0` | 66 | UnwindData |  |
| 178 | `RDPDecompress` | `0x62EA0` | 144 | UnwindData |  |
| 146 | `PAL_System_MemFree` | `0x63BF0` | 8,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `TSFree` | `0x63BF0` | 8,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `PAL_System_CritSecIsLockedByCurrentThread` | `0x65D30` | 56 | UnwindData |  |
| 186 | `RDPENCHLPWS_GetPortFromAddr` | `0x66210` | 71 | UnwindData |  |
| 171 | `RDPBASE_CreateInstance` | `0x68730` | 8,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `RDPENCGDIHLP_FlipBitmapBits` | `0x6A7A0` | 197 | UnwindData |  |
| 81 | `CAPAPI_InitializeCombinedCaps` | `0x6B050` | 107 | UnwindData |  |
| 107 | `MemEqual` | `0x6C210` | 177 | UnwindData |  |
| 193 | `RDPServerStackDiagnostics_GetSymbolicNameFromCode` | `0x6C2D0` | 17,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?ClearCache@CRDPCache@@UEAAJXZ` | `0x70630` | 203 | UnwindData |  |
| 179 | `RDPENCDirectConnector_CreateInstance` | `0x70D30` | 643 | UnwindData |  |
| 1 | `??0CRDPCache@@QEAA@XZ` | `0x715A0` | 169 | UnwindData |  |
| 239 | `TSAlloc` | `0x72430` | 4,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `CRDPCacCodec_CreateInstance` | `0x73520` | 276 | UnwindData |  |
| 89 | `CRDPENCGfxEncoder_CreateInstance` | `0x73ED0` | 448 | UnwindData |  |
| 87 | `CRDPCacVideoCodec_CreateInstance` | `0x75F90` | 23 | UnwindData |  |
| 233 | `RdpX_GetActivityIdPrefix` | `0x760F0` | 81 | UnwindData |  |
| 152 | `PAL_System_SemaphoreRelease` | `0x76BC0` | 40 | UnwindData |  |
| 184 | `RDPENCHLPWSErr2Hr` | `0x76D60` | 34 | UnwindData |  |
| 88 | `CRDPCaps_CreateInstance` | `0x76EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `?IsTestMode@PipelineClock@@QEAA_NXZ` | `0x76EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `RdpX_Threading_CreateCriticalSection` | `0x76F00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `PAL_System_SwitchToThread` | `0x76F30` | 16,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `CRDPCacCodecEncoder_CreateInstance` | `0x7B000` | 209 | UnwindData |  |
| 86 | `CRDPCacVideoCodecForHardwareClient_CreateInstance` | `0x7B0E0` | 141 | UnwindData |  |
| 232 | `RdpX_DebugBreak` | `0x80140` | 41,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0RdpEncodeBuffer@@QEAA@PEAVITSObjectPool@@@Z` | `0x8A510` | 76 | UnwindData |  |
| 6 | `??0RdpGfxProtocolBaseDecoder@@IEAA@XZ` | `0x8A820` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??1RdpGfxProtocolBaseDecoder@@IEAA@XZ` | `0x8A850` | 1,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?CreateInstance@CRdpGfxCapsSet@@SAJPEAXKPEAPEAUIRdpGfxCapsSet@@@Z` | `0x8ACE0` | 510 | UnwindData |  |
| 44 | `?IsSupportedVersion@CRdpGfxCaps@@SAHK@Z` | `0x8B8D0` | 34,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?XObjectId_RdpXHttpSession_CreateObject@@YA?AW4_XResult32@@PEAURdpXInterface@@IW4_XInterfaceId32@@PEAPEAX@Z` | `0x93E40` | 152 | UnwindData |  |
| 74 | `?XObjectId_RdpXInterfaceUriComponents_CreateObject@@YA?AW4_XResult32@@PEAURdpXInterface@@IW4_XInterfaceId32@@PEAPEAX@Z` | `0x93EE0` | 164 | UnwindData |  |
| 172 | `RDPCompress` | `0x956A0` | 84 | UnwindData |  |
| 175 | `RDPCompress_InitRecvContext` | `0x95700` | 141 | UnwindData |  |
| 176 | `RDPCompress_InitSendContext` | `0x957A0` | 153 | UnwindData |  |
| 177 | `RDPDeCompress_GetContextSize` | `0x95840` | 62 | UnwindData |  |
| 238 | `TRC_TraceBufferW` | `0x97700` | 317 | UnwindData |  |
| 14 | `?AlphaCompressor__CreateInstance@@YAJPEAPEAUIRdpImageCompressor@@@Z` | `0x978B0` | 2,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0NSCodecDecompressor@@QEAA@_N@Z` | `0x980F0` | 157 | UnwindData |  |
| 22 | `?CreateInstance@NSCodecCompressor@@SA_N_N00EAEAV?$TCntPtr@VNSCodecCompressor@@@@@Z` | `0x98880` | 113 | UnwindData |  |
| 25 | `?Decompress@NSCodecDecompressor@@QEAA_NPEBEIAEAVPixelMap@@@Z` | `0x98900` | 1,244 | UnwindData |  |
| 46 | `?NSRunLengthDecode@@YAKPEBEKPEAEK@Z` | `0x98FC0` | 349 | UnwindData |  |
| 90 | `CRDPNsCodec_CreateInstance` | `0x99BE0` | 619 | UnwindData |  |
| 23 | `?CreateInstance@PlanarCompressor@@SAJGGEHHHPEAPEAUIRdpImageCompressor@@@Z` | `0x99FD0` | 489 | UnwindData |  |
| 91 | `CRDPPlanarCompressor_CreateInstance` | `0x9AB90` | 531 | UnwindData |  |
| 78 | `BitmapCombinePlanes` | `0x9B3F0` | 172 | UnwindData |  |
| 79 | `CAPAPI_AddCapSet` | `0xA9270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `CAPAPI_MergeCombinedCaps` | `0xA9290` | 8,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `?CompressRdp8__CreateInstance@@YAJPEAPEAVIRdpPipeCompress@@I@Z` | `0xAB1E0` | 473 | UnwindData |  |
| 26 | `?DecompressRdp8__CreateInstance@@YAJPEAPEAVIRdpPipeDecompress@@@Z` | `0xAB8D0` | 274 | UnwindData |  |
| 39 | `?HintCoconet__CreateInstance@@YAJPEAPEAVIRdpPipeCompressHintProvider@@@Z` | `0xABB60` | 243 | UnwindData |  |
| 240 | `TSCreateBaseServices` | `0xAC500` | 187 | UnwindData |  |
| 241 | `TSCreateCoreEvents` | `0xAF370` | 219 | UnwindData |  |
| 242 | `TSCreatePlatform` | `0xB0470` | 254 | UnwindData |  |
| 50 | `?ProcessAlignedData_SSE2@SSECBCHash2@@AEAAXPEBIIII@Z` | `0xB1EA0` | 765 | UnwindData |  |
| 77 | `ApplySobelFilterOnLum` | `0xB21B0` | 491 | UnwindData |  |
| 95 | `DrawBox` | `0xB25D0` | 127 | UnwindData |  |
| 96 | `DrawHLine` | `0xB2660` | 148 | UnwindData |  |
| 98 | `DrawVLine` | `0xB2700` | 175 | UnwindData |  |
| 236 | `SaveImageToFile` | `0xB27C0` | 533 | UnwindData |  |
| 224 | `RdpIntersectRect` | `0xB29E0` | 84 | UnwindData |  |
| 108 | `MemMoveReverseAligned_SSE` | `0xB2A40` | 339 | UnwindData |  |
| 103 | `GridBA_CreateInstance` | `0xB4B90` | 656 | UnwindData |  |
| 135 | `PAL_System_DebugBreak` | `0xB7390` | 24 | UnwindData |  |
| 136 | `PAL_System_DebugOutput` | `0xB73B0` | 41 | UnwindData |  |
| 138 | `PAL_System_GetFIPSAlgorithmEnabled` | `0xB73E0` | 366 | UnwindData |  |
| 140 | `PAL_System_GetModuleFilename` | `0xB7560` | 316 | UnwindData |  |
| 154 | `PAL_System_Sleep` | `0xB76B0` | 5,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `PAL_System_AtomicExchange` | `0xB8E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `PAL_System_AtomicExchangeAdd` | `0xB8E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `PAL_System_AtomicExchangePointer` | `0xB8E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `PAL_System_CondReset` | `0xB8E70` | 33 | UnwindData |  |
| 130 | `PAL_System_CritSecTryEnter` | `0xB8EA0` | 46 | UnwindData |  |
| 150 | `PAL_System_SemaphoreAcquire` | `0xB8EE0` | 165 | UnwindData |  |
| 153 | `PAL_System_SingleCondWait` | `0xB8F90` | 65 | UnwindData |  |
| 157 | `PAL_System_TimeGetCurrent` | `0xB8FE0` | 111 | UnwindData |  |
| 160 | `PAL_System_TimeGetTickCount64` | `0xB9060` | 45 | UnwindData |  |
| 4 | `??0PipeETWEvents@@QEAA@XZ` | `0xB99C0` | 414 | UnwindData |  |
| 27 | `?Enable@PipeETWEvents@@UEAAJKK@Z` | `0xB9FE0` | 4,222 | UnwindData |  |
| 41 | `?Initialize@PipeETWEvents@@UEAAJPEAUIUnknown@@@Z` | `0xBB0C0` | 104 | UnwindData |  |
| 10 | `??1Evict@@QEAA@XZ` | `0xBBAC0` | 45 | UnwindData |  |
| 20 | `?CreateInstance@Evict@@SAJKKKKKPEAPEAV1@@Z` | `0xBBC40` | 365 | UnwindData |  |
| 48 | `?ParkEntry@Evict@@QEAAXPEAU_SCORE_ENTRY@@@Z` | `0xBC1D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `?UnevictEntry@Evict@@QEAAXPEAU_SCORE_ENTRY@@@Z` | `0xBC200` | 66 | UnwindData |  |
| 21 | `?CreateInstance@HashTable@@SAJKKPEAPEAUIHashBucket@@@Z` | `0xBC300` | 540 | UnwindData |  |
| 29 | `?FakeSleep@PipelineClock@@QEAAX_K@Z` | `0xBC8C0` | 65 | UnwindData |  |
| 55 | `?RdpGfxProtocolServerEncoder_CreateInstance@@YAJPEAVIRdpEncoderIO@@PEAPEAVIRdpPipeProtocolEncoderEx@@@Z` | `0xBDC90` | 500 | UnwindData |  |
| 8 | `??1CRDPCache@@UEAA@XZ` | `0xBE4B0` | 87 | UnwindData |  |
| 83 | `CRDPBitmapRecorder_CreateInstance` | `0xBF9F0` | 17,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `RdpTiledSurface_CreateInstance` | `0xC3CA0` | 28,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `RDPAPI_GetLongCounter` | `0xCAD90` | 1,079 | UnwindData |  |
| 181 | `RDPENCGDIHLP_FlipBitmapBitsInPlace` | `0xCB1D0` | 287 | UnwindData |  |
| 182 | `RDPENCGDIHLP_ValidatePointerParams` | `0xCB300` | 666 | UnwindData |  |
| 187 | `RDPENCHLP_GetInputDesktopName` | `0xCB6E0` | 340 | UnwindData |  |
| 188 | `RDPENCHLP_IsGreaterThanOrEqWin8` | `0xCB840` | 213 | UnwindData |  |
| 189 | `RDPENCHLP_IsSessionActive` | `0xCB920` | 350 | UnwindData |  |
| 190 | `RDPENCHLP_IsSessionRemote` | `0xCBA90` | 264 | UnwindData |  |
| 191 | `RDPENCHLP_TraceWindowInfo` | `0xCBBA0` | 675 | UnwindData |  |
| 192 | `RDPENCORE_AddGlobalObject` | `0xCC730` | 13,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `RdpTaskScheduler_CreateInstance` | `0xCFA50` | 544 | UnwindData |  |
| 226 | `RdpTaskTrigger_CreateInstance` | `0xCFC80` | 620 | UnwindData |  |
| 245 | `ThreadPoolHandle_CreateInstance` | `0xCFF00` | 462 | UnwindData |  |
| 2 | `??0CRDPENCONResolver@@QEAA@XZ` | `0xD7BD0` | 257 | UnwindData |  |
| 9 | `??1CRDPENCONResolver@@QEAA@XZ` | `0xD7D00` | 249 | UnwindData |  |
| 12 | `?AddConnection@CRDPENCONResolver@@QEAAJPEAGKH@Z` | `0xD7E80` | 404 | UnwindData |  |
| 35 | `?GetNext@CRDPENCONResolver@@QEAAHPEAPEAUsockaddr@@PEA_K@Z` | `0xD8B30` | 426 | UnwindData |  |
| 64 | `?SortAddresses@CRDPENCONResolver@@QEAAJXZ` | `0xD97E0` | 315 | UnwindData |  |
| 66 | `?StartEnum@CRDPENCONResolver@@QEAAIXZ` | `0xD9D70` | 111 | UnwindData |  |
| 13 | `?AddPortMapping@CRDPENCConnectorStringSerializer@@UEAAJPEAGK@Z` | `0xDA1C0` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?GetPortMapping@CRDPENCConnectorStringDeserializer@@QEAAJKPEAPEAGPEAK@Z` | `0xDA3D0` | 443 | UnwindData |  |
| 42 | `?InitializeInstance@CRDPENCConnectorStringSerializer@@UEAAJXZ` | `0xDA5A0` | 260 | UnwindData |  |
| 61 | `?SetConnectorId@CRDPENCConnectorStringSerializer@@UEAAJK@Z` | `0xDA740` | 123 | UnwindData |  |
| 63 | `?SetSessionId@CRDPENCConnectorStringSerializer@@UEAAJI@Z` | `0xDA7D0` | 123 | UnwindData |  |
| 71 | `?XMLDeserialize@CRDPENCConnectorStringDeserializer@@QEAAJPEAG@Z` | `0xDA860` | 911 | UnwindData |  |
| 72 | `?XMLSerialize@CRDPENCConnectorStringSerializer@@UEAAJPEAPEAG@Z` | `0xDAC00` | 123 | UnwindData |  |
| 18 | `?CreateInstance@CRDPENCONPort@@SAJPEAUaddrinfo@@HPEAXPEAPEAV1@@Z` | `0xDAE80` | 449 | UnwindData |  |
| 34 | `?GetNext@CRDPENCONIPHelper@@QEAAPEAU_SOCKET_ADDRESS@@XZ` | `0xDBE10` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `?Initialize@CRDPENCONIPHelper@@QEAAJKHPEAG@Z` | `0xDBE70` | 548 | UnwindData |  |
| 65 | `?StartEnum@CRDPENCONIPHelper@@QEAAHXZ` | `0xDC0A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `?Terminate@CRDPENCONIPHelper@@QEAAJXZ` | `0xDC0D0` | 63 | UnwindData |  |
| 203 | `RDPWSStreamConnector_CreateInstance` | `0x102D60` | 559 | UnwindData |  |
| 56 | `?RdpPerfLoggerStaticInitialize@@YAXXZ` | `0x102FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?RdpPerfLoggerStaticTerminate@@YAXXZ` | `0x102FC0` | 56 | UnwindData |  |
| 54 | `RDPServerStackDiagnostics_LogConnectionQOEScore` | `0x103510` | 151 | UnwindData |  |
| 194 | `RDPServerStackDiagnostics_LogCheckpoint` | `0x1035B0` | 64 | UnwindData |  |
| 195 | `RDPServerStackDiagnostics_LogContext` | `0x103600` | 239 | UnwindData |  |
| 196 | `RDPServerStackDiagnostics_LogDisconnect` | `0x103700` | 190 | UnwindData |  |
| 197 | `RDPServerStackDiagnostics_LogFailure` | `0x1037D0` | 422 | UnwindData |  |
| 198 | `RDPServerStackDiagnostics_LogShortpathCheckpoint` | `0x103980` | 291 | UnwindData |  |
| 199 | `RDPServerStackDiagnostics_LogShortpathFallbackCheckpoint` | `0x103AB0` | 77 | UnwindData |  |
| 200 | `RDPServerStackDiagnostics_LogStringContext` | `0x103C00` | 93 | UnwindData |  |
| 201 | `RDPServerStackDiagnostics_Register` | `0x103C70` | 43 | UnwindData |  |
| 202 | `RDPServerStackDiagnostics_Unregister` | `0x103CB0` | 52 | UnwindData |  |
| 47 | `?PAL_System_Win32_IsRunningInAppContainer@@YAHXZ` | `0x104670` | 818 | UnwindData |  |
| 116 | `PAL_System_Beep` | `0x105F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `PAL_System_CredProtect` | `0x105F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `PAL_System_CredUnprotect` | `0x105FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `PAL_System_CryptDecryptLegacy` | `0x105FB0` | 15 | UnwindData |  |
| 132 | `PAL_System_CryptEncrypt` | `0x105FD0` | 15 | UnwindData |  |
| 133 | `PAL_System_CryptFree` | `0x105FF0` | 120 | UnwindData |  |
| 137 | `PAL_System_GetComputerName` | `0x106070` | 31 | UnwindData |  |
| 139 | `PAL_System_GetLocalSessionId` | `0x1060A0` | 174 | UnwindData |  |
| 141 | `PAL_System_GetNetworkStatus` | `0x106160` | 179 | UnwindData |  |
| 143 | `PAL_System_GetWindowsProductId` | `0x106220` | 160 | UnwindData |  |
| 147 | `PAL_System_NetworkMonitorInit` | `0x1062D0` | 367 | UnwindData |  |
| 148 | `PAL_System_NetworkMonitorTerminate` | `0x106450` | 126 | UnwindData |  |
| 158 | `PAL_System_TimeGetDynamicTimeZoneInformation` | `0x1064E0` | 517 | UnwindData |  |
| 162 | `PAL_System_TimerCancel` | `0x1066F0` | 500 | UnwindData |  |
| 163 | `PAL_System_TimerDelete` | `0x1068F0` | 108 | UnwindData |  |
| 164 | `PAL_System_TimerInit` | `0x106970` | 350 | UnwindData |  |
| 165 | `PAL_System_TimerIsSet` | `0x106AE0` | 92 | UnwindData |  |
| 166 | `PAL_System_TimerSet` | `0x106B50` | 581 | UnwindData |  |
| 121 | `PAL_System_ConvertToAndFromWideChar` | `0x106F00` | 101 | UnwindData |  |
| 122 | `PAL_System_CreateGuid` | `0x106F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `PAL_System_CryptZeroMemory` | `0x106F90` | 40 | UnwindData |  |
| 149 | `PAL_System_SecureZeroMemory` | `0x106FC0` | 21 | UnwindData |  |
| 161 | `PAL_System_TimeGetTimeZoneInformation` | `0x106FE0` | 348 | UnwindData |  |
| 167 | `PAL_System_WideCharToUnicode16` | `0x107150` | 45,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `ICETransportContext_CreateInstance` | `0x1122F0` | 3,492 | UnwindData |  |
| 94 | `DecryptDataEx` | `0x13E0E0` | 201 | UnwindData |  |
| 99 | `EncryptClientRandom` | `0x13E420` | 263 | UnwindData |  |
| 253 | `UnpackServerCert` | `0x13E530` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `ValidateServerCert` | `0x13E5F0` | 435 | UnwindData |  |
| 105 | `MakeSessionKeys` | `0x13EAB0` | 461 | UnwindData |  |
| 254 | `UpdateSessionKey` | `0x13EC90` | 132 | UnwindData |  |
| 244 | `TSRNG_GenerateRandomBits` | `0x13ED20` | 25 | UnwindData |  |
| 204 | `RDP_HMACMD5Final` | `0x13EE30` | 66 | UnwindData |  |
| 205 | `RDP_HMACMD5Init` | `0x13EE80` | 181 | UnwindData |  |
| 211 | `RDP_RC4AllocKey` | `0x13EF40` | 30 | UnwindData |  |
| 212 | `RDP_RC4FreeKey` | `0x13EF70` | 52 | UnwindData |  |
| 213 | `RDP_RC4SetKey` | `0x13EFB0` | 198 | UnwindData |  |
| 214 | `RDP_RC4ZeroKey` | `0x13F080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `RDP_RsaBCryptDecryptPrivate` | `0x13F0A0` | 346 | UnwindData |  |
| 216 | `RDP_RsaBCryptGenerateRsaKeyPair` | `0x13F200` | 536 | UnwindData |  |
| 217 | `RDP_RsaBCryptPubKeyToBSafePubKey` | `0x13F420` | 272 | UnwindData |  |
| 218 | `RDP_RsaBSafeEncPublic` | `0x13F540` | 492 | UnwindData |  |
| 219 | `RDP_RsaGetPublicKeyDataLength` | `0x13F740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `RDP_RsaGetPublicKeyLength` | `0x13F760` | 120,364 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
