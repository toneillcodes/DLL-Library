# Binary Specification: WsmAgent.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WsmAgent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5a9b7ddd1d4fd360c9eba6e04f2e6a42f08477da4e8621cdc7355a18f25f0c0e`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `MI_Main` | `0x1C20` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllCanUnloadNow` | `0x1CB0` | 47 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x1CF0` | 119 | UnwindData |  |
| 5 | `DllMain` | `0x1D70` | 331 | UnwindData |  |
| 6 | `DllRegisterServer` | `0x1ED0` | 72 | UnwindData |  |
| 7 | `DllUnregisterServer` | `0x1F20` | 65 | UnwindData |  |
| 8 | `GetProviderClassID` | `0x2140` | 2,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??1CWSManCriticalSectionWithConditionVar@@QEAA@XZ` | `0x2AB0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `?GetInitError@CWSManCriticalSection@@QEBAKXZ` | `0x2CD0` | 1,644 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
