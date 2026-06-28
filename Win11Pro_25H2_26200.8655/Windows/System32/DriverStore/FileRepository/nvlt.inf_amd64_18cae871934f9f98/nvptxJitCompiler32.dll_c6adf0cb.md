# Binary Specification: nvptxJitCompiler32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\nvptxJitCompiler32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `c6adf0cb423c58ef6d9ca5117007f9ea6c3cc556809ac8d07100972ea4bd033e`
* **Total Exported Functions:** 22

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `__cuda_CallJitEntryPoint` | `0x2B990` | 592,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `nvPTXCompilerCompile` | `0xBC470` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `nvPTXCompilerCreate` | `0xBC7C0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `nvPTXCompilerDestroy` | `0xBC9A0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `nvPTXCompilerGetCompiledProgram` | `0xBCB50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `nvPTXCompilerGetCompiledProgramSize` | `0xBCB90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `nvPTXCompilerGetErrorLog` | `0xBCBC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `nvPTXCompilerGetErrorLogSize` | `0xBCC00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `nvPTXCompilerGetInfoLog` | `0xBCC30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `nvPTXCompilerGetInfoLogSize` | `0xBCC70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `nvPTXCompilerGetVersion` | `0xBCCA0` | 1,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `nvLinkerAddCubin` | `0xBD160` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `nvLinkerAddFatbin` | `0xBD4F0` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `nvLinkerCreate` | `0xBD720` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `nvLinkerDestroy` | `0xBD940` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `nvLinkerFinish` | `0xBDBE0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `nvLinkerGetErrorLog` | `0xBDDB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `nvLinkerGetErrorLogSize` | `0xBDDF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `nvLinkerGetInfoLog` | `0xBDE20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `nvLinkerGetInfoLogSize` | `0xBDE60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `nvLinkerGetLinkedCubin` | `0xBDE90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `nvLinkerGetLinkedCubinSize` | `0xBDEC0` | 10,941,370 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
