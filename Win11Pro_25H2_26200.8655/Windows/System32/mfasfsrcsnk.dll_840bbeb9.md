# Binary Specification: mfasfsrcsnk.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mfasfsrcsnk.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `840bbeb9a465a2c2a64f7ff52e2c3d3aa523c48cb35dc819e132ec79255a1025`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x26EF0` | 18,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2B6D0` | 55,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFCreateASFContentInfo` | `0x38E80` | 84,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MFCreateASFIndexer` | `0x4D8C0` | 158 | UnwindData |  |
| 5 | `MFCreateASFIndexerByteStream` | `0x4D970` | 31,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MFCreateASFMultiplexer` | `0x55310` | 158 | UnwindData |  |
| 11 | `MFCreateASFMutex` | `0x5B8D0` | 19,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MFCreateASFProfile` | `0x60320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MFCreateASFProfileFromPresentationDescriptor` | `0x60330` | 1,183 | UnwindData |  |
| 21 | `MFCreatePresentationDescriptorFromASFProfile` | `0x607E0` | 1,218 | UnwindData |  |
| 15 | `MFCreateASFStreamConfig` | `0x64C00` | 2,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MFCreateASFStreamPrioritization` | `0x65600` | 17,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MFCreateASFSplitter` | `0x69980` | 158 | UnwindData |  |
| 17 | `MFCreateASFStreamSelector` | `0x6E630` | 141 | UnwindData |  |
| 6 | `MFCreateASFMediaSink` | `0x8CAB0` | 26,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MFCreateASFMediaSinkActivate` | `0x93290` | 507 | UnwindData |  |
| 8 | `MFCreateASFMediaSinkActivateFromByteStream` | `0x934A0` | 675 | UnwindData |  |
| 9 | `MFCreateASFMediaSinkActivateNoInit` | `0x93750` | 292 | UnwindData |  |
| 19 | `MFCreateASFStreamingMediaSinkActivate` | `0x93880` | 499 | UnwindData |  |
| 20 | `MFCreateASFStreamingMediaSinkActivateNoInit` | `0x93A80` | 284 | UnwindData |  |
| 18 | `MFCreateASFStreamingMediaSink` | `0x98650` | 718,091 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
