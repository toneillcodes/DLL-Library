# Binary Specification: TpmTasks.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\TpmTasks.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `03ed7808fdb321a7a8b66d38e8f44ac785ac5e47295edb26235b30e05732e96c`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x161F0` | 64,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x161F0` | 64,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x25DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x25E00` | 63,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `TpmTasks_ApplySecureBootUpdateEx` | `0x357D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `TpmTasks_IsRebootRequiredBeforeUpdate` | `0x357E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `TpmTasks_IsSecureBootEnabled` | `0x357F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `TpmTasks_SetUpdateTriggerRegistry` | `0x35800` | 265,059 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
