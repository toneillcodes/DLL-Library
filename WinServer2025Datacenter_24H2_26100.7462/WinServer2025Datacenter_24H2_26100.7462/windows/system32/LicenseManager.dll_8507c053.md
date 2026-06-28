# Binary Specification: LicenseManager.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\LicenseManager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8507c05366b921c432368cf376fec8e88d4a080aa374e2f74cb0ed492d9ee8ea`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `ServiceCreateApplicationLicenseManager` | `0x49F70` | 89 | UnwindData |  |
| 10 | `ServiceBeginAcquireLicense` | `0x4AE10` | 93,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `SetServiceStatusHandle` | `0x61D10` | 3,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `ServicePackageRundownNotification` | `0x62C10` | 65,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllCanUnloadNow` | `0x72B90` | 42 | UnwindData |  |
| 6 | `DllGetActivationFactory` | `0x72BC0` | 45 | UnwindData |  |
| 7 | `DllGetClassObject` | `0x72C00` | 69 | UnwindData |  |
| 8 | `LmCreateLicenseManager` | `0x72C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `LmCreateStandardServiceProvider` | `0x72C60` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WnfEventHandlerForDeviceIdChange` | `0x72CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WnfEventHandlerForOfflinePcChange` | `0x72D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WnfEventHandlerForXboxTestNetworkConnectionComplete` | `0x72D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ServiceCleanup` | `0x72D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `ServiceEnsureLicenseForOptionalPackageUsage` | `0x72D30` | 49 | UnwindData |  |
| 14 | `ServiceEnsureLicenseForPackageActivation` | `0x72D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ServiceInitialize` | `0x72D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ServiceOptionalPackageRundownNotification` | `0x72D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ServicePackageSuspendedNotification` | `0x72DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ServicePrecacheLicenseForPackageResume` | `0x72DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `ServiceReset` | `0x72DC0` | 302,019 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
