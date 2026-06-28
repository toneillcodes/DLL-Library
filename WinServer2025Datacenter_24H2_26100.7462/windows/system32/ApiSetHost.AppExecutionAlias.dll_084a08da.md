# Binary Specification: ApiSetHost.AppExecutionAlias.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ApiSetHost.AppExecutionAlias.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `084a08dafb484a3226f3cffda627609ba4ee2e884505667ab1466d3295c358af`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `DllCanUnloadNow` | `0x33E0` | 81 | UnwindData |  |
| 11 | `DllGetActivationFactory` | `0x3440` | 466 | UnwindData |  |
| 12 | `DllGetClassObject` | `0x3620` | 232 | UnwindData |  |
| 1 | `CheckAppExecutionAliasApplicationType` | `0xDA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CreateAppExecutionAliasEx` | `0xDA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CloseAppExecutionAliasEx` | `0xDA10` | 50 | UnwindData |  |
| 3 | `CompleteAppExecutionAliasProcessCreationEx` | `0xDA50` | 122 | UnwindData |  |
| 4 | `CompletePackagedProcessCreationEx` | `0xDAD0` | 138 | UnwindData |  |
| 5 | `CreateAndPersistAppExecutionAliasEx` | `0xDB60` | 145 | UnwindData |  |
| 6 | `CreateAndPersistAppExecutionAliasEx2` | `0xDC00` | 159 | UnwindData |  |
| 8 | `CreateAppExecutionAliasEx2` | `0xDCB0` | 37 | UnwindData |  |
| 9 | `CreateAppExecutionAliasEx3` | `0xDCE0` | 479 | UnwindData |  |
| 13 | `FreeAppExecutionAliasInfoEx` | `0xDED0` | 38 | UnwindData |  |
| 14 | `GetAppExecutionAliasApplicationType` | `0xDF00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `GetAppExecutionAliasApplicationUserModelIdEx` | `0xDF20` | 33 | UnwindData |  |
| 16 | `GetAppExecutionAliasExecutableEx` | `0xDF50` | 33 | UnwindData |  |
| 17 | `GetAppExecutionAliasPackageFamilyNameEx` | `0xDF80` | 132 | UnwindData |  |
| 18 | `GetAppExecutionAliasPackageFullNameEx` | `0xE010` | 86 | UnwindData |  |
| 19 | `GetAppExecutionAliasPath` | `0xE070` | 28 | UnwindData |  |
| 20 | `GetAppExecutionAliasPathEx` | `0xE0A0` | 822 | UnwindData |  |
| 21 | `GetHostIdEx` | `0xE3E0` | 166 | UnwindData |  |
| 22 | `GetHostParametersEx` | `0xE490` | 166 | UnwindData |  |
| 23 | `LoadAppExecutionAliasInfoEx` | `0xE540` | 128 | UnwindData |  |
| 24 | `LoadAppExecutionAliasInfoEx2` | `0xE5D0` | 99 | UnwindData |  |
| 25 | `OpenAppExecutionAliasForUserEx` | `0xE640` | 131 | UnwindData |  |
| 26 | `PerformAppxLicenseRundownEx` | `0xE6D0` | 253 | UnwindData |  |
| 27 | `PersistAppExecutionAliasToFileEx` | `0xE7E0` | 169 | UnwindData |  |
| 28 | `PersistAppExecutionAliasToFileHandleEx` | `0xE890` | 26 | UnwindData |  |
