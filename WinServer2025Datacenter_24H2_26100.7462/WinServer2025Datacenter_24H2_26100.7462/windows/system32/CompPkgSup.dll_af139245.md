# Binary Specification: CompPkgSup.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\CompPkgSup.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `af139245ca8e987d5e11d9f5b144c1fdd5fb5bcf7adc00523ae9b8a114915af8`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AreDvdCodecsEnabled` | `0x1A260` | 511 | UnwindData |  |
| 2 | `GetDefaultContentDecryptionModuleFactory` | `0x1B700` | 780 | UnwindData |  |
| 3 | `GetMediaComponentPackageInfo` | `0x1BA20` | 466 | UnwindData |  |
| 4 | `GetMediaComponentPackageInfoInternal` | `0x1BC00` | 147 | UnwindData |  |
| 5 | `GetMediaExtensionCommunicationFactory` | `0x1BCA0` | 533 | UnwindData |  |
| 6 | `GetNetworkRequestCount` | `0x1C010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetServerForPMP` | `0x1C030` | 459 | UnwindData |  |
| 8 | `GetSystemNativeProcessorSignature` | `0x1C210` | 455 | UnwindData |  |
| 9 | `InstantiateComponentFromPackage` | `0x1C3E0` | 616 | UnwindData |  |
| 10 | `IsMediaBehaviorEnabled` | `0x1C650` | 72 | UnwindData |  |
| 11 | `RegisterMediaExtensionPackage` | `0x1C6A0` | 1,309 | UnwindData |  |
| 12 | `RegisterServerForPMP` | `0x1CBD0` | 473 | UnwindData |  |
| 13 | `RequireNetworkDuringMediaTaskCompletion` | `0x1CDB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `UnregisterServerForPMP` | `0x1CDD0` | 426 | UnwindData |  |
