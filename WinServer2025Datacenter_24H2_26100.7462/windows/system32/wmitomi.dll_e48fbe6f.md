# Binary Specification: wmitomi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wmitomi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e48fbe6f008b0cf6772691c4173880c9a52181a16fbd49d766784b8b904ae4d7`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0CCritSec@@QEAA@XZ` | `0x1070` | 31 | UnwindData |  |
| 3 | `??1CCritSec@@QEAA@XZ` | `0x2690` | 23 | UnwindData |  |
| 4 | `??4CAutoSetActivityId@@QEAAAEAV0@AEBV0@@Z` | `0x2720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??4CCritSec@@QEAAAEAV0@AEBV0@@Z` | `0x2740` | 7,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `?SetAdapter@AdapterContextBase@@QEAAJPEAUIUnknown@@@Z` | `0x42D0` | 29 | UnwindData |  |
| 6 | `??4MIServer@@QEAAAEAV0@$$QEAV0@@Z` | `0x7F50` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??4MIServer@@QEAAAEAV0@AEBV0@@Z` | `0x80C0` | 33,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `Adapter_CreateAdapterObject` | `0x10260` | 118 | UnwindData |  |
| 10 | `Adapter_DllCanUnloadNow` | `0x102E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `Adapter_DllGetClassObject` | `0x10320` | 218 | UnwindData |  |
| 12 | `Adapter_RegisterDLL` | `0x10400` | 21,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `Adapter_UnRegisterDLL` | `0x10400` | 21,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0MIServer@@QEAA@XZ` | `0x156D0` | 105 | UnwindData |  |
