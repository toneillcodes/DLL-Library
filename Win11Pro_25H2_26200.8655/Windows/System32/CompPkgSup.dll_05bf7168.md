# Binary Specification: CompPkgSup.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\CompPkgSup.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `05bf7168f6fe2ab6ef4406b836e63352f2bf256c10247bb59c5dd17a4047ecd6`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AreDvdCodecsEnabled` | `0x16A80` | 511 | UnwindData |  |
| 2 | `GetDefaultContentDecryptionModuleFactory` | `0x17F20` | 780 | UnwindData |  |
| 3 | `GetMediaComponentPackageInfo` | `0x18240` | 466 | UnwindData |  |
| 4 | `GetMediaComponentPackageInfoInternal` | `0x18420` | 147 | UnwindData |  |
| 5 | `GetMediaExtensionCommunicationFactory` | `0x184C0` | 547 | UnwindData |  |
| 6 | `GetNetworkRequestCount` | `0x18840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetServerForPMP` | `0x18860` | 459 | UnwindData |  |
| 8 | `GetSystemNativeProcessorSignature` | `0x18A40` | 455 | UnwindData |  |
| 9 | `InstantiateComponentFromPackage` | `0x18C10` | 616 | UnwindData |  |
| 10 | `IsMediaBehaviorEnabled` | `0x18E80` | 72 | UnwindData |  |
| 11 | `RegisterMediaExtensionPackage` | `0x18ED0` | 1,309 | UnwindData |  |
| 12 | `RegisterServerForPMP` | `0x19400` | 473 | UnwindData |  |
| 13 | `RequireNetworkDuringMediaTaskCompletion` | `0x195E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `UnregisterServerForPMP` | `0x19600` | 426 | UnwindData |  |
