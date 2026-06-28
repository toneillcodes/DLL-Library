# Binary Specification: mfcore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mfcore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `71f8366765edfabb5bdae20abf7efb89c7f06e051c362140620437c217f1be3c`
* **Total Exported Functions:** 53

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 48 | `MFGetService` | `0x9F970` | 151 | UnwindData |  |
| 25 | `MFCreateMediaProcessor` | `0xD34A0` | 674 | UnwindData |  |
| 32 | `MFCreateSampleCopierMFT` | `0xDBB60` | 414 | UnwindData |  |
| 19 | `MFCreateDeviceSourceActivate` | `0xFB990` | 691 | UnwindData |  |
| 14 | `MFCreateAggregateSource` | `0x108280` | 1,999 | UnwindData |  |
| 35 | `MFCreateSequencerSource` | `0x108A60` | 821 | UnwindData |  |
| 46 | `MFEnumDeviceSources` | `0x114830` | 499 | UnwindData |  |
| 3 | `CopyPropertyStore` | `0x123290` | 443 | UnwindData |  |
| 23 | `MFCreateFileSchemePlugin` | `0x1267E0` | 142 | UnwindData |  |
| 7 | `DllGetClassObject` | `0x127910` | 83 | UnwindData |  |
| 41 | `MFCreateTopology` | `0x149430` | 98 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x1494A0` | 61 | UnwindData |  |
| 18 | `MFCreateDeviceSource` | `0x150680` | 460 | UnwindData |  |
| 42 | `MFCreateTopologyNode` | `0x167F70` | 266 | UnwindData |  |
| 43 | `MFCreateTransformWrapper` | `0x16A130` | 77,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllRegisterServer` | `0x17D050` | 92 | UnwindData |  |
| 9 | `DllUnregisterServer` | `0x17D0C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MFCreatePresentationClock` | `0x17D0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `MFCreatePresentationClockAsyncTimeSource` | `0x17D0E0` | 5,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllGetActivationFactory` | `0x17E6F0` | 45 | UnwindData |  |
| 1 | `AppendPropVariant` | `0x18A0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ConvertPropVariant` | `0x18A0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CreateNamedPropertyStore` | `0x18A100` | 203 | UnwindData |  |
| 10 | `ExtractPropVariant` | `0x18A1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `MergePropertyStore` | `0x18A1F0` | 127 | UnwindData |  |
| 37 | `MFCreateSimpleTypeHandler` | `0x18B320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `MFGetMultipleServiceProviders` | `0x18B330` | 163 | UnwindData |  |
| 51 | `MFRequireProtectedEnvironment` | `0x18B3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `MFShutdownObject` | `0x18B3F0` | 252 | UnwindData |  |
| 17 | `MFCreateAudioRendererActivate` | `0x19D100` | 454 | UnwindData |  |
| 44 | `MFCreateWMAEncoderActivate` | `0x19D2D0` | 1,032 | UnwindData |  |
| 45 | `MFCreateWMVEncoderActivate` | `0x19D6E0` | 1,032 | UnwindData |  |
| 26 | `MFCreateMediaSession` | `0x1E1820` | 49 | UnwindData |  |
| 15 | `MFCreateAppSourceProxy` | `0x1EC7C0` | 531 | UnwindData |  |
| 20 | `MFCreateEncryptedMediaExtensionsStoreActivate` | `0x1EC9E0` | 1,712 | UnwindData |  |
| 27 | `MFCreatePMPHost` | `0x1F7640` | 271 | UnwindData |  |
| 29 | `MFCreatePMPServer` | `0x1F7760` | 443 | UnwindData |  |
| 28 | `MFCreatePMPMediaSession` | `0x206AE0` | 1,922 | UnwindData |  |
| 39 | `MFCreateStandardQualityManager` | `0x232930` | 4,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `MFCreateSequencerSegmentOffset` | `0x233BB0` | 573 | UnwindData |  |
| 50 | `MFReadSequencerSegmentOffset` | `0x233E00` | 522 | UnwindData |  |
| 36 | `MFCreateSequencerSourceRemoteStream` | `0x2407F0` | 133,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `MFCreateSoundEventSchemePlugin` | `0x2610A0` | 127 | UnwindData |  |
| 40 | `MFCreateTopoLoader` | `0x269360` | 471 | UnwindData |  |
| 49 | `MFGetTopoNodeCurrentType` | `0x2817F0` | 3,127 | UnwindData |  |
| 33 | `MFCreateSampleGrabberSinkActivate` | `0x28C990` | 1,008 | UnwindData |  |
| 11 | `MFCopyMFMetadata` | `0x29F1B0` | 764 | UnwindData |  |
| 12 | `MFCopyPropertyStore` | `0x29F4C0` | 760 | UnwindData |  |
| 13 | `MFCopyStreamMetadata` | `0x29F7C0` | 1,279 | UnwindData |  |
| 24 | `MFCreateMFMetadataOnPropertyStore` | `0x29FCD0` | 838 | UnwindData |  |
| 21 | `MFCreateExtendedCameraIntrinsicModel` | `0x2EF220` | 266 | UnwindData |  |
| 22 | `MFCreateExtendedCameraIntrinsics` | `0x2EF330` | 197 | UnwindData |  |
| 16 | `MFCreateAudioRenderer` | `0x2F6F40` | 2,466 | UnwindData |  |
