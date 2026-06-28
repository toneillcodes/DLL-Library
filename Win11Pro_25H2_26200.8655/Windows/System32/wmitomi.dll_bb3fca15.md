# Binary Specification: wmitomi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wmitomi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bb3fca15d69ca5fc01f092da28371d209dcd031d25dfb1138f02eb8584fcf0df`
* **Total Exported Functions:** 13

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0CCritSec@@QEAA@XZ` | `0x1300` | 31 | UnwindData |  |
| 3 | `??1CCritSec@@QEAA@XZ` | `0x2910` | 23 | UnwindData |  |
| 4 | `??4CAutoSetActivityId@@QEAAAEAV0@AEBV0@@Z` | `0x29A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??4CCritSec@@QEAAAEAV0@AEBV0@@Z` | `0x29C0` | 7,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `?SetAdapter@AdapterContextBase@@QEAAJPEAUIUnknown@@@Z` | `0x4550` | 29 | UnwindData |  |
| 6 | `??4MIServer@@QEAAAEAV0@$$QEAV0@@Z` | `0x9920` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??4MIServer@@QEAAAEAV0@AEBV0@@Z` | `0x9A90` | 62,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `Adapter_CreateAdapterObject` | `0x18CC0` | 118 | UnwindData |  |
| 10 | `Adapter_DllCanUnloadNow` | `0x18D40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `Adapter_DllGetClassObject` | `0x18D80` | 218 | UnwindData |  |
| 12 | `Adapter_RegisterDLL` | `0x18E60` | 21,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `Adapter_UnRegisterDLL` | `0x18E60` | 21,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0MIServer@@QEAA@XZ` | `0x1E130` | 105 | UnwindData |  |
