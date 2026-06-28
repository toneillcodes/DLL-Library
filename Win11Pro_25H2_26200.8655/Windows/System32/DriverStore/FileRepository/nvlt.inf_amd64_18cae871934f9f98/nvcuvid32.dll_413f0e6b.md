# Binary Specification: nvcuvid32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\nvcuvid32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `413f0e6b49e1152cda71454e276a44fb5f1cae1a0b5d739d321a912361cea4bb`
* **Total Exported Functions:** 39

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `NvToolCreateInterface` | `0x79E10` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `NvToolDestroyInterface` | `0x79ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `NvToolGetApiFunctionCount` | `0x79EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `NvToolGetApiID` | `0x79F10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `NvToolGetApiNames` | `0x79F30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `NvToolGetInterface` | `0x79F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `NvToolSetApiID` | `0x79F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `NvToolSetInterface` | `0x79F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `cuvidCreateVideoParser` | `0x79FB0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `cuvidCreateVideoSource` | `0x7A000` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `cuvidCreateVideoSourceW` | `0x7A050` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `cuvidDestroyVideoParser` | `0x7A0A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `cuvidDestroyVideoSource` | `0x7A0F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `cuvidGetSourceAudioFormat` | `0x7A140` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `cuvidGetSourceVideoFormat` | `0x7A190` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `cuvidGetVideoSourceState` | `0x7A1E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `cuvidParseVideoData` | `0x7A230` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `cuvidSetVideoSourceState` | `0x7A280` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `cuvidConvertYUVToRGB` | `0x7A2D0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `cuvidConvertYUVToRGBArray` | `0x7A340` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `cuvidCreateDecoder` | `0x7A390` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `cuvidCtxLock` | `0x7A3E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `cuvidCtxLockCreate` | `0x7A430` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `cuvidCtxLockDestroy` | `0x7A480` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `cuvidCtxUnlock` | `0x7A4D0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `cuvidDecodePicture` | `0x7A520` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `cuvidDestroyDecoder` | `0x7A570` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `cuvidGetDecodeStatus` | `0x7A5C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `cuvidGetDecoderCaps` | `0x7A610` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `cuvidGetVideoFrameSurface` | `0x7A660` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `cuvidMapVideoFrame64` | `0x7A6B0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `cuvidMapVideoFrame` | `0x7A700` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `cuvidPrivateOp` | `0x7A750` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `cuvidReconfigureDecoder` | `0x7A7A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `cuvidUnmapVideoFrame64` | `0x7A7F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `cuvidUnmapVideoFrame` | `0x7A850` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `__std_2U4S4U_X08` | `0x7A8A0` | 351,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateEncoderInterface` | `0xD0600` | 612,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `__std_4U4S4U_X04` | `0x166050` | 856,150 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
