# Binary Specification: nvvm64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\nvvm64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `75a758bed6240546e8412dd503dd29f51b7208dbc3b8710789879aba4596cddf`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NvCliCompileBitcode` | `0xA65E0` | 104 | UnwindData |  |
| 2 | `NvCliCompileLogFree` | `0xA7380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `NvCliCompiledProgramFree` | `0xA7380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `NvCliCompileProgram` | `0xA7390` | 724 | UnwindData |  |
| 4 | `NvCliCompileSource` | `0xA7670` | 95 | UnwindData |  |
| 6 | `NvCliFreeBuffer` | `0xA8690` | 10 | UnwindData |  |
| 7 | `NvCliGetBufferData` | `0xA86E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `NvCliLinkBitcode` | `0xA8700` | 144 | UnwindData |  |
| 9 | `NvCliQueryBinaryType` | `0xA8CD0` | 113 | UnwindData |  |
| 13 | `nvvmCompilerProperty` | `0xA8EF0` | 194,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `__nvvmHandle` | `0xD86D0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `nvvmAddModuleToProgram` | `0xD87A0` | 354 | UnwindData |  |
| 12 | `nvvmCompileProgram` | `0xD8910` | 6,686 | UnwindData |  |
| 14 | `nvvmCreateProgram` | `0xDA330` | 13 | UnwindData |  |
| 15 | `nvvmDestroyProgram` | `0xDA480` | 13 | UnwindData |  |
| 16 | `nvvmGetCompiledResult` | `0xDA640` | 13 | UnwindData |  |
| 17 | `nvvmGetCompiledResultSize` | `0xDA720` | 191 | UnwindData |  |
| 18 | `nvvmGetErrorString` | `0xDA9B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `nvvmGetProgramLog` | `0xDAA50` | 13 | UnwindData |  |
| 20 | `nvvmGetProgramLogSize` | `0xDAB30` | 172 | UnwindData |  |
| 21 | `nvvmIRVersion` | `0xDABE0` | 203 | UnwindData |  |
| 22 | `nvvmLazyAddModuleToProgram` | `0xDACB0` | 361 | UnwindData |  |
| 23 | `nvvmVerifyProgram` | `0xDAE20` | 47 | UnwindData |  |
| 24 | `nvvmVersion` | `0xDB2D0` | 167 | UnwindData |  |
