# Binary Specification: nvcuvid64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\nvcuvid64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `43d84281e19d09027e4fe6c3bfaf4d543b77742111dc744e704494394e64c442`
* **Total Exported Functions:** 39

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `NvToolCreateInterface` | `0x76420` | 130 | UnwindData |  |
| 4 | `NvToolDestroyInterface` | `0x764B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `NvToolGetApiFunctionCount` | `0x764D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `NvToolGetApiID` | `0x764E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `NvToolGetApiNames` | `0x764F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `NvToolGetInterface` | `0x76500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `NvToolSetApiID` | `0x76520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `NvToolSetInterface` | `0x76530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `cuvidCreateVideoParser` | `0x76550` | 126 | UnwindData |  |
| 16 | `cuvidCreateVideoSource` | `0x765D0` | 132 | UnwindData |  |
| 17 | `cuvidCreateVideoSourceW` | `0x76660` | 132 | UnwindData |  |
| 24 | `cuvidDestroyVideoParser` | `0x766F0` | 102 | UnwindData |  |
| 25 | `cuvidDestroyVideoSource` | `0x76760` | 102 | UnwindData |  |
| 28 | `cuvidGetSourceAudioFormat` | `0x767D0` | 132 | UnwindData |  |
| 29 | `cuvidGetSourceVideoFormat` | `0x76860` | 132 | UnwindData |  |
| 31 | `cuvidGetVideoSourceState` | `0x768F0` | 102 | UnwindData |  |
| 34 | `cuvidParseVideoData` | `0x76960` | 126 | UnwindData |  |
| 37 | `cuvidSetVideoSourceState` | `0x769E0` | 123 | UnwindData |  |
| 12 | `cuvidConvertYUVToRGB` | `0x76A60` | 190 | UnwindData |  |
| 13 | `cuvidConvertYUVToRGBArray` | `0x76B20` | 170 | UnwindData |  |
| 14 | `cuvidCreateDecoder` | `0x76BD0` | 126 | UnwindData |  |
| 18 | `cuvidCtxLock` | `0x76C50` | 123 | UnwindData |  |
| 19 | `cuvidCtxLockCreate` | `0x76CD0` | 126 | UnwindData |  |
| 20 | `cuvidCtxLockDestroy` | `0x76D50` | 102 | UnwindData |  |
| 21 | `cuvidCtxUnlock` | `0x76DC0` | 123 | UnwindData |  |
| 22 | `cuvidDecodePicture` | `0x76E40` | 126 | UnwindData |  |
| 23 | `cuvidDestroyDecoder` | `0x76EC0` | 102 | UnwindData |  |
| 26 | `cuvidGetDecodeStatus` | `0x76F30` | 129 | UnwindData |  |
| 27 | `cuvidGetDecoderCaps` | `0x76FC0` | 102 | UnwindData |  |
| 30 | `cuvidGetVideoFrameSurface` | `0x77030` | 129 | UnwindData |  |
| 32 | `cuvidMapVideoFrame` | `0x770C0` | 170 | UnwindData |  |
| 33 | `cuvidMapVideoFrame64` | `0x77170` | 170 | UnwindData |  |
| 35 | `cuvidPrivateOp` | `0x77220` | 129 | UnwindData |  |
| 36 | `cuvidReconfigureDecoder` | `0x772B0` | 126 | UnwindData |  |
| 38 | `cuvidUnmapVideoFrame` | `0x77330` | 123 | UnwindData |  |
| 39 | `cuvidUnmapVideoFrame64` | `0x773B0` | 126 | UnwindData |  |
| 11 | `__std_2U4S4U_X08` | `0x77430` | 102 | UnwindData |  |
| 1 | `CreateEncoderInterface` | `0xD7C30` | 124 | UnwindData |  |
| 2 | `__std_4U4S4U_X04` | `0x184060` | 477 | UnwindData |  |
