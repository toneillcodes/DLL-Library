# Binary Specification: printfilterpipelineprxy.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\printfilterpipelineprxy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `aa1c0674b1208d024c05e781fd92850f24df65275d83478a4d6e9952b2c6f474`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `GetPrintProcessorCapabilities` | `0x6F10` | 189 | UnwindData |  |
| 2 | `ClosePrintProcessor` | `0xC2C0` | 36 | UnwindData |  |
| 3 | `ControlPrintProcessor` | `0xC2F0` | 70 | UnwindData |  |
| 8 | `EnumPrintProcessorDatatypesW` | `0xC340` | 535 | UnwindData |  |
| 9 | `OpenPrintProcessor` | `0xC560` | 221 | UnwindData |  |
| 10 | `PrintDocumentOnPrintProcessor` | `0xC650` | 70 | UnwindData |  |
| 4 | `DllCanUnloadNow` | `0xC8D0` | 54 | UnwindData |  |
| 5 | `DllGetClassObject` | `0xC910` | 146 | UnwindData |  |
| 6 | `DllRegisterServer` | `0xCA00` | 55 | UnwindData |  |
| 7 | `DllUnregisterServer` | `0xCA40` | 564 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
