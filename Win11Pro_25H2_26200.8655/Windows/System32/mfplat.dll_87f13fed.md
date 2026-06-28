# Binary Specification: mfplat.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mfplat.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `87f13fed4873a9d4b9704f3e334d3821e8c797741775e06c921f157db9bc3b6b`
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
| 221 | `MFTraceError` | `0x4660` | 5,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `MFTraceFuncEnter` | `0x4660` | 5,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `MFllMulDiv` | `0x5C70` | 1,286 | UnwindData |  |
| 76 | `MFCreateMediaEvent` | `0x8BC0` | 59 | UnwindData |  |
| 31 | `MFCallStackTracingRestoreSnapshot` | `0xCA30` | 8,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `MFCallStackTracingTakeSnapshot` | `0xEBC0` | 3,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `MFCreateTrackedSample` | `0xF840` | 109 | UnwindData |  |
| 208 | `MFSplitSample` | `0xFF90` | 2,450 | UnwindData |  |
| 98 | `MFCreateSample` | `0x10930` | 136 | UnwindData |  |
| 191 | `MFPutWorkItem2` | `0x1A710` | 372 | UnwindData |  |
| 147 | `MFGetMFTMerit` | `0x1D260` | 48,645 | UnwindData |  |
| 12 | `CreatePropertyStore` | `0x29070` | 31 | UnwindData |  |
| 52 | `MFCreateAttributes` | `0x2A740` | 477 | UnwindData |  |
| 127 | `MFDeserializeAttributesFromStream` | `0x2AED0` | 738 | UnwindData |  |
| 166 | `MFInitAttributesFromBlob` | `0x2B4B0` | 72 | UnwindData |  |
| 214 | `MFTGetInfo` | `0x2B8B0` | 631 | UnwindData |  |
| 106 | `MFCreateStreamDescriptor` | `0x2D040` | 233 | UnwindData |  |
| 153 | `MFGetSupportedMimeTypes` | `0x2E4E0` | 75 | UnwindData |  |
| 13 | `DestroyPropVariant` | `0x324C0` | 4,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `MFGetPluginControl` | `0x337E0` | 156 | UnwindData |  |
| 135 | `MFFrameRateToAverageTimePerFrame` | `0x35640` | 17 | UnwindData |  |
| 126 | `MFCreateWaveFormatExFromMFMediaType` | `0x35820` | 1,288 | UnwindData |  |
| 48 | `MFCreateAMMediaTypeFromMFMediaType` | `0x35D50` | 178 | UnwindData |  |
| 165 | `MFInitAMMediaTypeFromMFMediaType` | `0x35E10` | 2,659 | UnwindData |  |
| 15 | `GetD3DFormatFromMFSubtype` | `0x37690` | 146 | UnwindData |  |
| 14 | `GetAMSubtypeFromD3DFormat` | `0x37730` | 126 | UnwindData |  |
| 170 | `MFInitMediaTypeFromMPEG2VideoInfo` | `0x381F0` | 294 | UnwindData |  |
| 167 | `MFInitMediaTypeFromAMMediaType` | `0x38320` | 902 | UnwindData |  |
| 171 | `MFInitMediaTypeFromVideoInfoHeader` | `0x386B0` | 175 | UnwindData |  |
| 172 | `MFInitMediaTypeFromVideoInfoHeader2` | `0x38770` | 973 | UnwindData |  |
| 121 | `MFCreateVideoMediaTypeFromVideoInfoHeader` | `0x39990` | 269 | UnwindData |  |
| 173 | `MFInitMediaTypeFromWaveFormatEx` | `0x3A350` | 995 | UnwindData |  |
| 84 | `MFCreateMediaTypeFromRepresentation` | `0x3BE30` | 1,607 | UnwindData |  |
| 120 | `MFCreateVideoMediaTypeFromSubtype` | `0x3C480` | 166 | UnwindData |  |
| 117 | `MFCreateVideoMediaType` | `0x3C530` | 150 | UnwindData |  |
| 82 | `MFCreateMediaType` | `0x3C660` | 164 | UnwindData |  |
| 168 | `MFInitMediaTypeFromMFVideoFormat` | `0x3C7D0` | 3,602 | UnwindData |  |
| 83 | `MFCreateMediaTypeFromProperties` | `0x3D660` | 2,907 | UnwindData |  |
| 75 | `MFCreateMediaBufferWrapper` | `0x41820` | 876 | UnwindData |  |
| 49 | `MFCreateAlignedMemoryBuffer` | `0x41BA0` | 678 | UnwindData |  |
| 85 | `MFCreateMemoryBuffer` | `0x41E50` | 650 | UnwindData |  |
| 22 | `MFBeginCreateFile` | `0x427D0` | 1,003 | UnwindData |  |
| 190 | `MFPutWorkItem` | `0x43FA0` | 345 | UnwindData |  |
| 114 | `MFCreateURLFromPath` | `0x44100` | 78 | UnwindData |  |
| 69 | `MFCreateMFByteStreamOnIStreamWithFlags` | `0x464D0` | 879 | UnwindData |  |
| 110 | `MFCreateTelemetrySession` | `0x47430` | 42 | UnwindData |  |
| 10 | `CopyPropVariant` | `0x4A2F0` | 86 | UnwindData |  |
| 45 | `MFCopyImage` | `0x4CD10` | 664 | UnwindData |  |
| 155 | `MFGetSystemTime` | `0x51370` | 80 | UnwindData |  |
| 77 | `MFCreateMediaEventResult` | `0x51BA0` | 303 | UnwindData |  |
| 200 | `MFSerializeAttributesToStream` | `0x54BC0` | 738 | UnwindData |  |
| 138 | `MFGetAttributesAsBlob` | `0x553D0` | 99 | UnwindData |  |
| 152 | `MFGetStrideForBitmapInfoHeader` | `0x566B0` | 52 | UnwindData |  |
| 73 | `MFCreateMFVideoFormatFromMFMediaType` | `0x58B80` | 1,582 | UnwindData |  |
| 157 | `MFGetUncompressedVideoFormat` | `0x595F0` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `MFCreateDXGISurfaceBuffer` | `0x59AD0` | 7,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `MFWrapMediaType` | `0x5B690` | 999 | UnwindData |  |
| 139 | `MFGetAttributesAsBlobSize` | `0x5BA80` | 399 | UnwindData |  |
| 95 | `MFCreatePropertiesFromMediaType` | `0x5EB90` | 3,911 | UnwindData |  |
| 93 | `MFCreatePathFromURL` | `0x68AA0` | 81 | UnwindData |  |
| 198 | `MFScheduleWorkItem` | `0x6A1A0` | 366 | UnwindData |  |
| 38 | `MFCombineSamples` | `0x701B0` | 1,197 | UnwindData |  |
| 54 | `MFCreateByteStreamHandlerAppServiceActivate` | `0x709D0` | 247 | UnwindData |  |
| 81 | `MFCreateMediaExtensionInprocActivate` | `0x71150` | 249 | UnwindData |  |
| 80 | `MFCreateMediaExtensionAppServiceActivate` | `0x71250` | 244 | UnwindData |  |
| 113 | `MFCreateTransformActivate` | `0x71500` | 454 | UnwindData |  |
| 183 | `MFLockDXGIDeviceManager` | `0x807A0` | 165 | UnwindData |  |
| 21 | `MFAverageTimePerFrameToFrameRate` | `0x83330` | 17 | UnwindData |  |
| 129 | `MFDeserializeMediaTypeFromStream` | `0x839C0` | 198 | UnwindData |  |
| 209 | `MFStartup` | `0x84E20` | 56 | UnwindData |  |
| 56 | `MFCreateCollection` | `0x86790` | 121 | UnwindData |  |
| 8 | `MFPlatformLittleEndian` | `0x86860` | 12,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `MFUnwrapMediaType` | `0x89910` | 517 | UnwindData |  |
| 11 | `CreatePropVariant` | `0x8A960` | 6,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `MFPutWorkItemEx2` | `0x8C130` | 3,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `MFCreateEventQueue` | `0x8CF50` | 194 | UnwindData |  |
| 207 | `MFShutdown` | `0x8E6A0` | 129 | UnwindData |  |
| 67 | `MFCreateFileFromHandle` | `0x8F9E0` | 453 | UnwindData |  |
| 143 | `MFGetConfigurationStore` | `0x93B20` | 28 | UnwindData |  |
| 192 | `MFPutWorkItemEx` | `0x95A00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `MFCreateMFByteStreamOnStreamEx` | `0x95A40` | 3,617 | UnwindData |  |
| 130 | `MFDeserializePresentationDescriptor` | `0x98FD0` | 222 | UnwindData |  |
| 175 | `MFInitVideoFormat_RGB` | `0x9BD50` | 348 | UnwindData |  |
| 180 | `MFIsLocallyRegisteredMimeType` | `0x9CF20` | 428 | UnwindData |  |
| 119 | `MFCreateVideoMediaTypeFromBitMapInfoHeaderEx` | `0x9D8E0` | 571 | UnwindData |  |
| 89 | `MFCreateMuxStreamMediaType` | `0x9E0C0` | 839 | UnwindData |  |
| 141 | `MFGetConfigurationDWORD` | `0x9F020` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `MFCreate2DMediaBuffer` | `0x9F440` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `MFTEnum` | `0x9F840` | 900 | UnwindData |  |
| 213 | `MFTEnumEx` | `0x9FBD0` | 2,837 | UnwindData |  |
| 9 | `ValidateWaveFormat` | `0xA0810` | 71 | UnwindData |  |
| 1 | `FormatTagFromWfx` | `0xA0A70` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `MFCreateMemoryStream` | `0xA0AF0` | 502 | UnwindData |  |
| 88 | `MFCreateMuxStreamAttributes` | `0xA27C0` | 703 | UnwindData |  |
| 103 | `MFCreateSourceResolver` | `0xA36C0` | 437 | UnwindData |  |
| 94 | `MFCreatePresentationDescriptor` | `0xA3EF0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `MFGetCallStackTracingWeakReference` | `0xA44A0` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `MFCreateLegacyMediaBufferOnMFMediaBuffer` | `0xA4A00` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `MFCreateVideoMediaTypeFromVideoInfoHeader2` | `0xA4F10` | 163 | UnwindData |  |
| 156 | `MFGetTimerPeriodicity` | `0xA5730` | 301 | UnwindData |  |
| 206 | `MFSetWindowForContentProtection` | `0xA5870` | 138 | UnwindData |  |
| 187 | `MFMapDX9FormatToDXGIFormat` | `0xA60B0` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `MFClearLocalMFTs` | `0xA64C0` | 91 | UnwindData |  |
| 70 | `MFCreateMFByteStreamOnStream` | `0xA77A0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `MFCreateStreamOnMFByteStreamEx` | `0xA7810` | 2,192 | UnwindData |  |
| 7 | `MFPlatformBigEndian` | `0xA8230` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `MFSetMinimumMemoryAlignment` | `0xA8430` | 9,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MFAllocateWorkQueue` | `0xAAAC0` | 4,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `MFCreateVideoSampleAllocatorEx` | `0xABB80` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `MFCreateMediaBufferFromMediaType` | `0xABC40` | 41 | UnwindData |  |
| 6 | `MFIsFeatureEnabled` | `0xAC640` | 51 | UnwindData |  |
| 66 | `MFCreateFile` | `0xACFC0` | 31 | UnwindData |  |
| 28 | `MFCalculateImageSize` | `0xACFF0` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `MFCreateSourceResolverInternal` | `0xAD610` | 440 | UnwindData |  |
| 61 | `MFCreateDXGIDeviceManager` | `0xADA70` | 4,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `MFTEnum2` | `0xAECE0` | 3,138 | UnwindData |  |
| 4 | `MFGetPlatformVersion` | `0xBB1F0` | 59 | UnwindData |  |
| 176 | `MFInvalidateMFTEnumCache` | `0xBDFB0` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `MFMapDXGIFormatToDX9Format` | `0xBE2F0` | 15,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFGetPlatformFlags` | `0xC2130` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `MFBeginRegisterWorkQueueWithMMCSS` | `0xC2530` | 40 | UnwindData |  |
| 29 | `MFCallStackTracingClearSnapshot` | `0xC2560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MFCallStackTracingLogSessionErrors` | `0xC2580` | 49 | UnwindData |  |
| 142 | `MFGetConfigurationPolicy` | `0xC25C0` | 28 | UnwindData |  |
| 144 | `MFGetConfigurationString` | `0xC25F0` | 28 | UnwindData |  |
| 145 | `MFGetContentProtectionSystemCLSID` | `0xC2620` | 1,261 | UnwindData |  |
| 5 | `MFGetRandomNumber` | `0xC2B20` | 207 | UnwindData |  |
| 34 | `MFCancelCreateFile` | `0xC4D80` | 93 | UnwindData |  |
| 111 | `MFCreateTempFile` | `0xC4DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `MFEndCreateFile` | `0xC4E00` | 611 | UnwindData |  |
| 23 | `MFBeginGetHostByName` | `0xC59F0` | 804 | UnwindData |  |
| 40 | `MFCompareSockaddrAddresses` | `0xC5D20` | 123 | UnwindData |  |
| 101 | `MFCreateSocket` | `0xC5DB0` | 501 | UnwindData |  |
| 115 | `MFCreateUdpSockets` | `0xC5FB0` | 1,738 | UnwindData |  |
| 132 | `MFEndGetHostByName` | `0xC6680` | 429 | UnwindData |  |
| 148 | `MFGetNumericNameFromSockaddr` | `0xC6840` | 855 | UnwindData |  |
| 151 | `MFGetSockaddrFromNumericName` | `0xC6BA0` | 670 | UnwindData |  |
| 205 | `MFSetSockaddrAny` | `0xC6E50` | 544 | UnwindData |  |
| 231 | `MFWrapSocket` | `0xC7080` | 536 | UnwindData |  |
| 39 | `MFCompareFullToPartialMediaType` | `0xC8020` | 4,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `MFCreateSocketListener` | `0xC9250` | 7,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `MFCreateSystemTimeSource` | `0xCAF60` | 159 | UnwindData |  |
| 136 | `MFFreeAdaptersAddresses` | `0xCB660` | 22 | UnwindData |  |
| 137 | `MFGetAdaptersAddresses` | `0xCB680` | 48 | UnwindData |  |
| 163 | `MFHeapAlloc` | `0xCB6F0` | 57 | UnwindData |  |
| 164 | `MFHeapFree` | `0xCB730` | 52 | UnwindData |  |
| 41 | `MFConvertColorInfoFromDXVA` | `0xD5F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `MFConvertColorInfoToDXVA` | `0xD5F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `MFConvertFromFP16Array` | `0xD5F50` | 70 | UnwindData |  |
| 44 | `MFConvertToFP16Array` | `0xD5FA0` | 212 | UnwindData |  |
| 174 | `MFInitVideoFormat` | `0xD6080` | 570 | UnwindData |  |
| 59 | `MFCreateD3D12SynchronizationObject` | `0xD9C20` | 9,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `MFCreateMuxStreamSample` | `0xDBF90` | 1,391 | UnwindData |  |
| 107 | `MFCreateStreamOnMFByteStream` | `0xDDED0` | 172 | UnwindData |  |
| 53 | `MFCreateAudioMediaType` | `0xE7E00` | 259 | UnwindData |  |
| 2 | `MFEnumLocalMFTRegistrations` | `0xE9680` | 5,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `MFTRegisterLocal` | `0xEAAD0` | 101 | UnwindData |  |
| 217 | `MFTRegisterLocalByCLSID` | `0xEAB40` | 101 | UnwindData |  |
| 219 | `MFTUnregisterLocal` | `0xEABB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `MFTUnregisterLocalByCLSID` | `0xEABC0` | 18 | UnwindData |  |
| 233 | `PropVariantFromStream` | `0xEABE0` | 929 | UnwindData |  |
| 234 | `PropVariantToStream` | `0xEAF90` | 535 | UnwindData |  |
| 27 | `MFCalculateBitmapImageSize` | `0xEB240` | 269 | UnwindData |  |
| 118 | `MFCreateVideoMediaTypeFromBitMapInfoHeader` | `0xEB360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `MFInitMediaTypeFromMPEG1VideoInfo` | `0xEB370` | 147 | UnwindData |  |
| 178 | `MFIsBottomUpFormat` | `0xEB410` | 747 | UnwindData |  |
| 229 | `MFValidateMediaTypeSize` | `0xEB710` | 739 | UnwindData |  |
| 210 | `MFStreamDescriptorProtectMediaType` | `0xED9F0` | 279 | UnwindData |  |
| 215 | `MFTRegister` | `0xF0A70` | 477 | UnwindData |  |
| 218 | `MFTUnregister` | `0xF0C60` | 73 | UnwindData |  |
| 20 | `MFAppendCollection` | `0xF2980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MFCreate2DMediaBufferOn1DMediaBuffer` | `0xF2990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `MFCreateAlignedSharedMemoryBuffer` | `0xF29A0` | 449 | UnwindData |  |
| 60 | `MFCreateDXGICrossAdapterBuffer` | `0xF2B70` | 104 | UnwindData |  |
| 63 | `MFCreateDXSurfaceBuffer` | `0xF2BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `MFCreateMemoryBufferFromRawBuffer` | `0xF2BF0` | 54 | UnwindData |  |
| 99 | `MFCreateSecureBufferAllocator` | `0xF2C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `MFCreateSharedMemoryMediaBufferFromMediaType` | `0xF2C40` | 56 | UnwindData |  |
| 105 | `MFCreateStagingSurfaceWrapper` | `0xF2C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `MFCreateWICBitmapBuffer` | `0xF2C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `MFDeserializeEvent` | `0xF2CA0` | 225 | UnwindData |  |
| 146 | `MFGetDXGIDeviceManageMode` | `0xF2D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `MFGetPlaneSize` | `0xF2DA0` | 29 | UnwindData |  |
| 201 | `MFSerializeEvent` | `0xF2DD0` | 315 | UnwindData |  |
| 202 | `MFSerializeMediaTypeToStream` | `0xF2F20` | 174 | UnwindData |  |
| 203 | `MFSerializePresentationDescriptor` | `0xF2FE0` | 325 | UnwindData |  |
| 224 | `MFUnlockDXGIDeviceManager` | `0xF3130` | 93 | UnwindData |  |
| 78 | `MFCreateMediaExtensionActivate` | `0xFF0A0` | 597 | UnwindData |  |
| 79 | `MFCreateMediaExtensionActivateNoInit` | `0xFF300` | 413 | UnwindData |  |
| 55 | `MFCreateByteStreamHandlerInprocActivate` | `0x1011F0` | 247 | UnwindData |  |
| 64 | `MFCreateEMEStoreObject` | `0x1050C0` | 234 | UnwindData |  |
| 36 | `MFCheckEnabledViaAppService` | `0x1217E0` | 445 | UnwindData |  |
| 91 | `MFCreateOOPMFTProxy` | `0x12E520` | 344 | UnwindData |  |
| 92 | `MFCreateOOPMFTRemote` | `0x135460` | 343 | UnwindData |  |
| 125 | `MFCreateWICDecoderProxy` | `0x146380` | 259 | UnwindData |  |
| 154 | `MFGetSupportedSchemes` | `0x14D8E0` | 1,226 | UnwindData |  |
| 161 | `MFHasLocallyRegisteredByteStreamHandlers` | `0x14EFF0` | 312 | UnwindData |  |
| 162 | `MFHasLocallyRegisteredSchemeHandlers` | `0x14F130` | 312 | UnwindData |  |
| 181 | `MFIsLocallyRegisteredSchemeHandler` | `0x14F270` | 501 | UnwindData |  |
| 194 | `MFRegisterLocalByteStreamHandler` | `0x14F470` | 602 | UnwindData |  |
| 195 | `MFRegisterLocalSchemeHandler` | `0x14F6D0` | 577 | UnwindData |  |
| 72 | `MFCreateMFByteStreamWrapper` | `0x157690` | 570 | UnwindData |  |
| 96 | `MFCreateReusableByteStream` | `0x1578D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `MFCreateReusableByteStreamWithSharedLock` | `0x157900` | 121,264 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `MFCanEnableHWDRMByDefault` | `0x1752B0` | 4,254 | UnwindData |  |
| 58 | `MFCreateContentProtectionDevice` | `0x176360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `MFIsContentProtectionDeviceSupported` | `0x176370` | 2,668 | UnwindData |  |
| 57 | `MFCreateContentDecryptorContext` | `0x178D50` | 246,364 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `MFCreateVideoDecryptorContext` | `0x178D50` | 246,364 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
