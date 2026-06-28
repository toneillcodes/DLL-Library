# Binary Specification: appbackgroundtask.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\appbackgroundtask.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ce136201f700cb8b348cd4ddad6664b6f8119e07deb42cb2f1f5dea2a81dc04e`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0x1E20` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x1EB0` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1EF0` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x1F70` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1FD0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x2020` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x2240` | 8,720 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
