# Binary Specification: IMEFILES.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\IME\SHARED\IMEFILES.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f82449bcbab63fa9d18c6a5e9c5421cbb42aac4a8861d8535c7b0a88a1fad6f2`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x12F20` | 68 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x12F70` | 120 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x13020` | 305 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x13160` | 229 | UnwindData |  |
| 5 | `FNRM_CleanupGarbageFiles` | `0x13250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `FNRM_GetActiveFile` | `0x13260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `FNRM_GetRegistrationLevel` | `0x13270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `FNRM_SetActiveFile` | `0x13290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `FNRM_UnregisterAllPerUserFilesExcept` | `0x132B0` | 73,171 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
