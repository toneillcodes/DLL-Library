# Binary Specification: mfplat.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mfplat.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0899b66893865ad40cbae7079dbdd34417fc9f92843303d67138a3f567c12e76`
* **Total Exported Functions:** 234

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `MFAddPeriodicCallback` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqAddPeriodicCallback` |
| 17 | `MFAllocateSerialWorkQueue` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqAllocateSerialWorkQueue` |
| 19 | `MFAllocateWorkQueueEx` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqAllocateWorkQueue` |
| 25 | `MFBeginRegisterWorkQueueWithMMCSSEx` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqBeginRegisterWorkQueueWithMMCSS` |
| 26 | `MFBeginUnregisterWorkQueueWithMMCSS` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqBeginUnregisterWorkQueueWithMMCSS` |
| 35 | `MFCancelWorkItem` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqCancelWorkItem` |
| 51 | `MFCreateAsyncResult` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqCreateAsyncResult` |
| 133 | `MFEndRegisterWorkQueueWithMMCSS` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqEndRegisterWorkQueueWithMMCSS` |
| 134 | `MFEndUnregisterWorkQueueWithMMCSS` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqEndUnregisterWorkQueueWithMMCSS` |
| 158 | `MFGetWorkQueueMMCSSClass` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqGetWorkQueueMMCSSClass` |
| 159 | `MFGetWorkQueueMMCSSPriority` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqGetWorkQueueMMCSSPriority` |
| 160 | `MFGetWorkQueueMMCSSTaskId` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqGetWorkQueueMMCSSTaskId` |
| 177 | `MFInvokeCallback` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqInvokeCallback` |
| 182 | `MFJoinWorkQueue` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqJoinWorkQueue` |
| 184 | `MFLockPlatform` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqLockPlatform` |
| 185 | `MFLockSharedWorkQueue` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqLockSharedWorkQueue` |
| 186 | `MFLockWorkQueue` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqLockWorkQueue` |
| 189 | `MFPutWaitingWorkItem` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqPutWaitingWorkItem` |
| 196 | `MFRegisterPlatformWithMMCSS` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqRegisterPlatformWithMMCSS` |
| 197 | `MFRemovePeriodicCallback` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqRemovePeriodicCallback` |
| 199 | `MFScheduleWorkItemEx` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqScheduleWorkItem` |
| 223 | `MFUnjoinWorkQueue` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqUnjoinWorkQueue` |
| 225 | `MFUnlockPlatform` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqUnlockPlatform` |
| 226 | `MFUnlockWorkQueue` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqUnlockWorkQueue` |
| 227 | `MFUnregisterPlatformFromMMCSS` | `0x0` | - | Forwarded | Forwarded to: `RTWorkQ.RtwqUnregisterPlatformFromMMCSS` |
| 221 | `MFTraceError` | `0x42B0` | 5,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `MFTraceFuncEnter` | `0x42B0` | 5,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `MFllMulDiv` | `0x58C0` | 1,286 | UnwindData |  |
| 76 | `MFCreateMediaEvent` | `0x8810` | 59 | UnwindData |  |
| 31 | `MFCallStackTracingRestoreSnapshot` | `0xC680` | 8,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `MFCallStackTracingTakeSnapshot` | `0xE810` | 3,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `MFCreateTrackedSample` | `0xF490` | 109 | UnwindData |  |
| 208 | `MFSplitSample` | `0xFBE0` | 2,450 | UnwindData |  |
| 98 | `MFCreateSample` | `0x10580` | 136 | UnwindData |  |
| 191 | `MFPutWorkItem2` | `0x1AAC0` | 372 | UnwindData |  |
| 147 | `MFGetMFTMerit` | `0x1DA40` | 48,645 | UnwindData |  |
| 12 | `CreatePropertyStore` | `0x29850` | 31 | UnwindData |  |
| 52 | `MFCreateAttributes` | `0x2AF20` | 477 | UnwindData |  |
| 127 | `MFDeserializeAttributesFromStream` | `0x2B6B0` | 738 | UnwindData |  |
| 166 | `MFInitAttributesFromBlob` | `0x2BC90` | 72 | UnwindData |  |
| 214 | `MFTGetInfo` | `0x2C090` | 631 | UnwindData |  |
| 106 | `MFCreateStreamDescriptor` | `0x2D820` | 233 | UnwindData |  |
| 153 | `MFGetSupportedMimeTypes` | `0x2ECC0` | 75 | UnwindData |  |
| 13 | `DestroyPropVariant` | `0x32CA0` | 4,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `MFBeginCreateFile` | `0x33FC0` | 1,003 | UnwindData |  |
| 190 | `MFPutWorkItem` | `0x35790` | 345 | UnwindData |  |
| 114 | `MFCreateURLFromPath` | `0x358F0` | 78 | UnwindData |  |
| 69 | `MFCreateMFByteStreamOnIStreamWithFlags` | `0x37CC0` | 879 | UnwindData |  |
| 110 | `MFCreateTelemetrySession` | `0x38C20` | 42 | UnwindData |  |
| 10 | `CopyPropVariant` | `0x3BAE0` | 86 | UnwindData |  |
| 93 | `MFCreatePathFromURL` | `0x42AE0` | 81 | UnwindData |  |
| 198 | `MFScheduleWorkItem` | `0x441E0` | 366 | UnwindData |  |
| 135 | `MFFrameRateToAverageTimePerFrame` | `0x48EE0` | 17 | UnwindData |  |
| 126 | `MFCreateWaveFormatExFromMFMediaType` | `0x490C0` | 1,288 | UnwindData |  |
| 48 | `MFCreateAMMediaTypeFromMFMediaType` | `0x495F0` | 178 | UnwindData |  |
| 165 | `MFInitAMMediaTypeFromMFMediaType` | `0x496B0` | 2,659 | UnwindData |  |
| 15 | `GetD3DFormatFromMFSubtype` | `0x4AF30` | 146 | UnwindData |  |
| 14 | `GetAMSubtypeFromD3DFormat` | `0x4AFD0` | 126 | UnwindData |  |
| 170 | `MFInitMediaTypeFromMPEG2VideoInfo` | `0x4BA90` | 294 | UnwindData |  |
| 167 | `MFInitMediaTypeFromAMMediaType` | `0x4BBC0` | 902 | UnwindData |  |
| 171 | `MFInitMediaTypeFromVideoInfoHeader` | `0x4BF50` | 175 | UnwindData |  |
| 172 | `MFInitMediaTypeFromVideoInfoHeader2` | `0x4C010` | 973 | UnwindData |  |
| 121 | `MFCreateVideoMediaTypeFromVideoInfoHeader` | `0x4D230` | 269 | UnwindData |  |
| 173 | `MFInitMediaTypeFromWaveFormatEx` | `0x4DBF0` | 995 | UnwindData |  |
| 84 | `MFCreateMediaTypeFromRepresentation` | `0x4F6D0` | 1,607 | UnwindData |  |
| 120 | `MFCreateVideoMediaTypeFromSubtype` | `0x4FD20` | 166 | UnwindData |  |
| 117 | `MFCreateVideoMediaType` | `0x4FDD0` | 150 | UnwindData |  |
| 82 | `MFCreateMediaType` | `0x4FF00` | 164 | UnwindData |  |
| 168 | `MFInitMediaTypeFromMFVideoFormat` | `0x50070` | 3,602 | UnwindData |  |
| 83 | `MFCreateMediaTypeFromProperties` | `0x50F00` | 2,907 | UnwindData |  |
| 74 | `MFCreateMediaBufferFromMediaType` | `0x57770` | 41 | UnwindData |  |
| 73 | `MFCreateMFVideoFormatFromMFMediaType` | `0x5A280` | 1,582 | UnwindData |  |
| 157 | `MFGetUncompressedVideoFormat` | `0x5A8C0` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `MFCreateDXGISurfaceBuffer` | `0x5ADA0` | 2,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `MFGetStrideForBitmapInfoHeader` | `0x5B920` | 52 | UnwindData |  |
| 75 | `MFCreateMediaBufferWrapper` | `0x5BAD0` | 876 | UnwindData |  |
| 49 | `MFCreateAlignedMemoryBuffer` | `0x5BE50` | 678 | UnwindData |  |
| 85 | `MFCreateMemoryBuffer` | `0x5C100` | 650 | UnwindData |  |
| 45 | `MFCopyImage` | `0x5EF10` | 664 | UnwindData |  |
| 155 | `MFGetSystemTime` | `0x63ED0` | 80 | UnwindData |  |
| 77 | `MFCreateMediaEventResult` | `0x64700` | 303 | UnwindData |  |
| 200 | `MFSerializeAttributesToStream` | `0x66590` | 738 | UnwindData |  |
| 138 | `MFGetAttributesAsBlob` | `0x66DA0` | 99 | UnwindData |  |
| 230 | `MFWrapMediaType` | `0x68290` | 999 | UnwindData |  |
| 139 | `MFGetAttributesAsBlobSize` | `0x68680` | 399 | UnwindData |  |
| 95 | `MFCreatePropertiesFromMediaType` | `0x6B790` | 3,911 | UnwindData |  |
| 38 | `MFCombineSamples` | `0x72A90` | 1,197 | UnwindData |  |
| 54 | `MFCreateByteStreamHandlerAppServiceActivate` | `0x732B0` | 247 | UnwindData |  |
| 81 | `MFCreateMediaExtensionInprocActivate` | `0x73A30` | 249 | UnwindData |  |
| 80 | `MFCreateMediaExtensionAppServiceActivate` | `0x73B30` | 244 | UnwindData |  |
| 113 | `MFCreateTransformActivate` | `0x73DE0` | 454 | UnwindData |  |
| 183 | `MFLockDXGIDeviceManager` | `0x82620` | 165 | UnwindData |  |
| 21 | `MFAverageTimePerFrameToFrameRate` | `0x85180` | 17 | UnwindData |  |
| 129 | `MFDeserializeMediaTypeFromStream` | `0x857C0` | 198 | UnwindData |  |
| 209 | `MFStartup` | `0x86D10` | 56 | UnwindData |  |
| 56 | `MFCreateCollection` | `0x88680` | 121 | UnwindData |  |
| 8 | `MFPlatformLittleEndian` | `0x88750` | 12,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `MFUnwrapMediaType` | `0x8B800` | 517 | UnwindData |  |
| 11 | `CreatePropVariant` | `0x8C960` | 7,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `MFPutWorkItemEx2` | `0x8E620` | 1,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `MFGetPluginControl` | `0x8EC70` | 156 | UnwindData |  |
| 65 | `MFCreateEventQueue` | `0x8FBB0` | 194 | UnwindData |  |
| 207 | `MFShutdown` | `0x912F0` | 129 | UnwindData |  |
| 67 | `MFCreateFileFromHandle` | `0x92630` | 453 | UnwindData |  |
| 143 | `MFGetConfigurationStore` | `0x96830` | 28 | UnwindData |  |
| 192 | `MFPutWorkItemEx` | `0x989F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `MFCreateMFByteStreamOnStreamEx` | `0x98A30` | 3,617 | UnwindData |  |
| 130 | `MFDeserializePresentationDescriptor` | `0x9C530` | 222 | UnwindData |  |
| 175 | `MFInitVideoFormat_RGB` | `0x9F510` | 348 | UnwindData |  |
| 180 | `MFIsLocallyRegisteredMimeType` | `0xA0510` | 428 | UnwindData |  |
| 119 | `MFCreateVideoMediaTypeFromBitMapInfoHeaderEx` | `0xA0C90` | 571 | UnwindData |  |
| 89 | `MFCreateMuxStreamMediaType` | `0xA1470` | 839 | UnwindData |  |
| 141 | `MFGetConfigurationDWORD` | `0xA23D0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `MFCreate2DMediaBuffer` | `0xA2490` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `MFTEnum` | `0xA2890` | 900 | UnwindData |  |
| 213 | `MFTEnumEx` | `0xA2C20` | 2,837 | UnwindData |  |
| 9 | `ValidateWaveFormat` | `0xA3860` | 71 | UnwindData |  |
| 1 | `FormatTagFromWfx` | `0xA3AC0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `MFCreateMemoryStream` | `0xA3B40` | 502 | UnwindData |  |
| 88 | `MFCreateMuxStreamAttributes` | `0xA5720` | 703 | UnwindData |  |
| 103 | `MFCreateSourceResolver` | `0xA6620` | 437 | UnwindData |  |
| 94 | `MFCreatePresentationDescriptor` | `0xA6E50` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `MFGetCallStackTracingWeakReference` | `0xA7400` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `MFCreateLegacyMediaBufferOnMFMediaBuffer` | `0xA7960` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `MFCreateVideoMediaTypeFromVideoInfoHeader2` | `0xA7E70` | 163 | UnwindData |  |
| 156 | `MFGetTimerPeriodicity` | `0xA8690` | 301 | UnwindData |  |
| 206 | `MFSetWindowForContentProtection` | `0xA87D0` | 138 | UnwindData |  |
| 187 | `MFMapDX9FormatToDXGIFormat` | `0xA8F70` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `MFClearLocalMFTs` | `0xA9380` | 91 | UnwindData |  |
| 70 | `MFCreateMFByteStreamOnStream` | `0xAA6A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `MFCreateStreamOnMFByteStreamEx` | `0xAA6D0` | 2,192 | UnwindData |  |
| 7 | `MFPlatformBigEndian` | `0xAB0F0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `MFSetMinimumMemoryAlignment` | `0xAB2F0` | 9,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MFAllocateWorkQueue` | `0xAD960` | 4,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `MFCreateVideoSampleAllocatorEx` | `0xAEA20` | 2,704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MFIsFeatureEnabled` | `0xAF4B0` | 51 | UnwindData |  |
| 66 | `MFCreateFile` | `0xAFE30` | 31 | UnwindData |  |
| 28 | `MFCalculateImageSize` | `0xAFE60` | 1,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `MFCreateSourceResolverInternal` | `0xB04F0` | 440 | UnwindData |  |
| 61 | `MFCreateDXGIDeviceManager` | `0xB0900` | 8,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `MFTEnum2` | `0xB2A40` | 3,138 | UnwindData |  |
| 4 | `MFGetPlatformVersion` | `0xBA790` | 59 | UnwindData |  |
| 176 | `MFInvalidateMFTEnumCache` | `0xBD5E0` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `MFMapDXGIFormatToDX9Format` | `0xBD920` | 16,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFGetPlatformFlags` | `0xC17E0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `MFBeginRegisterWorkQueueWithMMCSS` | `0xC1BE0` | 40 | UnwindData |  |
| 29 | `MFCallStackTracingClearSnapshot` | `0xC1C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MFCallStackTracingLogSessionErrors` | `0xC1C30` | 49 | UnwindData |  |
| 142 | `MFGetConfigurationPolicy` | `0xC1C70` | 28 | UnwindData |  |
| 144 | `MFGetConfigurationString` | `0xC1CA0` | 28 | UnwindData |  |
| 145 | `MFGetContentProtectionSystemCLSID` | `0xC1CD0` | 1,261 | UnwindData |  |
| 5 | `MFGetRandomNumber` | `0xC21D0` | 207 | UnwindData |  |
| 34 | `MFCancelCreateFile` | `0xC4430` | 93 | UnwindData |  |
| 111 | `MFCreateTempFile` | `0xC44A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `MFEndCreateFile` | `0xC44B0` | 611 | UnwindData |  |
| 23 | `MFBeginGetHostByName` | `0xC50A0` | 804 | UnwindData |  |
| 40 | `MFCompareSockaddrAddresses` | `0xC53D0` | 123 | UnwindData |  |
| 101 | `MFCreateSocket` | `0xC5460` | 501 | UnwindData |  |
| 115 | `MFCreateUdpSockets` | `0xC5660` | 1,738 | UnwindData |  |
| 132 | `MFEndGetHostByName` | `0xC5D30` | 429 | UnwindData |  |
| 148 | `MFGetNumericNameFromSockaddr` | `0xC5EF0` | 855 | UnwindData |  |
| 151 | `MFGetSockaddrFromNumericName` | `0xC6250` | 670 | UnwindData |  |
| 205 | `MFSetSockaddrAny` | `0xC6500` | 544 | UnwindData |  |
| 231 | `MFWrapSocket` | `0xC6730` | 536 | UnwindData |  |
| 39 | `MFCompareFullToPartialMediaType` | `0xC76D0` | 4,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `MFCreateSocketListener` | `0xC8900` | 7,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `MFCreateSystemTimeSource` | `0xCA610` | 159 | UnwindData |  |
| 136 | `MFFreeAdaptersAddresses` | `0xCAD10` | 22 | UnwindData |  |
| 137 | `MFGetAdaptersAddresses` | `0xCAD30` | 48 | UnwindData |  |
| 163 | `MFHeapAlloc` | `0xCADA0` | 57 | UnwindData |  |
| 164 | `MFHeapFree` | `0xCADE0` | 52 | UnwindData |  |
| 41 | `MFConvertColorInfoFromDXVA` | `0xD60D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `MFConvertColorInfoToDXVA` | `0xD60E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MFConvertFromFP16Array` | `0xD60F0` | 70 | UnwindData |  |
| 44 | `MFConvertToFP16Array` | `0xD6140` | 212 | UnwindData |  |
| 174 | `MFInitVideoFormat` | `0xD6220` | 570 | UnwindData |  |
| 59 | `MFCreateD3D12SynchronizationObject` | `0xDA1B0` | 9,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `MFCreateMuxStreamSample` | `0xDC520` | 1,391 | UnwindData |  |
| 107 | `MFCreateStreamOnMFByteStream` | `0xDE460` | 172 | UnwindData |  |
| 53 | `MFCreateAudioMediaType` | `0xE85A0` | 259 | UnwindData |  |
| 2 | `MFEnumLocalMFTRegistrations` | `0xE9BC0` | 4,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `MFTRegisterLocal` | `0xEAEB0` | 101 | UnwindData |  |
| 217 | `MFTRegisterLocalByCLSID` | `0xEAF20` | 101 | UnwindData |  |
| 219 | `MFTUnregisterLocal` | `0xEAF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `MFTUnregisterLocalByCLSID` | `0xEAFA0` | 18 | UnwindData |  |
| 233 | `PropVariantFromStream` | `0xEAFC0` | 929 | UnwindData |  |
| 234 | `PropVariantToStream` | `0xEB370` | 535 | UnwindData |  |
| 27 | `MFCalculateBitmapImageSize` | `0xEB620` | 269 | UnwindData |  |
| 118 | `MFCreateVideoMediaTypeFromBitMapInfoHeader` | `0xEB740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `MFInitMediaTypeFromMPEG1VideoInfo` | `0xEB750` | 147 | UnwindData |  |
| 178 | `MFIsBottomUpFormat` | `0xEB7F0` | 747 | UnwindData |  |
| 229 | `MFValidateMediaTypeSize` | `0xEBAF0` | 739 | UnwindData |  |
| 210 | `MFStreamDescriptorProtectMediaType` | `0xEDDD0` | 279 | UnwindData |  |
| 215 | `MFTRegister` | `0xF17A0` | 477 | UnwindData |  |
| 218 | `MFTUnregister` | `0xF1990` | 73 | UnwindData |  |
| 20 | `MFAppendCollection` | `0xF3350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MFCreate2DMediaBufferOn1DMediaBuffer` | `0xF3360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `MFCreateAlignedSharedMemoryBuffer` | `0xF3370` | 449 | UnwindData |  |
| 60 | `MFCreateDXGICrossAdapterBuffer` | `0xF3540` | 104 | UnwindData |  |
| 63 | `MFCreateDXSurfaceBuffer` | `0xF35B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `MFCreateMemoryBufferFromRawBuffer` | `0xF35C0` | 54 | UnwindData |  |
| 99 | `MFCreateSecureBufferAllocator` | `0xF3600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `MFCreateSharedMemoryMediaBufferFromMediaType` | `0xF3610` | 56 | UnwindData |  |
| 105 | `MFCreateStagingSurfaceWrapper` | `0xF3650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `MFCreateWICBitmapBuffer` | `0xF3660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `MFDeserializeEvent` | `0xF3670` | 225 | UnwindData |  |
| 146 | `MFGetDXGIDeviceManageMode` | `0xF3760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `MFGetPlaneSize` | `0xF3770` | 29 | UnwindData |  |
| 201 | `MFSerializeEvent` | `0xF37A0` | 315 | UnwindData |  |
| 202 | `MFSerializeMediaTypeToStream` | `0xF38F0` | 174 | UnwindData |  |
| 203 | `MFSerializePresentationDescriptor` | `0xF39B0` | 325 | UnwindData |  |
| 224 | `MFUnlockDXGIDeviceManager` | `0xF3B00` | 93 | UnwindData |  |
| 78 | `MFCreateMediaExtensionActivate` | `0xFFA70` | 597 | UnwindData |  |
| 79 | `MFCreateMediaExtensionActivateNoInit` | `0xFFCD0` | 413 | UnwindData |  |
| 55 | `MFCreateByteStreamHandlerInprocActivate` | `0x101BF0` | 247 | UnwindData |  |
| 64 | `MFCreateEMEStoreObject` | `0x105AC0` | 234 | UnwindData |  |
| 36 | `MFCheckEnabledViaAppService` | `0x1220A0` | 445 | UnwindData |  |
| 91 | `MFCreateOOPMFTProxy` | `0x12EDE0` | 344 | UnwindData |  |
| 92 | `MFCreateOOPMFTRemote` | `0x135D20` | 343 | UnwindData |  |
| 125 | `MFCreateWICDecoderProxy` | `0x146C40` | 259 | UnwindData |  |
| 154 | `MFGetSupportedSchemes` | `0x14E1A0` | 1,226 | UnwindData |  |
| 161 | `MFHasLocallyRegisteredByteStreamHandlers` | `0x14F8B0` | 312 | UnwindData |  |
| 162 | `MFHasLocallyRegisteredSchemeHandlers` | `0x14F9F0` | 312 | UnwindData |  |
| 181 | `MFIsLocallyRegisteredSchemeHandler` | `0x14FB30` | 501 | UnwindData |  |
| 194 | `MFRegisterLocalByteStreamHandler` | `0x14FD30` | 602 | UnwindData |  |
| 195 | `MFRegisterLocalSchemeHandler` | `0x14FF90` | 577 | UnwindData |  |
| 72 | `MFCreateMFByteStreamWrapper` | `0x157F50` | 570 | UnwindData |  |
| 96 | `MFCreateReusableByteStream` | `0x158190` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `MFCreateReusableByteStreamWithSharedLock` | `0x1581C0` | 120,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `MFCanEnableHWDRMByDefault` | `0x1757F0` | 3,355 | UnwindData |  |
| 58 | `MFCreateContentProtectionDevice` | `0x176520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `MFIsContentProtectionDeviceSupported` | `0x176530` | 2,668 | UnwindData |  |
| 57 | `MFCreateContentDecryptorContext` | `0x178E90` | 252,124 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `MFCreateVideoDecryptorContext` | `0x178E90` | 252,124 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
