# Binary Specification: mfcore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mfcore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f265d4146cbe247c2a0813d49e2d2e9a61d692f19cd2b85c23239ab09ffa3100`
* **Total Exported Functions:** 53

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 48 | `MFGetService` | `0xA6870` | 151 | UnwindData |  |
| 25 | `MFCreateMediaProcessor` | `0xCDCC0` | 674 | UnwindData |  |
| 32 | `MFCreateSampleCopierMFT` | `0xD7950` | 414 | UnwindData |  |
| 19 | `MFCreateDeviceSourceActivate` | `0xFAB30` | 691 | UnwindData |  |
| 14 | `MFCreateAggregateSource` | `0x105EC0` | 1,999 | UnwindData |  |
| 35 | `MFCreateSequencerSource` | `0x1066A0` | 821 | UnwindData |  |
| 46 | `MFEnumDeviceSources` | `0x1123C0` | 499 | UnwindData |  |
| 3 | `CopyPropertyStore` | `0x11FD50` | 443 | UnwindData |  |
| 23 | `MFCreateFileSchemePlugin` | `0x1232A0` | 142 | UnwindData |  |
| 7 | `DllGetClassObject` | `0x1243D0` | 83 | UnwindData |  |
| 41 | `MFCreateTopology` | `0x1461A0` | 98 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x146210` | 61 | UnwindData |  |
| 18 | `MFCreateDeviceSource` | `0x14E350` | 460 | UnwindData |  |
| 42 | `MFCreateTopologyNode` | `0x168360` | 266 | UnwindData |  |
| 43 | `MFCreateTransformWrapper` | `0x16A540` | 77,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllRegisterServer` | `0x17D4F0` | 92 | UnwindData |  |
| 9 | `DllUnregisterServer` | `0x17D560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MFCreatePresentationClock` | `0x17D570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `MFCreatePresentationClockAsyncTimeSource` | `0x17D580` | 5,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllGetActivationFactory` | `0x17EB90` | 45 | UnwindData |  |
| 1 | `AppendPropVariant` | `0x189AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ConvertPropVariant` | `0x189AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateNamedPropertyStore` | `0x189AF0` | 203 | UnwindData |  |
| 10 | `ExtractPropVariant` | `0x189BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `MergePropertyStore` | `0x189BE0` | 127 | UnwindData |  |
| 37 | `MFCreateSimpleTypeHandler` | `0x18AD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MFGetMultipleServiceProviders` | `0x18AD20` | 163 | UnwindData |  |
| 51 | `MFRequireProtectedEnvironment` | `0x18ADD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `MFShutdownObject` | `0x18ADE0` | 252 | UnwindData |  |
| 17 | `MFCreateAudioRendererActivate` | `0x19CDC0` | 454 | UnwindData |  |
| 44 | `MFCreateWMAEncoderActivate` | `0x19CF90` | 1,032 | UnwindData |  |
| 45 | `MFCreateWMVEncoderActivate` | `0x19D3A0` | 1,032 | UnwindData |  |
| 26 | `MFCreateMediaSession` | `0x1E2520` | 49 | UnwindData |  |
| 15 | `MFCreateAppSourceProxy` | `0x1ED4C0` | 531 | UnwindData |  |
| 20 | `MFCreateEncryptedMediaExtensionsStoreActivate` | `0x1ED6E0` | 1,712 | UnwindData |  |
| 27 | `MFCreatePMPHost` | `0x1F8340` | 271 | UnwindData |  |
| 29 | `MFCreatePMPServer` | `0x1F8460` | 443 | UnwindData |  |
| 28 | `MFCreatePMPMediaSession` | `0x2077E0` | 1,922 | UnwindData |  |
| 39 | `MFCreateStandardQualityManager` | `0x233630` | 4,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `MFCreateSequencerSegmentOffset` | `0x2348B0` | 573 | UnwindData |  |
| 50 | `MFReadSequencerSegmentOffset` | `0x234B00` | 522 | UnwindData |  |
| 36 | `MFCreateSequencerSourceRemoteStream` | `0x2414F0` | 133,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `MFCreateSoundEventSchemePlugin` | `0x261DA0` | 127 | UnwindData |  |
| 40 | `MFCreateTopoLoader` | `0x26A060` | 471 | UnwindData |  |
| 49 | `MFGetTopoNodeCurrentType` | `0x2823D0` | 3,127 | UnwindData |  |
| 33 | `MFCreateSampleGrabberSinkActivate` | `0x28D570` | 1,008 | UnwindData |  |
| 11 | `MFCopyMFMetadata` | `0x29FD90` | 764 | UnwindData |  |
| 12 | `MFCopyPropertyStore` | `0x2A00A0` | 760 | UnwindData |  |
| 13 | `MFCopyStreamMetadata` | `0x2A03A0` | 1,279 | UnwindData |  |
| 24 | `MFCreateMFMetadataOnPropertyStore` | `0x2A08B0` | 838 | UnwindData |  |
| 21 | `MFCreateExtendedCameraIntrinsicModel` | `0x2EFE00` | 266 | UnwindData |  |
| 22 | `MFCreateExtendedCameraIntrinsics` | `0x2EFF10` | 197 | UnwindData |  |
| 16 | `MFCreateAudioRenderer` | `0x2F7B20` | 2,466 | UnwindData |  |
