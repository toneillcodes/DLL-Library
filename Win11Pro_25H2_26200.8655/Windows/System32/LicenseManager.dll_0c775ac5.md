# Binary Specification: LicenseManager.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\LicenseManager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0c775ac5f1bb488746daddac0a7eb96014863ca96847b78407ee27d475d677cf`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `ServiceCreateApplicationLicenseManager` | `0x4A050` | 89 | UnwindData |  |
| 10 | `ServiceBeginAcquireLicense` | `0x4AE60` | 93,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `SetServiceStatusHandle` | `0x61B00` | 4,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `ServicePackageRundownNotification` | `0x62AB0` | 65,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllCanUnloadNow` | `0x72B00` | 42 | UnwindData |  |
| 6 | `DllGetActivationFactory` | `0x72B30` | 45 | UnwindData |  |
| 7 | `DllGetClassObject` | `0x72B70` | 69 | UnwindData |  |
| 8 | `LmCreateLicenseManager` | `0x72BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `LmCreateStandardServiceProvider` | `0x72BD0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WnfEventHandlerForDeviceIdChange` | `0x72C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WnfEventHandlerForOfflinePcChange` | `0x72C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WnfEventHandlerForXboxTestNetworkConnectionComplete` | `0x72C80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ServiceCleanup` | `0x72C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `ServiceEnsureLicenseForOptionalPackageUsage` | `0x72CA0` | 49 | UnwindData |  |
| 14 | `ServiceEnsureLicenseForPackageActivation` | `0x72CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `ServiceInitialize` | `0x72CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ServiceOptionalPackageRundownNotification` | `0x72D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `ServicePackageSuspendedNotification` | `0x72D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ServicePrecacheLicenseForPackageResume` | `0x72D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `ServiceReset` | `0x72D30` | 301,731 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
