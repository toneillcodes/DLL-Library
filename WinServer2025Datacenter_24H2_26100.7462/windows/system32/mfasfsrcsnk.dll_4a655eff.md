# Binary Specification: mfasfsrcsnk.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mfasfsrcsnk.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4a655eff04794bc887866e5e72c36076b0f8cf6ffe5c1920fe4affa2a2d16e9c`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x27010` | 18,400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2B7F0` | 55,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MFCreateASFContentInfo` | `0x38FA0` | 84,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MFCreateASFIndexer` | `0x4D9E0` | 158 | UnwindData |  |
| 5 | `MFCreateASFIndexerByteStream` | `0x4DA90` | 31,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `MFCreateASFMultiplexer` | `0x55430` | 158 | UnwindData |  |
| 11 | `MFCreateASFMutex` | `0x5B9F0` | 19,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `MFCreateASFProfile` | `0x60440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `MFCreateASFProfileFromPresentationDescriptor` | `0x60450` | 1,183 | UnwindData |  |
| 21 | `MFCreatePresentationDescriptorFromASFProfile` | `0x60900` | 1,218 | UnwindData |  |
| 15 | `MFCreateASFStreamConfig` | `0x64D20` | 2,560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `MFCreateASFStreamPrioritization` | `0x65720` | 17,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MFCreateASFSplitter` | `0x69AA0` | 158 | UnwindData |  |
| 17 | `MFCreateASFStreamSelector` | `0x6E750` | 141 | UnwindData |  |
| 6 | `MFCreateASFMediaSink` | `0x8CBB0` | 26,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MFCreateASFMediaSinkActivate` | `0x93390` | 507 | UnwindData |  |
| 8 | `MFCreateASFMediaSinkActivateFromByteStream` | `0x935A0` | 675 | UnwindData |  |
| 9 | `MFCreateASFMediaSinkActivateNoInit` | `0x93850` | 292 | UnwindData |  |
| 19 | `MFCreateASFStreamingMediaSinkActivate` | `0x93980` | 499 | UnwindData |  |
| 20 | `MFCreateASFStreamingMediaSinkActivateNoInit` | `0x93B80` | 284 | UnwindData |  |
| 18 | `MFCreateASFStreamingMediaSink` | `0x98750` | 727,163 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
