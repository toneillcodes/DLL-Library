# Binary Specification: IMEFILES.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\IME\SHARED\IMEFILES.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5c8095f57f034d1c7ad9a40f34f62ddb5ca2d272e4eb5a0e59a38ce98c1bf5e6`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x12FF0` | 68 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x13040` | 120 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x130F0` | 305 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x13230` | 229 | UnwindData |  |
| 5 | `FNRM_CleanupGarbageFiles` | `0x13320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `FNRM_GetActiveFile` | `0x13330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `FNRM_GetRegistrationLevel` | `0x13340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `FNRM_SetActiveFile` | `0x13360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `FNRM_UnregisterAllPerUserFilesExcept` | `0x13380` | 73,235 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
