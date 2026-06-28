# Binary Specification: ApiSetHost.AppExecutionAlias.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ApiSetHost.AppExecutionAlias.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `63fda8da76587d9b735de5f9d6025318ad970ae92db263b25a1ac243c63dfd67`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `DllCanUnloadNow` | `0x33F0` | 81 | UnwindData |  |
| 11 | `DllGetActivationFactory` | `0x3450` | 466 | UnwindData |  |
| 12 | `DllGetClassObject` | `0x3630` | 232 | UnwindData |  |
| 1 | `CheckAppExecutionAliasApplicationType` | `0xCD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CreateAppExecutionAliasEx` | `0xCD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CloseAppExecutionAliasEx` | `0xCD80` | 50 | UnwindData |  |
| 3 | `CompleteAppExecutionAliasProcessCreationEx` | `0xCDC0` | 122 | UnwindData |  |
| 4 | `CompletePackagedProcessCreationEx` | `0xCE40` | 138 | UnwindData |  |
| 5 | `CreateAndPersistAppExecutionAliasEx` | `0xCED0` | 145 | UnwindData |  |
| 6 | `CreateAndPersistAppExecutionAliasEx2` | `0xCF70` | 159 | UnwindData |  |
| 8 | `CreateAppExecutionAliasEx2` | `0xD020` | 37 | UnwindData |  |
| 9 | `CreateAppExecutionAliasEx3` | `0xD050` | 479 | UnwindData |  |
| 13 | `FreeAppExecutionAliasInfoEx` | `0xD240` | 38 | UnwindData |  |
| 14 | `GetAppExecutionAliasApplicationType` | `0xD270` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `GetAppExecutionAliasApplicationUserModelIdEx` | `0xD290` | 33 | UnwindData |  |
| 16 | `GetAppExecutionAliasExecutableEx` | `0xD2C0` | 33 | UnwindData |  |
| 17 | `GetAppExecutionAliasPackageFamilyNameEx` | `0xD2F0` | 132 | UnwindData |  |
| 18 | `GetAppExecutionAliasPackageFullNameEx` | `0xD380` | 86 | UnwindData |  |
| 19 | `GetAppExecutionAliasPath` | `0xD3E0` | 28 | UnwindData |  |
| 20 | `GetAppExecutionAliasPathEx` | `0xD410` | 1,118 | UnwindData |  |
| 21 | `GetHostIdEx` | `0xD880` | 166 | UnwindData |  |
| 22 | `GetHostParametersEx` | `0xD930` | 166 | UnwindData |  |
| 23 | `LoadAppExecutionAliasInfoEx` | `0xD9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `LoadAppExecutionAliasInfoEx2` | `0xDA00` | 99 | UnwindData |  |
| 25 | `OpenAppExecutionAliasForUserEx` | `0xDA70` | 131 | UnwindData |  |
| 26 | `PerformAppxLicenseRundownEx` | `0xDB00` | 253 | UnwindData |  |
| 27 | `PersistAppExecutionAliasToFileEx` | `0xDC10` | 169 | UnwindData |  |
| 28 | `PersistAppExecutionAliasToFileHandleEx` | `0xDCC0` | 26 | UnwindData |  |
