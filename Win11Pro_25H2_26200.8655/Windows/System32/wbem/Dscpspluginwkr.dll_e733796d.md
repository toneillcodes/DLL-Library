# Binary Specification: Dscpspluginwkr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\Dscpspluginwkr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e733796d44cacfc884748776480c7c061cd4c3ecd33cb1a895c374af5b637583`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CALogFreeMemory` | `0x19E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CALogSetJobDeviceName` | `0x1A00` | 68 | UnwindData |  |
| 3 | `CAWhatIfEnabled` | `0x1A50` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetResourceIdFromContext` | `0x1AF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `LogCADebugMessage` | `0x1B00` | 304 | UnwindData |  |
| 6 | `LogCAProgressMessage` | `0x1C40` | 59 | UnwindData |  |
| 7 | `LogCAVerboseMessage` | `0x1C90` | 315 | UnwindData |  |
| 8 | `LogCAWarningMessage` | `0x1DE0` | 309 | UnwindData |  |
| 9 | `LogCAWhatIfMessage` | `0x1F20` | 332 | UnwindData |  |
| 10 | `LogCAWriteMIError` | `0x2080` | 44 | UnwindData |  |
