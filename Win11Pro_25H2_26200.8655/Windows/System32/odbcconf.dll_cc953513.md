# Binary Specification: odbcconf.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\odbcconf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cc9535133eb3cf912aa8dea360e48d2e9eb93c869484d6f6620f2db72c78c18d`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `ExecuteAction` | `0x2D90` | 70 | UnwindData |  |
| 11 | `SetActionEnum` | `0x3430` | 31 | UnwindData |  |
| 12 | `SetActionName` | `0x34F0` | 49 | UnwindData |  |
| 7 | `SetActionLogFile` | `0x35C0` | 65 | UnwindData |  |
| 9 | `SetActionLogMode` | `0x3610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SetActionLogModeSz` | `0x3620` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SetSilent` | `0x3680` | 2,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `AppRegEnum` | `0x3E90` | 29 | UnwindData |  |
| 14 | `CloseAppRegEnum` | `0x3EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `RefreshAppRegEnum` | `0x3EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `RegisterApplication` | `0x3EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `UnregisterApplication` | `0x3EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `DllRegisterServer` | `0x3ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `DllUnregisterServer` | `0x3ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `OpenAppRegEnum` | `0x3ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `RunDLL32_RegisterApplication` | `0x3ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `RunDLL32_UnregisterApplication` | `0x3ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `QueryApplication` | `0x3EE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `DllCanUnloadNow` | `0x3F40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `DllGetClassObject` | `0x3F70` | 55 | UnwindData |  |
