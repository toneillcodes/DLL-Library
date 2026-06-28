# Binary Specification: avifil32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\avifil32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4944d79009a8fbe4e737655fee92ae61e3564b1ee3ca40037d76be6a335bcedf`
* **Total Exported Functions:** 76

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 27 | `AVISave` | `0x2140` | 512 | UnwindData |  |
| 28 | `AVISaveA` | `0x2140` | 512 | UnwindData |  |
| 31 | `AVISaveV` | `0x2350` | 192 | UnwindData |  |
| 32 | `AVISaveVA` | `0x2350` | 192 | UnwindData |  |
| 33 | `AVISaveVW` | `0x2420` | 3,648 | UnwindData |  |
| 34 | `AVISaveW` | `0x3270` | 512 | UnwindData |  |
| 29 | `AVISaveOptions` | `0x38F0` | 341 | UnwindData |  |
| 30 | `AVISaveOptionsFree` | `0x3A50` | 219 | UnwindData |  |
| 4 | `AVIClearClipboard` | `0x5010` | 242 | UnwindData |  |
| 22 | `AVIGetFromClipboard` | `0x5920` | 508 | UnwindData |  |
| 26 | `AVIPutFileOnClipboard` | `0x5B30` | 121 | UnwindData |  |
| 62 | `DllGetClassObject` | `0x7580` | 365 | UnwindData |  |
| 1 | `AVIBuildFilter` | `0x7B70` | 287 | UnwindData |  |
| 2 | `AVIBuildFilterA` | `0x7B70` | 287 | UnwindData |  |
| 3 | `AVIBuildFilterW` | `0x7CA0` | 1,692 | UnwindData |  |
| 5 | `AVIFileAddRef` | `0x8350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `AVIStreamAddRef` | `0x8350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `AVIFileCreateStreamA` | `0x8370` | 205 | UnwindData |  |
| 6 | `AVIFileCreateStream` | `0x8450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `AVIFileCreateStreamW` | `0x8450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `AVIFileEndRecord` | `0x8470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `AVIFileExit` | `0x8490` | 44 | UnwindData |  |
| 11 | `AVIFileGetStream` | `0x84D0` | 22 | UnwindData |  |
| 12 | `AVIFileInfo` | `0x84F0` | 247 | UnwindData |  |
| 13 | `AVIFileInfoA` | `0x84F0` | 247 | UnwindData |  |
| 14 | `AVIFileInfoW` | `0x85F0` | 73 | UnwindData |  |
| 15 | `AVIFileInit` | `0x8640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `AVIFileOpen` | `0x8660` | 186 | UnwindData |  |
| 17 | `AVIFileOpenA` | `0x8660` | 186 | UnwindData |  |
| 18 | `AVIFileOpenW` | `0x8720` | 474 | UnwindData |  |
| 19 | `AVIFileReadData` | `0x8900` | 22 | UnwindData |  |
| 55 | `AVIStreamSetFormat` | `0x8900` | 22 | UnwindData |  |
| 20 | `AVIFileRelease` | `0x8920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `AVIStreamRelease` | `0x8920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `AVIFileWriteData` | `0x8940` | 22 | UnwindData |  |
| 52 | `AVIStreamReadFormat` | `0x8940` | 22 | UnwindData |  |
| 23 | `AVIMakeCompressedStream` | `0x8960` | 370 | UnwindData |  |
| 36 | `AVIStreamBeginStreaming` | `0x8AE0` | 136 | UnwindData |  |
| 37 | `AVIStreamCreate` | `0x8B70` | 173 | UnwindData |  |
| 38 | `AVIStreamEndStreaming` | `0x8C30` | 116 | UnwindData |  |
| 39 | `AVIStreamFindSample` | `0x8CB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `AVIStreamInfo` | `0x8CE0` | 310 | UnwindData |  |
| 44 | `AVIStreamInfoA` | `0x8CE0` | 310 | UnwindData |  |
| 45 | `AVIStreamInfoW` | `0x8E20` | 73 | UnwindData |  |
| 46 | `AVIStreamLength` | `0x8E70` | 116 | UnwindData |  |
| 47 | `AVIStreamOpenFromFile` | `0x8EF0` | 141 | UnwindData |  |
| 48 | `AVIStreamOpenFromFileA` | `0x8EF0` | 141 | UnwindData |  |
| 49 | `AVIStreamOpenFromFileW` | `0x8F90` | 141 | UnwindData |  |
| 50 | `AVIStreamRead` | `0x9030` | 55 | UnwindData |  |
| 51 | `AVIStreamReadData` | `0x9070` | 22 | UnwindData |  |
| 54 | `AVIStreamSampleToTime` | `0x9090` | 290 | UnwindData |  |
| 56 | `AVIStreamStart` | `0x91C0` | 104 | UnwindData |  |
| 57 | `AVIStreamTimeToSample` | `0x9230` | 295 | UnwindData |  |
| 58 | `AVIStreamWrite` | `0x9360` | 80 | UnwindData |  |
| 59 | `AVIStreamWriteData` | `0x93C0` | 22 | UnwindData |  |
| 61 | `DllCanUnloadNow` | `0x9C80` | 32,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `AVIMakeFileFromStreams` | `0x11D00` | 115 | UnwindData |  |
| 25 | `AVIMakeStreamFromClipboard` | `0x121A0` | 329 | UnwindData |  |
| 60 | `CreateEditableStream` | `0x145B0` | 190 | UnwindData |  |
| 63 | `EditStreamClone` | `0x14680` | 126 | UnwindData |  |
| 64 | `EditStreamCopy` | `0x14710` | 142 | UnwindData |  |
| 65 | `EditStreamCut` | `0x147B0` | 142 | UnwindData |  |
| 66 | `EditStreamPaste` | `0x14850` | 168 | UnwindData |  |
| 67 | `EditStreamSetInfo` | `0x14900` | 297 | UnwindData |  |
| 68 | `EditStreamSetInfoA` | `0x14900` | 297 | UnwindData |  |
| 69 | `EditStreamSetInfoW` | `0x14A30` | 141 | UnwindData |  |
| 70 | `EditStreamSetName` | `0x14AD0` | 230 | UnwindData |  |
| 71 | `EditStreamSetNameA` | `0x14AD0` | 230 | UnwindData |  |
| 72 | `EditStreamSetNameW` | `0x14BC0` | 302 | UnwindData |  |
| 40 | `AVIStreamGetFrame` | `0x15890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `AVIStreamGetFrameClose` | `0x158B0` | 29 | UnwindData |  |
| 42 | `AVIStreamGetFrameOpen` | `0x158E0` | 280 | UnwindData |  |
| 74 | `IID_IAVIFile` | `0x1B370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `IID_IAVIStream` | `0x1B380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `IID_IGetFrame` | `0x1B3A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `IID_IAVIEditStream` | `0x1B3C0` | 0 | Indeterminate |  |
