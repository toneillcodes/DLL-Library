# Binary Specification: nvvm32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\nvvm32.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `6c5300f7f205e909ce7fb0b2d609b5643475439a3852b4a96b5695aa3179711c`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `NvCliCompileBitcode` | `0x68340` | 1,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `NvCliCompileLogFree` | `0x68A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `NvCliCompiledProgramFree` | `0x68A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `NvCliCompileProgram` | `0x68A20` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `NvCliCompileSource` | `0x68C10` | 2,816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `NvCliFreeBuffer` | `0x69710` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `NvCliGetBufferData` | `0x69750` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `NvCliLinkBitcode` | `0x69780` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `NvCliQueryBinaryType` | `0x69BA0` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `nvvmCompilerProperty` | `0x69D60` | 169,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `__nvvmHandle` | `0x93380` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `nvvmAddModuleToProgram` | `0x93430` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `nvvmCompileProgram` | `0x93540` | 5,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `nvvmCreateProgram` | `0x94950` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `nvvmDestroyProgram` | `0x94A90` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `nvvmGetCompiledResult` | `0x94BF0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `nvvmGetCompiledResultSize` | `0x94C90` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `nvvmGetErrorString` | `0x94E60` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `nvvmGetProgramLog` | `0x94EE0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `nvvmGetProgramLogSize` | `0x94F80` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `nvvmIRVersion` | `0x95000` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `nvvmLazyAddModuleToProgram` | `0x95090` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `nvvmVerifyProgram` | `0x951A0` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `nvvmVersion` | `0x95550` | 21,822,250 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
