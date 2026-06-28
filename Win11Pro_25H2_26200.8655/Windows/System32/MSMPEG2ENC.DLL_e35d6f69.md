# Binary Specification: MSMPEG2ENC.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\MSMPEG2ENC.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e35d6f695314bea0b5c85cd10dd2e8b21d050396d26942a393f99a0f377304e9`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x1E1B0` | 66 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1E200` | 49 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x1E550` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1E590` | 274 | UnwindData |  |
