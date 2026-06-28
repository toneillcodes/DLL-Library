# Binary Specification: nvptxJitCompiler64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\nvptxJitCompiler64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dffd0186e1936e3ce1ab6dd58fdae9e6ed36e1bfcb3e1c29e93622f116991771`
* **Total Exported Functions:** 22

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `__cuda_CallJitEntryPoint` | `0x3C7A0` | 4,068 | UnwindData |  |
| 13 | `nvPTXCompilerCompile` | `0xDBEE0` | 899 | UnwindData |  |
| 14 | `nvPTXCompilerCreate` | `0xDC270` | 481 | UnwindData |  |
| 15 | `nvPTXCompilerDestroy` | `0xDC460` | 422 | UnwindData |  |
| 16 | `nvPTXCompilerGetCompiledProgram` | `0xDC610` | 78 | UnwindData |  |
| 17 | `nvPTXCompilerGetCompiledProgramSize` | `0xDC660` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `nvPTXCompilerGetErrorLog` | `0xDC690` | 99 | UnwindData |  |
| 19 | `nvPTXCompilerGetErrorLogSize` | `0xDC700` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `nvPTXCompilerGetInfoLog` | `0xDC730` | 99 | UnwindData |  |
| 21 | `nvPTXCompilerGetInfoLogSize` | `0xDC7A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `nvPTXCompilerGetVersion` | `0xDC7D0` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `nvLinkerAddCubin` | `0xDCC50` | 889 | UnwindData |  |
| 3 | `nvLinkerAddFatbin` | `0xDCFD0` | 602 | UnwindData |  |
| 4 | `nvLinkerCreate` | `0xDD230` | 573 | UnwindData |  |
| 5 | `nvLinkerDestroy` | `0xDD470` | 663 | UnwindData |  |
| 6 | `nvLinkerFinish` | `0xDD710` | 468 | UnwindData |  |
| 7 | `nvLinkerGetErrorLog` | `0xDD8F0` | 99 | UnwindData |  |
| 8 | `nvLinkerGetErrorLogSize` | `0xDD960` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `nvLinkerGetInfoLog` | `0xDD990` | 99 | UnwindData |  |
| 10 | `nvLinkerGetInfoLogSize` | `0xDDA00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `nvLinkerGetLinkedCubin` | `0xDDA30` | 58 | UnwindData |  |
| 12 | `nvLinkerGetLinkedCubinSize` | `0xDDA70` | 12,687,532 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
