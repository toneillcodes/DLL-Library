# Binary Specification: colorui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\colorui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f9f55e7419b4380fb15d079bd064f9b93dd2bea33d490d0d5b801c7da00c4f2d`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `LaunchColorCpl` | `0x6650` | 794 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0xBDB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0xBDF0` | 362 | UnwindData |  |
| 4 | `DllMain` | `0xBF60` | 340 | UnwindData |  |
| 5 | `DllRegisterServer` | `0xC0C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0xC100` | 53,356 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
