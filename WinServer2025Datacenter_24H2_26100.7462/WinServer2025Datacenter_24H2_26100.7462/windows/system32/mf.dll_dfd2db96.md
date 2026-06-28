# Binary Specification: mf.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dfd2db960752422e2732ca704af0657b3d2f54c29046bb4873458338dbbea43e`
* **Total Exported Functions:** 94

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AppendPropVariant` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.AppendPropVariant` |
| 2 | `ConvertPropVariant` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.ConvertPropVariant` |
| 3 | `CopyPropertyStore` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.CopyPropertyStore` |
| 4 | `CreateNamedPropertyStore` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.CreateNamedPropertyStore` |
| 8 | `ExtractPropVariant` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.ExtractPropVariant` |
| 25 | `MFCreateAggregateSource` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateAggregateSource` |
| 26 | `MFCreateAppSourceProxy` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateAppSourceProxy` |
| 27 | `MFCreateAudioRenderer` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateAudioRenderer` |
| 28 | `MFCreateAudioRendererActivate` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateAudioRendererActivate` |
| 32 | `MFCreateDeviceSource` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateDeviceSource` |
| 33 | `MFCreateDeviceSourceActivate` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateDeviceSourceActivate` |
| 35 | `MFCreateEncryptedMediaExtensionsStoreActivate` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateEncryptedMediaExtensionsStoreActivate` |
| 38 | `MFCreateFileSchemePlugin` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateFileSchemePlugin` |
| 44 | `MFCreateMediaProcessor` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateMediaProcessor` |
| 45 | `MFCreateMediaSession` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateMediaSession` |
| 49 | `MFCreatePMPHost` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreatePMPHost` |
| 50 | `MFCreatePMPMediaSession` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreatePMPMediaSession` |
| 51 | `MFCreatePMPServer` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreatePMPServer` |
| 52 | `MFCreatePresentationClock` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreatePresentationClock` |
| 58 | `MFCreateSampleCopierMFT` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateSampleCopierMFT` |
| 59 | `MFCreateSampleGrabberSinkActivate` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateSampleGrabberSinkActivate` |
| 61 | `MFCreateSequencerSegmentOffset` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateSequencerSegmentOffset` |
| 62 | `MFCreateSequencerSource` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateSequencerSource` |
| 63 | `MFCreateSequencerSourceRemoteStream` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateSequencerSourceRemoteStream` |
| 64 | `MFCreateSimpleTypeHandler` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateSimpleTypeHandler` |
| 65 | `MFCreateSoundEventSchemePlugin` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateSoundEventSchemePlugin` |
| 67 | `MFCreateStandardQualityManager` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateStandardQualityManager` |
| 68 | `MFCreateTopoLoader` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateTopoLoader` |
| 69 | `MFCreateTopology` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateTopology` |
| 70 | `MFCreateTopologyNode` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateTopologyNode` |
| 71 | `MFCreateTranscodeProfile` | `0x0` | - | Forwarded | Forwarded to: `MFTranscode.MFCreateTranscodeProfile` |
| 72 | `MFCreateTranscodeSinkActivate` | `0x0` | - | Forwarded | Forwarded to: `MFTranscode.MFCreateTranscodeSinkActivate` |
| 73 | `MFCreateTranscodeTopology` | `0x0` | - | Forwarded | Forwarded to: `MFTranscode.MFCreateTranscodeTopology` |
| 74 | `MFCreateTranscodeTopologyFromByteStream` | `0x0` | - | Forwarded | Forwarded to: `MFTranscode.MFCreateTranscodeTopologyFromByteStream` |
| 78 | `MFCreateWMAEncoderActivate` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateWMAEncoderActivate` |
| 79 | `MFCreateWMVEncoderActivate` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFCreateWMVEncoderActivate` |
| 80 | `MFEnumDeviceSources` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFEnumDeviceSources` |
| 82 | `MFGetMultipleServiceProviders` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFGetMultipleServiceProviders` |
| 83 | `MFGetService` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFGetService` |
| 87 | `MFGetTopoNodeCurrentType` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFGetTopoNodeCurrentType` |
| 90 | `MFReadSequencerSegmentOffset` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFReadSequencerSegmentOffset` |
| 91 | `MFRequireProtectedEnvironment` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MFRequireProtectedEnvironment` |
| 93 | `MFTranscodeGetAudioOutputAvailableTypes` | `0x0` | - | Forwarded | Forwarded to: `MFTranscode.MFTranscodeGetAudioOutputAvailableTypes` |
| 94 | `MergePropertyStore` | `0x0` | - | Forwarded | Forwarded to: `MFCORE.MergePropertyStore` |
| 5 | `DllCanUnloadNow` | `0x2B550` | 61 | UnwindData |  |
| 7 | `DllGetClassObject` | `0x2B5A0` | 83 | UnwindData |  |
| 9 | `MFCreate3GPMediaSink` | `0x2B8F0` | 529 | UnwindData |  |
| 10 | `MFCreateAC3MediaSink` | `0x2BB10` | 515 | UnwindData |  |
| 11 | `MFCreateADTSMediaSink` | `0x2BD20` | 515 | UnwindData |  |
| 12 | `MFCreateASFByteStreamPlugin` | `0x2BF30` | 43 | UnwindData |  |
| 13 | `MFCreateASFContentInfo` | `0x2BF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `MFCreateASFIndexerByteStream` | `0x2BF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MFCreateASFIndexer` | `0x2BFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `MFCreateASFMediaSinkActivate` | `0x2BFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MFCreateASFMediaSink` | `0x2BFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MFCreateASFMultiplexer` | `0x2C010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `MFCreateASFProfileFromPresentationDescriptor` | `0x2C030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `MFCreateASFProfile` | `0x2C050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `MFCreateASFSplitter` | `0x2C070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `MFCreateASFStreamSelector` | `0x2C090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `MFCreateASFStreamingMediaSinkActivate` | `0x2C0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `MFCreateASFStreamingMediaSink` | `0x2C0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `MFCreateByteCacheFile` | `0x2C0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MFCreateCacheManager` | `0x2C110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `MFCreateCredentialCache` | `0x2C130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `MFCreateDrmNetNDSchemePlugin` | `0x2C150` | 43 | UnwindData |  |
| 36 | `MFCreateFMPEG4MediaSink` | `0x2C190` | 529 | UnwindData |  |
| 37 | `MFCreateFileBlockMap` | `0x2C3B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `MFCreateHttpSchemePlugin` | `0x2C3D0` | 43 | UnwindData |  |
| 40 | `MFCreateLPCMByteStreamPlugin` | `0x2C410` | 43 | UnwindData |  |
| 41 | `MFCreateMP3ByteStreamPlugin` | `0x2C450` | 43 | UnwindData |  |
| 42 | `MFCreateMP3MediaSink` | `0x2C490` | 503 | UnwindData |  |
| 43 | `MFCreateMPEG4MediaSink` | `0x2C690` | 529 | UnwindData |  |
| 46 | `MFCreateMuxSink` | `0x2C8B0` | 541 | UnwindData |  |
| 47 | `MFCreateNSCByteStreamPlugin` | `0x2CAE0` | 43 | UnwindData |  |
| 48 | `MFCreateNetSchemePlugin` | `0x2CB20` | 43 | UnwindData |  |
| 53 | `MFCreatePresentationDescriptorFromASFProfile` | `0x2CB60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `MFCreateProxyLocator` | `0x2CB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `MFCreateSAMIByteStreamPlugin` | `0x2CBA0` | 43 | UnwindData |  |
| 60 | `MFCreateSecureHttpSchemePlugin` | `0x2CBE0` | 43 | UnwindData |  |
| 66 | `MFCreateSourceResolver` | `0x2CC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `MFCreateUrlmonSchemePlugin` | `0x2CC40` | 43 | UnwindData |  |
| 84 | `MFGetSupportedMimeTypes` | `0x2CC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `MFGetSupportedSchemes` | `0x2CCA0` | 5,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllGetActivationFactory` | `0x2E210` | 45 | UnwindData |  |
| 77 | `MFCreateVideoRendererActivate` | `0x329D0` | 460 | UnwindData |  |
| 92 | `MFShutdownObject` | `0x32C00` | 252 | UnwindData |  |
| 76 | `MFCreateVideoRenderer` | `0x3B5E0` | 129 | UnwindData |  |
| 89 | `MFRR_CreateActivate` | `0x40D60` | 14,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `MFCreateRemoteDesktopPlugin` | `0x44720` | 574 | UnwindData |  |
| 54 | `MFCreateProtectedEnvironmentAccess` | `0x453E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `MFLoadSignedLibrary` | `0x453F0` | 28 | UnwindData |  |
| 81 | `MFGetLocalId` | `0x45E80` | 325 | UnwindData |  |
| 86 | `MFGetSystemId` | `0x46930` | 112,876 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
