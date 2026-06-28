# Binary Specification: cudnn_infer64_7.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\cudnn_infer64_7.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a07edbeeb2a4942fa8f66111e446684d9145030be76b0a8ce56142d892c2b6f9`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `cudnnGetConvolution2dDescriptor` | `0x1000` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `cudnnGetConvolution2dForwardOutputDim` | `0x1060` | 146 | UnwindData |  |
| 3 | `cudnnGetPooling2dDescriptor` | `0x1100` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `cudnnGetPooling2dForwardOutputDim` | `0x1160` | 86 | UnwindData |  |
| 5 | `cudnnSetConvolution2dDescriptor` | `0x1320` | 210 | UnwindData |  |
| 6 | `cudnnSetPooling2dDescriptor` | `0x1400` | 179 | UnwindData |  |
| 14 | `cudnnCreateActivationDescriptor` | `0x1620` | 76 | UnwindData |  |
| 15 | `cudnnCreateConvolutionDescriptor` | `0x1670` | 37 | UnwindData |  |
| 17 | `cudnnCreateOpTensorDescriptor` | `0x16E0` | 76 | UnwindData |  |
| 18 | `cudnnCreatePoolingDescriptor` | `0x1730` | 76 | UnwindData |  |
| 21 | `cudnnDestroyActivationDescriptor` | `0x1780` | 25 | UnwindData |  |
| 22 | `cudnnDestroyConvolutionDescriptor` | `0x1780` | 25 | UnwindData |  |
| 23 | `cudnnDestroyFilterDescriptor` | `0x1780` | 25 | UnwindData |  |
| 24 | `cudnnDestroyOpTensorDescriptor` | `0x1780` | 25 | UnwindData |  |
| 25 | `cudnnDestroyPoolingDescriptor` | `0x1780` | 25 | UnwindData |  |
| 26 | `cudnnDestroyTensorDescriptor` | `0x1780` | 25 | UnwindData |  |
| 27 | `cudnnGetActivationDescriptor` | `0x17A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `cudnnGetBackdoor` | `0x17C0` | 38 | UnwindData |  |
| 37 | `cudnnGetConvolutionGroupCount` | `0x17F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `cudnnGetConvolutionMathType` | `0x1810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `cudnnGetConvolutionNdDescriptor` | `0x1830` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `cudnnGetConvolutionNdForwardOutputDim` | `0x18C0` | 90 | UnwindData |  |
| 41 | `cudnnGetCudartVersion` | `0x1A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `cudnnGetErrorString` | `0x1A10` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `cudnnGetOpTensorDescriptor` | `0x1AE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `cudnnGetPoolingNdDescriptor` | `0x1B00` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `cudnnGetPoolingNdForwardOutputDim` | `0x1B90` | 53 | UnwindData |  |
| 47 | `cudnnGetProperty` | `0x1C40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `cudnnGetVersion` | `0x1C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `cudnnQueryRuntimeError` | `0x1C90` | 205 | UnwindData |  |
| 57 | `cudnnSetActivationDescriptor` | `0x1D60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `cudnnSetBackdoor` | `0x1D90` | 72 | UnwindData |  |
| 59 | `cudnnSetBackdoorEx` | `0x1DE0` | 38 | UnwindData |  |
| 60 | `cudnnSetConvolutionGroupCount` | `0x1E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `cudnnSetConvolutionMathType` | `0x1E30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `cudnnSetConvolutionNdDescriptor` | `0x1E60` | 183 | UnwindData |  |
| 64 | `cudnnSetOpTensorDescriptor` | `0x1F20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `cudnnSetPoolingNdDescriptor` | `0x1F50` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `cudnnCreate` | `0x21B0` | 39 | UnwindData |  |
| 20 | `cudnnDestroy` | `0x2660` | 27 | UnwindData |  |
| 48 | `cudnnGetStream` | `0x2780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `cudnnSetStream` | `0x27A0` | 93 | UnwindData |  |
| 16 | `cudnnCreateFilterDescriptor` | `0x2990` | 44 | UnwindData |  |
| 19 | `cudnnCreateTensorDescriptor` | `0x2A00` | 32 | UnwindData |  |
| 43 | `cudnnGetFilterNdDescriptor` | `0x2A90` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `cudnnGetTensorNdDescriptor` | `0x2B20` | 62 | UnwindData |  |
| 50 | `cudnnGetTensorSizeInBytes` | `0x2BE0` | 53 | UnwindData |  |
| 63 | `cudnnSetFilterNdDescriptor` | `0x2C20` | 76 | UnwindData |  |
| 68 | `cudnnSetTensorNdDescriptor` | `0x2D00` | 22 | UnwindData |  |
| 69 | `cudnnSetTensorNdDescriptorEx` | `0x2D20` | 62 | UnwindData |  |
| 9 | `cudnnAddTensor` | `0x3170` | 72 | UnwindData |  |
| 56 | `cudnnScaleTensor` | `0x33C0` | 237 | UnwindData |  |
| 67 | `cudnnSetTensor` | `0x34B0` | 227 | UnwindData |  |
| 71 | `cudnnTransformTensor` | `0x35A0` | 76 | UnwindData |  |
| 53 | `cudnnOpTensor` | `0x3930` | 106 | UnwindData |  |
| 10 | `cudnnConvolutionBackwardData` | `0x6F10` | 159 | UnwindData |  |
| 11 | `cudnnConvolutionBiasActivationForward` | `0x75B0` | 79 | UnwindData |  |
| 12 | `cudnnConvolutionForward` | `0x77D0` | 168 | UnwindData |  |
| 29 | `cudnnGetConvolutionBackwardDataAlgorithm` | `0x7880` | 79 | UnwindData |  |
| 30 | `cudnnGetConvolutionBackwardDataAlgorithmMaxCount` | `0x7BC0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `cudnnGetConvolutionBackwardDataAlgorithm_v7` | `0x7C30` | 221 | UnwindData |  |
| 32 | `cudnnGetConvolutionBackwardDataWorkspaceSize` | `0x7D10` | 22 | UnwindData |  |
| 33 | `cudnnGetConvolutionForwardAlgorithm` | `0x7D30` | 150 | UnwindData |  |
| 34 | `cudnnGetConvolutionForwardAlgorithmMaxCount` | `0x80A0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `cudnnGetConvolutionForwardAlgorithm_v7` | `0x8120` | 225 | UnwindData |  |
| 36 | `cudnnGetConvolutionForwardWorkspaceSize` | `0x8210` | 22 | UnwindData |  |
| 70 | `cudnnSoftmaxForward` | `0x320260` | 77 | UnwindData |  |
| 54 | `cudnnPoolingForward` | `0x32A3E0` | 77 | UnwindData |  |
| 8 | `cudnnActivationForward` | `0x335070` | 197 | UnwindData |  |
| 52 | `cudnnIm2Col` | `0x48D450` | 339 | UnwindData |  |
| 7 | `NvOptimusEnablementCuda` | `0x798880` | 0 | Indeterminate |  |
