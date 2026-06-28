# Binary Specification: WSClient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WSClient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `443e5091ddb32da5a5449adb9d3d3e4fdde37e4f38c2d5a3bdd797471c80746e`
* **Total Exported Functions:** 30

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `RefreshBannedAppsList` | `0x17A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WSpTLRW` | `0x17A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `AcquireDeveloperLicense` | `0x17B0` | 66 | UnwindData |  |
| 3 | `CheckDeveloperLicense` | `0x1800` | 59 | UnwindData |  |
| 4 | `GetApplicationURL` | `0x1850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `RemoveDeveloperLicense` | `0x1860` | 50 | UnwindData |  |
| 7 | `WSCallServer` | `0x18A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `WSCheckForConsumable` | `0x18D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `WSGetEvaluatePackageAttempted` | `0x18D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `WSEvaluatePackage` | `0x18F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `WSLicenseClose` | `0x18F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `WSLicenseFilterValidAppCategoryIds` | `0x18F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `WSLicenseInstallLicense` | `0x18F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `WSLicenseRefreshLicense` | `0x18F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `WSLicenseRevokeLicenses` | `0x18F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `WSLicenseUninstallLicense` | `0x18F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `WSNotifyPackageInstalled` | `0x18F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `WSLicenseCleanUpState` | `0x1910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `WSNotifyOOBECompletion` | `0x1910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `WSTriggerOOBEFileValidation` | `0x1910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `WSLicenseGetAllUserTokens` | `0x1920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `WSLicenseGetAllValidAppCategoryIds` | `0x1920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `WSLicenseGetDevInstalledApps` | `0x1920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `WSLicenseGetExtendedUserInfo` | `0x1950` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `WSLicenseGetFeatureLicenseResults` | `0x1980` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `WSLicenseGetLicensesForProducts` | `0x19B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `WSLicenseGetOAuthServiceTicket` | `0x19E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `WSLicenseGetProductLicenseResults` | `0x1A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `WSLicenseOpen` | `0x1A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `WSLicenseRetrieveMachineID` | `0x1A40` | 0 | Indeterminate |  |
