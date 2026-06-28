# Binary Specification: printfilterpipelineprxy.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\printfilterpipelineprxy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `715c40e9fea9a93f5918b0867d67db428fb7ffe8a58df4541ba1cb0c4fffaaad`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetPrintProcessorCapabilities` | `0x8DF0` | 189 | UnwindData |  |
| 2 | `ClosePrintProcessor` | `0xF070` | 36 | UnwindData |  |
| 3 | `ControlPrintProcessor` | `0xF0A0` | 70 | UnwindData |  |
| 8 | `EnumPrintProcessorDatatypesW` | `0xF0F0` | 535 | UnwindData |  |
| 9 | `OpenPrintProcessor` | `0xF310` | 221 | UnwindData |  |
| 10 | `PrintDocumentOnPrintProcessor` | `0xF400` | 70 | UnwindData |  |
| 4 | `DllCanUnloadNow` | `0xFB80` | 54 | UnwindData |  |
| 5 | `DllGetClassObject` | `0xFBC0` | 146 | UnwindData |  |
| 6 | `DllRegisterServer` | `0xFCB0` | 55 | UnwindData |  |
| 7 | `DllUnregisterServer` | `0xFCF0` | 644 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
